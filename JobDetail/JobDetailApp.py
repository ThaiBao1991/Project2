#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
JobDetailApp.py - Ứng Dụng Quản Lý & Tra Cứu Hồ Sơ Công Việc (JobDetail Intelligence Hub)
Tuân thủ tiêu chuẩn python_desktop_standards.md và customtkinter_perf_ui:
  - CustomTkinter + ttk.Treeview Dark Mode (Catppuccin Mocha)
  - Mô hình 5 Tầng Kiến Thức (Tổng quan, Kỹ năng, Lộ trình, Tài liệu, Phỏng vấn)
  - Bộ máy phân tích kép: Offline Smart Engine + Gemini AI
  - Tra cứu tức thì 60fps, lọc đa chiều, xuất Markdown
"""

import os
import sys
import json
import threading
import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Đảm bảo UTF-8 trên Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import customtkinter as ctk

from job_storage import JobStorage
from job_analyzer import JobAnalyzer

# =====================================================================
# HỆ MÀU CATPPUCCIN MOCHA ĐỒNG NHẤT
# =====================================================================
THEME = {
    "base": "#1e1e2e",         # Nền chính
    "mantle": "#181825",       # Sidebar / Header
    "crust": "#11111b",        # Nền sâu nhất
    "surface0": "#313244",     # Khung card / Border
    "surface1": "#45475a",     # Card highlight
    "text": "#cdd6f4",         # Chữ chính
    "subtext": "#a6adc8",      # Chữ phụ
    "blue": "#89b4fa",         # Accent chính
    "green": "#a6e3a1",        # Thành công / Must-have
    "yellow": "#f9e2af",       # Cảnh báo / Soft skills
    "red": "#f38ba8",          # Bắt buộc / Xóa
    "mauve": "#cba6f7",        # Tím nổi bật
    "peach": "#fab387",        # Cam điểm nhấn
}

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AddJobDialog(ctk.CTkToplevel):
    """Cửa sổ Modal thêm và phân tích JD mới."""
    def __init__(self, parent, on_save_callback):
        super().__init__(parent)
        self.parent = parent
        self.on_save_callback = on_save_callback
        self.analyzer = JobAnalyzer()

        self.title("➕ Nhập & Phân Tích Hồ Sơ JD Mới")
        self.geometry("780x680")
        self.minsize(650, 550)
        self.configure(fg_color=THEME["base"])

        # Đặt modal
        self.transient(parent)
        self.grab_set()

        self._build_ui()
        self.center_window()

    def center_window(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _build_ui(self):
        container = ctk.CTkFrame(self, fg_color=THEME["base"])
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Tiêu đề
        lbl_title = ctk.CTkLabel(
            container,
            text="💼 Bóc Tách & Phân Tích Bản Mô Tả Công Việc (JD)",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=THEME["blue"]
        )
        lbl_title.pack(anchor="w", pady=(0, 5))

        lbl_desc = ctk.CTkLabel(
            container,
            text="Dán nội dung tuyển dụng bên dưới. Hệ thống sẽ tự động bóc tách thành 5 Tầng Kiến Thức (Kỹ năng, Lộ trình, Tài liệu & Phỏng vấn).",
            font=ctk.CTkFont(size=12),
            text_color=THEME["subtext"]
        )
        lbl_desc.pack(anchor="w", pady=(0, 15))

        # Khung cấu hình Engine
        cfg_frame = ctk.CTkFrame(container, fg_color=THEME["surface0"], corner_radius=8)
        cfg_frame.pack(fill="x", pady=(0, 10), padx=2, ipady=5)

        ctk.CTkLabel(cfg_frame, text="Bộ máy phân tích:", font=ctk.CTkFont(size=12, weight="bold"), text_color=THEME["text"]).pack(side="left", padx=12)

        self.engine_var = ctk.StringVar(value="offline")
        self.radio_offline = ctk.CTkRadioButton(
            cfg_frame, text="⚡ Thông Minh Offline (Siêu tốc 0s, 100% riêng tư)",
            variable=self.engine_var, value="offline",
            command=self._on_engine_change,
            fg_color=THEME["blue"]
        )
        self.radio_offline.pack(side="left", padx=10)

        self.radio_ai = ctk.CTkRadioButton(
            cfg_frame, text="🤖 Gemini AI (Phân tích sâu)",
            variable=self.engine_var, value="ai",
            command=self._on_engine_change,
            fg_color=THEME["mauve"]
        )
        self.radio_ai.pack(side="left", padx=10)

        # API Key frame (ẩn khi chọn offline)
        self.key_frame = ctk.CTkFrame(container, fg_color="transparent")
        ctk.CTkLabel(self.key_frame, text="Gemini API Key:", font=ctk.CTkFont(size=12), text_color=THEME["subtext"]).pack(side="left", padx=(0, 10))
        self.txt_api_key = ctk.CTkEntry(
            self.key_frame,
            placeholder_text="Nhập API Key hoặc để trống nếu đã set biến môi trường GEMINI_API_KEY",
            width=480,
            show="•",
            fg_color=THEME["surface0"],
            border_color=THEME["surface1"]
        )
        self.txt_api_key.pack(side="left", fill="x", expand=True)

        # Khung nhập văn bản JD
        ctk.CTkLabel(container, text="Nội dung JD gốc (Raw Job Description):", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["text"]).pack(anchor="w", pady=(5, 5))

        self.txt_jd = ctk.CTkTextbox(
            container,
            fg_color=THEME["crust"],
            border_color=THEME["surface0"],
            border_width=1,
            text_color=THEME["text"],
            font=ctk.CTkFont(family="Consolas", size=12),
            wrap="word"
        )
        self.txt_jd.pack(fill="both", expand=True, pady=(0, 15))

        # Status & Nút bấm
        bot_frame = ctk.CTkFrame(container, fg_color="transparent")
        bot_frame.pack(fill="x")

        self.lbl_status = ctk.CTkLabel(bot_frame, text="", font=ctk.CTkFont(size=12), text_color=THEME["yellow"])
        self.lbl_status.pack(side="left")

        btn_cancel = ctk.CTkButton(
            bot_frame,
            text="Hủy Bỏ",
            fg_color=THEME["surface0"],
            hover_color=THEME["surface1"],
            text_color=THEME["text"],
            width=100,
            command=self.destroy
        )
        btn_cancel.pack(side="right", padx=(10, 0))

        self.btn_analyze = ctk.CTkButton(
            bot_frame,
            text="🚀 Bắt Đầu Phân Tích & Lưu",
            font=ctk.CTkFont(weight="bold"),
            fg_color=THEME["blue"],
            hover_color="#74c7ec",
            text_color=THEME["crust"],
            width=200,
            command=self._start_analysis
        )
        self.btn_analyze.pack(side="right")

    def _on_engine_change(self):
        if self.engine_var.get() == "ai":
            self.key_frame.pack(fill="x", pady=(0, 10), before=self.txt_jd)
        else:
            self.key_frame.pack_forget()

    def _start_analysis(self):
        raw_text = self.txt_jd.get("1.0", "end-1c").strip()
        if not raw_text:
            messagebox.showwarning("Thiếu nội dung", "Vui lòng dán nội dung JD cần phân tích!", parent=self)
            return

        is_offline = (self.engine_var.get() == "offline")
        api_key = self.txt_api_key.get().strip()

        self.btn_analyze.configure(state="disabled", text="⏳ Đang phân tích...")
        self.lbl_status.configure(text="Đang xử lý phân rã 5 tầng kiến thức...")

        # Chạy nền để không đơ UI
        threading.Thread(target=self._run_analysis_worker, args=(raw_text, is_offline, api_key), daemon=True).start()

    def _run_analysis_worker(self, raw_text, is_offline, api_key):
        try:
            analyzer = JobAnalyzer(api_key=api_key)
            result = analyzer.analyze(raw_text, force_offline=is_offline)
            self.after(0, self._on_analysis_success, result)
        except Exception as e:
            self.after(0, self._on_analysis_error, str(e))

    def _on_analysis_success(self, result):
        self.lbl_status.configure(text="✅ Phân tích hoàn tất! Đang lưu...", text_color=THEME["green"])
        if self.on_save_callback:
            self.on_save_callback(result)
        self.destroy()

    def _on_analysis_error(self, err_msg):
        self.btn_analyze.configure(state="normal", text="🚀 Bắt Đầu Phân Tích & Lưu")
        self.lbl_status.configure(text=f"❌ Lỗi: {err_msg}", text_color=THEME["red"])
        messagebox.showerror("Lỗi phân tích", f"Không thể phân tích JD:\n{err_msg}", parent=self)


class JobDetailApp(ctk.CTk):
    """Giao diện chính của ứng dụng JobDetail Intelligence Hub."""
    def __init__(self):
        super().__init__()
        self.storage = JobStorage()
        self.current_job = None
        self.all_jobs = []

        self.title("💼 JobDetail Intelligence Hub — Quản Lý & Tra Cứu Hồ Sơ Công Việc")
        self.geometry("1280x800")
        self.minsize(1050, 680)
        self.configure(fg_color=THEME["base"])

        self._seed_sample_data_if_empty()
        self._setup_treeview_style()
        self._build_ui()
        self._load_jobs()

    def _setup_treeview_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Dark.Treeview",
            background=THEME["crust"],
            foreground=THEME["text"],
            fieldbackground=THEME["crust"],
            borderwidth=0,
            rowheight=30,
            font=("Segoe UI", 10)
        )
        style.map(
            "Dark.Treeview",
            background=[("selected", THEME["surface0"])],
            foreground=[("selected", THEME["blue"])]
        )
        style.configure(
            "Dark.Treeview.Heading",
            background=THEME["surface0"],
            foreground=THEME["text"],
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            padding=(6, 6)
        )
        style.map("Dark.Treeview.Heading", background=[("active", THEME["surface1"])])

    def _build_ui(self):
        # 1. Top Header Bar
        self.header_bar = ctk.CTkFrame(self, fg_color=THEME["mantle"], height=52, corner_radius=0)
        self.header_bar.pack(fill="x", side="top")

        lbl_logo = ctk.CTkLabel(
            self.header_bar,
            text="💼 JobDetail Hub",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=THEME["blue"]
        )
        lbl_logo.pack(side="left", padx=20)

        lbl_sub = ctk.CTkLabel(
            self.header_bar,
            text="Phân tích & Nắm bắt công việc từ cơ bản đến chi tiết",
            font=ctk.CTkFont(size=12),
            text_color=THEME["subtext"]
        )
        lbl_sub.pack(side="left", padx=5)

        # Header Buttons
        btn_add = ctk.CTkButton(
            self.header_bar,
            text="➕ Thêm JD Mới",
            font=ctk.CTkFont(weight="bold"),
            fg_color=THEME["blue"],
            hover_color="#74c7ec",
            text_color=THEME["crust"],
            height=32,
            command=self._open_add_dialog
        )
        btn_add.pack(side="right", padx=15)

        btn_stats = ctk.CTkButton(
            self.header_bar,
            text="📊 Thống Kê",
            fg_color=THEME["surface0"],
            hover_color=THEME["surface1"],
            text_color=THEME["text"],
            height=32,
            command=self._show_statistics
        )
        btn_stats.pack(side="right", padx=(0, 5))

        # 2. Main Content Split Pane
        self.main_split = ctk.CTkFrame(self, fg_color=THEME["base"], corner_radius=0)
        self.main_split.pack(fill="both", expand=True)

        self._build_sidebar(self.main_split)
        self._build_detail_view(self.main_split)

    def _build_sidebar(self, parent):
        self.sidebar = ctk.CTkFrame(parent, fg_color=THEME["mantle"], width=380, corner_radius=0)
        self.sidebar.pack(side="left", fill="y", padx=0, pady=0)
        self.sidebar.pack_propagate(False)

        # Ô tìm kiếm
        search_box = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        search_box.pack(fill="x", padx=15, pady=(15, 8))

        self.txt_search = ctk.CTkEntry(
            search_box,
            placeholder_text="🔍 Tìm kiếm vị trí, kỹ năng, công ty...",
            height=36,
            fg_color=THEME["crust"],
            border_color=THEME["surface0"],
            text_color=THEME["text"]
        )
        self.txt_search.pack(fill="x")
        self.txt_search.bind("<KeyRelease>", lambda e: self._debounce_search())

        # Bộ lọc Filter Comboboxes
        filters_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        filters_frame.pack(fill="x", padx=15, pady=(0, 10))

        # Lọc Level
        ctk.CTkLabel(filters_frame, text="Level:", font=ctk.CTkFont(size=11), text_color=THEME["subtext"]).grid(row=0, column=0, sticky="w", pady=2)
        self.cb_level = ctk.CTkComboBox(
            filters_frame,
            values=["Tất cả", "Intern", "Fresher", "Junior", "Mid", "Senior", "Lead"],
            command=lambda v: self._apply_filter(),
            height=28,
            width=150,
            fg_color=THEME["crust"],
            border_color=THEME["surface0"]
        )
        self.cb_level.set("Tất cả")
        self.cb_level.grid(row=0, column=1, sticky="ew", padx=(5, 0), pady=2)

        # Lọc Lĩnh Vực
        ctk.CTkLabel(filters_frame, text="Ngành:", font=ctk.CTkFont(size=11), text_color=THEME["subtext"]).grid(row=1, column=0, sticky="w", pady=2)
        self.cb_cat = ctk.CTkComboBox(
            filters_frame,
            values=["Tất cả", "Backend", "Frontend", "Fullstack", "DevOps", "AI/Data", "Mobile", "QA"],
            command=lambda v: self._apply_filter(),
            height=28,
            width=150,
            fg_color=THEME["crust"],
            border_color=THEME["surface0"]
        )
        self.cb_cat.set("Tất cả")
        self.cb_cat.grid(row=1, column=1, sticky="ew", padx=(5, 0), pady=2)

        filters_frame.columnconfigure(1, weight=1)

        # Bảng danh sách công việc (ttk.Treeview)
        tree_container = ctk.CTkFrame(self.sidebar, fg_color=THEME["crust"], corner_radius=6)
        tree_container.pack(fill="both", expand=True, padx=15, pady=(0, 10))

        cols = ("title", "company", "level")
        self.tree = ttk.Treeview(tree_container, columns=cols, show="headings", style="Dark.Treeview", selectmode="browse")
        self.tree.heading("title", text="Vị Trí Tuyển Dụng")
        self.tree.heading("company", text="Công Ty")
        self.tree.heading("level", text="Cấp Bậc")

        self.tree.column("title", width=180, anchor="w")
        self.tree.column("company", width=110, anchor="w")
        self.tree.column("level", width=60, anchor="center")

        tree_scroll = ttk.Scrollbar(tree_container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=tree_scroll.set)

        self.tree.pack(side="left", fill="both", expand=True)
        tree_scroll.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self._on_job_select)

        # Nút chức năng đáy sidebar
        side_bot = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        side_bot.pack(fill="x", padx=15, pady=(0, 15))

        self.lbl_count = ctk.CTkLabel(side_bot, text="0 công việc", font=ctk.CTkFont(size=11), text_color=THEME["subtext"])
        self.lbl_count.pack(side="left")

        btn_del = ctk.CTkButton(
            side_bot,
            text="🗑️ Xóa",
            width=70,
            height=28,
            fg_color=THEME["surface0"],
            hover_color=THEME["red"],
            text_color=THEME["text"],
            command=self._delete_selected_job
        )
        btn_del.pack(side="right")

    def _build_detail_view(self, parent):
        self.detail_frame = ctk.CTkFrame(parent, fg_color=THEME["base"], corner_radius=0)
        self.detail_frame.pack(side="right", fill="both", expand=True, padx=20, pady=15)

        # 1. Header chi tiết công việc
        self.dt_header = ctk.CTkFrame(self.detail_frame, fg_color=THEME["surface0"], corner_radius=10)
        self.dt_header.pack(fill="x", pady=(0, 12), ipady=8, padx=2)

        header_top = ctk.CTkFrame(self.dt_header, fg_color="transparent")
        header_top.pack(fill="x", padx=15, pady=(8, 2))

        self.dt_title = ctk.CTkLabel(
            header_top,
            text="Chọn một công việc bên trái để xem phân tích",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=THEME["blue"]
        )
        self.dt_title.pack(side="left")

        # Nút Export & Copy
        btn_export = ctk.CTkButton(
            header_top,
            text="💾 Xuất Markdown",
            width=120,
            height=30,
            fg_color=THEME["surface1"],
            hover_color=THEME["blue"],
            text_color=THEME["text"],
            command=self._export_markdown_file
        )
        btn_export.pack(side="right", padx=(5, 0))

        btn_copy = ctk.CTkButton(
            header_top,
            text="📋 Copy Báo Cáo",
            width=110,
            height=30,
            fg_color=THEME["surface1"],
            hover_color=THEME["mauve"],
            text_color=THEME["text"],
            command=self._copy_markdown
        )
        btn_copy.pack(side="right")

        # Hàng Badges
        self.badges_frame = ctk.CTkFrame(self.dt_header, fg_color="transparent")
        self.badges_frame.pack(fill="x", padx=15, pady=(2, 6))

        self.lbl_company = ctk.CTkLabel(self.badges_frame, text="", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["text"])
        self.lbl_company.pack(side="left", padx=(0, 15))

        self.badge_level = self._create_badge(self.badges_frame, "Level: -", THEME["peach"])
        self.badge_cat = self._create_badge(self.badges_frame, "Ngành: -", THEME["blue"])
        self.badge_loc = self._create_badge(self.badges_frame, "Địa điểm: -", THEME["subtext"])
        self.badge_salary = self._create_badge(self.badges_frame, "Lương: -", THEME["green"])

        # Trạng thái học tập
        ctk.CTkLabel(self.badges_frame, text="Trạng thái:", font=ctk.CTkFont(size=12), text_color=THEME["subtext"]).pack(side="left", padx=(15, 5))
        self.cb_status = ctk.CTkComboBox(
            self.badges_frame,
            values=["New", "Learning", "Ready", "Applied"],
            width=110,
            height=26,
            command=self._on_status_change
        )
        self.cb_status.pack(side="left")

        # 2. Tabview 6 Tầng Kiến Thức
        self.tabview = ctk.CTkTabview(
            self.detail_frame,
            fg_color=THEME["surface0"],
            segmented_button_fg_color=THEME["crust"],
            segmented_button_selected_color=THEME["blue"],
            segmented_button_selected_hover_color="#74c7ec",
            segmented_button_unselected_color=THEME["surface0"],
            segmented_button_unselected_hover_color=THEME["surface1"],
            corner_radius=10
        )
        self.tabview.pack(fill="both", expand=True)

        self.tab_overview = self.tabview.add("📋 Tổng Quan")
        self.tab_skills = self.tabview.add("🛠️ Ma Trận Kỹ Năng")
        self.tab_roadmap = self.tabview.add("🧭 Lộ Trình Nắm Bắt")
        self.tab_resources = self.tabview.add("📚 Kho Tài Liệu")
        self.tab_interview = self.tabview.add("❓ Phỏng Vấn & Thực Chiến")
        self.tab_notes = self.tabview.add("📝 Ghi Chú & JD Gốc")

        self._build_tab_overview()
        self._build_tab_skills()
        self._build_tab_roadmap()
        self._build_tab_resources()
        self._build_tab_interview()
        self._build_tab_notes()

    def _create_badge(self, parent, text, color):
        lbl = ctk.CTkLabel(
            parent,
            text=text,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["crust"],
            text_color=color,
            corner_radius=6,
            padx=8,
            pady=2
        )
        lbl.pack(side="left", padx=4)
        return lbl

    # =====================================================================
    # BUILD CÁC TAB CHI TIẾT
    # =====================================================================
    def _build_tab_overview(self):
        scroll = ctk.CTkScrollableFrame(self.tab_overview, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=10, pady=10)

        # Card: Tóm tắt vai trò
        c1 = ctk.CTkFrame(scroll, fg_color=THEME["crust"], corner_radius=8)
        c1.pack(fill="x", pady=6, padx=5, ipady=8)
        ctk.CTkLabel(c1, text="🎯 Tóm Tắt Vai Trò (Role Mission):", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["yellow"]).pack(anchor="w", padx=12, pady=(4, 2))
        self.lbl_ov_summary = ctk.CTkLabel(c1, text="", font=ctk.CTkFont(size=13), text_color=THEME["text"], wraplength=750, justify="left")
        self.lbl_ov_summary.pack(anchor="w", padx=12, pady=(2, 6))

        # Card: Mục tiêu trọng tâm
        c2 = ctk.CTkFrame(scroll, fg_color=THEME["crust"], corner_radius=8)
        c2.pack(fill="x", pady=6, padx=5, ipady=8)
        ctk.CTkLabel(c2, text="🚀 Nhiệm Vụ Cốt Lõi Cần Hoàn Thành:", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["green"]).pack(anchor="w", padx=12, pady=(4, 2))
        self.lbl_ov_mission = ctk.CTkLabel(c2, text="", font=ctk.CTkFont(size=13), text_color=THEME["text"], wraplength=750, justify="left")
        self.lbl_ov_mission.pack(anchor="w", padx=12, pady=(2, 6))

        # Card: Hình thức làm việc & môi trường
        c3 = ctk.CTkFrame(scroll, fg_color=THEME["crust"], corner_radius=8)
        c3.pack(fill="x", pady=6, padx=5, ipady=8)
        ctk.CTkLabel(c3, text="🏢 Môi Trường & Chế Độ Làm Việc:", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["blue"]).pack(anchor="w", padx=12, pady=(4, 2))
        self.lbl_ov_mode = ctk.CTkLabel(c3, text="", font=ctk.CTkFont(size=13), text_color=THEME["text"], wraplength=750, justify="left")
        self.lbl_ov_mode.pack(anchor="w", padx=12, pady=(2, 6))

    def _build_tab_skills(self):
        self.scroll_skills = ctk.CTkScrollableFrame(self.tab_skills, fg_color="transparent")
        self.scroll_skills.pack(fill="both", expand=True, padx=10, pady=10)

    def _build_tab_roadmap(self):
        self.scroll_roadmap = ctk.CTkScrollableFrame(self.tab_roadmap, fg_color="transparent")
        self.scroll_roadmap.pack(fill="both", expand=True, padx=10, pady=10)

    def _build_tab_resources(self):
        self.scroll_resources = ctk.CTkScrollableFrame(self.tab_resources, fg_color="transparent")
        self.scroll_resources.pack(fill="both", expand=True, padx=10, pady=10)

    def _build_tab_interview(self):
        self.scroll_interview = ctk.CTkScrollableFrame(self.tab_interview, fg_color="transparent")
        self.scroll_interview.pack(fill="both", expand=True, padx=10, pady=10)

    def _build_tab_notes(self):
        container = ctk.CTkFrame(self.tab_notes, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=10, pady=10)

        # Cột trái: Ghi chú cá nhân
        left_box = ctk.CTkFrame(container, fg_color=THEME["crust"], corner_radius=8)
        left_box.pack(side="left", fill="both", expand=True, padx=(0, 6), pady=0)

        top_bar = ctk.CTkFrame(left_box, fg_color="transparent")
        top_bar.pack(fill="x", padx=10, pady=8)

        ctk.CTkLabel(top_bar, text="📝 Ghi Chú Cá Nhân & Kế Hoạch Ứng Tuyển:", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["yellow"]).pack(side="left")

        btn_save_notes = ctk.CTkButton(
            top_bar,
            text="💾 Lưu Ghi Chú",
            width=100,
            height=26,
            fg_color=THEME["blue"],
            hover_color="#74c7ec",
            text_color=THEME["crust"],
            command=self._save_notes
        )
        btn_save_notes.pack(side="right")

        self.txt_notes = ctk.CTkTextbox(
            left_box,
            fg_color=THEME["base"],
            text_color=THEME["text"],
            font=ctk.CTkFont(size=12),
            wrap="word"
        )
        self.txt_notes.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Cột phải: Raw JD
        right_box = ctk.CTkFrame(container, fg_color=THEME["crust"], corner_radius=8)
        right_box.pack(side="right", fill="both", expand=True, padx=(6, 0), pady=0)

        ctk.CTkLabel(right_box, text="📄 Văn Bản JD Gốc (Raw Job Description):", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["subtext"]).pack(anchor="w", padx=10, pady=8)

        self.txt_raw_jd = ctk.CTkTextbox(
            right_box,
            fg_color=THEME["base"],
            text_color=THEME["text"],
            font=ctk.CTkFont(family="Consolas", size=11),
            wrap="word"
        )
        self.txt_raw_jd.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    # =====================================================================
    # LOGIC NẠP DỮ LIỆU & HIỂN THỊ
    # =====================================================================
    def _seed_sample_data_if_empty(self):
        """Khởi tạo 2 hồ sơ công việc mẫu chất lượng cao nếu CSDL trống."""
        stats = self.storage.get_statistics()
        if stats["total"] == 0:
            sample_jd_python = """
