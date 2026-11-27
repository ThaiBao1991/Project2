# -*- coding: utf-8 -*-
"""
Module: xlsx_translator.py
Dịch file .xlsx ở mức XML (OOXML) bằng lxml để:
1. Giữ nguyên 100% công thức, màu nền (fills), viền (borders), ô gộp (mergeCells),
   hình ảnh (xl/media/*, xl/drawings/*), định dạng số, độ rộng cột, thiết lập in ấn.
2. LOẠI BỎ TRIỆT ĐỂ thẻ phiên âm Furigana Nhật (<rPh>, <phoneticPr>) trong sharedStrings.xml
   và inlineStr -> không bao giờ bị dính Katakana thừa vào tiếng Việt.
3. Dịch cả TextBox / Shape bên trong xl/drawings/drawing*.xml.
4. Ép toàn bộ font trong xl/styles.xml, sharedStrings.xml, theme1.xml và drawings sang Arial,
   xóa <charset> (tránh mã 128 Shift-JIS gây ô vuông) và <scheme>.
5. Bảo toàn kết cấu bố cục Excel:
   - TUYỆT ĐỐI KHÔNG tự ép wrapText lên các ô tiêu đề nổi (borderId=0) vốn cần tràn ngang tự nhiên.
   - Đổi textRotation="255" (xếp chữ dọc kiểu Nhật) -> "90" (xoay 90° đọc mượt tiếng Việt).
   - Tự động tính & nới chiều cao hàng hợp lý cho hàng tiêu đề xoay dọc (textRotation=90)
     và các ô đã bật wrapText để không bị cắt chữ theo chiều dọc.
"""

import math
import os
import re
import zipfile
from typing import Callable, Dict, List, Optional, Tuple
from lxml import etree

from language_config import get_default_font, get_target_locale
from translator_engine import DocumentTranslator, needs_translation

S_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"

S = f"{{{S_NS}}}"
A = f"{{{A_NS}}}"
XML_SPACE = f"{{{XML_NS}}}space"


def _strip_phonetics(elem: etree._Element):
    for tag in (f"{S}rPh", f"{S}phoneticPr"):
        for node in list(elem.findall(tag)):
            elem.remove(node)


def _force_font_on_xl_rpr(rpr: etree._Element, target_font: str = "Arial"):
    rfont = rpr.find(f"{S}rFont")
    if rfont is None:
        rfont = etree.SubElement(rpr, f"{S}rFont")
    rfont.set("val", target_font)
    for drop_tag in (f"{S}scheme", f"{S}charset"):
        for node in list(rpr.findall(drop_tag)):
            rpr.remove(node)


def _extract_style_meta(styles_root: etree._Element) -> Dict[int, Dict]:
    """Trích xuất metadata từng style xf (font_size, wrapText, textRotation, borderId)."""
    font_sizes: List[float] = []
    fonts = styles_root.find(f"{S}fonts")
    if fonts is not None:
        for font in fonts.findall(f"{S}font"):
            sz_el = font.find(f"{S}sz")
            try:
                font_sizes.append(float(sz_el.get("val", "10")) if sz_el is not None else 10.0)
            except ValueError:
                font_sizes.append(10.0)

    meta: Dict[int, Dict] = {}
    cell_xfs = styles_root.find(f"{S}cellXfs")
    if cell_xfs is not None:
        for idx, xf in enumerate(cell_xfs.findall(f"{S}xf")):
            try:
                fid = int(xf.get("fontId", "0"))
            except ValueError:
                fid = 0
            fsz = font_sizes[fid] if 0 <= fid < len(font_sizes) else 10.0
            al = xf.find(f"{S}alignment")
            wrap = al.get("wrapText") == "1" if al is not None else False
            rot = 0
            if al is not None and al.get("textRotation"):
                try:
                    rot = int(al.get("textRotation"))
                except ValueError:
                    rot = 0
            border_id = xf.get("borderId", "0")
            meta[idx] = {
                "font_size": fsz,
                "wrap": wrap,
                "rot": rot,
                "has_border": border_id != "0",
            }
    return meta


def _force_font_in_styles(root: etree._Element, target_font: str = "Arial", target_lang: str = "vi"):
    """
    Đổi toàn bộ font trong xl/styles.xml sang target_font, xóa charset/scheme.
    Chuyển textRotation="255" -> "90" khi ngôn ngữ đích không phải Nhật/Trung.
    KHÔNG tự ép wrapText lên các ô không có wrapText ban đầu (giữ nguyên bố cục tiêu đề nổi).
    """
    fonts = root.find(f"{S}fonts")
    if fonts is not None:
        for font in fonts.findall(f"{S}font"):
            name_el = font.find(f"{S}name")
            if name_el is None:
                name_el = etree.SubElement(font, f"{S}name")
            name_el.set("val", target_font)
            for drop_tag in (f"{S}scheme", f"{S}charset"):
                for node in list(font.findall(drop_tag)):
                    font.remove(node)

    if target_lang not in ("ja", "zh"):
        cell_xfs = root.find(f"{S}cellXfs")
        if cell_xfs is not None:
            for xf in cell_xfs.findall(f"{S}xf"):
                align = xf.find(f"{S}alignment")
                if align is not None and align.get("textRotation") == "255":
                    align.set("textRotation", "90")
                    xf.set("applyAlignment", "1")


