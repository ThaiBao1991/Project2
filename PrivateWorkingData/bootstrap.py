# -*- coding: utf-8 -*-
"""
bootstrap.py - Tự động kiểm tra và cài đặt thư viện Python cho PrivateVault.
Tuân thủ pattern Zero-Admin (--user khi không ở trong venv) và thoát sạch.
"""

import importlib
import os
import site
import subprocess
import sys

EXIT_MISSING_LIB_DIALOG = 2

REQUIRED_PACKAGES = {
    "customtkinter": "customtkinter>=5.2.0",
    "cryptography": "cryptography>=41.0.0",
    "wsgidav": "WsgiDAV>=4.3.0",
    "cheroot": "cheroot>=10.0.0",
    "pystray": "pystray>=0.19.5",
    "PIL": "Pillow>=10.0.0",
}


def configure_console_utf8() -> None:
    """Đảm bảo stdout/stderr hiển thị tiếng Việt UTF-8 trên Windows console."""
    for stream in (sys.stdout, sys.stderr):
        if stream is not None and hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass


def _is_in_venv() -> bool:
    return (
        hasattr(sys, "real_prefix")
        or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
    )


def _refresh_user_site_packages() -> None:
    """Nạp lại user site-packages vào sys.path cho lần chạy đầu tiên."""
    try:
        user_site = site.getusersitepackages()
        if user_site and os.path.isdir(user_site) and user_site not in sys.path:
            sys.path.append(user_site)
    except Exception:
        pass
    importlib.invalidate_caches()


def _check_missing() -> list[tuple[str, str]]:
    missing: list[tuple[str, str]] = []
    for mod_name, pip_spec in REQUIRED_PACKAGES.items():
        try:
            importlib.import_module(mod_name)
        except Exception:
            missing.append((mod_name, pip_spec))
    return missing


def _quote_pip_spec(spec: str) -> str:
    specials = ("<", ">", "=", "!", "~", "[", "]", " ")
    if any(ch in spec for ch in specials):
        return f'"{spec}"'
    return spec


def _show_missing_dialog(failed_specs: list[str], error_detail: str) -> None:
    """Hiển thị hộp thoại thông báo rõ ràng nếu không thể tự cài thư viện."""
    try:
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.withdraw()
        user_flag = "" if _is_in_venv() else "--user "
        quoted = " ".join(_quote_pip_spec(s) for s in failed_specs)
        cmd = f"python -m pip install {user_flag}{quoted}"
        msg = (
            "Không thể tự động cài đặt một số thư viện bắt buộc cho PrivateVault.\n\n"
            f"Thư viện thiếu: {', '.join(failed_specs)}\n\n"
            "Vui lòng kiểm tra kết nối mạng hoặc chạy lệnh sau trong CMD:\n"
            f"{cmd}\n\n"
            f"Chi tiết lỗi:\n{error_detail[:500]}"
        )
        messagebox.showerror("PrivateVault - Thiếu thư viện", msg)
        root.quit()
        root.destroy()
    except Exception:
        print("[ERROR] Thieu thu vien:", ", ".join(failed_specs))
        print(error_detail[:500])


def ensure_dependencies(silent: bool = False) -> bool:
    """
    Kiểm tra và tự động cài đặt các thư viện còn thiếu.
    Trả về True nếu đủ thư viện; nếu thất bại sẽ hiển thị thông báo và thoát mã 2.
    """
    configure_console_utf8()
    missing = _check_missing()
    if not missing:
        return True

    specs = [spec for _, spec in missing]
    if not silent:
        print(f"[PrivateVault] Dang tu dong cai dat thu vien thieu: {', '.join(specs)} ...")

    cmd = [sys.executable, "-m", "pip", "install", "--disable-pip-version-check"]
    if not _is_in_venv():
        cmd.append("--user")
    cmd.extend(specs)

    creationflags = 0
    if os.name == "nt":
        creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0)

    try:
        res = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            creationflags=creationflags,
            timeout=300,
        )
        _refresh_user_site_packages()
        still_missing = _check_missing()
        if not still_missing:
            if not silent:
                print("[PrivateVault] Cai dat thu vien hoan tat.")
            return True

        err_msg = (res.stderr or res.stdout or "Unknown pip error").strip()
        _show_missing_dialog([s for _, s in still_missing], err_msg)
        sys.exit(EXIT_MISSING_LIB_DIALOG)
    except Exception as exc:
        _show_missing_dialog(specs, str(exc))
        sys.exit(EXIT_MISSING_LIB_DIALOG)
