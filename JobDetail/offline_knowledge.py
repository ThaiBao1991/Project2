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

## 1. KHÁI NIỆM & TIÊU CHUẨN QUỐC TẾ
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

## 3. BẢNG PHÂN TÍCH 6 TỔN THẤT LỚN (SIX BIG LOSSES) & GIẢI PHÁP
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

## 5. SO SÁNH OEE VS TEEP & BÀI TOÁN THẨM ĐỊNH DỰ ÁN ĐẦU TƯ CAPEX

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
     Standard\ Time\ (ST) = Normal\ Time × (1 + Allowance)

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
  * Toàn chuyền dừng 20 phút để họp chất lượng đột xuất giải quyết khiếu nại khách hàng (10  người} × 20  phút} = 200  phút công}).
  → **Tổng Thời Gian Lao Động Thực Tế (Actual Working Labor Hours)**:
  4,500 - (30 + 60 + 200) = 4,210  phút công}
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
"""
    },

    "smed": {
        "title": "Cẩm Nang Kỹ Thuật SMED — Rút Ngắn Thời Gian Chuyển Đổi Khuôn/Mã Hàng Dưới 10 Phút",
        "summary": "Quy trình 4 bước của Shigeo Shingo, phân tách thao tác Trong vs Ngoài, Case Study ép nhựa 85p xuống 8p40s, kịch bản 2 người song song F1 Pit-stop và 6 cơ cấu gá kẹp 1 chạm.",
        "category": "Sản Xuất (Manufacturing)",
        "content": """# ⚡ CẨM NANG THỰC CHIẾN SMED (SINGLE-MINUTE EXCHANGE OF DIE)
*(Rút Ngắn Thời Gian Chuyển Đổi Khuôn Mẫu & Đổi Mã Hàng Về Mức Dưới 10 Phút)*

---

## 1. SMED LÀ GÌ VÀ VÌ SAO SMED LÀ TRÁI TIM CỦA SẢN XUẤT LEAN?
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

## 2. QUY TRÌNH 4 GIAI ĐOẠN SHINGO KINH ĐIỂN

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

## 3. CASE STUDY THỰC TẾ: RÚT NGẮN THỜI GIAN ĐỔI KHUÔN MÁY ÉP NHỰA TỪ 85 PHÚT XUỐNG 8 PHÚT 40 GIÂY

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
"""
    },

    "lean_muda": {
        "title": "Cẩm Nang 7 Lãng Phí (Muda), 5S, Kaizen & Cơ Cấu Poka-Yoke",
        "summary": "Chi tiết 7 lãng phí trong sản xuất TIMWOOD, phương pháp nhận diện tại xưởng, quy trình 5S, Kaizen và cơ cấu chống lỗi Poka-Yoke.",
        "category": "Sản Xuất (Manufacturing)",
        "content": """# 🧹 CẨM NANG LEAN MANUFACTURING: 7 LÃNG PHÍ, 5S & POKA-YOKE

## 1. 7 LOẠI LÃNG PHÍ TRONG SẢN XUẤT (TIMWOOD)
Lãng phí (Muda) là bất kỳ hoạt động nào tiêu tốn tài nguyên (thời gian, tiền bạc, nhân lực) nhưng **KHÔNG tạo ra giá trị mà khách hàng sẵn sàng chi trả**.

