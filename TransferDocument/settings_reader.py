# -*- coding: utf-8 -*-
"""
Module: settings_reader.py
Đọc & giải mã danh sách Gemini API Keys từ AskCpl/settings.json
(hoặc file settings.json / config.json cục bộ).
"""

import base64
import json
import os
from typing import Dict, List, Optional

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Danh sách đường dẫn ứng viên tới settings.json chứa Gemini API keys
CANDIDATE_SETTINGS_PATHS = [
    os.path.join(BASE_DIR, "settings.json"),
    r"C:\Users\12953 Bao\Desktop\desktop\work\Project\Python\BasicLearnPython\W3schools\Python Tutorial\GravityCode\Download\AskCpl\settings.json",
    os.path.normpath(os.path.join(BASE_DIR, "..", "..", "Python Tutorial", "GravityCode", "Download", "AskCpl", "settings.json")),
]

LOCAL_CONFIG_PATH = os.path.join(BASE_DIR, "config.json")


def decode_token(encoded: str) -> str:
    """Giải mã API key dạng ENC:... bằng thuật toán base64 + đảo chuỗi."""
    if not encoded or not isinstance(encoded, str):
        return ""
    if not encoded.startswith("ENC:"):
        return encoded.strip()
    try:
        b64 = encoded[4:]
        return base64.b64decode(b64.encode("utf-8")).decode("utf-8")[::-1].strip()
    except Exception:
        return ""


def encode_token(raw_key: str) -> str:
    """Mã hóa API key sang chuẩn ENC:..."""
    if not raw_key:
        return ""
    reversed_str = raw_key.strip()[::-1]
    b64 = base64.b64encode(reversed_str.encode("utf-8")).decode("utf-8")
    return f"ENC:{b64}"


def resolve_settings_path(custom_path: Optional[str] = None) -> Optional[str]:
    """Tìm đường dẫn settings.json hợp lệ đầu tiên."""
    if custom_path and os.path.exists(custom_path):
        return os.path.normpath(custom_path)

    # Kiểm tra trong config.json cục bộ xem user có cấu hình đường dẫn riêng không
    if os.path.exists(LOCAL_CONFIG_PATH):
        try:
            with open(LOCAL_CONFIG_PATH, "r", encoding="utf-8") as f:
                cfg = json.load(f)
            cfg_path = cfg.get("settings_json_path", "")
            if cfg_path and os.path.exists(cfg_path):
                return os.path.normpath(cfg_path)
        except Exception:
            pass

    for p in CANDIDATE_SETTINGS_PATHS:
        norm = os.path.normpath(p)
        if os.path.exists(norm):
            return norm
    return None


def load_gemini_keys(settings_path: Optional[str] = None) -> List[Dict]:
    """
    Đọc danh sách Gemini API keys từ settings.json.
    Tự động giải mã token ENC:...
    Trả về list các dict: [{key, email, status, ...}, ...]
    """
    path = resolve_settings_path(settings_path)
    if not path:
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return []

    gemini_cfg = data.get("gemini", {})
    api_keys = gemini_cfg.get("api_keys", [])

    decoded_keys: List[Dict] = []
    for item in api_keys:
        if not isinstance(item, dict):
            continue
        raw = item.get("key", "")
        decoded = decode_token(raw)
        if decoded:
            entry = dict(item)
            entry["key"] = decoded
            entry.setdefault("status", "active")
            entry.setdefault("email", "unknown")
            decoded_keys.append(entry)

    if not decoded_keys:
        single = gemini_cfg.get("api_key", "")
        decoded_single = decode_token(single)
        if decoded_single:
            decoded_keys.append({
                "key": decoded_single,
                "email": "default",
                "status": "active",
            })

    return decoded_keys


def get_active_model_list(settings_path: Optional[str] = None) -> List[str]:
    """Đọc danh sách model ưu tiên từ settings.json nếu có."""
    path = resolve_settings_path(settings_path)
    if not path:
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        models = data.get("gemini", {}).get("model_priority", [])
        return [m["name"] for m in models if isinstance(m, dict) and m.get("enabled", True) and m.get("name")]
    except Exception:
        return []
