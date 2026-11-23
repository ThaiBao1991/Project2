import os
import sys
import site
import shutil
import importlib
import importlib.metadata
import json
import re
import unicodedata
import subprocess
import threading
import queue
import time
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Ensure UTF-8 console output safely on Windows (safe under pythonw as well)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# =========================================================================
# AUTO-INSTALL REQUIRED LIBRARIES (Windows Safe + Auto-Heal + Clean Exit)
# =========================================================================
REQUIRED_PACKAGES = {
    "customtkinter": "customtkinter>=5.2.0",
}
if sys.platform == "win32":
    REQUIRED_PACKAGES["win32com.client"] = "pywin32>=306"

PACKAGE_CONFLICTS = {}
FALLBACK_PACKAGES = {}
EXIT_MISSING_LIB_DIALOG = 2


def _pip_base_name(pip_spec: str) -> str:
    for sep in ("==", ">=", "<=", "~=", "!=", ">", "<", "["):
        if sep in pip_spec:
            pip_spec = pip_spec.split(sep, 1)[0]
    return pip_spec.strip()


def _quote_pip_spec(spec: str) -> str:
    """Wrap pip spec in double quotes so CMD/PowerShell won't treat '>' as file redirection."""
    if any(ch in spec for ch in '<>=!~ []"'):
        return f'"{spec}"'
    return spec


def _can_import_requirement(module_name: str) -> bool:
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        fallback = FALLBACK_PACKAGES.get(module_name)
        if fallback:
            try:
                importlib.import_module(fallback[0])
                return True
            except ImportError:
                return False
        return False


def _refresh_import_paths(in_venv: bool):
    """Refresh sys.path and process newly installed .pth files (e.g., pywin32.pth)."""
    candidate_dirs = []
    if not in_venv:
        try:
            user_site = site.getusersitepackages()
            if user_site and os.path.isdir(user_site):
                candidate_dirs.append(user_site)
        except Exception:
            pass
    try:
        for sp in site.getsitepackages():
            if sp and os.path.isdir(sp):
                candidate_dirs.append(sp)
    except Exception:
        pass
    for d in candidate_dirs:
        try:
            site.addsitedir(d)
        except Exception:
            if d not in sys.path:
                sys.path.append(d)
    importlib.invalidate_caches()


def _collect_site_dirs() -> list:
    dirs = []
    try:
        user_site = site.getusersitepackages()
        if user_site:
            dirs.append(user_site)
    except Exception:
        pass
    try:
        dirs.extend(site.getsitepackages())
    except Exception:
        pass
    for p in sys.path:
        if p and os.path.basename(p).lower() == "site-packages":
            dirs.append(p)
    seen = set()
    result = []
    for d in dirs:
        norm = os.path.normcase(os.path.abspath(d))
        if norm not in seen and os.path.isdir(d):
            seen.add(norm)
            result.append(d)
    return result


def _heal_windows_package_conflict(module_name: str, pip_spec: str) -> bool:
    """Auto-detect and heal Windows NTFS case-collision / conflicting package installs."""
    if sys.platform != "win32":
        return False

    top_pkg = module_name.split(".")[0]
    conflict_pkgs = list(PACKAGE_CONFLICTS.get(top_pkg, []))
    target_base = _pip_base_name(pip_spec)

    found_conflicts = []
    for pkg in conflict_pkgs:
        try:
            importlib.metadata.distribution(pkg)
            found_conflicts.append(pkg)
        except importlib.metadata.PackageNotFoundError:
            pass

    wrong_case_dirs = []
    for sp in _collect_site_dirs():
        try:
            for entry in os.listdir(sp):
                full_path = os.path.join(sp, entry)
                if os.path.isdir(full_path) and entry.lower() == top_pkg.lower() and entry != top_pkg:
                    wrong_case_dirs.append(full_path)
        except OSError:
            pass

    if not found_conflicts and not wrong_case_dirs:
        return False

    print(
        f"[*] Phát hiện xung đột gói/chữ hoa-thường cho '{top_pkg}' "
        f"(conflicts={found_conflicts}, dirs={wrong_case_dirs}). Đang tự động sửa..."
    )

    to_uninstall = []
    for pkg in found_conflicts + [target_base]:
        if pkg not in to_uninstall:
            try:
                importlib.metadata.distribution(pkg)
                to_uninstall.append(pkg)
            except importlib.metadata.PackageNotFoundError:
                pass

    if to_uninstall:
        subprocess.run(
            [sys.executable, "-m", "pip", "uninstall", "-y", *to_uninstall],
            check=False,
        )

    for bad_dir in wrong_case_dirs:
        if os.path.exists(bad_dir):
            shutil.rmtree(bad_dir, ignore_errors=True)

    importlib.invalidate_caches()
    return True


def _show_manual_install_dialog(missing_packages: list, error_detail=""):
    in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    user_flag = "" if in_venv else "--user "
    quoted_pkgs = " ".join(_quote_pip_spec(p) for p in missing_packages)
    cmd = f"python -m pip install {user_flag}{quoted_pkgs}"
    try:
        root = tk.Tk()
        root.withdraw()
        err_win = tk.Toplevel(root)
        err_win.title("Lỗi Thiếu Thư Viện — Tài Liệu Intelligence Hub")
        err_win.geometry("660x360")

        def close_dialog():
            try:
                root.quit()
            except Exception:
                pass
            try:
                root.destroy()
            except Exception:
                pass

        err_win.protocol("WM_DELETE_WINDOW", close_dialog)

        tk.Label(
            err_win,
            text="Ứng dụng thiếu thư viện cần thiết và không thể tự cài đặt.",
            fg="red",
            font=("Segoe UI", 11, "bold"),
        ).pack(pady=(14, 4))

        if error_detail:
            tk.Label(
                err_win,
                text=f"Chi tiết: {str(error_detail)[:240]}",
                fg="#555555",
                font=("Segoe UI", 9),
                wraplength=610,
                justify="left",
            ).pack(pady=(0, 6))

        tk.Label(
            err_win,
            text="Vui lòng sao chép lệnh dưới đây (đã bọc ngoặc kép chuẩn CMD/PowerShell) và dán vào Terminal:",
            font=("Segoe UI", 10),
        ).pack(pady=4)

        txt = tk.Text(err_win, height=4, width=74, font=("Consolas", 10))
        txt.pack(pady=8, padx=14)
        txt.insert(tk.END, cmd)
        txt.config(state="disabled")

        btn_frame = tk.Frame(err_win)
        btn_frame.pack(pady=10)

        copy_status = tk.Label(err_win, text="", fg="green", font=("Segoe UI", 9))
        copy_status.pack()

        def copy_cmd():
            err_win.clipboard_clear()
            err_win.clipboard_append(cmd)
            err_win.update()
            copy_status.config(text="Đã sao chép lệnh vào clipboard!")

        tk.Button(btn_frame, text="Sao chép lệnh", command=copy_cmd, width=16).pack(side=tk.LEFT, padx=8)
        tk.Button(btn_frame, text="Thoát ứng dụng", command=close_dialog, width=16).pack(side=tk.LEFT, padx=8)

        root.mainloop()
    except tk.TclError:
        print(f"[!] Không thể tự cài đặt thư viện ({error_detail}). Chạy thủ công: {cmd}", file=sys.stderr)


def check_and_install_packages():
    missing_items = [
        (mod, pip_spec)
        for mod, pip_spec in REQUIRED_PACKAGES.items()
        if not _can_import_requirement(mod)
    ]

    if not missing_items:
        return

    in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    pip_base_cmd = [sys.executable, "-m", "pip", "install"]
    if not in_venv:
        pip_base_cmd.append("--user")

    missing_specs = [pip_spec for _, pip_spec in missing_items]
    print(f"[*] Đang tự động cài đặt thư viện còn thiếu: {', '.join(missing_specs)}")

    try:
        for mod, pip_spec in missing_items:
            _heal_windows_package_conflict(mod, pip_spec)

        subprocess.check_call(pip_base_cmd + missing_specs)
        _refresh_import_paths(in_venv)

        still_missing = []
        for mod, pip_spec in missing_items:
            if _can_import_requirement(mod):
                continue
            fallback = FALLBACK_PACKAGES.get(mod)
            if fallback:
                fb_mod, fb_pip = fallback
                print(f"[*] '{mod}' vẫn chưa import được, thử gói dự phòng: {fb_pip}")
                try:
                    subprocess.check_call(pip_base_cmd + [fb_pip])
                    _refresh_import_paths(in_venv)
                    importlib.import_module(fb_mod)
                    continue
                except Exception:
                    pass
            still_missing.append(pip_spec)

        if still_missing:
            raise ImportError(f"Đã chạy pip nhưng vẫn không thể import: {', '.join(still_missing)}")

        print("[*] Cài đặt thư viện thành công!")
    except Exception as exc:
        _show_manual_install_dialog(missing_specs, exc)
        sys.exit(EXIT_MISSING_LIB_DIALOG)


# Check & auto-install dependencies BEFORE third-party imports
check_and_install_packages()

import customtkinter as ctk

def remove_accents(input_str):
    if not input_str:
        return ""
    nfkd = unicodedata.normalize('NFKD', str(input_str))
    return "".join([c for c in nfkd if not unicodedata.combining(c)]).lower()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')
CATALOG_PATH = os.path.join(BASE_DIR, 'tailieu_catalog.json')
GOVERNANCE_PATH = os.path.join(BASE_DIR, 'governance_catalog.json')

# Import sync engine & governance
try:
    from sync_engine import (
        load_module_config,
        save_module_config,
        sync_single_module,
        rebuild_consolidated_catalog,
        sync_all_modules
    )
except ImportError:
    pass

try:
    from governance_matrix import load_governance_matrix
except ImportError:
    def load_governance_matrix():
        return []

from storage_manager import (
    get_storage_root,
    is_custom_storage_root,
    resolve_local_path,
    resolve_master_excel_path,
    get_storage_summary,
    move_all_documents,
    relink_storage_root,
    verify_all_links,
    move_selected_documents,
    update_document_paths,
    delete_documents,
    is_file_exists,
    path_exists,
    to_long_path,
)

# Theme Colors (Catppuccin Mocha Dark Mode)
THEME = {
    'bg': '#1e1e2e',
    'surface0': '#181825',
    'surface1': '#313244',
    'surface2': '#45475a',
    'text': '#cdd6f4',
    'subtext': '#a6adc8',
    'blue': '#89b4fa',
    'green': '#a6e3a1',
    'yellow': '#f9e2af',
    'peach': '#fab387',
    'red': '#f38ba8',
    'mauve': '#cba6f7',
    'lavender': '#b4befe',
    'sky': '#89dceb',
    'card_hover': '#3b3d54'
}

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

PAGE_SIZE = 25  # Items per lazy load batch (Zero-Lag Rule)

class TaiLieuApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("TÀI LIỆU INTELLIGENCE HUB — Tra Cứu, Quản Trị & Mở Nhanh File")
        self.geometry("1320x840")
        self.minsize(1080, 700)
        
        # Data
        self.catalog = []
        self.governance_data = []
        self.modules = []
        
        # Search & Filter States
        self.filtered_docs = []
        self.current_page = 1
        self.current_sort = "MASTER_FIRST"
        self.current_view_mode = "card"  # "card" or "table"
        self._search_job = None
        self.sync_thread = None
        self.storage_thread = None
        self.storage_cancel_event = threading.Event()
        self._ui_queue = queue.Queue()
        self._is_closing = False
        self._storage_summary_running = False
        self._poll_job = None
        self._init_storage_job = None
        
        # Governance Filter States
        self.filtered_gov = []
        self.current_gov_page = 1
        self.selected_pillar = "Tất Cả"
        self._gov_search_job = None
        
        # Load Initial Data
        self.load_modules_list()
        self.load_catalog_data()
        self.load_gov_data()
        
        # Setup UI
        self.setup_ui()
        self.refresh_stats()
        self.refresh_gov_tier_labels()
        self.apply_search_filter()
        self.apply_gov_filter()
        self.protocol("WM_DELETE_WINDOW", self.on_app_close)
        self._poll_job = self.after(50, self._poll_ui_queue)
        self._init_storage_job = self.after(120, self.refresh_storage_ui_async)

    def ui_call(self, fn, *args, **kwargs):
        """Thread-safe dispatch to the Tk main thread via queue (avoids 'main thread is not in main loop')."""
        if not self._is_closing:
            self._ui_queue.put((fn, args, kwargs))

    def _poll_ui_queue(self):
        if self._is_closing:
            return
        try:
            while True:
                fn, args, kwargs = self._ui_queue.get_nowait()
                try:
                    fn(*args, **kwargs)
                except Exception as e:
                    print(f"UI callback error: {e}")
        except queue.Empty:
            pass
        if not self._is_closing:
            try:
                if self.winfo_exists():
                    self._poll_job = self.after(50, self._poll_ui_queue)
            except Exception:
                pass

    def on_app_close(self):
        if self._is_closing:
            return
        self._is_closing = True
        self.storage_cancel_event.set()
        for attr in ("_search_job", "_gov_search_job", "_poll_job", "_init_storage_job"):
            job = getattr(self, attr, None)
            if job:
                try:
                    self.after_cancel(job)
                except Exception:
                    pass
                setattr(self, attr, None)
        # Cancel ALL pending Tcl/CustomTkinter 'after' callbacks cleanly to prevent stderr TclError
        try:
            for after_id in self.tk.call("after", "info"):
                try:
                    self.after_cancel(after_id)
                except Exception:
                    pass
        except Exception:
            pass
        try:
            self.quit()
        except Exception:
            pass
        try:
            self.destroy()
        except Exception:
            pass
        
    def load_modules_list(self):
        self.modules = []
        if os.path.exists(CONFIGS_DIR):
            cfg_files = sorted([f for f in os.listdir(CONFIGS_DIR) if f.endswith('.json')])
            for fname in cfg_files:
                path = os.path.join(CONFIGS_DIR, fname)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        cfg = json.load(f)
                        self.modules.append({
                            'id': cfg.get('id'),
                            'name': cfg.get('name'),
                            'file': fname,
                            'path': path,
                            'last_sync': cfg.get('last_sync_time') or 'Chưa cập nhật',
                            'total_files': len(cfg.get('sync_state', {})),
                            'excel_remote': cfg.get('excel_remote', ''),
                            'excel_local_name': cfg.get('excel_local_name', ''),
                            'local_subfolder': cfg.get('local_subfolder', '')
                        })
                except Exception as e:
                    print(f"Error loading {fname}: {e}")

    def load_catalog_data(self):
        if os.path.exists(CATALOG_PATH):
            try:
                with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
                    self.catalog = json.load(f)
            except Exception as e:
                print(f"Error loading catalog: {e}")
                self.catalog = []
        else:
            self.catalog = []

    def load_gov_data(self):
        self.governance_data = load_governance_matrix()

    def setup_ui(self):
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # 1. Top Header
        self.create_header()
        
        # 2. Main Tabview
        self.tabview = ctk.CTkTabview(self, fg_color=THEME['surface0'])
        self.tabview.grid(row=1, column=0, padx=12, pady=(0, 12), sticky="nsew")
        
        self.tab_search = self.tabview.add("🔍 Tra Cứu & Mở Nhanh")
        self.tab_governance = self.tabview.add("🏛️ Ma Trận Quản Trị & Điều Hành")
        self.tab_sync = self.tabview.add("🔄 Cập Nhật & Quản Lý Đồng Bộ")
        self.tab_storage = self.tabview.add("📦 Quản Lý Kho & Di Chuyển")
        
        self.setup_tab_search()
        self.setup_tab_governance()
        self.setup_tab_sync()
        self.setup_tab_storage()

    def create_header(self):
        header_frame = ctk.CTkFrame(self, fg_color=THEME['surface0'], corner_radius=10)
        header_frame.grid(row=0, column=0, padx=12, pady=10, sticky="ew")
        header_frame.grid_columnconfigure(1, weight=1)
        
        title_box = ctk.CTkFrame(header_frame, fg_color="transparent")
        title_box.grid(row=0, column=0, padx=12, pady=8, sticky="w")
        
        lbl_title = ctk.CTkLabel(
            title_box, 
            text="📚 TÀI LIỆU INTELLIGENCE HUB",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=THEME['blue']
        )
        lbl_title.pack(anchor="w")
        
        lbl_sub = ctk.CTkLabel(
            title_box,
            text="Tra Cứu Tốc Độ Cao • Ma Trận Quản Trị Điều Hành • Tải Vi Sai Thông Minh • 100% Tiếng Việt",
            font=ctk.CTkFont(size=12),
            text_color=THEME['subtext']
        )
        lbl_sub.pack(anchor="w")

        storage_row = ctk.CTkFrame(title_box, fg_color="transparent")
        storage_row.pack(anchor="w", pady=(3, 0))

        self.lbl_header_storage = ctk.CTkLabel(
            storage_row,
            text="💾 Kho PDF: ...",
            font=ctk.CTkFont(size=11),
            text_color=THEME['sky']
        )
        self.lbl_header_storage.pack(side="left")

        ctk.CTkButton(
            storage_row,
            text="📁 Mở Kho",
            width=68,
            height=22,
            font=ctk.CTkFont(size=10),
            fg_color=THEME['surface1'],
            hover_color=THEME['surface2'],
            text_color=THEME['text'],
            command=self.open_current_storage_folder
        ).pack(side="left", padx=(8, 4))

        ctk.CTkButton(
            storage_row,
            text="📦 Đổi / Quản Lý Kho",
            width=118,
            height=22,
            font=ctk.CTkFont(size=10, weight="bold"),
            fg_color=THEME['surface2'],
            hover_color=THEME['card_hover'],
            text_color=THEME['yellow'],
            command=lambda: self.tabview.set("📦 Quản Lý Kho & Di Chuyển")
        ).pack(side="left")
        
        # Quick Stats Badges
        self.stats_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        self.stats_frame.grid(row=0, column=1, padx=12, pady=8, sticky="e")
        
        self.lbl_stat_total = self.create_badge(self.stats_frame, "Tổng Tài Liệu", "0", THEME['blue'])
        self.lbl_stat_master = self.create_badge(self.stats_frame, "👑 Hồ Sơ Nguồn", "0", THEME['yellow'])
        self.lbl_stat_valid = self.create_badge(self.stats_frame, "Hiệu Lực", "0", THEME['green'])
        self.lbl_stat_canceled = self.create_badge(self.stats_frame, "Đã Hủy (Có Link)", "0", THEME['peach'])
        self.lbl_stat_local = self.create_badge(self.stats_frame, "Sẵn Sàng Offline", "0", THEME['lavender'])

    def create_badge(self, parent, label, value, color):
        f = ctk.CTkFrame(parent, fg_color=THEME['surface1'], corner_radius=8)
        f.pack(side="left", padx=4)
        
        lbl_v = ctk.CTkLabel(f, text=value, font=ctk.CTkFont(size=14, weight="bold"), text_color=color)
        lbl_v.pack(padx=8, pady=(3, 0))
        
        lbl_l = ctk.CTkLabel(f, text=label, font=ctk.CTkFont(size=10), text_color=THEME['subtext'])
        lbl_l.pack(padx=8, pady=(0, 3))
        return lbl_v

    def refresh_stats(self):
        total = len(self.catalog)
        master_count = sum(1 for d in self.catalog if d.get('is_master_root'))
        canceled = sum(1 for d in self.catalog if d.get('is_canceled'))
        valid = total - canceled
        local_ready = sum(1 for d in self.catalog if d.get('file_exists'))
        
        self.lbl_stat_total.configure(text=f"{total:,}")
        self.lbl_stat_master.configure(text=f"{master_count:,}")
        self.lbl_stat_valid.configure(text=f"{valid:,}")
        self.lbl_stat_canceled.configure(text=f"{canceled:,}")
        self.lbl_stat_local.configure(text=f"{local_ready:,}")

        if hasattr(self, 'lbl_header_storage'):
            cur_root = get_storage_root()
            sep_tag = " [Đã tách khỏi App]" if is_custom_storage_root() else " [Chung thư mục App]"
            disp_root = cur_root if len(cur_root) <= 68 else "..." + cur_root[-65:]
            self.lbl_header_storage.configure(
                text=f"💾 Kho PDF: {disp_root}{sep_tag}",
                text_color=THEME['green'] if is_custom_storage_root() else THEME['sky']
            )

    # =========================================================================
    # TAB 1: TRA CỨU & MỞ NHANH (LAZY LOADING & SORTING)
    # =========================================================================
    def setup_tab_search(self):
        self.tab_search.grid_rowconfigure(3, weight=1)
        self.tab_search.grid_columnconfigure(0, weight=1)
        
        # 1. Search Box with Debouncing
        top_filter = ctk.CTkFrame(self.tab_search, fg_color=THEME['surface1'], corner_radius=8)
        top_filter.grid(row=0, column=0, padx=8, pady=(6, 4), sticky="ew")
        top_filter.grid_columnconfigure(0, weight=1)
        
        search_box = ctk.CTkFrame(top_filter, fg_color="transparent")
        search_box.grid(row=0, column=0, padx=8, pady=(6, 4), sticky="ew")
        search_box.grid_columnconfigure(0, weight=1)
        
        self.search_var = tk.StringVar()
        self.search_var.trace_add('write', self.on_search_keypress)
        
        self.txt_search = ctk.CTkEntry(
            search_box,
            placeholder_text="🔍 Tìm kiếm theo mã tài liệu, tiêu đề tiếng Việt, tóm tắt công việc, linh kiện, máy đo, phòng ban...",
            textvariable=self.search_var,
            height=36,
            font=ctk.CTkFont(size=13)
        )
        self.txt_search.grid(row=0, column=0, sticky="ew", padx=(0, 8))
        
        btn_clear = ctk.CTkButton(
            search_box, 
            text="✕ Xóa", 
            width=60, 
            height=36,
            fg_color=THEME['surface2'],
            command=lambda: self.search_var.set("")
        )
        btn_clear.grid(row=0, column=1, padx=(0, 6))

        # View Mode Toggle (Card vs Table)
        self.btn_toggle_view = ctk.CTkSegmentedButton(
            search_box,
            values=["🗂 Dạng Thẻ", "📋 Dạng Bảng"],
            command=self.on_change_view_mode,
            height=36
        )
        self.btn_toggle_view.set("🗂 Dạng Thẻ")
        self.btn_toggle_view.grid(row=0, column=2)

        # Filters Row: Module, Pillar, Tier, Status & Master Excel
        filter_sub = ctk.CTkFrame(top_filter, fg_color="transparent")
        filter_sub.grid(row=1, column=0, padx=8, pady=(2, 6), sticky="ew")
        
        ctk.CTkLabel(filter_sub, text="Phân hệ:", text_color=THEME['subtext'], font=ctk.CTkFont(size=11)).pack(side="left", padx=(0, 4))
        self.mod_names = ["Tất Cả Phân Hệ"] + [m['name'] for m in self.modules]
        self.selected_mod_var = tk.StringVar(value="Tất Cả Phân Hệ")
        self.cmb_module = ctk.CTkOptionMenu(
            filter_sub,
            values=self.mod_names,
            variable=self.selected_mod_var,
            command=lambda v: self.apply_search_filter(),
            width=175,
            height=30,
            font=ctk.CTkFont(size=11)
        )
        self.cmb_module.pack(side="left", padx=2)

        ctk.CTkLabel(filter_sub, text="Lĩnh vực:", text_color=THEME['subtext'], font=ctk.CTkFont(size=11)).pack(side="left", padx=(6, 4))
        self.pillar_search_list = [
            "Tất Cả Lĩnh Vực",
            "🛡️ Đảm Bảo Chất Lượng",
            "🔧 Kỹ Thuật Sản Xuất",
            "🔍 Quy Cách Kiểm Tra",
            "📏 Đo Lường Hiệu Chỉnh",
            "🌿 Môi Trường & An Toàn",
            "📦 Quản Lý Kho Vận",
            "🏢 Quản Trị Chung"
        ]
        self.selected_search_pillar_var = tk.StringVar(value="Tất Cả Lĩnh Vực")
        self.cmb_search_pillar = ctk.CTkOptionMenu(
            filter_sub,
            values=self.pillar_search_list,
            variable=self.selected_search_pillar_var,
            command=lambda v: self.apply_search_filter(),
            width=175,
            height=30,
            font=ctk.CTkFont(size=11)
        )
        self.cmb_search_pillar.pack(side="left", padx=2)
        
        ctk.CTkLabel(filter_sub, text="Cấp bậc:", text_color=THEME['subtext'], font=ctk.CTkFont(size=11)).pack(side="left", padx=(6, 4))
        self.selected_tier_var = tk.StringVar(value="Tất Cả")
        self.cmb_tier = ctk.CTkSegmentedButton(
            filter_sub,
            values=["Tất Cả", "👑 Hồ Sơ Nguồn", "📄 Chi Tiết"],
            variable=self.selected_tier_var,
            command=lambda v: self.apply_search_filter(),
            height=30
        )
        self.cmb_tier.pack(side="left", padx=2)

        ctk.CTkLabel(filter_sub, text="Trạng thái:", text_color=THEME['subtext'], font=ctk.CTkFont(size=11)).pack(side="left", padx=(6, 4))
        self.selected_status_var = tk.StringVar(value="Tất Cả")
        self.cmb_status = ctk.CTkSegmentedButton(
            filter_sub,
            values=["Tất Cả", "Hiệu Lực", "Đã Hủy"],
            variable=self.selected_status_var,
            command=lambda v: self.apply_search_filter(),
            height=30
        )
        self.cmb_status.pack(side="left", padx=2)
        
        btn_open_excel = ctk.CTkButton(
            filter_sub,
            text="📊 File Excel Tổng",
            fg_color=THEME['mauve'],
            text_color="#1e1e2e",
            font=ctk.CTkFont(size=11, weight="bold"),
            height=30,
            command=self.open_active_module_master_excel
        )
        btn_open_excel.pack(side="right", padx=4)

        # 2. Sorting Toolbar (Nút Lọc Sắp Xếp Trực Quan)
        sort_bar = ctk.CTkFrame(self.tab_search, fg_color=THEME['surface0'], corner_radius=6)
        sort_bar.grid(row=1, column=0, padx=8, pady=(2, 2), sticky="ew")
        
        ctk.CTkLabel(
            sort_bar, 
            text="Sắp xếp theo:", 
            text_color=THEME['subtext'],
            font=ctk.CTkFont(size=11, weight="bold")
        ).pack(side="left", padx=(8, 6))
        
        self.sort_buttons = {}
        sort_defs = [
            ("MASTER_FIRST", "👑 Ưu Tiên Nguồn"),
            ("CODE_ASC", "🔤 Mã A→Z"),
            ("CODE_DESC", "🔤 Mã Z→A"),
            ("NAME_ASC", "📄 Tên File A→Z"),
            ("DATE_DESC", "🕒 Mới Cập Nhật"),
            ("STATUS_VALID", "🟢 Hiệu Lực Trước"),
            ("STATUS_CANCELED", "🟠 Đã Hủy Trước")
        ]
        
        for key, text in sort_defs:
            btn = ctk.CTkButton(
                sort_bar,
                text=text,
                height=26,
                font=ctk.CTkFont(size=11),
                fg_color=THEME['blue'] if key == self.current_sort else THEME['surface2'],
                text_color="#1e1e2e" if key == self.current_sort else THEME['text'],
                command=lambda k=key: self.set_sorting(k)
            )
            btn.pack(side="left", padx=3, pady=4)
            self.sort_buttons[key] = btn

        # Info & Count Bar
        info_bar = ctk.CTkFrame(self.tab_search, fg_color="transparent")
        info_bar.grid(row=2, column=0, padx=10, pady=(2, 2), sticky="ew")
        
        self.lbl_result_count = ctk.CTkLabel(
            info_bar,
            text="Đang hiển thị...",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=THEME['blue']
        )
        self.lbl_result_count.pack(side="left")
        
        self.lbl_load_stats = ctk.CTkLabel(
            info_bar,
            text="",
            font=ctk.CTkFont(size=11),
            text_color=THEME['subtext']
        )
        self.lbl_load_stats.pack(side="right")

        # 3. Dynamic Container (Card Container vs Table Container)
        self.container_view = ctk.CTkFrame(self.tab_search, fg_color=THEME['surface0'], corner_radius=8)
        self.container_view.grid(row=3, column=0, padx=8, pady=(0, 8), sticky="nsew")
        self.container_view.grid_rowconfigure(0, weight=1)
        self.container_view.grid_columnconfigure(0, weight=1)
        
        # 3A. Card View (Scrollable with Lazy Loading)
        self.scroll_cards = ctk.CTkScrollableFrame(self.container_view, fg_color="transparent")
        self.scroll_cards.grid(row=0, column=0, sticky="nsew")
        self.scroll_cards.grid_columnconfigure(0, weight=1)
        
        # 3B. Table View (High-Speed Treeview)
        self.table_frame = ctk.CTkFrame(self.container_view, fg_color=THEME['surface0'])
        self.setup_table_view()

    def setup_table_view(self):
        self.table_frame.grid_rowconfigure(0, weight=0)
        self.table_frame.grid_rowconfigure(1, weight=1)
        self.table_frame.grid_columnconfigure(0, weight=1)

        # Bulk Action Bar for Table View (Multi-Select Move / Relink / Delete)
        tbl_bar = ctk.CTkFrame(self.table_frame, fg_color=THEME['surface1'], corner_radius=6)
        tbl_bar.grid(row=0, column=0, columnspan=2, padx=2, pady=(2, 4), sticky="ew")

        self.lbl_table_sel = ctk.CTkLabel(
            tbl_bar,
            text="💡 Giữ Ctrl / Shift để chọn nhiều dòng • Click chuột phải để mở menu thao tác",
            font=ctk.CTkFont(size=11),
            text_color=THEME['subtext']
        )
        self.lbl_table_sel.pack(side="left", padx=8, pady=4)

        ctk.CTkButton(
            tbl_bar,
            text="🗑️ Xóa Đã Chọn",
            width=105,
            height=26,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME['red'],
            hover_color="#d97290",
            text_color="#1e1e2e",
            command=self.action_delete_selected_table_docs
        ).pack(side="right", padx=(3, 6), pady=4)

        ctk.CTkButton(
            tbl_bar,
            text="🔗 Đổi Link",
            width=85,
            height=26,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME['surface2'],
            hover_color=THEME['card_hover'],
            text_color=THEME['sky'],
            command=self.action_edit_selected_table_doc
        ).pack(side="right", padx=3, pady=4)

        ctk.CTkButton(
            tbl_bar,
            text="📦 Di Chuyển Đã Chọn",
            width=135,
            height=26,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME['yellow'],
            hover_color="#e5cd98",
            text_color="#1e1e2e",
            command=self.action_move_selected_table_docs
        ).pack(side="right", padx=3, pady=4)
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background=THEME['surface0'],
            foreground=THEME['text'],
            rowheight=32,
            fieldbackground=THEME['surface0'],
            font=("Segoe UI", 10),
            borderwidth=0
        )
        style.configure(
            "Treeview.Heading",
            background=THEME['surface1'],
            foreground=THEME['blue'],
            font=("Segoe UI", 11, "bold"),
            borderwidth=0
        )
        style.map("Treeview", background=[('selected', THEME['surface2'])])
        style.map("Treeview.Heading", background=[('active', THEME['surface2'])])
        
        cols = ("tier", "code", "title", "pillar", "dept", "status", "size", "local")
        self.tree = ttk.Treeview(self.table_frame, columns=cols, show="headings", selectmode="extended")
        
        self.tree.heading("tier", text="Cấp Bậc ▲▼", command=lambda: self.set_sorting("MASTER_FIRST"))
        self.tree.heading("code", text="Mã Số Tài Liệu ▲▼", command=lambda: self.set_sorting("CODE_ASC" if self.current_sort == "CODE_DESC" else "CODE_DESC"))
        self.tree.heading("title", text="Tiêu Đề & Tóm Tắt Nghiệp Vụ (Mô Tả Công Việc) ▲▼", command=lambda: self.set_sorting("NAME_ASC"))
        self.tree.heading("pillar", text="Lĩnh Vực Quản Trị")
        self.tree.heading("dept", text="Đơn Vị Sở Hữu")
        self.tree.heading("status", text="Trạng Thái")
        self.tree.heading("size", text="Kích Thước")
        self.tree.heading("local", text="Trạng Thái File")
        
        self.tree.column("tier", width=105, anchor="center")
        self.tree.column("code", width=145, anchor="w")
        self.tree.column("title", width=490, anchor="w")
        self.tree.column("pillar", width=155, anchor="w")
        self.tree.column("dept", width=160, anchor="w")
        self.tree.column("status", width=110, anchor="center")
        self.tree.column("size", width=80, anchor="center")
        self.tree.column("local", width=100, anchor="center")
        
        sb = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        
        self.tree.grid(row=1, column=0, sticky="nsew")
        sb.grid(row=1, column=1, sticky="ns")
        
        # Events
        self.tree.bind("<Double-1>", self.on_table_double_click)
        self.tree.bind("<Button-3>", self.on_table_right_click)
        self.tree.bind("<<TreeviewSelect>>", self.on_table_selection_change)

    def on_change_view_mode(self, mode_val):
        if "Thẻ" in mode_val:
            self.current_view_mode = "card"
            self.table_frame.grid_forget()
            self.scroll_cards.grid(row=0, column=0, sticky="nsew")
            self.render_cards_page(reset=True)
        else:
            self.current_view_mode = "table"
            self.scroll_cards.grid_forget()
            self.table_frame.grid(row=0, column=0, sticky="nsew")
            self.render_table_view()

    def on_search_keypress(self, *args):
        # Debounce: wait 150ms after user stops typing
        if self._search_job:
            self.after_cancel(self._search_job)
        self._search_job = self.after(150, self.apply_search_filter)

    def set_sorting(self, sort_key):
        self.current_sort = sort_key
        # Update button visual
        for k, btn in self.sort_buttons.items():
            if k == sort_key:
                btn.configure(fg_color=THEME['blue'], text_color="#1e1e2e")
            else:
                btn.configure(fg_color=THEME['surface2'], text_color=THEME['text'])
        self.apply_search_filter()

    def apply_search_filter(self):
        query = self.search_var.get().strip().lower()
        selected_mod = self.selected_mod_var.get()
        selected_pillar_filter = self.selected_search_pillar_var.get() if hasattr(self, 'selected_search_pillar_var') else "Tất Cả Lĩnh Vực"
        selected_tier = self.selected_tier_var.get()
        selected_status = self.selected_status_var.get()
        
        pillar_keywords = {
            "Chất Lượng": "Chất Lượng",
            "Kỹ Thuật": "Kỹ Thuật",
            "Kiểm Tra": "Kiểm Tra",
            "Đo Lường": "Đo Lường",
            "Môi Trường": "Môi Trường",
            "Kho": "Kho",
            "Quản Trị": "Quản Trị"
        }
        
        # 1. Filter
        filtered = []
        for doc in self.catalog:
            if selected_mod != "Tất Cả Phân Hệ" and doc.get('module_name') != selected_mod:
                continue
            if selected_pillar_filter != "Tất Cả Lĩnh Vực":
                doc_p = doc.get('pillar', '')
                matched_p = False
                for k, v in pillar_keywords.items():
                    if k in selected_pillar_filter and v in doc_p:
                        matched_p = True
                        break
                if not matched_p:
                    continue
            if selected_tier == "👑 Hồ Sơ Nguồn" and not doc.get('is_master_root'):
                continue
            elif selected_tier == "📄 Chi Tiết" and doc.get('is_master_root'):
                continue
            if selected_status == "Hiệu Lực" and doc.get('is_canceled'):
                continue
            elif "Đã Hủy" in selected_status and not doc.get('is_canceled'):
                continue
                
            filtered.append(doc)

        # 2. Multi-word & Unaccented Search (Tra cứu theo Nội Dung, Tóm Tắt, Mã, Phòng Ban, Thiết Bị)
        if query:
            q_clean = remove_accents(query)
            q_terms = [t for t in q_clean.split() if t]
            filtered_match = []
            for doc in filtered:
                search_blob = doc.get('search_text')
                if not search_blob:
                    search_blob = (
                        f"{doc.get('doc_code', '')} {doc.get('doc_title', '')} "
                        f"{doc.get('summary', '')} {doc.get('so_huu', '')} "
                        f"{doc.get('pillar', '')} {doc.get('filename', '')} "
                        f"{remove_accents(doc.get('doc_title', ''))} {remove_accents(doc.get('summary', ''))}"
                    )
                blob_clean = remove_accents(search_blob)
                if all(term in blob_clean for term in q_terms):
                    filtered_match.append(doc)
            filtered = filtered_match
            
        # 3. Sort
        if self.current_sort == "MASTER_FIRST":
            filtered.sort(key=lambda d: (0 if d.get('is_master_root') else 1, d.get('doc_code', '').lower()))
        elif self.current_sort == "CODE_ASC":
            filtered.sort(key=lambda d: d.get('doc_code', '').lower())
        elif self.current_sort == "CODE_DESC":
            filtered.sort(key=lambda d: d.get('doc_code', '').lower(), reverse=True)
        elif self.current_sort == "NAME_ASC":
            filtered.sort(key=lambda d: d.get('doc_title', d.get('filename', '')).lower())
        elif self.current_sort == "DATE_DESC":
            filtered.sort(key=lambda d: d.get('mtime', 0), reverse=True)
        elif self.current_sort == "STATUS_VALID":
            filtered.sort(key=lambda d: (1 if d.get('is_canceled') else 0, d.get('doc_code', '').lower()))
        elif self.current_sort == "STATUS_CANCELED":
            filtered.sort(key=lambda d: (0 if d.get('is_canceled') else 1, d.get('doc_code', '').lower()))
            
        self.filtered_docs = filtered
        self.current_page = 1
        
        total_matched = len(filtered)
        self.lbl_result_count.configure(
            text=f"Tìm thấy {total_matched:,} tài liệu phù hợp (trên tổng số {len(self.catalog):,})"
        )
        
        if self.current_view_mode == "card":
            self.render_cards_page(reset=True)
        else:
            self.render_table_view()

    # --- CARD VIEW (LAZY LOADING) ---
    def render_cards_page(self, reset=False):
        if reset:
            for w in self.scroll_cards.winfo_children():
                w.destroy()
            self.current_page = 1
            
        total = len(self.filtered_docs)
        if total == 0:
            empty_box = ctk.CTkFrame(self.scroll_cards, fg_color="transparent")
            empty_box.pack(expand=True, pady=60)
            ctk.CTkLabel(
                empty_box,
                text="Không tìm thấy tài liệu phù hợp với bộ lọc hiện tại.",
                font=ctk.CTkFont(size=14),
                text_color=THEME['subtext']
            ).pack()
            self.lbl_load_stats.configure(text="0 / 0 mục")
            return

        # Render slice for current page
        start_idx = (self.current_page - 1) * PAGE_SIZE
        end_idx = min(start_idx + PAGE_SIZE, total)
        
        # Remove existing footer if any
        if hasattr(self, 'footer_frame') and self.footer_frame.winfo_exists():
            self.footer_frame.destroy()

        # Render items batch
        for doc in self.filtered_docs[start_idx:end_idx]:
            self.create_doc_card(self.scroll_cards, doc)

        self.lbl_load_stats.configure(text=f"Đang hiển thị {end_idx:,} / {total:,} mục")

        # Footer for Lazy Loading (Kéo xuống nạp dần hoặc Bấm để tải tiếp)
        if end_idx < total:
            self.footer_frame = ctk.CTkFrame(self.scroll_cards, fg_color="transparent")
            self.footer_frame.pack(fill="x", pady=12)
            
            remaining = total - end_idx
            btn_load_more = ctk.CTkButton(
                self.footer_frame,
                text=f"⬇ Cuộn Xuống Hoặc Bấm Để Xem Thêm ({min(PAGE_SIZE, remaining)} mục tiếp theo / Còn lại {remaining:,})",
                fg_color=THEME['surface1'],
                hover_color=THEME['surface2'],
                text_color=THEME['blue'],
                height=36,
                font=ctk.CTkFont(size=12, weight="bold"),
                command=self.load_next_card_batch
            )
            btn_load_more.pack(expand=True, fill="x", padx=40)

    def load_next_card_batch(self):
        total = len(self.filtered_docs)
        if self.current_page * PAGE_SIZE < total:
            self.current_page += 1
            self.render_cards_page(reset=False)

    def create_doc_card(self, parent, doc):
        is_master = doc.get('is_master_root', False)
        border_w = 2 if is_master else 0
        border_c = THEME['yellow'] if is_master else THEME['surface1']

        card = ctk.CTkFrame(
            parent, 
            fg_color=THEME['surface1'], 
            corner_radius=8,
            border_width=border_w,
            border_color=border_c
        )
        card.pack(fill="x", padx=4, pady=3)
        card.grid_columnconfigure(1, weight=1)
        
        is_canceled = doc.get('is_canceled', False)
        status_color = THEME['peach'] if is_canceled else THEME['green']
        status_text = "Đã Hủy Bỏ (Đã Bổ Sung Link)" if is_canceled else "Hiệu Lực"
        
        # Left Box: Code & Module
        left_box = ctk.CTkFrame(card, fg_color="transparent", width=180)
        left_box.grid(row=0, column=0, padx=10, pady=8, sticky="w")
        
        code_lbl = ctk.CTkLabel(
            left_box,
            text=doc.get('doc_code', 'NO-CODE'),
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=THEME['yellow'] if is_master else THEME['blue']
        )
        code_lbl.pack(anchor="w")
        
        mod_lbl = ctk.CTkLabel(
            left_box,
            text=doc.get('module_name', ''),
            font=ctk.CTkFont(size=10),
            text_color=THEME['subtext']
        )
        mod_lbl.pack(anchor="w")

        # Middle Box: Title, Summary, Department & Governance Linkage
        mid_box = ctk.CTkFrame(card, fg_color="transparent")
        mid_box.grid(row=0, column=1, padx=8, pady=8, sticky="w")
        
        # 1. Main Vietnamese Title
        doc_title = doc.get('doc_title', doc.get('filename', ''))
        title_lbl = ctk.CTkLabel(
            mid_box,
            text=doc_title,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=THEME['text'],
            wraplength=640,
            justify="left"
        )
        title_lbl.pack(anchor="w")
        
        # 2. Executive Summary (Mô tả công việc & Mục đích của file)
        summary_text = doc.get('summary', '')
        if summary_text:
            summary_lbl = ctk.CTkLabel(
                mid_box,
                text=f"📋 Tóm tắt: {summary_text}",
                font=ctk.CTkFont(size=11),
                text_color=THEME['subtext'],
                wraplength=640,
                justify="left"
            )
            summary_lbl.pack(anchor="w", pady=(2, 2))
        
        meta_row = ctk.CTkFrame(mid_box, fg_color="transparent")
        meta_row.pack(anchor="w", pady=(2, 0))
        
        if is_master:
            tier_pill = ctk.CTkLabel(
                meta_row,
                text="👑 HỒ SƠ NGUỒN",
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=THEME['yellow']
            )
            tier_pill.pack(side="left", padx=(0, 8))
        else:
            p_ref = doc.get('parent_ref', '')
            if p_ref:
                ref_lbl = ctk.CTkLabel(
                    meta_row,
                    text=f"🔗 Căn cứ: {p_ref}",
                    font=ctk.CTkFont(size=10),
                    text_color=THEME['blue']
                )
                ref_lbl.pack(side="left", padx=(0, 8))

        dept_str = doc.get('so_huu', '')
        if dept_str:
            dept_lbl = ctk.CTkLabel(
                meta_row,
                text=f"🏢 {dept_str}",
                font=ctk.CTkFont(size=10),
                text_color=THEME['subtext']
            )
            dept_lbl.pack(side="left", padx=(0, 8))

        pillar_str = doc.get('pillar', '')
        if pillar_str:
            pillar_lbl = ctk.CTkLabel(
                meta_row,
                text=f"[{pillar_str}]",
                font=ctk.CTkFont(size=10, weight="bold"),
                text_color=THEME['mauve']
            )
            pillar_lbl.pack(side="left", padx=(0, 8))

        pill = ctk.CTkLabel(
            meta_row,
            text=f"● {status_text}",
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color=status_color
        )
        pill.pack(side="left", padx=(0, 8))
        
        local_exists = doc.get('file_exists', False)
        loc_badge = ctk.CTkLabel(
            meta_row,
            text="🟢 Cục Bộ" if local_exists else "🔴 Chưa Tải",
            font=ctk.CTkFont(size=10),
            text_color=THEME['green'] if local_exists else THEME['red']
        )
        loc_badge.pack(side="left")

        # Right Box: Action Buttons
        btn_box = ctk.CTkFrame(card, fg_color="transparent")
        btn_box.grid(row=0, column=2, padx=10, pady=8, sticky="e")
        
        btn_open_loc = ctk.CTkButton(
            btn_box,
            text="📄 Mở File",
            width=75,
            height=28,
            fg_color=THEME['blue'],
            text_color="#1e1e2e",
            font=ctk.CTkFont(weight="bold", size=11),
            command=lambda d=doc: self.open_local_file(d)
        )
        btn_open_loc.pack(side="left", padx=3)
        
        btn_open_net = ctk.CTkButton(
            btn_box,
            text="🌐 Ổ Mạng",
            width=75,
            height=28,
            fg_color=THEME['surface2'],
            text_color=THEME['text'],
            font=ctk.CTkFont(size=11),
            command=lambda d=doc: self.open_remote_file(d)
        )
        btn_open_net.pack(side="left", padx=3)
        
        btn_open_dir = ctk.CTkButton(
            btn_box,
            text="📁 Thư Mục",
            width=75,
            height=28,
            fg_color=THEME['surface2'],
            text_color=THEME['text'],
            font=ctk.CTkFont(size=11),
            command=lambda d=doc: self.open_file_folder(d)
        )
        btn_open_dir.pack(side="left", padx=3)

        btn_more = ctk.CTkButton(
            btn_box,
            text="⋯",
            width=32,
            height=28,
            fg_color=THEME['surface2'],
            hover_color=THEME['card_hover'],
            text_color=THEME['yellow'],
            font=ctk.CTkFont(size=14, weight="bold")
        )
        btn_more.configure(command=lambda d=doc, b=btn_more: self.show_card_doc_menu(d, b))
        btn_more.pack(side="left", padx=(3, 0))

    # --- TABLE VIEW (HIGH-SPEED C-ENGINE) ---
    def render_table_view(self):
        self.tree.delete(*self.tree.get_children())
        total = len(self.filtered_docs)
        self.lbl_load_stats.configure(text=f"Hiển thị bảng 100% ({total:,} mục)")
        
        for doc in self.filtered_docs:
            is_master = doc.get('is_master_root', False)
            tier_str = "👑 NGUỒN" if is_master else "📄 CHI TIẾT"
            code = doc.get('doc_code', '')
            title_clean = doc.get('doc_title', doc.get('filename', ''))
            summary_clean = doc.get('summary', '')
            title_display = f"{title_clean} — {summary_clean}" if summary_clean else title_clean
            pillar_str = doc.get('pillar', '')
            dept_str = doc.get('so_huu', '')
            is_canceled = doc.get('is_canceled', False)
            status = "Đã Hủy (Có Link)" if is_canceled else "Hiệu Lực"
            size_kb = f"{doc.get('size', 0) / 1024:.0f} KB"
            local_status = "🟢 Sẵn Sàng" if doc.get('file_exists') else "🔴 Chưa Tải"
            
            item_id = self.tree.insert("", "end", values=(tier_str, code, title_display, pillar_str, dept_str, status, size_kb, local_status))
            self.tree.set(item_id, "code", code)

    def on_table_double_click(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        idx = self.tree.index(sel[0])
        if 0 <= idx < len(self.filtered_docs):
            doc = self.filtered_docs[idx]
            self.open_local_file(doc)

    def get_selected_table_docs(self):
        docs = []
        for iid in self.tree.selection():
            idx = self.tree.index(iid)
            if 0 <= idx < len(self.filtered_docs):
                docs.append(self.filtered_docs[idx])
        return docs

    def on_table_selection_change(self, event=None):
        sel = self.tree.selection()
        if not sel:
            self.lbl_table_sel.configure(
                text="💡 Giữ Ctrl / Shift để chọn nhiều dòng • Click chuột phải để mở menu thao tác",
                text_color=THEME['subtext']
            )
        else:
            self.lbl_table_sel.configure(
                text=f"✓ Đang chọn {len(sel):,} tài liệu — Dùng nút bên phải hoặc chuột phải để Di chuyển / Đổi link / Xóa",
                text_color=THEME['yellow']
            )

    def show_card_doc_menu(self, doc, anchor_widget):
        menu = tk.Menu(
            self, tearoff=0,
            bg=THEME['surface1'], fg=THEME['text'],
            activebackground=THEME['blue'], activeforeground="#1e1e2e",
            font=("Segoe UI", 10)
        )
        menu.add_command(label="📦 Di Chuyển File Này Sang Thư Mục Khác...", command=lambda: self.open_move_docs_dialog([doc]))
        menu.add_command(label="🔗 Cập Nhật Địa Chỉ / Đổi Link...", command=lambda: self.open_edit_links_dialog(doc))
        menu.add_separator()
        menu.add_command(label="🗑️ Xóa Tài Liệu Này...", command=lambda: self.open_delete_docs_dialog([doc]))
        x = anchor_widget.winfo_rootx()
        y = anchor_widget.winfo_rooty() + anchor_widget.winfo_height()
        menu.tk_popup(x, y)

    def action_move_selected_table_docs(self):
        docs = self.get_selected_table_docs()
        if not docs:
            messagebox.showinfo("Chưa Chọn Tài Liệu", "Vui lòng chọn ít nhất 1 dòng trong bảng để di chuyển.")
            return
        self.open_move_docs_dialog(docs)

    def action_edit_selected_table_doc(self):
        docs = self.get_selected_table_docs()
        if not docs:
            messagebox.showinfo("Chưa Chọn Tài Liệu", "Vui lòng chọn 1 tài liệu trong bảng để cập nhật địa chỉ / đổi link.")
            return
        self.open_edit_links_dialog(docs[0])

    def action_delete_selected_table_docs(self):
        docs = self.get_selected_table_docs()
        if not docs:
            messagebox.showinfo("Chưa Chọn Tài Liệu", "Vui lòng chọn ít nhất 1 dòng trong bảng để xóa.")
            return
        self.open_delete_docs_dialog(docs)

    def on_table_right_click(self, event):
        iid = self.tree.identify_row(event.y)
        if not iid:
            return
        if iid not in self.tree.selection():
            self.tree.selection_set(iid)
        docs = self.get_selected_table_docs()
        if not docs:
            return
        menu = tk.Menu(
            self, tearoff=0,
            bg=THEME['surface1'], fg=THEME['text'],
            activebackground=THEME['blue'], activeforeground="#1e1e2e",
            font=("Segoe UI", 10)
        )
        if len(docs) == 1:
            doc = docs[0]
            menu.add_command(label="📄 Mở File Cục Bộ", command=lambda: self.open_local_file(doc))
            menu.add_command(label="🌐 Mở File Ổ Mạng Gốc", command=lambda: self.open_remote_file(doc))
            menu.add_command(label="📁 Mở Thư Mục Chứa File", command=lambda: self.open_file_folder(doc))
            menu.add_separator()
            menu.add_command(label="📦 Di Chuyển Tài Liệu Này...", command=lambda: self.open_move_docs_dialog([doc]))
            menu.add_command(label="🔗 Cập Nhật Địa Chỉ / Đổi Link...", command=lambda: self.open_edit_links_dialog(doc))
            menu.add_separator()
            menu.add_command(label="🗑️ Xóa Tài Liệu Này...", command=lambda: self.open_delete_docs_dialog([doc]))
        else:
            n = len(docs)
            menu.add_command(label=f"📦 Di Chuyển {n:,} Tài Liệu Đã Chọn...", command=lambda: self.open_move_docs_dialog(docs))
            menu.add_separator()
            menu.add_command(label=f"🗑️ Xóa {n:,} Tài Liệu Đã Chọn...", command=lambda: self.open_delete_docs_dialog(docs))
        menu.tk_popup(event.x_root, event.y_root)

    # --- FILE OPENING HELPERS ---
    def open_current_storage_folder(self):
        root = get_storage_root()
        if path_exists(root):
            try:
                os.startfile(root)
            except Exception as e:
                messagebox.showerror("Lỗi Mở Thư Mục", str(e))
        else:
            messagebox.showwarning("Không Tìm Thấy Thư Mục", f"Thư mục kho không tồn tại:\n{root}")

    def open_local_file(self, doc):
        local_rel = doc.get('local_path', '')
        full_path = resolve_local_path(local_rel)
        if full_path and is_file_exists(full_path):
            try:
                target = to_long_path(full_path) if len(full_path) >= 255 else full_path
                os.startfile(target)
            except Exception as e:
                messagebox.showerror("Lỗi Mở File", f"Không thể mở file cục bộ:\n{e}")
        else:
            remote_p = doc.get('remote_path', '')
            if remote_p and path_exists(remote_p):
                if messagebox.askyesno("File Chưa Có Cục Bộ", "File này chưa có ở kho cục bộ. Bạn có muốn mở trực tiếp từ ổ mạng không?"):
                    try:
                        os.startfile(remote_p)
                    except Exception as e:
                        messagebox.showerror("Lỗi Mở File", f"Không thể mở từ ổ mạng:\n{e}")
            else:
                messagebox.showwarning(
                    "Không Tìm Thấy File",
                    f"File không tồn tại tại địa chỉ cục bộ:\n{full_path or '(Trống)'}\n\n"
                    f"Gợi ý: Bạn có thể dùng chức năng '🔗 Cập nhật địa chỉ / Đổi link' hoặc vào tab '📦 Quản Lý Kho & Di Chuyển' để nối lại đường dẫn."
                )

    def open_remote_file(self, doc):
        remote_p = doc.get('remote_path', '')
        if remote_p and path_exists(remote_p):
            try:
                os.startfile(remote_p)
            except Exception as e:
                messagebox.showerror("Lỗi Mở Ổ Mạng", f"Không thể mở file trên ổ mạng:\n{e}")
        else:
            messagebox.showwarning("Không Tìm Thấy Ổ Mạng", f"Không thể kết nối tới file gốc trên máy chủ:\n{remote_p}")

    def open_file_folder(self, doc):
        local_rel = doc.get('local_path', '')
        full_path = resolve_local_path(local_rel)
        if full_path and is_file_exists(full_path):
            try:
                subprocess.Popen(['explorer', '/select,', os.path.normpath(full_path)])
            except Exception:
                os.startfile(os.path.dirname(full_path))
        else:
            remote_p = doc.get('remote_path', '')
            if remote_p and path_exists(remote_p):
                try:
                    subprocess.Popen(['explorer', '/select,', os.path.normpath(remote_p)])
                except Exception:
                    os.startfile(os.path.dirname(remote_p))
            else:
                messagebox.showwarning("Không Tìm Thấy Thư Mục", f"Không tìm thấy file cục bộ:\n{full_path or '(Trống)'}")

    def open_active_module_master_excel(self):
        selected_mod_name = self.selected_mod_var.get()
        target_mod = None
        for m in self.modules:
            if m['name'] == selected_mod_name:
                target_mod = m
                break
        if not target_mod:
            target_mod = self.modules[0] if self.modules else None
        if not target_mod:
            return
            
        local_excel = resolve_master_excel_path(target_mod['local_subfolder'], target_mod['excel_local_name'])
        if local_excel and is_file_exists(local_excel):
            try:
                os.startfile(local_excel)
                return
            except Exception:
                pass
        remote_excel = target_mod.get('excel_remote')
        if remote_excel and path_exists(remote_excel):
            try:
                os.startfile(remote_excel)
            except Exception as e:
                messagebox.showerror("Lỗi Mở File", str(e))
        else:
            messagebox.showwarning("Không Tìm Thấy", f"File Excel tổng chưa được tải về: {local_excel}")

    # =========================================================================
    # TAB 2: MA TRẬN QUẢN TRỊ & ĐIỀU HÀNH 7 YẾU TỐ
    # =========================================================================
    def setup_tab_governance(self):
        self.tab_governance.grid_rowconfigure(2, weight=1)
        self.tab_governance.grid_columnconfigure(0, weight=1)
        
        # 1. Pillar Selector & Search Bar
        gov_header = ctk.CTkFrame(self.tab_governance, fg_color=THEME['surface1'], corner_radius=8)
        gov_header.grid(row=0, column=0, padx=8, pady=(6, 4), sticky="ew")
        gov_header.grid_columnconfigure(0, weight=1)
        
        search_box = ctk.CTkFrame(gov_header, fg_color="transparent")
        search_box.grid(row=0, column=0, padx=8, pady=(6, 4), sticky="ew")
        search_box.grid_columnconfigure(0, weight=1)
        
        self.gov_search_var = tk.StringVar()
        self.gov_search_var.trace_add('write', self.on_gov_search_keypress)
        
        txt_gov_search = ctk.CTkEntry(
            search_box,
            placeholder_text="🔍 Tìm kiếm ma trận quản trị: theo mã số, tên quy định, rủi ro, dữ liệu kiểm soát, đơn vị sở hữu...",
            textvariable=self.gov_search_var,
            height=36,
            font=ctk.CTkFont(size=13)
        )
        txt_gov_search.grid(row=0, column=0, sticky="ew", padx=(0, 8))
        
        btn_gov_clear = ctk.CTkButton(
            search_box, 
            text="✕ Xóa", 
            width=60, 
            height=36,
            fg_color=THEME['surface2'],
            command=lambda: self.gov_search_var.set("")
        )
        btn_gov_clear.grid(row=0, column=1)

        # Row 2: Document Tier Segmented Filter (Hồ sơ nguồn vs Chi tiết)
        tier_bar = ctk.CTkFrame(gov_header, fg_color="transparent")
        tier_bar.grid(row=1, column=0, padx=8, pady=(2, 4), sticky="ew")
        
        ctk.CTkLabel(tier_bar, text="Cấp bậc văn bản:", font=ctk.CTkFont(size=11, weight="bold"), text_color=THEME['yellow']).pack(side="left", padx=(0, 6))
        self.gov_tier_var = tk.StringVar(value="Tất Cả")
        self.cmb_gov_tier = ctk.CTkSegmentedButton(
            tier_bar,
            values=["Tất Cả", "👑 Chỉ Hồ Sơ Nguồn Chuẩn", "📄 Hồ Sơ Triển Khai"],
            variable=self.gov_tier_var,
            command=lambda v: self.apply_gov_filter(),
            height=28
        )
        self.cmb_gov_tier.pack(side="left", padx=2)

        # Row 3: Pillars Bar (Pill buttons for 6 core governance pillars)
        pillars_bar = ctk.CTkFrame(gov_header, fg_color="transparent")
        pillars_bar.grid(row=2, column=0, padx=8, pady=(2, 6), sticky="ew")
        
        ctk.CTkLabel(pillars_bar, text="Trụ cột quản trị:", font=ctk.CTkFont(size=11, weight="bold"), text_color=THEME['subtext']).pack(side="left", padx=(0, 6))
        
        self.pillar_buttons = {}
        pillar_list = [
            ("Tất Cả", "🏛️ Tất Cả"),
            ("Kỹ Thuật & Thiết Bị Sản Xuất", "🔧 Kỹ Thuật Sản Xuất"),
            ("Đảm Bảo & Kiểm Soát Chất Lượng", "🛡️ Đảm Bảo Chất Lượng"),
            ("Quy Cách Kiểm Tra Linh Kiện", "🔍 Quy Cách Kiểm Tra"),
            ("Đo Lường & Hiệu Chỉnh Thiết Bị", "📏 Đo Lường Hiệu Chỉnh"),
            ("Quản Lý Môi Trường & Hóa Chất", "🌿 Môi Trường & An Toàn"),
            ("Quản Trị Chung & An Ninh Dữ Liệu", "🏢 Quản Trị & Bảo Mật"),
            ("Quản Lý Kho Vận & Vật Tư", "📦 Quản Lý Kho")
        ]
        
        for p_key, p_text in pillar_list:
            btn = ctk.CTkButton(
                pillars_bar,
                text=p_text,
                height=28,
                font=ctk.CTkFont(size=11),
                fg_color=THEME['mauve'] if p_key == self.selected_pillar else THEME['surface2'],
                text_color="#1e1e2e" if p_key == self.selected_pillar else THEME['text'],
                command=lambda k=p_key: self.set_governance_pillar(k)
            )
            btn.pack(side="left", padx=2)
            self.pillar_buttons[p_key] = btn

        # Info Count
        gov_info_bar = ctk.CTkFrame(self.tab_governance, fg_color="transparent")
        gov_info_bar.grid(row=1, column=0, padx=10, pady=(2, 2), sticky="ew")
        
        self.lbl_gov_count = ctk.CTkLabel(
            gov_info_bar,
            text="Đang hiển thị ma trận quản trị...",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=THEME['mauve']
        )
        self.lbl_gov_count.pack(side="left")

        # 2. Scrollable Container for Governance Cards (with Lazy Loading)
        self.scroll_gov = ctk.CTkScrollableFrame(self.tab_governance, fg_color=THEME['surface0'], corner_radius=8)
        self.scroll_gov.grid(row=2, column=0, padx=8, pady=(0, 8), sticky="nsew")
        self.scroll_gov.grid_columnconfigure(0, weight=1)

    def set_governance_pillar(self, pillar_key):
        self.selected_pillar = pillar_key
        for k, btn in self.pillar_buttons.items():
            if k == pillar_key:
                btn.configure(fg_color=THEME['mauve'], text_color="#1e1e2e")
            else:
                btn.configure(fg_color=THEME['surface2'], text_color=THEME['text'])
        self.apply_gov_filter()

    def on_gov_search_keypress(self, *args):
        if self._gov_search_job:
            self.after_cancel(self._gov_search_job)
        self._gov_search_job = self.after(150, self.apply_gov_filter)

    def apply_gov_filter(self):
        query = self.gov_search_var.get().strip().lower()
        tier_mode = self.gov_tier_var.get() if hasattr(self, 'gov_tier_var') else "Tất Cả"
        filtered = []
        
        for item in self.governance_data:
            if "Chỉ Hồ Sơ Nguồn" in tier_mode or "👑" in tier_mode:
                if not item.get('is_master_root'):
                    continue
            elif "Hồ Sơ Triển Khai" in tier_mode or "📄" in tier_mode:
                if item.get('is_master_root'):
                    continue

            if self.selected_pillar != "Tất Cả" and item.get('pillar') != self.selected_pillar:
                continue
                
            if query:
                combined_text = (
                    item.get('doc_code', '') + " " +
                    item.get('title', '') + " " +
                    item.get('so_huu', '') + " " +
                    item.get('kiem_soat', '') + " " +
                    item.get('ho_so', '') + " " +
                    item.get('rui_ro', '') + " " +
                    item.get('ket_qua', '') + " " +
                    item.get('doc_tier', '') + " " +
                    item.get('parent_ref', '')
                ).lower()
                if query not in combined_text:
                    continue
            filtered.append(item)
            
        self.filtered_gov = filtered
        self.current_gov_page = 1
        
        total = len(filtered)
        self.lbl_gov_count.configure(
            text=f"Mô hình Quản Trị 7 Yếu Tố: {total:,} quy trình chuẩn hóa (Bộ lọc: {tier_mode} • Trụ cột: {self.selected_pillar})"
        )
        self.render_gov_page(reset=True)

    def render_gov_page(self, reset=False):
        if reset:
            for w in self.scroll_gov.winfo_children():
                w.destroy()
            self.current_gov_page = 1
            
        total = len(self.filtered_gov)
        if total == 0:
            empty_box = ctk.CTkFrame(self.scroll_gov, fg_color="transparent")
            empty_box.pack(expand=True, pady=60)
            ctk.CTkLabel(empty_box, text="Không tìm thấy quy trình phù hợp.", font=ctk.CTkFont(size=14), text_color=THEME['subtext']).pack()
            return

        start_idx = (self.current_gov_page - 1) * PAGE_SIZE
        end_idx = min(start_idx + PAGE_SIZE, total)

        if hasattr(self, 'gov_footer_frame') and self.gov_footer_frame.winfo_exists():
            self.gov_footer_frame.destroy()

        for item in self.filtered_gov[start_idx:end_idx]:
            self.create_gov_card(self.scroll_gov, item)

        if end_idx < total:
            self.gov_footer_frame = ctk.CTkFrame(self.scroll_gov, fg_color="transparent")
            self.gov_footer_frame.pack(fill="x", pady=12)
            
            remaining = total - end_idx
            btn_load_more = ctk.CTkButton(
                self.gov_footer_frame,
                text=f"⬇ Xem Thêm ({min(PAGE_SIZE, remaining)} quy trình tiếp theo / Còn lại {remaining:,})",
                fg_color=THEME['surface1'],
                hover_color=THEME['surface2'],
                text_color=THEME['mauve'],
                height=34,
                font=ctk.CTkFont(size=12, weight="bold"),
                command=self.load_next_gov_batch
            )
            btn_load_more.pack(expand=True, fill="x", padx=40)

    def load_next_gov_batch(self):
        total = len(self.filtered_gov)
        if self.current_gov_page * PAGE_SIZE < total:
            self.current_gov_page += 1
            self.render_gov_page(reset=False)

    def create_gov_card(self, parent, item):
        is_master = item.get('is_master_root', False)
        border_w = 2 if is_master else 0
        border_c = THEME['yellow'] if is_master else THEME['surface1']

        card = ctk.CTkFrame(
            parent, 
            fg_color=THEME['surface1'], 
            corner_radius=8,
            border_width=border_w,
            border_color=border_c
        )
        card.pack(fill="x", padx=4, pady=4)
        card.grid_columnconfigure(0, weight=1)
        
        # Header Row
        header_row = ctk.CTkFrame(card, fg_color="transparent")
        header_row.pack(fill="x", padx=12, pady=(10, 4))
        
        icon = item.get('icon', '📌')
        pillar = item.get('pillar', '')
        code = item.get('doc_code', '')
        title = item.get('title', '')
        rev = item.get('rev', '')
        status = item.get('status', 'Đang Hiệu Lực')
        is_canceled = item.get('is_canceled', False)
        status_color = THEME['peach'] if is_canceled else THEME['green']
        
        lbl_code = ctk.CTkLabel(
            header_row,
            text=f"{icon} {code} (Rev: {rev})",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=THEME['yellow'] if is_master else THEME['blue']
        )
        lbl_code.pack(side="left")
        
        if is_master:
            tier_badge = ctk.CTkLabel(
                header_row,
                text=" [👑 HỒ SƠ NGUỒN] ",
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=THEME['yellow']
            )
            tier_badge.pack(side="left", padx=4)
        
        lbl_pillar = ctk.CTkLabel(
            header_row,
            text=f" [{pillar}] ",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=THEME['mauve']
        )
        lbl_pillar.pack(side="left", padx=6)
        
        lbl_status = ctk.CTkLabel(
            header_row,
            text=f"● {status}",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=status_color
        )
        lbl_status.pack(side="left")

        # Buttons on Right
        btn_box = ctk.CTkFrame(header_row, fg_color="transparent")
        btn_box.pack(side="right")
        
        btn_open = ctk.CTkButton(
            btn_box,
            text="📄 Mở Quy Trình",
            width=85,
            height=26,
            fg_color=THEME['mauve'],
            text_color="#1e1e2e",
            font=ctk.CTkFont(size=11, weight="bold"),
            command=lambda d=item: self.open_local_file(d)
        )
        btn_open.pack(side="left", padx=2)
        
        btn_remote = ctk.CTkButton(
            btn_box,
            text="🌐 Ổ Mạng",
            width=70,
            height=26,
            fg_color=THEME['surface2'],
            text_color=THEME['text'],
            font=ctk.CTkFont(size=11),
            command=lambda d=item: self.open_remote_file(d)
        )
        btn_remote.pack(side="left", padx=2)

        # Title & Governance Linkage
        title_box = ctk.CTkFrame(card, fg_color="transparent")
        title_box.pack(fill="x", padx=12, pady=(0, 6))

        lbl_name = ctk.CTkLabel(
            title_box,
            text=f"Tên văn bản: {title}",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=THEME['text']
        )
        lbl_name.pack(anchor="w")

        parent_ref = item.get('parent_ref', '')
        if is_master:
            link_text = "👑 QUY ĐỊNH NGUỒN CỐT LÕI — Căn cứ pháp lý cao nhất; toàn bộ biểu mẫu và quy trình tác nghiệp con phải tuân theo."
            link_color = THEME['yellow']
        else:
            link_text = f"🔗 Quy định nguồn gốc đối chiếu: {parent_ref} (Quy định chi tiết này được ban hành căn cứ theo hồ sơ nguồn)"
            link_color = THEME['blue']

        lbl_link = ctk.CTkLabel(
            title_box,
            text=link_text,
            font=ctk.CTkFont(size=11, slant="italic"),
            text_color=link_color
        )
        lbl_link.pack(anchor="w", pady=(2, 0))

        # 7-Element Grid
        grid_frame = ctk.CTkFrame(card, fg_color=THEME['surface0'], corner_radius=6)
        grid_frame.pack(fill="x", padx=12, pady=(0, 10))
        grid_frame.grid_columnconfigure(1, weight=1)
        grid_frame.grid_columnconfigure(3, weight=1)

        def add_gov_row(row_idx, col1, val1, col2, val2):
            ctk.CTkLabel(grid_frame, text=col1, font=ctk.CTkFont(size=11, weight="bold"), text_color=THEME['subtext']).grid(row=row_idx, column=0, padx=8, pady=3, sticky="nw")
            ctk.CTkLabel(grid_frame, text=val1, font=ctk.CTkFont(size=11), text_color=THEME['text'], wraplength=420, justify="left").grid(row=row_idx, column=1, padx=6, pady=3, sticky="w")
            ctk.CTkLabel(grid_frame, text=col2, font=ctk.CTkFont(size=11, weight="bold"), text_color=THEME['subtext']).grid(row=row_idx, column=2, padx=8, pady=3, sticky="nw")
            ctk.CTkLabel(grid_frame, text=val2, font=ctk.CTkFont(size=11), text_color=THEME['text'], wraplength=420, justify="left").grid(row=row_idx, column=3, padx=6, pady=3, sticky="w")

        add_gov_row(0, "🏢 Đơn vị sở hữu:", item.get('so_huu', ''), "🎯 Kiểm soát gì:", item.get('kiem_soat', ''))
        add_gov_row(1, "📁 Hồ sơ / Form:", item.get('ho_so', ''), "⚠️ Rủi ro tiềm ẩn:", item.get('rui_ro', ''))
        add_gov_row(2, "⚡ Kết quả / Xử lý:", item.get('ket_qua', ''), "💾 Lưu trữ & Thời hạn:", item.get('luu_tru', ''))

    # =========================================================================
    # TAB 3: CẬP NHẬT & ĐỒNG BỘ (2 CHẾ ĐỘ RÕ RÀNG)
    # =========================================================================
    def setup_tab_sync(self):
        self.tab_sync.grid_rowconfigure(1, weight=1)
        self.tab_sync.grid_columnconfigure(0, weight=1)
        
        # 1. Top Control Bar with 2 Clear Buttons
        top_bar = ctk.CTkFrame(self.tab_sync, fg_color=THEME['surface1'], corner_radius=8)
        top_bar.grid(row=0, column=0, padx=8, pady=6, sticky="ew")
        
        lbl_info = ctk.CTkLabel(
            top_bar,
            text="⚙️ Chọn Phân Hệ Cần Cập Nhật:",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=THEME['text']
        )
        lbl_info.pack(side="left", padx=10, pady=8)
        
        btn_sel_all = ctk.CTkButton(
            top_bar, text="✓ Chọn Tất Cả", width=85, height=28, fg_color=THEME['surface2'], font=ctk.CTkFont(size=11),
            command=self.select_all_sync_modules
        )
        btn_sel_all.pack(side="left", padx=3)
        
        btn_desel_all = ctk.CTkButton(
            top_bar, text="✗ Bỏ Chọn", width=75, height=28, fg_color=THEME['surface2'], font=ctk.CTkFont(size=11),
            command=self.deselect_all_sync_modules
        )
        btn_desel_all.pack(side="left", padx=3)
        
        # 2 Clear Sync Buttons: Fast vs Full
        self.btn_full_sync = ctk.CTkButton(
            top_bar,
            text="🔄 Đồng Bộ Toàn Bộ (Full Sync)",
            fg_color=THEME['surface2'],
            hover_color=THEME['card_hover'],
            text_color=THEME['text'],
            height=32,
            font=ctk.CTkFont(size=11, weight="bold"),
            command=lambda: self.start_sync_process(mode="full")
        )
        self.btn_full_sync.pack(side="right", padx=(4, 10), pady=8)

        self.btn_fast_sync = ctk.CTkButton(
            top_bar,
            text="⚡ Cập Nhật Nhanh (Chỉ File Mới)",
            fg_color=THEME['green'],
            hover_color="#89d682",
            text_color="#1e1e2e",
            height=32,
            font=ctk.CTkFont(size=11, weight="bold"),
            command=lambda: self.start_sync_process(mode="fast")
        )
        self.btn_fast_sync.pack(side="right", padx=4, pady=8)

        # 2. Split Content (Left: Checkboxes, Right: Progress & Log)
        content_split = ctk.CTkFrame(self.tab_sync, fg_color="transparent")
        content_split.grid(row=1, column=0, padx=8, pady=4, sticky="nsew")
        content_split.grid_rowconfigure(0, weight=1)
        content_split.grid_columnconfigure(0, weight=4)
        content_split.grid_columnconfigure(1, weight=6)
        
        scroll_modules = ctk.CTkScrollableFrame(
            content_split, 
            fg_color=THEME['surface1'], 
            corner_radius=8,
            label_text="Danh Sách 8 Phân Hệ Quản Lý"
        )
        scroll_modules.grid(row=0, column=0, padx=(0, 4), sticky="nsew")
        scroll_modules.grid_columnconfigure(0, weight=1)
        
        self.sync_checkboxes = {}
        for m in self.modules:
            mod_frame = ctk.CTkFrame(scroll_modules, fg_color=THEME['surface0'], corner_radius=6)
            mod_frame.pack(fill="x", padx=4, pady=3)
            
            var = tk.IntVar(value=1)
            chk = ctk.CTkCheckBox(
                mod_frame,
                text=m['name'],
                variable=var,
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color=THEME['text']
            )
            chk.pack(anchor="w", padx=8, pady=(5, 2))
            
            sub_lbl = ctk.CTkLabel(
                mod_frame,
                text=f"📁 {m['local_subfolder']} | Cập nhật: {m['last_sync']}",
                font=ctk.CTkFont(size=10),
                text_color=THEME['subtext']
            )
            sub_lbl.pack(anchor="w", padx=32, pady=(0, 5))
            
            self.sync_checkboxes[m['id']] = (var, sub_lbl)
            
        # Right Log Box
        right_box = ctk.CTkFrame(content_split, fg_color=THEME['surface1'], corner_radius=8)
        right_box.grid(row=0, column=1, padx=(4, 0), sticky="nsew")
        right_box.grid_rowconfigure(2, weight=1)
        right_box.grid_columnconfigure(0, weight=1)
        
        self.prog_bar = ctk.CTkProgressBar(right_box, fg_color=THEME['surface0'], progress_color=THEME['blue'])
        self.prog_bar.set(0)
        self.prog_bar.grid(row=0, column=0, padx=10, pady=(10, 4), sticky="ew")
        
        self.lbl_sync_status = ctk.CTkLabel(
            right_box,
            text="Sẵn sàng: Chọn chế độ 'Cập Nhật Nhanh' hoặc 'Đồng Bộ Toàn Bộ'...",
            font=ctk.CTkFont(size=11),
            text_color=THEME['subtext']
        )
        self.lbl_sync_status.grid(row=1, column=0, padx=10, pady=(0, 6), sticky="w")
        
        self.txt_sync_log = ctk.CTkTextbox(
            right_box,
            fg_color=THEME['surface0'],
            text_color=THEME['text'],
            font=ctk.CTkFont(family="Consolas", size=11)
        )
        self.txt_sync_log.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="nsew")

    def select_all_sync_modules(self):
        for var, _ in self.sync_checkboxes.values():
            var.set(1)

    def deselect_all_sync_modules(self):
        for var, _ in self.sync_checkboxes.values():
            var.set(0)

    def log_sync(self, msg):
        self.txt_sync_log.insert("end", msg + "\n")
        self.txt_sync_log.see("end")
        self.lbl_sync_status.configure(text=msg)

    def start_sync_process(self, mode="fast"):
        if self.sync_thread and self.sync_thread.is_alive():
            messagebox.showwarning("Đang Đồng Bộ", "Tiến trình đồng bộ đang chạy. Vui lòng đợi hoàn thành!")
            return
        if self.storage_thread and self.storage_thread.is_alive():
            messagebox.showwarning("Đang Xử Lý Kho", "Tiến trình di chuyển/xóa kho đang chạy. Vui lòng đợi hoàn thành trước khi đồng bộ!")
            return
            
        selected_ids = [m_id for m_id, (var, _) in self.sync_checkboxes.items() if var.get() == 1]
        if not selected_ids:
            messagebox.showinfo("Chưa Chọn Mục", "Vui lòng tích chọn ít nhất 1 phân hệ!")
            return
            
        mode_label = "⚡ CẬP NHẬT NHANH (CHỈ FILE MỚI)" if mode == "fast" else "🔄 ĐỒNG BỘ TOÀN BỘ"
        self.txt_sync_log.delete("1.0", "end")
        self.log_sync(f"🚀 Bắt đầu: {mode_label} ({len(selected_ids)} phân hệ)...")
        self.prog_bar.set(0)
        self.btn_fast_sync.configure(state="disabled")
        self.btn_full_sync.configure(state="disabled")
        
        def run():
            try:
                total_mods = len(selected_ids)
                for idx, mod_id in enumerate(selected_ids, 1):
                    cfg_path = None
                    for m in self.modules:
                        if m['id'] == mod_id:
                            cfg_path = m['path']
                            break
                    if cfg_path:
                        self.ui_call(self.log_sync, "--------------------------------------------------")
                        self.ui_call(self.log_sync, f"[{idx}/{total_mods}] Phân hệ: {mod_id}")
                        sync_single_module(cfg_path, mode=mode, progress_callback=lambda msg: self.ui_call(self.log_sync, msg))
                        self.ui_call(self.prog_bar.set, idx / total_mods)
                        
                self.ui_call(self.log_sync, "--------------------------------------------------")
                self.ui_call(self.log_sync, "Đang làm mới cơ sở dữ liệu và Ma Trận Quản Trị...")
                rebuild_consolidated_catalog()
                try:
                    from governance_matrix import build_governance_matrix
                    build_governance_matrix()
                except Exception:
                    pass
                self.ui_call(self.log_sync, "✅ ĐỒNG BỘ HOÀN TẤT THÀNH CÔNG 100%!")
                self.ui_call(self.on_sync_finished)
            except Exception as e:
                err_txt = str(e)
                self.ui_call(self.log_sync, f"❌ LỖI: {err_txt}")
                self.ui_call(lambda msg=err_txt: messagebox.showerror("Lỗi Cập Nhật", msg))
                self.ui_call(self.on_sync_finished)
                
        self.sync_thread = threading.Thread(target=run, daemon=True)
        self.sync_thread.start()

    def refresh_gov_tier_labels(self):
        if not hasattr(self, 'cmb_gov_tier'):
            return
        total = len(self.governance_data)
        masters = sum(1 for x in self.governance_data if x.get('is_master_root'))
        details = total - masters
        cur = self.gov_tier_var.get()
        v_all = f"Tất Cả ({total:,})"
        v_master = f"👑 Chỉ Hồ Sơ Nguồn Chuẩn ({masters:,})"
        v_detail = f"📄 Hồ Sơ Triển Khai ({details:,})"
        self.cmb_gov_tier.configure(values=[v_all, v_master, v_detail])
        if "Chỉ Hồ Sơ Nguồn" in cur or "👑" in cur:
            self.gov_tier_var.set(v_master)
        elif "Triển Khai" in cur or "📄" in cur:
            self.gov_tier_var.set(v_detail)
        else:
            self.gov_tier_var.set(v_all)

    def reload_all_data(self):
        self.load_modules_list()
        self.load_catalog_data()
        self.load_gov_data()
        self.refresh_stats()
        self.refresh_gov_tier_labels()
        if hasattr(self, 'sync_checkboxes'):
            mod_map = {m['id']: m for m in self.modules}
            for mid, (_, sub_lbl) in self.sync_checkboxes.items():
                if mid in mod_map:
                    m = mod_map[mid]
                    sub_lbl.configure(text=f"📁 {m['local_subfolder']} | File: {m['total_files']:,} | Cập nhật: {m['last_sync']}")
        self.apply_search_filter()
        self.apply_gov_filter()
        self.refresh_storage_ui_async()

    def on_sync_finished(self):
        self.btn_fast_sync.configure(state="normal")
        self.btn_full_sync.configure(state="normal")
        self.reload_all_data()
        messagebox.showinfo("Thành Công", "Quá trình cập nhật hoàn tất! Dữ liệu tra cứu và Ma Trận Quản Trị đã được làm mới.")

    # =========================================================================
    # TAB 4: QUẢN LÝ KHO LƯU TRỮ, DI CHUYỂN, ĐỔI LINK & XÓA TÀI LIỆU
    # =========================================================================
    def setup_tab_storage(self):
        self.tab_storage.grid_rowconfigure(0, weight=1)
        self.tab_storage.grid_columnconfigure(0, weight=5)
        self.tab_storage.grid_columnconfigure(1, weight=5)

        # LEFT PANEL: Scrollable controls for Storage Info, Move, Relink, Bulk Delete
        left_scroll = ctk.CTkScrollableFrame(self.tab_storage, fg_color="transparent")
        left_scroll.grid(row=0, column=0, padx=(6, 4), pady=6, sticky="nsew")
        left_scroll.grid_columnconfigure(0, weight=1)

        # --- CARD 1: CURRENT STORAGE INFO ---
        card_info = ctk.CTkFrame(left_scroll, fg_color=THEME['surface1'], corner_radius=8)
        card_info.pack(fill="x", padx=2, pady=(0, 8))

        ctk.CTkLabel(
            card_info,
            text="📍 1. HIỆN TRẠNG KHO LƯU TRỮ",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=THEME['blue']
        ).pack(anchor="w", padx=12, pady=(10, 4))

        self.lbl_app_dir_info = ctk.CTkLabel(
            card_info,
            text=f"🐍 Thư mục App & Data (Cố định): {BASE_DIR}",
            font=ctk.CTkFont(size=11),
            text_color=THEME['subtext'],
            wraplength=560,
            justify="left"
        )
        self.lbl_app_dir_info.pack(anchor="w", padx=12, pady=(0, 2))

        self.lbl_storage_root_info = ctk.CTkLabel(
            card_info,
            text=f"💾 Kho PDF hiện tại: {get_storage_root()}",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=THEME['sky'],
            wraplength=560,
            justify="left"
        )
        self.lbl_storage_root_info.pack(anchor="w", padx=12, pady=(2, 2))

        self.lbl_storage_summary = ctk.CTkLabel(
            card_info,
            text="Đang tính toán dung lượng kho...",
            font=ctk.CTkFont(size=11),
            text_color=THEME['text'],
            justify="left"
        )
        self.lbl_storage_summary.pack(anchor="w", padx=12, pady=(2, 6))

        info_btns = ctk.CTkFrame(card_info, fg_color="transparent")
        info_btns.pack(fill="x", padx=12, pady=(0, 10))

        ctk.CTkButton(
            info_btns, text="📁 Mở Kho PDF", width=110, height=28,
            fg_color=THEME['surface2'], hover_color=THEME['card_hover'],
            font=ctk.CTkFont(size=11), command=self.open_current_storage_folder
        ).pack(side="left", padx=(0, 6))

        ctk.CTkButton(
            info_btns, text="🔄 Quét Kiểm Tra Lại Link", width=165, height=28,
            fg_color=THEME['blue'], text_color="#1e1e2e",
            font=ctk.CTkFont(size=11, weight="bold"), command=self.start_verify_links_task
        ).pack(side="left", padx=(0, 6))

        ctk.CTkButton(
            info_btns, text="📊 Làm Mới Thống Kê", width=135, height=28,
            fg_color=THEME['surface2'], hover_color=THEME['card_hover'],
            font=ctk.CTkFont(size=11), command=self.refresh_storage_ui_async
        ).pack(side="left")

        # --- CARD 2: MOVE STORAGE / MODULES & AUTO-RELINK ---
        card_move = ctk.CTkFrame(left_scroll, fg_color=THEME['surface1'], corner_radius=8)
        card_move.pack(fill="x", padx=2, pady=(0, 8))

        ctk.CTkLabel(
            card_move,
            text="🚚 2. DI CHUYỂN TÀI LIỆU SANG ĐỊA CHỈ MỚI (TỰ ĐỘNG ĐỔI LINK)",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=THEME['green']
        ).pack(anchor="w", padx=12, pady=(10, 2))

        ctk.CTkLabel(
            card_move,
            text="Dời toàn bộ file PDF (hoặc chọn từng phân hệ) sang ổ đĩa / thư mục khác. "
                 "Thư mục App chỉ giữ lại mã nguồn Python và dữ liệu JSON, mọi link sẽ tự động cập nhật.",
            font=ctk.CTkFont(size=11),
            text_color=THEME['subtext'],
            wraplength=560,
            justify="left"
        ).pack(anchor="w", padx=12, pady=(0, 6))

        dest_row = ctk.CTkFrame(card_move, fg_color="transparent")
        dest_row.pack(fill="x", padx=12, pady=(0, 6))
        dest_row.grid_columnconfigure(0, weight=1)

        self.move_dest_var = tk.StringVar()
        ctk.CTkEntry(
            dest_row,
            textvariable=self.move_dest_var,
            placeholder_text="Chọn thư mục đích mới (VD: D:\\KhoTaiLieuMBC)...",
            height=32,
            font=ctk.CTkFont(size=12)
        ).grid(row=0, column=0, sticky="ew", padx=(0, 6))

        ctk.CTkButton(
            dest_row, text="📂 Chọn Thư Mục", width=120, height=32,
            fg_color=THEME['surface2'], hover_color=THEME['card_hover'],
            font=ctk.CTkFont(size=11, weight="bold"),
            command=self.browse_move_dest
        ).grid(row=0, column=1)

        # Scope Selector: All 8 Modules vs Selected Modules
        scope_row = ctk.CTkFrame(card_move, fg_color="transparent")
        scope_row.pack(fill="x", padx=12, pady=(2, 4))

        ctk.CTkLabel(scope_row, text="Phạm vi dời:", font=ctk.CTkFont(size=11, weight="bold"), text_color=THEME['text']).pack(side="left", padx=(0, 8))
        self.move_scope_var = tk.StringVar(value="Toàn Bộ 8 Phân Hệ")
        ctk.CTkSegmentedButton(
            scope_row,
            values=["Toàn Bộ 8 Phân Hệ", "Chọn Từng Phân Hệ"],
            variable=self.move_scope_var,
            command=self.on_move_scope_changed,
            height=28
        ).pack(side="left")

        # Collapsible module checklist (shown only when "Chọn Từng Phân Hệ")
        self.move_mod_box = ctk.CTkFrame(card_move, fg_color=THEME['surface0'], corner_radius=6)
        self.move_mod_vars = {}
        for idx_m, m in enumerate(self.modules):
            mv = tk.IntVar(value=1)
            cb = ctk.CTkCheckBox(
                self.move_mod_box,
                text=m['name'],
                variable=mv,
                font=ctk.CTkFont(size=11),
                checkbox_width=18,
                checkbox_height=18
            )
            cb.grid(row=idx_m // 2, column=idx_m % 2, padx=8, pady=3, sticky="w")
            self.move_mod_vars[m['id']] = mv

        # Options Checkboxes
        self.move_opts_box = ctk.CTkFrame(card_move, fg_color="transparent")
        self.move_opts_box.pack(fill="x", padx=12, pady=(4, 6))

        self.var_keep_excel_app = tk.BooleanVar(value=True)
        ctk.CTkCheckBox(
            self.move_opts_box,
            text="Chỉ di chuyển file PDF — giữ lại 8 file Excel tổng tại App/master_excels/",
            variable=self.var_keep_excel_app,
            font=ctk.CTkFont(size=11)
        ).pack(anchor="w", pady=2)

        self.var_move_copy_only = tk.BooleanVar(value=False)
        ctk.CTkCheckBox(
            self.move_opts_box,
            text="Sao chép thay vì di chuyển (Giữ nguyên bản gốc tại vị trí cũ)",
            variable=self.var_move_copy_only,
            font=ctk.CTkFont(size=11)
        ).pack(anchor="w", pady=2)

        self.var_move_cleanup = tk.BooleanVar(value=True)
        ctk.CTkCheckBox(
            self.move_opts_box,
            text="Tự động dọn các thư mục con rỗng ở vị trí cũ sau khi di chuyển xong",
            variable=self.var_move_cleanup,
            font=ctk.CTkFont(size=11)
        ).pack(anchor="w", pady=2)

        move_btn_row = ctk.CTkFrame(card_move, fg_color="transparent")
        move_btn_row.pack(fill="x", padx=12, pady=(2, 10))

        self.btn_start_move = ctk.CTkButton(
            move_btn_row,
            text="🚚 Bắt Đầu Di Chuyển & Tự Đổi Link",
            height=34,
            fg_color=THEME['green'],
            hover_color="#89d682",
            text_color="#1e1e2e",
            font=ctk.CTkFont(size=12, weight="bold"),
            command=self.start_move_storage_task
        )
        self.btn_start_move.pack(side="left", fill="x", expand=True, padx=(0, 6))

        self.btn_cancel_move = ctk.CTkButton(
            move_btn_row,
            text="⏹ Dừng An Toàn",
            width=115,
            height=34,
            fg_color=THEME['red'],
            hover_color="#d97290",
            text_color="#1e1e2e",
            font=ctk.CTkFont(size=11, weight="bold"),
            state="disabled",
            command=self.cancel_storage_task
        )
        self.btn_cancel_move.pack(side="left")

        # --- CARD 3: RELINK STORAGE ROOT (WITHOUT MOVING FILES) ---
        card_relink = ctk.CTkFrame(left_scroll, fg_color=THEME['surface1'], corner_radius=8)
        card_relink.pack(fill="x", padx=2, pady=(0, 8))

        ctk.CTkLabel(
            card_relink,
            text="🔗 3. CẬP NHẬT ĐỊA CHỈ KHO TÀI LIỆU (KHÔNG DI CHUYỂN FILE)",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=THEME['yellow']
        ).pack(anchor="w", padx=12, pady=(10, 2))

        ctk.CTkLabel(
            card_relink,
            text="Dùng khi bạn đã tự Cut/Copy thư mục PDF sang ổ đĩa khác bằng Windows Explorer "
                 "hoặc chuyển thư mục App sang máy khác và cần nối lại link ngay lập tức.",
            font=ctk.CTkFont(size=11),
            text_color=THEME['subtext'],
            wraplength=560,
            justify="left"
        ).pack(anchor="w", padx=12, pady=(0, 6))

        relink_row = ctk.CTkFrame(card_relink, fg_color="transparent")
        relink_row.pack(fill="x", padx=12, pady=(0, 4))
        relink_row.grid_columnconfigure(0, weight=1)

        self.relink_dest_var = tk.StringVar()
        ctk.CTkEntry(
            relink_row,
            textvariable=self.relink_dest_var,
            placeholder_text="Chọn thư mục đang chứa các file PDF đã dời...",
            height=32,
            font=ctk.CTkFont(size=12)
        ).grid(row=0, column=0, sticky="ew", padx=(0, 6))

        ctk.CTkButton(
            relink_row, text="📂 Chọn Thư Mục", width=120, height=32,
            fg_color=THEME['surface2'], hover_color=THEME['card_hover'],
            font=ctk.CTkFont(size=11, weight="bold"),
            command=self.browse_relink_dest
        ).grid(row=0, column=1)

        self.var_smart_scan = tk.BooleanVar(value=True)
        ctk.CTkCheckBox(
            card_relink,
            text="Dò tìm thông minh theo tên file (tự nối link kể cả khi bạn đã đổi tên thư mục con)",
            variable=self.var_smart_scan,
            font=ctk.CTkFont(size=11)
        ).pack(anchor="w", padx=12, pady=(2, 6))

        self.btn_relink_root = ctk.CTkButton(
            card_relink,
            text="🔗 Cập Nhật Địa Chỉ Kho & Nối Lại Link",
            height=34,
            fg_color=THEME['yellow'],
            hover_color="#e5cd98",
            text_color="#1e1e2e",
            font=ctk.CTkFont(size=12, weight="bold"),
            command=self.start_relink_storage_task
        )
        self.btn_relink_root.pack(fill="x", padx=12, pady=(0, 10))

        # --- CARD 4: BULK DELETE / CLEANUP ---
        card_del = ctk.CTkFrame(left_scroll, fg_color=THEME['surface1'], corner_radius=8)
        card_del.pack(fill="x", padx=2, pady=(0, 4))

        ctk.CTkLabel(
            card_del,
            text="🗑️ 4. DỌN DẸP & XÓA TÀI LIỆU HÀNG LOẠT",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=THEME['red']
        ).pack(anchor="w", padx=12, pady=(10, 2))

        ctk.CTkLabel(
            card_del,
            text="Xóa bớt file PDF trên ổ cứng để giải phóng dung lượng (mặc định đưa vào Thùng Rác Windows "
                 "và có tùy chọn giữ lại danh mục tra cứu để tải lại khi cần).",
            font=ctk.CTkFont(size=11),
            text_color=THEME['subtext'],
            wraplength=560,
            justify="left"
        ).pack(anchor="w", padx=12, pady=(0, 6))

        del_row1 = ctk.CTkFrame(card_del, fg_color="transparent")
        del_row1.pack(fill="x", padx=12, pady=(0, 6))

        ctk.CTkButton(
            del_row1,
            text="🧹 Xóa Toàn Bộ File PDF Đã Hủy Trên Ổ Cứng",
            height=30,
            fg_color=THEME['peach'],
            hover_color="#e59c72",
            text_color="#1e1e2e",
            font=ctk.CTkFont(size=11, weight="bold"),
            command=self.action_delete_canceled_pdfs
        ).pack(fill="x")

        del_row2 = ctk.CTkFrame(card_del, fg_color="transparent")
        del_row2.pack(fill="x", padx=12, pady=(0, 10))

        mod_opt_names = [m['name'] for m in self.modules] if self.modules else ["(Chưa có phân hệ)"]
        self.del_mod_var = tk.StringVar(value=mod_opt_names[0])
        ctk.CTkOptionMenu(
            del_row2,
            values=mod_opt_names,
            variable=self.del_mod_var,
            height=30,
            font=ctk.CTkFont(size=11)
        ).pack(side="left", fill="x", expand=True, padx=(0, 6))

        ctk.CTkButton(
            del_row2,
            text="🗑️ Xóa Phân Hệ Này...",
            width=145,
            height=30,
            fg_color=THEME['red'],
            hover_color="#d97290",
            text_color="#1e1e2e",
            font=ctk.CTkFont(size=11, weight="bold"),
            command=self.action_delete_module_docs
        ).pack(side="left")

        # RIGHT PANEL: Direct grid (no nested scroll!) with Module Table + Progress + Log
        right_panel = ctk.CTkFrame(self.tab_storage, fg_color=THEME['surface1'], corner_radius=8)
        right_panel.grid(row=0, column=1, padx=(4, 6), pady=6, sticky="nsew")
        right_panel.grid_rowconfigure(1, weight=4)
        right_panel.grid_rowconfigure(4, weight=6)
        right_panel.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            right_panel,
            text="📊 Thống Kê Dung Lượng & Trạng Thái Cục Bộ Theo Phân Hệ",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=THEME['blue']
        ).grid(row=0, column=0, padx=10, pady=(10, 4), sticky="w")

        tbl_wrap = ctk.CTkFrame(right_panel, fg_color=THEME['surface0'])
        tbl_wrap.grid(row=1, column=0, padx=10, pady=(0, 8), sticky="nsew")
        tbl_wrap.grid_rowconfigure(0, weight=1)
        tbl_wrap.grid_columnconfigure(0, weight=1)

        st_cols = ("module", "ready", "canceled", "size")
        self.storage_tree = ttk.Treeview(tbl_wrap, columns=st_cols, show="headings", height=8)
        self.storage_tree.heading("module", text="Phân Hệ")
        self.storage_tree.heading("ready", text="Sẵn Sàng / Tổng")
        self.storage_tree.heading("canceled", text="Đã Hủy (Cục Bộ)")
        self.storage_tree.heading("size", text="Dung Lượng")
        self.storage_tree.column("module", width=220, anchor="w")
        self.storage_tree.column("ready", width=110, anchor="center")
        self.storage_tree.column("canceled", width=105, anchor="center")
        self.storage_tree.column("size", width=95, anchor="e")
        st_sb = ttk.Scrollbar(tbl_wrap, orient="vertical", command=self.storage_tree.yview)
        self.storage_tree.configure(yscrollcommand=st_sb.set)
        self.storage_tree.grid(row=0, column=0, sticky="nsew")
        st_sb.grid(row=0, column=1, sticky="ns")

        self.storage_prog_bar = ctk.CTkProgressBar(right_panel, fg_color=THEME['surface0'], progress_color=THEME['green'])
        self.storage_prog_bar.set(0)
        self.storage_prog_bar.grid(row=2, column=0, padx=10, pady=(2, 4), sticky="ew")

        self.lbl_storage_status = ctk.CTkLabel(
            right_panel,
            text="Sẵn sàng thực hiện di chuyển, cập nhật địa chỉ hoặc dọn dẹp tài liệu...",
            font=ctk.CTkFont(size=11),
            text_color=THEME['subtext']
        )
        self.lbl_storage_status.grid(row=3, column=0, padx=10, pady=(0, 4), sticky="w")

        self.txt_storage_log = ctk.CTkTextbox(
            right_panel,
            fg_color=THEME['surface0'],
            text_color=THEME['text'],
            font=ctk.CTkFont(family="Consolas", size=11)
        )
        self.txt_storage_log.grid(row=4, column=0, padx=10, pady=(0, 10), sticky="nsew")

    def on_move_scope_changed(self, value):
        if "Từng" in value:
            self.move_mod_box.pack(fill="x", padx=12, pady=(2, 4), before=self.move_opts_box)
        else:
            self.move_mod_box.pack_forget()

    def browse_move_dest(self):
        chosen = filedialog.askdirectory(title="Chọn Thư Mục Đích Chứa Tài Liệu PDF")
        if chosen:
            self.move_dest_var.set(os.path.normpath(chosen))

    def browse_relink_dest(self):
        chosen = filedialog.askdirectory(title="Chọn Thư Mục Kho PDF Đã Chuyển Tới")
        if chosen:
            self.relink_dest_var.set(os.path.normpath(chosen))

    def log_storage(self, msg, pct=None):
        if hasattr(self, 'txt_storage_log'):
            self.txt_storage_log.insert("end", msg + "\n")
            self.txt_storage_log.see("end")
        if hasattr(self, 'lbl_storage_status'):
            first_line = msg.splitlines()[0] if msg else ""
            self.lbl_storage_status.configure(text=first_line)
        if pct is not None and hasattr(self, 'storage_prog_bar'):
            self.storage_prog_bar.set(max(0.0, min(1.0, float(pct))))

    def _set_storage_busy(self, busy: bool):
        st = "disabled" if busy else "normal"
        if hasattr(self, 'btn_start_move'):
            self.btn_start_move.configure(state=st)
        if hasattr(self, 'btn_relink_root'):
            self.btn_relink_root.configure(state=st)
        if hasattr(self, 'btn_cancel_move'):
            self.btn_cancel_move.configure(state="normal" if busy else "disabled")

    def _is_storage_busy(self) -> bool:
        if self.storage_thread and self.storage_thread.is_alive():
            messagebox.showwarning("Đang Xử Lý", "Một tác vụ quản lý kho đang chạy. Vui lòng đợi hoàn tất!")
            return True
        if self.sync_thread and self.sync_thread.is_alive():
            messagebox.showwarning("Đang Đồng Bộ", "Tiến trình đồng bộ đang chạy. Vui lòng đợi hoàn tất!")
            return True
        return False

    def cancel_storage_task(self):
        self.storage_cancel_event.set()
        self.log_storage("⏹ Đang dừng an toàn sau file hiện tại...")

    def refresh_storage_ui_async(self):
        if self._storage_summary_running:
            return
        self._storage_summary_running = True

        def worker():
            try:
                summary = get_storage_summary()
                self.ui_call(self._apply_storage_summary_ui, summary)
            except Exception as e:
                print(f"Storage summary error: {e}")
            finally:
                self._storage_summary_running = False
        threading.Thread(target=worker, daemon=True).start()

    def _apply_storage_summary_ui(self, s: dict):
        if not hasattr(self, 'lbl_storage_root_info'):
            return
        sep_text = "✅ Đã tách riêng PDF khỏi thư mục App" if s['is_separated'] else "📁 Đang nằm chung thư mục App"
        self.lbl_storage_root_info.configure(
            text=f"💾 Kho PDF hiện tại: {s['storage_root']}  ({sep_text})",
            text_color=THEME['green'] if s['is_separated'] else THEME['sky']
        )
        total_mb = s['total_bytes'] / (1024 ** 2)
        size_str = f"{total_mb / 1024:.2f} GB" if total_mb >= 1024 else f"{total_mb:.1f} MB"
        excel_mb = s['excel_bytes'] / (1024 ** 2)
        extra_custom = f" • Link riêng lẻ ngoài kho: {s['custom_path_docs']:,}" if s['custom_path_docs'] else ""
        self.lbl_storage_summary.configure(
            text=f"📄 PDF cục bộ: {s['existing_docs']:,} / {s['total_docs']:,} ({size_str}) • "
                 f"Chưa có file: {s['missing_docs']:,} • Excel tổng: {s['excel_count']} file ({excel_mb:.1f} MB){extra_custom}"
        )

        if hasattr(self, 'storage_tree'):
            self.storage_tree.delete(*self.storage_tree.get_children())
            for m in s.get('modules', []):
                mb = m['bytes'] / (1024 ** 2)
                m_sz = f"{mb / 1024:.2f} GB" if mb >= 1024 else f"{mb:.1f} MB"
                self.storage_tree.insert(
                    "", "end",
                    values=(
                        m['name'],
                        f"{m['existing']:,} / {m['total']:,}",
                        f"{m['canceled_existing']:,}",
                        m_sz
                    )
                )

    def start_verify_links_task(self):
        if self._is_storage_busy():
            return
        self.txt_storage_log.delete("1.0", "end")
        self.storage_prog_bar.set(0)
        self._set_storage_busy(True)

        def run():
            try:
                res = verify_all_links(progress_callback=lambda m, p=None: self.ui_call(self.log_storage, m, p))
                self.ui_call(
                    self._on_storage_task_done,
                    f"Kiểm tra liên kết hoàn tất!\n• Sẵn sàng cục bộ: {res['found']:,} / {res['total']:,}\n• Chưa có file: {res['missing']:,}"
                )
            except Exception as e:
                self.ui_call(self._on_storage_task_error, str(e))

        self.storage_thread = threading.Thread(target=run, daemon=True)
        self.storage_thread.start()

    def start_move_storage_task(self):
        if self._is_storage_busy():
            return
        dest = self.move_dest_var.get().strip()
        if not dest:
            messagebox.showwarning("Chưa Chọn Thư Mục Đích", "Vui lòng chọn thư mục đích muốn di chuyển tài liệu sang!")
            return

        is_partial = "Từng" in self.move_scope_var.get()
        selected_mods = None
        if is_partial:
            selected_mods = [mid for mid, var in self.move_mod_vars.items() if var.get() == 1]
            if not selected_mods:
                messagebox.showwarning("Chưa Chọn Phân Hệ", "Vui lòng tích chọn ít nhất 1 phân hệ để di chuyển!")
                return

        keep_excel = bool(self.var_keep_excel_app.get())
        copy_only = bool(self.var_move_copy_only.get())
        cleanup_empty = bool(self.var_move_cleanup.get())

        action_txt = "SAO CHÉP" if copy_only else "DI CHUYỂN"
        scope_txt = f"{len(selected_mods)} phân hệ đã chọn" if is_partial else "TOÀN BỘ 8 phân hệ"
        excel_txt = (
            "Giữ 8 file Excel tổng lại thư mục App/master_excels/"
            if keep_excel else "Di chuyển kèm cả 8 file Excel tổng sang thư mục đích"
        )
        confirm = messagebox.askyesno(
            f"Xác Nhận {action_txt} Kho Tài Liệu",
            f"Bạn có chắc chắn muốn {action_txt} {scope_txt}?\n\n"
            f"• Kho hiện tại: {get_storage_root()}\n"
            f"• Thư mục đích: {dest}\n"
            f"• Xử lý Excel tổng: {excel_txt}\n\n"
            f"Hệ thống sẽ tự kiểm tra kích thước file đích trước khi xóa file gốc và tự động cập nhật lại toàn bộ đường dẫn."
        )
        if not confirm:
            return

        self.storage_cancel_event.clear()
        self.txt_storage_log.delete("1.0", "end")
        self.storage_prog_bar.set(0)
        self._set_storage_busy(True)

        def run():
            try:
                stats = move_all_documents(
                    dest_root=dest,
                    module_ids=selected_mods,
                    include_excels=(not keep_excel),
                    keep_excel_in_app=keep_excel,
                    copy_only=copy_only,
                    cleanup_empty=cleanup_empty,
                    progress_callback=lambda m, p=None: self.ui_call(self.log_storage, m, p),
                    cancel_event=self.storage_cancel_event,
                )
                if not stats['ok'] and stats['moved'] == 0 and stats['error_details']:
                    self.ui_call(self._on_storage_task_error, "\n".join(stats['error_details'][:10]))
                    return

                mb = stats['bytes_moved'] / (1024 ** 2)
                summary_msg = (
                    f"{'Đã dừng an toàn giữa chừng!' if stats['cancelled'] else 'Hoàn tất di chuyển & cập nhật link!'}\n\n"
                    f"• File PDF đã xử lý: {stats['moved']:,} ({mb:.1f} MB)\n"
                    f"• Bỏ qua (đã ở đích): {stats['skipped_same']:,}\n"
                    f"• Chưa có file nguồn: {stats['missing_src']:,}\n"
                    f"• Thư mục rỗng đã dọn: {stats['empty_dirs_removed']:,}\n"
                    f"• Lỗi: {stats['errors']:,}\n"
                    f"• Kho PDF hiện tại: {get_storage_root()}"
                )
                if stats['error_details']:
                    summary_msg += "\n\nChi tiết lỗi đầu tiên:\n- " + "\n- ".join(stats['error_details'][:5])
                self.ui_call(self._on_storage_task_done, summary_msg)
            except Exception as e:
                self.ui_call(self._on_storage_task_error, str(e))

        self.storage_thread = threading.Thread(target=run, daemon=True)
        self.storage_thread.start()

    def start_relink_storage_task(self):
        if self._is_storage_busy():
            return
        new_root = self.relink_dest_var.get().strip()
        if not new_root or not path_exists(new_root):
            messagebox.showwarning("Thư Mục Không Hợp Lệ", "Vui lòng chọn một thư mục kho tài liệu hợp lệ đang tồn tại trên máy!")
            return

        smart_scan = bool(self.var_smart_scan.get())
        if not messagebox.askyesno(
            "Xác Nhận Cập Nhật Địa Chỉ Kho",
            f"Ứng dụng sẽ đổi địa chỉ kho lưu trữ sang:\n{new_root}\n\n"
            f"Thao tác này KHÔNG di chuyển hay xóa file nào — chỉ cập nhật lại liên kết cho toàn bộ danh mục.\nTiếp tục?"
        ):
            return

        self.txt_storage_log.delete("1.0", "end")
        self.storage_prog_bar.set(0)
        self._set_storage_busy(True)

        def run():
            try:
                stats = relink_storage_root(
                    new_root=new_root,
                    smart_scan=smart_scan,
                    progress_callback=lambda m, p=None: self.ui_call(self.log_storage, m, p),
                )
                if not stats.get('ok'):
                    self.ui_call(self._on_storage_task_error, stats.get('error', 'Lỗi cập nhật địa chỉ kho'))
                    return
                msg = (
                    f"Đã cập nhật địa chỉ kho tài liệu thành công!\n\n"
                    f"• Địa chỉ kho mới: {stats['new_root']}\n"
                    f"• Khớp tìm thấy: {stats['found']:,} / {stats['total']:,} tài liệu\n"
                    f"• Khớp nhờ dò thông minh: {stats['smart_matched']:,}\n"
                    f"• Chưa có file tại địa chỉ mới: {stats['missing']:,}"
                )
                self.ui_call(self._on_storage_task_done, msg)
            except Exception as e:
                self.ui_call(self._on_storage_task_error, str(e))

        self.storage_thread = threading.Thread(target=run, daemon=True)
        self.storage_thread.start()

    def _on_storage_task_done(self, info_msg: str):
        self._set_storage_busy(False)
        self.reload_all_data()
        messagebox.showinfo("Hoàn Tất", info_msg)

    def _on_storage_task_error(self, err_msg: str):
        self._set_storage_busy(False)
        self.log_storage(f"❌ LỖI: {err_msg}")
        self.reload_all_data()
        messagebox.showerror("Không Thể Thực Hiện", err_msg)

    def action_delete_canceled_pdfs(self):
        canceled_local = [d for d in self.catalog if d.get('is_canceled') and d.get('file_exists')]
        if not canceled_local:
            messagebox.showinfo("Không Có File Cần Dọn", "Hiện không có file PDF Đã Hủy nào đang lưu trên ổ cứng.")
            return
        self.open_delete_docs_dialog(
            canceled_local,
            title_override="🧹 Dọn File PDF Đã Hủy Trên Ổ Cứng",
            default_mode="disk_only"
        )

    def action_delete_module_docs(self):
        mod_name = self.del_mod_var.get()
        mod_docs = [d for d in self.catalog if d.get('module_name') == mod_name]
        if not mod_docs:
            messagebox.showinfo("Trống", f"Phân hệ '{mod_name}' không còn tài liệu nào trong danh mục.")
            return
        self.open_delete_docs_dialog(
            mod_docs,
            title_override=f"🗑️ Xóa Tài Liệu Phân Hệ: {mod_name}",
            default_mode="disk_only"
        )

    # =========================================================================
    # DIALOGS: EDIT LINK / MOVE SELECTED DOCS / DELETE DOCS
    # =========================================================================
    def open_edit_links_dialog(self, doc):
        dlg = ctk.CTkToplevel(self)
        dlg.title("🔗 Cập Nhật Địa Chỉ / Đổi Link Tài Liệu")
        dlg.geometry("700x380")
        dlg.minsize(600, 340)
        dlg.configure(fg_color=THEME['bg'])
        dlg.transient(self)
        dlg.grab_set()
        dlg.bind("<Escape>", lambda e: dlg.destroy())

        cur_local = doc.get('local_path', '')
        cur_resolved = resolve_local_path(cur_local)
        cur_remote = doc.get('remote_path', '')
        exists_now = is_file_exists(cur_resolved)

        ctk.CTkLabel(
            dlg,
            text=f"🔗 Cập Nhật Địa Chỉ: {doc.get('doc_code', '')}",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color=THEME['blue']
        ).pack(anchor="w", padx=16, pady=(14, 2))

        ctk.CTkLabel(
            dlg,
            text=f"{doc.get('doc_title', doc.get('filename', ''))}  •  Phân hệ: {doc.get('module_name', '')}",
            font=ctk.CTkFont(size=11),
            text_color=THEME['subtext'],
            wraplength=650,
            justify="left"
        ).pack(anchor="w", padx=16, pady=(0, 10))

        # Local path editor
        loc_card = ctk.CTkFrame(dlg, fg_color=THEME['surface1'], corner_radius=8)
        loc_card.pack(fill="x", padx=16, pady=(0, 10))

        status_badge = "🟢 File đang tồn tại" if exists_now else "🔴 File không tồn tại tại đường dẫn này"
        lbl_loc_st = ctk.CTkLabel(
            loc_card,
            text=f"Đường dẫn file cục bộ (PDF):  {status_badge}",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=THEME['green'] if exists_now else THEME['red']
        )
        lbl_loc_st.pack(anchor="w", padx=12, pady=(10, 4))

        loc_row = ctk.CTkFrame(loc_card, fg_color="transparent")
        loc_row.pack(fill="x", padx=12, pady=(0, 10))
        loc_row.grid_columnconfigure(0, weight=1)

        var_local = tk.StringVar(value=cur_resolved or cur_local)
        ctk.CTkEntry(loc_row, textvariable=var_local, height=34, font=ctk.CTkFont(size=11)).grid(
            row=0, column=0, sticky="ew", padx=(0, 6)
        )

        def browse_pdf():
            init_dir = os.path.dirname(cur_resolved) if cur_resolved and path_exists(os.path.dirname(cur_resolved)) else get_storage_root()
            picked = filedialog.askopenfilename(
                parent=dlg,
                title="Chọn File PDF Mới Cho Tài Liệu Này",
                initialdir=init_dir,
                filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
            )
            if picked:
                var_local.set(os.path.normpath(picked))
                lbl_loc_st.configure(text="Đường dẫn file cục bộ (PDF):  🟢 Đã chọn file hợp lệ", text_color=THEME['green'])

        ctk.CTkButton(
            loc_row, text="📂 Chọn File PDF", width=120, height=34,
            fg_color=THEME['blue'], text_color="#1e1e2e",
            font=ctk.CTkFont(size=11, weight="bold"), command=browse_pdf
        ).grid(row=0, column=1)

        # Remote path editor
        rem_card = ctk.CTkFrame(dlg, fg_color=THEME['surface1'], corner_radius=8)
        rem_card.pack(fill="x", padx=16, pady=(0, 14))

        ctk.CTkLabel(
            rem_card,
            text="Đường dẫn ổ mạng gốc (Remote Path — tùy chọn chỉnh sửa):",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=THEME['text']
        ).pack(anchor="w", padx=12, pady=(10, 4))

        var_remote = tk.StringVar(value=cur_remote)
        ctk.CTkEntry(rem_card, textvariable=var_remote, height=34, font=ctk.CTkFont(size=11)).pack(
            fill="x", padx=12, pady=(0, 10)
        )

        # Action Buttons
        btn_row = ctk.CTkFrame(dlg, fg_color="transparent")
        btn_row.pack(fill="x", padx=16, pady=(0, 12))

        def on_save():
            res = update_document_paths(
                module_id=doc.get('module_id', ''),
                remote_path=cur_remote,
                new_local_path=var_local.get().strip(),
                new_remote_path=var_remote.get().strip(),
            )
            if not res.get('ok'):
                messagebox.showerror("Lỗi Cập Nhật", res.get('error', 'Không thể lưu thay đổi.'), parent=dlg)
                return
            dlg.destroy()
            self.reload_all_data()
            st_txt = "🟢 Tồn tại" if res.get('file_exists') else "🔴 Chưa tìm thấy file tại đường dẫn mới"
            messagebox.showinfo(
                "Đã Cập Nhật Địa Chỉ",
                f"Đã lưu địa chỉ mới cho {doc.get('doc_code', '')}!\n\n"
                f"• Đường dẫn lưu: {res.get('local_path')}\n"
                f"• Trạng thái: {st_txt}"
            )

        ctk.CTkButton(
            btn_row, text="Hủy", width=90, height=34,
            fg_color=THEME['surface2'], command=dlg.destroy
        ).pack(side="right", padx=(6, 0))

        ctk.CTkButton(
            btn_row, text="💾 Lưu Địa Chỉ Mới", width=160, height=34,
            fg_color=THEME['green'], text_color="#1e1e2e",
            font=ctk.CTkFont(size=12, weight="bold"), command=on_save
        ).pack(side="right")

    def open_move_docs_dialog(self, docs):
        if not docs or self._is_storage_busy():
            return

        dlg = ctk.CTkToplevel(self)
        dlg.title(f"📦 Di Chuyển {len(docs):,} Tài Liệu")
        dlg.geometry("620x360")
        dlg.minsize(540, 320)
        dlg.configure(fg_color=THEME['bg'])
        dlg.transient(self)
        dlg.grab_set()
        dlg.bind("<Escape>", lambda e: dlg.destroy())

        ctk.CTkLabel(
            dlg,
            text=f"📦 Di Chuyển {len(docs):,} Tài Liệu Đã Chọn & Tự Cập Nhật Link",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color=THEME['yellow']
        ).pack(anchor="w", padx=16, pady=(14, 4))

        preview = ", ".join(d.get('doc_code', d.get('filename', '')) for d in docs[:5])
        if len(docs) > 5:
            preview += f" ... (+{len(docs) - 5:,} tài liệu khác)"
        ctk.CTkLabel(
            dlg, text=f"Mục đã chọn: {preview}",
            font=ctk.CTkFont(size=11), text_color=THEME['subtext'],
            wraplength=580, justify="left"
        ).pack(anchor="w", padx=16, pady=(0, 10))

        box = ctk.CTkFrame(dlg, fg_color=THEME['surface1'], corner_radius=8)
        box.pack(fill="x", padx=16, pady=(0, 10))

        ctk.CTkLabel(box, text="Thư mục đích:", font=ctk.CTkFont(size=12, weight="bold")).pack(anchor="w", padx=12, pady=(10, 4))
        row = ctk.CTkFrame(box, fg_color="transparent")
        row.pack(fill="x", padx=12, pady=(0, 8))
        row.grid_columnconfigure(0, weight=1)

        var_dest = tk.StringVar()
        ctk.CTkEntry(row, textvariable=var_dest, placeholder_text="Chọn thư mục muốn dời file tới...", height=34).grid(
            row=0, column=0, sticky="ew", padx=(0, 6)
        )

        def pick_dir():
            d = filedialog.askdirectory(parent=dlg, title="Chọn Thư Mục Đích")
            if d:
                var_dest.set(os.path.normpath(d))

        ctk.CTkButton(row, text="📂 Chọn", width=90, height=34, fg_color=THEME['surface2'], command=pick_dir).grid(row=0, column=1)

        var_keep_struct = tk.BooleanVar(value=(len(docs) > 1))
        ctk.CTkCheckBox(
            box, text="Giữ nguyên cấu trúc thư mục con bên trong thư mục đích",
            variable=var_keep_struct, font=ctk.CTkFont(size=11)
        ).pack(anchor="w", padx=12, pady=3)

        var_copy = tk.BooleanVar(value=False)
        ctk.CTkCheckBox(
            box, text="Sao chép (giữ lại file cũ) và đổi link trỏ sang bản mới",
            variable=var_copy, font=ctk.CTkFont(size=11)
        ).pack(anchor="w", padx=12, pady=(3, 10))

        btn_row = ctk.CTkFrame(dlg, fg_color="transparent")
        btn_row.pack(fill="x", padx=16, pady=(4, 12))

        def do_move():
            dest = var_dest.get().strip()
            if not dest:
                messagebox.showwarning("Thiếu Thư Mục Đích", "Vui lòng chọn thư mục đích!", parent=dlg)
                return
            dlg.destroy()
            self._set_storage_busy(True)

            def run():
                try:
                    stats = move_selected_documents(
                        docs=docs,
                        dest_dir=dest,
                        preserve_structure=bool(var_keep_struct.get()),
                        copy_only=bool(var_copy.get()),
                        progress_callback=lambda m, p=None: self.ui_call(self.log_storage, m, p),
                    )
                    msg = (
                        f"Hoàn tất {'sao chép' if var_copy.get() else 'di chuyển'}!\n\n"
                        f"• Thành công: {stats['moved']:,} file\n"
                        f"• Cập nhật link: {stats['updated_records']:,} bản ghi\n"
                        f"• Không có file cục bộ: {stats['missing']:,}\n"
                        f"• Lỗi: {stats['errors']:,}"
                    )
                    if stats['error_details']:
                        msg += "\n\nLỗi:\n- " + "\n- ".join(stats['error_details'][:5])
                    self.ui_call(self._on_storage_task_done, msg)
                except Exception as e:
                    self.ui_call(self._on_storage_task_error, str(e))

            self.storage_thread = threading.Thread(target=run, daemon=True)
            self.storage_thread.start()

        ctk.CTkButton(btn_row, text="Hủy", width=90, height=34, fg_color=THEME['surface2'], command=dlg.destroy).pack(side="right", padx=(6, 0))
        ctk.CTkButton(
            btn_row, text="📦 Thực Hiện Di Chuyển", width=175, height=34,
            fg_color=THEME['green'], text_color="#1e1e2e",
            font=ctk.CTkFont(size=12, weight="bold"), command=do_move
        ).pack(side="right")

    def open_delete_docs_dialog(self, docs, title_override=None, default_mode='disk_only'):
        if not docs or self._is_storage_busy():
            return

        # Compute size on disk quickly
        seen_paths = set()
        total_bytes = 0
        existing_cnt = 0
        for d in docs:
            fp = resolve_local_path(d.get('local_path', ''))
            if fp and is_file_exists(fp):
                nc = os.path.normcase(os.path.abspath(fp))
                if nc not in seen_paths:
                    seen_paths.add(nc)
                    existing_cnt += 1
                    try:
                        total_bytes += os.path.getsize(to_long_path(fp))
                    except OSError:
                        pass

        mb = total_bytes / (1024 ** 2)
        size_txt = f"{mb / 1024:.2f} GB" if mb >= 1024 else f"{mb:.2f} MB"

        dlg = ctk.CTkToplevel(self)
        dlg.title(title_override or f"🗑️ Xóa {len(docs):,} Tài Liệu")
        dlg.geometry("650x410")
        dlg.minsize(580, 370)
        dlg.configure(fg_color=THEME['bg'])
        dlg.transient(self)
        dlg.grab_set()
        dlg.bind("<Escape>", lambda e: dlg.destroy())

        ctk.CTkLabel(
            dlg,
            text=title_override or f"🗑️ Xác Nhận Xóa {len(docs):,} Tài Liệu",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color=THEME['red']
        ).pack(anchor="w", padx=16, pady=(14, 4))

        preview = ", ".join(d.get('doc_code', d.get('filename', '')) for d in docs[:5])
        if len(docs) > 5:
            preview += f" ... (+{len(docs) - 5:,} mục khác)"

        ctk.CTkLabel(
            dlg,
            text=f"Số bản ghi chọn: {len(docs):,}  •  File PDF có trên ổ cứng: {existing_cnt:,} ({size_txt})\nMục: {preview}",
            font=ctk.CTkFont(size=11),
            text_color=THEME['subtext'],
            wraplength=610,
            justify="left"
        ).pack(anchor="w", padx=16, pady=(0, 10))

        mode_box = ctk.CTkFrame(dlg, fg_color=THEME['surface1'], corner_radius=8)
        mode_box.pack(fill="x", padx=16, pady=(0, 10))

        ctk.CTkLabel(
            mode_box, text="Chọn phương thức xóa:",
            font=ctk.CTkFont(size=12, weight="bold"), text_color=THEME['text']
        ).pack(anchor="w", padx=12, pady=(10, 6))

        var_mode = tk.StringVar(value=default_mode)
        modes = [
            ("disk_only", "1. Chỉ xóa file PDF trên ổ cứng — giữ lại danh mục tra cứu & link ổ mạng (có thể tải lại sau)"),
            ("disk_and_catalog", "2. Xóa file PDF trên ổ cứng VÀ xóa hoàn toàn khỏi danh mục ứng dụng"),
            ("catalog_only", "3. Chỉ xóa khỏi danh mục ứng dụng — giữ nguyên file PDF trên ổ cứng"),
        ]
        for val, label in modes:
            ctk.CTkRadioButton(
                mode_box, text=label, variable=var_mode, value=val,
                font=ctk.CTkFont(size=11), radiobutton_width=18, radiobutton_height=18
            ).pack(anchor="w", padx=14, pady=4)

        var_recycle = tk.BooleanVar(value=True)
        ctk.CTkCheckBox(
            mode_box,
            text="♻️ Đưa file vào Thùng Rác Windows (An toàn — có thể khôi phục nếu lỡ tay)",
            variable=var_recycle,
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=THEME['green']
        ).pack(anchor="w", padx=14, pady=(8, 12))

        btn_row = ctk.CTkFrame(dlg, fg_color="transparent")
        btn_row.pack(fill="x", padx=16, pady=(4, 12))

        def do_delete():
            chosen_mode = var_mode.get()
            use_bin = bool(var_recycle.get())
            if chosen_mode == 'disk_and_catalog' and not use_bin:
                if not messagebox.askyesno(
                    "Cảnh Báo Xóa Vĩnh Viễn",
                    f"Bạn đang chọn XÓA VĨNH VIỄN (không qua Thùng Rác) {existing_cnt:,} file PDF và xóa khỏi danh mục!\n"
                    f"Thao tác này không thể hoàn tác. Bạn chắc chắn chứ?",
                    parent=dlg
                ):
                    return

            dlg.destroy()
            self._set_storage_busy(True)

            def run():
                try:
                    stats = delete_documents(
                        docs=docs,
                        mode=chosen_mode,
                        use_recycle_bin=use_bin,
                        cleanup_empty=True,
                        progress_callback=lambda m, p=None: self.ui_call(self.log_storage, m, p),
                    )
                    freed_mb = stats['bytes_freed'] / (1024 ** 2)
                    msg = (
                        f"Đã hoàn tất xóa tài liệu!\n\n"
                        f"• File xóa trên ổ cứng: {stats['files_deleted']:,} "
                        f"(vào Thùng Rác: {stats['files_recycled']:,})\n"
                        f"• Dung lượng giải phóng: {freed_mb:.2f} MB\n"
                        f"• Bản ghi đã gỡ khỏi danh mục: {stats['records_removed']:,}\n"
                        f"• Lỗi: {stats['errors']:,}"
                    )
                    if stats['error_details']:
                        msg += "\n\nChi tiết lỗi:\n- " + "\n- ".join(stats['error_details'][:5])
                    self.ui_call(self._on_storage_task_done, msg)
                except Exception as e:
                    self.ui_call(self._on_storage_task_error, str(e))

            self.storage_thread = threading.Thread(target=run, daemon=True)
            self.storage_thread.start()

        ctk.CTkButton(btn_row, text="Hủy", width=90, height=34, fg_color=THEME['surface2'], command=dlg.destroy).pack(side="right", padx=(6, 0))
        ctk.CTkButton(
            btn_row, text="🗑️ Xác Nhận Xóa", width=155, height=34,
            fg_color=THEME['red'], hover_color="#d97290", text_color="#1e1e2e",
            font=ctk.CTkFont(size=12, weight="bold"), command=do_delete
        ).pack(side="right")

def main():
    app = TaiLieuApp()
    try:
        app.mainloop()
    except KeyboardInterrupt:
        app.on_app_close()
    except tk.TclError:
        if not app._is_closing:
            raise
    finally:
        try:
            if not app._is_closing and app.winfo_exists():
                app.on_app_close()
        except Exception:
            pass
    sys.exit(0)


if __name__ == '__main__':
    main()
