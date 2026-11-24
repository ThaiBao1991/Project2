# -*- coding: utf-8 -*-
"""
cadivi_factory_flows.py — Bản Đồ Lưu Trình Dòng Chảy Vận Hành Nhà Máy CADIVI Miền Trung
& Kho Hành Động + 40 Tình Huống Thực Chiến Từ Đầu Đến Cuối Dành Cho Chuyên Viên OE.

Cấu trúc 3 trụ cột thực chiến (khác hoàn toàn với lý thuyết & giáo trình học):
  1. FACTORY_MASTER_MAP + STATIONS (10 Trạm S00 → S09): Dòng chảy khép kín từ Đơn hàng & Hoạch định →
     IQC → Kéo/Ủ → Bện → Đùn cách điện/Lưu hóa → Ghép lõi/Giáp → Đùn vỏ/In/Spark → Lab QA/QC →
     Đánh cuộn/Cut-Length/Giao hàng → Dòng chảy ngược (Thu hồi phế, Bảo trì Cơ Điện, Quyết toán giá thành).
  2. PRODUCT_FLOWS (6 Luồng F01 → F06): Đường đi công nghệ & chiến lược OE riêng cho 6 họ sản phẩm chủ lực CADIVI.
  3. SCENARIOS (40 Tình huống SC01 → SC40 chia thành 8 nhóm): Kịch bản thực tế dưới xưởng + 6 bước xử lý chuẩn OE.

100% Unicode thuần, KHÔNG dấu '$', dùng công thức [[TermKey|DisplayText]] cho Click-Anywhere Glossary.
"""

FACTORY_MASTER_MAP = """┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
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
   • Quyết toán SAP PP: Đối chiếu BOM Variance + Standard Cost + Báo cáo OEE/OLE/ROI về Ban Giám đốc"""


