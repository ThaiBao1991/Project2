# -*- coding: utf-8 -*-
"""
Module: docx_translator.py
Dịch file .docx ở mức XML (OOXML) bằng lxml:
1. Giữ nguyên 100% bố cục, màu sắc, bảng biểu, hình ảnh (word/media/*, w:drawing, w:pict),
   header, footer, footnotes, endnotes, TextBox / Shape (DrawingML wps:txbx & VML v:textbox).
2. Tự động gộp các đoạn văn bị tác giả Nhật bấm Enter ngắt dòng giữa câu (kèm dòng trống đệm)
   trước khi dịch -> hết xuống dòng vô lý & dịch nguyên câu tự nhiên.
3. Gộp các run <w:r> liên tiếp cùng định dạng; tự động chèn dấu cách tại ranh giới 2 run khác màu
   và chuẩn hóa dấu câu full-width Nhật (。 -> ., 、 -> ,).
4. Ép toàn bộ font sang Arial (ascii, hAnsi, eastAsia, cs + gỡ theme font Nhật/Trung/Hàn),
   gỡ thẻ kéo dãn chữ ngang (<w:w>, <w:fitText>, <w:spacing> giãn rộng) -> không lỗi ô vuông hay bẹt chữ.
5. Chống cắt/gãy chữ trong ô bảng hẹp & TextBox:
   - Thu gọn lề trong ô hẹp (tcMar), nới nhẹ cột nhãn hẹp theo đúng lưới tblGrid (bảo toàn 100% merge & tổng rộng bảng),
     co nhẹ cỡ chữ ô hẹp để không gãy từng chữ cái (M/ã, Tr/an).
   - Đổi trHeight exact -> atLeast, bật normAutofit cho TextBox/Shape.
"""

import os
import re
import zipfile
from typing import Callable, Dict, List, Optional, Tuple
from lxml import etree

from language_config import get_default_font, get_target_locale, is_space_delimited
from translator_engine import DocumentTranslator, needs_translation, RE_CJK

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
WPS_NS = "http://schemas.microsoft.com/office/word/2010/wordprocessingShape"
V_NS = "urn:schemas-microsoft-com:vml"
XML_NS = "http://www.w3.org/XML/1998/namespace"

W = f"{{{W_NS}}}"
A = f"{{{A_NS}}}"
WPS = f"{{{WPS_NS}}}"
V = f"{{{V_NS}}}"
XML_SPACE = f"{{{XML_NS}}}space"

INLINE_CONTAINERS = {
    f"{W}hyperlink",
    f"{W}ins",
    f"{W}smartTag",
    f"{W}sdt",
    f"{W}sdtContent",
    f"{W}fldSimple",
}

NON_TEXT_RUN_CHILDREN = {
    f"{W}drawing",
    f"{W}pict",
    f"{W}object",
    f"{W}br",
    f"{W}cr",
    f"{W}tab",
    f"{W}ptab",
    f"{W}fldChar",
    f"{W}instrText",
    f"{W}sym",
    f"{W}footnoteReference",
    f"{W}endnoteReference",
    f"{W}commentReference",
    f"{W}pgNum",
}

IGNORABLE_RUN_CHILDREN = {
    f"{W}rPr",
    f"{W}lastRenderedPageBreak",
    f"{W}noBreakHyphen",
    f"{W}softHyphen",
}

THEME_FONT_ATTRS = (
    f"{W}asciiTheme",
    f"{W}hAnsiTheme",
    f"{W}eastAsiaTheme",
    f"{W}cstheme",
)

# Dấu kết thúc câu hoàn chỉnh (nếu đoạn kết thúc bằng dấu này thì KHÔNG gộp với đoạn sau)
SENTENCE_END_CHARS = set("。.!！?？:：;；)）]】」』")

# Regex nhận diện đoạn bắt đầu 1 mục mới / ghi chú / danh sách (KHÔNG gộp vào đoạn trước)
RE_NEW_ITEM_START = re.compile(
    r"^[\s\u3000]*("
    r"\d+[\.\)．、]|"
    r"[\(（]\d+[\)）]|"
    r"[①-⑳]|"
    r"[a-zA-Z][\.\)]|"
    r"[・•▪■□●○◎△▲※★☆\-–—]|"
    r"(?:注|備考|例|参考|付図|付表|表|図|第\d|Ghi chú|Lưu ý|Ví dụ|Phụ lục|Bảng|Hình)"
    r")"
)


