# -*- coding: utf-8 -*-
"""
webdav_mount.py - Ổ đĩa ảo mã hóa AES-256-GCM KHÔNG CẦN QUYỀN ADMIN.
Tận dụng dịch vụ WebClient có sẵn của Windows để gắn ổ đĩa (VD: Z:\)
đọc/ghi trực tiếp qua RAM tới FolderBlobStore (0% file rõ chạm ổ cứng).
"""

from __future__ import annotations

import io
import os
import secrets
import socket
import string
import subprocess
import threading
import time
from typing import Optional

from wsgidav.dav_error import DAVError, HTTP_FORBIDDEN, HTTP_NOT_FOUND
from wsgidav.dav_provider import DAVCollection, DAVNonCollection, DAVProvider
from wsgidav.wsgidav_app import WsgiDAVApp

from crypto_engine import FolderBlobStore, MODE_WEBDAV, VaultEngine


def _find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


def _find_free_drive_letter() -> Optional[str]:
    """Tìm ký tự ổ đĩa trống (ưu tiên từ Z: ngược về M:)."""
    for letter in reversed(string.ascii_uppercase[12:]):  # Z -> M
        drive = f"{letter}:\\"
        if not os.path.exists(drive):
            return f"{letter}:"
    return None


def _run_hidden(cmd: list[str], timeout: int = 15) -> subprocess.CompletedProcess:
    creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0) if os.name == "nt" else 0
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        creationflags=creationflags,
        timeout=timeout,
    )


# ---------------------------------------------------------------------------
# WsgiDAV Custom Provider đọc/ghi trực tiếp AES-256-GCM trên RAM
# ---------------------------------------------------------------------------

class _RAMWriteBuffer(io.BytesIO):
    """Buffer ghi hoàn toàn trong RAM, không bao giờ tạo file tạm trên ổ đĩa."""

    def __init__(self, on_close_cb):
        super().__init__()
        self._on_close_cb = on_close_cb
        self._finalized = False

    def close(self) -> None:
        if not self._finalized:
            self._finalized = True
            self.seek(0)
            try:
                self._on_close_cb(self)
            finally:
                super().close()


class VaultFileResource(DAVNonCollection):
    def __init__(self, path: str, environ: dict, store: FolderBlobStore, rel_path: str):
        super().__init__(path, environ)
        self._store = store
        self._rel_path = rel_path

    def _info(self) -> dict:
        return self._store.get_file_info(self._rel_path) or {"size": 0, "mtime": time.time(), "blob": ""}

    def get_content_length(self) -> int:
        return int(self._info().get("size", 0))

    def get_content_type(self) -> str:
        import mimetypes
        ctype, _ = mimetypes.guess_type(self._rel_path)
        return ctype or "application/octet-stream"

    def get_last_modified(self) -> float:
        return float(self._info().get("mtime", time.time()))

    def get_creation_date(self) -> float:
        return self.get_last_modified()

    def get_etag(self) -> str:
        info = self._info()
        return f"{info.get('blob', '0')}-{info.get('size', 0)}-{int(info.get('mtime', 0))}"

    def support_etag(self) -> bool:
        return True

    def support_ranges(self) -> bool:
        return True

    def get_content(self):
        return self._store.open_reader(self._rel_path)

    def begin_write(self, *, content_type=None):
        def _commit(buf: io.BytesIO):
            buf.seek(0)
            self._store.write_file_from_stream(self._rel_path, buf)

        return _RAMWriteBuffer(_commit)

    def end_write(self, *, with_errors: bool):
        pass

    def delete(self):
        self._store.delete_path(self._rel_path)

    def handle_move(self, dest_path: str) -> bool:
        dest_folder, dest_rel = self.provider.split_vault_path(dest_path)
        src_folder, _ = self.provider.split_vault_path(self.path)
        if dest_folder and dest_folder == src_folder and dest_rel:
            self._store.move_path(self._rel_path, dest_rel)
            return True
        return False

    def handle_copy(self, dest_path: str, *, depth_infinity: bool) -> bool:
        dest_folder, dest_rel = self.provider.split_vault_path(dest_path)
        src_folder, _ = self.provider.split_vault_path(self.path)
        if dest_folder and dest_folder == src_folder and dest_rel:
            self._store.copy_path(self._rel_path, dest_rel)
            return True
        return False


