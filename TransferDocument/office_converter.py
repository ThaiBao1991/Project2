# -*- coding: utf-8 -*-
"""
Module: office_converter.py
Chuyển đổi định dạng Office cũ (.doc, .xls, .ppt) sang OOXML (.docx, .xlsx, .pptx)
và hỗ trợ xuất PDF preview thông qua Microsoft Office COM (win32com.client).
"""

import os
import shutil
import tempfile
from typing import Optional, Tuple

LEGACY_EXT_MAP = {
    ".doc": ".docx",
    ".xls": ".xlsx",
    ".ppt": ".pptx",
}

MODERN_EXTS = {".docx", ".xlsx", ".pptx"}
PDF_EXTS = {".pdf"}
SUPPORTED_EXTS = set(LEGACY_EXT_MAP.keys()) | MODERN_EXTS | PDF_EXTS


def _init_com():
    import pythoncom
    pythoncom.CoInitialize()


def _uninit_com():
    try:
        import pythoncom
        pythoncom.CoUninitialize()
    except Exception:
        pass


def convert_legacy_to_modern(input_path: str, work_dir: Optional[str] = None) -> Tuple[str, bool]:
    """
    Chuyển .doc -> .docx, .xls -> .xlsx, .ppt -> .pptx bằng MS Office COM.
    Trả về (modern_path, is_temp_converted).
    Nếu file đã là .docx/.xlsx/.pptx thì trả về chính input_path và False.
    """
    abs_in = os.path.abspath(input_path)
    ext = os.path.splitext(abs_in)[1].lower()

    if ext in MODERN_EXTS:
        return abs_in, False

    if ext not in LEGACY_EXT_MAP:
        raise ValueError(f"Định dạng không được hỗ trợ: {ext}")

    target_ext = LEGACY_EXT_MAP[ext]
    out_dir = work_dir or tempfile.mkdtemp(prefix="td_conv_")
    os.makedirs(out_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(abs_in))[0]
    out_path = os.path.abspath(os.path.join(out_dir, f"{stem}{target_ext}"))

    import win32com.client

    _init_com()
    try:
        if ext == ".doc":
            word = win32com.client.DispatchEx("Word.Application")
            word.Visible = False
            word.DisplayAlerts = 0
            doc = None
            try:
                doc = word.Documents.Open(abs_in, ConfirmConversions=False, ReadOnly=True, AddToRecentFiles=False)
                # 16 = wdFormatXMLDocument (.docx)
                doc.SaveAs2(out_path, FileFormat=16)
            finally:
                if doc is not None:
                    try:
                        doc.Close(False)
                    except Exception:
                        pass
                try:
                    word.Quit()
                except Exception:
                    pass

        elif ext == ".xls":
            excel = win32com.client.DispatchEx("Excel.Application")
            excel.Visible = False
            excel.DisplayAlerts = False
            wb = None
            try:
                wb = excel.Workbooks.Open(abs_in, UpdateLinks=0, ReadOnly=True)
                # 51 = xlOpenXMLWorkbook (.xlsx)
                wb.SaveAs(out_path, FileFormat=51)
            finally:
                if wb is not None:
                    try:
                        wb.Close(False)
                    except Exception:
                        pass
                try:
                    excel.Quit()
                except Exception:
                    pass

        elif ext == ".ppt":
            ppt = win32com.client.DispatchEx("PowerPoint.Application")
            pres = None
            try:
                pres = ppt.Presentations.Open(abs_in, ReadOnly=True, Untitled=False, WithWindow=False)
                # 24 = ppSaveAsOpenXMLPresentation (.pptx)
                pres.SaveAs(out_path, FileFormat=24)
            finally:
                if pres is not None:
                    try:
                        pres.Close()
                    except Exception:
                        pass
                try:
                    ppt.Quit()
                except Exception:
                    pass
    finally:
        _uninit_com()

    if not os.path.exists(out_path):
        raise RuntimeError(f"Chuyển đổi {ext} sang {target_ext} thất bại cho file: {abs_in}")

    return out_path, True


