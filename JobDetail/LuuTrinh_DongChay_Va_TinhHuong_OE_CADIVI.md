# 🏭 LƯU TRÌNH DÒNG CHẢY NHÀ MÁY CADIVI MIỀN TRUNG & BẢN ĐỒ HÀNH ĐỘNG + 40 TÌNH HUỐNG THỰC CHIẾN OE

> **Điểm khác biệt cốt lõi:** Nếu `GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md` là *lưu trình học từ số 0* và `CamNang_ToanDien_OE_CADIVI_MienTrung.md` là *kho kiến thức & 202 định nghĩa*, thì tài liệu này là **Bản Đồ Vận Hành Thực Tế Dưới Xưởng CADIVI** — đi theo dòng chảy thật của nguyên liệu & lệnh sản xuất từ lúc nhận đơn hàng đến lúc giao xe, chỉ rõ **OE làm được gì từ đầu đến cuối** kèm **40 tình huống nóng xử lý 6 bước**.

> **Liên kết đồng hành:** [CamNang_ToanDien_OE_CADIVI_MienTrung.md](CamNang_ToanDien_OE_CADIVI_MienTrung.md) (202 Thuật Ngữ & 16 Cẩm Nang) · [GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md) (32 Bài Học A–Z).

---

## 📑 MỤC LỤC ĐIỀU HƯỚNG NHANH