def _set_font_on_rpr(rpr: etree._Element, target_font: str = "Arial", target_locale: str = "vi-VN", clean_stretch: bool = True):
    """Ép font đích toàn diện, gỡ theme font, gỡ kéo dãn ngang và đặt ngôn ngữ tương ứng."""
    rfonts = rpr.find(f"{W}rFonts")
    if rfonts is None:
        rfonts = etree.Element(f"{W}rFonts")
        rpr.insert(0, rfonts)
    for attr in THEME_FONT_ATTRS:
        if attr in rfonts.attrib:
            del rfonts.attrib[attr]
    rfonts.set(f"{W}ascii", target_font)
    rfonts.set(f"{W}hAnsi", target_font)
    rfonts.set(f"{W}eastAsia", target_font)
    rfonts.set(f"{W}cs", target_font)

    if clean_stretch:
        for drop_tag in (f"{W}w", f"{W}fitText"):
            for node in list(rpr.findall(drop_tag)):
                rpr.remove(node)
        for sp in list(rpr.findall(f"{W}spacing")):
            try:
                val = int(sp.get(f"{W}val", "0"))
                if val > 20 or val < -10:
                    rpr.remove(sp)
            except ValueError:
                rpr.remove(sp)

    lang = rpr.find(f"{W}lang")
    if lang is not None:
        lang.set(f"{W}val", target_locale)
        lang.set(f"{W}eastAsia", target_locale)


def _force_font_in_xml(root: etree._Element, target_font: str = "Arial", target_locale: str = "vi-VN"):
    for rpr in root.iter(f"{W}rPr"):
        _set_font_on_rpr(rpr, target_font, target_locale, clean_stretch=True)
    for run in root.iter(f"{W}r"):
        if run.find(f"{W}t") is not None:
            rpr = run.find(f"{W}rPr")
            if rpr is None:
                rpr = etree.Element(f"{W}rPr")
                run.insert(0, rpr)
            _set_font_on_rpr(rpr, target_font, target_locale, clean_stretch=True)


def _force_font_in_theme(root: etree._Element, target_font: str = "Arial"):
    for tag in (f"{A}latin", f"{A}ea", f"{A}cs"):
        for el in root.iter(tag):
            if el.get("typeface") is not None:
                el.set("typeface", target_font)
    for el in root.iter(f"{A}font"):
        if el.get("typeface") is not None:
            el.set("typeface", target_font)


def _force_font_in_styles(root: etree._Element, target_font: str = "Arial", target_locale: str = "vi-VN"):
    doc_defaults = root.find(f"{W}docDefaults")
    if doc_defaults is not None:
        rpr_def = doc_defaults.find(f"{W}rPrDefault")
        if rpr_def is None:
            rpr_def = etree.SubElement(doc_defaults, f"{W}rPrDefault")
        rpr = rpr_def.find(f"{W}rPr")
        if rpr is None:
            rpr = etree.SubElement(rpr_def, f"{W}rPr")
        _set_font_on_rpr(rpr, target_font, target_locale, clean_stretch=False)

    for rpr in root.iter(f"{W}rPr"):
        _set_font_on_rpr(rpr, target_font, target_locale, clean_stretch=False)


def _fix_layout_anti_clipping(root: etree._Element):
    """Chống cắt/mất chữ trong hàng bảng và TextBox/Shape."""
    for tr_h in root.iter(f"{W}trHeight"):
        if tr_h.get(f"{W}hRule") == "exact":
            tr_h.set(f"{W}hRule", "atLeast")

    for body_pr in list(root.iter(f"{WPS}bodyPr")) + list(root.iter(f"{A}bodyPr")):
        no_af = body_pr.find(f"{A}noAutofit")
        sp_af = body_pr.find(f"{A}spAutoFit")
        norm_af = body_pr.find(f"{A}normAutofit")
        if no_af is not None:
            body_pr.remove(no_af)
            if sp_af is None and norm_af is None:
                norm = etree.Element(f"{A}normAutofit")
                norm.set("fontScale", "85000")
                norm.set("lnSpcReduction", "10000")
                body_pr.append(norm)
        elif sp_af is None and norm_af is None:
            norm = etree.Element(f"{A}normAutofit")
            norm.set("fontScale", "85000")
            norm.set("lnSpcReduction", "10000")
            body_pr.append(norm)

    for vtb in root.iter(f"{V}textbox"):
        style = vtb.get("style", "")
        if "mso-fit-shape-to-text" not in style:
            sep = ";" if style and not style.strip().endswith(";") else ""
            vtb.set("style", f"{style}{sep}mso-fit-shape-to-text:t")


