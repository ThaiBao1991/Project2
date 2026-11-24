# -*- coding: utf-8 -*-
"""
oe_calculators.py — Bộ 5 Công Cụ Tính Nhanh Thực Chiến OE & Giải Mã Mã Cáp CADIVI
+ Trình Giả Lập Phỏng Vấn Thử 30 Phút Có Đồng Hồ Đếm Ngược & Chấm Điểm /100 (MockInterviewDialog).

Tách riêng hoàn toàn phần hàm tính toán thuần (pure functions) để kiểm thử tự động 100%
và các cửa sổ popup CustomTkinter Catppuccin Mocha độc lập không làm chật giao diện chính.
"""

import math
import random
import re
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

try:
    import term_glossary
except Exception:
    term_glossary = None


# =====================================================================
# 1. CÁC HÀM TÍNH TOÁN THUẦN (PURE FUNCTIONS — KIỂM SOÁT CHẶT EDGE CASES)
# =====================================================================
def calc_oee_cable(planned_min, downtime_min, ideal_speed_m_per_min, total_meters, scrap_meters):
    """Tính OEE dây chuyền kéo/bện/đùn theo tốc độ mét/phút (Line Speed)."""
    if planned_min <= 0:
        raise ValueError("Thời gian kế hoạch phải > 0 phút.")
    if downtime_min < 0 or downtime_min >= planned_min:
        raise ValueError("Thời gian dừng máy phải ≥ 0 và nhỏ hơn thời gian kế hoạch.")
    if ideal_speed_m_per_min <= 0:
        raise ValueError("Tốc độ chuẩn (m/phút) phải > 0.")
    if total_meters <= 0:
        raise ValueError("Tổng sản lượng mét phải > 0.")
    if scrap_meters < 0 or scrap_meters > total_meters:
        raise ValueError("Phế phẩm (mét) phải trong khoảng 0 → Tổng sản lượng.")

    run_time = planned_min - downtime_min
    good_meters = total_meters - scrap_meters
    a = run_time / planned_min
    p = total_meters / (run_time * ideal_speed_m_per_min)
    q = good_meters / total_meters
    oee = a * p * q

    if oee >= 0.85:
        rating = "🏆 World-Class (≥ 85%)"
    elif oee >= 0.75:
        rating = "🟢 Tốt (75% – 84.9%)"
    elif oee >= 0.60:
        rating = "🟡 Trung bình (60% – 74.9% — Dư địa cải tiến lớn!)"
    else:
        rating = "🔴 Cảnh báo đỏ (< 60% — Cần SMED / TPM ngay!)"

    # Xác định trụ cột yếu nhất để gợi ý hướng hành động OE
    weakest = min([("Availability (Dừng máy / Đổi mã SMED)", a), ("Performance (Giảm tốc / Dừng vặt)", p), ("Quality (Phế đầu ca / Lỗi Spark)", q)], key=lambda x: x[1])
    warning_p = " (⚠️ P > 100%: Kiểm tra lại Tốc độ chuẩn Routing có đang đặt quá thấp không!)" if p > 1.0 else ""

    return {
        "run_time_min": round(run_time, 2),
        "good_meters": round(good_meters, 2),
        "availability": a * 100.0,
        "performance": p * 100.0,
        "quality": q * 100.0,
        "oee": oee * 100.0,
        "rating": rating,
        "weakest_pillar": weakest[0] + warning_p,
    }


def calc_copper_giveaway(d_nominal_mm, d_actual_mm, annual_copper_tons, copper_price_m_vnd_per_ton):
    """Tính % hao phí đồng biếu không (Copper Give-away) và số tiền thất thoát mỗi năm."""
    if d_nominal_mm <= 0 or d_actual_mm <= 0:
        raise ValueError("Đường kính danh định và thực tế phải > 0 mm.")
    if annual_copper_tons < 0 or copper_price_m_vnd_per_ton < 0:
        raise ValueError("Sản lượng đồng và đơn giá không được âm.")

    pct_diff = ((d_actual_mm / d_nominal_mm) ** 2 - 1.0) * 100.0
    extra_tons = annual_copper_tons * (pct_diff / 100.0)
    annual_loss_m_vnd = extra_tons * copper_price_m_vnd_per_ton

    if pct_diff > 1.0:
        advice = "🔴 Thất thoát lớn! Cần siết chu kỳ đánh bóng khuôn PCD & chạy SPC dịch tâm về sát IEC 60228."
    elif pct_diff > 0.4:
        advice = "🟡 Dư địa tối ưu tốt — theo dõi % IACS đầu vào và khóa tuổi thọ khuôn theo tấn kéo."
    elif pct_diff >= 0:
        advice = "🟢 Kiểm soát xuất sắc (≤ +0.4%) — nhớ kiểm tra chéo điện trở 20°C trên cầu Kelvin Bridge."
    else:
        advice = "⚠️ Đường kính thực nhỏ hơn chuẩn! BẮT BUỘC kiểm tra ngay điện trở DC 20°C tránh rớt QCVN 4 / IEC 60228!"

    return {
        "pct_giveaway": pct_diff,
        "extra_tons": extra_tons,
        "annual_loss_m_vnd": annual_loss_m_vnd,
        "advice": advice,
    }


def calc_pvc_volume_cost(price_a_per_kg, sg_a, price_b_per_kg, sg_b, annual_tons_a=100.0):
    """So sánh chi phí thực theo THỂ TÍCH (VNĐ/lít) giữa 2 loại hạt nhựa PVC (bóc trần bẫy bột đá CaCO3)."""
    if price_a_per_kg <= 0 or price_b_per_kg <= 0 or sg_a <= 0 or sg_b <= 0:
        raise ValueError("Đơn giá (VNĐ/kg) và tỷ trọng (g/cm³) phải > 0.")
    if annual_tons_a < 0:
        raise ValueError("Sản lượng năm không được âm.")

    cost_vol_a = price_a_per_kg * sg_a  # VNĐ / lít (dm³)
    cost_vol_b = price_b_per_kg * sg_b
    diff_pct = ((cost_vol_b - cost_vol_a) / cost_vol_a) * 100.0
    annual_liters = (annual_tons_a * 1000.0) / sg_a
    annual_diff_m_vnd = ((cost_vol_b - cost_vol_a) * annual_liters) / 1_000_000.0

    if diff_pct > 0:
        verdict = f"🔴 CẢNH BÁO BẪY TỶ TRỌNG: Nhựa B thực tế ĐẮT HƠN nhựa A +{diff_pct:.2f}% trên mỗi mét cáp (+{annual_diff_m_vnd:,.1f} triệu/năm)!"
    elif diff_pct < 0:
        verdict = f"🟢 Nhựa B rẻ hơn theo thể tích {abs(diff_pct):.2f}% (tiết kiệm ~{abs(annual_diff_m_vnd):,.1f} triệu/năm) — BẮT BUỘC chạy MOC + Aging Oven 7 ngày trước khi đổi!"
    else:
        verdict = "🟡 Chi phí theo thể tích tương đương nhau — ưu tiên nhựa có cơ lý Tensile & độ ổn định đùn tốt hơn."

    return {
        "cost_vol_a": cost_vol_a,
        "cost_vol_b": cost_vol_b,
        "diff_pct": diff_pct,
        "annual_diff_m_vnd": annual_diff_m_vnd,
        "verdict": verdict,
    }


def calc_cp_cpk(usl, lsl, mean, sigma):
    """Tính năng lực quá trình Cp, Cpk, Cpu, Cpl và mức đánh giá chuẩn Six Sigma."""
    if usl <= lsl:
        raise ValueError("Cận trên USL phải lớn hơn cận dưới LSL.")
    if sigma <= 0:
        raise ValueError("Độ lệch chuẩn σ phải > 0.")

    cp = (usl - lsl) / (6.0 * sigma)
    cpu = (usl - mean) / (3.0 * sigma)
    cpl = (mean - lsl) / (3.0 * sigma)
    cpk = min(cpu, cpl)
    sigma_short = cpk * 3.0

    if cpk >= 1.67:
        verdict = "🏆 Xuất sắc (≥ 1.67 — ~5 Sigma): Rất ổn định, đủ dư địa an toàn xem xét Target Shift tiết kiệm vật liệu!"
    elif cpk >= 1.33:
        verdict = "🟢 Đạt chuẩn công nghiệp (1.33 – 1.66 — ≥ 4 Sigma): Kiểm soát tốt bằng biểu đồ SPC."
    elif cpk >= 1.00:
        verdict = "🟡 Cận biên (1.00 – 1.32 — ~3 Sigma): Dễ phát sinh phế khi tâm trôi nhẹ — cần siết kiểm soát."
    else:
        verdict = "🔴 KHÔNG ĐẠT (< 1.00): Đang tạo ra phế phẩm trực tiếp! Cấm dịch tâm; phải mở dự án DMAIC giảm σ hoặc chỉnh lệch tâm ngay!"

    shift_note = ""
    if cp >= 1.33 and cpk < 1.33:
        target = (usl + lsl) / 2.0
        shift_note = f"💡 Phát hiện hay: Cp = {cp:.2f} (máy đủ chính xác!) nhưng Cpk thấp do LỆCH TÂM (Mean={mean:.3f} vs Target={target:.3f}) — chỉnh lại tâm máy sẽ nâng ngay Cpk mà không cần mua máy mới!"

    return {
        "cp": cp,
        "cpu": cpu,
        "cpl": cpl,
        "cpk": cpk,
        "sigma_short": sigma_short,
        "verdict": verdict,
        "shift_note": shift_note,
    }


def calc_inventory_and_roi(avg_daily_demand, std_demand, lead_time_days, std_lt_days, service_z, capex_m_vnd, monthly_savings_m_vnd):
    """Tính Tồn kho an toàn Safety Stock, Điểm đặt hàng ROP và Thời gian hoàn vốn Payback / ROI 1 năm."""
    if avg_daily_demand < 0 or std_demand < 0 or lead_time_days < 0 or std_lt_days < 0 or service_z <= 0:
        raise ValueError("Các thông số nhu cầu, Lead Time và hệ số Z phải hợp lệ (≥ 0, Z > 0).")
    if capex_m_vnd < 0 or monthly_savings_m_vnd < 0:
        raise ValueError("Vốn CAPEX và tiết kiệm/tháng không được âm.")

    safety_stock = service_z * math.sqrt(lead_time_days * (std_demand ** 2) + (avg_daily_demand ** 2) * (std_lt_days ** 2))
    rop = avg_daily_demand * lead_time_days + safety_stock

    if monthly_savings_m_vnd > 0 and capex_m_vnd > 0:
        payback_months = capex_m_vnd / monthly_savings_m_vnd
        roi_1yr = ((monthly_savings_m_vnd * 12.0 - capex_m_vnd) / capex_m_vnd) * 100.0
    elif capex_m_vnd == 0 and monthly_savings_m_vnd > 0:
        payback_months = 0.0
        roi_1yr = 999.9
    else:
        payback_months = float("inf")
        roi_1yr = -100.0

    if payback_months <= 12:
        roi_verdict = "🏆 Dự án VÀNG (Hoàn vốn ≤ 12 tháng): Khả năng được Ban Giám Đốc CADIVI duyệt rất cao!"
    elif payback_months <= 24:
        roi_verdict = "🟢 Khả thi tốt (Hoàn vốn 12–24 tháng): Nên kèm thêm 3 kịch bản độ nhạy Thận trọng–Cơ sở–Lạc quan."
    else:
        roi_verdict = "🟡 Hoàn vốn dài (> 24 tháng): Xem xét giải pháp Kaizen/SMED chi phí thấp trước khi trình mua CAPEX!"

    return {
        "safety_stock": safety_stock,
        "rop": rop,
        "payback_months": payback_months,
        "roi_1yr_pct": roi_1yr,
        "roi_verdict": roi_verdict,
    }


