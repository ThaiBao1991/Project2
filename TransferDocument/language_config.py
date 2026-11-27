# -*- coding: utf-8 -*-
"""
Module: language_config.py
Cấu hình đa ngôn ngữ Nguồn <-> Đích, ánh xạ Font hệ thống Windows (.ttf/.ttc),
Locale XML (vi-VN, ja-JP, en-US, zh-CN, ko-KR) và hậu tố tên file.
"""

import os
from typing import Dict, List, Optional, Tuple

WINDOWS_FONTS_DIR = r"C:\Windows\Fonts"

# Danh sách ngôn ngữ nguồn (hiển thị -> mã)
SOURCE_LANGUAGES: List[Tuple[str, str]] = [
    ("Tự động (Auto)", "auto"),
    ("Tiếng Việt (VI)", "vi"),
    ("Tiếng Nhật (JA)", "ja"),
    ("Tiếng Anh (EN)", "en"),
    ("Tiếng Trung (ZH)", "zh"),
    ("Tiếng Hàn (KO)", "ko"),
]

# Danh sách ngôn ngữ đích (hiển thị -> mã)
TARGET_LANGUAGES: List[Tuple[str, str]] = [
    ("Tiếng Việt (VI)", "vi"),
    ("Tiếng Nhật (JA)", "ja"),
    ("Tiếng Anh (EN)", "en"),
    ("Tiếng Trung (ZH)", "zh"),
    ("Tiếng Hàn (KO)", "ko"),
]

# Metadata từng ngôn ngữ đích
TARGET_LANG_META: Dict[str, Dict] = {
    "vi": {
        "name": "Tiếng Việt",
        "locale": "vi-VN",
        "suffix": "_VI",
        "default_font": "Arial",
        "recommended_fonts": ["Arial", "Times New Roman", "Calibri", "Tahoma", "Segoe UI"],
        "space_delimited": True,
    },
    "en": {
        "name": "Tiếng Anh",
        "locale": "en-US",
        "suffix": "_EN",
        "default_font": "Arial",
        "recommended_fonts": ["Arial", "Calibri", "Times New Roman", "Segoe UI", "Tahoma"],
        "space_delimited": True,
    },
    "ja": {
        "name": "Tiếng Nhật",
        "locale": "ja-JP",
        "suffix": "_JA",
        "default_font": "Yu Gothic",
        "recommended_fonts": ["Yu Gothic", "Meiryo", "MS Gothic", "MS Mincho"],
        "space_delimited": False,
    },
    "zh": {
        "name": "Tiếng Trung (Giản thể)",
        "locale": "zh-CN",
        "suffix": "_ZH",
        "default_font": "Microsoft YaHei",
        "recommended_fonts": ["Microsoft YaHei", "SimSun"],
        "space_delimited": False,
    },
    "ko": {
        "name": "Tiếng Hàn",
        "locale": "ko-KR",
        "suffix": "_KO",
        "default_font": "Malgun Gothic",
        "recommended_fonts": ["Malgun Gothic"],
        "space_delimited": True,
    },
}

