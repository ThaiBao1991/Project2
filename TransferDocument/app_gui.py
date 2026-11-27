# -*- coding: utf-8 -*-
"""
TransferDocument — Ứng dụng dịch tài liệu Office & PDF (.doc/.docx/.xls/.xlsx/.ppt/.pptx/.pdf)
đa ngôn ngữ Nguồn <-> Đích kèm chọn Font tương ứng, giữ nguyên định dạng, màu sắc, hình ảnh.
"""

import importlib
import os
import site
import subprocess
import sys
import threading
import time
from typing import List

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

EXIT_MISSING_LIB_DIALOG = 2

REQUIRED_PACKAGES = {
    "customtkinter": "customtkinter>=5.2.0",
    "lxml": "lxml>=4.9.0",
    "requests": "requests>=2.31.0",
    "win32com.client": "pywin32>=306",
    "pymupdf": "PyMuPDF>=1.24.0",
}


def ensure_dependencies() -> bool:
    """Tự động kiểm tra và cài đặt các thư viện cần thiết (pattern python_auto_install)."""
    missing = []
    for mod_name, pip_spec in REQUIRED_PACKAGES.items():
        try:
            importlib.import_module(mod_name)
        except ImportError:
            missing.append((mod_name, pip_spec))

    if not missing:
        return True

    in_venv = sys.prefix != sys.base_prefix
    specs = [spec for _, spec in missing]
    cmd = [sys.executable, "-m", "pip", "install"]
    if not in_venv:
        cmd.append("--user")
    cmd.extend(specs)

    print(f"[Auto-Install] Đang cài đặt thư viện thiếu: {', '.join(specs)} ...")
    try:
        subprocess.check_call(cmd)
        user_site = site.getusersitepackages()
        if user_site and os.path.isdir(user_site) and user_site not in sys.path:
            sys.path.append(user_site)
        importlib.invalidate_caches()
    except Exception as e:
        print(f"[Auto-Install] Cài tự động thất bại: {e}")

    still_missing = []
    for mod_name, pip_spec in missing:
        try:
            importlib.import_module(mod_name)
        except ImportError:
            still_missing.append(pip_spec)

    if still_missing:
        try:
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            quoted = " ".join(f'"{s}"' for s in still_missing)
            messagebox.showerror(
                "Thiếu thư viện Python",
                f"Không thể tự cài đặt các gói sau:\n{', '.join(still_missing)}\n\n"
                f"Vui lòng chạy lệnh sau trong CMD:\npython -m pip install {quoted}",
            )
            root.destroy()
        except Exception:
            pass
        sys.exit(EXIT_MISSING_LIB_DIALOG)

    return True


ensure_dependencies()

import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk

from document_processor import process_document
from language_config import (
    SOURCE_LANGUAGES,
    TARGET_LANGUAGES,
    get_default_font,
    get_recommended_fonts,
)
from office_converter import SUPPORTED_EXTS
from settings_reader import load_gemini_keys, resolve_settings_path
from translator_engine import DocumentTranslator

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SOURCE_DIR = os.path.join(BASE_DIR, "SourceDocument")
DEFAULT_OUTPUT_DIR = os.path.join(BASE_DIR, "OutputDocument")


class TransferDocumentApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("TransferDocument — Dịch Tài Liệu Office & PDF Đa Ngôn Ngữ")
        self.geometry("1040x740")
        self.minsize(900, 650)

        self.selected_files: List[str] = []
        self.output_dir = tk.StringVar(value=DEFAULT_OUTPUT_DIR)

        self._src_label_to_code = {lbl: code for lbl, code in SOURCE_LANGUAGES}
        self._tgt_label_to_code = {lbl: code for lbl, code in TARGET_LANGUAGES}

        self.source_lang_label = tk.StringVar(value=SOURCE_LANGUAGES[0][0])  # Tự động
        self.target_lang_label = tk.StringVar(value=TARGET_LANGUAGES[0][0])  # Tiếng Việt
        self.target_font_var = tk.StringVar(value=get_default_font("vi"))

        self.auto_fit_var = tk.BooleanVar(value=True)
        self.merge_para_var = tk.BooleanVar(value=True)
        self.use_glossary_var = tk.BooleanVar(value=True)
        self.use_cache_var = tk.BooleanVar(value=True)
        self.export_pdf_var = tk.BooleanVar(value=False)

        self._stop_event = threading.Event()
        self._worker_thread = None

        self._build_ui()
        self._load_initial_source_files()
        self._refresh_key_status()

        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _build_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(4, weight=1)

        # ── Header ──
        header = ctk.CTkFrame(self, corner_radius=10)
        header.grid(row=0, column=0, padx=14, pady=(12, 6), sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            header,
            text="TransferDocument — Dịch Word, Excel, PowerPoint & PDF giữ nguyên định dạng, màu sắc, hình ảnh",
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
        ).grid(row=0, column=0, padx=14, pady=(10, 2), sticky="w")

        self.key_status_label = ctk.CTkLabel(
            header,
            text="Đang kiểm tra Gemini API Keys...",
            font=ctk.CTkFont(family="Arial", size=12),
            text_color="#94a3b8",
        )
        self.key_status_label.grid(row=1, column=0, padx=14, pady=(0, 10), sticky="w")

        # ── Toolbar chọn file & thư mục xuất ──
        toolbar = ctk.CTkFrame(self, corner_radius=10)
        toolbar.grid(row=1, column=0, padx=14, pady=6, sticky="ew")
        toolbar.grid_columnconfigure(5, weight=1)

        ctk.CTkButton(
            toolbar, text="+ Chọn File Mới...", width=140, command=self._pick_files
        ).grid(row=0, column=0, padx=(10, 6), pady=10)

        ctk.CTkButton(
            toolbar, text="+ Chọn Thư Mục...", width=140, fg_color="#334155", hover_color="#475569",
            command=self._pick_folder
        ).grid(row=0, column=1, padx=6, pady=10)

        ctk.CTkButton(
            toolbar, text="Nạp SourceDocument", width=155, fg_color="#0f766e", hover_color="#115e59",
            command=self._load_initial_source_files
        ).grid(row=0, column=2, padx=6, pady=10)

        ctk.CTkButton(
            toolbar, text="Xóa File Chọn", width=115, fg_color="#7f1d1d", hover_color="#991b1b",
            command=self._remove_selected_file
        ).grid(row=0, column=3, padx=6, pady=10)

        ctk.CTkButton(
            toolbar, text="Xóa Hết", width=85, fg_color="#475569", hover_color="#64748b",
            command=self._clear_files
        ).grid(row=0, column=4, padx=6, pady=10)

        self.file_count_label = ctk.CTkLabel(
            toolbar, text="0 file", font=ctk.CTkFont(family="Arial", size=12, weight="bold")
        )
        self.file_count_label.grid(row=0, column=5, padx=12, sticky="e")

        # Dòng thư mục xuất
        out_row = ctk.CTkFrame(toolbar, fg_color="transparent")
        out_row.grid(row=1, column=0, columnspan=6, padx=10, pady=(0, 10), sticky="ew")
        out_row.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(out_row, text="Thư mục xuất:", font=ctk.CTkFont(family="Arial", size=12)).grid(
            row=0, column=0, padx=(0, 8)
        )
        ctk.CTkEntry(out_row, textvariable=self.output_dir, font=ctk.CTkFont(family="Arial", size=12)).grid(
            row=0, column=1, sticky="ew", padx=(0, 8)
        )
        ctk.CTkButton(out_row, text="Đổi thư mục", width=105, command=self._pick_output_dir).grid(
            row=0, column=2, padx=(0, 6)
        )
        ctk.CTkButton(
            out_row, text="Mở thư mục xuất", width=125, fg_color="#1d4ed8", hover_color="#1e40af",
            command=self._open_output_dir
        ).grid(row=0, column=3)

        # ── Danh sách file (Native Tk Listbox mượt 60fps dark-mode) ──
        list_frame = ctk.CTkFrame(self, corner_radius=10)
        list_frame.grid(row=2, column=0, padx=14, pady=6, sticky="nsew")
        list_frame.grid_columnconfigure(0, weight=1)
        list_frame.grid_rowconfigure(0, weight=1)

        self.file_listbox = tk.Listbox(
            list_frame,
            selectmode=tk.EXTENDED,
            bg="#1e293b",
            fg="#f1f5f9",
            selectbackground="#2563eb",
            selectforeground="#ffffff",
            font=("Arial", 10),
            borderwidth=0,
            highlightthickness=0,
            activestyle="none",
        )
        self.file_listbox.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="nsew")

        sb = ctk.CTkScrollbar(list_frame, command=self.file_listbox.yview)
        sb.grid(row=0, column=1, padx=(4, 8), pady=10, sticky="ns")
        self.file_listbox.configure(yscrollcommand=sb.set)

        # ── Khung chọn Ngôn ngữ Nguồn -> Đích + Font đích + Tùy chọn ──
        opts = ctk.CTkFrame(self, corner_radius=10)
        opts.grid(row=3, column=0, padx=14, pady=6, sticky="ew")
        opts.grid_columnconfigure(6, weight=1)

        # Hàng 1: Nguồn -> Đích + Font + Nút chạy
        ctk.CTkLabel(opts, text="Nguồn:", font=ctk.CTkFont(family="Arial", size=12, weight="bold")).grid(
            row=0, column=0, padx=(12, 4), pady=(10, 6), sticky="w"
        )
        ctk.CTkOptionMenu(
            opts,
            variable=self.source_lang_label,
            values=[lbl for lbl, _ in SOURCE_LANGUAGES],
            width=145,
        ).grid(row=0, column=1, padx=(0, 10), pady=(10, 6))

        ctk.CTkLabel(opts, text="→ Đích:", font=ctk.CTkFont(family="Arial", size=12, weight="bold")).grid(
            row=0, column=2, padx=(4, 4), pady=(10, 6), sticky="w"
        )
        ctk.CTkOptionMenu(
            opts,
            variable=self.target_lang_label,
            values=[lbl for lbl, _ in TARGET_LANGUAGES],
            width=145,
            command=self._on_target_lang_changed,
        ).grid(row=0, column=3, padx=(0, 10), pady=(10, 6))

        ctk.CTkLabel(opts, text="Font đích:", font=ctk.CTkFont(family="Arial", size=12, weight="bold")).grid(
            row=0, column=4, padx=(4, 4), pady=(10, 6), sticky="w"
        )
        self.font_menu = ctk.CTkOptionMenu(
            opts,
            variable=self.target_font_var,
            values=get_recommended_fonts("vi"),
            width=155,
        )
        self.font_menu.grid(row=0, column=5, padx=(0, 10), pady=(10, 6))

        btn_box = ctk.CTkFrame(opts, fg_color="transparent")
        btn_box.grid(row=0, column=6, rowspan=2, padx=10, pady=8, sticky="e")

        self.start_btn = ctk.CTkButton(
            btn_box,
            text="▶ BẮT ĐẦU DỊCH",
            width=155,
            height=40,
            fg_color="#16a34a",
            hover_color="#15803d",
            font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
            command=self._start_translation,
        )
        self.start_btn.pack(side="left", padx=(0, 8))

        self.stop_btn = ctk.CTkButton(
            btn_box,
            text="■ Dừng",
            width=80,
            height=40,
            fg_color="#dc2626",
            hover_color="#b91c1c",
            state="disabled",
            command=self._stop_translation,
        )
        self.stop_btn.pack(side="left")

        # Hàng 2: Các tùy chọn checkbox
        chk_row = ctk.CTkFrame(opts, fg_color="transparent")
        chk_row.grid(row=1, column=0, columnspan=6, padx=10, pady=(2, 10), sticky="w")

        ctk.CTkCheckBox(chk_row, text="Chống cắt/gãy ô chữ", variable=self.auto_fit_var).pack(side="left", padx=(2, 12))
        ctk.CTkCheckBox(chk_row, text="Gộp câu ngắt dòng (Word)", variable=self.merge_para_var).pack(side="left", padx=(0, 12))
        ctk.CTkCheckBox(chk_row, text="Glossary kỹ thuật", variable=self.use_glossary_var).pack(side="left", padx=(0, 12))
        ctk.CTkCheckBox(chk_row, text="Dùng Cache", variable=self.use_cache_var).pack(side="left", padx=(0, 12))
        ctk.CTkCheckBox(chk_row, text="Xuất thêm PDF", variable=self.export_pdf_var).pack(side="left", padx=(0, 8))

        # ── Tiến trình & Log ──
        log_frame = ctk.CTkFrame(self, corner_radius=10)
        log_frame.grid(row=4, column=0, padx=14, pady=(6, 12), sticky="nsew")
        log_frame.grid_columnconfigure(0, weight=1)
        log_frame.grid_rowconfigure(1, weight=1)

        prog_row = ctk.CTkFrame(log_frame, fg_color="transparent")
        prog_row.grid(row=0, column=0, padx=10, pady=(10, 4), sticky="ew")
        prog_row.grid_columnconfigure(0, weight=1)

        self.progress_bar = ctk.CTkProgressBar(prog_row)
        self.progress_bar.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        self.progress_bar.set(0)

        self.status_label = ctk.CTkLabel(
            prog_row, text="Sẵn sàng", font=ctk.CTkFont(family="Arial", size=12)
        )
        self.status_label.grid(row=0, column=1, sticky="e")

        self.log_box = ctk.CTkTextbox(
            log_frame,
            font=ctk.CTkFont(family="Consolas", size=11),
            wrap="word",
            state="disabled",
        )
        self.log_box.grid(row=1, column=0, padx=10, pady=(4, 10), sticky="nsew")

    def _on_target_lang_changed(self, selected_label: str):
        tgt_code = self._tgt_label_to_code.get(selected_label, "vi")
        rec_fonts = get_recommended_fonts(tgt_code)
        default_font = get_default_font(tgt_code)
        self.font_menu.configure(values=rec_fonts)
        self.target_font_var.set(default_font)
        self._log(f"🌐 Đã chọn ngôn ngữ đích: {selected_label} -> Font gợi ý: {default_font}")

    def _log(self, msg: str):
        ts = time.strftime("%H:%M:%S")
        line = f"[{ts}] {msg}\n"

        def _append():
            self.log_box.configure(state="normal")
            self.log_box.insert("end", line)
            self.log_box.see("end")
            self.log_box.configure(state="disabled")

        self.after(0, _append)

    def _set_progress(self, fraction: float, status: str):
        def _upd():
            self.progress_bar.set(max(0.0, min(1.0, fraction)))
            self.status_label.configure(text=status)
        self.after(0, _upd)

    def _refresh_key_status(self):
        path = resolve_settings_path()
        keys = load_gemini_keys()
        if keys:
            accounts = {k.get("email", "unknown") for k in keys}
            self.key_status_label.configure(
                text=f"✅ Sẵn sàng: {len(keys)} Gemini API Keys ({len(accounts)} tài khoản) — nguồn: {path}",
                text_color="#4ade80",
            )
        else:
            self.key_status_label.configure(
                text="⚠ Chưa tìm thấy Gemini API Key trong settings.json (kiểm tra AskCpl/settings.json)",
                text_color="#f87171",
            )

    def _refresh_listbox(self):
        self.file_listbox.delete(0, tk.END)
        for p in self.selected_files:
            ext = os.path.splitext(p)[1].upper()
            size_kb = os.path.getsize(p) / 1024 if os.path.exists(p) else 0
            self.file_listbox.insert(tk.END, f" [{ext}]  {os.path.basename(p)}   ({size_kb:.1f} KB)  —  {os.path.dirname(p)}")
        self.file_count_label.configure(text=f"{len(self.selected_files)} file")

    def _add_files(self, paths: List[str]):
        added = 0
        existing = set(os.path.normcase(os.path.abspath(p)) for p in self.selected_files)
        for p in paths:
            ap = os.path.abspath(p)
            ext = os.path.splitext(ap)[1].lower()
            if ext not in SUPPORTED_EXTS or os.path.basename(ap).startswith("~$"):
                continue
            key = os.path.normcase(ap)
            if key not in existing and os.path.isfile(ap):
                self.selected_files.append(ap)
                existing.add(key)
                added += 1
        self._refresh_listbox()
        if added:
            self._log(f"➕ Đã thêm {added} file vào danh sách.")

    def _load_initial_source_files(self):
        if os.path.isdir(DEFAULT_SOURCE_DIR):
            files = [
                os.path.join(DEFAULT_SOURCE_DIR, f)
                for f in sorted(os.listdir(DEFAULT_SOURCE_DIR))
            ]
            self._add_files(files)

    def _pick_files(self):
        paths = filedialog.askopenfilenames(
            title="Chọn tài liệu Office / PDF cần dịch",
            filetypes=[
                ("Tất cả tài liệu hỗ trợ", "*.docx *.doc *.xlsx *.xls *.pptx *.ppt *.pdf"),
                ("PDF", "*.pdf"),
                ("Word", "*.docx *.doc"),
                ("Excel", "*.xlsx *.xls"),
                ("PowerPoint", "*.pptx *.ppt"),
                ("Tất cả file", "*.*"),
            ],
        )
        if paths:
            self._add_files(list(paths))

    def _pick_folder(self):
        folder = filedialog.askdirectory(title="Chọn thư mục chứa tài liệu Office / PDF")
        if folder:
            found = []
            for root_dir, _, filenames in os.walk(folder):
                for fn in sorted(filenames):
                    found.append(os.path.join(root_dir, fn))
            self._add_files(found)

    def _remove_selected_file(self):
        sel = list(self.file_listbox.curselection())
        for idx in reversed(sel):
            if 0 <= idx < len(self.selected_files):
                self.selected_files.pop(idx)
        self._refresh_listbox()

    def _clear_files(self):
        self.selected_files.clear()
        self._refresh_listbox()

    def _pick_output_dir(self):
        folder = filedialog.askdirectory(title="Chọn thư mục lưu tài liệu đã dịch")
        if folder:
            self.output_dir.set(folder)

    def _open_output_dir(self):
        out_dir = self.output_dir.get().strip() or DEFAULT_OUTPUT_DIR
        os.makedirs(out_dir, exist_ok=True)
        os.startfile(out_dir)

    def _start_translation(self):
        if not self.selected_files:
            messagebox.showwarning("Chưa chọn file", "Vui lòng chọn ít nhất 1 tài liệu để dịch.")
            return
        if not load_gemini_keys():
            messagebox.showerror("Thiếu API Key", "Không tìm thấy Gemini API Key trong settings.json.")
            return

        src_code = self._src_label_to_code.get(self.source_lang_label.get(), "auto")
        tgt_code = self._tgt_label_to_code.get(self.target_lang_label.get(), "vi")
        if src_code == tgt_code and src_code != "auto":
            messagebox.showwarning("Trùng ngôn ngữ", "Ngôn ngữ nguồn và ngôn ngữ đích đang giống nhau!")
            return

        self._stop_event.clear()
        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self._set_progress(0.0, "Đang khởi tạo...")

        files_copy = list(self.selected_files)
        out_dir = self.output_dir.get().strip() or DEFAULT_OUTPUT_DIR
        font_name = self.target_font_var.get().strip() or get_default_font(tgt_code)

        self._worker_thread = threading.Thread(
            target=self._run_worker,
            args=(files_copy, out_dir, src_code, tgt_code, font_name),
            daemon=True,
        )
        self._worker_thread.start()

    def _stop_translation(self):
        self._stop_event.set()
        self._log("⏳ Đang gửi tín hiệu dừng an toàn...")
        self.stop_btn.configure(state="disabled")

    def _run_worker(self, files: List[str], out_dir: str, src_code: str, tgt_code: str, font_name: str):
        total = len(files)
        ok_count = 0
        fail_count = 0

        try:
            translator = DocumentTranslator(
                source_lang=src_code,
                target_lang=tgt_code,
                use_cache=self.use_cache_var.get(),
                use_glossary=self.use_glossary_var.get(),
                log_fn=self._log,
                stop_check=self._stop_event.is_set,
            )

            self._log(f"🌐 Cấu hình dịch: {src_code.upper()} → {tgt_code.upper()} | Font: {font_name}")

            for i, path in enumerate(files, start=1):
                if self._stop_event.is_set():
                    break
                name = os.path.basename(path)
                self._log(f"═══ [{i}/{total}] Bắt đầu xử lý: {name} ═══")
                self._set_progress((i - 1) / total, f"Đang dịch ({i}/{total}): {name}")

                def _sub_prog(done_b, total_b, msg):
                    frac = ((i - 1) + (done_b / max(total_b, 1))) / total
                    self._set_progress(frac, f"({i}/{total}) {name} — lô {done_b}/{total_b}")

                try:
                    stats = process_document(
                        input_path=path,
                        output_dir=out_dir,
                        translator=translator,
                        target_font=font_name,
                        auto_fit_layout=self.auto_fit_var.get(),
                        merge_broken_paragraphs=self.merge_para_var.get(),
                        also_export_pdf=self.export_pdf_var.get(),
                        progress_cb=_sub_prog,
                    )
                    ok_count += 1
                    self._log(
                        f"✅ Hoàn thành: {os.path.basename(stats['output'])} "
                        f"(font: {stats.get('font_used', font_name)}, giữ nguyên {stats.get('media_preserved', 0)} hình ảnh)"
                    )
                except Exception as e:
                    fail_count += 1
                    self._log(f"❌ Lỗi khi xử lý {name}: {e}")

            self._set_progress(1.0, f"Hoàn tất: {ok_count}/{total} thành công")
            self._log(f"🎉 XONG! Thành công: {ok_count}/{total}, Lỗi: {fail_count}. Thư mục: {out_dir}")
        except Exception as e:
            self._log(f"❌ Lỗi hệ thống: {e}")
            self._set_progress(0.0, "Gặp lỗi")
        finally:
            def _finish_ui():
                self.start_btn.configure(state="normal")
                self.stop_btn.configure(state="disabled")
            self.after(0, _finish_ui)

    def _on_close(self):
        self._stop_event.set()
        try:
            self.quit()
        except Exception:
            pass
        try:
            self.destroy()
        except Exception:
            pass


def main():
    app = TransferDocumentApp()
    try:
        app.mainloop()
    except KeyboardInterrupt:
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