STATIONS = [
    {
        "id": "S00",
        "code": "Trạm 00",
        "title": "Dòng Thông Tin & Hoạch Định Sản Xuất (S&OP → MPS → MRP → RCCP → CRP → MES)",
        "zone": "Phòng Kế Hoạch – Kinh Doanh – Mua Hàng – Ban Giám Đốc",
        "input": "Đơn hàng đại lý/dự án EVN, dự báo bán hàng 3–12 tháng, dữ liệu tồn kho [[ERP]], cây [[BOM]] & tốc độ máy (Routing).",
        "output": "Kế hoạch [[MPS]] tuần, lệnh mua đồng/nhựa [[MRP]], lịch tải từng máy [[CRP]] theo vòng màu [[Color Sequencing]] và Lệnh SX (Production Order) phát xuống phân xưởng.",
        "machines_and_teams": "Hệ thống [[ERP]] / [[SAP PP]], phần mềm lập lịch Excel/[[MES]]; phối hợp Kinh doanh – Kế hoạch – Mua hàng – Quản đốc 4 xưởng – OE.",
        "hidden_losses": (
            "• Lập lịch [[MRP]] mù tải (không kiểm [[RCCP]] nhân [[OEE]] thực) khiến xưởng Đùn bị giao tải 125% rồi trễ hàng dây chuyền.\n"
            "• Tồn kho ảo trên [[ERP]] lệch thực tế kho 5–8% gây dừng máy chờ hạt nhựa hoặc mua dư tồn đọng vốn hàng tỷ đồng.\n"
            "• Xếp lịch theo thứ tự đơn hàng chốt ngẫu nhiên (Đen → Trắng → Đen → Vàng) làm bùng nổ thời gian đổi mã [[SMED]] & nhựa xả [[Purging]].\n"
            "• Master Data (tốc độ chuẩn Routing, hệ số [[Lay-up Factor]], tỷ lệ phế chuẩn) cũ kỹ 2–3 năm không cập nhật làm méo toàn bộ giá thành."
        ),
        "oe_end_to_end_actions": (
            "1. **Kiểm toán Master Data (Đầu nguồn):** Đối chiếu tốc độ chuẩn Routing trên [[SAP PP]] với tốc độ thực đo tại máy kéo/bện/đùn; rà soát hệ số [[Lay-up Factor]] và tỷ lệ phế chuẩn trong cây [[BOM]].\n"
            "2. **Thiết kế mô hình kiểm tải [[RCCP]] & [[CRP]]:** Xây công cụ Excel/[[Power BI]] tự động nhân giờ kế hoạch với [[OEE]] thực từng máy cổ chai để báo sớm thiếu/dư tải trước 2–4 tuần.\n"
            "3. **Áp luật [[Campaign Scheduling]] & [[Color Sequencing]]:** Thống nhất với Kế hoạch & Kinh doanh vòng màu cố định (Trắng → Vàng → Xanh/Đỏ → Đen) và cơ chế chốt lịch đóng băng (Frozen Horizon 48–72 giờ) chống chen đơn phá chuyền.\n"
            "4. **Thiết lập tồn kho khoa học:** Phân nhóm 9 ô [[ABC-XYZ]], tính [[Safety Stock]] & điểm đặt hàng lại [[ROP]] bằng công thức thống kê, thay đổi từ cảm tính sang kéo [[Pull System]] cho dây dân dụng nhóm AX.\n"
            "5. **Gắn điểm chốt (Pacemaker):** Xác định rõ máy cổ chai [[Bottleneck]] (thường là Xưởng Đùn) làm điểm phát nhịp [[Drum-Buffer-Rope]] kéo ngược về Kéo & Bện."
        ),
        "kpis": "Schedule Adherence (Tuân thủ lịch SX) ≥ 90% | Độ chính xác tồn kho RIA ≥ 98.5% | Giao hàng đúng hẹn OTIF ≥ 96% | Tỷ lệ đổi ngược màu Tối→Sáng < 1 lần/tuần.",
        "key_terms": ["S&OP", "MPS", "MRP", "RCCP", "CRP", "SAP PP", "Campaign Scheduling", "Color Sequencing", "Safety Stock", "ROP", "ABC-XYZ"],
        "doc_key": "planning_quality_ehs_cost",
        "lesson_id": "L5.1"
    },
    {
        "id": "S01",
        "code": "Trạm 01",
        "title": "Tiếp Nhận Nguyên Vật Liệu, Kiểm Đầu Vào (IQC) & Quản Trị Kho NVL",
        "zone": "Kho Nguyên Vật Liệu – Phòng QA (IQC) – Phòng Mua Hàng",
        "input": "Cuộn đồng thanh Ø8.0mm (3–4 tấn/cuộn, chuẩn [[ASTM B49]]), nhôm thanh Ø9.5mm, bao hạt nhựa [[PVC]]/[[XLPE]]/[[LSZH]]/[[Masterbatch]], cuộn băng thép [[DSTA]], băng [[Mica FR]], [[Water-Blocking]].",
        "output": "NVL đã dán tem QR/Barcode đạt chuẩn IQC, phân khu sạch sẽ theo [[FIFO]], sẵn sàng cấp đúng mẻ ([[Kitting]]) ra đầu vào các phân xưởng.",
        "machines_and_teams": "Cầu trục/xe nâng hạng nặng, cầu đo [[Kelvin Bridge]] kiểm % [[IACS]], cân tỷ trọng Specific Gravity, máy thử độ ẩm hạt nhựa, tủ thử [[Tensile]]; đội Kho NVL – QA IQC – Mua hàng – OE.",
        "hidden_losses": (
            "• Mua đồng Rod giá rẻ hơn 1 triệu/tấn nhưng % [[IACS]] chỉ 99.6% (thay vì 101.4%) → Xưởng phải kéo sợi to hơn tốn thêm 4.5 triệu/tấn đồng!\n"
            "• Hạt nhựa [[PVC]] bị độn quá nhiều bột đá [[CaCO3 Filler]] làm tỷ trọng tăng từ 1.40 lên 1.52 g/cm³ → Dù đùn đúng chiều dày mm vẫn bị âm [[BOM]] +8.5% kg nhựa!\n"
            "• Bao hạt [[XLPE]] [[Silane]] hoặc băng [[Water-Blocking]] bị rách/xé miệng ngoài không khí ẩm Đà Nẵng → Khâu mạch sớm trong phễu làm sần vỏ & bít lưới lọc.\n"
            "• Không kiểm soát [[FIFO]] và [[Cycle Counting]] → Hạt nhựa quá hạn, cuộn đồng Rod bị cấn móp va chạm xe nâng gây đứt sợi hàng loạt ở Trạm 02."
        ),
        "oe_end_to_end_actions": (
            "1. **Đánh giá TCO (Tổng chi phí sở hữu) cho Mua hàng:** Lập bảng so sánh đơn giá thực theo % [[IACS]] (đối với đồng Rod) và theo **VNĐ/lít thể tích** (Đơn giá/kg × Tỷ trọng đối với hạt [[PVC]]/[[XLPE]]).\n"
            "2. **Chuẩn hóa cổng chặn IQC + [[MOC / ECN]]:** Mọi nhà cung cấp NVL mới bắt buộc qua thử nghiệm mẫu Pilot (đo IACS, Reverse Twist [[ASTM B49]], tỷ trọng, [[Tensile]] & 7 ngày [[Aging Oven]]) trước khi nhập đại trà.\n"
            "3. **Thiết kế [[5S]] & [[FIFO]] kho NVL:** Phân làn riêng tuyệt đối khu Đồng vs khu Nhôm (chống bụi đồng ăn mòn nhôm!), khu nhựa chống ẩm đóng kín hút chân không cho bao [[XLPE]]/[[LSZH]] dùng dở.\n"
            "4. **Triển khai [[Cycle Counting]] & [[Two-Bin Kanban]]:** Kiểm đếm luân phiên nhóm A hàng tuần giữ RIA ≥ 98.5%; áp [[Two-Bin Kanban]] + xe [[Milk Run]] cấp phát vật tư nhóm C (tem, màng co, [[Masterbatch]], găng tay)."
        ),
        "kpis": "Tỷ lệ lô NVL lỗi lọt xuống xưởng = 0% | Độ dẫn đồng Rod ≥ 100.8% [[IACS]] | Sai lệch tỷ trọng nhựa ≤ ±0.02 g/cm³ | Độ chính xác tồn kho RIA ≥ 98.5%.",
        "key_terms": ["ASTM B49", "IACS", "CaCO3 Filler", "FIFO", "Cycle Counting", "Two-Bin Kanban", "Kitting", "MOC / ECN", "Milk Run"],
        "doc_key": "bom_cost",
        "lesson_id": "L5.2"
    },
    {
        "id": "S02",
        "code": "Trạm 02",
        "title": "Xưởng Kéo Sợi (RBD / Multi-wire), Ủ Liên Tục, Phòng Khuôn PCD & Bể Nhũ Tương",
        "zone": "Phân Xưởng Kéo Sợi & Phòng Bảo Dưỡng Khuôn (Die Shop)",
        "input": "Cuộn đồng Rod Ø8.0mm (hoặc Nhôm Rod Ø9.5mm), bộ khuôn kim cương [[PCD]] đúng chuỗi giảm tiết diện, dung dịch nhũ tương [[Drawing Emulsion]].",
        "output": "Rulo sợi đồng/nhôm đạt chuẩn đường kính (±0.003–0.005mm), mềm dẻo (giãn dài ≥ 20–25% sau [[Annealing]]), bề mặt sáng bóng không oxy hóa, sẵn sàng cấp cho Xưởng Bện/Đùn.",
        "machines_and_teams": "Máy kéo thô [[RBD]] (tốc độ 20–32 m/s), máy kéo tinh đa sợi [[Multi-wire]] (8–24 sợi), bộ ủ [[Annealing]] Inline / Lò chuông, máy hàn [[Butt Welder]], bộ xả/thu [[Pay-off]]/[[Take-up]]; Tổ Kéo – Phòng Khuôn – Cơ điện – OE.",
        "hidden_losses": (
            "• **[[Copper Give-away]]:** Khuôn [[PCD]] định cỡ cuối chạy quá tuổi thọ mòn thêm +0.008 mm → Đốt không +2.4% khối lượng đồng nguyên chất (hàng tỷ đồng/năm!).\n"
            "• **Đứt sợi dừng máy (Wire Breaks):** Mỗi lần đứt trên máy [[RBD]] mất 15–20 phút xâu lại 11 khuôn; trên [[Multi-wire]] 16 sợi chỉ 1 sợi đứt là cả 16 sợi phải dừng!\n"
            "• **Lỗi ủ [[Annealing]]:** Đường cong điện áp ủ đáp ứng chậm lúc tăng/giảm tốc gây 40m dây cứng đầu/cuối rulo; hơi bảo vệ kém làm dây bị đen oxy hóa sau 24h.\n"
            "• **Bể nhũ tương [[Drawing Emulsion]] suy thoái:** Tụt nồng độ dầu, nhiễm khuẩn tụt pH < 7.8, châm nước cứng gây đóng cặn bít khuôn & tăng điện năng [[SEC]] kWh/tấn.\n"
            "• **Cuốn rulo [[Take-up]] lỗi rải dây:** Xếp chéo lớp (Cross-over) gây kẹt đứt sợi dây chuyền sang Trạm 03!"
        ),
        "oe_end_to_end_actions": (
            "1. **Triển khai pháp y đứt sợi [[Wire Break Forensics]]:** Đặt bảng mẫu nhận diện 6 hình thái đầu gãy ([[Cup-and-Cone]], hàn [[Butt Welder]], cháy hồ quang tang ủ, xước khuôn [[PCD]]) + giữ 100% mẫu đứt chạy [[Pareto]] 80/20 hàng tuần.\n"
            "2. **Quản trị vòng đời khuôn [[PCD]] & xóa [[Copper Give-away]]:** Lập hồ sơ từng mã khuôn (tấn kéo tối đa trước khi mang đi Re-polish), thay đồng bộ bộ Matched Die Set trên [[Multi-wire]] (dung sai ≤ 0.002mm), kéo tâm đường kính về sát chuẩn [[IEC 60228]] với [[Cpk]] ≥ 1.33.\n"
            "3. **Tối ưu [[OEE]] & [[OLE]] máy kéo:** Áp [[SMED]] thay cassette khuôn dự phòng đã lắp sẵn bên ngoài (40p → 11p), chuẩn hóa [[SOP]] hàn [[Butt Welder]] + test bẻ 90° đầu ca, vẽ [[Man-Machine Chart]] cho 1 thợ đứng 2–3 máy kéo tinh.\n"
            "4. **Khóa chuẩn [[Jishu Hozen]] bể nhũ tương & điện năng:** Đưa kiểm tra nồng độ khúc xạ kế + pH + độ dẫn nước DI vào Checklist đầu ca; đo [[SEC]] (kWh/tấn) từng máy để phát hiện trượt puly/khuôn mòn sớm."
        ),
        "kpis": "[[OEE]] máy RBD ≥ 78% | Tỷ lệ đứt sợi < 0.3 lần/tấn (RBD) & < 0.8 lần/tấn (Multi-wire) | [[Copper Give-away]] ≤ +0.4% | Điện năng [[SEC]] ổn định theo Baseline [[ISO 50001]].",
        "key_terms": ["RBD", "Multi-wire", "Annealing", "PCD", "Drawing Emulsion", "Butt Welder", "Wire Break Forensics", "Cup-and-Cone", "Copper Give-away", "IEC 60228"],
        "doc_key": "cable_extrusion_wire_forensics",
        "lesson_id": "L1.2"
    },
    {
        "id": "S03",
        "code": "Trạm 03",
        "title": "Xưởng Bện Ruột Dẫn (Buncher Dây Mềm / Rigid Strander Cáp Lực / ACSR)",
        "zone": "Phân Xưởng Bện Ruột Dẫn",
        "input": "Các rulo sợi đồng mềm/cứng hoặc sợi nhôm/thép từ Trạm 02 (đồng bộ chiều dài và đường kính), mỡ chống ăn mòn (với [[ACSR]]).",
        "output": "Rulo ruột dẫn đồng/nhôm đạt chuẩn cấu trúc cấp 2 (ép nén tròn hoặc rẻ quạt) hoặc cấp 5 (mềm dẻo), đúng bước xoắn [[Lay-up Factor]], đúng điện trở DC [[IEC 60228]].",
        "machines_and_teams": "Máy bện xoắn đôi tốc độ cao [[Buncher]], máy bện lồng cứng [[Rigid Strander]] (1+6+12+18+24 = 61 sợi) kèm bộ ép nén Compacting Roller, cần trục nạp rulo; Tổ Bện – Kho bán thành phẩm – OE.",
        "hidden_losses": (
            "• **Thay nạp rulo [[Rigid Strander]] cực lâu:** Thay thủ công 37–61 rulo vào lồng quay mất 60–90 phút, chiếm tới 25% thời gian ca!\n"
            "• **Chiều dài các rulo nạp không đồng đều:** Rulo ngắn nhất hết trước buộc dừng cả máy 61 sợi để nối dây hoặc bỏ phế hàng trăm mét đồng trên 36 rulo còn lại.\n"
            "• **Bước xoắn (Lay Length) chỉnh quá ngắn:** Làm tăng hệ số [[Lay-up Factor]] thêm +1.0–1.5%, âm thầm mất thêm 1.5% đồng cho cả đơn hàng mà không ai để ý!\n"
            "• **Lãng phí lao động ([[OLE]] thấp):** 1 thợ chỉ đứng canh 1–2 máy [[Buncher]] vì thiếu cảm biến tự dừng [[Jidoka]] và hay bị rối xả [[Pay-off]] (lỗi Birdcaging).\n"
            "• **Lẫn chiều dài rulo WIP:** Ùn tắc hàng chục rulo ruột đồng chờ giữa Xưởng Bện và Xưởng Đùn làm chật lối đi và dễ oxy hóa."
        ),
        "oe_end_to_end_actions": (
            "1. **Triển khai [[SMED]] nạp lồng [[Rigid Strander]]:** Soạn sẵn đồng bộ 100% rulo bằng chiều dài (Equal-length Kitting) trên giá xe đẩy bên ngoài trước khi máy dừng + phối hợp 2 người kiểu Pit-stop rút thời gian nạp từ 72p xuống ~24p!\n"
            "2. **Vẽ [[Man-Machine Chart]] nâng vọt [[OLE]] khu [[Buncher]]:** Phối hợp Cơ Điện lắp đủ cảm biến đứt sợi + cảm biến rung + đèn [[Andon]] trên cao để 1 công nhân vận hành an toàn 4–6 máy [[Buncher]] (tăng [[OLE]] từ ~52% lên ≥ 78%).\n"
            "3. **Kiểm toán bước xoắn [[Lay-up Factor]] & độ nén Compact:** Đo kiểm tra bước xoắn thực tế so với bản vẽ [[IEC 60228]] (giữ sát cận dài cho phép để tiết kiệm đồng tối đa mà ruột vẫn chắc đẹp!); tối ưu đường kính ruột ép nén giúp giảm 8–10% nhựa bọc ở Trạm 04!\n"
            "4. **Giới hạn WIP bằng ô sàn [[Kanban]] / [[Pull System]]:** Sơn vạch ô sàn cố định (vd: tối đa 10 rulo VC 2.5 giữa Bện & Đùn) — đủ ô thì chuyển mã khác, xóa cảnh đẩy dồn cục."
        ),
        "kpis": "[[OEE]] Rigid Strander ≥ 72% | [[OLE]] khu Buncher ≥ 78% (1 người / 4–6 máy) | Thời gian nạp lồng < 25 phút | Phế đồng đuôi rulo bện < 0.4%.",
        "key_terms": ["Buncher", "Rigid Strander", "ACSR", "Lay-up Factor", "SMED", "Man-Machine Chart", "OLE", "Jidoka", "Kanban", "Pull System"],
        "doc_key": "ole",
        "lesson_id": "L2.3"
    },
    {
        "id": "S04",
        "code": "Trạm 04",
        "title": "Xưởng Đùn Cách Điện (PVC / XLPE / CCV), Quấn Băng Mica FR & Lưu Hóa Khâu Mạch",
        "zone": "Phân Xưởng Đùn Cách Điện – Phòng Xông Sauna – Khu Quấn Băng Mica – Dây Chuyền CCV",
        "input": "Rulo ruột dẫn từ Trạm 03, hạt nhựa cách điện [[PVC]] / [[XLPE]] ([[Silane]] + 5% Catalyst) / XLPE Peroxide siêu sạch, [[Masterbatch]] màu, băng [[Mica FR]].",
        "output": "Rulo lõi cách điện đồng tâm ≥ 92%, đủ chiều dày [[IEC 60502]], 0 lỗi [[Spark Tester]], đạt khâu mạch [[Hot Set Test]] (với XLPE/Solar).",
        "machines_and_teams": "Máy đùn [[Extruder]] ([[L/D Ratio]] 20:1–28:1), đầu chữ T [[Crosshead]], [[Hopper Dryer]], [[Laser Gauge]], [[Cooling Trough]], [[Spark Tester]], phòng xông hơi Sauna, dây chuyền [[CCV]] khí Nitơ, máy quấn băng [[Mica FR]]; Tổ Đùn – Kỹ thuật Công nghệ – OE.",
        "hidden_losses": (
            "• **Nút thắt công suất ([[Bottleneck]]) số 1 toàn nhà máy:** Mọi phút dừng máy đùn đều làm mất thẳng sản lượng xuất xưởng của cả CADIVI!\n"
            "• **Đổi màu / đổi tiết diện cực lâu (45–60 phút)** & xả 20–30 kg nhựa [[Purging]] + hàng chục mét dây đồng dính nhựa cực đắt (mất 30% giá trị đồng thu hồi!).\n"
            "• **[[Over-thickness]] nhựa cách điện (+8% đến +15%):** Do lệch tâm [[Crosshead]], dao động [[Melt Pressure]] (Surging) hoặc công nhân cài dư cho 'chắc ăn đỡ rớt t_min'.\n"
            "• **Khuyết tật đùn buộc hạ tốc độ:** Sần da cá mập [[Sharkskin]], tắc lưới [[Screen Pack]], cặn [[Die Drool]], nước làm mát nóng mùa hè Đà Nẵng.\n"
            "• **Ùn tắc WIP ở Phòng Xông Sauna [[Silane]]:** Chờ gom đủ 12 rulo mới bật lò và cài dư thời gian xông (10h thay vì 6h) kéo dài [[Lead Time]] thêm 2–3 ngày!"
        ),
        "oe_end_to_end_actions": (
            "1. **Tấn công số 1 bằng [[SMED]] + [[Color Sequencing]] + [[Purging]]:** Quay video tách Thao tác Ngoài (tủ sấy sẵn Chày–Cối bên ngoài, phễu sấy di động, xe đồ nghề [[5S]] Shadow Board), đầu [[Crosshead]] tự định tâm, nạp Recipe 1-chạm trên [[HMI]], lịch vòng màu Sáng → Tối → Rút đổi mã 55p → 12–15p (-75%)!\n"
            "2. **Dự án [[Six Sigma]] [[DMAIC]] xóa [[Over-thickness]]:** Ổn định [[Melt Pressure]] (thay [[Screen Pack]] chủ động, chỉnh nhiệt vùng cấp liệu), lắp vòng kín [[Laser Gauge]] → [[Capstan]], kéo σ chiều dày từ 0.06mm xuống ≤ 0.02mm rồi mới dịch tâm Target Shift xuống sát t_nom (giữ [[Cpk]] ≥ 1.50 theo [[IEC 60502]])!\n"
            "3. **Chạy liên tục không dừng trên dây dân dụng:** Lắp [[Pay-off]] đôi (Dual Pay-off) + [[Accumulator]] + [[Take-up]] đôi xóa sổ 100% dừng vặt đổi rulo.\n"
            "4. **Giải phóng nút thắt Sauna & tối ưu [[Mica FR]]:** Dùng [[DOE]] + [[Hot Set Test]] rút thời gian xông đúng theo chiều dày lớp nhựa; hiệu chuẩn góc quấn [[Mica FR]] về đúng chồng mép 40% (tránh quấn dư 60% tốn băng & tốn XLPE bọc ngoài!).\n"
            "5. **Phân tuyến đúng [[L/D Ratio]] & giữ [[CCV]] chạy dài ngày:** Khóa cứng máy L/D 20:1 chạy PVC, L/D 26:1 chạy XLPE; gom đơn trung thế chạy Campaign 5–7 ngày liên tục trên [[CCV]]."
        ),
        "kpis": "[[OEE]] máy đùn cổ chai ≥ 75% | Thời gian đổi màu < 15 phút | [[Over-thickness]] ≤ +2.5% | [[Cpk]] đường kính ≥ 1.33–1.67 | Phế đồng dính nhựa < 0.5%.",
        "key_terms": ["Extruder", "Crosshead", "SMED", "Over-thickness", "Laser Gauge", "Melt Pressure", "Sharkskin", "Silane", "CCV", "Mica FR", "L/D Ratio"],
        "doc_key": "smed",
        "lesson_id": "L3.3"
    },
    {
        "id": "S05",
        "code": "Trạm 05",
        "title": "Ghép Lõi (Drum Twister), Chống Thấm, Đan Lưới Chống Nhiễu & Bọc Giáp Thép (DSTA)",
        "zone": "Phân Xưởng Hoàn Thiện Cáp Lực & Cáp Đặc Chủng",
        "input": "3–4 rulo lõi cách điện (Đỏ–Vàng–Xanh–Đen) từ Trạm 04, sợi độn PP, băng/sợi [[Water-Blocking]], suốt sợi đồng/thiếc cho [[Braiding]], cuộn băng thép mạ kẽm [[DSTA]] hoặc băng nhôm DATA.",
        "output": "Bó lõi cáp tròn đều chắc chắn, đủ độ che phủ lưới chống nhiễu (≥ 85%), đủ độ phủ giáp thép/nhôm 100% không hở khe, sẵn sàng đùn lớp vỏ hoàn thiện Trạm 06.",
        "machines_and_teams": "Máy ghép lõi [[Drum Twister]] (hoặc Planetary Strander), dàn máy đan lưới [[Braiding]] (16–36 suốt), máy quấn giáp băng thép [[DSTA]]/DATA; Tổ Ghép Lõi – Tổ Giáp – OE.",
        "hidden_losses": (
            "• **Lệch chiều dài 4 rulo lõi vào [[Drum Twister]]:** Rulo 1 dài 1,050m, rulo 2 dài 1,020m, rulo 3 dài 990m, rulo 4 dài 1,075m → Cáp thành phẩm chỉ dài 990m, buộc cắt bỏ lãng phí **175m lõi đồng bọc XLPE cực đắt**!\n"
            "• **Quấn sai bước xoắn ghép lõi hoặc lệch hướng lõi rẻ quạt:** Gây tăng [[Lay-up Factor]] (tốn đồng + nhựa) hoặc cáp méo gồ ghề làm tốn nhựa vỏ ngoài ở Trạm 06.\n"
            "• **Máy quấn giáp [[DSTA]] dừng hàn băng liên tục:** Dùng cuộn băng thép dạng bánh nhỏ (400m) phải dừng hàn 4–5 lần trên 1 rulo cáp!\n"
            "• **Nút thắt [[Braiding]] cực chậm & đan thừa mật độ:** Chỉnh mật độ phủ 93% (chuẩn chỉ ≥ 85%) làm tốc độ máy chậm đi -22% và tốn thêm +14% đồng mạ thiếc [[Tinned Copper]]!"
        ),
        "oe_end_to_end_actions": (
            "1. **Khóa đồng bộ chiều dài 4 rulo từ Trạm 04:** Kết nối [[MES]] & hiệu chuẩn định kỳ bánh đo mét máy đùn để 4 rulo cùng lệnh lệch nhau ≤ ±5m → Triệt tiêu 85% phế lõi lẻ tại [[Drum Twister]]!\n"
            "2. **Chuyển đổi sang cuộn băng thép khổ lớn (Traverse Wound Coil 2,500m):** Cắt 80% số lần dừng hàn nối trên máy bọc giáp [[DSTA]], nâng [[OEE]] từ 58% lên ~74%.\n"
            "3. **Tối ưu [[Braiding]] (1 người 6–10 máy + đúng mật độ 87%):** Quấn đồng bộ chiều dài toàn bộ 24 suốt Bobbin bằng nhau (không để hết lẻ từng suốt!), gắn cảm biến đứt sợi [[Jidoka]] và chỉnh bánh răng bước đan về mục tiêu 87%.\n"
            "4. **Kiểm soát kho kín chống ẩm cho [[Water-Blocking]] & Poka-Yoke phân biệt DSTA vs DATA:** Dán mã cảnh báo cấm tuyệt đối quấn băng thép [[DSTA]] lên cáp 1 lõi xoay chiều (tránh dòng điện xoáy làm nóng chảy cáp!)."
        ),
        "kpis": "Độ lệch chiều dài 4 rulo lõi ≤ ±0.5% | [[OEE]] Drum Twister & DSTA ≥ 72% | [[OLE]] cụm máy Braiding ≥ 80% | Phế lõi thừa < 0.6%.",
        "key_terms": ["Drum Twister", "DSTA", "Braiding", "Water-Blocking", "Lay-up Factor", "Tinned Copper", "Jidoka", "MES"],
        "doc_key": "cable_mfg_machines",
        "lesson_id": "L1.3"
    },
    {
        "id": "S06",
        "code": "Trạm 06",
        "title": "Đùn Vỏ Ngoài Hoàn Thiện (Sheathing), Làm Mát, In Phun Chữ & Kiểm Soát Trực Tuyến",
        "zone": "Phân Xưởng Đùn Vỏ Hoàn Thiện (PVC / HDPE / LSZH)",
        "input": "Bó lõi đã ghép/bọc giáp từ Trạm 05, hạt nhựa vỏ [[PVC]] / [[LSZH]] / HDPE đã sấy kỹ qua [[Hopper Dryer]], bộ Chày–Cối kiểu Tubing đúng [[DDR]], mực máy in phun.",
        "output": "Rulo cáp thành phẩm hoàn chỉnh, bề mặt bóng mịn không [[Sharkskin]]/[[Die Drool]], chữ in sắc nét đúng quy chuẩn, đủ chiều dài mét chính xác, 0 lỗi [[Spark Tester]].",
        "machines_and_teams": "Máy đùn vỏ cỡ lớn (Ø120–Ø150mm), đầu [[Crosshead]] Tubing, [[Laser Gauge]], máng nước [[Cooling Trough]] + Chiller, bộ thổi khô Air Wipe, [[Spark Tester]], máy in phun công nghiệp, [[Capstan]] Caterpillar + Encoder đo mét; Tổ Đùn Vỏ – QC – OE.",
        "hidden_losses": (
            "• **Chọn sai bộ Chày–Cối (lắp nhầm Pressure thay vì Tubing hoặc sai [[DDR]]):** Làm vỏ bám dính cứng vào lõi (khách hàng không tuốt được vỏ trả hàng!) hoặc rách ống nhựa liên tục khi chạy [[LSZH]].\n"
            "• **Máng nước [[Cooling Trough]] quá nóng buổi trưa Đà Nẵng (34°C):** Vỏ cáp ra khỏi máng còn mềm 55°C bị bết dính rulo → Công nhân tự hạ tốc độ máy đùn -20% (tụt [[OEE]] Performance nặng!).\n"
            "• **Bánh xe đo mét [[Capstan]] mòn không hiệu chuẩn:** Sai số +0.8% khiến nhà máy tự động 'tặng không' 40 km dây đồng/tháng — hoặc sai số âm -0.5% làm khách hàng kiện thiếu mét!\n"
            "• **Máy in phun hết mực/nhòe chữ ca đêm:** Chạy hổng hàng chục km cáp không có chữ thương hiệu CADIVI phải tuốt bỏ hoặc chạy in lại tốn kém."
        ),
        "oe_end_to_end_actions": (
            "1. **Lập Bảng chọn Chày–Cối chuẩn [[DDR]] + [[Poka-Yoke]] khắc mã 'T'/'P':** Chuẩn hóa bảng Excel tra đúng [[DDR]] (PVC: 1.5–2.5; LSZH: 1.1–1.6) và khắc laser ký hiệu + sơn màu chống lắp nhầm kiểu Pressure/Tubing.\n"
            "2. **Xử lý nút thắt nhiệt độ [[Cooling Trough]] & [[Die Drool]]:** Giám sát nhiệt độ nước máng trên [[SCADA]] (giữ ≤ 25°C, làm mát phân tầng cho vỏ dày), lắp biến tần [[VFD]] tiết kiệm điện bơm tuần hoàn, cấp dao đồng thau chống xước miệng khuôn Cối.\n"
            "3. **Gắn [[Poka-Yoke]] cho Máy in phun & [[Spark Tester]]:** Lắp cảm biến quang kiểm tra độ tương phản chữ in tự dừng sau 5m mất chữ; cài ngưỡng tự dừng máy trên [[PLC]] khi [[Spark Tester]] báo ≥ 2 lỗi/500m và kiểm tra nối đất đầu ca.\n"
            "4. **Hiệu chuẩn định kỳ bánh đo mét [[Capstan]]:** Đưa kiểm chuẩn sai số mét (≤ ±0.2%) bằng thước chuẩn vào lịch [[PM Compliance]] hàng tuần và [[LPA]]."
        ),
        "kpis": "[[OEE]] Đùn vỏ ≥ 74% | Độ đồng tâm vỏ ≥ 90% | Sai số chiều dài mét ≤ ±0.2% | Lỗi chữ in / bết vỏ = 0 cuộn | Thời gian dừng cạo [[Die Drool]] < 1 lần/ca.",
        "key_terms": ["DDR", "Crosshead", "LSZH", "Hopper Dryer", "Die Drool", "Cooling Trough", "Spark Tester", "Capstan", "Poka-Yoke", "SCADA"],
        "doc_key": "cable_extrusion_wire_forensics",
        "lesson_id": "L4.4"
    },
    {
        "id": "S07",
        "code": "Trạm 07",
        "title": "Phòng Thí Nghiệm Kiểm Định Xuất Xưởng (Lab QA/QC & Hợp Quy QCVN 4 / IEC)",
        "zone": "Phòng Thí Nghiệm Kiểm Tra Chất Lượng (Lab QA/QC)",
        "input": "Mẫu cắt đầu/cuối rulo và cuộn cáp thành phẩm từ Trạm 02–06 kèm Phiếu lệnh SX / Mã QR truy xuất.",
        "output": "Phiếu kết quả thử nghiệm (Test Report) đạt chuẩn [[IEC 60228]], [[IEC 60502]], [[QCVN 4]] (mở khóa trạng thái trên [[ERP]] cho phép nhập kho & xuất hàng) — hoặc Phiếu NCR cách ly lô lỗi kích hoạt [[8D]].",
        "machines_and_teams": "Cầu đo [[Kelvin Bridge]], bể thử cao áp [[Water Immersion]], tủ thử [[Hot Set Test]] 200°C, máy kéo vạn năng [[Tensile]], tủ lão hóa [[Aging Oven]], phòng lồng Faraday đo [[Partial Discharge]], kính hiển vi đo chiều dày; Phòng Lab QA/QC – Kỹ thuật – OE.",
        "hidden_losses": (
            "• **Cổ chai chờ giấy xuất xưởng (Lab Lead Time 5–8 giờ):** Xưởng mang mẫu lên rải rác, Lab ngâm nước từng cuộn lẻ tẻ làm hàng chục rulo thành phẩm nằm chật xưởng chờ giao!\n"
            "• **Sai số hệ thống đo ([[MSA]] / [[Gage R&R]] > 30%):** Quên quy đổi nhiệt độ 20°C trên [[Kelvin Bridge]] khi trưa nóng 30°C (báo rớt oan!), dao dập mẫu Dumbbell cùn làm đứt sớm giả tạo khi kéo [[Tensile]].\n"
            "• **Dữ liệu Lab 'ngủ yên trong sổ giấy':** Lab chỉ ghi Đạt/Không Đạt mà không nhập số đo liên tục (điện trở, chiều dày min, đường kính) cho OE phân tích [[SPC]] & [[Cpk]] → Bỏ lỡ hoàn toàn cơ hội giảm [[Copper Give-away]] & [[Over-thickness]]!"
        ),
        "oe_end_to_end_actions": (
            "1. **Tối ưu dòng chảy Phòng Lab (giảm chờ từ 6h → 2h):** Thiết lập lịch gom mẫu cố định theo khung giờ (vd: 10h – 15h – 21h), bố trí 2 bể [[Water Immersion]] luân phiên (1 bể ngâm ủ 1h song song 1 bể đang thử cao áp — đúng tư duy [[SMED]]!).\n"
            "2. **Thẩm định độ tin cậy đo lường bằng [[MSA]] / [[Gage R&R]]:** Chạy [[Gage R&R]] trên [[Minitab]] cho cầu [[Kelvin Bridge]], thước đo chiều dày quang học và máy [[Tensile]] (bắt buộc %GRR < 10% hoặc < 30%) trước mọi dự án [[DMAIC]].\n"
            "3. **Số hóa dữ liệu đo Lab tự động chảy về [[Power BI]] / [[Minitab]]:** Thiết kế form Excel/Python tự động quy đổi điện trở về 20°C, vẽ ngay biểu đồ [[SPC]] & tính [[FPY]] / [[RTY]] toàn chuỗi để cảnh báo xu hướng trôi trước khi rớt chuẩn [[QCVN 4]]!\n"
            "4. **Dẫn dắt xử lý sự cố chất lượng [[8D]]:** Khi có lô rớt [[Hot Set Test]] hoặc [[Partial Discharge]], OE chủ trì truy ngược phả hệ lô trên [[MES]] để khoanh vùng đúng lô lỗi và dứt điểm nguyên nhân gốc."
        ),
        "kpis": "Lab Lead Time ≤ 2 giờ | %GRR ([[Gage R&R]]) < 15% | Tỷ lệ đạt lần đầu toàn chuỗi [[RTY]] ≥ 94% | Tỷ lệ khiếu nại khách hàng = 0 vụ nghiêm trọng.",
        "key_terms": ["Kelvin Bridge", "Water Immersion", "Hot Set Test", "Tensile", "Aging Oven", "Partial Discharge", "QCVN 4", "Gage R&R", "MSA", "RTY", "8D"],
        "doc_key": "minitab_spc",
        "lesson_id": "L4.5"
    },
    {
        "id": "S08",
        "code": "Trạm 08",
        "title": "Đánh Cuộn, Cắt Đoạn (Cut-Length), Đóng Gói, Kho Thành Phẩm & Giao Hàng (OTIF)",
        "zone": "Tổ Đóng Cuộn – Khu Sang Rulo – Kho Thành Phẩm – Logistics",
        "input": "Rulo cáp thành phẩm đã được Lab Trạm 07 mở khóa đạt chuẩn, danh sách chiều dài cắt của từng đơn hàng dự án, rulo gỗ/thép, màng co, thùng carton, tem mã vạch QR.",
        "output": "Khoanh dây dân dụng 100m bọc màng co đẹp chuẩn hoặc rulo cáp lực cắt đúng mét dự án (kèm biên bản xuất xưởng & tem truy xuất QR), xếp xe giao đúng hẹn OTIF.",
        "machines_and_teams": "Máy đánh khoanh tự động/bán tự động 100m + buồng co màng nhiệt, máy sang cuộn cắt đoạn (Rewinding & Cutting Machine) có [[Spark Tester]] kiểm tra lại, cân sàn điện tử, xe nâng; Tổ Đóng gói – Kho TP – Kế hoạch – OE.",
        "hidden_losses": (
            "• **Phế mẩu thừa [[Cut-Length]] cực đắt (5–10% đơn hàng dự án):** Cắt rulo theo thứ tự ngẫu nhiên để dư hàng loạt khúc cáp lực 40–150m không bán được, phải tuốt đồng bán phế!\n"
            "• **Nút thắt lao động thủ công ([[OLE]] thấp):** Tổ đóng khoanh 100m mất cân bằng chuyền (người quấn dây chạy kịp nhưng người bọc màng/dán tem bị ùn ứ chờ đợi), di chuyển thừa theo sơ đồ [[Spaghetti]].\n"
            "• **Lỗi giao nhầm mã/thiếu mét/hư hỏng rulo:** Dán nhầm tem nhãn giữa dây VC 2.5 và VC 4.0 hoặc xếp rulo gỗ nặng thiếu chèn khóa gây trầy xước vỏ khi vận chuyển."
        ),
        "oe_end_to_end_actions": (
            "1. **Giải bài toán tối ưu [[Cut-Length]] bằng Excel Solver / [[Python]]:** Gom toàn bộ các đoạn lẻ dự án để tìm tổ hợp cắt sát 100% chiều dài rulo và đẩy tổng chiều dài mục tiêu ngược về Trạm 03–04 ngay từ lúc phát lệnh → Giảm phế mẩu thừa từ 8% xuống < 1.2%!\n"
            "2. **Cân bằng chuyền [[Yamazumi]] & [[Time Study]] tổ đóng khoanh 100m:** Đo [[SAM]] từng thao tác (cuốn → cột dây → dán tem → bọc màng co → xếp pallet), gom/tách bước kéo Balance Efficiency ≥ 85%, bố trí Layout hình chữ U giảm 50% bước đi trên sơ đồ [[Spaghetti]].\n"
            "3. **Áp [[Poka-Yoke]] quét mã vạch xuất kho:** Quét QR trên rulo khớp đúng lệnh xuất kho [[ERP]] mới cho in phiếu giao hàng — xóa 100% lỗi giao nhầm mã dây/sai mét.\n"
            "4. **Thiết lập siêu thị thành phẩm [[Kanban]] cho dây dân dụng nhóm AX:** Kiểm soát mức tồn Min–Max tự động kích hoạt bổ sung để đại lý đặt là có hàng giao ngay trong 24h (OTIF ≥ 97%)."
        ),
        "kpis": "Phế cắt đoạn [[Cut-Length]] < 1.2% | [[OLE]] tổ đóng cuộn ≥ 82% | Balance Efficiency ≥ 85% | Giao hàng đúng đủ OTIF ≥ 96% | Sai sót giao nhầm = 0.",
        "key_terms": ["Cut-Length", "Yamazumi", "Time Study", "SAM", "Spaghetti", "OLE", "Lead Time", "Poka-Yoke", "Python"],
        "doc_key": "cable_cost_capacity",
        "lesson_id": "L2.4"
    },
    {
        "id": "S09",
        "code": "Trạm 09",
        "title": "Dòng Chảy Ngược: Thu Hồi Phế Liệu, Bảo Trì Cơ Điện (TPM/PdM) & Quyết Toán Giá Thành",
        "zone": "Khu Tập Kết Phế Liệu – Phòng Cơ Điện (Bảo Trì) – Phòng Kế Toán Giá Thành",
        "input": "Phế liệu từ Trạm 02–08, yêu cầu sửa chữa & thẻ bất thường [[Red Tag]]/Fuguai, dữ liệu sản lượng/vật tư/giờ máy/điện năng cuối ca & cuối tháng trên [[SAP PP]] / [[MES]].",
        "output": "Đồng thu hồi giá trị cao nhất (~94%), nhựa sạch tái chế [[PVC]] hợp chuẩn (Regrind), máy móc duy trì [[MTBF]] cao an toàn [[LOTO]], và Báo cáo [[Standard Cost]] Variance + [[Cost Deployment]] trình Ban Giám Đốc.",
        "machines_and_teams": "Cân điện tử khu phế liệu, máy tuốt cáp/nghiền nhựa Regrind, thiết bị bảo trì [[CBM / PdM]] (camera ảnh nhiệt, bút đo rung, siêu âm rò khí nén), hệ thống [[SAP PP]] / [[Power BI]]; Cơ Điện – Kế Toán – EHS – OE.",
        "hidden_losses": (
            "• **Vứt lẫn 3 nhóm phế liệu ngay chân máy:** Vứt đồng trần (thu hồi ~94% giá trị) lẫn vào đồng dính nhựa (chỉ thu hồi ~65–70% sau tốn công bóc tách!) làm bốc hơi hàng trăm triệu đồng/năm!\n"
            "• **Bảo trì kiểu 'chữa cháy' (Reactive > 50%):** [[PM Compliance]] thấp (< 65%), [[Wrench Time]] thợ Cơ Điện chỉ ~30% do đi tìm phụ tùng/chờ máy → Máy cổ chai hỏng đột xuất giữa mùa cao điểm!\n"
            "• **Thất thoát năng lượng ẩn ([[ISO 50001]]):** Rò rỉ khí nén kêu xì khắp xưởng (tốn 20–30% điện máy nén khí!), bơm nước giải nhiệt chạy hết công suất 50Hz lúc non tải ca đêm.\n"
            "• **Đóng lệnh [[SAP PP]] kiểu Backflushing mù:** Hệ thống tự trừ kho theo định mức chuẩn làm báo cáo cuối tháng luôn 'đẹp như mơ = 0%', đến cuối năm kiểm kê kho mới tá hỏa hụt hàng chục tấn đồng!"
        ),
        "oe_end_to_end_actions": (
            "1. **Phân luồng 3 thùng phế mã màu [[5S]] + Tách Reason Code trên [[SAP PP]]:** Xanh = Đồng trần tinh khiết | Vàng = Đồng dính nhựa | Xám = Nhựa purge sạch tái chế; bắt buộc cân phế thực tế cuối ca đối chiếu [[BOM]] (cấm Backflush mù!).\n"
            "2. **Nâng cấp Bảo trì [[TPM]] + [[CBM / PdM]] + [[Wrench Time]]:** Chốt 'Cửa sổ Bảo trì Vàng' vào lịch [[MPS]] đẩy [[PM Compliance]] ≥ 90%; soạn sẵn bộ [[Kitting]] phụ tùng PM tăng [[Wrench Time]] từ 32% lên ≥ 50%; soi camera ảnh nhiệt tủ điện hàng tháng & bắt buộc [[LOTO]] 6 bước.\n"
            "3. **Chạy [[Cost Deployment]] & [[OEE Waterfall]] quy mọi tổn thất ra tiền VNĐ:** Phối hợp Kế toán tách rạch ròi Price Variance (giá đồng thị trường) vs Usage Variance (năng lực xưởng & OE), xác nhận Hard Savings thật cho mọi dự án [[ROI]] / [[Payback]].\n"
            "4. **Khóa hệ thống duy trì toàn nhà máy:** Vận hành nhịp nhàng họp tầng Tier 1–2–3, [[LSW]], kiểm tra phân tầng [[LPA]] và Ma trận leo thang sự cố [[Escalation Matrix]] (5p–15p–30p) để mọi thành quả bền vững vĩnh viễn!"
        ),
        "kpis": "Tỷ lệ thu hồi đồng trần riêng biệt ≥ 95% | [[PM Compliance]] ≥ 90% | [[Wrench Time]] ≥ 50% | Giảm điện năng [[SEC]] -5 đến -10%/năm | 0 tai nạn vi phạm [[LOTO]].",
        "key_terms": ["Scrap", "Standard Cost", "Cost Deployment", "OEE Waterfall", "PM Compliance", "Wrench Time", "CBM / PdM", "LOTO", "ISO 50001", "LSW", "LPA", "Escalation Matrix"],
        "doc_key": "oe_field_execution_case_test",
        "lesson_id": "L6.1"
    },
]