1. **T - Transportation (Vận chuyển thừa)**: Di chuyển vật tư, phôi giữa các xưởng quá xa. Giải pháp: Quy hoạch lại mặt bằng chuyền chữ U.
2. **I - Inventory (Tồn kho dư thừa)**: Tồn kho nguyên vật liệu, bán thành phẩm (WIP) nằm ngổn ngang. Giải pháp: Sản xuất kéo (Kanban), Just-In-Time.
3. **M - Motion (Thao tác thừa của công nhân)**: Cúi người, với tay, đi lại tìm dụng cụ. Giải pháp: Bố trí đồ nghề trong tầm với 40cm, bảng treo dụng cụ bóng (Shadow Board).
4. **W - Waiting (Thời gian chờ đợi)**: Chờ máy chạy, chờ nguyên liệu về, chờ QC nghiệm thu. Giải pháp: Cân bằng chuyền, bảo trì phòng ngừa TPM.
5. **O - Overproduction (Sản xuất dư thừa - NGUY HIỂM NHẤT)**: Sản xuất nhiều hơn hoặc sớm hơn đơn hàng. Đây là nguồn cơn sinh ra tồn kho, che giấu mọi khuyết tật máy móc.
6. **O - Overprocessing (Gia công thừa / Quá mức cần thiết)**: Đánh bóng bề mặt khách không yêu cầu, kiểm tra 3 lần qua nhiều khâu trung gian. Giải pháp: Chuẩn hóa tiêu chí chấp nhận theo đúng bản vẽ kỹ thuật.
7. **D - Defects (Phế phẩm & Sửa chữa)**: Sản phẩm lỗi phải vứt bỏ hoặc tốn công nhân làm lại (Rework). Giải pháp: Poka-Yoke, kiểm soát quá trình SPC.

---

## 2. QUY TRÌNH 5S THỰC CHIẾN TẠI HIỆN TRƯỜNG
- **S1 - Seiri (Sàng lọc)**: Phân loại đồ cần dùng và không cần dùng. Dán thẻ đỏ (Red Tag) vào đồ thừa và thanh lý khỏi xưởng trong 48h.
- **S2 - Seiton (Sắp xếp)**: *"Một chỗ cho mọi thứ, và mọi thứ ở đúng chỗ của nó"*. Kẻ vạch sơn phân vùng, dán nhãn tên, mã màu trực quan.
- **S3 - Seiso (Sạch sẽ)**: Vệ sinh là kiểm tra. Khi lau chùi máy, công nhân sẽ phát hiện rò rỉ dầu mỡ, lỏng ốc trước khi máy hỏng.
- **S4 - Seiketsu (Săn sóc)**: Chuẩn hóa 3S trên thành tiêu chuẩn bảng kiểm (5S Audit Checklist) chấm điểm thi đua hàng tuần.
- **S5 - Shitsuke (Sẵn sàng)**: Xây dựng thói quen và văn hóa tự giác tuân thủ cho toàn bộ cán bộ công nhân viên.

---

## 3. CƠ CẤU CHỐNG LỖI SAI POKA-YOKE (MISTAKE PROOFING)
Poka-Yoke là thiết kế cơ khí hoặc điện tử để **ngăn ngừa lỗi thao tác 100% ngay từ đầu**:
1. **Poka-Yoke Cảnh Báo (Warning)**: Còi hú, đèn Andon nhấp nháy khi công nhân quên 1 bước.
2. **Poka-Yoke Kiểm Soát (Control - Tốt nhất)**: Ngắt nguồn máy móc, không cho máy dập/hàn hoạt động nếu phôi chưa được đặt đúng vị trí.
*Ví dụ:* Khe cắm SIM điện thoại cắt vát 1 góc, đầu cắm USB, cữ gá có chốt định vị lệch tâm.
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
- Đảm bảo độ chính xác tồn kho hệ thống ERP (Record Inventory Accuracy - RIA) luôn đạt **≥ 98.5\%**.
"""
    },

    "excel_mfg": {
        "title": "Cẩm Nang Thực Hành Microsoft Excel Nâng Cao Trong Quản Lý Sản Xuất",
        "summary": "Hướng dẫn sử dụng Power Query gom dữ liệu log ca, lập báo cáo Pivot Table, vẽ biểu đồ Pareto 80/20 và mã VBA Macro tự động hóa báo cáo.",
        "category": "Phần Mềm & Công Cụ",
        "content": """# 📊 HƯỚNG DẪN THỰC HÀNH EXCEL NÂNG CAO TRONG QUẢN TRỊ SẢN XUẤT

## 1. TẠI SAO PHẢI DÙNG POWER QUERY THAY VÌ COPY-PASTE THỦ CÔNG?
Trong nhà máy, mỗi ngày có hàng chục file Excel ghi chép dừng máy từ các tổ/ca. Nếu copy-paste bằng tay sẽ mất 1 giờ/ngày và rất dễ nhầm lẫn.

