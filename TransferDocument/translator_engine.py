# -*- coding: utf-8 -*-
"""
Module: translator_engine.py
Engine dịch văn bản hàng loạt (batch JSON) đa ngôn ngữ (Nguồn <-> Đích) qua GeminiCoordinator.
Hỗ trợ:
- Dịch 2 chiều: Nhật/Anh/Trung/Hàn -> Việt, và Việt -> Nhật/Anh/Trung/Hàn (hoặc cặp bất kỳ).
- Bộ lọc thông minh: bỏ qua mã số, ký hiệu kỹ thuật, số thuần, đơn vị đo.
- Glossary thuật ngữ kỹ thuật (tự đảo chiều khi dịch Việt -> Nhật).
- Cache bền vững (translation_cache.json) tách riêng theo cặp (source_lang -> target_lang).
"""

import json
import os
import re
import threading
from typing import Callable, Dict, List, Optional

from gemini_safe import GeminiCoordinator, ErrorKind
from language_config import get_lang_meta
from settings_reader import load_gemini_keys, get_active_model_list

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CACHE_PATH = os.path.join(BASE_DIR, "translation_cache.json")
DEFAULT_GLOSSARY_PATH = os.path.join(BASE_DIR, "glossary.json")

# Glossary mặc định cho tài liệu kỹ thuật / tiêu chuẩn kiểm tra Nhật -> Việt
DEFAULT_GLOSSARY: Dict[str, str] = {
    "検査標準書": "Tiêu chuẩn kiểm tra",
    "測定標準": "Tiêu chuẩn đo lường",
    "測定・試験の方法に関する通則": "Quy định chung về phương pháp đo lường và thử nghiệm",
    "適用範囲": "Phạm vi áp dụng",
    "共通": "Dùng chung",
    "番号": "Mã số",
    "符号": "Ký hiệu",
    "作成": "Ngày lập",
    "改訂": "Sửa đổi",
    "頁": "Trang",
    "ノギス": "Thước cặp",
    "マイクロメータ": "Panme",
    "内側マイクロメータ": "Panme đo trong",
    "工具顕微鏡": "Kính hiển vi đo lường",
    "投影機": "Máy chiếu biên dạng",
    "デジタルインジケータ": "Đồng hồ so điện tử",
    "ダイヤルゲージ": "Đồng hồ so",
    "てこ式ダイヤルゲージ": "Đồng hồ so chân gập",
    "デプスゲージ": "Thước đo độ sâu",
    "表面粗さ測定機": "Máy đo độ nhám bề mặt",
    "形状測定機": "Máy đo biên dạng",
    "画像寸法測定機": "Máy đo kích thước bằng hình ảnh",
    "三次元粗さ測定機": "Máy đo độ nhám 3D",
    "三次元測定機": "Máy đo tọa độ 3D (CMM)",
    "真円度測定機": "Máy đo độ tròn",
    "校正": "Hiệu chuẩn",
    "公差": "Dung sai",
    "図面": "Bản vẽ",
    "部品": "Linh kiện",
    "製品": "Sản phẩm",
    "外観検査": "Kiểm tra ngoại quan",
    "寸法測定": "Đo kích thước",
    "合否判定": "Đánh giá Đạt/Không đạt",
    "備考": "Ghi chú",
}

RE_CJK = re.compile(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uac00-\ud7af]")
RE_JA_KANA = re.compile(r"[\u3040-\u30ff]")
RE_KO_HANGUL = re.compile(r"[\uac00-\ud7af]")
RE_VIET_DIACRITIC = re.compile(
    r"[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ"
    r"ÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]"
)
RE_NON_TRANSLATABLE = re.compile(
    r"^[\s\d\.\,\-\+\±\×\÷\/\:\;\(\)\[\]\{\}\<\>\=\~\!\@\#\$\%\^\&\*\_\|\\\'\"\`"
    r"°℃℉μµΩφΦφ∅○●◎△▲×✕✓✔✗✘※・－―‐～〜、。「」『』【】（）〔〕《》〈〉"
    r"A-Z0-9\-_/\.]+$"
)
RE_DOC_CODE = re.compile(r"^[A-Z]{1,4}\d?[-_][A-Z0-9]{1,4}(?:[-_][A-Z0-9]{1,6})*$")
RE_VERSION_CODE = re.compile(r"^\d{2,4}[-_]\d{1,3}(?:\s+[A-Za-z0-9]{1,3})?$")
RE_JA_STANDALONE_DATE = re.compile(r"^(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日$")
RE_EN_STANDALONE_DATE = re.compile(
    r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+(\d{1,2}),?\s+(\d{4})$", re.I
)
EN_MONTH_MAP = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}
RE_URL_OR_EMAIL = re.compile(r"^(https?://\S+|www\.\S+|\S+@\S+\.\S+)$", re.I)