PRODUCT_FLOWS = [
    {
        "id": "F01",
        "code": "Luồng A",
        "title": "Dây Điện Dân Dụng (VC / VCm / VCmd 450/750V) — Sản Lượng Lớn, Tốc Độ Cao (MTS Pull)",
        "product_examples": "Dây đơn cứng VC 1.5 / 2.5 / 4.0 / 6.0 mm²; Dây mềm VCm 1.5 / 2.5 mm²; Dây đôi mềm dẹt VCmd 2×1.5 mm² (chuẩn [[QCVN 4]]).",
        "route_diagram": (
            "Đồng Rod Ø8.0mm (IQC [[ASTM B49]])\n"
            "   │\n"
            "   ▼\n"
            "[S02] Kéo thô [[RBD]] (→ Ø1.38–2.0mm) ──▶ Kéo tinh [[Multi-wire]] (→ Ø0.25–0.67mm) + Ủ [[Annealing]]\n"
            "   │\n"
            "   ▼\n"
            "[S03] Bện ruột mềm trên máy [[Buncher]] (bỏ qua nếu dây đơn đặc VC Class 1)\n"
            "   │\n"
            "   ▼\n"
            "[S04/S06] Đùn bọc cách điện [[PVC]] tốc độ cao (300–800 m/phút) + [[Laser Gauge]] + [[Spark Tester]] + In chữ\n"
            "   │\n"
            "   ▼\n"
            "[S08] Đánh khoanh chuẩn 100m + Bọc màng co + Dán tem QR ──▶ [S07] Lab [[QCVN 4]] ──▶ Kho siêu thị đại lý"
        ),
        "bottleneck": "Máy đùn [[PVC]] tốc độ cao (bị kéo tụt [[OEE]] bởi đổi màu liên tục và dừng thay rulo xả/thu) + Khâu đánh khoanh đóng gói 100m (tốn nhân công).",
        "biggest_losses": "1. [[Copper Give-away]] (sản lượng cực lớn nên thừa +0.008mm mất hàng tỷ đồng!) · 2. Phế đổi màu & dừng thay rulo · 3. Sai số mét bánh đo [[Capstan]] (tặng thừa mét trên hàng chục nghìn khoanh 100m!) · 4. Lãng phí nhân công [[OLE]] ở khu Buncher & đóng khoanh.",
        "oe_strategy": (
            "• **Dòng chảy Kéo ([[Pull System]] / [[Kanban]]):** Vì dây VC bán đều quanh năm (nhóm AX trong [[ABC-XYZ]]), lập siêu thị thành phẩm & ô sàn Kanban giữa Bện ↔ Đùn thay vì đẩy lô khổng lồ.\n"
            "• **Biến máy đùn thành dòng chảy liên tục:** Lắp [[Pay-off]] đôi + [[Accumulator]] + [[Take-up]] tự động kết hợp luật vòng màu [[Color Sequencing]] (Trắng → Vàng → Xanh → Đỏ → Đen).\n"
            "• **Tối ưu [[OLE]] tối đa:** Vẽ [[Man-Machine Chart]] cho 1 công nhân đứng 4–6 máy [[Buncher]]; cân bằng chuyền [[Yamazumi]] tổ đóng khoanh 100m đạt Balance Efficiency ≥ 85%.\n"
            "• **Chặn thất thoát từng milimet:** Siết tuổi thọ khuôn [[PCD]] giảm [[Copper Give-away]] về ≤ +0.4%, hiệu chuẩn [[Capstan]] sai số ≤ ±0.2% và đảm bảo 100% đạt [[QCVN 4]]."
        ),
        "key_terms": ["QCVN 4", "RBD", "Multi-wire", "Buncher", "PVC", "Color Sequencing", "Accumulator", "Copper Give-away", "Yamazumi", "Kanban"],
        "doc_key": "oee",
        "lesson_id": "L1.1"
    },
    {
        "id": "F02",
        "code": "Luồng B",
        "title": "Cáp Điện Lực Hạ Thế 0.6/1kV (CVV / CXV / CXV-DSTA) — MTO/ATO Cho Công Trình & Dự Án",
        "product_examples": "Cáp 3–4 lõi cách điện [[XLPE]] vỏ [[PVC]]: CXV 3×50+1×25, CXV 3×120+1×70, CXV/DSTA 3×240+1×120 (chuẩn [[IEC 60502]]-1).",
        "route_diagram": (
            "Đồng Rod Ø8.0mm (IQC)\n"
            "   │\n"
            "   ▼\n"
            "[S02] Kéo thô [[RBD]] (→ Ø1.7–3.2mm) + Ủ [[Annealing]]\n"
            "   │\n"
            "   ▼\n"
            "[S03] Bện lồng cứng [[Rigid Strander]] (ép nén tròn Compact hoặc rẻ quạt Sector Class 2)\n"
            "   │\n"
            "   ▼\n"
            "[S04] Đùn cách điện [[XLPE]] [[Silane]] (95% nền + 5% Catalyst) ──▶ ★ PHÒNG XÔNG HƠI SAUNA (4–12h) ★\n"
            "   │\n"
            "   ▼\n"
            "[S05] Ghép 3–4 lõi trên [[Drum Twister]] (+ sợi độn + băng quấn) ──▶ Bọc đệm & Giáp thép [[DSTA]] (nếu có)\n"
            "   │\n"
            "   ▼\n"
            "[S06] Đùn vỏ ngoài [[PVC]] ([[Crosshead]] Tubing) + In chữ ──▶ [S07] Lab [[IEC 60502]] & [[Hot Set Test]]\n"
            "   │\n"
            "   ▼\n"
            "[S08] Cắt đoạn tối ưu [[Cut-Length]] sang Rulo gỗ ──▶ Xuất xe dự án"
        ),
        "bottleneck": "Phòng Xông Hơi Sauna (nơi dồn cục WIP chờ gom mẻ 2–3 ngày!) + Thời gian nạp 37–61 rulo trên [[Rigid Strander]] + Máy đùn vỏ cỡ lớn.",
        "biggest_losses": "1. Phế lõi đồng bọc XLPE bị thừa khi 4 rulo vào [[Drum Twister]] lệch chiều dài! · 2. Phế mẩu thừa [[Cut-Length]] cuối rulo dự án · 3. [[Over-thickness]] trên nhựa XLPE đắt tiền (không tái chế được!) · 4. Tồn kho WIP nằm chờ gom mẻ lò xông kéo dài [[Lead Time]] lên 10–14 ngày.",
        "oe_strategy": (
            "• **Đánh sập ùn tắc Phòng Xông Sauna:** Dùng [[DOE]] + [[Hot Set Test]] phân nhóm lịch xông theo độ dày (mỏng 4h, dày 8h) chạy theo nhịp cố định mỗi ca thay vì chờ gom đủ 12 rulo → Cắt 50% WIP & rút [[Lead Time]] từ 12 ngày xuống 4–5 ngày!\n"
            "• **Đồng bộ chiều dài 4 rulo lõi + Solver [[Cut-Length]]:** Khóa dung sai đo mét Trạm 04 ≤ ±0.5% trước khi vào [[Drum Twister]] và chạy Excel Solver/[[Python]] tổ hợp cắt rulo theo đơn dự án.\n"
            "• **[[SMED]] nạp lồng [[Rigid Strander]] & cuộn băng thép [[DSTA]] lớn:** Rút nạp lồng từ 72p → 24p; đổi cuộn băng thép 2,500m giảm 80% dừng hàn.\n"
            "• **Kiểm soát chặt vỏ Tubing & [[Over-thickness]]:** Gắn [[Laser Gauge]] vòng kín giữ vỏ đúng [[IEC 60502]] và đảm bảo dễ tuốt vỏ khi thi công."
        ),
        "key_terms": ["XLPE", "Silane", "Rigid Strander", "Drum Twister", "DSTA", "Cut-Length", "Hot Set Test", "Over-thickness", "IEC 60502", "VSM"],
        "doc_key": "cable_cost_capacity",
        "lesson_id": "L3.2"
    },
    {
        "id": "F03",
        "code": "Luồng C",
        "title": "Cáp Vặn Xoắn Treo Trên Không (ABC) & Dây Nhôm Trần Lõi Thép (ACSR) — Dự Án Điện Lực EVN",
        "product_examples": "Cáp vặn xoắn LV-ABC 2×16, 4×50, 4×95 mm²; Dây nhôm trần lõi thép [[ACSR]] 95/16, 185/29, 240/32 mm².",
        "route_diagram": (
            "Nhôm Rod Ø9.5mm (EC Grade ≥ 61% [[IACS]]) + Sợi Thép mạ kẽm (với [[ACSR]])\n"
            "   │  ⚠️ KHU VỰC KÉO NHÔM TÁCH BIỆT TUYỆT ĐỐI VỚI ĐỒNG!\n"
            "   ▼\n"
            "[S02] Kéo sợi nhôm (dùng dầu kéo chuyên dụng cho nhôm)\n"
            "   │\n"
            "   ▼\n"
            "[S03] Bện [[Rigid Strander]]:\n"
            "      ├─ Nhánh ACSR: Bện lớp nhôm quanh lõi thép + Bơm mỡ chịu nhiệt ──▶ Lab lực kéo UTS ──▶ Xuất EVN\n"
            "      └─ Nhánh ABC:  Bện ép nén ruột nhôm ──▶ [S04] Đùn [[XLPE]] Đen chống UV (2.5% Carbon Black, tạo gân 0-1-2-3)\n"
            "                     ──▶ Xông hơi [[Silane]] ──▶ [S05] Xoắn bó 4 lõi [[ABC Cable]] ──▶ [S07] Lab UV/Hot Set ──▶ Xuất EVN"
        ),
        "bottleneck": "Năng lực máy kéo nhôm & máy bện [[Rigid Strander]] vào mùa cao điểm đầu tư lưới điện EVN; kiểm soát bề mặt sạch không lẫn tạp chất đồng và độ đồng đều gân pha [[ABC Cable]].",
        "biggest_losses": "1. Nhiễm bụi đồng từ xưởng kéo đồng gây ăn mòn điện hóa rỗ sợi nhôm ngoài trời · 2. Tràn mỡ bôi trơn ra lớp ngoài [[ACSR]] bị EVN từ chối nghiệm thu · 3. Hàm lượng Carbon Black < 2% hoặc trộn kém làm rớt lão hóa UV · 4. Dừng đổi mã gân pha không tối ưu.",
        "oe_strategy": (
            "• **Cách ly 5S & [[Poka-Yoke]] Đồng vs Nhôm:** Phân tách tuyệt đối máy kéo/khuôn kéo/rulo nhôm riêng (sơn mã màu nhận diện rulo Nhôm), cấm tuyệt đối tái dùng khuôn cũ từ xưởng đồng.\n"
            "• **[[Campaign Scheduling]] 0-Purge cho 4 pha [[ABC Cable]]:** Vì cả 4 lõi đều dùng chung 1 loại nhựa [[XLPE]] Đen, xếp chạy liền mạch 4 pha chỉ tháo nhanh vòng Cối tạo gân (0–1–2–3 gân trong 5 phút) mà KHÔNG cần xả nhựa [[Purging]] → Tăng [[OEE]] máy đùn +9%!\n"
            "• **Định lượng mỡ tự động đồng bộ tốc độ cho [[ACSR]]:** Gắn bơm định lượng theo xung Encoder khống chế đúng g/m, xóa sạch lỗi tràn mỡ ra lớp nhôm ngoài.\n"
            "• **Siết tiến độ thầu EVN bằng [[RCCP]]:** Dự báo tải tấn nhôm trước 6–8 tuần để không vỡ cam kết giao hàng phạt hợp đồng dự án."
        ),
        "key_terms": ["ABC Cable", "ACSR", "IACS", "Rigid Strander", "XLPE", "Silane", "Campaign Scheduling", "RCCP", "Poka-Yoke"],
        "doc_key": "cable_mfg_machines",
        "lesson_id": "L1.3"
    },
    {
        "id": "F04",
        "code": "Luồng D",
        "title": "Cáp Điện Lực Trung Thế 24kV / 35kV (CXV/S/DSTA) — Công Nghệ Đỉnh Cao Ống Cong CCV",
        "product_examples": "Cáp trung thế 1 lõi hoặc 3 lõi 12/20(24)kV, 18/30(36)kV tiết diện 50–630 mm² (chuẩn [[IEC 60502]]-2).",
        "route_diagram": (
            "Đồng/Nhôm Rod siêu sạch ──▶ [S02] Kéo sợi ──▶ [S03] Bện ép nén siêu nhẵn (+ sợi [[Water-Blocking]] lõi)\n"
            "   │\n"
            "   ▼  ⚠️ CẤP LIỆU PHÒNG SẠCH (CLEANROOM) CHỐNG BỤI TẠP CHẤT!\n"
            "[S04] Dây chuyền [[CCV]] Đùn 3 lớp đồng thời (Bán dẫn trong + [[XLPE]] Peroxide + Bán dẫn ngoài)\n"
            "      ──▶ Ống lưu hóa cong dài 80–150m (Khí Nitơ 10–14 bar, 300–400°C) ──▶ Làm nguội áp suất cao\n"
            "   │\n"
            "   ▼\n"
            "[S05] Quấn băng bán dẫn [[Water-Blocking]] + Màn chắn băng/sợi đồng ──▶ Ghép 3 lõi [[Drum Twister]] ──▶ Giáp [[DSTA]]/DATA\n"
            "   │\n"
            "   ▼\n"
            "[S06] Đùn vỏ HDPE/PVC ──▶ [S07] ★ PHÒNG LỒNG FARADAY ĐO [[Partial Discharge]] (≤ 5 pC) ★ ──▶ Rulo thép xuất xưởng"
        ),
        "bottleneck": "Dây chuyền [[CCV]] triệu đô (chi phí khởi động/dừng lò cực lớn: tốn 4–6 giờ ổn định nhiệt áp & hàng trăm kg nhựa siêu sạch!) + Phòng thử cao áp Faraday đo [[Partial Discharge]].",
        "biggest_losses": "1. Bật/tắt dây chuyền [[CCV]] nhiều lần trong tuần do lịch chạy cắt nhỏ đơn hàng lẻ → Phế khởi động ăn sạch 100% lợi nhuận! · 2. Một hạt bụi hay 1 lần sụt áp khí Nitơ gây bọt khí làm cả rulo rớt [[Partial Discharge]] (> 5 pC) thành phế phẩm trị giá hàng trăm triệu! · 3. Ẩm băng chống thấm bán dẫn.",
        "oe_strategy": (
            "• **Tối đa hóa [[TEEP]] bằng chiến dịch chạy liên tục 24/7 ([[Campaign Scheduling]]):** Gom toàn bộ đơn trung thế 24kV chạy liên tục 5–7 ngày không tắt lò [[CCV]], cắt 65% phế khởi động!\n"
            "• **Giám sát [[SCADA]] / [[MES]] theo từng mét dây:** Ghi log liên tục áp suất khí Nitơ, nhiệt độ 3 đầu đùn, đường kính tia X/siêu âm gắn với vị trí mét cáp — khi có lỗi [[Partial Discharge]] truy ngược định vị TDR ra đúng giây xảy ra sự cố!\n"
            "• **Kỷ luật phòng sạch Cleanroom & bảo trì dự đoán [[CBM / PdM]]:** Nạp nhựa kín chân không tuyệt đối, bảo trì dự phòng hệ thống gia nhiệt/van Nitơ không để sụt áp đột ngột giữa mẻ."
        ),
        "key_terms": ["CCV", "Partial Discharge", "XLPE", "Water-Blocking", "IEC 60502", "TEEP", "Campaign Scheduling", "SCADA", "CBM / PdM"],
        "doc_key": "cable_mfg_machines",
        "lesson_id": "L1.4"
    },
    {
        "id": "F05",
        "code": "Luồng E",
        "title": "Cáp Chống Cháy & Ít Khói Không Halogen (FR / LSZH) — Chung Cư, Bệnh Viện, Sân Bay, Metro",
        "product_examples": "Cáp chống cháy CXV/FR, CXV/FRT (chịu lửa 750–950°C 90–180p theo IEC 60331) bọc vỏ [[LSZH]] ít khói không axit.",
        "route_diagram": (
            "Đồng Rod ──▶ [S02] Kéo sợi ──▶ [S03] Bện ruột đồng\n"
            "   │\n"
            "   ▼\n"
            "[S04a] ★ QUẤN BĂNG [[Mica FR]] (1–2 lớp, chồng mép Overlap chuẩn 30–50% + cảm biến đứt băng) ★\n"
            "   │\n"
            "   ▼\n"
            "[S04b] Đùn cách điện [[XLPE]] (+ Xông Sauna) ──▶ [S05] Ghép lõi [[Drum Twister]]\n"
            "   │\n"
            "   ▼  ⚠️ SẤY HÚT ẨM [[Hopper Dryer]] BẮT BUỘC + TRỤC VÍT NÉN THẤP + NHIỆT ≤ 165°C!\n"
            "[S06] Đùn vỏ ngoài [[LSZH]] ([[DDR]] nhỏ 1.1–1.6, kiểm soát chống rỗ khí & [[Die Drool]])\n"
            "   │\n"
            "   ▼\n"
            "[S07] Lab thử lửa IEC 60331, đo mật độ khói > 60% & độ axit khí cháy ──▶ [S08] Đóng rulo giao công trình"
        ),
        "bottleneck": "Tốc độ máy quấn băng [[Mica FR]] + Tốc độ đùn vỏ [[LSZH]] rất chậm (chỉ bằng 40–60% tốc độ [[PVC]] do độ nhớt cao & nhạy nhiệt phân hủy bột khoáng ATH sinh bọt khí!).",
        "biggest_losses": "1. Quấn băng [[Mica FR]] chồng mép dư lên 60% (tốn băng Mica đắt tiền + phình đường kính làm đội thêm nhựa XLPE!) · 2. Đùn [[LSZH]] bằng trục vít PVC & cài nhiệt cao > 175°C gây nổ bọt rỗ khí (phế 7–10%) và đóng cặn [[Die Drool]] dừng cạo liên tục · 3. Nhập sai Routing tốc độ trên [[ERP]] làm kế hoạch [[CRP]] bị vỡ tiến độ!",
        "oe_strategy": (
            "• **Tách riêng Routing tốc độ & trục vít cho [[LSZH]] trên [[SAP PP]]:** Tuyệt đối không dùng chung định mức tốc độ PVC; chỉ định máy có trục vít tỷ số nén thấp (~1.2:1) và bảng chọn Chày–Cối [[DDR]] 1.1–1.6.\n"
            "• **[[SMED]] phễu sấy di động [[Hopper Dryer]]:** Sấy sẵn hạt [[LSZH]] bên ngoài trước khi chuyển mẻ để xóa 120 phút dừng máy chờ sấy; đánh bóng mạ gương lòng Cối giảm [[Die Drool]] từ 6 lần/ca xuống < 1 lần/ca.\n"
            "• **Hiệu chuẩn góc quấn & [[Poka-Yoke]] đứt băng [[Mica FR]]:** Khống chế chồng mép đúng 40% ± 3% và khóa liên động cảm biến hết/đứt băng tự dừng trong 0.5 giây để không chạy hổng đoạn thiếu lớp chống cháy!"
        ),
        "key_terms": ["Mica FR", "LSZH", "Hopper Dryer", "DDR", "Die Drool", "Poka-Yoke", "CRP", "SAP PP", "SMED"],
        "doc_key": "cable_extrusion_wire_forensics",
        "lesson_id": "L4.4"
    },
    {
        "id": "F06",
        "code": "Luồng F",
        "title": "Cáp Đặc Chủng: Cáp Điện Mặt Trời (Solar H1Z2Z2-K) & Cáp Điều Khiển Chống Nhiễu (Braiding)",
        "product_examples": "Cáp Solar DC 1,500V [[Solar Cable]] 1×4.0 / 6.0 mm² chuẩn EN 50618; Cáp điều khiển chống nhiễu lưới đồng CVV-S 4×1.5 / 12×1.5 mm².",
        "route_diagram": (
            "Đồng Rod ──▶ [S02] Kéo tinh & Mạ thiếc ([[Tinned Copper]] dày 0.5–2.5 µm, không tróc xước!)\n"
            "   │\n"
            "   ▼\n"
            "[S03] Bện mềm Class 5 trên [[Buncher]] (chỉnh puly/lực căng êm bảo vệ lớp mạ thiếc)\n"
            "   │\n"
            "   ├──▶ Nhánh SOLAR CABLE: [S04/S06] Đồng đùn 2 lớp (Co-extrusion XLPO cách điện + vỏ UV)\n"
            "   │       ──▶ ★ CHIẾU XẠ [[E-beam]] (120–180 kGy + thẻ đo liều Dosimeter) ★ ──▶ Lab EN 50618\n"
            "   │\n"
            "   └──▶ Nhánh CÁP CHỐNG NHIỄU: [S04] Đùn lõi ──▶ [S05] Ghép lõi ──▶ ★ DÀN MÁY [[Braiding]] (3–12 m/p) ★\n"
            "           ──▶ [S06] Đùn vỏ PVC/LSZH ──▶ [S07] Lab điện trở & độ phủ ≥ 85% ──▶ Đóng cuộn"
        ),
        "bottleneck": "Dàn máy đan lưới [[Braiding]] (tốc độ chỉ 3–12 m/phút — chậm nhất toàn nhà máy!) và lịch gom lô chiếu xạ [[E-beam]] cho [[Solar Cable]].",
        "biggest_losses": "1. Máy [[Braiding]] đan thừa độ che phủ (93% thay vì chuẩn 85%) làm giảm -22% công suất cổ chai và đốt thừa +14% đồng mạ thiếc đắt tiền! · 2. Quấn suốt Bobbin dài ngắn lệch nhau gây dừng thay lẻ liên tục · 3. Xước tróc lớp mạ thiếc [[Tinned Copper]] làm rớt bài thử hóa chất chống ăn mòn · 4. Trộn lẫn phế đồng mạ thiếc với đồng trần.",
        "oe_strategy": (
            "• **Nâng vọt [[OLE]] khu [[Braiding]] bằng [[Man-Machine Chart]] + [[Jidoka]]:** Quấn đồng bộ 100% suốt Bobbin cùng chiều dài, chuẩn bị sẵn khay Bobbin thay nhanh bên ngoài ([[SMED]]), cài cảm biến đứt sợi tự dừng để 1 công nhân quản lý 6–10 máy [[Braiding]]!\n"
            "• **Chỉnh chuẩn bước đan về mục tiêu 87%:** Giải phóng ngay +20% công suất cổ chai và tiết kiệm hàng trăm triệu đồng mạ thiếc/năm.\n"
            "• **Áp dụng Co-extrusion 2 lớp & gom lô [[E-beam]] khoa học cho [[Solar Cable]]:** Đùn đồng thời cách điện + vỏ trong 1 lượt giảm 50% vận chuyển WIP; gắn thẻ Dosimeter đầu–cuối rulo đảm bảo liều bức xạ đồng đều.\n"
            "• **Tách mã vật tư & mã phế [[Tinned Copper]] riêng trên [[ERP]]:** Đảm bảo hạch toán đúng giá thành (cao hơn đồng trần 6–10%) và không lẫn khi thu hồi."
        ),
        "key_terms": ["Solar Cable", "Tinned Copper", "E-beam", "Braiding", "Man-Machine Chart", "Jidoka", "SMED", "OLE", "ERP"],
        "doc_key": "cable_extrusion_wire_forensics",
        "lesson_id": "L1.3"
    },
]