def _force_font_in_theme(root: etree._Element, target_font: str = "Arial"):
    for tag in (f"{A}latin", f"{A}ea", f"{A}cs"):
        for el in root.iter(tag):
            if el.get("typeface") is not None:
                el.set("typeface", target_font)
    for el in root.iter(f"{A}font"):
        if el.get("typeface") is not None:
            el.set("typeface", target_font)


def _force_font_in_drawing(root: etree._Element, target_font: str = "Arial", target_locale: str = "vi-VN", auto_fit: bool = True):
    for rpr in root.iter(f"{A}rPr"):
        for tag in (f"{A}latin", f"{A}ea", f"{A}cs"):
            el = rpr.find(tag)
            if el is None:
                el = etree.SubElement(rpr, tag)
            el.set("typeface", target_font)
        rpr.set("lang", target_locale)

    if auto_fit:
        for body_pr in root.iter(f"{A}bodyPr"):
            no_af = body_pr.find(f"{A}noAutofit")
            if no_af is not None:
                body_pr.remove(no_af)
            if body_pr.find(f"{A}spAutoFit") is None and body_pr.find(f"{A}normAutofit") is None:
                norm = etree.SubElement(body_pr, f"{A}normAutofit")
                norm.set("fontScale", "85000")


def _extract_si_text_and_mode(si: etree._Element) -> Tuple[str, str]:
    _strip_phonetics(si)
    runs = si.findall(f"{S}r")
    if runs:
        parts = []
        for r in runs:
            t = r.find(f"{S}t")
            if t is not None and t.text:
                parts.append(t.text)
        return "".join(parts), "rich"
    t = si.find(f"{S}t")
    return (t.text or "") if t is not None else "", "plain"


def _apply_si_translation(si: etree._Element, translated: str, mode: str, target_font: str = "Arial"):
    _strip_phonetics(si)
    if mode == "rich":
        runs = si.findall(f"{S}r")
        if runs:
            r0 = runs[0]
            rpr = r0.find(f"{S}rPr")
            if rpr is None:
                rpr = etree.Element(f"{S}rPr")
                r0.insert(0, rpr)
            _force_font_on_xl_rpr(rpr, target_font)
            t0 = r0.find(f"{S}t")
            if t0 is None:
                t0 = etree.SubElement(r0, f"{S}t")
            t0.text = translated
            t0.set(XML_SPACE, "preserve")
            for extra_r in runs[1:]:
                si.remove(extra_r)
            return
    t = si.find(f"{S}t")
    if t is None:
        t = etree.SubElement(si, f"{S}t")
    t.text = translated
    t.set(XML_SPACE, "preserve")


def _parse_vertical_merged_cells(sheet_root: etree._Element) -> set:
    """Trả về tập tọa độ ô (vd 'B8', 'B9'...) thuộc ô merge nhiều hàng theo chiều dọc."""
    vmerged_cells = set()
    merges = sheet_root.find(f"{S}mergeCells")
    if merges is None:
        return vmerged_cells
    ref_re = re.compile(r"^([A-Z]+)(\d+):([A-Z]+)(\d+)$")
    for mc in merges.findall(f"{S}mergeCell"):
        m = ref_re.match(mc.get("ref", ""))
        if m:
            c1, r1, c2, r2 = m.group(1), int(m.group(2)), m.group(3), int(m.group(4))
            if r2 > r1 and c1 == c2:
                for r in range(r1, r2 + 1):
                    vmerged_cells.add(f"{c1}{r}")
    return vmerged_cells


