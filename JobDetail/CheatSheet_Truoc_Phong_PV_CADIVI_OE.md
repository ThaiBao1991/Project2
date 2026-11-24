# ⚡ CHEAT SHEET TRƯỚC CỬA PHÒNG PHỎNG VẤN — CHUYÊN VIÊN OE CADIVI MIỀN TRUNG

> **Cách dùng:** Đọc trọn trong **10 phút** trước khi bước vào Nhà máy CADIVI Miền Trung (Đường số 2, KCN Hòa Cầm, Cẩm Lệ, Đà Nẵng). Mục 2 bên dưới có thể **in riêng ra 1 tờ A4** kẹp cùng CV mang thẳng vào phòng phỏng vấn!

---

## PHẦN 1: TỜ NHỚ NHANH 10 PHÚT TRƯỚC GIỜ G

### 1. Tự Giới Thiệu 90 Giây & 3 Quy Tắc Vàng Bảo Mật Số Liệu CV
- **4 mũi nhọn cá nhân (Phan Thanh Thái Bảo):**
  1. **Kỹ sư Cơ khí** định cư ổn định tại Đà Nẵng, 5+ năm kinh nghiệm nhà máy sản xuất.
  2. **2 năm Quản lý & Cải tiến SX 1 tại Fujikura Automotive** (dây dẫn ô tô — triển khai quét Barcode RE7 thay sổ giấy, phân tích lỗi theo công đoạn/người thao tác).
  3. **Nhóm trưởng Phòng Kiểm tra (QC) tại Mabuchi Motor Đà Nẵng** — vận hành OGP/Keyence/Canon INEX, làm **Time Study rút Canon INEX `60s → 30s/hạng mục` (`-50% thời gian đo`)**, cải tiến đồ gá **`1 → 16 mẫu/lượt gá`**.
  4. **Tự động hóa dữ liệu thực chiến (`Python / VBA / Excel / Access / Power BI`)**: rút báo cáo khách hàng `3–7 ngày → 2 giờ/tháng`, tự động nhập liệu máy OGP `120p → 15p/ngày` (`-87.5%`).
- **⚠️ 3 ĐIỀU TUYỆT ĐỐI KHÔNG NÓI HỚ:**
  - KHÔNG nói *"giảm 50% nhân sự"* (nói đúng: **giảm 50% thời gian đo/hạng mục**).
  - KHÔNG nói *"tăng năng suất 16 lần"* (nói đúng: **tăng sức chứa mỗi lượt gá 1→16 mẫu giảm thao tác gá lặp lại**).
  - KHÔNG tiết lộ con số tiết kiệm nội bộ công ty cũ khi hỏi về thẩm định thiết bị `~1.2 tỷ` — chỉ trình bày **PHƯƠNG PHÁP LUẬN thẩm định ROI/Payback** (tách *Hard Savings vs Soft Savings*, xác nhận chéo Kế toán, chạy 3 kịch bản độ nhạy!).

### 2. Bảng Giải Mã Mã Cáp CADIVI & Con Số Vàng Hay Bị Hỏi Nhẩm
| Ký hiệu CADIVI | Cấu tạo & Ý nghĩa cốt lõi | Máy móc / Điểm chú ý OE |
|---|---|---|
| **`VC 2.5` / `VCm` / `VCmd`** | Đồng đặc/mềm Class 5 + Cách điện PVC (70°C, QCVN 4) | Kéo → Buncher → Đùn PVC → Khoanh 100m (**Copper Give-away**, **Yamazumi**) |
| **`CVV` / `CXV 3×95+1×50`** | Đồng + Cách điện PVC (`V`) hoặc XLPE (`X`, 90°C) + Vỏ PVC | `CXV` có thêm **Phòng xông Sauna Silane** (nút thắt WIP) & **Drum Twister** |
| **`CXV/DSTA 3×120+1×70`** | Cáp lực 3–4 lõi + **2 lớp băng THÉP** chôn ngầm | Máy quấn giáp DSTA (đổi cuộn 2,500m giảm dừng hàn) + Solver **Cut-Length** |
| **`CXV/DATA 1×300`** | Cáp **1 lõi AC** bắt buộc **2 lớp băng NHÔM (`DATA`)** | **CẤM dùng thép DSTA** cho cáp 1 lõi AC vì dòng xoáy Eddy Current gây nóng chảy! |
| **`CXV/FR` / `LSZH`** | Quấn băng **Mica FR** (950°C/90–180p) + Vỏ ít khói **LSZH** | Chồng mép Mica 40%; LSZH dùng **trục vít nén thấp, nhiệt ≤ 165°C, DDR 1.1–1.6** |
| **`LV-ABC 4×50` / `As 240/32`** | Cáp **NHÔM** treo XLPE Đen 2.5% UV / Nhôm lõi thép **ACSR** | **Cách ly tuyệt đối bụi đồng**; ABC chạy 4 pha 0-Purge (chỉ đổi vòng Cối gân 5p) |
| **`CXV/S/DSTA 24kV`** | Cáp trung thế 3 lớp đồng đùn trên ống cong **CCV** | Chạy Campaign 24/7 giảm phế bật lò, Nitơ 12 bar, test **Partial Discharge ≤ 5 pC** |
| **`H1Z2Z2-K` / `CVV-S`** | Cáp **Solar** đồng mạ thiếc `E-beam` / Cáp lưới **Braiding** | Giữ phủ lưới 87% (không đan dư 93%), 1 người đứng 6–10 máy Braiding |

