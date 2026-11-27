# -*- coding: utf-8 -*-
"""
Module: pdf_translator.py
Engine dịch PDF độ chính xác cao (Spatial Cell-Aware + Highlight-Aware + Obstacle-Aware v1.4) bằng PyMuPDF:
1. Đọc đường kẻ bảng ngang/dọc từ vector graphics (page.get_drawings()) để nhận diện ranh giới ô bảng.
2. Nhận diện vùng tô màu highlight (vàng/xanh/hồng...) và vật cản (con dấu Annotation Stamp, hình ảnh).
3. Trích xuất từ mức ký tự (rawdict) -> loại bỏ khoảng trắng thừa, tách cột chuẩn xác;
   tự động gộp tiêu đề giãn chữ kiểu Nhật (vd: '点  検  ・  処  置  方  法' -> '点検・処置方法')
   và gộp mảnh cùng ô bảng hẹp.
4. Bảo vệ cấu trúc key-value không viền theo từng hàng ngang (vd: 制定 | 1994年6月20日, 改訂 | 2022年7月1日, 計測 | 000-0 g)
   -> không bao giờ gộp lệch hàng hay dịch sai vị trí mã phiên bản.
5. Xóa phẫu thuật 2 lớp:
   - Pass 1: Xóa đúng hình chữ nhật highlight cũ của các cụm đã dịch bằng PDF_REDACT_LINE_ART_REMOVE_IF_COVERED
     (giữ nguyên 100% đường kẻ bảng và highlight trên mã không dịch như '000-0 g').
   - Pass 2: Xóa lớp chữ gốc bằng fill=False + PDF_REDACT_IMAGE_NONE + PDF_REDACT_LINE_ART_NONE.
   - Pass 3: Chèn chữ dịch kèm font hệ thống nhúng + tô lại highlight CSS khớp 100% độ dài chữ mới,
     tự động tránh con dấu đỏ & hình ảnh.
"""

import html
import os
import re
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Tuple

import pymupdf

from language_config import get_default_font, is_space_delimited, resolve_font_file
from translator_engine import DocumentTranslator, needs_translation, RE_CJK, RE_VERSION_CODE

RE_NEW_ITEM = re.compile(
    r"^[\s\u3000]*("
    r"[・•▪■□●○◎△▲※★☆\-–—]|"
    r"\d+[\.\)．、]|"
    r"[\(（]\d+[\)）]|"
    r"[①-⑳]|"
    r"[\[［【]|"
    r"(?:注|備考|例|参考|尚、|なお、|又|また|制定|改訂|計測|Established|Revised|Measuring|Ghi chú|Lưu ý|Ví dụ|Note)"
    r")"
)

SENTENCE_END = set("。.!！?？")


@dataclass
class HighlightRect:
    rect: pymupdf.Rect
    hex_color: str
    used_by_translated: bool = False
    used_by_untranslated: bool = False


@dataclass
class LineSeg:
    bbox: pymupdf.Rect
    text: str
    size: float
    color_int: int
    bold: bool
    italic: bool
    centered: bool = False
    highlight_hex: Optional[str] = None
    highlight_indices: List[int] = field(default_factory=list)


@dataclass
class ParaGroup:
    segments: List[LineSeg] = field(default_factory=list)

    @property
    def bbox(self) -> pymupdf.Rect:
        r = pymupdf.Rect(self.segments[0].bbox)
        for s in self.segments[1:]:
            r |= s.bbox
        return r

    @property
    def text(self) -> str:
        parts = [s.text.strip() for s in self.segments if s.text.strip()]
        if not parts:
            return ""
        joined = parts[0]
        for nxt in parts[1:]:
            if re.search(r"[\u3040-\u9fff]$", joined) and re.search(r"^[\u3040-\u9fff]", nxt):
                joined += nxt
            else:
                joined += " " + nxt
        return joined

    @property
    def size(self) -> float:
        return self.segments[0].size

    @property
    def color_int(self) -> int:
        return self.segments[0].color_int

    @property
    def bold(self) -> bool:
        return sum(len(s.text) for s in self.segments if s.bold) >= sum(len(s.text) for s in self.segments) * 0.6

    @property
    def italic(self) -> bool:
        return sum(len(s.text) for s in self.segments if s.italic) >= sum(len(s.text) for s in self.segments) * 0.6

    @property
    def centered(self) -> bool:
        return len(self.segments) == 1 and self.segments[0].centered

    @property
    def highlight_hex(self) -> Optional[str]:
        hl_chars = sum(len(s.text) for s in self.segments if s.highlight_hex)
        tot_chars = max(1, sum(len(s.text) for s in self.segments))
        if hl_chars / tot_chars >= 0.55:
            for s in self.segments:
                if s.highlight_hex:
                    return s.highlight_hex
        return None


