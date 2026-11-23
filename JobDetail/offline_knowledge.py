#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
offline_knowledge.py - Kho Cẩm Nang Tri Thức & Tài Liệu Kỹ Thuật Chuyên Sâu 100% Offline
Chứa toàn bộ nội dung hướng dẫn, công thức, quy trình từng bước, sơ đồ và tình huống thực tế.
Hoạt động độc lập không cần kết nối mạng.
"""

import sys

# Đảm bảo UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


OFFLINE_DOCS = {
    "oee": {
        "title": "Cẩm Nang Toàn Diện Về Đo Lường & Tối Ưu Chỉ Số OEE (Overall Equipment Effectiveness)",
        "summary": "Tiêu chuẩn quốc tế đo lường hiệu suất thiết bị tổng thể, phân tách 6 tổn thất lớn (Six Big Losses), công thức tính toán theo ca và các giải pháp thực chiến.",
        "category": "Sản Xuất (Manufacturing)",
        "content": """# ⚙️ CẨM NANG TOÀN DIỆN VỀ CHỈ SỐ OEE & 6 TỔN THẤT LỚN

## 1. TẦNG 1: CƠ BẢN (BASIC) — KHÁI NIỆM & TIÊU CHUẨN QUỐC TẾ
OEE (Overall Equipment Effectiveness) là thước đo chuẩn mực vàng trong sản xuất tinh gọn để đo lường tỷ lệ thời gian sản xuất thực sự tạo ra giá trị so với thời gian lên kế hoạch.

### Tiêu Chuẩn Xếp Hạng OEE Quốc Tế:
- **100%**: Sản xuất hoàn hảo (Không có dừng máy, chạy tối đa tốc độ, 0 phế phẩm).
- **>= 85%**: Đẳng Cấp Thế Giới (World-Class OEE) — Mục tiêu của các nhà máy hàng đầu:
  * Availability (Độ khả dụng): >= 90.0%
  * Performance (Hiệu suất vận hành): >= 95.0%
  * Quality (Tỷ lệ chất lượng): >= 99.9%
- **60% - 70%**: Mức trung bình của các nhà máy công nghiệp truyền thống.
- **< 50%**: Cảnh báo đỏ — Nhà máy đang lãng phí trầm trọng vốn đầu tư thiết bị.

---

## 2. CÔNG THỨC TOÁN HỌC & CÁCH TÍNH TOÁN THEO CA

```text
┌────────────────────────────────────────────────────────────────────────┐
│  CÔNG THỨC TOÁN HỌC OEE CHUẨN QUỐC TẾ                                  │
└────────────────────────────────────────────────────────────────────────┘

  OEE = Availability (A)  ×  Performance (P)  ×  Quality (Q)

A. Độ Khả Dụng (Availability - A):
         Thời Gian Vận Hành Thực Tế (Operating Time)
  A  =  ─────────────────────────────────────────────
         Thời Gian Kế Hoạch (Planned Production Time)

  • Thời gian kế hoạch = Tổng thời gian ca (vd: 8 giờ = 480 phút) - Nghỉ giải lao/ăn ca (vd: 40 phút) = 440 phút.
  • Thời gian vận hành thực tế = Thời gian kế hoạch - Thời gian dừng máy (Downtime).

B. Hiệu Suất Vận Hành (Performance - P):
         Tổng Sản Phẩm Làm Ra × Chu Kỳ Chuẩn (Ideal Cycle Time)
  P  =  ────────────────────────────────────────────────────────
                      Thời Gian Vận Hành Thực Tế

  • Ideal Cycle Time: Thời gian thiết kế nhanh nhất để máy sản xuất 1 sản phẩm.

C. Tỷ Lệ Chất Lượng (Quality - Q):
         Số Lượng Sản Phẩm Đạt Chuẩn (Good Count)
  Q  =  ───────────────────────────────────────────
             Tổng Sản Lượng Làm Ra (Total Count)
```

---

## 3. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — BẢNG PHÂN TÍCH 6 TỔN THẤT LỚN (SIX BIG LOSSES) & GIẢI PHÁP
| Nhóm Chỉ Số | Loại Tổn Thất Lớn | Nguyên Nhân Thường Gặp | Giải Pháp Triệt Tiêu Cụ Thể |
| :--- | :--- | :--- | :--- |
| **Availability** | **1. Hỏng hóc đột xuất (Equipment Breakdown)** | Kém bảo trì, quá nhiệt, thiếu bôi trơn, mòn cơ khí | Áp dụng TPM (Bảo trì tự quản 5S), thiết lập lịch bảo trì phòng ngừa (PM) định kỳ. |
| **Availability** | **2. Cài đặt & Đổi mã (Setup & Adjustments)** | Đổi khuôn, thay dao, căn chỉnh kích thước lâu | Áp dụng kỹ thuật **SMED** (Single-Minute Exchange of Die) để đưa thời gian dừng về < 10 phút. |
| **Performance** | **3. Dừng vặt & Chạy không tải (Minor Stops < 5p)** | Kẹt phôi, cảm biến bẩn, cấp liệu bị nghẽn | Chuẩn hóa quy trình vệ sinh sensor, thiết kế phễu cấp liệu chống kẹt (Poka-Yoke). |
| **Performance** | **4. Giảm tốc độ chạy (Reduced Speed)** | Người vận hành sợ hỏng máy, linh kiện rung lắc | Hiệu chuẩn cơ khí, đào tạo lại công nhân, nâng dần tốc độ máy về mức thiết kế danh định. |
| **Quality** | **5. Phế phẩm khởi động (Startup Rejects)** | Nhiệt độ chưa ổn định, áp suất ban đầu sai | Tiêu chuẩn hóa quy trình làm nóng máy (Pre-heating SOP), kiểm soát thông số mẻ đầu tiên. |
| **Quality** | **6. Phế phẩm khi chạy (Production Rejects)** | Dao mòn, lỗi lắp ráp của công nhân | Gắn cảm biến kiểm tra tự động, kiểm soát quá trình thống kê (SPC) với Minitab. |

---

## 4. BÀI TOÁN THỰC TẾ & TÍNH TOÁN MẪU (CASE STUDY)

```text
┌────────────────────────────────────────────────────────────────────────┐
│  BÀI TOÁN THỰC TẾ & TÍNH TOÁN MẪU (CASE STUDY CA 8 TIẾNG)             │
└────────────────────────────────────────────────────────────────────────┘

📌 Dữ Liệu Ban Đầu Của Ca Làm Việc:
  • Tổng thời gian ca làm việc: 8 tiếng = 480 phút.
  • Nghỉ ăn ca (Không tính vào kế hoạch): 40 phút.
    → Thời gian sản xuất theo kế hoạch = 480 - 40 = 440 phút.
  • Dừng máy sự cố do hỏng bạc đạn: 30 phút.
  • Dừng máy đổi khuôn & mẫu mã: 30 phút.
    → Tổng thời gian dừng máy (Downtime) = 30 + 30 = 60 phút.
  • Thời gian vận hành thực tế = 440 - 60 = 380 phút (= 22,800 giây).
  • Chu kỳ lý thuyết của máy (Ideal Cycle Time): 20 giây / sản phẩm.
  • Tổng sản phẩm làm ra trong ca (Total Count): 950 sản phẩm.
  • Phế phẩm phát hiện (Defects): 50 sản phẩm.
    → Sản phẩm đạt chuẩn chất lượng (Good Count) = 950 - 50 = 900 sản phẩm.

──────────────────────────────────────────────────────────────────────────
📐 BƯỚC 1: TÍNH MỨC ĐỘ SẴN SÀNG (AVAILABILITY - A)
──────────────────────────────────────────────────────────────────────────
         Thời Gian Vận Hành Thực Tế         380 phút
  A  =  ────────────────────────────  =  ────────────  =  86.36%
         Thời Gian Kế Hoạch Chạy Máy        440 phút

──────────────────────────────────────────────────────────────────────────
📐 BƯỚC 2: TÍNH HIỆU SUẤT VẬN HÀNH (PERFORMANCE - P)
──────────────────────────────────────────────────────────────────────────
         Tổng Sản Lượng × Chu Kỳ Lý Thuyết     950 sp × 20 giây      19,000 giây
  P  =  ─────────────────────────────────── = ────────────────── = ───────────── = 83.33%
             Thời Gian Vận Hành Thực Tế           22,800 giây        22,800 giây

──────────────────────────────────────────────────────────────────────────
📐 BƯỚC 3: TÍNH TỶ LỆ CHẤT LƯỢNG (QUALITY - Q)
──────────────────────────────────────────────────────────────────────────
         Số Sản Phẩm Đạt Chuẩn       900 sản phẩm
  Q  =  ───────────────────────  =  ──────────────  =  94.74%
         Tổng Sản Phẩm Làm Ra        950 sản phẩm

──────────────────────────────────────────────────────────────────────────
🏆 BƯỚC 4: TỔNG HỢP CHỈ SỐ OEE TOÀN PHẦN
──────────────────────────────────────────────────────────────────────────
  OEE  =  Availability (A)  ×  Performance (P)  ×  Quality (Q)
       =  86.36%  ×  83.33%  ×  94.74%
       =  68.18%

💡 Đánh Giá & Nhận Xét Chuyên Gia:
  • OEE đạt 68.18% (dưới mức chuẩn World-Class 85%).
  • Điểm nghẽn lớn nhất: Hiệu suất (P = 83.33%) do dừng vặt hoặc máy giảm tốc độ,
    và Thời gian dừng máy (A = 86.36%) do đổi khuôn mất 30 phút.
  • Giải pháp ưu tiên: Áp dụng kỹ thuật SMED để rút thời gian đổi khuôn từ 30p
    xuống dưới 10p, giúp nâng A lên 90.9% và kéo OEE lên trên 72%!
```

---

## 5. TẦNG 3: NÂNG CAO (ADVANCED) — SO SÁNH OEE VS TEEP & BÀI TOÁN THẨM ĐỊNH DỰ ÁN ĐẦU TƯ CAPEX

```text
┌────────────────────────────────────────────────────────────────────────┐
│  CÔNG THỨC CHỈ SỐ TEEP (TOTAL EFFECTIVE EQUIPMENT PERFORMANCE)         │
└────────────────────────────────────────────────────────────────────────┘

  TEEP  =  OEE  ×  Tỷ Lệ Tải Thời Gian Lịch (Utilization / Loading)

                     Thời Gian Vận Hành Kế Hoạch (Planned Time)
  Loading Factor  =  ──────────────────────────────────────────
                     Tổng Thời Gian Lịch 24/7 (168 giờ / tuần)

  • Mẫu số của OEE : Chỉ tính trong ca làm việc được lên lịch (vd: 1 ca 8h = 440 phút).
  • Mẫu số của TEEP: Tính trên toàn bộ 24 giờ/ngày × 7 ngày/tuần (10,080 phút/tuần).
```

### Bài Toán Thẩm Định Mua Máy Mới (CAPEX Justification):
- **Tình huống:** Trưởng xưởng dập báo cáo: *"Máy dập hiện tại đã đạt OEE = 82% (rất cao), chuyền sau đang thiếu hàng, công ty cần chi 3.5 tỷ VNĐ mua thêm máy dập thứ hai!"*
- **Kỹ sư Cải tiến phân tích bằng TEEP:**
  * Nhà máy hiện chỉ chạy **1 ca 8 giờ/ngày, 5 ngày/tuần** → Thời gian kế hoạch = 40 giờ/tuần.
  * Tổng thời gian lịch = 168 giờ/tuần → Loading = 40 / 168 = 23.81%.
  * TEEP = OEE × Loading = 82% × 23.81% = 19.52%.
- **Kết luận của Giám đốc:** Máy dập thực tế đang **nằm nhàn rỗi tới hơn 80% thời gian trong tuần!** Thay vì bỏ 3.5 tỷ VNĐ mua máy mới, công ty chỉ cần tuyển thêm 1 thợ mở thêm ca 2 (tăng thời gian chạy lên 16 giờ/ngày), sản lượng tăng gấp đôi ngay lập tức mà tiết kiệm trọn vẹn 3.5 tỷ đồng tiền đầu tư thiết bị!

---

## 6. PHÒNG NGỪA DỪNG MÁY VI MÔ (MINOR STOPPAGE) & 8 TRỤ CỘT TPM
1. **Dừng máy vi mô (< 5 phút):** Là thủ phạm vô hình bào mòn 15-25% chỉ số Performance (P) mà không thể hiện trên biểu đồ dừng máy. Triệt tiêu bằng cách gắn cảm biến IoT đếm xung chu kỳ từng sản phẩm và chuẩn hóa việc vệ sinh máng trượt phôi.
2. **Kế hoạch 8 Trụ Cột TPM (Total Productive Maintenance):**
   - *Autonomous Maintenance (Jishu Hozen):* Công nhân tự bảo dưỡng hàng ngày (Lau chùi là Kiểm tra, tra dầu, siết ốc).
   - *Planned Maintenance:* Bảo trì phòng ngừa theo chu kỳ giờ chạy máy trước khi hỏng.
   - *Quality Maintenance:* Triệt tiêu nguyên nhân máy gây ra khuyết tật sản phẩm.
   - *Focused Improvement (Kobetsu Kaizen):* Thành lập nhóm giải quyết triệt để các tổn thất OEE lặp lại.

---

## 7. TẦNG 4: CHUYÊN GIA (EXPERT) — CASE STUDY ĐẶC THÙ NGÀNH DÂY CÁP ĐIỆN (CADIVI): TÍNH OEE THEO TỐC ĐỘ MÉT/PHÚT (m/min)

Khác với xưởng cơ khí đếm theo "cái/giây" (pieces/sec), các dây chuyền kéo sợi, bện và đùn bọc cáp điện hoạt động **liên tục theo tốc độ tuyến tính (mét/phút hoặc mét/giây)**.

**Bối cảnh thực tế tại Dây chuyền Đùn Bọc Cách Điện PVC (Máy đùn Ø 70mm) — Sản xuất dây dân dụng VC 2.5 mm²:**
- Thời gian ca làm việc: 8 tiếng = 480 phút; nghỉ ăn ca / bàn giao ca theo kế hoạch: 30 phút.
  → Thời gian kế hoạch (Planned Production Time) = 480 - 30 = 450 phút.
- Các sự cố dừng máy ghi nhận trong ca:
  * Đổi màu nhựa (Đen → Trắng) và xả làm sạch nòng (Purging): 35 phút.
  * Thay rulo cấp ruột dẫn đồng (Pay-off) và hàn nối đầu dây (3 lần × 8 phút): 24 phút.
  * Xử lý 2 lần báo lỗi thủng cách điện trên máy Spark Tester & dừng cắt nối: 16 phút.
  * Bảo trì xử lý nghẹt lưới lọc đầu đùn (Screen Pack): 15 phút.
  → Tổng Downtime = 35 + 24 + 16 + 15 = 90 phút.
  → Thời gian vận hành thực tế (Operating Time) = 450 - 90 = 360 phút.
- Tốc độ định mức thiết kế chuẩn (Ideal Line Speed) cho mã dây VC 2.5 mm²: **350 mét / phút**.
- Tổng chiều dài dây đùn ra trong ca (Total Length Produced): **108,000 mét**.
- Phế phẩm cắt bỏ (Scrap Length):
  * Đoạn dây phế đầu ca khi khởi động/ổn định đường kính & đổi màu (Startup/Purge Scrap): 2,400 mét.
  * Đoạn dây lỗi do thủng Spark, sần bề mặt nhựa, lệch tâm phải cắt loại: 3,000 mét.
  → Tổng phế phẩm = 5,400 mét → Chiều dài đạt chuẩn (Good Length) = 108,000 - 5,400 = 102,600 mét.

```text
┌────────────────────────────────────────────────────────────────────────┐
│  BÀI TOÁN TÍNH OEE THEO MÉT/PHÚT — DÂY CHUYỀN ĐÙN BỌC CÁP PVC          │
└────────────────────────────────────────────────────────────────────────┘

1. Độ Khả Dụng (Availability - A):
           Thời Gian Chạy Máy Thực Tế          360 phút
   A   =  ─────────────────────────────  =  ──────────────  =  80.00%
           Thời Gian Kế Hoạch Trong Ca         450 phút

2. Hiệu Suất Vận Hành (Performance - P):
           Tổng Chiều Dài Làm Ra (m)              108,000 mét
   P   =  ────────────────────────────────  =  ──────────────────────
           Thời Gian Chạy × Tốc Độ Chuẩn        360 phút × 350 m/phút

              108,000 mét
       =  ───────────────────  =  85.71%
              126,000 mét
   (Tốc độ chạy thực tế trung bình = 108,000 / 360 = 300 m/phút, thấp hơn chuẩn 50 m/phút!)

3. Tỷ Lệ Chất Lượng (Quality - Q):
           Chiều Dài Dây Đạt Chuẩn             102,600 mét
   Q   =  ───────────────────────────  =  ───────────────────  =  95.00%
           Tổng Chiều Dài Đã Đùn Ra            108,000 mét

4. Chỉ Số OEE Tổng Thể Máy Đùn Bọc Cáp:
   OEE = A × P × Q = 80.00% × 85.71% × 95.00% = 65.14%
```

**Phân Tích Tổn Thất & Kế Hoạch Tối Ưu Của Chuyên Viên OE CADIVI:**
1. **Tấn công Availability (80.0% → 91.1%):**
   - Áp dụng **Lập lịch Chuỗi Màu (Color Sequencing: Trắng → Vàng → Đỏ → Xanh → Đen)** và sấy sẵn đầu Chày-Cối bên ngoài (SMED) → Rút đổi màu từ 35p xuống 10p.
   - Bố trí cụm nhả dây đôi (Dual Pay-off) + bộ tích dây (Accumulator) cho phép hàn nối đồng khi máy vẫn chạy → Triệt tiêu 24p dừng thay rulo về 0p.
2. **Tấn công Performance (85.7% → 94.3%):**
   - Kiểm tra nguyên nhân công nhân ghìm tốc độ ở 300 m/phút thay vì 350 m/phút: phát hiện nước máng làm mát (Cooling Trough) quá nóng (38°C thay vì ≤ 25°C) làm nhựa mềm dễ trầy khi qua bánh kéo Capstan → Bảo trì tháp giải nhiệt/Chiller, nâng tốc độ lên 330 m/phút ổn định.
3. **Tấn công Quality (95.0% → 98.5%):**
   - Giảm phế phẩm khởi động và lỗi Spark bằng kiểm soát độ ẩm hạt nhựa PVC (Hopper Dryer) và gắn **Laser Diameter Gauge tự động hồi tiếp (Closed-loop Feedback)** điều chỉnh tốc độ Capstan giữ dung sai đường kính.
→ **Kết quả dự phóng sau cải tiến:** `OEE = 91.1% × 94.3% × 98.5% = 84.6%` (tăng thêm **+30% sản lượng mét dây/ca** mà không tốn chi phí mua thêm dây chuyền đùn!).
"""
    },

    "ole": {
        "title": "Cẩm Nang Toàn Diện Về Chỉ Số OLE & Năng Lực Lao Động (Overall Labor Effectiveness)",
        "summary": "Cẩm nang chuyên sâu từ Basic đến Expert: 3 trụ cột OLE, 6 tổn thất lao động, Time & Motion Study, 3 Case Study thực chiến có lời giải chi tiết, Line Balancing & Yamazumi, Ergonomics và số hóa MES/RFID.",
        "category": "Sản Xuất (Manufacturing)",
        "content": """# 👥 CẨM NANG TOÀN DIỆN VỀ CHỈ SỐ OLE (OVERALL LABOR EFFECTIVENESS) & NĂNG SUẤT LAO ĐỘNG
*(Kiến Thức Chuẩn Công Nghiệp Từ Cơ Bản Đến Chuyên Gia — Kèm 3 Case Study Thực Chiến Có Lời Giải Chi Tiết)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — ĐỊNH NGHĨA & BẢN CHẤT CỦA OLE

### OLE Là Gì Và Vì Sao OEE Không Thể Thay Thế OLE?
Trong khi OEE (Overall Equipment Effectiveness) đo lường mức độ khai thác máy móc thiết bị, **OLE (Overall Labor Effectiveness)** đo lường hiệu quả khai thác sức lao động con người trong sản xuất. 

```text
┌────────────────────────────────────────────────────────────────────────┐
│  BẢNG SO SÁNH CÁC CHỈ SỐ QUẢN TRỊ NĂNG SUẤT NHÀ MÁY                     │
├───────────────┬────────────────────────────────────────────────────────┤
│ Chỉ Số        │ Trọng Tâm Đánh Giá & Ý Nghĩa Thực Tế                   │
├───────────────┼────────────────────────────────────────────────────────┤
│ OEE           │ Đo lường máy móc (Availability × Performance × Quality)│
│ OLE           │ Đo lường nhân lực (Availability × Utilization × Quality│
│ OPE (People)  │ Tương tự OLE, dùng phổ biến trong lắp ráp thủ công     │
│ Năng Suất Đơn │ Sản lượng / Số giờ công (Thiếu góc nhìn chất lượng)    │
└───────────────┴────────────────────────────────────────────────────────┘
```

> [!IMPORTANT]
> **Quy luật nghịch lý thường gặp tại Genba:** Một xưởng dập có OEE lên tới 90% nhưng nhà máy vẫn thua lỗ do OLE chỉ đạt 55%. Máy móc chạy rất nhanh nhưng công nhân phải tốn hàng giờ chờ linh kiện, thao tác thừa, hoặc làm ra sản phẩm lỗi phải tháo ra sửa lại (Rework). OLE chính là thước đo quyết định giá thành nhân công trực tiếp trên mỗi đơn vị sản phẩm.

```text
┌────────────────────────────────────────────────────────────────────────┐
│  CÔNG THỨC TOÁN HỌC OLE (OVERALL LABOR EFFECTIVENESS)                  │
└────────────────────────────────────────────────────────────────────────┘

  OLE  =  Availability (Hiện Diện)  ×  Utilization (Hiệu Suất)  ×  Quality (Chất Lượng)

1. Availability (Tỷ lệ Hiện Diện Lao Động):
                    Thời Gian Công Nhân Thực Sự Ngồi Vào Vị Trí Làm Việc
  A_labor  =  ────────────────────────────────────────────────────────────────
                    Thời Gian Công Nhân Được Phân Công Trả Lương Trong Ca

  • Đo lường: Mức độ kỷ luật giờ giấc và tính sẵn sàng của lực lượng lao động.
  • Nguyên nhân giảm sút: Đi trễ về sớm, họp giao ban kéo dài, vắng mặt đột xuất, nghỉ cá nhân ngoài giờ quy định.

2. Utilization / Performance (Hiệu Suất Thao Tác Thao Tác):
                    Thời Lượng Chuẩn Của Các Sản Phẩm Đã Làm Ra (Earned Standard Hours)
  U_labor  =  ─────────────────────────────────────────────────────────────────────────────
                             Thời Gian Thực Tế Công Nhân Ngồi Thao Tác

  • Đo lường: Khi đã ngồi vào vị trí, công nhân thao tác nhanh hay chậm so với định mức kỹ thuật chuẩn (Standard Allowed Minutes - SAM).
  • Nguyên nhân giảm sút: Chờ linh kiện từ kho (Waiting), thao tác thừa do đồ gá đặt xa (Motion), nhịp độ làm việc uể oải, máy chạy chậm chờ nguội.

3. Quality (Tỷ Lệ Chất Lượng Tay Nghề):
                    Số Lượng Sản Phẩm Đạt Chuẩn Không Bị Lỗi Do Thao Tác
  Q_labor  =  ───────────────────────────────────────────────────────────────
                           Tổng Số Lượng Sản Phẩm Công Nhân Đã Thao Tác

  • Đo lường: Tay nghề chuẩn xác của công nhân, làm đúng ngay từ lần đầu tiên (Right First Time - RFT).
  • Nguyên nhân giảm sút: Lắp ngược linh kiện, siết ốc thiếu lực, làm xước bề mặt chi tiết, quên quét keo.
```

### Thang Đo Đánh Giá OLE Theo Chuẩn Quốc Tế:
- **Dưới 60%**: *Báo động đỏ (Critical)* — Lãng phí quỹ lương trầm trọng, quản trị hiện trường lỏng lẻo, chuyền tắc nghẽn liên tục.
- **60% - 75%**: *Mức trung bình (Average)* — Phổ biến ở các xưởng sản xuất truyền thống chưa áp dụng công cụ Lean.
- **75% - 85%**: *Mức vận hành tốt (Good / Lean)* — Dây chuyền được cân bằng tốt, kiểm soát chặt chẽ thời gian chờ đợi.
- **Trên 85%**: *Đẳng cấp thế giới (World-Class OLE)* — Dòng chảy 1 sản phẩm liên tục, lỗi thao tác dưới 0.5%, thao tác chuẩn hóa 100%.

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — MA TRẬN 6 TỔN THẤT LAO ĐỘNG & TIME STUDY

### Ma Trận 6 Tổn Thất Lao Động Lớn (The 6 Big Labor Losses)
Tương ứng với Six Big Losses của thiết bị trong OEE, kỹ sư Lean/IE phân loại 6 tổn thất lao động lớn làm xói mòn OLE:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  MA TRẬN ĐỐI CHIẾU 6 TỔN THẤT LỚN CỦA MÁY MÓC (OEE) VÀ CON NGƯỜI (OLE)                 │
├────────────────────┬───────────────────────────────────┬───────────────────────────────┤
│ Thành Phần         │ 6 Tổn Thất Thiết Bị (OEE)          │ 6 Tổn Thất Lao Động (OLE)     │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 1. Availability    │ • Sự cố hỏng hóc máy (Breakdown)  │ • Vắng mặt, đi muộn, về sớm   │
│    (Hiện diện)     │ • Cài đặt & Đổi khuôn (Setup)     │ • Họp kéo dài, đào tạo đầu ca │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 2. Utilization /   │ • Dừng vi mô & Chạy không tải     │ • Chờ vật tư, chờ lệnh (Wait) │
│    Performance     │ • Vận hành giảm tốc độ (Reduced)  │ • Thao tác thừa, chậm nhịp    │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 3. Quality         │ • Phế phẩm khi khởi động máy      │ • Lỗi do lắp sai, quên bước   │
│    (Chất lượng)    │ • Phế phẩm trong quá trình chạy   │ • Thao tác làm hỏng, sửa lại  │
└────────────────────┴───────────────────────────────────┴───────────────────────────────┘
```

### Phương Pháp Đo Lường Bấm Giờ Thao Tác (Time & Motion Study)
Để có định mức thời gian chuẩn (Standard Time) làm mẫu số tính Utilization, kỹ sư IE phải tiến hành nghiên cứu thời gian và chuyển động:

1. **Quy tắc bấm giờ Stopwatch:**
   - Quan sát công nhân làm việc bình thường, không thông báo đột ngột gây áp lực tâm lý.
   - Bấm giờ tối thiểu **10 đến 20 chu kỳ lặp lại liên tiếp**.
   - Loại bỏ các giá trị dị biệt (Outliers) do sự cố ngẫu nhiên (như đứt dây giày, làm rơi kìm).
   - Tính toán Thời gian Chu kỳ Quan sát Trung bình (Observed Time - OT).

2. **Hệ số Đánh giá Nỗ lực (Rating Factor - RF) & Dung sai Phụ cấp (Allowances):**
   - Không phải công nhân nào cũng thao tác với tốc độ chuẩn (100%). Người mới có thể đạt 80%, người lành nghề đạt 115%.
   - Thời gian cơ bản: Normal Time = OT × RF.
   - Cộng thêm phụ cấp nghỉ ngơi sinh lý và mệt mỏi thể chất (Allowances, thường từ 10% đến 15%):
     Standard Time (ST) = Normal Time × (1 + Allowance)

3. **Phân loại 3 nhóm thời gian thao tác (VA, NNVA, NVA):**
   - **VA (Value-Added - Tạo giá trị)**: Thao tác trực tiếp biến đổi hình dáng, cơ tính sản phẩm (vd: hàn, siết ốc, dán nhãn).
   - **NNVA (Necessary Non-Value-Added - Bắt buộc nhưng không tạo giá trị)**: Mở túi nilon lấy linh kiện, xoay phôi đúng chiều, đo kiểm tra kích thước.
   - **NVA (Non-Value-Added - Lãng phí tuyệt đối)**: Cúi nhặt chi tiết rơi dưới sàn, đi bộ sang bàn khác mượn kìm, đứng đợi keo khô.
   - *Mục tiêu cải tiến:* Đẩy tỷ lệ VA từ mức thông thường 20% lên trên 55% bằng cách bố trí lại bàn thao tác.

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — 3 BÀI TOÁN THỰC TẾ & TÍNH TOÁN MẪU (CASE STUDIES)

### 📌 CASE STUDY 1: TÍNH OLE CHO 1 CÔNG NHÂN TRẠM THAO TÁC ĐƠN LẺ
**Bối cảnh tại xưởng:**
Công nhân Nguyễn Văn A làm việc tại trạm Lắp Ráp Bản Lề trong ca làm việc 8 tiếng.

**Dữ liệu thu thập trong ca:**
- Thời gian ca làm việc: 8 giờ = 480 phút.
- Thời gian nghỉ ăn ca theo quy định: 40 phút.
  → **Thời gian phân công làm việc (Scheduled Time)** = 480 - 40 = 440 phút (26,400 giây).
- Trong ca phát sinh:
  * Họp an toàn giao ban đầu ca bị kéo dài: 15 phút.
  * Chờ nhân viên kho cấp thêm ốc vít: 25 phút.
  → **Thời gian công nhân thực sự ngồi thao tác** = 440 - (15 + 25) = 400 phút (24,000 giây).
- Định mức kỹ thuật chuẩn (Standard Allowed Minutes - SAM): **40 giây / sản phẩm**.
- Kết quả sản xuất cuối ca:
  * Tổng sản phẩm công nhân đã hoàn thành: **480 sản phẩm**.
  * Sau khi kiểm tra QC, phát hiện **24 sản phẩm bị bắt lệch ốc và trầy xước**.
  * Số sản phẩm đạt chuẩn chuyển sang khâu sau = 480 - 24 = 456 sản phẩm.

```text
┌────────────────────────────────────────────────────────────────────────┐
│  BÀI TOÁN TÍNH OLE CHO 1 CÔNG NHÂN (CASE STUDY 1)                      │
└────────────────────────────────────────────────────────────────────────┘

1. Tỷ lệ Hiện Diện (Availability):
                    Thời Gian Thực Sự Có Mặt Thao Tác
  A_labor  =  ─────────────────────────────────────────────
                    Thời Gian Phân Công Làm Việc Kế Hoạch

                    400 phút
  A_labor  =  ──────────────────  =  0.9091  →  90.91%
                    440 phút

2. Hiệu Suất Thao Tác (Utilization / Performance):
                    Tổng Thời Gian Chuẩn Cho 480 Sản Phẩm (Earned Time)
  U_labor  =  ─────────────────────────────────────────────────────────
                          Thời Gian Thực Tế Ngồi Làm Việc

                    480 sản phẩm  ×  40 giây / sản phẩm
  U_labor  =  ───────────────────────────────────────────
                             24,000 giây

                    19,200 giây
  U_labor  =  ──────────────────────  =  0.8000  →  80.00%
                    24,000 giây

3. Tỷ lệ Chất Lượng Tay Nghề (Quality):
                    Số Sản Phẩm Đạt Chuẩn (Không Lỗi)
  Q_labor  =  ─────────────────────────────────────────
                         Tổng Số Sản Phẩm Làm Ra

                    456 sản phẩm
  Q_labor  =  ──────────────────────  =  0.9500  →  95.00%
                    480 sản phẩm

4. Chỉ Số OLE Tổng Thể Của Công Nhân:
  OLE      =  A_labor  ×  U_labor  ×  Q_labor
  OLE      =  90.91%   ×  80.00%   ×  95.00%   =  69.09%
```

**Nhận xét & Hành động của Kỹ sư Cải tiến:**
- **Chẩn đoán:** OLE = 69.09% (Dưới chuẩn 75%). Tổn thất lớn nhất nằm ở **Hiệu suất U (80.00%)**, làm mất tới 20% năng lực lao động khi công nhân đang ngồi tại trạm.
- **Hành động Kaizen ngay:**
  1. *Triệt tiêu chờ đợi (25 phút):* Áp dụng cơ chế Thẻ rút Kanban hai thùng (Two-bin Kanban) để nhân viên Water Spider bù ốc vít trước khi trạm bị cạn kiệt.
  2. *Khắc phục nhịp thao tác chậm:* Công nhân mất trung bình 50 giây/sp (thực tế 24,000s / 480sp) trong khi chuẩn là 40s/sp. Bố trí lại tô vít treo pa-lăng lò xo tự lựa ngay trên đầu công nhân để giảm thời gian cầm/đặt dụng cụ.
  3. *Ngăn ngừa 24 sản phẩm lỗi:* Thiết kế đồ gá Poka-Yoke có chốt định vị chống bắt lệch ren, nâng Q lên 99%+.

---

### 📌 CASE STUDY 2: TÍNH OLE CHO TOÀN DÂY CHUYỀN LẮP RÁP 10 CÔNG NHÂN (LINE OLE)
Trong thực tế nhà máy, người quản lý cần đo lường OLE cho toàn bộ tổ đội hoặc dây chuyền sản xuất đa công đoạn.

**Dữ liệu dây chuyền đóng gói:**
- Số lượng công nhân trực tiếp trên chuyền: **10 người**.
- Ca làm việc 8 tiếng (480 phút), trừ 30 phút nghỉ giải lao.
  → **Thời gian phân công của 1 người** = 480 - 30 = 450 phút.
  → **Tổng Giờ Lao Động Kế Hoạch (Total Scheduled Labor Hours)** = 10 người × 450 phút = 4,500 phút công (75.0 giờ công).
- Dữ liệu ghi nhận từ hệ thống quẹt thẻ & điểm danh:
  * 1 công nhân đến trễ 30 phút; 1 công nhân xin về sớm 60 phút vì việc riêng.
  * Toàn chuyền dừng 20 phút để họp chất lượng đột xuất giải quyết khiếu nại khách hàng (10 người × 20 phút = 200 phút công).
  → **Tổng Thời Gian Lao Động Thực Tế (Actual Working Labor Hours)**:
  4,500 - (30 + 60 + 200) = 4,210 phút công
- Định mức kỹ thuật chuẩn của toàn chuyền (Standard Labor Hours per Unit): **2.0 phút công / sản phẩm**.
- Kết quả sản xuất của cả chuyền trong ca:
  * Hoàn thành: **1,850 sản phẩm**.
  * Kiểm tra chất lượng cuối chuyền phát hiện: **55 sản phẩm bị lỗi lắp ráp** do công nhân thao tác sai.
  * Số sản phẩm đạt chuẩn xuất xưởng = 1,850 - 55 = 1,795 sản phẩm.

```text
┌────────────────────────────────────────────────────────────────────────┐
│  BÀI TOÁN TÍNH LINE OLE CHO DÂY CHUYỀN 10 NGƯỜI (CASE STUDY 2)         │
└────────────────────────────────────────────────────────────────────────┘