def _get_cell_width_dxa(tc: etree._Element) -> Optional[int]:
    tcPr = tc.find(f"{W}tcPr")
    if tcPr is None:
        return None
    tcW = tcPr.find(f"{W}tcW")
    if tcW is None:
        return None
    if tcW.get(f"{W}type", "dxa") not in ("dxa", ""):
        return None
    try:
        return int(tcW.get(f"{W}w", "0"))
    except ValueError:
        return None


def _get_cell_grid_span(tc: etree._Element) -> int:
    tcPr = tc.find(f"{W}tcPr")
    if tcPr is None:
        return 1
    gs = tcPr.find(f"{W}gridSpan")
    if gs is None:
        return 1
    try:
        return max(1, int(gs.get(f"{W}val", "1")))
    except ValueError:
        return 1


def _set_cell_tight_margins(tc: etree._Element, lr_dxa: int = 20):
    """Thu gọn lề trái/phải của ô hẹp để tăng tối đa chiều rộng hiển thị chữ."""
    tcPr = tc.find(f"{W}tcPr")
    if tcPr is None:
        tcPr = etree.Element(f"{W}tcPr")
        tc.insert(0, tcPr)
    tcMar = tcPr.find(f"{W}tcMar")
    if tcMar is None:
        tcMar = etree.SubElement(tcPr, f"{W}tcMar")
    for side in ("left", "right"):
        el = tcMar.find(f"{W}{side}")
        if el is None:
            el = etree.SubElement(tcMar, f"{W}{side}")
        el.set(f"{W}w", str(lr_dxa))
        el.set(f"{W}type", "dxa")


def _shrink_cell_font(tc: etree._Element, max_sz_half_pt: int = 16):
    """Giảm nhẹ cỡ chữ trong các ô cực hẹp (vd 16 = 8pt) để chữ không bị gãy từng ký tự."""
    for run in tc.iter(f"{W}r"):
        if run.find(f"{W}t") is None:
            continue
        rpr = run.find(f"{W}rPr")
        if rpr is None:
            rpr = etree.Element(f"{W}rPr")
            run.insert(0, rpr)
        for sz_tag in (f"{W}sz", f"{W}szCs"):
            sz = rpr.find(sz_tag)
            if sz is None:
                sz = etree.SubElement(rpr, sz_tag)
                sz.set(f"{W}val", str(max_sz_half_pt))
            else:
                try:
                    cur = int(sz.get(f"{W}val", "20"))
                    if cur > max_sz_half_pt:
                        sz.set(f"{W}val", str(max_sz_half_pt))
                except ValueError:
                    pass


