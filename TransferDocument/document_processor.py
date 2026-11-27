# -*- coding: utf-8 -*-
"""
Module: document_processor.py
Bộ điều phối dịch chung cho mọi định dạng:
.doc, .docx, .xls, .xlsx, .ppt, .pptx, .pdf -> Đa ngôn ngữ đích & Font tương ứng.
"""

import os
import shutil
import tempfile
from typing import Callable, Dict, Optional

from language_config import get_default_font, get_target_suffix
from office_converter import convert_legacy_to_modern, export_to_pdf, SUPPORTED_EXTS, LEGACY_EXT_MAP
from translator_engine import DocumentTranslator
from docx_translator import translate_docx
from xlsx_translator import translate_xlsx
from pptx_translator import translate_pptx
from pdf_translator import translate_pdf


def _resolve_writable_output_path(path: str) -> str:
    """Nếu file đích đang bị Word/Excel/PDF viewer khóa (PermissionError), tự đổi sang _v2, _v3..."""
    if not os.path.exists(path):
        return path
    try:
        with open(path, "ab"):
            return path
    except PermissionError:
        stem, ext = os.path.splitext(path)
        for n in range(2, 100):
            cand = f"{stem}_v{n}{ext}"
            if not os.path.exists(cand):
                return cand
            try:
                with open(cand, "ab"):
                    return cand
            except PermissionError:
                continue
        raise


def build_output_path(input_path: str, output_dir: str, suffix: str = "_VI") -> str:
    """Tạo đường dẫn file đầu ra (định dạng cũ .doc/.xls/.ppt sẽ xuất ra .docx/.xlsx/.pptx)."""
    base = os.path.basename(input_path)
    stem, ext = os.path.splitext(base)
    low_ext = ext.lower()
    out_ext = LEGACY_EXT_MAP.get(low_ext, low_ext)
    os.makedirs(output_dir, exist_ok=True)
    raw_path = os.path.join(output_dir, f"{stem}{suffix}{out_ext}")
    return _resolve_writable_output_path(raw_path)


def process_document(
    input_path: str,
    output_dir: str,
    translator: DocumentTranslator,
    target_font: Optional[str] = None,
    suffix: Optional[str] = None,
    auto_fit_layout: bool = True,
    merge_broken_paragraphs: bool = True,
    also_export_pdf: bool = False,
    progress_cb: Optional[Callable[[int, int, str], None]] = None,
) -> Dict:
    """
    Xử lý dịch 1 tài liệu Office hoặc PDF hoàn chỉnh:
    1. Nếu là định dạng cũ (.doc, .xls, .ppt) -> chuyển đổi tạm sang OOXML qua Office COM.
    2. Dịch ở mức XML (Word/Excel/PowerPoint) hoặc Redact+Overlay Font Unicode (PDF).
    3. Tùy chọn xuất thêm bản PDF preview (với Office).
    4. Dọn sạch file tạm sau khi xong.
    """
    abs_in = os.path.abspath(input_path)
    if not os.path.exists(abs_in):
        raise FileNotFoundError(f"Không tìm thấy file: {abs_in}")

    ext = os.path.splitext(abs_in)[1].lower()
    if ext not in SUPPORTED_EXTS:
        raise ValueError(f"Định dạng chưa hỗ trợ: {ext} (hỗ trợ: {', '.join(sorted(SUPPORTED_EXTS))})")

    eff_suffix = suffix if suffix is not None else get_target_suffix(translator.target_lang)
    eff_font = target_font or get_default_font(translator.target_lang)
    out_path = build_output_path(abs_in, output_dir, suffix=eff_suffix)
    temp_dir = None

    try:
        work_input = abs_in
        if ext in LEGACY_EXT_MAP:
            temp_dir = tempfile.mkdtemp(prefix="td_office_")
            translator.log(f"🔄 Đang chuyển đổi {os.path.basename(abs_in)} ({ext} -> {LEGACY_EXT_MAP[ext]}) bằng MS Office...")
            work_input, _ = convert_legacy_to_modern(abs_in, work_dir=temp_dir)

        modern_ext = os.path.splitext(work_input)[1].lower()
        if modern_ext == ".docx":
            stats = translate_docx(
                work_input, out_path, translator,
                target_font=eff_font,
                auto_fit_layout=auto_fit_layout,
                merge_broken_paragraphs=merge_broken_paragraphs,
                progress_cb=progress_cb,
            )
        elif modern_ext == ".xlsx":
            stats = translate_xlsx(
                work_input, out_path, translator,
                target_font=eff_font,
                auto_fit_layout=auto_fit_layout,
                progress_cb=progress_cb,
            )
        elif modern_ext == ".pptx":
            stats = translate_pptx(
                work_input, out_path, translator,
                target_font=eff_font,
                auto_fit_layout=auto_fit_layout,
                progress_cb=progress_cb,
            )
        elif modern_ext == ".pdf":
            stats = translate_pdf(
                work_input, out_path, translator,
                target_font=eff_font,
                auto_fit_layout=auto_fit_layout,
                progress_cb=progress_cb,
            )
        else:
            raise ValueError(f"Định dạng không hợp lệ: {modern_ext}")

        stats["original_input"] = abs_in
        stats["output"] = out_path

        if also_export_pdf and modern_ext != ".pdf" and not translator.stop_check():
            translator.log(f"📑 Đang xuất thêm PDF: {os.path.basename(out_path)}...")
            pdf_out = export_to_pdf(out_path)
            stats["pdf_output"] = pdf_out

        return stats
    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)