class VaultFolderCollection(DAVCollection):
    def __init__(self, path: str, environ: dict, store: FolderBlobStore, rel_path: str):
        super().__init__(path, environ)
        self._store = store
        self._rel_path = rel_path

    def get_member_names(self) -> list[str]:
        dirs, files = self._store.list_children(self._rel_path)
        return dirs + files

    def get_member(self, name: str):
        child_rel = f"{self._rel_path}/{name}" if self._rel_path else name
        child_dav_path = f"{self.path.rstrip('/')}/{name}"
        if self._store.is_dir(child_rel):
            return VaultFolderCollection(child_dav_path, self.environ, self._store, child_rel)
        if self._store.is_file(child_rel):
            return VaultFileResource(child_dav_path, self.environ, self._store, child_rel)
        return None

    def create_empty_resource(self, name: str):
        child_rel = f"{self._rel_path}/{name}" if self._rel_path else name
        child_dav_path = f"{self.path.rstrip('/')}/{name}"
        self._store.write_file_from_stream(child_rel, io.BytesIO(b""))
        return VaultFileResource(child_dav_path, self.environ, self._store, child_rel)

    def create_collection(self, name: str):
        child_rel = f"{self._rel_path}/{name}" if self._rel_path else name
        child_dav_path = f"{self.path.rstrip('/')}/{name}"
        self._store.mkdir(child_rel)
        return VaultFolderCollection(child_dav_path, self.environ, self._store, child_rel)

    def delete(self):
        if not self._rel_path:
            # Không cho xóa folder gốc từ Explorer (phải xóa trong ứng dụng để an toàn)
            raise DAVError(HTTP_FORBIDDEN, "Hãy quản lý/xóa thư mục gốc từ ứng dụng PrivateVault.")
        self._store.delete_path(self._rel_path)

    def handle_move(self, dest_path: str) -> bool:
        if not self._rel_path:
            return False
        dest_folder, dest_rel = self.provider.split_vault_path(dest_path)
        src_folder, _ = self.provider.split_vault_path(self.path)
        if dest_folder and dest_folder == src_folder and dest_rel:
            self._store.move_path(self._rel_path, dest_rel)
            return True
        return False

    def handle_copy(self, dest_path: str, *, depth_infinity: bool) -> bool:
        if not self._rel_path:
            return False
        dest_folder, dest_rel = self.provider.split_vault_path(dest_path)
        src_folder, _ = self.provider.split_vault_path(self.path)
        if dest_folder and dest_folder == src_folder and dest_rel:
            self._store.copy_path(self._rel_path, dest_rel)
            return True
        return False


class VaultRootCollection(DAVCollection):
    def __init__(self, path: str, environ: dict, vault: VaultEngine):
        super().__init__(path, environ)
        self._vault = vault

    def get_member_names(self) -> list[str]:
        if not self._vault.is_unlocked:
            return []
        return sorted(
            mf.name
            for mf in self._vault.folders.values()
            if mf.mode == MODE_WEBDAV
        )

    def get_member(self, name: str):
        if not self._vault.is_unlocked:
            return None
        for fid, mf in self._vault.folders.items():
            if mf.mode == MODE_WEBDAV and mf.name == name:
                store = self._vault.get_store(fid)
                return VaultFolderCollection(f"/{name}", self.environ, store, "")
        return None

    def create_empty_resource(self, name: str):
        raise DAVError(HTTP_FORBIDDEN, "Chỉ được tạo tệp bên trong các thư mục được quản lý.")

    def create_collection(self, name: str):
        raise DAVError(HTTP_FORBIDDEN, "Hãy thêm thư mục mới từ ứng dụng PrivateVault.")

    def delete(self):
        raise DAVError(HTTP_FORBIDDEN)


class VaultDAVProvider(DAVProvider):
    def __init__(self, vault: VaultEngine):
        super().__init__()
        self._vault = vault

    @staticmethod
    def split_vault_path(path: str) -> tuple[str, str]:
        clean = path.strip("/")
        if not clean:
            return "", ""
        parts = clean.split("/", 1)
        folder_name = parts[0]
        rel_path = parts[1] if len(parts) > 1 else ""
        return folder_name, rel_path

    def get_resource_inst(self, path: str, environ: dict):
        if not self._vault.is_unlocked:
            raise DAVError(HTTP_NOT_FOUND)
        folder_name, rel_path = self.split_vault_path(path)
        if not folder_name:
            return VaultRootCollection("/", environ, self._vault)

        target_fid = None
        for fid, mf in self._vault.folders.items():
            if mf.mode == MODE_WEBDAV and mf.name == folder_name:
                target_fid = fid
                break
        if target_fid is None:
            return None

        store = self._vault.get_store(target_fid)
        if not rel_path or store.is_dir(rel_path):
            return VaultFolderCollection(path, environ, store, rel_path)
        if store.is_file(rel_path):
            return VaultFileResource(path, environ, store, rel_path)
        return None