def _int_color_to_hex(color_int: int) -> str:
    r = (color_int >> 16) & 0xFF
    g = (color_int >> 8) & 0xFF
    b = color_int & 0xFF
    return f"#{r:02x}{g:02x}{b:02x}"


def _rgb_tuple_to_hex(rgb: Tuple[float, float, float]) -> str:
    r = max(0, min(255, int(round(rgb[0] * 255))))
    g = max(0, min(255, int(round(rgb[1] * 255))))
    b = max(0, min(255, int(round(rgb[2] * 255))))
    return f"#{r:02x}{g:02x}{b:02x}"


def _extract_grid_and_highlights(
    page: pymupdf.Page,
) -> Tuple[List[Tuple[float, float, float]], List[Tuple[float, float, float]], List[HighlightRect]]:
    """
    Trích xuất đường kẻ bảng (h_lines, v_lines) VÀ các hình chữ nhật highlight màu sáng (vd vàng #ffff00).
    """
    h_lines: List[Tuple[float, float, float]] = []
    v_lines: List[Tuple[float, float, float]] = []
    highlights: List[HighlightRect] = []

    try:
        drawings = page.get_drawings()
    except Exception:
        return h_lines, v_lines, highlights

    for d in drawings:
        fill = d.get("fill")
        stroke = d.get("color")
        rect = d.get("rect")

        # Nhận diện vùng highlight màu sáng (vàng, xanh lá nhạt, cyan, hồng...) không phải trắng/đen/xám
        if (
            fill
            and isinstance(fill, (tuple, list))
            and len(fill) == 3
            and rect is not None
            and rect.height <= 36.0
            and rect.width >= 3.0
        ):
            r, g, b = float(fill[0]), float(fill[1]), float(fill[2])
            sat = max(r, g, b) - min(r, g, b)
            if sat >= 0.25 and max(r, g, b) >= 0.65:
                highlights.append(HighlightRect(rect=pymupdf.Rect(rect), hex_color=_rgb_tuple_to_hex((r, g, b))))

        for item in d.get("items", []):
            kind = item[0]
            if kind == "l":
                p1, p2 = item[1], item[2]
                if abs(p1.y - p2.y) <= 2.0 and abs(p1.x - p2.x) >= 12.0:
                    h_lines.append(((p1.y + p2.y) / 2.0, min(p1.x, p2.x), max(p1.x, p2.x)))
                elif abs(p1.x - p2.x) <= 2.0 and abs(p1.y - p2.y) >= 10.0:
                    v_lines.append(((p1.x + p2.x) / 2.0, min(p1.y, p2.y), max(p1.y, p2.y)))
            elif kind == "re":
                r_box = item[1]
                if r_box.height <= 2.5 and r_box.width >= 12.0:
                    h_lines.append(((r_box.y0 + r_box.y1) / 2.0, r_box.x0, r_box.x1))
                elif r_box.width <= 2.5 and r_box.height >= 10.0:
                    v_lines.append(((r_box.x0 + r_box.x1) / 2.0, r_box.y0, r_box.y1))
                elif r_box.width >= 14.0 and r_box.height >= 10.0 and stroke is not None:
                    h_lines.append((r_box.y0, r_box.x0, r_box.x1))
                    h_lines.append((r_box.y1, r_box.x0, r_box.x1))
                    v_lines.append((r_box.x0, r_box.y0, r_box.y1))
                    v_lines.append((r_box.x1, r_box.y0, r_box.y1))

    return h_lines, v_lines, highlights


def _extract_obstacles(page: pymupdf.Page) -> List[pymupdf.Rect]:
    """Thu thập tọa độ các vật cản không được ghi chữ đè lên: con dấu (Annotation Stamp) & hình ảnh."""
    obs: List[pymupdf.Rect] = []
    try:
        for annot in (page.annots() or []):
            if annot.rect and annot.rect.width >= 8 and annot.rect.height >= 8:
                obs.append(pymupdf.Rect(annot.rect))
    except Exception:
        pass
    try:
        for img in page.get_images(full=False):
            for r in page.get_image_rects(img[0]):
                if r.width >= 10 and r.height >= 10:
                    obs.append(pymupdf.Rect(r))
    except Exception:
        pass
    return obs