def decode_cadivi_cable(code_str):
    """Giải mã tự động ký hiệu mã dây & cáp điện CADIVI sang cấu tạo, tiêu chuẩn, chuỗi máy & lưu ý OE."""
    raw = (code_str or "").strip()
    if not raw:
        raise ValueError("Vui lòng nhập mã cáp CADIVI (vd: CXV/DSTA 3x120+1x70, VC 2.5, LV-ABC 4x50...).")

    up = raw.upper().replace("×", "X")
    tokens = re.split(r"[\s\-]+", up)
    head = tokens[0] if tokens else up

    conductor = "Ruột Đồng (Cu — chuẩn IEC 60228)"
    insulation = "PVC (Nhiệt độ làm việc tối đa 70°C)"
    armor_shield = "Không có giáp kim loại / màn chắn"
    sheath = "Không có lớp vỏ ngoài riêng (1 lớp bọc)"
    standard = "TCVN 6610 / QCVN 4 (450/750V)"
    route = "Kéo sợi RBD/Multi-wire → Ủ → Bện (nếu nhiều sợi) → Đùn PVC → Khoanh 100m → Lab QCVN 4"
    oe_note = "Tập trung: Copper Give-away (≤ +0.4%), Color Sequencing đổi màu, hiệu chuẩn bánh đo mét Capstan & Yamazumi đóng khoanh 100m."
    warning = ""

    # Nhận diện các họ mã đặc thù trước
    if "H1Z2Z2" in up or "SOLAR" in up:
        conductor = "Ruột Đồng mềm Class 5 MẠ THIẾC (Tinned Copper — chống oxy hóa 25 năm)"
        insulation = "Hợp chất XLPO ít khói không halogen khâu mạch E-beam (lõi 120°C)"
        sheath = "Vỏ ngoài XLPO chống tia UV, Ozone, axit/kiềm (DC 1,500V)"
        standard = "EN 50618 / IEC 62930 (Cáp điện mặt trời 25 năm)"
        route = "Kéo tinh + Mạ thiếc → Bện Buncher êm → Co-extrusion 2 lớp → Chiếu xạ E-beam (120–180 kGy) → Lab EN 50618"
        oe_note = "Tránh trầy xước lớp mạ thiếc, tối ưu gom lô chiếu xạ E-beam + dán thẻ đo liều Dosimeter đầu/cuối rulo."
    elif "ABC" in up:
        conductor = "Ruột NHÔM (Al — EC Grade ≥ 61% IACS) bện ép nén"
        insulation = "XLPE màu ĐEN chứa 2–2.5% muội than Carbon Black chống tia UV (90°C)"
        sheath = "Cáp vặn xoắn treo trên không (không vỏ chung, phân pha bằng 0–1–2–3 gân nổi)"
        standard = "TCVN 6447 / AS 3560 (Cáp vặn xoắn hạ thế EVN)"
        route = "Kéo Nhôm (cách ly tuyệt đối bụi đồng!) → Rigid Strander → Đùn XLPE Đen (đổi vòng Cối gân) → Xông Sauna Silane → Xoắn bó ABC"
        oe_note = "Campaign 4 pha KHÔNG cần xả nhựa Purging (chỉ đổi vòng Cối tạo gân 5 phút → +9% OEE!); kiểm soát hàm lượng UV Carbon Black ≥ 2%."
    elif up.startswith("AS ") or head == "AS" or "ACSR" in up:
        conductor = "Dây NHÔM trần bên ngoài dẫn điện + LÕI THÉP mạ kẽm ở giữa chịu lực kéo (ACSR)"
        insulation = "Dây trần (Không bọc cách điện — truyền tải điện đường dây trên không)"
        sheath = "Không vỏ (có bơm mỡ chịu nhiệt chống ăn mòn kẽm/nhôm bên trong lõi)"
        standard = "TCVN 5064 / IEC 61089 (Đường dây truyền tải EVN)"
        route = "Kéo Nhôm riêng biệt → Bện Rigid Strander quanh lõi thép + Bơm mỡ định lượng → Lab lực kéo đứt UTS"
        oe_note = "Gắn bơm định lượng mỡ đồng bộ tốc độ tránh tràn mỡ ra lớp nhôm ngoài (bị EVN từ chối); tách khu nhôm khỏi bụi đồng!"
    elif head.startswith("VC"):
        standard = "TCVN 6610 / IEC 60227 / QCVN 4 (Dây dân dụng 450/750V)"
        if "VCMT" in head:
            conductor = "Ruột Đồng mềm nhiều sợi Class 5 (2–3 lõi ghép xoắn tròn)"
            sheath = "Vỏ bọc ngoài PVC tròn bảo vệ (2 lớp PVC)"
            route = "Kéo Multi-wire + Ủ → Buncher → Đùn lõi PVC → Ghép lõi → Đùn vỏ PVC → Đánh khoanh 100m"
        elif "VCMD" in head:
            conductor = "Ruột Đồng mềm nhiều sợi Class 5 (2 lõi song song)"
            sheath = "Dây đôi mềm dẹt bọc PVC định hình"
            route = "Kéo Multi-wire + Ủ → Buncher → Đùn song song 2 lõi PVC → Đánh khoanh 100m"
        elif "VCM" in head:
            conductor = "Ruột Đồng mềm nhiều sợi mảnh Class 5 (dễ uốn)"
            route = "Kéo Multi-wire + Ủ → Buncher → Đùn PVC tốc độ cao → Đánh khoanh 100m"
        else:
            conductor = "Ruột Đồng đơn đặc Class 1 hoặc bện 7 sợi Class 2"
    else:
        # Mã cáp lực chuẩn CADIVI (C/A + V/X/E + V/E + /FR /DSTA /DATA /SWA /S)
        main_part = head.split("/")[0]
        if main_part.startswith("A"):
            conductor = "Ruột NHÔM (Al — chuẩn IEC 60228 Class 2, cách ly tuyệt đối khỏi bụi đồng!)"
        elif main_part.startswith("C"):
            conductor = "Ruột ĐỒNG (Cu — chuẩn IEC 60228 Class 2 ép nén tròn/rẻ quạt)"

        if len(main_part) >= 2 and main_part[1] == "X":
            insulation = "XLPE khâu mạch (Nhiệt độ làm việc 90°C, ngắn mạch 250°C — tải dòng cao hơn PVC 20–25%!)"
        elif len(main_part) >= 2 and main_part[1] == "V":
            insulation = "PVC (Nhiệt độ làm việc liên tục 70°C)"
        elif len(main_part) >= 2 and main_part[1] == "E":
            insulation = "PE / HDPE (Chống ẩm, độ bền cơ cao)"

        if "LSZH" in up or "LSHF" in up:
            sheath = "Vỏ ngoài LSZH / LSHF (Ít khói, không khí axit Halogen — dùng cho chung cư, bệnh viện, metro)"
        elif len(main_part) >= 3 and main_part[2] == "V":
            sheath = "Vỏ ngoài PVC (Đùn ống Tubing chống bám dính lõi)"
        elif len(main_part) >= 3 and main_part[2] == "E":
            sheath = "Vỏ ngoài PE / HDPE chịu mài mòn chôn ngầm"
        else:
            sheath = "1 lớp cách điện không có vỏ bảo vệ ngoài riêng (như dây CV / AV)"

        # Kiểm tra trung thế / chống cháy / giáp / màn chắn
        is_mv = any(k in up for k in ["24KV", "35KV", "22KV", "12/20", "18/30"])
        standard = "IEC 60502-2 / TCVN 5935-2 (Cáp lực Trung thế)" if is_mv else "IEC 60502-1 / TCVN 5935-1 (Cáp lực Hạ thế 0.6/1kV)"

        extras = []
        if "/FR" in up or "FRT" in up:
            extras.append("Quấn băng Mica FR chống cháy 750–950°C trong 90–180 phút (IEC 60331)")
        if "/S/" in up or up.endswith("-S") or "/S " in up:
            extras.append("Màn chắn đồng chống nhiễu EMI (băng đồng hoặc lưới đan Braiding)")
        if "DSTA" in up:
            extras.append("Áo giáp 2 lớp BĂNG THÉP mạ kẽm lệch pha (DSTA — chống va đập chôn ngầm)")
        if "DATA" in up:
            extras.append("Áo giáp 2 lớp BĂNG NHÔM không từ tính (DATA — chuyên dụng cho cáp 1 lõi xoay chiều!)")
        if "SWA" in up:
            extras.append("Áo giáp SỢI THÉP (SWA — chịu lực kéo dọc lớn khi kéo cáp ngầm/thẳng đứng)")
        if extras:
            armor_shield = " + ".join(extras)

        # Kiểm tra bẫy vật lý kinh điển: 1 lõi xoay chiều + DSTA thép!
        is_single_core = bool(re.search(r"\b1X\d+", up))
        if is_single_core and ("DSTA" in up or "SWA" in up):
            warning = "⚠️ CẢNH BÁO KỸ THUẬT CỰC QUAN TRỌNG: Phát hiện cáp 1 lõi (1×...) dùng giáp THÉP (DSTA/SWA)! Với dòng điện xoay chiều 1 lõi, giáp sắt từ sẽ sinh dòng xoáy Eddy Current nung nóng chảy cáp — BẮT BUỘC đổi sang băng NHÔM (DATA) hoặc sợi nhôm (AWA)!"

        steps = ["Kéo sợi RBD"]
        steps.append("Bện nén Rigid Strander")
        if "/FR" in up or "FRT" in up:
            steps.append("Quấn băng Mica FR (chồng mép 30–50%)")
        if is_mv:
            steps.append("Đùn 3 lớp & Lưu hóa ống cong CCV (Nitơ 12 bar)")
        elif "XLPE" in insulation:
            steps.append("Đùn XLPE Silane + Xông Sauna (4–12h)")
        else:
            steps.append("Đùn cách điện PVC")
        if not is_single_core and len(main_part) >= 3:
            steps.append("Ghép lõi Drum Twister")
        if "/S" in up or "-S" in up:
            steps.append("Đan lưới Braiding / Quấn màn chắn đồng")
        if "DSTA" in up or "DATA" in up or "SWA" in up:
            steps.append("Máy bọc giáp băng/sợi")
        if len(main_part) >= 3 or "LSZH" in up or "LSHF" in up:
            steps.append("Đùn vỏ ngoài Tubing + Laser Gauge + In chữ")
        steps.append("Lab " + ("Faraday PD ≤ 5pC" if is_mv else "IEC 60502 / Hot Set"))
        steps.append("Cắt đoạn Cut-Length sang Rulo gỗ")
        route = " → ".join(steps)

        if is_mv:
            oe_note = "Tối đa hóa Campaign 24/7 trên CCV (giảm phế bật/tắt lò), giám sát áp suất Nitơ SCADA theo từng mét & giữ Cleanroom nạp nhựa."
        elif "LSZH" in up or "LSHF" in up or "/FR" in up:
            oe_note = "Trục vít nén thấp, sấy Hopper Dryer kỹ, Melt Temp ≤ 165°C, DDR 1.1–1.6 chống Die Drool & rỗ khí; khống chế chồng mép Mica 40%."
        else:
            oe_note = "Xóa chờ gom mẻ Sauna, đồng bộ chiều dài 4 rulo trước Drum Twister, SMED nạp lồng Rigid Strander & Solver tối ưu Cut-Length."

    return {
        "raw": raw,
        "conductor": conductor,
        "insulation": insulation,
        "armor_shield": armor_shield,
        "sheath": sheath,
        "standard": standard,
        "route": route,
        "oe_note": oe_note,
        "warning": warning,
    }


