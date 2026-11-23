# -*- coding: utf-8 -*-
"""
crypto_engine.py - Lõi mã hóa AES-256-GCM, Scrypt KDF, Flat Blob Store,
đồng bộ Local Sync và Crypto-Shredding (Xóa không thể phục hồi).
"""

from __future__ import annotations

import base64
import json
import os
import shutil
import stat
import struct
import threading
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import BinaryIO, Optional

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

PVF_MAGIC = b"PVF1"
PVF_CHUNK_SIZE = 65536  # 64 KiB
PVF_TAG_SIZE = 16
PVF_ENC_CHUNK_SIZE = PVF_CHUNK_SIZE + PVF_TAG_SIZE
PVF_HEADER_SIZE = 4 + 8 + 8  # magic (4) + nonce_prefix (8) + plain_size (8)

SCRYPT_N = 2**15  # 32768 (~32MB RAM, cân bằng tốc độ & chống brute-force)
SCRYPT_R = 8
SCRYPT_P = 1

MODE_WEBDAV = "virtual_webdav"
MODE_LOCAL_SYNC = "local_sync"

WEBDAV_RECOMMENDED_MAX_FILE_BYTES = 48 * 1024 * 1024  # ~48 MB (dưới ngưỡng 50MB WebClient)


def _derive_kek(password: str, salt: bytes, n: int = SCRYPT_N, r: int = SCRYPT_R, p: int = SCRYPT_P) -> bytes:
    kdf = Scrypt(salt=salt, length=32, n=n, r=r, p=p)
    return kdf.derive(password.encode("utf-8"))


def _derive_subkey(master_key: bytes, info: bytes) -> bytes:
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=info,
    )
    return hkdf.derive(master_key)


def _make_readonly_writable(path: Path) -> None:
    try:
        os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
    except Exception:
        pass


