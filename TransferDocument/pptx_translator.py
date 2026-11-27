# -*- coding: utf-8 -*-
"""
Module: pptx_translator.py
Dịch file .pptx ở mức XML (OOXML) bằng lxml:
1. Quét đầy đủ: Slides (slide*.xml), Notes (notesSlide*.xml), Bảng (a:tbl), Nhóm hình (p:grpSp),
   SmartArt / Diagram (ppt/diagrams/data*.xml), Biểu đồ (ppt/charts/chart*.xml).
2. Gộp run <a:r> cùng định dạng (màu, đậm, nghiêng, gạch chân, cỡ chữ) để dịch nguyên câu
   và giữ nguyên màu nhấn mạnh; tự động chèn dấu cách giữa 2 run khác màu khi dịch sang ngôn ngữ có dấu cách.
3. Ép toàn bộ font sang target_font (a:latin, a:ea, a:cs, defRPr, endParaRPr, theme*.xml)
   và đặt locale (vi-VN, ja-JP, en-US, zh-CN, ko-KR) -> không lỗi ô vuông (□).
4. Bật normAutofit chống tràn khung slide và giữ nguyên 100% hình ảnh, màu nền, hiệu ứng.
"""

import os
import re
import zipfile
from typing import Callable, Dict, List, Optional, Tuple
from lxml import etree

from language_config import get_default_font, get_target_locale, is_space_delimited
from translator_engine import DocumentTranslator, needs_translation, RE_CJK

A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
A = f"{{{A_NS}}}"


def _set_font_on_arpr(rpr: etree._Element, target_font: str, target_locale: str):
    rpr.set("lang", target_locale)
    for tag in (f"{A}latin", f"{A}ea", f"{A}cs"):
        el = rpr.find(tag)
        if el is None:
            el = etree.SubElement(rpr, tag)
        el.set("typeface", target_font)
        # Xóa charset/pitchFamily cũ có thể gây ép font Nhật/Trung
        for drop_attr in ("charset", "pitchFamily"):
            if drop_attr in el.attrib:
                del el.attrib[drop_attr]


def _force_font_pptx(root: etree._Element, target_font: str, target_locale: str, auto_fit: bool = True):
    for tag in (f"{A}rPr", f"{A}defRPr", f"{A}endParaRPr"):
        for rpr in root.iter(tag):
            _set_font_on_arpr(rpr, target_font, target_locale)

    for run in root.iter(f"{A}r"):
        if run.find(f"{A}t") is not None:
            rpr = run.find(f"{A}rPr")
            if rpr is None:
                rpr = etree.Element(f"{A}rPr")
                run.insert(0, rpr)
            _set_font_on_arpr(rpr, target_font, target_locale)

    if auto_fit:
        for body_pr in root.iter(f"{A}bodyPr"):
            no_af = body_pr.find(f"{A}noAutofit")
            if no_af is not None:
                body_pr.remove(no_af)
            if body_pr.find(f"{A}spAutoFit") is None and body_pr.find(f"{A}normAutofit") is None:
                norm = etree.SubElement(body_pr, f"{A}normAutofit")
                norm.set("fontScale", "80000")
                norm.set("lnSpcReduction", "10000")


def _force_font_theme(root: etree._Element, target_font: str):
    for tag in (f"{A}latin", f"{A}ea", f"{A}cs"):
        for el in root.iter(tag):
            if el.get("typeface") is not None:
                el.set("typeface", target_font)
    for el in root.iter(f"{A}font"):
        if el.get("typeface") is not None:
            el.set("typeface", target_font)


def _arun_format_signature(run: etree._Element) -> Tuple:
    rpr = run.find(f"{A}rPr")
    if rpr is None:
        return ()
    solid = rpr.find(f"{A}solidFill")
    col = etree.tostring(solid, encoding="unicode") if solid is not None else None
    hl = rpr.find(f"{A}highlight")
    hl_s = etree.tostring(hl, encoding="unicode") if hl is not None else None
    return (
        rpr.get("b"),
        rpr.get("i"),
        rpr.get("u"),
        rpr.get("strike"),
        rpr.get("sz"),
        col,
        hl_s,
    )