SCENARIO_GROUPS = [
    "Tất cả 8 nhóm tình huống",
    "1. Kế Hoạch, Đơn Gấp & Ùn Tắc Dòng Chảy",
    "2. Xưởng Kéo Sợi, Ủ Đồng & Khuôn PCD",
    "3. Xưởng Bện, Ghép Lõi & Bọc Giáp",
    "4. Xưởng Đùn PVC / XLPE / LSZH / CCV",
    "5. Chất Lượng Trực Tuyến, Lab & Khiếu Nại",
    "6. Đóng Cuộn, Cut-Length, BOM & Phế Liệu",
    "7. Bảo Trì, Năng Lượng & An Toàn LOTO",
    "8. Con Người, Dữ Liệu MES & Văn Hóa Hiện Trường",
]


SCENARIOS = [
    # =========================================================================
    # NHÓM 1: KẾ HOẠCH, ĐƠN GẤP & ÙN TẮC DÒNG CHẢY (SC01 – SC05)
    # =========================================================================
    {
        "id": "SC01",
        "group": "1. Kế Hoạch, Đơn Gấp & Ùn Tắc Dòng Chảy",
        "station_id": "S00",
        "title": "Kinh doanh ép chen đơn gấp dây màu Trắng vào giữa ca máy đùn đang chạy màu Đen",
        "symptom": "Máy đùn số 2 đang chạy lô cáp màu Đen thì Kinh doanh gọi điện yêu cầu dừng gấp để chạy 3 km dây VC 2.5 màu Trắng giao trong chiều nay.",
        "impact": "Mất 50 phút đổi ngược màu Tối → Sáng + xả 26 kg nhựa [[Purging]] + phế dây đồng dính nhựa + làm trễ toàn bộ các đơn màu Đen phía sau.",
        "immediate_24h": "Không tranh cãi cảm tính — OE kiểm tra ngay tồn kho siêu thị thành phẩm xem có hàng sẵn giao tạm không, hoặc kiểm tra xem có máy đùn dự phòng khác đang chạy màu Sáng (Vàng/Xanh) để đẩy đơn sang mà không phá máy đang chạy Đen.",
        "rca": "Thiếu luật đóng băng lịch sản xuất (Frozen Horizon 48–72h), chưa có bảng chi phí ẩn đổi ngược màu (Changeover Cost) minh bạch giữa Kinh doanh và Sản xuất, và chưa lập siêu thị [[Kanban]] cho dây dân dụng nhóm AX.",
        "oe_solution": "1. Tính rõ bằng tiền: 1 lần chen đơn đổi ngược Đen → Trắng đốt mất ~1.8 triệu tiền nhựa/phế + 50 phút [[OEE]] máy cổ chai.\n2. Thiết lập Luật Bánh Xe Màu [[Color Sequencing]] cố định theo tuần (Thứ 2–3 Trắng/Vàng → Thứ 4–5 Xanh/Đỏ → Thứ 6–7 Đen) kèm cơ chế: chen ngang trong vùng đóng băng phải có chữ ký Giám đốc Nhà máy.\n3. Lập tồn kho an toàn [[Safety Stock]] siêu thị cho Top 10 mã dây VC bán chạy nhất.",
        "lock_in": "Ban hành [[SOP]] phối hợp [[S&OP]] / [[MPS]] giữa Kinh doanh – Kế hoạch – Sản xuất; theo dõi KPI 'Số lần phá lịch màu/tuần' trên bảng họp tuần Ban Giám đốc.",
        "key_terms": ["Color Sequencing", "Purging", "Campaign Scheduling", "Safety Stock", "Kanban", "S&OP", "MPS"],
        "doc_key": "smed",
        "lesson_id": "L3.3"
    },
    {
        "id": "SC02",
        "group": "1. Kế Hoạch, Đơn Gấp & Ùn Tắc Dòng Chảy",
        "station_id": "S00",
        "title": "Mùa cao điểm xây dựng, đơn hàng tăng vọt +35% làm Xưởng Đùn quá tải 122%",
        "symptom": "Phòng Kế hoạch báo tổng giờ yêu cầu tháng tới tại Xưởng Đùn là 1,240 giờ ròng trong khi 4 máy đùn ở [[OEE]] 65% chỉ chạy được tối đa 1,014 giờ (quá tải 122%, thiếu 226 giờ ròng!).",
        "impact": "Nguy cơ giao trễ hàng loạt dự án điện lực/đại lý (OTIF tụt xuống < 75%) hoặc phải xin mua máy đùn mới [[CAPEX]] nhiều tỷ đồng nhưng chờ 6 tháng mới về!",
        "immediate_24h": "Chạy nhanh mô hình [[RCCP]] tách tải theo từng cỡ cáp/máy đùn; phân loại đơn hàng nào là cổ chai thật sự, đơn hàng nào có thể chuyển đổi tuyến máy (Alternative Routing) hoặc chạy thêm ca Chủ nhật ngắn hạn.",
        "rca": "Theo Lý thuyết điểm nghẽn [[TOC]], Xưởng Đùn đang là [[Bottleneck]] nhưng mất tới 18% thời gian vào đổi mã [[SMED]] và 11% vào giảm tốc độ/dừng vặt — nghĩa là công suất 'ẩn' đang bị chôn ngay trong 4 máy hiện hữu!",
        "oe_solution": "Áp dụng 5 bước [[TOC]] (Khai thác cổ chai TRƯỚC KHI mua máy mới):\n1. Rút thời gian đổi màu/tiết diện bằng [[SMED]] + [[Color Sequencing]] (giải phóng ngay +95 giờ/tháng).\n2. Đẩy lịch ăn trưa luân phiên (Hot-seat) không tắt máy đùn (+48 giờ/tháng).\n3. Chuyển các mã dây nhỏ sang máy tốc độ cao hơn & tách đúng [[L/D Ratio]] (+55 giờ/tháng).\n4. Bảo trì [[PM Compliance]] 100% ngoài giờ cao điểm & chuyển bớt đơn không cốt lõi sang gia công tạm nếu vẫn thiếu +28 giờ.\n→ Tổng công suất giải phóng +198 đến +230 giờ/tháng với chi phí gần như 0 đồng [[CAPEX]]!",
        "lock_in": "Đưa bảng tải [[RCCP]] nhân [[OEE]] thực vào cuộc họp [[S&OP]] hàng tháng để cảnh báo thiếu tải sớm 6–8 tuần.",
        "key_terms": ["RCCP", "TOC", "Bottleneck", "OEE", "SMED", "CAPEX", "S&OP", "Lead Time"],
        "doc_key": "oe_field_execution_case_test",
        "lesson_id": "L5.3"
    },
    {
        "id": "SC03",
        "group": "1. Kế Hoạch, Đơn Gấp & Ùn Tắc Dòng Chảy",
        "station_id": "S03",
        "title": "Hàng trăm rulo đồng bện ùn tắc kín lối đi trước Xưởng Đùn trong khi Đóng Cuộn ngồi chờ",
        "symptom": "Đi [[Genba]] thấy 85 rulo bán thành phẩm chất đầy lối đi xe nâng giữa Xưởng Bện và Xưởng Đùn (có rulo nằm 5 ngày bắt đầu xỉn màu!), trong khi tổ Đóng Cuộn ở cuối xưởng lại thiếu hàng phải về sớm.",
        "impact": "Đọng vốn lưu động nhiều tỷ đồng đồng nguyên liệu trong [[WIP]], tăng nguy cơ tai nạn xe nâng, đồng bị oxy hóa đen và kéo dài [[Lead Time]] giao hàng.",
        "immediate_24h": "Kiểm đếm thực tế toàn bộ rulo WIP theo mã hàng, đối chiếu với lệnh ưu tiên đang chờ ở Đóng Cuộn để kéo đúng rulo cần giao gấp lên máy đùn trước.",
        "rca": "Nhà máy đang vận hành kiểu Đẩy (Push): Xưởng Kéo & Bện có công suất lớn hơn Xưởng Đùn và được chấm KPI theo 'tấn sản lượng đầu ra' → Càng chạy nhanh để lấy thành tích thì càng đổ núi WIP đè chết Xưởng Đùn!",
        "oe_solution": "1. Vẽ [[VSM]] chứng minh núi WIP không tạo thêm 1 đồng doanh thu nào mà làm tắc nghẽn dòng tiền.\n2. Thiết lập cơ chế [[Drum-Buffer-Rope]] & [[Pull System]]: Xưởng Đùn (cổ chai) là 'Trống' phát nhịp; kẻ đúng số ô sơn vàng [[Kanban]] trên sàn giữa Bện & Đùn (vd: tối đa 15 ô) — đầy ô thì Bện PHẢI chuyển sang chạy mã khác hoặc bảo trì [[5S]]/[[Jishu Hozen]].\n3. Sửa KPI Xưởng Bện từ 'tấn sản lượng tối đa' sang 'tỷ lệ tuân thủ lịch kéo của Xưởng Đùn (Schedule Adherence)'.",
        "lock_in": "Kiểm soát trực quan giới hạn trần WIP ([[Visual Management]]) ngay tại sàn xưởng trong kiểm tra phân tầng [[LPA]] hàng ngày.",
        "key_terms": ["WIP", "VSM", "Drum-Buffer-Rope", "Pull System", "Kanban", "Genba", "Lead Time", "Visual Management"],
        "doc_key": "lean_muda",
        "lesson_id": "L3.2"
    },
    {
        "id": "SC04",
        "group": "1. Kế Hoạch, Đơn Gấp & Ùn Tắc Dòng Chảy",
        "station_id": "S01",
        "title": "Hệ thống ERP báo tồn kho hạt nhựa XLPE còn 8 tấn nhưng ra kho thực tế chỉ còn 3 tấn",
        "symptom": "Kế hoạch phát lệnh chạy đơn hàng cáp CXV lớn vì thấy [[ERP]] báo còn 8 tấn hạt XLPE Silane, nhưng đến ca 2 Thủ kho báo hết sạch hạt nhựa — máy đùn cổ chai dừng chết 14 tiếng chờ mua gấp!",
        "impact": "Hụt 5 tấn nhựa ảo (~350 triệu), dừng máy cổ chai mất sản lượng, phải mua hàng gấp giá cao làm đội chi phí.",
        "immediate_24h": "Điều chuyển gấp hạt XLPE tương đương (đã qua IQC) hoặc đảo lịch sang chạy đơn PVC trong lúc chờ vật tư; tiến hành kiểm kê khẩn cấp toàn bộ mã nhựa nhóm A.",
        "rca": "1. Nhập xuất kho ghi sổ tay rồi cuối tuần mới nhập vào [[ERP]] (độ trễ dữ liệu).\n2. Xưởng lấy thêm bao nhựa bù cho phế [[Purging]]/[[Over-thickness]] mà không lập phiếu xuất bổ sung (do cấu hình Backflush trừ ảo theo [[BOM]] chuẩn!).\n3. Chưa có quy trình kiểm đếm luân phiên [[Cycle Counting]].",
        "oe_solution": "1. Cấm tuyệt đối xuất kho không phiếu/không quét Barcode — mọi bao nhựa ra khỏi kho phải quét ghi nhận tức thời vào [[ERP]]/[[MES]].\n2. Triển khai [[Cycle Counting]] theo phân nhóm [[ABC-XYZ]] (Nhóm A đồng/XLPE đếm hàng tuần, Nhóm B hàng tháng, Nhóm C hàng quý) giữ độ chính xác tồn kho RIA ≥ 98.5%.\n3. Tính lại điểm đặt hàng [[ROP]] & [[Safety Stock]] có tính đến biến động Lead Time giao hàng nhà cung cấp.",
        "lock_in": "Đưa KPI độ chính xác tồn kho (RIA ≥ 98.5%) vào đánh giá KPI Thủ kho & Kế hoạch; đối soát định kỳ phế thực tế vs xuất kho cuối mỗi ca.",
        "key_terms": ["ERP", "Cycle Counting", "ABC-XYZ", "Safety Stock", "ROP", "BOM", "SAP PP"],
        "doc_key": "bom_cost",
        "lesson_id": "L5.1"
    },
    {
        "id": "SC05",
        "group": "1. Kế Hoạch, Đơn Gấp & Ùn Tắc Dòng Chảy",
        "station_id": "S04",
        "title": "Phòng xông hơi XLPE Silane (Sauna) chờ gom mẻ làm Lead Time cáp CXV kéo dài 12 ngày",
        "symptom": "Khách hàng dự án phàn nàn đặt cáp CXV mất 12 ngày mới có hàng dù tổng thời gian máy chạy thực tế chỉ chưa tới 21 giờ (hiệu quả chuỗi PCE chỉ 7.3%!).",
        "impact": "Tồn kho dở dang [[WIP]] cực lớn trước phòng xông, chậm xoay vòng dòng tiền, dễ mất đơn hàng dự án cần gấp.",
        "immediate_24h": "Đi [[Genba]] đo thời gian nằm chờ thực tế của từng rulo lõi XLPE từ lúc rời máy đùn đến lúc vào và ra khỏi phòng xông Sauna.",
        "rca": "1. Xưởng có thói quen chờ gom đủ đầy 12 rulo lớn mới bật lò hơi xông 1 lần (rulo đầu tiên nằm chờ 36–48 giờ!).\n2. Cài chung 1 chế độ xông dư an toàn 10 giờ cho mọi cỡ cáp, kể cả lõi cách điện mỏng 0.7 mm vốn chỉ cần 4 giờ đã đạt [[Hot Set Test]]!",
        "oe_solution": "1. Phối hợp Phòng Lab chạy thử nghiệm [[DOE]] lấy mẫu [[Hot Set Test]] ở các mốc 4h – 6h – 8h theo 3 dải chiều dày cách điện (≤ 0.8mm, 0.9–1.2mm, ≥ 1.4mm).\n2. Thiết kế lịch xông cố định theo nhịp mỗi ca (không chờ đầy mới bật, hoặc ngăn vách lò xông thành 2 khoang nhỏ linh hoạt) kết hợp dùng thời gian xông tối ưu (4h / 6.5h / 9h).\n3. Kết quả thực tế: Cắt 52% lượng rulo WIP chờ xông, rút [[Lead Time]] cáp CXV từ 12 ngày xuống 4.5 ngày và tiết kiệm 18% nhiên liệu đốt lò hơi!",
        "lock_in": "Ban hành Bảng tra thời gian xông chuẩn theo chiều dày cách điện dán ngay cửa lò Sauna và theo dõi trên [[VSM]] hàng quý.",
        "key_terms": ["Silane", "XLPE", "Hot Set Test", "VSM", "WIP", "Lead Time", "DOE"],
        "doc_key": "lean_muda",
        "lesson_id": "L3.2"
    },

    # =========================================================================
    # NHÓM 2: XƯỞNG KÉO SỢI, Ủ ĐỒNG & KHUÔN PCD (SC06 – SC10)
    # =========================================================================
    {
        "id": "SC06",
        "group": "2. Xưởng Kéo Sợi, Ủ Đồng & Khuôn PCD",
        "station_id": "S02",
        "title": "Máy kéo thô RBD đứt sợi liên tục 8 lần/ca, xưởng và mua hàng đổ lỗi lẫn nhau",
        "symptom": "Máy kéo thô [[RBD]] đứt dây liên miên (mỗi lần dừng 18 phút xâu lại 11 khuôn, mất 750 kg sản lượng/lần!), xưởng đổ tại đồng Rod kém còn Mua hàng khẳng định giấy COA nhà cung cấp đạt chuẩn.",
        "impact": "[[OEE]] máy RBD rơi xuống dưới 55%, tạo hàng trăm kg đồng rối phế và gây thiếu sợi đồng cho toàn bộ Xưởng Bện phía sau.",
        "immediate_24h": "Yêu cầu công nhân KHÔNG vứt 2 đầu dây đứt — gắn thẻ ghi giờ/lô đồng/vị trí khuôn và thu gom 100% mẫu đầu gãy trong 48 giờ để soi kính hiển vi 30×.",
        "rca": "Áp dụng [[Wire Break Forensics]] phân loại 45 mẫu gãy theo [[Pareto]] 80/20: thực tế chỉ 15% là [[Cup-and-Cone]] (tạp chất đồng Rod), còn 48% có vết cháy hồ quang trên tang ủ [[Annealing]] và 27% gãy phẳng có bọt khí tại mối hàn [[Butt Welder]]!",
        "oe_solution": "1. Bảo trì đánh bóng ngay cổ góp & vòng tiếp xúc tang ủ [[Annealing]] loại bỏ hiện tượng đánh lửa hồ quang (giải quyết 48% sự cố!).\n2. Chuẩn hóa [[SOP]] hàn [[Butt Welder]] (vệ sinh đầu đồng bằng cồn, kiểm lực kẹp, ủ mối hàn 2 bước, test bẻ 90° đầu ca).\n3. Với 15% mẫu [[Cup-and-Cone]] có hạt tạp chất đen dưới kính hiển vi, lập hồ sơ bằng chứng ảnh gửi khiếu nại lô đồng Rod theo [[ASTM B49]].\n→ Số lần đứt sợi giảm từ 8 lần/ca xuống < 1.5 lần/ca (< 0.3 lần/tấn) chỉ sau 3 tuần!",
        "lock_in": "Treo Bảng mẫu nhận diện 6 hình thái đứt sợi ngay cạnh máy [[RBD]] và bắt buộc ghi mã hình thái đứt vào nhật ký [[MES]] / [[Downtime]].",
        "key_terms": ["RBD", "Wire Break Forensics", "Cup-and-Cone", "Annealing", "Butt Welder", "Pareto", "ASTM B49"],
        "doc_key": "cable_extrusion_wire_forensics",
        "lesson_id": "L4.4"
    },
    {
        "id": "SC07",
        "group": "2. Xưởng Kéo Sợi, Ủ Đồng & Khuôn PCD",
        "station_id": "S02",
        "title": "Máy kéo tinh Multi-wire 16 sợi liên tục đứt lặp đi lặp lại đúng sợi số 4 và số 9",
        "symptom": "Trên máy kéo đa sợi [[Multi-wire]] 16 đường dây, cứ chạy khoảng 20–30 phút lại đứt sợi số 4 hoặc số 9 làm cả 16 sợi phải dừng khẩn cấp cùng lúc!",
        "impact": "Hiệu suất máy kéo tinh tụt thê thảm (< 50%), tốn thời gian xâu dây & nối sợi cực lâu, làm chậm tiến độ cấp sợi cho Xưởng Bện [[Buncher]].",
        "immediate_24h": "Dừng lấy mẫu đo đường kính thực tế của cả 16 sợi sau từng cấp khuôn và kiểm tra kích thước lỗ khuôn [[PCD]] ở vị trí dây 4 & 9 tại Phòng Khuôn.",
        "rca": "Khi 1 khuôn ở dây số 4 bị hỏng trước đó, thợ bảo trì chỉ rút đại 1 khuôn mới keng thay lẻ vào giữa dàn 15 khuôn đã mòn +0.004mm! Vì 16 sợi chạy chung 1 trục kéo Capstan, sợi số 4 có độ giãn dài khác hẳn 15 sợi còn lại nên bị kéo căng vượt giới hạn rồi đứt liên hoàn!",
        "oe_solution": "1. Ban hành quy chuẩn tuyệt đối: Trên máy [[Multi-wire]] BẮT BUỘC thay đồng bộ cả bộ khuôn khớp kích thước (**Matched Die Set**, sai lệch giữa các khuôn cùng 1 hàng ≤ 0.002 mm).\n2. Đánh số quản lý bộ khuôn theo khay Kitting màu sắc tại Phòng Khuôn (Die Shop) kèm máy đo đường kính laser trước khi xuất xưởng.\n3. Kiểm tra thêm áp lực vòi phun [[Drawing Emulsion]] vào đúng khe dây 4 & 9 chống nghẹt cặn.",
        "lock_in": "Đưa kiểm tra 'Xác nhận Matched Die Set ≤ 0.002mm' vào phiếu giao nhận khuôn giữa Phòng Khuôn và Tổ Kéo tinh.",
        "key_terms": ["Multi-wire", "PCD", "Drawing Emulsion", "Kitting", "OEE"],
        "doc_key": "cable_extrusion_wire_forensics",
        "lesson_id": "L1.2"
    },
    {
        "id": "SC08",
        "group": "2. Xưởng Kéo Sợi, Ủ Đồng & Khuôn PCD",
        "station_id": "S02",
        "title": "Sợi đồng kéo ra bị cứng gãy khi bện ở Trạm 03 hoặc bị đen xỉn sau 24 giờ nằm kho",
        "symptom": "Xưởng Bện [[Buncher]] phản ánh cứ chạy đầu/cuối rulo đồng mới từ Xưởng Kéo là sợi bị cứng bung lò xo đứt liên tục; một số rulo khác để qua đêm bị ố nâu đen bề mặt.",
        "impact": "Phải hạ tốc độ máy bện -30%, cắt bỏ hàng chục mét sợi đầu/cuối rulo hoặc phải đưa rulo đi ủ lại trong lò chuông tốn điện & tăng phế.",
        "immediate_24h": "Cắt mẫu đầu–giữa–cuối rulo đo độ giãn dài [[Tensile]] (chuẩn phải ≥ 20–25%) và kiểm tra hệ thống hơi nước/khí bảo vệ + nhiệt độ nước làm mát trong ống ủ [[Annealing]].",
        "rca": "1. Đường cong đồng bộ điện áp ủ (Ramp Curve) trên [[PLC]] đáp ứng trễ 0.8 giây lúc máy tăng tốc/giảm tốc → Tạo ra 40m dây bị ủ non (cứng) ngay đầu & cuối mỗi rulo!\n2. Đường hơi nước bảo vệ chống oxy hóa bị hở gioăng lọt không khí vào ống ủ nóng 500°C và bộ thổi khô đầu ra yếu để nước đọng trên bề mặt đồng → Oxy hóa đen sợi sau 1 ngày!",
        "oe_solution": "1. Phối hợp Cơ Điện hiệu chỉnh lại hệ số bù trễ Ramp Curve điện áp ủ tỷ lệ chính xác theo bình phương tốc độ kéo trên [[PLC]].\n2. Thay gioăng kín ống hơi bảo vệ, kiểm tra chất lượng nước mềm/phụ gia chống oxy hóa trong bể làm nguội sau ủ và nâng cấp béc thổi khô Air Wipe trước khi cuốn lên [[Take-up]].\n3. Quấn màng PE chống ẩm bọc kín các rulo đồng thành phẩm nếu thời gian chờ sang Xưởng Bện > 12 giờ.",
        "lock_in": "Bổ sung test kiểm tra độ giãn dài đoạn đầu/cuối rulo vào [[Control Plan]] đầu ca máy kéo và kiểm tra áp suất hơi bảo vệ trong [[Jishu Hozen]].",
        "key_terms": ["Annealing", "PLC", "Tensile", "Take-up", "Control Plan", "Jishu Hozen"],
        "doc_key": "cable_mfg_machines",
        "lesson_id": "L1.2"
    },
    {
        "id": "SC09",
        "group": "2. Xưởng Kéo Sợi, Ủ Đồng & Khuôn PCD",
        "station_id": "S02",
        "title": "Đường kính sợi đồng kéo trôi dần lên +0.009mm gây âm định mức đồng Copper Give-away",
        "symptom": "Kế toán báo cuối quý Xưởng Kéo & Bện tiêu hao đồng vượt định mức [[BOM]] +2.1% (tương đương thất thoát ~5 tấn đồng ≈ 1.25 tỷ đồng/quý) dù tỷ lệ phế cân được tại thùng rác rất nhỏ!",
        "impact": "Chảy máu lợi nhuận âm thầm cực lớn — đồng nguyên chất bị 'biếu không' vào trong từng mét dây thành phẩm mà khách hàng không trả thêm tiền.",
        "immediate_24h": "Lấy ngẫu nhiên 30 mẫu sợi từ các máy kéo đo bằng Panme/Laser chính xác 0.001mm và đối chiếu điện trở 20°C trên cầu [[Kelvin Bridge]] so với trần [[IEC 60228]].",
        "rca": "Biểu đồ [[SPC]] Xbar-R phơi bày đường kính sợi đang trôi dần lên sát cận trên (+0.009mm) vì: (1) Không có giới hạn tấn đồng thay khuôn [[PCD]] (để khuôn mòn quá lâu mới tháo đi đánh bóng!), (2) Công nhân sợ rớt điện trở nên chủ động chọn khuôn hơi to hơn thiết kế +0.005mm cho 'an toàn'!",
        "oe_solution": "1. Thiết lập dự án [[Six Sigma]] [[DMAIC]] tối ưu [[Copper Give-away]]: Khảo sát % [[IACS]] thực tế của đồng Rod đầu vào (101.2% IACS) → Tính lại đường kính mục tiêu hợp pháp đạt [[IEC 60228]] với biên an toàn ≥ 3σ ([[Cpk]] ≥ 1.33).\n2. Khóa tuổi thọ khuôn [[PCD]] theo sản lượng tấn (vd: đạt 25 tấn hoặc đường kính chạm cận cảnh báo trên [[SPC]] là BẮT BUỘC tháo đi Re-polish!).\n3. Trình quy trình [[MOC / ECN]] được QA/QC & Giám đốc ký duyệt rồi cập nhật đồng bộ [[BOM]] trên [[SAP PP]].\n→ Kéo [[Copper Give-away]] từ +2.1% xuống +0.4%, thu hồi Hard Savings > 3 tỷ VNĐ/năm!",
        "lock_in": "Gắn biểu đồ [[SPC]] đo đường kính 2 giờ/lần (hoặc Laser online) vào [[Control Plan]] và chấm điểm tuân thủ trong [[LPA]].",
        "key_terms": ["Copper Give-away", "PCD", "IEC 60228", "IACS", "Kelvin Bridge", "SPC", "Cpk", "DMAIC", "MOC / ECN"],
        "doc_key": "cable_cost_capacity",
        "lesson_id": "L5.2"
    },
    {
        "id": "SC10",
        "group": "2. Xưởng Kéo Sợi, Ủ Đồng & Khuôn PCD",
        "station_id": "S02",
        "title": "Bể nhũ tương kéo sợi mùa hè bốc mùi, tụt pH và đóng cặn bít khuôn PCD",
        "symptom": "Vào tháng 6 nắng nóng Đà Nẵng, bể dung dịch [[Drawing Emulsion]] bốc mùi hôi thối, có lớp váng xanh đóng cặn quanh khuôn [[PCD]], tỷ lệ đứt sợi tăng gấp 3 và sợi đồng ra bị mờ xước.",
        "impact": "Hỏng sớm khuôn kim cương [[PCD]] đắt tiền, tăng mạnh lực kéo làm vọt tiền điện [[SEC]] kWh/tấn và giảm [[OEE]] toàn Xưởng Kéo.",
        "immediate_24h": "Đo ngay 5 thông số bể nhũ tương: Nồng độ (khúc xạ kế Refractometer), pH, độ dẫn điện nước (Conductivity), nhiệt độ bể và kiểm tra giấy lọc mạt đồng.",
        "rca": "1. Trời nóng bay hơi mạnh, công nhân lấy thẳng vòi nước máy cứng (chứa nhiều Canxi/Magie) châm bù mà quên châm dầu → Nồng độ tụt từ 5% xuống 1.8%, Canxi phản ứng với dầu tạo kết tủa xà phòng xanh bít khuôn!\n2. Nhiệt độ bể vượt 48°C tạo điều kiện vi khuẩn kỵ khí phát triển làm tụt pH xuống 7.1 gây thối dầu & ăn mòn đồng!",
        "oe_solution": "1. Xả vệ sinh diệt khuẩn toàn bộ bể, pha mới đúng chuẩn 4.5% (kéo tinh) / 10% (RBD) bằng 100% nước mềm khử ion (DI Water).\n2. Lắp vạch báo mức tự động + đường cấp nước DI riêng (khóa đường nước máy thường bằng [[Poka-Yoke]]!).\n3. Vệ sinh bộ trao đổi nhiệt làm mát bể giữ ổn định 35–42°C và lắp hệ thống sục khí nhẹ lúc nghỉ cuối tuần chống vi khuẩn kỵ khí.",
        "lock_in": "Đưa bảng đo 5 thông số bể nhũ tương (Nồng độ – pH – Độ dẫn – Nhiệt độ – Lọc) vào bảng [[Visual Management]] và [[Jishu Hozen]] đầu ca mỗi ngày.",
        "key_terms": ["Drawing Emulsion", "PCD", "SEC", "Poka-Yoke", "Jishu Hozen", "Visual Management"],
        "doc_key": "cable_mfg_machines",
        "lesson_id": "L1.2"
    },

    # =========================================================================
    # NHÓM 3: XƯỞNG BỆN, GHÉP LÕI & BỌC GIÁP (SC11 – SC15)
    # =========================================================================
    {
        "id": "SC11",
        "group": "3. Xưởng Bện, Ghép Lõi & Bọc Giáp",
        "station_id": "S03",
        "title": "Máy bện lồng cứng Rigid Strander mất 75 phút nạp 37 rulo mỗi lần đổi cỡ cáp",
        "symptom": "Mỗi khi chuyển từ bện cáp 95 mm² sang 185 mm², máy [[Rigid Strander]] dừng suốt 75 phút để công nhân tìm rulo, dùng cầu trục nhấc lắp từng cuộn vào các lồng và xâu sợi thủ công.",
        "impact": "Với 2 lần đổi cỡ/ngày, máy cổ chai của xưởng cáp lực mất toi 2.5 giờ/ngày (Availability giảm hơn 15%!).",
        "immediate_24h": "Quay video toàn bộ 75 phút nạp rulo bằng điện thoại và lập bảng tách từng thao tác theo giây (Bước 1–2 của [[SMED]]).",
        "rca": "Phân tích video phơi bày 45/75 phút (60%) là Thao tác Ngoài đang làm khi máy đứng im: đi tìm 37 rulo rải rác khắp xưởng (18p), chờ cầu trục bận cẩu khu khác (12p), kiểm tra thiếu rulo phải chạy sang Xưởng Kéo giục (10p), tìm kìm cắt & ống nối (5p)!",
        "oe_solution": "1. Áp dụng [[SMED]] + [[Kitting]]: Chuẩn bị đủ bộ 37 rulo có chiều dài bằng nhau đặt sẵn theo thứ tự lồng trên giá xe trượt bên cạnh máy TRƯỚC khi máy dừng 30 phút (cắt ngay 40 phút!).\n2. Thiết kế quy trình nạp song song 2 người kiểu F1 Pit-stop (1 người vận hành nâng rulo nạp lồng trước, 1 người xâu sợi & khóa chốt lồng sau) + áp dụng [[LOTO]] chuẩn 2 ổ khóa.\n3. Rút thời gian nạp lồng từ 75 phút xuống còn 24 phút (-68%), tăng ngay +1.7 giờ chạy máy mỗi ngày!",
        "lock_in": "Ban hành [[Standard Work]] nạp lồng 2 người dán ảnh trực quan [[OPL]] tại máy và kiểm tra tiến độ soạn Kitting trong [[LSW]] Tổ trưởng.",
        "key_terms": ["Rigid Strander", "SMED", "Kitting", "LOTO", "Standard Work", "OPL", "LSW"],
        "doc_key": "smed",
        "lesson_id": "L3.3"
    },
    {
        "id": "SC12",
        "group": "3. Xưởng Bện, Ghép Lõi & Bọc Giáp",
        "station_id": "S03",
        "title": "Máy bện Buncher dây mềm bị lỗi 'lồng chim' (Birdcaging) & sợi chùng lòi ra ngoài",
        "symptom": "Ruột đồng mềm Class 5 sau khi bện trên máy [[Buncher]] xuất hiện các đoạn sợi đồng phồng bung lên như lồng chim hoặc 1–2 sợi mảnh lòi ra khỏi bó — khi sang máy đùn Trạm 04 lập tức đâm thủng lớp PVC gây lỗi [[Spark Tester]]!",
        "impact": "Tỷ lệ phế dây mềm VCm vọt lên 4.5%, công nhân phải đứng canh máy sát sao (1 người chỉ đứng nổi 1–2 máy, [[OLE]] tụt thê thảm).",
        "immediate_24h": "Cách ly ngay các rulo ruột bị bung sợi không cho chạy vào máy đùn; kiểm tra lực căng phanh xả của toàn bộ giàn rulo [[Pay-off]] cấp vào máy Buncher đó.",
        "rca": "1. Phanh dây đai trên giàn [[Pay-off]] có cuộn mòn trơn (nhả dây lỏng chùng), có cuộn bó kẹt (căng quá mức) → Chênh lệch lực căng giữa các sợi làm sợi căng nằm chặt lõi giữa, còn sợi chùng bị đẩy phồng ra ngoài!\n2. Khuôn gom sợi (Closing Die) bị mòn rộng quá kích thước bó dây.",
        "oe_solution": "1. Bảo trì đồng bộ lại toàn bộ bộ hãm lực căng giàn xả [[Pay-off]] (dùng lực kế lò xo cân chỉnh đều nhau từng vị trí trong sai số ±5%).\n2. Thay khuôn gom sợi đúng đường kính chuẩn và kiểm tra rulo đồng đầu vào từ Trạm 02 không bị rối chéo lớp [[Take-up]].\n3. Gắn cảm biến quang/vòng chạm phát hiện sợi bung tự dừng [[Jidoka]] → Cho phép mở rộng mô hình [[Man-Machine Chart]] 1 công nhân đứng 4 máy an toàn!",
        "lock_in": "Đưa kiểm tra lực căng [[Pay-off]] và kích thước khuôn gom vào Checklist bảo trì [[PM Compliance]] hàng tuần.",
        "key_terms": ["Buncher", "Pay-off", "Take-up", "Spark Tester", "Jidoka", "Man-Machine Chart", "OLE"],
        "doc_key": "ole",
        "lesson_id": "L2.3"
    },
    {
        "id": "SC13",
        "group": "3. Xưởng Bện, Ghép Lõi & Bọc Giáp",
        "station_id": "S05",
        "title": "Ghép 4 lõi cáp lực trên Drum Twister bị lệch chiều dài 4 rulo gây cắt bỏ 165m lõi XLPE",
        "symptom": "Khi ghép cáp CXV 3×120+1×70 trên máy [[Drum Twister]], 4 rulo lõi từ Xưởng Đùn giao sang có chiều dài: Đỏ 1,050m, Vàng 1,020m, Xanh 995m, Đen 1,080m → Rulo Xanh hết trước tại mét 995 khiến 3 lõi kia dư bỏ tổng cộng 165m lõi đồng đã bọc XLPE!",
        "impact": "Một mét lõi đồng 120mm² bọc XLPE trị giá hàng trăm nghìn đồng — chỉ 1 mẻ ghép lệch chiều dài đốt mất vài chục triệu đồng phế phẩm đồng dính nhựa!",
        "immediate_24h": "Cân đo kiểm tra lại chiều dài thực tế các rulo đang chờ trước máy ghép; tạm ghép các rulo có chiều dài gần nhau nhất vào cùng 1 mẻ để giảm cắt bỏ.",
        "rca": "1. Bánh đo mét tại 2 máy đùn khác nhau (máy đùn pha và máy đùn trung tính) sai lệch hiệu chuẩn tới 3–5%!\n2. Công nhân đùn tự ý chạy dư thêm 'cho chắc khỏi thiếu' mà không khóa tự động dừng đúng số mét mục tiêu theo lệnh [[MES]] / [[ERP]].",
        "oe_solution": "1. Hiệu chuẩn đồng bộ toàn bộ bánh đo mét Encoder trên tất cả máy đùn về cùng sai số ≤ ±0.2%.\n2. Cài đặt tính năng tự động báo còi/dừng máy khi đạt đúng chiều dài lệnh trên [[HMI]] (vd: cùng dừng ở 1,010 m ± 3 m cho cả 4 lõi cùng đơn hàng).\n3. Ghép 4 rulo có cùng mã lệnh SX theo bộ [[Kitting]] trước khi đẩy vào [[Drum Twister]].\n→ Giảm phế lõi thừa cuối rulo từ ~5% xuống < 0.5%, tiết kiệm hàng trăm triệu đồng/năm!",
        "lock_in": "Gắn báo cáo theo dõi 'Độ lệch chiều dài giữa các lõi cùng bộ' trên [[Power BI]] và khóa kiểm chuẩn bánh đo mét vào lịch [[PM Compliance]].",
        "key_terms": ["Drum Twister", "XLPE", "Capstan", "HMI", "MES", "Kitting", "Scrap"],
        "doc_key": "cable_cost_capacity",
        "lesson_id": "L5.2"
    },
    {
        "id": "SC14",
        "group": "3. Xưởng Bện, Ghép Lõi & Bọc Giáp",
        "station_id": "S05",
        "title": "Bước xoắn Lay-up chỉnh quá ngắn làm âm đồng & nhựa +1.5% toàn bộ đơn hàng cáp nhiều lõi",
        "symptom": "Kiểm toán [[BOM]] cuối tháng cho thấy dòng cáp lực 4 lõi CXV liên tục bị âm vật tư đồng & XLPE thêm ~1.5% so với định mức chuẩn dù [[Copper Give-away]] và [[Over-thickness]] đều đã kiểm soát tốt!",
        "impact": "Đội giá thành sản xuất thầm lặng trên mọi km cáp nhiều lõi và giảm tốc độ máy ghép lõi (vì xoắn dày hơn nên kéo chậm hơn!).",
        "immediate_24h": "Đo trực tiếp bước xoắn (Lay Length — khoảng cách giữa 2 vòng xoắn cùng 1 lõi) bằng thước mét ngay trên máy [[Drum Twister]] & [[Rigid Strander]] so sánh với bản vẽ công nghệ.",
        "rca": "Công nhân cài nhầm tỷ số bánh răng/tốc độ quay lồng làm bước xoắn thực tế ngắn chỉ 300 mm (thay vì chuẩn thiết kế 420 mm) → Hệ số xoắn [[Lay-up Factor]] nhảy vọt từ 1.016 lên 1.031 (+1.51% cả đồng lẫn nhựa trên từng mét cáp!), đồng thời làm máy chạy chậm đi 28%!",
        "oe_solution": "1. Kiểm tra lại toàn bộ bảng tra bước xoắn chuẩn trên mọi máy [[Rigid Strander]] & [[Drum Twister]], tối ưu bước xoắn về sát cận dài tiêu chuẩn [[IEC 60502]] cho phép (vừa chắc gọn vừa tiết kiệm vật liệu tối đa!).\n2. Nạp cứng tỷ số tốc độ quay/tốc độ kéo vào thư viện Recipe tự động trên [[HMI]] khóa mật khẩu để công nhân không chỉnh tay sai lệch.\n3. Đồng bộ hệ số [[Lay-up Factor]] tính theo hình học 3D chuẩn lên cây [[BOM]] của [[SAP PP]].",
        "lock_in": "Thêm hạng mục đo kiểm tra bước xoắn đầu ca vào [[Control Plan]] và kiểm tra chéo trong [[LPA]].",
        "key_terms": ["Lay-up Factor", "Drum Twister", "Rigid Strander", "BOM", "IEC 60502", "HMI", "Control Plan"],
        "doc_key": "cable_cost_capacity",
        "lesson_id": "L5.2"
    },
    {
        "id": "SC15",
        "group": "3. Xưởng Bện, Ghép Lõi & Bọc Giáp",
        "station_id": "S05",
        "title": "Máy quấn giáp DSTA dừng hàn băng thép 4 lần/rulo & dàn máy Braiding chạy quá chậm",
        "symptom": "Đơn hàng cáp ngầm giáp thép [[DSTA]] và cáp điều khiển chống nhiễu [[Braiding]] luôn bị trễ giao hàng ở Trạm 05 dù Xưởng Đùn phía trước giao lõi rất sớm.",
        "impact": "Trạm 05 trở thành điểm nghẽn phụ bất ngờ làm chậm OTIF toàn dự án và tốn nhiều nhân công trực máy.",
        "immediate_24h": "Chạy bấm giờ [[Time Study]] trên máy quấn giáp DSTA (đếm số lần dừng hàn băng) và đo thực tế mật độ che phủ lưới quang học (Optical Coverage) trên dàn máy [[Braiding]].",
        "rca": "1. Máy giáp [[DSTA]] đang mua cuộn băng thép dạng bánh nhỏ (Pad Coil chỉ 400m) nên 1 rulo cáp 1,600m phải dừng hàn băng 4 lần (mất 60 phút/rulo!).\n2. Máy [[Braiding]] đang cài bước đan dày tạo mật độ phủ 93% (chuẩn chỉ yêu cầu ≥ 85%) làm tốc độ tuyến tính chậm mất -22% và tốn dư +14% đồng mạ thiếc [[Tinned Copper]], lại quấn các suốt Bobbin dài ngắn lệch nhau gây dừng thay lẻ liên tục!",
        "oe_solution": "1. Phối hợp Mua hàng chuyển sang cuộn băng thép quấn chéo (Traverse Wound Coil dài 2,500m) → Giảm 80% số lần dừng hàn, nâng [[OEE]] máy DSTA từ 58% lên 74%.\n2. Chỉnh lại bước đan máy [[Braiding]] về mục tiêu 87% (giải phóng ngay +22% công suất cổ chai & tiết kiệm > 300 triệu tiền đồng mạ thiếc/năm!).\n3. Quấn đồng bộ chiều dài 100% suốt Bobbin bằng nhau + lắp cảm biến đứt sợi [[Jidoka]] triển khai [[Man-Machine Chart]] 1 thợ quản 6–8 máy Braiding!",
        "lock_in": "Chuẩn hóa quy cách mua băng thép 2,500m trên [[ERP]] và treo bảng chuẩn góc đan + quy trình thay khay Bobbin đồng bộ tại máy.",
        "key_terms": ["DSTA", "Braiding", "Tinned Copper", "Time Study", "OEE", "Jidoka", "Man-Machine Chart"],
        "doc_key": "cable_extrusion_wire_forensics",
        "lesson_id": "L1.3"
    },

    # =========================================================================
    # NHÓM 4: XƯỞNG ĐÙN PVC / XLPE / LSZH / CCV (SC16 – SC20)
    # =========================================================================
    {
        "id": "SC16",
        "group": "4. Xưởng Đùn PVC / XLPE / LSZH / CCV",
        "station_id": "S04",
        "title": "Đổi màu nhựa & đổi tiết diện trên máy đùn mất 55 phút và xả 25 kg nhựa phế",
        "symptom": "Mỗi ca máy đùn dây dân dụng có 2–3 lần đổi màu/tiết diện, mỗi lần dừng 45–60 phút (chiếm 20–25% thời gian ca!) và thải ra đống nhựa xả 25 kg + 80m dây đồng dính nhựa.",
        "impact": "Thủ phạm số 1 kéo tụt [[OEE]] Availability xưởng Đùn xuống dưới 65% và đội cao chi phí phế liệu.",
        "immediate_24h": "Chọn 1 máy đùn cổ chai làm Pilot, quay video trọn vẹn 1 ca đổi mã từ mét dây đạt cuối cùng của lô A đến mét dây đạt đầu tiên của lô B.",
        "rca": "Hơn 55% thời gian dừng là lãng phí thuần túy: máy dừng rồi mới đi kho lấy bao nhựa/bộ Chày–Cối, chờ 20 phút nung nóng bộ khuôn nguội mới lắp vào, vặn tay 4 con ốc lấy tâm trên đầu [[Crosshead]] cũ và xả tẩy bằng nhựa thường thay vì [[Purging]] Compound.",
        "oe_solution": "Tổ chức Kaizen Blitz 5 ngày triển khai trọn bộ [[SMED]] 4 bước:\n1. Tách Thao tác Ngoài (tốn 0 đồng): Soạn sẵn bao nhựa, xe đồ nghề [[5S]] Shadow Board, tủ sấy nóng sẵn bộ Chày–Cối ở 160°C trước khi dừng máy → Giảm ngay từ 55p xuống 30p!\n2. Chuyển sang đầu [[Crosshead]] tự định tâm + nạp Recipe tự động trên [[HMI]] + dùng 2.5 kg hạt [[Purging]] Compound khi đổi màu tối → Rút xuống còn 12–14 phút (-76%) và nhựa xả giảm từ 25 kg xuống 6 kg!\n3. Xếp lịch [[Color Sequencing]] Sáng → Tối giảm 70% số lần xả nặng.",
        "lock_in": "Khóa bằng [[Standard Work]] đổi mã 12 phút, kiểm định [[2-Sample t-test]] (p < 0.05) chứng minh hiệu quả 30 ngày Trước–Sau và kiểm tra tuân thủ hàng ngày trong [[LSW]] Tổ trưởng.",
        "key_terms": ["SMED", "Crosshead", "Purging", "Color Sequencing", "5S", "HMI", "2-Sample t-test", "LSW"],
        "doc_key": "smed",
        "lesson_id": "L3.3"
    },
    {
        "id": "SC17",
        "group": "4. Xưởng Đùn PVC / XLPE / LSZH / CCV",
        "station_id": "S04",
        "title": "Đường kính vỏ cáp dao động hình sin (Surging) buộc công nhân bọc dày +12% Over-thickness",
        "symptom": "Số đo trên [[Laser Gauge]] cứ nhảy lên xuống ±0.06 mm đều đặn theo chu kỳ 12 giây; sợ rớt t_min theo [[IEC 60502]], công nhân vặn tăng chiều dày trung bình lên +12% so với chuẩn!",
        "impact": "Lãng phí hàng trăm triệu đồng hạt nhựa mỗi năm trên mỗi dây chuyền đùn và năng lực quá trình [[Cpk]] tụt xuống < 0.90.",
        "immediate_24h": "Xuất log đồ thị [[Melt Pressure]] và nhiệt độ 5 vùng nòng từ [[SCADA]]/[[HMI]] trong cùng khung giờ xảy ra dao động đường kính để so sánh pha dao động.",
        "rca": "Đồ thị [[Melt Pressure]] dao động sóng sin 195 ↔ 228 bar đúng nhịp 12 giây trùng khớp 100% dao động đường kính! Kiểm tra hiện trường phát hiện nhiệt độ vùng cấp liệu Zone 1 bị cài quá cao (155°C thay vì 135°C) làm hạt nhựa chảy dính bết vào cổ trục vít gây trượt cấp liệu chu kỳ (Feed Surging) + lưới lọc [[Screen Pack]] đã chạy quá hạn sắp tắc!",
        "oe_solution": "1. Hạ nhiệt độ Zone 1 về đúng 135°C, mở thông nước làm mát cổ phễu (Hopper Throat Cooling) và thay bộ lưới [[Screen Pack]] sạch → [[Melt Pressure]] phẳng lặng ở 210 ± 2 bar!\n2. Kích hoạt chế độ điều khiển vòng kín [[Laser Gauge]] Closed-loop liên động [[Capstan]] kéo độ lệch chuẩn σ đường kính từ 0.055 mm xuống 0.018 mm ([[Cpk]] nhảy từ 0.89 lên 1.65!).\n3. Sau khi σ đã thu hẹp ổn định 2 tuần, mới mở phiếu [[MOC / ECN]] dịch tâm chiều dày xuống sát t_nom (giảm 9.5% tiêu hao nhựa an toàn 100%!).",
        "lock_in": "Cài cảnh báo ngưỡng dao động [[Melt Pressure]] (> ±5 bar) và ngưỡng áp suất thay [[Screen Pack]] (250 bar) tự động trên [[SCADA]] / [[MES]].",
        "key_terms": ["Over-thickness", "Melt Pressure", "Laser Gauge", "Screen Pack", "Cpk", "IEC 60502", "SCADA", "MOC / ECN"],
        "doc_key": "cable_extrusion_wire_forensics",
        "lesson_id": "L4.4"
    },
    {
        "id": "SC18",
        "group": "4. Xưởng Đùn PVC / XLPE / LSZH / CCV",
        "station_id": "S04",
        "title": "Đẩy tốc độ đùn cáp XLPE / ABC lên cao thì bề mặt bị sần nhám da cá mập (Sharkskin)",
        "symptom": "Để đáp ứng đơn hàng EVN, xưởng tăng tốc độ đùn lõi XLPE cáp [[ABC Cable]] từ 110 lên 135 m/phút thì vỏ cách điện xuất hiện gợn nhăn mờ sần đều khắp chu vi — công nhân định hạ tốc độ về lại 100 m/phút.",
        "impact": "Mất ngay 20–25% công suất máy đùn cổ chai ([[OEE]] Performance giảm mạnh) hoặc bị QA trả lại vì lỗi ngoại quan.",
        "immediate_24h": "Soi bề mặt lỗi dưới kính lúp phân biệt rõ: vân nhăn đều vuông góc chiều chạy (đích thị [[Sharkskin]] do ứng suất trượt khuôn) — KHÔNG phải lỗ rỗ rải rác (ẩm) hay hạt lợn cợn (cháy Scorch).",
        "rca": "Ở tốc độ 135 m/phút, độ nhớt cao của nhựa XLPE khiến ứng suất cắt tại mép thoát Cối đùn vượt ngưỡng tới hạn (> 0.12 MPa), gây hiện tượng trượt–dính liên tục (Stick-Slip) xé rách bề mặt nhựa nóng chảy.",
        "oe_solution": "Xử lý đúng cơ chế vật lý để GIỮ TỐC ĐỘ CAO thay vì đầu hàng giảm tốc:\n1. Tăng nhẹ riêng nhiệt độ vùng Đầu khuôn Die (+12 đến +15°C: từ 190°C → 205°C) để giảm độ nhớt cục bộ ngay tại thành khuôn mà không làm cháy nhựa trong nòng.\n2. Nới nhẹ khe hở Cối (trong giới hạn [[DDR]] an toàn) dùng Cối có vùng dẫn hướng trơn mượt hơn.\n3. Phối hợp Kỹ thuật bổ sung 0.5% phụ gia trợ gia công PPA tạo màng trượt siêu mỏng trong lòng khuôn.\n→ Vỏ cáp bóng mịn ở đúng 135 m/phút (+22.7% năng suất!).",
        "lock_in": "Lưu thông số nhiệt độ Die mới + mã bộ Cối vào Recipe chuẩn trên [[HMI]] và cập nhật [[Control Plan]] dòng cáp ABC.",
        "key_terms": ["Sharkskin", "ABC Cable", "XLPE", "DDR", "OEE", "HMI", "Control Plan"],
        "doc_key": "cable_extrusion_wire_forensics",
        "lesson_id": "L4.4"
    },
    {
        "id": "SC19",
        "group": "4. Xưởng Đùn PVC / XLPE / LSZH / CCV",
        "station_id": "S06",
        "title": "Đùn vỏ cáp chống cháy LSZH bị nổ bọt rỗ khí và đóng cặn Die Drool phải dừng cạo 6 lần/ca",
        "symptom": "Chạy đơn hàng cáp [[LSZH]] cho dự án bệnh viện, bề mặt vỏ nổi bọt khí li ti rớt [[Spark Tester]], đồng thời miệng khuôn Cối đóng cục cặn [[Die Drool]] liên tục buộc thợ dừng máy cạo 6 lần/ca (mất 35 phút/ca!).",
        "impact": "Tỷ lệ phế cáp LSZH đắt tiền vọt lên 7.5%, trễ tiến độ công trình trọng điểm và nguy cơ xước hỏng miệng khuôn Cối.",
        "immediate_24h": "Kiểm tra độ ẩm hạt LSZH trước khi vào phễu, đo nhiệt độ thực của dòng nhựa nóng chảy (Melt Temp) ngay đầu khuôn bằng súng/que đo và thu hồi dao sắt công nhân đang dùng cạo khuôn!",
        "rca": "1. Hạt nhựa [[LSZH]] hút ẩm mạnh mùa mưa Đà Nẵng nhưng không được sấy kỹ qua [[Hopper Dryer]].\n2. Xưởng đang cho chạy LSZH trên máy dùng trục vít tỷ số nén cao của PVC & tốc độ quay vít quá nhanh → Nhiệt ma sát làm Melt Temp vượt 180°C khiến bột khoáng ATH phân hủy giải phóng hơi nước gây rỗ khí!\n3. Công nhân dùng dao sắt cạo [[Die Drool]] làm xước rỗ mép khuôn tạo ổ bám cặn nặng hơn + dùng sai bộ Cối có [[DDR]] 2.6 (quá cao so với ngưỡng 1.1–1.6 của LSZH!).",
        "oe_solution": "1. Chuyển toàn bộ mã [[LSZH]] sang máy có trục vít nén thấp (~1.2:1), sấy bắt buộc bằng [[Hopper Dryer]] 70°C × 3h (dùng phễu sấy di động làm External [[SMED]]), khống chế Melt Temp ≤ 165°C.\n2. Đánh bóng mạ Chrome gương lòng Cối, vát nhẹ mép thoát 30°, đổi đúng bộ Chày–Cối có [[DDR]] = 1.35 và cấp 100% dao cạo bằng ĐỒNG THAU (Brass Scraper).\n→ Phế rỗ khí giảm từ 7.5% xuống 0.6%, tốc độ đùn tăng +22% và chạy liên tục > 8 giờ không phải dừng cạo [[Die Drool]]!",
        "lock_in": "Tách Routing tốc độ & máy chuyên dụng cho [[LSZH]] trên [[SAP PP]]; đưa kiểm tra độ ẩm & dao đồng thau vào [[LPA]].",
        "key_terms": ["LSZH", "Die Drool", "Hopper Dryer", "DDR", "L/D Ratio", "Spark Tester", "SMED", "LPA"],
        "doc_key": "cable_extrusion_wire_forensics",
        "lesson_id": "L4.4"
    },
    {
        "id": "SC20",
        "group": "4. Xưởng Đùn PVC / XLPE / LSZH / CCV",
        "station_id": "S06",
        "title": "Trưa nắng Đà Nẵng 13h–16h nước máng làm mát nóng 34°C buộc hạ tốc độ máy đùn -20%",
        "symptom": "Dữ liệu [[OEE]] theo giờ cho thấy máy đùn vỏ cáp lực chạy đủ 100% tốc độ vào ca đêm và sáng sớm, nhưng cứ từ 13:00 đến 16:00 chiều lại giảm tốc -20% và vỏ cáp bị trầy xước bết dính khi cuộn lên rulo.",
        "impact": "Mất đều đặn 3 giờ chạy giảm tốc mỗi ngày vào suốt 5 tháng mùa nóng miền Trung (thiệt hại hàng chục km sản lượng/tháng).",
        "immediate_24h": "Xuất dữ liệu lịch sử Historian từ [[SCADA]] (hoặc đo nhiệt độ nước máng [[Cooling Trough]] mỗi giờ suốt 3 ngày) vẽ biểu đồ phân tán [[Scatter]] so với tốc độ máy đùn và tỷ lệ lỗi trầy vỏ.",
        "rca": "Biểu đồ [[Scatter]] chứng minh tương quan cực mạnh (r = +0.86, p < 0.001): lúc nắng gắt buổi trưa, tháp giải nhiệt bị bám rong rêu + béc phun nước máng nghẹt cặn vôi khiến nhiệt độ nước máng vọt từ 24°C lên 34°C → Vỏ cáp ra khỏi máng vẫn nóng 58°C chưa kịp đông cứng nên công nhân buộc phải giảm tốc độ đùn!",
        "oe_solution": "1. Vệ sinh tẩy cáu cặn vôi toàn bộ béc phun máng [[Cooling Trough]] & giàn tản nhiệt tháp giải nhiệt/Chiller.\n2. Lắp vách ngăn đảo dòng nước ngược chiều (Counter-flow) nâng hiệu suất truyền nhiệt và bổ sung thêm 4 mét máng phụ có làm mát Chiller giữ nhiệt độ nước ổn định ≤ 24°C cả lúc trưa nắng.\n3. Phối hợp gắn biến tần [[VFD]] cho bơm tuần hoàn nước để tự động chạy mạnh buổi trưa và giảm tốc tiết kiệm 35% điện vào ca đêm mát!\n→ Khôi phục 100% tốc độ đùn cả 3 ca (+18% sản lượng khung giờ chiều) và hoàn vốn [[Payback]] < 8 tháng!",
        "lock_in": "Gắn cảm biến nhiệt độ nước máng lên [[SCADA]] cài ngưỡng cảnh báo Alarm > 27°C và lịch vệ sinh tháp giải nhiệt định kỳ trong [[TPM]].",
        "key_terms": ["Cooling Trough", "Scatter", "SCADA", "VFD", "OEE", "Payback", "TPM"],
        "doc_key": "oee",
        "lesson_id": "L2.1"
    },
]