# Ánh xạ tên Font -> file font thực tế trên Windows (regular, bold, italic) dùng cho PDF PyMuPDF
FONT_FILE_MAP: Dict[str, Dict[str, List[str]]] = {
    "Arial": {
        "regular": ["arial.ttf"],
        "bold": ["arialbd.ttf", "arial.ttf"],
        "italic": ["ariali.ttf", "arial.ttf"],
        "bold_italic": ["arialbi.ttf", "arialbd.ttf", "arial.ttf"],
    },
    "Times New Roman": {
        "regular": ["times.ttf"],
        "bold": ["timesbd.ttf", "times.ttf"],
        "italic": ["timesi.ttf", "times.ttf"],
        "bold_italic": ["timesbi.ttf", "timesbd.ttf", "times.ttf"],
    },
    "Calibri": {
        "regular": ["calibri.ttf"],
        "bold": ["calibrib.ttf", "calibri.ttf"],
        "italic": ["calibrii.ttf", "calibri.ttf"],
        "bold_italic": ["calibriz.ttf", "calibrib.ttf", "calibri.ttf"],
    },
    "Tahoma": {
        "regular": ["tahoma.ttf"],
        "bold": ["tahomabd.ttf", "tahoma.ttf"],
        "italic": ["tahoma.ttf"],
        "bold_italic": ["tahomabd.ttf", "tahoma.ttf"],
    },
    "Segoe UI": {
        "regular": ["segoeui.ttf"],
        "bold": ["segoeuib.ttf", "segoeui.ttf"],
        "italic": ["segoeuii.ttf", "segoeui.ttf"],
        "bold_italic": ["segoeuiz.ttf", "segoeuib.ttf", "segoeui.ttf"],
    },
    "Yu Gothic": {
        "regular": ["YuGothR.ttc", "YuGothM.ttc", "meiryo.ttc", "msgothic.ttc"],
        "bold": ["YuGothB.ttc", "YuGothR.ttc", "meiryob.ttc", "msgothic.ttc"],
        "italic": ["YuGothR.ttc", "meiryo.ttc"],
        "bold_italic": ["YuGothB.ttc", "YuGothR.ttc"],
    },
    "Meiryo": {
        "regular": ["meiryo.ttc", "YuGothR.ttc", "msgothic.ttc"],
        "bold": ["meiryob.ttc", "meiryo.ttc"],
        "italic": ["meiryo.ttc"],
        "bold_italic": ["meiryob.ttc", "meiryo.ttc"],
    },
    "MS Gothic": {
        "regular": ["msgothic.ttc", "YuGothR.ttc"],
        "bold": ["msgothic.ttc", "YuGothB.ttc"],
        "italic": ["msgothic.ttc"],
        "bold_italic": ["msgothic.ttc"],
    },
    "MS Mincho": {
        "regular": ["msmincho.ttc", "YuGothR.ttc"],
        "bold": ["msmincho.ttc"],
        "italic": ["msmincho.ttc"],
        "bold_italic": ["msmincho.ttc"],
    },
    "Microsoft YaHei": {
        "regular": ["msyh.ttc", "simsun.ttc"],
        "bold": ["msyhbd.ttc", "msyh.ttc"],
        "italic": ["msyh.ttc"],
        "bold_italic": ["msyhbd.ttc", "msyh.ttc"],
    },
    "SimSun": {
        "regular": ["simsun.ttc", "msyh.ttc"],
        "bold": ["simsun.ttc", "msyhbd.ttc"],
        "italic": ["simsun.ttc"],
        "bold_italic": ["simsun.ttc"],
    },
    "Malgun Gothic": {
        "regular": ["malgun.ttf"],
        "bold": ["malgunbd.ttf", "malgun.ttf"],
        "italic": ["malgun.ttf"],
        "bold_italic": ["malgunbd.ttf", "malgun.ttf"],
    },
}

ALL_FONT_NAMES: List[str] = list(FONT_FILE_MAP.keys())


def get_lang_meta(target_lang: str) -> Dict:
    return TARGET_LANG_META.get((target_lang or "vi").lower(), TARGET_LANG_META["vi"])


def get_default_font(target_lang: str) -> str:
    return get_lang_meta(target_lang)["default_font"]


def get_recommended_fonts(target_lang: str) -> List[str]:
    rec = list(get_lang_meta(target_lang)["recommended_fonts"])
    # Đưa các font gợi ý lên đầu, vẫn kèm các font khác phía sau để user linh hoạt
    for f in ALL_FONT_NAMES:
        if f not in rec:
            rec.append(f)
    return rec


def get_target_locale(target_lang: str) -> str:
    return get_lang_meta(target_lang)["locale"]


def get_target_suffix(target_lang: str) -> str:
    return get_lang_meta(target_lang)["suffix"]


def is_space_delimited(target_lang: str) -> bool:
    return bool(get_lang_meta(target_lang).get("space_delimited", True))


def resolve_font_file(font_name: str, bold: bool = False, italic: bool = False) -> Optional[str]:
    """Tìm đường dẫn tuyệt đối file .ttf/.ttc trên Windows tương ứng với font & kiểu chữ."""
    entry = FONT_FILE_MAP.get(font_name) or FONT_FILE_MAP["Arial"]
    if bold and italic:
        key = "bold_italic"
    elif bold:
        key = "bold"
    elif italic:
        key = "italic"
    else:
        key = "regular"

    for fname in entry.get(key, []) + entry.get("regular", []):
        full = os.path.join(WINDOWS_FONTS_DIR, fname)
        if os.path.exists(full):
            return full

    # Fallback cuối cùng về Arial
    fallback = os.path.join(WINDOWS_FONTS_DIR, "arial.ttf")
    return fallback if os.path.exists(fallback) else None