def _optimize_narrow_table_cells(root: etree._Element):
    """
    Khắc phục lỗi ô nhãn quá hẹp trong biểu mẫu Nhật (vd: 番号 218 dxa, 符号 227 dxa, 頁 227 dxa):
    1. Thu nhỏ lề trái/phải (tcMar=20 dxa) cho mọi ô hẹp (< 750 dxa).
    2. Nếu bảng có lưới cột rõ ràng (tblGrid) và 1 cột nhãn đơn cực hẹp (< 620 dxa) nằm cạnh 1 cột rộng (> 1100 dxa),
       mượn an toàn một phần độ rộng (giữ nguyên 100% tổng chiều rộng bảng & không phá vỡ ô merge!).
    3. Co nhẹ cỡ chữ trong ô hẹp (xuống 7.5–8.5pt) nếu chữ dài hơn chiều rộng khả dụng.
    """
    for tbl in root.iter(f"{W}tbl"):
        rows = tbl.findall(f"{W}tr")
        tbl_grid = tbl.find(f"{W}tblGrid")
        grid_cols = tbl_grid.findall(f"{W}gridCol") if tbl_grid is not None else []

        # Bước 1: Tính toán xem cột đơn nào có nhãn hẹp cần nới
        if grid_cols and rows:
            num_cols = len(grid_cols)
            col_widths = []
            valid_grid = True
            for gc in grid_cols:
                try:
                    col_widths.append(int(gc.get(f"{W}w", "0")))
                except ValueError:
                    valid_grid = False
                    break

            if valid_grid and len(col_widths) == num_cols:
                # Bản đồ cell theo (row_idx, start_col, span)
                row_maps: List[List[Tuple[etree._Element, int, int]]] = []
                for tr in rows:
                    cur_c = 0
                    rmap = []
                    for tc in tr.findall(f"{W}tc"):
                        sp = _get_cell_grid_span(tc)
                        rmap.append((tc, cur_c, sp))
                        cur_c += sp
                    row_maps.append(rmap)

                # Xác định nhu cầu nới cho từng cột đơn hẹp
                col_need = [0] * num_cols
                for rmap in row_maps:
                    for tc, sc, sp in rmap:
                        if sp == 1 and sc < num_cols:
                            w = col_widths[sc]
                            txt = "".join(t.text or "" for t in tc.iter(f"{W}t")).strip()
                            if 0 < w < 650 and txt and len(txt) >= 2:
                                # Cần ít nhất ~560-720 dxa cho "Mã số", "Ký hiệu", "Trang"
                                longest_word = max((len(wd) for wd in txt.split()), default=len(txt))
                                target = min(760, max(540, longest_word * 110 + 120))
                                if target > w:
                                    col_need[sc] = max(col_need[sc], target - w)

                # Mượn an toàn từ cột lân cận rộng (ưu tiên cột phải hoặc cột trái rộng >= 1000 dxa)
                deltas = [0] * num_cols
                for c in range(num_cols):
                    need = col_need[c]
                    if need <= 0:
                        continue
                    # Kiểm tra xem có thể dịch ranh giới trái hoặc phải mà không cắt ngang cell nào
                    donor = None
                    # Thử mượn từ cột bên phải (c+1) hoặc bên trái (c-1) hoặc cột đầu rộng nhất
                    candidates = []
                    if c + 1 < num_cols and col_widths[c + 1] + deltas[c + 1] >= 900:
                        candidates.append(c + 1)
                    if c - 1 >= 0 and col_widths[c - 1] + deltas[c - 1] >= 1200:
                        candidates.append(c - 1)
                    # Nếu hai cột kề đều hẹp (vd ô 'Trang' cạnh '2/14'), mượn từ cột rộng nhất trong bảng (>= 2000 dxa)
                    if not candidates:
                        wide_cols = [idx for idx in range(num_cols) if idx != c and col_widths[idx] + deltas[idx] >= 2000]
                        if wide_cols:
                            candidates.append(max(wide_cols, key=lambda idx: col_widths[idx] + deltas[idx]))
                    if candidates:
                        donor = max(candidates, key=lambda idx: col_widths[idx] + deltas[idx])
                    if donor is not None:
                        avail = max(0, (col_widths[donor] + deltas[donor]) - 750)
                        take = min(need, avail, 380)
                        if take >= 60:
                            deltas[c] += take
                            deltas[donor] -= take

                # Áp dụng deltas đồng bộ lên cả tblGrid và từng tcW (bảo toàn 100% tổng chiều rộng & merge!)
                if any(d != 0 for d in deltas):
                    for c, d in enumerate(deltas):
                        if d != 0:
                            grid_cols[c].set(f"{W}w", str(col_widths[c] + d))
                    for rmap in row_maps:
                        for tc, sc, sp in rmap:
                            cell_delta = sum(deltas[sc:min(sc + sp, num_cols)])
                            if cell_delta != 0:
                                cur_w = _get_cell_width_dxa(tc)
                                if cur_w is not None and cur_w + cell_delta > 100:
                                    tc.find(f"{W}tcPr").find(f"{W}tcW").set(f"{W}w", str(cur_w + cell_delta))

        # Bước 2: Thu gọn lề trong & co nhẹ cỡ chữ cho các ô vẫn còn hẹp
        for tr in rows:
            for tc in tr.findall(f"{W}tc"):
                w = _get_cell_width_dxa(tc)
                if w is None or w <= 0:
                    continue
                txt = "".join(t.text or "" for t in tc.iter(f"{W}t")).strip()
                if not txt:
                    continue
                if w < 850:
                    _set_cell_tight_margins(tc, lr_dxa=20)
                    longest_word = max((len(wd) for wd in txt.split()), default=len(txt))
                    # Ước lượng chiều rộng cần cho 1 từ dài nhất ở 10pt (~110 dxa/ký tự)
                    if longest_word * 105 > (w - 40):
                        target_half_pt = 15 if w < 520 else 16  # 7.5pt hoặc 8pt
                        _shrink_cell_font(tc, max_sz_half_pt=target_half_pt)