# ---------------------------------------------------------------------------
# WebDAV Virtual Drive Controller
# ---------------------------------------------------------------------------

class WebDAVMountManager:
    """Khởi chạy WebDAV server nội bộ (127.0.0.1) và gắn/ngắt ổ đĩa Windows không cần Admin."""

    def __init__(self, vault: VaultEngine):
        self._vault = vault
        self._server = None
        self._thread: Optional[threading.Thread] = None
        self._port: Optional[int] = None
        self._token: Optional[str] = None
        self._drive_letter: Optional[str] = None
        self._lock = threading.RLock()

    @property
    def is_running(self) -> bool:
        return self._server is not None

    @property
    def drive_letter(self) -> Optional[str]:
        return self._drive_letter

    @property
    def mount_url(self) -> Optional[str]:
        if self._port and self._token:
            return f"http://127.0.0.1:{self._port}/{self._token}"
        return None

    @property
    def unc_path(self) -> Optional[str]:
        if self._port and self._token:
            return f"\\\\127.0.0.1@{self._port}\\DavWWWRoot\\{self._token}"
        return None

    def get_folder_access_path(self, folder_name: str) -> Optional[str]:
        if self._drive_letter:
            return f"{self._drive_letter}\\{folder_name}"
        if self.unc_path:
            return f"{self.unc_path}\\{folder_name}"
        return None

    def start_and_mount(self, preferred_drive: Optional[str] = None) -> tuple[bool, str]:
        """
        Khởi chạy WebDAV server trên 127.0.0.1:<port>/<random_token> và gắn thành ổ đĩa Windows.
        Trả về: (thành_công, thông_điệp)
        """
        with self._lock:
            if self.is_running:
                return True, f"Ổ ảo đã sẵn sàng tại {self._drive_letter or self.unc_path}"

            from cheroot import wsgi

            port = _find_free_port()
            token = f"pv_{secrets.token_hex(12)}"
            provider = VaultDAVProvider(self._vault)

            config = {
                "host": "127.0.0.1",
                "port": port,
                "provider_mapping": {f"/{token}": provider},
                "simple_dc": {"user_mapping": {"*": True}},
                "http_authenticator": {
                    "accept_basic": False,
                    "accept_digest": False,
                    "default_to_digest": False,
                },
                "dir_browser": {"enable": False},
                "lock_storage": True,
                "verbose": 0,
                "logging": {"enable": False},
            }

            app = WsgiDAVApp(config)
            server = wsgi.Server(("127.0.0.1", port), app, numthreads=12)
            thread = threading.Thread(target=server.safe_start, name="PrivateVault-WebDAV", daemon=True)
            thread.start()

            # Chờ server lắng nghe cổng
            ready = False
            for _ in range(30):
                try:
                    with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                        ready = True
                        break
                except OSError:
                    time.sleep(0.1)

            if not ready:
                try:
                    server.stop()
                except Exception:
                    pass
                return False, "Không thể khởi chạy máy chủ WebDAV nội bộ."

            self._server = server
            self._thread = thread
            self._port = port
            self._token = token

            # Gắn ổ đĩa Windows không cần quyền Admin qua `net use`
            drive = preferred_drive or _find_free_drive_letter()
            if drive and os.name == "nt":
                url = f"http://127.0.0.1:{port}/{token}"
                res = _run_hidden(["net", "use", drive, url, "/persistent:no"], timeout=15)
                if res.returncode == 0:
                    self._drive_letter = drive
                    return True, f"Đã gắn ổ đĩa ảo bảo mật tại {drive}\\"
                else:
                    # Fallback UNC nếu không gắn được ký tự ổ
                    err = (res.stderr or res.stdout).strip()
                    self._drive_letter = None
                    return True, f"WebDAV sẵn sàng qua UNC ({self.unc_path}). Lưu ý net use: {err}"

            return True, f"WebDAV sẵn sàng tại {self.mount_url}"

    def unmount_and_stop(self) -> None:
        """Ngắt ổ đĩa ảo (biến mất ngay khỏi Explorer) và dừng WebDAV server."""
        with self._lock:
            drive = self._drive_letter
            self._drive_letter = None
            if drive and os.name == "nt":
                try:
                    _run_hidden(["net", "use", drive, "/delete", "/yes"], timeout=10)
                except Exception:
                    pass

            if self._server is not None:
                try:
                    self._server.stop()
                except Exception:
                    pass
                self._server = None

            self._thread = None
            self._port = None
            self._token = None