- **Công thức vàng cần thuộc lòng:**
  - `OEE = A × P × Q` (ngành cáp tính theo **tốc độ mét/phút**; **cấm** lấy `AVERAGE()` của 5 ca mà phải dùng `SUM()` tổng có trọng số!).
  - `Copper Give-away % = [(D_thực / D_chuẩn)² − 1] × 100%` (dư chỉ `+0.008mm` trên dây `Ø0.67mm` = mất `+2.4%` đồng!).
  - **Tỷ trọng:** Đồng `8.89` · Nhôm `2.70` · PVC `1.40–1.50` · XLPE `0.92` (`VNĐ/lít = VNĐ/kg × Tỷ trọng` — bẫy độn bột đá CaCO3!).
  - **Điện trở 20°C `IEC 60228`:** `1.5mm² ≤ 12.1` · `2.5mm² ≤ 7.41` · `50mm² ≤ 0.387` · `95mm² ≤ 0.193` · `240mm² ≤ 0.0754 Ω/km` | Quy đổi nhiệt: `R_20 = R_t / [1 + 0.00393 × (t − 20)]`.
  - **Chiều dày min `IEC 60502`:** Cách điện `t_min ≥ 0.9×t_nom − 0.1mm`; Vỏ ngoài `t_min ≥ 0.85×t_nom − 0.1mm`.
  - **Hot Set Test (XLPE 200°C):** Giãn dài ≤ `175%`, Giãn dư ≤ `15%` | **Phòng Lab CADIVI đạt chuẩn quốc tế `ISO/IEC 17025 (VILAS)`**.

### 3. Khung 6 Bước Trả Lời MỌI Câu Hỏi Tình Huống Hiện Trường (Không Bao Giờ Bị Bí!)
1. **Khoanh vùng an toàn/chất lượng ngay (Containment & LOTO):** Chặn lỗi lọt ra khách hàng, đảm bảo an toàn.
2. **Đi Genba xem vật thật & số thật (3 Thực):** Không đoán mò trong phòng lạnh — soi đầu dây đứt, đo thực tế, kiểm tra độ tin cậy dữ liệu (`MSA / Gage R&R`).
3. **Truy nguyên nhân gốc (RCA):** `Pareto 80/20` → `5 Whys` / `Ishikawa 4M` → chứng minh thống kê trên Minitab (`t-test`, `ANOVA`, `Scatter`, `p < 0.05`).
4. **Giải pháp ưu tiên chi phí thấp trước (`TOC` / `SMED`):** Tách External 0 đồng trước khi xin mua máy `CAPEX`.
5. **Chứng minh bằng tiền (Hard Savings & ROI):** Xác nhận chéo với Kế toán & chạy `MOC/ECN` đảm bảo chuẩn `QCVN 4 / IEC`.
6. **Khóa chuẩn chống tái diễn:** `SOP` + `OPL` + `Poka-Yoke` + `Control Plan` + `LSW` + `LPA` + `Escalation Matrix`.