def _has_vline_between(x_left: float, x_right: float, y_mid: float, v_lines: List[Tuple[float, float, float]]) -> bool:
    for vx, vy0, vy1 in v_lines:
        if (x_left - 1.0) < vx < (x_right + 1.0) and (vy0 - 2.0) <= y_mid <= (vy1 + 2.0):
            return True
    return False


def _has_hline_between(y_top: float, y_bot: float, x_mid: float, h_lines: List[Tuple[float, float, float]]) -> bool:
    for hy, hx0, hx1 in h_lines:
        if (y_top - 1.5) < hy < (y_bot + 1.5) and (hx0 - 2.0) <= x_mid <= (hx1 + 2.0):
            return True
    return False


def _chars_to_lineseg(chars: List[Tuple]) -> LineSeg:
    x0 = min(c[1] for c in chars)
    y0 = min(c[2] for c in chars)
    x1 = max(c[3] for c in chars)
    y1 = max(c[4] for c in chars)

    out = [chars[0][0]]
    for prev, cur in zip(chars, chars[1:]):
        gap = cur[1] - prev[3]
        avg_sz = (prev[5] + cur[5]) / 2.0
        if gap >= avg_sz * 0.22:
            out.append(" ")
        out.append(cur[0])

    text = "".join(out).strip()
    sz = round(sum(c[5] for c in chars) / len(chars), 1)
    col_counts: Dict[int, int] = {}
    b_cnt = 0
    i_cnt = 0
    for c in chars:
        col_counts[c[6]] = col_counts.get(c[6], 0) + 1
        if c[7]:
            b_cnt += 1
        if c[8]:
            i_cnt += 1
    dom_col = max(col_counts, key=col_counts.get)
    return LineSeg(
        bbox=pymupdf.Rect(x0, y0, x1, y1),
        text=text,
        size=sz,
        color_int=dom_col,
        bold=b_cnt >= len(chars) * 0.6,
        italic=i_cnt >= len(chars) * 0.6,
    )


def _attach_highlights_to_segments(segs: List[LineSeg], highlights: List[HighlightRect]):
    """Gắn thông tin highlight màu cho từng LineSeg nằm trên vùng highlight."""
    if not highlights:
        return
    for seg in segs:
        sb = seg.bbox
        seg_area = max(1.0, sb.width * sb.height)
        matched_indices = []
        hl_overlap_w = 0.0
        hl_hex = None
        for idx, hr in enumerate(highlights):
            inter = sb & hr.rect
            if not inter.is_empty and inter.width > 1.0 and inter.height > 2.0:
                if (inter.width * inter.height) / seg_area >= 0.15 or inter.width >= hr.rect.width * 0.5:
                    matched_indices.append(idx)
                    hl_overlap_w += inter.width
                    hl_hex = hr.hex_color
        if matched_indices:
            seg.highlight_indices = matched_indices
            if hl_overlap_w >= sb.width * 0.50:
                seg.highlight_hex = hl_hex


