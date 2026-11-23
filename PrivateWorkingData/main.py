# -*- coding: utf-8 -*-
"""
main.py - PrivateVault Desktop Application (CustomTkinter + System Tray).
- Mặc định khóa cứng: không nhập mật khẩu thì không thấy và không thao tác được folder.
- Nhập mật khẩu 1 lần mỗi ngày (chạy nền System Tray, tự khóa khi qua 00:00).
- Kiến trúc Lai: Ổ ảo WebDAV (Zero-Admin) + Vault cục bộ (folder nặng > 50MB).
- Xóa không thể phục hồi: Chế độ A (xóa tay), Chế độ B (sai pass quá N lần), và Hẹn giờ xóa.
"""

from __future__ import annotations

import os
import subprocess
import sys
import threading
from datetime import datetime, timedelta
from pathlib import Path
from tkinter import filedialog, messagebox, ttk
import tkinter as tk
from typing import Optional

from bootstrap import ensure_dependencies

# Đảm bảo đủ thư viện trước khi import UI & Crypto
ensure_dependencies()

import customtkinter as ctk
from PIL import Image, ImageDraw
import pystray

from crypto_engine import MODE_LOCAL_SYNC, MODE_WEBDAV, VaultEngine
from policy_manager import PolicyManager
from webdav_mount import WebDAVMountManager

BASE_DIR = Path(__file__).resolve().parent

# Bảng màu Dark Security Theme
C = {
    "bg": "#0F172A",
    "panel": "#1E293B",
    "card": "#263449",
    "accent": "#38BDF8",
    "accent_hover": "#0284C7",
    "success": "#22C55E",
    "warning": "#F59E0B",
    "danger": "#EF4444",
    "danger_hover": "#B91C1C",
    "text": "#F8FAFC",
    "muted": "#94A3B8",
    "border": "#334155",
}


def format_size(num_bytes: int) -> str:
    val = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if val < 1024 or unit == "TB":
            return f"{val:.1f} {unit}" if unit != "B" else f"{int(val)} B"
        val /= 1024.0
    return f"{val:.1f} TB"


def open_in_explorer(path_str: str) -> None:
    if not path_str:
        return
    try:
        if os.name == "nt":
            os.startfile(path_str)
        else:
            subprocess.Popen(["xdg-open", path_str])
    except Exception as exc:
        messagebox.showerror("Không thể mở thư mục", f"Lỗi khi mở đường dẫn:\n{path_str}\n\n{exc}")


def create_tray_icon_image(locked: bool) -> Image.Image:
    img = Image.new("RGBA", (64, 64), (15, 23, 42, 255))
    draw = ImageDraw.Draw(img)
    color = (239, 68, 68, 255) if locked else (34, 197, 94, 255)
    # Vẽ biểu tượng ổ khóa đơn giản
    draw.arc([18, 10, 46, 36], start=180, end=360, fill=color, width=5)
    draw.rounded_rectangle([14, 28, 50, 54], radius=6, fill=color)
    draw.ellipse([28, 36, 36, 44], fill=(15, 23, 42, 255))
    return img


# ---------------------------------------------------------------------------
# Dialogs
# ---------------------------------------------------------------------------

class AddFolderDialog(ctk.CTkToplevel):
    """Hộp thoại thêm folder mới (từ máy hoặc tạo rỗng) với chọn chế độ Lai."""

    def __init__(self, parent, mode_create_empty: bool = False):
        super().__init__(parent)
        self.title("Tạo Folder Bảo Mật Rỗng" if mode_create_empty else "Thêm Folder Vào PrivateVault")
        self.geometry("540x390")
        self.resizable(False, False)
        self.configure(fg_color=C["bg"])
        self.transient(parent)
        self.grab_set()

        self.result: Optional[dict] = None
        self._create_empty = mode_create_empty

        self.var_src = tk.StringVar(value="")
        self.var_name = tk.StringVar(value="")
        self.var_mode = tk.StringVar(value=MODE_WEBDAV)
        self.var_shred_src = tk.BooleanVar(value=False)

        body = ctk.CTkFrame(self, fg_color=C["panel"], corner_radius=12)
        body.pack(fill="both", expand=True, padx=16, pady=16)

        if not mode_create_empty:
            ctk.CTkLabel(body, text="1. Chọn thư mục trên máy cần bảo mật:", text_color=C["text"], font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=16, pady=(14, 4))
            row = ctk.CTkFrame(body, fg_color="transparent")
            row.pack(fill="x", padx=16)
            ctk.CTkEntry(row, textvariable=self.var_src, placeholder_text="Đường dẫn thư mục gốc...", height=34).pack(side="left", fill="x", expand=True, padx=(0, 8))
            ctk.CTkButton(row, text="Chọn...", width=84, height=34, command=self._browse).pack(side="right")

        ctk.CTkLabel(body, text="Tên hiển thị trong Vault:", text_color=C["text"], font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=16, pady=(12, 4))
        ctk.CTkEntry(body, textvariable=self.var_name, placeholder_text="VD: DuAn_Mat_2026", height=34).pack(fill="x", padx=16)

        ctk.CTkLabel(body, text="Chế độ lưu trữ (Kiến trúc Lai):", text_color=C["text"], font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=16, pady=(14, 4))
        ctk.CTkRadioButton(
            body,
            text="Ổ đĩa ảo WebDAV (Mở/khóa <1s, 0% file rõ trên ổ đĩa, phù hợp file < 50MB)",
            variable=self.var_mode,
            value=MODE_WEBDAV,
            text_color=C["text"],
        ).pack(anchor="w", padx=20, pady=3)
        ctk.CTkRadioButton(
            body,
            text="Vault cục bộ - Local Sync (Cho dự án nặng, file > 50MB, nhiều file code)",
            variable=self.var_mode,
            value=MODE_LOCAL_SYNC,
            text_color=C["text"],
        ).pack(anchor="w", padx=20, pady=3)

        if not mode_create_empty:
            ctk.CTkCheckBox(
                body,
                text="Xóa vĩnh viễn (không thể phục hồi) thư mục gốc sau khi nạp vào Vault",
                variable=self.var_shred_src,
                text_color=C["warning"],
            ).pack(anchor="w", padx=20, pady=(12, 4))

        btn_row = ctk.CTkFrame(body, fg_color="transparent")
        btn_row.pack(fill="x", padx=16, pady=(18, 14))
        ctk.CTkButton(btn_row, text="Hủy", fg_color=C["card"], hover_color=C["border"], width=100, command=self.destroy).pack(side="right", padx=(8, 0))
        ctk.CTkButton(btn_row, text="Xác nhận thêm", fg_color=C["accent"], hover_color=C["accent_hover"], text_color="#000000", width=140, command=self._submit).pack(side="right")

    def _browse(self) -> None:
        folder = filedialog.askdirectory(title="Chọn thư mục cần đưa vào PrivateVault")
        if folder:
            self.var_src.set(folder)
            if not self.var_name.get().strip():
                self.var_name.set(Path(folder).name)

    def _submit(self) -> None:
        name = self.var_name.get().strip()
        src_str = self.var_src.get().strip()
        if not self._create_empty:
            if not src_str or not Path(src_str).is_dir():
                messagebox.showwarning("Thiếu thư mục", "Vui lòng chọn một thư mục hợp lệ.", parent=self)
                return
            if not name:
                name = Path(src_str).name
        else:
            if not name:
                messagebox.showwarning("Thiếu tên", "Vui lòng nhập tên cho folder mới.", parent=self)
                return

        if not self._create_empty and self.var_shred_src.get():
            ok = messagebox.askyesno(
                "Xác nhận xóa bản gốc",
                f"Sau khi mã hóa vào Vault, thư mục gốc:\n{src_str}\n\nsẽ bị XÓA VĨNH VIỄN không thể phục hồi.\nBạn chắc chắn muốn tiếp tục?",
                parent=self,
            )
            if not ok:
                return

        self.result = {
            "source_dir": Path(src_str) if (not self._create_empty and src_str) else None,
            "name": name,
            "mode": self.var_mode.get(),
            "shred_source": bool(self.var_shred_src.get()) if not self._create_empty else False,
        }
        self.destroy()