### 4. 5 Câu Hỏi Ngược Chốt Hạ Cực Ghi Điểm Cuối Buổi
1. *"Trong 6–12 tháng tới, đâu là nút thắt hoặc chỉ số lớn nhất mà Nhà máy CADIVI Miền Trung kỳ vọng vị trí OE tập trung xử lý đầu tiên?"*
2. *"Hiện nhà máy đang thu thập dữ liệu OEE và hao phí BOM tự động qua ERP/MES hay đang kết hợp nhật ký ca Excel ạ?"*
3. *"Vị trí OE tại Hòa Cầm phối hợp với Quản đốc 4 phân xưởng và đội OE Tổng công ty theo cơ chế nào ạ?"*
4. *"Phong trào 5S và Kaizen hiện đang ở giai đoạn nào và khó khăn lớn nhất khi duy trì là gì ạ?"*
5. *"Sau 2 tháng thử việc, kết quả cụ thể nào sẽ giúp anh/chị đánh giá rằng việc chọn em là hoàn toàn đúng đắn ạ?"*

---

## PHẦN 2: BẢN IN 1-TRANG A4 MANG VÀO PHÒNG PHỎNG VẤN — ĐỀ XUẤT KẾ HOẠCH 30–60–90 NGÀY TẠI CADIVI MIỀN TRUNG

> *(In gọn riêng Phần 2 này trên 1 mặt giấy A4, kẹp cùng CV để đặt lên bàn khi trình bày kế hoạch nhận việc!)*

### ĐỀ XUẤT LỘ TRÌNH HÀNH ĐỘNG 90 NGÀY ĐẦU — VỊ TRÍ CHUYÊN VIÊN TỐI ƯU QUY TRÌNH (OE)
**Ứng viên:** Phan Thanh Thái Bảo (Kỹ sư Cơ khí · 0903219205) | **Đơn vị:** Nhà máy CADIVI Miền Trung (KCN Hòa Cầm, Đà Nẵng)

| Giai đoạn | Mục tiêu trọng tâm | Hành động cụ thể tại hiện trường (Genba) | Sản phẩm bàn giao đo lường được |
|---|---|---|---|
| **Ngày 1 – 30**<br>*(Hiểu sâu & Chuẩn hóa nền)* | Nắm trọn dòng chảy 4 xưởng, xây niềm tin với Quản đốc & kiểm toán độ sạch dữ liệu | • Đi Genba đủ 3 ca tại Xưởng Kéo – Bện – Đùn – Đóng cuộn & Lab `ISO 17025`.<br>• Kiểm toán sổ ca, mã dừng máy, cây BOM (hệ số Lay-up) & đối chiếu số nhập kho.<br>• Vẽ Current State **VSM** cho 1 họ sản phẩm chủ lực (`VC` hoặc `CXV`). | • Báo cáo Kiểm toán Dữ liệu & Sơ đồ VSM Hiện trạng.<br>• Bảng chuẩn hóa 12–15 mã dừng máy (6 Big Losses) & phân loại 3 nhóm phế đồng/nhựa.<br>• 1 Quick-Win hỗ trợ giảm thao tác giấy tờ cho Tổ trưởng. |
| **Ngày 31 – 60**<br>*(Tự động hóa & Nhận diện điểm nghẽn)* | Tự động hóa báo cáo OEE/OLE/BOM & chỉ rõ Top 3 tổn thất quy ra tiền | • Xây bộ công cụ **Excel Power Query / Python / Power BI** tổng hợp OEE m/phút, Scrap & BOM Variance tự động.<br>• Chạy **Pareto 80/20** & **Cost Deployment** xác định nút thắt lớn nhất.<br>• Quay video Time Study đổi màu 1 máy đùn Pilot & phân tích `Cpk` (Copper Give-away / Over-thickness) từ dữ liệu Lab. | • Dashboard OEE / OLE / BOM chạy tự động 1-chạm.<br>• Báo cáo **A3** đề xuất Dự án Pilot số 1 kèm phân tích **ROI / Payback** sơ bộ (xác nhận chéo Kế toán). |
| **Ngày 61 – 90**<br>*(Pilot tạo tiền tươi & Khóa chuẩn)* | Triển khai 1 dự án Pilot hoàn chỉnh, chứng minh hiệu quả thống kê & khóa chuẩn nhân rộng | • Thực hiện **Kaizen Blitz 5 ngày** trên máy đùn/chuyền Pilot (ví dụ: SMED tách External + Color Sequencing + sấy sẵn Tip/Die; hoặc giảm Over-thickness/Cut-Length).<br>• Kiểm định **2-Sample t-test (`p < 0.05`)** dữ liệu Trước–Sau 30 ngày.<br>• Hoàn tất **MOC/ECN** (nếu liên quan dung sai `QCVN 4`) & bàn giao hệ duy trì. | • Giảm 30–50% thời gian chuyển đổi (hoặc cắt phế rõ rệt) có Kế toán xác nhận **Hard Savings**.<br>• Bộ tài liệu khóa chuẩn: **SOP + OPL + Control Plan + LSW + LPA** sẵn sàng nhân rộng quý tiếp theo. |