def _merge_spaced_cjk_and_cell_tokens(
    segs: List[LineSeg],
    v_lines: List[Tuple[float, float, float]],
    h_lines: List[Tuple[float, float, float]],
) -> List[LineSeg]:
    """
    1. Gộp các tiêu đề giãn chữ kiểu Nhật (vd: '点  検  ・  処  置  方  法' hoặc '内    容')
       khi các mảnh trên cùng 1 hàng chỉ gồm 1-2 ký tự CJK đơn lẻ, không bị đường kẻ dọc ngăn cách.
    2. Gộp các mảnh cùng nằm trên 1 dòng bên trong CÙNG 1 ô bảng hẹp (< 150pt) bị tách lẻ.
    """
    if len(segs) <= 1:
        return segs

    # Nhóm theo dải Y (cùng hàng ngang)
    sorted_s = sorted(segs, key=lambda s: (round(s.bbox.y0, 1), round(s.bbox.x0, 1)))
    rows: List[List[LineSeg]] = []
    for s in sorted_s:
        if rows and abs(rows[-1][0].bbox.y0 - s.bbox.y0) <= 3.5:
            rows[-1].append(s)
        else:
            rows.append([s])

    result: List[LineSeg] = []
    for row in rows:
        row.sort(key=lambda s: s.bbox.x0)
        i = 0
        while i < len(row):
            # Thử phát hiện chuỗi ký tự CJK giãn đều (spaced CJK header)
            cur = row[i]
            if len(cur.text.strip()) <= 2 and RE_CJK.search(cur.text):
                run = [cur]
                j = i + 1
                while j < len(row):
                    nxt = row[j]
                    prev = run[-1]
                    gap = nxt.bbox.x0 - prev.bbox.x1
                    y_mid = (prev.bbox.y0 + prev.bbox.y1) / 2.0
                    is_short_cjk = len(nxt.text.strip()) <= 2 and (RE_CJK.search(nxt.text) or nxt.text.strip() in ("・", "／", "/"))
                    if (
                        is_short_cjk
                        and abs(nxt.size - prev.size) <= 1.0
                        and nxt.color_int == prev.color_int
                        and gap <= 55.0
                        and not _has_vline_between(prev.bbox.x1, nxt.bbox.x0, y_mid, v_lines)
                    ):
                        run.append(nxt)
                        j += 1
                    else:
                        break
                if len(run) >= 2:
                    merged_bbox = pymupdf.Rect(run[0].bbox)
                    for r_s in run[1:]:
                        merged_bbox |= r_s.bbox
                    merged_text = "".join(r_s.text.strip() for r_s in run)
                    result.append(
                        LineSeg(
                            bbox=merged_bbox,
                            text=merged_text,
                            size=run[0].size,
                            color_int=run[0].color_int,
                            bold=run[0].bold,
                            italic=run[0].italic,
                            centered=True,
                        )
                    )
                    i = j
                    continue

            # Thử gộp 2 mảnh nằm trong CÙNG 1 ô bảng hẹp (< 150pt) không có đường kẻ dọc ngăn cách
            if i + 1 < len(row):
                nxt = row[i + 1]
                y_mid = (cur.bbox.y0 + cur.bbox.y1) / 2.0
                gap = nxt.bbox.x0 - cur.bbox.x1
                if (
                    gap <= 32.0
                    and abs(cur.size - nxt.size) <= 1.0
                    and cur.color_int == nxt.color_int
                    and not _has_vline_between(cur.bbox.x1, nxt.bbox.x0, y_mid, v_lines)
                ):
                    # Kiểm tra xem cả hai có nằm gọn trong 1 ô bảng hẹp (có vline bên trái & bên phải)
                    left_vs = [vx for vx, vy0, vy1 in v_lines if vx <= cur.bbox.x0 + 2.0 and vy0 - 2 <= y_mid <= vy1 + 2]
                    right_vs = [vx for vx, vy0, vy1 in v_lines if vx >= nxt.bbox.x1 - 2.0 and vy0 - 2 <= y_mid <= vy1 + 2]
                    if left_vs and right_vs and (min(right_vs) - max(left_vs)) <= 150.0:
                        merged_bbox = cur.bbox | nxt.bbox
                        sep = "" if (RE_CJK.search(cur.text[-1:]) and RE_CJK.search(nxt.text[:1])) else " "
                        row[i + 1] = LineSeg(
                            bbox=merged_bbox,
                            text=f"{cur.text.strip()}{sep}{nxt.text.strip()}",
                            size=cur.size,
                            color_int=cur.color_int,
                            bold=cur.bold,
                            italic=cur.italic,
                        )
                        i += 1
                        continue

            result.append(cur)
            i += 1

    return result