def _adjust_row_heights_in_sheet(
    sheet_root: etree._Element,
    ss_texts: Dict[int, str],
    style_meta: Dict[int, Dict],
):
    """
    Điều chỉnh chiều cao hàng thông minh, tôn trọng tuyệt đối bố cục & mergeCells:
    1. Hàng có ô xoay dọc (textRotation == 90): tính chiều cao cần thiết theo độ dài chuỗi tiếng Việt
       để tiêu đề dọc không bao giờ bị cắt mất chữ (như 'hiển vi đo lường').
    2. Hàng có ô ĐÃ BẬT wrapText="1" ban đầu (và có viền bảng): nới nhẹ nếu chữ xuống nhiều dòng.
    3. KHÔNG ĐỤNG tới các hàng tiêu đề nổi không viền / không wrapText (như '[Phụ bảng 1]...', '(4) Đo bước').
    """
    sheet_data = sheet_root.find(f"{S}sheetData")
    if sheet_data is None:
        return

    vmerged_cells = _parse_vertical_merged_cells(sheet_root)

    for row in sheet_data.findall(f"{S}row"):
        ht_str = row.get("ht")
        try:
            orig_ht = float(ht_str) if ht_str else 0.0
        except ValueError:
            orig_ht = 0.0

        needed_ht = orig_ht
        for c in row.findall(f"{S}c"):
            cell_ref = c.get("r", "")
            s_idx = int(c.get("s")) if c.get("s", "").isdigit() else 0
            smeta = style_meta.get(s_idx, {})
            rot = smeta.get("rot", 0)
            is_wrap = smeta.get("wrap", False)
            has_border = smeta.get("has_border", False)
            fsz = smeta.get("font_size", 10.0)

            txt = ""
            ctype = c.get("t")
            if ctype == "s":
                v = c.find(f"{S}v")
                if v is not None and v.text and v.text.isdigit():
                    txt = ss_texts.get(int(v.text), "")
            elif ctype == "inlineStr":
                is_el = c.find(f"{S}is")
                if is_el is not None:
                    txt = "".join(t.text or "" for t in is_el.iter(f"{S}t"))

            if not txt.strip():
                continue

            # Trường hợp 1: Tiêu đề xoay dọc 90° (textRotation=90)
            if rot in (90, 180, 255):
                lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
                longest = max((len(ln) for ln in lines), default=len(txt))
                if is_wrap and len(lines) == 1 and longest > 24:
                    eff_chars = math.ceil(longest * 0.62)
                else:
                    eff_chars = longest
                est_ht = eff_chars * (fsz * 0.58) + 20.0
                est_ht = min(240.0, est_ht)
                if est_ht > needed_ht:
                    needed_ht = est_ht

            # Trường hợp 2: Ô bình thường ĐÃ BẬT wrapText và nằm trong bảng có viền (bản thân ô này không bị merge dọc)
            elif is_wrap and has_border and cell_ref not in vmerged_cells:
                lines = txt.splitlines()
                est_lines = sum(max(1, math.ceil(len(ln) / 26)) for ln in lines)
                if est_lines >= 2:
                    base_ht = orig_ht if orig_ht > 0 else (fsz * 1.45)
                    est_ht = min(max(base_ht * 2.2, 48.0), est_lines * (fsz * 1.45) + 6.0)
                    if est_ht > needed_ht:
                        needed_ht = est_ht

        if needed_ht > orig_ht + 1.5:
            row.set("ht", f"{needed_ht:.1f}")
            row.set("customHeight", "1")