---

## PHẦN 3: 2 MẪU EMAIL CẢM ƠN (GỬI TRONG 12–24 GIỜ SAU PHỎNG VẤN)

### Mẫu 1 — Gửi Phòng Nhân Sự (HR CADIVI Miền Trung)
- **Tiêu đề:** `Cảm ơn buổi phỏng vấn vị trí Chuyên viên Tối ưu Quy trình (OE) — Phan Thanh Thái Bảo`
- **Nội dung:**
  > Kính gửi anh/chị [Tên HR] cùng Hội đồng tuyển dụng Nhà máy CADIVI Miền Trung,
  >
  > Em là Phan Thanh Thái Bảo. Em xin chân thành cảm ơn anh/chị đã dành thời gian phỏng vấn và chia sẻ rất cởi mở về định hướng vận hành cũng như kỳ vọng đối với vị trí Chuyên viên Tối ưu Quy trình (OE) tại Nhà máy Hòa Cầm trong buổi [sáng/chiều] hôm nay.
  >
  > Qua trao đổi, em càng thêm hứng thú với các bài toán thực tế tại nhà máy — từ tối ưu hiệu suất thiết bị (OEE), rút ngắn chuyển đổi (SMED) cho đến chuẩn hóa dữ liệu định mức BOM vật tư đồng/nhựa. Em tin tưởng nền tảng Kỹ sư Cơ khí, kinh nghiệm quản lý sản xuất dây dẫn – kiểm tra chất lượng và khả năng tự động hóa báo cáo bằng Excel/VBA/Python sẽ giúp em nhanh chóng hòa nhập và đóng góp kết quả đo lường được ngay trong 90 ngày đầu.
  >
  > Em rất mong sớm nhận được thông tin phản hồi từ quý Công ty và sẵn sàng bổ sung bất kỳ thông tin nào nếu cần. Kính chúc anh/chị nhiều sức khỏe và thành công!
  >
  > Trân trọng,  
  > **Phan Thanh Thái Bảo** — SĐT: 0903.219.205

### Mẫu 2 — Gửi Giám Đốc Nhà Máy / Trưởng Phòng OE (Nếu có địa chỉ Email)
- **Tiêu đề:** `Cảm ơn anh [Tên] & một vài góc nhìn nhỏ sau buổi trao đổi vị trí OE — Phan Thanh Thái Bảo`
- **Nội dung:**
  > Kính gửi anh [Tên],
  >
  > Em là Bảo, ứng viên vị trí Chuyên viên OE vừa có buổi trao đổi rất giá trị cùng anh [sáng/chiều] hôm nay tại Nhà máy CADIVI Miền Trung. Em rất ấn tượng với chia sẻ của anh về [chèn 1 vấn đề cụ thể anh ấy nhắc trong buổi PV — vd: bài toán rút ngắn thời gian đổi màu máy đùn và chuẩn hóa báo cáo hao phí BOM cuối ca].
  >
  > Sau buổi gặp, em có ghi chú lại hướng tiếp cận sơ bộ nếu có cơ hội đồng hành: bắt đầu từ khảo sát hiện trường 3 ca để chuẩn hóa mã dừng máy, tách thao tác chuyển đổi ngoài (External SMED) không tốn vốn đầu tư và xây bộ tổng hợp tự động đối chiếu chéo với kho/Lab ISO 17025.
  >
  > Một lần nữa em cảm ơn anh đã dành thời gian lắng nghe và rất mong có cơ hội đóng góp lâu dài cho Nhà máy CADIVI Miền Trung!
  >
  > Trân trọng,  
  > **Phan Thanh Thái Bảo** — SĐT: 0903.219.205