def _extract_line_segments(
    page: pymupdf.Page,
    v_lines: List[Tuple[float, float, float]],
    h_lines: List[Tuple[float, float, float]],
) -> List[LineSeg]:
    raw = page.get_text("rawdict")
    segs: List[LineSeg] = []

    for blk in raw.get("blocks", []):
        if blk.get("type") != 0:
            continue
        for line in blk.get("lines", []):
            ldir = line.get("dir", (1.0, 0.0))
            if abs(ldir[0]) < 0.7:
                continue

            chars = []
            for sp in line.get("spans", []):
                sz = float(sp.get("size", 10.0))
                col = int(sp.get("color", 0))
                flags = int(sp.get("flags", 0))
                is_b = bool(flags & 16)
                is_i = bool(flags & 2)
                for ch in sp.get("chars", []):
                    c = ch.get("c", "")
                    if not c or c.isspace():
                        continue
                    cb = ch.get("bbox")
                    if not cb:
                        continue
                    chars.append((c, cb[0], cb[1], cb[2], cb[3], sz, col, is_b, is_i))

            if not chars:
                continue

            chars.sort(key=lambda it: it[1])
            cur = [chars[0]]
            for ch in chars[1:]:
                prev = cur[-1]
                gap_x = ch[1] - prev[3]
                y_mid = (prev[2] + prev[4] + ch[2] + ch[4]) / 4.0
                avg_sz = (prev[5] + ch[5]) / 2.0
                split_thresh = max(avg_sz * 1.65, 14.5)
                if gap_x > split_thresh or _has_vline_between(prev[3], ch[1], y_mid, v_lines):
                    segs.append(_chars_to_lineseg(cur))
                    cur = [ch]
                else:
                    cur.append(ch)
            if cur:
                segs.append(_chars_to_lineseg(cur))

    return _merge_spaced_cjk_and_cell_tokens(segs, v_lines, h_lines)


def _has_row_companion(seg: LineSeg, all_segs: List[LineSeg]) -> Optional[float]:
    """
    Kiểm tra xem trên cùng hàng Y với `seg` có một segment khác (cột nhãn/giá trị kề bên) không.
    Trả về x0 gần nhất của companion (dùng phát hiện bảng key-value không viền như 制定 | 1994年6月20日).
    """
    companions = []
    for other in all_segs:
        if other is seg:
            continue
        if abs(other.bbox.y0 - seg.bbox.y0) <= 4.0:
            # Nằm cách nhau theo chiều X (cột khác)
            if other.bbox.x0 > seg.bbox.x1 + 5.0 or seg.bbox.x0 > other.bbox.x1 + 5.0:
                companions.append(other.bbox.x0)
    if not companions:
        return None
    return min(companions, key=lambda cx: abs(cx - seg.bbox.x0))


def _group_segments_into_paragraphs(
    segs: List[LineSeg],
    h_lines: List[Tuple[float, float, float]],
    v_lines: List[Tuple[float, float, float]],
) -> List[ParaGroup]:
    """
    Gộp các LineSeg cùng cột theo chiều dọc thành đoạn văn hoàn chỉnh:
    - KHÔNG gộp các hàng bảng key-value không viền (制定|1994, 改訂|2022, 計測|000-0 g).
    - KHÔNG gộp mã phiên bản (000-0 g) hay ngày tháng metadata với dòng trên/dưới.
    - KHÔNG gộp qua đường kẻ ngang/dọc của bảng hoặc khi khoảng cách dọc lớn.
    """
    if not segs:
        return []

    ordered = sorted(segs, key=lambda s: (round(s.bbox.y0, 1), round(s.bbox.x0, 1)))
    groups: List[ParaGroup] = []

    for seg in ordered:
        best_g: Optional[ParaGroup] = None
        best_gap = 1e9

        seg_is_ver = bool(RE_VERSION_CODE.match(seg.text.strip()))
        seg_comp = _has_row_companion(seg, ordered)

        for g in reversed(groups):
            last = g.segments[-1]
            if last.centered or seg.centered:
                continue
            gap_y = seg.bbox.y0 - last.bbox.y1
            if gap_y < -2.0 or gap_y > max(last.size * 0.78, 8.5):
                continue
            if abs(seg.size - last.size) > 1.2 or seg.color_int != last.color_int:
                continue

            # Không gộp mã phiên bản như '000-0 g'
            if seg_is_ver or RE_VERSION_CODE.match(last.text.strip()):
                continue

            # Không gộp nếu cả 2 dòng đều là cặp key-value song song trên cùng 2 cột (制定|1994, 改訂|2022, 計測|000-0 g)
            last_comp = _has_row_companion(last, ordered)
            if seg_comp is not None and last_comp is not None and abs(seg_comp - last_comp) <= 25.0:
                if len(last.text.strip()) <= 26 and len(seg.text.strip()) <= 26:
                    continue

            # Chồng lấn X và thẳng lề trái
            ov_x0 = max(last.bbox.x0, seg.bbox.x0)
            ov_x1 = min(last.bbox.x1, seg.bbox.x1)
            if ov_x1 <= ov_x0:
                continue
            if abs(last.bbox.x0 - seg.bbox.x0) > max(28.0, last.size * 2.8):
                continue

            # Không gộp khi khác trạng thái highlight hoàn toàn ở dòng ngắn
            if last.highlight_hex != seg.highlight_hex and (len(last.text) < 25 or len(seg.text) < 25):
                continue

            if RE_NEW_ITEM.match(seg.text):
                continue
            if last.text and last.text[-1] in SENTENCE_END and len(last.text) < 24:
                continue

            x_mid = (ov_x0 + ov_x1) / 2.0
            if _has_hline_between(last.bbox.y1, seg.bbox.y0, x_mid, h_lines):
                continue
            y_mid = (last.bbox.y0 + seg.bbox.y1) / 2.0
            if _has_vline_between(min(last.bbox.x0, seg.bbox.x0), max(last.bbox.x0, seg.bbox.x0), y_mid, v_lines):
                continue

            if gap_y < best_gap:
                best_gap = gap_y
                best_g = g

        if best_g is not None:
            best_g.segments.append(seg)
        else:
            groups.append(ParaGroup(segments=[seg]))

    return groups