def build_mock_interview_set(questions_list, seed=None):
    """Rút đúng bộ 10 câu hỏi chuẩn cấu trúc buổi phỏng vấn 30 phút thực tế tại CADIVI Miền Trung."""
    if not questions_list:
        return []
    rng = random.Random(seed)

    def _pick(predicate, count, used_ids):
        pool = [q for q in questions_list if q.get("id") not in used_ids and predicate(q)]
        rng.shuffle(pool)
        chosen = pool[:count]
        for q in chosen:
            used_ids.add(q.get("id"))
        return chosen

    used = set()
    picked = []
    # 1. Tự giới thiệu / Phản biện CV STAR (1 câu)
    picked += _pick(lambda q: q.get("id") == "q_star_01", 1, used)
    if not picked:
        picked += _pick(lambda q: "STAR" in q.get("category", ""), 1, used)
    # 2. Công nghệ cáp & 9 nhóm máy CADIVI (2 câu)
    picked += _pick(lambda q: "Công Nghệ & Máy Móc" in q.get("category", "") or "Đùn Cáp" in q.get("category", ""), 2, used)
    # 3. OEE / OLE / SMED / BOM (2 câu)
    picked += _pick(lambda q: any(k in q.get("category", "") for k in ["OEE", "OLE", "SMED", "BOM"]), 2, used)
    # 4. Six Sigma / Kế hoạch S&OP-MRP / Bảo trì / LSW (2 câu)
    picked += _pick(lambda q: any(k in q.get("category", "") for k in ["Six Sigma", "Kế Hoạch", "Hoạch Định", "SPC"]), 2, used)
    # 5. Câu hỏi bẫy HR/GĐ & Đàm phán lương / Hiểu CADIVI (1 câu)
    picked += _pick(lambda q: str(q.get("id", "")).startswith("q_war_"), 1, used)
    # 6. Tiếng Anh chuyên ngành OE (1 câu)
    picked += _pick(lambda q: str(q.get("id", "")).startswith("q_en_"), 1, used)
    # 7. Hỏi ngược nhà tuyển dụng / Hành vi chốt hạ (1 câu)
    picked += _pick(lambda q: "Hỏi Ngược" in q.get("category", "") or "STAR" in q.get("category", ""), 1, used)

    # Nếu chưa đủ 10 câu (do tập câu hỏi nhỏ), điền nốt ngẫu nhiên không trùng
    if len(picked) < 10:
        picked += _pick(lambda _q: True, 10 - len(picked), used)
    return picked[:10]