SCENARIOS.extend([
    # =========================================================================
    # NHÓM 5: CHẤT LƯỢNG TRỰC TUYẾN, LAB & KHIẾU NẠI KHÁCH HÀNG (SC21 – SC25)
    # =========================================================================
    {
        "id": "SC21",
        "group": "5. Chất Lượng Trực Tuyến, Lab & Khiếu Nại",
        "station_id": "S06",
        "title": "Spark Tester báo lỗi thủng lỗ kim đột biến 15 lần trên 1 rulo dây dân dụng",
        "symptom": "Đang đùn dây VC 2.5mm², màn hình [[Spark Tester]] liên tục nhảy số báo 15 lỗi phóng điện trong vòng 3,000m nhưng công nhân vẫn cố cho chạy hết rulo rồi mới dừng kiểm tra!",
        "impact": "Cả rulo 3,000m bị đánh dấu lỗi chi chít không cắt nổi thành khoanh 100m đạt chuẩn → Phế đồng dính nhựa hàng chục kg và nguy cơ lọt dây thủng cách điện ra thị trường!",
        "immediate_24h": "Cách ly ngay rulo lỗi (treo thẻ Đỏ NCR), kiểm tra tiếp địa nối đất (Grounding) của đầu xả [[Pay-off]] & test mẫu lỗ kim chuẩn trên [[Spark Tester]]; kiểm tra xem bộ thổi khô Air Wipe cuối máng nước có bị nước bắn vào đầu bi Spark gây báo giả không.",
        "rca": "Sau khi loại trừ báo giả do nước đọng, cắt soi kính hiển vi 5 điểm thủng thấy: 3 điểm do hạt tạp chất cháy đen (rách lưới [[Screen Pack]] vì công nhân tự ý bỏ bớt tấm lưới mịn 120 Mesh!), 2 điểm do bọt ẩm hạt nhựa [[PVC]] chưa sấy và máy không có liên động tự dừng [[Jidoka]] khi vượt ngưỡng lỗi!",
        "oe_solution": "1. Khôi phục chuẩn bộ lưới lọc 40/80/120/40 Mesh trên [[Screen Pack]] và cấm tuyệt đối bỏ bớt lưới.\n2. Tích hợp [[Jidoka]] nối tín hiệu xung đếm lỗi từ [[Spark Tester]] về [[PLC]]/[[MES]]: nếu trong 500m dây xuất hiện ≥ 2 lỗi Spark liên tiếp → Máy TỰ ĐỘNG dừng ngay & bật đèn [[Andon]] Đỏ!\n3. Kiểm tra và nâng cấp bộ thổi khô Air Wipe trước Spark Tester để triệt tiêu 100% lỗi báo giả do nước đọng.",
        "lock_in": "Bổ sung test thanh lỗ kim chuẩn (Fault Simulator) + kiểm tra dây tiếp địa đầu ca vào [[Control Plan]] và chấm điểm bắt buộc trong [[LPA]].",
        "key_terms": ["Spark Tester", "Jidoka", "Andon", "Screen Pack", "Pay-off", "PLC", "Control Plan", "LPA"],
        "doc_key": "cable_mfg_machines",
        "lesson_id": "L1.4"
    },
    {
        "id": "SC22",
        "group": "5. Chất Lượng Trực Tuyến, Lab & Khiếu Nại",
        "station_id": "S06",
        "title": "Máy in phun vỏ cáp hết mực lúc 2h sáng, chạy hổng 10 km dây không chữ thương hiệu",
        "symptom": "Vào 2 giờ sáng ca đêm, đầu in phun chữ lên vỏ dây hết mực/tắc vòi phun nhưng công nhân đang bận thay rulo ở đầu máy không phát hiện → Sáng ra phát hiện 10 km dây trơn bóng không có chữ CADIVI!",
        "impact": "Không được phép xuất bán theo quy chuẩn [[QCVN 4]] — phải mang chạy in lại chậm tốn nhân công hoặc tuốt bỏ gây thiệt hại hàng chục triệu đồng.",
        "immediate_24h": "Khoanh vùng toàn bộ các rulo sản xuất trong ca 3, tách riêng phần dây không có chữ để đánh giá phương án in lại trên máy sang cuộn (Rewinder) hay xử lý thu hồi.",
        "rca": "Chỉ dựa vào 'sự chú ý quan sát bằng mắt của con người' ở ca đêm lúc 2–4h sáng (lúc sinh học con người mệt mỏi nhất!) mà thiếu hoàn toàn cơ chế chống sai lỗi [[Poka-Yoke]].",
        "oe_solution": "1. Lắp cảm biến quang học tương phản (Contrast/Vision Sensor) đặt cách đầu in 1 mét nối về [[PLC]]: nếu sau 5 mét dây chạy qua mà không đọc thấy nhịp vạch chữ in → Còi hú, bật đèn [[Andon]] và tự động dừng máy!\n2. Gắn thêm cảnh báo mức bình mực thấp 15% trên màn hình [[HMI]] đầu máy.\n3. Chi phí lắp đặt chỉ ~8 triệu đồng, triệt tiêu 100% lỗi mất chữ in mãi mãi ([[Payback]] ngay từ vụ đầu tiên tránh được!).",
        "lock_in": "Đưa kiểm tra cảm biến đọc chữ in vào bảng khởi động máy đầu ca ([[Standard Work]]) và bảo trì vệ sinh đầu in định kỳ.",
        "key_terms": ["Poka-Yoke", "QCVN 4", "PLC", "Andon", "HMI", "Payback", "Standard Work"],
        "doc_key": "lean_muda",
        "lesson_id": "L3.1"
    },
    {
        "id": "SC23",
        "group": "5. Chất Lượng Trực Tuyến, Lab & Khiếu Nại",
        "station_id": "S07",
        "title": "Lô cáp lực XLPE Silane rớt phép thử Hot Set Test (200°C) sau khi đã xông hơi 8 tiếng",
        "symptom": "Phòng Lab báo mẫu cắt từ 4 rulo cáp CXV 3×95 sau khi xông hơi 8 giờ bị kéo giãn 210% (vượt trần ≤ 175% của [[Hot Set Test]]), có mẫu đứt luôn trong tủ 200°C!",
        "impact": "Tắc 4 rulo cáp lực trị giá hơn 800 triệu đồng không được phép xuất xưởng, nguy cơ trễ hạn hợp đồng dự án lớn.",
        "immediate_24h": "Giữ cách ly toàn bộ 4 rulo, lấy thêm mẫu ở đầu/cuối rulo khác cùng mẻ chạy lại [[Hot Set Test]] và kiểm tra ngay log nhiệt độ phòng xông Sauna + log định lượng phễu xúc tác Catalyst của máy đùn.",
        "rca": "Dùng [[5 Whys]] & [[Ishikawa]] tách 2 nguyên nhân gốc có thể: (A) Thiếu độ ẩm/nhiệt độ phòng xông Sauna bị tụt xuống 58°C do hỏng van bẫy hơi (có thể cứu được bằng cách xông bù thêm 6h!) vs (B) Công nhân quên bật bộ định lượng 5% hạt xúc tác Catalyst [[Silane]] (hoặc phễu Catalyst bị tắc nghẽn) lúc đùn → Hạt nhựa hoàn toàn không khâu mạch được (bắt buộc xử lý loại bỏ!).",
        "oe_solution": "1. Nếu nguyên nhân do van hơi Sauna: sửa van, đưa 4 rulo xông bổ sung đủ 85°C × 6h rồi test lại [[Hot Set Test]] đạt 100% (cứu trọn 800 triệu!).\n2. Nếu nguyên nhân do thiếu Catalyst: lắp ngay cảm biến lưu lượng/báo cạn phễu Catalyst nối liên động [[Poka-Yoke]] với [[PLC]] máy đùn (phễu Catalyst ngừng quay hoặc cạn → máy đùn KHÔNG thể chạy!).\n3. Gắn cảm biến nhiệt độ & độ ẩm tự ghi đồ thị phòng Sauna lên [[SCADA]].",
        "lock_in": "Cập nhật [[PFMEA]] nâng mức kiểm soát phát hiện thiếu Catalyst và bắt buộc kiểm tra đối chiếu kg Catalyst tiêu thụ vs kg nhựa nền cuối mỗi ca (tỷ lệ chuẩn 5:95).",
        "key_terms": ["Hot Set Test", "Silane", "XLPE", "5 Whys", "Ishikawa", "Poka-Yoke", "PFMEA", "SCADA"],
        "doc_key": "cable_mfg_machines",
        "lesson_id": "L4.5"
    },
    {
        "id": "SC24",
        "group": "5. Chất Lượng Trực Tuyến, Lab & Khiếu Nại",
        "station_id": "S07",
        "title": "Cáp trung thế 24kV rớt bài thử Phóng điện cục bộ Partial Discharge (14 pC > chuẩn 5 pC)",
        "symptom": "Trong phòng lồng Faraday, cuộn cáp trung thế 24kV dài 500m đo được phóng điện cục bộ [[Partial Discharge]] lên tới 14 pC tại điện áp 1.73 U0 (rớt xa chuẩn ≤ 5 pC theo [[IEC 60502]]-2!).",
        "impact": "Một rulo cáp trung thế hỏng thiệt hại vài trăm triệu đồng và uy tín nghiêm trọng nếu lọt ra lưới điện ngầm.",
        "immediate_24h": "Dùng thiết bị định vị phản xạ xung (TDR) xác định chính xác vị trí điểm phóng điện nằm tại mét thứ 420 trên rulo 500m; truy ngược ngay dữ liệu lịch sử dây chuyền [[CCV]] trên [[MES]] / [[SCADA]] đúng thời điểm chạy qua mét 420!",
        "rca": "Log [[SCADA]] tại đúng thời điểm chạy mét 420 cho thấy áp suất khí Nitơ trong ống lưu hóa [[CCV]] bị sụt đột ngột từ 12.0 bar xuống 7.5 bar trong 20 giây do van điều áp gặp sự cố → Tạo vi bọt khí (Micro-voids) bên trong lớp cách điện XLPE tại đúng đoạn mét 410–430!",
        "oe_solution": "1. Cắt bỏ đúng đoạn 30m lỗi (mét 405–435), thử lại [[Partial Discharge]] đoạn 400m còn lại đạt 1.2 pC (≤ 5 pC) — cứu được 80% giá trị rulo cáp!\n2. Phối hợp Cơ Điện bảo trì/lắp van điều áp Nitơ dự phòng song song và tích hợp cảnh báo tự đánh dấu vị trí mét trên [[MES]] ngay khi áp suất Nitơ sụt dưới 10.5 bar.\n3. Kiểm toán lại kỷ luật phòng sạch (Cleanroom) nạp hạt nhựa XLPE Peroxide tránh bụi tạp chất.",
        "lock_in": "Lập quy trình [[8D]] đóng triệt để sự cố, đưa kiểm định van áp suất khí Nitơ vào lịch [[CBM / PdM]] ưu tiên bậc 1 của dây chuyền [[CCV]].",
        "key_terms": ["Partial Discharge", "CCV", "IEC 60502", "MES", "SCADA", "8D", "CBM / PdM"],
        "doc_key": "cable_mfg_machines",
        "lesson_id": "L4.5"
    },
    {
        "id": "SC25",
        "group": "5. Chất Lượng Trực Tuyến, Lab & Khiếu Nại",
        "station_id": "S07",
        "title": "Cầu đo Kelvin Bridge báo rớt điện trở buổi trưa nóng & khách khiếu nại vỏ cáp CXV 'khó tuốt'",
        "symptom": "Gặp đồng thời 2 sự cố chất lượng: (A) 13h trưa Lab đo mẫu ruột cáp 50mm² được 0.395 Ω/km báo rớt chuẩn [[IEC 60228]] (≤ 0.387 Ω/km) đòi dừng Xưởng Kéo; (B) Khách hàng công trình khiếu nại vỏ cáp CXV dính chặt khó tuốt khi đấu tủ điện.",
        "impact": "Dừng máy oan gây mất sản lượng hoặc làm khách hàng công trình bức xúc đòi trả hàng.",
        "immediate_24h": "Tình huống A: Kiểm tra ngay nhiệt độ phòng Lab & nhiệt độ mẫu đồng đang đo (30°C hay mẫu vừa cắt nóng 45°C từ máy ra?). Tình huống B: Kiểm tra bộ Chày–Cối đã dùng trên máy đùn vỏ ở lệnh SX đó qua truy xuất mã rulo [[MES]].",
        "rca": "A: Nhân viên Lab mới quên nhân hệ số quy đổi về 20°C (ở 30°C, R_20 = 0.395 / [1 + 0.00393×10] = 0.380 Ω/km — ĐẠT 100% chuẩn!).\nB: Truy xuất [[MES]] thấy công nhân lắp nhầm bộ Chày–Cối kiểu Pressure (bọc áp lực lấp khe) thay vì kiểu Tubing (bọc ống) khi đùn lớp vỏ ngoài PVC cho cáp 4 lõi → Nhựa ép dính chặt cứng vào 4 lõi bên trong!",
        "oe_solution": "1. Cho Phòng Lab: Xây công cụ Excel/form tự động nhập nhiệt độ phòng & tự quy đổi R_20, bắt buộc để mẫu ổn định nhiệt 30 phút trong phòng 20–25°C trước khi kẹp [[Kelvin Bridge]], chạy thẩm định [[MSA]] / [[Gage R&R]].\n2. Cho Xưởng Đùn vỏ: Triển khai [[Poka-Yoke]] khắc laser chữ 'P' (Pressure) vs 'T' (Tubing) + sơn mã màu phân biệt ngay trên thân Chày–Cối và dịch VOC 'dễ tuốt vỏ' thành thông số CTQ lực bóc vỏ trong [[Control Plan]]!",
        "lock_in": "Đào tạo chuẩn 1 điểm [[OPL]] về quy đổi nhiệt độ 20°C tại Lab và kiểm tra mã 'T'/'P' trước khi đóng đầu [[Crosshead]] tại Xưởng Đùn.",
        "key_terms": ["Kelvin Bridge", "IEC 60228", "MSA", "Gage R&R", "Crosshead", "Poka-Yoke", "VOC", "CTQ", "OPL"],
        "doc_key": "planning_quality_ehs_cost",
        "lesson_id": "L4.5"
    },

    # =========================================================================
    # NHÓM 6: ĐÓNG CUỘN, CUT-LENGTH, BOM & PHẾ LIỆU (SC26 – SC30)
    # =========================================================================
    {
        "id": "SC26",
        "group": "6. Đóng Cuộn, Cut-Length, BOM & Phế Liệu",
        "station_id": "S08",
        "title": "Đơn hàng cáp lực dự án nhiều đoạn lẻ gây dư hàng trăm mét mẩu thừa Cut-Length",
        "symptom": "Đơn hàng cáp CXV 3×95+1×50 có 6 đoạn lẻ: 620m, 580m, 450m, 350m, 750m, 250m. Tổ cắt đoạn cứ lấy rulo chuẩn 1,500m cắt lần lượt theo danh sách làm dư ra 2 khúc lẻ 170m và 130m không bán được cho ai!",
        "impact": "300 mét cáp lực 3×95+1×50 thừa bị tuốt phế gây lỗ ngay > 110 triệu đồng chỉ trong 1 đơn hàng dự án!",
        "immediate_24h": "Tạm dừng cắt tùy tiện — gom danh sách tất cả các đoạn cắt dự án cùng chủng loại cáp trong tuần lại trên 1 bảng Excel để tổ hợp lại ngay.",
        "rca": "1. Không áp dụng thuật toán tổ hợp cắt (1D Cutting Stock Problem) ở Trạm 08.\n2. Phòng Kế hoạch phát lệnh cố định rulo 1,500m ở Trạm 03–04 mà không nhìn ngược danh sách tổng chiều dài các đoạn khách đặt!",
        "oe_solution": "1. Xây công cụ Excel Solver / [[Python]] (PuLP) tối ưu [[Cut-Length]] chỉ tốn 30 giây chạy: ghép Rulo 1 = 620 + 580 + 250 = 1,450m (dư 50m) và Rulo 2 = 750 + 450 + 350 = 1,550m (đặt chạy đúng 1,560m ngay từ lệnh Xưởng Bện & Đùn!).\n2. Với các đoạn dư dài > 80m còn lại, tạo danh mục 'Kho Đoạn Lẻ Tái Dùng' hiển thị cho Phòng Kinh doanh ưu tiên chào bán cho khách cần đoạn ngắn trước khi phát lệnh cắt mới.\n→ Giảm phế [[Cut-Length]] từ 9.5% xuống dưới 1.2%!",
        "lock_in": "Bắt buộc chạy bảng tổ hợp [[Cut-Length]] trước khi phát lệnh SX cáp lực dự án tại Phòng Kế hoạch (Trạm 00).",
        "key_terms": ["Cut-Length", "Python", "Excel", "BOM", "Scrap", "MRP"],
        "doc_key": "cable_cost_capacity",
        "lesson_id": "L5.3"
    },
    {
        "id": "SC27",
        "group": "6. Đóng Cuộn, Cut-Length, BOM & Phế Liệu",
        "station_id": "S06",
        "title": "Khách hàng phàn nàn cuộn dây thiếu mét — hoặc kiểm tra thấy xưởng tặng thừa +0.8m/cuộn",
        "symptom": "Kiểm tra đối chiếu chiều dài thực bằng bàn đo chuẩn 100m phát hiện máy đánh cuộn số 1 đang cắt thực tế 100.8m (tặng không +0.8%!), còn máy số 3 lại cắt hụt chỉ 99.3m (nguy cơ bị khách kiện gian lận!).",
        "impact": "Thừa +0.8m trên 50,000 khoanh dây VC/tháng = tặng không **40,000 mét dây đồng/tháng** (hàng trăm triệu đồng!); hụt -0.7m thì hủy hoại uy tín thương hiệu quốc gia CADIVI!",
        "immediate_24h": "Dừng kiểm chuẩn tức thời 100% bánh xe đo mét (Meter Counter Wheel / Encoder) trên tất cả máy đùn và máy đánh cuộn bằng thước chuẩn/sợi chuẩn 50m.",
        "rca": "1. Bánh xe đo mét bằng cao su bị mòn dần đường kính ngoài đi 0.8% sau 6 tháng chạy ma sát mà không có lịch hiệu chuẩn định kỳ → Cùng 1 vòng quay Encoder nhưng dây chạy qua dài hơn 0.8%!\n2. Hoặc lực ép bánh đo lỏng gây trượt (Slip) làm đếm thiếu mét (cắt thừa) hoặc dây kéo căng giãn đàn hồi khi nóng rồi co rút lại lúc nguội (cắt thiếu!).",
        "oe_solution": "1. Thay bánh xe đo mét bằng vật liệu chống mòn cao (hoặc đầu đo chiều dài không tiếp xúc Laser Doppler Velocimeter cho dây chuyền sản lượng lớn).\n2. Cài đặt hệ số bù co rút nhiệt chuẩn theo từng loại nhựa và siết chu kỳ kiểm chuẩn sai số mét (≤ ±0.2%) hàng tuần.\n3. Áp dụng kiểm tra đối chứng trọng lượng (Check-weigher) cuối chuyền đóng khoanh 100m như lớp [[Poka-Yoke]] thứ 2 (cuộn dây nhẹ hoặc nặng bất thường tự báo còi!).",
        "lock_in": "Đưa lịch hiệu chuẩn Encoder đo mét vào hệ thống [[PM Compliance]] hàng tuần và hồ sơ kiểm định thiết bị [[ISO 9001]].",
        "key_terms": ["Capstan", "Poka-Yoke", "PM Compliance", "ISO 9001", "Laser Gauge"],
        "doc_key": "cable_mfg_machines",
        "lesson_id": "L1.2"
    },
    {
        "id": "SC28",
        "group": "6. Đóng Cuộn, Cut-Length, BOM & Phế Liệu",
        "station_id": "S01",
        "title": "Cuối tháng Kế toán báo âm BOM nhựa PVC +4.9% dù chiều dày đo trên máy đùn đúng chuẩn 100%",
        "symptom": "Báo cáo [[Standard Cost]] cuối tháng cho thấy Xưởng Đùn tiêu hao vượt định mức [[BOM]] +4.9% kg hạt nhựa PVC vỏ (~280 triệu/tháng), dù Tổ trưởng & QA khẳng định chiều dày đo bằng [[Laser Gauge]] và kính hiển vi đều đúng chuẩn t_nom!",
        "impact": "Xưởng bị trừ thưởng oan, Kế toán nghi ngờ thất thoát kho hoặc báo cáo ảo.",
        "immediate_24h": "Lấy mẫu hạt nhựa PVC của 3 lô nhập gần nhất mang đo tỷ trọng riêng (Specific Gravity — g/cm³) và hàm lượng tro bột đá [[CaCO3 Filler]] tại Phòng Lab.",
        "rca": "Phát hiện 'Bẫy tỷ trọng [[CaCO3 Filler]]': Định mức [[BOM]] trên [[ERP]] được lập với tỷ trọng PVC chuẩn 1.40 g/cm³, nhưng nhà cung cấp mới (bán rẻ hơn 3% theo VNĐ/kg!) đã trộn tăng hàm lượng bột đá CaCO3 đẩy tỷ trọng thực tế lên 1.47–1.50 g/cm³ (+5% đến +7%)! Vì máy đùn bọc theo THỂ TÍCH (chiều dày mm), hạt nặng hơn 5% chắc chắn làm tốn thêm 5% kg nhựa dù chiều dày chuẩn từng 0.01 mm!",
        "oe_solution": "1. Chứng minh bằng công thức VNĐ/lít = (Đơn giá VNĐ/kg) × (Tỷ trọng kg/lít): Hạt rẻ hơn 3%/kg nhưng nặng hơn 6% thực chất ĐẮT HƠN +2.8% trên mỗi mét cáp, chưa kể còn giảm [[Tensile]] & làm mòn trục vít!\n2. Bổ sung tiêu chuẩn khống chế Tỷ trọng tối đa (vd: ≤ 1.42 ± 0.02 g/cm³) vào Hợp đồng Mua hàng và Phiếu kiểm tra IQC đầu vào (Trạm 01).\n3. Phối hợp Kế toán tách rõ chênh lệch do Tỷ trọng NVL khỏi chênh lệch vận hành của Xưởng Đùn!",
        "lock_in": "Đưa đo tỷ trọng 100% lô hạt PVC nhập kho vào [[Control Plan]] IQC và bảng đánh giá nhà cung cấp theo chi phí VNĐ/dm³.",
        "key_terms": ["CaCO3 Filler", "PVC", "BOM", "Standard Cost", "Laser Gauge", "Tensile", "Control Plan"],
        "doc_key": "cable_extrusion_wire_forensics",
        "lesson_id": "L5.2"
    },
    {
        "id": "SC29",
        "group": "6. Đóng Cuộn, Cut-Length, BOM & Phế Liệu",
        "station_id": "S09",
        "title": "Thùng phế liệu vứt lẫn đồng trần với đồng dính nhựa làm mất 30% giá trị thu hồi",
        "symptom": "Đi [[Genba]] khu tập kết phế liệu thấy các thùng phế từ Xưởng Kéo, Bện, Đùn vứt chung cả sợi đồng trần tinh khiết, đoạn cáp dính nhựa PVC/XLPE, băng thép và giẻ lau dầu!",
        "impact": "Đồng trần tinh khiết bán/tái nấu thu hồi ~94% giá trị đồng gốc, còn đồng lẫn nhựa dính tạp chất chỉ bán được ~65–70% (hoặc tốn thêm nhân công máy tuốt) → Đánh mất hàng trăm triệu đồng mỗi năm!",
        "immediate_24h": "Cân phân loại thực tế 1 tuần phế liệu tại 4 xưởng để tính ra đúng số tiền mất đi do trộn lẫn (trình số liệu trực quan cho Giám đốc & Quản đốc).",
        "rca": "1. Dưới chân máy chỉ đặt 1 thùng rác chung không phân loại.\n2. Trên [[SAP PP]] màn hình xác nhận lệnh CO11N chỉ có 1 mã 'Phế phẩm chung' không tách mã Đồng trần vs Đồng dính nhựa vs Nhựa purge sạch nên không ai quan tâm phân loại!",
        "oe_solution": "1. Triển khai hệ thống 3 thùng phế mã màu [[5S]] cố định ngay tại mọi chân máy:\n   • Thùng XANH: Đồng trần tinh khiết (thu hồi ~94%).\n   • Thùng VÀNG: Đồng dính nhựa (chuyển máy tuốt bóc tách).\n   • Thùng XÁM (lót khay inox sạch): Nhựa [[PVC]] purge sạch (nghiền tái chế Regrind dùng hợp lệ làm lớp độn Bedding!).\n2. Mở 3 mã Reason Code phế riêng biệt trên [[SAP PP]] / [[MES]] và cân ghi nhận riêng từng loại cuối mỗi ca.\n3. Gắn thưởng nhóm [[Kaizen]] cho phân xưởng đạt tỷ lệ phân loại sạch 100%.",
        "lock_in": "Đưa tiêu chí 'Thùng phế 3 màu không lẫn tạp chất' thành 1 câu hỏi bắt buộc trong phiếu kiểm tra [[LPA]] hàng ngày.",
        "key_terms": ["Scrap", "5S", "SAP PP", "PVC", "Kaizen", "LPA", "Genba"],
        "doc_key": "bom_cost",
        "lesson_id": "L5.4"
    },
    {
        "id": "SC30",
        "group": "6. Đóng Cuộn, Cut-Length, BOM & Phế Liệu",
        "station_id": "S08",
        "title": "Tổ đóng khoanh 100m dây dân dụng ùn ứ cuối ca, xin tuyển thêm 3 công nhân thời vụ",
        "symptom": "Khi Xưởng Đùn tăng tốc nhờ [[SMED]], tổ đóng khoanh 100m gồm 6 người không kịp đóng gói (ùn 40 rulo cuối ca), Tổ trưởng đề xuất tuyển gấp thêm 3 nhân sự mới.",
        "impact": "Tốn thêm ~300 triệu chi phí lương/năm trong khi hiệu suất thực tế của 6 người hiện tại chưa được đo đạc khoa học.",
        "immediate_24h": "OE xuống bấm giờ [[Time Study]] & [[Work Sampling]] cả 6 vị trí trong tổ đóng khoanh (Cuốn dây – Cột dây – Dán tem – Bọc màng co – Xếp thùng/pallet – Đẩy xe) và vẽ sơ đồ di chuyển [[Spaghetti]].",
        "rca": "Biểu đồ [[Yamazumi]] phơi bày sự mất cân bằng nghiêm trọng (Balance Efficiency chỉ 61%!): Người đứng máy cuốn chạy 18 giây/khoanh trong khi người dán tem + bọc màng mất 32 giây/khoanh (nút thắt!) còn người xếp pallet nhàn rỗi chờ tới 45% thời gian; bàn đóng gói đặt rời rạc làm công nhân phải đi bộ trung bình 4.5 km/ca!",
        "oe_solution": "1. Sắp xếp lại mặt bằng tổ đóng khoanh theo Layout chữ U sát nhau (dùng [[AutoCAD]] & con lăn trượt trọng lực chuyển khoanh giữa các bước → cắt 70% quãng đường trên sơ đồ [[Spaghetti]]!).\n2. Tái phân bổ thao tác trên [[Yamazumi]]: tách bước dán tem nhãn chuyển sang hỗ trợ từ vị trí xếp pallet nhàn rỗi, dùng máy bắn dây đai bán tự động → Đẩy Balance Efficiency từ 61% lên 88%, nâng sản lượng tổ 6 người từ 950 lên 1,380 khoanh/ca (+45%) mà KHÔNG cần tuyển thêm 1 người nào!",
        "lock_in": "Ban hành [[Standard Work]] theo Takt Time từng vị trí và theo dõi chỉ số [[OLE]] tổ đóng cuộn hàng ngày trên bảng [[Visual Management]].",
        "key_terms": ["Yamazumi", "Time Study", "Work Sampling", "Spaghetti", "AutoCAD", "OLE", "Standard Work", "Headcount Planning"],
        "doc_key": "ole",
        "lesson_id": "L2.4"
    },

    # =========================================================================
    # NHÓM 7: BẢO TRÌ, NĂNG LƯỢNG & AN TOÀN LOTO (SC31 – SC35)
    # =========================================================================
    {
        "id": "SC31",
        "group": "7. Bảo Trì, Năng Lượng & An Toàn LOTO",
        "station_id": "S09",
        "title": "Cháy tủ điện biến tần máy đùn cổ chai giữa mùa cao điểm gây dừng máy 3 ngày",
        "symptom": "Đang chạy cao điểm đơn hàng lớn, tủ điện biến tần chính của máy đùn số 3 bốc khói cháy cầu dao tổng — nhà máy phải dừng cổ chai suốt 72 giờ chờ linh kiện thay thế!",
        "impact": "Thiệt hại trực tiếp chi phí sửa chữa + mất sản lượng xuất xưởng > 300 triệu đồng, phá vỡ kế hoạch giao hàng cả tuần.",
        "immediate_24h": "Khoanh vùng đảm bảo an toàn điện [[LOTO]], điều chuyển tạm các đơn gấp sang máy đùn khác và kiểm tra ngay toàn bộ tủ điện các máy đùn/máy kéo còn lại để phòng cháy dây chuyền.",
        "rca": "Nhà máy chỉ chạy bảo trì 'hỏng mới sửa' (Reactive) và kiểm tra bằng mắt thường — đầu cos tiếp điểm bị lỏng phát nhiệt âm thầm lên 108°C trong nhiều tuần (giai đoạn P trên đường cong P–F) nhưng không ai phát hiện cho tới khi bốc cháy (Điểm F)!",
        "oe_solution": "1. Đề xuất đầu tư 1 camera ảnh nhiệt cầm tay (~25 triệu) + bút đo rung bạc đạn triển khai bảo trì dự đoán [[CBM / PdM]] định kỳ hàng tháng cho 100% tủ điện, biến tần và ổ bi máy cổ chai (RBD, Rigid Strander, Extruder).\n2. Thiết lập danh mục phụ tùng chiến lược (Critical Spare Parts — biến tần, cặp nhiệt điện, cầu dao tổng) kèm mức [[Safety Stock]] riêng.\n3. Gắn Ma trận leo thang sự cố [[Escalation Matrix]] (5p–15p–30p) để rút ngắn [[MTTR]] khi có dấu hiệu bất thường.\n→ Lần soi nhiệt đầu tiên đã phát hiện sớm 4 đầu cos nóng > 95°C và siết lại trong 15 phút nghỉ trưa — tránh được 4 vụ cháy tủ điện!",
        "lock_in": "Đưa lịch soi ảnh nhiệt + đo rung định kỳ vào hệ thống [[PM Compliance]] và theo dõi chỉ số [[MTBF]] tăng liên tục hàng quý.",
        "key_terms": ["CBM / PdM", "PM Compliance", "MTBF", "MTTR", "LOTO", "Escalation Matrix", "TPM"],
        "doc_key": "oe_field_execution_case_test",
        "lesson_id": "L6.1"
    },
    {
        "id": "SC32",
        "group": "7. Bảo Trì, Năng Lượng & An Toàn LOTO",
        "station_id": "S09",
        "title": "Đội Cơ Điện luôn than 'quá tải thiếu người' nhưng sự cố hỏng máy vẫn tăng liên tục",
        "symptom": "Phòng Cơ Điện có 8 kỹ thuật viên liên tục tăng ca cuối tuần và xin tuyển thêm 3 thợ mới, nhưng tỷ lệ [[PM Compliance]] vẫn chỉ đạt 58% và dừng máy sự cố Breakdown không giảm.",
        "impact": "Chi phí tăng ca bảo trì cao, thợ kiệt sức chạy chữa cháy, còn Xưởng Sản xuất thì kêu trời vì máy hay hỏng giữa ca.",
        "immediate_24h": "OE trao đổi minh bạch với Trưởng phòng Cơ Điện rằng sẽ đo [[Wrench Time]] bằng [[Work Sampling]] trong 5 ngày để tìm các rào cản hành chính đang làm mất thời gian của anh em thợ (tuyệt đối KHÔNG dùng để chấm phạt cá nhân!).",
        "rca": "Kết quả [[Work Sampling]] gây sốc: [[Wrench Time]] thực tế chỉ đạt 31%! Tới 69% thời gian thợ Cơ Điện bị đốt vào: chờ kho phụ tùng tìm vòng bi/điện trở (22%), chờ Sản xuất bàn giao dừng máy (18%), đi đi lại lại lấy thiếu cờ-lê (14%), chờ duyệt phiếu/hỏi lệnh (15%)!",
        "oe_solution": "1. Tổ chức [[5S]] lại Kho phụ tùng cơ điện dán mã theo từng máy & áp dụng [[Kitting]]: soạn sẵn trọn bộ phụ tùng + bản vẽ + dụng cụ vào khay trước ngày làm PM 24 giờ!\n2. Chốt 'Cửa sổ Bảo trì Vàng' (4 giờ cố định mỗi sáng Chủ nhật xen kẽ từng cụm máy) trực tiếp trong lịch [[MPS]] — Xưởng Sản xuất bắt buộc bàn giao máy đúng giờ!\n3. Trang bị xe đẩy đồ nghề di động đầy đủ dụng cụ chuẩn cho từng tổ bảo trì.\n→ [[Wrench Time]] tăng từ 31% lên 49% (+58% năng lực bảo trì thực, tương đương tuyển miễn phí thêm 4.5 kỹ thuật viên giỏi!), [[PM Compliance]] vọt lên 93% và Breakdown giảm 48%!",
        "lock_in": "Gắn KPI [[PM Compliance]] ≥ 90% và tỷ lệ Công việc có kế hoạch vs Chữa cháy (80/20) vào báo cáo tuần Phòng Cơ Điện.",
        "key_terms": ["Wrench Time", "Work Sampling", "PM Compliance", "Kitting", "5S", "MPS", "TPM"],
        "doc_key": "oe_field_execution_case_test",
        "lesson_id": "L6.1"
    },
    {
        "id": "SC33",
        "group": "7. Bảo Trì, Năng Lượng & An Toàn LOTO",
        "station_id": "S09",
        "title": "Hóa đơn tiền điện & chỉ số SEC (kWh/tấn đồng) tăng vọt +14% so với trung bình năm",
        "symptom": "Phòng Kế toán báo tháng vừa rồi tiền điện toàn nhà máy tăng bất thường +14% (~160 triệu VNĐ) dù sản lượng tấn cáp xuất xưởng gần như không đổi!",
        "impact": "Ăn mòn trực tiếp biên lợi nhuận sản xuất và vi phạm mục tiêu tiết kiệm năng lượng [[ISO 50001]].",
        "immediate_24h": "Đi kiểm tra nhà máy vào giờ nghỉ trưa/Chủ nhật khi máy sản xuất dừng (lắng nghe tiếng xì rò khí nén + ghi chỉ số công tơ điện chạy không tải Base Load!) và xuất dữ liệu hồi quy điện năng theo từng phân xưởng.",
        "rca": "Chạy phương trình hồi quy [[Regression]] (`kWh = Base_Load + b × Tấn`) phơi bày 3 ổ đốt điện khổng lồ:\n1. Hệ thống khí nén rò rỉ tới 27 điểm van/khớp nối làm máy nén khí chạy tải 70% ngay cả lúc xưởng nghỉ!\n2. Cụm bơm nước giải nhiệt 45kW & quạt tháp chạy cố định 50Hz suốt ca đêm non tải.\n3. Lò nung máy đùn bật sấy nóng trước 3 tiếng lãng phí khi chưa tới giờ chạy.",
        "oe_solution": "1. Chiến dịch săn rò khí nén cuối tuần bằng thẻ [[Red Tag]]/Fuguai (hoặc súng siêu âm): xử lý 25/27 điểm rò trong 10 ngày → Tiết kiệm ngay ~20 triệu/tháng (chi phí gần 0 đồng!).\n2. Lập dự án [[ROI]] lắp biến tần [[VFD]] có cảm biến áp suất/nhiệt độ phản hồi PID cho bơm giải nhiệt & quạt tháp (định luật P ∝ N³: giảm 20% tốc độ tiết kiệm gần 50% điện! Vốn 85 triệu, tiết kiệm 11 triệu/tháng → [[Payback]] 7.7 tháng!).\n3. Chuẩn hóa đồng hồ hẹn giờ tự động bật gia nhiệt máy đùn đúng 60 phút trước ca.\n→ Kéo [[SEC]] giảm ngay -11% bền vững!",
        "lock_in": "Gắn công tơ phụ theo dõi [[SEC]] (kWh/tấn) theo từng phân xưởng lên Dashboard [[Power BI]] chuẩn [[ISO 50001]].",
        "key_terms": ["SEC", "ISO 50001", "VFD", "Regression", "Red Tag", "ROI", "Payback", "Power BI"],
        "doc_key": "planning_quality_ehs_cost",
        "lesson_id": "L5.4"
    },
    {
        "id": "SC34",
        "group": "7. Bảo Trì, Năng Lượng & An Toàn LOTO",
        "station_id": "S04",
        "title": "Suýt xảy ra tai nạn nghiêm trọng (Near-miss) khi 2 thợ làm SMED nhanh quên khóa LOTO",
        "symptom": "Trong lúc thử nghiệm đổi khuôn nhanh [[SMED]] 2 người song song trên máy đùn/máy bện, người phía trước tưởng người phía sau đã xong nên bấm nút nhắp thử trục vít khi tay người kia vẫn gần đầu khuôn!",
        "impact": "Cảnh báo đỏ an toàn sinh mạng ([[EHS]] / [[ISO 45001]]) — chỉ 1 tai nạn lao động sẽ làm dừng toàn bộ dự án cải tiến OE và gây hậu quả không thể khắc phục.",
        "immediate_24h": "DỪNG NGAY thử nghiệm SMED, lập biên bản Near-miss minh bạch (không trù dập mà để sửa hệ thống!), tổ chức đánh giá rủi ro lại toàn bộ các bước thao tác cùng cán bộ EHS và Quản đốc.",
        "rca": "Khi thiết kế quy trình [[SMED]] Pit-stop 2 người đã quá tập trung rút ngắn giây mà bỏ sót bước bắt buộc khóa-thẻ năng lượng [[LOTO]] 6 bước và thiết bị kẹp nhiều ổ khóa (Group Lockout Hasp)!",
        "oe_solution": "1. Tích hợp CỨNG nguyên tắc bất di bất dịch '1 Người – 1 Ổ Khóa – 1 Chìa Khóa' vào bước số 1 của mọi bản [[SOP]] SMED & bảo trì: trang bị kẹp Hasp treo ngay cửa tủ điện máy — cả 2 thợ CÙNG móc ổ khóa cá nhân của mình, bấm thử nút Start kiểm chứng Zero Energy trước khi chạm tay vào khuôn!\n2. Thiết kế chốt định vị an toàn & tay cầm cách nhiệt chống bỏng cho đầu khuôn sấy nóng 160°C.\n3. Đào tạo lại 100% quy trình [[LOTO]] 6 bước (mất thêm chỉ 40 giây nhưng đảm bảo an toàn 100% tính mạng!).",
        "lock_in": "Đưa kiểm tra tuân thủ [[LOTO]] thành mục ưu tiên số 1 (Zero Tolerance — vi phạm dừng việc ngay!) trong mọi lượt kiểm tra [[LPA]] của Tổ trưởng, Quản đốc và Giám đốc.",
        "key_terms": ["LOTO", "EHS", "ISO 45001", "SMED", "SOP", "LPA"],
        "doc_key": "planning_quality_ehs_cost",
        "lesson_id": "L1.4"
    },
    {
        "id": "SC35",
        "group": "7. Bảo Trì, Năng Lượng & An Toàn LOTO",
        "station_id": "S03",
        "title": "Công nhân tự ý dán băng keo khóa chết cảm biến đứt sợi Jidoka cho 'đỡ bị dừng máy'",
        "symptom": "Đi [[Genba]] ca đêm phát hiện trên 2 máy bện [[Buncher]] và 1 máy quấn băng [[Mica FR]], công nhân lấy băng keo quấn khóa chết công tắc cảm biến đứt sợi để máy cứ chạy tiếp không tự dừng!",
        "impact": "Phá hủy hoàn toàn cơ chế [[Jidoka]], tạo ra hàng km cáp thiếu sợi đồng (rớt điện trở) hoặc thiếu lớp băng chống cháy [[Mica FR]] cực kỳ nguy hiểm lọt ra công trình!",
        "immediate_24h": "Tháo bỏ ngay băng keo, cách ly kiểm tra lại toàn bộ các rulo đã sản xuất trên 3 máy đó trong ca; nói chuyện trực tiếp lắng nghe lý do thật sự tại sao công nhân lại phải dán cảm biến!",
        "rca": "Hỏi thẳng dưới xưởng mới lộ ra nguyên nhân gốc đáng giật mình: Cảm biến bị hỏng lỏng dây hay BÁO GIẢ (False Trigger) dừng máy vô cớ 10 lần/ca làm công nhân không đạt định mức sản lượng bị trừ lương, báo bảo trì 2 tuần chưa sửa nên họ đành dán băng keo cho chạy!",
        "oe_solution": "1. Không đổ lỗi phạt công nhân đơn thuần — OE phối hợp Cơ Điện sửa dứt điểm ngay lập tức lỗi báo giả cảm biến (thay cảm biến quang/tiệm cận ổn định, đi lại dây chống nhiễu).\n2. Chỉnh lại cơ chế báo sự cố: nếu máy báo giả > 2 lần, công nhân bật đèn [[Andon]] kích hoạt [[Escalation Matrix]] để Cơ Điện xuống xử lý trong 15 phút.\n3. Nâng cấp cảm biến kiểu không thể đấu tắt/dán băng keo (Fail-safe Wiring trên [[PLC]]) để bảo vệ tuyệt đối chất lượng cáp chống cháy [[Mica FR]]!",
        "lock_in": "Thêm mục 'Kiểm thử kích hoạt cảm biến đứt sợi/băng tự dừng đầu ca' vào [[Control Plan]] và [[LPA]].",
        "key_terms": ["Jidoka", "Mica FR", "Buncher", "Andon", "Escalation Matrix", "PLC", "Control Plan", "Genba"],
        "doc_key": "lean_muda",
        "lesson_id": "L3.1"
    },

    # =========================================================================
    # NHÓM 8: CON NGƯỜI, DỮ LIỆU MES & VĂN HÓA HIỆN TRƯỜNG (SC36 – SC40)
    # =========================================================================
    {
        "id": "SC36",
        "group": "8. Con Người, Dữ Liệu MES & Văn Hóa Hiện Trường",
        "station_id": "S00",
        "title": "Báo cáo OEE ghi tay sổ giấy luôn đẹp 82% nhưng thực tế xưởng giao hàng trễ liên tục",
        "symptom": "Sổ ca hàng tháng báo cáo [[OEE]] Xưởng Đùn đạt 82% rất đẹp, nhưng sản lượng thực nhập kho chỉ đạt 66% công suất thiết kế và khách hàng kêu trễ hẹn liên tục!",
        "impact": "Ban Giám đốc bị 'mù số liệu', không nhìn thấy 40+ giờ dừng vặt và giảm tốc ẩn nên không thể đầu tư cải tiến đúng chỗ.",
        "immediate_24h": "Đối chiếu chéo 3 nguồn độc lập trong 7 ngày: (1) Sổ tay tổ trưởng, (2) Tổng số mét thực tế nhập kho thành phẩm / tổng giờ ca, (3) Bấm giờ [[Work Sampling]] thực tế tại máy đùn.",
        "rca": "Phơi bày 3 sai lệch kinh điển của báo cáo tay:\n1. Quên ghi toàn bộ các lần dừng vặt < 5 phút (mất 35% Downtime thực!).\n2. Dùng tốc độ định mức cũ lỗi thời (hoặc tự ý trừ hết thời gian đổi màu/chờ vật tư ra khỏi 'Thời gian kế hoạch' để làm đẹp Availability!).\n3. Không tính đủ phế đầu ca và phế cắt sửa.",
        "oe_solution": "1. Chuẩn hóa công thức [[OEE]] theo tốc độ chuẩn mét/phút & Bảng mã dừng máy gọn nhẹ (chỉ 12–15 mã chuẩn theo 6 Big Losses, cấm trừ đổi màu/chờ vật tư khỏi Planned Time!).\n2. Xây file [[Excel]] [[Power Query]] / [[Python]] đối chiếu tự động số mét nhập kho với giờ ca chạy để tự động phơi bày chênh lệch trước, rồi kết nối xung Encoder + cảm biến chạy máy thẳng vào [[MES]] & Dashboard [[Power BI]] real-time!\n3. Truyền thông rõ: OE đo [[OEE]] thật (66%) để GIÚP xưởng gỡ nút thắt tăng lương sản phẩm, KHÔNG dùng để truy phạt thành tích cũ!",
        "lock_in": "Họp 10 phút đầu ngày nhìn đúng 1 nguồn sự thật duy nhất (Single Source of Truth) trên Dashboard [[OEE Waterfall]] [[Power BI]].",
        "key_terms": ["OEE", "OEE Waterfall", "MES", "Power Query", "Power BI", "Python", "Work Sampling", "Downtime"],
        "doc_key": "erp_mes",
        "lesson_id": "L6.2"
    },
    {
        "id": "SC37",
        "group": "8. Con Người, Dữ Liệu MES & Văn Hóa Hiện Trường",
        "station_id": "S04",
        "title": "Quản đốc và Tổ trưởng phản kháng không hợp tác dự án SMED ('đang bận chạy hàng, đừng bày vẽ!')",
        "symptom": "Khi OE đề xuất quay video bấm giờ làm [[SMED]] trên máy đùn cổ chai, Quản đốc và Tổ trưởng tỏ thái độ lạnh nhạt, nói 'xưởng đang chạy sấp mặt không có thời gian họp hành vẽ vời giấy tờ!'",
        "impact": "Mọi sáng kiến OE sẽ chết yểu nếu không có sự đồng hành của người trực tiếp vận hành dưới xưởng.",
        "immediate_24h": "Lùi 1 bước, KHÔNG mang lý thuyết sách vở ra tranh luận hay báo cáo méc Giám đốc — xuống đứng cùng ca với anh em, hỏi thẳng: 'Ở máy này hiện tại việc gì đang làm anh em mệt nhất, mất công nhất hoặc hay bị mắng nhất?'",
        "rca": "Áp dụng mô hình quản trị thay đổi [[ADKAR]]: Xưởng phản kháng vì 2 nỗi sợ thực tế — (1) Sợ OE xuống 'soi lỗi' để cắt thưởng/cắt người, (2) Chưa thấy lợi ích trực tiếp cho bản thân (thiếu Desire — chữ D trong ADKAR!).",
        "oe_solution": "1. Làm ngay 1–2 dự án **Quick-Win giải tỏa nỗi đau của chính công nhân** trước (vd: hàn máng hứng nhựa nóng đỡ cúi đau lưng & bỏng tay, sắm bộ cờ-lê/xe đồ nghề [[5S]] gọn nhẹ, hỗ trợ làm báo cáo tự động cắt 25 phút viết sổ tay cuối ca cho Tổ trưởng!).\n2. Mời chính Tổ trưởng & thợ giỏi đồng thiết kế giải pháp [[Kaizen]] và ghi tên họ lên bảng vinh danh + thưởng nóng khi báo cáo Ban Giám đốc!\n3. Sau khi có niềm tin từ Quick-Win, mời họ cùng làm Pilot [[SMED]] 1 máy và chia sẻ lợi ích: máy chạy nhanh hơn, ít phế hơn → tăng thưởng năng suất thực cho cả tổ!",
        "lock_in": "Duy trì lịch đi [[Genba]] lắng nghe hàng ngày và hệ thống thưởng nóng sáng kiến [[Kaizen]] minh bạch trong 7 ngày.",
        "key_terms": ["ADKAR", "Genba", "Kaizen", "SMED", "5S", "A3"],
        "doc_key": "planning_quality_ehs_cost",
        "lesson_id": "L7.3"
    },
    {
        "id": "SC38",
        "group": "8. Con Người, Dữ Liệu MES & Văn Hóa Hiện Trường",
        "station_id": "S04",
        "title": "Dự án SMED / 5S thành công rực rỡ tháng đầu rồi 2 tháng sau trượt về thói quen cũ",
        "symptom": "Trong tháng Pilot có OE đứng sát bên, thời gian đổi mã máy đùn giảm đẹp từ 55p → 14p và khu máy sạch bóng [[5S]]. Hai tháng sau khi OE chuyển sang dự án khác, đổi mã lại phình lên 38 phút và xe đồ nghề mất nửa cờ-lê!",
        "impact": "Hiệu ứng 'sớm nở tối tàn' (Entropy cải tiến) làm lãng phí công sức và mất uy tín của phòng OE trước Ban Giám đốc.",
        "immediate_24h": "Đi kiểm tra hiện trường xem chính xác bước nào trong quy trình [[Standard Work]] đang bị bỏ qua (vd: không bật tủ sấy sẵn khuôn trước khi dừng máy, không trả đồ nghề về Shadow Board cuối ca).",
        "rca": "Hoàn thành tốt pha Improve nhưng làm quá yếu pha Control trong [[DMAIC]]: Thành quả chỉ dựa vào 'cá nhân OE đi nhắc' thay vì xây dựng hệ thống duy trì kỷ luật quản trị ([[LSW]] + [[LPA]] + [[Control Plan]])!",
        "oe_solution": "1. Biến thành quả cải tiến thành thói quen quản lý bằng **Bộ 3 Khóa Chuẩn**:\n   • [[LSW]] (Leader Standard Work): Thêm 2 dòng kiểm tra 3 phút đầu ca của Tổ trưởng ('Tủ sấy Tip/Die cho lệnh kế đã bật chưa?', 'Xe đồ nghề Shadow Board đủ món chưa?').\n   • [[LPA]] (Layered Process Audit): Tổ trưởng kiểm hàng ngày, Quản đốc/OE kiểm hàng tuần, Giám đốc kiểm ngẫu nhiên 2 tuần/lần (10 câu Có/Không).\n   • [[Visual Management]]: Treo biểu đồ theo dõi thời gian đổi mã từng ca ngay tại máy (đạt ≤ 15p tô Xanh, vượt > 20p tô Đỏ ghi rõ lý do!).\n2. Phối hợp cài quy trình kiểm soát tài liệu [[ISO 9001]] và đào tạo chuẩn cho công nhân mới thay ca.",
        "lock_in": "Bắt buộc ký bàn giao đầy đủ gói Control (`SOP` + `OPL` + `LSW` + `LPA`) trước khi chính thức đóng bất kỳ dự án OE nào!",
        "key_terms": ["LSW", "LPA", "Control Plan", "DMAIC", "Standard Work", "Visual Management", "ISO 9001", "OPL"],
        "doc_key": "oe_field_execution_case_test",
        "lesson_id": "L3.4"
    },
    {
        "id": "SC39",
        "group": "8. Con Người, Dữ Liệu MES & Văn Hóa Hiện Trường",
        "station_id": "S04",
        "title": "Công nhân Ca 1 và Ca 2 chỉnh nhiệt độ/tốc độ khác nhau tạo Histogram 2 đỉnh (Bimodal)",
        "symptom": "Vẽ biểu đồ [[Histogram]] đường kính dây VC 2.5mm² trên [[Minitab]] thấy hình 2 đỉnh tách biệt rõ rệt (đỉnh 1 tại 3.35mm, đỉnh 2 tại 3.44mm!) dù chạy cùng 1 máy đùn và cùng 1 lô hạt nhựa!",
        "impact": "Độ biến thiên tổng thể σ bị phình to gấp đôi làm [[Cpk]] rớt xuống < 0.85, gây vừa thừa nhựa ở Ca 2 vừa sát cận mỏng ở Ca 1.",
        "immediate_24h": "Phân tầng dữ liệu (Stratification trong [[7 QC Tools]]) tách theo Ca 1 / Ca 2 / Ca 3 và theo từng công nhân vận hành, chạy kiểm định [[ANOVA]] trên [[Minitab]] xác nhận khác biệt có ý nghĩa thống kê ([[p-value]] < 0.05).",
        "rca": "Kiểm tra màn hình [[HMI]] hai ca phát hiện: Tổ trưởng Ca 1 chỉnh theo chuẩn mới tiết kiệm nhựa (target 3.36mm), còn Tổ trưởng Ca 2 theo kinh nghiệm cũ sợ rớt [[Spark Tester]] nên vào đầu ca tự vặn tăng nhiệt độ & giảm tốc kéo lên 3.44mm (không phân quyền khóa Recipe trên HMI!).",
        "oe_solution": "1. Chạy thử nghiệm đối chứng trên dữ liệu thực tế cho cả 3 ca cùng thấy ở target 3.36mm tỷ lệ lỗi [[Spark Tester]] vẫn = 0%.\n2. Thiết lập **Thư viện công thức chạy máy chuẩn (Recipe Library)** trên [[HMI]]/[[PLC]] và phân quyền mật khẩu: công nhân chỉ chọn đúng mã hàng để máy tự nạp thông số chuẩn, chỉ Kỹ thuật/Quản đốc mới được phép điều chỉnh vượt biên ±3°C!\n3. Đồng bộ đào tạo lại cả 3 ca theo cùng 1 bản [[SOP]] và theo dõi [[SPC]] chung theo ca.\n→ [[Histogram]] gom về 1 đỉnh chuẩn duy nhất, [[Cpk]] nhảy vọt từ 0.85 lên 1.58!",
        "lock_in": "Gắn báo cáo so sánh chỉ số [[Cpk]] & tốc độ chạy giữa 3 ca trên [[Power BI]] để xóa lệch chuẩn giữa các kíp trực.",
        "key_terms": ["Histogram", "Minitab", "ANOVA", "p-value", "7 QC Tools", "HMI", "Cpk", "SPC"],
        "doc_key": "minitab_spc",
        "lesson_id": "L4.3"
    },
    {
        "id": "SC40",
        "group": "8. Con Người, Dữ Liệu MES & Văn Hóa Hiện Trường",
        "station_id": "S01",
        "title": "Phòng Mua hàng đề xuất đổi sang nhà cung cấp hạt nhựa / đồng Rod rẻ hơn 3% ngay lập tức",
        "symptom": "Để đạt KPI tiết kiệm chi phí mua hàng quý này, Phòng Mua hàng tìm được nhà cung cấp hạt nhựa PVC (hoặc đồng Rod) giá rẻ hơn 3% và muốn đưa thẳng 30 tấn xuống xưởng chạy đại trà ngay tuần tới!",
        "impact": "Rủi ro cực lớn: nếu lô nhựa bị bay hơi hóa dẻo rớt lão hóa [[Aging Oven]] 7 ngày, tăng tỷ trọng [[CaCO3 Filler]], hoặc đồng Rod độ dẫn [[IACS]] thấp / dày oxit làm hỏng khuôn [[PCD]], nhà máy có thể lỗ gấp 10 lần khoản tiền 'tiết kiệm mua hàng'!",
        "immediate_24h": "OE lập tức kích hoạt cổng kiểm soát thay đổi [[MOC / ECN]] — đề nghị tạm giữ nhập đại trà và chỉ nhập đúng 1 lô thử nghiệm nhỏ (Pilot Lot 500 kg nhựa hoặc 1 cuộn đồng Rod 3 tấn) để thẩm định toàn diện trước!",
        "rca": "KPI mua hàng chỉ đo đơn giá đầu vào (Purchase Price Variance) mà tách rời khỏi tổng chi phí vận hành dưới xưởng (Tỷ trọng VNĐ/lít, % [[IACS]], tỷ lệ đứt sợi/tấn, tốc độ đùn, tỷ lệ phế & tuổi thọ khuôn [[PCD]])!",
        "oe_solution": "Triển khai quy trình [[MOC / ECN]] 5 bước chuẩn mực liên phòng ban (Mua hàng – Kỹ thuật – QA Lab – OE – Kế toán):\n1. **Thẩm định Lab đầy đủ:** Kiểm % [[IACS]], Reverse Twist [[ASTM B49]] (với đồng); đo tỷ trọng Specific Gravity, [[Tensile]] & **BẮT BUỘC chờ đủ 7 ngày tủ lão hóa [[Aging Oven]]** (với nhựa)!\n2. **Chạy thử lô Pilot trên xưởng:** Đo đủ [[OEE]], tốc độ tối đa, [[Melt Pressure]], đứt sợi/tấn, lỗi [[Spark Tester]] và kiểm định [[2-Sample t-test]] so với nhà cung cấp hiện tại.\n3. **Tính Tổng Chi Phí Sở Hữu (TCO / [[Standard Cost]]):** Chỉ ký duyệt ECN cho nhập đại trà khi TCO thực sự rẻ hơn VÀ đạt 100% chuẩn [[QCVN 4]] / [[IEC 60502]]!",
        "lock_in": "Ban hành quy định [[ISO 9001]]: Kho NVL từ chối nhập đại trà bất kỳ mã nhà cung cấp mới nào chưa có chữ ký duyệt [[MOC / ECN]] hoàn chỉnh (đủ kết quả [[Aging Oven]] 7 ngày).",
        "key_terms": ["MOC / ECN", "Aging Oven", "IACS", "ASTM B49", "CaCO3 Filler", "2-Sample t-test", "Standard Cost", "QCVN 4"],
        "doc_key": "oe_field_execution_case_test",
        "lesson_id": "L4.5"
    },
])