def secure_delete_file(path: Path, full_passes: int = 1, fast_large_threshold: int = 8 * 1024 * 1024) -> bool:
    """
    Ghi đè ngẫu nhiên + fsync + truncate + đổi tên ngẫu nhiên + xóa.
    Với file cực lớn (> fast_large_threshold), ghi đè đầu/cuối/giữa để đảm bảo nhanh
    (lưu ý: với file mã hóa PVF, Crypto-Shredding đã hủy Master Key nên bản thân ciphertext
    vĩnh viễn không thể giải mã ngay cả trên SSD).
    """
    try:
        if not path.exists() or not path.is_file():
            return True
        _make_readonly_writable(path)
        size = path.stat().st_size
        if size > 0:
            with open(path, "r+b", buffering=0) as f:
                if size <= fast_large_threshold:
                    for p in range(max(1, full_passes)):
                        f.seek(0)
                        remaining = size
                        use_zero = (full_passes >= 2 and p == 1)
                        while remaining > 0:
                            chunk_len = min(262144, remaining)
                            f.write((b"\x00" * chunk_len) if use_zero else os.urandom(chunk_len))
                            remaining -= chunk_len
                        f.flush()
                        os.fsync(f.fileno())
                else:
                    # Ghi đè 1MB đầu, 1MB giữa, 1MB cuối
                    block = min(1024 * 1024, size)
                    for offset in (0, max(0, size // 2 - block // 2), max(0, size - block)):
                        f.seek(offset)
                        f.write(os.urandom(block))
                    f.flush()
                    os.fsync(f.fileno())
                f.truncate(0)
                f.flush()
                os.fsync(f.fileno())

        # Đổi tên ngẫu nhiên để xóa dấu vết tên file trong MFT/directory entry
        rand_name = path.with_name(f".shred_{uuid.uuid4().hex[:12]}.tmp")
        try:
            path.rename(rand_name)
            target = rand_name
        except Exception:
            target = path
        target.unlink(missing_ok=True)
        return True
    except Exception:
        try:
            path.unlink(missing_ok=True)
            return True
        except Exception:
            return False


def secure_delete_dir(dir_path: Path, full_passes: int = 1) -> list[str]:
    """Xóa an toàn toàn bộ cây thư mục. Trả về danh sách đường dẫn lỗi (nếu bị tiến trình khác khóa)."""
    errors: list[str] = []
    if not dir_path.exists():
        return errors

    for root, dirs, files in os.walk(dir_path, topdown=False):
        root_p = Path(root)
        for fname in files:
            fpath = root_p / fname
            if not secure_delete_file(fpath, full_passes=full_passes):
                errors.append(str(fpath))
        for dname in dirs:
            dpath = root_p / dname
            try:
                _make_readonly_writable(dpath)
                dpath.rmdir()
            except Exception:
                errors.append(str(dpath))

    try:
        _make_readonly_writable(dir_path)
        dir_path.rmdir()
    except Exception:
        if dir_path.exists():
            errors.append(str(dir_path))
    return errors


def _set_windows_hidden(path: Path) -> None:
    if os.name == "nt" and path.exists():
        try:
            import ctypes
            FILE_ATTRIBUTE_HIDDEN = 0x02
            ctypes.windll.kernel32.SetFileAttributesW(str(path), FILE_ATTRIBUTE_HIDDEN)
        except Exception:
            pass


def _atomic_write_bytes(target: Path, data: bytes) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + f".{uuid.uuid4().hex[:8]}.tmp")
    with open(tmp, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, target)


def encrypt_json_bytes(key: bytes, obj: dict) -> bytes:
    aes = AESGCM(key)
    nonce = os.urandom(12)
    raw = json.dumps(obj, ensure_ascii=False).encode("utf-8")
    ct = aes.encrypt(nonce, raw, b"PVJSON1")
    return b"PVJ1" + nonce + ct


def decrypt_json_bytes(key: bytes, data: bytes) -> dict:
    if len(data) < 4 + 12 + 16 or data[:4] != b"PVJ1":
        raise ValueError("Dữ liệu mã hóa JSON không hợp lệ hoặc đã bị hỏng.")
    aes = AESGCM(key)
    nonce = data[4:16]
    ct = data[16:]
    raw = aes.decrypt(nonce, ct, b"PVJSON1")
    return json.loads(raw.decode("utf-8"))


# ---------------------------------------------------------------------------
# Streaming Chunked AES-256-GCM File Format (PVF1)
# ---------------------------------------------------------------------------

def encrypt_stream_to_pvf(file_key: bytes, src_stream: BinaryIO, dst_path: Path) -> int:
    """Mã hóa từ binary stream ra file .pvf (chunked AES-256-GCM). Trả về tổng kích thước plaintext."""
    aes = AESGCM(file_key)
    nonce_prefix = os.urandom(8)
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = dst_path.with_suffix(f".{uuid.uuid4().hex[:8]}.tmp")
    total_plain = 0
    chunk_idx = 0

    with open(tmp, "wb") as out:
        # Placeholder header (ghi lại plain_size sau khi mã hóa xong)
        out.write(PVF_MAGIC + nonce_prefix + struct.pack(">Q", 0))
        while True:
            chunk = src_stream.read(PVF_CHUNK_SIZE)
            if not chunk:
                break
            total_plain += len(chunk)
            nonce = nonce_prefix + struct.pack(">I", chunk_idx)
            aad = PVF_MAGIC + struct.pack(">I", chunk_idx)
            out.write(aes.encrypt(nonce, chunk, aad))
            chunk_idx += 1

        # Cập nhật plain_size chính xác trong header
        out.seek(12)
        out.write(struct.pack(">Q", total_plain))
        out.flush()
        os.fsync(out.fileno())

    os.replace(tmp, dst_path)
    return total_plain


def encrypt_file_to_pvf(file_key: bytes, src_path: Path, dst_path: Path) -> int:
    with open(src_path, "rb") as src:
        return encrypt_stream_to_pvf(file_key, src, dst_path)


def decrypt_pvf_to_file(file_key: bytes, pvf_path: Path, dst_path: Path) -> int:
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    reader = PVFReader(file_key, pvf_path)
    total = 0
    try:
        with open(dst_path, "wb") as out:
            while True:
                data = reader.read(PVF_CHUNK_SIZE)
                if not data:
                    break
                out.write(data)
                total += len(data)
    finally:
        reader.close()
    return total


class PVFReader:
    """
    File-like object đọc giải mã on-the-fly từ file .pvf với hỗ trợ seek() O(1).
    Dùng trực tiếp cho WebDAV stream (0% plaintext ghi ra ổ đĩa).
    """

    def __init__(self, file_key: bytes, pvf_path: Path):
        self._aes = AESGCM(file_key)
        self._f = open(pvf_path, "rb")
        header = self._f.read(PVF_HEADER_SIZE)
        if len(header) != PVF_HEADER_SIZE or header[:4] != PVF_MAGIC:
            self._f.close()
            raise ValueError(f"Header PVF không hợp lệ: {pvf_path}")
        self._nonce_prefix = header[4:12]
        self.plain_size = struct.unpack(">Q", header[12:20])[0]
        self._pos = 0
        self._cached_idx: Optional[int] = None
        self._cached_plain: bytes = b""
        self.closed = False

    def _read_chunk(self, chunk_idx: int) -> bytes:
        if self._cached_idx == chunk_idx:
            return self._cached_plain
        offset = PVF_HEADER_SIZE + chunk_idx * PVF_ENC_CHUNK_SIZE
        self._f.seek(offset)
        enc = self._f.read(PVF_ENC_CHUNK_SIZE)
        if not enc:
            return b""
        nonce = self._nonce_prefix + struct.pack(">I", chunk_idx)
        aad = PVF_MAGIC + struct.pack(">I", chunk_idx)
        plain = self._aes.decrypt(nonce, enc, aad)
        self._cached_idx = chunk_idx
        self._cached_plain = plain
        return plain

    def read(self, size: int = -1) -> bytes:
        if self.closed or self._pos >= self.plain_size:
            return b""
        if size is None or size < 0:
            to_read = self.plain_size - self._pos
        else:
            to_read = min(size, self.plain_size - self._pos)
        if to_read <= 0:
            return b""

        parts: list[bytes] = []
        remaining = to_read
        while remaining > 0 and self._pos < self.plain_size:
            chunk_idx = self._pos // PVF_CHUNK_SIZE
            in_chunk_off = self._pos % PVF_CHUNK_SIZE
            plain_chunk = self._read_chunk(chunk_idx)
            if not plain_chunk:
                break
            take = min(remaining, len(plain_chunk) - in_chunk_off)
            if take <= 0:
                break
            parts.append(plain_chunk[in_chunk_off: in_chunk_off + take])
            self._pos += take
            remaining -= take
        return b"".join(parts)

    def seek(self, offset: int, whence: int = os.SEEK_SET) -> int:
        if whence == os.SEEK_SET:
            new_pos = offset
        elif whence == os.SEEK_CUR:
            new_pos = self._pos + offset
        elif whence == os.SEEK_END:
            new_pos = self.plain_size + offset
        else:
            raise ValueError("Invalid whence")
        self._pos = max(0, min(self.plain_size, new_pos))
        return self._pos

    def tell(self) -> int:
        return self._pos

    def readable(self) -> bool:
        return True

    def seekable(self) -> bool:
        return True

    def close(self) -> None:
        if not self.closed:
            self.closed = True
            self._cached_plain = b""
            self._cached_idx = None
            try:
                self._f.close()
            except Exception:
                pass

    def __enter__(self) -> "PVFReader":
        return self

    def __exit__(self, *args) -> None:
        self.close()


# ---------------------------------------------------------------------------
# Folder Store (Flat Blob Store + Encrypted Tree Index)
# ---------------------------------------------------------------------------

class FolderBlobStore:
    """
    Quản lý toàn bộ cây thư mục & tệp của 1 folder bảo mật dưới dạng:
    - tree.enc: JSON mã hóa AES-256-GCM lưu {"dirs": [...], "files": {rel_path: {blob, size, mtime}}}
    - <uuid>.pvf: từng file mã hóa phẳng (không lộ tên, không chạm giới hạn MAX_PATH Windows).
    """

    def __init__(self, folder_dir: Path, folder_key: bytes):
        self.folder_dir = folder_dir
        self.folder_key = folder_key
        self.tree_path = folder_dir / "tree.enc"
        self.lock = threading.RLock()
        self.dirs: set[str] = set()
        self.files: dict[str, dict] = {}
        self.folder_dir.mkdir(parents=True, exist_ok=True)
        self._load_tree()

    @staticmethod
    def norm_path(rel_path: str) -> str:
        p = rel_path.replace("\\", "/").strip("/")
        while "//" in p:
            p = p.replace("//", "/")
        return p

    def _load_tree(self) -> None:
        with self.lock:
            if not self.tree_path.exists():
                self.dirs = set()
                self.files = {}
                self._save_tree()
                return
            data = decrypt_json_bytes(self.folder_key, self.tree_path.read_bytes())
            self.dirs = set(data.get("dirs", []))
            self.files = dict(data.get("files", {}))

    def _save_tree(self) -> None:
        with self.lock:
            payload = {
                "dirs": sorted(self.dirs),
                "files": self.files,
            }
            enc = encrypt_json_bytes(self.folder_key, payload)
            _atomic_write_bytes(self.tree_path, enc)

    def _ensure_parent_dirs(self, rel_path: str) -> None:
        parts = rel_path.split("/")[:-1]
        cur = ""
        for part in parts:
            cur = f"{cur}/{part}" if cur else part
            self.dirs.add(cur)

    def exists(self, rel_path: str) -> bool:
        p = self.norm_path(rel_path)
        with self.lock:
            return p == "" or p in self.dirs or p in self.files

    def is_dir(self, rel_path: str) -> bool:
        p = self.norm_path(rel_path)
        with self.lock:
            return p == "" or p in self.dirs

    def is_file(self, rel_path: str) -> bool:
        p = self.norm_path(rel_path)
        with self.lock:
            return p in self.files

    def list_children(self, rel_dir: str) -> tuple[list[str], list[str]]:
        """Trả về (child_dir_names, child_file_names) trực tiếp bên trong rel_dir."""
        d = self.norm_path(rel_dir)
        prefix = f"{d}/" if d else ""
        child_dirs: set[str] = set()
        child_files: set[str] = set()
        with self.lock:
            for sub in self.dirs:
                if sub.startswith(prefix):
                    rest = sub[len(prefix):]
                    if rest and "/" not in rest:
                        child_dirs.add(rest)
            for fpath in self.files:
                if fpath.startswith(prefix):
                    rest = fpath[len(prefix):]
                    if rest and "/" not in rest:
                        child_files.add(rest)
        return sorted(child_dirs), sorted(child_files)

    def mkdir(self, rel_dir: str) -> None:
        d = self.norm_path(rel_dir)
        if not d:
            return
        with self.lock:
            if d in self.files:
                raise FileExistsError(f"Đã tồn tại tệp trùng tên: {d}")
            self._ensure_parent_dirs(d)
            self.dirs.add(d)
            self._save_tree()

    def write_file_from_stream(self, rel_path: str, stream: BinaryIO, mtime: Optional[float] = None) -> dict:
        p = self.norm_path(rel_path)
        if not p:
            raise ValueError("Đường dẫn tệp không hợp lệ.")
        blob_name = f"{uuid.uuid4().hex}.pvf"
        blob_path = self.folder_dir / blob_name
        plain_size = encrypt_stream_to_pvf(self.folder_key, stream, blob_path)
        now = mtime if mtime is not None else time.time()

        old_blob: Optional[str] = None
        with self.lock:
            if p in self.files:
                old_blob = self.files[p].get("blob")
            self._ensure_parent_dirs(p)
            self.files[p] = {
                "blob": blob_name,
                "size": plain_size,
                "mtime": now,
            }
            self._save_tree()

        if old_blob and old_blob != blob_name:
            secure_delete_file(self.folder_dir / old_blob, full_passes=1)
        return self.files[p]

    def write_file_from_path(self, rel_path: str, src_path: Path) -> dict:
        st = src_path.stat()
        with open(src_path, "rb") as f:
            return self.write_file_from_stream(rel_path, f, mtime=st.st_mtime)

    def open_reader(self, rel_path: str) -> PVFReader:
        p = self.norm_path(rel_path)
        with self.lock:
            info = self.files.get(p)
            if not info:
                raise FileNotFoundError(p)
            blob_path = self.folder_dir / info["blob"]
        return PVFReader(self.folder_key, blob_path)

    def get_file_info(self, rel_path: str) -> Optional[dict]:
        p = self.norm_path(rel_path)
        with self.lock:
            info = self.files.get(p)
            return dict(info) if info else None

    def delete_path(self, rel_path: str) -> None:
        p = self.norm_path(rel_path)
        if not p:
            return
        blobs_to_shred: list[str] = []
        with self.lock:
            if p in self.files:
                blobs_to_shred.append(self.files.pop(p)["blob"])
            elif p in self.dirs:
                prefix = f"{p}/"
                self.dirs.discard(p)
                for d in [x for x in self.dirs if x.startswith(prefix)]:
                    self.dirs.discard(d)
                for f in [x for x in self.files if x.startswith(prefix)]:
                    blobs_to_shred.append(self.files.pop(f)["blob"])
            self._save_tree()

        for b in blobs_to_shred:
            secure_delete_file(self.folder_dir / b, full_passes=1)

    def move_path(self, src_rel: str, dst_rel: str) -> None:
        src = self.norm_path(src_rel)
        dst = self.norm_path(dst_rel)
        if not src or not dst or src == dst:
            return
        with self.lock:
            if src in self.files:
                if dst in self.files:
                    old_blob = self.files.pop(dst)["blob"]
                    secure_delete_file(self.folder_dir / old_blob, full_passes=1)
                self._ensure_parent_dirs(dst)
                self.files[dst] = self.files.pop(src)
                self._save_tree()
            elif src in self.dirs:
                prefix = f"{src}/"
                self._ensure_parent_dirs(dst)
                new_dirs = set()
                for d in list(self.dirs):
                    if d == src:
                        self.dirs.discard(d)
                        new_dirs.add(dst)
                    elif d.startswith(prefix):
                        self.dirs.discard(d)
                        new_dirs.add(dst + d[len(src):])
                self.dirs.update(new_dirs)

                updates = {}
                for f in list(self.files.keys()):
                    if f.startswith(prefix):
                        updates[dst + f[len(src):]] = self.files.pop(f)
                self.files.update(updates)
                self._save_tree()

    def copy_path(self, src_rel: str, dst_rel: str) -> None:
        src = self.norm_path(src_rel)
        dst = self.norm_path(dst_rel)
        if not src or not dst or src == dst:
            return
        with self.lock:
            if src in self.files:
                info = self.files[src]
                src_blob = self.folder_dir / info["blob"]
                new_blob = f"{uuid.uuid4().hex}.pvf"
                shutil.copy2(src_blob, self.folder_dir / new_blob)
                self._ensure_parent_dirs(dst)
                self.files[dst] = {
                    "blob": new_blob,
                    "size": info["size"],
                    "mtime": time.time(),
                }
                self._save_tree()
            elif src in self.dirs:
                prefix = f"{src}/"
                self._ensure_parent_dirs(dst)
                self.dirs.add(dst)
                for d in list(self.dirs):
                    if d.startswith(prefix):
                        self.dirs.add(dst + d[len(src):])
                for f, info in list(self.files.items()):
                    if f.startswith(prefix):
                        src_blob = self.folder_dir / info["blob"]
                        new_blob = f"{uuid.uuid4().hex}.pvf"
                        shutil.copy2(src_blob, self.folder_dir / new_blob)
                        self.files[dst + f[len(src):]] = {
                            "blob": new_blob,
                            "size": info["size"],
                            "mtime": time.time(),
                        }
                self._save_tree()

    def import_host_directory(self, host_dir: Path) -> tuple[int, int]:
        """Nhập toàn bộ thư mục từ máy vào store mã hóa. Trả về (số_file, tổng_bytes)."""
        file_count = 0
        total_bytes = 0
        host_dir = host_dir.resolve()
        for root, dirs, files in os.walk(host_dir):
            root_p = Path(root)
            rel_root = root_p.relative_to(host_dir).as_posix()
            if rel_root != ".":
                self.mkdir(rel_root)
            for fname in files:
                fpath = root_p / fname
                rel = fname if rel_root == "." else f"{rel_root}/{fname}"
                info = self.write_file_from_path(rel, fpath)
                file_count += 1
                total_bytes += int(info["size"])
        return file_count, total_bytes

    def export_to_host_directory(self, dst_dir: Path) -> int:
        """Giải mã toàn bộ cây thư mục ra dst_dir. Trả về số file đã xuất."""
        dst_dir.mkdir(parents=True, exist_ok=True)
        count = 0
        with self.lock:
            dirs_snap = sorted(self.dirs)
            files_snap = list(self.files.items())

        for d in dirs_snap:
            (dst_dir / Path(d)).mkdir(parents=True, exist_ok=True)
        for rel, info in files_snap:
            target = dst_dir / Path(rel)
            blob_path = self.folder_dir / info["blob"]
            decrypt_pvf_to_file(self.folder_key, blob_path, target)
            mtime = info.get("mtime")
            if mtime:
                try:
                    os.utime(target, (mtime, mtime))
                except Exception:
                    pass
            count += 1
        return count

    def sync_from_host_directory(self, work_dir: Path) -> tuple[int, int]:
        """
        Đồng bộ thay đổi từ thư mục làm việc cục bộ (local_sync) ngược lại vào store mã hóa.
        Trả về (số_file_cập_nhật, số_file_xóa).
        """
        updated = 0
        deleted = 0
        if not work_dir.exists():
            return 0, 0

        seen_files: set[str] = set()
        seen_dirs: set[str] = set()

        for root, dirs, files in os.walk(work_dir):
            root_p = Path(root)
            rel_root = root_p.relative_to(work_dir).as_posix()
            if rel_root != ".":
                seen_dirs.add(self.norm_path(rel_root))
            for fname in files:
                fpath = root_p / fname
                rel = self.norm_path(fname if rel_root == "." else f"{rel_root}/{fname}")
                seen_files.add(rel)
                st = fpath.stat()
                existing = self.get_file_info(rel)
                if (
                    existing is None
                    or int(existing.get("size", -1)) != st.st_size
                    or abs(float(existing.get("mtime", 0)) - st.st_mtime) > 0.01
                ):
                    self.write_file_from_path(rel, fpath)
                    updated += 1

        # Cập nhật thư mục & xóa các file đã bị xóa trong work_dir
        with self.lock:
            old_files = set(self.files.keys())
            removed_files = old_files - seen_files
            for rf in removed_files:
                blob = self.files.pop(rf)["blob"]
                secure_delete_file(self.folder_dir / blob, full_passes=1)
                deleted += 1
            self.dirs = seen_dirs
            self._save_tree()

        return updated, deleted

    def stats(self) -> tuple[int, int]:
        """Trả về (số_file, tổng_kích_thước_plaintext)."""
        with self.lock:
            total = sum(int(v.get("size", 0)) for v in self.files.values())
            return len(self.files), total


# ---------------------------------------------------------------------------
# Vault Manager
# ---------------------------------------------------------------------------

@dataclass
class ManagedFolder:
    folder_id: str
    name: str
    mode: str  # MODE_WEBDAV | MODE_LOCAL_SYNC
    created_at: float = field(default_factory=time.time)
    original_path: str = ""

    def to_dict(self) -> dict:
        return {
            "folder_id": self.folder_id,
            "name": self.name,
            "mode": self.mode,
            "created_at": self.created_at,
            "original_path": self.original_path,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "ManagedFolder":
        return cls(
            folder_id=d["folder_id"],
            name=d["name"],
            mode=d.get("mode", MODE_WEBDAV),
            created_at=float(d.get("created_at", time.time())),
            original_path=d.get("original_path", ""),
        )


class VaultEngine:
    """
    Quản lý toàn bộ Vault: khởi tạo, xác thực mật khẩu, quản lý folder,
    đồng bộ Local Sync và Crypto-Shredding toàn phần/từng phần.
    """

    def __init__(self, base_dir: Path):
        self.base_dir = base_dir.resolve()
        self.vault_dir = self.base_dir / "vault_data"
        self.store_dir = self.vault_dir / "store"
        self.work_dir = self.vault_dir / "work"
        self.header_path = self.vault_dir / "vault_header.bin"
        self.meta_path = self.vault_dir / "vault_meta.enc"

        self._master_key: Optional[bytes] = None
        self._meta_key: Optional[bytes] = None
        self.folders: dict[str, ManagedFolder] = {}
        self._stores: dict[str, FolderBlobStore] = {}
        self._active_local_work: dict[str, Path] = {}
        self._lock = threading.RLock()

    @property
    def is_initialized(self) -> bool:
        return self.header_path.exists()

    @property
    def is_unlocked(self) -> bool:
        return self._master_key is not None

    def initialize_vault(self, password: str) -> None:
        if len(password) < 4:
            raise ValueError("Mật khẩu phải có ít nhất 4 ký tự.")
        self.vault_dir.mkdir(parents=True, exist_ok=True)
        self.store_dir.mkdir(parents=True, exist_ok=True)
        _set_windows_hidden(self.vault_dir)

        salt = os.urandom(32)
        kek = _derive_kek(password, salt)
        master_key = os.urandom(32)
        nonce = os.urandom(12)
        wrapped = AESGCM(kek).encrypt(nonce, master_key, b"PVHEADER1")

        header_obj = {
            "magic": "PVLT1",
            "salt": base64.b64encode(salt).decode("ascii"),
            "kdf": {"name": "scrypt", "n": SCRYPT_N, "r": SCRYPT_R, "p": SCRYPT_P},
            "nonce": base64.b64encode(nonce).decode("ascii"),
            "wrapped_master_key": base64.b64encode(wrapped).decode("ascii"),
        }
        _atomic_write_bytes(self.header_path, json.dumps(header_obj, indent=2).encode("utf-8"))

        self._master_key = master_key
        self._meta_key = _derive_subkey(master_key, b"privatevault:meta:v1")
        self.folders = {}
        self._stores = {}
        self._save_meta()

    def unlock(self, password: str) -> bool:
        if not self.is_initialized:
            raise RuntimeError("Vault chưa được khởi tạo.")
        try:
            header_obj = json.loads(self.header_path.read_text(encoding="utf-8"))
            salt = base64.b64decode(header_obj["salt"])
            kdf_cfg = header_obj.get("kdf", {})
            kek = _derive_kek(
                password,
                salt,
                n=int(kdf_cfg.get("n", SCRYPT_N)),
                r=int(kdf_cfg.get("r", SCRYPT_R)),
                p=int(kdf_cfg.get("p", SCRYPT_P)),
            )
            nonce = base64.b64decode(header_obj["nonce"])
            wrapped = base64.b64decode(header_obj["wrapped_master_key"])
            master_key = AESGCM(kek).decrypt(nonce, wrapped, b"PVHEADER1")
        except (InvalidTag, ValueError, KeyError):
            return False

        with self._lock:
            self._master_key = master_key
            self._meta_key = _derive_subkey(master_key, b"privatevault:meta:v1")
            self._load_meta()
            # Mở sẵn các FolderBlobStore
            self._stores = {}
            for fid in self.folders:
                self._stores[fid] = self._open_store(fid)
            # Giải mã các folder chế độ local_sync ra thư mục làm việc
            self._prepare_local_sync_folders()
        return True

    def change_password(self, old_password: str, new_password: str) -> bool:
        if len(new_password) < 4:
            raise ValueError("Mật khẩu mới phải có ít nhất 4 ký tự.")
        if not self.is_unlocked:
            raise RuntimeError("Cần mở khóa Vault trước khi đổi mật khẩu.")
        # Xác thực mật khẩu cũ trước
        header_obj = json.loads(self.header_path.read_text(encoding="utf-8"))
        salt = base64.b64decode(header_obj["salt"])
        kdf_cfg = header_obj.get("kdf", {})
        old_kek = _derive_kek(
            old_password,
            salt,
            n=int(kdf_cfg.get("n", SCRYPT_N)),
            r=int(kdf_cfg.get("r", SCRYPT_R)),
            p=int(kdf_cfg.get("p", SCRYPT_P)),
        )
        try:
            AESGCM(old_kek).decrypt(
                base64.b64decode(header_obj["nonce"]),
                base64.b64decode(header_obj["wrapped_master_key"]),
                b"PVHEADER1",
            )
        except InvalidTag:
            return False

        # Bọc lại cùng Master Key bằng mật khẩu mới (không cần mã hóa lại dữ liệu)
        new_salt = os.urandom(32)
        new_kek = _derive_kek(new_password, new_salt)
        new_nonce = os.urandom(12)
        wrapped = AESGCM(new_kek).encrypt(new_nonce, self._master_key, b"PVHEADER1")
        new_header = {
            "magic": "PVLT1",
            "salt": base64.b64encode(new_salt).decode("ascii"),
            "kdf": {"name": "scrypt", "n": SCRYPT_N, "r": SCRYPT_R, "p": SCRYPT_P},
            "nonce": base64.b64encode(new_nonce).decode("ascii"),
            "wrapped_master_key": base64.b64encode(wrapped).decode("ascii"),
        }
        _atomic_write_bytes(self.header_path, json.dumps(new_header, indent=2).encode("utf-8"))
        return True

    def _folder_key(self, folder_id: str) -> bytes:
        assert self._master_key is not None
        return _derive_subkey(self._master_key, f"privatevault:folder:{folder_id}".encode("utf-8"))

    def _open_store(self, folder_id: str) -> FolderBlobStore:
        return FolderBlobStore(self.store_dir / folder_id, self._folder_key(folder_id))

    def _load_meta(self) -> None:
        assert self._meta_key is not None
        if not self.meta_path.exists():
            self.folders = {}
            self._save_meta()
            return
        data = decrypt_json_bytes(self._meta_key, self.meta_path.read_bytes())
        self.folders = {
            fid: ManagedFolder.from_dict(item)
            for fid, item in data.get("folders", {}).items()
        }

    def _save_meta(self) -> None:
        assert self._meta_key is not None
        payload = {
            "version": 1,
            "folders": {fid: f.to_dict() for fid, f in self.folders.items()},
        }
        _atomic_write_bytes(self.meta_path, encrypt_json_bytes(self._meta_key, payload))

    def get_store(self, folder_id: str) -> FolderBlobStore:
        with self._lock:
            if not self.is_unlocked:
                raise RuntimeError("Vault đang khóa.")
            if folder_id not in self._stores:
                self._stores[folder_id] = self._open_store(folder_id)
            return self._stores[folder_id]

    def get_store_by_name(self, folder_name: str) -> Optional[FolderBlobStore]:
        with self._lock:
            for fid, mf in self.folders.items():
                if mf.name == folder_name:
                    return self.get_store(fid)
        return None

    def _safe_folder_name(self, name: str) -> str:
        clean = "".join(ch for ch in name.strip() if ch not in '<>:"/\\|?*').strip(" .")
        if not clean:
            clean = "Folder"
        existing = {f.name.lower() for f in self.folders.values()}
        candidate = clean
        idx = 2
        while candidate.lower() in existing:
            candidate = f"{clean}_{idx}"
            idx += 1
        return candidate

    def _prepare_local_sync_folders(self) -> None:
        self._active_local_work = {}
        local_folders = [f for f in self.folders.values() if f.mode == MODE_LOCAL_SYNC]
        if not local_folders:
            return
        self.work_dir.mkdir(parents=True, exist_ok=True)
        _set_windows_hidden(self.work_dir)
        for mf in local_folders:
            dst = self.work_dir / mf.folder_id / mf.name
            store = self.get_store(mf.folder_id)
            if not dst.exists():
                store.export_to_host_directory(dst)
            self._active_local_work[mf.folder_id] = dst

    def get_local_work_path(self, folder_id: str) -> Optional[Path]:
        return self._active_local_work.get(folder_id)

    def add_folder(
        self,
        source_dir: Optional[Path],
        name: str,
        mode: str = MODE_WEBDAV,
        shred_source: bool = False,
    ) -> tuple[ManagedFolder, int, int, list[str]]:
        """
        Thêm 1 folder mới vào Vault (có thể là folder rỗng nếu source_dir=None,
        hoặc nhập từ thư mục thật trên máy).
        Trả về: (ManagedFolder, file_count, total_bytes, warnings)
        """
        if not self.is_unlocked:
            raise RuntimeError("Vault đang khóa.")
        if mode not in (MODE_WEBDAV, MODE_LOCAL_SYNC):
            raise ValueError("Chế độ folder không hợp lệ.")

        warnings: list[str] = []
        fid = uuid.uuid4().hex[:16]
        safe_name = self._safe_folder_name(name)
        mf = ManagedFolder(
            folder_id=fid,
            name=safe_name,
            mode=mode,
            original_path=str(source_dir.resolve()) if source_dir else "",
        )

        store = self._open_store(fid)
        file_count = 0
        total_bytes = 0

        if source_dir is not None and source_dir.exists():
            # Kiểm tra cảnh báo file > 48MB nếu chọn chế độ WebDAV
            if mode == MODE_WEBDAV:
                large_files = []
                for root, _, files in os.walk(source_dir):
                    for fn in files:
                        fp = Path(root) / fn
                        try:
                            if fp.stat().st_size > WEBDAV_RECOMMENDED_MAX_FILE_BYTES:
                                large_files.append(fn)
                        except Exception:
                            pass
                if large_files:
                    warnings.append(
                        f"Có {len(large_files)} tệp > 48MB (VD: {large_files[0]}). "
                        "Windows WebClient giới hạn 50MB/tệp — nên chuyển folder này sang chế độ 'Vault cục bộ'."
                    )
            file_count, total_bytes = store.import_host_directory(source_dir)

        with self._lock:
            self.folders[fid] = mf
            self._stores[fid] = store
            self._save_meta()
            if mode == MODE_LOCAL_SYNC:
                self.work_dir.mkdir(parents=True, exist_ok=True)
                _set_windows_hidden(self.work_dir)
                dst = self.work_dir / fid / safe_name
                store.export_to_host_directory(dst)
                self._active_local_work[fid] = dst

        if shred_source and source_dir is not None and source_dir.exists():
            shred_errs = secure_delete_dir(source_dir, full_passes=1)
            if shred_errs:
                warnings.append(f"Không thể xóa sạch {len(shred_errs)} mục ở thư mục gốc (có thể đang mở).")

        return mf, file_count, total_bytes, warnings

    def switch_folder_mode(self, folder_id: str, new_mode: str) -> list[str]:
        """Chuyển đổi chế độ folder giữa virtual_webdav <-> local_sync không cần mã hóa lại."""
        if not self.is_unlocked:
            raise RuntimeError("Vault đang khóa.")
        warnings: list[str] = []
        with self._lock:
            mf = self.folders.get(folder_id)
            if not mf or mf.mode == new_mode:
                return warnings
            store = self.get_store(folder_id)
            if mf.mode == MODE_LOCAL_SYNC:
                work_p = self._active_local_work.pop(folder_id, None)
                if work_p and work_p.exists():
                    store.sync_from_host_directory(work_p)
                    errs = secure_delete_dir(self.work_dir / folder_id, full_passes=1)
                    if errs:
                        warnings.append(f"Còn {len(errs)} file tạm chưa xóa được ở bản cục bộ.")
            mf.mode = new_mode
            self._save_meta()
            if new_mode == MODE_LOCAL_SYNC:
                self.work_dir.mkdir(parents=True, exist_ok=True)
                _set_windows_hidden(self.work_dir)
                dst = self.work_dir / folder_id / mf.name
                store.export_to_host_directory(dst)
                self._active_local_work[folder_id] = dst
        return warnings

    def export_and_remove_folder(self, folder_id: str, target_dir: Path) -> Path:
        """Gỡ folder khỏi Vault và giải mã trực tiếp toàn bộ tệp/thư mục con vào target_dir."""
        if not self.is_unlocked:
            raise RuntimeError("Vault đang khóa.")
        with self._lock:
            mf = self.folders.get(folder_id)
            if not mf:
                raise KeyError("Không tìm thấy folder.")
            store = self.get_store(folder_id)
            # Đồng bộ thay đổi mới nhất nếu là local_sync
            work_p = self._active_local_work.get(folder_id)
            if work_p and work_p.exists():
                store.sync_from_host_directory(work_p)

            export_dir = target_dir
            store.export_to_host_directory(export_dir)
            self.shred_folder(folder_id)
            return export_dir

    def shred_folder(self, folder_id: str) -> list[str]:
        """Chế độ A: Xóa vĩnh viễn không thể phục hồi 1 folder cụ thể (Crypto-Shredding)."""
        if not self.is_unlocked:
            raise RuntimeError("Vault đang khóa.")
        errors: list[str] = []
        with self._lock:
            self.folders.pop(folder_id, None)
            self._stores.pop(folder_id, None)
            work_p = self._active_local_work.pop(folder_id, None)
            self._save_meta()

        # Hủy tree.enc 3 lượt trước -> mất toàn bộ chỉ mục tên file
        folder_store_dir = self.store_dir / folder_id
        tree_file = folder_store_dir / "tree.enc"
        if tree_file.exists():
            secure_delete_file(tree_file, full_passes=3)
        errors.extend(secure_delete_dir(folder_store_dir, full_passes=1))

        if work_p is not None:
            errors.extend(secure_delete_dir(self.work_dir / folder_id, full_passes=1))
        return errors

    def sync_all_local_folders(self) -> list[str]:
        """Đồng bộ toàn bộ folder local_sync vào store mã hóa (không khóa)."""
        warnings: list[str] = []
        if not self.is_unlocked:
            return warnings
        with self._lock:
            for fid, work_p in list(self._active_local_work.items()):
                if work_p.exists():
                    try:
                        self.get_store(fid).sync_from_host_directory(work_p)
                    except Exception as exc:
                        warnings.append(f"Lỗi đồng bộ folder {fid}: {exc}")
        return warnings

    def lock(self) -> list[str]:
        """
        Khóa Vault: đồng bộ & xóa an toàn toàn bộ bản giải mã local_sync,
        xóa Master Key khỏi RAM.
        """
        warnings: list[str] = []
        with self._lock:
            if self.is_unlocked:
                warnings.extend(self.sync_all_local_folders())
            self._active_local_work.clear()
            self._stores.clear()
            self.folders.clear()
            self._master_key = None
            self._meta_key = None

        if self.work_dir.exists():
            errs = secure_delete_dir(self.work_dir, full_passes=1)
            if errs:
                warnings.append(f"Có {len(errs)} tệp trong vùng làm việc đang bị chương trình khác mở.")
        return warnings

    def secure_wipe_all(self) -> list[str]:
        """
        CRYPTO-SHREDDING TOÀN BỘ VAULT (Chế độ A / Chế độ B / Hẹn giờ xóa).
        Có thể gọi NGAY CẢ KHI VAULT ĐANG KHÓA (không cần mật khẩu).
        1. Ghi đè 3 lượt & hủy vault_header.bin (tiêu hủy Master Key vĩnh viễn).
        2. Ghi đè 3 lượt & hủy vault_meta.enc.
        3. Xóa sạch toàn bộ store/ và work/.
        """
        errors: list[str] = []
        with self._lock:
            self._active_local_work.clear()
            self._stores.clear()
            self.folders.clear()
            self._master_key = None
            self._meta_key = None

        # Bước 1 & 2: Crypto-Shredding (tiêu hủy khóa chủ + metadata trước tiên -> < 50ms)
        if self.header_path.exists():
            if not secure_delete_file(self.header_path, full_passes=3):
                errors.append(str(self.header_path))
        if self.meta_path.exists():
            if not secure_delete_file(self.meta_path, full_passes=3):
                errors.append(str(self.meta_path))

        # Bước 3: Hủy toàn bộ dữ liệu store & bản rõ work
        if self.store_dir.exists():
            errors.extend(secure_delete_dir(self.store_dir, full_passes=1))
        if self.work_dir.exists():
            errors.extend(secure_delete_dir(self.work_dir, full_passes=1))

        return errors