def format_compact_date(text: str, target_lang: str) -> Optional[str]:
    """Định dạng gọn ngày tháng đơn lẻ (vd '1994年 6月 20日' -> '20/06/1994') cho ô metadata."""
    s = (text or "").strip()
    if not s:
        return None
    m_ja = RE_JA_STANDALONE_DATE.match(s)
    if m_ja:
        y, mo, d = int(m_ja.group(1)), int(m_ja.group(2)), int(m_ja.group(3))
        if target_lang in ("vi", "en"):
            return f"{d:02d}/{mo:02d}/{y:04d}"
    m_en = RE_EN_STANDALONE_DATE.match(s)
    if m_en:
        mo = EN_MONTH_MAP.get(m_en.group(1)[:3].lower(), 0)
        d, y = int(m_en.group(2)), int(m_en.group(3))
        if mo and target_lang == "vi":
            return f"{d:02d}/{mo:02d}/{y:04d}"
        if mo and target_lang == "ja":
            return f"{y:04d}年{mo}月{d}日"
    return None

UNIT_SET = {
    "mm", "cm", "km", "um", "nm", "kg", "mg", "ml", "hz", "khz", "mhz",
    "kv", "mv", "ma", "db", "rpm", "psi", "mpa", "kpa", "gpa", "pa",
    "ok", "ng", "no", "rev", "ver", "id", "qc", "qa", "iso", "jis", "din",
    "astm", "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "max", "min",
}


def normalize_source_text(text: str) -> str:
    """Chuẩn hóa chuỗi nguồn trước khi tra cache / gửi AI."""
    if not text:
        return ""
    lines = text.splitlines()
    norm_lines = []
    for line in lines:
        s = line.strip()
        if RE_CJK.search(s):
            s = re.sub(r"(?<=[\u3040-\u9fff])[ \u3000]+(?=[\u3040-\u9fff])", "", s)
            s = s.replace("\u3000", " ")
        s = re.sub(r"[ \t]{2,}", " ", s)
        norm_lines.append(s)
    return "\n".join(norm_lines).strip()


def needs_translation(text: str, source_lang: str = "auto", target_lang: str = "vi") -> bool:
    """Kiểm tra một chuỗi có cần dịch sang target_lang hay không (hỗ trợ 2 chiều)."""
    if not text:
        return False
    s = normalize_source_text(text)
    if not s:
        return False
    if RE_URL_OR_EMAIL.match(s):
        return False
    if RE_DOC_CODE.match(s) or RE_VERSION_CODE.match(s):
        return False

    tgt = (target_lang or "vi").lower()
    src = (source_lang or "auto").lower()

    has_cjk = bool(RE_CJK.search(s))
    has_vi = bool(RE_VIET_DIACRITIC.search(s))
    has_kana = bool(RE_JA_KANA.search(s))
    has_hangul = bool(RE_KO_HANGUL.search(s))

    # Nếu đã rõ ràng là ngôn ngữ đích (không lẫn ngôn ngữ khác) -> bỏ qua
    if tgt == "vi" and has_vi and not has_cjk:
        return False
    if tgt == "ja" and has_kana and not has_vi and not re.search(r"[A-Za-z]{4,}", s):
        return False
    if tgt == "ko" and has_hangul and not has_vi and not re.search(r"[A-Za-z]{4,}", s):
        return False

    # Nếu có ký tự tiếng Việt và ngôn ngữ đích KHÔNG phải tiếng Việt -> CHẮC CHẮN dịch!
    if has_vi and tgt != "vi":
        return True

    # Nếu có ký tự CJK và ngôn ngữ đích không phải cùng nhóm (hoặc nguồn khác đích)
    if has_cjk:
        if tgt in ("vi", "en"):
            return True
        if src != tgt:
            return True

    # Nếu chỉ toàn số, ký hiệu, mã viết hoa ngắn
    if RE_NON_TRANSLATABLE.match(s):
        words = re.findall(r"[A-Za-z]{2,}", s)
        if len(words) >= 2 and tgt != "en":
            return True
        return False

    # Kiểm tra có từ chữ cái Latin (tiếng Anh / tiếng Việt không dấu / ngoại ngữ)
    latin_words = re.findall(r"[A-Za-zÀ-ỹ]{2,}", s)
    if not latin_words:
        return False

    if len(latin_words) == 1 and latin_words[0].lower() in UNIT_SET and len(s) <= 8:
        return False

    # Nếu dịch sang tiếng Anh mà chuỗi chỉ toàn tiếng Anh ASCII thuần (không có dấu Việt/CJK)
    if tgt == "en" and src == "auto" and not has_vi and not has_cjk:
        # Vẫn dịch nếu nguồn được chỉ định rõ là vi (vd tiếng Việt không dấu)
        return False

    return True