# =========================================================================
# API TRA CỨU NHANH CHO JOBDETAILAPP & MARKDOWN EXPORTER
# =========================================================================
def get_master_map():
    """Trả về sơ đồ ASCII tổng thể dòng chảy khép kín 10 trạm CADIVI."""
    return FACTORY_MASTER_MAP


def get_stations():
    """Trả về danh sách 10 trạm dòng chảy nhà máy (S00 → S09)."""
    return STATIONS


def get_station(station_id):
    """Lấy chi tiết 1 trạm theo mã (vd: 'S04')."""
    if not station_id:
        return None
    sid = station_id.strip().upper()
    for st in STATIONS:
        if st["id"].upper() == sid:
            return st
    return None


def get_product_flows():
    """Trả về 6 lưu trình dòng chảy theo 6 họ sản phẩm chủ lực CADIVI."""
    return PRODUCT_FLOWS


def get_product_flow(flow_id):
    """Lấy chi tiết 1 luồng sản phẩm theo mã (vd: 'F01')."""
    if not flow_id:
        return None
    fid = flow_id.strip().upper()
    for fl in PRODUCT_FLOWS:
        if fl["id"].upper() == fid:
            return fl
    return None


def get_scenario_groups():
    """Trả về danh sách bộ lọc 8 nhóm tình huống thực chiến."""
    return SCENARIO_GROUPS