Vị trí: Senior Backend Engineer (Python)
Công ty: TechNova Solutions
Địa điểm: Hà Nội (Hybrid)
Mức lương: 40.000.000 - 55.000.000 VNĐ

Mô tả công việc:
- Thiết kế và phát triển hệ thống backend xử lý dữ liệu lớn phục vụ hàng triệu người dùng.
- Tối ưu hóa API hiệu năng cao với Python (FastAPI / Django), CSDL PostgreSQL và Redis cache.
- Triển khai dịch vụ lên hạ tầng Kubernetes, sử dụng Docker và xây dựng CI/CD pipeline tự động.
- Làm việc theo mô hình Agile/Scrum, chủ trì Code Review và nâng cao tiêu chuẩn kỹ thuật toàn đội ngũ.

Yêu cầu:
- Tối thiểu 5 năm kinh nghiệm làm việc chuyên sâu với Python.
- Nắm vững kiến trúc Microservices, Asyncio, ORM, và xử lý bất đồng bộ.
- Thành thạo thiết kế cơ sở dữ liệu quan hệ, tối ưu Index và giải quyết lỗi chậm truy vấn trong PostgreSQL.
- Tư duy giải quyết vấn đề xuất sắc, chủ động học hỏi và chia sẻ kiến thức.
"""
            analyzer = JobAnalyzer()
            res1 = analyzer.analyze(sample_jd_python, force_offline=True)
            self.storage.add_job(
                title=res1["title"],
                company=res1["company"],
                level=res1["level"],
                category=res1["category"],
                raw_jd=res1["raw_jd"],
                analysis=res1["analysis"],
                location=res1["location"],
                salary_range=res1["salary_range"],
                tags=res1["tags"]
            )

            sample_jd_react = """
