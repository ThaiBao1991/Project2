#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
JobDetailApp.py - Ứng Dụng Quản Lý & Tra Cứu Hồ Sơ Công Việc (JobDetail Intelligence Hub)
Tuân thủ tiêu chuẩn python_desktop_standards.md và customtkinter_perf_ui:
  - CustomTkinter + C-Engine tk.Text / tk.Listbox / ttk.Treeview Dark Mode (Catppuccin Mocha)
  - Lazy Tab Rendering + Zero Canvas Saturation (60fps Zero-Lag, tải tức thì < 100ms)
  - Click-Anywhere Term Glossary: Bấm vào bất kỳ thuật ngữ nào (MES, Minitab, OEE, SMED, XLPE...)
    ở mọi nơi trong ứng dụng đều mở ngay định nghĩa + khả năng áp dụng & ví dụ thực tế tại CADIVI!
  - Mô hình 5 Tầng Kiến Thức + 23 Cẩm Nang 100% Offline + 146 Câu Hỏi Phỏng Vấn + 202 Thuật Ngữ + Giáo Trình A–Z 32 Bài + Lưu Trình Dòng Chảy CADIVI & 40 Tình Huống OE + Công Cụ Tính OE & Phỏng Vấn 30p
"""

import os
import re
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
import offline_knowledge
try:
    import interview_bank
except Exception:
    interview_bank = None

try:
    import term_glossary
except Exception:
    term_glossary = None

try:
    import oe_curriculum
except Exception:
    oe_curriculum = None

try:
    import cadivi_factory_flows
except Exception:
    cadivi_factory_flows = None

try:
    import oe_calculators
except Exception:
    oe_calculators = None

# =====================================================================
# HỆ MÀU CATPPUCCIN MOCHA ĐỒNG NHẤT
# =====================================================================
THEME = {
    "base": "#1e1e2e",         # Nền chính
    "mantle": "#181825",       # Sidebar / Header
    "crust": "#11111b",        # Nền sâu nhất
    "surface0": "#313244",     # Khung card / Border
    "surface1": "#45475a",     # Card highlight
    "surface2": "#585b70",     # Đường kẻ phân cách / Viền phụ
    "text": "#cdd6f4",         # Chữ chính
    "subtext": "#a6adc8",      # Chữ phụ
    "blue": "#89b4fa",         # Accent chính
    "cyan": "#89dceb",         # Màu link thuật ngữ Click-Anywhere
    "green": "#a6e3a1",        # Thành công / Must-have
    "yellow": "#f9e2af",       # Cảnh báo / Soft skills
    "red": "#f38ba8",          # Bắt buộc / Xóa
    "mauve": "#cba6f7",        # Tím nổi bật
    "peach": "#fab387",        # Cam điểm nhấn
}

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# =====================================================================
# BỘ CÔNG CỤ C-ENGINE RICH TEXT + CLICK-ANYWHERE GLOSSARY HYPERLINKS
# =====================================================================
def sanitize_math_markup(text):
    """Lọc và chuyển đổi triệt để bất kỳ mã LaTeX còn sót sang Unicode toán học đẹp."""
    if not text:
        return ""
    text = text.replace("\x0crac", "/").replace("\x0c", "")
    text = re.sub(r'\\?t?ext\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\mathbf\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1) / (\2)', text)
    text = re.sub(r'_\{([^}]+)\}', r'_\1', text)
    text = re.sub(r'\\min\\left\(([^)]+)\)', r'min[\1]', text)
    text = text.replace(r'$\rightarrow$', '→').replace(r'\rightarrow', '→').replace('ightarrow', '→')
    text = text.replace(r'\times', '×').replace('\times', '×')
    text = text.replace(r'\ge', '≥').replace(r'\le', '≤')
    text = text.replace(r'\mu', 'μ').replace(r'\sigma', 'σ').replace(r'\Delta', 'Δ')
    text = text.replace(r'\phi', 'Ø').replace(r'\pm', '±')
    text = text.replace(r'\%', '%')
    lines = []
    for line in text.splitlines():
        if "ENV PATH=" in line:
            lines.append(line)
        else:
            lines.append(line.replace("$", ""))
    return "\n".join(lines)


def create_c_engine_text(parent, bg=None, font=("Segoe UI", 12), padx=14, pady=10):
    """
    Tạo widget tk.Text viết bằng C-engine tích hợp ttk.Scrollbar Dark Mode.
    Tốc độ render nhanh hơn 50-100 lần so với CTkScrollableFrame nhiều widget Canvas,
    hỗ trợ cuộn 60fps, chọn bôi đen copy chữ và click trực tiếp thuật ngữ!
    """
    bg_color = bg or THEME["crust"]
    wrapper = ctk.CTkFrame(parent, fg_color=bg_color, corner_radius=8, border_width=1, border_color=THEME["surface0"])
    tb = tk.Text(
        wrapper,
        bg=bg_color,
        fg=THEME["text"],
        insertbackground=THEME["blue"],
        selectbackground=THEME["surface1"],
        selectforeground="#ffffff",
        font=font,
        wrap="word",
        relief="flat",
        borderwidth=0,
        highlightthickness=0,
        padx=padx,
        pady=pady,
        spacing2=2,
        cursor="arrow",
    )
    sb = ttk.Scrollbar(wrapper, orient="vertical", command=tb.yview)
    tb.configure(yscrollcommand=sb.set)
    sb.pack(side="right", fill="y", padx=(0, 2), pady=4)
    tb.pack(side="left", fill="both", expand=True, padx=(2, 0), pady=2)
    configure_rich_text_tags(tb)
    return wrapper, tb


def configure_rich_text_tags(tb):
    """Cấu hình toàn bộ style tag chuẩn Catppuccin Mocha cho C-engine tk.Text."""
    tb.tag_config("h1", font=("Segoe UI", 15, "bold"), foreground=THEME["blue"], spacing1=10, spacing3=5)
    tb.tag_config("h2", font=("Segoe UI", 13, "bold"), foreground=THEME["green"], spacing1=10, spacing3=4)
    tb.tag_config("h3", font=("Segoe UI", 12, "bold"), foreground=THEME["yellow"], spacing1=7, spacing3=2)
    tb.tag_config("sec_red", font=("Segoe UI", 13, "bold"), foreground=THEME["red"], spacing1=10, spacing3=4)
    tb.tag_config("sec_green", font=("Segoe UI", 13, "bold"), foreground=THEME["green"], spacing1=10, spacing3=4)
    tb.tag_config("sec_blue", font=("Segoe UI", 13, "bold"), foreground=THEME["blue"], spacing1=10, spacing3=4)
    tb.tag_config("sec_yellow", font=("Segoe UI", 13, "bold"), foreground=THEME["yellow"], spacing1=10, spacing3=4)
    tb.tag_config("sec_peach", font=("Segoe UI", 13, "bold"), foreground=THEME["peach"], spacing1=10, spacing3=4)
    tb.tag_config("sec_mauve", font=("Segoe UI", 13, "bold"), foreground=THEME["mauve"], spacing1=10, spacing3=4)
    tb.tag_config("divider", font=("Consolas", 9), foreground=THEME.get("surface2", THEME["surface1"]), spacing1=4, spacing3=4)
    tb.tag_config("mathbox", font=("Consolas", 11), foreground=THEME["green"], background=THEME["mantle"], lmargin1=10, lmargin2=10)
    tb.tag_config("codeblock", font=("Consolas", 11), foreground=THEME["text"], background=THEME["mantle"], lmargin1=10, lmargin2=10)
    tb.tag_config("bullet", font=("Segoe UI", 11), foreground=THEME["text"], lmargin1=18, lmargin2=32, spacing1=2, spacing3=2)
    tb.tag_config("skill_red", font=("Segoe UI", 11), foreground=THEME["text"], background=THEME["mantle"], lmargin1=16, lmargin2=28, rmargin=12, spacing1=3, spacing3=3)
    tb.tag_config("skill_green", font=("Segoe UI", 11), foreground=THEME["text"], background=THEME["mantle"], lmargin1=16, lmargin2=28, rmargin=12, spacing1=3, spacing3=3)
    tb.tag_config("skill_blue", font=("Segoe UI", 11), foreground=THEME["text"], background=THEME["mantle"], lmargin1=16, lmargin2=28, rmargin=12, spacing1=3, spacing3=3)
    tb.tag_config("skill_yellow", font=("Segoe UI", 11), foreground=THEME["text"], background=THEME["mantle"], lmargin1=16, lmargin2=28, rmargin=12, spacing1=3, spacing3=3)
    tb.tag_config("card_box", font=("Segoe UI", 11), foreground=THEME["text"], background=THEME["mantle"], lmargin1=14, lmargin2=14, rmargin=14, spacing1=3, spacing3=4)
    tb.tag_config("q_title", font=("Segoe UI", 12, "bold"), foreground="#ffffff", lmargin1=8, lmargin2=8, spacing1=4, spacing3=4)
    tb.tag_config("ans_header", font=("Segoe UI", 10, "bold"), foreground=THEME["green"], background=THEME["mantle"], lmargin1=14, lmargin2=14, rmargin=14, spacing1=4, spacing3=2)
    tb.tag_config("ans_body", font=("Segoe UI", 11), foreground=THEME["text"], background=THEME["mantle"], lmargin1=18, lmargin2=28, rmargin=14, spacing1=1, spacing3=2)
    tb.tag_config("badge_peach", font=("Segoe UI", 10, "bold"), foreground=THEME["peach"], lmargin1=8)
    tb.tag_config("badge_mauve", font=("Segoe UI", 10, "bold"), foreground=THEME["mauve"], lmargin1=8)
    tb.tag_config("badge_blue", font=("Segoe UI", 10, "bold"), foreground=THEME["blue"], lmargin1=8)
    tb.tag_config("badge_green", font=("Segoe UI", 10, "bold"), foreground=THEME["green"])
    tb.tag_config("badge_sub", font=("Segoe UI", 10, "bold"), foreground=THEME["subtext"], lmargin1=8)
    tb.tag_config("bold", font=("Segoe UI", 11, "bold"), foreground="#ffffff")
    tb.tag_config("bold_inline", font=("Segoe UI", 11, "bold"), foreground="#ffffff")
    tb.tag_config("italic_inline", font=("Segoe UI", 11, "italic"), foreground=THEME["subtext"])
    tb.tag_config("inline_code", font=("Consolas", 10), foreground=THEME["yellow"], background=THEME["surface0"])
    tb.tag_config("normal", font=("Segoe UI", 11), foreground=THEME["text"], spacing1=2, spacing3=2)
    tb.tag_config("subtext", font=("Segoe UI", 10, "italic"), foreground=THEME["subtext"])
    tb.tag_config("raw_mono", font=("Consolas", 11), foreground=THEME["text"], spacing1=1, spacing3=1)
    tb.tag_config("chk_off", font=("Segoe UI", 12, "bold"), foreground=THEME["blue"])
    tb.tag_config("chk_on", font=("Segoe UI", 12, "bold"), foreground=THEME["green"])
    tb.tag_config("chk_done_txt", font=("Segoe UI", 11), foreground=THEME["subtext"], overstrike=True)
    # Tag nút tương tác chế độ luyện phỏng vấn (Active Recall)
    tb.tag_config("iv_toggle_btn", font=("Segoe UI", 10, "bold"), foreground=THEME["crust"], background=THEME["blue"])
    tb.tag_config("iv_ok_btn", font=("Segoe UI", 10, "bold"), foreground=THEME["crust"], background=THEME["green"])
    tb.tag_config("iv_rev_btn", font=("Segoe UI", 10, "bold"), foreground=THEME["crust"], background=THEME["peach"])
    tb.tag_config("iv_dim_btn", font=("Segoe UI", 10, "bold"), foreground=THEME["subtext"], background=THEME["surface0"])
    tb.tag_config("iv_status_ok", font=("Segoe UI", 10, "bold"), foreground=THEME["green"])
    tb.tag_config("iv_status_rev", font=("Segoe UI", 10, "bold"), foreground=THEME["peach"])
    # Tag tìm kiếm Ctrl+F trong cẩm nang
    tb.tag_config("find_highlight", background=THEME["surface2"], foreground=THEME["yellow"])
    tb.tag_config("find_current", background=THEME["yellow"], foreground=THEME["crust"])
    # Tag thuật ngữ có thể click ở mọi nơi (MES gạch chân cyan)
    tb.tag_config("term_link", foreground=THEME["cyan"], underline=True)
    tb.tag_config("term_link_bold", font=("Segoe UI", 11, "bold"), foreground=THEME["cyan"], underline=True)
    tb.tag_config("related_pill", font=("Segoe UI", 10, "bold"), foreground=THEME["crust"], background=THEME["cyan"])
    tb.tag_raise("term_link")
    tb.tag_raise("term_link_bold")
    tb.tag_raise("related_pill")
    tb.tag_raise("find_highlight")
    tb.tag_raise("find_current")
    tb.tag_raise("sel")


class TermHoverTooltip:
    """
    Tooltip siêu nhẹ tự hiện khi di chuột qua bất kỳ thuật ngữ gạch chân nào (MES, OEE, Minitab...).
    Tự động ẩn ngay khi rời chuột, cuộn trang hoặc bấm click để không bao giờ bị kẹt trên màn hình.
    """
    def __init__(self, widget):
        self.widget = widget
        self.tip_win = None
        self.current_key = None
        self._after_id = None

    def schedule(self, term_key, x_root, y_root):
        if term_key == self.current_key and self.tip_win is not None:
            return
        self.hide()
        self.current_key = term_key
        self._after_id = self.widget.after(180, lambda: self._show(term_key, x_root, y_root))

    def _show(self, term_key, x_root, y_root):
        if not term_glossary or not self.widget.winfo_exists():
            return
        info = term_glossary.get_term(term_key)
        if not info:
            return
        self.hide()
        self.current_key = term_key
        tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.configure(bg=THEME["cyan"])
        # Tính vị trí hiển thị tránh tràn màn hình phải/dưới
        scr_w = tw.winfo_screenwidth()
        scr_h = tw.winfo_screenheight()
        px = min(x_root + 14, max(10, scr_w - 430))
        py = min(y_root + 18, max(10, scr_h - 140))
        tw.wm_geometry(f"+{px}+{py}")

        inner = tk.Frame(tw, bg=THEME["mantle"], padx=10, pady=7)
        inner.pack(padx=1, pady=1)

        tk.Label(
            inner,
            text=f"📖 {info['term']} — {info['full_name']}",
            bg=THEME["mantle"], fg=THEME["cyan"],
            font=("Segoe UI", 10, "bold"), justify="left", wraplength=390, anchor="w"
        ).pack(anchor="w")
        tk.Label(
            inner,
            text=info.get("short_desc", ""),
            bg=THEME["mantle"], fg=THEME["text"],
            font=("Segoe UI", 9), justify="left", wraplength=390, anchor="w"
        ).pack(anchor="w", pady=(3, 2))
        tk.Label(
            inner,
            text="💡 Bấm chuột trái để xem đầy đủ định nghĩa, công thức & ví dụ CADIVI",
            bg=THEME["mantle"], fg=THEME["green"],
            font=("Segoe UI", 8, "italic"), anchor="w"
        ).pack(anchor="w")
        self.tip_win = tw

    def hide(self, _event=None):
        if self._after_id is not None:
            try:
                self.widget.after_cancel(self._after_id)
            except Exception:
                pass
            self._after_id = None
        if self.tip_win is not None:
            try:
                self.tip_win.destroy()
            except Exception:
                pass
            self.tip_win = None
        self.current_key = None


def bind_glossary_links(tb, on_term_click):
    """
    Gắn duy nhất bộ sự kiện C-engine lên tag 'term_link' và 'related_pill'
    kèm Live Hover Tooltip xem nhanh tóm tắt 1 dòng trước khi click!
    Chống nuốt click khi chuột rung 1-5px giữa nhấn và thả chuột.
    """
    tooltip = TermHoverTooltip(tb)
    tb._glossary_tooltip = tooltip
    press_pos = [None]

    def _get_term_at_coords(x, y):
        idx = tb.index(f"@{x},{y}")
        for tag in tb.tag_names(idx):
            if tag.startswith("term::"):
                return tag[6:]
        return None

    def _get_term_at_event(event):
        return _get_term_at_coords(event.x, event.y)

    def _on_press(event):
        press_pos[0] = (event.x, event.y)

    def _on_enter(event):
        tb.configure(cursor="hand2")
        key = _get_term_at_event(event)
        if key:
            tooltip.schedule(key, event.x_root, event.y_root)

    def _on_motion(event):
        key = _get_term_at_event(event)
        if key:
            tooltip.schedule(key, event.x_root, event.y_root)
        else:
            tooltip.hide()

    def _on_leave(_event):
        tb.configure(cursor="arrow")
        tooltip.hide()

    def _on_click(event):
        tooltip.hide()
        p = press_pos[0]
        press_pos[0] = None
        if p is not None:
            dist = max(abs(event.x - p[0]), abs(event.y - p[1]))
            # Chỉ bỏ qua khi người dùng thực sự kéo chuột bôi đen (> 5px) để copy
            if dist > 5 and tb.tag_ranges("sel"):
                return
        elif tb.tag_ranges("sel"):
            return
        key = _get_term_at_event(event)
        if not key and p is not None and max(abs(event.x - p[0]), abs(event.y - p[1])) <= 5:
            key = _get_term_at_coords(p[0], p[1])
        if key and on_term_click:
            tb.tag_remove("sel", "1.0", "end")
            on_term_click(key)
            return "break"

    tb.bind("<ButtonPress-1>", _on_press, add="+")
    tb.bind("<ButtonRelease-1>", _on_click, add="+")
    for link_tag in ("term_link", "related_pill"):
        tb.tag_bind(link_tag, "<Enter>", _on_enter)
        tb.tag_bind(link_tag, "<Motion>", _on_motion)
        tb.tag_bind(link_tag, "<Leave>", _on_leave)

    tb.bind("<MouseWheel>", tooltip.hide, add="+")
    tb.bind("<FocusOut>", tooltip.hide, add="+")
    tb.bind("<Destroy>", tooltip.hide, add="+")


_INLINE_MD_RE = re.compile(r"(`[^`\n]+`|\*\*[^*\n]+?\*\*|(?<!\*)\*(?!\s)[^*\n]+?(?<!\s)\*(?!\*))")
_HEADING_BASE_TAGS = {"h1", "h2", "h3", "q_title", "sec_red", "sec_green", "sec_blue", "sec_yellow", "sec_peach", "sec_mauve"}


def insert_with_glossary(tb, text, base_tag="normal", extra_tags=(), exclude_key=None):
    """
    Chèn văn bản vào tk.Text, tự động render sạch định dạng nội dòng (**in đậm**, *in nghiêng*, `code`),
    giải mã công thức tường minh [[TermKey|DisplayText]] kết hợp tự động nhận diện thuật ngữ
    — hiển thị chữ xanh gạch chân (MES gạch chân).
    Khi exclude_key được truyền (trong cửa sổ định nghĩa của chính thuật ngữ đó),
    tự động bỏ tự-link (self-link) để không còn hiện tượng bấm vào không nhảy!
    """
    if not text:
        return
    base_tuple = (base_tag,) + tuple(extra_tags)
    is_heading = base_tag in _HEADING_BASE_TAGS
    exclude_norm = exclude_key.strip().lower() if exclude_key else None

    def _emit_chunk(chunk_text, style_tags, is_bold_chunk=False):
        if not chunk_text:
            return
        if not term_glossary:
            tb.insert("end", chunk_text, style_tags)
            return
        segments = term_glossary.parse_rich_segments(chunk_text, auto_detect=True)
        for seg_text, canonical_key in segments:
            if canonical_key and (not exclude_norm or canonical_key.strip().lower() != exclude_norm):
                link_tags = ("term_link", "term_link_bold", f"term::{canonical_key}") if (is_bold_chunk and not is_heading) else ("term_link", f"term::{canonical_key}")
                tb.insert("end", seg_text, style_tags + link_tags)
            elif canonical_key and exclude_norm and canonical_key.strip().lower() == exclude_norm and not is_heading and not is_bold_chunk:
                # Tên của chính thuật ngữ đang mở: in đậm rõ ràng, KHÔNG gạch chân tự-link
                tb.insert("end", seg_text, style_tags + ("bold_inline",))
            else:
                tb.insert("end", seg_text, style_tags)

    cursor = 0
    for m in _INLINE_MD_RE.finditer(text):
        if m.start() > cursor:
            _emit_chunk(text[cursor:m.start()], base_tuple, is_bold_chunk=False)
        token = m.group(0)
        if token.startswith("`") and token.endswith("`") and len(token) >= 3:
            _emit_chunk(token[1:-1], base_tuple + ("inline_code",), is_bold_chunk=False)
        elif token.startswith("**") and token.endswith("**") and len(token) >= 5:
            inner = token[2:-2]
            b_tags = base_tuple if is_heading else base_tuple + ("bold_inline",)
            _emit_chunk(inner, b_tags, is_bold_chunk=True)
        elif token.startswith("*") and token.endswith("*") and len(token) >= 3:
            inner = token[1:-1]
            i_tags = base_tuple if is_heading else base_tuple + ("italic_inline",)
            _emit_chunk(inner, i_tags, is_bold_chunk=False)
        else:
            _emit_chunk(token, base_tuple, is_bold_chunk=False)
        cursor = m.end()

    if cursor < len(text):
        _emit_chunk(text[cursor:], base_tuple, is_bold_chunk=False)


# =====================================================================
# CỬA SỔ POPUP TRA CỨU THUẬT NGỮ CHUYÊN SÂU (CLICK-ANYWHERE POPUP)
# =====================================================================
class TermDetailPopup(ctk.CTkToplevel):
    """
    Cửa sổ tra cứu tức thì (< 15ms) hiển thị bài giảng mini đầy đủ: định nghĩa gốc, công thức/chuẩn,
    khả năng áp dụng, 2–3 ví dụ số liệu thực tế CADIVI & sai lầm cần tránh.
    Loại bỏ 100% tự-link (self-link), hỗ trợ Breadcrumb lịch sử Quay lại, nhảy Cẩm Nang & Giáo Trình A–Z!
    """
    def __init__(self, parent, term_key, open_doc_callback=None, open_lesson_callback=None):
        super().__init__(parent)
        self.parent = parent
        self.open_doc_callback = open_doc_callback
        self.open_lesson_callback = open_lesson_callback
        self.history = []
        self.current_info = None

        self.title("📖 Tra Cứu Thuật Ngữ OE & Dây Cáp Điện (CADIVI)")
        self.geometry("880x700")
        self.minsize(680, 520)
        self.configure(fg_color=THEME["base"])
        self.transient(parent)
        self.bind("<Escape>", lambda e: self.destroy())

        self._build_ui()
        self.show_term(term_key, push_history=False)
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _build_ui(self):
        container = ctk.CTkFrame(self, fg_color=THEME["base"])
        container.pack(fill="both", expand=True, padx=16, pady=14)

        # Header Bar
        top_bar = ctk.CTkFrame(container, fg_color=THEME["surface0"], corner_radius=8)
        top_bar.pack(fill="x", pady=(0, 10), ipady=6)

        row1 = ctk.CTkFrame(top_bar, fg_color="transparent")
        row1.pack(fill="x", padx=12, pady=(2, 4))

        self.lbl_cat = ctk.CTkLabel(
            row1, text="📚 THUẬT NGỮ",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=THEME["green"]
        )
        self.lbl_cat.pack(side="left")

        # Nút thao tác nhanh
        btn_close = ctk.CTkButton(
            row1, text="Đóng (Esc)", width=80, height=26,
            fg_color=THEME["surface1"], hover_color=THEME["red"],
            text_color=THEME["text"], command=self.destroy
        )
        btn_close.pack(side="right")

        btn_copy = ctk.CTkButton(
            row1, text="📋 Copy", width=70, height=26,
            fg_color=THEME["surface1"], hover_color=THEME["mauve"],
            text_color=THEME["text"], command=self._copy_term
        )
        btn_copy.pack(side="right", padx=(0, 6))

        self.btn_open_lesson = ctk.CTkButton(
            row1, text="🎓 Bài Giáo Trình", width=130, height=26,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["mauve"], hover_color=THEME["blue"],
            text_color=THEME["crust"], state="disabled",
            command=self._open_linked_lesson
        )
        self.btn_open_lesson.pack(side="right", padx=(0, 6))

        self.btn_open_doc = ctk.CTkButton(
            row1, text="📖 Cẩm Nang Gốc", width=128, height=26,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["green"], hover_color="#74c7ec",
            text_color=THEME["crust"], command=self._open_linked_doc
        )
        self.btn_open_doc.pack(side="right", padx=(0, 6))

        self.btn_back = ctk.CTkButton(
            row1, text="⬅ Quay lại", width=80, height=26,
            fg_color=THEME["surface1"], hover_color=THEME["blue"],
            text_color=THEME["text"], state="disabled",
            command=self._go_back
        )
        self.btn_back.pack(side="right", padx=(0, 6))

        # Tiêu đề thuật ngữ
        self.lbl_title = ctk.CTkLabel(
            top_bar, text="",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=THEME["cyan"],
            wraplength=820, justify="left", anchor="w"
        )
        self.lbl_title.pack(fill="x", padx=12, pady=(0, 2))

        self.lbl_breadcrumb = ctk.CTkLabel(
            top_bar, text="💡 Mẹo: Bấm vào thuật ngữ màu xanh gạch chân bên dưới để tra cứu mở rộng!",
            font=ctk.CTkFont(size=11),
            text_color=THEME["subtext"], anchor="w", wraplength=820, justify="left"
        )
        self.lbl_breadcrumb.pack(fill="x", padx=12, pady=(0, 2))

        # Nội dung chính dùng C-Engine tk.Text
        txt_wrap, self.tb = create_c_engine_text(container, bg=THEME["crust"], font=("Segoe UI", 11))
        txt_wrap.pack(fill="both", expand=True)
        bind_glossary_links(self.tb, lambda k: self.show_term(k, push_history=True))

    def show_term(self, term_key, push_history=True):
        if not term_glossary:
            return
        info = term_glossary.get_term(term_key)
        if not info:
            return

        if push_history and self.current_info and self.current_info["term"] != info["term"]:
            self.history.append(self.current_info["term"])
        self.current_info = info
        cur_key = info["term"]

        self.btn_back.configure(state="normal" if self.history else "disabled")
        self.title(f"📖 Thuật Ngữ: {cur_key} — {info['full_name']}")
        self.lbl_cat.configure(text=f"🏷️ {info.get('category', 'Thuật Ngữ')}  •  TRA CỨU TỨC THÌ 100% OFFLINE")
        self.lbl_title.configure(text=f"{cur_key}  —  {info['full_name']}")

        trail = (self.history[-4:] + [cur_key]) if self.history else [cur_key]
        trail_str = " › ".join(trail)
        self.lbl_breadcrumb.configure(
            text=f"📍 Hành trình tra cứu: {trail_str}   •   💡 Bấm vào thuật ngữ xanh gạch chân bất kỳ để nhảy tiếp!"
        )

        doc_key = info.get("doc_key", "")
        if doc_key and self.open_doc_callback:
            self.btn_open_doc.configure(state="normal")
        else:
            self.btn_open_doc.configure(state="disabled")

        lesson_id = info.get("lesson_id", "")
        if lesson_id and self.open_lesson_callback:
            self.btn_open_lesson.configure(text=f"🎓 Học Bài {lesson_id}", state="normal")
        else:
            self.btn_open_lesson.configure(text="🎓 Bài Giáo Trình", state="disabled")

        tb = self.tb
        tb.configure(state="normal")
        tb.delete("1.0", "end")

        # 1. Tóm tắt nhanh
        tb.insert("end", "⚡ TÓM TẮT NHANH (HIỂU TRONG 10 GIÂY)\n", "sec_yellow")
        insert_with_glossary(tb, info.get("short_desc", "") + "\n\n", "card_box", exclude_key=cur_key)

        # 2. Định nghĩa & Bản chất
        tb.insert("end", "📌 1. ĐỊNH NGHĨA ĐẦY ĐỦ & BẢN CHẤT KỸ THUẬT\n", "sec_blue")
        insert_with_glossary(tb, info.get("definition", "") + "\n\n", "normal", exclude_key=cur_key)

        # 3. Công thức / Thông số / Tiêu chuẩn
        if info.get("formula_or_spec"):
            tb.insert("end", "📐 2. CÔNG THỨC / THÔNG SỐ / TIÊU CHUẨN CỐT LÕI\n", "sec_green")
            tb.insert("end", sanitize_math_markup(info["formula_or_spec"]) + "\n\n", "mathbox")

        # 4. Khả năng áp dụng tại Nhà máy CADIVI Miền Trung
        tb.insert("end", "🏭 3. KHẢ NĂNG & KỊCH BẢN ÁP DỤNG TẠI NHÀ MÁY CADIVI MIỀN TRUNG\n", "sec_peach")
        insert_with_glossary(tb, info.get("cadivi_application", "") + "\n\n", "normal", exclude_key=cur_key)

        # 5. Ví dụ số liệu thực tế & đời sống
        tb.insert("end", "💡 4. VÍ DỤ THỰC TẾ & SỐ LIỆU CHI TIẾT TẠI CADIVI\n", "sec_mauve")
        insert_with_glossary(tb, info.get("cadivi_example", "") + "\n\n", "ans_body", exclude_key=cur_key)

        # 6. Sai lầm kinh điển cần tránh & mẹo thực chiến OE
        if info.get("common_mistakes"):
            tb.insert("end", "⚠️ 5. SAI LẦM KINH ĐIỂN CẦN TRÁNH & MẸO THỰC CHIẾN OE\n", "sec_red")
            insert_with_glossary(tb, info["common_mistakes"] + "\n\n", "card_box", exclude_key=cur_key)

        # 7. Thuật ngữ liên quan
        related = [r for r in info.get("related", []) if r != cur_key]
        if related:
            tb.insert("end", "─" * 76 + "\n", "divider")
            tb.insert("end", "🔗 THUẬT NGỮ LIÊN QUAN (Bấm để nhảy nhanh sang định nghĩa):\n", "sec_yellow")
            for rel in related:
                rel_info = term_glossary.get_term(rel)
                if rel_info and rel_info["term"] != cur_key:
                    tb.insert("end", f"  {rel_info['term']}  ", ("related_pill", f"term::{rel_info['term']}"))
                    tb.insert("end", "   ", "normal")
            tb.insert("end", "\n", "normal")

        tb.tag_raise("term_link")
        tb.tag_raise("term_link_bold")
        tb.tag_raise("related_pill")
        tb.tag_raise("sel")
        tb.see("1.0")
        tb.configure(state="disabled")
        self.lift()

    def _go_back(self):
        if self.history:
            prev_key = self.history.pop()
            self.show_term(prev_key, push_history=False)

    def _open_linked_doc(self):
        if self.current_info and self.current_info.get("doc_key") and self.open_doc_callback:
            self.open_doc_callback(self.current_info["doc_key"])

    def _open_linked_lesson(self):
        if self.current_info and self.current_info.get("lesson_id") and self.open_lesson_callback:
            self.open_lesson_callback(self.current_info["lesson_id"])

    def _copy_term(self):
        if not self.current_info:
            return
        i = self.current_info
        parts = [
            f"{i['term']} — {i['full_name']}",
            f"1. Định nghĩa:\n{i['definition']}",
            f"2. Công thức / Chuẩn:\n{i.get('formula_or_spec', '')}",
            f"3. Áp dụng tại Nhà máy CADIVI Miền Trung:\n{i['cadivi_application']}",
            f"4. Ví dụ thực tế tại CADIVI:\n{i['cadivi_example']}",
        ]
        if i.get("common_mistakes"):
            parts.append(f"5. Sai lầm cần tránh & Mẹo thực chiến OE:\n{i['common_mistakes']}")
        txt = "\n\n".join(parts) + "\n"
        if term_glossary:
            txt = term_glossary.strip_term_formulas(txt)
        self.clipboard_clear()
        self.clipboard_append(txt)
        messagebox.showinfo("Đã sao chép", f"Đã sao chép bài giảng mini & ví dụ CADIVI của '{i['term']}'!", parent=self)


# =====================================================================
# CỬA SỔ TỪ ĐIỂN THUẬT NGỮ 60FPS (C-ENGINE TK.LISTBOX + LIVE FILTER)
# =====================================================================
class GlossaryBrowserDialog(ctk.CTkToplevel):
    """Trình duyệt toàn bộ 202 thuật ngữ OE & CADIVI dùng C-engine tk.Listbox lọc 60fps."""
    def __init__(self, parent, open_doc_callback=None, open_lesson_callback=None):
        super().__init__(parent)
        self.parent = parent
        self.open_doc_callback = open_doc_callback
        self.open_lesson_callback = open_lesson_callback
        self.filtered_terms = []
        self.current_info = None

        total = len(term_glossary.get_all_terms()) if term_glossary else 0
        self.title(f"📖 Từ Điển Thuật Ngữ OE & Dây Cáp Điện CADIVI ({total} Thuật Ngữ — 100% Offline)")
        self.geometry("1080x700")
        self.minsize(840, 540)
        self.configure(fg_color=THEME["base"])
        self.transient(parent)
        self.bind("<Escape>", lambda e: self.destroy())

        self._build_ui()
        self._refresh_list()
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _build_ui(self):
        main = ctk.CTkFrame(self, fg_color=THEME["base"])
        main.pack(fill="both", expand=True, padx=14, pady=12)

        # Cột trái: Tìm kiếm + Lọc nhóm + C-Engine tk.Listbox
        left = ctk.CTkFrame(main, fg_color=THEME["mantle"], width=320, corner_radius=8)
        left.pack(side="left", fill="y", padx=(0, 12))
        left.pack_propagate(False)

        ctk.CTkLabel(
            left, text="🔍 Tra Cứu Thuật Ngữ Nhanh",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=THEME["cyan"]
        ).pack(anchor="w", padx=12, pady=(10, 6))

        self.ent_search = ctk.CTkEntry(
            left, placeholder_text="Gõ Six Sigma, MES, Minitab, OEE, XLPE...",
            height=34, fg_color=THEME["crust"],
            border_color=THEME["surface0"], text_color=THEME["text"]
        )
        self.ent_search.pack(fill="x", padx=12, pady=(0, 6))
        self.ent_search.bind("<KeyRelease>", lambda e: self._refresh_list())

        cats = term_glossary.get_categories() if term_glossary else ["Tất cả nhóm"]
        self.cb_cat = ctk.CTkComboBox(
            left, values=cats, height=30,
            fg_color=THEME["crust"], border_color=THEME["surface0"],
            command=lambda v: self._refresh_list()
        )
        self.cb_cat.set("Tất cả nhóm")
        self.cb_cat.pack(fill="x", padx=12, pady=(0, 6))

        self.lbl_cnt = ctk.CTkLabel(left, text="0 thuật ngữ", font=ctk.CTkFont(size=11), text_color=THEME["subtext"])
        self.lbl_cnt.pack(anchor="w", padx=12, pady=(0, 4))

        # C-Engine Listbox Dark Mode (tải 10,000 mục < 2ms theo customtkinter_perf_ui)
        lb_wrap = ctk.CTkFrame(left, fg_color=THEME["crust"], corner_radius=6)
        lb_wrap.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        sb = ttk.Scrollbar(lb_wrap, orient="vertical")
        self.lb = tk.Listbox(
            lb_wrap,
            bg=THEME["crust"],
            fg=THEME["text"],
            selectbackground=THEME["blue"],
            selectforeground=THEME["crust"],
            activestyle="none",
            font=("Segoe UI", 11),
            highlightthickness=0,
            borderwidth=0,
            yscrollcommand=sb.set
        )
        sb.configure(command=self.lb.yview)
        sb.pack(side="right", fill="y")
        self.lb.pack(side="left", fill="both", expand=True, padx=4, pady=4)
        self.lb.bind("<<ListboxSelect>>", self._on_select)
        self.lb.bind("<Return>", self._on_select)

        # Cột phải: Nội dung chi tiết thuật ngữ
        right = ctk.CTkFrame(main, fg_color=THEME["base"])
        right.pack(side="right", fill="both", expand=True)

        hdr = ctk.CTkFrame(right, fg_color=THEME["surface0"], corner_radius=8)
        hdr.pack(fill="x", pady=(0, 8), ipady=6)

        hdr_row = ctk.CTkFrame(hdr, fg_color="transparent")
        hdr_row.pack(fill="x", padx=12, pady=(2, 2))

        self.lbl_r_cat = ctk.CTkLabel(hdr_row, text="", font=ctk.CTkFont(size=11, weight="bold"), text_color=THEME["green"])
        self.lbl_r_cat.pack(side="left")

        self.btn_r_doc = ctk.CTkButton(
            hdr_row, text="📖 Cẩm Nang Sâu", width=130, height=26,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["green"], hover_color="#74c7ec",
            text_color=THEME["crust"], command=self._open_doc
        )
        self.btn_r_doc.pack(side="right")

        self.btn_r_lesson = ctk.CTkButton(
            hdr_row, text="🎓 Bài Giáo Trình", width=130, height=26,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["mauve"], hover_color=THEME["blue"],
            text_color=THEME["crust"], state="disabled",
            command=self._open_lesson
        )
        self.btn_r_lesson.pack(side="right", padx=(0, 6))

        self.lbl_r_title = ctk.CTkLabel(
            hdr, text="Chọn một thuật ngữ bên trái",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color=THEME["cyan"], wraplength=680, justify="left", anchor="w"
        )
        self.lbl_r_title.pack(fill="x", padx=12, pady=(2, 2))

        txt_wrap, self.tb = create_c_engine_text(right, bg=THEME["crust"], font=("Segoe UI", 11))
        txt_wrap.pack(fill="both", expand=True)
        bind_glossary_links(self.tb, self._jump_to_term)

    def _refresh_list(self):
        if not term_glossary:
            return
        kw = self.ent_search.get().strip()
        cat = self.cb_cat.get()
        self.filtered_terms = term_glossary.search_terms(kw, cat)
        self.lb.delete(0, "end")
        for info in self.filtered_terms:
            self.lb.insert("end", f"  {info['term']}  —  {info['full_name'][:34]}")
        self.lbl_cnt.configure(text=f"Hiển thị: {len(self.filtered_terms)} thuật ngữ")
        if self.filtered_terms:
            self.lb.selection_set(0)
            self._show_info(self.filtered_terms[0])

    def _on_select(self, _event=None):
        sel = self.lb.curselection()
        if not sel:
            return
        idx = sel[0]
        if 0 <= idx < len(self.filtered_terms):
            self._show_info(self.filtered_terms[idx])

    def _jump_to_term(self, term_key):
        if not term_glossary:
            return
        info = term_glossary.get_term(term_key)
        if not info:
            return
        self._show_info(info)
        for idx, item in enumerate(self.filtered_terms):
            if item["term"] == info["term"]:
                self.lb.selection_clear(0, "end")
                self.lb.selection_set(idx)
                self.lb.see(idx)
                break

    def _show_info(self, info):
        self.current_info = info
        cur_key = info["term"]
        self.lbl_r_cat.configure(text=f"🏷️ {info.get('category', '')}")
        self.lbl_r_title.configure(text=f"{cur_key}  —  {info['full_name']}")
        self.btn_r_doc.configure(state="normal" if info.get("doc_key") and self.open_doc_callback else "disabled")
        lid = info.get("lesson_id", "")
        if lid and self.open_lesson_callback:
            self.btn_r_lesson.configure(text=f"🎓 Học Bài {lid}", state="normal")
        else:
            self.btn_r_lesson.configure(text="🎓 Bài Giáo Trình", state="disabled")

        tb = self.tb
        tb.configure(state="normal")
        tb.delete("1.0", "end")

        tb.insert("end", "⚡ TÓM TẮT NHANH\n", "sec_yellow")
        insert_with_glossary(tb, info.get("short_desc", "") + "\n\n", "card_box", exclude_key=cur_key)

        tb.insert("end", "📌 1. ĐỊNH NGHĨA ĐẦY ĐỦ & BẢN CHẤT\n", "sec_blue")
        insert_with_glossary(tb, info.get("definition", "") + "\n\n", "normal", exclude_key=cur_key)

        if info.get("formula_or_spec"):
            tb.insert("end", "📐 2. CÔNG THỨC / THÔNG SỐ / TIÊU CHUẨN\n", "sec_green")
            tb.insert("end", sanitize_math_markup(info["formula_or_spec"]) + "\n\n", "mathbox")

        tb.insert("end", "🏭 3. KHẢ NĂNG ÁP DỤNG TẠI NHÀ MÁY CADIVI MIỀN TRUNG\n", "sec_peach")
        insert_with_glossary(tb, info.get("cadivi_application", "") + "\n\n", "normal", exclude_key=cur_key)

        tb.insert("end", "💡 4. VÍ DỤ THỰC TẾ & SỐ LIỆU CHI TIẾT TẠI CADIVI\n", "sec_mauve")
        insert_with_glossary(tb, info.get("cadivi_example", "") + "\n\n", "ans_body", exclude_key=cur_key)

        if info.get("common_mistakes"):
            tb.insert("end", "⚠️ 5. SAI LẦM KINH ĐIỂN CẦN TRÁNH & MẸO THỰC CHIẾN OE\n", "sec_red")
            insert_with_glossary(tb, info["common_mistakes"] + "\n\n", "card_box", exclude_key=cur_key)

        related = [r for r in info.get("related", []) if r != cur_key]
        if related:
            tb.insert("end", "─" * 70 + "\n", "divider")
            tb.insert("end", "🔗 THUẬT NGỮ LIÊN QUAN:\n", "sec_yellow")
            for rel in related:
                rel_info = term_glossary.get_term(rel)
                if rel_info and rel_info["term"] != cur_key:
                    tb.insert("end", f"  {rel_info['term']}  ", ("related_pill", f"term::{rel_info['term']}"))
                    tb.insert("end", "   ", "normal")
            tb.insert("end", "\n", "normal")

        tb.tag_raise("term_link")
        tb.tag_raise("term_link_bold")
        tb.tag_raise("related_pill")
        tb.tag_raise("sel")
        tb.see("1.0")
        tb.configure(state="disabled")

    def _open_doc(self):
        if self.current_info and self.current_info.get("doc_key") and self.open_doc_callback:
            self.open_doc_callback(self.current_info["doc_key"])

    def _open_lesson(self):
        if self.current_info and self.current_info.get("lesson_id") and self.open_lesson_callback:
            self.open_lesson_callback(self.current_info["lesson_id"])


# =====================================================================
# CỬA SỔ THÊM JD MỚI
# =====================================================================
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

        self.transient(parent)
        self.grab_set()
        self.bind("<Escape>", lambda e: self.destroy())

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


# =====================================================================
# TRÌNH ĐỌC CẨM NANG 100% OFFLINE (HỖ TRỢ CLICK THUẬT NGỮ MỌI NƠI)
# =====================================================================
class OfflineDocViewer(ctk.CTkToplevel):
    """Cửa sổ đọc Cẩm Nang Kỹ Thuật 100% Offline tích hợp Click-Anywhere Term Glossary."""
    def __init__(self, parent, title, content, category="Tài Liệu", on_term_click=None):
        super().__init__(parent)
        self.parent = parent
        self.doc_title = title
        self.content = content
        self.category = category
        self.on_term_click = on_term_click
        self._toc_map = {}
        self._find_matches = []
        self._find_idx = -1

        self.title(f"📖 Cẩm Nang Offline: {title}")
        self.geometry("980x760")
        self.minsize(760, 540)
        self.configure(fg_color=THEME["base"])

        self.transient(parent)
        self.bind("<Escape>", lambda e: self.destroy())
        self.bind("<Control-f>", self._focus_find)
        self.bind("<Control-F>", self._focus_find)
        self.bind("<F3>", lambda e: self._find_next())
        self.bind("<Shift-F3>", lambda e: self._find_prev())

        self._build_ui()
        self.center_window()

    def center_window(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _handle_term_click(self, term_key):
        if self.on_term_click:
            self.on_term_click(term_key)
        else:
            TermDetailPopup(self, term_key)

    def _build_ui(self):
        container = ctk.CTkFrame(self, fg_color=THEME["base"])
        container.pack(fill="both", expand=True, padx=20, pady=15)

        top_bar = ctk.CTkFrame(container, fg_color=THEME["surface0"], corner_radius=8)
        top_bar.pack(fill="x", pady=(0, 10), padx=2, ipady=6)

        left_info = ctk.CTkFrame(top_bar, fg_color="transparent")
        left_info.pack(side="left", padx=15, fill="x", expand=True)

        ctk.CTkLabel(
            left_info,
            text=f"📚 {self.category} • 100% OFFLINE HANDBOOK • 💡 Bấm vào từ xanh (MES, OEE, Minitab...) để tra cứu nhanh",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=THEME["green"]
        ).pack(anchor="w")

        ctk.CTkLabel(
            left_info,
            text=self.doc_title,
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color=THEME["blue"],
            wraplength=640,
            justify="left"
        ).pack(anchor="w", pady=(2, 0))

        btn_box = ctk.CTkFrame(top_bar, fg_color="transparent")
        btn_box.pack(side="right", padx=15)

        btn_copy = ctk.CTkButton(
            btn_box,
            text="📋 Copy Nội Dung",
            width=120,
            height=30,
            fg_color=THEME["surface1"],
            hover_color=THEME["mauve"],
            text_color=THEME["text"],
            command=self._copy_content
        )
        btn_copy.pack(side="left", padx=(0, 8))

        btn_close = ctk.CTkButton(
            btn_box,
            text="Đóng",
            width=70,
            height=30,
            fg_color=THEME["surface1"],
            hover_color=THEME["red"],
            text_color=THEME["text"],
            command=self.destroy
        )
        btn_close.pack(side="left")

        # Thanh công cụ Mục lục nhảy nhanh (TOC) & Tìm kiếm trong bài (Ctrl+F)
        nav_bar = ctk.CTkFrame(container, fg_color=THEME["mantle"], corner_radius=8)
        nav_bar.pack(fill="x", pady=(0, 8), padx=2, ipady=4)

        ctk.CTkLabel(
            nav_bar, text="📑 Mục lục:",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=THEME["yellow"]
        ).pack(side="left", padx=(10, 4))

        self.cbo_toc = ctk.CTkComboBox(
            nav_bar, values=["(Đang nạp mục lục...)"], width=330, height=28,
            fg_color=THEME["surface0"], border_color=THEME["surface1"],
            button_color=THEME["surface1"], text_color=THEME["text"],
            command=self._jump_to_toc
        )
        self.cbo_toc.pack(side="left", padx=(0, 12), pady=2)

        self.lbl_find_cnt = ctk.CTkLabel(
            nav_bar, text="0/0", width=46,
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=THEME["subtext"]
        )
        self.lbl_find_cnt.pack(side="right", padx=(2, 10))

        ctk.CTkButton(
            nav_bar, text="▼", width=28, height=28,
            fg_color=THEME["surface0"], hover_color=THEME["blue"],
            text_color=THEME["text"], command=self._find_next
        ).pack(side="right", padx=2)

        ctk.CTkButton(
            nav_bar, text="▲", width=28, height=28,
            fg_color=THEME["surface0"], hover_color=THEME["blue"],
            text_color=THEME["text"], command=self._find_prev
        ).pack(side="right", padx=2)

        self.ent_find = ctk.CTkEntry(
            nav_bar, placeholder_text="🔍 Tìm trong cẩm nang (Ctrl+F)...",
            width=210, height=28,
            fg_color=THEME["crust"], border_color=THEME["surface1"],
            text_color=THEME["text"]
        )
        self.ent_find.pack(side="right", padx=(6, 4), pady=2)
        self.ent_find.bind("<KeyRelease>", lambda e: self._find_in_doc())
        self.ent_find.bind("<Return>", lambda e: self._find_next())

        # Khung văn bản C-Engine tk.Text hỗ trợ Rich Syntax, Math Box & Clickable Glossary
        txt_wrap, self.txt_content = create_c_engine_text(container, bg=THEME["crust"], font=("Segoe UI", 12))
        txt_wrap.pack(fill="both", expand=True, pady=(0, 6))
        bind_glossary_links(self.txt_content, self._handle_term_click)
        self._render_styled_content()

    def _focus_find(self, _event=None):
        if hasattr(self, "ent_find"):
            self.ent_find.focus_set()
            self.ent_find.select_range(0, "end")
        return "break"

    def _jump_to_toc(self, label):
        idx = self._toc_map.get(label)
        if idx:
            self.txt_content.see(idx)
            self.txt_content.mark_set("insert", idx)

    def _find_in_doc(self, query=None):
        tb = self.txt_content
        tb.tag_remove("find_highlight", "1.0", "end")
        tb.tag_remove("find_current", "1.0", "end")
        self._find_matches = []
        self._find_idx = -1

        kw = (query if query is not None else self.ent_find.get()).strip()
        if not kw:
            self.lbl_find_cnt.configure(text="0/0", text_color=THEME["subtext"])
            return 0

        start = "1.0"
        while True:
            pos = tb.search(kw, start, stopindex="end", nocase=True)
            if not pos:
                break
            end_pos = f"{pos}+{len(kw)}c"
            self._find_matches.append((pos, end_pos))
            tb.tag_add("find_highlight", pos, end_pos)
            start = end_pos

        if self._find_matches:
            self._find_idx = 0
            self._highlight_current_match()
        else:
            self.lbl_find_cnt.configure(text="0/0", text_color=THEME["red"])
        return len(self._find_matches)

    def _highlight_current_match(self):
        tb = self.txt_content
        tb.tag_remove("find_current", "1.0", "end")
        if not self._find_matches or not (0 <= self._find_idx < len(self._find_matches)):
            return
        s, e = self._find_matches[self._find_idx]
        tb.tag_add("find_current", s, e)
        tb.tag_raise("find_current")
        tb.see(s)
        self.lbl_find_cnt.configure(
            text=f"{self._find_idx + 1}/{len(self._find_matches)}",
            text_color=THEME["green"]
        )

    def _find_next(self):
        if not self._find_matches:
            if self.ent_find.get().strip():
                self._find_in_doc()
            return
        self._find_idx = (self._find_idx + 1) % len(self._find_matches)
        self._highlight_current_match()

    def _find_prev(self):
        if not self._find_matches:
            return
        self._find_idx = (self._find_idx - 1) % len(self._find_matches)
        self._highlight_current_match()

    def _render_styled_content(self):
        """Duyệt từng dòng văn bản, tô màu Markdown, dựng Mục lục TOC và gắn link thuật ngữ tự động."""
        cleaned_text = self._sanitize_math_markup(self.content)
        tb = self.txt_content
        tb.configure(state="normal")
        tb.delete("1.0", "end")
        self._toc_map = {}
        toc_labels = []

        lines = cleaned_text.split("\n")
        in_code_block = False
        code_tag = "codeblock"

        for line in lines:
            stripped = line.strip()

            if stripped.startswith("```"):
                in_code_block = not in_code_block
                if in_code_block and any(k in stripped for k in ["text", "math"]):
                    code_tag = "mathbox"
                elif in_code_block:
                    code_tag = "codeblock"
                continue

            if in_code_block:
                safe_line = term_glossary.strip_term_formulas(line) if term_glossary else line
                tb.insert("end", safe_line + "\n", code_tag)
                continue

            if any(c in line for c in ["┌", "└", "│", "─", "├", "┤", "┬", "┴", "┼"]):
                safe_line = term_glossary.strip_term_formulas(line) if term_glossary else line
                tb.insert("end", safe_line + "\n", "mathbox")
                continue

            if stripped.startswith("# ") and not stripped.startswith("## "):
                line_idx = tb.index("end-1c linestart")
                clean_h = term_glossary.strip_term_formulas(stripped[2:]) if term_glossary else stripped[2:]
                clean_h = clean_h.replace("**", "").replace("`", "").strip()
                lbl = f"📌 {clean_h[:58]}"
                if lbl not in self._toc_map:
                    self._toc_map[lbl] = line_idx
                    toc_labels.append(lbl)
                insert_with_glossary(tb, stripped[2:] + "\n", "h1")
            elif stripped.startswith("## "):
                line_idx = tb.index("end-1c linestart")
                clean_h = term_glossary.strip_term_formulas(stripped[3:]) if term_glossary else stripped[3:]
                clean_h = clean_h.replace("**", "").replace("`", "").strip()
                lbl = f"▸ {clean_h[:58]}"
                if lbl not in self._toc_map:
                    self._toc_map[lbl] = line_idx
                    toc_labels.append(lbl)
                insert_with_glossary(tb, stripped[3:] + "\n", "h2")
            elif stripped.startswith("### "):
                line_idx = tb.index("end-1c linestart")
                clean_h = term_glossary.strip_term_formulas(stripped[4:]) if term_glossary else stripped[4:]
                clean_h = clean_h.replace("**", "").replace("`", "").strip()
                lbl = f"   • {clean_h[:54]}"
                if lbl not in self._toc_map:
                    self._toc_map[lbl] = line_idx
                    toc_labels.append(lbl)
                insert_with_glossary(tb, stripped[4:] + "\n", "h3")
            elif stripped in ["---", "===", "***"]:
                tb.insert("end", "─" * 70 + "\n", "divider")
            elif stripped.startswith("- ") or stripped.startswith("* ") or stripped.startswith("• "):
                bullet_text = "• " + stripped[2:].strip()
                insert_with_glossary(tb, bullet_text + "\n", "bullet")
            else:
                insert_with_glossary(tb, line + "\n", "normal")

        if hasattr(self, "cbo_toc"):
            if toc_labels:
                self.cbo_toc.configure(values=toc_labels)
                self.cbo_toc.set(toc_labels[0])
            else:
                self.cbo_toc.configure(values=["(Không có mục lục)"])
                self.cbo_toc.set("(Không có mục lục)")

        tb.tag_raise("term_link")
        tb.tag_raise("term_link_bold")
        tb.tag_raise("find_highlight")
        tb.tag_raise("find_current")
        tb.tag_raise("sel")
        tb.configure(state="disabled")

    def _sanitize_math_markup(self, text):
        return sanitize_math_markup(text)

    def _copy_content(self):
        cleaned = self._sanitize_math_markup(self.content)
        if term_glossary:
            cleaned = term_glossary.strip_term_formulas(cleaned)
        self.clipboard_clear()
        self.clipboard_append(cleaned)
        messagebox.showinfo("Đã sao chép", "Đã sao chép toàn bộ cẩm nang vào Clipboard!", parent=self)


# =====================================================================
# ỨNG DỤNG CHÍNH: JOBDETAIL INTELLIGENCE HUB (ZERO-LAG 60FPS)
# =====================================================================
class JobDetailApp(ctk.CTk):
    """Giao diện chính của ứng dụng JobDetail Intelligence Hub — Tối ưu Zero-Lag & Click-Anywhere Glossary."""
    def __init__(self):
        super().__init__()
        self.storage = JobStorage()
        self.current_job = None
        self.all_jobs = []
        self._dirty_tabs = set()
        self._current_interview_raw = []
        self._filtered_interview_items = []
        self._current_progress = {"roadmap": {}, "interview": {}, "curriculum": {}, "factory_flow": {}}
        self._roadmap_checked = {}
        self._interview_progress = {}
        self._curriculum_done = {}
        self._curriculum_lessons_view = []
        self._current_lesson_id = None
        self._factory_flow_done = {}
        self._flow_mode = "🗺️ 10 Trạm End-to-End"
        self._flow_items_view = []
        self._current_flow_item = None
        self._quiz_mode = False
        self._revealed_qids = set()
        self._term_popup = None
        self._glossary_dialog = None
        self._calc_dialog = None
        self._mock_dialog = None
        self._interview_search_timer = None

        self.title("💼 JobDetail Intelligence Hub — Quản Lý & Tra Cứu Hồ Sơ Công Việc (Zero-Lag + Clickable Glossary)")
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
        style.configure(
            "Vertical.TScrollbar",
            background=THEME["surface0"],
            troughcolor=THEME["crust"],
            bordercolor=THEME["crust"],
            arrowcolor=THEME["subtext"],
            relief="flat"
        )
        style.map("Vertical.TScrollbar", background=[("active", THEME["surface1"])])

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
            text="⚡ 60fps  •  💡 Bấm thuật ngữ xanh (MES, OEE...) để tra định nghĩa & ví dụ CADIVI",
            font=ctk.CTkFont(size=12),
            text_color=THEME["cyan"]
        )
        lbl_sub.pack(side="left", padx=5)

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
            width=92,
            command=self._show_statistics
        )
        btn_stats.pack(side="right", padx=(0, 6))

        term_cnt = len(term_glossary.get_all_terms()) if term_glossary else 0
        btn_glossary = ctk.CTkButton(
            self.header_bar,
            text=f"📖 Từ Điển ({term_cnt})",
            font=ctk.CTkFont(weight="bold"),
            fg_color=THEME["surface0"],
            hover_color=THEME["cyan"],
            text_color=THEME["cyan"],
            height=32,
            width=118,
            command=self._open_glossary_browser
        )
        btn_glossary.pack(side="right", padx=(0, 6))

        btn_mock = ctk.CTkButton(
            self.header_bar,
            text="🎤 Phỏng Vấn 30p",
            font=ctk.CTkFont(weight="bold"),
            fg_color=THEME["mauve"],
            hover_color=THEME["blue"],
            text_color=THEME["crust"],
            height=32,
            width=126,
            command=self._open_mock_interview
        )
        btn_mock.pack(side="right", padx=(0, 6))

        btn_calc = ctk.CTkButton(
            self.header_bar,
            text="🧮 Công Cụ OE",
            font=ctk.CTkFont(weight="bold"),
            fg_color=THEME["surface0"],
            hover_color=THEME["green"],
            text_color=THEME["green"],
            height=32,
            width=112,
            command=self._open_oe_calculators
        )
        btn_calc.pack(side="right", padx=(0, 6))

        # 2. Main Content Split Pane
        self.main_split = ctk.CTkFrame(self, fg_color=THEME["base"], corner_radius=0)
        self.main_split.pack(fill="both", expand=True)

        self._build_sidebar(self.main_split)
        self._build_detail_view(self.main_split)

    def _build_sidebar(self, parent):
        self.sidebar = ctk.CTkFrame(parent, fg_color=THEME["mantle"], width=360, corner_radius=0)
        self.sidebar.pack(side="left", fill="y", padx=0, pady=0)
        self.sidebar.pack_propagate(False)

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

        filters_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        filters_frame.pack(fill="x", padx=15, pady=(0, 10))

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

        ctk.CTkLabel(filters_frame, text="Ngành:", font=ctk.CTkFont(size=11), text_color=THEME["subtext"]).grid(row=1, column=0, sticky="w", pady=2)
        self.cb_cat = ctk.CTkComboBox(
            filters_frame,
            values=["Tất cả", "Sản Xuất (Manufacturing)", "Lean / IE", "Backend", "Frontend", "Fullstack", "DevOps", "AI/Data", "Mobile", "QA", "Khác"],
            command=lambda v: self._apply_filter(),
            height=28,
            width=150,
            fg_color=THEME["crust"],
            border_color=THEME["surface0"]
        )
        self.cb_cat.set("Tất cả")
        self.cb_cat.grid(row=1, column=1, sticky="ew", padx=(5, 0), pady=2)

        filters_frame.columnconfigure(1, weight=1)

        tree_container = ctk.CTkFrame(self.sidebar, fg_color=THEME["crust"], corner_radius=6)
        tree_container.pack(fill="both", expand=True, padx=15, pady=(0, 10))

        cols = ("title", "company", "level")
        self.tree = ttk.Treeview(tree_container, columns=cols, show="headings", style="Dark.Treeview", selectmode="browse")
        self.tree.heading("title", text="Vị Trí Tuyển Dụng")
        self.tree.heading("company", text="Công Ty")
        self.tree.heading("level", text="Cấp Bậc")

        self.tree.column("title", width=170, anchor="w")
        self.tree.column("company", width=105, anchor="w")
        self.tree.column("level", width=55, anchor="center")

        tree_scroll = ttk.Scrollbar(tree_container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=tree_scroll.set)

        self.tree.pack(side="left", fill="both", expand=True)
        tree_scroll.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self._on_job_select)

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
        self.detail_frame.pack(side="right", fill="both", expand=True, padx=16, pady=12)

        # 1. Header chi tiết công việc
        self.dt_header = ctk.CTkFrame(self.detail_frame, fg_color=THEME["surface0"], corner_radius=10)
        self.dt_header.pack(fill="x", pady=(0, 10), padx=2)

        action_bar = ctk.CTkFrame(self.dt_header, fg_color="transparent")
        action_bar.pack(fill="x", padx=15, pady=(8, 2))

        self.lbl_company = ctk.CTkLabel(
            action_bar,
            text="",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=THEME["yellow"]
        )
        self.lbl_company.pack(side="left")

        btn_export = ctk.CTkButton(
            action_bar,
            text="💾 Xuất Markdown",
            width=120,
            height=28,
            fg_color=THEME["surface1"],
            hover_color=THEME["blue"],
            text_color=THEME["text"],
            command=self._export_markdown_file
        )
        btn_export.pack(side="right", padx=(6, 0))

        btn_copy = ctk.CTkButton(
            action_bar,
            text="📋 Copy Báo Cáo",
            width=115,
            height=28,
            fg_color=THEME["surface1"],
            hover_color=THEME["mauve"],
            text_color=THEME["text"],
            command=self._copy_markdown
        )
        btn_copy.pack(side="right")

        title_box = ctk.CTkFrame(self.dt_header, fg_color="transparent")
        title_box.pack(fill="x", padx=15, pady=(2, 6))

        self.dt_title = ctk.CTkLabel(
            title_box,
            text="Chọn một công việc bên trái để xem phân tích",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=THEME["blue"],
            wraplength=820,
            justify="left",
            anchor="w"
        )
        self.dt_title.pack(fill="x", anchor="w")

        self.badges_frame = ctk.CTkFrame(self.dt_header, fg_color="transparent")
        self.badges_frame.pack(fill="x", padx=15, pady=(0, 10))

        self.badge_level = self._create_badge(self.badges_frame, "Level: -", THEME["peach"])
        self.badge_cat = self._create_badge(self.badges_frame, "Ngành: -", THEME["blue"])
        self.badge_loc = self._create_badge(self.badges_frame, "Địa điểm: -", THEME["subtext"])
        self.badge_salary = self._create_badge(self.badges_frame, "Lương: -", THEME["green"])
        self.badge_offline = self._create_badge(self.badges_frame, "🟢 100% Offline", THEME["green"])

        status_box = ctk.CTkFrame(self.badges_frame, fg_color="transparent")
        status_box.pack(side="left", padx=(10, 0))
        ctk.CTkLabel(status_box, text="Trạng thái:", font=ctk.CTkFont(size=11), text_color=THEME["subtext"]).pack(side="left", padx=(0, 4))
        self.cb_status = ctk.CTkComboBox(
            status_box,
            values=["New", "Learning", "Ready", "Applied"],
            width=98,
            height=24,
            command=self._on_status_change
        )
        self.cb_status.pack(side="left")

        # 2. Tabview 8 Tầng Kiến Thức, Dòng Chảy Nhà Máy & Giáo Trình A–Z (Lazy Tab Rendering)
        self.tabview = ctk.CTkTabview(
            self.detail_frame,
            fg_color=THEME["surface0"],
            segmented_button_fg_color=THEME["crust"],
            segmented_button_selected_color=THEME["blue"],
            segmented_button_selected_hover_color="#74c7ec",
            segmented_button_unselected_color=THEME["surface0"],
            segmented_button_unselected_hover_color=THEME["surface1"],
            corner_radius=10,
            command=self._on_tab_change
        )
        self.tabview.pack(fill="both", expand=True)

        self.TAB_MAP = {
            "📋 Tổng Quan": "overview",
            "🏭 Dòng Chảy CADIVI": "factory_flow",
            "🎓 Giáo Trình A–Z": "curriculum",
            "🛠️ Kỹ Năng": "skills",
            "🧭 Lộ Trình": "roadmap",
            "📚 Tài Liệu": "resources",
            "❓ Phỏng Vấn": "interview",
            "📝 Ghi Chú & JD": "notes",
        }

        self.tab_overview = self.tabview.add("📋 Tổng Quan")
        self.tab_factory_flow = self.tabview.add("🏭 Dòng Chảy CADIVI")
        self.tab_curriculum = self.tabview.add("🎓 Giáo Trình A–Z")
        self.tab_skills = self.tabview.add("🛠️ Kỹ Năng")
        self.tab_roadmap = self.tabview.add("🧭 Lộ Trình")
        self.tab_resources = self.tabview.add("📚 Tài Liệu")
        self.tab_interview = self.tabview.add("❓ Phỏng Vấn")
        self.tab_notes = self.tabview.add("📝 Ghi Chú & JD")

        self._build_tab_overview()
        self._build_tab_factory_flow()
        self._build_tab_curriculum()
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
        lbl.pack(side="left", padx=3)
        return lbl

    # =====================================================================
    # BUILD CÁC TAB CHI TIẾT (C-ENGINE ZERO-LAG + CLICKABLE GLOSSARY)
    # =====================================================================
    def _build_tab_overview(self):
        wrap, self.txt_overview = create_c_engine_text(self.tab_overview, bg=THEME["crust"], font=("Segoe UI", 12))
        wrap.pack(fill="both", expand=True, padx=10, pady=10)
        bind_glossary_links(self.txt_overview, self.open_term_popup)

    def _build_tab_factory_flow(self):
        """Tab Lưu Trình Dòng Chảy Vận Hành Nhà Máy CADIVI (10 Trạm, 6 Luồng SP, 40 Tình Huống OE)."""
        top_ctrl = ctk.CTkFrame(self.tab_factory_flow, fg_color=THEME["mantle"], corner_radius=8)
        top_ctrl.pack(fill="x", padx=8, pady=(8, 6), ipady=4)

        self.seg_flow_mode = ctk.CTkSegmentedButton(
            top_ctrl,
            values=["🗺️ 10 Trạm End-to-End", "🔀 6 Luồng Sản Phẩm", "🚨 40 Tình Huống OE"],
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color=THEME["crust"],
            selected_color=THEME["blue"],
            selected_hover_color="#74c7ec",
            unselected_color=THEME["surface0"],
            unselected_hover_color=THEME["surface1"],
            text_color=THEME["text"],
            command=self._on_flow_mode_change
        )
        self.seg_flow_mode.set("🗺️ 10 Trạm End-to-End")
        self.seg_flow_mode.pack(side="left", padx=10, pady=4)

        self.lbl_flow_progress = ctk.CTkLabel(
            top_ctrl,
            text="✅ Đã nắm: 0 / 56 mục (0.0%)  •  💾 SQLite",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=THEME["green"]
        )
        self.lbl_flow_progress.pack(side="right", padx=12, pady=4)

        main = ctk.CTkFrame(self.tab_factory_flow, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        # Cột trái: Bộ lọc (cho chế độ 40 Tình huống) + C-Engine tk.Listbox
        left = ctk.CTkFrame(main, fg_color=THEME["mantle"], width=345, corner_radius=8)
        left.pack(side="left", fill="y", padx=(0, 10))
        left.pack_propagate(False)

        self.lbl_flow_left_hdr = ctk.CTkLabel(
            left,
            text="🏭 DÒNG CHẢY 10 TRẠM CADIVI",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=THEME["cyan"]
        )
        self.lbl_flow_left_hdr.pack(anchor="w", padx=10, pady=(10, 4))

        # Khung lọc riêng cho chế độ 40 Tình huống (ẩn gọn ở 2 chế độ kia)
        self.flow_filter_frame = ctk.CTkFrame(left, fg_color="transparent")

        self.ent_flow_search = ctk.CTkEntry(
            self.flow_filter_frame,
            placeholder_text="🔍 Tìm tình huống, máy, lỗi (VD: Sharkskin, Sauna)...",
            height=30,
            fg_color=THEME["crust"],
            border_color=THEME["surface0"],
            text_color=THEME["text"]
        )
        self.ent_flow_search.pack(fill="x", padx=10, pady=(0, 5))
        self.ent_flow_search.bind("<KeyRelease>", lambda _e: self._refresh_flow_list())

        sc_groups = cadivi_factory_flows.get_scenario_groups() if cadivi_factory_flows else ["Tất cả 8 nhóm tình huống"]
        self.cb_flow_group = ctk.CTkComboBox(
            self.flow_filter_frame,
            values=sc_groups,
            height=28,
            fg_color=THEME["crust"],
            border_color=THEME["surface0"],
            button_color=THEME["surface1"],
            text_color=THEME["text"],
            command=lambda _v: self._refresh_flow_list()
        )
        self.cb_flow_group.set("Tất cả 8 nhóm tình huống")
        self.cb_flow_group.pack(fill="x", padx=10, pady=(0, 5))

        st_opts = ["Tất cả 10 trạm"]
        self._flow_station_map = {"Tất cả 10 trạm": "ALL"}
        if cadivi_factory_flows:
            for st in cadivi_factory_flows.get_stations():
                lbl = f"{st['id']} ({st['code']}): {st['title'][:26]}"
                st_opts.append(lbl)
                self._flow_station_map[lbl] = st["id"]
        self.cb_flow_station = ctk.CTkComboBox(
            self.flow_filter_frame,
            values=st_opts,
            height=28,
            fg_color=THEME["crust"],
            border_color=THEME["surface0"],
            button_color=THEME["surface1"],
            text_color=THEME["text"],
            command=lambda _v: self._refresh_flow_list()
        )
        self.cb_flow_station.set("Tất cả 10 trạm")
        self.cb_flow_station.pack(fill="x", padx=10, pady=(0, 4))

        self.lbl_flow_list_cnt = ctk.CTkLabel(
            left, text="", font=ctk.CTkFont(size=11), text_color=THEME["subtext"]
        )
        self.lbl_flow_list_cnt.pack(anchor="w", padx=10, pady=(0, 4))

        lb_wrap = ctk.CTkFrame(left, fg_color=THEME["crust"], corner_radius=6)
        lb_wrap.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        sb = ttk.Scrollbar(lb_wrap, orient="vertical")
        self.lb_flow = tk.Listbox(
            lb_wrap,
            bg=THEME["crust"],
            fg=THEME["text"],
            selectbackground=THEME["blue"],
            selectforeground=THEME["crust"],
            activestyle="none",
            font=("Segoe UI", 10),
            highlightthickness=0,
            borderwidth=0,
            yscrollcommand=sb.set
        )
        sb.configure(command=self.lb_flow.yview)
        sb.pack(side="right", fill="y")
        self.lb_flow.pack(side="left", fill="both", expand=True, padx=4, pady=4)
        self.lb_flow.bind("<<ListboxSelect>>", self._on_flow_select)
        self.lb_flow.bind("<Return>", self._on_flow_select)

        # Cột phải: Header thông tin + Nút hành động + C-Engine tk.Text
        right = ctk.CTkFrame(main, fg_color="transparent")
        right.pack(side="right", fill="both", expand=True)

        hdr = ctk.CTkFrame(right, fg_color=THEME["crust"], corner_radius=8, border_width=1, border_color=THEME["surface1"])
        hdr.pack(fill="x", pady=(0, 8), ipady=5)

        meta_row = ctk.CTkFrame(hdr, fg_color="transparent")
        meta_row.pack(fill="x", padx=12, pady=(4, 2))

        self.lbl_flow_badge = ctk.CTkLabel(
            meta_row, text="🏭 LƯU TRÌNH DÒNG CHẢY NHÀ MÁY CADIVI MIỀN TRUNG",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=THEME["green"]
        )
        self.lbl_flow_badge.pack(side="left")

        self.lbl_flow_extra = ctk.CTkLabel(
            meta_row, text="",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=THEME["yellow"]
        )
        self.lbl_flow_extra.pack(side="right")

        self.lbl_flow_title = ctk.CTkLabel(
            hdr, text="Chọn một Trạm, Luồng sản phẩm hoặc Tình huống bên trái",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=THEME["cyan"],
            wraplength=700, justify="left", anchor="w"
        )
        self.lbl_flow_title.pack(fill="x", padx=12, pady=(0, 6))

        act_row = ctk.CTkFrame(hdr, fg_color="transparent")
        act_row.pack(fill="x", padx=12, pady=(0, 4))

        self.btn_flow_done = ctk.CTkButton(
            act_row, text="☐ Đánh dấu đã nắm", width=150, height=28,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["surface0"], hover_color=THEME["green"],
            text_color=THEME["text"], command=self._toggle_current_flow_done
        )
        self.btn_flow_done.pack(side="left", padx=(0, 5))

        self.btn_flow_prev = ctk.CTkButton(
            act_row, text="⬅ Trước", width=76, height=28,
            fg_color=THEME["surface0"], hover_color=THEME["blue"],
            text_color=THEME["text"], command=lambda: self._step_flow_item(-1)
        )
        self.btn_flow_prev.pack(side="left", padx=(0, 4))

        self.btn_flow_next = ctk.CTkButton(
            act_row, text="Tiếp ➡", width=76, height=28,
            fg_color=THEME["blue"], hover_color="#74c7ec",
            text_color=THEME["crust"], font=ctk.CTkFont(size=11, weight="bold"),
            command=lambda: self._step_flow_item(1)
        )
        self.btn_flow_next.pack(side="left", padx=(0, 6))

        self.btn_flow_related_sc = ctk.CTkButton(
            act_row, text="🚨 Tình huống trạm này", width=150, height=28,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["peach"], hover_color=THEME["yellow"],
            text_color=THEME["crust"], command=self._jump_to_station_scenarios
        )
        self.btn_flow_related_sc.pack(side="left", padx=(0, 6))

        self.btn_flow_doc = ctk.CTkButton(
            act_row, text="📖 Cẩm Nang", width=102, height=28,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["green"], hover_color="#74c7ec",
            text_color=THEME["crust"], command=self._open_flow_doc
        )
        self.btn_flow_doc.pack(side="right")

        self.btn_flow_lesson = ctk.CTkButton(
            act_row, text="🎓 Bài Học", width=100, height=28,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["mauve"], hover_color=THEME["blue"],
            text_color=THEME["crust"], command=self._open_flow_lesson
        )
        self.btn_flow_lesson.pack(side="right", padx=(0, 5))

        wrap, self.txt_flow = create_c_engine_text(right, bg=THEME["crust"], font=("Segoe UI", 11))
        wrap.pack(fill="both", expand=True)
        bind_glossary_links(self.txt_flow, self.open_term_popup)

    def _build_tab_curriculum(self):
        """Tab Giáo Trình OE CADIVI Từ A–Z (8 Học Phần / 32 Bài Học Tuần Tự + Lưu Tiến Độ SQLite)."""
        main = ctk.CTkFrame(self.tab_curriculum, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=8, pady=8)

        # Cột trái: Bộ lọc Học phần + Tiến độ + C-Engine tk.Listbox 32 bài học
        left = ctk.CTkFrame(main, fg_color=THEME["mantle"], width=335, corner_radius=8)
        left.pack(side="left", fill="y", padx=(0, 10))
        left.pack_propagate(False)

        ctk.CTkLabel(
            left,
            text="🎓 GIÁO TRÌNH HỌC TỪ ĐẦU (A–Z)",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=THEME["cyan"]
        ).pack(anchor="w", padx=10, pady=(10, 2))

        self.lbl_curr_progress = ctk.CTkLabel(
            left,
            text="📊 Tiến độ: 0 / 32 bài (0.0%)  •  💾 SQLite",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=THEME["green"]
        )
        self.lbl_curr_progress.pack(anchor="w", padx=10, pady=(0, 6))

        mod_vals = ["Tất cả 8 Học Phần (32 bài)"]
        self._curr_mod_map = {"Tất cả 8 Học Phần (32 bài)": "ALL"}
        if oe_curriculum:
            for m in oe_curriculum.get_all_modules():
                short_t = m["title"].split(": ", 1)[-1]
                lbl = f"{m['id']}: {short_t}"
                mod_vals.append(lbl)
                self._curr_mod_map[lbl] = m["id"]

        self.cb_curr_module = ctk.CTkComboBox(
            left,
            values=mod_vals,
            height=30,
            fg_color=THEME["crust"],
            border_color=THEME["surface0"],
            button_color=THEME["surface1"],
            text_color=THEME["text"],
            command=lambda _v: self._refresh_curriculum_list()
        )
        self.cb_curr_module.set("Tất cả 8 Học Phần (32 bài)")
        self.cb_curr_module.pack(fill="x", padx=10, pady=(0, 8))

        lb_wrap = ctk.CTkFrame(left, fg_color=THEME["crust"], corner_radius=6)
        lb_wrap.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        sb = ttk.Scrollbar(lb_wrap, orient="vertical")
        self.lb_curriculum = tk.Listbox(
            lb_wrap,
            bg=THEME["crust"],
            fg=THEME["text"],
            selectbackground=THEME["blue"],
            selectforeground=THEME["crust"],
            activestyle="none",
            font=("Segoe UI", 10),
            highlightthickness=0,
            borderwidth=0,
            yscrollcommand=sb.set
        )
        sb.configure(command=self.lb_curriculum.yview)
        sb.pack(side="right", fill="y")
        self.lb_curriculum.pack(side="left", fill="both", expand=True, padx=4, pady=4)
        self.lb_curriculum.bind("<<ListboxSelect>>", self._on_curriculum_select)
        self.lb_curriculum.bind("<Return>", self._on_curriculum_select)

        # Cột phải: Nội dung chi tiết từng bài học + thanh điều hướng & hành động
        right = ctk.CTkFrame(main, fg_color="transparent")
        right.pack(side="right", fill="both", expand=True)

        hdr = ctk.CTkFrame(right, fg_color=THEME["crust"], corner_radius=8, border_width=1, border_color=THEME["surface1"])
        hdr.pack(fill="x", pady=(0, 8), ipady=5)

        meta_row = ctk.CTkFrame(hdr, fg_color="transparent")
        meta_row.pack(fill="x", padx=12, pady=(4, 2))

        self.lbl_les_module = ctk.CTkLabel(
            meta_row, text="📚 Chọn một bài học bên trái để bắt đầu",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=THEME["green"]
        )
        self.lbl_les_module.pack(side="left")

        self.lbl_les_meta = ctk.CTkLabel(
            meta_row, text="",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=THEME["yellow"]
        )
        self.lbl_les_meta.pack(side="right")

        self.lbl_les_title = ctk.CTkLabel(
            hdr, text="Giáo Trình Tự Học OE CADIVI Từ Số 0 Đến Chuyên Gia (32 Bài)",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=THEME["cyan"],
            wraplength=700, justify="left", anchor="w"
        )
        self.lbl_les_title.pack(fill="x", padx=12, pady=(0, 6))

        act_row = ctk.CTkFrame(hdr, fg_color="transparent")
        act_row.pack(fill="x", padx=12, pady=(0, 4))

        self.btn_les_done = ctk.CTkButton(
            act_row, text="☐ Đánh dấu đã học xong", width=165, height=28,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["surface0"], hover_color=THEME["green"],
            text_color=THEME["text"], command=self._toggle_current_lesson_done
        )
        self.btn_les_done.pack(side="left", padx=(0, 6))

        self.btn_les_prev = ctk.CTkButton(
            act_row, text="⬅ Bài trước", width=88, height=28,
            fg_color=THEME["surface0"], hover_color=THEME["blue"],
            text_color=THEME["text"], command=lambda: self._step_curriculum_lesson(-1)
        )
        self.btn_les_prev.pack(side="left", padx=(0, 4))

        self.btn_les_next = ctk.CTkButton(
            act_row, text="Bài tiếp ➡", width=88, height=28,
            fg_color=THEME["blue"], hover_color="#74c7ec",
            text_color=THEME["crust"], font=ctk.CTkFont(size=11, weight="bold"),
            command=lambda: self._step_curriculum_lesson(1)
        )
        self.btn_les_next.pack(side="left", padx=(0, 8))

        self.btn_les_iv = ctk.CTkButton(
            act_row, text="❓ Luyện Câu Hỏi", width=120, height=28,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["mauve"], hover_color=THEME["blue"],
            text_color=THEME["crust"], command=self._open_lesson_interview
        )
        self.btn_les_iv.pack(side="right")

        self.btn_les_doc = ctk.CTkButton(
            act_row, text="📖 Cẩm Nang Sâu", width=124, height=28,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["green"], hover_color="#74c7ec",
            text_color=THEME["crust"], command=self._open_lesson_doc
        )
        self.btn_les_doc.pack(side="right", padx=(0, 6))

        wrap, self.txt_curriculum = create_c_engine_text(right, bg=THEME["crust"], font=("Segoe UI", 11))
        wrap.pack(fill="both", expand=True)
        bind_glossary_links(self.txt_curriculum, self.open_term_popup)

    def _build_tab_skills(self):
        wrap, self.txt_skills = create_c_engine_text(self.tab_skills, bg=THEME["crust"], font=("Segoe UI", 11))
        wrap.pack(fill="both", expand=True, padx=10, pady=10)
        bind_glossary_links(self.txt_skills, self.open_term_popup)

    def _build_tab_roadmap(self):
        wrap, self.txt_roadmap = create_c_engine_text(self.tab_roadmap, bg=THEME["crust"], font=("Segoe UI", 11))
        wrap.pack(fill="both", expand=True, padx=10, pady=10)
        bind_glossary_links(self.txt_roadmap, self.open_term_popup)
        # Bật/tắt checkbox trực tiếp trên C-engine tk.Text
        self.txt_roadmap.tag_bind("chk_click", "<Enter>", lambda e: self.txt_roadmap.configure(cursor="hand2"))
        self.txt_roadmap.tag_bind("chk_click", "<Leave>", lambda e: self.txt_roadmap.configure(cursor="arrow"))
        self.txt_roadmap.tag_bind("chk_click", "<ButtonRelease-1>", self._on_roadmap_checkbox_click)

    def _build_tab_resources(self):
        self.scroll_resources = ctk.CTkScrollableFrame(self.tab_resources, fg_color="transparent")
        self.scroll_resources.pack(fill="both", expand=True, padx=10, pady=10)

    def _build_tab_interview(self):
        self.ctrl_interview = ctk.CTkFrame(self.tab_interview, fg_color=THEME["crust"], corner_radius=8)
        self.ctrl_interview.pack(fill="x", padx=10, pady=(10, 4), ipady=4)

        self.ent_interview_search = ctk.CTkEntry(
            self.ctrl_interview,
            placeholder_text="🔍 Tìm câu hỏi, máy móc, tình huống (60fps)...",
            width=240,
            height=30,
            fg_color=THEME["surface0"],
            border_color=THEME["surface1"],
            text_color=THEME["text"]
        )
        self.ent_interview_search.pack(side="left", padx=(10, 6), pady=4)
        self.ent_interview_search.bind("<KeyRelease>", lambda e: self._debounce_interview_search())

        cats = interview_bank.get_categories() if interview_bank else ["Tất cả chủ đề"]
        self.cbo_interview_cat = ctk.CTkComboBox(
            self.ctrl_interview,
            values=cats,
            width=235,
            height=30,
            fg_color=THEME["surface0"],
            button_color=THEME["surface1"],
            text_color=THEME["text"],
            command=lambda v: self._update_interview_display()
        )
        self.cbo_interview_cat.pack(side="left", padx=4, pady=4)

        self.cbo_interview_status = ctk.CTkComboBox(
            self.ctrl_interview,
            values=["Tất cả trạng thái", "Chưa thuộc", "🔁 Cần ôn lại", "✅ Đã thuộc"],
            width=145,
            height=30,
            fg_color=THEME["surface0"],
            button_color=THEME["surface1"],
            text_color=THEME["text"],
            command=lambda v: self._update_interview_display()
        )
        self.cbo_interview_status.set("Tất cả trạng thái")
        self.cbo_interview_status.pack(side="left", padx=4, pady=4)

        self.lbl_interview_count = ctk.CTkLabel(
            self.ctrl_interview,
            text="Hiển thị: 0 / 0 câu",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=THEME["blue"]
        )
        self.lbl_interview_count.pack(side="right", padx=10, pady=4)

        # Hàng 2: Chế độ Luyện Phỏng Vấn Chủ Động (Active Recall — Ẩn đáp án & Lưu SQLite)
        self.ctrl_quiz = ctk.CTkFrame(self.tab_interview, fg_color=THEME["mantle"], corner_radius=8)
        self.ctrl_quiz.pack(fill="x", padx=10, pady=(0, 6), ipady=3)

        self.var_quiz_mode = tk.BooleanVar(value=False)
        self.sw_quiz_mode = ctk.CTkSwitch(
            self.ctrl_quiz,
            text="🎯 Chế độ Luyện Phỏng Vấn (Ẩn đáp án)",
            variable=self.var_quiz_mode,
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=THEME["yellow"],
            progress_color=THEME["green"],
            command=self._toggle_quiz_mode
        )
        self.sw_quiz_mode.pack(side="left", padx=(12, 10), pady=4)

        self.btn_reveal_all = ctk.CTkButton(
            self.ctrl_quiz,
            text="👁️ Mở/Ẩn hết đáp án",
            width=135,
            height=26,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["surface0"],
            hover_color=THEME["blue"],
            text_color=THEME["text"],
            command=self._toggle_reveal_all
        )
        self.btn_reveal_all.pack(side="left", padx=4, pady=4)

        self.btn_mock_interview = ctk.CTkButton(
            self.ctrl_quiz,
            text="🎤 Phỏng Vấn Thử 30p",
            width=150,
            height=26,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=THEME["mauve"],
            hover_color=THEME["blue"],
            text_color=THEME["crust"],
            command=self._open_mock_interview
        )
        self.btn_mock_interview.pack(side="left", padx=4, pady=4)

        self.lbl_readiness = ctk.CTkLabel(
            self.ctrl_quiz,
            text="🏆 Sẵn sàng: 0 / 0 (0.0%)  •  💾 Tự động lưu SQLite",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=THEME["green"]
        )
        self.lbl_readiness.pack(side="right", padx=12, pady=4)

        # Thay thế hàng trăm widget CTk Canvas bằng 1 C-Engine tk.Text siêu tốc + Clickable Glossary + Quiz Action!
        wrap, self.txt_interview = create_c_engine_text(self.tab_interview, bg=THEME["crust"], font=("Segoe UI", 11))
        wrap.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        bind_glossary_links(self.txt_interview, self.open_term_popup)
        self.txt_interview.tag_bind("iv_action", "<Enter>", lambda e: self.txt_interview.configure(cursor="hand2"))
        self.txt_interview.tag_bind("iv_action", "<Leave>", lambda e: self.txt_interview.configure(cursor="arrow"))
        self.txt_interview.tag_bind("iv_action", "<ButtonRelease-1>", self._on_interview_action_click)

    def _build_tab_notes(self):
        container = ctk.CTkFrame(self.tab_notes, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=10, pady=10)

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

        right_box = ctk.CTkFrame(container, fg_color=THEME["crust"], corner_radius=8)
        right_box.pack(side="right", fill="both", expand=True, padx=(6, 0), pady=0)

        ctk.CTkLabel(
            right_box,
            text="📄 Văn Bản JD Gốc (💡 Bấm từ xanh để tra định nghĩa):",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=THEME["cyan"]
        ).pack(anchor="w", padx=10, pady=8)

        raw_wrap, self.txt_raw_jd = create_c_engine_text(right_box, bg=THEME["base"], font=("Consolas", 11), padx=10, pady=8)
        raw_wrap.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        bind_glossary_links(self.txt_raw_jd, self.open_term_popup)

    # =====================================================================
    # TRA CỨU THUẬT NGỮ TOÀN CỤC (CLICK-ANYWHERE HANDLER) & GIÁO TRÌNH A–Z
    # =====================================================================
    def open_term_popup(self, term_key):
        """Mở cửa sổ định nghĩa & ví dụ CADIVI cho thuật ngữ bất kỳ trong < 15ms."""
        if not term_glossary:
            return
        if self._term_popup is not None and self._term_popup.winfo_exists():
            self._term_popup.show_term(term_key, push_history=True)
            self._term_popup.lift()
            return self._term_popup
        self._term_popup = TermDetailPopup(
            self,
            term_key,
            open_doc_callback=self._open_offline_doc,
            open_lesson_callback=self.open_curriculum_lesson,
        )
        return self._term_popup

    def _open_glossary_browser(self):
        if self._glossary_dialog is not None and self._glossary_dialog.winfo_exists():
            self._glossary_dialog.lift()
            return self._glossary_dialog
        self._glossary_dialog = GlossaryBrowserDialog(
            self,
            open_doc_callback=self._open_offline_doc,
            open_lesson_callback=self.open_curriculum_lesson,
        )
        return self._glossary_dialog

    def _open_oe_calculators(self):
        """Mở cửa sổ 5 công cụ tính nhanh thực chiến OE & Giải mã mã cáp CADIVI."""
        if not oe_calculators:
            messagebox.showinfo("Công Cụ OE", "Module oe_calculators chưa sẵn sàng.", parent=self)
            return None
        if self._calc_dialog is not None and self._calc_dialog.winfo_exists():
            self._calc_dialog.lift()
            return self._calc_dialog
        self._calc_dialog = oe_calculators.OECalculatorDialog(self, THEME)
        return self._calc_dialog

    def _open_mock_interview(self):
        """Mở cửa sổ Phỏng vấn thử 30 phút (10 câu chuẩn cấu trúc + đồng hồ + chấm điểm /100)."""
        if not oe_calculators:
            messagebox.showinfo("Phỏng Vấn Thử", "Module oe_calculators chưa sẵn sàng.", parent=self)
            return None
        if self._mock_dialog is not None and self._mock_dialog.winfo_exists():
            self._mock_dialog.lift()
            return self._mock_dialog
        job_qs = []
        if self.current_job:
            job_qs = self.current_job.get("analysis", {}).get("interview_prep", []) or []
        if len(job_qs) >= 10:
            qs = job_qs
        elif len(getattr(self, "_current_interview_raw", []) or []) >= 10:
            qs = self._current_interview_raw
        else:
            qs = interview_bank.get_all_questions() if interview_bank else job_qs
        self._mock_dialog = oe_calculators.MockInterviewDialog(
            self, THEME, qs, on_term_click=self.open_term_popup
        )
        return self._mock_dialog

    def open_curriculum_lesson(self, lesson_id):
        """Nhảy thẳng từ Popup thuật ngữ hoặc nút bất kỳ sang đúng bài học trong Tab Giáo Trình A–Z."""
        if not oe_curriculum or not lesson_id:
            return
        self.tabview.set("🎓 Giáo Trình A–Z")
        self._dirty_tabs.discard("curriculum")
        if hasattr(self, "cb_curr_module"):
            self.cb_curr_module.set("Tất cả 8 Học Phần (32 bài)")
        self._refresh_curriculum_list(select_lesson_id=lesson_id)
        self.lift()

    def _render_curriculum_tab(self):
        self._refresh_curriculum_list(select_lesson_id=self._current_lesson_id)

    def _update_curriculum_progress_label(self):
        if not hasattr(self, "lbl_curr_progress") or not oe_curriculum:
            return
        total = len(oe_curriculum.get_all_lessons())
        done = sum(1 for l in oe_curriculum.get_all_lessons() if self._curriculum_done.get(l["id"], False))
        pct = (done / total * 100.0) if total else 0.0
        self.lbl_curr_progress.configure(text=f"📊 Tiến độ: {done} / {total} bài ({pct:.1f}%)  •  💾 SQLite")

    def _refresh_curriculum_list(self, select_lesson_id=None):
        if not oe_curriculum or not hasattr(self, "lb_curriculum"):
            return
        mod_label = self.cb_curr_module.get() if hasattr(self, "cb_curr_module") else "Tất cả 8 Học Phần (32 bài)"
        mod_id = self._curr_mod_map.get(mod_label, "ALL")
        self._curriculum_lessons_view = oe_curriculum.get_lessons_by_module(mod_id)

        self.lb_curriculum.delete(0, "end")
        target_idx = 0
        for idx, les in enumerate(self._curriculum_lessons_view):
            lid = les["id"]
            done = bool(self._curriculum_done.get(lid, False))
            mark = "☑" if done else "☐"
            short_title = les["title"].split(": ", 1)[-1]
            self.lb_curriculum.insert("end", f"  {mark} {lid} — {short_title[:36]}")
            if done:
                self.lb_curriculum.itemconfig(idx, fg=THEME["green"])
            if select_lesson_id and lid.upper() == select_lesson_id.upper():
                target_idx = idx

        self._update_curriculum_progress_label()
        if self._curriculum_lessons_view:
            self.lb_curriculum.selection_clear(0, "end")
            self.lb_curriculum.selection_set(target_idx)
            self.lb_curriculum.see(target_idx)
            self._render_lesson_detail(self._curriculum_lessons_view[target_idx])

    def _on_curriculum_select(self, _event=None):
        sel = self.lb_curriculum.curselection()
        if not sel:
            return
        idx = sel[0]
        if 0 <= idx < len(self._curriculum_lessons_view):
            self._render_lesson_detail(self._curriculum_lessons_view[idx])

    def _render_lesson_detail(self, lesson):
        if not lesson or not oe_curriculum:
            return
        lid = lesson["id"]
        self._current_lesson_id = lid

        mod_obj = next((m for m in oe_curriculum.get_all_modules() if m["id"] == lesson["module_id"]), None)
        mod_title = mod_obj["title"] if mod_obj else lesson["module_id"]
        self.lbl_les_module.configure(text=f"📚 {mod_title}")
        self.lbl_les_meta.configure(text=f"⏱️ {lesson.get('duration', '45 phút')}   •   📌 Yêu cầu: {lesson.get('prereq', 'Không')}")
        self.lbl_les_title.configure(text=lesson["title"])

        is_done = bool(self._curriculum_done.get(lid, False))
        if is_done:
            self.btn_les_done.configure(text="☑ Đã hoàn thành bài này", fg_color=THEME["green"], text_color=THEME["crust"])
        else:
            self.btn_les_done.configure(text="☐ Đánh dấu đã học xong", fg_color=THEME["surface0"], text_color=THEME["text"])

        all_lessons = oe_curriculum.get_all_lessons()
        pos = next((i for i, x in enumerate(all_lessons) if x["id"] == lid), 0)
        self.btn_les_prev.configure(state="normal" if pos > 0 else "disabled")
        self.btn_les_next.configure(state="normal" if pos < len(all_lessons) - 1 else "disabled")
        self.btn_les_doc.configure(state="normal" if lesson.get("doc_key") else "disabled")
        self.btn_les_iv.configure(state="normal" if lesson.get("interview_category") else "disabled")

        tb = self.txt_curriculum
        tb.configure(state="normal")
        tb.delete("1.0", "end")

        tb.insert("end", "💡 Cách học hiệu quả: Đọc kỹ lý thuyết → Bấm vào bất kỳ thuật ngữ xanh gạch chân nào để mở bài giảng mini → Tự làm Bài tập & trả lời 3 câu Checkpoint rồi tích ☑ hoàn thành!\n", "subtext")
        tb.insert("end", "─" * 86 + "\n", "divider")

        # 1. Mục tiêu bài học
        tb.insert("end", "🎯 1. MỤC TIÊU BÀI HỌC (HỌC XONG BẠN SẼ LÀM ĐƯỢC GÌ?)\n", "sec_yellow")
        for obj in lesson.get("objectives", []):
            tb.insert("end", "  • ", "bullet")
            insert_with_glossary(tb, obj + "\n", "bullet")
        tb.insert("end", "\n", "normal")

        # 2. Kiến thức cốt lõi
        tb.insert("end", "📘 2. KIẾN THỨC CỐT LÕI (TỪ NỀN TẢNG ĐẾN THỰC CHIẾN CADIVI)\n", "sec_blue")
        for line in lesson.get("core_theory", "").splitlines():
            s = line.strip()
            if s.startswith("•") or s.startswith("- "):
                insert_with_glossary(tb, "  " + s + "\n", "bullet")
            else:
                insert_with_glossary(tb, line + "\n", "normal")
        tb.insert("end", "\n", "normal")

        # 3. Ví dụ số liệu giải chi tiết
        tb.insert("end", "💡 3. VÍ DỤ SỐ LIỆU GIẢI CHI TIẾT TẠI CADIVI\n", "sec_mauve")
        insert_with_glossary(tb, lesson.get("worked_example", "") + "\n\n", "ans_body")

        # 4. Bài tập thực hành
        tb.insert("end", "🛠️ 4. BÀI TẬP THỰC HÀNH (HANDS-ON DRILL)\n", "sec_peach")
        insert_with_glossary(tb, lesson.get("hands_on_drill", "") + "\n\n", "card_box")

        # 5. Checkpoint tự kiểm tra
        tb.insert("end", "✅ 5. CÂU HỎI TỰ KIỂM TRA NHANH (CHECKPOINT TRƯỚC KHI QUA BÀI TIẾP)\n", "sec_green")
        for idx, cp in enumerate(lesson.get("checkpoints", []), 1):
            tb.insert("end", f"  {idx}. ", "bold")
            insert_with_glossary(tb, cp + "\n", "normal")
        tb.insert("end", "\n", "normal")

        # 6. Từ khóa trọng tâm bấm mở nhanh
        key_terms = lesson.get("key_terms", [])
        if key_terms and term_glossary:
            tb.insert("end", "─" * 86 + "\n", "divider")
            tb.insert("end", "🔑 6. TỪ KHÓA TRỌNG TÂM BÀI NÀY (Bấm để mở định nghĩa sâu & ví dụ CADIVI):\n", "sec_yellow")
            for kt in key_terms:
                info = term_glossary.get_term(kt)
                if info:
                    tb.insert("end", f"  {info['term']}  ", ("related_pill", f"term::{info['term']}"))
                    tb.insert("end", "   ", "normal")
            tb.insert("end", "\n", "normal")

        tb.tag_raise("term_link")
        tb.tag_raise("term_link_bold")
        tb.tag_raise("related_pill")
        tb.tag_raise("sel")
        tb.see("1.0")
        tb.configure(state="disabled")

    def _toggle_current_lesson_done(self):
        if not self._current_lesson_id:
            return
        lid = self._current_lesson_id
        self._curriculum_done[lid] = not bool(self._curriculum_done.get(lid, False))
        self._current_progress["curriculum"] = dict(self._curriculum_done)
        if self.current_job:
            jid = self.current_job["id"]
            self.storage.save_progress(jid, self._current_progress)
            self.current_job["progress"] = dict(self._current_progress)
        self._refresh_curriculum_list(select_lesson_id=lid)

    def _step_curriculum_lesson(self, delta):
        if not oe_curriculum or not self._current_lesson_id:
            return
        all_lessons = oe_curriculum.get_all_lessons()
        pos = next((i for i, x in enumerate(all_lessons) if x["id"] == self._current_lesson_id), 0)
        new_pos = max(0, min(len(all_lessons) - 1, pos + delta))
        next_lid = all_lessons[new_pos]["id"]
        if hasattr(self, "cb_curr_module"):
            self.cb_curr_module.set("Tất cả 8 Học Phần (32 bài)")
        self._refresh_curriculum_list(select_lesson_id=next_lid)

    def _open_lesson_doc(self):
        if not oe_curriculum or not self._current_lesson_id:
            return
        les = oe_curriculum.get_lesson(self._current_lesson_id)
        if les and les.get("doc_key"):
            self._open_offline_doc(les["doc_key"])

    def _open_lesson_interview(self):
        if not oe_curriculum or not self._current_lesson_id:
            return
        les = oe_curriculum.get_lesson(self._current_lesson_id)
        if not les:
            return
        cat = les.get("interview_category", "")
        self.tabview.set("❓ Phỏng Vấn")
        self._dirty_tabs.discard("interview")
        if hasattr(self, "ent_interview_search"):
            self.ent_interview_search.delete(0, "end")
        if hasattr(self, "cbo_interview_cat"):
            vals = list(self.cbo_interview_cat.cget("values"))
            self.cbo_interview_cat.set(cat if cat in vals else "Tất cả chủ đề")
        self._update_interview_display()

    # =====================================================================
    # LOGIC TAB LƯU TRÌNH DÒNG CHẢY NHÀ MÁY CADIVI (10 TRẠM / 6 LUỒNG / 40 TÌNH HUỐNG)
    # =====================================================================
    def _render_factory_flow_tab(self):
        self._on_flow_mode_change(self.seg_flow_mode.get() if hasattr(self, "seg_flow_mode") else "🗺️ 10 Trạm End-to-End")

    def _on_flow_mode_change(self, mode):
        if not cadivi_factory_flows or not hasattr(self, "lb_flow"):
            return
        self._flow_mode = mode
        if mode == "🚨 40 Tình Huống OE":
            self.lbl_flow_left_hdr.configure(text="🚨 40 TÌNH HUỐNG THỰC CHIẾN OE")
            self.flow_filter_frame.pack(fill="x", before=self.lbl_flow_list_cnt)
        elif mode == "🔀 6 Luồng Sản Phẩm":
            self.lbl_flow_left_hdr.configure(text="🔀 6 LUỒNG SẢN PHẨM CADIVI")
            self.flow_filter_frame.pack_forget()
        else:
            self.lbl_flow_left_hdr.configure(text="🏭 DÒNG CHẢY 10 TRẠM CADIVI")
            self.flow_filter_frame.pack_forget()
        self._refresh_flow_list()

    def _update_flow_progress_label(self):
        if not hasattr(self, "lbl_flow_progress") or not cadivi_factory_flows:
            return
        all_ids = (
            [s["id"] for s in cadivi_factory_flows.get_stations()]
            + [f["id"] for f in cadivi_factory_flows.get_product_flows()]
            + [sc["id"] for sc in cadivi_factory_flows.get_scenarios()]
        )
        total = len(all_ids)
        done = sum(1 for k in all_ids if self._factory_flow_done.get(k, False))
        pct = (done / total * 100.0) if total else 0.0
        self.lbl_flow_progress.configure(text=f"✅ Đã nắm: {done} / {total} mục ({pct:.1f}%)  •  💾 SQLite")

    def _refresh_flow_list(self, select_id=None):
        if not cadivi_factory_flows or not hasattr(self, "lb_flow"):
            return
        mode = self.seg_flow_mode.get()
        items = []
        if mode == "🗺️ 10 Trạm End-to-End":
            items.append({"_kind": "master", "id": "MASTER", "label": "  🗺️ SƠ ĐỒ TỔNG THỂ 10 TRẠM CADIVI"})
            for st in cadivi_factory_flows.get_stations():
                done = bool(self._factory_flow_done.get(st["id"], False))
                mark = "☑" if done else "☐"
                items.append({
                    "_kind": "station",
                    "id": st["id"],
                    "data": st,
                    "done": done,
                    "label": f"  {mark} {st['code']}: {st['title'][:30]}",
                })
            self.lbl_flow_list_cnt.configure(text="Sơ đồ tổng thể + 10 Trạm (S00 → S09)")
        elif mode == "🔀 6 Luồng Sản Phẩm":
            for fl in cadivi_factory_flows.get_product_flows():
                done = bool(self._factory_flow_done.get(fl["id"], False))
                mark = "☑" if done else "☐"
                items.append({
                    "_kind": "flow",
                    "id": fl["id"],
                    "data": fl,
                    "done": done,
                    "label": f"  {mark} {fl['code']}: {fl['title'][:30]}",
                })
            self.lbl_flow_list_cnt.configure(text="6 Họ sản phẩm cốt lõi CADIVI")
        else:
            kw = self.ent_flow_search.get().strip() if hasattr(self, "ent_flow_search") else ""
            grp = self.cb_flow_group.get() if hasattr(self, "cb_flow_group") else "Tất cả 8 nhóm tình huống"
            st_lbl = self.cb_flow_station.get() if hasattr(self, "cb_flow_station") else "Tất cả 10 trạm"
            sid = self._flow_station_map.get(st_lbl, "ALL")
            matched = cadivi_factory_flows.search_scenarios(kw, grp, sid)
            for sc in matched:
                done = bool(self._factory_flow_done.get(sc["id"], False))
                mark = "☑" if done else "☐"
                items.append({
                    "_kind": "scenario",
                    "id": sc["id"],
                    "data": sc,
                    "done": done,
                    "label": f"  {mark} [{sc['id']}·{sc['station_id']}] {sc['title'][:28]}",
                })
            total_sc = len(cadivi_factory_flows.get_scenarios())
            self.lbl_flow_list_cnt.configure(text=f"Hiển thị: {len(matched)} / {total_sc} tình huống")

        self._flow_items_view = items
        self.lb_flow.delete(0, "end")
        target_idx = 0
        for idx, it in enumerate(items):
            self.lb_flow.insert("end", it["label"])
            if it.get("_kind") == "master":
                self.lb_flow.itemconfig(idx, fg=THEME["yellow"])
            elif it.get("done"):
                self.lb_flow.itemconfig(idx, fg=THEME["green"])
            if select_id and it["id"].upper() == select_id.upper():
                target_idx = idx

        self._update_flow_progress_label()
        if items:
            self.lb_flow.selection_clear(0, "end")
            self.lb_flow.selection_set(target_idx)
            self.lb_flow.see(target_idx)
            self._render_flow_detail(items[target_idx])
        else:
            self._current_flow_item = None
            self.lbl_flow_badge.configure(text="🔍 Không tìm thấy tình huống phù hợp")
            self.lbl_flow_extra.configure(text="")
            self.lbl_flow_title.configure(text="Thử xóa bớt bộ lọc hoặc nhập từ khóa khác")
            self.btn_flow_done.configure(state="disabled")
            self.btn_flow_doc.configure(state="disabled")
            self.btn_flow_lesson.configure(state="disabled")
            self.btn_flow_related_sc.pack_forget()
            tb = self.txt_flow
            tb.configure(state="normal")
            tb.delete("1.0", "end")
            tb.insert("end", "\n  🔍 Không có tình huống nào khớp với từ khóa/bộ lọc hiện tại.", "subtext")
            tb.configure(state="disabled")

    def _on_flow_select(self, _event=None):
        sel = self.lb_flow.curselection()
        if not sel:
            return
        idx = sel[0]
        if 0 <= idx < len(self._flow_items_view):
            self._render_flow_detail(self._flow_items_view[idx])

    def _render_flow_detail(self, item):
        if not item or not cadivi_factory_flows:
            return
        self._current_flow_item = item
        kind = item["_kind"]
        iid = item["id"]
        idx = next((i for i, x in enumerate(self._flow_items_view) if x["id"] == iid), 0)
        self.btn_flow_prev.configure(state="normal" if idx > 0 else "disabled")
        self.btn_flow_next.configure(state="normal" if idx < len(self._flow_items_view) - 1 else "disabled")

        tb = self.txt_flow
        tb.configure(state="normal")
        tb.delete("1.0", "end")

        if kind == "master":
            self.lbl_flow_badge.configure(text="🗺️ BẢN ĐỒ TỔNG THỂ DÒNG CHẢY NHÀ MÁY CADIVI MIỀN TRUNG")
            self.lbl_flow_extra.configure(text="10 Trạm · 6 Luồng SP · 40 Tình Huống OE")
            self.lbl_flow_title.configure(text="Dòng Chảy Vật Tư, Thông Tin, Chất Lượng & Chi Phí Khép Kín Từ Đầu Đến Cuối")
            self.btn_flow_done.configure(text="📋 Tổng quan dòng chảy", state="disabled", fg_color=THEME["surface0"], text_color=THEME["subtext"])
            self.btn_flow_doc.configure(state="normal")
            self.btn_flow_lesson.configure(state="normal")
            self.btn_flow_related_sc.pack_forget()

            tb.insert("end", "💡 Khác với kiến thức lý thuyết hay giáo trình học, tab này mô phỏng ĐÚNG DÒNG CHẢY THỰC TẾ trong nhà máy CADIVI: chọn từng Trạm bên trái (Trạm 00 → Trạm 09), chuyển sang '🔀 6 Luồng Sản Phẩm' để xem đường đi riêng từng dòng cáp, hoặc mở '🚨 40 Tình Huống OE' để xem kịch bản xử lý thực chiến!\n", "subtext")
            tb.insert("end", "─" * 88 + "\n", "divider")
            tb.insert("end", cadivi_factory_flows.get_master_map() + "\n\n", "mathbox")

            tb.insert("end", "🎯 4 DÒNG CHẢY CHUYÊN VIÊN OE PHẢI NHÌN THẤY XUYÊN SUỐT NHÀ MÁY CADIVI\n", "sec_yellow")
            overview_lines = [
                "1. **Dòng Thông Tin (Trạm 00):** [[S&OP]] → [[MPS]] → [[MRP]] → [[RCCP]] → [[CRP]] → Lệnh SX [[SAP PP]] / [[MES]]. Đứt gãy ở đây gây quá tải ảo, chen đơn phá màu và tồn kho lệch!",
                "2. **Dòng Vật Tư & Tạo Giá Trị (Trạm 01 → 08):** Đồng/Nhôm Rod → [[RBD]] / [[Multi-wire]] + [[Annealing]] → [[Buncher]] / [[Rigid Strander]] → Đùn [[PVC]]/[[XLPE]]/[[LSZH]]/[[CCV]] → [[Drum Twister]] / [[DSTA]] / [[Braiding]] → Đùn vỏ & In chữ → Lab → Đóng cuộn / [[Cut-Length]] giao hàng.",
                "3. **Dòng Chất Lượng & Dữ Liệu (IQC → Trực tuyến → Lab):** [[ASTM B49]] ([[IACS]], tỷ trọng [[CaCO3 Filler]]) → [[Laser Gauge]] + [[Spark Tester]] + [[SPC]] → [[Kelvin Bridge]], [[Water Immersion]], [[Hot Set Test]], [[Partial Discharge]] & [[QCVN 4]].",
                "4. **Dòng Chảy Ngược (Trạm 09 — Tiền Rơi Ở Đây!):** Thu hồi tách riêng phế đồng trần (~94%) vs đồng dính nhựa vs nhựa purge; bảo trì chủ động [[TPM]] / [[CBM / PdM]] / [[LOTO]]; quyết toán [[Standard Cost]] & [[Cost Deployment]] trình Ban Giám Đốc!",
            ]
            for ln in overview_lines:
                insert_with_glossary(tb, "  " + ln + "\n", "normal")
            tb.insert("end", "\n👉 Hãy bấm vào Trạm 00 bên trái (hoặc bấm nút Tiếp ➡) để đi lần lượt từng trạm từ đầu đến cuối nhà máy!\n", "sec_green")

        elif kind == "station":
            st = item["data"]
            sc_cnt = len(cadivi_factory_flows.search_scenarios(station_id=st["id"]))
            is_done = bool(self._factory_flow_done.get(iid, False))
            self.lbl_flow_badge.configure(text=f"🏭 {st['code'].upper()} ({st['id']})  •  {st['zone']}")
            self.lbl_flow_extra.configure(text=f"🚨 {sc_cnt} tình huống thực chiến tại trạm này")
            self.lbl_flow_title.configure(text=st["title"])
            self._set_flow_done_btn_state(is_done)
            self.btn_flow_doc.configure(state="normal" if st.get("doc_key") else "disabled")
            self.btn_flow_lesson.configure(state="normal" if st.get("lesson_id") else "disabled")
            if sc_cnt > 0:
                self.btn_flow_related_sc.configure(text=f"🚨 {sc_cnt} Tình huống trạm này")
                self.btn_flow_related_sc.pack(side="left", padx=(0, 6))
            else:
                self.btn_flow_related_sc.pack_forget()

            tb.insert("end", "📥 1. ĐẦU VÀO (INPUT — VẬT TƯ & THÔNG TIN)\n", "sec_blue")
            insert_with_glossary(tb, st["input"] + "\n\n", "card_box")

            tb.insert("end", "📤 2. ĐẦU RA (OUTPUT — BÀN GIAO SANG TRẠM KẾ TIẾP)\n", "sec_green")
            insert_with_glossary(tb, st["output"] + "\n\n", "card_box")

            tb.insert("end", "⚙️ 3. THIẾT BỊ, MÁY MÓC & PHÒNG BAN THAM GIA\n", "sec_yellow")
            insert_with_glossary(tb, st["machines_and_teams"] + "\n\n", "normal")

            tb.insert("end", "⚠️ 4. ĐIỂM NGHẼN & TỔN THẤT ẨN THƯỜNG GẶP TẠI TRẠM NÀY\n", "sec_red")
            for ln in st["hidden_losses"].splitlines():
                insert_with_glossary(tb, ln + "\n", "bullet" if ln.strip().startswith("•") else "normal")
            tb.insert("end", "\n", "normal")

            tb.insert("end", "🚀 5. CHUYÊN VIÊN OE LÀM ĐƯỢC GÌ TỪ ĐẦU ĐẾN CUỐI TẠI TRẠM NÀY?\n", "sec_mauve")
            for ln in st["oe_end_to_end_actions"].splitlines():
                insert_with_glossary(tb, ln + "\n", "ans_body")
            tb.insert("end", "\n", "normal")

            tb.insert("end", "📊 6. BỘ KPI MỤC TIÊU OE THEO DÕI TẠI CADIVI\n", "sec_peach")
            insert_with_glossary(tb, st["kpis"] + "\n\n", "card_box")

            self._insert_flow_key_terms(tb, st.get("key_terms", []))

        elif kind == "flow":
            fl = item["data"]
            is_done = bool(self._factory_flow_done.get(iid, False))
            self.lbl_flow_badge.configure(text=f"🔀 {fl['code'].upper()} ({fl['id']})  •  LƯU TRÌNH CÔNG NGHỆ ĐẶC THÙ")
            self.lbl_flow_extra.configure(text=f"📖 Cẩm nang: {fl.get('doc_key', '')}  •  🎓 {fl.get('lesson_id', '')}")
            self.lbl_flow_title.configure(text=fl["title"])
            self._set_flow_done_btn_state(is_done)
            self.btn_flow_doc.configure(state="normal" if fl.get("doc_key") else "disabled")
            self.btn_flow_lesson.configure(state="normal" if fl.get("lesson_id") else "disabled")
            self.btn_flow_related_sc.pack_forget()

            tb.insert("end", "📦 1. SẢN PHẨM ĐIỂN HÌNH TẠI NHÀ MÁY CADIVI\n", "sec_yellow")
            insert_with_glossary(tb, fl["product_examples"] + "\n\n", "card_box")

            tb.insert("end", "🗺️ 2. SƠ ĐỒ ĐƯỜNG ĐI CÔNG NGHỆ TỪ ĐẦU ĐẾN CUỐI\n", "sec_blue")
            for ln in fl["route_diagram"].splitlines():
                insert_with_glossary(tb, ln + "\n", "codeblock")
            tb.insert("end", "\n", "normal")

            tb.insert("end", "🔴 3. ĐIỂM NGHẼN CỔ CHAI ĐẶC TRƯNG CỦA DÒNG SẢN PHẨM NÀY\n", "sec_red")
            insert_with_glossary(tb, fl["bottleneck"] + "\n\n", "card_box")

            tb.insert("end", "💸 4. CÁC TỔN THẤT CHI PHÍ / CHẤT LƯỢNG LỚN NHẤT\n", "sec_peach")
            insert_with_glossary(tb, fl["biggest_losses"] + "\n\n", "normal")

            tb.insert("end", "🚀 5. CHIẾN LƯỢC HÀNH ĐỘNG TRỌNG ĐIỂM CỦA CHUYÊN VIÊN OE\n", "sec_green")
            for ln in fl["oe_strategy"].splitlines():
                insert_with_glossary(tb, ln + "\n", "ans_body")
            tb.insert("end", "\n", "normal")

            self._insert_flow_key_terms(tb, fl.get("key_terms", []))

        elif kind == "scenario":
            sc = item["data"]
            st_obj = cadivi_factory_flows.get_station(sc["station_id"])
            st_name = f"{st_obj['code']} — {st_obj['title'][:40]}" if st_obj else sc["station_id"]
            is_done = bool(self._factory_flow_done.get(iid, False))
            self.lbl_flow_badge.configure(text=f"🚨 {sc['id']}  •  {sc['group']}")
            self.lbl_flow_extra.configure(text=f"📍 {st_name}")
            self.lbl_flow_title.configure(text=sc["title"])
            self._set_flow_done_btn_state(is_done)
            self.btn_flow_doc.configure(state="normal" if sc.get("doc_key") else "disabled")
            self.btn_flow_lesson.configure(state="normal" if sc.get("lesson_id") else "disabled")
            self.btn_flow_related_sc.pack_forget()

            tb.insert("end", "🚨 1. DẤU HIỆU HIỆN TRƯỜNG (TRIGGER / SYMPTOM)\n", "sec_red")
            insert_with_glossary(tb, sc["symptom"] + "\n\n", "card_box")

            tb.insert("end", "💥 2. TÁC ĐỘNG THỰC TẾ ĐẾN DÒNG CHẢY & CHI PHÍ\n", "sec_peach")
            insert_with_glossary(tb, sc["impact"] + "\n\n", "normal")

            tb.insert("end", "⏱️ 3. HÀNH ĐỘNG KHOANH VÙNG NGAY TRONG 24 GIỜ (CONTAINMENT & GENBA)\n", "sec_yellow")
            insert_with_glossary(tb, sc["immediate_24h"] + "\n\n", "card_box")

            tb.insert("end", "🔍 4. TRUY TÌM NGUYÊN NHÂN GỐC (ROOT CAUSE ANALYSIS — RCA)\n", "sec_blue")
            for ln in sc["rca"].splitlines():
                insert_with_glossary(tb, ln + "\n", "normal")
            tb.insert("end", "\n", "normal")

            tb.insert("end", "🛠️ 5. GIẢI PHÁP XỬ LÝ CỦA OE & HIỆU QUẢ SỐ LIỆU THỰC TẾ\n", "sec_green")
            for ln in sc["oe_solution"].splitlines():
                insert_with_glossary(tb, ln + "\n", "ans_body")
            tb.insert("end", "\n", "normal")

            tb.insert("end", "🔒 6. KHÓA CHUẨN CHỐNG TÁI DIỄN (STANDARDIZE & CONTROL)\n", "sec_mauve")
            insert_with_glossary(tb, sc["lock_in"] + "\n\n", "card_box")

            self._insert_flow_key_terms(tb, sc.get("key_terms", []))

        tb.tag_raise("term_link")
        tb.tag_raise("term_link_bold")
        tb.tag_raise("related_pill")
        tb.tag_raise("sel")
        tb.see("1.0")
        tb.configure(state="disabled")

    def _set_flow_done_btn_state(self, is_done):
        if is_done:
            self.btn_flow_done.configure(text="☑ Đã nắm vững", state="normal", fg_color=THEME["green"], text_color=THEME["crust"])
        else:
            self.btn_flow_done.configure(text="☐ Đánh dấu đã nắm", state="normal", fg_color=THEME["surface0"], text_color=THEME["text"])

    def _insert_flow_key_terms(self, tb, key_terms):
        if key_terms and term_glossary:
            tb.insert("end", "─" * 86 + "\n", "divider")
            tb.insert("end", "🔑 TỪ KHÓA TRỌNG TÂM (Bấm để mở định nghĩa sâu & ví dụ CADIVI):\n", "sec_yellow")
            for kt in key_terms:
                info = term_glossary.get_term(kt)
                if info:
                    tb.insert("end", f"  {info['term']}  ", ("related_pill", f"term::{info['term']}"))
                    tb.insert("end", "   ", "normal")
            tb.insert("end", "\n", "normal")

    def _toggle_current_flow_done(self):
        if not self._current_flow_item or self._current_flow_item.get("_kind") == "master":
            return
        iid = self._current_flow_item["id"]
        self._factory_flow_done[iid] = not bool(self._factory_flow_done.get(iid, False))
        self._current_progress["factory_flow"] = dict(self._factory_flow_done)
        if self.current_job:
            jid = self.current_job["id"]
            self.storage.save_progress(jid, self._current_progress)
            self.current_job["progress"] = dict(self._current_progress)
        self._refresh_flow_list(select_id=iid)

    def _step_flow_item(self, delta):
        if not self._flow_items_view or not self._current_flow_item:
            return
        cur_id = self._current_flow_item["id"]
        pos = next((i for i, x in enumerate(self._flow_items_view) if x["id"] == cur_id), 0)
        new_pos = max(0, min(len(self._flow_items_view) - 1, pos + delta))
        self.lb_flow.selection_clear(0, "end")
        self.lb_flow.selection_set(new_pos)
        self.lb_flow.see(new_pos)
        self._render_flow_detail(self._flow_items_view[new_pos])

    def _jump_to_station_scenarios(self):
        if not self._current_flow_item or self._current_flow_item.get("_kind") != "station":
            return
        sid = self._current_flow_item["id"]
        self.seg_flow_mode.set("🚨 40 Tình Huống OE")
        if hasattr(self, "ent_flow_search"):
            self.ent_flow_search.delete(0, "end")
        if hasattr(self, "cb_flow_group"):
            self.cb_flow_group.set("Tất cả 8 nhóm tình huống")
        target_lbl = next((lbl for lbl, v in self._flow_station_map.items() if v == sid), "Tất cả 10 trạm")
        if hasattr(self, "cb_flow_station"):
            self.cb_flow_station.set(target_lbl)
        self._on_flow_mode_change("🚨 40 Tình Huống OE")

    def _open_flow_doc(self):
        if not self._current_flow_item:
            return
        if self._current_flow_item.get("_kind") == "master":
            self._open_offline_doc("cable_mfg_machines")
            return
        dk = self._current_flow_item.get("data", {}).get("doc_key")
        if dk:
            self._open_offline_doc(dk)

    def _open_flow_lesson(self):
        if not self._current_flow_item:
            return
        if self._current_flow_item.get("_kind") == "master":
            self.open_curriculum_lesson("L1.1")
            return
        lid = self._current_flow_item.get("data", {}).get("lesson_id")
        if lid:
            self.open_curriculum_lesson(lid)

    # =====================================================================
    # LOGIC NẠP DỮ LIỆU & LAZY TAB RENDERING
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
"""
            analyzer = JobAnalyzer()
            res1 = analyzer.analyze(sample_jd_python, force_offline=True)
            self.storage.add_job(
                title=res1["title"], company=res1["company"], level=res1["level"],
                category=res1["category"], raw_jd=res1["raw_jd"], analysis=res1["analysis"],
                location=res1["location"], salary_range=res1["salary_range"], tags=res1["tags"]
            )

            sample_jd_react = """
Vị trí: Junior Frontend Developer (React / TypeScript)
Công ty: FPT Digital Lab
Địa điểm: TP. Hồ Chí Minh
Mức lương: 12.000.000 - 18.000.000 VNĐ

Yêu cầu:
- 1-2 năm kinh nghiệm với JavaScript (ES6+), ReactJS và TypeScript.
- Sử dụng Git thành thạo.
"""
            res2 = analyzer.analyze(sample_jd_react, force_offline=True)
            self.storage.add_job(
                title=res2["title"], company=res2["company"], level=res2["level"],
                category=res2["category"], raw_jd=res2["raw_jd"], analysis=res2["analysis"],
                location=res2["location"], salary_range=res2["salary_range"], tags=res2["tags"]
            )

    def _load_jobs(self):
        """Tải danh sách công việc từ CSDL."""
        kw = self.txt_search.get().strip() if hasattr(self, "txt_search") else ""
        lvl = self.cb_level.get() if hasattr(self, "cb_level") else "Tất cả"
        cat = self.cb_cat.get() if hasattr(self, "cb_cat") else "Tất cả"

        self.all_jobs = self.storage.list_jobs(keyword=kw, level=lvl, category=cat)

        for item in self.tree.get_children():
            self.tree.delete(item)

        for job in self.all_jobs:
            self.tree.insert("", "end", iid=str(job["id"]), values=(job["title"], job["company"], job["level"]))

        self.lbl_count.configure(text=f"Tổng số: {len(self.all_jobs)} công việc")

        children = self.tree.get_children()
        if children:
            self.tree.selection_set(children[0])
            self._display_job_detail(int(children[0]))

    def _debounce_search(self):
        if hasattr(self, "_search_timer") and self._search_timer:
            self.after_cancel(self._search_timer)
        self._search_timer = self.after(150, self._load_jobs)

    def _debounce_interview_search(self):
        if self._interview_search_timer:
            self.after_cancel(self._interview_search_timer)
        self._interview_search_timer = self.after(120, self._update_interview_display)

    def _apply_filter(self):
        self._load_jobs()

    def _on_job_select(self, _event):
        sel = self.tree.selection()
        if not sel:
            return
        job_id = int(sel[0])
        if self.current_job and self.current_job.get("id") == job_id:
            return
        self._display_job_detail(job_id)

    def _display_job_detail(self, job_id):
        """Cập nhật tức thì Header + Tab đang mở (Lazy Tab Rendering cho 5 tab còn lại)."""
        job = self.storage.get_job(job_id)
        if not job:
            return
        self.current_job = job

        # 1. Header & Badges (~2ms)
        self.dt_title.configure(text=job["title"])
        self.lbl_company.configure(text=f"🏢 {job['company']}")
        self.badge_level.configure(text=f"Level: {job['level']}")
        self.badge_cat.configure(text=f"Ngành: {job['category']}")
        self.badge_loc.configure(text=f"📍 {job.get('location', 'N/A')}")
        self.badge_salary.configure(text=f"💰 {job.get('salary_range', 'Thỏa thuận')}")
        self.cb_status.set(job.get("status", "New"))

        # Nạp tiến độ học tập bền vững từ SQLite (Roadmap + Phỏng vấn + Giáo Trình + Dòng Chảy CADIVI)
        prog = job.get("progress") if isinstance(job.get("progress"), dict) else self.storage.get_progress(job_id)
        self._current_progress = {
            "roadmap": dict(prog.get("roadmap", {})),
            "interview": dict(prog.get("interview", {})),
            "curriculum": dict(prog.get("curriculum", {})),
            "factory_flow": dict(prog.get("factory_flow", {})),
        }
        self._roadmap_checked = self._current_progress["roadmap"]
        self._interview_progress = self._current_progress["interview"]
        self._curriculum_done = self._current_progress["curriculum"]
        self._factory_flow_done = self._current_progress["factory_flow"]
        self._revealed_qids = set()

        # Chuẩn bị danh sách câu hỏi & combobox (không render UI nếu chưa mở tab Phỏng vấn)
        analysis = job.get("analysis", {})
        self._current_interview_raw = analysis.get("interview_prep", []) or []
        present_cats = ["Tất cả chủ đề"]
        for q in self._current_interview_raw:
            c = q.get("category")
            if c and c not in present_cats:
                present_cats.append(c)
        if len(present_cats) > 1 and hasattr(self, "cbo_interview_cat"):
            self.cbo_interview_cat.configure(values=present_cats)
            self.cbo_interview_cat.set("Tất cả chủ đề")
        if hasattr(self, "cbo_interview_status"):
            self.cbo_interview_status.set("Tất cả trạng thái")
        if hasattr(self, "ent_interview_search"):
            self.ent_interview_search.delete(0, "end")
        self._update_interview_readiness_label()

        # Đánh dấu tất cả 8 tab cần render, sau đó CHỈ render tab đang hiển thị!
        self._dirty_tabs = {"overview", "factory_flow", "curriculum", "skills", "roadmap", "resources", "interview", "notes"}
        self._render_current_tab()

    def _on_tab_change(self):
        self._render_current_tab()

    def _render_current_tab(self):
        if not self.current_job:
            return
        active_label = self.tabview.get()
        tab_key = self.TAB_MAP.get(active_label)
        if not tab_key or tab_key not in self._dirty_tabs:
            return
        self._dirty_tabs.discard(tab_key)

        analysis = self.current_job.get("analysis", {})
        if tab_key == "overview":
            self._render_overview_tab(analysis.get("overview", {}))
        elif tab_key == "factory_flow":
            self._render_factory_flow_tab()
        elif tab_key == "curriculum":
            self._render_curriculum_tab()
        elif tab_key == "skills":
            self._render_skills_tab(analysis.get("skills_matrix", {}))
        elif tab_key == "roadmap":
            self._render_roadmap_tab(analysis.get("roadmap", []))
        elif tab_key == "resources":
            self._render_resources_tab(analysis.get("resources", {}))
        elif tab_key == "interview":
            self._update_interview_display()
        elif tab_key == "notes":
            self._render_notes_tab()

    # =====================================================================
    # RENDER CÁC TAB CHI TIẾT (NHANH < 20ms, HỖ TRỢ CLICK THUẬT NGỮ)
    # =====================================================================
    def _render_overview_tab(self, overview):
        tb = self.txt_overview
        tb.configure(state="normal")
        tb.delete("1.0", "end")

        tb.insert("end", "💡 Mẹo học nhanh: Bấm trực tiếp vào các thuật ngữ màu xanh gạch chân (OEE, OLE, MES, SMED, BOM, XLPE...) để mở định nghĩa & ví dụ thực tế tại CADIVI!\n", "subtext")
        tb.insert("end", "─" * 82 + "\n", "divider")

        tb.insert("end", "🎯 TÓM TẮT VAI TRÒ (ROLE OVERVIEW)\n", "sec_yellow")
        insert_with_glossary(tb, overview.get("summary", "Chưa có tóm tắt vai trò.") + "\n\n", "card_box")

        tb.insert("end", "🚀 NHIỆM VỤ CỐT LÕI CẦN HOÀN THÀNH (CORE MISSION)\n", "sec_green")
        insert_with_glossary(tb, overview.get("mission", "Chưa có thông tin nhiệm vụ.") + "\n\n", "card_box")

        tb.insert("end", "🏢 MÔI TRƯỜNG & CHẾ ĐỘ LÀM VIỆC (WORK MODE)\n", "sec_blue")
        insert_with_glossary(tb, overview.get("work_mode", "N/A") + "\n", "card_box")

        tb.tag_raise("term_link")
        tb.tag_raise("sel")
        tb.see("1.0")
        tb.configure(state="disabled")

    def _render_skills_tab(self, skills):
        tb = self.txt_skills
        tb.configure(state="normal")
        tb.delete("1.0", "end")

        tb.insert("end", "💡 Bấm vào bất kỳ công cụ hoặc thuật ngữ màu xanh nào bên dưới (MES, Minitab, Power BI, OEE, SMED, XLPE, IEC 60228...) để xem định nghĩa & cách áp dụng tại CADIVI!\n", "subtext")
        tb.insert("end", "─" * 82 + "\n", "divider")

        sections = [
            ("🔴 KỸ NĂNG BẮT BUỘC (MUST-HAVE / CORE)", skills.get("must_have", []), "sec_red", "skill_red"),
            ("🟢 KỸ NĂNG ƯU TIÊN / ĐIỂM CỘNG (NICE-TO-HAVE)", skills.get("nice_to_have", []), "sec_green", "skill_green"),
            ("⚙️ CÔNG CỤ & HỆ SINH THÁI PHẦN MỀM (TOOLS & PLATFORMS)", skills.get("tools", []), "sec_blue", "skill_blue"),
            ("💡 KỸ NĂNG MỀM & PHƯƠNG PHÁP LUẬN (SOFT SKILLS)", skills.get("soft_skills", []), "sec_yellow", "skill_yellow"),
        ]
        for header, items, h_tag, item_tag in sections:
            tb.insert("end", f"{header}\n", h_tag)
            if not items:
                tb.insert("end", "  (Không có thông tin)\n\n", "subtext")
                continue
            for it in items:
                tb.insert("end", "  • ", item_tag)
                insert_with_glossary(tb, it + "\n", item_tag)
            tb.insert("end", "\n", "normal")

        tb.tag_raise("term_link")
        tb.tag_raise("sel")
        tb.see("1.0")
        tb.configure(state="disabled")

    def _render_roadmap_tab(self, roadmap):
        tb = self.txt_roadmap
        tb.configure(state="normal")
        tb.delete("1.0", "end")

        if not roadmap:
            tb.insert("end", "Chưa có lộ trình phân rã.", "subtext")
            tb.configure(state="disabled")
            return

        job_id = self.current_job["id"] if self.current_job else 0
        total_actions = sum(len(ph.get("action_items", [])) for ph in roadmap)
        done_actions = 0
        for p_idx, ph in enumerate(roadmap, 1):
            for a_idx in range(len(ph.get("action_items", []))):
                if self._roadmap_checked.get(f"{p_idx}:{a_idx}", False):
                    done_actions += 1
        pct = (done_actions / total_actions * 100.0) if total_actions else 0.0
        tb.insert("end", f"✅ Tiến độ hoàn thành lộ trình: {done_actions} / {total_actions} đầu việc ({pct:.1f}%)  •  💾 Tự động lưu vào SQLite\n", "sec_green")
        tb.insert("end", "💡 Bấm vào ô [ ☐ ] để đánh dấu hoàn thành từng việc  •  Bấm vào thuật ngữ xanh gạch chân (Genba, VSM, SMED, OEE, Minitab...) để tra cứu tức thì!\n", "subtext")
        tb.insert("end", "─" * 82 + "\n", "divider")

        for p_idx, phase in enumerate(roadmap, 1):
            p_title = phase.get("phase", f"Giai đoạn {p_idx}")
            tb.insert("end", f"🧭 GIAI ĐOẠN {p_idx}: ", "sec_blue")
            insert_with_glossary(tb, p_title + "\n", "sec_blue")

            goals = phase.get("goals", [])
            if goals:
                tb.insert("end", "  🎯 Mục tiêu trọng tâm:\n", "sec_yellow")
                for g in goals:
                    tb.insert("end", "    • ", "bullet")
                    insert_with_glossary(tb, g + "\n", "bullet")

            actions = phase.get("action_items", [])
            if actions:
                tb.insert("end", "  ✅ Hành động cụ thể (Bấm ☐ để tích chọn — tự động lưu):\n", "sec_green")
                for a_idx, a in enumerate(actions):
                    chk_key = f"{p_idx}:{a_idx}"
                    is_done = bool(self._roadmap_checked.get(chk_key, False))
                    chk_tag = f"chk::{job_id}:{p_idx}:{a_idx}"
                    icon = "  ☑  " if is_done else "  ☐  "
                    tb.insert("end", icon, ("chk_on" if is_done else "chk_off", "chk_click", chk_tag))
                    insert_with_glossary(tb, a + "\n", "chk_done_txt" if is_done else "normal")

            tb.insert("end", "\n" + "─" * 82 + "\n", "divider")

        tb.tag_raise("term_link")
        tb.tag_raise("term_link_bold")
        tb.tag_raise("sel")
        tb.see("1.0")
        tb.configure(state="disabled")

    def _on_roadmap_checkbox_click(self, event):
        tb = self.txt_roadmap
        idx = tb.index(f"@{event.x},{event.y}")
        for tag in tb.tag_names(idx):
            if tag.startswith("chk::"):
                parts = tag[5:].split(":")
                job_id = int(parts[0])
                chk_key = f"{parts[1]}:{parts[2]}"
                self._roadmap_checked[chk_key] = not bool(self._roadmap_checked.get(chk_key, False))
                self._current_progress["roadmap"] = dict(self._roadmap_checked)
                if job_id:
                    self.storage.save_progress(job_id, self._current_progress)
                    if self.current_job and self.current_job.get("id") == job_id:
                        self.current_job["progress"] = dict(self._current_progress)
                yview = tb.yview()
                self._render_roadmap_tab(self.current_job.get("analysis", {}).get("roadmap", []))
                tb.yview_moveto(yview[0])
                return "break"

    def _render_notes_tab(self):
        job = self.current_job
        if not job:
            return
        self.txt_notes.delete("1.0", "end")
        self.txt_notes.insert("1.0", job.get("user_notes", ""))

        tb = self.txt_raw_jd
        tb.configure(state="normal")
        tb.delete("1.0", "end")
        insert_with_glossary(tb, job.get("raw_jd", ""), "raw_mono")
        tb.tag_raise("term_link")
        tb.tag_raise("sel")
        tb.see("1.0")
        tb.configure(state="disabled")

    def _open_offline_doc(self, doc_key):
        """Mở cửa sổ đọc cẩm nang kỹ thuật 100% offline."""
        doc = offline_knowledge.get_offline_doc(doc_key)
        if doc:
            OfflineDocViewer(
                self,
                doc["title"],
                doc["content"],
                doc.get("category", "Cẩm Nang Kỹ Thuật"),
                on_term_click=self.open_term_popup
            )
        else:
            messagebox.showinfo("Cẩm Nang Offline", f"Cẩm nang '{doc_key}' đang được cập nhật thêm nội dung.", parent=self)

    def _resolve_doc_key(self, name):
        """Ánh xạ tên tài liệu/phần mềm sang ID cẩm nang offline."""
        nl = name.lower()
        if hasattr(offline_knowledge, "OFFLINE_DOCS") and nl in offline_knowledge.OFFLINE_DOCS:
            return nl
        if any(k in nl for k in ["cận chiến", "mã cáp", "decoder", "warroom", "iso 17025", "vilas", "offer", "thư cảm ơn", "gelex", "90 giây", "tự giới thiệu"]):
            return "cadivi_interview_warroom_decoder"
        if any(k in nl for k in ["work sampling", "cost deployment", "loss tree", "wcm", "lsw", "lpa", "wrench time", "pm compliance", "pdm", "case study", "đề thi", "vòng 2", "moc", "ecn", "headcount"]):
            return "oe_field_execution_case_test"
        if any(k in nl for k in ["extrusion", "l/d", "ddr", "melt pressure", "sharkskin", "die drool", "regrind", "cup-and-cone", "forensics", "solar", "h1z2z2", "braiding", "qcvn 4", "astm b49", "en 50618"]):
            return "cable_extrusion_wire_forensics"
        if any(k in nl for k in ["s&op", "mps", "mrp", "crp", "rty", "fpy", "loto", "ehs", "iso 9001", "iso 14001", "iso 45001", "iso 50001", "standard cost", "hoshin", "adkar", "7 qc", "kế hoạch", "an toàn"]):
            return "planning_quality_ehs_cost"
        if any(k in nl for k in ["dây cáp", "cáp điện", "cadivi", "máy móc", "kéo sợi", "đùn", "xlpe", "iec 60228", "iec 60502", "spark", "acsr", "mica", "partial discharge", "water immersion"]):
            return "cable_mfg_machines"
        if any(k in nl for k in ["six sigma", "dmaic", "pfmea", "toc", "tpm", "operational excellence", "asq"]):
            return "oe_six_sigma_dmaic"
        if any(k in nl for k in ["năng lực", "rccp", "capacity", "cut-length", "cost accounting", "giá thành", "copper give"]):
            return "cable_cost_capacity"
        if "oee" in nl:
            return "oee"
        if "ole" in nl:
            return "ole"
        if "smed" in nl:
            return "smed"
        if any(k in nl for k in ["lean", "muda", "5s", "kaizen", "poka", "vsm"]):
            return "lean_muda"
        if any(k in nl for k in ["bom", "định mức", "hao phí"]):
            return "bom_cost"
        if any(k in nl for k in ["excel", "power query", "vba"]):
            return "excel_mfg"
        if any(k in nl for k in ["power bi", "powerbi"]):
            return "powerbi_mfg"
        if any(k in nl for k in ["minitab", "spc", "cpk"]):
            return "minitab_spc"
        if any(k in nl for k in ["autocad", "visio", "layout", "spaghetti"]):
            return "autocad_layout"
        if any(k in nl for k in ["sap", "mes", "erp", "scada"]):
            return "erp_mes"
        if any(k in nl for k in ["python", "fastapi", "django"]):
            return "python_core"
        if any(k in nl for k in ["react", "javascript", "typescript", "frontend"]):
            return "react_fe"
        if any(k in nl for k in ["docker", "kubernetes", "k8s", "container"]):
            return "docker_devops"
        if any(k in nl for k in ["postgres", "sql", "dbeaver", "database"]):
            return "sql_db"
        if any(k in nl for k in ["redis", "cache"]):
            return "redis_cache"
        if any(k in nl for k in ["git", "github", "gitlab"]):
            return "git_vcs"
        return "oee"

    def _render_resources_tab(self, resources):
        for w in self.scroll_resources.winfo_children():
            w.destroy()

        # === 1. BANNER TRUNG TÂM CẨM NANG & TỪ ĐIỂN 100% OFFLINE ===
        c_hub = ctk.CTkFrame(self.scroll_resources, fg_color=THEME["crust"], corner_radius=8)
        c_hub.pack(fill="x", pady=6, padx=5, ipady=8)

        hub_top = ctk.CTkFrame(c_hub, fg_color="transparent")
        hub_top.pack(fill="x", padx=12, pady=(4, 6))

        ctk.CTkLabel(
            hub_top,
            text="📖 KHO CẨM NANG KỸ THUẬT 100% OFFLINE (BẤM XEM TỨC THÌ KHÔNG CẦN MẠNG):",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=THEME["green"]
        ).pack(side="left")

        term_cnt = len(term_glossary.get_all_terms()) if term_glossary else 0
        ctk.CTkButton(
            hub_top,
            text=f"🔎 Mở Từ Điển {term_cnt} Thuật Ngữ CADIVI OE",
            font=ctk.CTkFont(size=11, weight="bold"),
            height=26,
            fg_color=THEME["cyan"],
            hover_color=THEME["blue"],
            text_color=THEME["crust"],
            command=self._open_glossary_browser
        ).pack(side="right")

        grid_frame = ctk.CTkFrame(c_hub, fg_color="transparent")
        grid_frame.pack(fill="x", padx=12, pady=(0, 4))

        cat = (self.current_job.get("category", "") if self.current_job else "").lower()
        is_it = any(k in cat for k in ["backend", "frontend", "devops", "fullstack", "data", "software", "it"])

        if is_it:
            quick_guides = [
                ("🐍 Python Core & GIL", "python_core"),
                ("⚛️ React 18 & Virtual DOM", "react_fe"),
                ("🐳 Docker & Multi-stage", "docker_devops"),
                ("🗄️ SQL & B-Tree Index", "sql_db"),
                ("⚡ Redis Caching", "redis_cache"),
                ("🌿 Git Branching & Rebase", "git_vcs"),
                ("📊 Excel Power Query", "excel_mfg"),
                ("📈 Power BI Dashboard", "powerbi_mfg"),
                ("⚙️ Cẩm Nang OEE", "oee"),
                ("🏭 Hệ Thống ERP/MES", "erp_mes")
            ]
        else:
            quick_guides = [
                ("🎯 Cận Chiến PV & Mã Cáp", "cadivi_interview_warroom_decoder"),
                ("🔌 Máy Móc Cáp (CADIVI)", "cable_mfg_machines"),
                ("🔬 Đùn Sâu & Đứt Sợi", "cable_extrusion_wire_forensics"),
                ("🎯 Thực Địa & Test Vòng 2", "oe_field_execution_case_test"),
                ("🏆 OE / Six Sigma / DMAIC", "oe_six_sigma_dmaic"),
                ("💰 Năng Lực & Chi Phí Cáp", "cable_cost_capacity"),
                ("📋 Kế Hoạch, RTY & ISO", "planning_quality_ehs_cost"),
                ("⚙️ Cẩm Nang OEE", "oee"),
                ("👥 Cẩm Nang OLE", "ole"),
                ("⚡ Kỹ Thuật SMED", "smed"),
                ("🧹 8 Lãng Phí & VSM/5S", "lean_muda"),
                ("📦 Định Mức BOM & Kho", "bom_cost"),
                ("🎯 Minitab & SPC", "minitab_spc"),
                ("📊 Excel Power Query/VBA", "excel_mfg"),
                ("📈 Power BI Dashboard", "powerbi_mfg"),
                ("📐 AutoCAD Layout", "autocad_layout"),
                ("🏭 Hệ Thống ERP/MES", "erp_mes")
            ]

        for idx, (label, key) in enumerate(quick_guides):
            r = idx // 5
            c = idx % 5
            btn = ctk.CTkButton(
                grid_frame,
                text=label,
                font=ctk.CTkFont(size=11, weight="bold"),
                height=28,
                fg_color=THEME["surface0"],
                hover_color=THEME["green"],
                text_color=THEME["text"],
                command=lambda k=key: self._open_offline_doc(k)
            )
            btn.grid(row=r, column=c, padx=3, pady=3, sticky="ew")
            grid_frame.columnconfigure(c, weight=1)

        # === 2. PHẦN MỀM & CÔNG CỤ HỖ TRỢ CHUYÊN DỤNG ===
        softwares = resources.get("softwares", [])
        if not softwares:
            if not is_it:
                softwares = [
                    {"name": "Microsoft Excel Nâng Cao (Power Query, VBA)", "role": "Xử lý dữ liệu thô nhiều ca, vẽ biểu đồ Pareto 80/20, tự động hóa Macro VBA", "url": "https://support.microsoft.com/excel", "doc_key": "excel_mfg"},
                    {"name": "Microsoft Power BI", "role": "Xây dựng Dashboard OEE/OLE thời gian thực, trực quan hóa xu hướng", "url": "https://powerbi.microsoft.com/", "doc_key": "powerbi_mfg"},
                    {"name": "Minitab", "role": "Kiểm soát quá trình thống kê SPC (Xbar-R), phân tích năng lực quá trình Cpk", "url": "https://www.minitab.com/", "doc_key": "minitab_spc"},
                    {"name": "AutoCAD / MS Visio", "role": "Thiết kế Layout xưởng, vẽ sơ đồ Spaghetti, sơ đồ chuỗi giá trị VSM", "url": "https://www.autodesk.com/", "doc_key": "autocad_layout"},
                    {"name": "Hệ thống SAP ERP (PP) & MES", "role": "Quản lý định mức vật tư BOM, lệnh sản xuất và thu thập dữ liệu máy", "url": "https://help.sap.com/", "doc_key": "erp_mes"}
                ]
            else:
                softwares = [
                    {"name": "Visual Studio Code / JetBrains IDE", "role": "Môi trường lập trình, gỡ lỗi và quản lý mã nguồn", "url": "https://code.visualstudio.com/", "doc_key": "python_core"},
                    {"name": "Git & GitHub / GitLab", "role": "Quản lý phiên bản mã nguồn, Pull Request và CI/CD", "url": "https://github.com/", "doc_key": "git_vcs"},
                    {"name": "Docker & Docker Compose", "role": "Đóng gói container môi trường phát triển độc lập", "url": "https://www.docker.com/", "doc_key": "docker_devops"},
                    {"name": "PostgreSQL / DBeaver", "role": "Quản trị cơ sở dữ liệu quan hệ và tối ưu truy vấn SQL", "url": "https://dbeaver.io/", "doc_key": "sql_db"},
                    {"name": "Redis Insight", "role": "Giám sát bộ nhớ cache và tối ưu hóa hiệu năng in-memory", "url": "https://redis.io/insight/", "doc_key": "redis_cache"}
                ]

        if softwares:
            c_soft = ctk.CTkFrame(self.scroll_resources, fg_color=THEME["crust"], corner_radius=8)
            c_soft.pack(fill="x", pady=6, padx=5, ipady=6)
            ctk.CTkLabel(c_soft, text="💻 Hệ Sinh Thái Phần Mềm Hỗ Trợ Chuyên Dụng:", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["yellow"]).pack(anchor="w", padx=12, pady=(4, 6))

            for s in softwares:
                row = ctk.CTkFrame(c_soft, fg_color=THEME["surface0"], corner_radius=6)
                row.pack(fill="x", padx=12, pady=3, ipady=4)

                s_name = s.get("name", "Software")
                s_url = s.get("url", "#")
                s_role = s.get("role", "")
                doc_key = s.get("doc_key") or self._resolve_doc_key(s_name)

                info_box = ctk.CTkFrame(row, fg_color="transparent")
                info_box.pack(side="left", padx=10, fill="x", expand=True)
                ctk.CTkLabel(info_box, text=f"⚙️ {s_name}", font=ctk.CTkFont(size=12, weight="bold"), text_color=THEME["text"]).pack(anchor="w")
                if s_role:
                    ctk.CTkLabel(info_box, text=s_role, font=ctk.CTkFont(size=11), text_color=THEME["subtext"], wraplength=480, justify="left").pack(anchor="w")

                btn_offline = ctk.CTkButton(
                    row, text="📖 Đọc Cẩm Nang", width=125, height=26,
                    font=ctk.CTkFont(size=11, weight="bold"),
                    fg_color=THEME["green"], hover_color="#74c7ec", text_color=THEME["crust"],
                    command=lambda k=doc_key: self._open_offline_doc(k)
                )
                btn_offline.pack(side="right", padx=(4, 10))

                btn_open = ctk.CTkButton(
                    row, text="🌐 Web", width=50, height=26,
                    fg_color=THEME["surface1"], hover_color=THEME["blue"], text_color=THEME["subtext"],
                    command=lambda u=s_url: webbrowser.open(u)
                )
                btn_open.pack(side="right", padx=(0, 2))

        # === 3. TÀI LIỆU CHÍNH THỐNG ===
        docs = resources.get("official_docs", [])
        c1 = ctk.CTkFrame(self.scroll_resources, fg_color=THEME["crust"], corner_radius=8)
        c1.pack(fill="x", pady=6, padx=5, ipady=6)
        ctk.CTkLabel(c1, text="🌐 Tài Liệu Chính Thống & Tiêu Chuẩn Ngành:", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["blue"]).pack(anchor="w", padx=12, pady=(4, 6))

        if docs:
            for d in docs:
                row = ctk.CTkFrame(c1, fg_color=THEME["surface0"], corner_radius=6)
                row.pack(fill="x", padx=12, pady=3, ipady=4)

                name = d.get("name", "Docs")
                url = d.get("url", "#")
                desc = d.get("desc", "")
                doc_key = d.get("doc_key") or self._resolve_doc_key(name)

                info_box = ctk.CTkFrame(row, fg_color="transparent")
                info_box.pack(side="left", padx=10, fill="x", expand=True)
                ctk.CTkLabel(info_box, text=name, font=ctk.CTkFont(size=12, weight="bold"), text_color=THEME["text"]).pack(anchor="w")
                if desc:
                    ctk.CTkLabel(info_box, text=desc, font=ctk.CTkFont(size=11), text_color=THEME["subtext"], wraplength=480, justify="left").pack(anchor="w")

                btn_offline = ctk.CTkButton(
                    row, text="📖 Đọc Cẩm Nang", width=125, height=26,
                    font=ctk.CTkFont(size=11, weight="bold"),
                    fg_color=THEME["green"], hover_color="#74c7ec", text_color=THEME["crust"],
                    command=lambda k=doc_key: self._open_offline_doc(k)
                )
                btn_offline.pack(side="right", padx=(4, 10))

                btn_open = ctk.CTkButton(
                    row, text="🌐 Web", width=50, height=26,
                    fg_color=THEME["surface1"], hover_color=THEME["blue"], text_color=THEME["subtext"],
                    command=lambda u=url: webbrowser.open(u)
                )
                btn_open.pack(side="right", padx=(0, 2))
        else:
            ctk.CTkLabel(c1, text="Chưa có tài liệu.", text_color=THEME["subtext"]).pack(padx=12, pady=4)

        # === 4. SÁCH KINH ĐIỂN ===
        books = resources.get("books", [])
        c2 = ctk.CTkFrame(self.scroll_resources, fg_color=THEME["crust"], corner_radius=8)
        c2.pack(fill="x", pady=6, padx=5, ipady=6)
        ctk.CTkLabel(c2, text="📖 Sách & Giáo Trình Kinh Điển:", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["peach"]).pack(anchor="w", padx=12, pady=(4, 6))
        for b in books:
            ctk.CTkLabel(c2, text=f"  📚 {b}", font=ctk.CTkFont(size=12), text_color=THEME["text"]).pack(anchor="w", padx=12, pady=2)

        # === 5. TỪ KHÓA VÀNG ===
        keywords = resources.get("search_keywords", [])
        c3 = ctk.CTkFrame(self.scroll_resources, fg_color=THEME["crust"], corner_radius=8)
        c3.pack(fill="x", pady=6, padx=5, ipady=6)
        ctk.CTkLabel(c3, text="🔍 Từ Khóa Vàng Tra Cứu Google / Tài Liệu Chuẩn:", font=ctk.CTkFont(size=13, weight="bold"), text_color=THEME["yellow"]).pack(anchor="w", padx=12, pady=(4, 6))
        kw_box = ctk.CTkFrame(c3, fg_color="transparent")
        kw_box.pack(fill="x", padx=12, pady=(0, 4))
        for idx, kw in enumerate(keywords):
            r = idx // 2
            c = idx % 2
            lbl = ctk.CTkLabel(
                kw_box,
                text=f"`{kw}`",
                font=ctk.CTkFont(family="Consolas", size=11),
                fg_color=THEME["surface0"],
                text_color=THEME["yellow"],
                corner_radius=4,
                padx=8,
                pady=4,
                wraplength=340,
                justify="left",
                anchor="w"
            )
            lbl.grid(row=r, column=c, padx=4, pady=3, sticky="ew")
            kw_box.columnconfigure(c, weight=1)

    def _render_interview_tab(self, interview):
        self._current_interview_raw = interview or []
        present_cats = ["Tất cả chủ đề"]
        for q in self._current_interview_raw:
            c = q.get("category")
            if c and c not in present_cats:
                present_cats.append(c)
        if len(present_cats) > 1 and hasattr(self, "cbo_interview_cat"):
            self.cbo_interview_cat.configure(values=present_cats)
            self.cbo_interview_cat.set("Tất cả chủ đề")
        if hasattr(self, "ent_interview_search"):
            self.ent_interview_search.delete(0, "end")
        self._update_interview_display()

    def _toggle_quiz_mode(self):
        self._quiz_mode = bool(self.var_quiz_mode.get())
        self._revealed_qids = set()
        self._update_interview_display()

    def _toggle_reveal_all(self):
        if not self._quiz_mode:
            self.var_quiz_mode.set(True)
            self._quiz_mode = True
        visible_ids = [item.get("id") or f"q_{i}" for i, item in enumerate(self._filtered_interview_items, 1)]
        if visible_ids and all(qid in self._revealed_qids for qid in visible_ids):
            self._revealed_qids.difference_update(visible_ids)
        else:
            self._revealed_qids.update(visible_ids)
        self._update_interview_display(preserve_scroll=True)

    def _update_interview_readiness_label(self):
        if not hasattr(self, "lbl_readiness"):
            return
        total = len(self._current_interview_raw)
        mastered = sum(1 for v in self._interview_progress.values() if v == "mastered")
        review = sum(1 for v in self._interview_progress.values() if v == "review")
        pct = (mastered / total * 100.0) if total else 0.0
        self.lbl_readiness.configure(
            text=f"🏆 Sẵn sàng: {mastered}/{total} ({pct:.1f}%)  •  🔁 Cần ôn: {review}  •  💾 Tự động lưu"
        )

    def _mark_interview_status(self, qid, new_state):
        if self._interview_progress.get(qid) == new_state:
            self._interview_progress.pop(qid, None)
        else:
            self._interview_progress[qid] = new_state
        self._current_progress["interview"] = dict(self._interview_progress)
        if self.current_job:
            jid = self.current_job["id"]
            self.storage.save_progress(jid, self._current_progress)
            self.current_job["progress"] = dict(self._current_progress)
        self._update_interview_readiness_label()

    def _on_interview_action_click(self, event):
        tb = self.txt_interview
        if tb.tag_ranges("sel"):
            return
        idx = tb.index(f"@{event.x},{event.y}")
        for tag in tb.tag_names(idx):
            if tag.startswith("iv_reveal::"):
                qid = tag[len("iv_reveal::"):]
                if qid in self._revealed_qids:
                    self._revealed_qids.discard(qid)
                else:
                    self._revealed_qids.add(qid)
                self._update_interview_display(preserve_scroll=True)
                return "break"
            if tag.startswith("iv_mark::"):
                rest = tag[len("iv_mark::"):]
                qid, state = rest.rsplit("::", 1)
                self._mark_interview_status(qid, state)
                self._update_interview_display(preserve_scroll=True)
                return "break"

    def _update_interview_display(self, preserve_scroll=False):
        """Render toàn bộ danh sách câu hỏi trên 1 widget C-Engine tk.Text trong < 250ms, hỗ trợ Chế độ Luyện Phỏng Vấn."""
        tb = self.txt_interview
        saved_yview = tb.yview() if preserve_scroll else None
        tb.configure(state="normal")
        tb.delete("1.0", "end")

        if not self._current_interview_raw:
            self._filtered_interview_items = []
            tb.insert("end", "Chưa có câu hỏi phỏng vấn.", "subtext")
            tb.configure(state="disabled")
            if hasattr(self, "lbl_interview_count"):
                self.lbl_interview_count.configure(text="Hiển thị: 0 / 0 câu")
            self._update_interview_readiness_label()
            return

        kw = self.ent_interview_search.get().strip().lower() if hasattr(self, "ent_interview_search") else ""
        selected_cat = self.cbo_interview_cat.get() if hasattr(self, "cbo_interview_cat") else "Tất cả chủ đề"
        selected_status = self.cbo_interview_status.get() if hasattr(self, "cbo_interview_status") else "Tất cả trạng thái"

        filtered = []
        for orig_idx, item in enumerate(self._current_interview_raw, 1):
            qid = item.get("id") or f"q_{orig_idx}"
            cat = item.get("category", "")
            q_text = item.get("question", "")
            kp = item.get("key_points", "")
            q_type = item.get("type", "")
            st = self._interview_progress.get(qid, "")

            if selected_cat != "Tất cả chủ đề" and cat != selected_cat:
                continue
            if selected_status == "Chưa thuộc" and st == "mastered":
                continue
            if selected_status == "🔁 Cần ôn lại" and st != "review":
                continue
            if selected_status == "✅ Đã thuộc" and st != "mastered":
                continue

            if kw:
                haystack = f"{q_text} {kp} {cat} {q_type}".lower()
                if kw not in haystack:
                    stripped_hay = term_glossary.strip_term_formulas(haystack) if term_glossary else haystack
                    if kw not in stripped_hay:
                        continue

            filtered.append((qid, item))

        self._filtered_interview_items = [it for _, it in filtered]
        total_cnt = len(self._current_interview_raw)
        shown_cnt = len(filtered)
        if hasattr(self, "lbl_interview_count"):
            self.lbl_interview_count.configure(text=f"Hiển thị: {shown_cnt} / {total_cnt} câu")
        self._update_interview_readiness_label()

        if not filtered:
            tb.insert("end", "\n  🔍 Không tìm thấy câu hỏi nào phù hợp với bộ lọc.", "subtext")
            tb.configure(state="disabled")
            return

        mode_hint = (
            "🎯 ĐANG Ở CHẾ ĐỘ LUYỆN PHỎNG VẤN: Tự trả lời trong đầu trước → Bấm [ 👁️ Xem gợi ý ] để đối chiếu → Chấm [ ✅ Đã thuộc ] hoặc [ 🔁 Cần ôn lại ]!\n"
            if self._quiz_mode else
            "💡 Bấm vào thuật ngữ xanh gạch chân (MES, Minitab, OEE, LOTO...) để tra cứu • Bật 🎯 Chế độ Luyện Phỏng Vấn ở trên để ẩn đáp án & tự kiểm tra!\n"
        )
        tb.insert("end", mode_hint, "subtext")
        tb.insert("end", "─" * 88 + "\n", "divider")

        type_tag_map = {
            "Tình Huống Thực Chiến": "badge_peach",
            "Khái Niệm Cốt Lõi": "badge_mauve",
            "Phân Tích Sâu": "badge_blue",
            "General": "badge_sub"
        }

        for idx, (qid, item) in enumerate(filtered, 1):
            q_text = item.get("question", "")
            q_type = item.get("type", "General")
            q_cat = item.get("category", "")
            key_points = item.get("key_points", "")
            st = self._interview_progress.get(qid, "")

            badge_tag = type_tag_map.get(q_type, "badge_mauve")
            tb.insert("end", f"#{idx} [{q_type}]", badge_tag)
            if q_cat:
                tb.insert("end", f"   📌 {q_cat}", "badge_green")
            if st == "mastered":
                tb.insert("end", "   ✅ ĐÃ THUỘC", "iv_status_ok")
            elif st == "review":
                tb.insert("end", "   🔁 CẦN ÔN LẠI", "iv_status_rev")
            tb.insert("end", "\n", "normal")

            insert_with_glossary(tb, q_text + "\n", "q_title")

            # Hàng nút tương tác nhanh cho từng câu hỏi
            tb.insert("end", "   ", "normal")
            if self._quiz_mode:
                is_open = qid in self._revealed_qids
                btn_lbl = " 🙈 Ẩn gợi ý " if is_open else " 👁️ Xem gợi ý trả lời "
                tb.insert("end", btn_lbl, ("iv_toggle_btn", "iv_action", f"iv_reveal::{qid}"))
                tb.insert("end", "   ", "normal")

            ok_tag = "iv_ok_btn" if st == "mastered" else "iv_dim_btn"
            rev_tag = "iv_rev_btn" if st == "review" else "iv_dim_btn"
            tb.insert("end", " ✅ Đã thuộc ", (ok_tag, "iv_action", f"iv_mark::{qid}::mastered"))
            tb.insert("end", "  ", "normal")
            tb.insert("end", " 🔁 Cần ôn lại ", (rev_tag, "iv_action", f"iv_mark::{qid}::review"))
            tb.insert("end", "\n", "normal")

            if (not self._quiz_mode) or (qid in self._revealed_qids):
                tb.insert("end", "💡 Gợi ý trả lời & Điểm mấu chốt:\n", "ans_header")
                insert_with_glossary(tb, key_points + "\n", "ans_body")

            tb.insert("end", "─" * 88 + "\n", "divider")

        tb.tag_raise("term_link")
        tb.tag_raise("term_link_bold")
        tb.tag_raise("iv_action")
        tb.tag_raise("sel")
        if saved_yview is not None:
            tb.yview_moveto(saved_yview[0])
        else:
            tb.see("1.0")
        tb.configure(state="disabled")

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

        if term_glossary:
            msg.append(f"\n📖 Kho Từ Điển Thuật Ngữ Offline: {len(term_glossary.get_all_terms())} thuật ngữ (202/202 làm sâu)")
        if oe_curriculum:
            mods = len(oe_curriculum.get_all_modules())
            less = len(oe_curriculum.get_all_lessons())
            msg.append(f"🎓 Giáo Trình OE A–Z: {mods} Học phần / {less} Bài học tuần tự")
        if cadivi_factory_flows:
            msg.append(
                f"🏭 Dòng Chảy CADIVI: {len(cadivi_factory_flows.get_stations())} Trạm · "
                f"{len(cadivi_factory_flows.get_product_flows())} Luồng SP · "
                f"{len(cadivi_factory_flows.get_scenarios())} Tình Huống OE"
            )

        messagebox.showinfo("Thống Kê JobDetail Hub", "\n".join(msg))


def main():
    app = JobDetailApp()
    app.mainloop()


if __name__ == "__main__":
    main()