# =====================================================================
# 2. CỬA SỔ POPUP BỘ CÔNG CỤ TÍNH NHANH OE & GIẢI MÃ MÃ CÁP CADIVI
# =====================================================================
class OECalculatorDialog(ctk.CTkToplevel):
    """Cửa sổ 5 công cụ tính nhanh OE & Giải mã mã cáp CADIVI — học nhanh qua số liệu thật."""
    def __init__(self, parent, theme):
        super().__init__(parent)
        self.theme = theme
        self.title("🧮 Bộ Công Cụ Tính Nhanh Thực Chiến OE & Giải Mã Mã Cáp CADIVI")
        self.geometry("860x660")
        self.minsize(720, 560)
        self.configure(fg_color=theme["base"])
        self.transient(parent)
        self.bind("<Escape>", lambda _e: self.destroy())

        self._build_ui()
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _make_field(self, parent, row, label, default_val):
        ctk.CTkLabel(parent, text=label, font=ctk.CTkFont(size=12), text_color=self.theme["text"], anchor="w").grid(row=row, column=0, sticky="w", padx=(10, 8), pady=5)
        ent = ctk.CTkEntry(parent, width=180, height=30, fg_color=self.theme["crust"], border_color=self.theme["surface1"], text_color=self.theme["text"])
        ent.insert(0, str(default_val))
        ent.grid(row=row, column=1, sticky="ew", padx=(0, 10), pady=5)
        parent.columnconfigure(1, weight=1)
        return ent

    def _make_output_box(self, parent, height=180):
        tb = ctk.CTkTextbox(parent, height=height, fg_color=self.theme["crust"], text_color=self.theme["text"], font=ctk.CTkFont(family="Consolas", size=12), wrap="word")
        tb.pack(fill="both", expand=True, padx=10, pady=(6, 10))
        return tb

    def _set_output(self, tb, text):
        tb.configure(state="normal")
        tb.delete("1.0", "end")
        tb.insert("1.0", text)
        tb.configure(state="disabled")

    def _build_ui(self):
        t = self.theme
        ctk.CTkLabel(
            self,
            text="🧮 CÔNG CỤ THỰC HÀNH TÍNH NHANH OE & GIẢI MÃ MÃ CÁP CADIVI (BẤM SỐ THẤY NGAY BẢN CHẤT!)",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=t["cyan"]
        ).pack(anchor="w", padx=16, pady=(12, 6))

        tabs = ctk.CTkTabview(
            self, fg_color=t["surface0"], segmented_button_fg_color=t["crust"],
            segmented_button_selected_color=t["blue"], corner_radius=8
        )
        tabs.pack(fill="both", expand=True, padx=14, pady=(0, 14))

        self._build_oee_tab(tabs.add("⚙️ OEE (m/phút)"))
        self._build_material_tab(tabs.add("💰 Đồng & Nhựa PVC"))
        self._build_cpk_tab(tabs.add("🎯 Cp / Cpk"))
        self._build_inv_roi_tab(tabs.add("📦 Tồn Kho & ROI"))
        self._build_decoder_tab(tabs.add("🔌 Giải Mã Mã Cáp"))

    def _build_oee_tab(self, tab):
        frm = ctk.CTkFrame(tab, fg_color=self.theme["mantle"], corner_radius=8)
        frm.pack(fill="x", padx=10, pady=8)
        self.e_oee_plan = self._make_field(frm, 0, "Thời gian kế hoạch ca (phút, vd 450p × 5 ca = 2250):", "2250")
        self.e_oee_down = self._make_field(frm, 1, "Tổng thời gian dừng máy Downtime (phút):", "275")
        self.e_oee_spd = self._make_field(frm, 2, "Tốc độ chuẩn thiết kế (m/phút):", "320")
        self.e_oee_tot = self._make_field(frm, 3, "Tổng sản lượng chạy ra (mét):", "548000")
        self.e_oee_scr = self._make_field(frm, 4, "Tổng phế phẩm đầu ca & lỗi Spark (mét):", "14000")

        ctk.CTkButton(
            tab, text="⚡ Tính OEE Dây Chuyền Cáp", height=32, font=ctk.CTkFont(weight="bold"),
            fg_color=self.theme["green"], text_color=self.theme["crust"], command=self._run_oee
        ).pack(anchor="w", padx=10, pady=(2, 4))
        self.out_oee = self._make_output_box(tab)
        self._run_oee()

    def _run_oee(self):
        try:
            r = calc_oee_cable(
                float(self.e_oee_plan.get()), float(self.e_oee_down.get()),
                float(self.e_oee_spd.get()), float(self.e_oee_tot.get()), float(self.e_oee_scr.get())
            )
            txt = (
                f"📊 KẾT QUẢ PHÂN TÍCH OEE DÂY CHUYỀN CÁP:\n"
                f"  • Thời gian chạy thực tế (Run Time) : {r['run_time_min']:,.1f} phút\n"
                f"  • Sản lượng đạt chuẩn (Good Meters) : {r['good_meters']:,.0f} mét\n"
                f"  ────────────────────────────────────────────────────\n"
                f"  • Availability (A — Độ khả dụng)    : {r['availability']:.2f}%\n"
                f"  • Performance  (P — Tốc độ chạy)    : {r['performance']:.2f}%\n"
                f"  • Quality      (Q — Chất lượng)     : {r['quality']:.2f}%\n"
                f"  ➤ TỔNG OEE = A × P × Q              : {r['oee']:.2f}%   [{r['rating']}]\n\n"
                f"🎯 Trụ cột yếu nhất cần OE ưu tiên tấn công trước:\n"
                f"  → {r['weakest_pillar']}"
            )
            self._set_output(self.out_oee, txt)
        except Exception as e:
            self._set_output(self.out_oee, f"❌ Lỗi nhập liệu: {e}")

    def _build_material_tab(self, tab):
        split = ctk.CTkFrame(tab, fg_color="transparent")
        split.pack(fill="x", padx=6, pady=6)

        # Trái: Copper Give-away
        f_cu = ctk.CTkFrame(split, fg_color=self.theme["mantle"], corner_radius=8)
        f_cu.pack(side="left", fill="both", expand=True, padx=(4, 6))
        ctk.CTkLabel(f_cu, text="🔶 1. Tính Hao Phí Đồng (Copper Give-away)", font=ctk.CTkFont(size=12, weight="bold"), text_color=self.theme["yellow"]).grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=(6, 2))
        self.e_cu_nom = self._make_field(f_cu, 1, "Đường kính chuẩn (mm):", "0.670")
        self.e_cu_act = self._make_field(f_cu, 2, "Đường kính thực đo (mm):", "0.678")
        self.e_cu_ton = self._make_field(f_cu, 3, "Sản lượng đồng/năm (tấn):", "200")
        self.e_cu_prc = self._make_field(f_cu, 4, "Giá đồng (triệu VNĐ/tấn):", "250")

        # Phải: Bẫy tỷ trọng PVC CaCO3
        f_pvc = ctk.CTkFrame(split, fg_color=self.theme["mantle"], corner_radius=8)
        f_pvc.pack(side="right", fill="both", expand=True, padx=(6, 4))
        ctk.CTkLabel(f_pvc, text="🧪 2. Bẫy Tỷ Trọng Nhựa PVC (VNĐ/kg vs VNĐ/lít)", font=ctk.CTkFont(size=12, weight="bold"), text_color=self.theme["peach"]).grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=(6, 2))
        self.e_pvc_pa = self._make_field(f_pvc, 1, "Giá nhựa A hiện tại (đ/kg):", "30000")
        self.e_pvc_sa = self._make_field(f_pvc, 2, "Tỷ trọng nhựa A (g/cm³):", "1.40")
        self.e_pvc_pb = self._make_field(f_pvc, 3, "Giá nhựa B mới (đ/kg):", "28500")
        self.e_pvc_sb = self._make_field(f_pvc, 4, "Tỷ trọng nhựa B (g/cm³):", "1.54")

        ctk.CTkButton(
            tab, text="💰 Tính Thất Thoát Đồng & So Sánh Chi Phí Thể Tích Nhựa PVC", height=32, font=ctk.CTkFont(weight="bold"),
            fg_color=self.theme["yellow"], text_color=self.theme["crust"], command=self._run_material
        ).pack(anchor="w", padx=10, pady=(4, 4))
        self.out_mat = self._make_output_box(tab)
        self._run_material()

    def _run_material(self):
        try:
            cu = calc_copper_giveaway(float(self.e_cu_nom.get()), float(self.e_cu_act.get()), float(self.e_cu_ton.get()), float(self.e_cu_prc.get()))
            pvc = calc_pvc_volume_cost(float(self.e_pvc_pa.get()), float(self.e_pvc_sa.get()), float(self.e_pvc_pb.get()), float(self.e_pvc_sb.get()), 200.0)
            txt = (
                f"🔶 1. PHÂN TÍCH COPPER GIVE-AWAY:\n"
                f"  • % Đồng dư = [(D_thực/D_chuẩn)² − 1] : {cu['pct_giveaway']:+.2f}%\n"
                f"  • Khối lượng đồng thừa / năm          : {cu['extra_tons']:+.2f} tấn/năm\n"
                f"  • Tiền đồng 'biếu không' / năm        : {cu['annual_loss_m_vnd']:+,.1f} triệu VNĐ/năm\n"
                f"  → {cu['advice']}\n\n"
                f"🧪 2. SO SÁNH CHI PHÍ THỰC THEO THỂ TÍCH NHỰA PVC (Quy đổi 200 tấn nhựa A/năm):\n"
                f"  • Chi phí nhựa A (VNĐ/lít)            : {pvc['cost_vol_a']:,.0f} đ/lít\n"
                f"  • Chi phí nhựa B (VNĐ/lít)            : {pvc['cost_vol_b']:,.0f} đ/lít\n"
                f"  → {pvc['verdict']}"
            )
            self._set_output(self.out_mat, txt)
        except Exception as e:
            self._set_output(self.out_mat, f"❌ Lỗi nhập liệu: {e}")

    def _build_cpk_tab(self, tab):
        frm = ctk.CTkFrame(tab, fg_color=self.theme["mantle"], corner_radius=8)
        frm.pack(fill="x", padx=10, pady=8)
        self.e_cpk_usl = self._make_field(frm, 0, "Cận dung sai trên USL (mm, vd dây VC 2.5):", "3.46")
        self.e_cpk_lsl = self._make_field(frm, 1, "Cận dung sai dưới LSL (mm):", "3.26")
        self.e_cpk_mean = self._make_field(frm, 2, "Giá trị trung bình thực đo Mean (mm):", "3.40")
        self.e_cpk_sig = self._make_field(frm, 3, "Độ lệch chuẩn σ thực đo (mm):", "0.020")

        ctk.CTkButton(
            tab, text="🎯 Tính Năng Lực Quá Trình Cp / Cpk", height=32, font=ctk.CTkFont(weight="bold"),
            fg_color=self.theme["cyan"], text_color=self.theme["crust"], command=self._run_cpk
        ).pack(anchor="w", padx=10, pady=(2, 4))
        self.out_cpk = self._make_output_box(tab)
        self._run_cpk()

    def _run_cpk(self):
        try:
            r = calc_cp_cpk(float(self.e_cpk_usl.get()), float(self.e_cpk_lsl.get()), float(self.e_cpk_mean.get()), float(self.e_cpk_sig.get()))
            txt = (
                f"🎯 KẾT QUẢ PHÂN TÍCH NĂNG LỰC QUÁ TRÌNH (SPC / SIX SIGMA):\n"
                f"  • Cp  (Năng lực tiềm năng của máy) : {r['cp']:.3f}\n"
                f"  • Cpu (Cận trên) / Cpl (Cận dưới)  : {r['cpu']:.3f}  /  {r['cpl']:.3f}\n"
                f"  • Cpk (Năng lực thực tế)           : {r['cpk']:.3f}   (≈ {r['sigma_short']:.2f} Sigma ngắn hạn)\n\n"
                f"📌 Đánh giá OE:\n  {r['verdict']}\n"
            )
            if r["shift_note"]:
                txt += f"\n{r['shift_note']}"
            self._set_output(self.out_cpk, txt)
        except Exception as e:
            self._set_output(self.out_cpk, f"❌ Lỗi nhập liệu: {e}")

    def _build_inv_roi_tab(self, tab):
        split = ctk.CTkFrame(tab, fg_color="transparent")
        split.pack(fill="x", padx=6, pady=6)

        f1 = ctk.CTkFrame(split, fg_color=self.theme["mantle"], corner_radius=8)
        f1.pack(side="left", fill="both", expand=True, padx=(4, 6))
        ctk.CTkLabel(f1, text="📦 1. Safety Stock & Điểm Đặt Hàng ROP", font=ctk.CTkFont(size=12, weight="bold"), text_color=self.theme["blue"]).grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=(6, 2))
        self.e_inv_d = self._make_field(f1, 1, "Tiêu thụ TB/ngày (tấn):", "4.0")
        self.e_inv_sd = self._make_field(f1, 2, "Độ lệch chuẩn σ_D (tấn):", "0.8")
        self.e_inv_lt = self._make_field(f1, 3, "Lead Time nhập (ngày):", "12")
        self.e_inv_slt = self._make_field(f1, 4, "Độ lệch σ_LT (ngày):", "2.0")
        self.e_inv_z = self._make_field(f1, 5, "Hệ số Z (95%=1.65; 98%=2.05):", "1.65")

        f2 = ctk.CTkFrame(split, fg_color=self.theme["mantle"], corner_radius=8)
        f2.pack(side="right", fill="both", expand=True, padx=(6, 4))
        ctk.CTkLabel(f2, text="💵 2. Thẩm Định CAPEX — ROI & Payback", font=ctk.CTkFont(size=12, weight="bold"), text_color=self.theme["green"]).grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=(6, 2))
        self.e_roi_cap = self._make_field(f2, 1, "Tổng vốn CAPEX (triệu VNĐ):", "350")
        self.e_roi_sav = self._make_field(f2, 2, "Hard Savings/tháng (triệu):", "42")

        ctk.CTkButton(
            tab, text="📊 Tính Safety Stock / ROP & Hoàn Vốn Payback", height=32, font=ctk.CTkFont(weight="bold"),
            fg_color=self.theme["blue"], text_color=self.theme["crust"], command=self._run_inv_roi
        ).pack(anchor="w", padx=10, pady=(4, 4))
        self.out_inv = self._make_output_box(tab)
        self._run_inv_roi()

    def _run_inv_roi(self):
        try:
            r = calc_inventory_and_roi(
                float(self.e_inv_d.get()), float(self.e_inv_sd.get()), float(self.e_inv_lt.get()),
                float(self.e_inv_slt.get()), float(self.e_inv_z.get()),
                float(self.e_roi_cap.get()), float(self.e_roi_sav.get())
            )
            pb = "∞" if math.isinf(r["payback_months"]) else f"{r['payback_months']:.1f} tháng"
            txt = (
                f"📦 1. HOẠCH ĐỊNH TỒN KHO AN TOÀN (SAFETY STOCK & ROP):\n"
                f"  • Tồn kho an toàn (Safety Stock) : {r['safety_stock']:.2f} tấn\n"
                f"  • Điểm đặt hàng lại (ROP)        : {r['rop']:.2f} tấn (Chạm mức này ERP phát lệnh mua mới!)\n\n"
                f"💵 2. THẨM ĐỊNH HIỆU QUẢ ĐẦU TƯ (CAPEX / ROI / PAYBACK):\n"
                f"  • Thời gian hoàn vốn (Payback)   : {pb}\n"
                f"  • Tỷ suất hoàn vốn năm đầu (ROI) : {r['roi_1yr_pct']:+.1f}%\n"
                f"  → {r['roi_verdict']}"
            )
            self._set_output(self.out_inv, txt)
        except Exception as e:
            self._set_output(self.out_inv, f"❌ Lỗi nhập liệu: {e}")

    def _build_decoder_tab(self, tab):
        top = ctk.CTkFrame(tab, fg_color=self.theme["mantle"], corner_radius=8)
        top.pack(fill="x", padx=10, pady=8)
        ctk.CTkLabel(top, text="🔌 Nhập hoặc bấm chọn nhanh mã cáp CADIVI:", font=ctk.CTkFont(size=12, weight="bold"), text_color=self.theme["cyan"]).pack(anchor="w", padx=10, pady=(8, 4))

        row = ctk.CTkFrame(top, fg_color="transparent")
        row.pack(fill="x", padx=10, pady=(0, 6))
        self.e_code = ctk.CTkEntry(row, height=32, fg_color=self.theme["crust"], border_color=self.theme["surface1"], text_color=self.theme["text"])
        self.e_code.insert(0, "CXV/DSTA 3x120+1x70 - 0.6/1kV")
        self.e_code.pack(side="left", fill="x", expand=True, padx=(0, 8))
        self.e_code.bind("<Return>", lambda _e: self._run_decoder())

        ctk.CTkButton(
            row, text="🔎 Giải Mã Ngay", width=130, height=32, font=ctk.CTkFont(weight="bold"),
            fg_color=self.theme["green"], text_color=self.theme["crust"], command=self._run_decoder
        ).pack(side="right")

        # Nút chọn nhanh 8 mã kinh điển
        chips = ctk.CTkFrame(top, fg_color="transparent")
        chips.pack(fill="x", padx=10, pady=(0, 8))
        samples = ["VC 2.5", "VCmd 2x1.5", "CXV 3x95+1x50", "CXV/DSTA 3x120+1x70", "CXV/DATA 1x300", "CXV/FR 4x16 LSZH", "LV-ABC 4x50", "As 240/32", "H1Z2Z2-K 1x6.0"]
        for s in samples:
            ctk.CTkButton(
                chips, text=s, height=24, width=90, font=ctk.CTkFont(size=10, weight="bold"),
                fg_color=self.theme["surface0"], hover_color=self.theme["blue"], text_color=self.theme["text"],
                command=lambda val=s: self._pick_sample_code(val)
            ).pack(side="left", padx=2, pady=2)

        self.out_dec = self._make_output_box(tab, height=260)
        self._run_decoder()

    def _pick_sample_code(self, code):
        self.e_code.delete(0, "end")
        self.e_code.insert(0, code)
        self._run_decoder()

    def _run_decoder(self):
        try:
            r = decode_cadivi_cable(self.e_code.get())
            lines = [
                f"🔌 KẾT QUẢ GIẢI MÃ MÃ CÁP CADIVI:  {r['raw']}",
                "═" * 74,
                f"• Ruột dẫn (Conductor)    : {r['conductor']}",
                f"• Cách điện (Insulation)  : {r['insulation']}",
                f"• Giáp / Màn chắn / FR    : {r['armor_shield']}",
                f"• Vỏ bọc ngoài (Sheath)   : {r['sheath']}",
                f"• Tiêu chuẩn áp dụng      : {r['standard']}",
                "",
                f"🏭 LƯU TRÌNH MÁY MÓC TẠI NHÀ MÁY CADIVI:",
                f"  {r['route']}",
                "",
                f"🎯 TRỌNG TÂM TỐI ƯU CỦA CHUYÊN VIÊN OE:",
                f"  {r['oe_note']}",
            ]
            if r["warning"]:
                lines.append("\n" + r["warning"])
            self._set_output(self.out_dec, "\n".join(lines))
        except Exception as e:
            self._set_output(self.out_dec, f"❌ {e}")