### Các Bước Gom File Tự Động Bằng Power Query:
1. Lưu tất cả các file log ca vào 1 thư mục cố định: `D:\ProductionLogs\`.
2. Mở Excel mới → Vào tab **Data** → **Get Data** → **From File** → **From Folder**.
3. Chọn thư mục `ProductionLogs` → Bấm **Combine & Transform Data**.
4. Power Query sẽ tự động nối tất cả các dòng dữ liệu, loại bỏ dòng tiêu đề lặp, chuẩn hóa cột Ngày tháng và Thời gian dừng máy.
5. Mỗi ngày có file log mới bỏ vào thư mục, chỉ cần vào Excel bấm **Refresh All** là toàn bộ báo cáo tự động cập nhật trong 3 giây!

---

## 2. VẼ BIỂU ĐỒ PARETO 80/20 NGUYÊN NHÂN DỪNG MÁY
1. Quét chọn 2 cột: Cột A (Nguyên nhân dừng máy) và Cột B (Tổng số phút dừng).
2. Vào tab **Insert** → Chọn biểu đồ **Pareto Chart** (Có đường cong tích lũy %).
3. Nhìn vào điểm giao cắt 80% để chỉ mặt điểm tên 3 nguyên nhân cốt lõi cần tổ chức cuộc họp Kaizen xử lý ngay trong tuần.

---

## 3. ĐOẠN MÃ VBA MACRO TỰ ĐỘNG XUẤT BÁO CÁO CA HÀNG NGÀY
Nhấn `Alt + F11` trong Excel, chèn Module mới và dán đoạn mã sau:

```vba
Sub ExportDailyProductionReport()
    Dim ws As Worksheet
    Dim savePath As String
    Dim fileName As String
    
    Set ws = ThisWorkbook.Sheets("BaoCaoCa")
    savePath = ThisWorkbook.Path & "\\BaoCaoPDF\\"
    
    ' Tạo thư mục nếu chưa có
    If Dir(savePath, vbDirectory) = "" Then
        MkDir savePath
    End If
    
    fileName = "BaoCao_SanXuat_" & Format(Now, "yyyy-mm-dd_hhnn") & ".pdf"
    
    ' Xuất Sheet ra file PDF tự động
    ws.ExportAsFixedFormat Type:=xlTypePDF, _
        fileName:=savePath & fileName, _
        Quality:=xlQualityStandard, _
        IncludeDocProperties:=True, _
        IgnorePrintAreas:=False, _
        OpenAfterPublish:=False
        
    MsgBox "Đã xuất báo cáo sản xuất PDF thành công tại: " & vbCrLf & savePath & fileName, vbInformation, "Thông Báo Kỹ Sư Lean"