def _compute_safe_insert_box(
    group: ParaGroup,
    all_groups: List[ParaGroup],
    h_lines: List[Tuple[float, float, float]],
    v_lines: List[Tuple[float, float, float]],
    obstacles: List[pymupdf.Rect],
    page_rect: pymupdf.Rect,
) -> pymupdf.Rect:
    """
    Tính khung đích insert_htmlbox an toàn:
    - Nếu là tiêu đề căn giữa trong ô bảng (group.centered): mở đều sang 2 đường kẻ dọc của ô.
    - Tránh tuyệt đối đường kẻ dọc/ngang, các nhóm chữ khác, con dấu đỏ (Stamp) và hình ảnh (obstacles)!
    """
    r = pymupdf.Rect(group.bbox)
    y_mid = (r.y0 + r.y1) / 2.0
    x_mid = (r.x0 + r.x1) / 2.0

    # Nếu là tiêu đề căn giữa (vd: 'Phương pháp kiểm tra và xử lý'), lấy đúng biên trái/phải của ô bảng
    if group.centered:
        left_vs = [vx for vx, vy0, vy1 in v_lines if vx <= r.x0 + 2.0 and vy0 - 2.0 <= y_mid <= vy1 + 2.0]
        right_vs = [vx for vx, vy0, vy1 in v_lines if vx >= r.x1 - 2.0 and vy0 - 2.0 <= y_mid <= vy1 + 2.0]
        box_x0 = (max(left_vs) + 3.0) if left_vs else max(page_rect.x0 + 4.0, r.x0 - 4.0)
        box_x1 = (min(right_vs) - 3.0) if right_vs else min(page_rect.x1 - 4.0, r.x1 + 4.0)
        return pymupdf.Rect(box_x0, max(page_rect.y0 + 2.0, r.y0 - 1.0), max(box_x0 + 10.0, box_x1), r.y1 + 2.5)

    # Giới hạn phải tối đa
    max_x1 = page_rect.x1 - 12.0
    for vx, vy0, vy1 in v_lines:
        if vx >= r.x1 - 2.0 and vy0 - 2.0 <= y_mid <= vy1 + 2.0:
            max_x1 = min(max_x1, vx - 2.0)

    for other in all_groups:
        if other is group:
            continue
        ob = other.bbox
        if min(r.y1, ob.y1) - max(r.y0, ob.y0) > 2.0 and ob.x0 >= r.x0 + 2.0:
            max_x1 = min(max_x1, ob.x0 - 4.0)

    # Tránh con dấu đỏ (Annotation Stamp) & hình ảnh chèn (obstacles)
    for obs in obstacles:
        if min(r.y1 + 4.0, obs.y1) - max(r.y0 - 2.0, obs.y0) > 2.0 and obs.x0 > r.x0 + 10.0:
            max_x1 = min(max_x1, obs.x0 - 4.0)

    target_x1 = min(max_x1, max(r.x1 + 1.5, r.x1 + max(20.0, r.width * 0.22)))
    if target_x1 < r.x0 + 10.0:
        target_x1 = max(r.x0 + 10.0, max_x1)

    # Giới hạn dưới tối đa
    max_y1 = page_rect.y1 - 12.0
    for hy, hx0, hx1 in h_lines:
        if hy >= r.y1 - 1.5 and hx0 - 2.0 <= x_mid <= hx1 + 2.0:
            max_y1 = min(max_y1, hy - 1.5)

    for other in all_groups:
        if other is group:
            continue
        ob = other.bbox
        if min(target_x1, ob.x1) - max(r.x0, ob.x0) > 2.0 and ob.y0 >= r.y1 - 1.0:
            max_y1 = min(max_y1, ob.y0 - 1.5)

    target_y1 = min(max_y1, r.y1 + max(3.5, group.size * 0.55))
    if target_y1 < r.y1 + 1.5:
        target_y1 = max(r.y1 + 1.5, max_y1)

    return pymupdf.Rect(
        max(page_rect.x0 + 2.0, r.x0 - 0.5),
        max(page_rect.y0 + 2.0, r.y0 - 0.8),
        max(r.x0 + 6.0, target_x1),
        max(r.y0 + 6.0, target_y1),
    )