def translate_xlsx(
    input_path: str,
    output_path: str,
    translator: DocumentTranslator,
    target_font: Optional[str] = None,
    auto_fit_layout: bool = True,
    progress_cb: Optional[Callable[[int, int, str], None]] = None,
) -> Dict:
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    parser = etree.XMLParser(remove_blank_text=False, recover=True)

    font_name = target_font or get_default_font(translator.target_lang)
    locale = get_target_locale(translator.target_lang)

    with zipfile.ZipFile(input_path, "r") as zin:
        entries = {name: zin.read(name) for name in zin.namelist()}

    # 0. Chuẩn hóa styles.xml & lấy metadata (font size, wrap, textRotation, border)
    style_meta: Dict[int, Dict] = {}
    if "xl/styles.xml" in entries:
        st_root = etree.fromstring(entries["xl/styles.xml"], parser=parser)
        _force_font_in_styles(st_root, font_name, translator.target_lang)
        style_meta = _extract_style_meta(st_root)
        entries["xl/styles.xml"] = etree.tostring(
            st_root, xml_declaration=True, encoding="UTF-8", standalone=True
        )

    # 1. Thu thập chuỗi từ sharedStrings.xml
    ss_root = None
    ss_items: List[Tuple[int, etree._Element, str, str]] = []
    if "xl/sharedStrings.xml" in entries:
        ss_root = etree.fromstring(entries["xl/sharedStrings.xml"], parser=parser)
        for idx, si in enumerate(ss_root.findall(f"{S}si")):
            txt, mode = _extract_si_text_and_mode(si)
            ss_items.append((idx, si, txt, mode))

    # 2. Thu thập inlineStr từ các worksheet
    sheet_roots: Dict[str, etree._Element] = {}
    inline_items: List[Tuple[etree._Element, str, str]] = []
    sheet_re = re.compile(r"^xl/worksheets/sheet\d+\.xml$", re.I)
    for name, data in entries.items():
        if sheet_re.match(name):
            sroot = etree.fromstring(data, parser=parser)
            sheet_roots[name] = sroot
            for c in sroot.iter(f"{S}c"):
                if c.get("t") == "inlineStr":
                    is_el = c.find(f"{S}is")
                    if is_el is not None:
                        txt, mode = _extract_si_text_and_mode(is_el)
                        inline_items.append((is_el, txt, mode))

    # 3. Thu thập văn bản trong Drawing / TextBox
    drawing_roots: Dict[str, etree._Element] = {}
    drawing_paras: List[Tuple[List[etree._Element], str]] = []
    drawing_re = re.compile(r"^xl/drawings/drawing\d+\.xml$", re.I)
    for name, data in entries.items():
        if drawing_re.match(name):
            droot = etree.fromstring(data, parser=parser)
            drawing_roots[name] = droot
            for p in droot.iter(f"{A}p"):
                runs = p.findall(f"{A}r")
                if runs:
                    combined = "".join((r.find(f"{A}t").text or "") for r in runs if r.find(f"{A}t") is not None)
                    if combined.strip():
                        drawing_paras.append((runs, combined))

    # 4. Dịch toàn bộ văn bản
    raw_texts: List[str] = []
    for _, _, txt, _ in ss_items:
        if needs_translation(txt, translator.source_lang, translator.target_lang):
            raw_texts.append(txt)
    for _, txt, _ in inline_items:
        if needs_translation(txt, translator.source_lang, translator.target_lang):
            raw_texts.append(txt)
    for _, txt in drawing_paras:
        if needs_translation(txt, translator.source_lang, translator.target_lang):
            raw_texts.append(txt)

    translator.log(
        f"📊 XLSX: tìm thấy {len(ss_items)} sharedStrings, {len(inline_items)} inlineStr, "
        f"{len(drawing_paras)} textbox ({len(raw_texts)} mục cần dịch, font: {font_name})."
    )

    trans_map = translator.translate_texts(raw_texts, progress_cb=progress_cb)

    # 5. Áp bản dịch vào sharedStrings
    translated_count = 0
    ss_final_texts: Dict[int, str] = {}
    if ss_root is not None:
        for idx, si, txt, mode in ss_items:
            vi = trans_map.get(txt)
            if vi:
                _apply_si_translation(si, vi, mode, target_font=font_name)
                ss_final_texts[idx] = vi
                translated_count += 1
            else:
                ss_final_texts[idx] = txt
                if mode == "rich":
                    for r in si.findall(f"{S}r"):
                        rpr = r.find(f"{S}rPr")
                        if rpr is not None:
                            _force_font_on_xl_rpr(rpr, font_name)
        entries["xl/sharedStrings.xml"] = etree.tostring(
            ss_root, xml_declaration=True, encoding="UTF-8", standalone=True
        )

    # 6. Áp bản dịch vào inlineStr & tinh chỉnh chiều cao hàng xoay dọc / bảng wrap
    for is_el, txt, mode in inline_items:
        vi = trans_map.get(txt)
        if vi:
            _apply_si_translation(is_el, vi, mode, target_font=font_name)
            translated_count += 1

    for name, sroot in sheet_roots.items():
        if auto_fit_layout:
            _adjust_row_heights_in_sheet(sroot, ss_final_texts, style_meta)
        entries[name] = etree.tostring(sroot, xml_declaration=True, encoding="UTF-8", standalone=True)

    # 7. Áp bản dịch vào Drawings / TextBox
    for runs, txt in drawing_paras:
        vi = trans_map.get(txt)
        if vi:
            t0 = runs[0].find(f"{A}t")
            if t0 is not None:
                t0.text = vi
            for extra_r in runs[1:]:
                et = extra_r.find(f"{A}t")
                if et is not None:
                    et.text = ""
            translated_count += 1

    for name, droot in drawing_roots.items():
        _force_font_in_drawing(droot, font_name, locale, auto_fit=auto_fit_layout)
        entries[name] = etree.tostring(droot, xml_declaration=True, encoding="UTF-8", standalone=True)

    # 8. Theme -> target_font
    for name in list(entries.keys()):
        if name.lower().startswith("xl/theme/") and name.lower().endswith(".xml"):
            troot = etree.fromstring(entries[name], parser=parser)
            _force_font_in_theme(troot, font_name)
            entries[name] = etree.tostring(troot, xml_declaration=True, encoding="UTF-8", standalone=True)

    # 9. Ghi file .xlsx mới
    media_count = sum(1 for n in entries if n.startswith("xl/media/"))
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for name, data in entries.items():
            zout.writestr(name, data)

    return {
        "input": input_path,
        "output": output_path,
        "items_total": len(ss_items) + len(inline_items) + len(drawing_paras),
        "items_translated": translated_count,
        "media_preserved": media_count,
        "font_used": font_name,
    }