End Sub
```
"""
    },

    "powerbi_mfg": {
        "title": "Cẩm Nang Xây Dựng Dashboard Sản Xuất Trên Microsoft Power BI",
        "summary": "Thiết kế mô hình dữ liệu Star Schema, viết công thức DAX đo lường OEE/OLE thời gian thực, thiết lập Scheduled Refresh tự động.",
        "category": "Phần Mềm & Công Cụ",
        "content": """# 📈 THIẾT KẾ DASHBOARD OEE/OLE TRỰC QUAN TRÊN MICROSOFT POWER BI

## 1. MÔ HÌNH DỮ LIỆU CHUẨN (STAR SCHEMA)
Để Dashboard chạy mượt mà không bị giật đơ khi dữ liệu lên tới hàng triệu dòng:
- **Bảng Fact (Sự kiện)**: `Fact_Production` (Ghi nhận từng sản phẩm/lô: Ngày, Giờ, Mã Máy, Mã Hàng, Số lượng đạt, Phế phẩm) và `Fact_Downtime` (Ghi nhận dừng máy: Bắt đầu, Kết thúc, Mã lỗi).
- **Bảng Dimension (Chiều tra cứu)**: `Dim_Machines` (Danh mục máy), `Dim_Products` (Danh mục mã hàng & Ideal Cycle Time), `Dim_Date` (Bảng lịch thời gian).

---

## 2. CÁC HÀM CÔNG THỨC DAX CHUẨN ĐO LƯỜNG SẢN XUẤT

### Tính Availability (Độ khả dụng):
```dax
Availability_Rate = 
VAR PlannedTime = SUM(Fact_Production[PlannedMinutes])
VAR ActualDowntime = SUM(Fact_Downtime[DowntimeMinutes])
VAR OperatingTime = PlannedTime - ActualDowntime
RETURN
DIVIDE(OperatingTime, PlannedTime, 0)
```

### Tính Performance (Hiệu suất):
```dax
Performance_Rate = 
VAR TotalProduced = SUM(Fact_Production[TotalCount])
VAR OperatingTimeSeconds = (SUM(Fact_Production[PlannedMinutes]) - SUM(Fact_Downtime[DowntimeMinutes])) * 60
VAR IdealProducedSeconds = SUMX(Fact_Production, Fact_Production[TotalCount] * RELATED(Dim_Products[IdealCycleTimeSeconds]))
RETURN
DIVIDE(IdealProducedSeconds, OperatingTimeSeconds, 0)
```

### Tính Quality (Tỷ lệ chất lượng):
```dax
Quality_Rate = 
DIVIDE(
    SUM(Fact_Production[GoodCount]),
    SUM(Fact_Production[TotalCount]),
    0
)
```

### Tính OEE Tổng Thể:
```dax
OEE_Score = [Availability_Rate] * [Performance_Rate] * [Quality_Rate]
```
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
- **Nghịch lý rõ rệt:** Cp = 1.33 chứng tỏ độ biến động của máy cực kỳ hẹp và ổn định (đủ năng lực 4 Sigma). Tuy nhiên C_{pk} = 0.80 (< 1.0) lại là mức báo động đỏ sinh ra phế phẩm hàng loạt!
- **Nguyên nhân cốt lõi:** Phân phối kích thước bị **Lệch Tâm 0.04 mm về phía USL** (tiệm cận sát vách dung sai trên), làm chi tiết bị tiện quá to.
- **Hành động kỹ thuật cực kỳ đơn giản mà không tốn tiền:**
  * Kỹ sư chỉ cần vào màn hình điều khiển máy tiện CNC, nhập bù trừ gốc tọa độ (Tool Offset adjustment): lùi mũi dao Z/X lại đúng **0.04  mm}**.
  * Sau khi dịch tâm μ từ 25.04 mm về đúng 25.00 mm:
    C_{pk\ mới} = \frac{25.10 - 25.00}{3 × 0.025} = \frac{0.10}{0.075} = 1.333
  * Ngay lập tức quy trình đạt chuẩn công nghiệp Cpk = 1.33 mà không tốn bất kỳ chi phí bảo trì nào!

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
        "title": "Cẩm Nang Thiết Kế Mặt Bằng Xưởng Tinh Gọn (Plant Layout) & Sơ Đồ Spaghetti",
        "summary": "Nguyên tắc thiết kế chuyền chữ U, kỹ thuật vẽ Spaghetti Diagram phân tích quãng đường di chuyển của công nhân, phân định luồng giao thông 5S.",
        "category": "Phần Mềm & Công Cụ",
        "content": """# 📐 THIẾT KẾ MẶT BẰNG NHÀ XƯỞNG TINH GỌN (PLANT LAYOUT) & SPAGHETTI

## 1. NGUYÊN TẮC BỐ TRÍ CHUYỀN CHỮ U (U-SHAPED CELL)
Bố trí máy móc theo hàng thẳng dài truyền thống gây ra lãng phí đi lại rất lớn. Bố trí chuyền sản xuất hình chữ U mang lại các ưu thế vượt trội:
1. **Điểm đầu và điểm cuối gần nhau**: Công nhân nạp nguyên liệu vào và lấy thành phẩm ra tại cùng một vị trí → Giảm quãng đường di chuyển tới 70%.
2. **Linh hoạt nhân lực**: Khi sản lượng ít, 1 công nhân có thể phụ trách 3 máy (Đa năng - Multi-skilled worker); khi đơn hàng nhiều, có thể bố trí 3 công nhân đứng vào các vị trí mà không cần đổi layout.
3. **Luồng 1 sản phẩm (One-Piece Flow)**: Sản phẩm làm xong ở máy 1 chuyển ngay sang máy 2, triệt tiêu việc chất đống hàng chờ (WIP) giữa các công đoạn.

---

## 2. KỸ THUẬT VẼ SƠ ĐỒ SPAGHETTI DIAGRAM
Sơ đồ Spaghetti là công cụ trực quan hóa toàn bộ quãng đường di chuyển của công nhân hoặc nguyên vật liệu trên bản vẽ mặt bằng xưởng (AutoCAD).

### Các Bước Thực Hiện:
1. In bản vẽ mặt bằng tỷ lệ chuẩn của xưởng ra giấy A3 hoặc mở trên AutoCAD.
2. Cầm bảng vẽ đi theo chân một công nhân trong suốt 1 ca làm việc.
3. Vẽ một đường nét liền theo từng bước chân của họ (khi đi lấy đồ gá, lấy ốc vít, đi bỏ phế phẩm...).
4. Đo tổng chiều dài quãng đường đi lại trong 1 ca (thường dao động từ 5km - 10km đi bộ lãng phí!).
5. Cải tiến: Đưa dụng cụ và nguyên vật liệu lại sát vị trí đứng trong bán kính 1 sải tay (Point-of-Use Storage) → Vẽ lại sơ đồ sau cải tiến để chứng minh quãng đường giảm từ 7km xuống còn dưới 1km.
"""
    },

    "erp_mes": {
        "title": "Cẩm Nang Tích Hợp Hệ Thống Quản Trị ERP (SAP PP) & Hệ Thống Điều Hành MES",
        "summary": "Mô hình kiến trúc tự động hóa kim tự tháp ISA-95, luồng điều hành lệnh sản xuất từ SAP PP xuống MES và gửi dữ liệu OEE/Downtime thời gian thực.",
        "category": "Phần Mềm & Công Cụ",
        "content": """# 🏭 TÍCH HỢP HỆ THỐNG ERP (SAP PP) & MES TRONG NHÀ MÁY THÔNG MINH

## 1. MÔ HÌNH KIẾN TRÚC PHÂN TẦNG (CHUẨN ISA-95)
- **Tầng 4 - Quản trị Doanh nghiệp (ERP - SAP S/4HANA / Oracle)**: Quản lý kế hoạch kinh doanh, đơn hàng bán hàng, định mức BOM, mua hàng nguyên vật liệu và hạch toán giá thành tài chính.
- **Tầng 3 - Điều hành Sản xuất (MES - Manufacturing Execution System)**: Điều độ lệnh sản xuất cho từng máy, theo dõi sản lượng từng ca, quản lý truy xuất nguồn gốc (Traceability) lô hàng.
- **Tầng 2 & 1 - Giám sát & Điều khiển (SCADA / PLC / Cảm biến)**: Thu thập xung đếm sản phẩm từ cảm biến quang, tín hiệu dừng máy từ rơ-le nhiệt, trạng thái lỗi từ PLC.

---

## 2. LUỒNG DỮ LIỆU TỰ ĐỘNG GIỮA MES VÀ ERP
1. **Từ ERP xuống MES**: ERP phát hành Lệnh Sản Xuất (Production Order) kèm mã hàng, số lượng và định mức BOM tiêu chuẩn → Đẩy xuống MES.
2. **Tại hiện trường (MES Execution)**: Công nhân quét mã vạch nhận việc trên màn hình cảm ứng tại máy. Hệ thống tự động đếm sản phẩm đạt và phế phẩm qua cảm biến.
3. **Từ MES ngược lên ERP**: Hết ca, MES tự động gửi thông điệp xác nhận sản lượng thực tế (Confirmation) và số giờ dừng máy về ERP để kế toán hạch toán đúng chi phí nhân công và tiêu hao vật tư.
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