### Phần I: 10 Trạm Dòng Chảy Vận Hành Khép Kín (S00 → S09)
- **[Trạm 00 (S00)](#tram-s00)** — Dòng Thông Tin & Hoạch Định Sản Xuất (S&OP → MPS → MRP → RCCP → CRP → MES)
- **[Trạm 01 (S01)](#tram-s01)** — Tiếp Nhận Nguyên Vật Liệu, Kiểm Đầu Vào (IQC) & Quản Trị Kho NVL
- **[Trạm 02 (S02)](#tram-s02)** — Xưởng Kéo Sợi (RBD / Multi-wire), Ủ Liên Tục, Phòng Khuôn PCD & Bể Nhũ Tương
- **[Trạm 03 (S03)](#tram-s03)** — Xưởng Bện Ruột Dẫn (Buncher Dây Mềm / Rigid Strander Cáp Lực / ACSR)
- **[Trạm 04 (S04)](#tram-s04)** — Xưởng Đùn Cách Điện (PVC / XLPE / CCV), Quấn Băng Mica FR & Lưu Hóa Khâu Mạch
- **[Trạm 05 (S05)](#tram-s05)** — Ghép Lõi (Drum Twister), Chống Thấm, Đan Lưới Chống Nhiễu & Bọc Giáp Thép (DSTA)
- **[Trạm 06 (S06)](#tram-s06)** — Đùn Vỏ Ngoài Hoàn Thiện (Sheathing), Làm Mát, In Phun Chữ & Kiểm Soát Trực Tuyến
- **[Trạm 07 (S07)](#tram-s07)** — Phòng Thí Nghiệm Kiểm Định Xuất Xưởng (Lab QA/QC & Hợp Quy QCVN 4 / IEC)
- **[Trạm 08 (S08)](#tram-s08)** — Đánh Cuộn, Cắt Đoạn (Cut-Length), Đóng Gói, Kho Thành Phẩm & Giao Hàng (OTIF)
- **[Trạm 09 (S09)](#tram-s09)** — Dòng Chảy Ngược: Thu Hồi Phế Liệu, Bảo Trì Cơ Điện (TPM/PdM) & Quyết Toán Giá Thành

### Phần II: 6 Lưu Trình Dòng Chảy Đặc Thù Theo Họ Sản Phẩm CADIVI (F01 → F06)
- **[Luồng A (F01)](#luong-f01)** — Dây Điện Dân Dụng (VC / VCm / VCmd 450/750V) — Sản Lượng Lớn, Tốc Độ Cao (MTS Pull)
- **[Luồng B (F02)](#luong-f02)** — Cáp Điện Lực Hạ Thế 0.6/1kV (CVV / CXV / CXV-DSTA) — MTO/ATO Cho Công Trình & Dự Án
- **[Luồng C (F03)](#luong-f03)** — Cáp Vặn Xoắn Treo Trên Không (ABC) & Dây Nhôm Trần Lõi Thép (ACSR) — Dự Án Điện Lực EVN
- **[Luồng D (F04)](#luong-f04)** — Cáp Điện Lực Trung Thế 24kV / 35kV (CXV/S/DSTA) — Công Nghệ Đỉnh Cao Ống Cong CCV
- **[Luồng E (F05)](#luong-f05)** — Cáp Chống Cháy & Ít Khói Không Halogen (FR / LSZH) — Chung Cư, Bệnh Viện, Sân Bay, Metro
- **[Luồng F (F06)](#luong-f06)** — Cáp Đặc Chủng: Cáp Điện Mặt Trời (Solar H1Z2Z2-K) & Cáp Điều Khiển Chống Nhiễu (Braiding)

### Phần III: Kho 40 Tình Huống Thực Chiến Hiện Trường & Kịch Bản Xử Lý OE (8 Nhóm)
- **1. Kế Hoạch, Đơn Gấp & Ùn Tắc Dòng Chảy** (5 tình huống): [SC01](#tinh-huong-sc01) · [SC02](#tinh-huong-sc02) · [SC03](#tinh-huong-sc03) · [SC04](#tinh-huong-sc04) · [SC05](#tinh-huong-sc05)
- **2. Xưởng Kéo Sợi, Ủ Đồng & Khuôn PCD** (5 tình huống): [SC06](#tinh-huong-sc06) · [SC07](#tinh-huong-sc07) · [SC08](#tinh-huong-sc08) · [SC09](#tinh-huong-sc09) · [SC10](#tinh-huong-sc10)
- **3. Xưởng Bện, Ghép Lõi & Bọc Giáp** (5 tình huống): [SC11](#tinh-huong-sc11) · [SC12](#tinh-huong-sc12) · [SC13](#tinh-huong-sc13) · [SC14](#tinh-huong-sc14) · [SC15](#tinh-huong-sc15)
- **4. Xưởng Đùn PVC / XLPE / LSZH / CCV** (5 tình huống): [SC16](#tinh-huong-sc16) · [SC17](#tinh-huong-sc17) · [SC18](#tinh-huong-sc18) · [SC19](#tinh-huong-sc19) · [SC20](#tinh-huong-sc20)
- **5. Chất Lượng Trực Tuyến, Lab & Khiếu Nại** (5 tình huống): [SC21](#tinh-huong-sc21) · [SC22](#tinh-huong-sc22) · [SC23](#tinh-huong-sc23) · [SC24](#tinh-huong-sc24) · [SC25](#tinh-huong-sc25)
- **6. Đóng Cuộn, Cut-Length, BOM & Phế Liệu** (5 tình huống): [SC26](#tinh-huong-sc26) · [SC27](#tinh-huong-sc27) · [SC28](#tinh-huong-sc28) · [SC29](#tinh-huong-sc29) · [SC30](#tinh-huong-sc30)
- **7. Bảo Trì, Năng Lượng & An Toàn LOTO** (5 tình huống): [SC31](#tinh-huong-sc31) · [SC32](#tinh-huong-sc32) · [SC33](#tinh-huong-sc33) · [SC34](#tinh-huong-sc34) · [SC35](#tinh-huong-sc35)
- **8. Con Người, Dữ Liệu MES & Văn Hóa Hiện Trường** (5 tình huống): [SC36](#tinh-huong-sc36) · [SC37](#tinh-huong-sc37) · [SC38](#tinh-huong-sc38) · [SC39](#tinh-huong-sc39) · [SC40](#tinh-huong-sc40)

---

# PHẦN I: SƠ ĐỒ TỔNG THỂ & 10 TRẠM DÒNG CHẢY KHÉP KÍN TẠI NHÀ MÁY CADIVI MIỀN TRUNG

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│  LƯU TRÌNH DÒNG CHẢY TỔNG THỂ KHÉP KÍN — NHÀ MÁY DÂY CÁP ĐIỆN CADIVI MIỀN TRUNG (HÒA CẦM)      │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘

  [DÒNG THÔNG TIN & LỆNH SẢN XUẤT (ERP / SAP PP / MES)]
   Khách hàng / Đại lý / EVN ──▶ S&OP (Tháng) ──▶ MPS & RCCP (Tuần) ──▶ MRP & CRP (Ca/Máy)
                                                                              │
  ════════════════════════════════════════════════════════════════════════════▼════════════════════
  [DÒNG CHẢY VẬT TƯ CHÍNH (MATERIAL & VALUE FLOW — TRẠM S01 → S08)]

   [S01: IQC & KHO NVL]     Đồng Rod Ø8.0 (ASTM B49), Nhôm Rod Ø9.5, Hạt PVC/XLPE/LSZH, Băng Thép/Mica
            │               (Kiểm IACS, độ ẩm, tỷ trọng CaCO3, cấp FIFO + Barcode lô)
            ▼
   [S02: KÉO SỢI & Ủ]       RBD (Ø8→1.38–3.5mm) ──▶ Multi-wire (→0.15–0.5mm) + Inline Annealing
            │               (Phòng khuôn PCD, bể nhũ tương Drawing Emulsion, hàn nối Butt Welder)
            ▼
   [S03: BỆN RUỘT DẪN]      Dây mềm Class 5: Buncher  │  Cáp lực Class 2: Rigid Strander (Ép nén)
            │               Dây nhôm trần/lõi thép: ACSR (+ bơm mỡ)
            ▼
   [S04: ĐÙN CÁCH ĐIỆN      PVC (dây VC/CV)  │  XLPE Silane ──▶ Phòng xông Sauna (4–12h)
      & KHÂU MẠCH]          Trung thế 24kV: CCV 3 lớp (Nitơ 12 bar)  │  Chống cháy: Quấn băng Mica FR
            │               Cáp Solar: Co-extrusion XLPO ──▶ Chiếu xạ E-beam
            ▼
   [S05: GHÉP LÕI, CHỐNG    Drum Twister (Ghép 3–4 lõi + độn) ──▶ Water-Blocking (chống thấm dọc)
     NHIỄU & BỌC GIÁP]      Braiding (đan lưới đồng/thiếc chống nhiễu) ──▶ DSTA / DATA (giáp thép/nhôm)
            ▼
   [S06: ĐÙN VỎ, IN CHỮ     Crosshead (Tubing) ──▶ Laser Gauge (Closed-loop) ──▶ Cooling Trough
     & KIỂM TRỰC TUYẾN]     ──▶ Air Wipe ──▶ Spark Tester (Cao áp) ──▶ In phun ──▶ Capstan đo mét
            ▼
   [S07: LAB QA/QC          Kelvin Bridge (R ở 20°C) · Water Immersion · Hot Set 200°C · Tensile
     XUẤT XƯỞNG]            Aging Oven (7 ngày) · Partial Discharge (≤5 pC) · Hợp quy QCVN 4 / IEC
            ▼
   [S08: ĐÁNH CUỘN, CẮT     Dây VC: Khoanh 100m + màng co  │  Cáp lực: Cắt đoạn Cut-Length lên Rulo gỗ
     ĐOẠN & GIAO HÀNG]      Tem QR truy xuất ──▶ Kho Thành phẩm ──▶ Giao hàng đúng hẹn OTIF
  ════════════════════════════════════════════════════════════════════════════╤════════════════════
                                                                              ▼
  [S09: DÒNG CHẢY NGƯỢC (REVERSE FLOW — PHẾ LIỆU, BẢO TRÌ & GIÁ THÀNH)]
   • Thu hồi 3 dòng phế: Đồng trần (~94% giá trị) │ Đồng dính nhựa (bóc tách) │ Nhựa Purge (Regrind)
   • Bảo trì Cơ Điện: PM định kỳ + CBM/PdM + LOTO 6 bước + Kho phụ tùng Kitting
   • Quyết toán SAP PP: Đối chiếu BOM Variance + Standard Cost + Báo cáo OEE/OLE/ROI về Ban Giám đốc
```

<a id="tram-s00"></a>
## Trạm 00 (S00): Dòng Thông Tin & Hoạch Định Sản Xuất (S&OP → MPS → MRP → RCCP → CRP → MES)
> 📍 **Khu vực / Phòng ban:** Phòng Kế Hoạch – Kinh Doanh – Mua Hàng – Ban Giám Đốc | 📖 **Cẩm nang sâu:** `planning_quality_ehs_cost` | 🎓 **Bài giáo trình:** [L5.1](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l5-1)

- **📥 Đầu vào (Input):** Đơn hàng đại lý/dự án EVN, dự báo bán hàng 3–12 tháng, dữ liệu tồn kho [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp), cây [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) & tốc độ máy (Routing).
- **📤 Đầu ra (Output):** Kế hoạch [MPS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mps) tuần, lệnh mua đồng/nhựa [MRP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mrp), lịch tải từng máy [CRP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crp) theo vòng màu [Color Sequencing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-color-sequencing) và Lệnh SX (Production Order) phát xuống phân xưởng.
- **⚙️ Máy móc & Phòng ban tham gia:** Hệ thống [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp) / [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp), phần mềm lập lịch Excel/[MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes); phối hợp Kinh doanh – Kế hoạch – Mua hàng – Quản đốc 4 xưởng – OE.

### ⚠️ Điểm Nghẽn & Tổn Thất Ẩn Thường Gặp
• Lập lịch [MRP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mrp) mù tải (không kiểm [RCCP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rccp) nhân [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) thực) khiến xưởng Đùn bị giao tải 125% rồi trễ hàng dây chuyền.
• Tồn kho ảo trên [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp) lệch thực tế kho 5–8% gây dừng máy chờ hạt nhựa hoặc mua dư tồn đọng vốn hàng tỷ đồng.
• Xếp lịch theo thứ tự đơn hàng chốt ngẫu nhiên (Đen → Trắng → Đen → Vàng) làm bùng nổ thời gian đổi mã [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) & nhựa xả [Purging](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-purging).
• Master Data (tốc độ chuẩn Routing, hệ số [Lay-up Factor](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lay-up-factor), tỷ lệ phế chuẩn) cũ kỹ 2–3 năm không cập nhật làm méo toàn bộ giá thành.

### 🚀 Chuyên Viên OE Làm Được Gì Từ Đầu Đến Cuối Tại Trạm Này?
1. **Kiểm toán Master Data (Đầu nguồn):** Đối chiếu tốc độ chuẩn Routing trên [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp) với tốc độ thực đo tại máy kéo/bện/đùn; rà soát hệ số [Lay-up Factor](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lay-up-factor) và tỷ lệ phế chuẩn trong cây [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom).
2. **Thiết kế mô hình kiểm tải [RCCP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rccp) & [CRP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crp):** Xây công cụ Excel/[Power BI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-power-bi) tự động nhân giờ kế hoạch với [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) thực từng máy cổ chai để báo sớm thiếu/dư tải trước 2–4 tuần.
3. **Áp luật [Campaign Scheduling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-campaign-scheduling) & [Color Sequencing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-color-sequencing):** Thống nhất với Kế hoạch & Kinh doanh vòng màu cố định (Trắng → Vàng → Xanh/Đỏ → Đen) và cơ chế chốt lịch đóng băng (Frozen Horizon 48–72 giờ) chống chen đơn phá chuyền.
4. **Thiết lập tồn kho khoa học:** Phân nhóm 9 ô [ABC-XYZ](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-abc-xyz), tính [Safety Stock](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-safety-stock) & điểm đặt hàng lại [ROP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rop) bằng công thức thống kê, thay đổi từ cảm tính sang kéo [Pull System](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pull-system) cho dây dân dụng nhóm AX.
5. **Gắn điểm chốt (Pacemaker):** Xác định rõ máy cổ chai [Bottleneck](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bottleneck) (thường là Xưởng Đùn) làm điểm phát nhịp [Drum-Buffer-Rope](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-buffer-rope) kéo ngược về Kéo & Bện.

**📊 Bộ KPI Mục Tiêu CADIVI:** Schedule Adherence (Tuân thủ lịch SX) ≥ 90% | Độ chính xác tồn kho RIA ≥ 98.5% | Giao hàng đúng hẹn OTIF ≥ 96% | Tỷ lệ đổi ngược màu Tối→Sáng < 1 lần/tuần.

**🔑 Từ khóa tra cứu nhanh:** [S&OP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-s-op) · [MPS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mps) · [MRP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mrp) · [RCCP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rccp) · [CRP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crp) · [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp) · [Campaign Scheduling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-campaign-scheduling) · [Color Sequencing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-color-sequencing) · [Safety Stock](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-safety-stock) · [ROP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rop) · [ABC-XYZ](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-abc-xyz)

---

<a id="tram-s01"></a>
## Trạm 01 (S01): Tiếp Nhận Nguyên Vật Liệu, Kiểm Đầu Vào (IQC) & Quản Trị Kho NVL
> 📍 **Khu vực / Phòng ban:** Kho Nguyên Vật Liệu – Phòng QA (IQC) – Phòng Mua Hàng | 📖 **Cẩm nang sâu:** `bom_cost` | 🎓 **Bài giáo trình:** [L5.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l5-2)

- **📥 Đầu vào (Input):** Cuộn đồng thanh Ø8.0mm (3–4 tấn/cuộn, chuẩn [ASTM B49](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-astm-b49)), nhôm thanh Ø9.5mm, bao hạt nhựa [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc)/[XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe)/[LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh)/[Masterbatch](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-masterbatch), cuộn băng thép [DSTA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dsta), băng [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr), [Water-Blocking](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-water-blocking).
- **📤 Đầu ra (Output):** NVL đã dán tem QR/Barcode đạt chuẩn IQC, phân khu sạch sẽ theo [FIFO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-fifo), sẵn sàng cấp đúng mẻ ([Kitting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kitting)) ra đầu vào các phân xưởng.
- **⚙️ Máy móc & Phòng ban tham gia:** Cầu trục/xe nâng hạng nặng, cầu đo [Kelvin Bridge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kelvin-bridge) kiểm % [IACS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iacs), cân tỷ trọng Specific Gravity, máy thử độ ẩm hạt nhựa, tủ thử [Tensile](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tensile); đội Kho NVL – QA IQC – Mua hàng – OE.

### ⚠️ Điểm Nghẽn & Tổn Thất Ẩn Thường Gặp
• Mua đồng Rod giá rẻ hơn 1 triệu/tấn nhưng % [IACS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iacs) chỉ 99.6% (thay vì 101.4%) → Xưởng phải kéo sợi to hơn tốn thêm 4.5 triệu/tấn đồng!
• Hạt nhựa [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc) bị độn quá nhiều bột đá [CaCO3 Filler](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-caco3-filler) làm tỷ trọng tăng từ 1.40 lên 1.52 g/cm³ → Dù đùn đúng chiều dày mm vẫn bị âm [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) +8.5% kg nhựa!
• Bao hạt [XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe) [Silane](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-silane) hoặc băng [Water-Blocking](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-water-blocking) bị rách/xé miệng ngoài không khí ẩm Đà Nẵng → Khâu mạch sớm trong phễu làm sần vỏ & bít lưới lọc.
• Không kiểm soát [FIFO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-fifo) và [Cycle Counting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cycle-counting) → Hạt nhựa quá hạn, cuộn đồng Rod bị cấn móp va chạm xe nâng gây đứt sợi hàng loạt ở Trạm 02.

### 🚀 Chuyên Viên OE Làm Được Gì Từ Đầu Đến Cuối Tại Trạm Này?
1. **Đánh giá TCO (Tổng chi phí sở hữu) cho Mua hàng:** Lập bảng so sánh đơn giá thực theo % [IACS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iacs) (đối với đồng Rod) và theo **VNĐ/lít thể tích** (Đơn giá/kg × Tỷ trọng đối với hạt [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc)/[XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe)).
2. **Chuẩn hóa cổng chặn IQC + [MOC / ECN](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-moc-ecn):** Mọi nhà cung cấp NVL mới bắt buộc qua thử nghiệm mẫu Pilot (đo IACS, Reverse Twist [ASTM B49](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-astm-b49), tỷ trọng, [Tensile](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tensile) & 7 ngày [Aging Oven](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-aging-oven)) trước khi nhập đại trà.
3. **Thiết kế [5S](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5s) & [FIFO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-fifo) kho NVL:** Phân làn riêng tuyệt đối khu Đồng vs khu Nhôm (chống bụi đồng ăn mòn nhôm!), khu nhựa chống ẩm đóng kín hút chân không cho bao [XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe)/[LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) dùng dở.
4. **Triển khai [Cycle Counting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cycle-counting) & [Two-Bin Kanban](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-two-bin-kanban):** Kiểm đếm luân phiên nhóm A hàng tuần giữ RIA ≥ 98.5%; áp [Two-Bin Kanban](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-two-bin-kanban) + xe [Milk Run](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-milk-run) cấp phát vật tư nhóm C (tem, màng co, [Masterbatch](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-masterbatch), găng tay).

**📊 Bộ KPI Mục Tiêu CADIVI:** Tỷ lệ lô NVL lỗi lọt xuống xưởng = 0% | Độ dẫn đồng Rod ≥ 100.8% [IACS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iacs) | Sai lệch tỷ trọng nhựa ≤ ±0.02 g/cm³ | Độ chính xác tồn kho RIA ≥ 98.5%.

**🔑 Từ khóa tra cứu nhanh:** [ASTM B49](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-astm-b49) · [IACS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iacs) · [CaCO3 Filler](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-caco3-filler) · [FIFO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-fifo) · [Cycle Counting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cycle-counting) · [Two-Bin Kanban](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-two-bin-kanban) · [Kitting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kitting) · [MOC / ECN](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-moc-ecn) · [Milk Run](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-milk-run)

---

<a id="tram-s02"></a>
## Trạm 02 (S02): Xưởng Kéo Sợi (RBD / Multi-wire), Ủ Liên Tục, Phòng Khuôn PCD & Bể Nhũ Tương
> 📍 **Khu vực / Phòng ban:** Phân Xưởng Kéo Sợi & Phòng Bảo Dưỡng Khuôn (Die Shop) | 📖 **Cẩm nang sâu:** `cable_extrusion_wire_forensics` | 🎓 **Bài giáo trình:** [L1.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l1-2)

- **📥 Đầu vào (Input):** Cuộn đồng Rod Ø8.0mm (hoặc Nhôm Rod Ø9.5mm), bộ khuôn kim cương [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd) đúng chuỗi giảm tiết diện, dung dịch nhũ tương [Drawing Emulsion](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drawing-emulsion).
- **📤 Đầu ra (Output):** Rulo sợi đồng/nhôm đạt chuẩn đường kính (±0.003–0.005mm), mềm dẻo (giãn dài ≥ 20–25% sau [Annealing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-annealing)), bề mặt sáng bóng không oxy hóa, sẵn sàng cấp cho Xưởng Bện/Đùn.
- **⚙️ Máy móc & Phòng ban tham gia:** Máy kéo thô [RBD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rbd) (tốc độ 20–32 m/s), máy kéo tinh đa sợi [Multi-wire](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-multi-wire) (8–24 sợi), bộ ủ [Annealing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-annealing) Inline / Lò chuông, máy hàn [Butt Welder](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-butt-welder), bộ xả/thu [Pay-off](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pay-off)/[Take-up](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-take-up); Tổ Kéo – Phòng Khuôn – Cơ điện – OE.

### ⚠️ Điểm Nghẽn & Tổn Thất Ẩn Thường Gặp
• **[Copper Give-away](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-copper-give-away):** Khuôn [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd) định cỡ cuối chạy quá tuổi thọ mòn thêm +0.008 mm → Đốt không +2.4% khối lượng đồng nguyên chất (hàng tỷ đồng/năm!).
• **Đứt sợi dừng máy (Wire Breaks):** Mỗi lần đứt trên máy [RBD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rbd) mất 15–20 phút xâu lại 11 khuôn; trên [Multi-wire](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-multi-wire) 16 sợi chỉ 1 sợi đứt là cả 16 sợi phải dừng!
• **Lỗi ủ [Annealing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-annealing):** Đường cong điện áp ủ đáp ứng chậm lúc tăng/giảm tốc gây 40m dây cứng đầu/cuối rulo; hơi bảo vệ kém làm dây bị đen oxy hóa sau 24h.
• **Bể nhũ tương [Drawing Emulsion](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drawing-emulsion) suy thoái:** Tụt nồng độ dầu, nhiễm khuẩn tụt pH < 7.8, châm nước cứng gây đóng cặn bít khuôn & tăng điện năng [SEC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sec) kWh/tấn.
• **Cuốn rulo [Take-up](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-take-up) lỗi rải dây:** Xếp chéo lớp (Cross-over) gây kẹt đứt sợi dây chuyền sang Trạm 03!

### 🚀 Chuyên Viên OE Làm Được Gì Từ Đầu Đến Cuối Tại Trạm Này?
1. **Triển khai pháp y đứt sợi [Wire Break Forensics](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wire-break-forensics):** Đặt bảng mẫu nhận diện 6 hình thái đầu gãy ([Cup-and-Cone](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cup-and-cone), hàn [Butt Welder](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-butt-welder), cháy hồ quang tang ủ, xước khuôn [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd)) + giữ 100% mẫu đứt chạy [Pareto](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pareto) 80/20 hàng tuần.
2. **Quản trị vòng đời khuôn [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd) & xóa [Copper Give-away](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-copper-give-away):** Lập hồ sơ từng mã khuôn (tấn kéo tối đa trước khi mang đi Re-polish), thay đồng bộ bộ Matched Die Set trên [Multi-wire](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-multi-wire) (dung sai ≤ 0.002mm), kéo tâm đường kính về sát chuẩn [IEC 60228](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60228) với [Cpk](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cpk) ≥ 1.33.
3. **Tối ưu [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) & [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) máy kéo:** Áp [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) thay cassette khuôn dự phòng đã lắp sẵn bên ngoài (40p → 11p), chuẩn hóa [SOP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sop) hàn [Butt Welder](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-butt-welder) + test bẻ 90° đầu ca, vẽ [Man-Machine Chart](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-man-machine-chart) cho 1 thợ đứng 2–3 máy kéo tinh.
4. **Khóa chuẩn [Jishu Hozen](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jishu-hozen) bể nhũ tương & điện năng:** Đưa kiểm tra nồng độ khúc xạ kế + pH + độ dẫn nước DI vào Checklist đầu ca; đo [SEC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sec) (kWh/tấn) từng máy để phát hiện trượt puly/khuôn mòn sớm.

**📊 Bộ KPI Mục Tiêu CADIVI:** [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) máy RBD ≥ 78% | Tỷ lệ đứt sợi < 0.3 lần/tấn (RBD) & < 0.8 lần/tấn (Multi-wire) | [Copper Give-away](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-copper-give-away) ≤ +0.4% | Điện năng [SEC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sec) ổn định theo Baseline [ISO 50001](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iso-50001).

**🔑 Từ khóa tra cứu nhanh:** [RBD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rbd) · [Multi-wire](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-multi-wire) · [Annealing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-annealing) · [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd) · [Drawing Emulsion](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drawing-emulsion) · [Butt Welder](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-butt-welder) · [Wire Break Forensics](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wire-break-forensics) · [Cup-and-Cone](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cup-and-cone) · [Copper Give-away](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-copper-give-away) · [IEC 60228](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60228)

---

<a id="tram-s03"></a>
## Trạm 03 (S03): Xưởng Bện Ruột Dẫn (Buncher Dây Mềm / Rigid Strander Cáp Lực / ACSR)
> 📍 **Khu vực / Phòng ban:** Phân Xưởng Bện Ruột Dẫn | 📖 **Cẩm nang sâu:** `ole` | 🎓 **Bài giáo trình:** [L2.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l2-3)

- **📥 Đầu vào (Input):** Các rulo sợi đồng mềm/cứng hoặc sợi nhôm/thép từ Trạm 02 (đồng bộ chiều dài và đường kính), mỡ chống ăn mòn (với [ACSR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-acsr)).
- **📤 Đầu ra (Output):** Rulo ruột dẫn đồng/nhôm đạt chuẩn cấu trúc cấp 2 (ép nén tròn hoặc rẻ quạt) hoặc cấp 5 (mềm dẻo), đúng bước xoắn [Lay-up Factor](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lay-up-factor), đúng điện trở DC [IEC 60228](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60228).
- **⚙️ Máy móc & Phòng ban tham gia:** Máy bện xoắn đôi tốc độ cao [Buncher](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-buncher), máy bện lồng cứng [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander) (1+6+12+18+24 = 61 sợi) kèm bộ ép nén Compacting Roller, cần trục nạp rulo; Tổ Bện – Kho bán thành phẩm – OE.

### ⚠️ Điểm Nghẽn & Tổn Thất Ẩn Thường Gặp
• **Thay nạp rulo [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander) cực lâu:** Thay thủ công 37–61 rulo vào lồng quay mất 60–90 phút, chiếm tới 25% thời gian ca!
• **Chiều dài các rulo nạp không đồng đều:** Rulo ngắn nhất hết trước buộc dừng cả máy 61 sợi để nối dây hoặc bỏ phế hàng trăm mét đồng trên 36 rulo còn lại.
• **Bước xoắn (Lay Length) chỉnh quá ngắn:** Làm tăng hệ số [Lay-up Factor](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lay-up-factor) thêm +1.0–1.5%, âm thầm mất thêm 1.5% đồng cho cả đơn hàng mà không ai để ý!
• **Lãng phí lao động ([OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) thấp):** 1 thợ chỉ đứng canh 1–2 máy [Buncher](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-buncher) vì thiếu cảm biến tự dừng [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka) và hay bị rối xả [Pay-off](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pay-off) (lỗi Birdcaging).
• **Lẫn chiều dài rulo WIP:** Ùn tắc hàng chục rulo ruột đồng chờ giữa Xưởng Bện và Xưởng Đùn làm chật lối đi và dễ oxy hóa.

### 🚀 Chuyên Viên OE Làm Được Gì Từ Đầu Đến Cuối Tại Trạm Này?
1. **Triển khai [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) nạp lồng [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander):** Soạn sẵn đồng bộ 100% rulo bằng chiều dài (Equal-length Kitting) trên giá xe đẩy bên ngoài trước khi máy dừng + phối hợp 2 người kiểu Pit-stop rút thời gian nạp từ 72p xuống ~24p!
2. **Vẽ [Man-Machine Chart](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-man-machine-chart) nâng vọt [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) khu [Buncher](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-buncher):** Phối hợp Cơ Điện lắp đủ cảm biến đứt sợi + cảm biến rung + đèn [Andon](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-andon) trên cao để 1 công nhân vận hành an toàn 4–6 máy [Buncher](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-buncher) (tăng [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) từ ~52% lên ≥ 78%).
3. **Kiểm toán bước xoắn [Lay-up Factor](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lay-up-factor) & độ nén Compact:** Đo kiểm tra bước xoắn thực tế so với bản vẽ [IEC 60228](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60228) (giữ sát cận dài cho phép để tiết kiệm đồng tối đa mà ruột vẫn chắc đẹp!); tối ưu đường kính ruột ép nén giúp giảm 8–10% nhựa bọc ở Trạm 04!
4. **Giới hạn WIP bằng ô sàn [Kanban](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kanban) / [Pull System](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pull-system):** Sơn vạch ô sàn cố định (vd: tối đa 10 rulo VC 2.5 giữa Bện & Đùn) — đủ ô thì chuyển mã khác, xóa cảnh đẩy dồn cục.

**📊 Bộ KPI Mục Tiêu CADIVI:** [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) Rigid Strander ≥ 72% | [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) khu Buncher ≥ 78% (1 người / 4–6 máy) | Thời gian nạp lồng < 25 phút | Phế đồng đuôi rulo bện < 0.4%.

**🔑 Từ khóa tra cứu nhanh:** [Buncher](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-buncher) · [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander) · [ACSR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-acsr) · [Lay-up Factor](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lay-up-factor) · [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) · [Man-Machine Chart](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-man-machine-chart) · [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) · [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka) · [Kanban](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kanban) · [Pull System](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pull-system)

---

<a id="tram-s04"></a>
## Trạm 04 (S04): Xưởng Đùn Cách Điện (PVC / XLPE / CCV), Quấn Băng Mica FR & Lưu Hóa Khâu Mạch
> 📍 **Khu vực / Phòng ban:** Phân Xưởng Đùn Cách Điện – Phòng Xông Sauna – Khu Quấn Băng Mica – Dây Chuyền CCV | 📖 **Cẩm nang sâu:** `smed` | 🎓 **Bài giáo trình:** [L3.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l3-3)

- **📥 Đầu vào (Input):** Rulo ruột dẫn từ Trạm 03, hạt nhựa cách điện [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc) / [XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe) ([Silane](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-silane) + 5% Catalyst) / XLPE Peroxide siêu sạch, [Masterbatch](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-masterbatch) màu, băng [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr).
- **📤 Đầu ra (Output):** Rulo lõi cách điện đồng tâm ≥ 92%, đủ chiều dày [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502), 0 lỗi [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester), đạt khâu mạch [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test) (với XLPE/Solar).
- **⚙️ Máy móc & Phòng ban tham gia:** Máy đùn [Extruder](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-extruder) ([L/D Ratio](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-l-d-ratio) 20:1–28:1), đầu chữ T [Crosshead](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crosshead), [Hopper Dryer](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hopper-dryer), [Laser Gauge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-laser-gauge), [Cooling Trough](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cooling-trough), [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester), phòng xông hơi Sauna, dây chuyền [CCV](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ccv) khí Nitơ, máy quấn băng [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr); Tổ Đùn – Kỹ thuật Công nghệ – OE.

### ⚠️ Điểm Nghẽn & Tổn Thất Ẩn Thường Gặp
• **Nút thắt công suất ([Bottleneck](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bottleneck)) số 1 toàn nhà máy:** Mọi phút dừng máy đùn đều làm mất thẳng sản lượng xuất xưởng của cả CADIVI!
• **Đổi màu / đổi tiết diện cực lâu (45–60 phút)** & xả 20–30 kg nhựa [Purging](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-purging) + hàng chục mét dây đồng dính nhựa cực đắt (mất 30% giá trị đồng thu hồi!).
• **[Over-thickness](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-over-thickness) nhựa cách điện (+8% đến +15%):** Do lệch tâm [Crosshead](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crosshead), dao động [Melt Pressure](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-melt-pressure) (Surging) hoặc công nhân cài dư cho 'chắc ăn đỡ rớt t_min'.
• **Khuyết tật đùn buộc hạ tốc độ:** Sần da cá mập [Sharkskin](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sharkskin), tắc lưới [Screen Pack](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-screen-pack), cặn [Die Drool](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-die-drool), nước làm mát nóng mùa hè Đà Nẵng.
• **Ùn tắc WIP ở Phòng Xông Sauna [Silane](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-silane):** Chờ gom đủ 12 rulo mới bật lò và cài dư thời gian xông (10h thay vì 6h) kéo dài [Lead Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lead-time) thêm 2–3 ngày!

### 🚀 Chuyên Viên OE Làm Được Gì Từ Đầu Đến Cuối Tại Trạm Này?
1. **Tấn công số 1 bằng [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) + [Color Sequencing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-color-sequencing) + [Purging](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-purging):** Quay video tách Thao tác Ngoài (tủ sấy sẵn Chày–Cối bên ngoài, phễu sấy di động, xe đồ nghề [5S](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5s) Shadow Board), đầu [Crosshead](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crosshead) tự định tâm, nạp Recipe 1-chạm trên [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi), lịch vòng màu Sáng → Tối → Rút đổi mã 55p → 12–15p (-75%)!
2. **Dự án [Six Sigma](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-six-sigma) [DMAIC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dmaic) xóa [Over-thickness](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-over-thickness):** Ổn định [Melt Pressure](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-melt-pressure) (thay [Screen Pack](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-screen-pack) chủ động, chỉnh nhiệt vùng cấp liệu), lắp vòng kín [Laser Gauge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-laser-gauge) → [Capstan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-capstan), kéo σ chiều dày từ 0.06mm xuống ≤ 0.02mm rồi mới dịch tâm Target Shift xuống sát t_nom (giữ [Cpk](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cpk) ≥ 1.50 theo [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502))!
3. **Chạy liên tục không dừng trên dây dân dụng:** Lắp [Pay-off](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pay-off) đôi (Dual Pay-off) + [Accumulator](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-accumulator) + [Take-up](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-take-up) đôi xóa sổ 100% dừng vặt đổi rulo.
4. **Giải phóng nút thắt Sauna & tối ưu [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr):** Dùng [DOE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-doe) + [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test) rút thời gian xông đúng theo chiều dày lớp nhựa; hiệu chuẩn góc quấn [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr) về đúng chồng mép 40% (tránh quấn dư 60% tốn băng & tốn XLPE bọc ngoài!).
5. **Phân tuyến đúng [L/D Ratio](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-l-d-ratio) & giữ [CCV](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ccv) chạy dài ngày:** Khóa cứng máy L/D 20:1 chạy PVC, L/D 26:1 chạy XLPE; gom đơn trung thế chạy Campaign 5–7 ngày liên tục trên [CCV](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ccv).

**📊 Bộ KPI Mục Tiêu CADIVI:** [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) máy đùn cổ chai ≥ 75% | Thời gian đổi màu < 15 phút | [Over-thickness](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-over-thickness) ≤ +2.5% | [Cpk](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cpk) đường kính ≥ 1.33–1.67 | Phế đồng dính nhựa < 0.5%.

**🔑 Từ khóa tra cứu nhanh:** [Extruder](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-extruder) · [Crosshead](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crosshead) · [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) · [Over-thickness](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-over-thickness) · [Laser Gauge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-laser-gauge) · [Melt Pressure](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-melt-pressure) · [Sharkskin](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sharkskin) · [Silane](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-silane) · [CCV](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ccv) · [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr) · [L/D Ratio](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-l-d-ratio)

---

<a id="tram-s05"></a>
## Trạm 05 (S05): Ghép Lõi (Drum Twister), Chống Thấm, Đan Lưới Chống Nhiễu & Bọc Giáp Thép (DSTA)
> 📍 **Khu vực / Phòng ban:** Phân Xưởng Hoàn Thiện Cáp Lực & Cáp Đặc Chủng | 📖 **Cẩm nang sâu:** `cable_mfg_machines` | 🎓 **Bài giáo trình:** [L1.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l1-3)

- **📥 Đầu vào (Input):** 3–4 rulo lõi cách điện (Đỏ–Vàng–Xanh–Đen) từ Trạm 04, sợi độn PP, băng/sợi [Water-Blocking](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-water-blocking), suốt sợi đồng/thiếc cho [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding), cuộn băng thép mạ kẽm [DSTA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dsta) hoặc băng nhôm DATA.
- **📤 Đầu ra (Output):** Bó lõi cáp tròn đều chắc chắn, đủ độ che phủ lưới chống nhiễu (≥ 85%), đủ độ phủ giáp thép/nhôm 100% không hở khe, sẵn sàng đùn lớp vỏ hoàn thiện Trạm 06.
- **⚙️ Máy móc & Phòng ban tham gia:** Máy ghép lõi [Drum Twister](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-twister) (hoặc Planetary Strander), dàn máy đan lưới [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding) (16–36 suốt), máy quấn giáp băng thép [DSTA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dsta)/DATA; Tổ Ghép Lõi – Tổ Giáp – OE.

### ⚠️ Điểm Nghẽn & Tổn Thất Ẩn Thường Gặp
• **Lệch chiều dài 4 rulo lõi vào [Drum Twister](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-twister):** Rulo 1 dài 1,050m, rulo 2 dài 1,020m, rulo 3 dài 990m, rulo 4 dài 1,075m → Cáp thành phẩm chỉ dài 990m, buộc cắt bỏ lãng phí **175m lõi đồng bọc XLPE cực đắt**!
• **Quấn sai bước xoắn ghép lõi hoặc lệch hướng lõi rẻ quạt:** Gây tăng [Lay-up Factor](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lay-up-factor) (tốn đồng + nhựa) hoặc cáp méo gồ ghề làm tốn nhựa vỏ ngoài ở Trạm 06.
• **Máy quấn giáp [DSTA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dsta) dừng hàn băng liên tục:** Dùng cuộn băng thép dạng bánh nhỏ (400m) phải dừng hàn 4–5 lần trên 1 rulo cáp!
• **Nút thắt [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding) cực chậm & đan thừa mật độ:** Chỉnh mật độ phủ 93% (chuẩn chỉ ≥ 85%) làm tốc độ máy chậm đi -22% và tốn thêm +14% đồng mạ thiếc [Tinned Copper](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tinned-copper)!

### 🚀 Chuyên Viên OE Làm Được Gì Từ Đầu Đến Cuối Tại Trạm Này?
1. **Khóa đồng bộ chiều dài 4 rulo từ Trạm 04:** Kết nối [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes) & hiệu chuẩn định kỳ bánh đo mét máy đùn để 4 rulo cùng lệnh lệch nhau ≤ ±5m → Triệt tiêu 85% phế lõi lẻ tại [Drum Twister](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-twister)!
2. **Chuyển đổi sang cuộn băng thép khổ lớn (Traverse Wound Coil 2,500m):** Cắt 80% số lần dừng hàn nối trên máy bọc giáp [DSTA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dsta), nâng [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) từ 58% lên ~74%.
3. **Tối ưu [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding) (1 người 6–10 máy + đúng mật độ 87%):** Quấn đồng bộ chiều dài toàn bộ 24 suốt Bobbin bằng nhau (không để hết lẻ từng suốt!), gắn cảm biến đứt sợi [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka) và chỉnh bánh răng bước đan về mục tiêu 87%.
4. **Kiểm soát kho kín chống ẩm cho [Water-Blocking](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-water-blocking) & Poka-Yoke phân biệt DSTA vs DATA:** Dán mã cảnh báo cấm tuyệt đối quấn băng thép [DSTA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dsta) lên cáp 1 lõi xoay chiều (tránh dòng điện xoáy làm nóng chảy cáp!).

**📊 Bộ KPI Mục Tiêu CADIVI:** Độ lệch chiều dài 4 rulo lõi ≤ ±0.5% | [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) Drum Twister & DSTA ≥ 72% | [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) cụm máy Braiding ≥ 80% | Phế lõi thừa < 0.6%.

**🔑 Từ khóa tra cứu nhanh:** [Drum Twister](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-twister) · [DSTA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dsta) · [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding) · [Water-Blocking](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-water-blocking) · [Lay-up Factor](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lay-up-factor) · [Tinned Copper](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tinned-copper) · [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka) · [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes)

---

<a id="tram-s06"></a>
## Trạm 06 (S06): Đùn Vỏ Ngoài Hoàn Thiện (Sheathing), Làm Mát, In Phun Chữ & Kiểm Soát Trực Tuyến
> 📍 **Khu vực / Phòng ban:** Phân Xưởng Đùn Vỏ Hoàn Thiện (PVC / HDPE / LSZH) | 📖 **Cẩm nang sâu:** `cable_extrusion_wire_forensics` | 🎓 **Bài giáo trình:** [L4.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l4-4)

- **📥 Đầu vào (Input):** Bó lõi đã ghép/bọc giáp từ Trạm 05, hạt nhựa vỏ [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc) / [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) / HDPE đã sấy kỹ qua [Hopper Dryer](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hopper-dryer), bộ Chày–Cối kiểu Tubing đúng [DDR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ddr), mực máy in phun.
- **📤 Đầu ra (Output):** Rulo cáp thành phẩm hoàn chỉnh, bề mặt bóng mịn không [Sharkskin](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sharkskin)/[Die Drool](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-die-drool), chữ in sắc nét đúng quy chuẩn, đủ chiều dài mét chính xác, 0 lỗi [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester).
- **⚙️ Máy móc & Phòng ban tham gia:** Máy đùn vỏ cỡ lớn (Ø120–Ø150mm), đầu [Crosshead](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crosshead) Tubing, [Laser Gauge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-laser-gauge), máng nước [Cooling Trough](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cooling-trough) + Chiller, bộ thổi khô Air Wipe, [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester), máy in phun công nghiệp, [Capstan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-capstan) Caterpillar + Encoder đo mét; Tổ Đùn Vỏ – QC – OE.

### ⚠️ Điểm Nghẽn & Tổn Thất Ẩn Thường Gặp
• **Chọn sai bộ Chày–Cối (lắp nhầm Pressure thay vì Tubing hoặc sai [DDR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ddr)):** Làm vỏ bám dính cứng vào lõi (khách hàng không tuốt được vỏ trả hàng!) hoặc rách ống nhựa liên tục khi chạy [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh).
• **Máng nước [Cooling Trough](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cooling-trough) quá nóng buổi trưa Đà Nẵng (34°C):** Vỏ cáp ra khỏi máng còn mềm 55°C bị bết dính rulo → Công nhân tự hạ tốc độ máy đùn -20% (tụt [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) Performance nặng!).
• **Bánh xe đo mét [Capstan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-capstan) mòn không hiệu chuẩn:** Sai số +0.8% khiến nhà máy tự động 'tặng không' 40 km dây đồng/tháng — hoặc sai số âm -0.5% làm khách hàng kiện thiếu mét!
• **Máy in phun hết mực/nhòe chữ ca đêm:** Chạy hổng hàng chục km cáp không có chữ thương hiệu CADIVI phải tuốt bỏ hoặc chạy in lại tốn kém.

### 🚀 Chuyên Viên OE Làm Được Gì Từ Đầu Đến Cuối Tại Trạm Này?
1. **Lập Bảng chọn Chày–Cối chuẩn [DDR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ddr) + [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) khắc mã 'T'/'P':** Chuẩn hóa bảng Excel tra đúng [DDR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ddr) (PVC: 1.5–2.5; LSZH: 1.1–1.6) và khắc laser ký hiệu + sơn màu chống lắp nhầm kiểu Pressure/Tubing.
2. **Xử lý nút thắt nhiệt độ [Cooling Trough](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cooling-trough) & [Die Drool](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-die-drool):** Giám sát nhiệt độ nước máng trên [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada) (giữ ≤ 25°C, làm mát phân tầng cho vỏ dày), lắp biến tần [VFD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-vfd) tiết kiệm điện bơm tuần hoàn, cấp dao đồng thau chống xước miệng khuôn Cối.
3. **Gắn [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) cho Máy in phun & [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester):** Lắp cảm biến quang kiểm tra độ tương phản chữ in tự dừng sau 5m mất chữ; cài ngưỡng tự dừng máy trên [PLC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-plc) khi [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester) báo ≥ 2 lỗi/500m và kiểm tra nối đất đầu ca.
4. **Hiệu chuẩn định kỳ bánh đo mét [Capstan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-capstan):** Đưa kiểm chuẩn sai số mét (≤ ±0.2%) bằng thước chuẩn vào lịch [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) hàng tuần và [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa).

**📊 Bộ KPI Mục Tiêu CADIVI:** [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) Đùn vỏ ≥ 74% | Độ đồng tâm vỏ ≥ 90% | Sai số chiều dài mét ≤ ±0.2% | Lỗi chữ in / bết vỏ = 0 cuộn | Thời gian dừng cạo [Die Drool](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-die-drool) < 1 lần/ca.

**🔑 Từ khóa tra cứu nhanh:** [DDR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ddr) · [Crosshead](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crosshead) · [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) · [Hopper Dryer](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hopper-dryer) · [Die Drool](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-die-drool) · [Cooling Trough](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cooling-trough) · [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester) · [Capstan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-capstan) · [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) · [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada)

---

<a id="tram-s07"></a>
## Trạm 07 (S07): Phòng Thí Nghiệm Kiểm Định Xuất Xưởng (Lab QA/QC & Hợp Quy QCVN 4 / IEC)
> 📍 **Khu vực / Phòng ban:** Phòng Thí Nghiệm Kiểm Tra Chất Lượng (Lab QA/QC) | 📖 **Cẩm nang sâu:** `minitab_spc` | 🎓 **Bài giáo trình:** [L4.5](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l4-5)

- **📥 Đầu vào (Input):** Mẫu cắt đầu/cuối rulo và cuộn cáp thành phẩm từ Trạm 02–06 kèm Phiếu lệnh SX / Mã QR truy xuất.
- **📤 Đầu ra (Output):** Phiếu kết quả thử nghiệm (Test Report) đạt chuẩn [IEC 60228](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60228), [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502), [QCVN 4](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-qcvn-4) (mở khóa trạng thái trên [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp) cho phép nhập kho & xuất hàng) — hoặc Phiếu NCR cách ly lô lỗi kích hoạt [8D](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-8d).
- **⚙️ Máy móc & Phòng ban tham gia:** Cầu đo [Kelvin Bridge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kelvin-bridge), bể thử cao áp [Water Immersion](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-water-immersion), tủ thử [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test) 200°C, máy kéo vạn năng [Tensile](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tensile), tủ lão hóa [Aging Oven](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-aging-oven), phòng lồng Faraday đo [Partial Discharge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-partial-discharge), kính hiển vi đo chiều dày; Phòng Lab QA/QC – Kỹ thuật – OE.

### ⚠️ Điểm Nghẽn & Tổn Thất Ẩn Thường Gặp
• **Cổ chai chờ giấy xuất xưởng (Lab Lead Time 5–8 giờ):** Xưởng mang mẫu lên rải rác, Lab ngâm nước từng cuộn lẻ tẻ làm hàng chục rulo thành phẩm nằm chật xưởng chờ giao!
• **Sai số hệ thống đo ([MSA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-msa) / [Gage R&R](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-gage-r-r) > 30%):** Quên quy đổi nhiệt độ 20°C trên [Kelvin Bridge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kelvin-bridge) khi trưa nóng 30°C (báo rớt oan!), dao dập mẫu Dumbbell cùn làm đứt sớm giả tạo khi kéo [Tensile](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tensile).
• **Dữ liệu Lab 'ngủ yên trong sổ giấy':** Lab chỉ ghi Đạt/Không Đạt mà không nhập số đo liên tục (điện trở, chiều dày min, đường kính) cho OE phân tích [SPC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spc) & [Cpk](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cpk) → Bỏ lỡ hoàn toàn cơ hội giảm [Copper Give-away](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-copper-give-away) & [Over-thickness](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-over-thickness)!

### 🚀 Chuyên Viên OE Làm Được Gì Từ Đầu Đến Cuối Tại Trạm Này?
1. **Tối ưu dòng chảy Phòng Lab (giảm chờ từ 6h → 2h):** Thiết lập lịch gom mẫu cố định theo khung giờ (vd: 10h – 15h – 21h), bố trí 2 bể [Water Immersion](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-water-immersion) luân phiên (1 bể ngâm ủ 1h song song 1 bể đang thử cao áp — đúng tư duy [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed)!).
2. **Thẩm định độ tin cậy đo lường bằng [MSA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-msa) / [Gage R&R](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-gage-r-r):** Chạy [Gage R&R](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-gage-r-r) trên [Minitab](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-minitab) cho cầu [Kelvin Bridge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kelvin-bridge), thước đo chiều dày quang học và máy [Tensile](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tensile) (bắt buộc %GRR < 10% hoặc < 30%) trước mọi dự án [DMAIC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dmaic).
3. **Số hóa dữ liệu đo Lab tự động chảy về [Power BI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-power-bi) / [Minitab](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-minitab):** Thiết kế form Excel/Python tự động quy đổi điện trở về 20°C, vẽ ngay biểu đồ [SPC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spc) & tính [FPY](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-fpy) / [RTY](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rty) toàn chuỗi để cảnh báo xu hướng trôi trước khi rớt chuẩn [QCVN 4](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-qcvn-4)!
4. **Dẫn dắt xử lý sự cố chất lượng [8D](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-8d):** Khi có lô rớt [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test) hoặc [Partial Discharge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-partial-discharge), OE chủ trì truy ngược phả hệ lô trên [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes) để khoanh vùng đúng lô lỗi và dứt điểm nguyên nhân gốc.

**📊 Bộ KPI Mục Tiêu CADIVI:** Lab Lead Time ≤ 2 giờ | %GRR ([Gage R&R](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-gage-r-r)) < 15% | Tỷ lệ đạt lần đầu toàn chuỗi [RTY](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rty) ≥ 94% | Tỷ lệ khiếu nại khách hàng = 0 vụ nghiêm trọng.

**🔑 Từ khóa tra cứu nhanh:** [Kelvin Bridge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kelvin-bridge) · [Water Immersion](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-water-immersion) · [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test) · [Tensile](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tensile) · [Aging Oven](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-aging-oven) · [Partial Discharge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-partial-discharge) · [QCVN 4](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-qcvn-4) · [Gage R&R](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-gage-r-r) · [MSA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-msa) · [RTY](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rty) · [8D](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-8d)

---

<a id="tram-s08"></a>
## Trạm 08 (S08): Đánh Cuộn, Cắt Đoạn (Cut-Length), Đóng Gói, Kho Thành Phẩm & Giao Hàng (OTIF)
> 📍 **Khu vực / Phòng ban:** Tổ Đóng Cuộn – Khu Sang Rulo – Kho Thành Phẩm – Logistics | 📖 **Cẩm nang sâu:** `cable_cost_capacity` | 🎓 **Bài giáo trình:** [L2.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l2-4)

- **📥 Đầu vào (Input):** Rulo cáp thành phẩm đã được Lab Trạm 07 mở khóa đạt chuẩn, danh sách chiều dài cắt của từng đơn hàng dự án, rulo gỗ/thép, màng co, thùng carton, tem mã vạch QR.
- **📤 Đầu ra (Output):** Khoanh dây dân dụng 100m bọc màng co đẹp chuẩn hoặc rulo cáp lực cắt đúng mét dự án (kèm biên bản xuất xưởng & tem truy xuất QR), xếp xe giao đúng hẹn OTIF.
- **⚙️ Máy móc & Phòng ban tham gia:** Máy đánh khoanh tự động/bán tự động 100m + buồng co màng nhiệt, máy sang cuộn cắt đoạn (Rewinding & Cutting Machine) có [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester) kiểm tra lại, cân sàn điện tử, xe nâng; Tổ Đóng gói – Kho TP – Kế hoạch – OE.

### ⚠️ Điểm Nghẽn & Tổn Thất Ẩn Thường Gặp
• **Phế mẩu thừa [Cut-Length](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cut-length) cực đắt (5–10% đơn hàng dự án):** Cắt rulo theo thứ tự ngẫu nhiên để dư hàng loạt khúc cáp lực 40–150m không bán được, phải tuốt đồng bán phế!
• **Nút thắt lao động thủ công ([OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) thấp):** Tổ đóng khoanh 100m mất cân bằng chuyền (người quấn dây chạy kịp nhưng người bọc màng/dán tem bị ùn ứ chờ đợi), di chuyển thừa theo sơ đồ [Spaghetti](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spaghetti).
• **Lỗi giao nhầm mã/thiếu mét/hư hỏng rulo:** Dán nhầm tem nhãn giữa dây VC 2.5 và VC 4.0 hoặc xếp rulo gỗ nặng thiếu chèn khóa gây trầy xước vỏ khi vận chuyển.

### 🚀 Chuyên Viên OE Làm Được Gì Từ Đầu Đến Cuối Tại Trạm Này?
1. **Giải bài toán tối ưu [Cut-Length](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cut-length) bằng Excel Solver / [Python](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-python):** Gom toàn bộ các đoạn lẻ dự án để tìm tổ hợp cắt sát 100% chiều dài rulo và đẩy tổng chiều dài mục tiêu ngược về Trạm 03–04 ngay từ lúc phát lệnh → Giảm phế mẩu thừa từ 8% xuống < 1.2%!
2. **Cân bằng chuyền [Yamazumi](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-yamazumi) & [Time Study](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-time-study) tổ đóng khoanh 100m:** Đo [SAM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-time-study) từng thao tác (cuốn → cột dây → dán tem → bọc màng co → xếp pallet), gom/tách bước kéo Balance Efficiency ≥ 85%, bố trí Layout hình chữ U giảm 50% bước đi trên sơ đồ [Spaghetti](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spaghetti).
3. **Áp [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) quét mã vạch xuất kho:** Quét QR trên rulo khớp đúng lệnh xuất kho [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp) mới cho in phiếu giao hàng — xóa 100% lỗi giao nhầm mã dây/sai mét.
4. **Thiết lập siêu thị thành phẩm [Kanban](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kanban) cho dây dân dụng nhóm AX:** Kiểm soát mức tồn Min–Max tự động kích hoạt bổ sung để đại lý đặt là có hàng giao ngay trong 24h (OTIF ≥ 97%).

**📊 Bộ KPI Mục Tiêu CADIVI:** Phế cắt đoạn [Cut-Length](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cut-length) < 1.2% | [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) tổ đóng cuộn ≥ 82% | Balance Efficiency ≥ 85% | Giao hàng đúng đủ OTIF ≥ 96% | Sai sót giao nhầm = 0.

**🔑 Từ khóa tra cứu nhanh:** [Cut-Length](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cut-length) · [Yamazumi](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-yamazumi) · [Time Study](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-time-study) · [Time Study](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-time-study) · [Spaghetti](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spaghetti) · [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) · [Lead Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lead-time) · [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) · [Python](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-python)

---

<a id="tram-s09"></a>
## Trạm 09 (S09): Dòng Chảy Ngược: Thu Hồi Phế Liệu, Bảo Trì Cơ Điện (TPM/PdM) & Quyết Toán Giá Thành
> 📍 **Khu vực / Phòng ban:** Khu Tập Kết Phế Liệu – Phòng Cơ Điện (Bảo Trì) – Phòng Kế Toán Giá Thành | 📖 **Cẩm nang sâu:** `oe_field_execution_case_test` | 🎓 **Bài giáo trình:** [L6.1](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l6-1)

- **📥 Đầu vào (Input):** Phế liệu từ Trạm 02–08, yêu cầu sửa chữa & thẻ bất thường [Red Tag](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-red-tag)/Fuguai, dữ liệu sản lượng/vật tư/giờ máy/điện năng cuối ca & cuối tháng trên [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp) / [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes).
- **📤 Đầu ra (Output):** Đồng thu hồi giá trị cao nhất (~94%), nhựa sạch tái chế [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc) hợp chuẩn (Regrind), máy móc duy trì [MTBF](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mtbf) cao an toàn [LOTO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loto), và Báo cáo [Standard Cost](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-cost) Variance + [Cost Deployment](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cost-deployment) trình Ban Giám Đốc.
- **⚙️ Máy móc & Phòng ban tham gia:** Cân điện tử khu phế liệu, máy tuốt cáp/nghiền nhựa Regrind, thiết bị bảo trì [CBM / PdM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cbm-pdm) (camera ảnh nhiệt, bút đo rung, siêu âm rò khí nén), hệ thống [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp) / [Power BI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-power-bi); Cơ Điện – Kế Toán – EHS – OE.

### ⚠️ Điểm Nghẽn & Tổn Thất Ẩn Thường Gặp
• **Vứt lẫn 3 nhóm phế liệu ngay chân máy:** Vứt đồng trần (thu hồi ~94% giá trị) lẫn vào đồng dính nhựa (chỉ thu hồi ~65–70% sau tốn công bóc tách!) làm bốc hơi hàng trăm triệu đồng/năm!
• **Bảo trì kiểu 'chữa cháy' (Reactive > 50%):** [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) thấp (< 65%), [Wrench Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wrench-time) thợ Cơ Điện chỉ ~30% do đi tìm phụ tùng/chờ máy → Máy cổ chai hỏng đột xuất giữa mùa cao điểm!
• **Thất thoát năng lượng ẩn ([ISO 50001](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iso-50001)):** Rò rỉ khí nén kêu xì khắp xưởng (tốn 20–30% điện máy nén khí!), bơm nước giải nhiệt chạy hết công suất 50Hz lúc non tải ca đêm.
• **Đóng lệnh [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp) kiểu Backflushing mù:** Hệ thống tự trừ kho theo định mức chuẩn làm báo cáo cuối tháng luôn 'đẹp như mơ = 0%', đến cuối năm kiểm kê kho mới tá hỏa hụt hàng chục tấn đồng!

### 🚀 Chuyên Viên OE Làm Được Gì Từ Đầu Đến Cuối Tại Trạm Này?
1. **Phân luồng 3 thùng phế mã màu [5S](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5s) + Tách Reason Code trên [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp):** Xanh = Đồng trần tinh khiết | Vàng = Đồng dính nhựa | Xám = Nhựa purge sạch tái chế; bắt buộc cân phế thực tế cuối ca đối chiếu [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) (cấm Backflush mù!).
2. **Nâng cấp Bảo trì [TPM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tpm) + [CBM / PdM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cbm-pdm) + [Wrench Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wrench-time):** Chốt 'Cửa sổ Bảo trì Vàng' vào lịch [MPS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mps) đẩy [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) ≥ 90%; soạn sẵn bộ [Kitting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kitting) phụ tùng PM tăng [Wrench Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wrench-time) từ 32% lên ≥ 50%; soi camera ảnh nhiệt tủ điện hàng tháng & bắt buộc [LOTO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loto) 6 bước.
3. **Chạy [Cost Deployment](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cost-deployment) & [OEE Waterfall](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loss-tree) quy mọi tổn thất ra tiền VNĐ:** Phối hợp Kế toán tách rạch ròi Price Variance (giá đồng thị trường) vs Usage Variance (năng lực xưởng & OE), xác nhận Hard Savings thật cho mọi dự án [ROI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-roi) / [Payback](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-payback).
4. **Khóa hệ thống duy trì toàn nhà máy:** Vận hành nhịp nhàng họp tầng Tier 1–2–3, [LSW](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lsw), kiểm tra phân tầng [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa) và Ma trận leo thang sự cố [Escalation Matrix](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-escalation-matrix) (5p–15p–30p) để mọi thành quả bền vững vĩnh viễn!

**📊 Bộ KPI Mục Tiêu CADIVI:** Tỷ lệ thu hồi đồng trần riêng biệt ≥ 95% | [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) ≥ 90% | [Wrench Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wrench-time) ≥ 50% | Giảm điện năng [SEC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sec) -5 đến -10%/năm | 0 tai nạn vi phạm [LOTO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loto).

**🔑 Từ khóa tra cứu nhanh:** [Scrap](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scrap) · [Standard Cost](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-cost) · [Cost Deployment](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cost-deployment) · [Loss Tree](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loss-tree) · [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) · [Wrench Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wrench-time) · [CBM / PdM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cbm-pdm) · [LOTO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loto) · [ISO 50001](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iso-50001) · [LSW](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lsw) · [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa) · [Escalation Matrix](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-escalation-matrix)

---

# PHẦN II: 6 LƯU TRÌNH DÒNG CHẢY ĐẶC THÙ THEO HỌ SẢN PHẨM CHỦ LỰC CỦA CADIVI

<a id="luong-f01"></a>
## Luồng A (F01): Dây Điện Dân Dụng (VC / VCm / VCmd 450/750V) — Sản Lượng Lớn, Tốc Độ Cao (MTS Pull)
> 📖 **Cẩm nang sâu:** `oee` | 🎓 **Bài giáo trình:** [L1.1](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l1-1)

- **📦 Sản phẩm điển hình:** Dây đơn cứng VC 1.5 / 2.5 / 4.0 / 6.0 mm²; Dây mềm VCm 1.5 / 2.5 mm²; Dây đôi mềm dẹt VCmd 2×1.5 mm² (chuẩn [QCVN 4](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-qcvn-4)).

### 🗺️ Sơ Đồ Đường Đi Công Nghệ
```text
Đồng Rod Ø8.0mm (IQC ASTM B49)
   │
   ▼
[S02] Kéo thô RBD (→ Ø1.38–2.0mm) ──▶ Kéo tinh Multi-wire (→ Ø0.25–0.67mm) + Ủ Annealing
   │
   ▼
[S03] Bện ruột mềm trên máy Buncher (bỏ qua nếu dây đơn đặc VC Class 1)
   │
   ▼
[S04/S06] Đùn bọc cách điện PVC tốc độ cao (300–800 m/phút) + Laser Gauge + Spark Tester + In chữ
   │
   ▼
[S08] Đánh khoanh chuẩn 100m + Bọc màng co + Dán tem QR ──▶ [S07] Lab QCVN 4 ──▶ Kho siêu thị đại lý
```

- **🔴 Điểm nghẽn cổ chai đặc trưng:** Máy đùn [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc) tốc độ cao (bị kéo tụt [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) bởi đổi màu liên tục và dừng thay rulo xả/thu) + Khâu đánh khoanh đóng gói 100m (tốn nhân công).
- **💸 Tổn thất lớn nhất:** 1. [Copper Give-away](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-copper-give-away) (sản lượng cực lớn nên thừa +0.008mm mất hàng tỷ đồng!) · 2. Phế đổi màu & dừng thay rulo · 3. Sai số mét bánh đo [Capstan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-capstan) (tặng thừa mét trên hàng chục nghìn khoanh 100m!) · 4. Lãng phí nhân công [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) ở khu Buncher & đóng khoanh.

### 🚀 Chiến Lược Hành Động Trọng Điểm Của OE
• **Dòng chảy Kéo ([Pull System](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pull-system) / [Kanban](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kanban)):** Vì dây VC bán đều quanh năm (nhóm AX trong [ABC-XYZ](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-abc-xyz)), lập siêu thị thành phẩm & ô sàn Kanban giữa Bện ↔ Đùn thay vì đẩy lô khổng lồ.
• **Biến máy đùn thành dòng chảy liên tục:** Lắp [Pay-off](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pay-off) đôi + [Accumulator](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-accumulator) + [Take-up](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-take-up) tự động kết hợp luật vòng màu [Color Sequencing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-color-sequencing) (Trắng → Vàng → Xanh → Đỏ → Đen).
• **Tối ưu [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) tối đa:** Vẽ [Man-Machine Chart](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-man-machine-chart) cho 1 công nhân đứng 4–6 máy [Buncher](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-buncher); cân bằng chuyền [Yamazumi](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-yamazumi) tổ đóng khoanh 100m đạt Balance Efficiency ≥ 85%.
• **Chặn thất thoát từng milimet:** Siết tuổi thọ khuôn [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd) giảm [Copper Give-away](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-copper-give-away) về ≤ +0.4%, hiệu chuẩn [Capstan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-capstan) sai số ≤ ±0.2% và đảm bảo 100% đạt [QCVN 4](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-qcvn-4).

**🔑 Từ khóa tra cứu nhanh:** [QCVN 4](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-qcvn-4) · [RBD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rbd) · [Multi-wire](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-multi-wire) · [Buncher](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-buncher) · [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc) · [Color Sequencing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-color-sequencing) · [Accumulator](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-accumulator) · [Copper Give-away](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-copper-give-away) · [Yamazumi](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-yamazumi) · [Kanban](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kanban)

---

<a id="luong-f02"></a>
## Luồng B (F02): Cáp Điện Lực Hạ Thế 0.6/1kV (CVV / CXV / CXV-DSTA) — MTO/ATO Cho Công Trình & Dự Án
> 📖 **Cẩm nang sâu:** `cable_cost_capacity` | 🎓 **Bài giáo trình:** [L3.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l3-2)

- **📦 Sản phẩm điển hình:** Cáp 3–4 lõi cách điện [XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe) vỏ [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc): CXV 3×50+1×25, CXV 3×120+1×70, CXV/DSTA 3×240+1×120 (chuẩn [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502)-1).

### 🗺️ Sơ Đồ Đường Đi Công Nghệ
```text
Đồng Rod Ø8.0mm (IQC)
   │
   ▼
[S02] Kéo thô RBD (→ Ø1.7–3.2mm) + Ủ Annealing
   │
   ▼
[S03] Bện lồng cứng Rigid Strander (ép nén tròn Compact hoặc rẻ quạt Sector Class 2)
   │
   ▼
[S04] Đùn cách điện XLPE Silane (95% nền + 5% Catalyst) ──▶ ★ PHÒNG XÔNG HƠI SAUNA (4–12h) ★
   │
   ▼
[S05] Ghép 3–4 lõi trên Drum Twister (+ sợi độn + băng quấn) ──▶ Bọc đệm & Giáp thép DSTA (nếu có)
   │
   ▼
[S06] Đùn vỏ ngoài PVC (Crosshead Tubing) + In chữ ──▶ [S07] Lab IEC 60502 & Hot Set Test
   │
   ▼
[S08] Cắt đoạn tối ưu Cut-Length sang Rulo gỗ ──▶ Xuất xe dự án
```

- **🔴 Điểm nghẽn cổ chai đặc trưng:** Phòng Xông Hơi Sauna (nơi dồn cục WIP chờ gom mẻ 2–3 ngày!) + Thời gian nạp 37–61 rulo trên [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander) + Máy đùn vỏ cỡ lớn.
- **💸 Tổn thất lớn nhất:** 1. Phế lõi đồng bọc XLPE bị thừa khi 4 rulo vào [Drum Twister](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-twister) lệch chiều dài! · 2. Phế mẩu thừa [Cut-Length](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cut-length) cuối rulo dự án · 3. [Over-thickness](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-over-thickness) trên nhựa XLPE đắt tiền (không tái chế được!) · 4. Tồn kho WIP nằm chờ gom mẻ lò xông kéo dài [Lead Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lead-time) lên 10–14 ngày.

### 🚀 Chiến Lược Hành Động Trọng Điểm Của OE
• **Đánh sập ùn tắc Phòng Xông Sauna:** Dùng [DOE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-doe) + [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test) phân nhóm lịch xông theo độ dày (mỏng 4h, dày 8h) chạy theo nhịp cố định mỗi ca thay vì chờ gom đủ 12 rulo → Cắt 50% WIP & rút [Lead Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lead-time) từ 12 ngày xuống 4–5 ngày!
• **Đồng bộ chiều dài 4 rulo lõi + Solver [Cut-Length](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cut-length):** Khóa dung sai đo mét Trạm 04 ≤ ±0.5% trước khi vào [Drum Twister](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-twister) và chạy Excel Solver/[Python](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-python) tổ hợp cắt rulo theo đơn dự án.
• **[SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) nạp lồng [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander) & cuộn băng thép [DSTA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dsta) lớn:** Rút nạp lồng từ 72p → 24p; đổi cuộn băng thép 2,500m giảm 80% dừng hàn.
• **Kiểm soát chặt vỏ Tubing & [Over-thickness](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-over-thickness):** Gắn [Laser Gauge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-laser-gauge) vòng kín giữ vỏ đúng [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502) và đảm bảo dễ tuốt vỏ khi thi công.

**🔑 Từ khóa tra cứu nhanh:** [XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe) · [Silane](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-silane) · [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander) · [Drum Twister](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-twister) · [DSTA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dsta) · [Cut-Length](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cut-length) · [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test) · [Over-thickness](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-over-thickness) · [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502) · [VSM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-vsm)

---

<a id="luong-f03"></a>
## Luồng C (F03): Cáp Vặn Xoắn Treo Trên Không (ABC) & Dây Nhôm Trần Lõi Thép (ACSR) — Dự Án Điện Lực EVN
> 📖 **Cẩm nang sâu:** `cable_mfg_machines` | 🎓 **Bài giáo trình:** [L1.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l1-3)

- **📦 Sản phẩm điển hình:** Cáp vặn xoắn LV-ABC 2×16, 4×50, 4×95 mm²; Dây nhôm trần lõi thép [ACSR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-acsr) 95/16, 185/29, 240/32 mm².

### 🗺️ Sơ Đồ Đường Đi Công Nghệ
```text
Nhôm Rod Ø9.5mm (EC Grade ≥ 61% IACS) + Sợi Thép mạ kẽm (với ACSR)
   │  ⚠️ KHU VỰC KÉO NHÔM TÁCH BIỆT TUYỆT ĐỐI VỚI ĐỒNG!
   ▼
[S02] Kéo sợi nhôm (dùng dầu kéo chuyên dụng cho nhôm)
   │
   ▼
[S03] Bện Rigid Strander:
      ├─ Nhánh ACSR: Bện lớp nhôm quanh lõi thép + Bơm mỡ chịu nhiệt ──▶ Lab lực kéo UTS ──▶ Xuất EVN
      └─ Nhánh ABC:  Bện ép nén ruột nhôm ──▶ [S04] Đùn XLPE Đen chống UV (2.5% Carbon Black, tạo gân 0-1-2-3)
                     ──▶ Xông hơi Silane ──▶ [S05] Xoắn bó 4 lõi ABC Cable ──▶ [S07] Lab UV/Hot Set ──▶ Xuất EVN
```

- **🔴 Điểm nghẽn cổ chai đặc trưng:** Năng lực máy kéo nhôm & máy bện [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander) vào mùa cao điểm đầu tư lưới điện EVN; kiểm soát bề mặt sạch không lẫn tạp chất đồng và độ đồng đều gân pha [ABC Cable](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-abc-cable).
- **💸 Tổn thất lớn nhất:** 1. Nhiễm bụi đồng từ xưởng kéo đồng gây ăn mòn điện hóa rỗ sợi nhôm ngoài trời · 2. Tràn mỡ bôi trơn ra lớp ngoài [ACSR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-acsr) bị EVN từ chối nghiệm thu · 3. Hàm lượng Carbon Black < 2% hoặc trộn kém làm rớt lão hóa UV · 4. Dừng đổi mã gân pha không tối ưu.

### 🚀 Chiến Lược Hành Động Trọng Điểm Của OE
• **Cách ly 5S & [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) Đồng vs Nhôm:** Phân tách tuyệt đối máy kéo/khuôn kéo/rulo nhôm riêng (sơn mã màu nhận diện rulo Nhôm), cấm tuyệt đối tái dùng khuôn cũ từ xưởng đồng.
• **[Campaign Scheduling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-campaign-scheduling) 0-Purge cho 4 pha [ABC Cable](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-abc-cable):** Vì cả 4 lõi đều dùng chung 1 loại nhựa [XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe) Đen, xếp chạy liền mạch 4 pha chỉ tháo nhanh vòng Cối tạo gân (0–1–2–3 gân trong 5 phút) mà KHÔNG cần xả nhựa [Purging](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-purging) → Tăng [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) máy đùn +9%!
• **Định lượng mỡ tự động đồng bộ tốc độ cho [ACSR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-acsr):** Gắn bơm định lượng theo xung Encoder khống chế đúng g/m, xóa sạch lỗi tràn mỡ ra lớp nhôm ngoài.
• **Siết tiến độ thầu EVN bằng [RCCP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rccp):** Dự báo tải tấn nhôm trước 6–8 tuần để không vỡ cam kết giao hàng phạt hợp đồng dự án.

**🔑 Từ khóa tra cứu nhanh:** [ABC Cable](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-abc-cable) · [ACSR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-acsr) · [IACS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iacs) · [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander) · [XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe) · [Silane](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-silane) · [Campaign Scheduling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-campaign-scheduling) · [RCCP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rccp) · [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke)

---

<a id="luong-f04"></a>
## Luồng D (F04): Cáp Điện Lực Trung Thế 24kV / 35kV (CXV/S/DSTA) — Công Nghệ Đỉnh Cao Ống Cong CCV
> 📖 **Cẩm nang sâu:** `cable_mfg_machines` | 🎓 **Bài giáo trình:** [L1.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l1-4)

- **📦 Sản phẩm điển hình:** Cáp trung thế 1 lõi hoặc 3 lõi 12/20(24)kV, 18/30(36)kV tiết diện 50–630 mm² (chuẩn [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502)-2).

### 🗺️ Sơ Đồ Đường Đi Công Nghệ
```text
Đồng/Nhôm Rod siêu sạch ──▶ [S02] Kéo sợi ──▶ [S03] Bện ép nén siêu nhẵn (+ sợi Water-Blocking lõi)
   │
   ▼  ⚠️ CẤP LIỆU PHÒNG SẠCH (CLEANROOM) CHỐNG BỤI TẠP CHẤT!
[S04] Dây chuyền CCV Đùn 3 lớp đồng thời (Bán dẫn trong + XLPE Peroxide + Bán dẫn ngoài)
      ──▶ Ống lưu hóa cong dài 80–150m (Khí Nitơ 10–14 bar, 300–400°C) ──▶ Làm nguội áp suất cao
   │
   ▼
[S05] Quấn băng bán dẫn Water-Blocking + Màn chắn băng/sợi đồng ──▶ Ghép 3 lõi Drum Twister ──▶ Giáp DSTA/DATA
   │
   ▼
[S06] Đùn vỏ HDPE/PVC ──▶ [S07] ★ PHÒNG LỒNG FARADAY ĐO Partial Discharge (≤ 5 pC) ★ ──▶ Rulo thép xuất xưởng
```

- **🔴 Điểm nghẽn cổ chai đặc trưng:** Dây chuyền [CCV](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ccv) triệu đô (chi phí khởi động/dừng lò cực lớn: tốn 4–6 giờ ổn định nhiệt áp & hàng trăm kg nhựa siêu sạch!) + Phòng thử cao áp Faraday đo [Partial Discharge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-partial-discharge).
- **💸 Tổn thất lớn nhất:** 1. Bật/tắt dây chuyền [CCV](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ccv) nhiều lần trong tuần do lịch chạy cắt nhỏ đơn hàng lẻ → Phế khởi động ăn sạch 100% lợi nhuận! · 2. Một hạt bụi hay 1 lần sụt áp khí Nitơ gây bọt khí làm cả rulo rớt [Partial Discharge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-partial-discharge) (> 5 pC) thành phế phẩm trị giá hàng trăm triệu! · 3. Ẩm băng chống thấm bán dẫn.

### 🚀 Chiến Lược Hành Động Trọng Điểm Của OE
• **Tối đa hóa [TEEP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-teep) bằng chiến dịch chạy liên tục 24/7 ([Campaign Scheduling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-campaign-scheduling)):** Gom toàn bộ đơn trung thế 24kV chạy liên tục 5–7 ngày không tắt lò [CCV](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ccv), cắt 65% phế khởi động!
• **Giám sát [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada) / [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes) theo từng mét dây:** Ghi log liên tục áp suất khí Nitơ, nhiệt độ 3 đầu đùn, đường kính tia X/siêu âm gắn với vị trí mét cáp — khi có lỗi [Partial Discharge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-partial-discharge) truy ngược định vị TDR ra đúng giây xảy ra sự cố!
• **Kỷ luật phòng sạch Cleanroom & bảo trì dự đoán [CBM / PdM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cbm-pdm):** Nạp nhựa kín chân không tuyệt đối, bảo trì dự phòng hệ thống gia nhiệt/van Nitơ không để sụt áp đột ngột giữa mẻ.

**🔑 Từ khóa tra cứu nhanh:** [CCV](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ccv) · [Partial Discharge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-partial-discharge) · [XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe) · [Water-Blocking](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-water-blocking) · [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502) · [TEEP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-teep) · [Campaign Scheduling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-campaign-scheduling) · [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada) · [CBM / PdM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cbm-pdm)

---

<a id="luong-f05"></a>
## Luồng E (F05): Cáp Chống Cháy & Ít Khói Không Halogen (FR / LSZH) — Chung Cư, Bệnh Viện, Sân Bay, Metro
> 📖 **Cẩm nang sâu:** `cable_extrusion_wire_forensics` | 🎓 **Bài giáo trình:** [L4.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l4-4)

- **📦 Sản phẩm điển hình:** Cáp chống cháy CXV/FR, CXV/FRT (chịu lửa 750–950°C 90–180p theo IEC 60331) bọc vỏ [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) ít khói không axit.

### 🗺️ Sơ Đồ Đường Đi Công Nghệ
```text
Đồng Rod ──▶ [S02] Kéo sợi ──▶ [S03] Bện ruột đồng
   │
   ▼
[S04a] ★ QUẤN BĂNG Mica FR (1–2 lớp, chồng mép Overlap chuẩn 30–50% + cảm biến đứt băng) ★
   │
   ▼
[S04b] Đùn cách điện XLPE (+ Xông Sauna) ──▶ [S05] Ghép lõi Drum Twister
   │
   ▼  ⚠️ SẤY HÚT ẨM Hopper Dryer BẮT BUỘC + TRỤC VÍT NÉN THẤP + NHIỆT ≤ 165°C!
[S06] Đùn vỏ ngoài LSZH (DDR nhỏ 1.1–1.6, kiểm soát chống rỗ khí & Die Drool)
   │
   ▼
[S07] Lab thử lửa IEC 60331, đo mật độ khói > 60% & độ axit khí cháy ──▶ [S08] Đóng rulo giao công trình
```

- **🔴 Điểm nghẽn cổ chai đặc trưng:** Tốc độ máy quấn băng [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr) + Tốc độ đùn vỏ [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) rất chậm (chỉ bằng 40–60% tốc độ [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc) do độ nhớt cao & nhạy nhiệt phân hủy bột khoáng ATH sinh bọt khí!).
- **💸 Tổn thất lớn nhất:** 1. Quấn băng [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr) chồng mép dư lên 60% (tốn băng Mica đắt tiền + phình đường kính làm đội thêm nhựa XLPE!) · 2. Đùn [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) bằng trục vít PVC & cài nhiệt cao > 175°C gây nổ bọt rỗ khí (phế 7–10%) và đóng cặn [Die Drool](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-die-drool) dừng cạo liên tục · 3. Nhập sai Routing tốc độ trên [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp) làm kế hoạch [CRP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crp) bị vỡ tiến độ!

### 🚀 Chiến Lược Hành Động Trọng Điểm Của OE
• **Tách riêng Routing tốc độ & trục vít cho [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) trên [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp):** Tuyệt đối không dùng chung định mức tốc độ PVC; chỉ định máy có trục vít tỷ số nén thấp (~1.2:1) và bảng chọn Chày–Cối [DDR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ddr) 1.1–1.6.
• **[SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) phễu sấy di động [Hopper Dryer](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hopper-dryer):** Sấy sẵn hạt [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) bên ngoài trước khi chuyển mẻ để xóa 120 phút dừng máy chờ sấy; đánh bóng mạ gương lòng Cối giảm [Die Drool](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-die-drool) từ 6 lần/ca xuống < 1 lần/ca.
• **Hiệu chuẩn góc quấn & [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) đứt băng [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr):** Khống chế chồng mép đúng 40% ± 3% và khóa liên động cảm biến hết/đứt băng tự dừng trong 0.5 giây để không chạy hổng đoạn thiếu lớp chống cháy!

**🔑 Từ khóa tra cứu nhanh:** [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr) · [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) · [Hopper Dryer](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hopper-dryer) · [DDR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ddr) · [Die Drool](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-die-drool) · [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) · [CRP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crp) · [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp) · [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed)

---

<a id="luong-f06"></a>
## Luồng F (F06): Cáp Đặc Chủng: Cáp Điện Mặt Trời (Solar H1Z2Z2-K) & Cáp Điều Khiển Chống Nhiễu (Braiding)
> 📖 **Cẩm nang sâu:** `cable_extrusion_wire_forensics` | 🎓 **Bài giáo trình:** [L1.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l1-3)

- **📦 Sản phẩm điển hình:** Cáp Solar DC 1,500V [Solar Cable](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-solar-cable) 1×4.0 / 6.0 mm² chuẩn EN 50618; Cáp điều khiển chống nhiễu lưới đồng CVV-S 4×1.5 / 12×1.5 mm².

### 🗺️ Sơ Đồ Đường Đi Công Nghệ
```text
Đồng Rod ──▶ [S02] Kéo tinh & Mạ thiếc (Tinned Copper dày 0.5–2.5 µm, không tróc xước!)
   │
   ▼
[S03] Bện mềm Class 5 trên Buncher (chỉnh puly/lực căng êm bảo vệ lớp mạ thiếc)
   │
   ├──▶ Nhánh SOLAR CABLE: [S04/S06] Đồng đùn 2 lớp (Co-extrusion XLPO cách điện + vỏ UV)
   │       ──▶ ★ CHIẾU XẠ E-beam (120–180 kGy + thẻ đo liều Dosimeter) ★ ──▶ Lab EN 50618
   │
   └──▶ Nhánh CÁP CHỐNG NHIỄU: [S04] Đùn lõi ──▶ [S05] Ghép lõi ──▶ ★ DÀN MÁY Braiding (3–12 m/p) ★
           ──▶ [S06] Đùn vỏ PVC/LSZH ──▶ [S07] Lab điện trở & độ phủ ≥ 85% ──▶ Đóng cuộn
```

- **🔴 Điểm nghẽn cổ chai đặc trưng:** Dàn máy đan lưới [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding) (tốc độ chỉ 3–12 m/phút — chậm nhất toàn nhà máy!) và lịch gom lô chiếu xạ [E-beam](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-e-beam) cho [Solar Cable](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-solar-cable).
- **💸 Tổn thất lớn nhất:** 1. Máy [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding) đan thừa độ che phủ (93% thay vì chuẩn 85%) làm giảm -22% công suất cổ chai và đốt thừa +14% đồng mạ thiếc đắt tiền! · 2. Quấn suốt Bobbin dài ngắn lệch nhau gây dừng thay lẻ liên tục · 3. Xước tróc lớp mạ thiếc [Tinned Copper](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tinned-copper) làm rớt bài thử hóa chất chống ăn mòn · 4. Trộn lẫn phế đồng mạ thiếc với đồng trần.

### 🚀 Chiến Lược Hành Động Trọng Điểm Của OE
• **Nâng vọt [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) khu [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding) bằng [Man-Machine Chart](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-man-machine-chart) + [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka):** Quấn đồng bộ 100% suốt Bobbin cùng chiều dài, chuẩn bị sẵn khay Bobbin thay nhanh bên ngoài ([SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed)), cài cảm biến đứt sợi tự dừng để 1 công nhân quản lý 6–10 máy [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding)!
• **Chỉnh chuẩn bước đan về mục tiêu 87%:** Giải phóng ngay +20% công suất cổ chai và tiết kiệm hàng trăm triệu đồng mạ thiếc/năm.
• **Áp dụng Co-extrusion 2 lớp & gom lô [E-beam](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-e-beam) khoa học cho [Solar Cable](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-solar-cable):** Đùn đồng thời cách điện + vỏ trong 1 lượt giảm 50% vận chuyển WIP; gắn thẻ Dosimeter đầu–cuối rulo đảm bảo liều bức xạ đồng đều.
• **Tách mã vật tư & mã phế [Tinned Copper](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tinned-copper) riêng trên [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp):** Đảm bảo hạch toán đúng giá thành (cao hơn đồng trần 6–10%) và không lẫn khi thu hồi.

**🔑 Từ khóa tra cứu nhanh:** [Solar Cable](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-solar-cable) · [Tinned Copper](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tinned-copper) · [E-beam](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-e-beam) · [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding) · [Man-Machine Chart](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-man-machine-chart) · [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka) · [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) · [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) · [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp)

---

# PHẦN III: KHO 40 TÌNH HUỐNG THỰC CHIẾN HIỆN TRƯỜNG & KỊCH BẢN XỬ LÝ 6 BƯỚC CHUẨN OE

## 1. Kế Hoạch, Đơn Gấp & Ùn Tắc Dòng Chảy

<a id="tinh-huong-sc01"></a>
### SC01: Kinh doanh ép chen đơn gấp dây màu Trắng vào giữa ca máy đùn đang chạy màu Đen
> 📍 **Trạm xảy ra:** [Trạm 00 (S00)](#tram-s00) | 📖 **Cẩm nang:** `smed` | 🎓 **Bài học:** [L3.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l3-3)

1. **🚨 Dấu hiệu hiện trường:** Máy đùn số 2 đang chạy lô cáp màu Đen thì Kinh doanh gọi điện yêu cầu dừng gấp để chạy 3 km dây VC 2.5 màu Trắng giao trong chiều nay.
2. **💥 Tác động dòng chảy & chi phí:** Mất 50 phút đổi ngược màu Tối → Sáng + xả 26 kg nhựa [Purging](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-purging) + phế dây đồng dính nhựa + làm trễ toàn bộ các đơn màu Đen phía sau.
3. **⏱️ Khoanh vùng ngay trong 24h:** Không tranh cãi cảm tính — OE kiểm tra ngay tồn kho siêu thị thành phẩm xem có hàng sẵn giao tạm không, hoặc kiểm tra xem có máy đùn dự phòng khác đang chạy màu Sáng (Vàng/Xanh) để đẩy đơn sang mà không phá máy đang chạy Đen.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Thiếu luật đóng băng lịch sản xuất (Frozen Horizon 48–72h), chưa có bảng chi phí ẩn đổi ngược màu (Changeover Cost) minh bạch giữa Kinh doanh và Sản xuất, và chưa lập siêu thị [Kanban](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kanban) cho dây dân dụng nhóm AX.
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Tính rõ bằng tiền: 1 lần chen đơn đổi ngược Đen → Trắng đốt mất ~1.8 triệu tiền nhựa/phế + 50 phút [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) máy cổ chai.
2. Thiết lập Luật Bánh Xe Màu [Color Sequencing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-color-sequencing) cố định theo tuần (Thứ 2–3 Trắng/Vàng → Thứ 4–5 Xanh/Đỏ → Thứ 6–7 Đen) kèm cơ chế: chen ngang trong vùng đóng băng phải có chữ ký Giám đốc Nhà máy.
3. Lập tồn kho an toàn [Safety Stock](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-safety-stock) siêu thị cho Top 10 mã dây VC bán chạy nhất.
6. **🔒 Khóa chuẩn chống tái diễn:** Ban hành [SOP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sop) phối hợp [S&OP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-s-op) / [MPS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mps) giữa Kinh doanh – Kế hoạch – Sản xuất; theo dõi KPI 'Số lần phá lịch màu/tuần' trên bảng họp tuần Ban Giám đốc.

**🔑 Từ khóa tra cứu nhanh:** [Color Sequencing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-color-sequencing) · [Purging](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-purging) · [Campaign Scheduling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-campaign-scheduling) · [Safety Stock](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-safety-stock) · [Kanban](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kanban) · [S&OP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-s-op) · [MPS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mps)

---

<a id="tinh-huong-sc02"></a>
### SC02: Mùa cao điểm xây dựng, đơn hàng tăng vọt +35% làm Xưởng Đùn quá tải 122%
> 📍 **Trạm xảy ra:** [Trạm 00 (S00)](#tram-s00) | 📖 **Cẩm nang:** `oe_field_execution_case_test` | 🎓 **Bài học:** [L5.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l5-3)

1. **🚨 Dấu hiệu hiện trường:** Phòng Kế hoạch báo tổng giờ yêu cầu tháng tới tại Xưởng Đùn là 1,240 giờ ròng trong khi 4 máy đùn ở [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) 65% chỉ chạy được tối đa 1,014 giờ (quá tải 122%, thiếu 226 giờ ròng!).
2. **💥 Tác động dòng chảy & chi phí:** Nguy cơ giao trễ hàng loạt dự án điện lực/đại lý (OTIF tụt xuống < 75%) hoặc phải xin mua máy đùn mới [CAPEX](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-capex) nhiều tỷ đồng nhưng chờ 6 tháng mới về!
3. **⏱️ Khoanh vùng ngay trong 24h:** Chạy nhanh mô hình [RCCP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rccp) tách tải theo từng cỡ cáp/máy đùn; phân loại đơn hàng nào là cổ chai thật sự, đơn hàng nào có thể chuyển đổi tuyến máy (Alternative Routing) hoặc chạy thêm ca Chủ nhật ngắn hạn.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Theo Lý thuyết điểm nghẽn [TOC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-toc), Xưởng Đùn đang là [Bottleneck](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bottleneck) nhưng mất tới 18% thời gian vào đổi mã [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) và 11% vào giảm tốc độ/dừng vặt — nghĩa là công suất 'ẩn' đang bị chôn ngay trong 4 máy hiện hữu!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
Áp dụng 5 bước [TOC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-toc) (Khai thác cổ chai TRƯỚC KHI mua máy mới):
1. Rút thời gian đổi màu/tiết diện bằng [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) + [Color Sequencing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-color-sequencing) (giải phóng ngay +95 giờ/tháng).
2. Đẩy lịch ăn trưa luân phiên (Hot-seat) không tắt máy đùn (+48 giờ/tháng).
3. Chuyển các mã dây nhỏ sang máy tốc độ cao hơn & tách đúng [L/D Ratio](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-l-d-ratio) (+55 giờ/tháng).
4. Bảo trì [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) 100% ngoài giờ cao điểm & chuyển bớt đơn không cốt lõi sang gia công tạm nếu vẫn thiếu +28 giờ.
→ Tổng công suất giải phóng +198 đến +230 giờ/tháng với chi phí gần như 0 đồng [CAPEX](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-capex)!
6. **🔒 Khóa chuẩn chống tái diễn:** Đưa bảng tải [RCCP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rccp) nhân [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) thực vào cuộc họp [S&OP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-s-op) hàng tháng để cảnh báo thiếu tải sớm 6–8 tuần.

**🔑 Từ khóa tra cứu nhanh:** [RCCP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rccp) · [TOC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-toc) · [Bottleneck](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bottleneck) · [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) · [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) · [CAPEX](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-capex) · [S&OP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-s-op) · [Lead Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lead-time)

---

<a id="tinh-huong-sc03"></a>
### SC03: Hàng trăm rulo đồng bện ùn tắc kín lối đi trước Xưởng Đùn trong khi Đóng Cuộn ngồi chờ
> 📍 **Trạm xảy ra:** [Trạm 03 (S03)](#tram-s03) | 📖 **Cẩm nang:** `lean_muda` | 🎓 **Bài học:** [L3.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l3-2)

1. **🚨 Dấu hiệu hiện trường:** Đi [Genba](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-genba) thấy 85 rulo bán thành phẩm chất đầy lối đi xe nâng giữa Xưởng Bện và Xưởng Đùn (có rulo nằm 5 ngày bắt đầu xỉn màu!), trong khi tổ Đóng Cuộn ở cuối xưởng lại thiếu hàng phải về sớm.
2. **💥 Tác động dòng chảy & chi phí:** Đọng vốn lưu động nhiều tỷ đồng đồng nguyên liệu trong [WIP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wip), tăng nguy cơ tai nạn xe nâng, đồng bị oxy hóa đen và kéo dài [Lead Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lead-time) giao hàng.
3. **⏱️ Khoanh vùng ngay trong 24h:** Kiểm đếm thực tế toàn bộ rulo WIP theo mã hàng, đối chiếu với lệnh ưu tiên đang chờ ở Đóng Cuộn để kéo đúng rulo cần giao gấp lên máy đùn trước.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Nhà máy đang vận hành kiểu Đẩy (Push): Xưởng Kéo & Bện có công suất lớn hơn Xưởng Đùn và được chấm KPI theo 'tấn sản lượng đầu ra' → Càng chạy nhanh để lấy thành tích thì càng đổ núi WIP đè chết Xưởng Đùn!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Vẽ [VSM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-vsm) chứng minh núi WIP không tạo thêm 1 đồng doanh thu nào mà làm tắc nghẽn dòng tiền.
2. Thiết lập cơ chế [Drum-Buffer-Rope](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-buffer-rope) & [Pull System](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pull-system): Xưởng Đùn (cổ chai) là 'Trống' phát nhịp; kẻ đúng số ô sơn vàng [Kanban](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kanban) trên sàn giữa Bện & Đùn (vd: tối đa 15 ô) — đầy ô thì Bện PHẢI chuyển sang chạy mã khác hoặc bảo trì [5S](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5s)/[Jishu Hozen](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jishu-hozen).
3. Sửa KPI Xưởng Bện từ 'tấn sản lượng tối đa' sang 'tỷ lệ tuân thủ lịch kéo của Xưởng Đùn (Schedule Adherence)'.
6. **🔒 Khóa chuẩn chống tái diễn:** Kiểm soát trực quan giới hạn trần WIP ([Visual Management](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-visual-management)) ngay tại sàn xưởng trong kiểm tra phân tầng [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa) hàng ngày.

**🔑 Từ khóa tra cứu nhanh:** [WIP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wip) · [VSM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-vsm) · [Drum-Buffer-Rope](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-buffer-rope) · [Pull System](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pull-system) · [Kanban](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kanban) · [Genba](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-genba) · [Lead Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lead-time) · [Visual Management](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-visual-management)

---

<a id="tinh-huong-sc04"></a>
### SC04: Hệ thống ERP báo tồn kho hạt nhựa XLPE còn 8 tấn nhưng ra kho thực tế chỉ còn 3 tấn
> 📍 **Trạm xảy ra:** [Trạm 01 (S01)](#tram-s01) | 📖 **Cẩm nang:** `bom_cost` | 🎓 **Bài học:** [L5.1](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l5-1)

1. **🚨 Dấu hiệu hiện trường:** Kế hoạch phát lệnh chạy đơn hàng cáp CXV lớn vì thấy [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp) báo còn 8 tấn hạt XLPE Silane, nhưng đến ca 2 Thủ kho báo hết sạch hạt nhựa — máy đùn cổ chai dừng chết 14 tiếng chờ mua gấp!
2. **💥 Tác động dòng chảy & chi phí:** Hụt 5 tấn nhựa ảo (~350 triệu), dừng máy cổ chai mất sản lượng, phải mua hàng gấp giá cao làm đội chi phí.
3. **⏱️ Khoanh vùng ngay trong 24h:** Điều chuyển gấp hạt XLPE tương đương (đã qua IQC) hoặc đảo lịch sang chạy đơn PVC trong lúc chờ vật tư; tiến hành kiểm kê khẩn cấp toàn bộ mã nhựa nhóm A.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** 1. Nhập xuất kho ghi sổ tay rồi cuối tuần mới nhập vào [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp) (độ trễ dữ liệu).
2. Xưởng lấy thêm bao nhựa bù cho phế [Purging](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-purging)/[Over-thickness](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-over-thickness) mà không lập phiếu xuất bổ sung (do cấu hình Backflush trừ ảo theo [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) chuẩn!).
3. Chưa có quy trình kiểm đếm luân phiên [Cycle Counting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cycle-counting).
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Cấm tuyệt đối xuất kho không phiếu/không quét Barcode — mọi bao nhựa ra khỏi kho phải quét ghi nhận tức thời vào [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp)/[MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes).
2. Triển khai [Cycle Counting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cycle-counting) theo phân nhóm [ABC-XYZ](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-abc-xyz) (Nhóm A đồng/XLPE đếm hàng tuần, Nhóm B hàng tháng, Nhóm C hàng quý) giữ độ chính xác tồn kho RIA ≥ 98.5%.
3. Tính lại điểm đặt hàng [ROP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rop) & [Safety Stock](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-safety-stock) có tính đến biến động Lead Time giao hàng nhà cung cấp.
6. **🔒 Khóa chuẩn chống tái diễn:** Đưa KPI độ chính xác tồn kho (RIA ≥ 98.5%) vào đánh giá KPI Thủ kho & Kế hoạch; đối soát định kỳ phế thực tế vs xuất kho cuối mỗi ca.

**🔑 Từ khóa tra cứu nhanh:** [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp) · [Cycle Counting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cycle-counting) · [ABC-XYZ](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-abc-xyz) · [Safety Stock](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-safety-stock) · [ROP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rop) · [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) · [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp)

---

<a id="tinh-huong-sc05"></a>
### SC05: Phòng xông hơi XLPE Silane (Sauna) chờ gom mẻ làm Lead Time cáp CXV kéo dài 12 ngày
> 📍 **Trạm xảy ra:** [Trạm 04 (S04)](#tram-s04) | 📖 **Cẩm nang:** `lean_muda` | 🎓 **Bài học:** [L3.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l3-2)

1. **🚨 Dấu hiệu hiện trường:** Khách hàng dự án phàn nàn đặt cáp CXV mất 12 ngày mới có hàng dù tổng thời gian máy chạy thực tế chỉ chưa tới 21 giờ (hiệu quả chuỗi PCE chỉ 7.3%!).
2. **💥 Tác động dòng chảy & chi phí:** Tồn kho dở dang [WIP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wip) cực lớn trước phòng xông, chậm xoay vòng dòng tiền, dễ mất đơn hàng dự án cần gấp.
3. **⏱️ Khoanh vùng ngay trong 24h:** Đi [Genba](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-genba) đo thời gian nằm chờ thực tế của từng rulo lõi XLPE từ lúc rời máy đùn đến lúc vào và ra khỏi phòng xông Sauna.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** 1. Xưởng có thói quen chờ gom đủ đầy 12 rulo lớn mới bật lò hơi xông 1 lần (rulo đầu tiên nằm chờ 36–48 giờ!).
2. Cài chung 1 chế độ xông dư an toàn 10 giờ cho mọi cỡ cáp, kể cả lõi cách điện mỏng 0.7 mm vốn chỉ cần 4 giờ đã đạt [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test)!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Phối hợp Phòng Lab chạy thử nghiệm [DOE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-doe) lấy mẫu [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test) ở các mốc 4h – 6h – 8h theo 3 dải chiều dày cách điện (≤ 0.8mm, 0.9–1.2mm, ≥ 1.4mm).
2. Thiết kế lịch xông cố định theo nhịp mỗi ca (không chờ đầy mới bật, hoặc ngăn vách lò xông thành 2 khoang nhỏ linh hoạt) kết hợp dùng thời gian xông tối ưu (4h / 6.5h / 9h).
3. Kết quả thực tế: Cắt 52% lượng rulo WIP chờ xông, rút [Lead Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lead-time) cáp CXV từ 12 ngày xuống 4.5 ngày và tiết kiệm 18% nhiên liệu đốt lò hơi!
6. **🔒 Khóa chuẩn chống tái diễn:** Ban hành Bảng tra thời gian xông chuẩn theo chiều dày cách điện dán ngay cửa lò Sauna và theo dõi trên [VSM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-vsm) hàng quý.

**🔑 Từ khóa tra cứu nhanh:** [Silane](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-silane) · [XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe) · [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test) · [VSM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-vsm) · [WIP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wip) · [Lead Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lead-time) · [DOE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-doe)

---

## 2. Xưởng Kéo Sợi, Ủ Đồng & Khuôn PCD

<a id="tinh-huong-sc06"></a>
### SC06: Máy kéo thô RBD đứt sợi liên tục 8 lần/ca, xưởng và mua hàng đổ lỗi lẫn nhau
> 📍 **Trạm xảy ra:** [Trạm 02 (S02)](#tram-s02) | 📖 **Cẩm nang:** `cable_extrusion_wire_forensics` | 🎓 **Bài học:** [L4.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l4-4)

1. **🚨 Dấu hiệu hiện trường:** Máy kéo thô [RBD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rbd) đứt dây liên miên (mỗi lần dừng 18 phút xâu lại 11 khuôn, mất 750 kg sản lượng/lần!), xưởng đổ tại đồng Rod kém còn Mua hàng khẳng định giấy COA nhà cung cấp đạt chuẩn.
2. **💥 Tác động dòng chảy & chi phí:** [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) máy RBD rơi xuống dưới 55%, tạo hàng trăm kg đồng rối phế và gây thiếu sợi đồng cho toàn bộ Xưởng Bện phía sau.
3. **⏱️ Khoanh vùng ngay trong 24h:** Yêu cầu công nhân KHÔNG vứt 2 đầu dây đứt — gắn thẻ ghi giờ/lô đồng/vị trí khuôn và thu gom 100% mẫu đầu gãy trong 48 giờ để soi kính hiển vi 30×.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Áp dụng [Wire Break Forensics](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wire-break-forensics) phân loại 45 mẫu gãy theo [Pareto](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pareto) 80/20: thực tế chỉ 15% là [Cup-and-Cone](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cup-and-cone) (tạp chất đồng Rod), còn 48% có vết cháy hồ quang trên tang ủ [Annealing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-annealing) và 27% gãy phẳng có bọt khí tại mối hàn [Butt Welder](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-butt-welder)!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Bảo trì đánh bóng ngay cổ góp & vòng tiếp xúc tang ủ [Annealing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-annealing) loại bỏ hiện tượng đánh lửa hồ quang (giải quyết 48% sự cố!).
2. Chuẩn hóa [SOP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sop) hàn [Butt Welder](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-butt-welder) (vệ sinh đầu đồng bằng cồn, kiểm lực kẹp, ủ mối hàn 2 bước, test bẻ 90° đầu ca).
3. Với 15% mẫu [Cup-and-Cone](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cup-and-cone) có hạt tạp chất đen dưới kính hiển vi, lập hồ sơ bằng chứng ảnh gửi khiếu nại lô đồng Rod theo [ASTM B49](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-astm-b49).
→ Số lần đứt sợi giảm từ 8 lần/ca xuống < 1.5 lần/ca (< 0.3 lần/tấn) chỉ sau 3 tuần!
6. **🔒 Khóa chuẩn chống tái diễn:** Treo Bảng mẫu nhận diện 6 hình thái đứt sợi ngay cạnh máy [RBD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rbd) và bắt buộc ghi mã hình thái đứt vào nhật ký [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes) / [Downtime](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-downtime).

**🔑 Từ khóa tra cứu nhanh:** [RBD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rbd) · [Wire Break Forensics](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wire-break-forensics) · [Cup-and-Cone](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cup-and-cone) · [Annealing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-annealing) · [Butt Welder](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-butt-welder) · [Pareto](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pareto) · [ASTM B49](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-astm-b49)

---

<a id="tinh-huong-sc07"></a>
### SC07: Máy kéo tinh Multi-wire 16 sợi liên tục đứt lặp đi lặp lại đúng sợi số 4 và số 9
> 📍 **Trạm xảy ra:** [Trạm 02 (S02)](#tram-s02) | 📖 **Cẩm nang:** `cable_extrusion_wire_forensics` | 🎓 **Bài học:** [L1.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l1-2)

1. **🚨 Dấu hiệu hiện trường:** Trên máy kéo đa sợi [Multi-wire](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-multi-wire) 16 đường dây, cứ chạy khoảng 20–30 phút lại đứt sợi số 4 hoặc số 9 làm cả 16 sợi phải dừng khẩn cấp cùng lúc!
2. **💥 Tác động dòng chảy & chi phí:** Hiệu suất máy kéo tinh tụt thê thảm (< 50%), tốn thời gian xâu dây & nối sợi cực lâu, làm chậm tiến độ cấp sợi cho Xưởng Bện [Buncher](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-buncher).
3. **⏱️ Khoanh vùng ngay trong 24h:** Dừng lấy mẫu đo đường kính thực tế của cả 16 sợi sau từng cấp khuôn và kiểm tra kích thước lỗ khuôn [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd) ở vị trí dây 4 & 9 tại Phòng Khuôn.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Khi 1 khuôn ở dây số 4 bị hỏng trước đó, thợ bảo trì chỉ rút đại 1 khuôn mới keng thay lẻ vào giữa dàn 15 khuôn đã mòn +0.004mm! Vì 16 sợi chạy chung 1 trục kéo Capstan, sợi số 4 có độ giãn dài khác hẳn 15 sợi còn lại nên bị kéo căng vượt giới hạn rồi đứt liên hoàn!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Ban hành quy chuẩn tuyệt đối: Trên máy [Multi-wire](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-multi-wire) BẮT BUỘC thay đồng bộ cả bộ khuôn khớp kích thước (**Matched Die Set**, sai lệch giữa các khuôn cùng 1 hàng ≤ 0.002 mm).
2. Đánh số quản lý bộ khuôn theo khay Kitting màu sắc tại Phòng Khuôn (Die Shop) kèm máy đo đường kính laser trước khi xuất xưởng.
3. Kiểm tra thêm áp lực vòi phun [Drawing Emulsion](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drawing-emulsion) vào đúng khe dây 4 & 9 chống nghẹt cặn.
6. **🔒 Khóa chuẩn chống tái diễn:** Đưa kiểm tra 'Xác nhận Matched Die Set ≤ 0.002mm' vào phiếu giao nhận khuôn giữa Phòng Khuôn và Tổ Kéo tinh.

**🔑 Từ khóa tra cứu nhanh:** [Multi-wire](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-multi-wire) · [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd) · [Drawing Emulsion](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drawing-emulsion) · [Kitting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kitting) · [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee)

---

<a id="tinh-huong-sc08"></a>
### SC08: Sợi đồng kéo ra bị cứng gãy khi bện ở Trạm 03 hoặc bị đen xỉn sau 24 giờ nằm kho
> 📍 **Trạm xảy ra:** [Trạm 02 (S02)](#tram-s02) | 📖 **Cẩm nang:** `cable_mfg_machines` | 🎓 **Bài học:** [L1.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l1-2)

1. **🚨 Dấu hiệu hiện trường:** Xưởng Bện [Buncher](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-buncher) phản ánh cứ chạy đầu/cuối rulo đồng mới từ Xưởng Kéo là sợi bị cứng bung lò xo đứt liên tục; một số rulo khác để qua đêm bị ố nâu đen bề mặt.
2. **💥 Tác động dòng chảy & chi phí:** Phải hạ tốc độ máy bện -30%, cắt bỏ hàng chục mét sợi đầu/cuối rulo hoặc phải đưa rulo đi ủ lại trong lò chuông tốn điện & tăng phế.
3. **⏱️ Khoanh vùng ngay trong 24h:** Cắt mẫu đầu–giữa–cuối rulo đo độ giãn dài [Tensile](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tensile) (chuẩn phải ≥ 20–25%) và kiểm tra hệ thống hơi nước/khí bảo vệ + nhiệt độ nước làm mát trong ống ủ [Annealing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-annealing).
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** 1. Đường cong đồng bộ điện áp ủ (Ramp Curve) trên [PLC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-plc) đáp ứng trễ 0.8 giây lúc máy tăng tốc/giảm tốc → Tạo ra 40m dây bị ủ non (cứng) ngay đầu & cuối mỗi rulo!
2. Đường hơi nước bảo vệ chống oxy hóa bị hở gioăng lọt không khí vào ống ủ nóng 500°C và bộ thổi khô đầu ra yếu để nước đọng trên bề mặt đồng → Oxy hóa đen sợi sau 1 ngày!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Phối hợp Cơ Điện hiệu chỉnh lại hệ số bù trễ Ramp Curve điện áp ủ tỷ lệ chính xác theo bình phương tốc độ kéo trên [PLC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-plc).
2. Thay gioăng kín ống hơi bảo vệ, kiểm tra chất lượng nước mềm/phụ gia chống oxy hóa trong bể làm nguội sau ủ và nâng cấp béc thổi khô Air Wipe trước khi cuốn lên [Take-up](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-take-up).
3. Quấn màng PE chống ẩm bọc kín các rulo đồng thành phẩm nếu thời gian chờ sang Xưởng Bện > 12 giờ.
6. **🔒 Khóa chuẩn chống tái diễn:** Bổ sung test kiểm tra độ giãn dài đoạn đầu/cuối rulo vào [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan) đầu ca máy kéo và kiểm tra áp suất hơi bảo vệ trong [Jishu Hozen](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jishu-hozen).

**🔑 Từ khóa tra cứu nhanh:** [Annealing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-annealing) · [PLC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-plc) · [Tensile](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tensile) · [Take-up](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-take-up) · [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan) · [Jishu Hozen](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jishu-hozen)

---

<a id="tinh-huong-sc09"></a>
### SC09: Đường kính sợi đồng kéo trôi dần lên +0.009mm gây âm định mức đồng Copper Give-away
> 📍 **Trạm xảy ra:** [Trạm 02 (S02)](#tram-s02) | 📖 **Cẩm nang:** `cable_cost_capacity` | 🎓 **Bài học:** [L5.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l5-2)

1. **🚨 Dấu hiệu hiện trường:** Kế toán báo cuối quý Xưởng Kéo & Bện tiêu hao đồng vượt định mức [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) +2.1% (tương đương thất thoát ~5 tấn đồng ≈ 1.25 tỷ đồng/quý) dù tỷ lệ phế cân được tại thùng rác rất nhỏ!
2. **💥 Tác động dòng chảy & chi phí:** Chảy máu lợi nhuận âm thầm cực lớn — đồng nguyên chất bị 'biếu không' vào trong từng mét dây thành phẩm mà khách hàng không trả thêm tiền.
3. **⏱️ Khoanh vùng ngay trong 24h:** Lấy ngẫu nhiên 30 mẫu sợi từ các máy kéo đo bằng Panme/Laser chính xác 0.001mm và đối chiếu điện trở 20°C trên cầu [Kelvin Bridge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kelvin-bridge) so với trần [IEC 60228](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60228).
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Biểu đồ [SPC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spc) Xbar-R phơi bày đường kính sợi đang trôi dần lên sát cận trên (+0.009mm) vì: (1) Không có giới hạn tấn đồng thay khuôn [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd) (để khuôn mòn quá lâu mới tháo đi đánh bóng!), (2) Công nhân sợ rớt điện trở nên chủ động chọn khuôn hơi to hơn thiết kế +0.005mm cho 'an toàn'!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Thiết lập dự án [Six Sigma](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-six-sigma) [DMAIC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dmaic) tối ưu [Copper Give-away](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-copper-give-away): Khảo sát % [IACS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iacs) thực tế của đồng Rod đầu vào (101.2% IACS) → Tính lại đường kính mục tiêu hợp pháp đạt [IEC 60228](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60228) với biên an toàn ≥ 3σ ([Cpk](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cpk) ≥ 1.33).
2. Khóa tuổi thọ khuôn [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd) theo sản lượng tấn (vd: đạt 25 tấn hoặc đường kính chạm cận cảnh báo trên [SPC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spc) là BẮT BUỘC tháo đi Re-polish!).
3. Trình quy trình [MOC / ECN](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-moc-ecn) được QA/QC & Giám đốc ký duyệt rồi cập nhật đồng bộ [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) trên [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp).
→ Kéo [Copper Give-away](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-copper-give-away) từ +2.1% xuống +0.4%, thu hồi Hard Savings > 3 tỷ VNĐ/năm!
6. **🔒 Khóa chuẩn chống tái diễn:** Gắn biểu đồ [SPC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spc) đo đường kính 2 giờ/lần (hoặc Laser online) vào [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan) và chấm điểm tuân thủ trong [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa).

**🔑 Từ khóa tra cứu nhanh:** [Copper Give-away](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-copper-give-away) · [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd) · [IEC 60228](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60228) · [IACS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iacs) · [Kelvin Bridge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kelvin-bridge) · [SPC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spc) · [Cpk](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cpk) · [DMAIC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dmaic) · [MOC / ECN](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-moc-ecn)

---

<a id="tinh-huong-sc10"></a>
### SC10: Bể nhũ tương kéo sợi mùa hè bốc mùi, tụt pH và đóng cặn bít khuôn PCD
> 📍 **Trạm xảy ra:** [Trạm 02 (S02)](#tram-s02) | 📖 **Cẩm nang:** `cable_mfg_machines` | 🎓 **Bài học:** [L1.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l1-2)

1. **🚨 Dấu hiệu hiện trường:** Vào tháng 6 nắng nóng Đà Nẵng, bể dung dịch [Drawing Emulsion](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drawing-emulsion) bốc mùi hôi thối, có lớp váng xanh đóng cặn quanh khuôn [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd), tỷ lệ đứt sợi tăng gấp 3 và sợi đồng ra bị mờ xước.
2. **💥 Tác động dòng chảy & chi phí:** Hỏng sớm khuôn kim cương [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd) đắt tiền, tăng mạnh lực kéo làm vọt tiền điện [SEC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sec) kWh/tấn và giảm [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) toàn Xưởng Kéo.
3. **⏱️ Khoanh vùng ngay trong 24h:** Đo ngay 5 thông số bể nhũ tương: Nồng độ (khúc xạ kế Refractometer), pH, độ dẫn điện nước (Conductivity), nhiệt độ bể và kiểm tra giấy lọc mạt đồng.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** 1. Trời nóng bay hơi mạnh, công nhân lấy thẳng vòi nước máy cứng (chứa nhiều Canxi/Magie) châm bù mà quên châm dầu → Nồng độ tụt từ 5% xuống 1.8%, Canxi phản ứng với dầu tạo kết tủa xà phòng xanh bít khuôn!
2. Nhiệt độ bể vượt 48°C tạo điều kiện vi khuẩn kỵ khí phát triển làm tụt pH xuống 7.1 gây thối dầu & ăn mòn đồng!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Xả vệ sinh diệt khuẩn toàn bộ bể, pha mới đúng chuẩn 4.5% (kéo tinh) / 10% (RBD) bằng 100% nước mềm khử ion (DI Water).
2. Lắp vạch báo mức tự động + đường cấp nước DI riêng (khóa đường nước máy thường bằng [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke)!).
3. Vệ sinh bộ trao đổi nhiệt làm mát bể giữ ổn định 35–42°C và lắp hệ thống sục khí nhẹ lúc nghỉ cuối tuần chống vi khuẩn kỵ khí.
6. **🔒 Khóa chuẩn chống tái diễn:** Đưa bảng đo 5 thông số bể nhũ tương (Nồng độ – pH – Độ dẫn – Nhiệt độ – Lọc) vào bảng [Visual Management](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-visual-management) và [Jishu Hozen](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jishu-hozen) đầu ca mỗi ngày.

**🔑 Từ khóa tra cứu nhanh:** [Drawing Emulsion](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drawing-emulsion) · [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd) · [SEC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sec) · [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) · [Jishu Hozen](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jishu-hozen) · [Visual Management](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-visual-management)

---

## 3. Xưởng Bện, Ghép Lõi & Bọc Giáp

<a id="tinh-huong-sc11"></a>
### SC11: Máy bện lồng cứng Rigid Strander mất 75 phút nạp 37 rulo mỗi lần đổi cỡ cáp
> 📍 **Trạm xảy ra:** [Trạm 03 (S03)](#tram-s03) | 📖 **Cẩm nang:** `smed` | 🎓 **Bài học:** [L3.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l3-3)

1. **🚨 Dấu hiệu hiện trường:** Mỗi khi chuyển từ bện cáp 95 mm² sang 185 mm², máy [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander) dừng suốt 75 phút để công nhân tìm rulo, dùng cầu trục nhấc lắp từng cuộn vào các lồng và xâu sợi thủ công.
2. **💥 Tác động dòng chảy & chi phí:** Với 2 lần đổi cỡ/ngày, máy cổ chai của xưởng cáp lực mất toi 2.5 giờ/ngày (Availability giảm hơn 15%!).
3. **⏱️ Khoanh vùng ngay trong 24h:** Quay video toàn bộ 75 phút nạp rulo bằng điện thoại và lập bảng tách từng thao tác theo giây (Bước 1–2 của [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed)).
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Phân tích video phơi bày 45/75 phút (60%) là Thao tác Ngoài đang làm khi máy đứng im: đi tìm 37 rulo rải rác khắp xưởng (18p), chờ cầu trục bận cẩu khu khác (12p), kiểm tra thiếu rulo phải chạy sang Xưởng Kéo giục (10p), tìm kìm cắt & ống nối (5p)!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Áp dụng [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) + [Kitting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kitting): Chuẩn bị đủ bộ 37 rulo có chiều dài bằng nhau đặt sẵn theo thứ tự lồng trên giá xe trượt bên cạnh máy TRƯỚC khi máy dừng 30 phút (cắt ngay 40 phút!).
2. Thiết kế quy trình nạp song song 2 người kiểu F1 Pit-stop (1 người vận hành nâng rulo nạp lồng trước, 1 người xâu sợi & khóa chốt lồng sau) + áp dụng [LOTO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loto) chuẩn 2 ổ khóa.
3. Rút thời gian nạp lồng từ 75 phút xuống còn 24 phút (-68%), tăng ngay +1.7 giờ chạy máy mỗi ngày!
6. **🔒 Khóa chuẩn chống tái diễn:** Ban hành [Standard Work](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-work) nạp lồng 2 người dán ảnh trực quan [OPL](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sop) tại máy và kiểm tra tiến độ soạn Kitting trong [LSW](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lsw) Tổ trưởng.

**🔑 Từ khóa tra cứu nhanh:** [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander) · [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) · [Kitting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kitting) · [LOTO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loto) · [Standard Work](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-work) · [SOP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sop) · [LSW](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lsw)

---

<a id="tinh-huong-sc12"></a>
### SC12: Máy bện Buncher dây mềm bị lỗi 'lồng chim' (Birdcaging) & sợi chùng lòi ra ngoài
> 📍 **Trạm xảy ra:** [Trạm 03 (S03)](#tram-s03) | 📖 **Cẩm nang:** `ole` | 🎓 **Bài học:** [L2.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l2-3)

1. **🚨 Dấu hiệu hiện trường:** Ruột đồng mềm Class 5 sau khi bện trên máy [Buncher](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-buncher) xuất hiện các đoạn sợi đồng phồng bung lên như lồng chim hoặc 1–2 sợi mảnh lòi ra khỏi bó — khi sang máy đùn Trạm 04 lập tức đâm thủng lớp PVC gây lỗi [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester)!
2. **💥 Tác động dòng chảy & chi phí:** Tỷ lệ phế dây mềm VCm vọt lên 4.5%, công nhân phải đứng canh máy sát sao (1 người chỉ đứng nổi 1–2 máy, [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) tụt thê thảm).
3. **⏱️ Khoanh vùng ngay trong 24h:** Cách ly ngay các rulo ruột bị bung sợi không cho chạy vào máy đùn; kiểm tra lực căng phanh xả của toàn bộ giàn rulo [Pay-off](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pay-off) cấp vào máy Buncher đó.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** 1. Phanh dây đai trên giàn [Pay-off](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pay-off) có cuộn mòn trơn (nhả dây lỏng chùng), có cuộn bó kẹt (căng quá mức) → Chênh lệch lực căng giữa các sợi làm sợi căng nằm chặt lõi giữa, còn sợi chùng bị đẩy phồng ra ngoài!
2. Khuôn gom sợi (Closing Die) bị mòn rộng quá kích thước bó dây.
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Bảo trì đồng bộ lại toàn bộ bộ hãm lực căng giàn xả [Pay-off](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pay-off) (dùng lực kế lò xo cân chỉnh đều nhau từng vị trí trong sai số ±5%).
2. Thay khuôn gom sợi đúng đường kính chuẩn và kiểm tra rulo đồng đầu vào từ Trạm 02 không bị rối chéo lớp [Take-up](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-take-up).
3. Gắn cảm biến quang/vòng chạm phát hiện sợi bung tự dừng [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka) → Cho phép mở rộng mô hình [Man-Machine Chart](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-man-machine-chart) 1 công nhân đứng 4 máy an toàn!
6. **🔒 Khóa chuẩn chống tái diễn:** Đưa kiểm tra lực căng [Pay-off](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pay-off) và kích thước khuôn gom vào Checklist bảo trì [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) hàng tuần.

**🔑 Từ khóa tra cứu nhanh:** [Buncher](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-buncher) · [Pay-off](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pay-off) · [Take-up](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-take-up) · [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester) · [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka) · [Man-Machine Chart](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-man-machine-chart) · [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole)

---

<a id="tinh-huong-sc13"></a>
### SC13: Ghép 4 lõi cáp lực trên Drum Twister bị lệch chiều dài 4 rulo gây cắt bỏ 165m lõi XLPE
> 📍 **Trạm xảy ra:** [Trạm 05 (S05)](#tram-s05) | 📖 **Cẩm nang:** `cable_cost_capacity` | 🎓 **Bài học:** [L5.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l5-2)

1. **🚨 Dấu hiệu hiện trường:** Khi ghép cáp CXV 3×120+1×70 trên máy [Drum Twister](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-twister), 4 rulo lõi từ Xưởng Đùn giao sang có chiều dài: Đỏ 1,050m, Vàng 1,020m, Xanh 995m, Đen 1,080m → Rulo Xanh hết trước tại mét 995 khiến 3 lõi kia dư bỏ tổng cộng 165m lõi đồng đã bọc XLPE!
2. **💥 Tác động dòng chảy & chi phí:** Một mét lõi đồng 120mm² bọc XLPE trị giá hàng trăm nghìn đồng — chỉ 1 mẻ ghép lệch chiều dài đốt mất vài chục triệu đồng phế phẩm đồng dính nhựa!
3. **⏱️ Khoanh vùng ngay trong 24h:** Cân đo kiểm tra lại chiều dài thực tế các rulo đang chờ trước máy ghép; tạm ghép các rulo có chiều dài gần nhau nhất vào cùng 1 mẻ để giảm cắt bỏ.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** 1. Bánh đo mét tại 2 máy đùn khác nhau (máy đùn pha và máy đùn trung tính) sai lệch hiệu chuẩn tới 3–5%!
2. Công nhân đùn tự ý chạy dư thêm 'cho chắc khỏi thiếu' mà không khóa tự động dừng đúng số mét mục tiêu theo lệnh [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes) / [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp).
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Hiệu chuẩn đồng bộ toàn bộ bánh đo mét Encoder trên tất cả máy đùn về cùng sai số ≤ ±0.2%.
2. Cài đặt tính năng tự động báo còi/dừng máy khi đạt đúng chiều dài lệnh trên [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi) (vd: cùng dừng ở 1,010 m ± 3 m cho cả 4 lõi cùng đơn hàng).
3. Ghép 4 rulo có cùng mã lệnh SX theo bộ [Kitting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kitting) trước khi đẩy vào [Drum Twister](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-twister).
→ Giảm phế lõi thừa cuối rulo từ ~5% xuống < 0.5%, tiết kiệm hàng trăm triệu đồng/năm!
6. **🔒 Khóa chuẩn chống tái diễn:** Gắn báo cáo theo dõi 'Độ lệch chiều dài giữa các lõi cùng bộ' trên [Power BI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-power-bi) và khóa kiểm chuẩn bánh đo mét vào lịch [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance).

**🔑 Từ khóa tra cứu nhanh:** [Drum Twister](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-twister) · [XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe) · [Capstan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-capstan) · [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi) · [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes) · [Kitting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kitting) · [Scrap](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scrap)

---

<a id="tinh-huong-sc14"></a>
### SC14: Bước xoắn Lay-up chỉnh quá ngắn làm âm đồng & nhựa +1.5% toàn bộ đơn hàng cáp nhiều lõi
> 📍 **Trạm xảy ra:** [Trạm 05 (S05)](#tram-s05) | 📖 **Cẩm nang:** `cable_cost_capacity` | 🎓 **Bài học:** [L5.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l5-2)

1. **🚨 Dấu hiệu hiện trường:** Kiểm toán [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) cuối tháng cho thấy dòng cáp lực 4 lõi CXV liên tục bị âm vật tư đồng & XLPE thêm ~1.5% so với định mức chuẩn dù [Copper Give-away](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-copper-give-away) và [Over-thickness](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-over-thickness) đều đã kiểm soát tốt!
2. **💥 Tác động dòng chảy & chi phí:** Đội giá thành sản xuất thầm lặng trên mọi km cáp nhiều lõi và giảm tốc độ máy ghép lõi (vì xoắn dày hơn nên kéo chậm hơn!).
3. **⏱️ Khoanh vùng ngay trong 24h:** Đo trực tiếp bước xoắn (Lay Length — khoảng cách giữa 2 vòng xoắn cùng 1 lõi) bằng thước mét ngay trên máy [Drum Twister](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-twister) & [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander) so sánh với bản vẽ công nghệ.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Công nhân cài nhầm tỷ số bánh răng/tốc độ quay lồng làm bước xoắn thực tế ngắn chỉ 300 mm (thay vì chuẩn thiết kế 420 mm) → Hệ số xoắn [Lay-up Factor](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lay-up-factor) nhảy vọt từ 1.016 lên 1.031 (+1.51% cả đồng lẫn nhựa trên từng mét cáp!), đồng thời làm máy chạy chậm đi 28%!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Kiểm tra lại toàn bộ bảng tra bước xoắn chuẩn trên mọi máy [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander) & [Drum Twister](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-twister), tối ưu bước xoắn về sát cận dài tiêu chuẩn [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502) cho phép (vừa chắc gọn vừa tiết kiệm vật liệu tối đa!).
2. Nạp cứng tỷ số tốc độ quay/tốc độ kéo vào thư viện Recipe tự động trên [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi) khóa mật khẩu để công nhân không chỉnh tay sai lệch.
3. Đồng bộ hệ số [Lay-up Factor](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lay-up-factor) tính theo hình học 3D chuẩn lên cây [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) của [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp).
6. **🔒 Khóa chuẩn chống tái diễn:** Thêm hạng mục đo kiểm tra bước xoắn đầu ca vào [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan) và kiểm tra chéo trong [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa).

**🔑 Từ khóa tra cứu nhanh:** [Lay-up Factor](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lay-up-factor) · [Drum Twister](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-drum-twister) · [Rigid Strander](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-rigid-strander) · [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) · [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502) · [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi) · [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan)

---

<a id="tinh-huong-sc15"></a>
### SC15: Máy quấn giáp DSTA dừng hàn băng thép 4 lần/rulo & dàn máy Braiding chạy quá chậm
> 📍 **Trạm xảy ra:** [Trạm 05 (S05)](#tram-s05) | 📖 **Cẩm nang:** `cable_extrusion_wire_forensics` | 🎓 **Bài học:** [L1.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l1-3)

1. **🚨 Dấu hiệu hiện trường:** Đơn hàng cáp ngầm giáp thép [DSTA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dsta) và cáp điều khiển chống nhiễu [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding) luôn bị trễ giao hàng ở Trạm 05 dù Xưởng Đùn phía trước giao lõi rất sớm.
2. **💥 Tác động dòng chảy & chi phí:** Trạm 05 trở thành điểm nghẽn phụ bất ngờ làm chậm OTIF toàn dự án và tốn nhiều nhân công trực máy.
3. **⏱️ Khoanh vùng ngay trong 24h:** Chạy bấm giờ [Time Study](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-time-study) trên máy quấn giáp DSTA (đếm số lần dừng hàn băng) và đo thực tế mật độ che phủ lưới quang học (Optical Coverage) trên dàn máy [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding).
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** 1. Máy giáp [DSTA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dsta) đang mua cuộn băng thép dạng bánh nhỏ (Pad Coil chỉ 400m) nên 1 rulo cáp 1,600m phải dừng hàn băng 4 lần (mất 60 phút/rulo!).
2. Máy [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding) đang cài bước đan dày tạo mật độ phủ 93% (chuẩn chỉ yêu cầu ≥ 85%) làm tốc độ tuyến tính chậm mất -22% và tốn dư +14% đồng mạ thiếc [Tinned Copper](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tinned-copper), lại quấn các suốt Bobbin dài ngắn lệch nhau gây dừng thay lẻ liên tục!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Phối hợp Mua hàng chuyển sang cuộn băng thép quấn chéo (Traverse Wound Coil dài 2,500m) → Giảm 80% số lần dừng hàn, nâng [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) máy DSTA từ 58% lên 74%.
2. Chỉnh lại bước đan máy [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding) về mục tiêu 87% (giải phóng ngay +22% công suất cổ chai & tiết kiệm > 300 triệu tiền đồng mạ thiếc/năm!).
3. Quấn đồng bộ chiều dài 100% suốt Bobbin bằng nhau + lắp cảm biến đứt sợi [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka) triển khai [Man-Machine Chart](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-man-machine-chart) 1 thợ quản 6–8 máy Braiding!
6. **🔒 Khóa chuẩn chống tái diễn:** Chuẩn hóa quy cách mua băng thép 2,500m trên [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp) và treo bảng chuẩn góc đan + quy trình thay khay Bobbin đồng bộ tại máy.

**🔑 Từ khóa tra cứu nhanh:** [DSTA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dsta) · [Braiding](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-braiding) · [Tinned Copper](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tinned-copper) · [Time Study](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-time-study) · [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) · [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka) · [Man-Machine Chart](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-man-machine-chart)

---

## 4. Xưởng Đùn PVC / XLPE / LSZH / CCV

<a id="tinh-huong-sc16"></a>
### SC16: Đổi màu nhựa & đổi tiết diện trên máy đùn mất 55 phút và xả 25 kg nhựa phế
> 📍 **Trạm xảy ra:** [Trạm 04 (S04)](#tram-s04) | 📖 **Cẩm nang:** `smed` | 🎓 **Bài học:** [L3.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l3-3)

1. **🚨 Dấu hiệu hiện trường:** Mỗi ca máy đùn dây dân dụng có 2–3 lần đổi màu/tiết diện, mỗi lần dừng 45–60 phút (chiếm 20–25% thời gian ca!) và thải ra đống nhựa xả 25 kg + 80m dây đồng dính nhựa.
2. **💥 Tác động dòng chảy & chi phí:** Thủ phạm số 1 kéo tụt [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) Availability xưởng Đùn xuống dưới 65% và đội cao chi phí phế liệu.
3. **⏱️ Khoanh vùng ngay trong 24h:** Chọn 1 máy đùn cổ chai làm Pilot, quay video trọn vẹn 1 ca đổi mã từ mét dây đạt cuối cùng của lô A đến mét dây đạt đầu tiên của lô B.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Hơn 55% thời gian dừng là lãng phí thuần túy: máy dừng rồi mới đi kho lấy bao nhựa/bộ Chày–Cối, chờ 20 phút nung nóng bộ khuôn nguội mới lắp vào, vặn tay 4 con ốc lấy tâm trên đầu [Crosshead](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crosshead) cũ và xả tẩy bằng nhựa thường thay vì [Purging](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-purging) Compound.
5. **🛠️ Giải pháp OE & Số liệu tác động:**
Tổ chức Kaizen Blitz 5 ngày triển khai trọn bộ [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) 4 bước:
1. Tách Thao tác Ngoài (tốn 0 đồng): Soạn sẵn bao nhựa, xe đồ nghề [5S](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5s) Shadow Board, tủ sấy nóng sẵn bộ Chày–Cối ở 160°C trước khi dừng máy → Giảm ngay từ 55p xuống 30p!
2. Chuyển sang đầu [Crosshead](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crosshead) tự định tâm + nạp Recipe tự động trên [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi) + dùng 2.5 kg hạt [Purging](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-purging) Compound khi đổi màu tối → Rút xuống còn 12–14 phút (-76%) và nhựa xả giảm từ 25 kg xuống 6 kg!
3. Xếp lịch [Color Sequencing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-color-sequencing) Sáng → Tối giảm 70% số lần xả nặng.
6. **🔒 Khóa chuẩn chống tái diễn:** Khóa bằng [Standard Work](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-work) đổi mã 12 phút, kiểm định [2-Sample t-test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-2-sample-t-test) (p < 0.05) chứng minh hiệu quả 30 ngày Trước–Sau và kiểm tra tuân thủ hàng ngày trong [LSW](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lsw) Tổ trưởng.

**🔑 Từ khóa tra cứu nhanh:** [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) · [Crosshead](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crosshead) · [Purging](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-purging) · [Color Sequencing](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-color-sequencing) · [5S](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5s) · [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi) · [2-Sample t-test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-2-sample-t-test) · [LSW](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lsw)

---

<a id="tinh-huong-sc17"></a>
### SC17: Đường kính vỏ cáp dao động hình sin (Surging) buộc công nhân bọc dày +12% Over-thickness
> 📍 **Trạm xảy ra:** [Trạm 04 (S04)](#tram-s04) | 📖 **Cẩm nang:** `cable_extrusion_wire_forensics` | 🎓 **Bài học:** [L4.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l4-4)

1. **🚨 Dấu hiệu hiện trường:** Số đo trên [Laser Gauge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-laser-gauge) cứ nhảy lên xuống ±0.06 mm đều đặn theo chu kỳ 12 giây; sợ rớt t_min theo [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502), công nhân vặn tăng chiều dày trung bình lên +12% so với chuẩn!
2. **💥 Tác động dòng chảy & chi phí:** Lãng phí hàng trăm triệu đồng hạt nhựa mỗi năm trên mỗi dây chuyền đùn và năng lực quá trình [Cpk](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cpk) tụt xuống < 0.90.
3. **⏱️ Khoanh vùng ngay trong 24h:** Xuất log đồ thị [Melt Pressure](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-melt-pressure) và nhiệt độ 5 vùng nòng từ [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada)/[HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi) trong cùng khung giờ xảy ra dao động đường kính để so sánh pha dao động.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Đồ thị [Melt Pressure](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-melt-pressure) dao động sóng sin 195 ↔ 228 bar đúng nhịp 12 giây trùng khớp 100% dao động đường kính! Kiểm tra hiện trường phát hiện nhiệt độ vùng cấp liệu Zone 1 bị cài quá cao (155°C thay vì 135°C) làm hạt nhựa chảy dính bết vào cổ trục vít gây trượt cấp liệu chu kỳ (Feed Surging) + lưới lọc [Screen Pack](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-screen-pack) đã chạy quá hạn sắp tắc!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Hạ nhiệt độ Zone 1 về đúng 135°C, mở thông nước làm mát cổ phễu (Hopper Throat Cooling) và thay bộ lưới [Screen Pack](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-screen-pack) sạch → [Melt Pressure](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-melt-pressure) phẳng lặng ở 210 ± 2 bar!
2. Kích hoạt chế độ điều khiển vòng kín [Laser Gauge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-laser-gauge) Closed-loop liên động [Capstan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-capstan) kéo độ lệch chuẩn σ đường kính từ 0.055 mm xuống 0.018 mm ([Cpk](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cpk) nhảy từ 0.89 lên 1.65!).
3. Sau khi σ đã thu hẹp ổn định 2 tuần, mới mở phiếu [MOC / ECN](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-moc-ecn) dịch tâm chiều dày xuống sát t_nom (giảm 9.5% tiêu hao nhựa an toàn 100%!).
6. **🔒 Khóa chuẩn chống tái diễn:** Cài cảnh báo ngưỡng dao động [Melt Pressure](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-melt-pressure) (> ±5 bar) và ngưỡng áp suất thay [Screen Pack](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-screen-pack) (250 bar) tự động trên [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada) / [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes).

**🔑 Từ khóa tra cứu nhanh:** [Over-thickness](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-over-thickness) · [Melt Pressure](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-melt-pressure) · [Laser Gauge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-laser-gauge) · [Screen Pack](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-screen-pack) · [Cpk](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cpk) · [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502) · [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada) · [MOC / ECN](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-moc-ecn)

---

<a id="tinh-huong-sc18"></a>
### SC18: Đẩy tốc độ đùn cáp XLPE / ABC lên cao thì bề mặt bị sần nhám da cá mập (Sharkskin)
> 📍 **Trạm xảy ra:** [Trạm 04 (S04)](#tram-s04) | 📖 **Cẩm nang:** `cable_extrusion_wire_forensics` | 🎓 **Bài học:** [L4.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l4-4)

1. **🚨 Dấu hiệu hiện trường:** Để đáp ứng đơn hàng EVN, xưởng tăng tốc độ đùn lõi XLPE cáp [ABC Cable](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-abc-cable) từ 110 lên 135 m/phút thì vỏ cách điện xuất hiện gợn nhăn mờ sần đều khắp chu vi — công nhân định hạ tốc độ về lại 100 m/phút.
2. **💥 Tác động dòng chảy & chi phí:** Mất ngay 20–25% công suất máy đùn cổ chai ([OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) Performance giảm mạnh) hoặc bị QA trả lại vì lỗi ngoại quan.
3. **⏱️ Khoanh vùng ngay trong 24h:** Soi bề mặt lỗi dưới kính lúp phân biệt rõ: vân nhăn đều vuông góc chiều chạy (đích thị [Sharkskin](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sharkskin) do ứng suất trượt khuôn) — KHÔNG phải lỗ rỗ rải rác (ẩm) hay hạt lợn cợn (cháy Scorch).
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Ở tốc độ 135 m/phút, độ nhớt cao của nhựa XLPE khiến ứng suất cắt tại mép thoát Cối đùn vượt ngưỡng tới hạn (> 0.12 MPa), gây hiện tượng trượt–dính liên tục (Stick-Slip) xé rách bề mặt nhựa nóng chảy.
5. **🛠️ Giải pháp OE & Số liệu tác động:**
Xử lý đúng cơ chế vật lý để GIỮ TỐC ĐỘ CAO thay vì đầu hàng giảm tốc:
1. Tăng nhẹ riêng nhiệt độ vùng Đầu khuôn Die (+12 đến +15°C: từ 190°C → 205°C) để giảm độ nhớt cục bộ ngay tại thành khuôn mà không làm cháy nhựa trong nòng.
2. Nới nhẹ khe hở Cối (trong giới hạn [DDR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ddr) an toàn) dùng Cối có vùng dẫn hướng trơn mượt hơn.
3. Phối hợp Kỹ thuật bổ sung 0.5% phụ gia trợ gia công PPA tạo màng trượt siêu mỏng trong lòng khuôn.
→ Vỏ cáp bóng mịn ở đúng 135 m/phút (+22.7% năng suất!).
6. **🔒 Khóa chuẩn chống tái diễn:** Lưu thông số nhiệt độ Die mới + mã bộ Cối vào Recipe chuẩn trên [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi) và cập nhật [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan) dòng cáp ABC.

**🔑 Từ khóa tra cứu nhanh:** [Sharkskin](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sharkskin) · [ABC Cable](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-abc-cable) · [XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe) · [DDR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ddr) · [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) · [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi) · [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan)

---

<a id="tinh-huong-sc19"></a>
### SC19: Đùn vỏ cáp chống cháy LSZH bị nổ bọt rỗ khí và đóng cặn Die Drool phải dừng cạo 6 lần/ca
> 📍 **Trạm xảy ra:** [Trạm 06 (S06)](#tram-s06) | 📖 **Cẩm nang:** `cable_extrusion_wire_forensics` | 🎓 **Bài học:** [L4.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l4-4)

1. **🚨 Dấu hiệu hiện trường:** Chạy đơn hàng cáp [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) cho dự án bệnh viện, bề mặt vỏ nổi bọt khí li ti rớt [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester), đồng thời miệng khuôn Cối đóng cục cặn [Die Drool](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-die-drool) liên tục buộc thợ dừng máy cạo 6 lần/ca (mất 35 phút/ca!).
2. **💥 Tác động dòng chảy & chi phí:** Tỷ lệ phế cáp LSZH đắt tiền vọt lên 7.5%, trễ tiến độ công trình trọng điểm và nguy cơ xước hỏng miệng khuôn Cối.
3. **⏱️ Khoanh vùng ngay trong 24h:** Kiểm tra độ ẩm hạt LSZH trước khi vào phễu, đo nhiệt độ thực của dòng nhựa nóng chảy (Melt Temp) ngay đầu khuôn bằng súng/que đo và thu hồi dao sắt công nhân đang dùng cạo khuôn!
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** 1. Hạt nhựa [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) hút ẩm mạnh mùa mưa Đà Nẵng nhưng không được sấy kỹ qua [Hopper Dryer](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hopper-dryer).
2. Xưởng đang cho chạy LSZH trên máy dùng trục vít tỷ số nén cao của PVC & tốc độ quay vít quá nhanh → Nhiệt ma sát làm Melt Temp vượt 180°C khiến bột khoáng ATH phân hủy giải phóng hơi nước gây rỗ khí!
3. Công nhân dùng dao sắt cạo [Die Drool](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-die-drool) làm xước rỗ mép khuôn tạo ổ bám cặn nặng hơn + dùng sai bộ Cối có [DDR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ddr) 2.6 (quá cao so với ngưỡng 1.1–1.6 của LSZH!).
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Chuyển toàn bộ mã [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) sang máy có trục vít nén thấp (~1.2:1), sấy bắt buộc bằng [Hopper Dryer](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hopper-dryer) 70°C × 3h (dùng phễu sấy di động làm External [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed)), khống chế Melt Temp ≤ 165°C.
2. Đánh bóng mạ Chrome gương lòng Cối, vát nhẹ mép thoát 30°, đổi đúng bộ Chày–Cối có [DDR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ddr) = 1.35 và cấp 100% dao cạo bằng ĐỒNG THAU (Brass Scraper).
→ Phế rỗ khí giảm từ 7.5% xuống 0.6%, tốc độ đùn tăng +22% và chạy liên tục > 8 giờ không phải dừng cạo [Die Drool](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-die-drool)!
6. **🔒 Khóa chuẩn chống tái diễn:** Tách Routing tốc độ & máy chuyên dụng cho [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) trên [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp); đưa kiểm tra độ ẩm & dao đồng thau vào [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa).

**🔑 Từ khóa tra cứu nhanh:** [LSZH](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lszh) · [Die Drool](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-die-drool) · [Hopper Dryer](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hopper-dryer) · [DDR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ddr) · [L/D Ratio](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-l-d-ratio) · [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester) · [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) · [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa)

---

<a id="tinh-huong-sc20"></a>
### SC20: Trưa nắng Đà Nẵng 13h–16h nước máng làm mát nóng 34°C buộc hạ tốc độ máy đùn -20%
> 📍 **Trạm xảy ra:** [Trạm 06 (S06)](#tram-s06) | 📖 **Cẩm nang:** `oee` | 🎓 **Bài học:** [L2.1](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l2-1)

1. **🚨 Dấu hiệu hiện trường:** Dữ liệu [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) theo giờ cho thấy máy đùn vỏ cáp lực chạy đủ 100% tốc độ vào ca đêm và sáng sớm, nhưng cứ từ 13:00 đến 16:00 chiều lại giảm tốc -20% và vỏ cáp bị trầy xước bết dính khi cuộn lên rulo.
2. **💥 Tác động dòng chảy & chi phí:** Mất đều đặn 3 giờ chạy giảm tốc mỗi ngày vào suốt 5 tháng mùa nóng miền Trung (thiệt hại hàng chục km sản lượng/tháng).
3. **⏱️ Khoanh vùng ngay trong 24h:** Xuất dữ liệu lịch sử Historian từ [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada) (hoặc đo nhiệt độ nước máng [Cooling Trough](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cooling-trough) mỗi giờ suốt 3 ngày) vẽ biểu đồ phân tán [Scatter](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scatter) so với tốc độ máy đùn và tỷ lệ lỗi trầy vỏ.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Biểu đồ [Scatter](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scatter) chứng minh tương quan cực mạnh (r = +0.86, p < 0.001): lúc nắng gắt buổi trưa, tháp giải nhiệt bị bám rong rêu + béc phun nước máng nghẹt cặn vôi khiến nhiệt độ nước máng vọt từ 24°C lên 34°C → Vỏ cáp ra khỏi máng vẫn nóng 58°C chưa kịp đông cứng nên công nhân buộc phải giảm tốc độ đùn!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Vệ sinh tẩy cáu cặn vôi toàn bộ béc phun máng [Cooling Trough](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cooling-trough) & giàn tản nhiệt tháp giải nhiệt/Chiller.
2. Lắp vách ngăn đảo dòng nước ngược chiều (Counter-flow) nâng hiệu suất truyền nhiệt và bổ sung thêm 4 mét máng phụ có làm mát Chiller giữ nhiệt độ nước ổn định ≤ 24°C cả lúc trưa nắng.
3. Phối hợp gắn biến tần [VFD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-vfd) cho bơm tuần hoàn nước để tự động chạy mạnh buổi trưa và giảm tốc tiết kiệm 35% điện vào ca đêm mát!
→ Khôi phục 100% tốc độ đùn cả 3 ca (+18% sản lượng khung giờ chiều) và hoàn vốn [Payback](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-payback) < 8 tháng!
6. **🔒 Khóa chuẩn chống tái diễn:** Gắn cảm biến nhiệt độ nước máng lên [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada) cài ngưỡng cảnh báo Alarm > 27°C và lịch vệ sinh tháp giải nhiệt định kỳ trong [TPM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tpm).

**🔑 Từ khóa tra cứu nhanh:** [Cooling Trough](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cooling-trough) · [Scatter](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scatter) · [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada) · [VFD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-vfd) · [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) · [Payback](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-payback) · [TPM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tpm)

---

## 5. Chất Lượng Trực Tuyến, Lab & Khiếu Nại

<a id="tinh-huong-sc21"></a>
### SC21: Spark Tester báo lỗi thủng lỗ kim đột biến 15 lần trên 1 rulo dây dân dụng
> 📍 **Trạm xảy ra:** [Trạm 06 (S06)](#tram-s06) | 📖 **Cẩm nang:** `cable_mfg_machines` | 🎓 **Bài học:** [L1.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l1-4)

1. **🚨 Dấu hiệu hiện trường:** Đang đùn dây VC 2.5mm², màn hình [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester) liên tục nhảy số báo 15 lỗi phóng điện trong vòng 3,000m nhưng công nhân vẫn cố cho chạy hết rulo rồi mới dừng kiểm tra!
2. **💥 Tác động dòng chảy & chi phí:** Cả rulo 3,000m bị đánh dấu lỗi chi chít không cắt nổi thành khoanh 100m đạt chuẩn → Phế đồng dính nhựa hàng chục kg và nguy cơ lọt dây thủng cách điện ra thị trường!
3. **⏱️ Khoanh vùng ngay trong 24h:** Cách ly ngay rulo lỗi (treo thẻ Đỏ NCR), kiểm tra tiếp địa nối đất (Grounding) của đầu xả [Pay-off](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pay-off) & test mẫu lỗ kim chuẩn trên [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester); kiểm tra xem bộ thổi khô Air Wipe cuối máng nước có bị nước bắn vào đầu bi Spark gây báo giả không.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Sau khi loại trừ báo giả do nước đọng, cắt soi kính hiển vi 5 điểm thủng thấy: 3 điểm do hạt tạp chất cháy đen (rách lưới [Screen Pack](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-screen-pack) vì công nhân tự ý bỏ bớt tấm lưới mịn 120 Mesh!), 2 điểm do bọt ẩm hạt nhựa [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc) chưa sấy và máy không có liên động tự dừng [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka) khi vượt ngưỡng lỗi!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Khôi phục chuẩn bộ lưới lọc 40/80/120/40 Mesh trên [Screen Pack](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-screen-pack) và cấm tuyệt đối bỏ bớt lưới.
2. Tích hợp [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka) nối tín hiệu xung đếm lỗi từ [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester) về [PLC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-plc)/[MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes): nếu trong 500m dây xuất hiện ≥ 2 lỗi Spark liên tiếp → Máy TỰ ĐỘNG dừng ngay & bật đèn [Andon](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-andon) Đỏ!
3. Kiểm tra và nâng cấp bộ thổi khô Air Wipe trước Spark Tester để triệt tiêu 100% lỗi báo giả do nước đọng.
6. **🔒 Khóa chuẩn chống tái diễn:** Bổ sung test thanh lỗ kim chuẩn (Fault Simulator) + kiểm tra dây tiếp địa đầu ca vào [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan) và chấm điểm bắt buộc trong [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa).

**🔑 Từ khóa tra cứu nhanh:** [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester) · [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka) · [Andon](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-andon) · [Screen Pack](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-screen-pack) · [Pay-off](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pay-off) · [PLC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-plc) · [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan) · [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa)

---

<a id="tinh-huong-sc22"></a>
### SC22: Máy in phun vỏ cáp hết mực lúc 2h sáng, chạy hổng 10 km dây không chữ thương hiệu
> 📍 **Trạm xảy ra:** [Trạm 06 (S06)](#tram-s06) | 📖 **Cẩm nang:** `lean_muda` | 🎓 **Bài học:** [L3.1](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l3-1)

1. **🚨 Dấu hiệu hiện trường:** Vào 2 giờ sáng ca đêm, đầu in phun chữ lên vỏ dây hết mực/tắc vòi phun nhưng công nhân đang bận thay rulo ở đầu máy không phát hiện → Sáng ra phát hiện 10 km dây trơn bóng không có chữ CADIVI!
2. **💥 Tác động dòng chảy & chi phí:** Không được phép xuất bán theo quy chuẩn [QCVN 4](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-qcvn-4) — phải mang chạy in lại chậm tốn nhân công hoặc tuốt bỏ gây thiệt hại hàng chục triệu đồng.
3. **⏱️ Khoanh vùng ngay trong 24h:** Khoanh vùng toàn bộ các rulo sản xuất trong ca 3, tách riêng phần dây không có chữ để đánh giá phương án in lại trên máy sang cuộn (Rewinder) hay xử lý thu hồi.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Chỉ dựa vào 'sự chú ý quan sát bằng mắt của con người' ở ca đêm lúc 2–4h sáng (lúc sinh học con người mệt mỏi nhất!) mà thiếu hoàn toàn cơ chế chống sai lỗi [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke).
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Lắp cảm biến quang học tương phản (Contrast/Vision Sensor) đặt cách đầu in 1 mét nối về [PLC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-plc): nếu sau 5 mét dây chạy qua mà không đọc thấy nhịp vạch chữ in → Còi hú, bật đèn [Andon](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-andon) và tự động dừng máy!
2. Gắn thêm cảnh báo mức bình mực thấp 15% trên màn hình [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi) đầu máy.
3. Chi phí lắp đặt chỉ ~8 triệu đồng, triệt tiêu 100% lỗi mất chữ in mãi mãi ([Payback](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-payback) ngay từ vụ đầu tiên tránh được!).
6. **🔒 Khóa chuẩn chống tái diễn:** Đưa kiểm tra cảm biến đọc chữ in vào bảng khởi động máy đầu ca ([Standard Work](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-work)) và bảo trì vệ sinh đầu in định kỳ.

**🔑 Từ khóa tra cứu nhanh:** [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) · [QCVN 4](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-qcvn-4) · [PLC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-plc) · [Andon](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-andon) · [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi) · [Payback](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-payback) · [Standard Work](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-work)

---

<a id="tinh-huong-sc23"></a>
### SC23: Lô cáp lực XLPE Silane rớt phép thử Hot Set Test (200°C) sau khi đã xông hơi 8 tiếng
> 📍 **Trạm xảy ra:** [Trạm 07 (S07)](#tram-s07) | 📖 **Cẩm nang:** `cable_mfg_machines` | 🎓 **Bài học:** [L4.5](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l4-5)

1. **🚨 Dấu hiệu hiện trường:** Phòng Lab báo mẫu cắt từ 4 rulo cáp CXV 3×95 sau khi xông hơi 8 giờ bị kéo giãn 210% (vượt trần ≤ 175% của [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test)), có mẫu đứt luôn trong tủ 200°C!
2. **💥 Tác động dòng chảy & chi phí:** Tắc 4 rulo cáp lực trị giá hơn 800 triệu đồng không được phép xuất xưởng, nguy cơ trễ hạn hợp đồng dự án lớn.
3. **⏱️ Khoanh vùng ngay trong 24h:** Giữ cách ly toàn bộ 4 rulo, lấy thêm mẫu ở đầu/cuối rulo khác cùng mẻ chạy lại [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test) và kiểm tra ngay log nhiệt độ phòng xông Sauna + log định lượng phễu xúc tác Catalyst của máy đùn.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Dùng [5 Whys](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5-whys) & [Ishikawa](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ishikawa) tách 2 nguyên nhân gốc có thể: (A) Thiếu độ ẩm/nhiệt độ phòng xông Sauna bị tụt xuống 58°C do hỏng van bẫy hơi (có thể cứu được bằng cách xông bù thêm 6h!) vs (B) Công nhân quên bật bộ định lượng 5% hạt xúc tác Catalyst [Silane](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-silane) (hoặc phễu Catalyst bị tắc nghẽn) lúc đùn → Hạt nhựa hoàn toàn không khâu mạch được (bắt buộc xử lý loại bỏ!).
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Nếu nguyên nhân do van hơi Sauna: sửa van, đưa 4 rulo xông bổ sung đủ 85°C × 6h rồi test lại [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test) đạt 100% (cứu trọn 800 triệu!).
2. Nếu nguyên nhân do thiếu Catalyst: lắp ngay cảm biến lưu lượng/báo cạn phễu Catalyst nối liên động [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) với [PLC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-plc) máy đùn (phễu Catalyst ngừng quay hoặc cạn → máy đùn KHÔNG thể chạy!).
3. Gắn cảm biến nhiệt độ & độ ẩm tự ghi đồ thị phòng Sauna lên [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada).
6. **🔒 Khóa chuẩn chống tái diễn:** Cập nhật [PFMEA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pfmea) nâng mức kiểm soát phát hiện thiếu Catalyst và bắt buộc kiểm tra đối chiếu kg Catalyst tiêu thụ vs kg nhựa nền cuối mỗi ca (tỷ lệ chuẩn 5:95).

**🔑 Từ khóa tra cứu nhanh:** [Hot Set Test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hot-set-test) · [Silane](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-silane) · [XLPE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-xlpe) · [5 Whys](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5-whys) · [Ishikawa](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ishikawa) · [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) · [PFMEA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pfmea) · [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada)

---

<a id="tinh-huong-sc24"></a>
### SC24: Cáp trung thế 24kV rớt bài thử Phóng điện cục bộ Partial Discharge (14 pC > chuẩn 5 pC)
> 📍 **Trạm xảy ra:** [Trạm 07 (S07)](#tram-s07) | 📖 **Cẩm nang:** `cable_mfg_machines` | 🎓 **Bài học:** [L4.5](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l4-5)

1. **🚨 Dấu hiệu hiện trường:** Trong phòng lồng Faraday, cuộn cáp trung thế 24kV dài 500m đo được phóng điện cục bộ [Partial Discharge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-partial-discharge) lên tới 14 pC tại điện áp 1.73 U0 (rớt xa chuẩn ≤ 5 pC theo [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502)-2!).
2. **💥 Tác động dòng chảy & chi phí:** Một rulo cáp trung thế hỏng thiệt hại vài trăm triệu đồng và uy tín nghiêm trọng nếu lọt ra lưới điện ngầm.
3. **⏱️ Khoanh vùng ngay trong 24h:** Dùng thiết bị định vị phản xạ xung (TDR) xác định chính xác vị trí điểm phóng điện nằm tại mét thứ 420 trên rulo 500m; truy ngược ngay dữ liệu lịch sử dây chuyền [CCV](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ccv) trên [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes) / [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada) đúng thời điểm chạy qua mét 420!
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Log [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada) tại đúng thời điểm chạy mét 420 cho thấy áp suất khí Nitơ trong ống lưu hóa [CCV](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ccv) bị sụt đột ngột từ 12.0 bar xuống 7.5 bar trong 20 giây do van điều áp gặp sự cố → Tạo vi bọt khí (Micro-voids) bên trong lớp cách điện XLPE tại đúng đoạn mét 410–430!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Cắt bỏ đúng đoạn 30m lỗi (mét 405–435), thử lại [Partial Discharge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-partial-discharge) đoạn 400m còn lại đạt 1.2 pC (≤ 5 pC) — cứu được 80% giá trị rulo cáp!
2. Phối hợp Cơ Điện bảo trì/lắp van điều áp Nitơ dự phòng song song và tích hợp cảnh báo tự đánh dấu vị trí mét trên [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes) ngay khi áp suất Nitơ sụt dưới 10.5 bar.
3. Kiểm toán lại kỷ luật phòng sạch (Cleanroom) nạp hạt nhựa XLPE Peroxide tránh bụi tạp chất.
6. **🔒 Khóa chuẩn chống tái diễn:** Lập quy trình [8D](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-8d) đóng triệt để sự cố, đưa kiểm định van áp suất khí Nitơ vào lịch [CBM / PdM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cbm-pdm) ưu tiên bậc 1 của dây chuyền [CCV](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ccv).

**🔑 Từ khóa tra cứu nhanh:** [Partial Discharge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-partial-discharge) · [CCV](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ccv) · [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502) · [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes) · [SCADA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scada) · [8D](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-8d) · [CBM / PdM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cbm-pdm)

---

<a id="tinh-huong-sc25"></a>
### SC25: Cầu đo Kelvin Bridge báo rớt điện trở buổi trưa nóng & khách khiếu nại vỏ cáp CXV 'khó tuốt'
> 📍 **Trạm xảy ra:** [Trạm 07 (S07)](#tram-s07) | 📖 **Cẩm nang:** `planning_quality_ehs_cost` | 🎓 **Bài học:** [L4.5](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l4-5)

1. **🚨 Dấu hiệu hiện trường:** Gặp đồng thời 2 sự cố chất lượng: (A) 13h trưa Lab đo mẫu ruột cáp 50mm² được 0.395 Ω/km báo rớt chuẩn [IEC 60228](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60228) (≤ 0.387 Ω/km) đòi dừng Xưởng Kéo; (B) Khách hàng công trình khiếu nại vỏ cáp CXV dính chặt khó tuốt khi đấu tủ điện.
2. **💥 Tác động dòng chảy & chi phí:** Dừng máy oan gây mất sản lượng hoặc làm khách hàng công trình bức xúc đòi trả hàng.
3. **⏱️ Khoanh vùng ngay trong 24h:** Tình huống A: Kiểm tra ngay nhiệt độ phòng Lab & nhiệt độ mẫu đồng đang đo (30°C hay mẫu vừa cắt nóng 45°C từ máy ra?). Tình huống B: Kiểm tra bộ Chày–Cối đã dùng trên máy đùn vỏ ở lệnh SX đó qua truy xuất mã rulo [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes).
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** A: Nhân viên Lab mới quên nhân hệ số quy đổi về 20°C (ở 30°C, R_20 = 0.395 / [1 + 0.00393×10] = 0.380 Ω/km — ĐẠT 100% chuẩn!).
B: Truy xuất [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes) thấy công nhân lắp nhầm bộ Chày–Cối kiểu Pressure (bọc áp lực lấp khe) thay vì kiểu Tubing (bọc ống) khi đùn lớp vỏ ngoài PVC cho cáp 4 lõi → Nhựa ép dính chặt cứng vào 4 lõi bên trong!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Cho Phòng Lab: Xây công cụ Excel/form tự động nhập nhiệt độ phòng & tự quy đổi R_20, bắt buộc để mẫu ổn định nhiệt 30 phút trong phòng 20–25°C trước khi kẹp [Kelvin Bridge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kelvin-bridge), chạy thẩm định [MSA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-msa) / [Gage R&R](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-gage-r-r).
2. Cho Xưởng Đùn vỏ: Triển khai [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) khắc laser chữ 'P' (Pressure) vs 'T' (Tubing) + sơn mã màu phân biệt ngay trên thân Chày–Cối và dịch VOC 'dễ tuốt vỏ' thành thông số CTQ lực bóc vỏ trong [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan)!
6. **🔒 Khóa chuẩn chống tái diễn:** Đào tạo chuẩn 1 điểm [OPL](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sop) về quy đổi nhiệt độ 20°C tại Lab và kiểm tra mã 'T'/'P' trước khi đóng đầu [Crosshead](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crosshead) tại Xưởng Đùn.

**🔑 Từ khóa tra cứu nhanh:** [Kelvin Bridge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kelvin-bridge) · [IEC 60228](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60228) · [MSA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-msa) · [Gage R&R](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-gage-r-r) · [Crosshead](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-crosshead) · [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) · [VOC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-voc) · [CTQ](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ctq) · [SOP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sop)

---

## 6. Đóng Cuộn, Cut-Length, BOM & Phế Liệu

<a id="tinh-huong-sc26"></a>
### SC26: Đơn hàng cáp lực dự án nhiều đoạn lẻ gây dư hàng trăm mét mẩu thừa Cut-Length
> 📍 **Trạm xảy ra:** [Trạm 08 (S08)](#tram-s08) | 📖 **Cẩm nang:** `cable_cost_capacity` | 🎓 **Bài học:** [L5.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l5-3)

1. **🚨 Dấu hiệu hiện trường:** Đơn hàng cáp CXV 3×95+1×50 có 6 đoạn lẻ: 620m, 580m, 450m, 350m, 750m, 250m. Tổ cắt đoạn cứ lấy rulo chuẩn 1,500m cắt lần lượt theo danh sách làm dư ra 2 khúc lẻ 170m và 130m không bán được cho ai!
2. **💥 Tác động dòng chảy & chi phí:** 300 mét cáp lực 3×95+1×50 thừa bị tuốt phế gây lỗ ngay > 110 triệu đồng chỉ trong 1 đơn hàng dự án!
3. **⏱️ Khoanh vùng ngay trong 24h:** Tạm dừng cắt tùy tiện — gom danh sách tất cả các đoạn cắt dự án cùng chủng loại cáp trong tuần lại trên 1 bảng Excel để tổ hợp lại ngay.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** 1. Không áp dụng thuật toán tổ hợp cắt (1D Cutting Stock Problem) ở Trạm 08.
2. Phòng Kế hoạch phát lệnh cố định rulo 1,500m ở Trạm 03–04 mà không nhìn ngược danh sách tổng chiều dài các đoạn khách đặt!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Xây công cụ Excel Solver / [Python](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-python) (PuLP) tối ưu [Cut-Length](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cut-length) chỉ tốn 30 giây chạy: ghép Rulo 1 = 620 + 580 + 250 = 1,450m (dư 50m) và Rulo 2 = 750 + 450 + 350 = 1,550m (đặt chạy đúng 1,560m ngay từ lệnh Xưởng Bện & Đùn!).
2. Với các đoạn dư dài > 80m còn lại, tạo danh mục 'Kho Đoạn Lẻ Tái Dùng' hiển thị cho Phòng Kinh doanh ưu tiên chào bán cho khách cần đoạn ngắn trước khi phát lệnh cắt mới.
→ Giảm phế [Cut-Length](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cut-length) từ 9.5% xuống dưới 1.2%!
6. **🔒 Khóa chuẩn chống tái diễn:** Bắt buộc chạy bảng tổ hợp [Cut-Length](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cut-length) trước khi phát lệnh SX cáp lực dự án tại Phòng Kế hoạch (Trạm 00).

**🔑 Từ khóa tra cứu nhanh:** [Cut-Length](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cut-length) · [Python](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-python) · [Excel](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-excel) · [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) · [Scrap](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scrap) · [MRP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mrp)

---

<a id="tinh-huong-sc27"></a>
### SC27: Khách hàng phàn nàn cuộn dây thiếu mét — hoặc kiểm tra thấy xưởng tặng thừa +0.8m/cuộn
> 📍 **Trạm xảy ra:** [Trạm 06 (S06)](#tram-s06) | 📖 **Cẩm nang:** `cable_mfg_machines` | 🎓 **Bài học:** [L1.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l1-2)

1. **🚨 Dấu hiệu hiện trường:** Kiểm tra đối chiếu chiều dài thực bằng bàn đo chuẩn 100m phát hiện máy đánh cuộn số 1 đang cắt thực tế 100.8m (tặng không +0.8%!), còn máy số 3 lại cắt hụt chỉ 99.3m (nguy cơ bị khách kiện gian lận!).
2. **💥 Tác động dòng chảy & chi phí:** Thừa +0.8m trên 50,000 khoanh dây VC/tháng = tặng không **40,000 mét dây đồng/tháng** (hàng trăm triệu đồng!); hụt -0.7m thì hủy hoại uy tín thương hiệu quốc gia CADIVI!
3. **⏱️ Khoanh vùng ngay trong 24h:** Dừng kiểm chuẩn tức thời 100% bánh xe đo mét (Meter Counter Wheel / Encoder) trên tất cả máy đùn và máy đánh cuộn bằng thước chuẩn/sợi chuẩn 50m.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** 1. Bánh xe đo mét bằng cao su bị mòn dần đường kính ngoài đi 0.8% sau 6 tháng chạy ma sát mà không có lịch hiệu chuẩn định kỳ → Cùng 1 vòng quay Encoder nhưng dây chạy qua dài hơn 0.8%!
2. Hoặc lực ép bánh đo lỏng gây trượt (Slip) làm đếm thiếu mét (cắt thừa) hoặc dây kéo căng giãn đàn hồi khi nóng rồi co rút lại lúc nguội (cắt thiếu!).
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Thay bánh xe đo mét bằng vật liệu chống mòn cao (hoặc đầu đo chiều dài không tiếp xúc Laser Doppler Velocimeter cho dây chuyền sản lượng lớn).
2. Cài đặt hệ số bù co rút nhiệt chuẩn theo từng loại nhựa và siết chu kỳ kiểm chuẩn sai số mét (≤ ±0.2%) hàng tuần.
3. Áp dụng kiểm tra đối chứng trọng lượng (Check-weigher) cuối chuyền đóng khoanh 100m như lớp [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) thứ 2 (cuộn dây nhẹ hoặc nặng bất thường tự báo còi!).
6. **🔒 Khóa chuẩn chống tái diễn:** Đưa lịch hiệu chuẩn Encoder đo mét vào hệ thống [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) hàng tuần và hồ sơ kiểm định thiết bị [ISO 9001](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iso-9001).

**🔑 Từ khóa tra cứu nhanh:** [Capstan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-capstan) · [Poka-Yoke](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-poka-yoke) · [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) · [ISO 9001](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iso-9001) · [Laser Gauge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-laser-gauge)

---

<a id="tinh-huong-sc28"></a>
### SC28: Cuối tháng Kế toán báo âm BOM nhựa PVC +4.9% dù chiều dày đo trên máy đùn đúng chuẩn 100%
> 📍 **Trạm xảy ra:** [Trạm 01 (S01)](#tram-s01) | 📖 **Cẩm nang:** `cable_extrusion_wire_forensics` | 🎓 **Bài học:** [L5.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l5-2)

1. **🚨 Dấu hiệu hiện trường:** Báo cáo [Standard Cost](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-cost) cuối tháng cho thấy Xưởng Đùn tiêu hao vượt định mức [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) +4.9% kg hạt nhựa PVC vỏ (~280 triệu/tháng), dù Tổ trưởng & QA khẳng định chiều dày đo bằng [Laser Gauge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-laser-gauge) và kính hiển vi đều đúng chuẩn t_nom!
2. **💥 Tác động dòng chảy & chi phí:** Xưởng bị trừ thưởng oan, Kế toán nghi ngờ thất thoát kho hoặc báo cáo ảo.
3. **⏱️ Khoanh vùng ngay trong 24h:** Lấy mẫu hạt nhựa PVC của 3 lô nhập gần nhất mang đo tỷ trọng riêng (Specific Gravity — g/cm³) và hàm lượng tro bột đá [CaCO3 Filler](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-caco3-filler) tại Phòng Lab.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Phát hiện 'Bẫy tỷ trọng [CaCO3 Filler](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-caco3-filler)': Định mức [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) trên [ERP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-erp) được lập với tỷ trọng PVC chuẩn 1.40 g/cm³, nhưng nhà cung cấp mới (bán rẻ hơn 3% theo VNĐ/kg!) đã trộn tăng hàm lượng bột đá CaCO3 đẩy tỷ trọng thực tế lên 1.47–1.50 g/cm³ (+5% đến +7%)! Vì máy đùn bọc theo THỂ TÍCH (chiều dày mm), hạt nặng hơn 5% chắc chắn làm tốn thêm 5% kg nhựa dù chiều dày chuẩn từng 0.01 mm!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Chứng minh bằng công thức VNĐ/lít = (Đơn giá VNĐ/kg) × (Tỷ trọng kg/lít): Hạt rẻ hơn 3%/kg nhưng nặng hơn 6% thực chất ĐẮT HƠN +2.8% trên mỗi mét cáp, chưa kể còn giảm [Tensile](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tensile) & làm mòn trục vít!
2. Bổ sung tiêu chuẩn khống chế Tỷ trọng tối đa (vd: ≤ 1.42 ± 0.02 g/cm³) vào Hợp đồng Mua hàng và Phiếu kiểm tra IQC đầu vào (Trạm 01).
3. Phối hợp Kế toán tách rõ chênh lệch do Tỷ trọng NVL khỏi chênh lệch vận hành của Xưởng Đùn!
6. **🔒 Khóa chuẩn chống tái diễn:** Đưa đo tỷ trọng 100% lô hạt PVC nhập kho vào [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan) IQC và bảng đánh giá nhà cung cấp theo chi phí VNĐ/dm³.

**🔑 Từ khóa tra cứu nhanh:** [CaCO3 Filler](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-caco3-filler) · [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc) · [BOM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-bom) · [Standard Cost](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-cost) · [Laser Gauge](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-laser-gauge) · [Tensile](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tensile) · [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan)

---

<a id="tinh-huong-sc29"></a>
### SC29: Thùng phế liệu vứt lẫn đồng trần với đồng dính nhựa làm mất 30% giá trị thu hồi
> 📍 **Trạm xảy ra:** [Trạm 09 (S09)](#tram-s09) | 📖 **Cẩm nang:** `bom_cost` | 🎓 **Bài học:** [L5.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l5-4)

1. **🚨 Dấu hiệu hiện trường:** Đi [Genba](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-genba) khu tập kết phế liệu thấy các thùng phế từ Xưởng Kéo, Bện, Đùn vứt chung cả sợi đồng trần tinh khiết, đoạn cáp dính nhựa PVC/XLPE, băng thép và giẻ lau dầu!
2. **💥 Tác động dòng chảy & chi phí:** Đồng trần tinh khiết bán/tái nấu thu hồi ~94% giá trị đồng gốc, còn đồng lẫn nhựa dính tạp chất chỉ bán được ~65–70% (hoặc tốn thêm nhân công máy tuốt) → Đánh mất hàng trăm triệu đồng mỗi năm!
3. **⏱️ Khoanh vùng ngay trong 24h:** Cân phân loại thực tế 1 tuần phế liệu tại 4 xưởng để tính ra đúng số tiền mất đi do trộn lẫn (trình số liệu trực quan cho Giám đốc & Quản đốc).
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** 1. Dưới chân máy chỉ đặt 1 thùng rác chung không phân loại.
2. Trên [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp) màn hình xác nhận lệnh CO11N chỉ có 1 mã 'Phế phẩm chung' không tách mã Đồng trần vs Đồng dính nhựa vs Nhựa purge sạch nên không ai quan tâm phân loại!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Triển khai hệ thống 3 thùng phế mã màu [5S](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5s) cố định ngay tại mọi chân máy:
   • Thùng XANH: Đồng trần tinh khiết (thu hồi ~94%).
   • Thùng VÀNG: Đồng dính nhựa (chuyển máy tuốt bóc tách).
   • Thùng XÁM (lót khay inox sạch): Nhựa [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc) purge sạch (nghiền tái chế Regrind dùng hợp lệ làm lớp độn Bedding!).
2. Mở 3 mã Reason Code phế riêng biệt trên [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp) / [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes) và cân ghi nhận riêng từng loại cuối mỗi ca.
3. Gắn thưởng nhóm [Kaizen](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kaizen) cho phân xưởng đạt tỷ lệ phân loại sạch 100%.
6. **🔒 Khóa chuẩn chống tái diễn:** Đưa tiêu chí 'Thùng phế 3 màu không lẫn tạp chất' thành 1 câu hỏi bắt buộc trong phiếu kiểm tra [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa) hàng ngày.

**🔑 Từ khóa tra cứu nhanh:** [Scrap](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-scrap) · [5S](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5s) · [SAP PP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sap-pp) · [PVC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pvc) · [Kaizen](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kaizen) · [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa) · [Genba](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-genba)

---

<a id="tinh-huong-sc30"></a>
### SC30: Tổ đóng khoanh 100m dây dân dụng ùn ứ cuối ca, xin tuyển thêm 3 công nhân thời vụ
> 📍 **Trạm xảy ra:** [Trạm 08 (S08)](#tram-s08) | 📖 **Cẩm nang:** `ole` | 🎓 **Bài học:** [L2.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l2-4)

1. **🚨 Dấu hiệu hiện trường:** Khi Xưởng Đùn tăng tốc nhờ [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed), tổ đóng khoanh 100m gồm 6 người không kịp đóng gói (ùn 40 rulo cuối ca), Tổ trưởng đề xuất tuyển gấp thêm 3 nhân sự mới.
2. **💥 Tác động dòng chảy & chi phí:** Tốn thêm ~300 triệu chi phí lương/năm trong khi hiệu suất thực tế của 6 người hiện tại chưa được đo đạc khoa học.
3. **⏱️ Khoanh vùng ngay trong 24h:** OE xuống bấm giờ [Time Study](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-time-study) & [Work Sampling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-work-sampling) cả 6 vị trí trong tổ đóng khoanh (Cuốn dây – Cột dây – Dán tem – Bọc màng co – Xếp thùng/pallet – Đẩy xe) và vẽ sơ đồ di chuyển [Spaghetti](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spaghetti).
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Biểu đồ [Yamazumi](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-yamazumi) phơi bày sự mất cân bằng nghiêm trọng (Balance Efficiency chỉ 61%!): Người đứng máy cuốn chạy 18 giây/khoanh trong khi người dán tem + bọc màng mất 32 giây/khoanh (nút thắt!) còn người xếp pallet nhàn rỗi chờ tới 45% thời gian; bàn đóng gói đặt rời rạc làm công nhân phải đi bộ trung bình 4.5 km/ca!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Sắp xếp lại mặt bằng tổ đóng khoanh theo Layout chữ U sát nhau (dùng [AutoCAD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-autocad) & con lăn trượt trọng lực chuyển khoanh giữa các bước → cắt 70% quãng đường trên sơ đồ [Spaghetti](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spaghetti)!).
2. Tái phân bổ thao tác trên [Yamazumi](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-yamazumi): tách bước dán tem nhãn chuyển sang hỗ trợ từ vị trí xếp pallet nhàn rỗi, dùng máy bắn dây đai bán tự động → Đẩy Balance Efficiency từ 61% lên 88%, nâng sản lượng tổ 6 người từ 950 lên 1,380 khoanh/ca (+45%) mà KHÔNG cần tuyển thêm 1 người nào!
6. **🔒 Khóa chuẩn chống tái diễn:** Ban hành [Standard Work](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-work) theo Takt Time từng vị trí và theo dõi chỉ số [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) tổ đóng cuộn hàng ngày trên bảng [Visual Management](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-visual-management).

**🔑 Từ khóa tra cứu nhanh:** [Yamazumi](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-yamazumi) · [Time Study](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-time-study) · [Work Sampling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-work-sampling) · [Spaghetti](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spaghetti) · [AutoCAD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-autocad) · [OLE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ole) · [Standard Work](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-work) · [Headcount Planning](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-headcount-planning)

---

## 7. Bảo Trì, Năng Lượng & An Toàn LOTO

<a id="tinh-huong-sc31"></a>
### SC31: Cháy tủ điện biến tần máy đùn cổ chai giữa mùa cao điểm gây dừng máy 3 ngày
> 📍 **Trạm xảy ra:** [Trạm 09 (S09)](#tram-s09) | 📖 **Cẩm nang:** `oe_field_execution_case_test` | 🎓 **Bài học:** [L6.1](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l6-1)

1. **🚨 Dấu hiệu hiện trường:** Đang chạy cao điểm đơn hàng lớn, tủ điện biến tần chính của máy đùn số 3 bốc khói cháy cầu dao tổng — nhà máy phải dừng cổ chai suốt 72 giờ chờ linh kiện thay thế!
2. **💥 Tác động dòng chảy & chi phí:** Thiệt hại trực tiếp chi phí sửa chữa + mất sản lượng xuất xưởng > 300 triệu đồng, phá vỡ kế hoạch giao hàng cả tuần.
3. **⏱️ Khoanh vùng ngay trong 24h:** Khoanh vùng đảm bảo an toàn điện [LOTO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loto), điều chuyển tạm các đơn gấp sang máy đùn khác và kiểm tra ngay toàn bộ tủ điện các máy đùn/máy kéo còn lại để phòng cháy dây chuyền.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Nhà máy chỉ chạy bảo trì 'hỏng mới sửa' (Reactive) và kiểm tra bằng mắt thường — đầu cos tiếp điểm bị lỏng phát nhiệt âm thầm lên 108°C trong nhiều tuần (giai đoạn P trên đường cong P–F) nhưng không ai phát hiện cho tới khi bốc cháy (Điểm F)!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Đề xuất đầu tư 1 camera ảnh nhiệt cầm tay (~25 triệu) + bút đo rung bạc đạn triển khai bảo trì dự đoán [CBM / PdM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cbm-pdm) định kỳ hàng tháng cho 100% tủ điện, biến tần và ổ bi máy cổ chai (RBD, Rigid Strander, Extruder).
2. Thiết lập danh mục phụ tùng chiến lược (Critical Spare Parts — biến tần, cặp nhiệt điện, cầu dao tổng) kèm mức [Safety Stock](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-safety-stock) riêng.
3. Gắn Ma trận leo thang sự cố [Escalation Matrix](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-escalation-matrix) (5p–15p–30p) để rút ngắn [MTTR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mttr) khi có dấu hiệu bất thường.
→ Lần soi nhiệt đầu tiên đã phát hiện sớm 4 đầu cos nóng > 95°C và siết lại trong 15 phút nghỉ trưa — tránh được 4 vụ cháy tủ điện!
6. **🔒 Khóa chuẩn chống tái diễn:** Đưa lịch soi ảnh nhiệt + đo rung định kỳ vào hệ thống [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) và theo dõi chỉ số [MTBF](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mtbf) tăng liên tục hàng quý.

**🔑 Từ khóa tra cứu nhanh:** [CBM / PdM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cbm-pdm) · [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) · [MTBF](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mtbf) · [MTTR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mttr) · [LOTO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loto) · [Escalation Matrix](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-escalation-matrix) · [TPM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tpm)

---

<a id="tinh-huong-sc32"></a>
### SC32: Đội Cơ Điện luôn than 'quá tải thiếu người' nhưng sự cố hỏng máy vẫn tăng liên tục
> 📍 **Trạm xảy ra:** [Trạm 09 (S09)](#tram-s09) | 📖 **Cẩm nang:** `oe_field_execution_case_test` | 🎓 **Bài học:** [L6.1](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l6-1)

1. **🚨 Dấu hiệu hiện trường:** Phòng Cơ Điện có 8 kỹ thuật viên liên tục tăng ca cuối tuần và xin tuyển thêm 3 thợ mới, nhưng tỷ lệ [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) vẫn chỉ đạt 58% và dừng máy sự cố Breakdown không giảm.
2. **💥 Tác động dòng chảy & chi phí:** Chi phí tăng ca bảo trì cao, thợ kiệt sức chạy chữa cháy, còn Xưởng Sản xuất thì kêu trời vì máy hay hỏng giữa ca.
3. **⏱️ Khoanh vùng ngay trong 24h:** OE trao đổi minh bạch với Trưởng phòng Cơ Điện rằng sẽ đo [Wrench Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wrench-time) bằng [Work Sampling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-work-sampling) trong 5 ngày để tìm các rào cản hành chính đang làm mất thời gian của anh em thợ (tuyệt đối KHÔNG dùng để chấm phạt cá nhân!).
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Kết quả [Work Sampling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-work-sampling) gây sốc: [Wrench Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wrench-time) thực tế chỉ đạt 31%! Tới 69% thời gian thợ Cơ Điện bị đốt vào: chờ kho phụ tùng tìm vòng bi/điện trở (22%), chờ Sản xuất bàn giao dừng máy (18%), đi đi lại lại lấy thiếu cờ-lê (14%), chờ duyệt phiếu/hỏi lệnh (15%)!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Tổ chức [5S](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5s) lại Kho phụ tùng cơ điện dán mã theo từng máy & áp dụng [Kitting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kitting): soạn sẵn trọn bộ phụ tùng + bản vẽ + dụng cụ vào khay trước ngày làm PM 24 giờ!
2. Chốt 'Cửa sổ Bảo trì Vàng' (4 giờ cố định mỗi sáng Chủ nhật xen kẽ từng cụm máy) trực tiếp trong lịch [MPS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mps) — Xưởng Sản xuất bắt buộc bàn giao máy đúng giờ!
3. Trang bị xe đẩy đồ nghề di động đầy đủ dụng cụ chuẩn cho từng tổ bảo trì.
→ [Wrench Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wrench-time) tăng từ 31% lên 49% (+58% năng lực bảo trì thực, tương đương tuyển miễn phí thêm 4.5 kỹ thuật viên giỏi!), [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) vọt lên 93% và Breakdown giảm 48%!
6. **🔒 Khóa chuẩn chống tái diễn:** Gắn KPI [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) ≥ 90% và tỷ lệ Công việc có kế hoạch vs Chữa cháy (80/20) vào báo cáo tuần Phòng Cơ Điện.

**🔑 Từ khóa tra cứu nhanh:** [Wrench Time](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-wrench-time) · [Work Sampling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-work-sampling) · [PM Compliance](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pm-compliance) · [Kitting](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kitting) · [5S](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5s) · [MPS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mps) · [TPM](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tpm)

---

<a id="tinh-huong-sc33"></a>
### SC33: Hóa đơn tiền điện & chỉ số SEC (kWh/tấn đồng) tăng vọt +14% so với trung bình năm
> 📍 **Trạm xảy ra:** [Trạm 09 (S09)](#tram-s09) | 📖 **Cẩm nang:** `planning_quality_ehs_cost` | 🎓 **Bài học:** [L5.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l5-4)

1. **🚨 Dấu hiệu hiện trường:** Phòng Kế toán báo tháng vừa rồi tiền điện toàn nhà máy tăng bất thường +14% (~160 triệu VNĐ) dù sản lượng tấn cáp xuất xưởng gần như không đổi!
2. **💥 Tác động dòng chảy & chi phí:** Ăn mòn trực tiếp biên lợi nhuận sản xuất và vi phạm mục tiêu tiết kiệm năng lượng [ISO 50001](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iso-50001).
3. **⏱️ Khoanh vùng ngay trong 24h:** Đi kiểm tra nhà máy vào giờ nghỉ trưa/Chủ nhật khi máy sản xuất dừng (lắng nghe tiếng xì rò khí nén + ghi chỉ số công tơ điện chạy không tải Base Load!) và xuất dữ liệu hồi quy điện năng theo từng phân xưởng.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Chạy phương trình hồi quy [Regression](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-regression) (`kWh = Base_Load + b × Tấn`) phơi bày 3 ổ đốt điện khổng lồ:
1. Hệ thống khí nén rò rỉ tới 27 điểm van/khớp nối làm máy nén khí chạy tải 70% ngay cả lúc xưởng nghỉ!
2. Cụm bơm nước giải nhiệt 45kW & quạt tháp chạy cố định 50Hz suốt ca đêm non tải.
3. Lò nung máy đùn bật sấy nóng trước 3 tiếng lãng phí khi chưa tới giờ chạy.
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Chiến dịch săn rò khí nén cuối tuần bằng thẻ [Red Tag](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-red-tag)/Fuguai (hoặc súng siêu âm): xử lý 25/27 điểm rò trong 10 ngày → Tiết kiệm ngay ~20 triệu/tháng (chi phí gần 0 đồng!).
2. Lập dự án [ROI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-roi) lắp biến tần [VFD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-vfd) có cảm biến áp suất/nhiệt độ phản hồi PID cho bơm giải nhiệt & quạt tháp (định luật P ∝ N³: giảm 20% tốc độ tiết kiệm gần 50% điện! Vốn 85 triệu, tiết kiệm 11 triệu/tháng → [Payback](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-payback) 7.7 tháng!).
3. Chuẩn hóa đồng hồ hẹn giờ tự động bật gia nhiệt máy đùn đúng 60 phút trước ca.
→ Kéo [SEC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sec) giảm ngay -11% bền vững!
6. **🔒 Khóa chuẩn chống tái diễn:** Gắn công tơ phụ theo dõi [SEC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sec) (kWh/tấn) theo từng phân xưởng lên Dashboard [Power BI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-power-bi) chuẩn [ISO 50001](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iso-50001).

**🔑 Từ khóa tra cứu nhanh:** [SEC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sec) · [ISO 50001](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iso-50001) · [VFD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-vfd) · [Regression](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-regression) · [Red Tag](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-red-tag) · [ROI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-roi) · [Payback](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-payback) · [Power BI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-power-bi)

---

<a id="tinh-huong-sc34"></a>
### SC34: Suýt xảy ra tai nạn nghiêm trọng (Near-miss) khi 2 thợ làm SMED nhanh quên khóa LOTO
> 📍 **Trạm xảy ra:** [Trạm 04 (S04)](#tram-s04) | 📖 **Cẩm nang:** `planning_quality_ehs_cost` | 🎓 **Bài học:** [L1.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l1-4)

1. **🚨 Dấu hiệu hiện trường:** Trong lúc thử nghiệm đổi khuôn nhanh [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) 2 người song song trên máy đùn/máy bện, người phía trước tưởng người phía sau đã xong nên bấm nút nhắp thử trục vít khi tay người kia vẫn gần đầu khuôn!
2. **💥 Tác động dòng chảy & chi phí:** Cảnh báo đỏ an toàn sinh mạng ([EHS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ehs) / [ISO 45001](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iso-45001)) — chỉ 1 tai nạn lao động sẽ làm dừng toàn bộ dự án cải tiến OE và gây hậu quả không thể khắc phục.
3. **⏱️ Khoanh vùng ngay trong 24h:** DỪNG NGAY thử nghiệm SMED, lập biên bản Near-miss minh bạch (không trù dập mà để sửa hệ thống!), tổ chức đánh giá rủi ro lại toàn bộ các bước thao tác cùng cán bộ EHS và Quản đốc.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Khi thiết kế quy trình [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) Pit-stop 2 người đã quá tập trung rút ngắn giây mà bỏ sót bước bắt buộc khóa-thẻ năng lượng [LOTO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loto) 6 bước và thiết bị kẹp nhiều ổ khóa (Group Lockout Hasp)!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Tích hợp CỨNG nguyên tắc bất di bất dịch '1 Người – 1 Ổ Khóa – 1 Chìa Khóa' vào bước số 1 của mọi bản [SOP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sop) SMED & bảo trì: trang bị kẹp Hasp treo ngay cửa tủ điện máy — cả 2 thợ CÙNG móc ổ khóa cá nhân của mình, bấm thử nút Start kiểm chứng Zero Energy trước khi chạm tay vào khuôn!
2. Thiết kế chốt định vị an toàn & tay cầm cách nhiệt chống bỏng cho đầu khuôn sấy nóng 160°C.
3. Đào tạo lại 100% quy trình [LOTO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loto) 6 bước (mất thêm chỉ 40 giây nhưng đảm bảo an toàn 100% tính mạng!).
6. **🔒 Khóa chuẩn chống tái diễn:** Đưa kiểm tra tuân thủ [LOTO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loto) thành mục ưu tiên số 1 (Zero Tolerance — vi phạm dừng việc ngay!) trong mọi lượt kiểm tra [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa) của Tổ trưởng, Quản đốc và Giám đốc.

**🔑 Từ khóa tra cứu nhanh:** [LOTO](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loto) · [EHS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-ehs) · [ISO 45001](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iso-45001) · [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) · [SOP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sop) · [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa)

---

<a id="tinh-huong-sc35"></a>
### SC35: Công nhân tự ý dán băng keo khóa chết cảm biến đứt sợi Jidoka cho 'đỡ bị dừng máy'
> 📍 **Trạm xảy ra:** [Trạm 03 (S03)](#tram-s03) | 📖 **Cẩm nang:** `lean_muda` | 🎓 **Bài học:** [L3.1](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l3-1)

1. **🚨 Dấu hiệu hiện trường:** Đi [Genba](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-genba) ca đêm phát hiện trên 2 máy bện [Buncher](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-buncher) và 1 máy quấn băng [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr), công nhân lấy băng keo quấn khóa chết công tắc cảm biến đứt sợi để máy cứ chạy tiếp không tự dừng!
2. **💥 Tác động dòng chảy & chi phí:** Phá hủy hoàn toàn cơ chế [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka), tạo ra hàng km cáp thiếu sợi đồng (rớt điện trở) hoặc thiếu lớp băng chống cháy [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr) cực kỳ nguy hiểm lọt ra công trình!
3. **⏱️ Khoanh vùng ngay trong 24h:** Tháo bỏ ngay băng keo, cách ly kiểm tra lại toàn bộ các rulo đã sản xuất trên 3 máy đó trong ca; nói chuyện trực tiếp lắng nghe lý do thật sự tại sao công nhân lại phải dán cảm biến!
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Hỏi thẳng dưới xưởng mới lộ ra nguyên nhân gốc đáng giật mình: Cảm biến bị hỏng lỏng dây hay BÁO GIẢ (False Trigger) dừng máy vô cớ 10 lần/ca làm công nhân không đạt định mức sản lượng bị trừ lương, báo bảo trì 2 tuần chưa sửa nên họ đành dán băng keo cho chạy!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Không đổ lỗi phạt công nhân đơn thuần — OE phối hợp Cơ Điện sửa dứt điểm ngay lập tức lỗi báo giả cảm biến (thay cảm biến quang/tiệm cận ổn định, đi lại dây chống nhiễu).
2. Chỉnh lại cơ chế báo sự cố: nếu máy báo giả > 2 lần, công nhân bật đèn [Andon](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-andon) kích hoạt [Escalation Matrix](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-escalation-matrix) để Cơ Điện xuống xử lý trong 15 phút.
3. Nâng cấp cảm biến kiểu không thể đấu tắt/dán băng keo (Fail-safe Wiring trên [PLC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-plc)) để bảo vệ tuyệt đối chất lượng cáp chống cháy [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr)!
6. **🔒 Khóa chuẩn chống tái diễn:** Thêm mục 'Kiểm thử kích hoạt cảm biến đứt sợi/băng tự dừng đầu ca' vào [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan) và [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa).

**🔑 Từ khóa tra cứu nhanh:** [Jidoka](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-jidoka) · [Mica FR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mica-fr) · [Buncher](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-buncher) · [Andon](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-andon) · [Escalation Matrix](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-escalation-matrix) · [PLC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-plc) · [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan) · [Genba](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-genba)

---

## 8. Con Người, Dữ Liệu MES & Văn Hóa Hiện Trường

<a id="tinh-huong-sc36"></a>
### SC36: Báo cáo OEE ghi tay sổ giấy luôn đẹp 82% nhưng thực tế xưởng giao hàng trễ liên tục
> 📍 **Trạm xảy ra:** [Trạm 00 (S00)](#tram-s00) | 📖 **Cẩm nang:** `erp_mes` | 🎓 **Bài học:** [L6.2](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l6-2)

1. **🚨 Dấu hiệu hiện trường:** Sổ ca hàng tháng báo cáo [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) Xưởng Đùn đạt 82% rất đẹp, nhưng sản lượng thực nhập kho chỉ đạt 66% công suất thiết kế và khách hàng kêu trễ hẹn liên tục!
2. **💥 Tác động dòng chảy & chi phí:** Ban Giám đốc bị 'mù số liệu', không nhìn thấy 40+ giờ dừng vặt và giảm tốc ẩn nên không thể đầu tư cải tiến đúng chỗ.
3. **⏱️ Khoanh vùng ngay trong 24h:** Đối chiếu chéo 3 nguồn độc lập trong 7 ngày: (1) Sổ tay tổ trưởng, (2) Tổng số mét thực tế nhập kho thành phẩm / tổng giờ ca, (3) Bấm giờ [Work Sampling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-work-sampling) thực tế tại máy đùn.
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Phơi bày 3 sai lệch kinh điển của báo cáo tay:
1. Quên ghi toàn bộ các lần dừng vặt < 5 phút (mất 35% Downtime thực!).
2. Dùng tốc độ định mức cũ lỗi thời (hoặc tự ý trừ hết thời gian đổi màu/chờ vật tư ra khỏi 'Thời gian kế hoạch' để làm đẹp Availability!).
3. Không tính đủ phế đầu ca và phế cắt sửa.
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Chuẩn hóa công thức [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) theo tốc độ chuẩn mét/phút & Bảng mã dừng máy gọn nhẹ (chỉ 12–15 mã chuẩn theo 6 Big Losses, cấm trừ đổi màu/chờ vật tư khỏi Planned Time!).
2. Xây file [Excel](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-excel) [Power Query](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-power-query) / [Python](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-python) đối chiếu tự động số mét nhập kho với giờ ca chạy để tự động phơi bày chênh lệch trước, rồi kết nối xung Encoder + cảm biến chạy máy thẳng vào [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes) & Dashboard [Power BI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-power-bi) real-time!
3. Truyền thông rõ: OE đo [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) thật (66%) để GIÚP xưởng gỡ nút thắt tăng lương sản phẩm, KHÔNG dùng để truy phạt thành tích cũ!
6. **🔒 Khóa chuẩn chống tái diễn:** Họp 10 phút đầu ngày nhìn đúng 1 nguồn sự thật duy nhất (Single Source of Truth) trên Dashboard [OEE Waterfall](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loss-tree) [Power BI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-power-bi).

**🔑 Từ khóa tra cứu nhanh:** [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee) · [Loss Tree](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-loss-tree) · [MES](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-mes) · [Power Query](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-power-query) · [Power BI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-power-bi) · [Python](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-python) · [Work Sampling](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-work-sampling) · [Downtime](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-downtime)

---

<a id="tinh-huong-sc37"></a>
### SC37: Quản đốc và Tổ trưởng phản kháng không hợp tác dự án SMED ('đang bận chạy hàng, đừng bày vẽ!')
> 📍 **Trạm xảy ra:** [Trạm 04 (S04)](#tram-s04) | 📖 **Cẩm nang:** `planning_quality_ehs_cost` | 🎓 **Bài học:** [L7.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l7-3)

1. **🚨 Dấu hiệu hiện trường:** Khi OE đề xuất quay video bấm giờ làm [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) trên máy đùn cổ chai, Quản đốc và Tổ trưởng tỏ thái độ lạnh nhạt, nói 'xưởng đang chạy sấp mặt không có thời gian họp hành vẽ vời giấy tờ!'
2. **💥 Tác động dòng chảy & chi phí:** Mọi sáng kiến OE sẽ chết yểu nếu không có sự đồng hành của người trực tiếp vận hành dưới xưởng.
3. **⏱️ Khoanh vùng ngay trong 24h:** Lùi 1 bước, KHÔNG mang lý thuyết sách vở ra tranh luận hay báo cáo méc Giám đốc — xuống đứng cùng ca với anh em, hỏi thẳng: 'Ở máy này hiện tại việc gì đang làm anh em mệt nhất, mất công nhất hoặc hay bị mắng nhất?'
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Áp dụng mô hình quản trị thay đổi [ADKAR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-adkar): Xưởng phản kháng vì 2 nỗi sợ thực tế — (1) Sợ OE xuống 'soi lỗi' để cắt thưởng/cắt người, (2) Chưa thấy lợi ích trực tiếp cho bản thân (thiếu Desire — chữ D trong ADKAR!).
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Làm ngay 1–2 dự án **Quick-Win giải tỏa nỗi đau của chính công nhân** trước (vd: hàn máng hứng nhựa nóng đỡ cúi đau lưng & bỏng tay, sắm bộ cờ-lê/xe đồ nghề [5S](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5s) gọn nhẹ, hỗ trợ làm báo cáo tự động cắt 25 phút viết sổ tay cuối ca cho Tổ trưởng!).
2. Mời chính Tổ trưởng & thợ giỏi đồng thiết kế giải pháp [Kaizen](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kaizen) và ghi tên họ lên bảng vinh danh + thưởng nóng khi báo cáo Ban Giám đốc!
3. Sau khi có niềm tin từ Quick-Win, mời họ cùng làm Pilot [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) 1 máy và chia sẻ lợi ích: máy chạy nhanh hơn, ít phế hơn → tăng thưởng năng suất thực cho cả tổ!
6. **🔒 Khóa chuẩn chống tái diễn:** Duy trì lịch đi [Genba](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-genba) lắng nghe hàng ngày và hệ thống thưởng nóng sáng kiến [Kaizen](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kaizen) minh bạch trong 7 ngày.

**🔑 Từ khóa tra cứu nhanh:** [ADKAR](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-adkar) · [Genba](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-genba) · [Kaizen](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-kaizen) · [SMED](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-smed) · [5S](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5s) · [A3](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-a3)

---

<a id="tinh-huong-sc38"></a>
### SC38: Dự án SMED / 5S thành công rực rỡ tháng đầu rồi 2 tháng sau trượt về thói quen cũ
> 📍 **Trạm xảy ra:** [Trạm 04 (S04)](#tram-s04) | 📖 **Cẩm nang:** `oe_field_execution_case_test` | 🎓 **Bài học:** [L3.4](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l3-4)

1. **🚨 Dấu hiệu hiện trường:** Trong tháng Pilot có OE đứng sát bên, thời gian đổi mã máy đùn giảm đẹp từ 55p → 14p và khu máy sạch bóng [5S](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-5s). Hai tháng sau khi OE chuyển sang dự án khác, đổi mã lại phình lên 38 phút và xe đồ nghề mất nửa cờ-lê!
2. **💥 Tác động dòng chảy & chi phí:** Hiệu ứng 'sớm nở tối tàn' (Entropy cải tiến) làm lãng phí công sức và mất uy tín của phòng OE trước Ban Giám đốc.
3. **⏱️ Khoanh vùng ngay trong 24h:** Đi kiểm tra hiện trường xem chính xác bước nào trong quy trình [Standard Work](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-work) đang bị bỏ qua (vd: không bật tủ sấy sẵn khuôn trước khi dừng máy, không trả đồ nghề về Shadow Board cuối ca).
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Hoàn thành tốt pha Improve nhưng làm quá yếu pha Control trong [DMAIC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dmaic): Thành quả chỉ dựa vào 'cá nhân OE đi nhắc' thay vì xây dựng hệ thống duy trì kỷ luật quản trị ([LSW](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lsw) + [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa) + [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan))!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Biến thành quả cải tiến thành thói quen quản lý bằng **Bộ 3 Khóa Chuẩn**:
   • [LSW](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lsw) (Leader Standard Work): Thêm 2 dòng kiểm tra 3 phút đầu ca của Tổ trưởng ('Tủ sấy Tip/Die cho lệnh kế đã bật chưa?', 'Xe đồ nghề Shadow Board đủ món chưa?').
   • [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa) (Layered Process Audit): Tổ trưởng kiểm hàng ngày, Quản đốc/OE kiểm hàng tuần, Giám đốc kiểm ngẫu nhiên 2 tuần/lần (10 câu Có/Không).
   • [Visual Management](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-visual-management): Treo biểu đồ theo dõi thời gian đổi mã từng ca ngay tại máy (đạt ≤ 15p tô Xanh, vượt > 20p tô Đỏ ghi rõ lý do!).
2. Phối hợp cài quy trình kiểm soát tài liệu [ISO 9001](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iso-9001) và đào tạo chuẩn cho công nhân mới thay ca.
6. **🔒 Khóa chuẩn chống tái diễn:** Bắt buộc ký bàn giao đầy đủ gói Control (`SOP` + `OPL` + `LSW` + `LPA`) trước khi chính thức đóng bất kỳ dự án OE nào!

**🔑 Từ khóa tra cứu nhanh:** [LSW](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lsw) · [LPA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-lpa) · [Control Plan](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-control-plan) · [DMAIC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-dmaic) · [Standard Work](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-work) · [Visual Management](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-visual-management) · [ISO 9001](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iso-9001) · [SOP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sop)

---

<a id="tinh-huong-sc39"></a>
### SC39: Công nhân Ca 1 và Ca 2 chỉnh nhiệt độ/tốc độ khác nhau tạo Histogram 2 đỉnh (Bimodal)
> 📍 **Trạm xảy ra:** [Trạm 04 (S04)](#tram-s04) | 📖 **Cẩm nang:** `minitab_spc` | 🎓 **Bài học:** [L4.3](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l4-3)

1. **🚨 Dấu hiệu hiện trường:** Vẽ biểu đồ [Histogram](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-histogram) đường kính dây VC 2.5mm² trên [Minitab](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-minitab) thấy hình 2 đỉnh tách biệt rõ rệt (đỉnh 1 tại 3.35mm, đỉnh 2 tại 3.44mm!) dù chạy cùng 1 máy đùn và cùng 1 lô hạt nhựa!
2. **💥 Tác động dòng chảy & chi phí:** Độ biến thiên tổng thể σ bị phình to gấp đôi làm [Cpk](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cpk) rớt xuống < 0.85, gây vừa thừa nhựa ở Ca 2 vừa sát cận mỏng ở Ca 1.
3. **⏱️ Khoanh vùng ngay trong 24h:** Phân tầng dữ liệu (Stratification trong [7 QC Tools](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-7-qc-tools)) tách theo Ca 1 / Ca 2 / Ca 3 và theo từng công nhân vận hành, chạy kiểm định [ANOVA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-anova) trên [Minitab](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-minitab) xác nhận khác biệt có ý nghĩa thống kê ([p-value](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-p-value) < 0.05).
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** Kiểm tra màn hình [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi) hai ca phát hiện: Tổ trưởng Ca 1 chỉnh theo chuẩn mới tiết kiệm nhựa (target 3.36mm), còn Tổ trưởng Ca 2 theo kinh nghiệm cũ sợ rớt [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester) nên vào đầu ca tự vặn tăng nhiệt độ & giảm tốc kéo lên 3.44mm (không phân quyền khóa Recipe trên HMI!).
5. **🛠️ Giải pháp OE & Số liệu tác động:**
1. Chạy thử nghiệm đối chứng trên dữ liệu thực tế cho cả 3 ca cùng thấy ở target 3.36mm tỷ lệ lỗi [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester) vẫn = 0%.
2. Thiết lập **Thư viện công thức chạy máy chuẩn (Recipe Library)** trên [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi)/[PLC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-plc) và phân quyền mật khẩu: công nhân chỉ chọn đúng mã hàng để máy tự nạp thông số chuẩn, chỉ Kỹ thuật/Quản đốc mới được phép điều chỉnh vượt biên ±3°C!
3. Đồng bộ đào tạo lại cả 3 ca theo cùng 1 bản [SOP](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-sop) và theo dõi [SPC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spc) chung theo ca.
→ [Histogram](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-histogram) gom về 1 đỉnh chuẩn duy nhất, [Cpk](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cpk) nhảy vọt từ 0.85 lên 1.58!
6. **🔒 Khóa chuẩn chống tái diễn:** Gắn báo cáo so sánh chỉ số [Cpk](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cpk) & tốc độ chạy giữa 3 ca trên [Power BI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-power-bi) để xóa lệch chuẩn giữa các kíp trực.

**🔑 Từ khóa tra cứu nhanh:** [Histogram](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-histogram) · [Minitab](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-minitab) · [ANOVA](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-anova) · [p-value](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-p-value) · [7 QC Tools](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-7-qc-tools) · [HMI](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-hmi) · [Cpk](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-cpk) · [SPC](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spc)

---

<a id="tinh-huong-sc40"></a>
### SC40: Phòng Mua hàng đề xuất đổi sang nhà cung cấp hạt nhựa / đồng Rod rẻ hơn 3% ngay lập tức
> 📍 **Trạm xảy ra:** [Trạm 01 (S01)](#tram-s01) | 📖 **Cẩm nang:** `oe_field_execution_case_test` | 🎓 **Bài học:** [L4.5](GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md#bai-l4-5)

1. **🚨 Dấu hiệu hiện trường:** Để đạt KPI tiết kiệm chi phí mua hàng quý này, Phòng Mua hàng tìm được nhà cung cấp hạt nhựa PVC (hoặc đồng Rod) giá rẻ hơn 3% và muốn đưa thẳng 30 tấn xuống xưởng chạy đại trà ngay tuần tới!
2. **💥 Tác động dòng chảy & chi phí:** Rủi ro cực lớn: nếu lô nhựa bị bay hơi hóa dẻo rớt lão hóa [Aging Oven](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-aging-oven) 7 ngày, tăng tỷ trọng [CaCO3 Filler](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-caco3-filler), hoặc đồng Rod độ dẫn [IACS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iacs) thấp / dày oxit làm hỏng khuôn [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd), nhà máy có thể lỗ gấp 10 lần khoản tiền 'tiết kiệm mua hàng'!
3. **⏱️ Khoanh vùng ngay trong 24h:** OE lập tức kích hoạt cổng kiểm soát thay đổi [MOC / ECN](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-moc-ecn) — đề nghị tạm giữ nhập đại trà và chỉ nhập đúng 1 lô thử nghiệm nhỏ (Pilot Lot 500 kg nhựa hoặc 1 cuộn đồng Rod 3 tấn) để thẩm định toàn diện trước!
4. **🔍 Truy tìm Nguyên nhân gốc (RCA):** KPI mua hàng chỉ đo đơn giá đầu vào (Purchase Price Variance) mà tách rời khỏi tổng chi phí vận hành dưới xưởng (Tỷ trọng VNĐ/lít, % [IACS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iacs), tỷ lệ đứt sợi/tấn, tốc độ đùn, tỷ lệ phế & tuổi thọ khuôn [PCD](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-pcd))!
5. **🛠️ Giải pháp OE & Số liệu tác động:**
Triển khai quy trình [MOC / ECN](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-moc-ecn) 5 bước chuẩn mực liên phòng ban (Mua hàng – Kỹ thuật – QA Lab – OE – Kế toán):
1. **Thẩm định Lab đầy đủ:** Kiểm % [IACS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iacs), Reverse Twist [ASTM B49](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-astm-b49) (với đồng); đo tỷ trọng Specific Gravity, [Tensile](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-tensile) & **BẮT BUỘC chờ đủ 7 ngày tủ lão hóa [Aging Oven](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-aging-oven)** (với nhựa)!
2. **Chạy thử lô Pilot trên xưởng:** Đo đủ [OEE](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-oee), tốc độ tối đa, [Melt Pressure](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-melt-pressure), đứt sợi/tấn, lỗi [Spark Tester](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-spark-tester) và kiểm định [2-Sample t-test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-2-sample-t-test) so với nhà cung cấp hiện tại.
3. **Tính Tổng Chi Phí Sở Hữu (TCO / [Standard Cost](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-cost)):** Chỉ ký duyệt ECN cho nhập đại trà khi TCO thực sự rẻ hơn VÀ đạt 100% chuẩn [QCVN 4](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-qcvn-4) / [IEC 60502](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iec-60502)!
6. **🔒 Khóa chuẩn chống tái diễn:** Ban hành quy định [ISO 9001](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iso-9001): Kho NVL từ chối nhập đại trà bất kỳ mã nhà cung cấp mới nào chưa có chữ ký duyệt [MOC / ECN](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-moc-ecn) hoàn chỉnh (đủ kết quả [Aging Oven](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-aging-oven) 7 ngày).

**🔑 Từ khóa tra cứu nhanh:** [MOC / ECN](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-moc-ecn) · [Aging Oven](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-aging-oven) · [IACS](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-iacs) · [ASTM B49](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-astm-b49) · [CaCO3 Filler](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-caco3-filler) · [2-Sample t-test](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-2-sample-t-test) · [Standard Cost](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-standard-cost) · [QCVN 4](CamNang_ToanDien_OE_CADIVI_MienTrung.md#term-qcvn-4)

---