# =====================================================================
# 3. TRÌNH PHỎNG VẤN THỬ 30 PHÚT CÓ ĐỒNG HỒ & CHẤM ĐIỂM /100
# =====================================================================
class MockInterviewDialog(ctk.CTkToplevel):
    """Mô phỏng 1 buổi phỏng vấn OE CADIVI thật 30 phút (10 câu trộn chuẩn cấu trúc + tự chấm điểm /100)."""
    def __init__(self, parent, theme, questions_list, on_term_click=None):
        super().__init__(parent)
        self.theme = theme
        self.all_questions = questions_list or []
        self.on_term_click = on_term_click
        self.session_qs = build_mock_interview_set(self.all_questions)
        self.idx = 0
        self.scores = {}  # q_index -> 0 / 5 / 10
        self.revealed = set()
        self.remaining_sec = 30 * 60
        self.timer_running = False
        self._timer_after = None

        self.title("🎤 Phỏng Vấn Thử 30 Phút — Chuyên Viên OE Nhà Máy CADIVI Miền Trung")
        self.geometry("920x680")
        self.minsize(740, 560)
        self.configure(fg_color=theme["base"])
        self.transient(parent)
        self.bind("<Escape>", lambda _e: self._on_close())
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        self._build_ui()
        self._render_question()
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def _on_close(self):
        self.timer_running = False
        if self._timer_after:
            try:
                self.after_cancel(self._timer_after)
            except Exception:
                pass
        self.destroy()

    def _build_ui(self):
        t = self.theme
        top = ctk.CTkFrame(self, fg_color=t["mantle"], corner_radius=8)
        top.pack(fill="x", padx=14, pady=(12, 8), ipady=6)

        self.lbl_prog = ctk.CTkLabel(top, text="Câu 1 / 10", font=ctk.CTkFont(size=15, weight="bold"), text_color=t["cyan"])
        self.lbl_prog.pack(side="left", padx=14)

        self.lbl_score = ctk.CTkLabel(top, text="🏆 Điểm: 0 / 100", font=ctk.CTkFont(size=13, weight="bold"), text_color=t["green"])
        self.lbl_score.pack(side="left", padx=10)

        self.lbl_timer = ctk.CTkLabel(top, text="⏱️ 30:00", font=ctk.CTkFont(family="Consolas", size=16, weight="bold"), text_color=t["yellow"])
        self.lbl_timer.pack(side="right", padx=14)

        self.btn_timer = ctk.CTkButton(top, text="▶ Bắt đầu 30p", width=110, height=28, fg_color=t["green"], text_color=t["crust"], font=ctk.CTkFont(weight="bold"), command=self._toggle_timer)
        self.btn_timer.pack(side="right", padx=4)

        ctk.CTkButton(top, text="🎲 Đề mới", width=85, height=28, fg_color=t["surface0"], hover_color=t["blue"], text_color=t["text"], command=self._new_deck).pack(side="right", padx=4)

        # Khung câu hỏi + đáp án
        self.lbl_cat = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=12, weight="bold"), text_color=t["peach"], anchor="w")
        self.lbl_cat.pack(fill="x", padx=18, pady=(2, 2))

        self.txt_q = ctk.CTkTextbox(self, height=110, fg_color=t["surface0"], text_color="#ffffff", font=ctk.CTkFont(size=14, weight="bold"), wrap="word", corner_radius=8)
        self.txt_q.pack(fill="x", padx=14, pady=(0, 8))

        mid_bar = ctk.CTkFrame(self, fg_color="transparent")
        mid_bar.pack(fill="x", padx=14, pady=(0, 6))

        self.btn_reveal = ctk.CTkButton(
            mid_bar, text="👁️ Hiện Gợi Ý Trả Lời (Sau khi bạn tự nói xong)", height=30,
            font=ctk.CTkFont(size=12, weight="bold"), fg_color=t["blue"], text_color=t["crust"],
            command=self._toggle_reveal
        )
        self.btn_reveal.pack(side="left")

        ctk.CTkLabel(mid_bar, text="Tự chấm câu này:", font=ctk.CTkFont(size=12, weight="bold"), text_color=t["subtext"]).pack(side="right", padx=(10, 6))
        self.btn_s10 = ctk.CTkButton(mid_bar, text="✅ 10đ (Tự tin)", width=106, height=28, fg_color=t["surface0"], hover_color=t["green"], text_color=t["text"], command=lambda: self._score(10))
        self.btn_s10.pack(side="right", padx=2)
        self.btn_s5 = ctk.CTkButton(mid_bar, text="🟡 5đ (Tạm ổn)", width=104, height=28, fg_color=t["surface0"], hover_color=t["yellow"], text_color=t["text"], command=lambda: self._score(5))
        self.btn_s5.pack(side="right", padx=2)
        self.btn_s0 = ctk.CTkButton(mid_bar, text="❌ 0đ (Cần ôn)", width=104, height=28, fg_color=t["surface0"], hover_color=t["red"], text_color=t["text"], command=lambda: self._score(0))
        self.btn_s0.pack(side="right", padx=2)

        self.txt_ans = ctk.CTkTextbox(self, fg_color=t["crust"], text_color=t["text"], font=ctk.CTkFont(size=12), wrap="word", corner_radius=8)
        self.txt_ans.pack(fill="both", expand=True, padx=14, pady=(0, 10))

        # Thanh điều hướng cuối
        bot = ctk.CTkFrame(self, fg_color="transparent")
        bot.pack(fill="x", padx=14, pady=(0, 12))

        self.btn_prev = ctk.CTkButton(bot, text="⬅ Câu trước", width=110, height=32, fg_color=t["surface0"], hover_color=t["blue"], command=lambda: self._step(-1))
        self.btn_prev.pack(side="left")

        self.btn_next = ctk.CTkButton(bot, text="Câu tiếp ➡", width=110, height=32, fg_color=t["blue"], text_color=t["crust"], font=ctk.CTkFont(weight="bold"), command=lambda: self._step(1))
        self.btn_next.pack(side="left", padx=8)

        ctk.CTkButton(bot, text="📊 Xem Tổng Kết & Chẩn Đoán Điểm Yếu", width=260, height=32, fg_color=t["mauve"], text_color=t["crust"], font=ctk.CTkFont(weight="bold"), command=self._show_summary).pack(side="right")

    def _toggle_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.btn_timer.configure(text="▶ Tiếp tục", fg_color=self.theme["green"])
        else:
            self.timer_running = True
            self.btn_timer.configure(text="⏸ Tạm dừng", fg_color=self.theme["peach"])
            self._tick()

    def _tick(self):
        if not self.timer_running or not self.winfo_exists():
            return
        if self.remaining_sec > 0:
            self.remaining_sec -= 1
            m, s = divmod(self.remaining_sec, 60)
            col = self.theme["red"] if self.remaining_sec < 300 else self.theme["yellow"]
            self.lbl_timer.configure(text=f"⏱️ {m:02d}:{s:02d}", text_color=col)
            self._timer_after = self.after(1000, self._tick)
        else:
            self.timer_running = False
            self.lbl_timer.configure(text="⏱️ 00:00 HẾT GIỜ!", text_color=self.theme["red"])
            self._show_summary()

    def _new_deck(self):
        self.session_qs = build_mock_interview_set(self.all_questions)
        self.idx = 0
        self.scores = {}
        self.revealed = set()
        self.remaining_sec = 30 * 60
        self.timer_running = False
        self.lbl_timer.configure(text="⏱️ 30:00", text_color=self.theme["yellow"])
        self.btn_timer.configure(text="▶ Bắt đầu 30p", fg_color=self.theme["green"])
        self._render_question()

    def _clean(self, txt):
        if term_glossary:
            txt = term_glossary.strip_term_formulas(txt)
        return txt.replace("**", "").replace("`", "")

    def _render_question(self):
        if not self.session_qs:
            return
        q = self.session_qs[self.idx]
        total = len(self.session_qs)
        tot_pts = sum(self.scores.values())
        self.lbl_prog.configure(text=f"Câu {self.idx + 1} / {total}")
        self.lbl_score.configure(text=f"🏆 Điểm: {tot_pts} / {total * 10}  (Đã chấm: {len(self.scores)}/{total})")
        self.lbl_cat.configure(text=f"📌 Chủ đề: {q.get('category', '')}   •   [{q.get('type', '')}]")

        self.txt_q.configure(state="normal")
        self.txt_q.delete("1.0", "end")
        self.txt_q.insert("1.0", self._clean(q.get("question", "")))
        self.txt_q.configure(state="disabled")

        self.txt_ans.configure(state="normal")
        self.txt_ans.delete("1.0", "end")
        if self.idx in self.revealed:
            self.txt_ans.insert("1.0", "💡 GỢI Ý TRẢ LỜI CHUẨN CHUYÊN GIA:\n\n" + self._clean(q.get("key_points", "")))
            self.btn_reveal.configure(text="🙈 Ẩn Gợi Ý Trả Lời")
        else:
            self.txt_ans.insert("1.0", "\n\n    🎤 Hãy bấm '▶ Bắt đầu 30p' và TỰ TRẢ LỜI THÀNH TIẾNG trong 2–3 phút như đang ngồi trước Hội đồng CADIVI.\n\n    Sau khi nói xong, bấm nút '👁️ Hiện Gợi Ý Trả Lời' để đối chiếu và tự chấm điểm 0 / 5 / 10!")
            self.btn_reveal.configure(text="👁️ Hiện Gợi Ý Trả Lời (Sau khi tự nói xong)")
        self.txt_ans.configure(state="disabled")

        cur_sc = self.scores.get(self.idx)
        self.btn_s0.configure(fg_color=self.theme["red"] if cur_sc == 0 else self.theme["surface0"], text_color=self.theme["crust"] if cur_sc == 0 else self.theme["text"])
        self.btn_s5.configure(fg_color=self.theme["yellow"] if cur_sc == 5 else self.theme["surface0"], text_color=self.theme["crust"] if cur_sc == 5 else self.theme["text"])
        self.btn_s10.configure(fg_color=self.theme["green"] if cur_sc == 10 else self.theme["surface0"], text_color=self.theme["crust"] if cur_sc == 10 else self.theme["text"])

        self.btn_prev.configure(state="normal" if self.idx > 0 else "disabled")
        self.btn_next.configure(state="normal" if self.idx < total - 1 else "disabled")

    def _toggle_reveal(self):
        if self.idx in self.revealed:
            self.revealed.discard(self.idx)
        else:
            self.revealed.add(self.idx)
        self._render_question()

    def _score(self, pts):
        self.scores[self.idx] = pts
        self._render_question()

    def _step(self, delta):
        if not self.session_qs:
            return
        self.idx = max(0, min(len(self.session_qs) - 1, self.idx + delta))
        self._render_question()

    def _show_summary(self):
        total = len(self.session_qs)
        pts = sum(self.scores.values())
        weak = [f"• Câu {i+1} ({self.scores.get(i, 0)}đ): {self.session_qs[i].get('category', '')}" for i in range(total) if self.scores.get(i, 0) < 10]
        if pts >= 85:
            verdict = "🏆 XUẤT SẮC! Bạn hoàn toàn sẵn sàng chinh phục phỏng vấn CADIVI & tự tin đàm phán mức đầu khung 17–18 triệu!"
        elif pts >= 70:
            verdict = "🟢 KHÁ TỐT! Chỉ cần ôn lại nhanh các câu < 10đ bên dưới là đạt phong độ đỉnh cao."
        else:
            verdict = "🟡 CẦN ÔN THÊM! Mở lại Tab 🏭 Dòng Chảy CADIVI & 🎓 Giáo Trình A–Z luyện các mảng yếu rồi thi thử lại."

        summary = [
            f"📊 KẾT QUẢ PHỎNG VẤN THỬ 30 PHÚT CADIVI OE",
            f"  • Tổng điểm đạt được: {pts} / {total * 10}  (Đã chấm {len(self.scores)}/{total} câu)",
            f"  • Đánh giá: {verdict}",
            "",
            "🎯 CÁC CÂU / CHỦ ĐỀ CẦN ÔN LẠI NGAY:" if weak else "🎉 Tuyệt vời! Không có câu nào dưới 10 điểm!"
        ] + weak
        self.txt_ans.configure(state="normal")
        self.txt_ans.delete("1.0", "end")
        self.txt_ans.insert("1.0", "\n".join(summary))
        self.txt_ans.configure(state="disabled")