def _run_format_signature(run: etree._Element) -> Tuple:
    rpr = run.find(f"{W}rPr")
    if rpr is None:
        return ()

    def _on(tag: str) -> bool:
        el = rpr.find(f"{W}{tag}")
        if el is None:
            return False
        val = el.get(f"{W}val")
        return val not in ("0", "false", "none")

    color_el = rpr.find(f"{W}color")
    color = color_el.get(f"{W}val") if color_el is not None else None

    hl_el = rpr.find(f"{W}highlight")
    hl = hl_el.get(f"{W}val") if hl_el is not None else None

    shd_el = rpr.find(f"{W}shd")
    shd = shd_el.get(f"{W}fill") if shd_el is not None else None

    u_el = rpr.find(f"{W}u")
    u_val = u_el.get(f"{W}val") if u_el is not None else None
    if u_val == "none":
        u_val = None

    va_el = rpr.find(f"{W}vertAlign")
    va = va_el.get(f"{W}val") if va_el is not None else None

    return (_on("b"), _on("i"), _on("strike"), color, hl, shd, u_val, va)


def _is_pure_text_run(run: etree._Element) -> bool:
    has_text = False
    for child in run:
        tag = child.tag
        if tag in IGNORABLE_RUN_CHILDREN:
            continue
        if tag == f"{W}t":
            has_text = True
            continue
        if tag in NON_TEXT_RUN_CHILDREN or tag != f"{W}t":
            return False
    return has_text


def _has_translatable_t(run: etree._Element) -> bool:
    if run.find(f"{W}instrText") is not None:
        return False
    for t in run.findall(f"{W}t"):
        if t.text and t.text.strip():
            return True
    return False


def _get_run_text(run: etree._Element) -> str:
    return "".join(t.text or "" for t in run.findall(f"{W}t"))


def _paragraph_plain_text(p: etree._Element) -> str:
    parts = []
    for child in p:
        if child.tag == f"{W}r":
            parts.append(_get_run_text(child))
        elif child.tag in INLINE_CONTAINERS:
            for r in child.findall(f"{W}r"):
                parts.append(_get_run_text(r))
    return "".join(parts)


def _paragraph_has_non_text_objects(p: etree._Element) -> bool:
    """Kiểm tra đoạn có chứa ảnh, shape, pageBreak, field, tab hay không (nếu có thì KHÔNG gộp)."""
    for child in p:
        if child.tag == f"{W}pPr":
            if child.find(f"{W}pageBreakBefore") is not None or child.find(f"{W}sectPr") is not None:
                return True
            if child.find(f"{W}numPr") is not None:
                return True
            continue
        if child.tag == f"{W}r":
            for rc in child:
                if rc.tag in NON_TEXT_RUN_CHILDREN:
                    return True
        elif child.tag not in INLINE_CONTAINERS and child.tag not in (
            f"{W}bookmarkStart", f"{W}bookmarkEnd", f"{W}proofErr"
        ):
            return True
    return False


def _paragraph_dominant_color(p: etree._Element) -> Optional[str]:
    for r in p.findall(f"{W}r"):
        if _get_run_text(r).strip():
            rpr = r.find(f"{W}rPr")
            if rpr is not None:
                c = rpr.find(f"{W}color")
                if c is not None:
                    return c.get(f"{W}val")
            return None
    return None