Vị trí: Junior Frontend Developer (React / TypeScript)
Công ty: FPT Digital Lab
Địa điểm: TP. Hồ Chí Minh
Mức lương: 12.000.000 - 18.000.000 VNĐ

Mô tả công việc:
- Phát triển giao diện người dùng hiện đại, responsive trên Web sử dụng ReactJS, TypeScript và TailwindCSS.
- Phối hợp chặt chẽ với UI/UX Designer và Backend team để tích hợp RESTful API.
- Tối ưu Core Web Vitals, đảm bảo trải nghiệm người dùng mượt mà trên nhiều thiết bị.

Yêu cầu:
- 1-2 năm kinh nghiệm với JavaScript (ES6+), ReactJS và TypeScript.
- Nắm vững React Hooks, State Management và cấu trúc Component.
- Sử dụng Git thành thạo. Tinh thần trách nhiệm và ham học hỏi.
"""
            res2 = analyzer.analyze(sample_jd_react, force_offline=True)
            self.storage.add_job(
                title=res2["title"],
                company=res2["company"],
                level=res2["level"],
                category=res2["category"],
                raw_jd=res2["raw_jd"],
                analysis=res2["analysis"],
                location=res2["location"],
                salary_range=res2["salary_range"],
                tags=res2["tags"]
            )

    def _load_jobs(self):
        """Tải danh sách công việc từ CSDL."""
        kw = self.txt_search.get().strip() if hasattr(self, "txt_search") else ""
        lvl = self.cb_level.get() if hasattr(self, "cb_level") else "Tất cả"
        cat = self.cb_cat.get() if hasattr(self, "cb_cat") else "Tất cả"

        self.all_jobs = self.storage.list_jobs(keyword=kw, level=lvl, category=cat)

        # Xóa bảng cũ
        for item in self.tree.get_children():
            self.tree.delete(item)

        for job in self.all_jobs:
            self.tree.insert("", "end", iid=str(job["id"]), values=(job["title"], job["company"], job["level"]))

        self.lbl_count.configure(text=f"Tổng số: {len(self.all_jobs)} công việc")

        # Chọn dòng đầu tiên nếu có
        children = self.tree.get_children()
        if children:
            self.tree.selection_set(children[0])
            self._display_job_detail(int(children[0]))

    def _debounce_search(self):
        if hasattr(self, "_search_timer") and self._search_timer:
            self.after_cancel(self._search_timer)
        self._search_timer = self.after(150, self._load_jobs)

    def _apply_filter(self):
        self._load_jobs()

    def _on_job_select(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        job_id = int(sel[0])
        self._display_job_detail(job_id)

    def _display_job_detail(self, job_id):
        job = self.storage.get_job(job_id)
        if not job:
            return
        self.current_job = job

        # 1. Header & Badges
        self.dt_title.configure(text=job["title"])
        self.lbl_company.configure(text=f"🏢 {job['company']}")
        self.badge_level.configure(text=f"Level: {job['level']}")
        self.badge_cat.configure(text=f"Ngành: {job['category']}")
        self.badge_loc.configure(text=f"📍 {job.get('location', 'N/A')}")
        self.badge_salary.configure(text=f"💰 {job.get('salary_range', 'Thỏa thuận')}")
        self.cb_status.set(job.get("status", "New"))

        analysis = job.get("analysis", {})
        overview = analysis.get("overview", {})

        # Tab 1: Overview
        self.lbl_ov_summary.configure(text=overview.get("summary", "Chưa có tóm tắt vai trò."))
        self.lbl_ov_mission.configure(text=overview.get("mission", "Chưa có thông tin nhiệm vụ."))
        self.lbl_ov_mode.configure(text=overview.get("work_mode", "N/A"))

        # Tab 2: Skills
        self._render_skills_tab(analysis.get("skills_matrix", {}))

        # Tab 3: Roadmap
        self._render_roadmap_tab(analysis.get("roadmap", []))

        # Tab 4: Resources
        self._render_resources_tab(analysis.get("resources", {}))

        # Tab 5: Interview
        self._render_interview_tab(analysis.get("interview_prep", []))

        # Tab 6: Notes & Raw
        self.txt_notes.delete("1.0", "end")
        self.txt_notes.insert("1.0", job.get("user_notes", ""))

        self.txt_raw_jd.delete("1.0", "end")
        self.txt_raw_jd.insert("1.0", job.get("raw_jd", ""))

    def _render_skills_tab(self, skills):
        for w in self.scroll_skills.winfo_children():
            w.destroy()

        def add_skill_section(title, items, icon, color):
            frame = ctk.CTkFrame(self.scroll_skills, fg_color=THEME["crust"], corner_radius=8)
            frame.pack(fill="x", pady=6, padx=5, ipady=6)
            ctk.CTkLabel(frame, text=f"{icon} {title}:", font=ctk.CTkFont(size=13, weight="bold"), text_color=color).pack(anchor="w", padx=12, pady=(4, 6))

            pill_box = ctk.CTkFrame(frame, fg_color="transparent")
            pill_box.pack(fill="x", padx=12, pady=(0, 4))

            if not items:
                ctk.CTkLabel(pill_box, text="(Không có thông tin)", text_color=THEME["subtext"], font=ctk.CTkFont(size=12)).pack(side="left")
                return

            for it in items:
                lbl = ctk.CTkLabel(
                    pill_box,
                    text=it,
                    font=ctk.CTkFont(size=12, weight="bold"),
                    fg_color=THEME["surface0"],
                    text_color=color,
                    corner_radius=6,
                    padx=10,
                    pady=3
                )
                lbl.pack(side="left", padx=4, pady=3)

        add_skill_section("Kỹ Năng Bắt Buộc (Must-Have / Core)", skills.get("must_have", []), "🔴", THEME["red"])
        add_skill_section("Kỹ Năng Ưu Tiên / Điểm Cộng (Nice-To-Have)", skills.get("nice_to_have", []), "🟢", THEME["green"])
        add_skill_section("Công Cụ & Môi Trường Làm Việc (Tools)", skills.get("tools", []), "⚙️", THEME["blue"])
        add_skill_section("Kỹ Năng Mềm & Phương Pháp Luận", skills.get("soft_skills", []), "💡", THEME["yellow"])

    def _render_roadmap_tab(self, roadmap):
        for w in self.scroll_roadmap.winfo_children():
            w.destroy()

        if not roadmap:
            ctk.CTkLabel(self.scroll_roadmap, text="Chưa có lộ trình phân rã.", text_color=THEME["subtext"]).pack(pady=20)
            return

        for idx, phase in enumerate(roadmap, 1):
            card = ctk.CTkFrame(self.scroll_roadmap, fg_color=THEME["crust"], corner_radius=8)
            card.pack(fill="x", pady=8, padx=5, ipady=8)

            p_title = phase.get("phase", f"Giai đoạn {idx}")
            ctk.CTkLabel(card, text=f"🧭 {p_title}", font=ctk.CTkFont(size=14, weight="bold"), text_color=THEME["blue"]).pack(anchor="w", padx=15, pady=(6, 4))

            # Goals
            goals = phase.get("goals", [])
            if goals:
                ctk.CTkLabel(card, text="Mục tiêu trọng tâm:", font=ctk.CTkFont(size=12, weight="bold"), text_color=THEME["yellow"]).pack(anchor="w", padx=15, pady=(2, 2))
                for g in goals:
                    ctk.CTkLabel(card, text=f"  • {g}", font=ctk.CTkFont(size=12), text_color=THEME["text"], wraplength=700, justify="left").pack(anchor="w", padx=15, pady=1)

            # Actions with checkboxes
            actions = phase.get("action_items", [])
            if actions:
                ctk.CTkLabel(card, text="Hành động cụ thể (Checklist):", font=ctk.CTkFont(size=12, weight="bold"), text_color=THEME["green"]).pack(anchor="w", padx=15, pady=(6, 2))
                for a in actions:
                    cb = ctk.CTkCheckBox(card, text=a, font=ctk.CTkFont(size=12), text_color=THEME["text"], fg_color=THEME["blue"], hover_color="#74c7ec")
                    cb.pack(anchor="w", padx=20, pady=2)

    def _render_resources_tab(self, resources):
        for w in self.scroll_resources.winfo_children():
            w.destroy()

        # 1. Official Documentation
        docs = resources.get("official_docs", [])
        c1 = ctk.CTkFrame(self.scroll_resources, fg_color=THEME["crust"], corner_radius=8)
        c1.pack(fill="x", pady=6, padx=5, ipady=6)
        ctk.CTkLabel(c1, text="🌐 Tài Liệu Chính Thống (Official Documentation):", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["blue"]).pack(anchor="w", padx=12, pady=(4, 6))

        if docs:
            for d in docs:
                row = ctk.CTkFrame(c1, fg_color=THEME["surface0"], corner_radius=6)
                row.pack(fill="x", padx=12, pady=3, ipady=4)

                name = d.get("name", "Docs")
                url = d.get("url", "#")
                desc = d.get("desc", "")

                info_box = ctk.CTkFrame(row, fg_color="transparent")
                info_box.pack(side="left", padx=10, fill="x", expand=True)
                ctk.CTkLabel(info_box, text=name, font=ctk.CTkFont(size=12, weight="bold"), text_color=THEME["text"]).pack(anchor="w")
                if desc:
                    ctk.CTkLabel(info_box, text=desc, font=ctk.CTkFont(size=11), text_color=THEME["subtext"]).pack(anchor="w")

                btn_open = ctk.CTkButton(
                    row,
                    text="🔗 Mở Web",
                    width=80,
                    height=26,
                    fg_color=THEME["blue"],
                    hover_color="#74c7ec",
                    text_color=THEME["crust"],
                    command=lambda u=url: webbrowser.open(u)
                )
                btn_open.pack(side="right", padx=10)
        else:
            ctk.CTkLabel(c1, text="Chưa có tài liệu.", text_color=THEME["subtext"]).pack(padx=12, pady=4)

        # 2. Books
        books = resources.get("books", [])
        c2 = ctk.CTkFrame(self.scroll_resources, fg_color=THEME["crust"], corner_radius=8)
        c2.pack(fill="x", pady=6, padx=5, ipady=6)
        ctk.CTkLabel(c2, text="📖 Sách & Giáo Trình Kinh Điển:", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["peach"]).pack(anchor="w", padx=12, pady=(4, 6))
        for b in books:
            ctk.CTkLabel(c2, text=f"  📚 {b}", font=ctk.CTkFont(size=12), text_color=THEME["text"]).pack(anchor="w", padx=12, pady=2)

        # 3. Search Keywords
        keywords = resources.get("search_keywords", [])
        c3 = ctk.CTkFrame(self.scroll_resources, fg_color=THEME["crust"], corner_radius=8)
        c3.pack(fill="x", pady=6, padx=5, ipady=6)
        ctk.CTkLabel(c3, text="🔍 Từ Khóa Vàng Tra Cứu Google / GitHub:", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["yellow"]).pack(anchor="w", padx=12, pady=(4, 6))
        kw_box = ctk.CTkFrame(c3, fg_color="transparent")
        kw_box.pack(fill="x", padx=12, pady=(0, 4))
        for kw in keywords:
            lbl = ctk.CTkLabel(
                kw_box,
                text=f"`{kw}`",
                font=ctk.CTkFont(family="Consolas", size=11),
                fg_color=THEME["surface0"],
                text_color=THEME["yellow"],
                corner_radius=4,
                padx=8,
                pady=2
            )
            lbl.pack(side="left", padx=4, pady=3)

    def _render_interview_tab(self, interview):
        for w in self.scroll_interview.winfo_children():
            w.destroy()

        if not interview:
            ctk.CTkLabel(self.scroll_interview, text="Chưa có câu hỏi phỏng vấn.", text_color=THEME["subtext"]).pack(pady=20)
            return

        for idx, item in enumerate(interview, 1):
            card = ctk.CTkFrame(self.scroll_interview, fg_color=THEME["crust"], corner_radius=8)
            card.pack(fill="x", pady=6, padx=5, ipady=6)

            q_text = item.get("question", "")
            q_type = item.get("type", "General")
            key_points = item.get("key_points", "")

            # Header câu hỏi
            top_row = ctk.CTkFrame(card, fg_color="transparent")
            top_row.pack(fill="x", padx=12, pady=(4, 2))

            ctk.CTkLabel(
                top_row,
                text=f"Câu {idx} [{q_type}]",
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color=THEME["mauve"]
            ).pack(side="left")

            ctk.CTkLabel(
                card,
                text=q_text,
                font=ctk.CTkFont(size=13, weight="bold"),
                text_color=THEME["text"],
                wraplength=720,
                justify="left"
            ).pack(anchor="w", padx=12, pady=(2, 6))

            # Khung gợi ý trả lời (Collapsible frame)
            ans_frame = ctk.CTkFrame(card, fg_color=THEME["surface0"], corner_radius=6)
            ans_frame.pack(fill="x", padx=12, pady=(0, 6), ipady=4)

            ctk.CTkLabel(
                ans_frame,
                text="💡 Gợi ý trả lời & Điểm mấu chốt:",
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=THEME["green"]
            ).pack(anchor="w", padx=10, pady=(2, 2))

            ctk.CTkLabel(
                ans_frame,
                text=key_points,
                font=ctk.CTkFont(size=12),
                text_color=THEME["text"],
                wraplength=700,
                justify="left"
            ).pack(anchor="w", padx=10, pady=(0, 4))

    # =====================================================================
    # CÁC HÀNH ĐỘNG NGƯỜI DÙNG
    # =====================================================================
    def _open_add_dialog(self):
        AddJobDialog(self, on_save_callback=self._on_job_saved)

    def _on_job_saved(self, result):
        job_id = self.storage.add_job(
            title=result["title"],
            company=result["company"],
            level=result["level"],
            category=result["category"],
            raw_jd=result["raw_jd"],
            analysis=result["analysis"],
            location=result.get("location", ""),
            salary_range=result.get("salary_range", ""),
            tags=result.get("tags", [])
        )
        self._load_jobs()
        # Chọn ngay công việc vừa thêm
        if str(job_id) in self.tree.get_children():
            self.tree.selection_set(str(job_id))
            self._display_job_detail(job_id)

    def _delete_selected_job(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Chưa chọn", "Vui lòng chọn công việc cần xóa!")
            return

        job_id = int(sel[0])
        job = self.storage.get_job(job_id)
        if not job:
            return

        confirm = messagebox.askyesno(
            "Xác nhận xóa",
            f"Bạn có chắc chắn muốn xóa hồ sơ công việc:\n'{job['title']} - {job['company']}' không?"
        )
        if confirm:
            self.storage.delete_job(job_id)
            self._load_jobs()

    def _on_status_change(self, new_status):
        if self.current_job:
            self.storage.update_status(self.current_job["id"], new_status)
            self.current_job["status"] = new_status

    def _save_notes(self):
        if not self.current_job:
            return
        notes = self.txt_notes.get("1.0", "end-1c").strip()
        self.storage.update_notes(self.current_job["id"], notes)
        self.current_job["user_notes"] = notes
        messagebox.showinfo("Thành công", "Đã lưu ghi chú cá nhân!")

    def _copy_markdown(self):
        if not self.current_job:
            messagebox.showwarning("Chưa chọn", "Vui lòng chọn công việc cần copy báo cáo!")
            return
        md = self.storage.export_job_markdown(self.current_job["id"])
        self.clipboard_clear()
        self.clipboard_append(md)
        messagebox.showinfo("Đã sao chép", "Đã sao chép toàn bộ hồ sơ Markdown vào bộ nhớ tạm (Clipboard)!")

    def _export_markdown_file(self):
        if not self.current_job:
            messagebox.showwarning("Chưa chọn", "Vui lòng chọn công việc cần xuất file!")
            return

        clean_title = "".join(c for c in self.current_job["title"] if c.isalnum() or c in (" ", "_", "-")).strip()
        default_name = f"JD_{clean_title}_{self.current_job['company']}.md".replace(" ", "_")

        filepath = filedialog.asksaveasfilename(
            parent=self,
            title="Lưu Hồ Sơ Công Việc (Markdown)",
            initialfile=default_name,
            defaultextension=".md",
            filetypes=[("Markdown Files", "*.md"), ("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            md = self.storage.export_job_markdown(self.current_job["id"])
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(md)
            messagebox.showinfo("Xuất thành công", f"Đã lưu hồ sơ Markdown tại:\n{filepath}")

    def _show_statistics(self):
        stats = self.storage.get_statistics()
        msg = [
            f"📊 TỔNG QUAN HỒ SƠ CÔNG VIỆC: {stats['total']} vị trí\n",
            "📌 Theo Cấp Bậc (Level):"
        ]
        for lvl, cnt in stats["by_level"].items():
            msg.append(f"  • {lvl}: {cnt}")

        msg.append("\n🛠️ Theo Ngành Nghề (Category):")
        for cat, cnt in stats["by_category"].items():
            msg.append(f"  • {cat}: {cnt}")

        msg.append("\n📈 Theo Trạng Thái (Status):")
        for st, cnt in stats["by_status"].items():
            msg.append(f"  • {st}: {cnt}")

        messagebox.showinfo("Thống Kê JobDetail Hub", "\n".join(msg))


def main():
    app = JobDetailApp()
    app.mainloop()


if __name__ == "__main__":
    main()