def _strip_json_fences(raw: str) -> str:
    s = (raw or "").strip()
    if s.startswith("```"):
        s = re.sub(r"^```(?:json)?\s*", "", s, flags=re.I)
        s = re.sub(r"\s*```$", "", s)
    first = s.find("{")
    last = s.rfind("}")
    if first != -1 and last != -1 and last > first:
        s = s[first:last + 1]
    return s.strip()


class TranslationCache:
    """Cache bản dịch lưu ra JSON (UTF-8) an toàn đa luồng, tách theo cặp (source->target)."""

    def __init__(self, cache_path: str = DEFAULT_CACHE_PATH):
        self.cache_path = cache_path
        self._lock = threading.Lock()
        self._data: Dict[str, str] = {}
        self.load()

    def load(self):
        if os.path.exists(self.cache_path):
            try:
                with open(self.cache_path, "r", encoding="utf-8") as f:
                    obj = json.load(f)
                if isinstance(obj, dict):
                    self._data = obj
            except Exception:
                self._data = {}

    def save(self):
        with self._lock:
            try:
                tmp = self.cache_path + ".tmp"
                with open(tmp, "w", encoding="utf-8") as f:
                    json.dump(self._data, f, ensure_ascii=False, indent=2)
                os.replace(tmp, self.cache_path)
            except Exception:
                pass

    def make_key(self, source_lang: str, target_lang: str, norm_text: str) -> str:
        # Giữ tương thích ngược với cache v1 khi target_lang == 'vi'
        if target_lang == "vi":
            return f"{source_lang}||{norm_text}"
        return f"{source_lang}->{target_lang}||{norm_text}"

    def get(self, source_lang: str, target_lang: str, norm_text: str) -> Optional[str]:
        with self._lock:
            k = self.make_key(source_lang, target_lang, norm_text)
            val = self._data.get(k)
            if val is None and target_lang == "vi":
                val = self._data.get(f"{source_lang}->{target_lang}||{norm_text}")
            return val

    def set(self, source_lang: str, target_lang: str, norm_text: str, translated: str):
        with self._lock:
            self._data[self.make_key(source_lang, target_lang, norm_text)] = translated

    def clear(self):
        with self._lock:
            self._data.clear()
        self.save()


def load_glossary(
    target_lang: str = "vi",
    source_lang: str = "auto",
    glossary_path: str = DEFAULT_GLOSSARY_PATH,
) -> Dict[str, str]:
    """
    Nạp glossary theo chiều dịch:
    - sang 'vi': dùng glossary gốc (Nhật -> Việt) + glossary.json cục bộ.
    - 'vi' -> 'ja' (hoặc 'auto' -> 'ja'): tự động đảo chiều glossary (Việt -> Nhật).
    - các cặp khác: chỉ dùng nếu khớp trong glossary.json tùy chỉnh.
    """
    base = dict(DEFAULT_GLOSSARY)
    if os.path.exists(glossary_path):
        try:
            with open(glossary_path, "r", encoding="utf-8") as f:
                custom = json.load(f)
            if isinstance(custom, dict):
                for k, v in custom.items():
                    if isinstance(k, str) and isinstance(v, str) and k.strip() and v.strip():
                        base[k.strip()] = v.strip()
        except Exception:
            pass

    tgt = (target_lang or "vi").lower()
    src = (source_lang or "auto").lower()
    if tgt == "vi":
        return base
    if tgt == "ja" and src in ("vi", "auto"):
        # Đảo chiều Việt -> Nhật
        return {v: k for k, v in base.items() if v and k}
    return {}