def get_scenarios():
    """Trả về toàn bộ 40 tình huống thực chiến OE dưới xưởng CADIVI."""
    return SCENARIOS


def get_scenario(scenario_id):
    """Lấy chi tiết 1 tình huống theo mã (vd: 'SC16')."""
    if not scenario_id:
        return None
    scid = scenario_id.strip().upper()
    for sc in SCENARIOS:
        if sc["id"].upper() == scid:
            return sc
    return None


def search_scenarios(keyword="", group="Tất cả 8 nhóm tình huống", station_id="ALL"):
    """Lọc nhanh 60fps 40 tình huống thực chiến theo từ khóa, nhóm và trạm."""
    kw = (keyword or "").strip().lower()
    results = []
    for sc in SCENARIOS:
        if group and group != "Tất cả 8 nhóm tình huống" and sc.get("group") != group:
            continue
        if station_id and station_id != "ALL" and sc.get("station_id") != station_id:
            continue
        if kw:
            hay = " ".join([
                sc.get("id", ""),
                sc.get("title", ""),
                sc.get("group", ""),
                sc.get("station_id", ""),
                sc.get("symptom", ""),
                sc.get("impact", ""),
                sc.get("rca", ""),
                sc.get("oe_solution", ""),
                sc.get("lock_in", ""),
                " ".join(sc.get("key_terms", [])),
            ]).lower()
            if kw not in hay:
                # Hỗ trợ tìm từ khi văn bản chứa công thức [[Key|Display]]
                import re as _re
                clean_hay = _re.sub(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]", lambda m: (m.group(2) or m.group(1)), hay)
                if kw not in clean_hay:
                    continue
        results.append(sc)
    return results