def _merge_broken_paragraphs_in_container(container: etree._Element) -> int:
    """
    Gộp các đoạn <w:p> bị tác giả Nhật bấm Enter ngắt dòng giữa câu (kể cả khi có 1 đoạn trống đệm ở giữa).
    Giữ nguyên tuyệt đối: tiêu đề ngắn, mục đánh số, ghi chú, đoạn chứa hình ảnh/tab/pageBreak, đoạn khác màu.
    """
    merged_count = 0
    children = list(container)
    i = 0
    while i < len(children):
        el = children[i]
        if el.tag != f"{W}p":
            i += 1
            continue

        txt_a = _paragraph_plain_text(el).strip()
        if not txt_a or _paragraph_has_non_text_objects(el):
            i += 1
            continue

        # Chỉ gộp khi đoạn A đủ dài (tránh gộp nhầm tiêu đề ngắn) và chưa kết thúc câu
        is_cjk = bool(RE_CJK.search(txt_a))
        min_len = 16 if is_cjk else 35
        if len(txt_a) < min_len or txt_a[-1] in SENTENCE_END_CHARS:
            i += 1
            continue

        # Tìm đoạn tiếp theo (cho phép bỏ qua tối đa 1 đoạn trống thuần túy làm dòng đệm)
        j = i + 1
        spacer_idx = None
        if j < len(children) and children[j].tag == f"{W}p":
            if not _paragraph_plain_text(children[j]).strip() and not _paragraph_has_non_text_objects(children[j]):
                spacer_idx = j
                j += 1

        if j >= len(children) or children[j].tag != f"{W}p":
            i += 1
            continue

        next_p = children[j]
        txt_b = _paragraph_plain_text(next_p).strip()
        if not txt_b or _paragraph_has_non_text_objects(next_p):
            i += 1
            continue

        # Không gộp nếu đoạn B bắt đầu mục mới / danh sách / ghi chú
        if RE_NEW_ITEM_START.match(txt_b):
            i += 1
            continue

        # Chỉ gộp khi cùng màu chữ chủ đạo
        if _paragraph_dominant_color(el) != _paragraph_dominant_color(next_p):
            i += 1
            continue

        # Gộp các run của next_p vào cuối el (bỏ khoảng trắng dẫn đầu thừa của next_p)
        first_text_trimmed = False
        for child in list(next_p):
            if child.tag == f"{W}pPr":
                continue
            if child.tag == f"{W}r" and not first_text_trimmed:
                for t in child.findall(f"{W}t"):
                    if t.text:
                        stripped = t.text.lstrip(" \t\u3000")
                        if stripped != t.text:
                            t.text = stripped
                        if t.text:
                            first_text_trimmed = True
                            break
            el.append(child)

        # Xóa spacer (nếu có) và next_p khỏi container
        container.remove(next_p)
        if spacer_idx is not None:
            container.remove(children[spacer_idx])
        merged_count += 1
        # Refresh children và tiếp tục kiểm tra tại cùng vị trí i (trường hợp 1 câu bị bẻ thành 3 dòng)
        children = list(container)

    return merged_count


def _merge_broken_paragraphs(root: etree._Element) -> int:
    """Chạy gộp đoạn bị ngắt giữa câu trong body, từng ô bảng <w:tc>, và từng TextBox <w:txbxContent>."""
    total = 0
    for tag in (f"{W}body", f"{W}tc", f"{W}txbxContent"):
        for container in root.iter(tag):
            total += _merge_broken_paragraphs_in_container(container)
    return total


def _iter_inline_elements(parent: etree._Element):
    for child in parent:
        tag = child.tag
        if tag == f"{W}r":
            yield child
        elif tag in INLINE_CONTAINERS:
            yield from _iter_inline_elements(child)
        elif tag in (f"{W}del", f"{W}moveFrom"):
            continue
        else:
            if tag not in (f"{W}pPr", f"{W}bookmarkStart", f"{W}bookmarkEnd", f"{W}proofErr", f"{W}permStart", f"{W}permEnd"):
                yield None