class DocumentTranslator:
    """Bộ dịch hàng loạt văn bản tài liệu đa ngôn ngữ dùng GeminiCoordinator."""

    def __init__(
        self,
        source_lang: str = "auto",
        target_lang: str = "vi",
        settings_path: Optional[str] = None,
        use_cache: bool = True,
        use_glossary: bool = True,
        log_fn: Optional[Callable[[str], None]] = None,
        stop_check: Optional[Callable[[], bool]] = None,
        batch_max_items: int = 35,
        batch_max_chars: int = 3200,
    ):
        self.source_lang = (source_lang or "auto").lower()
        self.target_lang = (target_lang or "vi").lower()
        self.settings_path = settings_path
        self.use_cache = use_cache
        self.use_glossary = use_glossary
        self.log = log_fn or (lambda m: None)
        self.stop_check = stop_check or (lambda: False)
        self.batch_max_items = batch_max_items
        self.batch_max_chars = batch_max_chars

        self.cache = TranslationCache()
        self.glossary = load_glossary(self.target_lang, self.source_lang) if use_glossary else {}

        models = get_active_model_list(settings_path)
        self.coordinator = GeminiCoordinator(
            models=models if models else None,
            log_fn=self.log,
            key_loader=lambda: load_gemini_keys(self.settings_path),
            stop_check=self.stop_check,
            temperature=0.1,
            max_output_tokens=8192,
            timeout=120,
            lock_after_success=False,
        )

    def _build_prompt(self, items: Dict[str, str]) -> str:
        src_desc = {
            "auto": "tự động nhận diện (tiếng Nhật / Việt / Anh / Trung / Hàn)",
            "vi": "tiếng Việt",
            "ja": "tiếng Nhật",
            "en": "tiếng Anh",
            "zh": "tiếng Trung",
            "ko": "tiếng Hàn",
        }.get(self.source_lang, self.source_lang)

        tgt_meta = get_lang_meta(self.target_lang)
        tgt_name = tgt_meta["name"]

        joined_src = "\n".join(items.values())
        relevant_glossary = {
            k: v for k, v in self.glossary.items() if k in joined_src
        }
        glossary_block = ""
        if relevant_glossary:
            lines = [f"- {k} => {v}" for k, v in list(relevant_glossary.items())[:40]]
            glossary_block = "\nThuật ngữ kỹ thuật ưu tiên dùng nhất quán:\n" + "\n".join(lines) + "\n"

        payload = json.dumps(items, ensure_ascii=False, indent=2)
        return (
            f"Bạn là chuyên gia biên dịch tài liệu kỹ thuật công nghiệp (QA/QC, cơ khí, tiêu chuẩn kiểm tra, tài liệu doanh nghiệp) "
            f"từ {src_desc} sang {tgt_name} chuẩn xác, tự nhiên, súc tích để vừa khung bảng/ô tài liệu.\n"
            f"Quy tắc BẮT BUỘC:\n"
            f"1. Trả về DUY NHẤT một JSON object hợp lệ giữ nguyên 100% các key số ('0', '1', ...), KHÔNG thêm giải thích hay markdown thừa.\n"
            f"2. Giữ nguyên tuyệt đối các mã tài liệu (vd: ZZ-A1-06-1, BA-A1-08A-B), số hiệu, ký hiệu (○, △, ×, ±, μm, mm, ℃, Φ), số thứ tự đầu mục (1., 2.1, (1), a)).\n"
            f"3. Nếu chuỗi có ký tự xuống dòng \\n, giữ cấu trúc xuống dòng tương ứng.\n"
            f"4. Dịch hoàn toàn sang {tgt_name}, KHÔNG để sót từ ngoại ngữ (trừ tên riêng / mã kỹ thuật / đơn vị đo).\n"
            f"5. Nếu một chuỗi đã là số/ký hiệu hoặc đã đúng là {tgt_name} thì giữ nguyên.\n"
            f"{glossary_block}\n"
            f"Dữ liệu JSON cần dịch:\n{payload}"
        )

    def _translate_batch(self, texts: List[str]) -> Dict[str, str]:
        if not texts or self.stop_check():
            return {}

        items = {str(i): t for i, t in enumerate(texts)}
        prompt = self._build_prompt(items)
        res = self.coordinator.request(prompt, json_mode=True, temperature=0.1, max_output_tokens=8192)

        if not res.get("ok"):
            err = res.get("error", {})
            kind = err.get("kind", "")
            msg = err.get("message", "")
            if kind in (ErrorKind.STOPPED, ErrorKind.ALL_BUDGET_EXHAUSTED, ErrorKind.NO_KEY):
                raise RuntimeError(f"Dừng dịch ({kind}): {msg}")
            self.log(f"⚠ Lỗi batch ({kind}): {msg}")
            return {}

        raw_text = res.get("text", "")
        cleaned = _strip_json_fences(raw_text)
        parsed = None
        try:
            parsed = json.loads(cleaned)
        except Exception as e:
            self.log(f"⚠ Lỗi parse JSON từ AI ({e}), sẽ chia nhỏ batch để thử lại...")

        result: Dict[str, str] = {}
        missing: List[str] = []

        if isinstance(parsed, dict):
            for i, src in enumerate(texts):
                val = parsed.get(str(i))
                if isinstance(val, str) and val.strip():
                    result[src] = val.strip()
                else:
                    missing.append(src)
        else:
            missing = list(texts)

        if missing and len(texts) > 1 and not self.stop_check():
            mid = max(1, len(missing) // 2)
            if len(missing) == len(texts):
                part1 = missing[:mid]
                part2 = missing[mid:]
                result.update(self._translate_batch(part1))
                if part2:
                    result.update(self._translate_batch(part2))
            else:
                result.update(self._translate_batch(missing))

        return result

    def translate_texts(
        self,
        raw_texts: List[str],
        progress_cb: Optional[Callable[[int, int, str], None]] = None,
    ) -> Dict[str, str]:
        raw_to_norm: Dict[str, str] = {}
        unique_norms: List[str] = []
        seen_norms = set()

        for raw in raw_texts:
            if raw in raw_to_norm:
                continue
            if not needs_translation(raw, self.source_lang, self.target_lang):
                continue
            norm = normalize_source_text(raw)
            if not norm:
                continue
            raw_to_norm[raw] = norm
            if norm not in seen_norms:
                seen_norms.add(norm)
                unique_norms.append(norm)

        if not unique_norms:
            return {}

        norm_to_tgt: Dict[str, str] = {}
        to_call: List[str] = []

        for norm in unique_norms:
            compact_dt = format_compact_date(norm, self.target_lang)
            if compact_dt:
                norm_to_tgt[norm] = compact_dt
                continue
            if self.use_glossary and norm in self.glossary:
                norm_to_tgt[norm] = self.glossary[norm]
                continue
            if self.use_cache:
                cached = self.cache.get(self.source_lang, self.target_lang, norm)
                if cached:
                    norm_to_tgt[norm] = cached
                    continue
            to_call.append(norm)

        cached_hits = len(unique_norms) - len(to_call)
        if cached_hits > 0:
            self.log(f"⚡ Đã dùng cache/glossary cho {cached_hits}/{len(unique_norms)} cụm văn bản.")

        batches: List[List[str]] = []
        cur_batch: List[str] = []
        cur_chars = 0
        for item in to_call:
            item_len = len(item)
            if cur_batch and (
                len(cur_batch) >= self.batch_max_items
                or cur_chars + item_len > self.batch_max_chars
            ):
                batches.append(cur_batch)
                cur_batch = []
                cur_chars = 0
            cur_batch.append(item)
            cur_chars += item_len
        if cur_batch:
            batches.append(cur_batch)

        total_batches = len(batches)
        for idx, batch in enumerate(batches, start=1):
            if self.stop_check():
                self.log("🛑 Đã nhận lệnh dừng từ người dùng.")
                break
            msg = f"🤖 Đang dịch lô {idx}/{total_batches} ({len(batch)} đoạn -> {self.target_lang.upper()})..."
            self.log(msg)
            if progress_cb:
                progress_cb(idx - 1, total_batches, msg)
            translated_map = self._translate_batch(batch)
            for k, v in translated_map.items():
                norm_to_tgt[k] = v
                if self.use_cache:
                    self.cache.set(self.source_lang, self.target_lang, k, v)
            if self.use_cache:
                self.cache.save()
            if progress_cb:
                progress_cb(idx, total_batches, f"✅ Hoàn tất lô {idx}/{total_batches}")

        final_map: Dict[str, str] = {}
        for raw, norm in raw_to_norm.items():
            translated = norm_to_tgt.get(norm)
            if not translated:
                continue
            lead = " " if raw.startswith(" ") else ""
            trail = " " if raw.endswith(" ") else ""
            final_map[raw] = f"{lead}{translated}{trail}"

        return final_map