def _collect_pptx_segments(root: etree._Element) -> List[Tuple[List[etree._Element], str]]:
    """Gộp các <a:r> liên tiếp có cùng màu/đậm/nghiêng/cỡ chữ trong mỗi <a:p>."""
    segments: List[Tuple[List[etree._Element], str]] = []
    for p in root.iter(f"{A}p"):
        cur_runs: List[etree._Element] = []
        cur_sig = None

        def flush():
            nonlocal cur_runs, cur_sig
            if cur_runs:
                combined = "".join((r.find(f"{A}t").text or "") for r in cur_runs if r.find(f"{A}t") is not None)
                if combined.strip():
                    segments.append((list(cur_runs), combined))
            cur_runs = []
            cur_sig = None

        for child in p:
            if child.tag == f"{A}r" and child.find(f"{A}t") is not None:
                sig = _arun_format_signature(child)
                if cur_runs and sig != cur_sig:
                    flush()
                cur_runs.append(child)
                cur_sig = sig
            elif child.tag in (f"{A}br", f"{A}fld"):
                flush()
        flush()
    return segments


def _fix_pptx_spacing_and_punct(root: etree._Element, target_lang: str):
    """Chèn dấu cách giữa 2 run khác màu (khi ngôn ngữ đích có dấu cách) và chuẩn hóa dấu câu."""
    space_lang = is_space_delimited(target_lang)
    word_or_close = re.compile(r"[\w\)\]\}”\"%℃°.,;:!?]$", re.UNICODE)
    word_or_open = re.compile(r"^[\w\(\[\{“\"]", re.UNICODE)

    for p in root.iter(f"{A}p"):
        t_list = [r.find(f"{A}t") for r in p.findall(f"{A}r") if r.find(f"{A}t") is not None and (r.find(f"{A}t").text or "")]
        if not t_list:
            continue

        if space_lang:
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
                        t.text = re.sub(r" {2,}", " ", txt)

            for idx in range(len(t_list) - 1):
                lt = t_list[idx].text or ""
                rt = t_list[idx + 1].text or ""
                if not lt or not rt or lt[-1].isspace() or rt[0].isspace():
                    continue
                if rt[0] in ".,;:!?)]}”\"%°" or lt[-1] in "([{“\"/-–—":
                    continue
                if word_or_close.search(lt) and word_or_open.search(rt):
                    if lt[-1].isdigit() and rt[0].isdigit():
                        continue
                    t_list[idx].text = lt + " "


def translate_pptx(
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

    content_re = re.compile(
        r"^ppt/(slides/slide\d+|notesSlides/notesSlide\d+|diagrams/data\d+|charts/chart\d+)\.xml$",
        re.I,
    )
    parsed_parts: Dict[str, etree._Element] = {}
    segments: List[Tuple[List[etree._Element], str]] = []

    for name, data in entries.items():
        if content_re.match(name):
            root = etree.fromstring(data, parser=parser)
            parsed_parts[name] = root
            segments.extend(_collect_pptx_segments(root))

    raw_texts = [t for _, t in segments if needs_translation(t, translator.source_lang, translator.target_lang)]
    translator.log(
        f"📽 PPTX: tìm thấy {len(segments)} đoạn ({len(raw_texts)} đoạn cần dịch) "
        f"trên {len(parsed_parts)} phần XML (font: {font_name})."
    )
    trans_map = translator.translate_texts(raw_texts, progress_cb=progress_cb)

    replaced = 0
    for runs, txt in segments:
        vi = trans_map.get(txt)
        if vi:
            t0 = runs[0].find(f"{A}t")
            if t0 is not None:
                t0.text = vi
            for extra in runs[1:]:
                et = extra.find(f"{A}t")
                if et is not None:
                    et.text = ""
            replaced += 1

    for name, root in parsed_parts.items():
        _fix_pptx_spacing_and_punct(root, translator.target_lang)
        _force_font_pptx(root, font_name, locale, auto_fit=auto_fit_layout)
        entries[name] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

    for name in list(entries.keys()):
        if name.lower().startswith("ppt/theme/") and name.lower().endswith(".xml"):
            troot = etree.fromstring(entries[name], parser=parser)
            _force_font_theme(troot, font_name)
            entries[name] = etree.tostring(troot, xml_declaration=True, encoding="UTF-8", standalone=True)

    media_count = sum(1 for n in entries if n.startswith("ppt/media/"))
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for name, data in entries.items():
            zout.writestr(name, data)

    return {
        "input": input_path,
        "output": output_path,
        "segments_total": len(segments),
        "segments_translated": replaced,
        "media_preserved": media_count,
        "font_used": font_name,
    }