def _collect_segments(root: etree._Element) -> List[Tuple[List[etree._Element], str]]:
    segments: List[Tuple[List[etree._Element], str]] = []
    for p in root.iter(f"{W}p"):
        cur_runs: List[etree._Element] = []
        cur_sig = None

        def flush():
            nonlocal cur_runs, cur_sig
            if cur_runs:
                combined = "".join(_get_run_text(r) for r in cur_runs)
                if combined.strip():
                    segments.append((list(cur_runs), combined))
            cur_runs = []
            cur_sig = None

        for node in _iter_inline_elements(p):
            if node is None:
                flush()
                continue
            if not _is_pure_text_run(node):
                flush()
                if _has_translatable_t(node):
                    mixed_text = _get_run_text(node)
                    if mixed_text.strip():
                        segments.append(([node], mixed_text))
                continue
            sig = _run_format_signature(node)
            if cur_runs and sig != cur_sig:
                flush()
            cur_runs.append(node)
            cur_sig = sig

        flush()
    return segments


def _apply_translation_to_runs(runs: List[etree._Element], translated: str):
    first_run = runs[0]
    t_nodes = first_run.findall(f"{W}t")
    if t_nodes:
        t0 = t_nodes[0]
        t0.text = translated
        t0.set(XML_SPACE, "preserve")
        for extra_t in t_nodes[1:]:
            extra_t.text = ""
    else:
        t0 = etree.SubElement(first_run, f"{W}t")
        t0.text = translated
        t0.set(XML_SPACE, "preserve")

    for r in runs[1:]:
        for t in r.findall(f"{W}t"):
            t.text = ""