1. Line Availability (Tỷ lệ Hiện Diện Toàn Chuyền):
                         Tổng Phút Công Làm Việc Thực Tế
  Line_A   =  ────────────────────────────────────────────────────
                    Tổng Phút Công Kế Hoạch Được Phân Bổ

                    4,210 phút công
  Line_A   =  ──────────────────────────  =  0.9356  →  93.56%
                    4,500 phút công

2. Line Utilization (Hiệu Suất Sử Dụng Lao Động):
                    Giờ Lao Động Chuẩn Tạo Ra (Earned Standard Minutes)
  Line_U   =  ─────────────────────────────────────────────────────────
                          Tổng Phút Công Thực Tế Ngồi Làm Việc

                    1,850 sản phẩm  ×  2.0 phút công / sản phẩm
  Line_U   =  ───────────────────────────────────────────────────
                              4,210 phút công

                    3,700 phút công
  Line_U   =  ──────────────────────────  =  0.8789  →  87.89%
                    4,210 phút công

3. Line Quality (Chất Lượng Chuyền):
                    Số Sản Phẩm Đạt Chuẩn Xuất Xưởng
  Line_Q   =  ──────────────────────────────────────────
                       Tổng Sản Phẩm Đã Lắp Ráp

                    1,795 sản phẩm
  Line_Q   =  ──────────────────────  =  0.9703  →  97.03%
                    1,850 sản phẩm

4. Chỉ Số OLE Toàn Chuyền (Line OLE):
  Line_OLE =  Line_A  ×  Line_U  ×  Line_Q
  Line_OLE =  93.56%  ×  87.89%  ×  97.03%   =  79.79%
```

**Phân tích Chi phí Lương Lãng phí (Labor Cost Variance):**
- Tổng thời gian lãng phí trong ca = 4,500 - (1,795 × 2.0) = 4,500 - 3,590 = 910 phút công (15.17 giờ công).
- Với đơn giá lương nhân công trung bình 60,000 VNĐ/giờ, ca làm việc này đã làm thất thoát:
  • Chi Phí Thất Thoát = 15.17 giờ × 60,000 VNĐ = 910,200 VNĐ / ca
- Một tháng chạy 2 ca × 26 ngày → Nhà máy mất hơn **47,300,000 VNĐ** tiền lương vô ích trên duy nhất 1 dây chuyền này!

---

### 📌 CASE STUDY 3: KỸ THUẬT CÂN BẰNG CHUYỀN (LINE BALANCING) & BIỂU ĐỒ YAMAZUMI
Khi Utilization thấp, nguyên nhân số 1 luôn là **Mất cân bằng giữa các công đoạn** (Line Imbalance).

**Bài toán dây chuyền lắp ráp điện tử gồm 5 trạm liên tiếp:**
- Trạm 1 (Lắp bo mạch vào vỏ): Chu kỳ T1 = 24 giây.
- Trạm 2 (Bắt vít 4 góc): Chu kỳ T2 = 42 giây *(Điểm nghẽn - Bottleneck lớn nhất)*.
- Trạm 3 (Cắm cáp kết nối): Chu kỳ T3 = 18 giây *(Trạm quá rảnh rỗi)*.
- Trạm 4 (Dán tem mã vạch & đóng nắp): Chu kỳ T4 = 35 giây.
- Trạm 5 (Kiểm tra chức năng & đóng hộp): Chu kỳ T5 = 26 giây.
- **Nhu cầu khách hàng:** 900 sản phẩm / ngày (Ca 7.5 giờ khả dụng = 27,000 giây).

```text
┌────────────────────────────────────────────────────────────────────────┐
│  BÀI TOÁN CÂN BẰNG CHUYỀN & CHỈ SỐ SMOOTHNESS INDEX (CASE STUDY 3)     │
└────────────────────────────────────────────────────────────────────────┘

1. Nhịp Takt Time Yêu Cầu Của Khách Hàng:
                   27,000 giây
  Takt Time  =  ─────────────────  =  30 giây / sản phẩm.
                  900 sản phẩm

2. Đánh Giá Hiện Trạng Chuyền:
  • Tổng thời gian gia công = 24 + 42 + 18 + 35 + 26 = 145 giây.
  • Trạm Bottleneck = Trạm 2 (42 giây) > Takt Time (30 giây) → KHÔNG ĐẠT TIẾN ĐỘ!
  • Trạm 3 (18 giây) bị thiếu việc làm, công nhân đứng chờ 24 giây mỗi chu kỳ.

3. Hiệu Suất Cân Bằng Chuyền Ban Đầu (LBE):
                    Tổng Cycle Time Tất Cả Các Trạm
  LBE        =  ───────────────────────────────────────  × 100%
                   Số Trạm  ×  Cycle Time Trạm Nghẽn

                        145 giây
  LBE        =  ───────────────────────  ×  100%  =  69.05%
                   5 trạm  ×  42 giây

4. Chỉ Số Mượt Mà Của Chuyền (Smoothness Index - SI):
  SI = sqrt( (42-24)^2 + (42-42)^2 + (42-18)^2 + (42-35)^2 + (42-26)^2 )
  SI = sqrt( 324 + 0 + 576 + 49 + 256 ) = sqrt(1,205) = 34.71 giây.
  (SI càng lớn chứng tỏ áp lực công việc giữa các trạm càng lệch nhau nghiêm trọng).
```

```text
┌────────────────────────────────────────────────────────────────────────┐
│  KẾ HOẠCH TÁI CÂN BẰNG CHUYỀN BẰNG BIỂU ĐỒ YAMAZUMI                    │
└────────────────────────────────────────────────────────────────────────┘

• BƯỚC 1: Bóc tách thao tác Trạm 2 (42s):
  - Lấy 4 vít và gá vào lỗ: 14 giây.
  - Bắn súng siết vít 4 vị trí: 28 giây.
• BƯỚC 2: San sẻ thao tác sang Trạm 1 và Trạm 3:
  - Chuyển thao tác 'Gá sẵn 4 vít vào lỗ' (14s) về Trạm 1 làm trước:
    → Trạm 1 mới = 24s + 14s (nhưng tối ưu đồ gá cấp vít tự động giảm còn 5s) = 29 giây.
  - Trạm 2 chỉ còn việc bắn súng siết vít = 28 giây (< Takt Time 30s).
• BƯỚC 3: Tối ưu Trạm 4 (35s):
  - Chuyển bước 'Dán tem mã vạch' (7s) sang Trạm 3 đang quá rảnh rỗi (18s):
    → Trạm 3 mới = 18s + 7s = 25 giây.
    → Trạm 4 mới = 35s - 7s = 28 giây.
  - Trạm 5 giữ nguyên = 26 giây.

KẾT QUẢ SAU KAIZEN TÁI CÂN BẰNG:
  • Chu kỳ mới: Trạm 1 (29s) | Trạm 2 (28s) | Trạm 3 (25s) | Trạm 4 (28s) | Trạm 5 (26s).
  • Trạm Bottleneck lớn nhất mới = 29 giây (< Takt Time 30s) → ĐẠT 100% SẢN LƯỢNG!
  • Tổng thời gian gia công mới = 29 + 28 + 25 + 28 + 26 = 136 giây.
  • LBE Mới = 136 / (5 × 29) = 93.79%  (Tăng vọt từ 69.05% lên 93.79%!).
  • SI Mới  = sqrt( (29-29)^2 + (29-28)^2 + (29-25)^2 + (29-28)^2 + (29-26)^2 )
            = sqrt( 0 + 1 + 16 + 1 + 9 ) = sqrt(27) = 5.20 giây (Giảm từ 34.71s về 5.20s!).
```

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — NHÂN TRẮC HỌC ERGONOMICS & SỐ HÓA OLE BẰNG MES/RFID

### Thiết Kế Trạm Làm Việc Chuẩn Nhân Trắc Học (Ergonomics)
Năng suất công nhân (U) suy giảm 15-20% vào cuối ca do sự mệt mỏi thể chất tích tụ (Fatigue). Kỹ sư IE đẳng cấp thế giới triệt tiêu mệt mỏi bằng thiết kế bàn thao tác chuẩn:

1. **Vùng Thao Tác Vàng (The Golden Working Zone):**
   - Bán kính với tay tối ưu: **Dưới 40 cm** tính từ ngực công nhân, cẳng tay gập một góc 90° đến 100°.
   - Mọi linh kiện và dụng cụ dùng liên tục (tần suất > 5 lần/phút) bắt buộc phải nằm trong vùng này.
   - Triệt tiêu hoàn toàn động tác cúi gập lưng (Back bending > 20°) hoặc kiễng chân vươn tay quá đầu.

2. **Độ cao mặt bàn thao tác chuẩn theo tính chất công việc:**
   - *Công việc lắp ráp vi mạch / đòi hỏi độ chính xác cao:* Mặt bàn cao hơn khuỷu tay 5 - 10 cm (có điểm tựa cho cẳng tay chống mỏi).
   - *Công việc lắp ráp nhẹ:* Mặt bàn thấp hơn khuỷu tay 5 - 10 cm.
   - *Công việc đóng gói nặng / dùng lực ép thân trên:* Mặt bàn thấp hơn khuỷu tay 15 - 20 cm.

### Kiến Trúc Số Hóa Đo Lường OLE Tự Động (Smart Paperless Genba)
Thay vì dùng bảng ghi chép giấy cuối ca vừa tốn công vừa dễ gian lận số liệu, các nhà máy thông minh triển khai giải pháp số hóa tự động:

```text
┌────────────────────────────────────────────────────────────────────────┐
│  KIẾN TRÚC THU THẬP & TÍNH TOÁN OLE THỜI GIAN THỰC (REAL-TIME MES)     │
└────────────────────────────────────────────────────────────────────────┘

  [Thẻ RFID Công Nhân]  ──(Quẹt thẻ đầu ca)──>  Ghi nhận Availability (Giờ Có Mặt)
                                                       │
  [Cảm Biến Quang PLC]  ──(Đếm xung sản phẩm)──> Ghi nhận Sản Lượng Tức Thì
                                                       │
  [Trạm QC Vision AI ]  ──(Phát hiện khuyết tật)─> Ghi nhận Phế Phẩm Thao Tác
                                                       │
                                                       ▼
                            ┌────────────────────────────────────┐
                            │      HỆ THỐNG MES PHÂN TẦNG        │
                            │   Tính OLE tự động từng 15 phút    │
                            └────────────────────────────────────┘
                                       │              │
                     ┌─────────────────┘              └────────────────┐
                     ▼                                                 ▼
        [Andon TV Treo Trên Chuyền]                    [Phân Hệ SAP ERP PP/CO]
     Báo động đỏ khi U < 80% để Quản Đốc           Hạch toán giá thành biến đổi lương
     xuống xưởng hỗ trợ ngay lập tức               theo Lệnh Sản Xuất (Work Order)
```

### Phương Pháp Đào Tạo Kỹ Năng Đa Năng TWI (Training Within Industry)
Để duy trì OLE ổn định khi có biến động công nhân vắng mặt, nhà máy áp dụng chương trình TWI với 3 hợp phần:
- **Job Instruction (JI - Hướng dẫn công việc):** Chuẩn hóa việc hướng dẫn thợ mới qua 4 bước: (1) Chuẩn bị tâm thế, (2) Trình bày thao tác then chốt và lý do an toàn, (3) Cho thợ mới làm thử và tự giải thích, (4) Thả lỏng theo dõi kèm cặp.
- **Job Methods (JM - Cải tiến phương pháp):** Đào tạo chính công nhân biết tự đặt câu hỏi 5W1H cho từng cử động của mình để đề xuất Kaizen.
- **Job Relations (JR - Quan hệ công việc):** Kỹ năng giải quyết xung đột, xây dựng tinh thần đồng đội cho các Tổ trưởng chuyền.

---

### 📌 CASE STUDY 4 (ĐẶC THÙ NHÀ MÁY CÁP ĐIỆN CADIVI): BIỂU ĐỒ NGƯỜI–MÁY (MAN-MACHINE CHART) — 1 CÔNG NHÂN ĐỨNG NHIỀU MÁY BỆN/KÉO & TỐI ƯU OLE ĐÓNG CUỘN

**Bài Toán A — Mô Hình 1 Công Nhân Đứng Nhiều Máy Bện Xoắn Đôi (Double Twist Buncher):**
Tại phân xưởng Bện dây dân dụng mềm (`VCm 1.5 mm²`), mỗi máy Buncher chạy đầy 1 rulo thành phẩm 630mm hết **32 phút máy tự chạy** (`T = 32 phút`). Sau đó công nhân cần:
- Tháo rulo đầy, lắp rulo rỗng, hàn/nối sợi, bấm chạy lại: `a = 8 phút`.
- Di chuyển sang máy kế tiếp & kiểm tra lực căng/nhãn rulo: `w = 2 phút`.

```text
┌────────────────────────────────────────────────────────────────────────┐
│  TÍNH SỐ MÁY TỐI ƯU 1 CÔNG NHÂN PHỤ TRÁCH (MAN-MACHINE CHART)         │
└────────────────────────────────────────────────────────────────────────┘

1. Số máy lý thuyết tối đa 1 công nhân đứng được mà KHÔNG để máy chờ:
           a + T        8 + 32       40 phút
   N   =  ───────  =  ──────────  =  ───────  =  4.0 máy / công nhân
           a + w        8 + 2        10 phút

2. Kiểm tra hiệu suất theo 2 phương án bố trí thực tế tại xưởng:
   • Phương án 1 (Hiện trạng — 1 người đứng 2 máy):
     - Công nhân bận: 2 × (8 + 2) = 20 phút / chu kỳ 40 phút → Hiệu suất người chỉ đạt 50%!
     - Lãng phí tới 50% quỹ lương nhân công trực tiếp!
   • Phương án 2 (Tối ưu OE — 1 người đứng 3 máy, có dự phòng xử lý đứt sợi):
     - Công nhân bận: 3 × (8 + 2) = 30 phút / chu kỳ 40 phút → Utilization đạt 75%.
     - Còn 10 phút đệm (25%) để xử lý đứt sợi bất ngờ, cân phế và làm 5S mà không gây
       hiện tượng giao thoa máy (Machine Interference — 2 máy dừng cùng lúc phải chờ người).
   → Chuyển từ 1 người/2 máy sang 1 người/3 máy: Năng suất lao động (OLE) TĂNG 50%,
     cắt giảm 33% định biên nhân công trực tiếp khu bện mà OEE máy vẫn giữ vững > 85%!
```

**Bài Toán B — Cải Tiến OLE Tại Tổ Đóng Cuộn Khoanh 100m Dây Dân Dụng:**
- Trước cải tiến: 4 công nhân (1 người đứng máy cuộn, 1 người buộc dây rút/dán tem, 1 người bọc màng co nhiệt, 1 người xếp thùng/pallet) — Trạm dán tem & buộc dây bị nghẽn (`CT = 28 giây/cuộn`) trong khi máy cuộn chỉ mất `18 giây/cuộn` → `LBE = 68%`.
- Giải pháp OE: Gắn máy cấp dây rút tự động + súng bắn tem mã vạch liên kết máy cuộn tự động in tem ngay khi đủ 100.0 mét → Kéo chu kỳ trạm nghẽn từ 28s xuống 19s, rút từ 4 xuống 3 người trên chuyền đóng gói (`LBE` tăng từ `68%` lên `92%`, tăng sản lượng đóng gói thêm **+47%** mỗi ca!).
"""
    },

    "smed": {
        "title": "Cẩm Nang Kỹ Thuật SMED — Rút Ngắn Thời Gian Chuyển Đổi Khuôn/Mã Hàng Dưới 10 Phút",
        "summary": "Quy trình 4 bước của Shigeo Shingo, phân tách thao tác Trong vs Ngoài, Case Study ép nhựa 85p xuống 8p40s, kịch bản 2 người song song F1 Pit-stop và 6 cơ cấu gá kẹp 1 chạm.",
        "category": "Sản Xuất (Manufacturing)",
        "content": """# ⚡ CẨM NANG THỰC CHIẾN SMED (SINGLE-MINUTE EXCHANGE OF DIE)
*(Rút Ngắn Thời Gian Chuyển Đổi Khuôn Mẫu & Đổi Mã Hàng Về Mức Dưới 10 Phút)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — SMED LÀ GÌ VÀ VÌ SAO SMED LÀ TRÁI TIM CỦA SẢN XUẤT LEAN?
SMED (Single-Minute Exchange of Die) là phương pháp luận mang tính cách mạng do kỹ sư huyền thoại **Shigeo Shingo** sáng lập tại Toyota, với mục tiêu đưa thời gian chuyển đổi khuôn mẫu hoặc đổi mã hàng (Changeover Time) về mức **Dưới 1 con số (Single-Minute: dưới 10 phút)**.

```text
┌────────────────────────────────────────────────────────────────────────┐
│  ĐỊNH NGHĨA CHUẨN VỀ THỜI GIAN CHUYỂN ĐỔI (CHANGEOVER TIME)            │
└────────────────────────────────────────────────────────────────────────┘

  [Sản phẩm đạt chuẩn CUỐI CÙNG của Lô A]  
                     │
                     ▼ ─── BẮT ĐẦU TÍNH GIỜ CHANGEOVER ───
  • Dừng máy, tháo khuôn cũ, cẩu khuôn mới, căn chỉnh
  • Chạy thử, đo kiểm tra kích thước
                     ▲ ─── KẾT THÚC TÍNH GIỜ CHANGEOVER ───
                     │
  [Sản phẩm đạt chuẩn ĐẦU TIÊN của Lô B chạy ở vận tốc danh định]
```

> [!TIP]
> **Tác động đòn bẩy của SMED đối với toàn chuỗi giá trị:** Khi thời gian đổi khuôn giảm từ 2 tiếng xuống 8 phút, nhà máy không còn bị bắt buộc phải chạy các lô hàng khổng lồ (Large Batch). Doanh nghiệp có thể chuyển sang sản xuất linh hoạt theo lô nhỏ (Small Batch / High-Mix Low-Volume), cắt giảm 70% tồn kho thành phẩm (WIP) và rút ngắn thời gian giao hàng (Lead Time) từ 3 tuần xuống còn 3 ngày!

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — QUY TRÌNH 4 GIAI ĐOẠN SHINGO KINH ĐIỂN

```text
┌────────────────────────────────────────────────────────────────────────┐
│  4 GIAI ĐOẠN TRIỂN KHAI SMED THEO CHUẨN SHIGEO SHINGO                  │
└────────────────────────────────────────────────────────────────────────┘

  [Giai đoạn 0: Hiện trạng hỗn loạn]  (Máy dừng, công nhân chạy tìm đồ nghề)
                 │
                 ▼
  [Giai đoạn 1: Phân tách rạch ròi Thao tác Trong & Ngoài] (Giảm ngay 30-50%)
                 │
                 ▼
  [Giai đoạn 2: Chuyển đổi thao tác Trong thành thao tác Ngoài]
                 │
                 ▼
  [Giai đoạn 3: Hợp lý hóa & Tinh gọn toàn bộ thao tác còn lại]
```

### 1. Thao tác Trong (Internal Setup - I):
- Là những hành động **CHỈ CÓ THỂ THỰC HIỆN KHI MÁY ĐÃ DỪNG HẲN**.
- Ví dụ: Tháo bu-lông kẹp khuôn cũ, cẩu khuôn cũ ra khỏi bàn ép, đặt khuôn mới vào rãnh định vị.

### 2. Thao tác Ngoài (External Setup - E):
- Là những hành động **HOÀN TOÀN CÓ THỂ LÀM TRƯỚC KHI DỪNG MÁY (hoặc sau khi máy mới đã chạy lại)**.
- Ví dụ: Lấy khuôn mới từ kho về đặt sẵn sát vạch máy, chuẩn bị sẵn bu-lông lục giác, gia nhiệt trước phôi/khuôn, chuẩn bị tài liệu thông số kỹ thuật (Recipe).
- *Quy tắc vàng số 1 của SMED:* **TUYỆT ĐỐI KHÔNG BAO GIỜ để máy dừng rồi mới bắt đầu đi tìm dụng cụ hay nâng khuôn từ kho về!**

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — CASE STUDY THỰC TẾ: RÚT NGẮN THỜI GIAN ĐỔI KHUÔN MÁY ÉP NHỰA TỪ 85 PHÚT XUỐNG 8 PHÚT 40 GIÂY

**Bối cảnh tại nhà máy linh kiện ô tô:**
Máy ép nhựa 450 tấn mất trung bình 85 phút cho mỗi lần đổi khuôn. Nhà máy phải chạy lô 5,000 sản phẩm mới bõ chi phí dừng máy, gây ứ đọng kho hàng. Đội ngũ Kỹ sư Cải tiến đã tổ chức 1 tuần Kaizen Blitz theo SMED.

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  BẢNG BÓC TÁCH & TỐI ƯU HÓA 10 THAO TÁC ĐỔI KHUÔN TRƯỚC VS SAU KAIZEN                  │
├────┬──────────────────────────────────┬──────────┬──────────┬──────────┬───────────────┤
│ STT│ Mô Tả Thao Tác Thao Tác          │ Ban Đầu  │ Phân Loại│ Sau Kaizen│ Giải Pháp Kỹ Thuật            │
├────┼──────────────────────────────────┼──────────┼──────────┼──────────┼───────────────┤
│ 1  │ Đi tìm và cẩu khuôn mới từ kho về│ 15 phút  │ External │ 0 phút   │ Chuyển ra Ngoài: Đặt sát máy  │
│ 2  │ Đi tìm cờ lê, lục giác, bu-lông  │ 8 phút   │ External │ 0 phút   │ Bảng 5S xe đồ nghề chuyên dụng│
│ 3  │ Tháo 8 bu-lông dài khuôn cũ      │ 12 phút  │ Internal │ 1.5 phút │ Kẹp thủy lực 1-chạm (Clamp)   │
│ 4  │ Rút 8 ống nước làm mát cũ        │ 6 phút   │ Internal │ 1.0 phút │ Khớp nối nhanh (Quick Coupler)│
│ 5  │ Cẩu khuôn cũ ra, cẩu khuôn mới vào│ 14 phút  │ Internal │ 3.0 phút │ Vạch định vị Laser + Chốt côn │
│ 6  │ Siết 8 bu-lông khuôn mới         │ 11 phút  │ Internal │ 1.5 phút │ Kẹp thủy lực khóa 1 nút bấm   │
│ 7  │ Cắm 8 ống nước làm mát khuôn mới │ 5 phút   │ Internal │ 1.0 phút │ Cụm gom đa cổng (Manifold)    │
│ 8  │ Chờ gia nhiệt khuôn lên 80°C     │ 25 phút  │ External │ 0 phút   │ Sấy nóng trước ở trạm phụ bên │
│ 9  │ Cài đặt thông số nhiệt/áp suất   │ 4 phút   │ External │ 0.5 phút │ Quét mã vạch nạp Recipe tự động│
│ 10 │ Ép thử và đo chỉnh phế phẩm đầu ca│ 15 phút  │ Internal │ 2.0 phút │ Cữ gá cấm xoay, ép 1 chiếc đạt│
├────┴──────────────────────────────────┴──────────┴──────────┴──────────┴───────────────┤
│ TỔNG THỜI GIAN MÁY DỪNG (DOWNTIME):    │ 85 PHÚT  │          │ 8 PHÚT 40 GIÂY (GIẢM 89.8%!)  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. KỊCH BẢN PHỐI HỢP 2 NGƯỜI SONG SONG (F1 PIT-STOP WORKFLOW)
Để đổi khuôn an toàn và siêu tốc trong 8 phút, hai kỹ thuật viên A và B phối hợp như đội thay lốp xe đua F1:

```text
┌────────────────────────────────────────────────────────────────────────┐
│  SƠ ĐỒ PHÂN CÔNG THAO TÁC SONG SONG GIỮA 2 KỸ THUẬT VIÊN               │
└────────────────────────────────────────────────────────────────────────┘

  [Tín hiệu máy dừng] ──────────────────────────────────────────────────
           │
           ├──────────────────────────────┬──────────────────────────────┐
           ▼                              ▼                              ▼
  [KỸ THUẬT VIÊN A - ĐỨNG TRƯỚC]         [KỸ THUẬT VIÊN B - ĐỨNG SAU]   [HỆ THỐNG AN TOÀN]
  • Phút 0-1: Tháo khớp nước trước       • Phút 0-1: Tháo khớp nước sau • Khóa LOTO điện
  • Phút 1-2: Nhả kẹp thủy lực trước     • Phút 1-2: Nhả kẹp thủy lực sau• Bấm nút mở kẹp
  • Phút 2-5: Hướng dẫn móc cẩu khuôn cũ • Phút 2-5: Đẩy khuôn mới vào ray • Cần cẩu xoay 180°
  • Phút 5-6: Khóa chốt định vị côn      • Phút 5-6: Kiểm tra cữ kẹp sau • Khóa thủy lực
  • Phút 6-7: Cắm cụm Manifold nước trước • Phút 6-7: Cắm cụm Manifold sau• Mở van làm mát
  • Phút 7-8: Quét Barcode nạp Recipe    • Phút 7-8: Vệ sinh phễu nhựa  • Bấm chạy tự động