# =====================================================================
# 4. BỘ SINH FILE EXCEL THỰC HÀNH VÒNG 2 CHUẨN OOXML (.XLSX — 0 PHỤ THUỘC)
# =====================================================================
def _excel_col_letter(idx):
    s = ""
    while idx > 0:
        idx, rem = divmod(idx - 1, 26)
        s = chr(65 + rem) + s
    return s


def export_practice_workbook(filepath="BaiTap_ThucHanh_Vong2_OE_CADIVI.xlsx"):
    """
    Sinh file Excel thực hành Vòng 2 chuẩn ECMA-376 (.xlsx) không cần openpyxl,
    gồm 6 sheet có sẵn dữ liệu thô + công thức Excel sống (SUM, AVERAGE, IF).
    """
    import zipfile
    from xml.sax.saxutils import escape

    sheets = []

    def add_sheet(name, rows, col_widths):
        sheets.append((name[:31], rows, col_widths))

    # --- SHEET 1: 1_Raw_Log_5_Ca ---
    s1_rows = [
        (1, [(1, "BÀI TẬP THỰC HÀNH VÒNG 2 (ĐỀ 1) — DỮ LIỆU THÔ 5 CA MÁY ĐÙN #2 (DÂY VC 2.5mm² — TỐC ĐỘ CHUẨN 320 m/phút)", 1, False)]),
        (2, [(1, "Hướng dẫn: Ô màu vàng có thể thay đổi số để thực hành. Toàn bộ công thức OEE & Pareto tự tính ở Sheet 2!", 15, False)]),
        (4, [
            (1, "Ca SX", 2, False), (2, "Giờ KH (phút)", 2, False), (3, "Tốc độ chuẩn (m/p)", 2, False),
            (4, "Dừng Đổi màu (p)", 2, False), (5, "Dừng Hỏng máy (p)", 2, False), (6, "Dừng Chờ rulo (p)", 2, False),
            (7, "Dừng Vặt/Spark (p)", 2, False), (8, "Tổng Dừng (p)", 2, False), (9, "Giờ Chạy Thực (p)", 2, False),
            (10, "Tổng SL (mét)", 2, False), (11, "Phế phẩm (mét)", 2, False), (12, "SL Đạt (mét)", 2, False),
            (13, "OEE Ca (%)", 2, False),
        ]),
    ]
    raw_shifts = [
        ("Ca 1 - T2", 450, 320, 45, 0,  10, 5,  108000, 2500),
        ("Ca 2 - T2", 450, 320, 55, 25, 0,  10,  96000, 3200),
        ("Ca 1 - T3", 450, 320, 0,  0,  15, 5,  124000, 1800),
        ("Ca 2 - T3", 450, 320, 50, 15, 5,  10, 102000, 3800),
        ("Ca 1 - T4", 450, 320, 20, 0,  0,  5,  118000, 2700),
    ]
    for i, (ca, plan, spd, d_col, d_brk, d_mat, d_min, tot_m, scr_m) in enumerate(raw_shifts, start=5):
        s1_rows.append((i, [
            (1, ca, 3, False), (2, plan, 14, False), (3, spd, 14, False),
            (4, d_col, 14, False), (5, d_brk, 14, False), (6, d_mat, 14, False), (7, d_min, 14, False),
            (8, f"=SUM(D{i}:G{i})", 4, True),
            (9, f"=B{i}-H{i}", 4, True),
            (10, tot_m, 14, False), (11, scr_m, 14, False),
            (12, f"=J{i}-K{i}", 4, True),
            (13, f"=(I{i}/B{i})*(J{i}/(I{i}*C{i}))*(L{i}/J{i})", 6, True),
        ]))
    s1_rows.append((10, [
        (1, "TỔNG 5 CA", 7, False),
        (2, "=SUM(B5:B9)", 8, True), (3, "=AVERAGE(C5:C9)", 8, True),
        (4, "=SUM(D5:D9)", 8, True), (5, "=SUM(E5:E9)", 8, True), (6, "=SUM(F5:F9)", 8, True), (7, "=SUM(G5:G9)", 8, True),
        (8, "=SUM(H5:H9)", 8, True), (9, "=SUM(I5:I9)", 8, True),
        (10, "=SUM(J5:J9)", 8, True), (11, "=SUM(K5:K9)", 8, True), (12, "=SUM(L5:L9)", 8, True),
        (13, "=(I10/B10)*(J10/(I10*C10))*(L10/J10)", 9, True),
    ]))
    add_sheet("1_Raw_Log_5_Ca", s1_rows, {1: 14, 2: 14, 3: 16, 4: 16, 5: 16, 6: 16, 7: 16, 8: 14, 9: 16, 10: 15, 11: 14, 12: 15, 13: 13})

    # --- SHEET 2: 2_Giai_OEE_Pareto ---
    s2_rows = [
        (1, [(1, "ĐÁP ÁN ĐỀ 1 — TÍNH OEE CÓ TRỌNG SỐ CHUẨN, BẪY AVERAGE() & PHÂN TÍCH PARETO 80/20", 1, False)]),
        (3, [(1, "Chỉ số OEE Tổng 5 Ca", 2, False), (2, "Công thức chuẩn OE", 2, False), (3, "Kết quả", 2, False), (4, "Ghi chú thực chiến CADIVI", 2, False)]),
        (4, [(1, "Availability (A — Độ khả dụng)", 3, False), (2, "Tổng Giờ Chạy / Tổng Giờ KH", 3, False), (3, "='1_Raw_Log_5_Ca'!I10/'1_Raw_Log_5_Ca'!B10", 6, True), (4, "Mất 275p dừng máy / 2,250p kế hoạch", 3, False)]),
        (5, [(1, "Performance (P — Tốc độ chạy)", 3, False), (2, "Tổng SL (m) / (Giờ Chạy × 320 m/p)", 3, False), (3, "='1_Raw_Log_5_Ca'!J10/('1_Raw_Log_5_Ca'!I10*'1_Raw_Log_5_Ca'!C10)", 6, True), (4, "Tốc độ thực bình quân = 277.5 m/p (chậm -13.3% so chuẩn!)", 3, False)]),
        (6, [(1, "Quality (Q — Chất lượng)", 3, False), (2, "Tổng SL Đạt / Tổng SL Chạy", 3, False), (3, "='1_Raw_Log_5_Ca'!L10/'1_Raw_Log_5_Ca'!J10", 6, True), (4, "14,000m phế đầu ca & lỗi Spark cần cắt bằng SMED/SPC", 3, False)]),
        (7, [(1, "TỔNG OEE CHUẨN (Có trọng số)", 7, False), (2, "A × P × Q (= Good Meters / Ideal Max)", 7, False), (3, "=C4*C5*C6", 9, True), (4, "CHÍNH XÁC 74.17% (534,000 / 720,000m) — Luôn dùng SUM tổng trước khi chia!", 7, False)]),
        (8, [(1, "⚠️ BẪY SAI: Dùng AVERAGE(OEE 5 ca)", 10, False), (2, "Trung bình cộng đơn giản 5 ca", 10, False), (3, "=AVERAGE('1_Raw_Log_5_Ca'!M5:M9)", 13, True), (4, "Nếu số giờ KH mỗi ca khác nhau (ca ngắn/ca dài), AVERAGE() sẽ SAI NẶNG!", 10, False)]),
        (10, [(1, "PHÂN TÍCH PARETO 80/20 NGUYÊN NHÂN DỪNG MÁY (275 PHÚT)", 15, False)]),
        (11, [(1, "Nguyên nhân dừng máy (Xếp giảm dần)", 2, False), (2, "Tổng phút dừng", 2, False), (3, "% Đóng góp", 2, False), (4, "% Tích lũy (Pareto)", 2, False)]),
        (12, [(1, "1. Đổi màu / Đổi tiết diện (SMED)", 7, False), (2, "='1_Raw_Log_5_Ca'!D10", 8, True), (3, "=B12/$B$16", 9, True), (4, "=C12", 9, True)]),
        (13, [(1, "2. Hỏng máy đột xuất (Breakdown / TPM)", 3, False), (2, "='1_Raw_Log_5_Ca'!E10", 4, True), (3, "=B13/$B$16", 6, True), (4, "=D12+C13", 6, True)]),
        (14, [(1, "3. Dừng vặt / Lỗi Spark (Minor Stops)", 3, False), (2, "='1_Raw_Log_5_Ca'!G10", 4, True), (3, "=B14/$B$16", 6, True), (4, "=D13+C14", 6, True)]),
        (15, [(1, "4. Chờ rulo đồng / xe nâng (Kanban/Andon)", 3, False), (2, "='1_Raw_Log_5_Ca'!F10", 4, True), (3, "=B15/$B$16", 6, True), (4, "=D14+C15", 6, True)]),
        (16, [(1, "TỔNG THỜI GIAN DỪNG MÁY", 7, False), (2, "=SUM(B12:B15)", 8, True), (3, "=SUM(C12:C15)", 9, True), (4, "➤ Riêng Đổi màu chiếm 61.8% — Đánh SMED + Color Sequencing đầu tiên!", 7, False)]),
    ]
    add_sheet("2_Giai_OEE_Pareto", s2_rows, {1: 42, 2: 34, 3: 16, 4: 56})

    # --- SHEET 3: 3_BOM_Giveaway_PVC ---
    s3_rows = [
        (1, [(1, "BÀI TẬP TỐI ƯU VẬT TƯ CÁP — COPPER GIVE-AWAY & BẪY TỶ TRỌNG NHỰA PVC (CaCO3)", 1, False)]),
        (3, [(1, "PHẦN A: TÍNH HAO PHÍ ĐỒNG BIẾU KHÔNG (COPPER GIVE-AWAY) — DÂY VC 2.5mm² (7 SỢI Ø0.67mm)", 15, False)]),
        (4, [(1, "Thông số", 2, False), (2, "Giá trị", 2, False), (3, "Đơn vị", 2, False), (4, "Diễn giải", 2, False)]),
        (5, [(1, "Đường kính sợi đồng danh định (D_chuẩn)", 3, False), (2, 0.670, 11, False), (3, "mm", 3, False), (4, "Thiết kế đạt chuẩn điện trở IEC 60228", 3, False)]),
        (6, [(1, "Đường kính thực đo do khuôn PCD mòn (D_thực)", 3, False), (2, 0.678, 11, False), (3, "mm", 3, False), (4, "Chỉ to hơn +0.008mm (bằng 1/10 sợi tóc!)", 3, False)]),
        (7, [(1, "Sản lượng đồng kéo hàng năm cho mã dây", 3, False), (2, 200, 14, False), (3, "tấn/năm", 3, False), (4, "Nhập sản lượng thực tế nhà máy", 3, False)]),
        (8, [(1, "Đơn giá đồng nguyên liệu", 3, False), (2, 250, 14, False), (3, "triệu/tấn", 3, False), (4, "Giá đồng Cathode / Rod bình quân", 3, False)]),
        (9, [(1, "% Đồng biếu không = (D_thực/D_chuẩn)² − 1", 7, False), (2, "=(B6/B5)^2-1", 9, True), (3, "%", 7, False), (4, "Diện tích tiết diện tỷ lệ BÌNH PHƯƠNG đường kính!", 7, False)]),
        (10, [(1, "Khối lượng đồng thất thoát / năm", 7, False), (2, "=B7*B9", 12, True), (3, "tấn/năm", 7, False), (4, "Đồng biếu không khách hàng trong từng mét dây", 7, False)]),
        (11, [(1, "TIỀN THẤT THOÁT DO COPPER GIVE-AWAY / NĂM", 10, False), (2, "=B10*B8", 12, True), (3, "triệu VNĐ/năm", 10, False), (4, "Chỉ 0.008mm mòn khuôn đã làm bay 1.2 TỶ VNĐ/năm!", 10, False)]),
        (13, [(1, "PHẦN B: BẪY TỶ TRỌNG NHỰA PVC (BỘT ĐÁ CaCO3) — MUA RẺ THEO KG NHƯNG ĐẮT THEO MÉT CÁP!", 15, False)]),
        (14, [(1, "Hạng mục so sánh", 2, False), (2, "Nhựa A (Hiện tại)", 2, False), (3, "Nhựa B (Giá rẻ hơn)", 2, False), (4, "Chênh lệch (B vs A)", 2, False)]),
        (15, [(1, "Đơn giá mua theo khối lượng (VNĐ/kg)", 3, False), (2, 30000, 14, False), (3, 28500, 14, False), (4, "=(C15-B15)/B15", 6, True)]),
        (16, [(1, "Tỷ trọng riêng Specific Gravity (kg/lít = g/cm³)", 3, False), (2, 1.40, 11, False), (3, 1.54, 11, False), (4, "=(C16-B16)/B16", 6, True)]),
        (17, [(1, "CHI PHÍ THỰC THEO THỂ TÍCH (VNĐ / LÍT LỚP VỎ)", 7, False), (2, "=B15*B16", 8, True), (3, "=C15*C16", 8, True), (4, "=(C17-B17)/B17", 13, True)]),
        (18, [(1, "Kết luận OE cho Phòng Mua Hàng", 10, False), (2, '=IF(C17>B17,"PHẢN ĐỐI: Nhựa B ĐẮT HƠN theo mét cáp!","XEM XÉT: Chạy MOC & Aging Oven 7 ngày")', 10, True), (3, "Chênh lệch trên 200 tấn nhựa A (triệu/năm):", 3, False), (4, "=(C17-B17)*(200000/B16)/1000000", 12, True)]),
    ]
    add_sheet("3_BOM_Giveaway_PVC", s3_rows, {1: 48, 2: 22, 3: 24, 4: 48})

    # --- SHEET 4: 4_RCCP_Tai_122% ---
    s4_rows = [
        (1, [(1, "ĐÁP ÁN ĐỀ 2 — GIẢI CỨU XƯỞNG ĐÙN QUÁ TẢI 122% MÙA CAO ĐIỂM KHÔNG MUA MÁY MỚI (TOC + SMED)", 1, False)]),
        (3, [(1, "Hạng mục Hoạch định Năng lực Thô (RCCP)", 2, False), (2, "Giá trị", 2, False), (3, "Đơn vị", 2, False), (4, "Ghi chú", 2, False)]),
        (4, [(1, "Số máy đùn cổ chai", 3, False), (2, 4, 14, False), (3, "máy", 3, False), (4, "Xưởng Đùn CADIVI Miền Trung", 3, False)]),
        (5, [(1, "Giờ kế hoạch chuẩn / máy / tháng (26 ngày × 15h)", 3, False), (2, 390, 14, False), (3, "giờ/máy", 3, False), (4, "2 ca chuẩn 7.5h kế hoạch/ca", 3, False)]),
        (6, [(1, "OEE thực tế lịch sử của Xưởng Đùn", 3, False), (2, 0.65, 11, False), (3, "%", 3, False), (4, "Luôn nhân OEE thực khi tính RCCP!", 3, False)]),
        (7, [(1, "Năng lực khả dụng thực tế ban đầu", 7, False), (2, "=B4*B5*B6", 12, True), (3, "giờ ròng/tháng", 7, False), (4, "4 × 390 × 65% = 1,014 giờ ròng", 7, False)]),
        (8, [(1, "Nhu cầu giờ máy tháng cao điểm (+35% đơn hàng)", 3, False), (2, 1240, 14, False), (3, "giờ ròng/tháng", 3, False), (4, "Đề bài Case Study Vòng 2", 3, False)]),
        (9, [(1, "Tỷ lệ tải ban đầu (Load %) & Giờ thiếu hụt", 10, False), (2, "=B8/B7", 13, True), (3, "Thiếu (giờ):", 10, False), (4, "=B8-B7", 12, True)]),
        (11, [(1, "GÓI 4 GIẢI PHÁP TOC / SMED KHÔNG TỐN CAPEX (KHAI THÁC CỔ CHAI TRƯỚC KHI MUA MÁY!)", 15, False)]),
        (12, [(1, "Giải pháp OE cụ thể", 2, False), (2, "Giờ giải phóng/tháng", 2, False), (3, "Chi phí CAPEX", 2, False), (4, "Cách thực thi hiện trường", 2, False)]),
        (13, [(1, "1. SMED + Color Sequencing (giảm đổi màu 50p → 15p)", 3, False), (2, 95, 14, False), (3, "0 đồng", 3, False), (4, "Tách External, sấy sẵn Tip/Die, bánh xe màu Sáng→Tối", 3, False)]),
        (14, [(1, "2. Ăn ca luân phiên (Hot-seat) không tắt máy cổ chai", 3, False), (2, 48, 14, False), (3, "0 đồng", 3, False), (4, "Điều phối 1 thợ đa năng thay ăn trưa cho 4 máy đùn", 3, False)]),
        (15, [(1, "3. Chuyển dây nhỏ sang máy tốc độ cao / đúng L/D", 3, False), (2, 55, 14, False), (3, "0 đồng", 3, False), (4, "Phân tuyến chuẩn: L/D 20 chạy PVC, L/D 26 chạy XLPE", 3, False)]),
        (16, [(1, "4. Dời toàn bộ bảo trì PM sang khung nghỉ Chủ nhật", 3, False), (2, 52, 14, False), (3, "Tăng ca nhỏ", 3, False), (4, "Bảo toàn 100% thời gian chạy máy cổ chai trong tuần", 3, False)]),
        (17, [(1, "TỔNG NĂNG LỰC MỚI SAU GIẢI PHÓNG", 7, False), (2, "=B7+SUM(B13:B16)", 12, True), (3, "Load % mới:", 7, False), (4, "=B8/B17", 9, True)]),
    ]
    add_sheet("4_RCCP_Tai_122%", s4_rows, {1: 48, 2: 20, 3: 18, 4: 50})

    # --- SHEET 5: 5_ROI_Payback_3KichBan ---
    s5_rows = [
        (1, [(1, "ĐÁP ÁN ĐỀ 3 — THẨM ĐỊNH CAPEX LASER GAUGE CLOSED-LOOP (3 KỊCH BẢN ĐỘ NHẠY)", 1, False)]),
        (3, [(1, "Thông số Đầu vào Dự án", 2, False), (2, "Kịch bản Thận trọng (-25%)", 2, False), (3, "Kịch bản Cơ sở (Base)", 2, False), (4, "Kịch bản Lạc quan (+20%)", 2, False)]),
        (4, [(1, "Tổng vốn đầu tư CAPEX (Máy + Lắp đặt, triệu VNĐ)", 3, False), (2, 350, 14, False), (3, 350, 14, False), (4, 350, 14, False)]),
        (5, [(1, "Chi phí bảo trì / hiệu chuẩn OPEX (triệu/năm)", 3, False), (2, 18, 14, False), (3, 18, 14, False), (4, 18, 14, False)]),
        (6, [(1, "Hard Savings giảm Over-thickness nhựa (triệu/tháng)", 3, False), (2, "=C6*0.75", 12, True), (3, 34, 14, False), (4, "=C6*1.20", 12, True)]),
        (7, [(1, "Hard Savings giảm phế đầu ca & lỗi Spark (triệu/tháng)", 3, False), (2, "=C7*0.75", 12, True), (3, 11, 14, False), (4, "=C7*1.20", 12, True)]),
        (8, [(1, "Tổng Hard Savings ròng / tháng (trừ OPEX/12)", 7, False), (2, "=B6+B7-B5/12", 12, True), (3, "=C6+C7-C5/12", 12, True), (4, "=D6+D7-D5/12", 12, True)]),
        (9, [(1, "THỜI GIAN HOÀN VỐN PAYBACK (THÁNG)", 7, False), (2, "=B4/B8", 12, True), (3, "=C4/C8", 12, True), (4, "=D4/D8", 12, True)]),
        (10, [(1, "TỶ SUẤT HOÀN VỐN NĂM ĐẦU ROI (%)", 7, False), (2, "=(B8*12-B4)/B4", 9, True), (3, "=(C8*12-C4)/C4", 9, True), (4, "=(D8*12-D4)/D4", 9, True)]),
        (11, [(1, "Đánh giá duyệt đầu tư", 7, False), (2, '=IF(B9<=12,"DUYỆT NGAY (<12 tháng)","Cân nhắc")', 7, True), (3, '=IF(C9<=12,"DUYỆT NGAY (<12 tháng)","Cân nhắc")', 7, True), (4, '=IF(D9<=12,"DUYỆT NGAY (<12 tháng)","Cân nhắc")', 7, True)]),
    ]
    add_sheet("5_ROI_Payback_3KichBan", s5_rows, {1: 48, 2: 26, 3: 24, 4: 26})

    # --- SHEET 6: 6_SoSanh_Offer_Nam ---
    s6_rows = [
        (1, [(1, "BẢNG TỰ SO SÁNH TỔNG THU NHẬP NĂM (TOTAL COMPENSATION): CÔNG TY CŨ vs OFFER CADIVI", 1, False)]),
        (2, [(1, "Hướng dẫn: Nhập con số thực tế của bạn vào các ô màu vàng (đơn vị: triệu VNĐ) để so sánh chính xác cả năm!", 15, False)]),
        (4, [(1, "Cấu phần Thu nhập / Chi phí (Triệu VNĐ)", 2, False), (2, "Hiện tại (VD: Mabuchi)", 2, False), (3, "Offer CADIVI Miền Trung", 2, False), (4, "Chênh lệch (CADIVI − Cũ)", 2, False)]),
        (5, [(1, "1. Lương cơ bản thực nhận / tháng", 3, False), (2, 15.0, 11, False), (3, 17.5, 11, False), (4, "=C5-B5", 5, True)]),
        (6, [(1, "2. Phụ cấp cố định / tháng (ăn, xăng, chuyên cần, chức vụ)", 3, False), (2, 1.5, 11, False), (3, 1.5, 11, False), (4, "=C6-B6", 5, True)]),
        (7, [(1, "➤ Tổng thu nhập cố định 12 tháng = (1+2) × 12", 7, False), (2, "=(B5+B6)*12", 12, True), (3, "=(C5+C6)*12", 12, True), (4, "=C7-B7", 12, True)]),
        (8, [(1, "3. Thưởng Tháng 13 (triệu/năm)", 3, False), (2, 15.0, 11, False), (3, 17.5, 11, False), (4, "=C8-B8", 5, True)]),
        (9, [(1, "4. Thưởng KPI / Hiệu quả SXKD / Thưởng Tết & Lễ (triệu/năm)", 3, False), (2, 20.0, 11, False), (3, 25.0, 11, False), (4, "=C9-B9", 5, True)]),
        (10, [(1, "5. Phúc lợi quy đổi khác (du lịch, BH sức khỏe, quà lễ/năm)", 3, False), (2, 5.0, 11, False), (3, 6.0, 11, False), (4, "=C10-B10", 5, True)]),
        (11, [(1, "6. Trừ (-) Chi phí xăng xe & hao mòn đi lại cả năm", 3, False), (2, 7.2, 11, False), (3, 4.8, 11, False), (4, "=C11-B11", 5, True)]),
        (12, [(1, "🏆 TỔNG THU NHẬP RÒNG CẢ NĂM (TRIỆU VNĐ / NĂM)", 7, False), (2, "=B7+B8+B9+B10-B11", 12, True), (3, "=C7+C8+C9+C10-C11", 12, True), (4, "=C12-B12", 12, True)]),
        (13, [(1, "💵 BÌNH QUÂN THỰC NHẬN QUY ĐỔI / THÁNG (÷ 12)", 7, False), (2, "=B12/12", 12, True), (3, "=C12/12", 12, True), (4, "=C13-B13", 12, True)]),
    ]
    add_sheet("6_SoSanh_Offer_Nam", s6_rows, {1: 52, 2: 24, 3: 24, 4: 26})

    styles_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <numFmts count="3">
    <numFmt numFmtId="164" formatCode="#,##0"/>
    <numFmt numFmtId="165" formatCode="#,##0.00"/>
    <numFmt numFmtId="166" formatCode="0.00%"/>
  </numFmts>
  <fonts count="5">
    <font><sz val="11"/><name val="Segoe UI"/></font>
    <font><b/><sz val="13"/><color rgb="FFFFFFFF"/><name val="Segoe UI"/></font>
    <font><b/><sz val="11"/><color rgb="FFFFFFFF"/><name val="Segoe UI"/></font>
    <font><b/><sz val="11"/><color rgb="FF0F5132"/><name val="Segoe UI"/></font>
    <font><b/><sz val="11"/><color rgb="FF842029"/><name val="Segoe UI"/></font>
  </fonts>
  <fills count="7">
    <fill><patternFill patternType="none"/></fill>
    <fill><patternFill patternType="gray125"/></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FF1E3A5F"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FF2B5B84"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FFD9F2E6"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FFFADBD8"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FFFFF9DB"/></patternFill></fill>
  </fills>
  <borders count="2">
    <border><left/><right/><top/><bottom/><diagonal/></border>
    <border>
      <left style="thin"><color rgb="FFBFBFBF"/></left>
      <right style="thin"><color rgb="FFBFBFBF"/></right>
      <top style="thin"><color rgb="FFBFBFBF"/></top>
      <bottom style="thin"><color rgb="FFBFBFBF"/></bottom>
      <diagonal/>
    </border>
  </borders>
  <cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
  <cellXfs count="16">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>
    <xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment vertical="center"/></xf>
    <xf numFmtId="0" fontId="2" fillId="3" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment horizontal="center" vertical="center" wrapText="1"/></xf>
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1" applyAlignment="1"><alignment vertical="center" wrapText="1"/></xf>
    <xf numFmtId="164" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1"/>
    <xf numFmtId="165" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1"/>
    <xf numFmtId="166" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="3" fillId="4" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment vertical="center" wrapText="1"/></xf>
    <xf numFmtId="164" fontId="3" fillId="4" borderId="1" xfId="0" applyNumberFormat="1" applyFont="1" applyFill="1" applyBorder="1"/>
    <xf numFmtId="166" fontId="3" fillId="4" borderId="1" xfId="0" applyNumberFormat="1" applyFont="1" applyFill="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="4" fillId="5" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment vertical="center" wrapText="1"/></xf>
    <xf numFmtId="165" fontId="0" fillId="6" borderId="1" xfId="0" applyNumberFormat="1" applyFill="1" applyBorder="1"/>
    <xf numFmtId="165" fontId="3" fillId="4" borderId="1" xfId="0" applyNumberFormat="1" applyFont="1" applyFill="1" applyBorder="1"/>
    <xf numFmtId="166" fontId="4" fillId="5" borderId="1" xfId="0" applyNumberFormat="1" applyFont="1" applyFill="1" applyBorder="1"/>
    <xf numFmtId="164" fontId="0" fillId="6" borderId="1" xfId="0" applyNumberFormat="1" applyFill="1" applyBorder="1"/>
    <xf numFmtId="0" fontId="3" fillId="4" borderId="0" xfId="0" applyFont="1" applyFill="1"/>
  </cellXfs>