def _fix_inter_segment_spacing_and_punct(root: etree._Element, target_lang: str = "vi"):
    """
    Khắc phục triệt để lỗi mất dấu cách giữa 2 đoạn khác màu/định dạng (Hình 2)
    và chuẩn hóa dấu câu full-width Nhật còn sót khi ngôn ngữ đích có dấu cách (vi/en/ko).
    """
    if not is_space_delimited(target_lang):
        return
    word_or_close = re.compile(r"[\w\)\]\}”\"%℃°.,;:!?]$", re.UNICODE)
    word_or_open = re.compile(r"^[\w\(\[\{“\"]", re.UNICODE)

    for p in root.iter(f"{W}p"):
        # Gom danh sách các <w:t> không rỗng theo thứ tự xuất hiện trong cùng cấp đoạn
        t_list: List[etree._Element] = []
        for node in _iter_inline_elements(p):
            if node is None:
                continue
            for t in node.findall(f"{W}t"):
                if t.text:
                    t_list.append(t)

        if not t_list:
            continue

        # 1. Chuẩn hóa dấu câu full-width Nhật trong đoạn đã dịch (không có ký tự CJK)
        full_txt = "".join(t.text or "" for t in t_list)
        if not RE_CJK.search(full_txt):
            for t in t_list:
                txt = t.text
                if any(ch in txt for ch in ("。", "、", "，", "：", "（", "）", "「", "」")):
                    txt = (
                        txt.replace("。", ".")
                        .replace("、", ",")
                        .replace("，", ", ")
                        .replace("：", ": ")
                        .replace("（", "(")
                        .replace("）", ")")
                        .replace("「", "“")
                        .replace("」", "”")
                    )
                    txt = re.sub(r" {2,}", " ", txt)
                    t.text = txt
                    t.set(XML_SPACE, "preserve")

        # 2. Chèn dấu cách giữa 2 <w:t> liền kề bị dính chữ do đổi màu/định dạng
        for idx in range(len(t_list) - 1):
            left_t = t_list[idx]
            right_t = t_list[idx + 1]
            lt = left_t.text or ""
            rt = right_t.text or ""
            if not lt or not rt:
                continue
            if lt[-1].isspace() or rt[0].isspace():
                continue
            # Tránh chèn space trước dấu chấm/phẩy/hai chấm hoặc sau dấu mở ngoặc
            if rt[0] in ".,;:!?)]}”\"%°":
                continue
            if lt[-1] in "([{“\"/-–—":
                continue
            if word_or_close.search(lt) and word_or_open.search(rt):
                # Nếu là hai số tách nhau như '20' + '26' hoặc mã 'B' + 'A-A1-08' thì không chèn
                if lt[-1].isdigit() and rt[0].isdigit():
                    continue
                if len(lt.strip()) == 1 and lt.strip().isupper() and rt.startswith(tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ-")):
                    continue
                left_t.text = lt + " "
                left_t.set(XML_SPACE, "preserve")


def translate_docx(
    input_path: str,
    output_path: str,
    translator: DocumentTranslator,
    target_font: Optional[str] = None,
    auto_fit_layout: bool = True,
    merge_broken_paragraphs: bool = True,
    progress_cb: Optional[Callable[[int, int, str], None]] = None,
) -> Dict:
    """
    Dịch toàn bộ file .docx -> output_path, giữ nguyên định dạng/màu sắc/hình ảnh,
    đổi font đích (target_font), gộp câu ngắt dòng thủ công, thêm space giữa các màu và tối ưu ô bảng hẹp.
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    parser = etree.XMLParser(remove_blank_text=False, recover=True)

    font_name = target_font or get_default_font(translator.target_lang)
    locale = get_target_locale(translator.target_lang)

    with zipfile.ZipFile(input_path, "r") as zin:
        entries = {name: zin.read(name) for name in zin.namelist()}

    content_part_re = re.compile(
        r"^word/(document|header\d*|footer\d*|footnotes|endnotes)\.xml$", re.I
    )
    parsed_parts: Dict[str, etree._Element] = {}
    all_segments: List[Tuple[List[etree._Element], str]] = []
    merged_total = 0

    for name, data in entries.items():
        if content_part_re.match(name):
            root = etree.fromstring(data, parser=parser)
            if merge_broken_paragraphs:
                merged_total += _merge_broken_paragraphs(root)
            parsed_parts[name] = root
            all_segments.extend(_collect_segments(root))

    if merged_total > 0:
        translator.log(f"🔗 Đã tự động gộp {merged_total} dòng bị ngắt giữa câu trước khi dịch.")

    raw_texts = [
        text for _, text in all_segments
        if needs_translation(text, translator.source_lang, translator.target_lang)
    ]
    translator.log(
        f"📄 DOCX: tìm thấy {len(all_segments)} đoạn văn bản ({len(raw_texts)} đoạn cần dịch) "
        f"trên {len(parsed_parts)} phần XML (font: {font_name})."
    )

    trans_map = translator.translate_texts(raw_texts, progress_cb=progress_cb)

    replaced_count = 0
    for runs, orig_text in all_segments:
        vi = trans_map.get(orig_text)
        if vi:
            _apply_translation_to_runs(runs, vi)
            replaced_count += 1

    for name, root in parsed_parts.items():
        _fix_inter_segment_spacing_and_punct(root, translator.target_lang)
        _force_font_in_xml(root, font_name, locale)
        if auto_fit_layout:
            _fix_layout_anti_clipping(root)
            _optimize_narrow_table_cells(root)
        entries[name] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

    for name in list(entries.keys()):
        low = name.lower()
        if low == "word/styles.xml":
            sroot = etree.fromstring(entries[name], parser=parser)
            _force_font_in_styles(sroot, font_name, locale)
            entries[name] = etree.tostring(sroot, xml_declaration=True, encoding="UTF-8", standalone=True)
        elif low == "word/numbering.xml":
            nroot = etree.fromstring(entries[name], parser=parser)
            _force_font_in_xml(nroot, font_name, locale)
            entries[name] = etree.tostring(nroot, xml_declaration=True, encoding="UTF-8", standalone=True)
        elif low.startswith("word/theme/") and low.endswith(".xml"):
            troot = etree.fromstring(entries[name], parser=parser)
            _force_font_in_theme(troot, font_name)
            entries[name] = etree.tostring(troot, xml_declaration=True, encoding="UTF-8", standalone=True)

    media_count = sum(1 for n in entries if n.startswith("word/media/"))
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for name, data in entries.items():
            zout.writestr(name, data)

    return {
        "input": input_path,
        "output": output_path,
        "segments_total": len(all_segments),
        "segments_translated": replaced_count,
        "paragraphs_merged": merged_total,
        "media_preserved": media_count,
        "font_used": font_name,
    }