```

---

## 5. 6 CƠ CẤU CƠ KHÍ GÁ KẸP MỘT CHẠM (ONE-TOUCH CLAMPING)
Kỹ sư cơ khí Lean loại bỏ lãng phí vặn ren ốc bằng các cơ cấu sau:
1. **Lỗ khóa hình quả lê (Pear-shaped hole) kết hợp long đen chữ U:** Bu-lông chỉ cần nới lỏng đúng 1 vòng quay là nhấc được chi tiết ra ngoài.
2. **Kẹp nêm / Chốt côn (Wedge clamp):** Dùng búa gõ nhẹ 1 nhịp chốt nêm để khóa chặt vị trí thay cho việc siết 4 bu-lông dài.
3. **Cơ cấu kẹp Cam (Cam-action latch):** Gạt tay kẹp 90° để tạo lực ép 200 kg định vị đồ gá.
4. **Khớp nối nhanh thủy lực/khí nén (Pneumatic Quick Coupler):** Ấn vào là khóa chặt, gạt vòng đệm là nhả tức thì.
5. **Cụm gom đường nước Manifold:** Thay vì cắm từng ống nước riêng rẽ, 8 đường ống được gộp vào 1 khối cắm đa chân (Multi-coupling plate).
6. **Cữ chặn đệm bậc (Stepped spacer):** Chiều cao khuôn khác nhau được bù bằng các khối đệm chuẩn, không cần vặn ren kích nâng bàn máy.

---

## 6. TẦNG 4: CHUYÊN GIA (EXPERT) — CASE STUDY ĐẶC THÙ NGÀNH DÂY CÁP ĐIỆN (CADIVI): SMED CHUYỂN ĐỔI MÀU NHỰA & TIẾT DIỆN MÁY ĐÙN BỌC CÁP (55 PHÚT → 12 PHÚT)

**Bối cảnh thực tế tại xưởng Đùn Bọc Cách Điện PVC/XLPE:**
Mỗi lần chuyển đổi từ dây `VC 4.0 mm² (Màu Đen)` sang dây `VC 2.5 mm² (Màu Trắng)` trên dây chuyền đùn Ø 70mm mất trung bình **55 phút dừng máy**, xả bỏ **25 kg nhựa hỗn hợp (Purge Scrap)** và cắt bỏ **160 mét dây đồng bọc nhựa lỗi đầu ca**.

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  BẢNG BÓC TÁCH SMED MÁY ĐÙN BỌC CÁP TRƯỚC VS SAU CẢI TIẾN (55 PHÚT → 12 PHÚT)          │
├────┬────────────────────────────────────┬──────────┬──────────┬──────────┬─────────────┤
│ STT│ Thao Tác Chuyển Đổi Máy Đùn        │ Ban Đầu  │ Phân Loại│ Sau SMED │ Giải Pháp   │
├────┼────────────────────────────────────┼──────────┼──────────┼──────────┼─────────────┤
│ 1  │ Hút hết nhựa Đen & xả sang Trắng   │ 18 phút  │ Điều độ  │ 3.0 phút │ Chuỗi màu + │
│    │ (đổi ngược Tối → Sáng cực lâu)     │          │ Internal │          │ Purging Cpd │
├────┼────────────────────────────────────┼──────────┼──────────┼──────────┼─────────────┤
│ 2  │ Đi kho lấy hạt nhựa & sấy khô      │ 10 phút  │ External │ 0.0 phút │ Phễu hút di │
│    │                                    │          │          │          │ động sấy sẵn│
├────┼────────────────────────────────────┼──────────┼──────────┼──────────┼─────────────┤
│ 3  │ Tháo đầu chữ thập, thay Chày-Cối   │ 12 phút  │ Internal │ 3.5 phút │ Đầu tháo    │
│    │ (Tip & Die) và chỉnh ốc tâm        │          │          │          │ nhanh tự tâm│
├────┼────────────────────────────────────┼──────────┼──────────┼──────────┼─────────────┤
│ 4  │ Gia nhiệt lại đầu đùn mới từ nguội │  8 phút  │ External │ 0.0 phút │ Tủ sấy nóng │
│    │ lên 165°C                          │          │          │          │ sẵn bên ngoài│
├────┼────────────────────────────────────┼──────────┼──────────┼──────────┼─────────────┤
│ 5  │ Thay rulo đồng 2.5mm², xỏ dây      │  4 phút  │ External │ 2.5 phút │ Dual Pay-off│
│    │ qua đầu đùn & nối đầu dây          │          │ Internal │          │ + Hàn nối   │
├────┼────────────────────────────────────┼──────────┼──────────┼──────────┼─────────────┤
│ 6  │ Chạy thử, đo kính hiển vi, chỉnh   │  3 phút  │ Internal │ 3.0 phút │ Nạp Recipe  │
│    │ tốc độ đạt chuẩn đường kính Laser  │          │          │          │ PLC tự động │
├────┴────────────────────────────────────┴──────────┴──────────┴──────────┴─────────────┤
│ TỔNG THỜI GIAN MÁY ĐÙN DỪNG:            │ 55 PHÚT  │          │ 12 PHÚT (GIẢM 78.2%!)  │
│ LƯỢNG NHỰA XẢ PURGE + DÂY PHẾ ĐẦU CA:   │ 25 kg    │          │ 6 kg (GIẢM 76.0%!)     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

**4 Vũ Khí SMED Đặc Thù Ngành Dây Cáp Điện (Bắt Buộc Nắm Vững):**
1. **Lập lịch theo Chuỗi Màu (Color Sequencing):** Luôn xếp thứ tự `Trắng → Vàng → Xanh lá → Đỏ → Xanh dương → Đen` (hoặc dùng công nghệ *Masterbatch* cấp hạt màu trực tiếp tại cổ phễu thay vì dùng nhựa pha sẵn màu).
2. **Sấy Nóng Trước Đầu Chày-Cối (External Pre-heating):** Đầu Crosshead/Tip-Die dự phòng được vệ sinh, lắp ghép và sấy sẵn 160°C trong tủ nhiệt đặt ngay cạnh máy đùn trước giờ đổi mã 30 phút.
3. **Đầu Đùn Tự Định Tâm (Self-Centering Crosshead):** Triệt tiêu 100% bước vặn 4 ốc căn chỉnh độ lệch tâm (Eccentricity) thủ công kéo dài 10–15 phút.
4. **Cụm Nhả & Thu Dây Kép (Dual Pay-off / Dual Take-up) + Bộ Tích Dây (Accumulator) + Máy Hàn Đối Đầu (Butt Welder):** Cho phép công nhân hàn nối cuộn đồng mới ngay khi dây chuyền đùn vẫn chạy ở tốc độ 300 m/phút → Thời gian dừng đổi rulo = **0 giây**!
"""
    },

    "lean_muda": {
        "title": "Cẩm Nang Lean Manufacturing Toàn Diện: 8 Lãng Phí (TIMWOODS), VSM, 5S, Kaizen & Poka-Yoke",
        "summary": "Cẩm nang 4 tầng (Basic → Expert): 8 lãng phí TIMWOODS gắn ví dụ thực tế nhà máy cáp điện, VSM Current → Future State, Hệ thống kéo Kanban/Heijunka, 5S chuẩn Nhật và 5 cơ cấu Poka-Yoke xưởng cáp.",
        "category": "Sản Xuất (Manufacturing)",
        "content": r"""# 🧹 CẨM NANG LEAN MANUFACTURING TOÀN DIỆN: 8 LÃNG PHÍ, VSM, 5S & POKA-YOKE
*(Từ Triết Lý Nền Tảng Đến Triển Khai Thực Chiến Tại Nhà Máy Dây Cáp Điện CADIVI)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — 5 NGUYÊN TẮC LEAN & 8 LOẠI LÃNG PHÍ (TIMWOODS)

### 5 Nguyên Tắc Vàng Của Sản Xuất Tinh Gọn (James Womack & Daniel Jones):
1. **Xác định Giá trị (Define Value):** Chỉ những gì khách hàng sẵn sàng trả tiền (sợi đồng đạt điện trở IEC, lớp cách điện đạt chiều dày chuẩn, giao đúng hẹn) mới là Giá trị (VA).
2. **Lập Bản đồ Chuỗi Giá trị (Map the Value Stream):** Phơi bày toàn bộ hành trình từ đồng rod nhập kho đến cuộn cáp xuất xưởng để lột trần mọi bước chờ đợi và lãng phí.
3. **Tạo Dòng chảy Liên tục (Create Flow):** Loại bỏ nút thắt, giảm kích thước lô, hạn chế để rulo nằm chờ nhiều ngày giữa Kéo – Bện – Đùn.
4. **Thiết lập Hệ thống Kéo (Establish Pull):** Công đoạn sau dùng đến đâu, công đoạn trước mới sản xuất bù đến đó (Kanban / Siêu thị rulo), chấm dứt sản xuất Đẩy (Push) gây núi tồn kho.
5. **Theo đuổi Sự Hoàn hảo (Pursue Perfection):** Duy trì Kaizen hàng ngày không có điểm dừng.

### 8 Loại Lãng Phí (TIMWOODS) Kèm Ví Dụ Thực Chiến Tại Nhà Máy Dây Cáp Điện:
```text
┌────┬─────────────────────────┬─────────────────────────────────────────────────────────┐
│ Ký │ Loại Lãng Phí           │ Biểu Hiện Thực Tế Tại Nhà Máy Dây Cáp Điện (CADIVI)     │
├────┼─────────────────────────┼─────────────────────────────────────────────────────────┤
│ T  │ Transportation          │ Xe nâng chở rulo đồng 2 tấn chạy lòng vòng 400m giữa    │
│    │ (Vận chuyển thừa)       │ xưởng Kéo, kho đệm ngoài trời và xưởng Bện/Đùn.         │
├────┼─────────────────────────┼─────────────────────────────────────────────────────────┤
│ I  │ Inventory               │ Hàng trăm rulo bán thành phẩm (WIP) chất kín lối đi     │
│    │ (Tồn kho dư thừa)       │ chờ đùn bọc suốt 5–7 ngày, chôn hàng chục tỷ đồng vốn.  │
├────┼─────────────────────────┼─────────────────────────────────────────────────────────┤
│ M  │ Motion                  │ Công nhân đóng cuộn cúi xuống sàn nhấc cuộn 100m, đi bộ │
│    │ (Thao tác thừa)         │ 20m lấy tem nhãn, tìm thước kẹp hoặc lục giác đổi khuôn.│
├────┼─────────────────────────┼─────────────────────────────────────────────────────────┤
│ W  │ Waiting                 │ Máy đùn dừng bật nhiệt chờ xe nâng cấp rulo ruột đồng,  │
│    │ (Thời gian chờ đợi)     │ chờ QC cắt mẫu đo chiều dày mới cho chạy tiếp.          │
├────┼─────────────────────────┼─────────────────────────────────────────────────────────┤
│ O  │ Overproduction          │ Kéo/bện dư rulo mã dây chưa có đơn hàng để "lấy sản     │
│    │ (SX thừa - NGUY HIỂM #1)│ lượng tấn" → Che giấu lỗi và sinh ra tồn kho chết!      │
├────┼─────────────────────────┼─────────────────────────────────────────────────────────┤
│ O  │ Overprocessing          │ Bọc lớp cách điện dày dư +0.10 mm so với chuẩn TCVN     │
│    │ (Gia công thừa)         │ (Over-thickness) hoặc kéo đồng dư +0.01 mm (Give-away). │
├────┼─────────────────────────┼─────────────────────────────────────────────────────────┤
│ D  │ Defects                 │ Dây lỗi thủng Spark, lệch tâm, đứt sợi phải cắt nối,    │
│    │ (Phế phẩm & Làm lại)    │ mẩu cáp ngắn 80m dư rulo bán phế đồng dính nhựa mất 20%.│
├────┼─────────────────────────┼─────────────────────────────────────────────────────────┤
│ S  │ Skills Unused (Thứ 8)   │ Không lắng nghe góp ý của thợ máy đùn/kéo 10 năm kinh   │
│    │ (Lãng phí trí tuệ)      │ nghiệm về vị trí đặt đồ nghề, lỗi kẹt puli hay rò dầu.  │
└────┴─────────────────────────┴─────────────────────────────────────────────────────────┘
```

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — 5S CHUẨN NHẬT, KAIZEN & HỆ THỐNG POKA-YOKE

### Quy Trình 5S Thực Chiến Tại Hiện Trường (Không Phải Dọn Vệ Sinh Hình Thức):
- **S1 — Seiri (Sàng lọc):** Phân loại đồ cần dùng và đồ thừa (rulo hỏng, khuôn mòn cũ, hạt nhựa dư mất nhãn). Dán **Thẻ Đỏ (Red Tag)** tập kết về khu vực cách ly và thanh lý trong 48 giờ.
- **S2 — Seiton (Sắp xếp):** *"30 giây tìm thấy bất cứ thứ gì"* — Bảng treo dụng cụ có hình bóng (Shadow Board) cho bộ cờ lê/Tip-Die ngay cạnh máy đùn; kẻ vạch sơn phân vùng rulo Đạt (Xanh) – Chờ QC (Vàng) – Phế/Cách ly (Đỏ).
- **S3 — Seiso (Sạch sẽ = Kiểm tra):** Khi lau chùi máy kéo/bện/đùn, công nhân phát hiện rò rỉ dầu nhũ tương, lỏng bu-lông đầu chữ thập, bụi bám mắt Laser Gauge → Dán **Thẻ Fuguai (Thẻ bất thường)** báo bảo trì xử lý sớm trước khi máy dừng đột xuất.
- **S4 — Seiketsu (Săn sóc):** Chuẩn hóa 3S thành bảng tiêu chuẩn trực quan kèm ảnh mẫu "Trước – Sau" và Checklist chấm điểm Audit 5S định kỳ hàng tuần.
- **S5 — Shitsuke (Sẵn sàng):** Xây dựng thói quen kỷ luật tự giác, biểu dương tổ xuất sắc trên bảng SQDC.

### 5 Ứng Dụng Poka-Yoke Thực Chiến Trong Nhà Máy Dây Cáp Điện:
1. **Poka-Yoke Kiểm Soát (Control) — Cảm Biến Đứt Sợi Quang/Cơ Trên Máy Bện:** Ngay khi 1 trong 19 sợi đồng bị đứt, cần cảm biến sập xuống ngắt PLC dừng máy bện trong 0.5 giây, ngăn chặn tạo ra hàng trăm mét ruột dẫn thiếu sợi!
2. **Poka-Yoke Quét Barcode Rulo (Chống Bện/Đùn Nhầm Tiết Diện):** Công nhân bắt buộc quét mã vạch lệnh sản xuất và mã vạch từng rulo đồng đầu vào; nếu sai tiết diện/sai loại đồng-nhôm, hệ thống khóa nút khởi động máy.
3. **Poka-Yoke Liên Động Cửa Lồng Máy Bện (Safety Interlock):** Cửa bảo vệ lồng quay mở ra → công tắc hành trình tự động khóa nguồn động cơ, tuyệt đối không thể chạy máy khi đang thao tác nạp rulo.
4. **Poka-Yoke Spark Tester Liên Động Phun Mực Đánh Dấu:** Khi phát hiện tia lửa đánh thủng cách điện, máy lập tức phun chấm mực màu tương phản tại đúng tọa độ lỗi và ghi nhận vị trí mét lên màn hình để tổ sang cuộn cắt bỏ chính xác, không để lọt ra khách hàng.
5. **Poka-Yoke Ngăn Đổi Nhầm Cỡ Khuôn (Color-Coded Die Storage):** Bộ khuôn kéo/chày-cối được mã màu và khắc laser tiết diện rõ nét, giá cắm khuôn có rãnh định hình riêng từng size không thể cắm nhầm vị trí.

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — BẢN ĐỒ CHUỖI GIÁ TRỊ (VSM) & TÍNH TOÁN PCE%

**Case Study VSM Thực Chiến — Đơn Hàng Cáp Lực CXV 3x50+1x25 (Lô 10,000 mét):**

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  SO SÁNH VSM HIỆN TRẠNG (CURRENT STATE) VS TƯƠNG LAI (FUTURE STATE) — NHÀ MÁY CÁP      │
└────────────────────────────────────────────────────────────────────────────────────────┘

[CURRENT STATE — HỆ THỐNG ĐẨY PUSH TRUYỀN THỐNG]:
  Kéo Thô RBD  ──(Chờ 2.5 ngày)──>  Bện Nén 50mm²  ──(Chờ 3.0 ngày)──>  Đùn XLPE
  CT: 4.5 giờ                        CT: 6.0 giờ                         CT: 5.5 giờ
      ──(Chờ xông Sauna 1.5 ngày)──>  Ghép Lõi  ──(Chờ 2.5 ngày)──>  Đùn Vỏ PVC & QC
                                      CT: 5.0 giờ                    CT: 6.5 giờ

  • Tổng Thời Gian Gia Công Tạo Giá Trị (Total VA Time) = 4.5 + 6.0 + 5.5 + 5.0 + 6.5 = 27.5 giờ (1.15 ngày).
  • Tổng Thời Gian Lưu Chuyển Toàn Chuỗi (Total Lead Time) = 1.15 + 2.5 + 3.0 + 1.5 + 2.5 + 1.35 (kho) = 12.0 ngày (288 giờ).
  • Hiệu Quả Chuỗi Giá Trị (Process Cycle Efficiency — PCE):
             Total VA Time          27.5 giờ
    PCE  =  ────────────────  =  ──────────────  × 100%  =  9.55%
            Total Lead Time         288 giờ
  → Hơn 90% thời gian là RULO NẰM CHỜ LÃNG PHÍ trên sàn xưởng!

[FUTURE STATE — ÁP DỤNG SIÊU THỊ KANBAN, SMED & ĐIỀU ĐỘ ĐỒNG BỘ]:
  • Giới hạn kho đệm WIP (CONWIP) giữa các công đoạn tối đa 0.5 ngày.
  • Áp dụng SMED rút đổi mã đùn từ 55p → 12p để giảm kích thước lô chạy.
  • Xếp lịch đồng bộ vào bể xông hơi XLPE ngay khi đùn xong (chờ ≤ 4 giờ).
  → Tổng Lead Time giảm từ 12.0 ngày xuống 4.2 ngày (100.8 giờ)!
  → PCE tăng từ 9.55% lên 27.3%; Giải phóng 65% tồn kho rulo WIP & giao hàng nhanh gấp 2.8 lần!
```

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — HỆ THỐNG KÉO KANBAN, HEIJUNKA & VĂN HÓA KAIZEN

1. **San Phẳng Sản Xuất (Heijunka — Production Leveling):**
   - Thay vì tuần đầu tháng nhàn rỗi rồi tuần cuối tháng chạy tăng ca điên cuồng gây lỗi và hỏng máy (Muri — Quá tải & Mura — Biến động không đều), Heijunka chia đều khối lượng sản xuất và cơ cấu sản phẩm (Product Mix) theo từng ngày/tuần.
   - Áp dụng **Bánh xe sản xuất (Product Wheel)** cho dây chuyền đùn để cân bằng giữa tần suất đổi mã (SMED) và mức tồn kho thành phẩm an toàn.
2. **Phân Biệt 3 Cấp Độ Cải Tiến (Kaizen – Kaikaku – Kakushin):**
   - *Kaizen:* Cải tiến nhỏ hàng ngày chi phí thấp do chính công nhân đề xuất qua phiếu *Teian* (phản hồi trong 48h, thưởng nóng nhỏ, ghi nhận công khai).
   - *Kaikaku:* Sự kiện đột phá 5 ngày (*Kaizen Blitz*): tái cấu trúc toàn bộ 1 dây chuyền SMED hoặc quy hoạch lại kho đệm rulo.
   - *Kakushin:* Đổi mới công nghệ chiến lược (đầu tư dây chuyền đùn có Laser Closed-loop tự động điều chỉnh đường kính hoặc tích hợp MES/SCADA toàn nhà máy).
3. **Quản Trị Thay Đổi Khi Triển Khai Lean (Chống Phản Kháng Xưởng):**
   - Luôn khẳng định nguyên tắc *"Lean không sa thải người — Lean xóa thao tác cực nhọc, nguy hiểm và lãng phí"*.
   - Bắt đầu từ các dự án *Quick-Win* giúp giảm vất vả cho công nhân trước (xe đẩy dụng cụ, tời nâng rulo, cải thiện thông gió/chiếu sáng), đồng hành với Quản đốc đứng tên đồng triển khai để xây dựng văn hóa cải tiến bền vững.
"""
    },

    "bom_cost": {
        "title": "Cẩm Nang Quản Lý Định Mức Vật Tư BOM & Kiểm Soát Hao Phí Giá Thành",
        "summary": "Phân tầng kiến thức BOM từ Basic đến Expert: EBOM vs MBOM vs SBOM, Case Study tính chênh lệch BOM Variance cho lô 10,000 sản phẩm, đối soát 3 điểm, cơ chế Kitting và Two-bin Kanban.",
        "category": "Sản Xuất (Manufacturing)",
        "content": """# 📦 CẨM NANG ĐỊNH MỨC VẬT TƯ BOM & KIỂM SOÁT HAO PHÍ SẢN XUẤT
*(Quản Trị Chi Phí Vật Tư & Triệt Tiêu Hao Phí Từ Cơ Bản Đến Chuyên Gia)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — ĐỊNH NGHĨA & CẤU TRÚC PHÂN TẦNG BOM
BOM (Bill of Materials) là cây danh mục định mức kỹ thuật liệt kê chi tiết mọi nguyên vật liệu thô (Raw Materials), bán thành phẩm (Sub-assemblies), linh kiện tiêu hao và bao bì đóng gói cần thiết để sản xuất ra **1 đơn vị thành phẩm hoàn chỉnh**.

```text
┌────────────────────────────────────────────────────────────────────────┐
│  PHÂN BIỆT 3 CẤP ĐỘ CÂY ĐỊNH MỨC BOM TRONG DOANH NGHIỆP               │
├─────────┬───────────────────┬──────────────────────────────────────────┤
│ Cấp Độ  │ Tên Gọi Chuẩn     │ Đơn Vị Phụ Trách & Vai Trò Cốt Lõi       │
├─────────┼───────────────────┼──────────────────────────────────────────┤
│ EBOM    │ Engineering BOM   │ Phòng R&D / Thiết kế CAD: Cấu trúc hình  │
│         │                   │ học của sản phẩm, chưa tính bao bì/keo   │
├─────────┼───────────────────┼──────────────────────────────────────────┤
│ MBOM    │ Manufacturing BOM │ Phòng PE/IE / Sản xuất: Thứ tự lắp ráp,  │
│         │                   │ cộng thêm tỷ lệ hao hụt công nghệ (Yield)│
├─────────┼───────────────────┼──────────────────────────────────────────┤
│ SBOM    │ Sales BOM         │ Phòng Kinh Doanh: Cấu hình bán cho khách │
│         │                   │ kèm phụ kiện, catalogue, dây sạc cáp     │
└─────────┴───────────────────┴──────────────────────────────────────────┘
```

### Phân Loại 2 Dạng Hao Phí Nguyên Vật Liệu:
1. **Hao phí công nghệ tự nhiên (Inherent / Technological Loss):**
   - Là phần vật tư bắt buộc phải cắt bỏ do đặc thù phương pháp cơ tính gia công (vd: mạt cưa, ba-via đúc, đầu mẩu phôi kim loại cắt thanh 6m thành 450mm, cuống keo nhựa khuôn ép).
   - *Cách quản trị:* Được đo đạc chính xác và tính thẳng vào định mức MBOM (Standard Scrap Factor). Tối ưu bằng phần mềm xếp phôi tự động (Nesting Software).
2. **Hao phí bất thường do vận hành (Abnormal / Operational Scrap):**
   - Là vật tư bị hỏng do con người hoặc máy móc sai sót: phôi trầy xước, khoan sai tâm, chỉnh cữ máy phung phí vật tư test đầu ca, rơi vỡ, bảo quản ẩm mốc trong kho.
   - *Cách quản trị:* Là mục tiêu tối thượng mà Kỹ sư Cải tiến phải triệt tiêu qua biểu đồ Pareto nguyên nhân phế phẩm.

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — CÔNG THỨC PHÂN TÍCH CHÊNH LỆCH BOM (BOM VARIANCE)

```text
┌────────────────────────────────────────────────────────────────────────┐
│  CÔNG THỨC PHÂN TÍCH CHÊNH LỆCH ĐỊNH MỨC VẬT TƯ (BOM VARIANCE)         │
└────────────────────────────────────────────────────────────────────────┘

1. Công thức Lượng Hao Hụt Chênh Lệch (Quantity Variance):
  Qty_Variance = Tổng NVL Thực Tế Xuất Kho - (Thành Phẩm Đạt Chuẩn × Định Mức MBOM)

2. Công thức Giá Trị Thất Thoát Bằng Tiền (Cost Variance):
  Cost_Variance = Qty_Variance  ×  Đơn Giá Mua Vào Của Nguyên Vật Liệu

  • Nếu Variance > 0 : Bị Hao Hụt Vượt Định Mức → Đội chi phí, ăn mòn lợi nhuận!
  • Nếu Variance < 0 : Bất thường dữ liệu (Xuất thiếu linh kiện hoặc bớt xén bước kiểm tra).
  • Nếu Variance = 0 : Quá trình vận hành đạt chuẩn định mức 100%.
```

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — BÀI TOÁN THỰC TẾ LÔ 10,000 SẢN PHẨM (CASE STUDY)

**Bối cảnh tại xưởng cơ khí:**
Công ty sản xuất lô hàng **10,000 Cụm Van Thủy Lực (Mã SP: V-450)** theo Lệnh Sản Xuất số WO-8802.

**Dữ liệu định mức BOM chuẩn và thực tế xuất kho:**
1. **Thép thanh tròn C45 (Ø 32 mm):**
   - Định mức BOM chuẩn: 0.45 kg / sản phẩm (Đã gồm 5% hao phí tiện mạt sắt tự nhiên).
   - Lý thuyết cho 10,000 sản phẩm = 10,000 × 0.45 = 4,500 kg.
   - Thực tế kho đã xuất cấp cho xưởng: **4,850 kg**.
   - Đơn giá: 28,000 VNĐ / kg.
2. **Gioăng cao su chịu dầu NBR:**
   - Định mức BOM chuẩn: 2 chiếc / sản phẩm (Không có hao phí công nghệ).
   - Lý thuyết cho 10,000 sản phẩm = 10,000 × 2 = 20,000 chiếc.
   - Thực tế kho đã xuất cấp cho xưởng: **21,400 chiếc**.
   - Đơn giá: 4,500 VNĐ / chiếc.
3. **Bu-lông cường độ cao M6x25:**
   - Định mức BOM chuẩn: 4 chiếc / sản phẩm.
   - Lý thuyết cho 10,000 sản phẩm = 10,000 × 4 = 40,000 chiếc.
   - Thực tế kho đã xuất cấp cho xưởng: **40,300 chiếc**.
   - Đơn giá: 1,200 VNĐ / chiếc.

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  BẢNG TÍNH TOÁN CHÊNH LỆCH ĐỊNH MỨC BOM CHO LÔ 10,000 SẢN PHẨM                         │
├────┬────────────────────┬──────────┬──────────┬────────────┬───────────┬───────────────┤
│ STT│ Tên Vật Tư         │ BOM Lý Th│ Xuất Thực│ Lượng Lệch │ Đơn Giá   │ Tiền Thiệt Hại│
├────┼────────────────────┼──────────┼──────────┼────────────┼───────────┼───────────────┤
│ 1  │ Thép thanh C45     │ 4,500 kg │ 4,850 kg │ +350 kg    │ 28,000 đ  │ 9,800,000 đ   │
│ 2  │ Gioăng cao su NBR  │ 20,000 c │ 21,400 c │ +1,400 c   │ 4,500 đ   │ 6,300,000 đ   │
│ 3  │ Bu-lông M6x25      │ 40,000 c │ 40,300 c │ +300 c     │ 1,200 đ   │ 360,000 đ     │
├────┴────────────────────┴──────────┴──────────┴────────────┴───────────┴───────────────┤
│ TỔNG THIỆT HẠI VƯỢT ĐỊNH MỨC BOM TRONG 1 LỆNH SẢN XUẤT:                 │ 16,460,000 đ  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

**Quy trình 3 bước điều tra truy tìm nguyên nhân:**
1. **Thép thanh C45 (Mất 350 kg):** Xuống hiện trường kiểm tra phôi thừa đầu mẩu. Phát hiện nhà cung ứng giao thanh thép dài 5.8m thay vì chuẩn 6.0m, khiến mỗi thanh bị thừa đuôi mẩu 40cm không thể tiện thêm van. → Yêu cầu Mua hàng đòi nhà cung ứng bồi thường.
2. **Gioăng cao su NBR (Mất 1,400 chiếc):** Công nhân dùng đầu nhọn tô vít để cậy gioăng vào rãnh làm rách mép gioăng hàng loạt. → Cải tiến làm que tra gioăng bằng nhựa Teflon bo tròn (Poka-Yoke), triệt tiêu hoàn toàn rách gioăng.
3. **Bu-lông M6x25 (Mất 300 chiếc):** Rơi vãi xuống sàn do bao bì rách. → Bố trí khay hứng từ tính (Magnetic Tray) dưới bàn thao tác.

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — KIỂM SOÁT VẬT TƯ BẰNG KITTING & CYCLE COUNTING ABC

### 1. Kỹ Thuật Kitting (Soạn Linh Kiện Đồng Bộ Theo Bộ):
- Thay vì cấp cả bao 5,000 ốc vít và 1,000 gioăng ngổn ngang cạnh chuyền dễ rơi vãi và thất thoát, kho phụ trách chuẩn bị sẵn **Khay Kitting** chứa đúng tỷ lệ linh kiện cho 10 sản phẩm.
- Khi lắp xong 10 chiếc, nếu trên khay còn sót lại 1 chi tiết → Công nhân lập tức nhận biết mình đã quên gắn linh kiện, tự kiểm tra lỗi tại chỗ.

### 2. Mô Hình Kanban Hai Thùng (Two-Bin Kanban):
- Thùng A đặt tại vị trí làm việc; Thùng B đặt dự phòng phía sau.
- Khi Thùng A hết, công nhân kéo Thùng B lên sử dụng và đặt vỏ Thùng A vào vị trí chờ cấp.
- Nhân viên Water Spider tuần tra mỗi 30 phút, nhìn thấy Thùng A rỗng sẽ mang vào kho châm đúng số lượng định mức, ngăn ngừa việc công nhân tự ý tích trữ vật tư riêng tại xưởng.

### 3. Kiểm Kê Luân Phiên (Cycle Counting) Kết Hợp Phân Loại ABC:
- **Nhóm A (20% mã hàng chiếm 80% giá trị - Thép hợp kim, vi mạch, động cơ):** Kiểm đếm hàng tuần.
- **Nhóm B (30% mã hàng chiếm 15% giá trị - Khuôn gá, cảm biến):** Kiểm đếm hàng tháng.
- **Nhóm C (50% mã hàng chiếm 5% giá trị - Ốc vít, vòng đệm, keo):** Kiểm đếm hàng quý.
- Đảm bảo độ chính xác tồn kho hệ thống ERP (Record Inventory Accuracy - RIA) luôn đạt **≥ 98.5%**.

---

## 5. CASE STUDY 2 (ĐẶC THÙ NGÀNH CÁP ĐIỆN CADIVI): CÂY BOM ĐA TẦNG CÁP LỰC CXV 3×50+1×25 & KIỂM SOÁT PHẾ ĐỒNG TRẦN VS ĐỒNG DÍNH NHỰA

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  CẤU TRÚC CÂY BOM ĐA TẦNG (MULTI-LEVEL MBOM) — 1,000 MÉT CÁP CXV 3×50 + 1×25 - 0.6/1kV│
└────────────────────────────────────────────────────────────────────────────────────────┘

Cấp 0: Thành phẩm Cáp lực CXV 3×50+1×25 (1,000 m, Rulo gỗ Ø 1,400mm)
  ├── Cấp 1: Vỏ bọc ngoài PVC màu đen (chiều dày chuẩn 1.8 mm) ─────── ~385 kg nhựa PVC
  ├── Cấp 1: Băng quấn định hình + Dây độn PP (Filler) ─────────────── ~35 kg PP/Tape
  ├── Cấp 1: 3 Lõi pha 50 mm² cách điện XLPE (Đỏ, Vàng, Xanh)
  │     ├── Cấp 2: Nhựa cách điện XLPE Silane (chiều dày 1.0 mm) ───── ~92 kg XLPE (3 lõi)
  │     └── Cấp 2: Ruột đồng bện nén 50 mm² (3 lõi × 1,000m × hệ số xoắn 1.02)
  │           └── Cấp 3: Đồng rod Ø 8.0 mm (kèm 0.4% hao phí kéo/bện) ~1,338 kg Đồng
  └── Cấp 1: 1 Lõi trung tính 25 mm² cách điện XLPE (Màu Đen)
        ├── Cấp 2: Nhựa cách điện XLPE Silane (chiều dày 0.9 mm) ───── ~22 kg XLPE
        └── Cấp 2: Ruột đồng bện nén 25 mm² (1 lõi × 1,000m × hệ số xoắn 1.02)
              └── Cấp 3: Đồng rod Ø 8.0 mm (kèm 0.4% hao phí kéo/bện) ~224 kg Đồng
  ────────────────────────────────────────────────────────────────────────────────────────
  TỔNG ĐỒNG ĐỊNH MỨC = ~1,562 kg (~390 triệu VNĐ — chiếm ~78% tổng giá trị NVL!)
```

**Bẫy Hao Phí Sống Còn Khi Kiểm Soát BOM Cáp Điện:**
1. **Phân tách tuyệt đối 2 loại phế liệu đồng:**
   - *Phế đồng trần (Bare Copper Scrap — từ kéo/ủ/bện):* Bán/tái chế thu hồi lại được **93–96%** giá trị đồng gốc.
   - *Phế đồng dính nhựa (Insulated Copper Scrap — từ đùn/cắt đầu-đuôi/lỗi Spark):* Tốn công tuốt/băm tách nhựa, chỉ thu hồi được **75–82%** → Mỗi 1 tấn đồng đã bọc nhựa bị loại phế làm nhà máy **mất trắng 45–60 triệu VNĐ** so với đồng trần!
2. **Nguyên tắc kiểm soát BOM Variance theo 3 chốt chặn:**
   - Chốt 1 (Trước khi đùn): Cân kiểm tra khối lượng & đo điện trở ruột dẫn sau bện — TUYỆT ĐỐI không đùn bọc nhựa lên cuộn ruột đồng đã lỗi bện hoặc thiếu mét.
   - Chốt 2 (Tại máy đùn): Cân phế nhựa xả (Purge), nhựa thừa cắt đầu-đuôi và kiểm soát chiều dày cách điện trung bình bằng SPC (tránh bọc dư +0.08 mm làm âm BOM nhựa cuối tháng).
   - Chốt 3 (Cuối lệnh sản xuất): Đối soát 3 điểm `Đồng xuất kho = Đồng trong thành phẩm + Đồng tồn rulo dở dang + Đồng phế cân thực tế` — sai lệch khối lượng cho phép phải **< 0.15%**.
"""
    },

    "excel_mfg": {
        "title": "Cẩm Nang Microsoft Excel Nâng Cao (Power Query, Pivot, VBA & Python) Trong Quản Lý Sản Xuất OE",
        "summary": "Cẩm nang 4 tầng (Basic → Expert): Hàm sản xuất cốt lõi, Power Query gom file nhật ký ca Kéo–Bện–Đùn tự động, mô hình Pareto 80/20 & OEE/BOM Variance, VBA Macro và kết hợp Python tự động hóa báo cáo.",
        "category": "Phần Mềm & Công Cụ",
        "content": r"""# 📊 CẨM NANG EXCEL NÂNG CAO (POWER QUERY, VBA & PYTHON) CHO CHUYÊN VIÊN OE
*(Tự Động Hóa Dữ Liệu Sản Xuất Từ Cơ Bản Đến Chuyên Gia — Ứng Dụng Thực Chiến Nhà Máy Dây Cáp Điện)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — CÁC HÀM XƯƠNG SỐNG & QUY TẮC THIẾT KẾ BẢNG DỮ LIỆU CHUẨN

### Quy Tắc Vàng Lưu Trữ Dữ Liệu Sản Xuất (Tidy Data Rule):
- **TUYỆT ĐỐI KHÔNG** gộp ô (Merge Cells) trong bảng dữ liệu thô, không chia mỗi tháng/mỗi máy ra một sheet kiểu báo cáo trình bày rồi dùng công thức cộng tay xuyên sheet!
- Mọi dữ liệu nhật ký ca (Kéo, Bện, Đùn, QC) phải tổ chức theo chuẩn bảng 1 chiều (**Tabular Format**): 1 dòng = 1 ca/1 lệnh chạy máy; mỗi cột = 1 thuộc tính rõ ràng (`Ngay`, `Ca`, `Ma_May`, `Cong_Doan`, `Ma_Cap`, `Chieu_Dai_Dat_m`, `Chieu_Dai_Phe_m`, `Toc_Do_Chuan_m_phut`, `Thoi_Gian_Ke_Hoach_p`, `Ma_Loi_Dung`, `Phut_Dung`, `Phe_Dong_kg`, `Phe_Nhua_kg`).

### Bộ 8 Hàm Excel Bắt Buộc Thành Thạo Cho Chuyên Viên OE:
1. `XLOOKUP(lookup_val, lookup_arr, return_arr, [if_not_found])`: Tra tốc độ chuẩn (m/phút), định mức BOM đồng/nhựa theo mã cáp — thay thế hoàn toàn VLOOKUP chậm và dễ gãy khi chèn cột.
2. `SUMIFS` / `COUNTIFS` / `AVERAGEIFS`: Tổng hợp sản lượng mét dây, số phút dừng máy theo đa điều kiện (Ngày + Ca + Tổ + Mã Lỗi).
3. `AGGREGATE(9, 6, range)` / `SUBTOTAL`: Tính tổng/trung bình tự động bỏ qua dòng ẩn khi Filter và bỏ qua giá trị lỗi `#DIV/0!`.
4. `STDEV.S` & `PERCENTILE.INC`: Tính nhanh độ lệch chuẩn đường kính vỏ cáp và kiểm tra độ phân tán thời gian chuyển đổi SMED ngay trên Excel.
5. `IFERROR(A/B, 0)`: Chặn lỗi chia 0 khi máy không có kế hoạch chạy trong ca.
6. `Pivot Table + Slicer + Timeline`: Tương tác lọc nhanh OEE theo Máy/Ca/Tháng trong 5 giây mà không viết 1 dòng công thức nào.

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — GOM DỮ LIỆU NHIỀU CA TỰ ĐỘNG BẰNG POWER QUERY

Trong nhà máy cáp điện, mỗi phân xưởng (Kéo, Bện, Đùn, Đóng gói) gửi riêng 1 file Excel nhật ký ca mỗi ngày. Copy-paste thủ công mất 1–2 giờ/ngày và cực dễ lệch dòng.

### Quy Trình 6 Bước Power Query (1 Nút Refresh Cập Nhật Toàn Nhà Máy):
1. Đặt toàn bộ file nhật ký ca vào thư mục chuẩn: `D:\CADIVI_OE\NhatKyCa\`.
2. Mở Excel tổng hợp → Tab **Data** → **Get Data** → **From File** → **From Folder**.
3. Chọn thư mục → Bấm **Combine & Transform Data** để mở trình soạn thảo Power Query Editor.
4. Thực hiện các bước làm sạch lặp lại tự động (Applied Steps):
   - Lọc bỏ dòng trống (`Remove Blank Rows`) và dòng tiêu đề lặp lại từ các file con.
   - Dùng **Unpivot Other Columns** nếu file tổ trưởng ghi các mã lỗi dừng máy nằm trải ngang thành nhiều cột (đổi từ dạng ngang sang 2 cột chuẩn: `Ly_Do_Dung` và `So_Phut`).
   - Chuẩn hóa định dạng `Date`, `Decimal Number`, xóa khoảng trắng thừa (`Trim`), gộp bảng tra định mức chuẩn (`Merge Queries` với bảng `Dim_MaCap_BOM`).
5. Bấm **Close & Load To...** → Chọn **Only Create Connection + Add this data to the Data Model** (nén bằng động cơ VertiPaq, xử lý mượt trên 2 triệu dòng mà không đơ Excel!).
6. Hằng sáng chỉ cần bỏ file ca mới vào thư mục và bấm **Refresh All** → Toàn bộ báo cáo OEE, OLE, Pareto và BOM Variance cập nhật xong trong **3 giây**!

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — BÀI TOÁN MẪU PHÂN TÍCH PARETO 80/20 & BOM VARIANCE

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  BẢNG PHÂN TÍCH PARETO 80/20 NGUYÊN NHÂN DỪNG MÁY ĐÙN (THÁNG 10 — TỔNG 1,800 PHÚT)      │
├────┬──────────────────────────────────┬───────────┬────────────┬───────────────────────┤
│ STT│ Nguyên Nhân Dừng Máy Đùn         │ Phút Dừng │ Tỷ Trọng % │ Tích Lũy % (Cum %)    │
├────┼──────────────────────────────────┼───────────┼────────────┼───────────────────────┤
│ 1  │ Đổi màu nhựa & xả nòng (Purging) │  630 phút │   35.0%    │   35.0%  ◄── Ưu tiên 1│
│ 2  │ Thay khuôn Chày-Cối & chỉnh tâm  │  450 phút │   25.0%    │   60.0%  ◄── Ưu tiên 2│
│ 3  │ Thay rulo cấp đồng & hàn nối     │  360 phút │   20.0%    │   80.0%  ◄── Đạt 80%! │
│ 4  │ Báo lỗi thủng Spark Tester       │  180 phút │   10.0%    │   90.0%               │
│ 5  │ Nghẹt lưới lọc & sự cố điện trở  │  108 phút │    6.0%    │   96.0%               │
│ 6  │ Chờ xe nâng / chờ QC duyệt mẫu   │   72 phút │    4.0%    │  100.0%               │
└────┴──────────────────────────────────┴───────────┴────────────┴───────────────────────┘
  → Quy tắc 80/20: Chỉ cần tập trung 1 dự án SMED + Color Sequencing + Dual Pay-off vào
    3 nguyên nhân đầu tiên đã triệt tiêu được 80% tổng thời gian dừng máy của cả xưởng!
```

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — TỰ ĐỘNG HÓA VBA MACRO & KẾT HỢP PYTHON (PANDAS/OPENPYXL)

### Đoạn Mã VBA Macro Tự Động Xuất Báo Cáo Ca PDF & Cảnh Báo OEE Dưới Chuẩn:
Nhấn `Alt + F11` trong Excel → Insert Module → Dán đoạn mã sau:

```vba
Sub ExportDailyProductionReport()
    Dim ws As Worksheet
    Dim savePath As String
    Dim fileName As String

    Set ws = ThisWorkbook.Sheets("BaoCaoCa")
    savePath = ThisWorkbook.Path & "\BaoCaoPDF\"

    If Dir(savePath, vbDirectory) = "" Then
        MkDir savePath
    End If

    fileName = "BaoCao_OE_SanXuat_" & Format(Now, "yyyy-mm-dd_hhnn") & ".pdf"

    ws.ExportAsFixedFormat Type:=xlTypePDF, _
        fileName:=savePath & fileName, _
        Quality:=xlQualityStandard, _
        IncludeDocProperties:=True, _
        IgnorePrintAreas:=False, _
        OpenAfterPublish:=False

    MsgBox "Đã xuất báo cáo sản xuất PDF thành công tại: " & vbCrLf & savePath & fileName, vbInformation, "Chuyên Viên OE"
End Sub
```

### Quy Trình Kết Hợp Python (`pandas` + `openpyxl`) Tăng Tốc Báo Cáo Từ 3 Ngày → 2 Giờ:
- Khi dữ liệu đo kiểm từ phòng Lab/máy đùn xuất ra hàng trăm file `.csv`/`.txt` mỗi tuần, Chuyên viên OE viết script Python đọc toàn bộ thư mục bằng `glob` + `pandas.concat()`, tự động tính `OEE`, `OLE`, `Cpk`, kiểm tra giá trị dị biệt (`Outliers`), tính `BOM Variance` và xuất thẳng ra file Excel định dạng đẹp kèm biểu đồ bằng `openpyxl` — giúp loại bỏ 100% lỗi nhập tay và giải phóng 85% thời gian cho việc xuống hiện trường Genba!
"""
    },

    "powerbi_mfg": {
        "title": "Cẩm Nang Xây Dựng Dashboard Sản Xuất (OEE, OLE, BOM & Phế Phẩm Cáp) Trên Power BI",
        "summary": "Cẩm nang 4 tầng (Basic → Expert): Star Schema nhà máy cáp điện, công thức DAX tính OEE theo mét/phút & hao phí đồng/nhựa, Pareto DAX động, thiết kế 3 tầng Dashboard và Scheduled Refresh Gateway.",
        "category": "Phần Mềm & Công Cụ",
        "content": r"""# 📈 CẨM NANG XÂY DỰNG DASHBOARD OEE/OLE & BOM TRÊN MICROSOFT POWER BI
*(Kiến Trúc Dữ Liệu Sản Xuất Chuẩn Công Nghiệp Từ Cơ Bản Đến Chuyên Gia)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — MÔ HÌNH DỮ LIỆU STAR SCHEMA NHÀ MÁY SẢN XUẤT

Không bao giờ dồn tất cả 40 cột vào 1 bảng phẳng duy nhất trên Power BI (gây chậm, sai công thức khi ghép Downtime và Production). Luôn tách theo **Mô hình Hình Sao (Star Schema)**:

```text
┌────────────────────────────────────────────────────────────────────────┐
│  KIẾN TRÚC STAR SCHEMA CHO DASHBOARD NHÀ MÁY DÂY CÁP ĐIỆN              │
└────────────────────────────────────────────────────────────────────────┘

                  [Dim_Date (Lịch/Ca)]       [Dim_Machines (Kéo/Bện/Đùn)]
                           │                             │
                           ▼ (1-to-Many)                 ▼ (1-to-Many)
  [Dim_CableSKU] ──> [Fact_Production_Log]        [Fact_Downtime_Log]
  (Tốc độ chuẩn,      • Ngay, Ca, MaMay            • Ngay, Ca, MaMay
   Định mức Đồng/     • MaCap, Met_Dat             • MaLoiDung, PhutDung
   Nhựa BOM)          • Met_Phe, PlannedMin        • Nhom_6_TonThat
                      • Dong_Thuc_kg, Nhua_Thuc_kg
```

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — BỘ CÔNG THỨC DAX CHUẨN TÍNH OEE CƠ KHÍ & CÁP ĐIỆN

### Tính Availability (Độ Khả Dụng):
```dax
Availability_Rate =
VAR PlannedTime = SUM(Fact_Production[PlannedMinutes])
VAR ActualDowntime = SUM(Fact_Downtime[DowntimeMinutes])
VAR OperatingTime = MAX(PlannedTime - ActualDowntime, 0)
RETURN
DIVIDE(OperatingTime, PlannedTime, 0)
```

### Tính Performance Cho Nhà Máy Cơ Khí (Theo Chu Kỳ Giây/Sản Phẩm):
```dax
Performance_Rate =
VAR OperatingTimeSeconds = (SUM(Fact_Production[PlannedMinutes]) - SUM(Fact_Downtime[DowntimeMinutes])) * 60
VAR IdealProducedSeconds = SUMX(Fact_Production, Fact_Production[TotalCount] * RELATED(Dim_Products[IdealCycleTimeSeconds]))
RETURN
DIVIDE(IdealProducedSeconds, OperatingTimeSeconds, 0)
```

### Tính Performance Đặc Thù Ngành Dây Cáp Điện (Theo Tốc Độ Mét/Phút):
```dax
Performance_Cable_Rate =
VAR ActualOperatingMin = SUM(Fact_Production[PlannedMinutes]) - SUM(Fact_Downtime[DowntimeMinutes])
VAR IdealOperatingMin =
    SUMX(
        Fact_Production,
        DIVIDE(
            Fact_Production[TotalMeters],
            RELATED(Dim_CableSKU[IdealSpeed_MetersPerMin]),
            0
        )
    )
RETURN
DIVIDE(IdealOperatingMin, ActualOperatingMin, 0)
```

### Tính Quality & OEE Tổng Thể:
```dax
Quality_Rate =
DIVIDE(SUM(Fact_Production[GoodMeters]), SUM(Fact_Production[TotalMeters]), 0)

OEE_Score = [Availability_Rate] * [Performance_Cable_Rate] * [Quality_Rate]
```

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — DAX ĐO HAO PHÍ BOM ĐỒNG/NHỰA & BIỂU ĐỒ PARETO ĐỘNG

### Tính Tỷ Lệ Chênh Lệch Định Mức Đồng (Copper Variance %) & Thiệt Hại Bằng Tiền:
```dax
Copper_Standard_Kg =
SUMX(
    Fact_Production,
    (Fact_Production[GoodMeters] / 1000) * RELATED(Dim_CableSKU[BOM_Copper_KgPerKm])
)

Copper_Variance_Kg = SUM(Fact_Production[Actual_Copper_Kg]) - [Copper_Standard_Kg]

Copper_Variance_Pct = DIVIDE([Copper_Variance_Kg], [Copper_Standard_Kg], 0)

Scrap_Financial_Loss_VND =
    SUM(Fact_Production[BareCopperScrap_Kg]) * 15000 +
    SUM(Fact_Production[InsulatedCopperScrap_Kg]) * 52000 +
    SUM(Fact_Production[PVC_Purge_Scrap_Kg]) * 28000
```

### Công Thức DAX Tính Đường Tích Lũy Pareto 80/20 Động Cho Nguyên Nhân Dừng Máy:
```dax
Downtime_Cum_Pct =
VAR CurrentLoss = [Total_Downtime_Min]
VAR AllLoss = CALCULATE([Total_Downtime_Min], ALLSELECTED(Dim_DowntimeReason))
VAR CumLoss =
    CALCULATE(
        [Total_Downtime_Min],
        FILTER(
            ALLSELECTED(Dim_DowntimeReason),
            [Total_Downtime_Min] >= CurrentLoss
        )
    )
RETURN
DIVIDE(CumLoss, AllLoss, 0)
```

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — THIẾT KẾ DASHBOARD 3 TẦNG & TRIỂN KHAI VẬN HÀNH TỰ ĐỘNG

1. **Thiết Kế Đúng Đối Tượng Xem (Không Nhồi 20 Biểu Đồ Lên 1 Trang):**
   - *Trang 1 (Executive View — Giám đốc Nhà máy):* 5 KPI Card lớn (OEE tổng, OLE tổng, Tấn đồng xuất xưởng, Tỷ lệ phế liệu %, Tiền chênh lệch BOM), biểu đồ xu hướng 12 tháng, xếp hạng hiệu quả các phân xưởng (Kéo / Bện / Đùn / Đóng gói).
   - *Trang 2 (Operational Deep-Dive — Quản đốc & Chuyên viên OE):* Biểu đồ Pareto nguyên nhân dừng máy, Ma trận nhiệt (Heatmap) OEE theo Ca 1/Ca 2/Ca 3 × Ngày trong tuần, Drill-through xuống từng mã dây cáp bị lỗi nhiều nhất.
   - *Trang 3 (Before–After Kaizen Tracker):* Biểu đồ cột kiểm soát so sánh trực tiếp thời gian đổi mã SMED và tỷ lệ phế phẩm trước/sau cải tiến kèm tổng giá trị tiết kiệm ROI lũy kế.
2. **Tự Động Cập Nhật (Scheduled Refresh & On-Premises Data Gateway):**
   - Cài đặt *On-Premises Data Gateway* trên máy chủ nội bộ nhà máy để Power BI tự động lấy dữ liệu từ SQL Server/ERP/Thư mục Excel lúc 07:00 sáng và 19:00 tối mỗi ngày (kết hợp phân quyền *Row-Level Security - RLS* để Quản đốc xưởng nào chỉ xem chi tiết tổ mình phụ trách).
"""
    },

    "minitab_spc": {
        "title": "Cẩm Nang Minitab — Kiểm Soát Quá Trình Thống Kê (SPC) & Năng Lực Quá Trình (Cpk)",
        "summary": "Cẩm nang SPC toàn diện từ Basic đến Expert: Xbar-R / I-MR, Case Study tiện trục 25mm tính Cp/Cpk/Ppk, 4 quy tắc Nelson Rules và quy trình đánh giá Gage R&R.",
        "category": "Phần Mềm & Công Cụ",
        "content": """# 🎯 CẨM NANG MINITAB & KIỂM SOÁT THỐNG KÊ QUÁ TRÌNH (SPC)
*(Làm Chủ Quá Trình Thống Kê, Năng Lực Cpk & Hệ Thống Đo Lường Từ Cơ Bản Đến Chuyên Gia)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — Ý NGHĨA SPC & PHÂN LOẠI BIẾN THIÊN
SPC (Statistical Process Control) là phương pháp ứng dụng toán học thống kê để theo dõi, kiểm soát và cải tiến quy trình sản xuất nhằm ngăn ngừa phế phẩm phát sinh ngay từ nguồn:

```text
┌────────────────────────────────────────────────────────────────────────┐
│  PHÂN BIỆT 2 DẠNG BIẾN THIÊN TRONG QUÁ TRÌNH GIA CÔNG                  │
├─────────────────────┬──────────────────────────────────────────────────┤
│ Sai Số Ngẫu Nhiên   │ Dao động tự nhiên của hệ thống (nhiệt độ môi     │
│ (Common Causes)     │ trường, độ rung máy nhẹ). Ổn định & dự báo được  │
├─────────────────────┼──────────────────────────────────────────────────┤
│ Sai Số Đặc Biệt     │ Sự cố bất thường ngoài dự kiến (gãy mũi dao, mẻ  │
│ (Special Causes)    │ dao, nhầm phôi, công nhân chưa qua đào tạo).     │
└─────────────────────┴──────────────────────────────────────────────────┘
```

> [!CAUTION]
> **Quy luật chiếc Phễu Deming (Tampering):** Khi quy trình chỉ có sai số ngẫu nhiên, nếu người kỹ sư can thiệp thái quá (thấy 1 chi tiết hơi to là vặn ốc sang trái, chi tiết sau hơi nhỏ lại vặn ốc sang phải), hành động này sẽ **làm tăng gấp đôi biến động của hệ thống** và biến một máy móc đang chạy ổn định thành một đống phế phẩm hỗn loạn!

### Lựa Chọn Biểu Đồ Kiểm Soát Phù Hợp:
- **Dữ liệu biến lượng đo lường liên tục (Continuous Data):**
  * Nhóm con n = 2 - 9 (lấy mẫu 5 chi tiết/giờ) → Dùng **Biểu đồ Xbar-R (Trung bình & Khoảng biến thiên)**.
  * Mẫu đơn chiếc n = 1 (đo nhiệt độ lò, thời gian sấy mỗi mẻ) → Dùng **Biểu đồ I-MR (Individual & Moving Range)**.
- **Dữ liệu đếm thuộc tính khuyết tật (Attribute Data):**
  * Tỷ lệ sản phẩm phế phẩm (%) → Dùng **Biểu đồ p-chart**.
  * Đếm tổng số lỗi khuyết tật trên một sản phẩm → Dùng **Biểu đồ u-chart**.

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — CÔNG THỨC TÍNH NĂNG LỰC QUY TRÌNH (Cp & Cpk)

```text
┌────────────────────────────────────────────────────────────────────────┐
│  CÔNG THỨC TÍNH NĂNG LỰC QUY TRÌNH (PROCESS CAPABILITY)                │
└────────────────────────────────────────────────────────────────────────┘

1. Chỉ số Cp (Năng lực tiềm năng - Bề rộng phân tán, chưa xét lệch tâm):
            USL - LSL
     Cp  =  ─────────
               6σ

2. Chỉ số Cpk (Năng lực thực tế - Có tính đến độ lệch tâm so với danh định):
     Cpk =  min [ (USL - μ) / (3σ) ,  (μ - LSL) / (3σ) ]

     Trong đó:
     • USL: Giới hạn dung sai trên (Upper Specification Limit)
     • LSL: Giới hạn dung sai dưới (Lower Specification Limit)
     • μ  : Giá trị trung bình của quá trình sản xuất (Process Mean)
     • σ  : Độ lệch chuẩn ước lượng nội bộ (Within-subgroup Standard Deviation)

3. Tiêu Chuẩn Xếp Hạng Cpk Quốc Tế:
   • Cpk < 1.00        : KHÔNG ĐẠT → Sinh ra phế phẩm (> 2,700 PPM), bắt buộc dừng máy.
   • 1.00 ≤ Cpk < 1.33 : Tạm chấp nhận, rủi ro cao, phải theo dõi chặt chẽ.
   • Cpk ≥ 1.33        : ĐẠT CHUẨN CÔNG NGHIỆP (4 Sigma) → Tỷ lệ lỗi < 63 PPM (phần triệu).
   • Cpk ≥ 1.67        : ĐẲNG CẤP THẾ GIỚI (World-Class / Six Sigma) → Tỷ lệ lỗi < 0.6 PPM.
```

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — BÀI TOÁN THỰC TẾ TIỆN TRỤC CƠ KHÍ (CASE STUDY)

**Bối cảnh tại xưởng tiện CNC:**
Gia công trục thép đường kính danh định Ø 25.0 mm với dung sai cho phép: 25.0 ± 0.1 mm.
- **USL (Cận trên)** = 25.0 + 0.1 = 25.10 mm.
- **LSL (Cận dưới)** = 25.0 - 0.1 = 24.90 mm.
- Khoảng dung sai cho phép T = USL - LSL = 0.20 mm.

**Kết quả đo đạc 100 sản phẩm liên tiếp đưa vào Minitab:**
- Giá trị trung bình của mẫu đo: μ = 25.04 mm *(Bị lệch tâm dương 0.04 mm)*.
- Độ lệch chuẩn nội bộ ước lượng: σ = 0.025 mm.

```text
┌────────────────────────────────────────────────────────────────────────┐
│  BÀI TOÁN TÍNH TOÁN CP & CPK TRỤC TIỆN (CASE STUDY)                    │
└────────────────────────────────────────────────────────────────────────┘

1. Tính Năng Lực Tiềm Năng Cp:
            USL - LSL          25.10 - 24.90           0.20
     Cp  =  ─────────   =   ──────────────────   =   ────────  =  1.333
               6σ           6  ×  0.025               0.150

2. Tính Năng Lực Thực Tế Cpk:
     • Phía dung sai trên:
       CPU = (USL - μ) / (3σ) = (25.10 - 25.04) / (3 × 0.025) = 0.060 / 0.075 = 0.800

     • Phía dung sai dưới:
       CPL = (μ - LSL) / (3σ) = (25.04 - 24.90) / (3 × 0.025) = 0.140 / 0.075 = 1.867

     • Giá trị Cpk thực tế:
       Cpk = min(CPU, CPL) = min(0.800, 1.867) = 0.800
```

**Nhận xét chuyên gia & Hành động giải cứu:**
- **Nghịch lý rõ rệt:** `Cp = 1.33` chứng tỏ độ biến động của máy cực kỳ hẹp và ổn định (đủ năng lực 4 Sigma). Tuy nhiên `Cpk = 0.80` (< 1.0) lại là mức báo động đỏ sinh ra phế phẩm hàng loạt!
- **Nguyên nhân cốt lõi:** Phân phối kích thước bị **Lệch Tâm 0.04 mm về phía USL** (tiệm cận sát vách dung sai trên), làm chi tiết bị tiện quá to.
- **Hành động kỹ thuật cực kỳ đơn giản mà không tốn tiền:**
  * Kỹ sư chỉ cần vào màn hình điều khiển máy tiện CNC, nhập bù trừ gốc tọa độ (Tool Offset adjustment): lùi mũi dao Z/X lại đúng **0.04 mm**.
  * Sau khi dịch tâm μ từ 25.04 mm về đúng 25.00 mm:
```text
                  25.10 - 25.00         0.100
    Cpk mới  =  ─────────────────  =  ─────────  =  1.333
                  3 × 0.025             0.075
```
  * Ngay lập tức quy trình đạt chuẩn công nghiệp `Cpk = 1.33` mà không tốn bất kỳ chi phí bảo trì nào!

---

### 📌 CASE STUDY 2 (NGÀNH DÂY CÁP ĐIỆN CADIVI): KIỂM SOÁT ĐƯỜNG KÍNH BỌC CÁCH ĐIỆN LASER GAUGE & KIỂM ĐỊNH 2-SAMPLE T-TEST TRƯỚC–SAU

**Bối cảnh tại dây chuyền đùn dây dân dụng VC 2.5 mm²:**
- Đường kính ruột đồng chuẩn: Ø 1.78 mm. Chiều dày cách điện danh định theo TCVN 6610-3: **0.80 mm** (Chiều dày điểm mỏng nhất cho phép ≥ 0.62 mm → Đường kính ngoài tối thiểu an toàn `LSL = 3.28 mm`, trần kinh tế `USL = 3.52 mm`, mục tiêu danh định `Target = 3.38 mm`).
- **Trước cải tiến (Chỉnh tốc độ bằng tay):** Độ lệch chuẩn `σ = 0.055 mm`. Để không bao giờ bị rớt chuẩn dưới 3.28 mm, công nhân phải chỉnh tâm chạy lên tận `μ = 3.46 mm` (dư +0.08 mm đường kính = **lãng phí ~11.5% nhựa PVC!**).
- **Sau cải tiến (Gắn vòng hồi tiếp kín Laser Gauge → điều khiển tốc độ Capstan tự động):** Độ lệch chuẩn thu hẹp từ `σ = 0.055 mm` xuống còn `σ = 0.020 mm`!
- Chuyên viên OE tự tin hạ đường kính mục tiêu `μ` từ `3.46 mm` về `3.36 mm`:
  * Kiểm tra biên dưới an toàn: `CPL = (3.36 - 3.28) / (3 × 0.020) = 0.08 / 0.06 = 1.33` (Đạt chuẩn 4 Sigma, < 63 PPM!).
  * Chạy **2-Sample t-test** trong Minitab (`Stat → Basic Statistics → 2-Sample t`) trên 100 mẫu trước & sau → `p-value = 0.000 (< 0.05)` → Khẳng định khoa học cải tiến giảm **0.10 mm đường kính ngoài**, tiết kiệm ngay **~1.1 tấn nhựa PVC / tháng / 1 dây chuyền** mà 100% dây vẫn đạt chuẩn TCVN!

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — 4 QUY TẮC NELSON RULES & ĐÁNH GIÁ HỆ THỐNG ĐO GAGE R&R

### 4 Quy Tắc Nhận Diện Lỗi Sớm Trên Biểu Đồ Xbar-R (Nelson Rules):
1. **Rule 1:** Có 1 điểm duy nhất nằm vượt ra ngoài giới hạn kiểm soát 3-Sigma (UCL hoặc LCL). → *Biến động cực đoan, dừng chuyền kiểm tra ngay*.
2. **Rule 2:** Có 9 điểm liên tiếp cùng nằm về một phía của đường tâm trung bình (Center Line). → *Quy trình bị lệch tâm (mòn dao, nhiệt độ tăng)*.
3. **Rule 3:** Có 6 điểm liên tiếp tăng dần đều hoặc giảm dần đều. → *Xu hướng trôi dạt (Drift trend)*.
4. **Rule 4:** Có 14 điểm liên tiếp dao động lên xuống xen kẽ (hình răng cưa). → *Dữ liệu bị lấy lẫn lộn từ 2 nguồn máy hoặc 2 công nhân khác nhau*.

### Phân Tích Hệ Thống Đo Lường (Gage R&R - MSA):
Trước khi tin tưởng vào số liệu SPC, hệ thống đo lường bắt buộc phải được chứng nhận:
- Thực hiện thí nghiệm: **10 mẫu chi tiết × 3 người đo × 3 lần lặp lại**.
- **Tiêu chuẩn %GRR (Gage Repeatability & Reproducibility):**
  * %GRR < 10%: Hệ thống đo lường xuất sắc.
  * 10% ≤ %GRR ≤ 30%: Tạm chấp nhận tùy mức độ quan trọng.
  * %GRR > 30%: **HỆ THỐNG ĐO LƯỜNG HỎNG**, số liệu vô giá trị!
- Nếu Repeatability cao → Thay thiết bị đo mới hoặc hiệu chuẩn.
- Nếu Reproducibility cao → Do người đo thao tác khác nhau, cần chuẩn hóa tư thế cầm thước và lực siết.
"""
    },

    "autocad_layout": {
        "title": "Cẩm Nang Thiết Kế Mặt Bằng Xưởng Tinh Gọn (Plant Layout), SLP & Sơ Đồ Spaghetti (Ngành Cáp Điện)",
        "summary": "Cẩm nang 4 tầng (Basic → Expert): 3 mô hình Layout, phương pháp SLP (REL Chart & From-To Matrix), đặc thù bố trí phân xưởng Kéo–Bện–Đùn–Cầu trục nhà máy cáp CADIVI và Case Study Spaghetti Diagram.",
        "category": "Phần Mềm & Công Cụ",
        "content": r"""# 📐 CẨM NANG THIẾT KẾ MẶT BẰNG XƯỞNG TINH GỌN (PLANT LAYOUT) & SPAGHETTI
*(Từ Cơ Bản Đến Chuyên Gia — Đặc Thù Bố Trí Nhà Máy Dây Cáp Điện & Lắp Ráp)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — 3 MÔ HÌNH BỐ TRÍ MẶT BẰNG & CHUYỀN CHỮ U

```text
┌─────────────────────┬────────────────────────────────────────────────────────────┐
│ Mô Hình Layout      │ Đặc Điểm & Ứng Dụng Thực Tế Trong Nhà Máy                  │
├─────────────────────┼────────────────────────────────────────────────────────────┤
│ 1. Process Layout   │ Gom máy cùng chức năng vào 1 khu (Khu Kéo riêng, Khu Bện   │
│    (Theo công nghệ) │ riêng, Khu Đùn riêng). Linh hoạt cho đa mã cáp lực nhưng   │
│                     │ dễ phát sinh tồn kho rulo WIP lớn và vận chuyển xa.        │
├─────────────────────┼────────────────────────────────────────────────────────────┤
│ 2. Product/Cellular │ Bố trí liên hoàn theo nhóm họ sản phẩm (vd: chuyền chuyên  │
│    (Theo sản phẩm)  │ dây dân dụng VC từ Kéo tinh → Đùn nhanh → Coiler tự động). │
│    Chuyền Chữ U     │ Giảm 70% quãng đường đi lại, linh hoạt Shojinka nhân lực.  │
├─────────────────────┼────────────────────────────────────────────────────────────┤
│ 3. Fixed-Position   │ Sản phẩm cố định 1 chỗ vì quá nặng/lớn (đóng tàu, máy bay).│
└─────────────────────┴────────────────────────────────────────────────────────────┘
```

### Ưu Thế Của Chuyền Chữ U (U-Shaped Cell) Cho Khâu Đóng Gói / Lắp Ráp:
1. **Điểm đầu và điểm cuối sát nhau:** 1 công nhân có thể nạp đầu vào và lấy thành phẩm cùng 1 vị trí → Giảm 70% quãng đường đi bộ.
2. **Linh hoạt nhân lực (Shojinka):** Khi đơn hàng ít, 1 công nhân đứng giữa chữ U vận hành 2–3 trạm; khi cao điểm, tăng lên 3–4 công nhân mà không cần dời máy.
3. **Luồng 1 sản phẩm (One-Piece Flow):** Triệt tiêu chất đống bán thành phẩm WIP giữa các công đoạn.

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — PHƯƠNG PHÁP SLP (SYSTEMATIC LAYOUT PLANNING) & SPAGHETTI

### Phương Pháp Hoạch Định Mặt Bằng Hệ Thống SLP (Richard Muther):
1. **Phân tích P-Q (Product – Quantity):** Vẽ biểu đồ Pareto sản lượng theo mã sản phẩm để quyết định khu nào bố trí *Product Flow* (dây dân dụng chạy liên tục) và khu nào bố trí *Process Flow* (cáp lực đặc thù).
2. **Ma trận Từ–Đến (From-To Chart):** Thống kê tổng số chuyến xe nâng/cầu trục chở rulo giữa từng cặp phân xưởng mỗi ngày (ví dụ: Kéo → Bện 45 chuyến/ngày; Bện → Đùn 60 chuyến/ngày).
3. **Biểu đồ Quan hệ (REL Chart — A, E, I, O, U, X):**
   - `A` (Absolutely necessary — Bắt buộc sát nhau): Xưởng Đùn ↔ Kho đệm rulo đã bện & Bể xông hơi XLPE.
   - `X` (Undesirable — Bắt buộc cách ly xa): Khu máy trộn/băm nhựa bụi ồn ↔ Phòng Lab QA/QC chính xác cao (đo điện trở/kính hiển vi cần phòng điều hòa ổn định 23°C ± 2°C!).

### Quy Trình Vẽ Sơ Đồ Spaghetti Diagram Bằng AutoCAD:
1. Mở bản vẽ mặt bằng AutoCAD tỷ lệ 1:100, in ra giấy A3.
2. Đi theo công nhân (hoặc xe nâng) suốt 1 ca làm việc, vẽ nét liền theo từng bước di chuyển và đo tổng quãng đường bằng lệnh `PLINE` + `LIST` trên AutoCAD.
3. Đưa dụng cụ, tem nhãn, rulo phụ về **Point-of-Use Storage** (trong bán kính 1 sải tay) → Vẽ lại sơ đồ sau cải tiến để chứng minh ROI giảm 40–65% quãng đường di chuyển.

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — CASE STUDY TỐI ƯU LAYOUT KHU ĐÓNG CUỘN KHOANH DÂY DÂN DỤNG

- **Hiện trạng đo bằng Spaghetti Diagram:** 1 công nhân đóng cuộn khoanh 100m phải di chuyển trung bình **5.8 km / ca** (đi lấy màng co 12m, đi lấy thùng carton 18m, đẩy xe cuộn sang khu cân QC 25m).
- **Cải tiến Layout (Chi phí < 15 triệu VNĐ):** Xoay máy cuộn và máy co nhiệt thành góc chữ L/U, đặt kệ trượt trọng lực (Flow Rack) cấp sẵn thùng carton + tem nhãn ngay phía sau lưng, đặt cân kiểm tra tích hợp băng tải con lăn nối thẳng ra pallet xuất hàng.
- **Kết quả sau cải tiến:** Quãng đường đi bộ giảm từ **5.8 km → 1.9 km / ca (giảm 67.2%)**, sản lượng tổ đóng gói tăng **+22%**, công nhân hết đau mỏi lưng cuối ca.

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — NGUYÊN TẮC ĐẶC THÙ LAYOUT NHÀ MÁY DÂY CÁP ĐIỆN (CADIVI)

1. **Tôn trọng hình học dây chuyền dài liên hoàn:** Dây chuyền Kéo thô RBD dài 20–30m, dây chuyền Đùn bọc cáp dài 35–60m (Pay-off → Extruder → Máng nước làm mát dài 15–25m → Capstan → Take-up) bắt buộc bố trí **thẳng hàng song song** dọc theo nhịp cột nhà xưởng để không bị gãy góc uốn cáp.
2. **Đồng bộ Hành lang Cầu Trục (Overhead Crane) 2–5 tấn:** Khu máy kéo thô, bện lồng cứng và đùn cáp lực tiết diện lớn tới 300 mm² có rulo thép nặng 1–5 tấn → Bắt buộc bố trí nằm trọn trong vùng phủ móc cầu trục; rãnh cáp ngầm/đường ống nước giải nhiệt phải đi chìm an toàn.
3. **Khu Đệm Siêu Thị Rulo (WIP Supermarket) & An Toàn 5S:** Kẻ vạch sơn rộng ≥ 3.5m cho đường xe nâng rulo, tách biệt hoàn toàn với lối đi bộ xanh có lan can bảo vệ; bố trí tủ hút mùi/khói nhựa cục bộ ngay trên đầu chữ thập máy đùn PVC và tường tiêu âm cho khu máy kéo/bện tốc độ cao (> 85 dB).
"""
    },

    "erp_mes": {
        "title": "Cẩm Nang Tích Hợp Hệ Thống Quản Trị ERP (SAP PP), MES & SCADA/PLC Nhà Máy Thông Minh",
        "summary": "Cẩm nang 4 tầng (Basic → Expert): Kiến trúc phân tầng ISA-95, tích hợp máy đùn/kéo cáp (PLC + Laser Gauge + Spark Tester → MES → ERP), truy xuất nguồn gốc từng rulo bằng Barcode/QR và nguyên tắc Lean-First.",
        "category": "Phần Mềm & Công Cụ",
        "content": r"""# 🏭 CẨM NANG TÍCH HỢP ERP (SAP PP), MES & SCADA/PLC NHÀ MÁY THÔNG MINH
*(Từ Nền Tảng ISA-95 Đến Kiến Trúc Số Hóa Thực Chiến Nhà Máy Dây Cáp Điện)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — KIẾN TRÚC PHÂN TẦNG KIM TỰ THÁP ISA-95

```text
┌────────────────────────────────────────────────────────────────────────┐
│  KIM TỰ THÁP TỰ ĐỘNG HÓA NHÀ MÁY CHUẨN QUỐC TẾ ISA-95                  │
└────────────────────────────────────────────────────────────────────────┘

  [Tầng 4: ERP — SAP S/4HANA / Oracle / Bravo]   ◄── Chu kỳ: Ngày / Tuần / Tháng
    • Đơn hàng bán, Mua đồng/nhựa, Kế hoạch MRP, Định mức BOM, Giá thành COGS
                           ▲  │  (Lệnh SX Production Order ↓  |  ↑ Xác nhận sản lượng)
                           │  ▼
  [Tầng 3: MES — Manufacturing Execution System]  ◄── Chu kỳ: Phút / Giờ / Ca
    • Điều độ từng máy, OEE/OLE thời gian thực, Truy xuất phả hệ rulo (Traceability)
    • Quản lý mã dừng máy (Downtime Codes), Kiểm soát phế phẩm & QC In-line
                           ▲  │  (Nạp Recipe ↓  |  ↑ Xung mét dây, trạng thái máy)
                           │  ▼
  [Tầng 2: SCADA / HMI — Giám Sát Dây Chuyền]     ◄── Chu kỳ: Giây
    • Màn hình điều khiển nhiệt độ vùng đùn, tốc độ Capstan, cảnh báo Andon
                           ▲  │
                           │  ▼
  [Tầng 1 & 0: PLC & Cảm Biến Hiện Trường]        ◄── Chu kỳ: Mili-giây
    • Encoder đếm mét dây, Laser Diameter Gauge, Spark Tester, Cảm biến đứt sợi
```

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — LUỒNG DỮ LIỆU KHÉP KÍN TRONG NHÀ MÁY DÂY CÁP ĐIỆN

1. **Bước 1 — Phát hành lệnh (ERP → MES):** ERP đẩy Lệnh Sản Xuất (Work Order) kèm mã cáp (vd: `CXV 3x50+1x25`), chiều dài yêu cầu `2,000m`, định mức BOM đồng/nhựa và trình tự công đoạn (Routing) xuống MES.
2. **Bước 2 — Quét nhận việc & xác thực vật tư tại máy (Poka-Yoke):** Công nhân quét thẻ nhân viên RFID + quét mã vạch **Barcode/QR dán trên rulo đồng đầu vào** và bao hạt nhựa. MES tự kiểm tra đúng mã BOM mới mở khóa cho máy chạy.
3. **Bước 3 — Thu thập tự động (PLC → MES):**
   - Bộ đếm chiều dài (Length Encoder) tự động đẩy số mét chạy thực tế vào MES (chấm dứt ghi sổ tay).
   - Thiết bị **Laser Diameter Gauge** gửi đường kính trung bình & độ lệch tâm liên tục để vẽ SPC.
   - Thiết bị **Spark Tester** ghi nhận chính xác tọa độ mét bị lỗi đánh thủng.
   - Khi máy dừng > 2 phút, màn hình HMI cạnh máy bật bảng chọn nhanh mã lý do dừng (Đổi màu / Thay rulo / Đứt sợi / Sửa máy).
4. **Bước 4 — Chốt ca & Hạch toán ngược (MES → ERP):** Cuối ca, MES tự động đồng bộ chiều dài đạt chuẩn, cân nặng phế liệu đồng trần/đồng dính nhựa và số giờ công về ERP để kế toán tính giá thành thực tế và BOM Variance ngay ngày hôm sau.

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — TRUY XUẤT PHẢ HỆ RULO (LOT GENEALOGY / TRACEABILITY)

Khi một công trình điện lực phản hồi 1 cuộn cáp bị sự cố cách điện, hệ thống Barcode/QR trên MES cho phép Chuyên viên OE & QA **truy ngược trong 30 giây**:
`Số Serial Rulo Thành Phẩm` → Chạy trên `Máy Đùn số 3, Ca 2 ngày 15/10, Thợ vận hành Nguyễn Văn B` → Dùng `Lô hạt nhựa XLPE #XL-2026-089` + `Rulo ruột bện #B-4412` → Bện trên `Máy Rigid #2` → Kéo từ `Cuộn Đồng Rod nhà cung ứng X, Lô #CU-991`!
→ Giúp khoanh vùng thu hồi chính xác 1 lô lỗi thay vì phải dừng kiểm tra cả kho hàng hàng trăm tấn!

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — QUY TẮC "LEAN-FIRST" & XỬ LÝ LỆCH PHA DỮ LIỆU

1. **Nguyên tắc vàng: "Chuẩn hóa Lean trước, Số hóa sau":** Nếu mã lỗi dừng máy không thống nhất, BOM còn sai hệ số xoắn, rulo không đánh mã số rõ ràng → Đưa MES đắt tiền vào chỉ tạo ra *"rác tốc độ cao"*.
2. **Chiến lược chuyển đổi số từng bước (Low-Cost Digitalization — Phù hợp lộ trình OE CADIVI):**
   - *Giai đoạn 1 (0–3 tháng, chi phí ≈ 0):* Chuẩn hóa mẫu nhập liệu Excel/Barcode đơn giản tại máy (tương tự cải tiến công đoạn RE7), tự động gom bằng Power Query/Python để có dữ liệu sạch.
   - *Giai đoạn 2 (3–9 tháng):* Gắn bộ Edge IoT/PLC giá rẻ đọc tín hiệu Chạy/Dừng & bộ đếm mét đẩy lên Dashboard Power BI/TV Andon xưởng.
   - *Giai đoạn 3 (9–18 tháng):* Tích hợp đồng bộ 2 chiều đầy đủ giữa MES và ERP toàn nhà máy.
3. **Kiểm soát chênh lệch dữ liệu sổ tay vs PLC:** Luôn hiệu chuẩn định kỳ cảm biến/bánh xe đo mét (tránh trượt bánh xe làm sai số mét 1–2%), kết hợp đối chiếu chéo khối lượng cân thực tế cuộn cáp để ngăn chặn triệt để gian lận báo cáo ca.
"""
    },

    "cable_mfg_machines": {
        "title": "Bách Khoa Quy Trình Công Nghệ & Hệ Thống 9 Nhóm Máy Móc Nhà Máy Dây Cáp Điện (CADIVI)",
        "summary": "Cẩm nang 4 tầng (Basic → Expert) độc quyền cho OE CADIVI Miền Trung: Quy trình 7 công đoạn khép kín, chi tiết 9 nhóm máy móc (Kéo RBD/Tinh, Lò ủ, Bện Buncher/Rigid, Đùn PVC/XLPE + Spark/Laser, Lưu hóa CCV/Sauna, Ghép lõi & Giáp DSTA, Đóng cuộn, Lab IEC & Phụ trợ), thông số vận hành, lỗi đặc thù và điểm đánh OE.",
        "category": "Sản Xuất (Manufacturing)",
        "content": r"""# 🔌 BÁCH KHOA QUY TRÌNH CÔNG NGHỆ & HỆ THỐNG 9 NHÓM MÁY MÓC NHÀ MÁY DÂY CÁP ĐIỆN (CADIVI)
*(Tài Liệu Thực Chiến Từ Cơ Bản Đến Chuyên Gia Dành Riêng Cho Vị Trí Chuyên Viên OE — Nhà Máy CADIVI Miền Trung)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — BỨC TRANH TOÀN CẢNH NHÀ MÁY CADIVI MIỀN TRUNG & CHUỖI 7 CÔNG ĐOẠN

**Thông Tin Cốt Lõi Về Nhà Máy CADIVI Miền Trung:**
- **Địa điểm:** Đường số 2, Khu công nghiệp Hòa Cầm, Quận Cẩm Lệ, TP. Đà Nẵng.
- **Sản phẩm chủ lực:** Dây điện dân dụng (VC, VCm, VCmd, VCmt), dây và cáp điện lực hạ thế (CV, CVV, CXV, AV, AVV, AXV), cáp trung thế treo, dây đồng trần, dây nhôm trần, cáp điện kế, cáp chậm cháy/không khói halogen (FR / LSHF-LSZH) — tiết diện ruột dẫn từ `0.5 mm²` lên đến `300 mm²` (và lớn hơn).
- **Thiết bị & Tiêu chuẩn:** Dây chuyền hiện đại nhập khẩu từ Đức (Niehoff, Troester, Sikora...), Nhật Bản, Đài Loan, Châu Âu; sản phẩm tuân thủ chuẩn quốc gia **TCVN** và quốc tế **IEC 60228, IEC 60502, IEC 60332, ASTM, JIS, UL**.

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  SƠ ĐỒ DÒNG CHẢY CÔNG NGHỆ KHÉP KÍN SẢN XUẤT DÂY & CÁP ĐIỆN (7 CÔNG ĐOẠN)              │
└────────────────────────────────────────────────────────────────────────────────────────┘

  [1. NVL ĐẦU VÀO]      Đồng Rod Ø 8.0mm (Cu ≥ 99.99%), Nhôm Rod Ø 9.5mm, Hạt nhựa PVC/XLPE/LSZH
         │
         ▼
  [2. KÉO SỢI]          Kéo Thô (RBD) → Kéo Trung (Intermediate) → Kéo Tinh / Nhiều sợi (Multi-wire)
         │              (Giảm đường kính sợi qua dãy khuôn PCD / Hợp kim + Nhũ tương làm mát)
         ▼
  [3. Ủ MỀM]            Ủ liên tục (In-line Annealer) HOẶC Lò ủ chuông khí bảo vệ (Batch Furnace)
         │              (Phục hồi độ dẻo 20-30%, độ dẫn điện IACS ≥ 100%, chống oxy hóa đen)
         ▼
  [4. BỆN RUỘT DẪN]     Bện xoắn đôi (Double Twist Buncher) | Bện lồng cứng (Rigid) / Bện ống (Tubular)
         │              (Tạo ruột dẫn nhiều sợi: 7, 19, 37, 61 sợi; bện tròn nén hoặc bện rẻ quạt)
         ▼
  [5. BỌC CÁCH ĐIỆN]    Dây chuyền Đùn nhựa (Extrusion Line: PVC / XLPE / PE / LSZH)
         │              + Laser Gauge đo đường kính/lệch tâm + Spark Tester cao áp + Lưu hóa XLPE
         ▼
  [6. GHÉP LÕI & VỎ]    Ghép lõi nhiều pha (Drum Twister / Laying-up) → Quấn độn PP/Băng định hình
         │              → Giáp băng thép DSTA / Sợi thép SWA (nếu cáp ngầm) → Đùn bọc vỏ ngoài
         ▼
  [7. THỬ NGHIỆM &      Phòng Lab QA/QC (Điện trở 20°C, Cao áp HV, PD, Kéo đứt, Lão hóa, Chiều dày)
      ĐÓNG GÓI]         → Máy cuộn khoanh 100m + Màng co nhiệt HOẶC Sang rulo gỗ/thép → Xuất kho
```

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — CHI TIẾT 9 NHÓM MÁY MÓC CÓ THỂ CÓ TRONG NHÀ MÁY DÂY CÁP ĐIỆN

### NHÓM 1: MÁY KÉO THÔ (ROD BREAKDOWN MACHINE — RBD)
- **Chức năng:** Kéo thanh đồng rod đầu vào **Ø 8.0 mm** (hoặc nhôm rod **Ø 9.5 mm**) xuống các đường kính trung gian **Ø 1.38 mm – Ø 4.5 mm** (sản lượng lớn, động cơ công suất rất cao 200–500 kW).
- **Cấu tạo chính:** Giàn nhả cuộn đồng rod (Pay-off) + Máy hàn nối đối đầu (Butt Welder) → Hộp khuôn kéo 9–13 cấp (dùng khuôn kim cương nhân tạo **PCD** hoặc hợp kim) ngập trong bể **nhũ tương bôi trơn & làm mát (Drawing Emulsion)** → Bộ ủ điện trở liên tục (**In-line Continuous Annealer** phun hơi nước bảo vệ tránh đen đồng) → Bộ thu dây đôi tự động (**Dual Spooler / Coiler** đổi rulo không dừng máy).
- **Thông số OE trọng yếu:** Tốc độ kéo (15–35 m/s), Tỷ lệ giảm tiết diện mỗi cấp khuôn (Drafting Ratio ~18–26%), Nồng độ & nhiệt độ nhũ tương (35–42°C, pH 7.5–8.5), Dòng điện ủ theo tốc độ.
- **Lỗi & Tổn thất OEE đặc thù:** Đứt sợi (Wire Break — tính KPI: *số lần đứt / tấn đồng*), Mòn khuôn gây **Copper Give-away** (kéo to thừa +0.01mm), Cháy/đen bề mặt đồng do thiếu hơi nước ủ, Bề mặt xước do mạt đồng lẫn trong bể dầu.

### NHÓM 2: MÁY KÉO TRUNG & MÁY KÉO TINH / KÉO NHIỀU SỢI (INTERMEDIATE & MULTI-WIRE FINE DRAWING)
- **Chức năng:** Kéo sợi đồng từ Ø 1.8–2.6 mm xuống các sợi mảnh **Ø 0.15 mm – Ø 1.0 mm** (dùng cho dây mềm nhiều sợi VCm, VCmd, dây điều khiển). Máy kéo nhiều sợi (**Multi-wire Drawing**) có thể kéo đồng thời **8, 16 hoặc 24 sợi** song song trên cùng 1 khung máy!
- **Thông số OE trọng yếu:** Tốc độ 20–35 m/s, đồng đều lực căng giữa các sợi, kiểm soát độ giãn dài đồng nhất giữa sợi số 1 và sợi số 16.
- **Điểm đánh OE:** Tối ưu **Man-Machine Chart** (1 công nhân đứng 2–4 máy), quản lý lịch thay bộ khuôn theo định mức tấn đồng (PM), phân tích kính hiển vi đầu sợi đứt để phân biệt lỗi đồng rod vs lỗi mòn khuôn.

### NHÓM 3: HỆ THỐNG Ủ ĐỒNG (INLINE ANNEALER & LÒ Ủ CHUÔNG — BELL/BATCH ANNEALING FURNACE)
- **Chức năng:** Làm mềm sợi đồng bị cứng giòn do kéo nguội (Work Hardening), phục hồi độ giãn dài đạt 20–30% và đảm bảo điện trở suất đạt chuẩn **IEC 60228** (≥ 100% IACS).
- **2 loại phổ biến:**
  1. *Ủ liên tục trực tuyến (In-line Resistance Annealer):* Gắn liền sau máy kéo, gia nhiệt tức thời bằng dòng điện ngắn mạch chạy qua 2 puli tiếp xúc trong buồng hơi nước → Không tồn kho WIP, Lead Time ngắn.
  2. *Lò ủ chuông chân không / khí bảo vệ N2 (Bell-type / Vacuum Batch Furnace):* Xếp cả chồng rulo vào chuông kín, hút chân không/bơm khí trơ Nitơ nung 250–380°C theo mẻ 6–12 giờ → Cần tối ưu xếp đầy tải mẻ (Full-load utilization) và tránh lỗi dính bết vòng dây (Stickiness) do quá nhiệt.

### NHÓM 4: HỆ THỐNG MÁY BỆN RUỘT DẪN (STRANDING & BUNCHING MACHINES)
- **Chức năng:** Xoắn nhiều sợi đồng/nhôm đơn thành ruột dẫn hoàn chỉnh đạt độ mềm dẻo và tiết diện tiêu chuẩn (`0.5` đến `300 mm²+`).
- **4 dòng máy bện điển hình trong nhà máy cáp:**
  1. **Máy bện xoắn đôi (Double Twist Buncher — Ø 500/630/800mm):** Cánh cung quay tốc độ cao tạo 2 vòng xoắn mỗi vòng quay → Năng suất cực cao cho dây mềm dân dụng nhiều sợi mảnh (VCm, VCmd).
  2. **Máy bện ống (Tubular Strander):** Tốc độ cao cho ruột dẫn 7 sợi hoặc 19 sợi tiết diện nhỏ–trung.
  3. **Máy bện lồng cứng (Rigid Frame Strander — 12+18+24+30 bobbins):** Trụ cột sản xuất cáp lực hạ thế/trung thế **19, 37, 61 sợi** tiết diện lớn tới **300–630 mm²**; trang bị khuôn ép nén (**Compacting Die / Rollers**) tạo **ruột bện tròn ép chặt (Compacted Round)** hoặc **ruột bện rẻ quạt (Sector-shaped)** giúp tiết kiệm 10–15% nhựa cách điện ở khâu sau!
  4. **Máy bện kiểu Skip Strander / Planetary Strander:** Dùng cho cáp đặc biệt cần không xoắn ngược ứng suất sợi.
- **Tổn thất OEE & OE đặc thù:** Thời gian nạp hàng chục rulo (Loading Bobbins — điểm đánh SMED bằng bộ nạp nhanh Side-loader & xe nâng rulo chuyên dụng), Đứt 1 sợi gây dừng cả lồng bện, Sai bước xoắn (Lay Length) gây tăng hao phí đồng (Hệ số xoắn *Lay-up Factor*), và **bài toán Cut-Length** (bện dư mẩu ngắn trên rulo).

### NHÓM 5: DÂY CHUYỀN ĐÙN BỌC CÁCH ĐIỆN & BỌC VỎ (EXTRUSION LINES — PVC / PE / XLPE / LSZH)
Đây là **TRÁI TIM & ĐIỂM NGHẼN QUAN TRỌNG NHẤT** của mọi nhà máy dây cáp điện (dài từ 25m đến 60m)!
- **Cấu trúc 10 cụm thiết bị dọc 1 dây chuyền đùn chuẩn:**
  1. *Cụm nhả ruột dẫn (Pay-off — đơn hoặc kép Dual Pay-off)* + *Bộ tích dây & giữ lực căng (Accumulator / Dancer)*.
  2. *Bộ gia nhiệt trước ruột dẫn (Conductor Pre-heater — cảm ứng/điện trở):* Làm nóng đồng trước khi vào đầu đùn giúp nhựa bám chặt, tránh co ngót tách lớp và giảm ứng suất nhiệt.
  3. *Máy đùn trục vít đơn (Single-Screw Extruder — Ø 50 / 65 / 70 / 90 / 120 / 150 mm):* Phễu cấp & sấy hút ẩm hạt nhựa (*Hopper Dryer*) → Trục vít (*Screw*, tỷ lệ L/D thường 24:1 – 28:1) → Nòng xy-lanh (*Barrel*) chia 4–6 vùng gia nhiệt & quạt làm mát độc lập → Lưới lọc cặn (*Screen Pack / Breaker Plate*).
  4. *Đầu chữ thập (Crosshead) & Bộ Chày–Cối (Tip & Die):* Quyết định hình học lớp cách điện (dạng ép áp lực *Pressure Tooling* hay dạng ống kéo *Tubing Tooling*) và độ đồng tâm.
  5. *Thiết bị đo đường kính Laser & đo độ lệch tâm trực tuyến (Laser Diameter & Eccentricity Gauge — hãng Sikora/Zumbach):* Đo liên tục 1,000 lần/giây, nối vòng kín (**Closed-loop**) tự động chỉnh tốc độ Capstan giữ đường kính chuẩn xác đến `±0.01 mm`!
  6. *Máng làm mát nước nhiều vùng (Multi-stage Cooling Trough):* Nước ấm vùng đầu (tránh sốc nhiệt co rút XLPE/PE) → Nước lạnh tuần hoàn từ Chiller/Tháp giải nhiệt.
  7. *Máy thử cao áp trực tuyến (**Spark Tester** — 3 kV đến 25 kV):* Phát hiện tức thì lỗ mọt khí, dị vật, chỗ nhựa mỏng thủng bằng tia lửa điện cao tần.
  8. *Máy in phun/in lăn thông số (Inkjet / Meter Marking Printer):* In tên hãng CADIVI, quy cách cáp, tiêu chuẩn TCVN, số mét liên tục lên bề mặt vỏ.
  9. *Bộ kéo cáp (Capstan / Caterpillar Haul-off):* Tạo lực kéo ổn định và đo chiều dài bằng Encoder chính xác.
  10. *Cụm thu dây tự động (Dual Automatic Take-up / Portal Take-up):* Tự cắt và sang cuộn sang rulo thứ 2 không dừng máy ở tốc độ 300–800 m/phút (với dây dân dụng)!
- **Thông số vận hành sống còn:** Profile nhiệt độ các vùng đùn (PVC: 140–185°C; XLPE Silane: 160–210°C; LSZH: kiểm soát chặt tránh cháy), Tốc độ trục vít (RPM), Áp suất đầu đùn (Bar), Tốc độ dây (m/phút), Lực căng Pay-off/Take-up, Nhiệt độ nước làm mát (≤ 25°C).
- **Điểm đánh OE lớn nhất:** SMED đổi màu/đổi tiết diện + Color Sequencing + Purging Compound; Triệt tiêu **Over-thickness** (giảm chiều dày nhựa dư 0.05–0.10 mm bằng SPC & Laser Gauge); Giảm **Startup/Tail-end Scrap**; Triệt tiêu lỗi **Spark Fault** và giảm điện năng chờ nhiệt (*Idle Heating*).

### NHÓM 6: HỆ THỐNG KHÂU MẠCH / LƯU HÓA XLPE (CROSS-LINKING SYSTEMS)
- **Mục đích:** Tạo liên kết ngang hóa học 3 chiều cho nhựa PE thành XLPE giúp cáp chịu nhiệt độ vận hành liên tục **90°C** (so với 70°C của PVC) và chịu ngắn mạch tới **250°C**!
- **2 công nghệ chính:**
  1. *Silane XLPE + Bể nước nóng (Hot Water Bath 80–90°C) hoặc Phòng xông hơi (Steam Sauna):* Đùn lõi xong mới đưa rulo vào xông 4–12 giờ → Trọng tâm OE là quản trị WIP rulo chờ xông và xếp đầy tải mẻ tránh nghẽn dòng.
  2. *Dây chuyền lưu hóa liên tục CCV (Catenary Continuous Vulcanization — cho cáp trung thế/cao thế):* Đầu đùn 3 lớp đồng thời (bán dẫn trong – XLPE – bán dẫn ngoài) đi qua ống lưu hóa áp suất khí Nitơ dài 80–120m → Tuyệt đối không được dừng đột xuất (TPM là sống còn!).

### NHÓM 7: MÁY GHÉP LÕI & GIÁP BẢO VỆ (CABLING / LAYING-UP & ARMORING MACHINES)
- **Chức năng:** Chập xoắn 2, 3, 4 lõi pha lại thành lõi cáp hoàn chỉnh (cáp lực `CXV 3x50+1x25`, cáp điều khiển nhiều lõi), chèn dây độn nhựa PP (Filler) để cáp tròn đều, quấn băng định hình (Binder Tape) và bọc giáp bảo vệ cơ học cho cáp ngầm:
  - *Máy ghép lõi (Drum Twister / Planetary Cabler)*: Rulo thu cáp vừa quay trục vừa xoắn tạo bước ghép đều, tốc độ cao.
  - *Đầu giáp băng thép mạ kẽm 2 lớp (DSTA — Double Steel Tape Armoring)* hoặc *Giáp sợi thép (SWA — Steel Wire Armoring)* cho cáp đi ngầm chịu va đập cơ học.
- **Điểm đánh OE:** Đồng bộ chiều dài chính xác 100% giữa 3 lõi pha + 1 lõi trung tính trước khi đưa vào ghép (nếu 1 trong 4 rulo lõi bị ngắn hơn 30m → Cả 3 lõi kia cũng phải cắt bỏ theo 30m = **Thảm họa hao phí gấp 4 lần!**).

### NHÓM 8: MÁY CUỘN KHOANH TỰ ĐỘNG, BỌC MÀNG CO & SANG RULO (COILING, SHRINKING & REWINDING)
- **Chức năng:** Sang dây dân dụng từ rulo lớn thành khoanh tròn chuẩn **100 mét** (`Automatic Coiler`), quấn màng co nhiệt (`Shrink Wrapper`), dán tem chống hàng giả/mã vạch; hoặc sang cáp lực sang rulo gỗ/thép xuất hàng theo chiều dài đặt hàng của công trình (`Drum Rewinder`).
- **Điểm đánh OE:** Đây là khu vực **thâm dụng lao động nhất** trong nhà máy cáp → Mỏ vàng để tối ưu **OLE**, Cân bằng chuyền Yamazumi, Ergonomics bàn thao tác và cắt giảm quãng đường di chuyển bằng Spaghetti Diagram!

### NHÓM 9: PHÒNG LAB THỬ NGHIỆM QA/QC & HỆ THỐNG PHỤ TRỢ (TESTING LAB & UTILITIES)
- **Thiết bị Phòng Thí Nghiệm QA/QC (Liên kết trực tiếp thế mạnh đo kiểm của kỹ sư QC/IE):**
  1. *Cầu đo điện trở chính xác (Kelvin Bridge / Micro-ohmmeter):* Đo điện trở ruột dẫn 1 chiều quy về 20°C kiểm chuẩn **IEC 60228**.
  2. *Máy chiếu quang học / Kính hiển vi đo mặt cắt (Profile Projector / Optical Microscope):* Đo chiều dày cách điện/vỏ trung bình, điểm mỏng nhất và độ lệch tâm (tương đồng hoàn toàn tư duy vận hành **OGP SmartScope / Keyence IM / Canon INEX**!).
  3. *Máy thử cao áp chịu đựng (HV AC/DC Withstand + Bể nước ngâm cáp)* & *Máy đo phóng điện cục bộ (Partial Discharge — PD)* cho cáp trung thế.
  4. *Máy thử kéo nén vạn năng (Universal Tensile Machine)* & *Tủ sấy lão hóa nhiệt (Aging Oven)*: Kiểm tra độ bền kéo đứt (MPa), độ giãn dài (%) và thử biến dạng nhiệt XLPE (**Hot Set Test**).
  5. *Buồng thử cháy lan (Vertical Flame Test IEC 60332)* & *Thử khói/Halogen* cho cáp chống cháy/LSHF.
- **Thiết bị Phụ trợ Nhà máy (Utilities & Material Handling):**
  - *Hệ thống trộn nhựa (PVC Compounding Mixer) & Máy sấy hút ẩm nhựa (Hopper Dryer)*.
  - *Tháp giải nhiệt (Cooling Tower) & Máy làm lạnh nước (Chiller)* cấp nước lạnh cho máng đùn & bể nhũ tương kéo đồng.
  - *Hệ thống Cầu trục (Overhead Crane 2–5 tấn)*, *Xe nâng (Forklift)* vận chuyển rulo nặng.
  - *Máy băm nghiền nhựa phế (Granulator)* & *Trạm cân điện tử kiểm soát phế liệu đồng trần/đồng bọc nhựa*.

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — MA TRẬN LỖI CÔNG NGHỆ, NGUYÊN NHÂN & ĐIỂM ĐÁNH OE THEO TỪNG MÁY

```text
┌──────────────────┬───────────────────────────┬──────────────────────────┬───────────────────────┐
│ Nhóm Máy         │ Lỗi & Tổn Thất Lớn Nhất   │ Nguyên Nhân Kỹ Thuật     │ Vũ Khí Tối Ưu OE      │
├──────────────────┼───────────────────────────┼──────────────────────────┼───────────────────────┤
│ Kéo thô RBD &    │ • Đứt sợi (Wire Break)    │ Mòn khuôn PCD, nhũ tương │ PM thay khuôn theo    │
│ Kéo tinh         │ • Dư đồng (Give-away)     │ bẩn/nóng, lỗi mối hàn,   │ tấn, lọc dầu ly tâm,  │
│                  │ • Oxy hóa đen đồng        │ sai drafting ratio       │ KPI Breaks/Ton        │
├──────────────────┼───────────────────────────┼──────────────────────────┼───────────────────────┤
│ Máy Bện          │ • Thời gian nạp rulo lâu  │ Thao tác nạp từng rulo   │ SMED bộ nạp nhanh,    │
│ (Buncher/Rigid)  │ • Sai bước xoắn/đứt 1 sợi │ thủ công, lực căng lệch, │ Man-Machine (1 người/ │
│                  │ • Dư mẩu rulo (Remnant)   │ bện không khớp đơn cắt   │ 3 máy), Cut-Length    │
├──────────────────┼───────────────────────────┼──────────────────────────┼───────────────────────┤
│ Máy Đùn Bọc      │ • Đổi màu/Purge 40-60p    │ Xếp lịch lộn xộn, chỉnh  │ Color Sequencing,     │
│ (PVC/XLPE/LSZH)  │ • Bọc dư nhựa +0.08mm     │ tâm ốc tay, nhựa ẩm,     │ SMED sấy đầu đùn,     │
│                  │ • Lỗi thủng Spark/Lệch tâm│ nước làm mát nóng >30°C  │ Laser Closed-loop SPC │
├──────────────────┼───────────────────────────┼──────────────────────────┼───────────────────────┤
│ Ghép Lõi &       │ • Lệch chiều dài giữa     │ Sai số Encoder đo mét ở  │ Hiệu chuẩn Encoder    │
│ Bọc Vỏ           │   3 lõi pha → Cắt bỏ x4   │ máy đùn lõi trước đó     │ định kỳ, Backward Plan│
├──────────────────┼───────────────────────────┼──────────────────────────┼───────────────────────┤
│ Đóng Cuộn &      │ • Năng suất lao động OLE  │ Nghẽn khâu dán tem/màng  │ Line Balancing,       │
│ Kho Rulo         │   thấp, đi lại thừa nhiều │ co, tìm rulo không vị trí│ Spaghetti, Barcode QR │
└──────────────────┴───────────────────────────┴──────────────────────────┴───────────────────────┘
```

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — ĐỌC HIỂU KÝ HIỆU CÁP CADIVI & CÁC TIÊU CHUẨN QUỐC TẾ CỐT LÕI

### Giải Mã Nhanh Ký Hiệu Cáp CADIVI Phổ Biến (Giúp Tự Tin Ngay Trong Buổi Phỏng Vấn):
- **VC / VCm / VCmd / VCmt:** Dây đơn cứng (`VC`), dây đơn mềm nhiều sợi (`VCm`), dây đôi mềm dẹt (`VCmd`), dây đôi mềm tròn (`VCmt`) — ruột đồng, cách điện PVC (`V`).
- **CV / CVV:** Cáp điện lực hạ thế ruột đồng (`C`), cách điện PVC (`V`), vỏ bảo vệ PVC (`V`).
- **CXV:** Cáp điện lực hạ thế ruột đồng (`C`), cách điện **XLPE (`X`)**, vỏ bảo vệ **PVC (`V`)** (vd: `CXV 3×50+1×25-0.6/1kV`).
- **CXV/DATA hoặc CXV/DSTA:** Cáp CXV có thêm lớp giáp 2 băng nhôm (`DATA` — cho cáp 1 lõi chống dòng xoáy) hoặc giáp 2 băng thép mạ kẽm (`DSTA` — cáp ngầm nhiều lõi).
- **AV / AXV / ABC:** Ruột **nhôm (`A`)**, cáp nhôm vặn xoắn treo trên không (`ABC` — Aerial Bundled Cable).
- **CXV/FR hoặc CXV/LSHF:** Cáp chống cháy có băng Mica chịu lửa (`FR` — Fire Resistant) hoặc vỏ không khói không halogen (`LSHF / LSZH`).

### 4 Bộ Tiêu Chuẩn Kỹ Thuật OE CADIVI Cần Biết Ý Nghĩa:
1. **[[IEC 60228]] / TCVN 6612:** Tiêu chuẩn **Ruột dẫn cáp cách điện** (Class 1 đặc, Class 2 bện tròn/nén, Class 5 mềm; quy định trần **điện trở DC tối đa tại 20°C** — gốc rễ của bài toán chống *[[Copper Give-away]]*!).
2. **[[IEC 60502]]-1 & 60502-2 / TCVN 5935:** Tiêu chuẩn **Cáp điện lực có cách điện dạng đùn** (hạ thế 1–3 kV và trung thế 6–30 kV; quy định công thức chiều dày cách điện/vỏ tối thiểu `t_min ≥ 0.9 × t_nom - 0.1 mm` — gốc rễ của bài toán [[SPC]] chống *[[Over-thickness]]*!).
3. **TCVN 6610 / IEC 60227:** Tiêu chuẩn dây dân dụng bọc [[PVC]] điện áp đến 450/750V.
4. **IEC 60332 / IEC 60754 / IEC 61034:** Tiêu chuẩn thử nghiệm chậm cháy, chống cháy lan, lượng khí axit halogen và mật độ khói cho dòng cáp an toàn cao cấp ([[LSZH]] / [[Mica FR]]).

---

## 5. ĐẶC THÙ CÁP RUỘT NHÔM [[ACSR]] / [[ABC Cable|CÁP ABC]], CÁP CHỐNG CHÁY [[Mica FR]] & THỬ NGHIỆM [[Partial Discharge|PD]] / [[Water Immersion]]

*(Phần mở rộng chuyên sâu giúp OE CADIVI Miền Trung xử lý trọn vẹn mọi chủng loại sản phẩm ngoài cáp đồng PVC/XLPE truyền thống)*

### 5.1. Đặc Thù Gia Công Ruột Nhôm ([[ACSR]] & [[ABC Cable|Cáp ABC]]) So Với Ruột Đồng:
- **Tính chất cơ lý khác biệt lớn:** Nhôm nhẹ hơn đồng ~3.3 lần (`2.70 g/cm³` so với `8.89 g/cm³`), mềm và dễ xước bề mặt nhưng độ bền kéo thấp hơn nhiều, dễ đứt sợi khi sức căng không đều; độ dẫn điện ~61% [[IACS]] (đồng ~100% IACS) nên cùng dòng tải tiết diện nhôm phải lớn hơn ~1.6 lần.
- **Kéo sợi nhôm (Aluminum Rod Breakdown):** Khác với đồng dùng [[Drawing Emulsion|nhũ tương kéo sợi gốc nước]], kéo nhôm thường dùng **dầu kéo chuyên dụng (Neat Oil)** có độ nhớt cao hơn và hệ lọc tinh chặt chẽ để tránh mạt nhôm bám khuôn [[PCD]] gây xước sợi và gãy sợi liên hoàn.
- **Bện cáp nhôm lõi thép ([[ACSR]]):**
  * Cấu trúc gồm lõi thép mạ kẽm chịu lực ở tâm (1 hoặc 7 sợi thép) và các lớp sợi nhôm 1350-H19 bện xoắn bao quanh bằng [[Rigid Strander|máy bện khung cứng]].
  * **Lỗi OE hay gặp:** Lồng đèn (Birdcaging) do lực căng giữa các sợi nhôm lệch nhau hoặc bước xoắn (Lay Length) lệch chuẩn; bám dầu mỡ thừa lên sợi nhôm; trượt căng lõi thép tâm.
  * **Kiểm soát:** Chuẩn hóa lực căng từng [[Pay-off|cuộn xả (Pay-off)]] bằng đồng hồ lực căng định kỳ, kiểm soát bôi mỡ chống ăn mòn (nếu khách hàng EVN yêu cầu cáp ven biển miền Trung) theo đúng định mức [[BOM]].
- **Cáp nhôm vặn xoắn treo trên không ([[ABC Cable|Cáp ABC]] — Aerial Bundled Cable):**
  * Gồm 2–4 lõi nhôm bọc [[XLPE]] màu đen chống tia cực tím UV (chứa ~2–2.5% Carbon Black [[Masterbatch]]) được bện xoắn chặt với nhau mà không có lớp vỏ chung bên ngoài.
  * **Điểm nghẽn OE thực chiến:** Nếu độ bám dính và độ đồng tâm lớp XLPE đen kém hoặc rãnh gân phân biệt pha (1 gân / 2 gân / 3 gân nổi trên vỏ) bị mờ do khuôn đùn mòn → Khó phân biệt pha ngoài công trường EVN và dễ bị trả lô!

### 5.2. Công Nghệ Cáp Chống Cháy [[Mica FR]] (Fire Resistant — IEC 60331):
- **Mục đích:** Duy trì cấp điện liên tục cho hệ thống bơm chữa cháy, quạt tăng áp, thang máy thoát hiểm ở **750°C – 950°C trong 90 – 180 phút** khi tòa nhà cháy.
- **Công đoạn đặc thù:** Sau khi bện ruột đồng, ruột dẫn đi qua **máy quấn băng Mica tốc độ cao (Mica Taping Machine)** với **độ chồng mí (Overlap)** chuẩn `35% – 50%` (thường quấn 2 lớp ngược chiều) trước khi bọc lớp cách điện [[XLPE]] và vỏ [[LSZH]].
- **3 Tổn thất OE điển hình tại máy quấn băng Mica:**
  1. **Đứt băng Mica liên tục:** Băng Mica giòn, hút ẩm; chỉ cần lực căng cuộn băng cao quá mức hoặc độ ẩm kho bảo quản cao → Đứt băng, dừng máy ([[Downtime]] cao và tạo đoạn nối lỗi).
  2. **Quấn dư độ chồng mí (Over-lapping):** Chỉnh góc quấn sai làm Overlap tăng từ 40% lên 55% → Hao phí băng Mica (vật tư nhập khẩu đắt tiền) vượt định mức [[BOM]] tới **25–30%**!
  3. **Rách băng Mica khi vào đầu máy đùn:** Nếu khe hở ống định hướng (Tip) quá chật hoặc không đồng tâm → Cào rách lớp Mica, cáp trượt bài test đốt lửa IEC 60331.
- **Giải pháp OE:** Lắp cảm biến [[Poka-Yoke]] phát hiện đứt/hết băng dừng máy tức thì (< 0.5s), kiểm soát độ ẩm kho Mica, khóa bảng tốc độ vòng quay đầu quấn theo tốc độ tuyến tính máy và giám sát độ chồng mí trong [[Control Plan]].

### 5.3. Hai Bài Thử Nghiệm Điện Cao Áp Trọng Yếu Tại Phòng Lab QA/QC CADIVI:
- **1. Thử Nghiệm Phóng Điện Cục Bộ ([[Partial Discharge|PD — Partial Discharge Test]], IEC 60502-2 / IEC 60885-3):**
  * **Áp dụng:** Bắt buộc 100% cuộn cáp trung thế (6 kV – 35 kV) bọc [[XLPE]] 3 lớp (Bán dẫn trong + Cách điện XLPE + Bán dẫn ngoài) chạy trên dây chuyền [[CCV Line]].
  * **Bản chất:** Đo xung phóng điện siêu nhỏ (đơn vị `pC` — picocoulomb, yêu cầu thường `≤ 5 pC` hoặc `≤ 10 pC` ở điện áp thử `1.73 U0` hoặc `2 U0`) bên trong phòng thử bọc lưới chắn nhiễu (Faraday Cage).
  * **Góc nhìn OE:** Nếu lô cáp trung thế bị lỗi PD (`> 10 pC`), nguyên nhân 90% đến từ: **bọt khí siêu nhỏ (Micro-void)**, **tạp chất bẩn trong hạt nhựa XLPE** (nhiễm bụi khi nạp phễu không kín hoặc [[Screen Pack|lưới lọc đầu đùn]] bị rách), hoặc **gồ ghề mặt phân cách lớp bán dẫn (Protrusion)**. Một cuộn cáp trung thế 500m hỏng PD có thể gây thiệt hại hàng trăm triệu đồng → OE phải kiểm soát tuyệt đối độ sạch phòng nạp hạt (Cleanroom Feeding) và chu kỳ thay Screen Pack!
- **2. Thử Nghiệm Ngâm Nước Chịu Điện Áp ([[Water Immersion|Water Immersion Voltage Test]], IEC 60502-1 / TCVN 5935):**
  * **Áp dụng:** Thử nghiệm xuất xưởng trên các cuộn cáp hạ thế (0.6/1 kV) và dây dân dụng sau khi đùn cách điện / hoàn thiện.
  * **Bản chất:** Ngâm toàn bộ cuộn cáp vào bể nước (thời gian tối thiểu 1 giờ ở nhiệt độ quy định, hai đầu lõi để khô nhô lên mặt nước), sau đó đặt điện áp cao AC (ví dụ `3.5 kV` trong 5 phút với cáp 0.6/1 kV) giữa ruột dẫn và nước nối đất.
  * **Góc nhìn OE:** Dù đã chạy qua [[Spark Tester]] trên dây chuyền, bài thử ngâm nước vẫn là "cửa ải cuối" bắt lỗi **lỗ kim siêu nhỏ (Pinholes)**, vết rạn do [[Cooling Trough|máng làm mát]] sốc nhiệt hoặc **điện trở cách điện thấp** do nhựa hút ẩm. Đồng thời bể thử cao áp là khu vực rủi ro điện giật cực cao → Bắt buộc áp dụng nghiêm ngặt khóa liên động cửa rào an toàn (Interlock) và quy trình [[LOTO]]!
"""
    },

    "oe_six_sigma_dmaic": {
        "title": "Cẩm Nang Operational Excellence (OE), Lean Six Sigma (DMAIC), TOC, TPM, PFMEA & Kiểm Định ROI",
        "summary": "Cẩm nang 4 tầng (Basic → Expert): Phân biệt OE/Lean/Six Sigma/IE, 5 pha DMAIC kèm Case Study giảm phế phẩm đùn cáp, 5 bước TOC (Drum-Buffer-Rope), TPM (MTBF/MTTR), PFMEA tính RPN, kiểm định thống kê t-test/ANOVA/p-value và bài toán tài chính ROI/Payback.",
        "category": "Sản Xuất (Manufacturing)",
        "content": r"""# 🏆 CẨM NANG OPERATIONAL EXCELLENCE (OE), SIX SIGMA (DMAIC), TOC, TPM & ROI
*(Hệ Phương Pháp Luận Toàn Diện Của Chuyên Viên Tối Ưu Quy Trình Từ Cơ Bản Đến Chuyên Gia)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — PHÂN BIỆT OE, LEAN, SIX SIGMA & IE + HỆ QUẢN TRỊ HÀNG NGÀY

```text
┌─────────────────────────┬───────────────────────────────────────────────────────────────┐
│ Hệ Phương Pháp          │ Trọng Tâm Mục Tiêu & Bộ Công Cụ Đại Diện                      │
├─────────────────────────┼───────────────────────────────────────────────────────────────┤
│ Industrial Engineering  │ Thiết lập chuẩn mực: Time & Motion Study, Định mức lao động   │
│ (IE — Kỹ thuật CN)      │ (SAM), Cân bằng chuyền, Layout, Ergonomics, Hoạch định RCCP.  │
├─────────────────────────┼───────────────────────────────────────────────────────────────┤
│ Lean Manufacturing      │ Tăng TỐC ĐỘ DÒNG CHẢY & XÓA 8 LÃNG PHÍ (TIMWOODS):            │
│ (Sản xuất tinh gọn)     │ VSM, 5S, SMED, Pull/Kanban, Poka-Yoke, Heijunka, Kaizen.      │
├─────────────────────────┼───────────────────────────────────────────────────────────────┤
│ Six Sigma               │ Giảm ĐỘ BIẾN THIÊN (σ) & XÓA KHUYẾT TẬT (< 3.4 DPMO):         │
│ (Chất lượng thống kê)   │ DMAIC, SPC (Xbar-R, Cpk), MSA Gage R&R, t-test, ANOVA, DOE.   │
├─────────────────────────┼───────────────────────────────────────────────────────────────┤
│ Operational Excellence  │ TẦNG HỆ THỐNG TỔNG THỂ kết hợp IE + Lean + Six Sigma +        │
│ (OE — Xuất sắc Vận hành)│ Quản trị hàng ngày đa tầng (Tier 1-2-3 SQDC) + Văn hóa + ROI. │
└─────────────────────────┴───────────────────────────────────────────────────────────────┘
```

### Hệ Thống Quản Trị Hàng Ngày Đa Tầng (Tiered Daily Management — SQDC):
- **Tier 1 (Tổ/Ca — 5–10 phút đầu ca):** Tổ trưởng rà soát 4 chữ cái **S**afety (An toàn) – **Q**uality (Chất lượng/Spark) – **D**elivery (Sản lượng mét/tiến độ) – **C**ost (OEE/Phế đồng-nhựa).
- **Tier 2 (Phân xưởng — 15 phút buổi sáng):** Quản đốc + OE + Bảo trì + QC + Điều độ xử lý các điểm Đỏ từ Tier 1 với bảng hành động rõ ràng: **Ai làm – Việc gì – Hạn hoàn thành (Who – What – When)**.
- **Tier 3 (Nhà máy — Hàng ngày/tuần):** Giám đốc nhà máy quyết định nguồn lực liên phòng ban và tiến độ dự án Kaizen/CAPEX.

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — LÝ THUYẾT ĐIỂM NGHẼN (TOC), TPM & PFMEA

### A. 5 Bước Tập Trung Của Lý Thuyết Điểm Nghẽn (Theory of Constraints — TOC):
1. **Identify (Xác định):** Tìm ĐÚNG công đoạn nút thắt quyết định sản lượng xuất xưởng (vd: Máy đùn bọc vỏ lớn số 2 có hàng rulo ùn ứ trước cửa).
2. **Exploit (Khai thác tối đa — 0 đồng CAPEX):** Giữ máy nút thắt chạy 100% thời gian ăn ca (bố trí thay phiên), áp dụng SMED, kiểm soát QC chặt đầu vào để nút thắt không bao giờ chạy hàng lỗi.
3. **Subordinate (Bắt các máy khác phục tùng):** Điều tiết tốc độ máy Kéo/Bện phía trước theo đúng nhịp máy nút thắt (cơ chế **Drum–Buffer–Rope**: Trống gõ nhịp – Đệm an toàn trước nút thắt – Dây kéo hạn chế cấp nguyên liệu thừa).
4. **Elevate (Nâng cấp năng lực):** Khi khai thác kịch trần vẫn thiếu tải → mở thêm ca, cải tiến nâng tốc độ hoặc đầu tư thêm máy.
5. **Repeat (Lặp lại):** Khi nút thắt cũ biến mất, điểm nghẽn mới sẽ xuất hiện ở chỗ khác → Quay lại Bước 1!

### B. 8 Trụ Cột TPM & 2 Chỉ Số Độ Tin Cậy Thiết Bị (MTBF / MTTR):
```text
┌────────────────────────────────────────────────────────────────────────┐
│  CÔNG THỨC ĐO ĐỘ TIN CẬY THIẾT BỊ TRONG TPM                            │
└────────────────────────────────────────────────────────────────────────┘

             Tổng Thời Gian Máy Vận Hành Thực Tế (Giờ)
  MTBF  =  ─────────────────────────────────────────────  (Càng CAO càng tốt)
                  Tổng Số Lần Dừng Hỏng Đột Xuất

             Tổng Thời Gian Dừng Sửa Chữa Sự Cố (Giờ)
  MTTR  =  ─────────────────────────────────────────────  (Càng THẤP càng tốt)
                  Tổng Số Lần Dừng Hỏng Đột Xuất

  Ví dụ thực tế Máy Kéo Thô RBD trong tháng:
  • Tổng thời gian chạy = 420 giờ; Hỏng đột xuất = 6 lần; Tổng thời gian sửa = 9 giờ.
  → MTBF = 420 / 6 = 70 giờ/lần hỏng  |  MTTR = 9 / 6 = 1.5 giờ/lần sửa.
  → Mục tiêu TPM: Đẩy MTBF > 150 giờ (bảo trì tự quản Jishu Hozen & PM đúng hạn)
    và kéo MTTR < 0.75 giờ (sẵn phụ tùng vòng bi/điện trở + SOP sửa lỗi nhanh).
```

### C. Lập Bảng PFMEA (Phân Tích Sai Lỗi & Tác Động Quá Trình) Cho Dây Chuyền Đùn Cáp:
Công thức điểm ưu tiên rủi ro: `RPN = Severity (S: 1–10) × Occurrence (O: 1–10) × Detection (D: 1–10)` (Lưu ý chuẩn AIAG-VDA mới: luôn hành động ưu tiên cao nhất với mọi lỗi có `S ≥ 9` bất kể RPN!).

```text
┌───────────────────┬──────────────────────┬────┬────┬────┬─────┬──────────────────────────┐
│ Công Đoạn Đùn     │ Dạng Lỗi Tiềm Ẩn     │  S │  O │  D │ RPN │ Hành Động Khắc Phục (OE) │
├───────────────────┼──────────────────────┼────┼────┼────┼─────┼──────────────────────────┤
│ Bọc cách điện     │ Lệch tâm vỏ quá mỏng │  9 │  4 │  5 │ 180 │ Gắn Laser Eccentricity   │
│ PVC / XLPE        │ (nguy cơ chập cháy)  │    │    │    │     │ Gauge trực tuyến (D→2)   │
├───────────────────┼──────────────────────┼────┼────┼────┼─────┼──────────────────────────┤
│ Sấy & Cấp hạt     │ Hạt PVC ẩm tạo bọt   │  8 │  5 │  4 │ 160 │ Khóa liên động nhiệt độ  │
│ nhựa              │ khí → thủng Spark    │    │    │    │     │ Hopper Dryer (O→2)       │
├───────────────────┼──────────────────────┼────┼────┼────┼─────┼──────────────────────────┤
│ In phun vỏ cáp    │ Mờ chữ/sai số mét    │  5 │  3 │  4 │  60 │ Kiểm tra đầu cuộn + PM   │
│                   │ trên bề mặt vỏ       │    │    │    │     │ vệ sinh đầu phun mỗi ca  │
└───────────────────┴──────────────────────┴────┴────┴────┴─────┴──────────────────────────┘
```

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — CASE STUDY DỰ ÁN DMAIC GIẢM PHẾ PHẨM ĐÙN CÁP (3.8% → 0.8%)

**Đề bài dự án OE (3 tháng tại Nhà máy CADIVI):** Dây chuyền Đùn số 4 sản xuất dây `VC 2.5 mm²` có tỷ lệ phế phẩm trung bình **3.8%** (chi phí tổn thất phế đồng dính nhựa & PVC ~**95 triệu VNĐ/tháng**).

1. **D — Define (Tuần 1):**
   - Lập *Project Charter*: Giảm tỷ lệ phế phẩm từ `3.8%` xuống `≤ 1.0%` trong 12 tuần (mục tiêu tiết kiệm ≥ 70 triệu/tháng).
   - Xác định *CTQ*: Đường kính ngoài 3.38 ± 0.10 mm, chiều dày min ≥ 0.62 mm, 0 lỗi Spark/cuộn.
2. **M — Measure (Tuần 2–3):**
   - Kiểm định MSA Gage R&R cho kính hiển vi đo chiều dày & cân phế → đạt `%GRR = 6.2%` (< 10%, tin cậy).
   - Thu thập Baseline 30 ngày & vẽ **Pareto lỗi**: 45% do *Lệch tâm/mỏng vỏ đầu ca*, 32% do *Thủng Spark (bọt khí/hạt cháy)*, 15% do *Xả nhựa đổi màu*, 8% nguyên nhân khác.
3. **A — Analyze (Tuần 4–6):**
   - Vẽ Xương cá (Ishikawa) + 5 Whys; chạy **ANOVA & Hồi quy trên Minitab** kiểm chứng dữ liệu thực:
     * Nhiệt độ vùng đùn 3 dao động ±12°C do bộ điều khiển PID cũ hỏng cảm biến (`p = 0.001`).
     * Hạt nhựa nạp vào phễu chưa sấy đủ thời gian ca đêm (`p = 0.004`).
     * Chỉnh tâm 4 ốc thủ công mỗi lần đổi màu gây phế đầu ca dài 150m (`p = 0.000`).
4. **I — Improve (Tuần 7–9):**
   - Thay cặp cảm biến nhiệt + hiệu chuẩn PID giữ dao động `≤ ±2°C`; lắp bộ định giờ sấy hạt nhựa bắt buộc 45 phút ở 75°C; triển khai SMED + Color Sequencing + sấy sẵn đầu chữ thập tự định tâm.
   - Chạy Pilot 20 ca → Tỷ lệ phế giảm còn **0.78%**.
5. **C — Control (Tuần 10–12):**
   - Chạy kiểm định **2-Sample t-test** (Trước: `Mean = 3.80%, SD = 0.62%` vs Sau: `Mean = 0.78%, SD = 0.19%`) → **`p-value = 0.000 (< 0.05)`** — chứng minh thống kê chắc chắn ≥ 99.9%!
   - Ban hành **Control Plan**, biểu đồ Xbar-R theo ca, bảng SOP 1 trang (OPL) treo tại máy; duy trì theo dõi 90 ngày xác nhận tiết kiệm thực đạt **75.5 triệu VNĐ/tháng (~906 triệu/năm)**.

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — CHỌN ĐÚNG KIỂM ĐỊNH THỐNG KÊ & THẨM ĐỊNH TÀI CHÍNH ROI / PAYBACK

### Bản Đồ Chọn Nhanh Kiểm Định Giả Thuyết (Hypothesis Testing) Cho Báo Cáo Trước–Sau:
- **So sánh trung bình 2 nhóm (Trước vs Sau cải tiến, dữ liệu liên tục chuẩn):** Dùng **2-Sample t-test** (hoặc **Paired t-test** nếu đo trên cùng 1 mẫu/máy).
- **So sánh trung bình ≥ 3 nhóm (vd: Ca 1 vs Ca 2 vs Ca 3, hoặc Máy đùn 1 vs 2 vs 3):** Dùng **One-Way ANOVA**.
- **So sánh dữ liệu phi chuẩn (thời gian đổi mã bị lệch phải):** Dùng **Mann-Whitney U test** (2 nhóm) hoặc **Kruskal-Wallis** (≥ 3 nhóm).
- **So sánh tỷ lệ lỗi % (vd: tỷ lệ cuộn lỗi Spark Trước vs Sau):** Dùng **2-Proportions Test** hoặc **Chi-Square Test**.
- **Nguyên tắc đọc kết quả:** *"If p is low, H0 must go"* — Khi **p-value < 0.05**, sự cải tiến là CÓ Ý NGHĨA THỐNG KÊ (độ tin cậy 95%), không phải ngẫu nhiên!

### Bài Toán Thẩm Định Tài Chính CAPEX / ROI Chuẩn Ban Giám Đốc:
```text
┌────────────────────────────────────────────────────────────────────────┐
│  BÀI TOÁN THẨM ĐỊNH ĐẦU TƯ THIẾT BỊ TỰ ĐỘNG (CAPEX & PAYBACK PERIOD)   │
└────────────────────────────────────────────────────────────────────────┘

Giả sử đề xuất đầu tư Hệ thống đo đường kính/độ lệch tâm Laser Closed-loop
cho 2 dây chuyền đùn chủ lực:
  • Tổng vốn đầu tư (Total CAPEX): 960,000,000 VNĐ (thiết bị + lắp đặt + đào tạo).
  • Chi phí vận hành/hiệu chuẩn hàng năm (OPEX): 36,000,000 VNĐ/năm (3 triệu/tháng).
  • Lợi ích tiền tươi trực tiếp (Hard Savings — đã được Kế toán xác nhận):
    - Tiết kiệm 6% lượng nhựa PVC bọc dư trên 2 máy = 2,400 kg/tháng × 32,000 đ = 76.8 triệu/tháng.
    - Giảm phế phẩm đồng dính nhựa đầu ca 400 kg/tháng × 50,000 đ (chênh lệch) = 20.0 triệu/tháng.
    → Tổng lợi ích gộp = 96.8 triệu/tháng.
    → Tiết kiệm ròng (Net Monthly Savings) = 96.8 - 3.0 = 93.8 triệu VNĐ/tháng.

1. Thời gian hoàn vốn đơn giản (Simple Payback Period):
                Tổng Vốn Đầu Tư (CAPEX)          960 triệu
   Payback  =  ───────────────────────────  =  ─────────────  =  10.23 tháng (< 1 năm!)
                Tiết Kiệm Ròng Hàng Tháng       93.8 triệu

2. Tỷ Suất Hoàn Vốn Năm Đầu (1st-Year ROI):
                (93.8 × 12) - 960        1,125.6 - 960
   ROI      =  ───────────────────  =  ─────────────────  × 100%  =  +17.25% (ngay năm 1!)
                       960                    960
   (Từ năm thứ 2 trở đi sinh lời ròng > 1.12 tỷ VNĐ/năm!)

3. Quy tắc vàng trình bày BGĐ: Luôn kèm 3 kịch bản độ nhạy (Thận trọng đạt 70% mục tiêu
   → hoàn vốn 14.6 tháng; Cơ sở → 10.2 tháng; Tích cực → 8.5 tháng) để chứng minh dự án cực an toàn!
```
"""
    },

    "cable_cost_capacity": {
        "title": "Cẩm Nang Hoạch Định Năng Lực (RCCP), BOM Cáp Điện, Hao Phí Đồng/Nhựa & Tối Ưu Cut-Length",
        "summary": "Cẩm nang 4 tầng (Basic → Expert): Công thức tính khối lượng đồng/nhôm (kèm hệ số xoắn Lay-up Factor) và nhựa cách điện hình vành khăn, định lượng Copper Give-away & Over-thickness, tối ưu cắt rulo Cut-Length, hoạch định năng lực RCCP tấn/km và kiểm soát điện năng kWh/tấn.",
        "category": "Sản Xuất (Manufacturing)",
        "content": r"""# 💰 CẨM NANG HOẠCH ĐỊNH NĂNG LỰC (RCCP), BOM CÁP ĐIỆN & TỐI ƯU GIÁ THÀNH
*(Từ Công Thức Vật Lý Ruột Dẫn Đến Bài Toán Tiết Kiệm Hàng Tỷ Đồng Tại Nhà Máy Dây Cáp Điện)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — CÔNG THỨC TÍNH ĐỊNH MỨC ĐỒNG/NHÔM & NHỰA CÁCH ĐIỆN TRÊN 1 KM CÁP

Để không bị "mù số liệu" khi đọc bảng định mức BOM tại CADIVI, Chuyên viên OE phải thuộc lòng 3 công thức hình học vật lý cốt lõi:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  BỘ 3 CÔNG THỨC ĐỊNH MỨC KHỐI LƯỢNG NGUYÊN VẬT LIỆU NGÀNH DÂY CÁP ĐIỆN (kg / km)       │
└────────────────────────────────────────────────────────────────────────────────────────┘

1. Khối Lượng Kim Loại Ruột Dẫn (M_metal — kg / km):
                     π × d²
   M_metal  =  n  ×  ──────  ×  ρ_metal  ×  k_xoan
                       4

   Trong đó:
   • n        : Số sợi đơn cấu thành ruột dẫn (vd: 1, 7, 19, 37 sợi).
   • d        : Đường kính 1 sợi đơn (mm).
   • ρ_metal  : Khối lượng riêng kim loại — Đồng (Cu) = 8.89 g/cm³; Nhôm (Al) = 2.703 g/cm³.
   • k_xoan   : Hệ số xoắn bện (Lay-up / Stranding Factor) = sqrt(1 + (π × D_pitch / h)²)
                (Ruột đặc 1 sợi: k = 1.00; Ruột bện nhiều sợi: thường k = 1.015 đến 1.035).

2. Khối Lượng Nhựa Cách Điện / Vỏ Bọc Hình Vành Khăn (M_plastic — kg / km):
                 π
   M_plastic = ───── × (D_ngoai² - D_trong²) × ρ_nhua
                 4
   (Hoặc dạng theo chiều dày t:  M_plastic = π × (D_trong + t) × t × ρ_nhua)

   Trong đó:
   • D_trong  : Đường kính trước khi bọc (mm); D_ngoai = D_trong + 2×t (mm).
   • t        : Chiều dày lớp nhựa cách điện / vỏ bọc (mm).
   • ρ_nhua   : Khối lượng riêng nhựa — PVC ≈ 1.38 – 1.48 g/cm³; XLPE ≈ 0.92 – 0.94 g/cm³;
                PE ≈ 0.92 – 0.95 g/cm³; LSZH/LSHF ≈ 1.45 – 1.60 g/cm³.

3. Điện Trở Ruột Dẫn 1 Chiều Lý Thuyết Ở 20°C (R_20 — Ω / km):
                 17.241 × k_xoan
   R_20 (Cu) ≈  ──────────────────   (S là tổng tiết diện mặt cắt đồng thực tế, mm²)
                        S
```

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — BÀI TOÁN ĐỊNH LƯỢNG "COPPER GIVE-AWAY" & "OVER-THICKNESS"

### Bài Toán 1 — Thiệt Hại Khổng Lồ Từ "Copper Give-away" (Kéo Dư Chỉ 0.01 mm!):
Một dây chuyền kéo sợi đơn **Ø 1.78 mm** (cho dây dân dụng `VC 2.5 mm²`) có sản lượng **200 tấn đồng/tháng** (đơn giá đồng rod ≈ `250,000,000 VNĐ / tấn`).
- Do khuôn kéo bị mòn chậm thay, đường kính thực tế trung bình là **Ø 1.79 mm** (chỉ to hơn chuẩn đúng **0.01 mm** — bằng 1/7 sợi tóc!).
- Tỷ lệ tăng khối lượng đồng tỷ lệ với bình phương đường kính:
```text
   Tỷ lệ dư đồng  =  (1.79² / 1.78²) - 1  =  (3.2041 / 3.1684) - 1  =  +1.127%

   → Lượng đồng "cho không" khách hàng = 200 tấn × 1.127% = 2.254 tấn / tháng!
   → Tiền lợi nhuận BỐC HƠI = 2.254 tấn × 250 triệu = 563,500,000 VNĐ / THÁNG
                                                     ≈ 6.76 TỶ ĐỒNG / NĂM!
```
→ **Bài học OE:** Đầu tư quản lý tuổi thọ khuôn kéo PCD, đo điện trở thực tế và kiểm soát SPC đường kính kéo là mỏ vàng lớn nhất nhà máy cáp!

### Bài Toán 2 — Thiệt Hại Từ Bọc Dư Nhựa Cách Điện (Over-thickness +0.08 mm):
Dây `VC 2.5 mm²` (`D_trong = 1.78 mm`, nhựa PVC `ρ = 1.42 g/cm³`, đơn giá `32,000 VNĐ/kg`), sản lượng **5,000 km/tháng**:
- Định mức chiều dày chuẩn `t_chuẩn = 0.80 mm`:
  `M_chuẩn = 3.1416 × (1.78 + 0.80) × 0.80 × 1.42 = 9.21 kg/km`.
- Do lệch tâm cao, công nhân chỉnh bọc dày lên `t_thực = 0.88 mm` (dư `+0.08 mm`):
  `M_thực = 3.1416 × (1.78 + 0.88) × 0.88 × 1.42 = 10.44 kg/km`.
- Chênh lệch = `+1.23 kg/km` (+13.4% nhựa!).
- Trên sản lượng 5,000 km/tháng → **Thất thoát `6,150 kg PVC/tháng` = `196.8 triệu VNĐ/tháng` (~2.36 tỷ VNĐ/năm)** chỉ trên 1 mã dây!

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — HOẠCH ĐỊNH NĂNG LỰC THÔ (RCCP) & TỐI ƯU CẮT RULO (CUT-LENGTH)

### Bài Toán A — Hoạch Định Năng Lực Thô (Rough-Cut Capacity Planning — RCCP):
Phòng Kinh doanh đưa kế hoạch tháng tới: **300 tấn cáp các loại**. Nhà máy chạy **26 ngày × 2 ca × 7.5 giờ kế hoạch/ca = 390 giờ kế hoạch / máy / tháng**.

```text
┌───────────────────┬────────┬───────────┬─────────────┬──────────────┬───────────┬──────────┐
│ Công Đoạn         │ Số Máy │ OEE Thực  │ Giờ Khả Dụng│ Giờ Yêu Cầu  │ Tải Load% │ Đánh Giá │
│                   │        │ Lịch Sử   │ Thực Tế (h) │ Cho 300 Tấn  │           │          │
├───────────────────┼────────┼───────────┼─────────────┼──────────────┼───────────┼──────────┤
│ 1. Kéo Thô RBD    │   2    │   78%     │   608.4 h   │    440.0 h   │   72.3%   │ Đủ tải   │
│ 2. Kéo Trung/Tinh │   6    │   75%     │ 1,755.0 h   │  1,380.0 h   │   78.6%   │ Đủ tải   │
│ 3. Bện Ruột Dẫn   │   5    │   72%     │ 1,404.0 h   │  1,220.0 h   │   86.9%   │ Cận tải  │
│ 4. Đùn Cách Điện  │   4    │   65%     │ 1,014.0 h   │  1,180.0 h   │  116.4%   │ QUÁ TẢI! │
│ 5. Ghép Lõi & Vỏ  │   3    │   70%     │   819.0 h   │    680.0 h   │   83.0%   │ Đủ tải   │
└───────────────────┴────────┴───────────┴─────────────┴──────────────┴───────────┴──────────┘
  (Công thức: Giờ Khả Dụng Thực Tế = Số Máy × 390 giờ × OEE Thực Lịch Sử)
```
**Quyết định điều hành từ báo cáo RCCP của OE:**
- Điểm nghẽn tuyệt đối nằm ở **Công đoạn 4: Đùn Cách Điện (thiếu 166 giờ chạy máy ròng)**.
- **3 phương án giải cứu không mua máy mới:**
  1. Triển khai ngay SMED + Color Sequencing nâng OEE máy đùn từ `65% → 76%` → Tăng ngay `+171.6 giờ` khả dụng thực tế (giải quyết sạch phần thiếu hụt!).
  2. Mở tăng cường Ca 3 cục bộ cho riêng 2 máy đùn chủ lực trong 2 tuần cao điểm.
  3. TUYỆT ĐỐI không tăng ca tràn lan ở xưởng Kéo/Bện vì đang dư tải — tăng ca xưởng Kéo chỉ tạo thêm núi WIP!

### Bài Toán B — Tối Ưu Chiều Dài Rulo (Cut-Length / Cutting Stock Optimization):
- Khi đơn hàng cần nhiều đoạn lẻ (vd: 400m, 500m, 650m, 1,000m), thay vì bện tràn đầy rulo 2,200m rồi cắt thừa mẩu 150–250m bỏ phế:
  1. Dùng công cụ **Excel Solver** hoặc **Python (`PuLP` / Linear Programming)** để tìm tổ hợp ghép đoạn sao cho tổng chiều dài các đoạn + `15m hao hụt đầu-đuôi` khớp sát `98–99.5%` chiều dài rulo.
  2. Triển khai kế hoạch **Backward Length Planning** từ công đoạn Đùn vỏ ngược về Ghép lõi → Đùn lõi → Bện ruột để tất cả 3 pha Đỏ–Vàng–Xanh có chiều dài bằng nhau chuẩn xác đến `±0.3%`.

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — PHÂN TÍCH GIÁ THÀNH SẢN XUẤT & TỐI ƯU ĐIỆN NĂNG (kWh / TẤN)

### Cấu Trúc Giá Thành 1 Km Cáp Điện & Thứ Tự Đòn Bẩy Tài Chính:
1. **Nguyên vật liệu trực tiếp (80–88%):** Đồng/Nhôm (60–75%), Nhựa PVC/XLPE/LSZH (15–25%), Băng thép/Rulo (3–5%).
2. **Chi phí sản xuất chung Overhead (6–12%):** Trong đó **Điện năng tiêu thụ** cho động cơ kéo thô (300 kW), lò ủ, điện trở nòng đùn và Chiller chiếm tỷ trọng rất lớn!
3. **Nhân công trực tiếp (4–7%):** Lương vận hành, phụ cấp ca đêm, tăng ca.

### 4 Biện Pháp Giảm Cường Độ Điện Năng (`SEC = kWh / Tấn Sản Phẩm`) Ngay Tại Xưởng:
1. **Xóa thời gian "Đùn chờ nhiệt không tải" (Idle Heating):** Lập lịch liên hoàn không để máy đùn bật điện trở 180°C ngồi chờ rulo hay chờ đổi màu 2 giờ/ngày; bọc áo cách nhiệt (Insulation Jackets) quanh nòng Barrel giúp giảm **15–25%** điện gia nhiệt.
2. **Dịch chuyển phụ tải giờ thấp điểm (Load Shifting):** Lập lịch chạy các lò ủ chuông, bể xông XLPE và máy kéo thô công suất lớn vào khung giờ thấp điểm điện lực (22:00 – 04:00, đơn giá điện thấp hơn giờ cao điểm 2.5–3 lần!).
3. **Kiểm toán rò rỉ khí nén & biến tần (VFD):** Kiểm tra siêu âm rò rỉ van khí nén định kỳ hàng quý; kiểm tra hiệu suất Chiller/Tháp giải nhiệt.
4. **Nâng cao OEE tổng thể:** Máy chạy ít dừng vặt, ít chạy lại phế phẩm → Khấu hao và chi phí điện cố định phân bổ trên mỗi km cáp đạt chuẩn giảm ngay **10–18%**!
"""
    },

    "planning_quality_ehs_cost": {
        "title": "Cẩm Nang Kế Hoạch S&OP–MRP–CRP, Chất Lượng FPY/RTY, An Toàn LOTO–ISO, Giá Thành Định Mức & Hoshin/ADKAR",
        "summary": "Cẩm nang 4 tầng (Basic → Expert): Luồng kế hoạch S&OP → MPS → MRP → RCCP → CRP, tồn kho Safety Stock/ROP/ABC-XYZ/Milk Run, chất lượng toàn chuỗi FPY vs RTY & 7 QC Tools/Control Plan, an toàn EHS/LOTO 6 bước & 4 chuẩn ISO 9001/14001/45001/50001, kế toán giá thành Standard Cost Variance và quản trị thay đổi Hoshin Kanri / ADKAR tại CADIVI.",
        "category": "Sản Xuất (Manufacturing)",
        "content": r"""# 📋 CẨM NANG KẾ HOẠCH (S&OP–MRP–CRP), CHẤT LƯỢNG (FPY/RTY), AN TOÀN (LOTO/ISO) & GIÁ THÀNH ĐỊNH MỨC
*(4 Mảnh Ghép Hệ Thống Đưa Chuyên Viên OE CADIVI Từ Cải Tiến Cục Bộ Lên Quản Trị Vận Hành Toàn Diện)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — HỆ THỐNG HOẠCH ĐỊNH SẢN XUẤT ([[S&OP]] → [[MPS]] → [[MRP]] → [[CRP]]) & TỒN KHO KHOA HỌC

### 1.1. Luồng Hoạch Định 5 Tầng Từ Kinh Doanh Đến Từng Máy Dưới Xưởng:
Nhiều nhà máy hay rơi vào cảnh "Kinh doanh bán một đằng, Xưởng chạy một nẻo, Kho đồng hết bất ngờ mà tồn kho thành phẩm lại đầy ắp". Gốc rễ là đứt gãy chuỗi 5 tầng hoạch định sau:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  1. S&OP (Sales & Operations Planning — Tầm nhìn 3–18 tháng, theo Nhóm sản phẩm/Tấn)  │
│     • Ban Giám Đốc + Kinh doanh + Sản xuất + Mua hàng cân đối Cầu dự báo vs Năng lực   │
│                                          │                                             │
│                                          ▼                                             │
│  2. MPS (Master Production Schedule — Tầm nhìn 4–12 tuần, theo Mã cáp SKU cụ thể)     │
│     • Kế hoạch sản xuất tổng thể: Tuần nào giao bao nhiêu km CXV 3×50, CVV 4×16...    │
│     • Kiểm tra tải thô bằng RCCP (Rough-Cut Capacity Planning) ở công đoạn cổ chai!    │
│                                          │                                             │
│                                          ▼                                             │
│  3. MRP (Material Requirements Planning — Phá rã BOM theo ngày/tuần trên ERP)         │
│     • Tính chính xác cần mua/xuất bao nhiêu tấn Đồng Rod, hạt XLPE, PVC, Băng thép,   │
│       Rulo gỗ tại từng thời điểm (trừ đi Tồn kho khả dụng & Hàng đang về).            │
│                                          │                                             │
│                                          ▼                                             │
│  4. CRP (Capacity Requirements Planning — Hoạch định năng lực chi tiết từng máy/ca)   │
│     • Chuyển lệnh MRP sang tải giờ máy chi tiết theo Routing + Thời gian Setup (SMED)  │
│     • Phát hiện quá tải theo từng máy đùn, từng ca để san tải hoặc tăng ca cục bộ.    │
│                                          │                                             │
│                                          ▼                                             │
│  5. PAC / MES Shop-Floor Dispatching (Điều độ thời gian thực từng giờ tại xưởng)      │
│     • Sắp thứ tự chạy tối ưu (Color Sequencing), ghi nhận sản lượng & OEE thực tế.    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2. Quản Trị Tồn Kho & Cấp Vật Tư Tinh Gọn Tại CADIVI:
- **[[Safety Stock]] (Tồn kho an toàn):** Lượng đệm bảo vệ xưởng khỏi biến động nhu cầu đơn hàng dự án điện lực và độ trễ giao hàng (Lead Time) của nhà cung cấp đồng/hạt nhựa nhập khẩu.
  * Công thức chuẩn: `SS = Z × √(LT × σ_D² + D̄² × σ_LT²)` (với mức phục vụ 95% → `Z = 1.65`; mức 98% → `Z = 2.05`).
- **[[ROP]] (Reorder Point — Điểm đặt hàng lại):** Mức tồn kho kích hoạt phát đơn mua mới để hàng kịp về trước khi cạn.
  * Công thức: `ROP = (Nhu cầu trung bình/ngày × Lead Time ngày) + Safety Stock`.
  * *Ví dụ tại CADIVI:* Hạt nhựa [[XLPE]] Silane tiêu thụ trung bình `4 tấn/ngày`, thời gian giao hàng nhà cung cấp `12 ngày`, Safety Stock `14 tấn` → `ROP = 4 × 12 + 14 = 62 tấn`. Khi tồn khả dụng trên [[ERP]] chạm `62 tấn`, hệ thống tự phát yêu cầu mua hàng ngay!
- **Phân loại ma trận [[ABC-XYZ]]:**
  * **Trục ABC (Giá trị tiêu thụ năm):** Nhóm A (70–80% giá trị: Đồng Rod, Nhôm Rod, Hạt XLPE/LSZH) kiểm soát chặt hàng ngày; Nhóm C (5% giá trị: băng keo, tem nhãn, bao bì) dùng [[Two-Bin Kanban]] tự động bổ sung.
  * **Trục XYZ (Độ ổn định nhu cầu theo hệ số biến thiên CV):** Nhóm X (ổn định: dây dân dụng VCm 1.5–4.0 mm²) sản xuất theo mức tồn kho tối thiểu (MTS — Make-to-Stock); Nhóm Z (thất thường: cáp dự án trung thế giáp thép DSTA/FR) sản xuất theo đơn đặt hàng (MTO — Make-to-Order).
- **[[Milk Run]] (Chuyến xe thu gom/cấp phát tuần hoàn):** Thay vì công nhân đứng máy bỏ chuyền tự đi tìm rulo, hạt nhựa, màu [[Masterbatch]] (lãng phí Motion & Waiting), 1 xe nâng/xe kéo vật tư chạy đúng tuyến định kỳ mỗi 60 phút cấp vật tư đúng vị trí và thu hồi rulo rỗng/phế liệu về kho!

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — CHẤT LƯỢNG TOÀN CHUỖI ([[FPY]] / [[RTY]]) & BỘ CÔNG CỤ [[7 QC Tools|7 QC TOOLS]]

### 2.1. Cái Bẫy "Tỷ Lệ Đạt Cao Ảo" & Sự Khác Biệt Sống Còn Giữa [[FPY]] và [[RTY]]:
- **Traditional Yield (Tỷ lệ đạt cuối chuyền):** Chỉ đếm thành phẩm cuối cùng sau khi đã sửa lỗi (Rework) / cắt nối → **Che giấu hoàn toàn** nhà máy ẩn (Hidden Factory) gồm nhân công sửa lỗi, điện năng chạy lại và đồng/nhựa cắt bỏ!
- **[[FPY]] (First Pass Yield — Tỷ lệ đạt ngay lần đầu):** Tỷ lệ sản phẩm đạt chuẩn ở 1 công đoạn ngay lần chạy đầu tiên mà KHÔNG cần sửa chữa, đánh dấu lỗi hay chạy lại.
- **[[RTY]] (Rolled Throughput Yield — Tỷ lệ đạt xuyên suốt toàn chuỗi):** Tích số `FPY` của tất cả các công đoạn nối tiếp nhau trong dây chuyền.

```text
VÍ DỤ TÍNH RTY THỰC TẾ DÂY CHUYỀN CÁP CXV 3×50+1×25 TẠI NHÀ MÁY CADIVI:
┌─────────────────────────┬──────────┬─────────────────────────────────────────────┐
│ Công Đoạn               │   FPY    │ Dạng Lỗi Phổ Biến Bị Ẩn Nếu Chỉ Xem Cuối   │
├─────────────────────────┼──────────┼─────────────────────────────────────────────┤
│ 1. Kéo Thô & Trung RBD  │  98.0%   │ Đứt sợi, xước bề mặt, sai đường kính khuôn  │
│ 2. Ủ Mềm & Bện Ruột     │  99.0%   │ Bung sợi, sai bước xoắn, vượt điện trở DC   │
│ 3. Đùn Cách Điện XLPE   │  97.0%   │ Lệch tâm, lỗi Spark Tester, sần nhựa        │
│ 4. Lưu Hóa (Xông Hơi)   │  95.0%   │ Không đạt độ giãn dài nóng (Hot Set Test)   │
│ 5. Ghép Lõi & Giáp DSTA │  96.0%   │ Lệch chiều dài 3 pha → Cắt bỏ đoạn thừa     │
│ 6. Đùn Vỏ PVC & Lab QC  │  97.0%   │ Mờ chữ in phun, trầy vỏ, lỗi ngâm nước      │
├─────────────────────────┴──────────┴─────────────────────────────────────────────┤
│  RTY = 0.98 × 0.99 × 0.97 × 0.95 × 0.96 × 0.97 = 0.8327  →  CHỈ ĐẠT 83.27% !    │
│  → Cứ 100 km khởi tạo, gần 16.73 km bị vướng lỗi/rework/cắt đoạn ở giữa đường!  │
└──────────────────────────────────────────────────────────────────────────────────┘
```
- **[[DPMO]] (Defects Per Million Opportunities):** Quy đổi số lỗi trên 1 triệu cơ hội lỗi để đối sánh mức Sigma (3 Sigma ≈ 66,807 DPMO; 4 Sigma ≈ 6,210 DPMO; 6 Sigma = 3.4 DPMO).

### 2.2. Bộ [[7 QC Tools|7 Công Cụ Kiểm Soát Chất Lượng (7 QC Tools)]] & Cầu Nối [[VOC]] → [[CTQ]] → [[Control Plan]]:
1. **Check Sheet (Phiếu kiểm tra):** Thu thập dữ liệu lỗi/[[Downtime]] đúng chuẩn ngay tại máy (nền tảng trước khi lên [[MES]]).
2. **[[Pareto|Biểu đồ Pareto (80/20)]]:** Xác định 20% nguyên nhân gây ra 80% mét phế phẩm hoặc 80% giờ dừng máy để tập trung nguồn lực OE.
3. **[[Fishbone|Biểu đồ Xương Cá (Ishikawa 6M)]]:** Truy gốc rễ theo 6 nhóm: Man, Machine, Material, Method, Measurement, Mother Nature (Environment).
4. **[[Histogram]] (Biểu đồ tần suất):** Quan sát hình dạng phân bố đường kính/chiều dày bọc cáp (lệch trái/phải, 2 đỉnh do 2 ca vận hành khác chuẩn hoặc 2 lô hạt nhựa khác nhau).
5. **[[Scatter]] (Biểu đồ phân tán & Tương quan r):** Kiểm chứng mối quan hệ nhân quả, ví dụ: *Nhiệt độ vùng đầu đùn (X) vs Độ lệch tâm cách điện (Y)* hoặc *Tốc độ kéo (X) vs Tần suất đứt sợi (Y)*.
6. **Stratification (Phân tầng dữ liệu):** Tách dữ liệu theo Ca 1/Ca 2/Ca 3, theo Máy số 1/2/3, theo Nhà cung cấp hạt nhựa để không bị số trung bình đánh lừa.
7. **[[SPC|Control Chart (Biểu đồ kiểm soát Xbar-R / I-MR)]]:** Phát hiện xu hướng bất thường trước khi tạo phế phẩm.

- **Quy trình khóa chất lượng bền vững:** Chuyển yêu cầu khách hàng ([[VOC]] — ví dụ: "cáp ngầm chạy dự án không bị chạm chập, giao đúng tiến độ") thành thông số đo lường được ([[CTQ]] — ví dụ: `t_min ≥ 1.07 mm`, `Spark = 0`, `PD ≤ 5 pC`), vẽ sơ đồ tổng quan [[SIPOC]] (Supplier – Input – Process – Output – Customer) ở pha Define, đánh giá rủi ro bằng [[PFMEA]] và chốt phương pháp kiểm soát hàng ngày vào **[[Control Plan]]** (ghi rõ: thông số kiểm soát, tần suất đo, dụng cụ đo, biểu đồ SPC, và **Reaction Plan** khi vượt ngưỡng!).

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — AN TOÀN LAO ĐỘNG ([[EHS]] / [[LOTO]]) & BỘ TỨ CHUẨN [[ISO 9001|ISO]] NHÀ MÁY

### 3.1. Nguyên Tắc Bất Di Bất Dịch Của OE: "Không Tối Ưu Tốc Độ Đánh Đổi An Toàn (Safety First)!"
Trong nhà máy dây cáp điện, rủi ro tai nạn nghiêm trọng luôn rình rập: **cuốn kẹp cơ học** ở trống bện quay tốc độ cao / máy kéo dây, **bỏng nhiệt 180–220°C** ở đầu máy đùn & lò lưu hóa, **điện giật cao áp** ở [[Spark Tester]] (10–25 kV) và phòng thử [[Water Immersion]] / [[Partial Discharge|PD]], **va chạm xe nâng** chở rulo nặng 2–5 tấn.

- **Quy Trình Khóa & Gắn Thẻ An Toàn 6 Bước — [[LOTO]] (Lockout / Tagout):** Bắt buộc khi bảo trì, thay khuôn kéo, vệ sinh lưới lọc [[Screen Pack]], gỡ rối dây trong buồng máy bện:
  1. **Thông báo** cho toàn bộ nhân sự vận hành & giám sát ca trước khi tắt máy.
  2. **Tắt máy bình thường** bằng bảng điều khiển (không cắt cầu dao đột ngột khi đang tải nặng trừ trường hợp khẩn cấp).
  3. **Cô lập toàn bộ nguồn năng lượng** (điện 3 pha, khí nén, thủy lực, hơi nóng lò xông XLPE, thế năng rulo treo).
  4. **Gắn Khóa cá nhân (Lock) & Thẻ cảnh báo (Tag)** ghi rõ Tên – Bộ phận – Thời gian – Lý do lên từng điểm cô lập (nguyên tắc *"1 người – 1 khóa – 1 chìa"*).
  5. **Xả năng lượng tồn dư** (xả áp khí nén, xả tụ điện, chèn nêm chống lăn rulo, đợi đầu đùn nguội hoặc mang găng chống nhiệt).
  6. **Try-Out (Thử khởi động xác nhận Zero Energy):** Bấm nút Start xác nhận máy thực sự không chạy, sau đó trả công tắc về OFF rồi mới chạm tay vào vùng nguy hiểm!
- **Áp dụng OE vào [[EHS]]:** Mọi dự án [[SMED]] (rút ngắn thời gian thay khuôn) hoặc sửa Layout xưởng trên AutoCAD PHẢI qua bước đánh giá rủi ro an toàn (JSA / HIRA), tuyệt đối không tháo bỏ rào chắn liên động (Safety Interlock) hay cảm biến rèm quang để "chạy cho nhanh".

### 3.2. Bộ Tứ Tiêu Chuẩn Hệ Thống Quản Lý ISO Tại Nhà Máy CADIVI:
1. **[[ISO 9001]] (Hệ thống Quản lý Chất lượng — QMS):** Khung chuẩn hóa quy trình [[SOP]], kiểm soát thay đổi tài liệu, hiệu chuẩn thiết bị đo ([[Gage R&R]], thước đo Laser, cầu đo điện trở), xử lý sản phẩm không phù hợp (NCR) và hành động khắc phục phòng ngừa (CAPA / [[8D Report]]).
2. **[[ISO 14001]] (Hệ thống Quản lý Môi trường — EMS):** Kiểm soát thu gom và xử lý chất thải nguy hại đặc thù ngành cáp (dầu [[Drawing Emulsion|nhũ tương kéo sợi]] thải, bùn đồng, giẻ lau dính dầu, khói mùi nhựa PVC/XLPE, tiếng ồn xưởng bện) và tái chế phế liệu đồng/nhựa đúng quy định.
3. **[[ISO 45001]] (Hệ thống Quản lý An toàn & Sức khỏe Nghề nghiệp — OHSMS):** Nhận diện mối nguy (HIRA), kiểm soát [[LOTO]], thiết bị bảo hộ PPE (nút chống ồn > 85 dB khu kéo/bện, giày mũi thép, kính bảo hộ, găng chống nhiệt), điều tra sự cố suýt tai nạn (Near-Miss).
4. **[[ISO 50001]] (Hệ thống Quản lý Năng lượng — EnMS):** Rất "ăn điểm" với vị trí OE CADIVI! Tập trung xây dựng đường cơ sở năng lượng (EnB), chỉ số hiệu suất năng lượng (EnPI = `kWh / tấn cáp`), giám sát các điểm tiêu thụ trọng yếu SEU (máy kéo thô RBD, đầu đùn, Chiller, máy nén khí), lắp biến tần [[VFD]] và dịch chuyển phụ tải giờ thấp điểm!

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — KẾ TOÁN GIÁ THÀNH ĐỊNH MỨC ([[Standard Cost]]) & QUẢN TRỊ CHIẾN LƯỢC ([[Hoshin Kanri]] / [[ADKAR]])

### 4.1. Đọc Hiểu Báo Cáo Chênh Lệch Giá Thành ([[Standard Cost|Standard Cost Variance]]) Để Nói Chuyện Với Ban Giám Đốc & Tài Chính:
Chuyên viên OE giỏi không chỉ nói "giảm được 12 phút/ca" mà phải giải trình được trên bảng **Chênh lệch Giá thành Định mức vs Thực tế** của phòng Kế toán:

```text
TỔNG CHÊNH LỆCH GIÁ THÀNH = CHÊNH LỆCH NVL + CHÊNH LỆCH NHÂN CÔNG + CHÊNH LỆCH OVERHEAD
┌───────────────────────────────────┬───────────────────────────────────────────────────────┐
│ Loại Chênh Lệch (Variance)        │ Ai Chịu Trách Nhiệm & Đòn Bẩy Của OE Tại CADIVI?     │
├───────────────────────────────────┼───────────────────────────────────────────────────────┤
│ 1. Material Price Variance        │ (Giá mua thực - Giá chuẩn) × Lượng mua thực           │
│    (Biến động giá đồng LME/nhựa)  │ → Phòng Mua hàng (Purchasing) quản lý, KHÔNG phải OE. │
├───────────────────────────────────┼───────────────────────────────────────────────────────┤
│ 2. Material Usage / Yield Variance│ (Lượng dùng thực - Định mức BOM chuẩn) × Giá chuẩn    │
│    (Chênh lệch tiêu hao vật tư)   │ → TRỌNG TÂM #1 CỦA OE! (Copper Give-away, Over-thick, │
│                                   │   Scrap khởi động SMED, phế phẩm cắt đoạn Cut-Length) │
├───────────────────────────────────┼───────────────────────────────────────────────────────┤
│ 3. Labor Efficiency Variance      │ (Giờ công thực - Giờ công chuẩn) × Đơn giá giờ chuẩn  │
│    (Hiệu suất lao động OLE)       │ → TRỌNG TÂM #2 CỦA OE! (Cân bằng chuyền, giảm Motion, │
│                                   │   1 người đứng đa máy, giảm tăng ca do chờ vật tư)    │
├───────────────────────────────────┼───────────────────────────────────────────────────────┤
│ 4. Overhead Absorption Variance   │ Khấu hao máy + Điện nền + Lương gián tiếp / Sản lượng │
│    (Phân bổ định phí theo OEE)    │ → TRỌNG TÂM #3 CỦA OE! (Tăng OEE = Tăng mẫu số km cáp │
│                                   │   → Tự động kéo giảm giá thành đơn vị mỗi km cáp!)    │
└───────────────────────────────────┴───────────────────────────────────────────────────────┘
```

### 4.2. Triển Khai Chiến Lược Từ Ban Giám Đốc Xuống Xưởng ([[Hoshin Kanri]]) & Quản Trị Thay Đổi ([[ADKAR]]):
- **[[Hoshin Kanri]] (Policy Deployment — Triển khai chính sách qua Ma trận X-Matrix):**
  * Cầu nối liên kết **Mục tiêu 3–5 năm của Tổng Công ty CADIVI** (vd: giảm 8% giá thành chuyển đổi, nâng OEE trung bình lên 78%) → **Mục tiêu năm của Nhà máy Miền Trung** → **Các dự án OE ưu tiên hàng quý** (SMED đùn, SPC chống Over-thickness, số hóa báo cáo MES) → **KPI từng Phân xưởng/Tổ sản xuất** theo dõi trên bảng [[Visual Management]] (SQDCM: Safety – Quality – Delivery – Cost – Morale) hàng ngày!
- **Mô Hình Quản Trị Thay Đổi [[ADKAR]] (Khi Xưởng Phản Đối Cải Tiến):**
  * Thực tế 70% dự án OE thất bại không phải vì kỹ thuật sai mà vì **con người từ chối thay đổi** (công nhân sợ bị soi lỗi, sợ tăng định mức, tổ trưởng ngại đổi thói quen).
  * OE áp dụng 5 bước **ADKAR** để hóa giải tận gốc:
    1. **A — Awareness (Nhận thức):** Cho xưởng thấy rõ nỗi đau chung bằng số liệu thật tại [[Genba]] (vd: "đổi màu lâu 65 phút làm anh em phải tăng ca thứ Bảy, rất mệt!").
    2. **D — Desire (Mong muốn):** Giải quyết trước các bức xúc của công nhân (bố trí xe đẩy đồ nghề 5S, giảm bê vác nặng) để họ thấy cải tiến **giúp việc của chính họ nhẹ hơn**, không phải để cắt thưởng.
    3. **K — Knowledge (Kiến thức):** Đào tạo thực hành cầm tay chỉ việc tại máy (OJT), tài liệu trực quan 1 trang ([[SOP|OPL — One-Point Lesson]]) nhiều hình ảnh thay vì quy trình toàn chữ.
    4. **A — Ability (Năng lực):** Chạy thử nghiệm (Pilot) trên 1 máy đùn cùng tổ trưởng giỏi nhất, đo thời gian và ghi nhận thành tích chung của tổ.
    5. **R — Reinforcement (Củng cố):** Chuẩn hóa vào [[SOP]] & [[Control Plan]], thưởng nóng Kaizen minh bạch và kiểm tra duy trì ([[LPA|Layered Process Audit — LPA]]) định kỳ hàng tuần để không tái diễn thói quen cũ!
"""
    },

    "cable_extrusion_wire_forensics": {
        "title": "Cẩm Nang Công Nghệ Đùn Cáp Chuyên Sâu, Phân Tích Đứt Sợi Đồng & Các Dòng Cáp Đặc Chủng (Solar / Chống Nhiễu / Ngầm)",
        "summary": "Cẩm nang 4 tầng (Basic → Expert): Trục vít L/D & tỷ số nén (PVC vs XLPE/LSZH), áp suất/nhiệt độ nhựa nóng chảy (Melt Pressure/Temp), DDR/DRB chọn Chày-Cối, chẩn đoán 5 khuyết tật đùn (Sharkskin, Die Drool, Voids, Scorch), bài toán CaCO3/Specific Gravity & Regrind, phân loại mặt gãy đứt sợi (Cup-and-Cone vs Inclusion vs Weld Break) và công nghệ cáp Solar H1Z2Z2-K, bện lưới Braiding, băng chống thấm Water-Blocking & QCVN 4.",
        "category": "Sản Xuất (Manufacturing)",
        "content": r"""# 🔬 CẨM NANG CÔNG NGHỆ ĐÙN CÁP CHUYÊN SÂU, PHÂN TÍCH ĐỨT SỢI & CÁP ĐẶC CHỦNG CADIVI
*(Đào Sâu "Ruột Gan" Thiết Bị Đùn – Kéo Sợi & Các Dòng Sản Phẩm Biên Lợi Nhuận Cao Để Chinh Phục Hội Đồng Kỹ Thuật CADIVI)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — CẤU TẠO TRỤC VÍT ĐÙN ([[L/D Ratio]]) & GIÁM SÁT [[Melt Pressure|ÁP SUẤT – NHIỆT ĐỘ NÓNG CHẢY]]

### 1.1. Tại Sao Không Thể Dùng Chung 1 Trục Vít Cho Mọi Loại Nhựa Cáp?
Mỗi loại polymer ngành dây cáp điện có độ nhạy nhiệt và đặc tính lưu biến khác nhau hoàn toàn. Chuyên viên OE khi lập kế hoạch chuyển chuyền ([[RCCP]] / [[SMED]]) bắt buộc hiểu 3 thông số thiết kế trục vít trên máy [[Extruder]]:

```text
┌───────────────────┬───────────────┬────────────────┬────────────────────────┬─────────────────────────────┐
│ Loại Nhựa Cáp     │ Tỷ Lệ L/D     │ Tỷ Số Nén (CR) │ Nhiệt Độ Đùn Điển Hình │ Rủi Ro Nếu Dùng Sai Trục Vít│
├───────────────────┼───────────────┼────────────────┼────────────────────────┼─────────────────────────────┤
│ PVC (Cách điện/Vỏ)│ 20:1 – 24:1   │ 2.0 – 2.5 : 1  │ 150°C – 175°C          │ L/D quá dài → cháy xém HCl! │
│ PE / XLPE         │ 25:1 – 30:1   │ 2.8 – 3.5 : 1  │ 165°C – 210°C (PE)     │ Nén yếu → nhựa chưa tan đều │
│ (XLPE Silane/CCV) │ (Barrier)     │                │ 125°C – 140°C (Perox.) │ Quá nhiệt → đóng rắn sớm!   │
│ LSZH / HFFR       │ 22:1 – 25:1   │ 1.8 – 2.3 : 1  │ 140°C – 165°C          │ Lực cắt cao → phân hủy rộp! │
└───────────────────┴───────────────┴────────────────┴────────────────────────┴─────────────────────────────┘
```

### 1.2. Đọc "Nhịp Tim" Máy Đùn Qua [[Melt Pressure]] & Melt Temperature:
- **Áp suất nóng chảy (Melt Pressure):** Đo bằng cảm biến ngay trước tấm đột lỗ (Breaker Plate) và lưới lọc [[Screen Pack]].
  * Khi áp suất tăng từ từ +25–30% ở cùng vòng quay trục vít → Lưới lọc đang bẩn nghẹt, phải lên lịch thay vào cuối lệnh sản xuất trước khi rách lưới hoặc tụt lưu lượng.
  * Khi áp suất nhấp nhô chu kỳ (`±15 bar` — *Surging*) → Đường kính vỏ cáp trên [[Laser Gauge]] cũng dao động sóng sin khiến chỉ số [[Cpk]] sụt giảm mạnh!
- **Nhiệt độ khối nhựa thực (Melt Temperature):** Luôn cao hơn nhiệt độ hiển thị trên đồng hồ vỏ nòng Barrel `10–25°C` do **nhiệt ma sát cắt trượt (Shear Heating)** khi trục vít quay nhanh. Đừng bao giờ đẩy tốc độ trục vít lên quá giới hạn mà quên theo dõi Melt Temperature!

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — CHỌN BỘ CHÀY–CỐI ([[DDR|DDR / DRB]]) & CHẨN ĐOÁN 5 KHUYẾT TẬT ĐÙN KINH ĐIỂN

### 2.1. Đùn Ép (Pressure Tooling) vs Đùn Ống (Tube Tooling) & Công Thức [[DDR]] / DRB:
- **Đùn Ép (Pressure Tooling):** Đầu Chày (Tip) nằm thụt sâu bên trong Cối (Die); nhựa nóng chảy bị ép thẳng vào khe sợi đồng dưới áp suất cao → Bám dính chặt, điền đầy khe hở (thường dùng bọc vỏ điền đầy cáp nhiều lõi hoặc cáp chống thấm).
- **Đùn Ống (Tube Tooling — phổ biến nhất cho dây dân dụng & cách điện):** Đầu Chày nhô bằng miệng Cối tạo thành ống nhựa rồi kéo rút + hút chân không ôm sát lõi → Đều độ dày, dễ tuốt vỏ khi thợ điện đấu nối và đạt tốc độ mét/phút cao hơn nhiều!
- **Công thức chuẩn chọn bộ Chày–Cối đùn ống:**
  * `DDR (Draw-Down Ratio) = (D_die² - D_tip²) / (D_cable² - D_core²)` (PVC: `1.5–2.5`; PE/XLPE: `1.3–2.2`; LSZH: `1.2–1.8`).
  * `DRB (Draw-Ratio Balance) = (D_die / D_cable) / (D_tip / D_core)` (Chuẩn cân bằng tốt nhất: `0.95 – 1.08`).
  * **Lỗi OE hay gặp:** Công nhân lấy đại bộ cối rộng quá chuẩn (`DDR > 3.5`) vì ngại thay cối → Vỏ cáp chịu ứng suất kéo lớn, bị **co ngót đầu cáp**, **nứt khi thử uốn lạnh** và rò rỉ lượng nhựa [[Over-thickness]] cực lớn!

### 2.2. Ma Trận Chẩn Đoán Nhanh 5 Khuyết Tật Bề Mặt Đùn Cáp Tại Genba:

```text
┌───────────────────────┬───────────────────────────────────────┬───────────────────────────────────────┐
│ Khuyết Tật Đùn        │ Dấu Hiệu Nhận Diện & Nguyên Nhân Gốc  │ Giải Pháp Xử Lý Nhanh Tại Xưởng       │
├───────────────────────┼───────────────────────────────────────┼───────────────────────────────────────┤
│ 1. Sharkskin /        │ Bề mặt sần nhám mờ như da cá mập do   │ Tăng nhẹ nhiệt Die +5–10°C; kiểm tra  │
│    Melt Fracture      │ ứng suất cắt miệng cối quá cao khi    │ khe hở Die/DDR; dùng phụ gia trợ đùn  │
│    (Sần da cá mập)    │ ép chạy tốc độ quá nhanh              │ PPA 0.5%                              │
├───────────────────────┼───────────────────────────────────────┼───────────────────────────────────────┤
│ 2. Bambooing          │ Vỏ cáp gợn ngấn tròn đều như đốt tre  │ Kiểm tra bộ điều khiển tốc độ Capstan,│
│    (Gợn đốt tre)      │ do trượt Capstan hoặc áp suất Surging │ cân chỉnh vùng nhiệt cấp liệu Feed    │
├───────────────────────┼───────────────────────────────────────┼───────────────────────────────────────┤
│ 3. Die Drool          │ Nhựa/bột độn tích cục cháy ở mép cối  │ Sấy khô nhựa đủ giờ; giảm nhiệt cuối; │
│    (Đóng cặn mép cối) │ rồi rơi bám cục lên cáp gây lỗi Spark │ vát mép thoát 45° & mạ Chrome lòng cối│
├───────────────────────┼───────────────────────────────────────┼───────────────────────────────────────┤
│ 4. Voids / Blistering │ Rỗ bọt khí li ti bên trong hoặc phồng │ Sấy nhựa trên Hopper Dryer ≥ 2–4h;    │
│    (Rỗ bọt / phồng)   │ mặt vỏ do nhựa ẩm hoặc nhiệt quá cao  │ kiểm tra hút chân không & nhiệt nước  │
├───────────────────────┼───────────────────────────────────────┼───────────────────────────────────────┤
│ 5. Scorch / Pre-cure  │ Hạt lợn cợn vàng/nâu trong XLPE/PVC   │ Giảm nhiệt nòng & tốc độ trục vít;    │
│    (Cháy xém / đóng   │ do lưu nhiệt lâu ở vùng chết đầu đùn  │ làm sạch vùng chết Crosshead; không   │
│     rắn sớm)          │ hoặc dừng máy ngâm nhiệt quá lâu      │ để máy dừng ngâm nhựa > 15 phút!      │
└───────────────────────┴───────────────────────────────────────┴───────────────────────────────────────┘
```

### 2.3. Công Thức Nhựa ([[CaCO3 Filler]] & [[Specific Gravity]]) & Bài Toán Nhựa Tái Chế [[Regrind]]:
- **Bẫy kinh tế "Giá rẻ/kg nhưng Đắt/km":** Nhà cung cấp chào hạt PVC rẻ hơn `2%` theo đơn giá `VNĐ/kg` nhờ độn thêm bột đá `CaCO3`, nhưng làm [[Specific Gravity|tỷ trọng nhựa]] tăng từ `1.45` lên `1.54 g/cm³` (`+6.2%`) → Vì cáp bọc theo **thể tích (mm² × km)**, thực tế mỗi km cáp tiêu thụ nhiều kg nhựa hơn khiến **tổng chi phí/km lại ĐẮT HƠN gần 4%** và dễ rớt bài test cơ lý [[Tensile]]/[[Aging Oven]]!
- **Quản trị nhựa nghiền [[Regrind]]:**
  * **PVC nhiệt dẻo:** Có thể nghiền lại các đoạn xả đầu ca sạch, cùng màu (không dính đồng, không cháy đen) để pha tỷ lệ kiểm soát (vd: 5–15%) cho lớp độn trong hoặc vỏ ngoài nếu qua kiểm chứng Lab; giúp thu hồi giá trị ~18,000đ/kg thay vì bán phế bẩn 4,000đ/kg.
  * **XLPE đã lưu hóa:** Là nhựa nhiệt rắn, **KHÔNG THỂ** nấu chảy đùn lại làm cách điện → Bắt buộc tối ưu [[SMED]] & [[Purging]] để không phát sinh phế ngay từ đầu!

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — PHÂN TÍCH MẶT GÃY ĐỨT SỢI ĐỒNG ([[Wire Break Forensics]]) & IQC [[ASTM B49]]

Tại phân xưởng Kéo sợi ([[RBD]] / [[Multi-wire]]), mỗi lần đứt sợi mất 10–25 phút xỏ lại toàn bộ 16–24 cấp khuôn [[PCD]]. Chuyên viên OE phải biết **đọc mặt gãy dưới kính lúp/kính hiển vi** để khoanh vùng đúng chủ sở hữu sự cố:

```text
┌───────────────────────────┬──────────────────────────────────────┬───────────────────────────────────┐
│ Dạng Mặt Gãy Đầu Sợi      │ Nguyên Nhân Gốc Thực Sự              │ Bộ Phận Hành Động Khắc Phục       │
├───────────────────────────┼──────────────────────────────────────┼───────────────────────────────────┤
│ 1. Hình Chén–Côn          │ Vật liệu tốt nhưng lực căng vượt     │ Xưởng Kéo & Bảo trì: Kiểm tra     │
│    (Cup-and-Cone)         │ giới hạn bền kéo (khuôn mòn, kẹt     │ cấp khuôn PCD, vòi nhũ tương,     │
│                           │ Pay-off, thiếu bôi trơn nhũ tương)   │ độ trượt bánh kéo Capstan         │
├───────────────────────────┼──────────────────────────────────────┼───────────────────────────────────┤
│ 2. Gãy Dẹt Có Hạt Lạ /    │ Tạp chất oxit, xỉ sắt hoặc vảy gấp   │ Phòng Mua Hàng & IQC: Đối chiếu   │
│    Vảy Gấp (Inclusion /   │ trên thanh đồng Rod 8mm đầu vào      │ COA chuẩn ASTM B49, lập 8D khiếu  │
│    Sliver / Lap)          │ (lỗi luyện đúc từ nhà cung cấp)      │ nại & phong tỏa lô đồng Rod lỗi   │
├───────────────────────────┼──────────────────────────────────────┼───────────────────────────────────┤
│ 3. Gãy Phẳng Giòn Tại     │ Mối hàn đối đầu (Butt Weld) bị lệch  │ Xưởng Kéo: Hiệu chuẩn lại dòng    │
│    Mối Hàn (Weld Break)   │ tâm, rỗ bọt hoặc quên bước ủ mềm     │ điện hàn & thời gian ủ lại mối    │
│                           │ (Post-anneal) ngay sau khi hàn       │ hàn trên Butt Welder (SOP/OPL)    │
├───────────────────────────┼──────────────────────────────────────┼───────────────────────────────────┤
│ 4. Gãy V hình Mũi Tên     │ Rạn nứt từ lõi sợi do góc côn khuôn  │ Phòng Kỹ Thuật & Khuôn: Mài lại   │
│    (Central Burst /       │ quá lớn (> 20°) hoặc giảm tiết diện  │ đúng góc côn 16–18° cho đồng và   │
│    Chevron)               │ một bước quá đột ngột                │ cân bằng lại bảng thứ tự khuôn    │
└───────────────────────────┴──────────────────────────────────────┴───────────────────────────────────┘
```
- **Kết nối dữ liệu [[ASTM B49]] (IQC) với [[MES]]:** Gắn mã lô đồng Rod đầu vào vào lệnh kéo trên MES để cuối tháng chạy [[ANOVA]] / [[Pareto]] so sánh tỷ lệ `số lần đứt sợi / tấn đồng` và `% [[IACS]]` giữa các nhà cung cấp!

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — CÁC DÒNG CÁP GIÁ TRỊ CAO CỦA CADIVI & RÀNG BUỘC PHÁP LÝ [[QCVN 4]]

### 4.1. 3 Dòng Sản Phẩm Chuyên Dụng Biên Lợi Nhuận Cao & Trọng Tâm Tối Ưu OE:
1. **Cáp Năng Lượng Mặt Trời [[Solar Cable|Solar PV H1Z2Z2-K]] (EN 50618 / IEC 62930 — 1,500V DC):**
   - Cấu tạo: Ruột đồng mềm Class 5 mạ thiếc ([[Tinned Copper]]) + Cách điện & Vỏ kép XLPO chịu tia UV/Ozone 25 năm, liên kết ngang bằng công nghệ [[E-beam|chiếu xạ chùm tia điện tử]] hoặc Silane đặc chủng.
   - **Điểm đánh OE:** Thay puly dẫn bằng gốm chống xước lớp mạ thiếc; lập lịch gom đơn (`Campaign Scheduling`) theo màu Đỏ/Đen giảm phế XLPO đắt tiền; tối ưu tải rulo khi chuyển đi chiếu xạ [[E-beam]] để cắt giảm chi phí chiếu xạ & [[Lead Time]].
2. **Cáp Điều Khiển & Chống Nhiễu (`DVV/Sc`, `CVV/Sc`) — Công Đoạn [[Braiding|Bện Lưới / Quấn Băng Đồng]]:**
   - Máy bện lưới (16–24 suốt sợi đồng nhỏ) chạy tốc độ rất chậm (`2–8 m/phút`) nên cực dễ tạo cổ chai.
   - **Điểm đánh OE:** Áp dụng [[Man-Machine Chart]] cho 1 công nhân vận hành 4–8 máy; chuẩn hóa đánh suốt đồng đều chiều dài trên máy Rewinder để thay trọn bộ [[Kitting|Kit 24 suốt]] trong 1 lần dừng thay vì dừng lẻ tẻ 16 lần/ca; gắn cảm biến đứt sợi [[Poka-Yoke]].
3. **Cáp Ngầm Chống Thấm Dọc Với [[Water-Blocking|Băng/Sợi Trương Nở Water-Blocking]]:**
   - Băng chứa bột siêu thấm SAP cực kỳ kỵ ẩm → OE kiểm soát tủ bảo quản kín (`< 50% RH`), quản lý [[FIFO]], kiểm soát chặt độ chồng mí (`Overlap 15–25%`) theo [[BOM]] và cảm biến đứt băng dừng máy tức thì.

### 4.2. Đường Biên Pháp Lý Tuyệt Đối — [[QCVN 4]] (Dấu Hợp Quy CR) & [[MOC / ECN]]:
- Khi triển khai bất kỳ cải tiến giảm [[Copper Give-away]] hay giảm [[Over-thickness]] trên dây dân dụng (`VC`, `VCm`, `VCmd`, `VCmt`), OE phải nhớ **[[QCVN 4]]** là quy chuẩn quốc gia BẮT BUỘC: luôn khóa giới hạn kiểm soát nội bộ cao hơn ngưỡng tối thiểu QCVN 4 ít nhất `3σ` và bắt buộc chạy đủ 5 bước **[[MOC / ECN]]** (Đề xuất → Đánh giá rủi ro liên phòng ban → Pilot Trial & test Lab → Phê duyệt → Cập nhật đồng bộ SOP, Control Plan & MBOM trên ERP)!
"""
    },

    "oe_field_execution_case_test": {
        "title": "Cẩm Nang Thực Địa OE (Work Sampling, Loss Tree WCM, LSW/LPA, Bảo Trì) & Bộ 3 Đề Thi Thực Hành Vòng 2 CADIVI",
        "summary": "Cẩm nang 4 tầng (Basic → Expert): Đo năng suất bằng Work Sampling (Tippett), Cây tổn thất OEE Waterfall & Cost Deployment (WCM), Hệ thống duy trì bền vững LSW + LPA + Andon Escalation Matrix (SLA), Đường cong học việc Learning Curve, KPI Bảo trì (PM Compliance, Wrench Time, CBM/PdM), Định biên 3 ca 4 kíp & 3 Đề thi thực hành Vòng 2 OE CADIVI kèm lời giải chi tiết.",
        "category": "Sản Xuất (Manufacturing)",
        "content": r"""# 🎯 CẨM NANG THỰC ĐỊA OE (WORK SAMPLING, WCM, LSW/LPA) & BỘ 3 ĐỀ THI THỰC HÀNH VÒNG 2 CADIVI
*(Từ Công Cụ Đo Đạc Hiện Trường Của Chuyên Gia Đến Bộ Đề Test Thực Chiến Phỏng Vấn Vòng 2 Có Lời Giải Chi Tiết)*

---

## 1. TẦNG 1: CƠ BẢN (BASIC) — ĐO NĂNG SUẤT KHÔNG CẦN BẤM GIỜ LIÊN TỤC BẰNG [[Work Sampling]] & ĐỊNH BIÊN [[Headcount Planning|3 CA 4 KÍP]]

### 1.1. Khi Nào Dùng [[Work Sampling]] (Lấy Mẫu Công Việc — Tippett) Thay Cho [[Time Study]]?
- **Time Study (bấm giờ đồng hồ):** Hợp với thao tác lặp chu kỳ ngắn 10–120 giây (như tổ Đóng cuộn khoanh 100m, đo Canon INEX).
- **Work Sampling (chụp mẫu ngẫu nhiên):** Vũ khí số 1 cho công việc chu kỳ dài/phi chu kỳ tại nhà máy cáp: **công nhân đứng 3 máy bện, tài xế xe nâng chở rulo, đội bảo trì cơ điện, nhân viên kho**. Bạn chỉ cần đi dọc tuyến theo các mốc phút ngẫu nhiên và tích chọn trạng thái tại đúng tích tắc nhìn thấy (Đang chạy/làm việc VA · Đổi mã/Cài đặt · Chờ vật tư/rulo · Đi tìm đồ · Nghỉ/Vắng mặt).

```text
CÔNG THỨC TÍNH CỠ MẪU WORK SAMPLING (Độ tin cậy 95% → Z = 1.96):
         Z² × p × (1 - p)
  N  =  ──────────────────
                e²
Ví dụ tại CADIVI Miền Trung: Khảo sát 4 tài xế xe nâng kho rulo & xưởng Đùn.
  • Ước lượng sơ bộ tỷ lệ thời gian chờ/chạy rỗng: p = 0.30 (30%).
  • Độ chính xác mong muốn: sai số tuyệt đối e = ±0.03 (±3%).
  • N = (1.96² × 0.30 × 0.70) / 0.03² = 0.8067 / 0.0009 = 897 lượt quan sát!
  • Với 4 xe nâng: 897 / 4 ≈ 225 lượt đi qua tuyến trong 5 ngày (chỉ ~45 lượt/ngày, mỗi lượt 2 phút!).
```

### 1.2. Bài Toán Định Biên Nhân Sự ([[Headcount Planning]]) & Mô Hình 3 Ca – 4 Kíp Theo Luật Lao Động VN:
- **Tránh bẫy tính thiếu người:** Luôn nhân hệ số dự phòng nghỉ phép/ốm đau (`Absenteeism 6–8%`) và chia cho hiệu suất thực [[OLE]], đồng thời tôn trọng trần tăng ca Luật Lao động Việt Nam (**≤ 40 giờ/tháng** và **≤ 200 giờ/năm**, tối đa **300 giờ/năm** với ngành sản xuất đặc thù).
- **Khi chạy liên tục 24/7** cho lò [[CCV]] hoặc dây chuyền Đùn cao điểm: áp dụng **3 Ca – 4 Kíp** (3 kíp luân phiên chạy 8h/ca, 1 kíp nghỉ xoay vòng) giúp máy chạy 168 giờ/tuần mà không vi phạm giờ làm thêm!
- **Dự báo năng suất công nhân mới bằng [[Learning Curve|Đường cong học việc 80%]]:** `Y_n = Y_1 × n^(-0.3219)` giúp phòng Kế hoạch biết tuần 1 công nhân mới chỉ đạt ~65–70% tốc độ chuẩn và sẽ chạm 95% sau 3–4 tuần đào tạo [[TWI]].

---

## 2. TẦNG 2: TRUNG CẤP (INTERMEDIATE) — CÂY TỔN THẤT [[Loss Tree]] & [[Cost Deployment]] (WCM)

Muốn Giám đốc Nhà máy CADIVI duyệt dự án OE ngay trong 5 phút, đừng chỉ trình bày phần trăm % — hãy dịch mọi phút dừng máy và kg phế thành **Thác nước Tổn thất Bằng Tiền (VNĐ/tháng)**:

```text
VÍ DỤ BẢNG COST DEPLOYMENT (WCM) QUÝ 1 — NHÀ MÁY DÂY CÁP ĐIỆN (MÔ PHỎNG):
┌────┬───────────────────────────────────┬──────────────────────────┬──────────────┬───────────┐
│ STT│ Nhóm Tổn Thất Tại Xưởng           │ Quy Đổi Dữ Liệu Gốc      │ Thiệt Hại/Th │ Ưu Tiên   │
├────┼───────────────────────────────────┼──────────────────────────┼──────────────┼───────────┤
│ 1  │ Over-thickness nhựa bọc XLPE/PVC  │ Dư trung bình +0.07 mm   │  195 triệu   │ #1 (Đánh  │
│    │ (SPC tâm dịch cao vì sợ mỏng)     │ trên 180 tấn nhựa/tháng  │  VNĐ / tháng │  ngay!)   │
├────┼───────────────────────────────────┼──────────────────────────┼──────────────┼───────────┤
│ 2  │ Copper Give-away (Dư đường kính   │ Dư +0.008 mm trên        │  165 triệu   │ #2 (Đánh  │
│    │ đồng so chuẩn điện trở IEC 60228) │ 220 tấn đồng kéo/tháng   │  VNĐ / tháng │  ngay!)   │
├────┼───────────────────────────────────┼──────────────────────────┼──────────────┼───────────┤
│ 3  │ Phế đồng dính nhựa & Purge khi    │ 48 lần đổi mã/tháng ×    │  110 triệu   │ #3 (SMED +│
│    │ chuyển đổi mã/màu máy đùn         │ 140m dây phế + 20kg nhựa │  VNĐ / tháng │  ColorSeq)│
├────┼───────────────────────────────────┼──────────────────────────┼──────────────┼───────────┤
│ 4  │ Đứt sợi máy kéo RBD/Multi-wire &  │ 65 giờ dừng cổ chai/tháng│   85 triệu   │ #4 (Khuôn │
│    │ mất công suất giờ máy (OEE Loss)  │ × chi phí cơ hội/giờ     │  VNĐ / tháng │  PCD/IQC) │
├────┼───────────────────────────────────┼──────────────────────────┼──────────────┼───────────┤
│ 5  │ Rò rỉ khí nén & đùn chờ nhiệt     │ 11,000 kWh thừa/tháng    │   24 triệu   │ #5 (Quick │
│    │ không tải (ISO 50001)             │ × 2,200đ/kWh             │  VNĐ / tháng │  Win)     │
└────┴───────────────────────────────────┴──────────────────────────┴──────────────┴───────────┘
```

---

## 3. TẦNG 3: NÂNG CAO (ADVANCED) — HỆ THỐNG DUY TRÌ BỀN VỮNG ([[LSW]], [[LPA]], [[Escalation Matrix]]) & KPI BẢO TRÌ

### 3.1. Bộ Ba Chống "Tái Nghiện Thói Quen Cũ" Sau Khi Kết Thúc Dự Án Kaizen:
1. **[[LSW]] (Leader Standard Work — Công việc chuẩn của Quản lý):**
   - Tổ trưởng (80% chuẩn hóa): Đầu ca họp 5 phút tại bảng SQDCM (Tier 1) → Kiểm tra đủ 5S, [[LOTO]], mẫu test [[Spark Tester]], tủ sấy Tip/Die cho lệnh kế tiếp → Cập nhật sản lượng theo giờ (`Hour-by-Hour Board`).
   - Quản đốc & OE (50% chuẩn hóa): Đi Genba Walk kiểm tra điểm đỏ (Tier 2) lúc 09:00 hàng ngày, gỡ điểm nghẽn liên phòng ban trong 24 giờ.
2. **[[LPA]] (Layered Process Audit — Kiểm tra phân tầng 3 cấp):**
   - Tầng 1 (Tổ trưởng — hàng ngày), Tầng 2 (Quản đốc / OE / QA — hàng tuần), Tầng 3 (Giám đốc nhà máy — 2 tuần/lần) cùng dùng 1 bảng câu hỏi ngắn 8–10 mục Có/Không đi thẳng xuống máy.
3. **[[Escalation Matrix]] (Ma trận leo thang sự cố có SLA thời gian):**
   - `0–5 phút dừng`: Tổ trưởng có mặt xử lý → `5–15 phút`: Bảo trì/Kỹ thuật tiếp ứng → `15–30 phút`: Quản đốc & OE điều phối → `> 60 phút` hoặc lỗi lô lớn/an toàn: Giám đốc Nhà máy trực tiếp chỉ đạo!

### 3.2. Bộ 3 KPI Bảo Trì OE Cần Phối Hợp Chặt Với Phòng Cơ Điện:
- **[[PM Compliance]] ≥ 90%:** Khóa khung giờ giao máy bảo trì cố định trên lịch [[MPS]]/[[CRP]] để không "nợ PM" dẫn tới nổ hỏng nặng giữa ca.
- **[[Wrench Time]] (từ ~30% → 50%+):** Dùng [[Work Sampling]] phát hiện thợ bảo trì tốn 40% thời gian đi tìm phụ tùng → Tổ chức tủ phụ tùng 5S + [[Kitting]] vật tư trước giờ bảo trì.
- **[[CBM / PdM]] (Bảo trì dự đoán):** Camera nhiệt ảnh soi tủ điện/đầu đùn, bút đo rung vòng bi máy kéo/bện, siêu âm rò khí nén và theo dõi đồ thị [[Melt Pressure]] trên [[MES]]!

---

## 4. TẦNG 4: CHUYÊN GIA (EXPERT) — BỘ 3 ĐỀ THI THỰC HÀNH PHỎNG VẤN VÒNG 2 OE CADIVI (CÓ LỜI GIẢI CHI TIẾT)

### ĐỀ THI 1 (BÀI TEST EXCEL / DATA — 45 PHÚT): PHÂN TÍCH NHẬT KÝ 5 CA MÁY ĐÙN BỌC CÁP PVC
**Đề bài:** Cho bảng nhật ký 5 ca liên tiếp của Máy Đùn số 2 chạy dây `VC 2.5 mm²` (Ca chuẩn `480p`, nghỉ kế hoạch `30p/ca` → `450p/ca`; tốc độ định mức `320 m/phút`; định mức BOM chuẩn: đồng `22.2 kg/km`, nhựa PVC `12.5 kg/km`; đơn giá đồng `250,000đ/kg`, nhựa PVC `28,000đ/kg`):

```text
┌─────┬──────────┬──────────┬──────────┬──────────┬──────────┬───────────┬──────────┬──────────┐
│ Ca  │ Dừng Đổi │ Dừng Sự  │ Dừng Khác│ Tổng Mét │ Phế Cắt  │ Đồng Xuất │ Nhựa Xuất│ Ghi Chú  │
│     │ Màu (ph) │ Cố (ph)  │ (ph)     │ Đùn (m)  │ Bỏ (m)   │ Thực (kg) │ Thực (kg)│          │
├─────┼──────────┼──────────┼──────────┼──────────┼──────────┼───────────┼──────────┼──────────┤
│ Ca 1│    45    │    15    │    10    │ 102,000  │   3,200  │   2,305   │   1,385  │ Đen→Trắng│
│ Ca 2│    15    │    25    │     5    │ 116,000  │   2,000  │   2,600   │   1,520  │ Hỏng bơm │
│ Ca 3│    50    │    10    │    10    │ 100,000  │   3,800  │   2,270   │   1,365  │ Đen→Vàng │
│ Ca 4│    10    │     0    │    10    │ 125,000  │   1,500  │   2,795   │   1,610  │ Trắng→Đỏ │
│ Ca 5│    40    │    20    │    10    │ 105,000  │   3,500  │   2,380   │   1,420  │ Xanh→Trắ │
├─────┼──────────┼──────────┼──────────┼──────────┼──────────┼───────────┼──────────┼──────────┤
│TỔNG │   160    │    70    │    45    │ 548,000  │  14,000  │  12,350   │   7,300  │ 5 Ca     │
└─────┴──────────┴──────────┴──────────┴──────────┴──────────┴───────────┴──────────┴──────────┘
```

**Lời giải mẫu ghi điểm tuyệt đối (kèm tư duy công thức Excel):**
1. **Tính OEE tổng 5 ca:**
   - `Planned Time = 5 × 450 = 2,250 phút`; `Total Downtime = 160 + 70 + 45 = 275 phút` → `Operating Time = 1,975 phút`.
   - `Availability (A) = 1,975 / 2,250 = 87.78%`.
   - `Performance (P) = 548,000 / (1,975 × 320) = 548,000 / 632,000 = 86.71%` (tốc độ thực bình quân chỉ `277.5 m/phút` so với chuẩn `320`).
   - `Good Length = 548,000 - 14,000 = 534,000 m = 534.0 km` → `Quality (Q) = 534,000 / 548,000 = 97.45%`.
   - **`OEE = 87.78% × 86.71% × 97.45% = 74.16%`**.
   - *Công thức Excel nhanh:* Dùng `SUMIFS` gom Downtime theo Mã lý do; dùng `Power Query` tự gộp file nhiều ca; tính OEE trên tổng thời gian/sản lượng (KHÔNG lấy `AVERAGE` của 5 OEE lẻ!).
2. **Phân tích Pareto Downtime:** Đổi màu chiếm `160 / 275 = 58.2%` tổng dừng máy — đặc biệt rơi đúng vào 3 ca đổi màu ngược **Tối → Sáng** (Ca 1, 3, 5 mất 40–50p/lần so với Ca 4 Sáng → Tối chỉ 10p!).
3. **Tính BOM Variance (so với sản lượng Đạt `534.0 km`):**
   - Đồng chuẩn cho `534 km` = `534 × 22.2 = 11,854.8 kg`. Thực xuất `12,350 kg` → **Vượt định mức `+495.2 kg`** (trong đó phế cắt `14 km ≈ 310.8 kg` đồng dính nhựa, còn lại `+184.4 kg ≈ +1.5%` là **[[Copper Give-away]]**!). Thiệt hại gộp trước thu hồi phế: `495.2 × 250,000 = 123.8 triệu VNĐ` chỉ trong 5 ca!
   - Nhựa PVC chuẩn cho `534 km` = `534 × 12.5 = 6,675.0 kg`. Thực xuất `7,300 kg` → **Vượt định mức `+625.0 kg`** (trong đó `14 km` phế ≈ `175 kg`, còn lại `+450 kg ≈ +6.6%` là **[[Over-thickness]] + Purge Scrap**!). Thiệt hại nhựa: `625 × 28,000 = 17.5 triệu VNĐ`.
4. **3 Hành động ưu tiên đề xuất Ban Giám Đốc:** (1) Đảo lịch chạy theo [[Color Sequencing]] Sáng → Tối + sấy sẵn Tip/Die ([[SMED]]) để kéo đổi màu từ 45p về 12p; (2) Kiểm tra [[SPC]] đường kính đồng đầu vào và chiều dày Laser Gauge chặn ngay `+1.5%` dư đồng & `+6.6%` dư nhựa; (3) Kiểm tra nước làm mát/tốc độ [[Capstan]] kéo tốc độ từ `277.5` về `305+ m/phút`.

---

### ĐỀ THI 2 (CASE STUDY ĐIỀU ĐỘ & NĂNG LỰC — 30 PHÚT): ĐƠN HÀNG GẤP CÁP CXV & ABC TĂNG +35%
**Đề bài:** Tháng tới đơn hàng dự án điện lực tăng đột biến `+35%`, đẩy tải dự báo lên: Xưởng Kéo `82%`, Xưởng Bện `91%`, **Xưởng Đùn `122%` (thiếu 210 giờ chạy máy ròng)**, Xưởng Đóng gói `85%`. Không được mua thêm máy mới và không vượt trần tăng ca `40 giờ/người/tháng`. Bạn lập phương án giải cứu thế nào?

**Khung trả lời chuẩn OE (5 bước chốt hạ):**
1. **Áp dụng [[TOC]] (Không giải cứu dàn trải):** Khóa cổ chai duy nhất là Xưởng Đùn (`122%`). Tuyệt đối không tăng ca Xưởng Kéo/Đóng gói để tránh tạo núi [[WIP]].
2. **Khai thác tại chỗ (Exploit — tăng ngay ~130 giờ ròng không tốn nhân công):** Áp dụng [[Color Sequencing]] + gom đơn cùng tiết diện (`Campaign Scheduling`) giảm 50% số lần đổi mã + cắt thời gian đổi mã bằng [[SMED]] → Nâng OEE máy đùn từ `66% → 75%` (+13.6% công suất ròng).
3. **Mở rộng ca cục bộ đúng luật ([[Headcount Planning]]):** Điều chuyển tạm 4 công nhân đa kỹ năng từ Xưởng Kéo (đang dư 18% tải) kết hợp tuyển thời vụ khu Đóng gói đơn giản để mở **Ca 3 cục bộ cho riêng 2 máy Đùn chủ lực trong 3 tuần** (3 ca – 4 kíp luân phiên, tăng ca từng người giữ `≤ 32 giờ/tháng` dưới trần 40 giờ!).
4. **Bảo vệ cổ chai bằng Buffer & [[PM Compliance]]:** Thiết lập vùng đệm 1 ca bán thành phẩm rulo đồng bện trước máy Đùn (không bao giờ để máy Đùn đói hàng); bố trí thợ bảo trì trực sẵn theo [[Escalation Matrix]] SLA 5 phút.
5. **Theo dõi hàng ngày (Tier 2):** Báo cáo tiến độ giờ máy thực vs kế hoạch lúc 09:00 mỗi sáng để điều chỉnh kịp thời nếu phát sinh đơn chen ngang.

---

### ĐỀ THI 3 (THUYẾT TRÌNH A3 & PHẢN BIỆN ROI — 15 PHÚT): BẢO VỆ ĐẦU TƯ LASER GAUGE CLOSED-LOOP
**Tình huống:** Giám đốc hỏi: *"Bộ đo đường kính Laser Closed-loop giá 420 triệu VNĐ — Kế toán trưởng bảo đắt quá, em chứng minh sao để anh ký duyệt?"*

**Cấu trúc phản biện sắc bén (4 điểm ăn trọn lòng tin lãnh đạo):**
1. **Tách rạch ròi Hard Savings (tiền tươi Kế toán kiểm chứng được):** Không tính các lợi ích mơ hồ; chỉ lấy dữ liệu [[SPC]] đo thực tế 30 ngày tại máy đùn đang dư bình quân `+0.06 mm` nhựa vỏ (do công nhân phải chỉnh dày để né lỗi mỏng khi đo tay 30 phút/lần). Với sản lượng `120 tấn nhựa/tháng` × tiết kiệm thận trọng `2.5%` = `3.0 tấn/tháng` × `32 triệu/tấn` = **96 triệu VNĐ/tháng** (chưa kể giảm 40% phế khởi động đầu ca!).
2. **Trình bày 3 kịch bản độ nhạy (Sensitivity Analysis):**
   - *Kịch bản Thận trọng (chỉ tiết kiệm 1.5% = 57.6 tr/tháng):* Payback = `420 / 57.6 = 7.3 tháng`.
   - *Kịch bản Cơ sở (2.5% = 96.0 tr/tháng):* Payback = `4.4 tháng`.
   - *Kịch bản Lạc quan (3.2% + giảm phế đầu ca = 135 tr/tháng):* Payback = `3.1 tháng`.
3. **Cam kết Pilot 1 máy trước khi nhân rộng:** Xin phê duyệt lắp thử **1 bộ trên máy đùn sản lượng lớn nhất**, chốt trước phương pháp đo kiểm Trước–Sau với Phòng Kế toán & QA (dùng [[2-Sample t-test]] kiểm chứng `p-value < 0.05` sau 30 ngày) — đạt cam kết mới trình mua tiếp cho các máy còn lại!
4. **Liên hệ trải nghiệm thật (trung thực số liệu):** Chia sẻ tư duy đánh giá đầu tư thiết bị đo tự động bạn đã làm thực tế tại Mabuchi (so sánh Time Study đo tay 60s → tự động 30s, tính rõ chi phí đầu tư, vận hành và điều kiện giả định thay vì đưa con số phóng đại).
"""
    },

    "python_core": {
        "title": "Cẩm Nang Lập Trình Python Chuyên Sâu & Tối Ưu Hiệu Năng",
        "category": "Lập Trình & Công Nghệ (Backend)",
        "summary": "Chi tiết kiến trúc CPython, cơ chế GIL, xử lý CPU-bound vs IO-bound, quản lý bộ nhớ, Data Structures O(1), Type Hinting và Design Patterns.",
        "content": """# CẨM NANG LẬP TRÌNH PYTHON CHUYÊN SÂU & TỐI ƯU HIỆU NĂNG

---

## 1. BẢN CHẤT KIẾN TRÚC CPYTHON & CƠ CHẾ GIL
- **GIL (Global Interpreter Lock)**: Là cơ chế khóa loại trừ tương hỗ (Mutex) được thiết kế bên trong CPython nhằm ngăn chặn nhiều luồng (threads) thực thi bytecode Python cùng một lúc.
- **Tại sao CPython cần GIL?**: Quản lý bộ nhớ của Python dựa trên cơ chế đếm tham chiếu (Reference Counting). Nếu không có GIL, các race conditions có thể dẫn đến rò rỉ bộ nhớ hoặc thu hồi sai đối tượng đang dùng.
- **Xử lý Tác Vụ IO-bound vs CPU-bound**:
  * **IO-bound (Gọi API, Đọc/Ghi File, Truy vấn CSDL)**: Sử dụng `asyncio` (Event Loop đơn luồng bất đồng bộ) hoặc `threading.Thread`. Khi chờ I/O, Python tự động nhả GIL để luồng khác chạy.
  * **CPU-bound (Tính toán khoa học, Mã hóa, Xử lý ảnh, Phân tích dữ liệu lớn)**: BẮT BUỘC dùng `multiprocessing.Process` hoặc `concurrent.futures.ProcessPoolExecutor` để tạo các tiến trình con độc lập với GIL riêng và tận dụng toàn bộ số nhân CPU.

---

## 2. CẤU TRÚC DỮ LIỆU & ĐỘ PHỨC TẠP THỜI GIAN
- **List vs Tuple**:
  * `list`: Mảng động (Dynamic Array), có thể thay đổi (mutable), chi phí cấp phát bộ nhớ dự phòng (over-allocation). Thao tác `append` đạt O(1) khấu hao, chèn `insert(0, x)` là O(n).
  * `tuple`: Bất biến (immutable), kích thước cố định, tiêu tốn ít RAM hơn list ~20%, tối ưu hóa trong bộ nhớ CPython (tuple caching).
- **Dict & Set (Bảng băm - Hash Table)**:
  * Truy xuất `d[key]` và kiểm tra `x in s` đạt trung bình O(1).
  * Điều kiện: `key` phải là đối tượng băm được (hashable) và triển khai cả hai phương thức `__hash__()` và `__eq__()`.

---

## 3. ASYNCIO & CLEAN ARCHITECTURE BEST PRACTICES
1. **Tuyệt đối không chạy hàm blocking trong coroutine**: Không dùng `time.sleep()` hay gọi thư viện `requests` đồng bộ trong hàm `async def` vì sẽ làm nghẽn toàn bộ Event Loop. Thay vào đó, dùng `asyncio.sleep()` và `httpx.AsyncClient` hoặc bọc trong `asyncio.to_thread()`.
2. **Context Managers (`with` & `async with`)**: Luôn sử dụng để tự động đóng tài nguyên mạng, DB connection pool và file descriptors an toàn chống leak.
3. **Type Hinting & Mypy**: Sử dụng type annotations đầy đủ (`from typing import Optional, List, Dict, Union`) giúp phát hiện lỗi kiểu dữ liệu trước khi chạy runtime.
"""
    },
    "react_fe": {
        "title": "Cẩm Nang Kiến Trúc React 18+ & Modern Frontend Engineering",
        "category": "Lập Trình & Công Nghệ (Frontend)",
        "summary": "Làm chủ Virtual DOM, Thuật toán Reconciliation, Custom Hooks, useMemo/useCallback trade-offs, Concurrent Mode và kiến trúc ứng dụng web.",
        "content": """# CẨM NANG KIẾN TRÚC REACT 18+ & MODERN FRONTEND ENGINEERING

---

## 1. VIRTUAL DOM & THUẬT TOÁN RECONCILIATION
- **Bản chất Virtual DOM**: Là một cây đối tượng JavaScript thuần túy mô phỏng cấu trúc của Real DOM thực tế trong trình duyệt.
- **Cơ chế Diffing Heuristics (O(n) thay vì O(n³))**:
  1. Hai phần tử khác kiểu (ví dụ `<div>` đổi thành `<span>`): React sẽ hủy bỏ toàn bộ cây cũ và dựng lại cây mới.
  2. Hai phần tử cùng kiểu: React chỉ so sánh và cập nhật các thuộc tính (attributes/classes) bị thay đổi.
  3. Xử lý danh sách con bằng `key`: Khóa `key` duy nhất và ổn định giúp React nhận diện chính xác phần tử nào bị thêm, xóa hoặc dịch chuyển. **Tuyệt đối không dùng index của mảng làm key** nếu danh sách có phân trang, lọc hoặc xóa phần tử.

---

## 2. QUY TẮC VÀNG VỀ HOOKS & CLOSURE TRAP
- **2 Quy tắc bắt buộc**:
  1. Chỉ gọi Hooks ở cấp cao nhất (Top-level) của Functional Component, không gọi trong vòng lặp `for`, câu lệnh điều kiện `if` hoặc hàm lồng nhau.
  2. Chỉ gọi Hooks từ React Function Components hoặc Custom Hooks.
- **Stale Closure Trap trong `useEffect`**:
  * Xảy ra khi hàm effect tham chiếu đến biến state cũ do mảng dependencies `[]` khai báo thiếu biến đó.
  * Giải pháp: Sử dụng Functional State Update `setCount(prev => prev + 1)` hoặc bổ sung đầy đủ dependencies.

---

## 3. TỐI ƯU HIỆU NĂNG: KHI NÀO DÙNG `useMemo` & `useCallback`?
- **useCallback**: Ghi nhớ tham chiếu hàm (function reference) giữa các lần render. Chỉ có ý nghĩa khi truyền hàm đó xuống component con đã được bọc `React.memo(ChildComponent)`.
- **useMemo**: Ghi nhớ kết quả tính toán phức tạp (CPU-intensive). Không lạm dụng cho các phép toán đơn giản vì chi phí khởi tạo memoization closure tốn kém hơn phép tính cơ bản.
- **Concurrent Mode & `useTransition`**: Đánh dấu các cập nhật state thứ cấp (ví dụ: gõ tìm kiếm lọc danh sách 1,000 mục) là non-urgent để trình duyệt không bị đơ giật khung hình khi người dùng gõ phím.
"""
    },
    "docker_devops": {
        "title": "Cẩm Nang Docker & Containerization Thực Chiến",
        "category": "Hạ Tầng & DevOps",
        "summary": "Tối ưu hóa Dockerfile Multi-stage builds, giảm dung lượng image 95%, quản lý Docker Compose, Network, Volume và chuẩn hóa CI/CD.",
        "content": """# CẨM NANG DOCKER & CONTAINERIZATION THỰC CHIẾN

---

## 1. KỸ THUẬT MULTI-STAGE BUILDS (GIẢM IMAGE TỪ 1GB XUỐNG 50MB)
Tách riêng biệt môi trường Build (cần compiler, SDK, header files) và môi trường Chạy Runtime (chỉ chứa file nhị phân hoặc mã nguồn đã build):

```dockerfile
# Stage 1: Build & Dependencies
FROM python:3.11-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Runtime Production
FROM python:3.11-alpine AS runner
WORKDIR /app
# Tạo user non-root để đảm bảo bảo mật
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
COPY --from=builder /root/.local /home/appuser/.local
COPY --chown=appuser:appgroup . .
USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 2. QUY TẮC CACHE LAYER TRONG DOCKERFILE
- Mỗi dòng lệnh (`RUN`, `COPY`, `ADD`) tạo ra một layer chỉ đọc mới.
- Docker cache theo thứ tự từ trên xuống dưới. Nếu 1 layer bị thay đổi, tất cả các layer phía sau nó đều bị vô hiệu hóa cache.
- **Quy tắc vàng**: Copy file quản lý thư viện (`requirements.txt`, `package.json`) và cài đặt dependencies TRƯỚC, sau đó mới `COPY . .` toàn bộ mã nguồn.

---

## 3. DOCKER NETWORKING & HEALTHCHECKS
- **Network Bridge**: Cho phép các container trong cùng mạng liên lạc với nhau qua tên dịch vụ (Service Name DNS) thay vì IP động.
- **Container Healthcheck**: Thiết lập lệnh kiểm tra định kỳ trong `docker-compose.yml` để Docker tự động phát hiện container bị đơ hoặc lỗi DB connection và khởi động lại kịp thời.
"""
    },
    "sql_db": {
        "title": "Cẩm Nang Cơ Sở Dữ Liệu Quan Hệ SQL & Tối Ưu Truy Vấn",
        "category": "Cơ Sở Dữ Liệu (Database)",
        "summary": "Bản chất B-Tree Index, Leftmost Prefix Rule, tối ưu hóa Explain Analyze, cơ chế MVCC, khắc phục triệt để lỗi N+1 Query và chuẩn ACID.",
        "content": """# CẨM NANG CƠ SỞ DỮ LIỆU QUAN HỆ SQL & TỐI ƯU TRUY VẤN

---

## 1. CẤU TRÚC B-TREE INDEX & NGUYÊN TẮC TIỀN TỐ TRÁI NHẤT
- **Bản chất B-Tree Index**: Cây cân bằng tự duy trì thứ tự sắp xếp của dữ liệu theo khóa, giúp giảm độ phức tạp tìm kiếm từ quét toàn bảng (Sequential Scan - O(n)) xuống tìm kiếm theo nhánh cây (Index Scan - O(log n)).
- **Quy tắc tiền tố trái nhất (Leftmost Prefix Rule)**:
  * Khi tạo Composite Index trên nhiều cột `INDEX (col_A, col_B, col_C)`:
  * Truy vấn có `WHERE col_A = 1` → **DÙNG ĐƯỢC INDEX**.
  * Truy vấn có `WHERE col_A = 1 AND col_B = 2` → **DÙNG ĐƯỢC INDEX**.
  * Truy vấn chỉ có `WHERE col_B = 2` hoặc `WHERE col_C = 3` → **HOÀN TOÀN KHÔNG DÙNG ĐƯỢC INDEX** (Bị quét Full Table Scan)!

---

## 2. CƠ CHẾ MVCC (MULTI-VERSION CONCURRENCY CONTROL)
- **Nguyên lý hoạt động (trong PostgreSQL/MySQL InnoDB)**:
  * Khi sửa hoặc xóa dữ liệu, CSDL không ghi đè trực tiếp lên đĩa mà đánh dấu phiên bản cũ và tạo một bản ghi phiên bản mới.
  * Mỗi transaction có một snapshot thời điểm (Transaction ID). Câu lệnh `SELECT` chỉ đọc các dòng dữ liệu có phiên bản hợp lệ với snapshot của nó.
  * **Hệ quả vàng**: Thao tác đọc (Readers) không bao giờ khóa thao tác ghi (Writers), và thao tác ghi không khóa thao tác đọc!

---

## 3. KHẮC PHỤC TRIỆT ĐỂ LỖI N+1 QUERY
- **Triệu chứng**: Khi lấy danh sách N đơn hàng và lặp qua từng đơn hàng để lấy thông tin khách hàng, ứng dụng phát ra 1 câu lệnh lấy danh sách và N câu lệnh phụ riêng biệt → Làm sập DB khi N lớn.
- **Giải pháp**:
  * Sử dụng kỹ thuật `JOIN` để gom về 1 câu query duy nhất (Django: `select_related`).
  * Hoặc dùng toán tử `WHERE id IN (...)` để lấy toàn bộ dữ liệu phụ trong lần query thứ 2 (Django: `prefetch_related`).
"""
    },
    "redis_cache": {
        "title": "Cẩm Nang Hệ Thống Caching Chuyên Sâu Với Redis",
        "category": "Cơ Sở Dữ Liệu & Cache",
        "summary": "Chiến lược Cache-Aside, Write-Through, xử lý các thảm họa Cache Breakdown, Cache Avalanche, Cache Penetration và Distributed Lock.",
        "content": """# CẨM NANG HỆ THỐNG CACHING CHUYÊN SÂU VỚI REDIS

---

## 1. CÁC MẪU THIẾT KẾ CACHING PHỔ BIẾN
1. **Cache-Aside (Lazy Loading - Phổ biến nhất)**:
   - Ứng dụng đọc từ Cache trước. Nếu có (Cache Hit) → Trả về dữ liệu ngay.
   - Nếu không có (Cache Miss) → Đọc từ CSDL chính, ghi kết quả vào Cache kèm thời gian sống (TTL), rồi trả về.
2. **Write-Through**: Dữ liệu được ghi đồng thời vào Cache và CSDL trong cùng một giao dịch.

---

## 2. BỘ BA THẢM HỌA CACHE & CÁCH PHÒNG CHỐNG
- **Cache Breakdown (Điểm sập khóa nóng)**:
  * Một Hot Key chứa lượng truy cập cực lớn bị hết hạn TTL đúng lúc cao điểm → Hàng triệu request đồng loạt ùa vào CSDL gây sập hệ thống.
  * **Giải pháp**: Áp dụng Mutex / Distributed Lock (chỉ cho 1 tiến trình truy vấn CSDL và tái tạo cache; các tiến trình khác chờ).
- **Cache Avalanche (Tuyết lở Cache)**:
  * Hàng loạt key được gán cùng một thời gian hết hạn TTL (ví dụ cùng 60 phút) → Cùng lúc hết hạn khiến toàn bộ lưu lượng dồn vào DB.
  * **Giải pháp**: Bổ sung độ trôi ngẫu nhiên (Random Jitter TTL): `TTL = 3600 + random(0, 300)`.
- **Cache Penetration (Xuyên thủng Cache)**:
  * Hacker liên tục gửi request tìm kiếm các ID không hề tồn tại trong hệ thống → Cache luôn Miss và DB bị quét liên tục.
  * **Giải pháp**: Lưu giá trị rỗng (`Null Value`) có TTL ngắn vào cache, hoặc sử dụng bộ lọc Bloom Filter.
"""
    },
    "git_vcs": {
        "title": "Cẩm Nang Quản Lý Mã Nguồn Git Chuyên Nghiệp",
        "category": "Công Cụ Phát Triển (VCS)",
        "summary": "Quy tắc vàng Git Rebase vs Git Merge, giải quyết Conflict trong Detached HEAD, gỡ lỗi bằng Git Bisect, Cherry-Pick và chuẩn mực Gitflow.",
        "content": """# CẨM NANG QUẢN LÝ MÃ NGUỒN GIT CHUYÊN NGHIỆP

---

## 1. QUY TẮC VÀNG: GIT REBASE VS GIT MERGE
- **Git Merge**: Tạo ra một commit gộp (Merge Commit) giữ nguyên trọn vẹn lịch sử phân nhánh của dự án. An toàn cho các nhánh dùng chung (`main`, `develop`).
- **Git Rebase**: Di chuyển toàn bộ các commit của nhánh hiện tại lên đỉnh của nhánh đích, tạo ra một lịch sử commit tuyến tính sạch đẹp.
- **QUY TẮC BẤT DI BẤT DỊCH CỦA REBASE**:
  * CHỈ rebase trên các nhánh tính năng cục bộ (local feature branch) do chính bạn làm việc.
  * **TUYỆT ĐỐI KHÔNG REBASE** các nhánh đã được đẩy (pushed) lên server và có người khác đang cùng làm việc, vì sẽ làm thay đổi SHA hash của commit và phá hủy lịch sử git của đồng nghiệp!

---

## 2. TRUY LÙNG BUG BẰNG `git bisect`
Khi phát hiện một bug trên Production nhưng không biết commit nào trong số hàng trăm commit gần đây gây ra lỗi:
1. `git bisect start`: Khởi động chế độ tìm kiếm nhị phân.
2. `git bisect bad`: Đánh dấu commit hiện tại bị lỗi.
3. `git bisect good <commit_sha_cu>`: Đánh dấu commit cũ trước đó vẫn hoạt động tốt.
4. Git sẽ tự động checkout commit ở giữa. Bạn chạy thử test, gõ `git bisect good` hoặc `git bisect bad`.
5. Sau O(log n) bước (chỉ khoảng 5-7 lần kiểm tra thay vì 100 lần), Git sẽ chỉ đích danh commit gây lỗi!

---

## 3. XỬ LÝ CONFLICT AN TOÀN
- Khi gặp xung đột khi rebase hoặc merge:
  1. Kiểm tra trạng thái: `git status`.
  2. Mở file xung đột, xử lý các thẻ `<<<<<<<`, `=======`, `>>>>>>>`.
  3. Đánh dấu đã giải quyết: `git add <file>`.
  4. Tiếp tục: `git rebase --continue` (hoặc `git merge --continue`).
  5. Nếu muốn hủy bỏ an toàn: `git rebase --abort`.
"""
    }
}


def get_offline_doc(doc_id):
    """Lấy nội dung cẩm nang offline theo ID."""
    return OFFLINE_DOCS.get(doc_id.lower().strip())


def search_offline_docs(keyword):
    """Tìm kiếm trong kho cẩm nang offline."""
    kw = keyword.lower().strip()
    results = []
    for k, doc in OFFLINE_DOCS.items():
        if kw in doc["title"].lower() or kw in doc["summary"].lower() or kw in doc["content"].lower():
            results.append({"id": k, **doc})
    return results


def get_all_offline_docs():
    """Lấy danh sách tất cả cẩm nang offline có sẵn."""
    return [{"id": k, **doc} for k, doc in OFFLINE_DOCS.items()]