def _clean_output_text(text: str, target_lang: str) -> str:
    if not text:
        return ""
    s = text.replace("\uf0b7", "•").replace("\uf0a7", "•")
    if is_space_delimited(target_lang):
        s = re.sub(r"^[\s]*・\s*", "• ", s)
        s = s.replace("\n・", "\n• ")
        s = (
            s.replace("。", ".")
            .replace("、", ",")
            .replace("，", ", ")
            .replace("：", ": ")
            .replace("（", "(")
            .replace("）", ")")
        )
        s = re.sub(r" {2,}", " ", s)
    return s.strip()


def _build_pdf_css(font_path_reg: str, font_path_bold: Optional[str]) -> Tuple[str, str]:
    font_dir = os.path.dirname(font_path_reg)
    reg_name = os.path.basename(font_path_reg)
    bold_name = os.path.basename(font_path_bold) if font_path_bold else reg_name
    css = (
        f"@font-face {{ font-family: 'TDTarget'; src: url('{reg_name}'); font-weight: normal; font-style: normal; }}\n"
        f"@font-face {{ font-family: 'TDTarget'; src: url('{bold_name}'); font-weight: bold; font-style: normal; }}\n"
        f"* {{ font-family: 'TDTarget', sans-serif; margin: 0; padding: 0; line-height: 1.15; }}"
    )
    return css, font_dir