def export_to_pdf(input_path: str, pdf_path: Optional[str] = None) -> str:
    """Xuất file Word/Excel/PowerPoint sang PDF bằng MS Office COM."""
    abs_in = os.path.abspath(input_path)
    ext = os.path.splitext(abs_in)[1].lower()
    if pdf_path is None:
        pdf_path = os.path.splitext(abs_in)[0] + ".pdf"
    abs_pdf = os.path.abspath(pdf_path)

    import win32com.client

    _init_com()
    try:
        if ext in (".docx", ".doc"):
            word = win32com.client.DispatchEx("Word.Application")
            word.Visible = False
            word.DisplayAlerts = 0
            doc = None
            try:
                doc = word.Documents.Open(abs_in, ConfirmConversions=False, ReadOnly=True, AddToRecentFiles=False)
                # 17 = wdFormatPDF
                doc.SaveAs2(abs_pdf, FileFormat=17)
            finally:
                if doc is not None:
                    try:
                        doc.Close(False)
                    except Exception:
                        pass
                try:
                    word.Quit()
                except Exception:
                    pass
        elif ext in (".xlsx", ".xls"):
            excel = win32com.client.DispatchEx("Excel.Application")
            excel.Visible = False
            excel.DisplayAlerts = False
            wb = None
            try:
                wb = excel.Workbooks.Open(abs_in, UpdateLinks=0, ReadOnly=True)
                # 0 = xlTypePDF
                wb.ExportAsFixedFormat(0, abs_pdf)
            finally:
                if wb is not None:
                    try:
                        wb.Close(False)
                    except Exception:
                        pass
                try:
                    excel.Quit()
                except Exception:
                    pass
        elif ext in (".pptx", ".ppt"):
            ppt = win32com.client.DispatchEx("PowerPoint.Application")
            pres = None
            try:
                pres = ppt.Presentations.Open(abs_in, ReadOnly=True, Untitled=False, WithWindow=False)
                # 32 = ppSaveAsPDF
                pres.SaveAs(abs_pdf, FileFormat=32)
            finally:
                if pres is not None:
                    try:
                        pres.Close()
                    except Exception:
                        pass
                try:
                    ppt.Quit()
                except Exception:
                    pass
        else:
            raise ValueError(f"Không hỗ trợ xuất PDF cho định dạng: {ext}")
    finally:
        _uninit_com()

    return abs_pdf


def verify_office_file_opens(file_path: str) -> Tuple[bool, str]:
    """Mở thử file bằng Word/Excel/PowerPoint COM hoặc PyMuPDF để xác nhận hợp lệ 100%."""
    abs_in = os.path.abspath(file_path)
    ext = os.path.splitext(abs_in)[1].lower()
    if ext == ".pdf":
        try:
            import pymupdf
            doc = pymupdf.open(abs_in)
            pages = len(doc)
            imgs = sum(len(p.get_images(full=False)) for p in doc)
            doc.close()
            return True, f"PDF OK (pages={pages}, images={imgs})"
        except Exception as e:
            return False, f"PDF open error: {e}"
    import win32com.client

    _init_com()
    try:
        if ext in (".docx", ".doc"):
            word = win32com.client.DispatchEx("Word.Application")
            word.Visible = False
            word.DisplayAlerts = 0
            doc = None
            try:
                doc = word.Documents.Open(abs_in, ConfirmConversions=False, ReadOnly=True, AddToRecentFiles=False)
                pages = doc.ComputeStatistics(2)  # wdStatisticPages
                tables = doc.Tables.Count
                shapes = doc.Shapes.Count
                inline_shapes = doc.InlineShapes.Count
                return True, f"Word OK (pages={pages}, tables={tables}, shapes={shapes}, inline_images={inline_shapes})"
            finally:
                if doc is not None:
                    try:
                        doc.Close(False)
                    except Exception:
                        pass
                try:
                    word.Quit()
                except Exception:
                    pass
        elif ext in (".xlsx", ".xls"):
            excel = win32com.client.DispatchEx("Excel.Application")
            excel.Visible = False
            excel.DisplayAlerts = False
            wb = None
            try:
                wb = excel.Workbooks.Open(abs_in, UpdateLinks=0, ReadOnly=True)
                sheets = wb.Sheets.Count
                return True, f"Excel OK (sheets={sheets})"
            finally:
                if wb is not None:
                    try:
                        wb.Close(False)
                    except Exception:
                        pass
                try:
                    excel.Quit()
                except Exception:
                    pass
        elif ext in (".pptx", ".ppt"):
            ppt = win32com.client.DispatchEx("PowerPoint.Application")
            pres = None
            try:
                pres = ppt.Presentations.Open(abs_in, ReadOnly=True, Untitled=False, WithWindow=False)
                slides = pres.Slides.Count
                return True, f"PowerPoint OK (slides={slides})"
            finally:
                if pres is not None:
                    try:
                        pres.Close()
                    except Exception:
                        pass
                try:
                    ppt.Quit()
                except Exception:
                    pass
        return False, f"Unsupported extension: {ext}"
    except Exception as e:
        return False, f"COM open error: {e}"
    finally:
        _uninit_com()