# ---------------------------------------------------------------------------
# Main Application
# ---------------------------------------------------------------------------

class PrivateVaultApp:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.vault = VaultEngine(BASE_DIR)
        self.policy = PolicyManager(self.vault.vault_dir)
        self.webdav = WebDAVMountManager(self.vault)

        self.root = ctk.CTk()
        self.root.title("PrivateVault — Bảo Mật Folder Portable")
        self.root.geometry("980x650")
        self.root.minsize(860, 560)
        self.root.configure(fg_color=C["bg"])
        self.root.protocol("WM_DELETE_WINDOW", self._on_close_window)

        self._tray_icon: Optional[pystray.Icon] = None
        self._tray_thread: Optional[threading.Thread] = None
        self._is_exiting = False
        self._busy = False

        self.container = ctk.CTkFrame(self.root, fg_color=C["bg"])
        self.container.pack(fill="both", expand=True)

        # Kiểm tra lịch hẹn giờ xóa NGAY KHI KHỞI ĐỘNG (trước cả màn hình nhập mật khẩu)
        self._check_startup_scheduled_wipe()

        self._render_locked_screen()
        self._start_tray()
        self._schedule_background_tick()

    # ------------------------------------------------------------------
    # Startup & Background Policy Monitor
    # ------------------------------------------------------------------

    def _check_startup_scheduled_wipe(self) -> None:
        if self.vault.is_initialized and self.policy.is_scheduled_wipe_due():
            self._execute_full_wipe("Đến hạn Hẹn giờ xóa (kích hoạt lúc khởi động ứng dụng)")

    def _schedule_background_tick(self) -> None:
        if self._is_exiting:
            return
        try:
            # 1. Kiểm tra hẹn giờ xóa
            if self.vault.is_initialized and self.policy.is_scheduled_wipe_due():
                self._execute_full_wipe("Đến hạn Hẹn giờ xóa tự động")
                messagebox.showwarning(
                    "PrivateVault — Đã tự hủy dữ liệu",
                    "Đã đến mốc Hẹn giờ xóa!\nToàn bộ dữ liệu & khóa mã hóa đã bị tiêu hủy vĩnh viễn không thể phục hồi.",
                )
            # 2. Kiểm tra phiên mở khóa (tự khóa khi hết số giờ cài đặt hoặc sang ngày mới 00:00)
            elif self.vault.is_unlocked and self.policy.is_session_expired():
                self._lock_vault(reason=self.policy.session_expire_reason())

            # 3. Cập nhật đồng hồ đếm ngược phiên & hẹn giờ xóa trên UI nếu có
            self._refresh_countdown_labels()
        except Exception:
            pass
        self.root.after(5000, self._schedule_background_tick)

    def _refresh_countdown_labels(self) -> None:
        if hasattr(self, "lbl_session") and self.lbl_session.winfo_exists() and self.vault.is_unlocked:
            drive_label = self.webdav.drive_letter or "UNC"
            self.lbl_session.configure(text=f"{self.policy.session_status_str()}  |  Ổ ảo: {drive_label}")
        txt = self.policy.remaining_until_wipe_str()
        if hasattr(self, "lbl_lock_timer") and self.lbl_lock_timer.winfo_exists():
            if self.policy.state.scheduled_wipe_enabled:
                self.lbl_lock_timer.configure(text=f"⏰ Hẹn giờ tự hủy: {txt} ({self.policy.state.scheduled_wipe_at})")
            else:
                self.lbl_lock_timer.configure(text="")
        if hasattr(self, "lbl_policy_timer") and self.lbl_policy_timer.winfo_exists():
            if self.policy.state.scheduled_wipe_enabled:
                self.lbl_policy_timer.configure(
                    text=f"ĐANG BẬT — {txt} (Mốc: {self.policy.state.scheduled_wipe_at})",
                    text_color=C["danger"],
                )
            else:
                self.lbl_policy_timer.configure(text="Đang tắt", text_color=C["muted"])

    # ------------------------------------------------------------------
    # System Tray
    # ------------------------------------------------------------------

    def _start_tray(self) -> None:
        try:
            menu = pystray.Menu(
                pystray.MenuItem("Mở PrivateVault", lambda icon, item: self.root.after(0, self._show_window), default=True),
                pystray.MenuItem("Khóa ngay (Lock)", lambda icon, item: self.root.after(0, lambda: self._lock_vault("Đã khóa thủ công từ khay hệ thống."))),
                pystray.Menu.SEPARATOR,
                pystray.MenuItem("Thoát & Khóa an toàn", lambda icon, item: self.root.after(0, self._exit_app)),
            )
            self._tray_icon = pystray.Icon(
                "PrivateVault",
                create_tray_icon_image(locked=not self.vault.is_unlocked),
                "PrivateVault (Đang khóa)",
                menu,
            )
            self._tray_thread = threading.Thread(target=self._tray_icon.run, daemon=True)
            self._tray_thread.start()
        except Exception:
            self._tray_icon = None

    def _update_tray_status(self) -> None:
        if self._tray_icon is None:
            return
        try:
            locked = not self.vault.is_unlocked
            self._tray_icon.icon = create_tray_icon_image(locked=locked)
            self._tray_icon.title = (
                "PrivateVault (Đang khóa)"
                if locked
                else f"PrivateVault (Đã mở khóa {self.policy.unlocked_date})"
            )
        except Exception:
            pass

    def _show_window(self) -> None:
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()

    def _hide_to_tray(self) -> None:
        self.root.withdraw()

    def _on_close_window(self) -> None:
        if self.vault.is_unlocked and self._tray_icon is not None:
            choice = messagebox.askyesnocancel(
                "PrivateVault đang mở khóa",
                "Chọn [Yes] để thu nhỏ xuống khay hệ thống (giữ phiên 1 lần/ngày đến 00:00).\n"
                "Chọn [No] để KHÓA CỨNG và thoát hoàn toàn ứng dụng.\n"
                "Chọn [Cancel] để quay lại.",
            )
            if choice is True:
                self._hide_to_tray()
            elif choice is False:
                self._exit_app()
            return
        self._exit_app()

    def _exit_app(self) -> None:
        if self._is_exiting:
            return
        self._is_exiting = True
        try:
            self.webdav.unmount_and_stop()
        except Exception:
            pass
        try:
            if self.vault.is_unlocked:
                self.vault.lock()
                self.policy.mark_locked()
        except Exception:
            pass
        try:
            if self._tray_icon is not None:
                self._tray_icon.stop()
        except Exception:
            pass
        try:
            self.root.quit()
            self.root.destroy()
        except Exception:
            pass
        sys.exit(0)

    # ------------------------------------------------------------------
    # Screen Helpers
    # ------------------------------------------------------------------

    def _clear_container(self) -> None:
        for child in self.container.winfo_children():
            child.destroy()

    # ------------------------------------------------------------------
    # Screen 1: Locked / First-Time Setup
    # ------------------------------------------------------------------

    def _render_locked_screen(self, status_msg: str = "") -> None:
        self._clear_container()
        self._update_tray_status()

        card = ctk.CTkFrame(self.container, fg_color=C["panel"], corner_radius=16, width=480)
        card.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(card, text="🔒 PrivateVault", font=("Segoe UI", 26, "bold"), text_color=C["accent"]).pack(padx=36, pady=(28, 4))

        if not self.vault.is_initialized:
            ctk.CTkLabel(
                card,
                text="Khởi tạo mật khẩu chính để bảo vệ các thư mục của bạn.\nKhông có mật khẩu sẽ không thể thấy hoặc mở dữ liệu.",
                font=("Segoe UI", 12),
                text_color=C["muted"],
                justify="center",
            ).pack(padx=32, pady=(0, 14))

            if self.policy.state.last_wipe_reason:
                ctk.CTkLabel(
                    card,
                    text=f"⚠️ Lần hủy dữ liệu gần nhất ({self.policy.state.last_wipe_at}):\n{self.policy.state.last_wipe_reason}",
                    font=("Segoe UI", 11, "bold"),
                    text_color=C["danger"],
                    justify="center",
                ).pack(padx=24, pady=(0, 12))

            self.entry_pw1 = ctk.CTkEntry(card, placeholder_text="Nhập mật khẩu chính (>= 4 ký tự)", show="•", width=340, height=40)
            self.entry_pw1.pack(padx=32, pady=6)
            self.entry_pw2 = ctk.CTkEntry(card, placeholder_text="Nhập lại mật khẩu chính", show="•", width=340, height=40)
            self.entry_pw2.pack(padx=32, pady=6)
            self.entry_pw2.bind("<Return>", lambda _e: self._handle_init_vault())

            self.lbl_lock_err = ctk.CTkLabel(card, text=status_msg, text_color=C["warning"], font=("Segoe UI", 12))
            self.lbl_lock_err.pack(padx=24, pady=(6, 4))

            ctk.CTkButton(
                card,
                text="Khởi tạo Vault & Mở khóa hôm nay",
                width=340,
                height=42,
                fg_color=C["accent"],
                hover_color=C["accent_hover"],
                text_color="#000000",
                font=("Segoe UI", 13, "bold"),
                command=self._handle_init_vault,
            ).pack(padx=32, pady=(8, 28))
            self.entry_pw1.focus_set()
        else:
            ctk.CTkLabel(
                card,
                text="Vault đang khóa cứng. Nhập mật khẩu 1 lần duy nhất cho hôm nay\nđể mở khóa và quản lý các thư mục bảo mật.",
                font=("Segoe UI", 12),
                text_color=C["muted"],
                justify="center",
            ).pack(padx=32, pady=(0, 14))

            self.entry_pw = ctk.CTkEntry(card, placeholder_text="Nhập mật khẩu để mở khóa...", show="•", width=340, height=42)
            self.entry_pw.pack(padx=32, pady=6)
            self.entry_pw.bind("<Return>", lambda _e: self._handle_unlock())

            self.lbl_lock_err = ctk.CTkLabel(card, text=status_msg, text_color=C["danger"], font=("Segoe UI", 12), justify="center")
            self.lbl_lock_err.pack(padx=24, pady=(6, 2))

            self.lbl_lock_timer = ctk.CTkLabel(card, text="", text_color=C["warning"], font=("Segoe UI", 11, "bold"))
            self.lbl_lock_timer.pack(padx=24, pady=(0, 8))
            self._refresh_countdown_labels()

            if self.policy.state.auto_wipe_on_fail and self.policy.state.failed_attempts > 0:
                self.lbl_lock_err.configure(
                    text=f"⚠️ Đã nhập sai {self.policy.state.failed_attempts}/{self.policy.state.max_failed_attempts} lần — quá ngưỡng sẽ tự xóa sạch dữ liệu!"
                )

            ctk.CTkButton(
                card,
                text="🔓 Mở khóa hôm nay",
                width=340,
                height=42,
                fg_color=C["accent"],
                hover_color=C["accent_hover"],
                text_color="#000000",
                font=("Segoe UI", 13, "bold"),
                command=self._handle_unlock,
            ).pack(padx=32, pady=(4, 28))
            self.entry_pw.focus_set()

    def _handle_init_vault(self) -> None:
        pw1 = self.entry_pw1.get()
        pw2 = self.entry_pw2.get()
        if len(pw1) < 4:
            self.lbl_lock_err.configure(text="Mật khẩu phải có ít nhất 4 ký tự.")
            return
        if pw1 != pw2:
            self.lbl_lock_err.configure(text="Mật khẩu nhập lại không khớp.")
            return
        try:
            self.vault.initialize_vault(pw1)
            self.policy.mark_unlocked_today()
            self.webdav.start_and_mount()
            self._render_main_screen()
        except Exception as exc:
            self.lbl_lock_err.configure(text=f"Lỗi khởi tạo: {exc}")

    def _handle_unlock(self) -> None:
        # Kiểm tra hẹn giờ xóa trước khi cho mở khóa
        if self.policy.is_scheduled_wipe_due():
            self._execute_full_wipe("Đến hạn Hẹn giờ xóa tự động")
            messagebox.showwarning("PrivateVault", "Đã quá mốc Hẹn giờ xóa! Toàn bộ dữ liệu đã bị hủy vĩnh viễn.")
            return

        pw = self.entry_pw.get()
        if not pw:
            self.lbl_lock_err.configure(text="Vui lòng nhập mật khẩu.")
            return

        if self.vault.unlock(pw):
            self.policy.mark_unlocked_today()
            ok, msg = self.webdav.start_and_mount()
            self._render_main_screen(banner_msg=msg if ok else f"Lưu ý ổ ảo: {msg}")
        else:
            self.entry_pw.delete(0, "end")
            fails, max_f, should_wipe = self.policy.record_failed_attempt()
            if should_wipe:
                self._execute_full_wipe(f"Nhập sai mật khẩu {fails}/{max_f} lần (Chế độ B)")
                messagebox.showerror(
                    "PrivateVault — TỰ HỦY DỮ LIỆU",
                    f"Bạn đã nhập sai mật khẩu {fails}/{max_f} lần!\nToàn bộ khóa mã hóa và dữ liệu đã bị XÓA VĨNH VIỄN không thể phục hồi.",
                )
            else:
                extra = (
                    f" (Sai {fails}/{max_f} lần — quá ngưỡng sẽ TỰ XÓA SẠCH!)"
                    if self.policy.state.auto_wipe_on_fail
                    else ""
                )
                self.lbl_lock_err.configure(text=f"Mật khẩu không đúng!{extra}")

    # ------------------------------------------------------------------
    # Screen 2: Main Unlocked Workspace
    # ------------------------------------------------------------------

    def _render_main_screen(self, banner_msg: str = "") -> None:
        self._clear_container()
        self._update_tray_status()

        # Top Header Bar
        header = ctk.CTkFrame(self.container, fg_color=C["panel"], corner_radius=0, height=62)
        header.pack(fill="x")
        header.pack_propagate(False)

        ctk.CTkLabel(header, text="🔓 PrivateVault", font=("Segoe UI", 18, "bold"), text_color=C["accent"]).pack(side="left", padx=(18, 12))

        drive_label = self.webdav.drive_letter or "UNC"
        self.lbl_session = ctk.CTkLabel(
            header,
            text=f"{self.policy.session_status_str()}  |  Ổ ảo: {drive_label}",
            font=("Segoe UI", 12),
            text_color=C["success"],
        )
        self.lbl_session.pack(side="left", padx=8)

        ctk.CTkButton(header, text="Thoát & Khóa", width=110, height=32, fg_color=C["card"], hover_color=C["danger"], command=self._exit_app).pack(side="right", padx=(6, 14))
        ctk.CTkButton(header, text="🔒 Khóa ngay", width=106, height=32, fg_color=C["warning"], hover_color="#D97706", text_color="#000000", command=lambda: self._lock_vault("Đã khóa thủ công.")).pack(side="right", padx=6)
        if self._tray_icon is not None:
            ctk.CTkButton(header, text="⬇ Thu nhỏ Tray", width=120, height=32, fg_color=C["card"], hover_color=C["border"], command=self._hide_to_tray).pack(side="right", padx=6)
        if self.webdav.drive_letter:
            ctk.CTkButton(header, text=f"📂 Mở ổ {self.webdav.drive_letter}\\", width=110, height=32, fg_color=C["accent"], hover_color=C["accent_hover"], text_color="#000000", command=lambda: open_in_explorer(f"{self.webdav.drive_letter}\\")).pack(side="right", padx=6)

        # Tabs
        tabs = ctk.CTkTabview(self.container, fg_color=C["bg"], segmented_button_fg_color=C["panel"], segmented_button_selected_color=C["accent"], segmented_button_selected_hover_color=C["accent_hover"])
        tabs.pack(fill="both", expand=True, padx=14, pady=(10, 8))
        tab_folders = tabs.add("📁 Quản lý Folder")
        tab_wipe = tabs.add("☠️ Thiết lập Xóa & Bảo mật")

        self._build_folders_tab(tab_folders)
        self._build_policy_tab(tab_wipe)

        # Status bar
        self.lbl_status = ctk.CTkLabel(
            self.container,
            text=banner_msg or "Sẵn sàng. Mọi thao tác trong ngày không cần nhập lại mật khẩu cho tới 00:00.",
            font=("Segoe UI", 11),
            text_color=C["muted"],
            anchor="w",
        )
        self.lbl_status.pack(fill="x", padx=18, pady=(0, 8))

    def _build_folders_tab(self, parent) -> None:
        toolbar = ctk.CTkFrame(parent, fg_color=C["panel"], corner_radius=10)
        toolbar.pack(fill="x", padx=4, pady=(4, 10))

        ctk.CTkButton(toolbar, text="+ Thêm Folder từ máy", fg_color=C["accent"], hover_color=C["accent_hover"], text_color="#000000", height=34, command=lambda: self._add_folder(False)).pack(side="left", padx=(10, 6), pady=8)
        ctk.CTkButton(toolbar, text="+ Tạo Folder rỗng", fg_color=C["card"], hover_color=C["border"], height=34, command=lambda: self._add_folder(True)).pack(side="left", padx=6, pady=8)
        ctk.CTkButton(toolbar, text="📂 Mở", fg_color=C["card"], hover_color=C["border"], width=86, height=34, command=self._open_selected_folder).pack(side="left", padx=6, pady=8)
        ctk.CTkButton(toolbar, text="🔄 Đổi chế độ", fg_color=C["card"], hover_color=C["border"], width=116, height=34, command=self._switch_selected_mode).pack(side="left", padx=6, pady=8)
        ctk.CTkButton(toolbar, text="📤 Gỡ & Xuất", fg_color=C["card"], hover_color=C["border"], width=110, height=34, command=self._export_remove_selected).pack(side="left", padx=6, pady=8)
        ctk.CTkButton(toolbar, text="🗑 Xóa vĩnh viễn", fg_color=C["danger"], hover_color=C["danger_hover"], width=130, height=34, command=self._shred_selected_folder).pack(side="right", padx=(6, 10), pady=8)
        ctk.CTkButton(toolbar, text="↻ Làm mới", fg_color=C["card"], hover_color=C["border"], width=90, height=34, command=self._refresh_folder_tree).pack(side="right", padx=6, pady=8)

        # C-Engine ttk.Treeview Dark Mode (Zero-Lag)
        tree_frame = ctk.CTkFrame(parent, fg_color=C["panel"], corner_radius=10)
        tree_frame.pack(fill="both", expand=True, padx=4, pady=(0, 4))

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "PV.Treeview",
            background=C["panel"],
            foreground=C["text"],
            fieldbackground=C["panel"],
            rowheight=32,
            borderwidth=0,
            font=("Segoe UI", 10),
        )
        style.configure(
            "PV.Treeview.Heading",
            background=C["card"],
            foreground=C["accent"],
            font=("Segoe UI", 10, "bold"),
            borderwidth=0,
        )
        style.map("PV.Treeview", background=[("selected", "#0369A1")], foreground=[("selected", "#FFFFFF")])

        cols = ("name", "mode", "files", "size", "access")
        self.tree = ttk.Treeview(tree_frame, columns=cols, show="headings", style="PV.Treeview", selectmode="browse")
        self.tree.heading("name", text="Tên Folder")
        self.tree.heading("mode", text="Chế độ")
        self.tree.heading("files", text="Số tệp")
        self.tree.heading("size", text="Dung lượng")
        self.tree.heading("access", text="Đường dẫn truy cập hiện tại")

        self.tree.column("name", width=190, anchor="w")
        self.tree.column("mode", width=140, anchor="center")
        self.tree.column("files", width=80, anchor="center")
        self.tree.column("size", width=100, anchor="e")
        self.tree.column("access", width=360, anchor="w")

        sb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side="left", fill="both", expand=True, padx=(8, 0), pady=8)
        sb.pack(side="right", fill="y", padx=(0, 6), pady=8)
        self.tree.bind("<Double-1>", lambda _e: self._open_selected_folder())

        self._refresh_folder_tree()

    def _build_policy_tab(self, parent) -> None:
        scroll = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=4, pady=4)

        # --- Khối 0: Thiết lập thời gian tự động khóa (1 lần/ngày hoặc sau mỗi X giờ) ---
        card_s = ctk.CTkFrame(scroll, fg_color=C["panel"], corner_radius=12)
        card_s.pack(fill="x", padx=6, pady=6)
        ctk.CTkLabel(card_s, text="⏱️ Thiết Lập Tự Động Khóa (Yêu Cầu Nhập Lại Mật Khẩu)", font=("Segoe UI", 14, "bold"), text_color=C["accent"]).pack(anchor="w", padx=16, pady=(12, 6))

        self.var_session_mode = tk.StringVar(value=self.policy.state.session_mode)
        h_val = self.policy.state.session_timeout_hours
        self.var_session_hours = tk.StringVar(value=f"{int(h_val)}" if h_val == int(h_val) else f"{h_val:g}")

        ctk.CTkRadioButton(
            card_s,
            text="Chỉ nhập mật khẩu 1 lần mỗi ngày (tự động khóa lúc 00:00)",
            variable=self.var_session_mode,
            value="daily",
            text_color=C["text"],
        ).pack(anchor="w", padx=20, pady=3)

        row_sh = ctk.CTkFrame(card_s, fg_color="transparent")
        row_sh.pack(fill="x", padx=20, pady=(4, 14))
        ctk.CTkRadioButton(
            row_sh,
            text="Tự động khóa sau mỗi:",
            variable=self.var_session_mode,
            value="hours",
            text_color=C["text"],
        ).pack(side="left")
        ctk.CTkEntry(row_sh, textvariable=self.var_session_hours, width=64, height=32).pack(side="left", padx=(6, 6))
        ctk.CTkLabel(row_sh, text="giờ", text_color=C["muted"]).pack(side="left", padx=(0, 10))
        for preset in ("1", "2", "4", "8"):
            ctk.CTkButton(
                row_sh,
                text=f"{preset}h",
                width=42,
                height=28,
                fg_color=C["card"],
                hover_color=C["border"],
                command=lambda p=preset: (self.var_session_mode.set("hours"), self.var_session_hours.set(p)),
            ).pack(side="left", padx=3)
        ctk.CTkButton(
            row_sh,
            text="Lưu tự khóa",
            width=110,
            height=32,
            fg_color=C["accent"],
            hover_color=C["accent_hover"],
            text_color="#000000",
            command=self._save_session_policy,
        ).pack(side="right")

        # --- Khối 1: Chế độ A (Xóa vĩnh viễn ngay lập tức) ---
        card_a = ctk.CTkFrame(scroll, fg_color=C["panel"], corner_radius=12, border_width=1, border_color=C["danger"])
        card_a.pack(fill="x", padx=6, pady=6)
        ctk.CTkLabel(card_a, text="☠️ Chế độ A — Xóa Sạch Toàn Bộ Dữ Liệu Ngay Lập Tức (Panic Wipe)", font=("Segoe UI", 14, "bold"), text_color=C["danger"]).pack(anchor="w", padx=16, pady=(12, 4))
        ctk.CTkLabel(
            card_a,
            text="Tiêu hủy vĩnh viễn Master Key (Crypto-Shredding 3 lượt) + xóa toàn bộ folder đã lưu.\nDữ liệu KHÔNG THỂ PHỤC HỒI bằng bất kỳ phần mềm cứu dữ liệu nào kể cả trên SSD.",
            font=("Segoe UI", 12),
            text_color=C["muted"],
            justify="left",
        ).pack(anchor="w", padx=16, pady=(0, 10))
        ctk.CTkButton(
            card_a,
            text="☠️ XÓA SẠCH TOÀN BỘ VAULT NGAY",
            fg_color=C["danger"],
            hover_color=C["danger_hover"],
            height=38,
            font=("Segoe UI", 13, "bold"),
            command=self._handle_panic_wipe,
        ).pack(anchor="w", padx=16, pady=(0, 14))

        # --- Khối 2: Chế độ B (Sai mật khẩu quá N lần tự hủy) ---
        card_b = ctk.CTkFrame(scroll, fg_color=C["panel"], corner_radius=12)
        card_b.pack(fill="x", padx=6, pady=6)
        ctk.CTkLabel(card_b, text="🛡️ Chế độ B — Tự Động Xóa Khi Nhập Sai Mật Khẩu", font=("Segoe UI", 14, "bold"), text_color=C["warning"]).pack(anchor="w", padx=16, pady=(12, 4))
        row_b = ctk.CTkFrame(card_b, fg_color="transparent")
        row_b.pack(fill="x", padx=16, pady=(4, 14))

        self.var_fail_wipe = tk.BooleanVar(value=self.policy.state.auto_wipe_on_fail)
        self.var_max_fails = tk.StringVar(value=str(self.policy.state.max_failed_attempts))

        ctk.CTkSwitch(row_b, text="Bật tự hủy khi nhập sai mật khẩu", variable=self.var_fail_wipe, text_color=C["text"]).pack(side="left", padx=(0, 18))
        ctk.CTkLabel(row_b, text="Số lần sai tối đa:", text_color=C["muted"]).pack(side="left", padx=(0, 6))
        ctk.CTkEntry(row_b, textvariable=self.var_max_fails, width=64, height=32).pack(side="left", padx=(0, 14))
        ctk.CTkButton(row_b, text="Lưu cài đặt B", width=120, height=32, fg_color=C["accent"], hover_color=C["accent_hover"], text_color="#000000", command=self._save_mode_b).pack(side="left")

        # --- Khối 3: Hẹn giờ xóa dữ liệu ---
        card_t = ctk.CTkFrame(scroll, fg_color=C["panel"], corner_radius=12)
        card_t.pack(fill="x", padx=6, pady=6)
        ctk.CTkLabel(card_t, text="⏰ Hẹn Giờ Xóa Sạch Dữ Liệu (Scheduled Auto-Wipe)", font=("Segoe UI", 14, "bold"), text_color=C["accent"]).pack(anchor="w", padx=16, pady=(12, 4))
        self.lbl_policy_timer = ctk.CTkLabel(card_t, text="", font=("Segoe UI", 12, "bold"))
        self.lbl_policy_timer.pack(anchor="w", padx=16, pady=(0, 8))
        self._refresh_countdown_labels()

        # Kiểu 1: Mốc ngày giờ cụ thể
        row_t1 = ctk.CTkFrame(card_t, fg_color="transparent")
        row_t1.pack(fill="x", padx=16, pady=4)
        ctk.CTkLabel(row_t1, text="Mốc ngày giờ (YYYY-MM-DD HH:MM):", text_color=C["text"], width=230, anchor="w").pack(side="left")
        default_dt = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
        self.var_wipe_dt = tk.StringVar(value=self.policy.state.scheduled_wipe_at[:16] if self.policy.state.scheduled_wipe_at else default_dt)
        ctk.CTkEntry(row_t1, textvariable=self.var_wipe_dt, width=180, height=32).pack(side="left", padx=(0, 10))
        ctk.CTkButton(row_t1, text="Đặt mốc ngày giờ", width=140, height=32, fg_color=C["warning"], hover_color="#D97706", text_color="#000000", command=self._set_schedule_datetime).pack(side="left")

        # Kiểu 2: Đếm ngược
        row_t2 = ctk.CTkFrame(card_t, fg_color="transparent")
        row_t2.pack(fill="x", padx=16, pady=(4, 14))
        ctk.CTkLabel(row_t2, text="Hoặc đếm ngược sau:", text_color=C["text"], width=230, anchor="w").pack(side="left")
        self.var_cd_days = tk.StringVar(value="0")
        self.var_cd_hours = tk.StringVar(value="1")
        self.var_cd_mins = tk.StringVar(value="0")
        ctk.CTkEntry(row_t2, textvariable=self.var_cd_days, width=50, height=32).pack(side="left")
        ctk.CTkLabel(row_t2, text="ngày", text_color=C["muted"]).pack(side="left", padx=(4, 10))
        ctk.CTkEntry(row_t2, textvariable=self.var_cd_hours, width=50, height=32).pack(side="left")
        ctk.CTkLabel(row_t2, text="giờ", text_color=C["muted"]).pack(side="left", padx=(4, 10))
        ctk.CTkEntry(row_t2, textvariable=self.var_cd_mins, width=50, height=32).pack(side="left")
        ctk.CTkLabel(row_t2, text="phút", text_color=C["muted"]).pack(side="left", padx=(4, 12))
        ctk.CTkButton(row_t2, text="Bật đếm ngược", width=120, height=32, fg_color=C["warning"], hover_color="#D97706", text_color="#000000", command=self._set_schedule_countdown).pack(side="left", padx=(0, 8))
        ctk.CTkButton(row_t2, text="Hủy hẹn giờ", width=105, height=32, fg_color=C["card"], hover_color=C["border"], command=self._cancel_schedule).pack(side="left")

        # --- Khối 4: Đổi mật khẩu chính ---
        card_pw = ctk.CTkFrame(scroll, fg_color=C["panel"], corner_radius=12)
        card_pw.pack(fill="x", padx=6, pady=6)
        ctk.CTkLabel(card_pw, text="🔑 Đổi Mật Khẩu Chính", font=("Segoe UI", 14, "bold"), text_color=C["text"]).pack(anchor="w", padx=16, pady=(12, 6))
        row_pw = ctk.CTkFrame(card_pw, fg_color="transparent")
        row_pw.pack(fill="x", padx=16, pady=(0, 14))
        self.ent_old_pw = ctk.CTkEntry(row_pw, placeholder_text="Mật khẩu hiện tại", show="•", width=180, height=32)
        self.ent_old_pw.pack(side="left", padx=(0, 8))
        self.ent_new_pw1 = ctk.CTkEntry(row_pw, placeholder_text="Mật khẩu mới", show="•", width=180, height=32)
        self.ent_new_pw1.pack(side="left", padx=(0, 8))
        self.ent_new_pw2 = ctk.CTkEntry(row_pw, placeholder_text="Nhập lại mật khẩu mới", show="•", width=180, height=32)
        self.ent_new_pw2.pack(side="left", padx=(0, 10))
        ctk.CTkButton(row_pw, text="Đổi mật khẩu", width=120, height=32, fg_color=C["accent"], hover_color=C["accent_hover"], text_color="#000000", command=self._handle_change_password).pack(side="left")

    # ------------------------------------------------------------------
    # Folder Actions
    # ------------------------------------------------------------------

    def _set_status(self, text: str) -> None:
        if hasattr(self, "lbl_status") and self.lbl_status.winfo_exists():
            self.lbl_status.configure(text=text)

    def _refresh_folder_tree(self) -> None:
        if not hasattr(self, "tree") or not self.tree.winfo_exists():
            return
        for item in self.tree.get_children():
            self.tree.delete(item)
        if not self.vault.is_unlocked:
            return
        for fid, mf in sorted(self.vault.folders.items(), key=lambda x: x[1].name.lower()):
            store = self.vault.get_store(fid)
            fcount, fbytes = store.stats()
            if mf.mode == MODE_WEBDAV:
                mode_label = "Ổ ảo WebDAV"
                access = self.webdav.get_folder_access_path(mf.name) or "(Chưa gắn ổ)"
            else:
                mode_label = "Vault cục bộ"
                wp = self.vault.get_local_work_path(fid)
                access = str(wp) if wp else "(Đang đồng bộ)"
            self.tree.insert("", "end", iid=fid, values=(mf.name, mode_label, fcount, format_size(fbytes), access))

    def _get_selected_folder_id(self) -> Optional[str]:
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Chưa chọn folder", "Vui lòng chọn một folder trong danh sách trước.")
            return None
        return sel[0]

    def _add_folder(self, create_empty: bool) -> None:
        if self._busy:
            return
        dlg = AddFolderDialog(self.root, mode_create_empty=create_empty)
        self.root.wait_window(dlg)
        if not dlg.result:
            return

        data = dlg.result
        self._busy = True
        self._set_status(f"Đang mã hóa và thêm folder '{data['name']}'...")

        def _worker():
            try:
                mf, fcount, total_b, warnings = self.vault.add_folder(
                    source_dir=data["source_dir"],
                    name=data["name"],
                    mode=data["mode"],
                    shred_source=data["shred_source"],
                )
                def _done():
                    self._busy = False
                    self._refresh_folder_tree()
                    self._set_status(f"Đã thêm '{mf.name}' ({fcount} tệp, {format_size(total_b)}).")
                    if warnings:
                        messagebox.showwarning("Lưu ý sau khi thêm folder", "\n\n".join(warnings))
                self.root.after(0, _done)
            except Exception as exc:
                def _err():
                    self._busy = False
                    self._set_status("Thêm folder thất bại.")
                    messagebox.showerror("Lỗi thêm folder", str(exc))
                self.root.after(0, _err)

        threading.Thread(target=_worker, daemon=True).start()

    def _open_selected_folder(self) -> None:
        fid = self._get_selected_folder_id()
        if not fid:
            return
        mf = self.vault.folders.get(fid)
        if not mf:
            return
        if mf.mode == MODE_WEBDAV:
            path_str = self.webdav.get_folder_access_path(mf.name)
        else:
            wp = self.vault.get_local_work_path(fid)
            path_str = str(wp) if wp else None
        if path_str:
            open_in_explorer(path_str)
        else:
            messagebox.showwarning("Chưa sẵn sàng", "Không xác định được đường dẫn mở cho folder này.")

    def _switch_selected_mode(self) -> None:
        fid = self._get_selected_folder_id()
        if not fid:
            return
        mf = self.vault.folders.get(fid)
        if not mf:
            return
        new_mode = MODE_LOCAL_SYNC if mf.mode == MODE_WEBDAV else MODE_WEBDAV
        new_label = "Vault cục bộ (Local Sync)" if new_mode == MODE_LOCAL_SYNC else "Ổ ảo WebDAV"
        if not messagebox.askyesno("Đổi chế độ folder", f"Chuyển folder '{mf.name}' sang chế độ:\n{new_label}?"):
            return
        try:
            warnings = self.vault.switch_folder_mode(fid, new_mode)
            self._refresh_folder_tree()
            self._set_status(f"Đã chuyển '{mf.name}' sang {new_label}.")
            if warnings:
                messagebox.showwarning("Lưu ý", "\n".join(warnings))
        except Exception as exc:
            messagebox.showerror("Lỗi đổi chế độ", str(exc))

    def _export_remove_selected(self) -> None:
        fid = self._get_selected_folder_id()
        if not fid:
            return
        mf = self.vault.folders.get(fid)
        if not mf:
            return
        initial_dir = ""
        if mf.original_path:
            orig = Path(mf.original_path)
            if orig.exists():
                initial_dir = str(orig)
            elif orig.parent.exists():
                initial_dir = str(orig.parent)
        dst = filedialog.askdirectory(
            title=f"Chọn thư mục đích để giải mã trực tiếp các tệp của '{mf.name}' vào đó",
            initialdir=initial_dir or None,
        )
        if not dst:
            return
        if not messagebox.askyesno(
            "Xác nhận gỡ khỏi Vault",
            f"Giải mã và chuyển trực tiếp các tệp của '{mf.name}' vào:\n{dst}\n(không tạo lồng thêm thư mục '{mf.name}')\nvà gỡ khỏi PrivateVault?",
        ):
            return
        try:
            out_dir = self.vault.export_and_remove_folder(fid, Path(dst))
            self._refresh_folder_tree()
            self._set_status(f"Đã xuất trực tiếp các tệp của '{mf.name}' ra {out_dir}")
            messagebox.showinfo("Hoàn tất", f"Đã chuyển toàn bộ tệp ra:\n{out_dir}")
        except Exception as exc:
            messagebox.showerror("Lỗi xuất dữ liệu", str(exc))

    def _shred_selected_folder(self) -> None:
        fid = self._get_selected_folder_id()
        if not fid:
            return
        mf = self.vault.folders.get(fid)
        if not mf:
            return
        confirm = ctk.CTkInputDialog(
            text=f"CẢNH BÁO: Thao tác này sẽ XÓA VĨNH VIỄN không thể phục hồi folder:\n'{mf.name}'\n\nNhập chính xác chữ XOA để xác nhận:",
            title="Xóa vĩnh viễn Folder (Chế độ A)",
        ).get_input()
        if confirm != "XOA":
            return
        errs = self.vault.shred_folder(fid)
        self._refresh_folder_tree()
        if errs:
            messagebox.showwarning("Hoàn tất kèm cảnh báo", f"Đã hủy khóa & chỉ mục của '{mf.name}', nhưng có {len(errs)} mục đang bị khóa bởi tiến trình khác.")
        else:
            self._set_status(f"Đã xóa vĩnh viễn không thể phục hồi folder '{mf.name}'.")

    # ------------------------------------------------------------------
    # Policy & Wipe Actions
    # ------------------------------------------------------------------

    def _lock_vault(self, reason: str = "") -> None:
        self.webdav.unmount_and_stop()
        warnings = self.vault.lock()
        self.policy.mark_locked()
        msg = reason
        if warnings:
            msg = f"{reason}\nLưu ý: {warnings[0]}" if reason else warnings[0]
        self._render_locked_screen(status_msg=msg)

    def _execute_full_wipe(self, reason: str) -> None:
        self.webdav.unmount_and_stop()
        self.vault.secure_wipe_all()
        self.policy.record_wipe_executed(reason)
        self._render_locked_screen(status_msg=f"ĐÃ XÓA SẠCH TOÀN BỘ DỮ LIỆU: {reason}")

    def _handle_panic_wipe(self) -> None:
        confirm = ctk.CTkInputDialog(
            text="CẢNH BÁO CỰC KỲ NGUY HIỂM!\n\nToàn bộ khóa mã hóa và TẤT CẢ folder trong PrivateVault sẽ bị XÓA VĨNH VIỄN không thể phục hồi.\n\nNhập chính xác: XOA VINH VIEN",
            title="Xác nhận Hủy Toàn Bộ Vault (Chế độ A)",
        ).get_input()
        if confirm != "XOA VINH VIEN":
            return
        self._execute_full_wipe("Người dùng kích hoạt Xóa sạch thủ công (Chế độ A)")
        messagebox.showinfo("Hoàn tất", "Đã tiêu hủy toàn bộ khóa mã hóa và dữ liệu không thể phục hồi.")

    def _save_session_policy(self) -> None:
        mode = self.var_session_mode.get()
        hours = 1.0
        if mode == "hours":
            try:
                hours = float(self.var_session_hours.get().strip().replace(",", "."))
                if hours <= 0 or hours > 720:
                    raise ValueError
            except ValueError:
                messagebox.showwarning("Giá trị không hợp lệ", "Số giờ tự khóa phải là số dương (VD: 0.5, 1, 2, 4, tối đa 720 giờ).")
                return
        self.policy.configure_session_policy(mode, hours)
        # Đặt lại mốc bắt đầu phiên hiện tại từ bây giờ nếu đang mở khóa để tránh khóa đột ngột ngay khi vừa đổi
        if self.vault.is_unlocked:
            self.policy.mark_unlocked_today()
        self._refresh_countdown_labels()
        desc = f"Tự động khóa sau mỗi {hours:g} giờ" if mode == "hours" else "1 lần mỗi ngày (tự khóa lúc 00:00)"
        self._set_status(f"Đã lưu chính sách tự khóa: {desc}.")
        messagebox.showinfo("Đã lưu", f"Chính sách tự động khóa:\n{desc}")

    def _save_mode_b(self) -> None:
        try:
            n = int(self.var_max_fails.get().strip())
            if n < 1 or n > 50:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Giá trị không hợp lệ", "Số lần sai tối đa phải là số nguyên từ 1 đến 50.")
            return
        self.policy.configure_fail_wipe(self.var_fail_wipe.get(), n)
        status = f"BẬT (tự xóa sau {n} lần sai)" if self.var_fail_wipe.get() else "TẮT"
        self._set_status(f"Đã lưu Chế độ B: {status}.")
        messagebox.showinfo("Đã lưu", f"Chế độ B (Tự xóa khi sai mật khẩu): {status}")

    def _set_schedule_datetime(self) -> None:
        raw = self.var_wipe_dt.get().strip()
        try:
            target = datetime.strptime(raw, "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showwarning("Sai định dạng", "Vui lòng nhập đúng định dạng YYYY-MM-DD HH:MM (VD: 2026-12-01 18:00).")
            return
        if target <= datetime.now():
            messagebox.showwarning("Mốc thời gian không hợp lệ", "Mốc hẹn giờ xóa phải lớn hơn thời gian hiện tại.")
            return
        if not messagebox.askyesno("Xác nhận hẹn giờ xóa", f"Toàn bộ dữ liệu trong Vault sẽ TỰ ĐỘNG XÓA VĨNH VIỄN vào lúc:\n{target.strftime('%Y-%m-%d %H:%M:00')}\n\nBạn chắc chắn muốn kích hoạt?"):
            return
        self.policy.set_scheduled_wipe_at(target)
        self._refresh_countdown_labels()
        self._set_status(f"Đã bật Hẹn giờ xóa lúc {target.strftime('%Y-%m-%d %H:%M:00')}.")

    def _set_schedule_countdown(self) -> None:
        try:
            d = float(self.var_cd_days.get().strip() or 0)
            h = float(self.var_cd_hours.get().strip() or 0)
            m = float(self.var_cd_mins.get().strip() or 0)
            if d < 0 or h < 0 or m < 0 or (d == 0 and h == 0 and m == 0):
                raise ValueError
        except ValueError:
            messagebox.showwarning("Sai giá trị", "Vui lòng nhập số ngày/giờ/phút hợp lệ (> 0).")
            return
        target = datetime.now() + timedelta(days=d, hours=h, minutes=m)
        if not messagebox.askyesno("Xác nhận đếm ngược tự hủy", f"Toàn bộ dữ liệu sẽ TỰ ĐỘNG XÓA VĨNH VIỄN vào lúc:\n{target.strftime('%Y-%m-%d %H:%M:%S')}\n\nBạn chắc chắn muốn kích hoạt?"):
            return
        self.policy.set_scheduled_wipe_countdown(days=d, hours=h, minutes=m)
        self._refresh_countdown_labels()
        self._set_status(f"Đã bật đếm ngược tự hủy -> {target.strftime('%Y-%m-%d %H:%M:%S')}.")

    def _cancel_schedule(self) -> None:
        self.policy.disable_scheduled_wipe()
        self._refresh_countdown_labels()
        self._set_status("Đã hủy lịch Hẹn giờ xóa.")

    def _handle_change_password(self) -> None:
        old_pw = self.ent_old_pw.get()
        new1 = self.ent_new_pw1.get()
        new2 = self.ent_new_pw2.get()
        if len(new1) < 4:
            messagebox.showwarning("Mật khẩu ngắn", "Mật khẩu mới phải có ít nhất 4 ký tự.")
            return
        if new1 != new2:
            messagebox.showwarning("Không khớp", "Mật khẩu mới nhập lại không khớp.")
            return
        if self.vault.change_password(old_pw, new1):
            self.ent_old_pw.delete(0, "end")
            self.ent_new_pw1.delete(0, "end")
            self.ent_new_pw2.delete(0, "end")
            messagebox.showinfo("Thành công", "Đã đổi mật khẩu chính thành công!")
        else:
            messagebox.showerror("Sai mật khẩu", "Mật khẩu hiện tại không đúng.")

    def run(self) -> None:
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self._exit_app()


def main() -> None:
    app = PrivateVaultApp()
    app.run()


if __name__ == "__main__":
    main()