def translate_pdf(
    input_path: str,
    output_path: str,
    translator: DocumentTranslator,
    target_font: Optional[str] = None,
    auto_fit_layout: bool = True,
    progress_cb: Optional[Callable[[int, int, str], None]] = None,
) -> Dict:
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    font_name = target_font or get_default_font(translator.target_lang)
    font_reg = resolve_font_file(font_name, bold=False)
    font_bold = resolve_font_file(font_name, bold=True)
    if not font_reg:
        raise RuntimeError(f"Không tìm thấy file font hệ thống cho '{font_name}'")

    css_base, font_dir = _build_pdf_css(font_reg, font_bold)
    archive = pymupdf.Archive(font_dir)

    doc = pymupdf.open(input_path)
    total_pages = len(doc)
    scan_pages: List[int] = []
    total_images = 0

    page_plans = []
    all_raw_texts: List[str] = []

    for p_idx in range(total_pages):
        page = doc[p_idx]
        total_images += len(page.get_images(full=False))
        h_lines, v_lines, highlights = _extract_grid_and_highlights(page)
        obstacles = _extract_obstacles(page)
        segs = _extract_line_segments(page, v_lines, h_lines)
        if not segs:
            scan_pages.append(p_idx + 1)
            continue

        _attach_highlights_to_segments(segs, highlights)
        groups = _group_segments_into_paragraphs(segs, h_lines, v_lines)

        trans_groups: List[Tuple[ParaGroup, str]] = []
        for g in groups:
            txt = g.text
            if txt and needs_translation(txt, translator.source_lang, translator.target_lang):
                trans_groups.append((g, txt))
                all_raw_texts.append(txt)
                for seg in g.segments:
                    for hi in seg.highlight_indices:
                        highlights[hi].used_by_translated = True
            else:
                for seg in g.segments:
                    for hi in seg.highlight_indices:
                        highlights[hi].used_by_untranslated = True

        page_plans.append((p_idx, groups, h_lines, v_lines, highlights, obstacles, trans_groups))

    if scan_pages:
        translator.log(
            f"⚠ Phát hiện {len(scan_pages)} trang PDF không có lớp văn bản (PDF scan/ảnh): "
            f"trang {scan_pages[:10]} — cần OCR trước để dịch các trang này."
        )

    translator.log(
        f"📕 PDF (Spatial+Highlight Engine v1.4): {total_pages} trang, tìm thấy {len(all_raw_texts)} khối/ô cần dịch "
        f"(font nhúng: {font_name})."
    )

    trans_map = translator.translate_texts(all_raw_texts, progress_cb=progress_cb)

    translated_count = 0
    for p_idx, all_groups, h_lines, v_lines, highlights, obstacles, trans_groups in page_plans:
        page = doc[p_idx]
        to_draw: List[Tuple[ParaGroup, str, pymupdf.Rect]] = []

        # Pass 1: Xóa sạch các hình chữ nhật highlight cũ thuộc cụm ĐÃ DỊCH (giữ nguyên highlight trên mã không dịch như 000-0 g!)
        hl_removed = False
        for hr in highlights:
            if hr.used_by_translated and not hr.used_by_untranslated:
                hr_exp = pymupdf.Rect(hr.rect.x0 - 0.5, hr.rect.y0 - 0.5, hr.rect.x1 + 0.5, hr.rect.y1 + 0.5)
                page.add_redact_annot(hr_exp, fill=False)
                hl_removed = True
        if hl_removed:
            page.apply_redactions(
                images=pymupdf.PDF_REDACT_IMAGE_NONE,
                graphics=pymupdf.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED,
            )

        # Pass 2: Xóa phẫu thuật từng dòng gốc bằng fill=False (giữ 100% đường kẻ bảng, con dấu đỏ, ảnh!)
        for g, orig_txt in trans_groups:
            tr = trans_map.get(orig_txt)
            if not tr:
                continue
            tr_clean = _clean_output_text(tr, translator.target_lang)
            if not tr_clean:
                continue
            for seg in g.segments:
                sr = pymupdf.Rect(
                    seg.bbox.x0 + 0.1,
                    seg.bbox.y0 + 0.1,
                    max(seg.bbox.x0 + 1.0, seg.bbox.x1 - 0.1),
                    max(seg.bbox.y0 + 1.0, seg.bbox.y1 - 0.1),
                )
                page.add_redact_annot(sr, fill=False)
            box = _compute_safe_insert_box(g, all_groups, h_lines, v_lines, obstacles, page.rect)
            to_draw.append((g, tr_clean, box))
            translated_count += 1

        if not to_draw:
            continue

        page.apply_redactions(
            images=pymupdf.PDF_REDACT_IMAGE_NONE,
            graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
        )

        # Pass 3: Chèn văn bản đã dịch + tô lại highlight CSS khớp 100% chữ mới
        for g, tr_clean, box in to_draw:
            escaped = html.escape(tr_clean).replace("\n", "<br/>")
            hex_col = _int_color_to_hex(g.color_int)
            weight = "bold" if g.bold else "normal"
            style = "italic" if g.italic else "normal"
            align = "center" if g.centered else "left"
            font_sz = max(5.5, min(g.size, 36.0))
            hl_hex = g.highlight_hex
            inner = (
                f"<span style='background-color:{hl_hex};'>{escaped}</span>"
                if hl_hex
                else escaped
            )
            snippet = (
                f"<div style='font-size:{font_sz:.1f}pt; color:{hex_col}; "
                f"font-weight:{weight}; font-style:{style}; text-align:{align};'>{inner}</div>"
            )
            page.insert_htmlbox(
                box,
                snippet,
                css=css_base,
                archive=archive,
                scale_low=0.0 if auto_fit_layout else 1.0,
            )

    try:
        doc.subset_fonts()
    except Exception:
        pass
    doc.save(output_path, garbage=3, deflate=True)
    doc.close()

    return {
        "input": input_path,
        "output": output_path,
        "pages": total_pages,
        "scan_pages": scan_pages,
        "blocks_total": len(all_raw_texts),
        "blocks_translated": translated_count,
        "media_preserved": total_images,
        "font_used": font_name,
    }