</styleSheet>'''

    def build_sheet_xml(rows, col_widths):
        cols_xml = ""
        if col_widths:
            cols_xml = "<cols>" + "".join(
                f'<col min="{c}" max="{c}" width="{w}" customWidth="1"/>' for c, w in sorted(col_widths.items())
            ) + "</cols>"
        row_parts = []
        for r_idx, cells in rows:
            c_parts = []
            for c_idx, val, st_idx, is_formula in cells:
                ref = f"{_excel_col_letter(c_idx)}{r_idx}"
                if is_formula:
                    c_parts.append(f'<c r="{ref}" s="{st_idx}"><f>{escape(str(val).lstrip("="))}</f></c>')
                elif isinstance(val, (int, float)):
                    c_parts.append(f'<c r="{ref}" s="{st_idx}"><v>{val}</v></c>')
                else:
                    c_parts.append(f'<c r="{ref}" s="{st_idx}" t="inlineStr"><is><t>{escape(str(val))}</t></is></c>')
            ht = ' ht="26" customHeight="1"' if r_idx == 1 else ""
            row_parts.append(f'<row r="{r_idx}"{ht}>' + "".join(c_parts) + "</row>")
        return (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
            f'{cols_xml}<sheetData>{"".join(row_parts)}</sheetData></worksheet>'
        )

    n = len(sheets)
    ct_sheets = "".join(
        f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
        for i in range(1, n + 1)
    )
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
        '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
        f'{ct_sheets}</Types>'
    )
    root_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
        '</Relationships>'
    )
    wb_sheets = "".join(
        f'<sheet name="{escape(name)}" sheetId="{i}" r:id="rId{i}"/>'
        for i, (name, _, _) in enumerate(sheets, 1)
    )
    workbook_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<sheets>{wb_sheets}</sheets>'
        '<calcPr calcId="191029" fullCalcOnLoad="1"/></workbook>'
    )
    wb_rels_items = "".join(
        f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>'
        for i in range(1, n + 1)
    ) + f'<Relationship Id="rId{n+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
    wb_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        f'{wb_rels_items}</Relationships>'
    )

    with zipfile.ZipFile(filepath, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", root_rels)
        zf.writestr("xl/workbook.xml", workbook_xml)
        zf.writestr("xl/_rels/workbook.xml.rels", wb_rels)
        zf.writestr("xl/styles.xml", styles_xml)
        for i, (_, rows, widths) in enumerate(sheets, 1):
            zf.writestr(f"xl/worksheets/sheet{i}.xml", build_sheet_xml(rows, widths))
    return filepath
