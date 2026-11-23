# -*- coding: utf-8 -*-
"""
oe_curriculum.py — Giáo Trình Học Từng Bước Một (Từ Con Số 0 → Chuyên Gia OE Nhà Máy Dây Cáp Điện CADIVI)

Cấu trúc chuẩn 8 Học Phần (Modules) — 32 Bài Học Tuần Tự (L1.1 → L8.3):
  - Học Phần 1 (4 bài): Nhập môn Nhà máy Dây Cáp Điện CADIVI, Máy móc, Tiêu chuẩn & An toàn EHS/LOTO/ISO
  - Học Phần 2 (4 bài): Đo lường Hiệu suất Máy & Lao động (OEE m/phút, TEEP, OLE, Time Study, Work Sampling, Yamazumi, Headcount)
  - Học Phần 3 (4 bài): Lean Manufacturing, VSM, AutoCAD Layout, SMED Máy Đùn & Hệ thống Duy trì LSW/LPA/ADKAR
  - Học Phần 4 (5 bài): Chất lượng Toàn chuỗi (7 QC Tools, FPY/RTY), Six Sigma DMAIC, Minitab SPC/t-test, Đùn Sâu & Đứt Sợi Đồng, Lab QA/QC & MOC
  - Học Phần 5 (4 bài): Hoạch định S&OP–MPS–MRP–RCCP–CRP, Cây BOM Cáp & Copper Give-away/Over-thickness, TOC/Cut-Length, Standard Cost/WCM/SEC/ROI
  - Học Phần 6 (4 bài): Bảo trì Hiện đại TPM/PdM, Số hóa ISA-95/MES/ERP, Tự động hóa Excel/VBA/Python & Power BI Dashboard
  - Học Phần 7 (4 bài): Giải 3 Đề Thi Thực Hành Vòng 2, Kịch bản Phỏng vấn STAR / Phản biện CV & Tổng duyệt 128 Câu Hỏi
  - Học Phần 8 (3 bài): Cẩm nang Hành động Thực tế Ngày 1 → Ngày 90 Khi Trúng Tuyển OE CADIVI Miền Trung

Mỗi bài học có đủ 6 phần thực hành và dùng công thức tường minh [[TermKey|Text]] để click tra cứu tức thì!
"""

MODULES = [
    {"id": "M1", "title": "Học Phần 1: Nhập Môn Nhà Máy Cáp Điện CADIVI, Máy Móc, Tiêu Chuẩn & An Toàn"},
    {"id": "M2", "title": "Học Phần 2: Đo Lường Hiệu Suất Máy & Lao Động (OEE, TEEP, OLE, Time Study, Cân Bằng Chuyền)"},
    {"id": "M3", "title": "Học Phần 3: Lean Manufacturing, VSM, Layout AutoCAD, SMED & Duy Trì Bền Vững"},
    {"id": "M4", "title": "Học Phần 4: Chất Lượng Toàn Chuỗi, Six Sigma DMAIC, Minitab & Công Nghệ Đùn – Đứt Sợi"},
    {"id": "M5", "title": "Học Phần 5: Hoạch Định S&OP–MRP–CRP, Định Mức BOM Cáp, TOC & Tối Ưu Giá Thành"},
    {"id": "M6", "title": "Học Phần 6: Bảo Trì TPM/PdM & Số Hóa Dữ Liệu (MES/ERP, Excel/Python, Power BI)"},
    {"id": "M7", "title": "Học Phần 7: Luyện Đề Thi Thực Hành Vòng 2 & Chinh Phục Phỏng Vấn CADIVI"},
    {"id": "M8", "title": "Học Phần 8: Kế Hoạch Hành Động Thực Chiến Ngày 1 → Ngày 90 Tại CADIVI Miền Trung"},
]

LESSONS = [
    # =========================================================================
    # HỌC PHẦN 1: NHẬP MÔN NHÀ MÁY DÂY CÁP ĐIỆN CADIVI (4 BÀI)
    # =========================================================================
    {
        "id": "L1.1",
        "module_id": "M1",
        "title": "Bài 1.1: Hiểu Tận Gốc Vị Trí Chuyên Viên OE Là Gì? Phân Biệt OE – IE – QA – Quản Đốc Tại CADIVI",
        "duration": "45 phút",
        "prereq": "Không yêu cầu (Bắt đầu từ số 0)",
        "objectives": [
            "Hiểu rõ 7 đầu việc thực tế trong JD Chuyên viên Tối ưu Quy trình (OE) tại Nhà máy CADIVI Miền Trung (KCN Hòa Cầm, Đà Nẵng).",
            "Phân biệt rạch ròi vai trò của OE với Kỹ sư IE truyền thống, QA/QC, Kỹ thuật Công nghệ và Quản đốc phân xưởng.",
            "Nhận diện 4 thế mạnh sẵn có của bản thân (Kỹ sư Cơ khí, Time Study, Python/VBA/Excel, kinh nghiệm dây dẫn/QC) khớp với vị trí OE."
        ],
        "core_theory": (
            "1. **[[OE|Operational Excellence (OE)]] là ai trong nhà máy?** Hãy hình dung Nhà máy CADIVI như một vận động viên marathon: Quản đốc phân xưởng điều hành chạy đúng tiến độ từng ca, QA/QC kiểm tra xem sản phẩm có đạt chuẩn không, Bảo trì sửa khi máy hỏng — còn Chuyên viên **OE** là **'bác sĩ vận hành & kiến trúc sư dữ liệu'** nhìn xuyên suốt toàn bộ 7 công đoạn để tìm ra chỗ nào đang mất tốc độ ([[OEE]]), chỗ nào tốn công thừa ([[OLE]]), chỗ nào rò rỉ đồng/nhựa ([[BOM]]), rồi dẫn dắt liên phòng ban giải quyết tận gốc và chứng minh bằng tiền thật ([[ROI]]).\n"
            "2. **Phân biệt nhanh 4 vai trò hay nhầm:**\n"
            "   • **IE (Industrial Engineer):** Tập trung đo chuẩn thời gian ([[Time Study]]), định mức lao động, bố trí mặt bằng.\n"
            "   • **QA/QC:** Tập trung kiểm định chất lượng mẫu đạt tiêu chuẩn [[IEC 60228]] / [[IEC 60502]] / [[QCVN 4]] và xử lý khiếu nại.\n"
            "   • **Kỹ thuật Công nghệ:** Chịu trách nhiệm thiết kế kết cấu cáp, công thức nhựa, thông số máy.\n"
            "   • **OE (Operational Excellence):** Tích hợp cả công cụ IE + [[Lean]] + [[Six Sigma]] + Phân tích dữ liệu ([[Excel]]/[[Power BI]]/[[Minitab]]) + Kinh tế sản xuất để nâng hiệu suất toàn nhà máy!\n"
            "3. **Bản đồ 7 trách nhiệm cốt lõi theo JD CADIVI:** (1) Đo năng lực & hao phí, (2) Đánh giá hiệu quả máy–người–vật tư–chi phí, (3) Phân tích [[OEE]]/[[OLE]] tìm [[Bottleneck]], (4) Triển khai [[Lean]] ([[5S]], [[Kaizen]], [[VSM]], [[SMED]], [[Poka-Yoke]]), (5) Đánh giá Trước–Sau bằng thống kê & [[ROI]], (6) Phối hợp liên phòng ban & [[MES]], (7) Lập báo cáo quản trị định hướng cho Ban Giám đốc."
        ),
        "worked_example": (
            "• **Kịch bản phân vai thực tế tại CADIVI:** Tháng này chi phí nhựa PVC vượt định mức +4%. QA đo thấy sản phẩm vẫn đạt chuẩn độ dày (không bị mỏng); Quản đốc bảo máy vẫn chạy bình thường. Chính Chuyên viên **OE** lấy dữ liệu [[Laser Gauge]] chạy [[Minitab]] phát hiện công nhân đang đùn dày thừa +0.08 mm ([[Over-thickness]]) vì sợ mỏng, sau đó phối hợp Kỹ thuật & Sản xuất hiệu chỉnh quy trình giúp tiết kiệm hàng trăm triệu đồng/năm!"
        ),
        "hands_on_drill": (
            "• **Bài tập 5 phút:** Viết ra 1 đoạn tự giới thiệu 60 giây trả lời câu 'Em hiểu vị trí Chuyên viên OE tại CADIVI sẽ làm gì mỗi ngày và điểm mạnh của em là gì?' theo 3 ý: (1) Hiểu đúng 3 bài toán lớn nhất của nhà máy cáp (OEE/SMED – BOM đồng/nhựa – Số hóa dữ liệu), (2) Chứng minh bằng 3 thành tích thật (Time Study Canon INEX 60s→30s, Tự động hóa Python/VBA/Excel, Nền tảng QC/dây dẫn), (3) Tinh thần bám [[Genba]] không ngại xuống xưởng."
        ),
        "checkpoints": [
            "Sự khác biệt lớn nhất giữa một người làm QA/QC và một Chuyên viên OE là gì?",
            "Trong nhà máy dây cáp điện, khoản chi phí nào chiếm tỷ trọng lớn nhất (80–88%) giá thành sản phẩm?",
            "Nếu Quản đốc xưởng nói 'tôi cần thêm người/thêm máy', câu hỏi đầu tiên OE phải đặt ra là gì?"
        ],
        "key_terms": ["OE", "Lean", "Six Sigma", "OEE", "OLE", "BOM", "Genba", "ROI"],
        "doc_key": "oe_six_sigma_dmaic",
        "interview_category": "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE"
    },
    {
        "id": "L1.2",
        "module_id": "M1",
        "title": "Bài 1.2: Chuỗi Công Nghệ 7 Công Đoạn & 9 Nhóm Máy Móc Trong Nhà Máy Dây Cáp Điện CADIVI",
        "duration": "60 phút",
        "prereq": "Bài 1.1",
        "objectives": [
            "Thuộc làu hành trình biến 1 cuộn đồng thanh Ø 8mm thành cuộn dây dân dụng VC hoặc cáp lực CXV/DSTA hoàn chỉnh.",
            "Nhận diện đúng tên, chức năng và điểm tổn thất OE của 9 nhóm máy móc chính trong nhà máy CADIVI.",
            "Hiểu sự khác nhau giữa gia công cáp ruột đồng và cáp ruột nhôm (ACSR, ABC)."
        ],
        "core_theory": (
            "1. **Hành trình 7 công đoạn cốt lõi:**\n"
            "   • **Bước 1 — Kéo sợi (Wire Drawing):** Cuộn đồng Rod Ø 8.0 mm (hoặc nhôm Rod Ø 9.5 mm) đi qua máy kéo thô [[RBD]] → xuống máy kéo trung/tinh [[Multi-wire]] qua 9–24 cấp khuôn kim cương [[PCD]] ngâm trong bể dầu nhũ tương [[Drawing Emulsion]] để kéo mảnh xuống Ø 0.2–3.0 mm.\n"
            "   • **Bước 2 — Ủ mềm ([[Annealing]]):** Sợi đồng sau kéo bị cứng giòn do biến cứng nguội → cần đi qua bộ ủ liên tục (Inline Annealer bằng dòng điện) hoặc lò ủ chuông chân không để lấy lại độ mềm dẻo (độ giãn dài ≥ 20–25%) và độ dẫn điện ≥ 100% [[IACS]].\n"
            "   • **Bước 3 — Bện ruột dẫn (Stranding):** Ghép xoắn nhiều sợi đơn thành lõi cáp dẫn điện bằng máy [[Buncher]] (cho dây mềm dân dụng Class 5) hoặc máy bện lồng cứng [[Rigid Strander]] (cho cáp lực lớn Class 2, có thể bện nén tròn hoặc bện rẻ quạt).\n"
            "   • **Bước 4 — Đùn bọc cách điện ([[Extruder]]):** Ruột dẫn đi qua [[Pay-off]] → đầu chữ thập [[Crosshead]] (bộ Chày–Cối bọc nhựa [[PVC]] / [[XLPE]] / [[LSZH]] nóng chảy) → máng làm mát [[Cooling Trough]] → máy đo đường kính [[Laser Gauge]] → máy kiểm tra thủng cách điện cao áp [[Spark Tester]] → bánh kéo [[Capstan]] → trống thu [[Take-up]].\n"
            "   • **Bước 5 — Lưu hóa XLPE (Crosslinking):** Nhựa [[XLPE]] cần tạo liên kết ngang chịu nhiệt 90°C bằng công nghệ ủ hơi ẩm [[Silane]] (hạ thế) hoặc dây chuyền ống lưu hóa liên tục [[CCV]] (trung thế) hoặc chiếu xạ [[E-beam]] (cáp Solar).\n"
            "   • **Bước 6 — Ghép lõi, Giáp bảo vệ & Bọc vỏ ngoài:** Ghép 2–4 lõi màu (Đỏ–Vàng–Xanh–Đen) trên máy [[Drum Twister]] + độn PP → quấn giáp 2 băng thép [[DSTA]] (nếu là cáp ngầm) → đùn lớp vỏ bảo vệ ngoài + in phun thông số CADIVI.\n"
            "   • **Bước 7 — Kiểm nghiệm Lab & Đóng gói:** Thử nghiệm điện trở [[Kelvin Bridge]], ngâm nước cao áp [[Water Immersion]], phóng điện cục bộ [[Partial Discharge|PD]] → Cuộn khoanh 100m hoặc đóng rulo gỗ xuất kho!"
        ),
        "worked_example": (
            "• **Bản đồ tổn thất OE theo từng nhóm máy:** Máy kéo RBD/Multi-wire hay mất OEE vì **đứt sợi & mòn khuôn PCD** (gây [[Copper Give-away]]); Máy bện hay mất OLE vì **1 người đứng ít máy & thay suốt lẻ tẻ**; Máy đùn hay mất OEE vì **đổi màu/tiết diện lâu ([[SMED]]) & phế đầu ca** + mất tiền nhựa vì **[[Over-thickness]]**; Ghép lõi hay mất đồng vì **lệch chiều dài 3 pha cắt bỏ đuôi rulo**!"
        ),
        "hands_on_drill": (
            "• **Bài tập vẽ sơ đồ 5 phút:** Gấp tài liệu lại, lấy tờ giấy trắng tự vẽ lại chuỗi 7 công đoạn từ Cuộn Đồng Rod 8mm đến Rulo cáp `CXV/DSTA 3×50+1×25`, ghi tên ít nhất 1 máy chính và 1 lỗi OE lớn nhất ở mỗi công đoạn!"
        ),
        "checkpoints": [
            "Vì sao sợi đồng sau khi kéo qua máy RBD bắt buộc phải qua công đoạn Ủ mềm (Annealing)?",
            "Phân biệt công dụng của máy Buncher và máy Rigid Strander?",
            "Laser Gauge và Spark Tester nằm ở vị trí nào trên dây chuyền đùn và dùng để bắt lỗi gì?"
        ],
        "key_terms": ["RBD", "Multi-wire", "PCD", "Annealing", "Buncher", "Rigid Strander", "Extruder", "Crosshead", "Laser Gauge", "Spark Tester", "Drum Twister", "DSTA"],
        "doc_key": "cable_mfg_machines",
        "interview_category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)"
    },
    {
        "id": "L1.3",
        "module_id": "M1",
        "title": "Bài 1.3: Giải Mã Toàn Bộ Ký Hiệu Cáp CADIVI & 5 Bộ Tiêu Chuẩn Kỹ Thuật Sống Còn (IEC / TCVN / QCVN 4)",
        "duration": "45 phút",
        "prereq": "Bài 1.2",
        "objectives": [
            "Nhìn bất kỳ mã cáp CADIVI nào (VC, VCm, CVV, CXV/DSTA, ABC, ACSR, CXV/FR, H1Z2Z2-K) đều đọc vanh vách cấu tạo từ trong ra ngoài.",
            "Hiểu ý nghĩa kỹ thuật & tác động trực tiếp tới chi phí BOM của 5 tiêu chuẩn IEC 60228, IEC 60502, TCVN 6610, QCVN 4 và ASTM B49."
        ],
        "core_theory": (
            "1. **Bảng giải mã chữ cái ký hiệu cáp CADIVI (Cực dễ nhớ):**\n"
            "   • **Ruột dẫn:** `C` = Đồng (Copper); `A` = Nhôm (Aluminum); `m` = Mềm nhiều sợi mảnh; `d` = Đôi dẹt; `t` = Đôi tròn.\n"
            "   • **Cách điện & Vỏ:** `V` = [[PVC]]; `X` = [[XLPE]] (chịu nhiệt 90°C, chịu dòng tải lớn hơn PVC 70°C); `LSHF`/`LSZH` = [[LSZH]] chậm cháy ít khói không halogen.\n"
            "   • **Lớp đặc biệt:** `DSTA` = Giáp 2 băng thép mạ kẽm ([[DSTA]]); `DATA` = Giáp 2 băng nhôm (cho cáp 1 lõi chống dòng xoáy); `FR` = Chống cháy băng [[Mica FR]]; `Sc` = Màn chắn băng/lưới đồng chống nhiễu ([[Braiding]]); `ABC` = [[ABC Cable|Cáp nhôm vặn xoắn treo trên không]]; `ACSR` = [[ACSR|Dây nhôm trần lõi thép]]; `H1Z2Z2-K` = [[Solar Cable|Cáp năng lượng mặt trời]].\n"
            "2. **5 Bộ tiêu chuẩn OE bắt buộc nắm (vì chúng định nghĩa ranh giới tiết kiệm đồng & nhựa!):**\n"
            "   • **[[IEC 60228]] / TCVN 6612:** Quy định **Điện trở DC tối đa ở 20°C** cho từng tiết diện danh định → Không quy định cứng đường kính mm mà quy định trần điện trở! Đây là gốc rễ bài toán giảm [[Copper Give-away]].\n"
            "   • **[[IEC 60502]] / TCVN 5935:** Cáp điện lực đùn (1–30 kV), quy định công thức chiều dày cách điện tối thiểu `t_min ≥ 0.9 × t_nom − 0.1 mm` → Gốc rễ bài toán giảm [[Over-thickness]].\n"
            "   • **[[QCVN 4]] / TCVN 6610 (IEC 60227):** Quy chuẩn pháp lý BẮT BUỘC gắn dấu hợp quy CR cho dây dân dụng bọc PVC 450/750V.\n"
            "   • **[[ASTM B49]]:** Quy chuẩn đồng Rod Ø 8mm đầu vào (Cu ≥ 99.90%, ≥ 100% [[IACS]]).\n"
            "   • **IEC 60331 / 60332:** Tiêu chuẩn cáp chống cháy duy trì mạch điện 750–950°C ([[Mica FR]]) và chống cháy lan."
        ),
        "worked_example": (
            "• **Đọc mẫu 3 mã cáp kinh điển tại CADIVI Miền Trung:**\n"
            "  1. `VCm 2.5 - 450/750V`: Dây đơn mềm ruột đồng nhiều sợi (`C`+`m`), cách điện PVC (`V`), tiết diện 2.5 mm², điện áp 450/750V (chịu quản lý bắt buộc [[QCVN 4]]).\n"
            "  2. `CXV/DSTA 3×50+1×25 - 0.6/1kV`: Cáp ngầm hạ thế ruột đồng (`C`), cách điện XLPE (`X`), giáp 2 băng thép (`DSTA`), vỏ PVC (`V`), gồm 3 lõi pha 50 mm² + 1 lõi trung tính 25 mm².\n"
            "  3. `ABC 4×50 - 0.6/1kV`: Cáp nhôm vặn xoắn treo cột 4 lõi nhôm 50 mm² bọc XLPE đen chống tia UV (không có vỏ bọc chung)."
        ),
        "hands_on_drill": (
            "• **Bài tập giải mã nhanh:** Tự dịch sang cấu tạo đầy đủ 4 mã cáp sau: (a) `CVV 4×16`, (b) `CXV/DATA 1×240`, (c) `CXV/FR/LSHF 2×2.5`, (d) `ACSR 240/32`. Sau đó tính `t_min` cho phép theo [[IEC 60502]] nếu chiều dày danh định `t_nom = 1.2 mm` (Đáp án: `0.9 × 1.2 − 0.1 = 0.98 mm`)."
        ),
        "checkpoints": [
            "Vì sao cáp 1 lõi ngầm dùng giáp băng nhôm (DATA) thay vì giáp băng thép (DSTA)?",
            "IEC 60228 kiểm soát ruột dẫn bằng tiêu chí đường kính hay tiêu chí điện trở DC ở 20°C?",
            "Nếu giảm chiều dày vỏ cáp xuống sát chuẩn QCVN 4 quá mức, rủi ro pháp lý gì sẽ xảy ra?"
        ],
        "key_terms": ["IEC 60228", "IEC 60502", "QCVN 4", "ASTM B49", "XLPE", "PVC", "LSZH", "DSTA", "ACSR", "ABC Cable", "Mica FR", "Solar Cable"],
        "doc_key": "cable_mfg_machines",
        "interview_category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)"
    },
    {
        "id": "L1.4",
        "module_id": "M1",
        "title": "Bài 1.4: An Toàn Xưởng Cáp (EHS & LOTO 6 Bước) và Bộ Tứ Hệ Thống ISO 9001–14001–45001–50001",
        "duration": "40 phút",
        "prereq": "Bài 1.2",
        "objectives": [
            "Thuộc lòng 6 bước quy trình khóa-thẻ an toàn LOTO và Tháp kiểm soát rủi ro 5 bậc EHS trước khi bước xuống xưởng.",
            "Hiểu rõ 4 rủi ro tai nạn đặc thù của nhà máy dây cáp điện và nguyên tắc bất di bất dịch 'An toàn trên hết' khi làm SMED/Layout.",
            "Nắm vai trò thực tế của 4 chuẩn ISO (9001, 14001, 45001, 50001) trong công việc hàng ngày của Chuyên viên OE."
        ],
        "core_theory": (
            "1. **4 Mối nguy sinh tử trong nhà máy dây cáp điện:** (1) Cuốn kẹp cơ khí ở trống bện quay tốc độ cao, bánh kéo [[Capstan]], máy kéo [[RBD]]; (2) Bỏng nhiệt 180–220°C ở đầu máy đùn & hơi nóng bể lưu hóa; (3) Điện giật cao áp ở [[Spark Tester]] (10–25 kV) & bể thử [[Water Immersion]] / [[Partial Discharge|PD]]; (4) Va chạm xe nâng chở rulo 2–5 tấn & lăn rulo.\n"
            "2. **Quy trình [[LOTO]] 6 bước bắt buộc (nguyên tắc 1 Người – 1 Khóa – 1 Chìa):** (1) Thông báo → (2) Tắt máy bình thường → (3) Cô lập toàn bộ nguồn năng lượng (điện, khí nén, thủy lực, hơi nóng, thế năng rulo) → (4) Gắn Khóa cá nhân + Thẻ cảnh báo → (5) Xả năng lượng tồn dư → (6) **Try-Out** bấm nút Start xác nhận Zero Energy rồi trả về OFF!\n"
            "3. **Tháp 5 bậc kiểm soát rủi ro [[EHS]]:** Loại bỏ → Thay thế → Kiểm soát kỹ thuật (Rào chắn liên động Interlock, chụp hút khói, bàn nâng [[Ergonomics]]) → Kiểm soát hành chính ([[SOP]], [[LOTO]]) → Bảo hộ PPE (hàng rào cuối cùng!).\n"
            "4. **Bộ tứ ISO nhà máy CADIVI:** [[ISO 9001]] (Chất lượng, SOP, hiệu chuẩn, NCR/CAPA) · [[ISO 14001]] (Môi trường, dầu nhũ tương thải, khói nhựa) · [[ISO 45001]] (An toàn nghề nghiệp, HIRA, Near-Miss) · [[ISO 50001]] (Quản lý năng lượng `kWh/tấn`, [[VFD]], dịch chuyển tải giờ thấp điểm!)."
        ),
        "worked_example": (
            "• **Tình huống đạo đức nghề nghiệp OE:** Một công nhân máy bện đề xuất nối tắt công tắc cửa rào an toàn để đỡ mất 10 giây chờ trống dừng mỗi lần mở cửa → OE kiên quyết **TỪ CHỐI** vì vi phạm nghiêm trọng [[EHS]]/[[ISO 45001]], đồng thời phối hợp Cơ điện lắp phanh hãm điện tử giúp trống dừng êm trong 3 giây (vừa an toàn tuyệt đối vừa nhanh hơn 7 giây!)."
        ),
        "hands_on_drill": (
            "• **Bài tập tình huống:** Bạn chuẩn bị thực hiện dự án [[SMED]] thay lưới lọc [[Screen Pack]] và bộ Chày–Cối trên máy đùn PVC đang nóng 175°C. Hãy liệt kê đủ 6 bước [[LOTO]] và 3 thiết bị bảo hộ PPE bắt buộc trước khi chạm tay vào đầu đùn."
        ),
        "checkpoints": [
            "Vì sao chỉ bấm nút Dừng Khẩn Cấp (E-Stop) KHÔNG được coi là đã thực hiện LOTO?",
            "Bước số 6 (Try-Out) trong quy trình LOTO dùng để ngăn chặn tai nạn gì?",
            "ISO 50001 liên kết trực tiếp với chỉ số chi phí nào của Chuyên viên OE?"
        ],
        "key_terms": ["EHS", "LOTO", "ISO 9001", "ISO 14001", "ISO 45001", "ISO 50001", "Ergonomics", "VFD"],
        "doc_key": "planning_quality_ehs_cost",
        "interview_category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành"
    },

    # =========================================================================
    # HỌC PHẦN 2: ĐO LƯỜNG HIỆU SUẤT MÁY & LAO ĐỘNG (4 BÀI)
    # =========================================================================
    {
        "id": "L2.1",
        "module_id": "M2",
        "title": "Bài 2.1: Làm Chủ OEE Theo Tốc Độ Mét/Phút, 6 Tổn Thất Lớn & Chỉ Số TEEP Thẩm Định Mua Máy",
        "duration": "60 phút",
        "prereq": "Bài 1.2",
        "objectives": [
            "Tính thành thạo A, P, Q và OEE cho dây chuyền cáp điện liên tục (tính theo mét/phút thay vì chiếc/giây).",
            "Phân rã chính xác mọi phút dừng máy và phế phẩm vào đúng 6 Tổn thất lớn (Six Big Losses).",
            "Biết dùng TEEP để phản biện đề xuất mua thêm máy mới (CAPEX) khi nhà máy chưa khai thác hết thời gian lịch."
        ],
        "core_theory": (
            "1. **Bộ công thức [[OEE]] chuẩn ngành dây cáp điện (Continuous Line Speed):**\n"
            "   • `Planned Time = Tổng thời gian ca − Thời gian nghỉ kế hoạch (ăn ca, họp giao ban kế hoạch)`.\n"
            "   • `A (Availability) = Operating Time / Planned Time` (Tổn thất 1: Breakdown hỏng máy; Tổn thất 2: Setup/Đổi màu–tiết diện).\n"
            "   • `P (Performance) = Tổng Mét Chạy Ra / (Operating Time × Tốc độ định mức chuẩn m/phút)` (Tổn thất 3: Dừng vặt < 5p; Tổn thất 4: Chạy chậm hơn tốc độ chuẩn).\n"
            "   • `Q (Quality) = Mét Đạt Chuẩn / Tổng Mét Chạy Ra` (Tổn thất 5: Phế khởi động/đổi màu; Tổn thất 6: Phế lỗi Spark/lệch tâm trong ca).\n"
            "   • `OEE = A × P × Q` (Chuẩn World-Class ≥ 85%; nhà máy công nghiệp trung bình 60–70%).\n"
            "2. **Phân biệt [[OEE]] vs [[TEEP]]:** `TEEP = OEE × (Planned Time / Tổng thời gian lịch 24×7)`. OEE đánh giá hiệu quả trong ca mở máy; TEEP đánh giá mức khai thác tài sản trên toàn bộ 168 giờ/tuần để thẩm định [[CAPEX]]."
        ),
        "worked_example": (
            "• **Bài toán mẫu máy đùn dây VC 2.5 mm²:** Ca 480p, nghỉ ăn ca 30p → Planned = 450p. Dừng đổi màu 35p + thay rulo 24p + lỗi Spark 16p + nghẹt lưới 15p = 90p [[Downtime]] → Operating = 360p → `A = 360/450 = 80.00%`. Tốc độ chuẩn = 350 m/p; chạy ra 108,000m → `P = 108,000 / (360×350) = 85.71%`. Cắt phế 5,400m → Đạt 102,600m → `Q = 102,600/108,000 = 95.00%`. **`OEE = 80.0% × 85.71% × 95.0% = 65.14%`**!"
        ),
        "hands_on_drill": (
            "• **Bài tập tự bấm máy tính:** Một máy kéo sợi chạy ca 480p (ăn ca 30p), dừng đứt sợi 45p và thay khuôn 30p; tốc độ định mức 1,200 m/phút; tổng mét kéo ra 382,500m, trong đó có 12,500m lỗi bề mặt cắt bỏ. Hãy tính A, P, Q và OEE! *(Đáp án đối chiếu: Planned=450p, Run=375p → A=83.33%; P=382,500/[375×1,200]=85.00%; Q=370,000/382,500=96.73%; OEE=68.52%)*."
        ),
        "checkpoints": [
            "Vì sao tuyệt đối KHÔNG được tính OEE tuần bằng cách lấy hàm AVERAGE của 15 con số OEE từng ca?",
            "Nếu máy đùn đạt OEE = 88% nhưng nhà máy vẫn trễ giao hàng và lỗ, nguyên nhân có thể là gì?",
            "Khi nào OE dùng TEEP thay vì OEE để thuyết phục Ban Giám đốc?"
        ],
        "key_terms": ["OEE", "TEEP", "Six Big Losses", "Downtime", "CAPEX", "Loss Tree"],
        "doc_key": "oee",
        "interview_category": "OEE & 6 Tổn Thất Lớn"
    },
    {
        "id": "L2.2",
        "module_id": "M2",
        "title": "Bài 2.2: Làm Chủ OLE, Time & Motion Study (Tính SAM) và Lấy Mẫu Công Việc (Work Sampling)",
        "duration": "60 phút",
        "prereq": "Bài 2.1",
        "objectives": [
            "Tính thành thạo 3 trụ cột của chỉ số OLE và quy đổi phút công lãng phí thành tiền lương thất thoát VNĐ/tháng.",
            "Thực hiện đúng 6 bước Time & Motion Study từ bấm giờ thực tế đến tính Thời gian chuẩn SAM có Allowances.",
            "Biết chọn và tính cỡ mẫu Work Sampling (Tippett) cho công việc chu kỳ dài (xe nâng, bảo trì, đứng đa máy)."
        ],
        "core_theory": (
            "1. **Chỉ số [[OLE]] (Overall Labor Effectiveness):** Đo hiệu quả sử dụng sức lao động theo đúng 3 trụ cột `OLE = Availability × Performance(Utilization) × Quality`:\n"
            "   • `A_L = Thời gian làm việc thực / Tổng thời gian chấm công` (tổn thất do chờ rulo, chờ lệnh).\n"
            "   • `P_L = (Tổng sản lượng × Thời gian chuẩn SAM) / Thời gian làm việc thực` (tổn thất do thao tác thừa Motion, chuyền lệch).\n"
            "   • `Q_L = Sản lượng đạt chuẩn ngay / Tổng sản lượng`.\n"
            "2. **Quy trình tính [[Time Study|SAM]]:** `Normal Time = Observed Time × Performance Rating (%)` → `SAM = Normal Time × (1 + Allowances 12–15%)`. Luôn tách 3 nhóm VA (tạo giá trị), NNVA (phụ trợ cần thiết), NVA (lãng phí phải cắt!).\n"
            "3. **Phương pháp [[Work Sampling]] (Tippett):** Khi không thể đứng bấm giờ liên tục (xe nâng chở rulo, thợ bảo trì đo [[Wrench Time]], công nhân đứng 4 máy bện), dùng chụp mẫu ngẫu nhiên với cỡ mẫu `N = [ Z² × p × (1 − p) ] / e²` (độ tin cậy 95% → `Z = 1.96`)."
        ),
        "worked_example": (
            "• **Bài toán OLE tổ Đóng cuộn 10 người:** 4,500 phút công kế hoạch; chờ vật tư 290p → Thực làm 4,210p (`A = 93.56%`). SAM = 2.0p/cuộn, làm 1,850 cuộn → `P = 3,700/4,210 = 87.89%`. Sửa lại 55 cuộn → Đạt 1,795 cuộn (`Q = 97.03%`). `OLE = 79.79%`. Phút công vô ích = `4,500 − 1,795×2.0 = 910 phút công/ca` ≈ 15.17 giờ công × 60,000đ = **910,200đ/ca → ~47.3 triệu VNĐ/tháng** chỉ trên 1 tổ!"
        ),
        "hands_on_drill": (
            "• **Bài tập 2 ý:** (1) Bạn bấm giờ 15 chu kỳ đóng bao cuộn dây được trung bình 45 giây, công nhân làm khá nhanh (Rating = 110%), phụ cấp Allowances = 15%. Tính SAM! *(Đáp án: 45×1.10×1.15 = 56.93 giây)*. (2) Cần khảo sát tỷ lệ chạy không tải của đội xe nâng (ước lượng p = 0.25, sai số e = ±0.03, Z = 1.96), tính số lượt quan sát N cần thiết! *(Đáp án: 800 lượt)*."
        ),
        "checkpoints": [
            "Làm sao nâng OLE mà KHÔNG bắt công nhân chạy quá sức hay tăng ca?",
            "Tại sao không được chọn mốc giờ tròn cố định (08:00, 09:00...) khi thực hiện Work Sampling?",
            "Khi bấm giờ Time Study, phải làm gì trước tiên để công nhân hợp tác thật lòng thay vì cố tình làm chậm?"
        ],
        "key_terms": ["OLE", "Time Study", "Work Sampling", "Standard Work", "Wrench Time", "Ergonomics"],
        "doc_key": "ole",
        "interview_category": "OLE & Năng Suất Lao Động"
    },
    {
        "id": "L2.3",
        "module_id": "M2",
        "title": "Bài 2.3: Takt Time, Cân Bằng Chuyền (Yamazumi / LBE / SI) & Biểu Đồ Người–Máy (Man-Machine Chart)",
        "duration": "60 phút",
        "prereq": "Bài 2.2",
        "objectives": [
            "Tính đúng Takt Time, Cycle Time, hiệu suất cân bằng chuyền LBE và độ mượt Smoothness Index (SI).",
            "Biết dựng biểu đồ Yamazumi và tái phân bổ thao tác cắt giảm nhân công thừa hoặc nâng sản lượng.",
            "Biết vẽ Biểu đồ Người–Máy (Man-Machine Chart) và bảng SWCT để tối ưu mô hình 1 người đứng nhiều máy tại xưởng cáp."
        ],
        "core_theory": (
            "1. **Cân bằng chuyền cho khu lắp ráp / đóng cuộn:**\n"
            "   • `[[Takt Time]] = Thời gian làm việc ròng / Nhu cầu khách hàng` (luôn đặt Target Cycle Time = 85–90% Takt Time).\n"
            "   • Số người tối thiểu lý thuyết = `Tổng thời gian thao tác (ΣCT) / Takt Time` (làm tròn lên).\n"
            "   • `[[LBE]] = ΣCT / (Số trạm N × CT_max) × 100%` (mục tiêu ≥ 85–90%).\n"
            "   • `[[Smoothness Index]] (SI) = √[ Σ(CT_max − CT_i)² ]` (càng tiến về 0 càng công bằng đều tay!).\n"
            "   • Công cụ tái phân bổ: Biểu đồ [[Yamazumi]] (tách VA/NNVA/NVA → xóa Đỏ NVA → ghép trạm thấp tải → tách bớt thao tác từ trạm vượt Takt).\n"
            "2. **Tối ưu 1 người đứng đa máy bằng [[Man-Machine Chart]] & [[Work Combination Table|SWCT]]:**\n"
            "   • Số máy tối ưu lý thuyết 1 công nhân đứng: `N = (L + M) / (L + W)` (L = thời gian thao tác nạp/gỡ của người, M = thời gian máy tự chạy, W = thời gian đi bộ giữa 2 máy).\n"
            "   • Luôn bố trí **lệch pha khởi động** giữa các máy để tránh 2 máy hết rulo cùng lúc (Interference Loss)!"
        ),
        "worked_example": (
            "• **Cân bằng chuyền 5 trạm đóng cuộn (Takt = 30s):** Hiện trạng 5 người: [29s, 28s, 14s, 25s, 11s] → ΣCT = 107s, LBE = 73.8%, SI = 23.6s. Xóa 11s NVA còn 96s, gom lại thành 4 trạm đều nhau [25s, 24s, 24s, 23s] → Giảm 1 công nhân (-20% lương), năng suất tăng 29s→25s (+16%), LBE vọt lên 96.0%, SI giảm mạnh về 2.45s!"
        ),
        "hands_on_drill": (
            "• **Bài tập Man-Machine Chart máy Bện:** Một máy bện Buncher tự chạy `M = 40 phút`, công nhân thay rulo & nối dây mất `L = 7 phút`, đi bộ sang máy kế bên mất `W = 1 phút`. Tính số máy tối ưu 1 người đứng được và đề xuất số máy thực tế an toàn! *(Đáp án: N = (7+40)/(7+1) = 5.87 → Bố trí 3–4 máy/người có chừa thời gian xử lý đứt sợi đột xuất)*."
        ),
        "checkpoints": [
            "Sự khác nhau giữa Takt Time và Cycle Time là gì?",
            "Nếu LBE = 72% và SI = 28 giây, bước đầu tiên trên biểu đồ Yamazumi bạn phải làm là gì?",
            "Điều kiện kỹ thuật bắt buộc (Jidoka) để 1 công nhân đứng an toàn 4 máy bện cùng lúc là gì?"
        ],
        "key_terms": ["Takt Time", "Cycle Time", "Yamazumi", "LBE", "Smoothness Index", "Man-Machine Chart", "Work Combination Table", "Jidoka"],
        "doc_key": "ole",
        "interview_category": "Cân Bằng Chuyền & Takt Time"
    },
    {
        "id": "L2.4",
        "module_id": "M2",
        "title": "Bài 2.4: Hoạch Định Định Biên Nhân Sự (Headcount), 3 Ca – 4 Kíp, Đường Cong Học Việc & TWI",
        "duration": "45 phút",
        "prereq": "Bài 2.3",
        "objectives": [
            "Lập được bảng tính định biên nhân sự đầy đủ (có OLE, hệ số dự phòng nghỉ phép và giới hạn tăng ca Luật Lao động VN).",
            "Hiểu cơ chế xoay ca 3 Ca – 4 Kíp khi chạy máy liên tục 24/7 và cách dùng Đường cong học việc (Learning Curve) dự báo công nhân mới.",
            "Nắm phương pháp đào tạo nhanh chuẩn hóa TWI (JI/JM/JR) và Ma trận đa kỹ năng (Shojinka)."
        ],
        "core_theory": (
            "1. **Công thức [[Headcount Planning|Định biên nhân sự]] thực tế:**\n"
            "   • `Định biên = [ Tổng giờ công tiêu chuẩn / (Giờ ròng 1 người × OLE mục tiêu) ] × (1 + Tỷ lệ vắng mặt/nghỉ phép 6–8%)`.\n"
            "   • Luôn tuân thủ Luật Lao động VN: Tăng ca ≤ 40 giờ/tháng, ≤ 200 giờ/năm (tối đa 300 giờ/năm với ngành đặc thù). Khi cần chạy 24/7 (lò [[CCV]]/máy đùn cao điểm), dùng mô hình **3 Ca – 4 Kíp** (3 kíp chạy 8h/ca, 1 kíp nghỉ xoay vòng).\n"
            "2. **Dự báo năng suất công nhân mới với [[Learning Curve]] (Quy luật 80–85%):** Mỗi lần sản lượng tích lũy tăng gấp đôi, thời gian thao tác giảm xuống còn 80–85% (`Y_n = Y_1 × n^b`) → Không đặt định mức 100% ngay tuần đầu cho thợ mới!\n"
            "3. **Đào tạo tốc độ cao bằng [[TWI]] & linh hoạt hóa nhân lực [[Shojinka]]:** Lập Ma trận Đa kỹ năng (Skill Matrix L1–L4) để chủ động luân chuyển công nhân giữa các xưởng dư tải và quá tải theo mùa vụ đơn hàng."
        ),
        "worked_example": (
            "• **Kịch bản tăng đơn hàng +30% mùa cao điểm CADIVI:** Thay vì tuyển ồ ạt 12 người mới (tốn thời gian học việc 1 tháng & dư thừa sau mùa cao điểm) hoặc ép tăng ca 70h/tháng vi phạm luật, OE điều chuyển 4 công nhân đa kỹ năng từ Xưởng Kéo (tải 75%) sang mở Ca 3 cục bộ cho 2 máy Đùn cổ chai và tuyển thời vụ đơn giản cho khâu đóng gói!"
        ),
        "hands_on_drill": (
            "• **Bài tập định biên:** Xưởng đóng gói cần xuất 4,500 cuộn dây/ngày, SAM = 1.2 phút/cuộn, mỗi ca ròng 450 phút, OLE mục tiêu 80%, dự phòng nghỉ phép 7%. Hãy tính số công nhân cần thiết cho cả 2 ca! *(Đáp án: Tổng công = 5,400p; mỗi người tạo 450×0.8=360p → 15 người có mặt × 1.07 = 16.05 → 16–17 người cho 2 ca)*."
        ),
        "checkpoints": [
            "Mô hình 3 Ca – 4 Kíp giải quyết bài toán pháp lý và vận hành nào?",
            "Nếu công nhân mới chỉ đạt 65% tốc độ chuẩn tuần đầu, làm sao kết hợp TWI và Learning Curve để đẩy nhanh tiến độ?",
            "Shojinka yêu cầu những điều kiện gì về Layout và Kỹ năng công nhân?"
        ],
        "key_terms": ["Headcount Planning", "Learning Curve", "TWI", "Shojinka", "OLE", "RCCP"],
        "doc_key": "oe_field_execution_case_test",
        "interview_category": "Hoạch Định Năng Lực, Điều Độ & Chi Phí"
    },

    # =========================================================================
    # HỌC PHẦN 3: LEAN MANUFACTURING, VSM, LAYOUT & SMED (4 BÀI)
    # =========================================================================
    {
        "id": "L3.1",
        "module_id": "M3",
        "title": "Bài 3.1: 8 Lãng Phí TIMWOODS Xưởng Cáp, 5S / Red Tag, Quản Trị Trực Quan & Poka-Yoke",
        "duration": "55 phút",
        "prereq": "Bài 1.2",
        "objectives": [
            "Nhận diện ngay tại hiện trường cả 8 loại lãng phí TIMWOODS ở 4 phân xưởng CADIVI.",
            "Triển khai 5S thực chất (gắn Red Tag, Shadow Board, phân loại 3 thùng phế) chứ không chỉ quét dọn hình thức.",
            "Thiết kế được ít nhất 5 cơ cấu chống sai lỗi Poka-Yoke & Jidoka đặc thù cho dây chuyền cáp điện."
        ],
        "core_theory": (
            "1. **Soi [[TIMWOOD|8 Lãng phí TIMWOODS]] ở CADIVI:** Chú ý đặc biệt 2 loại gây thiệt hại lớn nhất nhưng hay bị bỏ qua: **Overproduction** (chạy thừa mã dễ làm tăng [[WIP]]) và **Overprocessing** (bọc nhựa dư [[Over-thickness]], kéo đồng dư [[Copper Give-away]], nhập số liệu lặp 3 lần!).\n"
            "2. **[[5S]] + [[Red Tag]] + [[Visual Management]]:** Sàng lọc khuôn cũ/rulo hỏng bằng Red Tag → Kẻ vạch sàn phân vùng rõ rệt → Dán bảng Shadow Board dụng cụ SMED → Quy tắc '3 giây – 3 mét' trên mọi đồng hồ áp suất/nhiệt độ & bảng Hour-by-Hour.\n"
            "3. **[[Poka-Yoke]] & [[Jidoka]]:** Đừng kêu công nhân 'cố nhớ cho kỹ' lúc 3 giờ sáng! Hãy khóa lỗi bằng kỹ thuật: Quét [[Barcode]] bao nhựa khớp lệnh SX, cảm biến đứt sợi/đứt băng Mica tự dừng 0.5s, cữ lắp khuôn bất đối xứng, cảm biến quang bắt lỗi mất mực in phun vỏ cáp!"
        ),
        "worked_example": (
            "• **3 Quick-Win 5S + Poka-Yoke chi phí thấp cho tháng đầu tại CADIVI:** (1) Đặt 3 thùng phế sơn 3 màu riêng biệt Xanh/Vàng/Xám tại mỗi máy đùn (tách đồng trần vs đồng dính nhựa vs PVC sạch), (2) Gắn cảm biến kiểm tra nét chữ in phun tự dừng sau 5m lỗi mực (chi phí ~8 triệu, cứu lô cáp trăm triệu), (3) Bảng Shadow Board xe đồ nghề SMED đặt sát đầu máy đùn!"
        ),
        "hands_on_drill": (
            "• **Bài tập thiết kế Poka-Yoke:** Công nhân ca đêm máy đùn thỉnh thoảng nạp nhầm bao hạt PVC cách điện vào phễu máy chạy vỏ PVC (hai loại hạt màu giống hệt nhau). Hãy thiết kế 1 giải pháp Poka-Yoke (ngăn ngừa hoặc phát hiện tức thì) chi phí thấp nhất!"
        ),
        "checkpoints": [
            "Vì sao Overproduction được gọi là 'mẹ của mọi loại lãng phí'?",
            "Kiểm tra 100% bằng mắt thường của QC có được coi là Poka-Yoke không? Tại sao?",
            "S3 (Seiso — Sạch sẽ) trong 5S có ý nghĩa sâu xa gì liên quan đến bảo trì thiết bị?"
        ],
        "key_terms": ["Lean", "TIMWOOD", "5S", "Red Tag", "Visual Management", "Poka-Yoke", "Jidoka", "Kaizen", "SOP"],
        "doc_key": "lean_muda",
        "interview_category": "7 Lãng Phí (TIMWOOD) & 5S"
    },
    {
        "id": "L3.2",
        "module_id": "M3",
        "title": "Bài 3.2: Bản Đồ Chuỗi Giá Trị VSM, Sơ Đồ Spaghetti, Layout AutoCAD & Hệ Thống Kéo Kanban / Milk Run",
        "duration": "60 phút",
        "prereq": "Bài 3.1",
        "objectives": [
            "Vẽ được Current State VSM và thiết kế Future State VSM kèm chỉ số PCE & Kaizen Bursts.",
            "Vẽ sơ đồ Spaghetti trên bản vẽ mặt bằng AutoCAD, áp dụng nguyên tắc bố trí chuyền dài & chuyền chữ U.",
            "Thiết kế hệ thống kéo Pull / Kanban, Two-Bin Kanban và tuyến tiếp liệu Water Spider / Milk Run."
        ],
        "core_theory": (
            "1. **[[VSM]] (Value Stream Mapping):** Đi bộ ngược từ Kho Xuất về Kho Đồng Rod để ghi nhận thực tế C/T, C/O, OEE và số rulo [[WIP]] giữa từng công đoạn → Tính [[Lead Time]] tổng vs Thời gian gia công thực (Process Time) → Áp dụng Định luật Little (`LT = WIP / Throughput`) để cắt thời gian chờ (thường chiếm 90%+ Lead Time!).\n"
            "2. **[[Spaghetti]] & Plant Layout trên [[AutoCAD]]:** Với dây chuyền cáp dài 35–60m, bố trí luồng chữ I thẳng liên hoàn Kéo → Bện → Đùn, tách rõ hành lang xe nâng (rộng ≥ 3.5m) & lối đi người, chừa không gian bảo trì rút trục vít 1.5m; còn khu Đóng cuộn khoanh áp dụng chuyền chữ U + [[One-Piece Flow]].\n"
            "3. **[[Pull System]] + [[Kanban]] + [[Milk Run]]:** Dùng ô sàn giới hạn WIP giữa Bện và Đùn (dây dân dụng); dùng [[Two-Bin Kanban]] cho tem nhãn/màng co/lưới lọc; bố trí nhân sự [[Water Spider]] chạy tuyến [[Milk Run]] mỗi 45–60 phút giao đủ vật tư & thu hồi rulo rỗng!"
        ),
        "worked_example": (
            "• **Tính số ô sàn Kanban giữa Bện & Đùn dây VC 2.5:** Tiêu thụ 16 rulo/ngày, thời gian bổ sung 0.5 ngày, an toàn 25% → `16 × 0.5 × 1.25 = 10 ô vàng`. Kết hợp chuyển 3 xe nâng sang 2 tuyến Milk Run giúp giảm 38% quãng đường chạy không tải và cắt 55% WIP nằm chờ trên sàn!"
        ),
        "hands_on_drill": (
            "• **Bài tập tính PCE trên VSM:** Một đơn hàng cáp lực đi qua 5 công đoạn có tổng thời gian máy chạy thực sự là 16 giờ, nhưng tổng thời gian từ lúc xuất đồng đến lúc nhập kho thành phẩm là 10 ngày làm việc (240 giờ). Tính tỷ lệ PCE (%) và nêu 3 vị trí thường tạo thời gian chờ lớn nhất cần tấn công trước! *(Đáp án: PCE = 16/240 = 6.67%)*."
        ),
        "checkpoints": [
            "Tại sao phải đi bộ ngược dòng dưới xưởng để vẽ VSM thay vì ngồi trên phòng lấy số từ ERP?",
            "Trong xưởng cáp, khi nào nên dùng siêu thị Pull/Kanban và khi nào nên dùng MTO kéo theo đơn hàng?",
            "Vai trò cốt lõi của Water Spider & Milk Run đối với OEE và OLE là gì?"
        ],
        "key_terms": ["VSM", "Lead Time", "WIP", "Spaghetti", "AutoCAD", "One-Piece Flow", "Pull System", "Kanban", "Two-Bin Kanban", "Milk Run", "Water Spider", "FIFO"],
        "doc_key": "autocad_layout",
        "interview_category": "Bố Trí Mặt Bằng & Luồng 1 Sản Phẩm"
    },
    {
        "id": "L3.3",
        "module_id": "M3",
        "title": "Bài 3.3: Làm Chủ Kỹ Thuật SMED 4 Bước Cho Máy Đùn Bọc Cáp (Rút Chuyển Đổi 55 Phút → 12 Phút)",
        "duration": "60 phút",
        "prereq": "Bài 2.2, Bài 3.1",
        "objectives": [
            "Thành thạo quy trình 4 bước của Shigeo Shingo (tách Internal vs External, chuyển Internal → External, tinh gọn Internal).",
            "Áp dụng nhuần nhuyễn 4 vũ khí SMED đặc thù máy đùn cáp điện (Color Sequencing, Purging, Sấy sẵn Tip/Die, Dual Pay-off/Accumulator).",
            "Biết tổ chức kịch bản phối hợp 2 người song song (F1 Pit-Stop) và thiết kế cơ cấu gá kẹp 1 chạm."
        ],
        "core_theory": (
            "1. **Định nghĩa chuẩn giờ [[SMED]]:** Từ mét cáp đạt chuẩn cuối cùng của mã cũ → đến mét cáp đạt chuẩn đầu tiên ở tốc độ danh định của mã mới!\n"
            "2. **4 Bước kinh điển:** (0) Quay video hiện trạng → (1) Tách **Thao tác Trong** (bắt buộc dừng máy) vs **Thao tác Ngoài** (chuẩn bị trước khi máy dừng: lấy hạt nhựa, sấy khô, mang bộ Chày–Cối & đồ nghề đặt sát máy — giảm ngay 30–50% tốn 0 đồng!) → (2) Chuyển Trong thành Ngoài (tủ sấy nóng sẵn đầu [[Crosshead]] 160°C bên ngoài; [[Dual Pay-off|Pay-off]] + [[Accumulator]] + [[Butt Welder]] hàn nối đồng khi máy đang chạy!) → (3) Tinh gọn phần Trong (đầu đùn tự định tâm xóa chỉnh 4 ốc, kẹp 1 chạm, 2 người làm song song, nạp Recipe 1-chạm trên [[HMI]]).\n"
            "3. **Tối ưu điều độ chuyển đổi bằng [[Color Sequencing]] & [[Campaign Scheduling]]:** Xếp chuỗi màu `Trắng → Vàng → Xanh lá → Đỏ → Xanh dương → Đen` (hoặc cấp hạt màu [[Masterbatch]] tại cổ phễu) kết hợp hợp chất xả [[Purging]] giúp cắt 75% lượng nhựa xả!"
        ),
        "worked_example": (
            "• **Case Study máy đùn PVC CADIVI (55p → 12p):** (1) Đổi màu Đen→Trắng 18p → 3p nhờ Color Sequencing + Purging; (2) Lấy & sấy nhựa 10p → 0p (External phễu di động); (3) Tháo lắp chỉnh tâm Tip/Die 12p → 3.5p (đầu tự định tâm); (4) Gia nhiệt đầu mới 8p → 0p (tủ sấy sẵn bên ngoài); (5) Thay rulo & nối dây 4p → 2.5p; (6) Chỉnh tốc độ đạt chuẩn Laser 3p → 3p (nạp Recipe PLC). **Kết quả:** Giảm Downtime 78.2% và giảm phế nhựa xả 25 kg → 6 kg (-76%)!"
        ),
        "hands_on_drill": (
            "• **Bài tập phân loại Internal vs External:** Cho 6 bước đổi mã máy đùn: (a) Đi kho lấy bao nhựa màu mới, (b) Tháo Chày–Cối cũ khỏi đầu đùn, (c) Gia nhiệt Chày–Cối mới lên 165°C, (d) Cân chỉnh đường kính trên Laser Gauge, (e) Đi tìm cờ-lê và lưới lọc mới, (f) Làm sạch lưới lọc cũ vừa tháo ra. Hãy phân loại từng bước sang Internal hay External và đề xuất cách rút ngắn!"
        ),
        "checkpoints": [
            "Bước nào trong 4 bước SMED mang lại hiệu quả giảm thời gian lớn nhất với chi phí gần bằng 0 đồng?",
            "Vì sao đổi màu ngược Đen → Trắng tốn thời gian và phế nhựa gấp 4 lần đổi Trắng → Đen?",
            "Bộ đôi Dual Pay-off + Accumulator + Butt Welder giúp giảm thời gian dừng đổi rulo về mức nào?"
        ],
        "key_terms": ["SMED", "Color Sequencing", "Campaign Scheduling", "Purging", "Masterbatch", "Crosshead", "Pay-off", "Take-up", "Accumulator", "Butt Welder"],
        "doc_key": "smed",
        "interview_category": "SMED & Rút Ngắn Chuyển Đổi"
    },
    {
        "id": "L3.4",
        "module_id": "M3",
        "title": "Bài 3.4: Hệ Thống Duy Trì Cải Tiến Bền Vững — Hoshin Kanri, ADKAR, LSW, LPA & Andon Escalation",
        "duration": "50 phút",
        "prereq": "Bài 3.1, Bài 3.3",
        "objectives": [
            "Hiểu lý do 70% dự án Lean chết yểu sau 3 tháng và cách dùng mô hình ADKAR hóa giải phản kháng của công nhân/tổ trưởng.",
            "Thiết kế được bộ ba duy trì bền vững: Leader Standard Work (LSW), Layered Process Audit (LPA) 3 cấp và Andon Escalation Matrix.",
            "Biết liên kết mục tiêu nhà máy CADIVI từ trên xuống dưới bằng Ma trận X-Matrix của Hoshin Kanri & giao ban Tier 1–2–3."
        ],
        "core_theory": (
            "1. **Triển khai chiến lược bằng [[Hoshin Kanri]] (X-Matrix + Catchball):** Liên kết mục tiêu năm của Ban Giám đốc CADIVI → Top 3–5 dự án OE ưu tiên → [[KPI]] SQDCM hàng ngày tại các tổ.\n"
            "2. **Quản trị thay đổi con người bằng [[ADKAR]]:** Đi đủ 5 bước **Awareness** (cho xưởng thấy nỗi đau thật bằng số liệu) → **Desire** (làm Quick-Win giúp công nhân đỡ cực trước!) → **Knowledge** (OPL/TWI cầm tay chỉ việc) → **Ability** (Pilot 1 máy cùng tổ trưởng giỏi nhất) → **Reinforcement** (chuẩn hóa SOP, thưởng nóng Kaizen).\n"
            "3. **Bộ 3 Khóa Chuẩn Chống Tái Diễn:**\n"
            "   • **[[LSW]] (Leader Standard Work):** Lịch kiểm tra cố định đầu/giữa/cuối ca của Tổ trưởng & Quản đốc.\n"
            "   • **[[LPA]] (Layered Process Audit):** Kiểm tra nhanh 8–10 câu Có/Không ở 3 tầng (Tổ trưởng hàng ngày → Quản đốc/OE hàng tuần → Giám đốc 2 tuần/lần).\n"
            "   • **[[Andon]] + [[Escalation Matrix]]:** Mốc SLA ứng cứu sự cố 5p (Tổ trưởng) → 15p (Bảo trì) → 30p (Quản đốc/OE) → 60p (Giám đốc)."
        ),
        "worked_example": (
            "• **Kịch bản xử lý tổ trưởng phản đối SMED:** Tổ trưởng xưởng Đùn bảo 'mấy cậu kỹ sư văn phòng vẽ chuyện, tụi tôi làm 10 năm nay đổi màu 50 phút quen rồi!'. OE không tranh cãi lý thuyết mà hỏi thăm chỗ anh em cực nhất (bê khuôn nặng & hay phải tăng ca thứ Bảy) → Làm trước xe đẩy khuôn + bảng 5S giúp tổ nhẹ việc (tạo Desire!), mời chính anh tổ trưởng đó đồng dẫn dắt Pilot máy số 1 và báo cáo thành tích vinh danh tổ trước Ban Giám đốc!"
        ),
        "hands_on_drill": (
            "• **Bài tập thiết kế phiếu LPA:** Viết 6 câu hỏi Có/Không thật cụ thể (kiểm được trong 5 phút tại máy đùn bọc cáp) để đưa vào phiếu kiểm tra phân tầng [[LPA]] hàng tuần (bao phủ đủ 4 mảng: An toàn LOTO, Chất lượng Spark/Laser, Chuẩn SMED, 5S & Phân loại phế)."
        ),
        "checkpoints": [
            "Vì sao đào tạo SOP rất kỹ (Knowledge) mà công nhân vẫn không chịu làm theo quy trình mới theo mô hình ADKAR?",
            "Sự khác nhau giữa Standard Work của công nhân và Leader Standard Work (LSW) là gì?",
            "Tại sao LPA bắt buộc phải có sự tham gia định kỳ của cả Giám đốc Nhà máy (Layer 3)?"
        ],
        "key_terms": ["Hoshin Kanri", "ADKAR", "LSW", "LPA", "Andon", "Escalation Matrix", "KPI", "Visual Management"],
        "doc_key": "oe_field_execution_case_test",
        "interview_category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2"
    },

    # =========================================================================
    # HỌC PHẦN 4: CHẤT LƯỢNG, SIX SIGMA DMAIC, MINITAB & ĐÙN SÂU (5 BÀI)
    # =========================================================================
    {
        "id": "L4.1",
        "module_id": "M4",
        "title": "Bài 4.1: Chất Lượng Xuyên Suốt FPY vs RTY (Hidden Factory), DPMO & 7 Công Cụ QC Kinh Điển",
        "duration": "55 phút",
        "prereq": "Bài 1.2",
        "objectives": [
            "Phân biệt Final Yield vs FPY vs RTY và tính được hiệu suất xuyên suốt RTY cho dây chuyền cáp 6 công đoạn.",
            "Quy đổi số lỗi sang DPMO và đối chiếu mức Sigma Level.",
            "Sử dụng đúng lúc cả 7 QC Tools (Check Sheet, Pareto, Fishbone, Histogram, Scatter, Stratification, Control Chart)."
        ],
        "core_theory": (
            "1. **Bóc trần 'Nhà máy ẩn' bằng [[FPY]] & [[RTY]]:**\n"
            "   • Final Yield cuối chuyền che giấu toàn bộ hàng bị sửa lại (Rework/cắt nối) ở giữa đường.\n"
            "   • `[[FPY]] = (Đầu vào − Scrap − Rework) / Đầu vào` (tỷ lệ đạt ngay lần đầu ở 1 công đoạn).\n"
            "   • `[[RTY]] = FPY_1 × FPY_2 × ... × FPY_n` (tỷ lệ một mét cáp đi trót lọt từ đồng rod đến thành phẩm không dính bất kỳ lỗi/sửa chữa nào!).\n"
            "   • `[[DPMO]] = [ Số lỗi / (Số đơn vị × Số cơ hội lỗi) ] × 1,000,000` (3σ ≈ 66,807; 4σ ≈ 6,210; 6σ ≤ 3.4).\n"
            "2. **Làm chủ [[7 QC Tools]]:** [[Pareto]] (chọn 20% lỗi gây 80% thiệt hại) → [[Ishikawa|Xương cá 6M]] + [[5 Whys]] (truy gốc rễ) → [[Histogram]] (xem phân bố lệch hay 2 đỉnh theo ca) → [[Scatter]] (kiểm chứng tương quan X–Y, vd: Nhiệt đầu đùn vs Lệch tâm) → Phân tầng (theo Ca/Máy/Lô nhựa) → [[SPC|Control Chart]] (theo dõi ổn định)."
        ),
        "worked_example": (
            "• **Tính RTY dây chuyền cáp CXV 6 công đoạn tại CADIVI:** Kéo (98%) × Ủ/Bện (99%) × Đùn XLPE (97%) × Lưu hóa (95%) × Ghép lõi/DSTA (96%) × Đùn vỏ/Lab (97%) → **`RTY = 0.98×0.99×0.97×0.95×0.96×0.97 = 83.27%`**! Dù mỗi khâu đều nhìn có vẻ đẹp (95–99%), thực tế gần 17% sản lượng đã rơi vào Hidden Factory phải cắt nối/chạy lại!"
        ),
        "hands_on_drill": (
            "• **Bài tập tính nhanh:** Nếu OE cải tiến khâu Lưu hóa từ FPY 95% → 98.5% và khâu Ghép lõi từ 96% → 98.5% (4 khâu còn lại giữ nguyên), RTY toàn chuỗi tăng lên bao nhiêu %? *(Đáp án: 0.98×0.99×0.97×0.985×0.985×0.97 = 88.57%, tăng thêm +5.3 điểm %!)*."
        ),
        "checkpoints": [
            "Vì sao một cuộn dây có 1 điểm Spark phải đưa sang máy Rewind cắt bỏ 5m chia làm 2 cuộn vẫn được tính là KHÔNG đạt FPY?",
            "Khi nhìn biểu đồ Histogram đường kính cáp thấy xuất hiện 2 đỉnh tách biệt (Bimodal), nguyên nhân thực tế ở xưởng thường là gì?",
            "Sự khác nhau giữa việc dùng Pareto và việc dùng Ishikawa + 5 Whys trong quy trình giải quyết vấn đề?"
        ],
        "key_terms": ["FPY", "RTY", "DPMO", "7 QC Tools", "Pareto", "Ishikawa", "5 Whys", "Histogram", "Scatter", "Scrap"],
        "doc_key": "planning_quality_ehs_cost",
        "interview_category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành"
    },
    {
        "id": "L4.2",
        "module_id": "M4",
        "title": "Bài 4.2: Six Sigma Từ Zero Đến Green Belt & 5 Pha DMAIC (SIPOC, VOC–CTQ, PFMEA, Control Plan)",
        "duration": "65 phút",
        "prereq": "Bài 4.1",
        "objectives": [
            "Hiểu cặn kẽ bản chất toán học của Six Sigma (μ ± 6σ, dịch chuyển 1.5σ, hệ thống đai Green/Black Belt) và Lean Six Sigma.",
            "Nắm chắc mục tiêu & bộ công cụ đầu ra bắt buộc của từng pha trong 5 pha DMAIC.",
            "Biết lập bảng SIPOC, cây chuyển hóa VOC → CTQ, đánh giá rủi ro PFMEA (RPN) và khóa chuẩn bằng Control Plan."
        ],
        "core_theory": (
            "1. **Bản chất [[Six Sigma]] & [[Lean Six Sigma]]:** Nếu [[Lean]] làm quy trình NHANH hơn thì [[Six Sigma]] thu hẹp độ lệch chuẩn `σ` để quy trình CHÍNH XÁC hơn (nhét được 6 lần độ lệch chuẩn `σ` từ tâm đến cận dung sai USL/LSL → kể cả khi tâm dịch dài hạn `1.5σ`, tỷ lệ lỗi vẫn ≤ `3.4 DPMO`, tức 99.99966% đạt chuẩn!). Nắm rõ vai trò [[Green Belt]] trong JD CADIVI.\n"
            "2. **Lộ trình 5 pha [[DMAIC]] chuẩn mực:**\n"
            "   • **D — Define:** Chốt Project Charter (mục tiêu VNĐ/tỷ lệ lỗi), dịch tiếng nói khách hàng [[VOC]] thành chỉ tiêu đo được [[CTQ]], vẽ ranh giới quy trình [[SIPOC]].\n"
            "   • **M — Measure:** BẮT BUỘC kiểm chứng hệ thống đo bằng [[MSA]] / [[Gage R&R]] trước! Sau đó đo năng lực nền (Baseline [[Cpk]] / [[RTY]]).\n"
            "   • **A — Analyze:** Dùng [[Ishikawa]], [[PFMEA]] (tính `RPN = S × O × D`), [[2-Sample t-test]] / [[ANOVA]] / [[Regression]] chứng minh đâu là nguyên nhân gốc thật (`[[p-value]] < 0.05`).\n"
            "   • **I — Improve:** Dùng [[DOE]] tối ưu thông số, chạy thử Pilot, kiểm chứng Trước–Sau và tính [[ROI]].\n"
            "   • **C — Control:** Khóa chặt thành quả bằng [[Control Plan]] (kèm Reaction Plan), [[SPC]], [[Poka-Yoke]], [[SOP]] & [[LPA]]!"
        ),
        "worked_example": (
            "• **Case Study DMAIC giảm phế đùn cáp XLPE tại CADIVI:** D: Giảm phế đùn máy số 4 từ 3.8% xuống < 1.0% (mục tiêu tiết kiệm > 900 tr/năm). M: Chạy Gage R&R kính hiển vi đạt %GRR = 6.2%, đo baseline `σ = 0.055 mm`, `Cpk = 0.85`. A: Phân tích ANOVA/PFMEA tìm ra 2 gốc rễ (độ ẩm hạt nhựa cao & nhiệt nước làm mát > 32°C làm lệch tâm). I: Lắp Hopper Dryer 75°C + bảo trì Chiller + Laser Closed-loop → thu hẹp `σ = 0.020 mm`, `Cpk = 1.67`, phế giảm còn 0.78% (`p-value = 0.000`). C: Đưa vào Control Plan & LPA!"
        ),
        "hands_on_drill": (
            "• **Bài tập lập SIPOC & PFMEA nhanh:** Vẽ bảng 5 cột [[SIPOC]] (S–I–P–O–C) cho công đoạn 'Đùn bọc cách điện XLPE' và tính điểm RPN cho lỗi 'Nhựa ẩm gây thủng Spark Tester' với `Severity = 8`, `Occurrence = 6`, `Detection = 5` *(RPN = 240 — ưu tiên xử lý khẩn cấp!)*."
        ),
        "checkpoints": [
            "Khi nào nên dùng công cụ Kaizen/5S đơn giản và khi nào mới cần mở một dự án Six Sigma DMAIC đầy đủ?",
            "Tại sao trong pha Measure bắt buộc phải làm MSA (Gage R&R) trước khi đo Cpk?",
            "Sự khác nhau giữa chỉ số RPN cũ và Action Priority (AP) trong PFMEA mới (AIAG-VDA)?"
        ],
        "key_terms": ["Six Sigma", "Lean Six Sigma", "Green Belt", "DMAIC", "SIPOC", "VOC", "CTQ", "PFMEA", "Control Plan", "8D", "A3", "PDCA"],
        "doc_key": "oe_six_sigma_dmaic",
        "interview_category": "OE, Six Sigma (DMAIC), TOC, TPM & PFMEA"
    },
    {
        "id": "L4.3",
        "module_id": "M4",
        "title": "Bài 4.3: Thực Hành Thống Kê Minitab — SPC (Xbar-R, Nelson Rules), Cp/Cpk/Ppk, MSA & Chọn Đúng Kiểm Định",
        "duration": "65 phút",
        "prereq": "Bài 4.2",
        "objectives": [
            "Đọc hiểu biểu đồ kiểm soát SPC (Xbar-R, I-MR) và 4 quy tắc Nelson Rules phát hiện bất thường trước khi sinh phế phẩm.",
            "Phân biệt chính xác Cp vs Cpk vs Ppk và hiểu cách xử lý khi Cp cao nhưng Cpk thấp.",
            "Thuộc 'Bản đồ chọn đúng phép kiểm định thống kê' trên Minitab (t-test, ANOVA, Chi-Square, Regression, DOE, Box-Cox)."
        ],
        "core_theory": (
            "1. **[[SPC]] & [[Nelson Rules]]:** Tách biến thiên Tự nhiên (Common Cause) vs Bất thường (Special Cause — 1 điểm vượt `±3σ`, 7–9 điểm nằm cùng 1 phía tâm, 6 điểm tăng/giảm liên tục báo khuôn [[PCD]] đang mòn dần!).\n"
            "2. **[[Cpk]] vs [[Ppk]]:** `Cp = (USL − LSL) / 6σ` đo độ chụm tiềm năng; `Cpk = min[(USL−μ)/3σ, (μ−LSL)/3σ]` đo năng lực ngắn hạn có tính độ lệch tâm (chuẩn đạt ≥ 1.33, tốt ≥ 1.67); `Ppk` dùng `σ_overall` phản ánh năng lực dài hạn qua nhiều ca/lô nhựa. Nếu `Cp = 1.60` nhưng `Cpk = 0.85` → máy rất ổn định nhưng đang bị **lệch tâm** (chỉ cần chỉnh tâm Offset là đẹp ngay!).\n"
            "3. **Kiểm chứng đo lường [[MSA]] / [[Gage R&R]]:** `%GRR < 10%` đạt tốt; `10–30%` chấp nhận có điều kiện; `> 30%` hệ thống đo hỏng!\n"
            "4. **Bản đồ chọn kiểm định [[Minitab]] (nhìn đúng kiểu dữ liệu X & Y):**\n"
            "   • So sánh 2 nhóm liên tục (Trước vs Sau SMED): **[[2-Sample t-test]]** (hoặc Paired t-test nếu đo trên cùng mẫu).\n"
            "   • So sánh ≥ 3 nhóm liên tục (3 ca hoặc 3 nhà cung cấp đồng): **[[ANOVA]]**.\n"
            "   • So sánh tỷ lệ lỗi Đạt/Hỏng giữa các ca/máy (dữ liệu đếm): **[[Chi-Square]]**.\n"
            "   • Tìm phương trình dự báo X liên tục → Y liên tục (Nhiệt độ vs Đường kính): **[[Regression]]**.\n"
            "   • Tìm tổ hợp thông số tối ưu cùng lúc nhiều yếu tố: **[[DOE]]**.\n"
            "   • Dữ liệu bị lệch không phân phối chuẩn trước khi tính Cpk: Biến đổi **[[Box-Cox]]**.\n"
            "   • Đọc kết quả: **[[p-value]] < 0.05** → Khác biệt có ý nghĩa thống kê với độ tin cậy 95%!"
        ),
        "worked_example": (
            "• **Bài toán Cpk chiều dày vỏ cáp:** Yêu cầu `1.20 ± 0.15 mm` (`LSL = 1.05`, `USL = 1.35`). Đo thực tế `μ = 1.26 mm`, `σ = 0.030 mm`. Tính: `Cp = 0.30 / (6×0.03) = 1.67` (máy cực chuẩn!), nhưng `Cpk = min[(1.35−1.26)/0.09, (1.26−1.05)/0.09] = min(1.00, 2.33) = 1.00` (chưa đạt 1.33 vì lệch tâm lên trên +0.06 mm, gây [[Over-thickness]]!) → Chỉnh hạ tâm tốc độ Capstan về `μ = 1.20 mm` lập tức `Cpk = 1.67` và tiết kiệm hàng trăm triệu nhựa!"
        ),
        "hands_on_drill": (
            "• **Bài tập chọn phép kiểm định Minitab:** Xác định dùng phép kiểm định nào cho 3 tình huống tại CADIVI: (1) So sánh số lần lỗi Spark (có/không) giữa 3 ca làm việc? *(Chi-Square)*; (2) So sánh thời gian đổi mã trung bình Trước vs Sau SMED? *(2-Sample t-test)*; (3) So sánh độ lệch tâm trung bình (mm) của 4 máy đùn cùng lúc? *(One-Way ANOVA)*."
        ),
        "checkpoints": [
            "Nếu Cp = 1.80 nhưng Cpk = 0.70, bạn có cần mua máy đùn mới không? Phải làm gì?",
            "p-value = 0.002 có ý nghĩa gì khi trình bày kết quả cải tiến Trước–Sau cho Ban Giám đốc?",
            "Nếu dữ liệu chiều dày đo bằng Panme có %GRR = 35%, bạn có được phép dùng dữ liệu đó kết luận dự án không?"
        ],
        "key_terms": ["Minitab", "SPC", "Cpk", "Ppk", "MSA", "Gage R&R", "Nelson Rules", "2-Sample t-test", "p-value", "ANOVA", "Chi-Square", "Regression", "DOE", "Box-Cox"],
        "doc_key": "minitab_spc",
        "interview_category": "SPC, Minitab & Cp/Cpk"
    },
    {
        "id": "L4.4",
        "module_id": "M4",
        "title": "Bài 4.4: Công Nghệ Đùn Cáp Chuyên Sâu (L/D, Melt Pressure, DDR, Khuyết Tật) & Phân Tích Đứt Sợi Đồng",
        "duration": "65 phút",
        "prereq": "Bài 1.2, Bài 1.3",
        "objectives": [
            "Hiểu sâu cấu tạo trục vít L/D, tín hiệu áp suất Melt Pressure, công thức chọn Chày–Cối DDR/DRB và 5 khuyết tật bề mặt đùn.",
            "Tránh bẫy chi phí hạt nhựa bằng Volume Cost (CaCO3 Filler / Specific Gravity) và quy chuẩn quản trị nhựa tái chế Regrind.",
            "Biết soi mặt gãy đứt sợi đồng (Cup-and-Cone vs Inclusion vs Weld Break) để truy trúng lỗi nội bộ hay lỗi nhà cung cấp."
        ],
        "core_theory": (
            "1. **Trục vít & Áp suất máy đùn:** [[L/D Ratio]] ngắn (`20–24:1`) cho [[PVC]] nhạy nhiệt; dài (`25–30:1`) cho PE/[[XLPE]]; nén thấp (`1.8–2.3:1`) cho [[LSZH]]. Theo dõi [[Melt Pressure]] báo sớm nghẹt [[Screen Pack]] (+25–30% áp suất) hoặc dao động đường kính (Surging).\n"
            "2. **Chọn Chày–Cối bằng [[DDR]] / DRB & xử lý 5 khuyết tật đùn:** Đùn Ống (Tube Tooling: dễ tuốt, tốc độ cao, `DDR PVC 1.5–2.5`, `DRB 0.95–1.08`) vs Đùn Ép (Pressure Tooling: bám chặt). Chẩn đoán nhanh: [[Sharkskin]] (sần da cá mập do quá tốc độ/nhiệt Die thấp), `Bambooing` (trượt Capstan/Surging), [[Die Drool]] (đóng cặn mép cối), `Voids` (nhựa ẩm quên sấy [[Hopper Dryer]]), `Scorch` (cháy xém ngâm nhiệt).\n"
            "3. **Kinh tế hạt nhựa:** Đánh giá bằng `Volume Cost = Giá/kg × [[Specific Gravity]]` (tránh bẫy nhựa rẻ/kg nhưng độn nhiều [[CaCO3 Filler]] làm nặng tỷ trọng → đắt/km!). Quản trị phân loại sạch nhựa nhiệt dẻo [[Regrind]] (PVC) vs nhiệt rắn XLPE không đùn lại được.\n"
            "4. **[[Wire Break Forensics]] (Phân tích mặt gãy đứt sợi đồng):** Hình [[Cup-and-Cone]] = lỗi lực căng/khuôn [[PCD]]/[[Drawing Emulsion|nhũ tương]] nội bộ; Gãy dẹt có tạp chất Inclusion = lỗi đồng Rod đầu vào ([[ASTM B49]]); Gãy phẳng giòn mối hàn = lỗi [[Butt Welder]] quên ủ!"
        ),
        "worked_example": (
            "• **Bài toán phản biện mua nhựa rẻ 2.5%:** Hạt PVC B rẻ hơn 2.5% giá/kg nhưng tỷ trọng tăng từ 1.45 → 1.54 (+6.21%) → Chi phí nhựa trên mỗi km cáp thực tế tăng `0.975 × 1.0621 = 1.0355` (+3.55% ĐẮT HƠN!), chưa kể gây đóng cặn [[Die Drool]] và rớt [[Tensile]]!"
        ),
        "hands_on_drill": (
            "• **Bài tập chẩn đoán Genba:** Trả lời nhanh 3 ca bệnh xưởng cáp: (1) Vỏ cáp HDPE bị sần nhám khi đẩy tốc độ từ 60 lên 85 m/p → Lỗi gì & chỉnh thông số nào? (2) Đồng hồ Melt Pressure tăng từ 180 lên 240 bar ở cùng vòng quay trục vít → Báo hiệu điều gì? (3) Soi 15 đầu sợi đồng đứt thấy 12 đầu có hình chén-côn đối xứng → Truy lỗi xưởng Kéo hay nhà cung cấp đồng?"
        ),
        "checkpoints": [
            "Vì sao chạy nhựa PVC trên trục vít dài L/D 30:1 của PE lại cực kỳ nguy hiểm?",
            "Hậu quả khi công nhân lắp đại cối quá rộng làm DDR = 3.6 vượt xa chuẩn 1.5–2.5 là gì?",
            "Đặc thù tối ưu OE của cáp Solar H1Z2Z2-K và công đoạn bện lưới Braiding là gì?"
        ],
        "key_terms": ["L/D Ratio", "Melt Pressure", "DDR", "Sharkskin", "Die Drool", "CaCO3 Filler", "Specific Gravity", "Regrind", "Wire Break Forensics", "Cup-and-Cone", "Solar Cable", "Tinned Copper", "E-beam", "Braiding", "Water-Blocking"],
        "doc_key": "cable_extrusion_wire_forensics",
        "interview_category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2"
    },
    {
        "id": "L4.5",
        "module_id": "M4",
        "title": "Bài 4.5: Phòng Lab Kiểm Nghiệm Cáp Điện CADIVI & Quy Trình Kiểm Soát Thay Đổi Kỹ Thuật (MOC / ECN)",
        "duration": "45 phút",
        "prereq": "Bài 1.3, Bài 4.4",
        "objectives": [
            "Hiểu rõ mục đích, thông số và mối liên kết trực tiếp với OE của 6 phép thử cốt lõi trong Phòng Lab CADIVI.",
            "Rút ngắn Lead Time chờ kết quả Lab và tận dụng dữ liệu Lab để mở khóa tiết kiệm đồng/nhựa.",
            "Áp dụng quy trình 5 bước MOC/ECN trước mọi thay đổi định mức, công thức nhựa hay tốc độ máy."
        ],
        "core_theory": (
            "1. **6 Phép thử vàng trong Phòng Lab QA/QC Dây Cáp Điện:**\n"
            "   • **Đo điện trở DC 20°C ([[Kelvin Bridge]]):** Kiểm chuẩn [[IEC 60228]] — dữ liệu đầu vào số 1 để tính [[Copper Give-away]].\n"
            "   • **Đo chiều dày & đồng tâm (Kính hiển vi quang học / [[Laser Gauge]]):** Kiểm chuẩn [[IEC 60502]] — dữ liệu đầu vào số 1 để tính [[Over-thickness]].\n"
            "   • **Thử độ giãn dài nóng ([[Hot Set Test]] ở 200°C):** Xác nhận nhựa [[XLPE]] đã lưu hóa đủ liên kết ngang chưa (độ giãn dài tải ≤ 175%, dư sau nguội ≤ 15%).\n"
            "   • **Thử cơ lý kéo đứt ([[Tensile]]) & Lão hóa nhiệt ([[Aging Oven]] 7 ngày):** Xác nhận độ bền vỏ nhựa & tuổi thọ 20–30 năm.\n"
            "   • **Thử cao áp ngâm nước ([[Water Immersion]] 2.5–3.5 kV):** Bắt lỗ kim Pinholes & cách điện ẩm ở cáp hạ thế.\n"
            "   • **Thử Phóng điện cục bộ ([[Partial Discharge|PD]] ≤ 5 pC trong phòng Faraday):** Cửa ải tối hậu của cáp trung thế XLPE 6–35 kV!\n"
            "2. **Quy trình [[MOC / ECN]] 5 bước bắt buộc:** Đề xuất → Thẩm định rủi ro chéo (Kỹ thuật – QA – EHS – BOM) → Chạy Pilot & test đủ Lab → Phê duyệt chính thức → Cập nhật đồng bộ [[SOP]], [[Control Plan]] & MBOM trên [[ERP]]!"
        ),
        "worked_example": (
            "• **Giảm Lead Time chờ Lab bằng tư duy OE:** Khảo sát thấy mỗi cuộn cáp hoàn thiện nằm chờ trung bình 6 giờ mới có giấy xuất xưởng từ Lab do xưởng mang mẫu lên rải rác và chờ ngâm nước 1 giờ lẻ tẻ → Thiết lập lịch gom mẫu cố định (10h – 15h – 21h) + chuẩn bị sẵn đầu tuốt mẫu trước giúp rút thời gian cấp giấy xuống còn 2 giờ!"
        ),
        "hands_on_drill": (
            "• **Bài tập tình huống:** Một lô cáp trung thế 24kV rớt phép thử [[Partial Discharge]] (đo được 18 pC > chuẩn 5 pC). Dựa trên chuỗi công nghệ đã học, hãy liệt kê 3 nguyên nhân gốc tại dây chuyền đùn [[CCV]] cần truy ngược ngay trên [[MES]]!"
        ),
        "checkpoints": [
            "Dù máy đùn đã có Spark Tester trên dây chuyền, vì sao Phòng Lab vẫn phải chạy bài thử Water Immersion?",
            "Phép thử Hot Set Test dùng để kiểm tra loại vật liệu nào và nếu không đạt thì lỗi thường nằm ở khâu nào?",
            "Tại sao không được tự ý hạ chiều dày bọc nhựa toàn xưởng khi chưa chạy quy trình MOC/ECN?"
        ],
        "key_terms": ["Kelvin Bridge", "Hot Set Test", "Tensile", "Aging Oven", "Water Immersion", "Partial Discharge", "Spark Tester", "MOC / ECN"],
        "doc_key": "cable_mfg_machines",
        "interview_category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)"
    },


    # =========================================================================
    # HỌC PHẦN 5: HOẠCH ĐỊNH NĂNG LỰC, BOM CÁP & TỐI ƯU GIÁ THÀNH (4 BÀI)
    # =========================================================================
    {
        "id": "L5.1",
        "module_id": "M5",
        "title": "Bài 5.1: Luồng Hoạch Định 5 Tầng S&OP → MPS → MRP → RCCP → CRP & Tồn Kho Safety Stock / ROP / ABC-XYZ",
        "duration": "60 phút",
        "prereq": "Bài 2.1, Bài 3.2",
        "objectives": [
            "Nắm trọn luồng hoạch định từ chiến lược tháng (S&OP) xuống mã cáp tuần (MPS), phá rã vật tư (MRP), tải thô (RCCP) và tải chi tiết từng máy (CRP).",
            "Tính thành thạo tồn kho an toàn Safety Stock và điểm đặt hàng lại ROP theo công thức thống kê.",
            "Phân khúc danh mục cáp & vật tư theo ma trận 9 ô ABC-XYZ kết hợp Cycle Counting và Kitting."
        ],
        "core_theory": (
            "1. **Chuỗi 5 tầng hoạch định không bị đứt gãy:** [[S&OP]] (3–18 tháng, theo nhóm tấn sản phẩm, Ban Giám đốc chốt Cung = Cầu) → [[MPS]] (4–12 tuần, chi tiết theo mã cáp SKU, kiểm tra tải thô bằng [[RCCP]] có nhân [[OEE]] thực!) → [[MRP]] (phá rã [[BOM]] tính lượng đồng/nhựa cần mua & thời điểm về) → [[CRP]] (kiểm tra tải giờ từng máy cụ thể theo từng ca/ngày để san tải) → Điều độ hiện trường [[MES]]/[[Campaign Scheduling]].\n"
            "2. **Quản trị tồn kho khoa học thay vì cảm tính:**\n"
            "   • `[[Safety Stock]] = Z × √(LT × σ_D² + D̄² × σ_LT²)` (95% → `Z = 1.65`; 98% → `Z = 2.05`).\n"
            "   • `[[ROP]] = (Nhu cầu bình quân/ngày × Lead Time) + Safety Stock`.\n"
            "   • Ma trận [[ABC-XYZ]]: Nhóm **AX** (dây dân dụng VC bán đều, giá trị cao) chạy Pull/Siêu thị & giao JIT; Nhóm **AZ** (cáp dự án đặc thù) chạy MTO theo đơn hàng; Nhóm **CX** (tem/màng co) chạy [[Two-Bin Kanban]].\n"
            "   • Giữ độ chính xác kho ERP (RIA ≥ 98.5%) bằng [[Cycle Counting]] luân phiên (A đếm tuần, B tháng, C quý) và soạn sẵn [[Kitting]]."
        ),
        "worked_example": (
            "• **Tính Safety Stock & ROP hạt XLPE Silane tại CADIVI:** Tiêu thụ `D̄ = 4.0 tấn/ngày` (`σ_D = 0.8`), Lead Time nhập `12 ngày` (`σ_LT = 2`), phục vụ 95% (`Z = 1.65`) → `SS = 1.65 × √(12×0.64 + 16×4) = 14.0 tấn` → **`ROP = 4×12 + 14 = 62.0 tấn`**. Khi tồn khả dụng trên [[ERP]] chạm 62 tấn, hệ thống tự phát yêu cầu mua mới!"
        ),
        "hands_on_drill": (
            "• **Bài tập kiểm tra tải RCCP:** Xưởng Đùn có 4 máy, mỗi máy chạy 390 giờ kế hoạch/tháng, OEE thực lịch sử 65%. Tháng tới cần chạy 1,180 giờ máy ròng. Tính Giờ khả dụng thực tế, % Tải (Load%) và số giờ thiếu hụt! *(Đáp án: Khả dụng = 4×390×0.65 = 1,014h; Load% = 116.4%; thiếu 166 giờ ròng)*."
        ),
        "checkpoints": [
            "Khác biệt cốt lõi giữa RCCP (tầng MPS) và CRP (tầng MRP) là gì?",
            "Tại sao MRP truyền thống có thể tạo ra lịch sản xuất bất khả thi nếu không kiểm tra năng lực?",
            "Nếu không có Cycle Counting mà tồn kho ERP bị lệch 6%, hệ thống MRP sẽ gặp hậu quả gì?"
        ],
        "key_terms": ["S&OP", "MPS", "MRP", "RCCP", "CRP", "Safety Stock", "ROP", "ABC-XYZ", "Cycle Counting", "Kitting"],
        "doc_key": "planning_quality_ehs_cost",
        "interview_category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành"
    },
    {
        "id": "L5.2",
        "module_id": "M5",
        "title": "Bài 5.2: Cây Định Mức BOM Đa Tầng Cáp Điện & Giải Mã 2 Mỏ Vàng Copper Give-away / Over-thickness",
        "duration": "65 phút",
        "prereq": "Bài 1.3, Bài 4.3",
        "objectives": [
            "Tính thành thạo khối lượng đồng/nhôm lý thuyết có hệ số xoắn Lay-up Factor và khối lượng nhựa bọc hình vành khăn cho 1 km cáp.",
            "Định lượng chính xác thiệt hại VNĐ/năm từ Copper Give-away (+0.01 mm đồng) và Over-thickness (+0.08 mm nhựa).",
            "Biết cách bóc tách BOM Variance để phân biệt lỗi công nghệ, lỗi vận hành và lỗi tỷ trọng nguyên liệu."
        ],
        "core_theory": (
            "1. **2 Công thức vàng cốt lõi của ngành dây cáp điện (BẮT BUỘC THUỘC):**\n"
            "   • **Khối lượng Đồng ruột dẫn (kg/km):** `M_Cu = N_sợi × (π/4 × d²) × 8.89 × [[Lay-up Factor]]` (Nhôm thay `8.89` bằng `2.70`; hệ số xoắn bện thường `1.015 – 1.045`).\n"
            "   • **Khối lượng Nhựa cách điện / vỏ (kg/km):** `M_nhựa = 0.7854 × (D_ngoài² − D_trong²) × [[Specific Gravity|Tỷ trọng nhựa]]` (XLPE ~0.92; PVC ~1.40–1.50; LSZH ~1.50).\n"
            "2. **2 'Mỏ vàng tỷ đồng' của Chuyên viên OE CADIVI:**\n"
            "   • **[[Copper Give-away]] (Dư đường kính đồng):** Chỉ cần kéo thừa `+0.01 mm` trên sợi Ø 1.78 mm, diện tích (khối lượng) tăng `+1.13%` (do tỷ lệ bình phương `d²`!) — trên sản lượng 200 tấn đồng/tháng (~50 tỷ đồng tiền đồng), `+1.13%` là **~565 triệu/tháng (~6.7 tỷ VNĐ/năm)** biếu không khách hàng! Giải pháp: Kiểm soát vòng đời khuôn [[PCD]], chọn đồng Rod có `% [[IACS]]` cao, kéo tâm sát cận dưới điện trở [[IEC 60228]] bằng [[SPC]].\n"
            "   • **[[Over-thickness]] (Bọc dư chiều dày nhựa):** Do máy đùn lệch tâm/dao động rộng (`σ` lớn), công nhân chỉnh bọc thừa +0.08 mm để né lỗi mỏng → Dùng [[Laser Gauge]] Closed-loop + [[SPC]] thu hẹp `σ` kéo tâm về `t_min + 4σ` tiết kiệm ngay 2–4% nhựa (hàng tỷ đồng/năm)!"
        ),
        "worked_example": (
            "• **Tính nhanh thiệt hại +0.01 mm đường kính sợi đồng Ø 1.78 mm:** Tỷ lệ tăng khối lượng = `(1.79² − 1.78²) / 1.78² = (3.2041 − 3.1684) / 3.1684 = +1.127%`. Với sản lượng 200 tấn/tháng × giá đồng 250 triệu/tấn = 50 tỷ/tháng → Thiệt hại ròng = `50 tỷ × 1.127%` = **563.5 triệu VNĐ/tháng = 6.76 tỷ VNĐ/năm**!"
        ),
        "hands_on_drill": (
            "• **Bài tập tính khối lượng nhựa:** Một sợi lõi đồng có đường kính `D_trong = 4.0 mm`, bọc lớp nhựa PVC tỷ trọng `1.45 g/cm³` với chiều dày danh định `1.0 mm` (`D_ngoài = 6.0 mm`). Tính khối lượng nhựa PVC cho 1 km dây, và tính xem nếu bọc dư thêm `+0.10 mm` mỗi phía (`D_ngoài = 6.2 mm`) thì khối lượng nhựa tăng thêm bao nhiêu %? *(Đáp án: Chuẩn = 0.7854×(36−16)×1.45 = 22.78 kg/km; Dư = 0.7854×(38.44−16)×1.45 = 25.56 kg/km → Tăng tới +12.2% tiền nhựa!)*."
        ),
        "checkpoints": [
            "Vì sao độ tinh khiết đồng (% IACS tăng từ 100% lên 101.2%) lại giúp giảm Copper Give-away?",
            "Nếu Laser Gauge đo chiều dày vỏ hoàn toàn đúng chuẩn nhưng báo cáo BOM vẫn báo vượt kg nhựa +3%, bạn phải kiểm tra thông số nào của lô hạt nhựa?",
            "Sự khác nhau giữa EBOM và MBOM trong nhà máy cáp điện là gì?"
        ],
        "key_terms": ["BOM", "Lay-up Factor", "Copper Give-away", "Over-thickness", "Specific Gravity", "IACS", "IEC 60228", "IEC 60502", "Laser Gauge"],
        "doc_key": "cable_cost_capacity",
        "interview_category": "Định Mức BOM & Hao Phí"
    },
    {
        "id": "L5.3",
        "module_id": "M5",
        "title": "Bài 5.3: Lý Thuyết Điểm Nghẽn TOC (Drum-Buffer-Rope), Tối Ưu Cắt Rulo (Cut-Length) & Quản Trị Phế Liệu",
        "duration": "55 phút",
        "prereq": "Bài 5.1, Bài 5.2",
        "objectives": [
            "Áp dụng nhuần nhuyễn 5 bước tập trung TOC và cơ chế Drum-Buffer-Rope để giải tỏa điểm nghẽn nhà máy mà không sinh WIP.",
            "Giải bài toán tối ưu chiều dài cắt rulo (Cut-Length / Backward Length Planning) bằng Excel Solver / Python.",
            "Phân tách và kiểm soát đúng 3 nhóm phế liệu đặc thù CADIVI (Đồng trần / Đồng dính nhựa / Nhựa xả)."
        ],
        "core_theory": (
            "1. **5 Bước [[TOC]] & [[Drum-Buffer-Rope]]:** (1) Tìm đúng [[Bottleneck]] (thường là Đùn hoặc Giáp/Lưu hóa) → (2) Khai thác tối đa không tốn CAPEX (SMED, ăn ca luân phiên, không chạy phôi lỗi vào cổ chai) → (3) Đồng bộ hóa toàn xưởng theo nhịp cổ chai bằng **Drum (Lịch cổ chai) – Buffer (Đệm 1 ca trước cổ chai) – Rope (Kìm đầu vào Xưởng Kéo)** → (4) Nâng cấp (mở Ca 3 cục bộ / mua máy) → (5) Lặp lại khi điểm nghẽn dịch chuyển.\n"
            "2. **Bài toán [[Cut-Length]] & Backward Length Planning:** Khi ghép cáp 3–4 lõi pha (Đỏ–Vàng–Xanh–Đen), chỉ cần 1 lõi bị thiếu 20m do sai số Encoder đo mét ở máy đùn trước đó → Phải cắt bỏ **20m × 3 lõi còn lại = 60m đồng bọc nhựa phế**! Giải pháp: Hiệu chuẩn Encoder định kỳ hàng tuần, lập kế hoạch chiều dài ngược từ bước cuối (Backward Length Planning) và ghép các đoạn lẻ đơn hàng bằng [[Excel|Excel Solver]] / [[Python]] (`PuLP`) đạt hiệu suất dùng rulo 98.5–99.5%!\n"
            "3. **Quản trị 3 nhóm [[Scrap|Phế liệu]]:** Tách sạch 100% **Đồng trần** (~94% thu hồi) khỏi **Đồng dính nhựa** (lỗ ròng gấp 4 lần!) và **Nhựa PVC sạch** ([[Regrind]])."
        ),
        "worked_example": (
            "• **Ghép cắt rulo 2,000m cho đơn hàng đoạn lẻ:** Thay vì cắt 1 đoạn 650m + 1 đoạn 1,100m rồi bỏ mẩu dư 250m (phế 12.5%), bộ tối ưu Solver ghép tổ hợp `650 + 650 + 680 + 20m đầu-đuôi = 2,000m` → Tỷ lệ tận dụng đạt **99.0%**, giảm mẩu cắt thừa gần về 0!"
        ),
        "hands_on_drill": (
            "• **Bài tập quản trị Buffer DBR:** Xưởng Bện cung cấp 10 rulo/ca cho Xưởng Đùn (cổ chai). Nếu đặt Buffer chuẩn 9 rulo trước máy Đùn (Vùng Xanh 7–9, Vàng 4–6, Đỏ ≤ 3), khi thấy trên sàn chỉ còn đúng 3 rulo đồng bện, toàn bộ các bộ phận (Bện, Kéo, Bảo trì, Kế hoạch) phải hành động gì ngay lập tức?"
        ),
        "checkpoints": [
            "Vì sao đặt tồn kho đệm Buffer ở PHÍA SAU điểm nghẽn không giúp tăng sản lượng nhà máy?",
            "Tại sao 100 kg phế cáp đồng dính nhựa XLPE lại gây thiệt hại ròng gấp hơn 4 lần 100 kg phế đồng trần?",
            "Làm sao chấm dứt tình trạng 3 lõi pha ghép lại bị lệch chiều dài đuôi rulo 20–30 mét?"
        ],
        "key_terms": ["TOC", "Bottleneck", "Drum-Buffer-Rope", "Cut-Length", "Scrap", "Regrind", "WIP"],
        "doc_key": "cable_cost_capacity",
        "interview_category": "Hoạch Định Năng Lực, Điều Độ & Chi Phí"
    },
    {
        "id": "L5.4",
        "module_id": "M5",
        "title": "Bài 5.4: Kế Toán Giá Thành (Standard Cost), Cây Tổn Thất Tiền (WCM), Điện Năng (SEC) & Thẩm Định ROI",
        "duration": "60 phút",
        "prereq": "Bài 5.2, Bài 2.1",
        "objectives": [
            "Đọc hiểu & giải trình 4 loại chênh lệch giá thành Standard Cost Variance với Phòng Kế toán và Ban Giám đốc.",
            "Lập được Bảng Cost Deployment (WCM) & OEE Waterfall quy đổi mọi tổn thất xưởng sang tiền VNĐ/tháng.",
            "Tính chuẩn cường độ điện năng SEC (kWh/tấn) và xây bảng thẩm định ROI / Payback Period 3 kịch bản độ nhạy."
        ],
        "core_theory": (
            "1. **4 Nhánh Chênh lệch [[Standard Cost]]:** (1) *Material Price Variance* (giá đồng LME/nhựa — phòng Mua hàng chịu trách nhiệm), (2) ***Material Usage Variance*** (đồng/nhựa tiêu hao vượt BOM — **Mũi nhọn #1 của OE**!), (3) ***Labor Efficiency Variance*** (giờ công vượt chuẩn — **Mũi nhọn #2 của OE**!), (4) ***Overhead Absorption Variance*** (phân bổ khấu hao & điện cố định theo sản lượng [[OEE]] — **Mũi nhọn #3 của OE**!).\n"
            "2. **[[Loss Tree]] & [[Cost Deployment]] (WCM):** Xếp hạng tất cả tổn thất hiện trường theo **VNĐ/tháng** để dồn lực đánh đúng 2–3 dự án lớn nhất.\n"
            "3. **Tối ưu Cường độ Điện năng `[[SEC]] = kWh / Tấn` ([[ISO 50001]]):** Bọc áo cách nhiệt nòng đùn + giảm đùn chờ nhiệt không tải (Idle Heating) + dịch chuyển lò ủ/xông XLPE sang giờ thấp điểm 22:00–04:00 (đơn giá điện rẻ hơn 2.5–3 lần!) + lắp [[VFD]] cho bơm/quạt + vá rò khí nén.\n"
            "4. **Thẩm định [[CAPEX]] / [[ROI]] / [[Payback]]:** Chỉ tính **Hard Savings** có Kế toán xác nhận, trừ đủ chi phí vận hành/bảo trì, lập đủ 3 kịch bản (Thận trọng / Cơ sở / Lạc quan) và cam kết chạy Pilot 1 máy kiểm chứng [[2-Sample t-test]] trước khi mua hàng loạt!"
        ),
        "worked_example": (
            "• **Thẩm định lắp Laser Gauge Closed-loop (420 triệu):** Tiết kiệm thận trọng 2.5% trên 120 tấn nhựa/tháng = 3.0 tấn × 32tr = **96 triệu/tháng** (Hard Savings). Kịch bản Cơ sở: Payback = `420 / 96 = 4.38 tháng`; Kịch bản Thận trọng (1.5% = 57.6 tr/tháng): Payback = `7.3 tháng`; Kịch bản Lạc quan (3.2% + giảm phế đầu ca = 135 tr/tháng): Payback = `3.1 tháng` → Rủi ro cực thấp, Ban Giám đốc duyệt ngay!"
        ),
        "hands_on_drill": (
            "• **Bài tập phân tích Standard Cost:** Tháng này giá đồng thực tế tăng từ 240tr → 250tr/tấn; xưởng sản xuất 100 km cáp (định mức chuẩn 1.0 tấn/km = 100 tấn) nhưng thực xuất 103 tấn đồng. Hãy tách chính xác Material Price Variance và Material Usage Variance (VNĐ)! *(Đáp án: Price Variance = (250−240)×103 = +1,030 triệu [do thị trường]; Usage Variance = (103−100)×240 = +720 triệu [do xưởng/OE phải xử lý!])*."
        ),
        "checkpoints": [
            "Hard Savings khác Soft Savings ở điểm nào và tại sao Kế toán trưởng chỉ công nhận Hard Savings khi tính ROI?",
            "Tại sao nâng OEE giúp tự động giảm giá thành Overhead/km cáp ngay cả khi tổng lương và khấu hao không đổi?",
            "Liệt kê 4 cách giảm cường độ điện năng SEC (kWh/tấn) trong nhà máy dây cáp điện!"
        ],
        "key_terms": ["Standard Cost", "Cost Deployment", "Loss Tree", "SEC", "ISO 50001", "VFD", "CAPEX", "ROI", "Payback"],
        "doc_key": "planning_quality_ehs_cost",
        "interview_category": "Hoạch Định Năng Lực, Điều Độ & Chi Phí"
    },

    # =========================================================================
    # HỌC PHẦN 6: BẢO TRÌ TPM/PdM & SỐ HÓA DỮ LIỆU SẢN XUẤT (4 BÀI)
    # =========================================================================
    {
        "id": "L6.1",
        "module_id": "M6",
        "title": "Bài 6.1: Bảo Trì Hiện Đại TPM (8 Trụ Cột), Jishu Hozen, MTBF/MTTR, PM Compliance, Wrench Time & PdM",
        "duration": "55 phút",
        "prereq": "Bài 2.1, Bài 2.2",
        "objectives": [
            "Hiểu 8 trụ cột TPM và cách triển khai Bảo trì Tự quản Jishu Hozen (CIL 7 phút đầu ca) cùng công nhân xưởng cáp.",
            "Tính đúng MTBF, MTTR, PM Compliance và đo nâng cao Wrench Time của đội Cơ Điện.",
            "Ứng dụng 4 công cụ Bảo trì Dự đoán (CBM/PdM) chi phí thấp cho nhà máy cáp điện."
        ],
        "core_theory": (
            "1. **[[TPM]] & [[Jishu Hozen]]:** Phá vỡ bức tường 'tôi chạy máy, anh đi sửa' bằng 7 bước Jishu Hozen & bộ kiểm tra **CIL** (Lau chùi – Kiểm tra – Bôi trơn) đầu ca kết hợp thẻ bất thường [[Red Tag|Fuguai]].\n"
            "2. **Bộ 4 KPI Bảo trì OE cần theo dõi cùng Cơ Điện:**\n"
            "   • **[[MTBF]]** = Tổng giờ chạy thực / Số lần hỏng đột xuất (đo độ tin cậy — càng cao càng tốt).\n"
            "   • **[[MTTR]]** = Tổng giờ dừng sửa đến khi ra hàng đạt / Số lần hỏng (đo tốc độ khôi phục — rút bằng [[Escalation Matrix]] + kho phụ tùng 5S).\n"
            "   • **[[PM Compliance]]** ≥ 90% (khóa khung giờ giao máy PM cố định trên lịch [[MPS]]).\n"
            "   • **[[Wrench Time]]** (tỷ lệ thời gian thợ bảo trì thực sự thao tác kỹ thuật — đo bằng [[Work Sampling]], nâng từ ~30% lên 50%+ nhờ [[Kitting]] phụ tùng PM!).\n"
            "3. **[[CBM / PdM]] (Bảo trì dự đoán theo đường cong P–F):** Dùng Camera ảnh nhiệt soi tủ điện/điện trở đùn, bút đo rung vòng bi máy kéo/bện, siêu âm rò khí nén và biểu đồ [[Melt Pressure]] thay lưới [[Screen Pack]] trước khi nghẹt!"
        ),
        "worked_example": (
            "• **Tính hiệu quả tăng Wrench Time đội Cơ Điện 8 người:** Nâng Wrench Time từ 32% lên 48% bằng Kitting phụ tùng PM + 5S tủ đồ nghề → Năng lực thực làm tăng tương đương từ 2.56 lên 3.84 kỹ thuật viên liên tục (**+50% năng lực bảo trì không tốn tiền tuyển thêm 4 thợ!**)."
        ),
        "hands_on_drill": (
            "• **Bài tập tính MTBF & MTTR:** Một máy đùn trong tháng chạy tổng cộng 400 giờ thực tế, gặp 5 lần hỏng sự cố đột xuất làm mất tổng cộng 200 phút dừng sửa chữa. Tính MTBF (giờ), MTTR (phút) và tỷ lệ Availability kỹ thuật! *(Đáp án: MTBF = 80 giờ; MTTR = 40 phút = 0.667h; Availability kỹ thuật = 80 / 80.667 = 99.17%)*."
        ),
        "checkpoints": [
            "Trong 4 đoạn thời gian cấu thành MTTR, đoạn nào OE có thể cắt giảm nhanh nhất mà không cần thay thiết bị?",
            "Nếu Sản xuất liên tục từ chối giao máy cho Bảo trì làm PM vì đơn hàng gấp, OE giải quyết mâu thuẫn này thế nào?",
            "Nêu 4 thiết bị kiểm tra CBM/PdM giá hợp lý nhưng hiệu quả cao nhất cho nhà máy dây cáp điện CADIVI!"
        ],
        "key_terms": ["TPM", "Jishu Hozen", "MTBF", "MTTR", "PM Compliance", "Wrench Time", "CBM / PdM", "Red Tag"],
        "doc_key": "oe_field_execution_case_test",
        "interview_category": "OE, Six Sigma (DMAIC), TOC, TPM & PFMEA"
    },
    {
        "id": "L6.2",
        "module_id": "M6",
        "title": "Bài 6.2: Kiến Trúc Số Hóa Nhà Máy ISA-95 — Từ PLC / HMI / SCADA → MES → ERP SAP PP & Barcode Rulo",
        "duration": "55 phút",
        "prereq": "Bài 1.2, Bài 5.1",
        "objectives": [
            "Hiểu rõ ranh giới và cách truyền dữ liệu giữa 5 tầng kim tự tháp ISA-95.",
            "Phân biệt chính xác chức năng của PLC, HMI, SCADA, MES và ERP (SAP PP) trong nhà máy cáp điện.",
            "Thiết kế được luồng quét Barcode/QR quản lý rulo bán thành phẩm, chống nhầm vật tư và truy xuất nguồn gốc 100%."
        ],
        "core_theory": (
            "1. **Kim tự tháp [[ISA-95]] (đi từ máy lên Ban Giám đốc):** Tầng 0–1 (Dây chuyền + Cảm biến [[Laser Gauge]], [[Spark Tester]], Encoder, [[Melt Pressure]]) → Tầng 2 ([[PLC]] điều khiển mili-giây, [[HMI]] màn hình tại máy nạp Recipe, [[SCADA]] giám sát tập trung & lưu Historian) → Tầng 3 ([[MES]] điều hành lệnh SX theo ca/giờ, tính [[OEE]] thời gian thực, ghi nhận [[Downtime]], phả hệ rulo) → Tầng 4 ([[ERP]] / [[SAP PP]] quản trị S&OP/MRP, BOM, tồn kho, kế toán [[Standard Cost]]).\n"
            "2. **Lộ trình số hóa thông minh (không đốt tiền):** Bước 1: Chuẩn hóa dữ liệu nguồn (12–15 mã Downtime chuẩn, mã phế tách 3 loại, Master Data MBOM/Routing sạch trên ERP) → Bước 2: Dùng [[Barcode|QR Code]] chịu dầu dán thẻ rulo bán thành phẩm (tương tự dự án RE7 Fujikura của bạn!) → Bước 3: Kết nối tín hiệu chạy/dừng & đếm mét PLC vào Mini-MES / MES chính thức!"
        ),
        "worked_example": (
            "• **Luồng dữ liệu khép kín 1 lệnh cáp CXV 10 km trên ISA-95:** ERP (SAP PP) phát lệnh sản xuất `WO-2026-089` → MES nhận lệnh đẩy Recipe xuống HMI máy đùn → Công nhân quét mã QR bao nhựa XLPE xác nhận đúng mã (Poka-Yoke) → Trong ca, PLC tự gửi mét chạy, đường kính Laser & điểm Spark về MES → Cuối ca MES in tem QR dán rulo và tự đẩy số mét đạt + kg phế thực tế ngược về SAP PP quyết toán BOM!"
        ),
        "hands_on_drill": (
            "• **Bài tập thiết kế bảng mã Downtime chuẩn MES:** Hãy nhóm gọn toàn bộ sự cố thực tế tại Xưởng Đùn CADIVI vào tối đa **12 mã lý do dừng máy** sao cho vừa ngắn gọn dễ bấm trên màn hình HMI, vừa ánh xạ chính xác vào 6 Big Losses & đúng bộ phận chịu trách nhiệm (SX / Bảo trì / Kế hoạch / Kho / QA)."
        ),
        "checkpoints": [
            "Khác biệt giữa HMI, SCADA và MES là gì?",
            "Tại sao không nên triển khai phần mềm MES đắt tiền ngay khi xưởng chưa chuẩn hóa bảng mã dừng máy và định mức tốc độ chuẩn?",
            "Lợi ích kép (về cả OLE lẫn Poka-Yoke) của việc dán thẻ QR chịu dầu lên từng rulo bán thành phẩm?"
        ],
        "key_terms": ["ISA-95", "PLC", "HMI", "SCADA", "MES", "ERP", "SAP PP", "Barcode"],
        "doc_key": "erp_mes",
        "interview_category": "ERP/MES & Quản Lý Genba"
    },
    {
        "id": "L6.3",
        "module_id": "M6",
        "title": "Bài 6.3: Thực Chiến Excel Power Query, VBA Macro & Python Tự Động Hóa Báo Cáo Sản Xuất 1-Chạm",
        "duration": "55 phút",
        "prereq": "Bài 2.1, Bài 5.2",
        "objectives": [
            "Dùng Power Query Folder Connector gộp tự động hàng chục file nhật ký ca Excel thành 1 bảng dữ liệu sạch chuẩn chỉ bằng 1 nút Refresh.",
            "Biết khi nào nên dùng Excel công thức/Pivot, khi nào dùng Power Query, khi nào dùng VBA Macro và khi nào dùng Python (Pandas/PuLP).",
            "Chuyển hóa trực tiếp thành tích tự động hóa tại Mabuchi (3–7 ngày→2h, 120p→15p) thành giải pháp cụ thể cho 30 ngày đầu tại CADIVI."
        ],
        "core_theory": (
            "1. **Bộ công cụ tự động hóa 4 tầng cho Chuyên viên OE:**\n"
            "   • **[[Excel]] Nâng cao:** `XLOOKUP`, `SUMIFS`, `Pivot Table`, `Excel Solver` (tối ưu [[Cut-Length]]). Quy tắc vàng: Bảng dữ liệu thô chuẩn bảng phẳng (Flat Table), tuyệt đối KHÔNG Merge Cells!\n"
            "   • **[[Power Query]]:** Gom tự động 90 file nhật ký ca/tháng từ 1 thư mục, tự Unpivot cột ngày/ca, làm sạch định dạng, nối bảng định mức [[BOM]] & Tốc độ chuẩn tự động 100%.\n"
            "   • **[[VBA]] Macro:** Tạo nút bấm ngay trong Excel (`.xlsm`) kiểm tra ràng buộc nhập liệu tại nguồn và xuất báo cáo PDF sáng gửi 4 Quản đốc trong 5 giây.\n"
            "   • **[[Python]] (`pandas`, `openpyxl`, `scipy`, `pulp`):** Xử lý file log lớn từ máy đo [[Laser Gauge]] / OGP hàng trăm nghìn dòng trong 2 giây, tự chạy kiểm định [[2-Sample t-test]]/[[Cpk]] và tối ưu cắt ghép rulo!"
        ),
        "worked_example": (
            "• **Quy trình 1-chạm thay thế 2 ngày gom báo cáo thủ công tại CADIVI:** Tạo 1 thư mục chia sẻ nội bộ `\\Server\\BaoCaoCa_Thang11\\` chứa 4 file chuẩn của 4 xưởng (Kéo, Bện, Đùn, Đóng gói). File tổng hợp OE dùng [[Power Query]] trỏ thẳng vào thư mục đó, tự nối với bảng `Master_Speed_BOM.xlsx` → Mỗi sáng 07:45 chỉ cần bấm đúng 1 nút **Refresh All** là có đủ bảng OEE, OLE, Pareto Downtime & BOM Variance sạch 100%!"
        ),
        "hands_on_drill": (
            "• **Bài tập tránh 3 bẫy Excel hay chết trong bài test tuyển dụng:** (1) Tại sao phải tính `OEE = SUM(Good_Len) / SUM(Planned_Min * Ideal_Speed)` (hoặc `A*P*Q` trên tổng) mà KHÔNG dùng `AVERAGE(OEE_Ca)`? (2) Viết công thức `SUMIFS` tính tổng phút dừng máy riêng cho Máy Đùn #2 do nguyên nhân 'Đổi màu' trong tháng 11. (3) Nếu bảng báo cáo đang để 30 cột ngang (Ngày 1 → Ngày 30), dùng lệnh nào trong Power Query để xoay dọc về 2 cột `[Ngày, Sản lượng]`? *(Đáp án: Unpivot Other Columns)*."
        ),
        "checkpoints": [
            "Ưu điểm lớn nhất của Power Query so với viết hàng nghìn công thức VLOOKUP kéo tay là gì?",
            "Khi nào OE nên chọn Python thay vì Excel thuần?",
            "Nếu sửa tay trực tiếp vào bảng kết quả Power Query thì điều gì xảy ra ở lần Refresh tiếp theo?"
        ],
        "key_terms": ["Excel", "Power Query", "VBA", "Python", "Cut-Length", "OEE", "BOM"],
        "doc_key": "excel_mfg",
        "interview_category": "ERP/MES & Quản Lý Genba"
    },
    {
        "id": "L6.4",
        "module_id": "M6",
        "title": "Bài 6.4: Thiết Kế Power BI Dashboard Quản Trị Nhà Máy Dây Cáp Điện (Star Schema & DAX Chuẩn)",
        "duration": "55 phút",
        "prereq": "Bài 6.3, Bài 2.1",
        "objectives": [
            "Thiết kế đúng mô hình dữ liệu Star Schema cho nhà máy cáp điện (bảng Fact giao dịch nối bảng Dim danh mục).",
            "Viết chính xác các công thức DAX Measure chuẩn trọng số (OEE m/phút, Scrap %, BOM Loss VNĐ, Pareto tích lũy).",
            "Bố cục Dashboard 3 tầng trực quan (Executive → Plant/OE → Shop-floor) tự động làm mới bằng On-premises Gateway."
        ],
        "core_theory": (
            "1. **Mô hình dữ liệu chuẩn Star Schema (tránh nhồi tất cả vào 1 bảng khổng lồ):**\n"
            "   • **Bảng Fact (Giao dịch theo ca/lệnh):** `Fact_Production` (Ngày, Ca, Máy, Mã Cáp, Planned_Min, Run_Min, Total_m, Good_m, Actual_Cu_Kg, Actual_Plastic_Kg), `Fact_Downtime` (Ngày, Ca, Máy, Mã Lý Do, Số Phút).\n"
            "   • **Bảng Dim (Danh mục tra cứu nối quan hệ 1–Nhiều):** `Dim_Date`, `Dim_Machine` (Xưởng, Loại máy, Tốc độ chuẩn), `Dim_Product` (Mã cáp, Định mức BOM đồng/nhựa), `Dim_DowntimeCode` (Nhóm 6 Big Losses, Phòng ban phụ trách).\n"
            "2. **Bộ [[DAX]] Measure cốt lõi không bao giờ sai trọng số:**\n"
            "   • `Availability = DIVIDE(SUM(Fact_Production[Run_Min]), SUM(Fact_Production[Planned_Min]), 0)`\n"
            "   • `Performance = DIVIDE(SUM(Fact_Production[Total_m]), SUMX(Fact_Production, Fact_Production[Run_Min] * RELATED(Dim_Machine[Ideal_Speed])), 0)`\n"
            "   • `Quality = DIVIDE(SUM(Fact_Production[Good_m]), SUM(Fact_Production[Total_m]), 0)`\n"
            "   • `OEE = [Availability] * [Performance] * [Quality]`.\n"
            "3. **Trình bày trực quan trên [[Power BI]]:** Góc trên cùng là 4–5 thẻ KPI lớn kèm mũi tên Xanh/Đỏ so với Target; giữa là biểu đồ [[Loss Tree|OEE Waterfall]] & xu hướng 12 tuần; dưới là [[Pareto]] Top 5 Downtime & bảng chi tiết Drill-through xuống tận từng ca!"
        ),
        "worked_example": (
            "• **Kịch bản trình chiếu trong cuộc họp sáng thứ Hai CADIVI:** Chỉ cần mở 1 trang Power BI, Giám đốc bấm lọc 'Xưởng Đùn' → lập tức thấy OEE tuần đạt 68.4% (-6.6% so mục tiêu 75%), nhìn sang phải thấy ngay Máy Đùn #4 tụt xuống 59% do 2 lý do lớn nhất là 'Đổi màu ngược' (140p) và 'Nghẹt lưới lọc' (75p) → Ra quyết định điều hành ngay trong 3 phút!"
        ),
        "hands_on_drill": (
            "• **Bài tập viết DAX:** Viết biểu thức DAX `Scrap_Rate_%` tính tỷ lệ phế mét toàn xưởng dùng hàm `DIVIDE` chống chia cho 0, và viết biểu thức `OEE_LastMonth` sử dụng `CALCULATE([OEE], DATEADD(Dim_Date[Date], -1, MONTH))` để so sánh tháng này với tháng trước!"
        ),
        "checkpoints": [
            "Tại sao phải dùng hàm DIVIDE(a, b, 0) thay vì dấu `/` trong DAX?",
            "Sự khác nhau giữa Calculated Column và Measure trong Power BI, và tại sao OEE bắt buộc phải viết bằng Measure?",
            "Star Schema gồm những loại bảng nào và vì sao mạnh hơn để 1 bảng phẳng duy nhất?"
        ],
        "key_terms": ["Power BI", "DAX", "Power Query", "OEE", "Loss Tree", "Pareto", "KPI"],
        "doc_key": "powerbi_mfg",
        "interview_category": "ERP/MES & Quản Lý Genba"
    },

    # =========================================================================
    # HỌC PHẦN 7: ĐỀ THI THỰC HÀNH VÒNG 2 & CHINH PHỤC PHỎNG VẤN (4 BÀI)
    # =========================================================================
    {
        "id": "L7.1",
        "module_id": "M7",
        "title": "Bài 7.1: Giải Trọn Đề Thi Thực Hành Excel Vòng 2 — Nhật Ký 5 Ca Máy Đùn (OEE, Pareto & BOM Variance VNĐ)",
        "duration": "60 phút",
        "prereq": "Bài 2.1, Bài 5.2, Bài 6.3",
        "objectives": [
            "Tự tay giải chuẩn xác 100% Đề Thi Thực Hành Vòng 2 (45 phút) từ bảng log thô 5 ca máy đùn dây VC 2.5 mm².",
            "Tránh sạch 4 cái bẫy chí mạng thí sinh hay mất điểm khi làm bài test Excel OE.",
            "Biết chuyển đổi bảng tính thô thành 3 khuyến nghị hành động thuyết phục Ban Giám đốc."
        ],
        "core_theory": (
            "1. **Cấu trúc tiêu chuẩn của Bài Test Thực Hành Vòng 2 OE (30–60 phút):** Nhà tuyển dụng đưa 1 file Excel chứa nhật ký ca thô + định mức BOM + đơn giá vật tư và yêu cầu 4 đầu ra: (1) Tính bảng tổng hợp [[OEE]] (A, P, Q) đúng trọng số, (2) Vẽ [[Pareto]] tìm nguyên nhân dừng máy số 1, (3) Tính [[BOM|BOM Variance]] ra số kg và tiền VNĐ, (4) Đề xuất 3 hành động ưu tiên ngắn hạn & dài hạn.\n"
            "2. **4 Cái bẫy thí sinh hay trượt nhất:**\n"
            "   • Bẫy 1: Lấy `AVERAGE(OEE_Ca1:Ca5)` thay vì tính từ Tổng Operating / Tổng Planned.\n"
            "   • Bẫy 2: Quên trừ nghỉ ăn ca 30 phút/ca khỏi Planned Time.\n"
            "   • Bẫy 3: Nhân định mức BOM với Tổng mét đùn (548 km) thay vì **Mét Đạt Chuẩn (534 km)** → Giấu sạch lượng đồng & nhựa mất theo phế cắt!\n"
            "   • Bẫy 4: Chỉ ghi con số % mà quên quy ra tiền VNĐ và quên phân tách phần đồng dư đường kính ([[Copper Give-away]]) với phần đồng bị cắt phế!"
        ),
        "worked_example": (
            "• **Kết quả chuẩn Đề Thi 1 (chi tiết bảng đầy đủ trong Cẩm nang `oe_field_execution_case_test`):**\n"
            "  - Planned = `2,250p`, Downtime = `275p` (Đổi màu 160p = 58.2% Pareto!) → Run = `1,975p` → **`A = 87.78%`**.\n"
            "  - Tổng chạy `548,000m`, chuẩn `320 m/p` → **`P = 86.71%`** (tốc độ thực bình quân 277.5 m/p).\n"
            "  - Phế `14,000m` → Đạt `534,000m` → **`Q = 97.45%`** → **`OEE Tổng = 74.16%`**.\n"
            "  - Đồng chuẩn cho 534 km = `11,854.8 kg` vs Thực xuất `12,350 kg` → **Vượt +495.2 kg** (gồm 310.8 kg phế cắt & +184.4 kg = +1.5% [[Copper Give-away]], tổng trị giá gộp 123.8 triệu chỉ trong 5 ca!). Nhựa vượt **+625 kg** (~17.5 triệu)!"
        ),
        "hands_on_drill": (
            "• **Thực hành bấm giờ 20 phút:** Mở Excel thật trên máy tính, tự nhập lại bảng 5 ca trong Cẩm nang `🎯 Thực Địa & Test Vòng 2` (Đề 1), tự viết công thức tính lại toàn bộ OEE = 74.16%, vẽ biểu đồ Pareto Downtime và tính BOM Variance VNĐ không nhìn đáp án!"
        ),
        "checkpoints": [
            "Khi kiểm tra 5 ca trong Đề 1, nhìn cột Ghi Chú đổi màu bạn phát hiện ra quy luật bất thường gì giữa Ca 1–3–5 so với Ca 4?",
            "Làm sao tách riêng lượng đồng mất do phế cắt 14 km với lượng đồng mất do Copper Give-away?",
            "Trong 3 hành động đề xuất sau bài test, hành động nào làm được NGAY tuần sau với chi phí 0 đồng?"
        ],
        "key_terms": ["OEE", "Pareto", "BOM", "Copper Give-away", "Over-thickness", "Color Sequencing", "SMED", "Excel"],
        "doc_key": "oe_field_execution_case_test",
        "interview_category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2"
    },
    {
        "id": "L7.2",
        "module_id": "M7",
        "title": "Bài 7.2: Giải Case Study Điều Độ Đơn Hàng +35% & Thuyết Trình A3 / Phản Biện ROI Trước Giám Đốc",
        "duration": "55 phút",
        "prereq": "Bài 5.3, Bài 5.4",
        "objectives": [
            "Trình bày mạch lạc trong 5 phút phương án giải cứu xưởng Đùn quá tải 122% không mua máy mới và đúng Luật Lao động VN.",
            "Bảo vệ vững vàng đề xuất CAPEX (như bộ Laser Gauge 420 triệu) trước những câu hỏi phản biện sắc bén của Kế toán trưởng & Giám đốc."
        ],
        "core_theory": (
            "1. **Khung trả lời Case Study Quá Tải Năng Lực (Đề 2 — 5 bước chốt điểm tuyệt đối):**\n"
            "   • Bước 1: Dùng [[TOC]] khóa đúng [[Bottleneck]] (Xưởng Đùn 122%), CẤM tăng ca dàn trải ở xưởng dư tải.\n"
            "   • Bước 2: Khai thác miễn phí tại chỗ ([[Campaign Scheduling]] + [[Color Sequencing]] + [[SMED]] nâng OEE Đùn 66%→75%, thu lại ~130 giờ ròng!).\n"
            "   • Bước 3: Điều chuyển công nhân đa kỹ năng ([[Shojinka]]) mở Ca 3 cục bộ cho riêng 2 máy Đùn theo [[Headcount Planning|3 Ca – 4 Kíp]] giữ tăng ca ≤ 32h/người/tháng (dưới trần 40h Luật LĐ).\n"
            "   • Bước 4: Bảo vệ cổ chai bằng đệm [[Drum-Buffer-Rope]] 1 ca + [[Escalation Matrix]] SLA 5 phút.\n"
            "   • Bước 5: Giao ban sáng Tier 2 theo dõi giờ máy thực vs kế hoạch hàng ngày.\n"
            "2. **Khung Thuyết Trình [[A3]] & Bảo Vệ [[ROI]] (Đề 3 — 4 chốt chặn hạ gục phản biện):**\n"
            "   • Chỉ dùng **Hard Savings** có dữ liệu [[SPC]] thật và đơn giá từ Kế toán.\n"
            "   • Trình đủ **3 kịch bản độ nhạy** (Thận trọng / Cơ sở / Lạc quan).\n"
            "   • Đề xuất **Pilot 1 máy trước** — cam kết kiểm chứng [[2-Sample t-test]] (`p < 0.05`) đạt thật mới xin duyệt mua tiếp các máy còn lại!"
        ),
        "worked_example": (
            "• **Câu chốt ăn điểm trước Kế toán trưởng:** 'Thưa anh/chị, để tránh rủi ro đầu tư dàn trải, em đề xuất chỉ đầu tư trước 1 bộ Laser Closed-loop 420 triệu cho Máy Đùn sản lượng lớn nhất, chốt trước công thức đo Trước–Sau cùng Phòng Kế toán. Ngay cả ở kịch bản thận trọng nhất (chỉ giảm 1.5% nhựa dư), thời gian hoàn vốn vẫn là 7.3 tháng; sau 30 ngày chạy thực tế đạt đúng kiểm định p < 0.05 ta mới trình nhân rộng!'"
        ),
        "hands_on_drill": (
            "• **Bài tập luyện nói to (3 phút):** Bấm đồng hồ điện thoại 3 phút, tự đứng trình bày liền mạch phương án giải cứu Đề 2 (Xưởng Đùn quá tải 122%) và Đề 3 (bảo vệ Laser Gauge 420 triệu) như đang ngồi đối diện Giám đốc Nhà máy CADIVI Miền Trung!"
        ),
        "checkpoints": [
            "Vì sao tuyệt đối không được đề xuất tăng ca toàn nhà máy khi chỉ có Xưởng Đùn bị quá tải 122%?",
            "Nếu Kế toán trưởng hỏi 'lỡ máy mua về không giảm được 2.5% nhựa như em tính thì sao?', bạn trả lời thế nào?",
            "Tại sao đề xuất chạy Pilot 1 máy trước luôn dễ được Ban Giám đốc phê duyệt hơn đề xuất mua ngay cho cả 6 máy?"
        ],
        "key_terms": ["TOC", "Bottleneck", "SMED", "Headcount Planning", "A3", "ROI", "Payback", "2-Sample t-test"],
        "doc_key": "oe_field_execution_case_test",
        "interview_category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2"
    },
    {
        "id": "L7.3",
        "module_id": "M7",
        "title": "Bài 7.3: Chiến Lược Phỏng Vấn Hành Vi STAR, Phản Biện Minh Bạch CV Cá Nhân & Thương Lượng Thu Nhập",
        "duration": "50 phút",
        "prereq": "Bài 1.1, Bài 7.2",
        "objectives": [
            "Trả lời sắc bén, trung thực và nhất quán 100% mọi câu hỏi xoáy sâu vào CV của bản thân (Mabuchi Motor & Fujikura).",
            "Ứng xử khéo léo, chuyên nghiệp về giới hạn bảo mật số liệu ROI và xử lý điểm yếu 'chưa từng làm trực tiếp nhà máy dây cáp lực'.",
            "Nắm chiến lược trao đổi mức lương 16–18 triệu (+ thưởng năm CADIVI/GELEX) tự tin, lịch thiệp."
        ],
        "core_theory": (
            "1. **4 Mũi nhọn CV Phan Thanh Thái Bảo cần đánh bóng theo chuẩn [[STAR]]:**\n"
            "   • **Mũi 1 ([[Time Study]] & Đồ gá Mabuchi):** Giảm 50% thời gian đo hạng mục bằng Canon INEX (`60s → 30s`); cải tiến bệ đo tăng sức chứa từ `1 → 16 mẫu/lượt gá` → Luôn nói chuẩn xác: giảm thao tác gá lặp lại & rút ngắn thời gian đo, **KHÔNG** nói quá thành tăng năng suất 16× hay giảm 50% nhân sự!\n"
            "   • **Mũi 2 (Tự động hóa [[Python]] / [[VBA]] / [[Excel]] / Access):** Báo cáo khách hàng `3–7 ngày → 2 giờ/tháng`; nhập liệu OGP `120p → 15p/ngày (-87.5%)` → Áp thẳng vào gom nhật ký ca & Dashboard OEE/BOM CADIVI.\n"
            "   • **Mũi 3 (Thực địa ngành dây dẫn Fujikura):** 2 năm Quản lý & Cải tiến SX 1, triển khai quét [[Barcode]] công đoạn RE7 thay sổ tay, phân tích lỗi theo công đoạn/người thao tác.\n"
            "   • **Mũi 4 (Thẩm định đầu tư [[ROI]] & Nền tảng QC chính xác):** Khi được hỏi về dự án thẩm định đầu tư (~1.2 tỷ), giữ nguyên tắc bảo mật tài chính công ty cũ — tập trung trình bày **phương pháp luận tính Payback, tách Hard/Soft Savings & 3 kịch bản độ nhạy**!\n"
            "2. **Hóa giải câu hỏi khó 'Em chưa làm ngành dây cáp lực bao giờ thì làm sao tối ưu được?':** Khẳng định phương pháp luận OE (OEE, OLE, SMED, DMAIC, SPC, BOM, dữ liệu) là chuẩn quốc tế áp dụng được cho mọi nhà máy; hơn nữa bạn đã có nền tảng Cơ khí + ngành dây dẫn Fujikura + đã chủ động nghiên cứu sâu trọn quy trình 7 công đoạn Kéo–Ủ–Bện–Đùn–Spark–Lab & tiêu chuẩn IEC 60228/60502 của CADIVI!"
        ),
        "worked_example": (
            "• **Mẫu trả lời câu hỏi về mức lương kỳ vọng:** 'Em có tìm hiểu khung lương vị trí OE tại CADIVI Miền Trung là 16–18 triệu cùng chính sách thưởng năm và phúc lợi rất ổn định của hệ thống CADIVI/GELEX. Với kinh nghiệm làm Nhóm trưởng QC, cải tiến Time Study, tự động hóa dữ liệu Python/VBA và sẵn sàng xuống Genba ngay ngày đầu, em mong muốn mức đề xuất nằm trong khung 17–18 triệu (hoặc theo thang đánh giá năng lực của công ty), và cam kết chứng minh giá trị tiết kiệm thực vượt xa chi phí lương ngay trong giai đoạn thử việc!'"
        ),
        "hands_on_drill": (
            "• **Bài tập luyện phản biện 5 câu hóc búa:** Tự trả lời thành tiếng: (1) Vì sao bạn rời Mabuchi (Nhóm trưởng QC) để chuyển sang OE CADIVI? (2) Bạn có bị ngợp khi sang nhà máy dây cáp công nghiệp nặng, nóng và ồn hơn xưởng motor không? (3) Kể một lần đề xuất cải tiến của bạn bị từ chối và cách bạn xử lý? (4) Nếu quản đốc lớn tuổi hơn không hợp tác cung cấp số liệu thì bạn làm sao? (5) Số liệu cải tiến 1→16 mẫu có phải giúp tăng năng suất 16 lần không?"
        ),
        "checkpoints": [
            "Tại sao tuyệt đối không được nói quá 'bệ đo 1 → 16 mẫu làm tăng năng suất 16 lần'?",
            "Nếu hội đồng hỏi sâu con số lợi nhuận chi tiết của dự án 1.2 tỷ ở công ty cũ, cách trả lời chuyên nghiệp nhất là gì?",
            "Ba lợi thế lớn nhất khiến một kỹ sư QC/Cơ khí biết lập trình Python/VBA rất phù hợp làm OE tại CADIVI?"
        ],
        "key_terms": ["STAR", "ADKAR", "Time Study", "ROI", "Payback", "Python", "VBA", "Barcode"],
        "doc_key": "oe_six_sigma_dmaic",
        "interview_category": "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE"
    },
    {
        "id": "L7.4",
        "module_id": "M7",
        "title": "Bài 7.4: Tổng Duyệt 128 Câu Hỏi (Chế Độ Ẩn Đáp Án) & 5 Câu Hỏi Ngược Ghi Điểm Với Giám Đốc CADIVI",
        "duration": "90 phút",
        "prereq": "Hoàn thành Học phần 1 đến 7.3",
        "objectives": [
            "Sử dụng hiệu quả Chế độ Luyện Phỏng Vấn Ẩn Đáp Án ngay trong Tab Phỏng Vấn để tự kiểm tra đạt ≥ 85% câu hỏi 'Đã thuộc'.",
            "Thuộc và sử dụng tự nhiên 5 câu hỏi ngược thông minh cuối buổi phỏng vấn để thể hiện tầm tư duy của một Chuyên viên OE thực thụ."
        ],
        "core_theory": (
            "1. **Phương pháp luyện Active Recall (Chủ động gợi nhớ) 3 vòng trên App JobDetail:**\n"
            "   • **Vòng 1:** Mở Tab `❓ Phỏng Vấn & Thực Chiến`, bật công tắc **`🎯 Chế độ Luyện Phỏng Vấn (Ẩn đáp án)`**. Đọc câu hỏi, tự nói ra 3 ý chính trong 45 giây rồi mới bấm `[👁️ Xem gợi ý trả lời]` để đối chiếu; chấm ngay `[✅ Đã thuộc]` hoặc `[🔁 Cần ôn lại]`.\n"
            "   • **Vòng 2:** Bấm bộ lọc trạng thái chọn riêng **`🔁 Cần ôn lại`** để đào sâu lại những câu còn vấp và click trực tiếp vào thuật ngữ gạch chân xem lại ví dụ.\n"
            "   • **Vòng 3 (Đêm trước phỏng vấn):** Chỉ lướt nhanh Chủ đề 11 (Máy móc CADIVI), Chủ đề 14 (STAR/CV), Chủ đề 15 (Hỏi ngược) và Chủ đề 17 (Test Vòng 2).\n"
            "2. **5 Câu hỏi ngược đắt giá cuối buổi phỏng vấn (chọn 2–3 câu hỏi đúng lúc):**\n"
            "   • Câu 1: *'Hiện tại Nhà máy CADIVI Miền Trung đang ưu tiên tấn công bài toán OE nào nhất trong 6 tháng tới — nâng OEE/SMED xưởng Đùn, kiểm soát hao phí BOM đồng–nhựa, hay chuẩn hóa dữ liệu MES/Power BI?'*\n"
            "   • Câu 2: *'Hệ thống thu thập dữ liệu sản xuất (nhật ký ca, dừng máy, phế phẩm) dưới xưởng hiện đang ghi nhận thủ công qua Excel hay đã kết nối PLC/MES đến mức độ nào ạ?'*\n"
            "   • Câu 3: *'Trong 90 ngày thử việc, Ban Giám đốc kỳ vọng Chuyên viên OE cần bàn giao được đầu ra cụ thể nào để đánh giá là hoàn thành xuất sắc?'*\n"
            "   • Câu 4: *'Cơ chế phối hợp giữa OE với Quản đốc các phân xưởng, Kỹ thuật công nghệ và Kế toán BOM khi triển khai cải tiến Pilot ở nhà máy diễn ra như thế nào ạ?'*"
        ),
        "worked_example": (
            "• **Hiệu ứng tâm lý của câu hỏi ngược thông minh:** Khi bạn hỏi thẳng vào trọng tâm 'ưu tiên SMED đùn, hao phí BOM hay số hóa dữ liệu trong 6 tháng tới?', Giám đốc Nhà máy lập tức nhìn thấy bạn đã suy nghĩ như **người trong cuộc sẵn sàng bắt tay vào việc ngay thứ Hai tuần tới** chứ không phải một ứng viên đi xin việc thụ động!"
        ),
        "hands_on_drill": (
            "• **Thử thách tổng duyệt:** Bấm nút **`❓ Luyện Câu Hỏi Chủ Đề Này`** ngay trên thanh công cụ bài học, bật Chế độ Ẩn Đáp Án và hoàn thành ít nhất 20 câu hỏi đầu tiên ở 2 nhóm quan trọng nhất (Chủ đề 11 & Chủ đề 17) để đạt mục tiêu sẵn sàng!"
        ),
        "checkpoints": [
            "Bạn đã đạt tỷ lệ bao nhiêu % câu hỏi '✅ Đã thuộc' trong ngân hàng 128 câu hỏi?",
            "Nếu buổi phỏng vấn chỉ còn 3 phút cuối, bạn chọn hỏi 2 câu hỏi ngược nào giá trị nhất?",
            "Những điều gì tuyệt đối KHÔNG nên hỏi hoặc nói ở buổi phỏng vấn vòng 1?"
        ],
        "key_terms": ["OE", "STAR", "Hoshin Kanri", "OEE", "SMED", "BOM", "MES"],
        "doc_key": "oe_field_execution_case_test",
        "interview_category": "Câu Hỏi Hỏi Ngược Nhà Tuyển Dụng CADIVI"
    },

    # =========================================================================
    # HỌC PHẦN 8: KẾ HOẠCH HÀNH ĐỘNG NGÀY 1 → NGÀY 90 KHI TRÚNG TUYỂN (3 BÀI)
    # =========================================================================
    {
        "id": "L8.1",
        "module_id": "M8",
        "title": "Bài 8.1: Ngày 1–15 Tại CADIVI Miền Trung — Đi Genba 3 Ca, Tạo Lòng Tin & Kiểm Toán Độ Tin Cậy Dữ Liệu",
        "duration": "45 phút",
        "prereq": "Hoàn thành Học phần 1–6",
        "objectives": [
            "Xây dựng quan hệ hợp tác thân thiện với Quản đốc, Tổ trưởng, Cơ Điện, Kỹ thuật và Lab QA/QC ngay từ tuần đầu.",
            "Hoàn thành kiểm toán thực địa 3 ca và đánh giá chính xác độ tin cậy dữ liệu sản xuất hiện có.",
            "Chốt được Bảng Mã Lý Do Dừng Máy chuẩn và sơ đồ Current State VSM đầu tiên."
        ],
        "core_theory": (
            "1. **Quy tắc vàng 15 ngày đầu — 'Nghe nhiều, Hỏi khiêm tốn, Đừng vội phán xét!':**\n"
            "   • Tuyệt đối không chê bai cách làm cũ của xưởng trong 2 tuần đầu (gây phản kháng ngay lập tức!).\n"
            "   • Đi [[Genba]] đủ cả 3 ca (kể cả 1–2 buổi khảo sát Ca 2/Ca 3) tại 4 phân xưởng Kéo – Bện – Đùn – Đóng gói để hiểu nhịp vận hành thật và hỏi công nhân 'Chỗ nào làm anh em vất vả, hay kẹt, hay mất thời gian nhất?'.\n"
            "2. **Kiểm toán 3 nguồn dữ liệu sống còn:**\n"
            "   • Đối chiếu số liệu dừng máy trong sổ tay ca với đồng hồ/PLC xem có bị bỏ sót dừng vặt < 5p không.\n"
            "   • Đối chiếu số lượng phế liệu cân nhập kho phế xem đã tách rõ 3 nhóm (Đồng trần / Đồng dính nhựa / Nhựa purge) chưa.\n"
            "   • Đối chiếu tốc độ chuẩn (Routing) và định mức [[BOM]] trên [[ERP]] xem còn lạc hậu so với thực tế máy móc không.\n"
            "3. **Đầu ra cuối Ngày 15:** 01 Bản đồ [[VSM]] Hiện trạng + 01 Bảng chuẩn hóa 12–15 mã [[Downtime]] theo [[Six Big Losses]] + Danh sách Top 10 nỗi đau của công nhân cần làm Quick-Win!"
        ),
        "worked_example": (
            "• **Cách mở lời lấy thiện cảm với Tổ trưởng xưởng Đùn ngày thứ 3:** 'Anh ơi, em mới qua phụ trách tối ưu quy trình, em chưa rành máy đùn bằng anh làm mười mấy năm đâu. Anh cho em đứng phụ quan sát ca đổi màu hôm nay để xem công đoạn nào anh em cực nhất (như khiêng khuôn, tìm đồ, chờ xe nâng) em ghi lại đề xuất hỗ trợ trước nha anh!' → 99% tổ trưởng sẽ mở lòng chia sẻ mọi bí mật hiện trường!"
        ),
        "hands_on_drill": (
            "• **Checklist chuẩn bị sổ tay Genba Ngày 1:** Soạn sẵn 1 trang sổ tay gồm 8 mục kiểm tra: (1) Danh sách tên các máy & tốc độ danh định, (2) Mẫu sổ báo cáo ca hiện hành, (3) Biểu mẫu cân phế, (4) Thời gian đổi màu trung bình hiện tại, (5) Vị trí khu WIP rulo, (6) Tần suất lấy mẫu Lab, (7) Mã dừng máy đang dùng, (8) Ghi nhận 5 bức xúc lớn nhất của công nhân."
        ),
        "checkpoints": [
            "Sai lầm lớn nhất của kỹ sư OE mới vào nhà máy trong 2 tuần đầu dễ khiến cả xưởng tẩy chay là gì?",
            "Vì sao bắt buộc phải xuống khảo sát cả Ca 3 ban đêm ít nhất 1–2 buổi trong 15 ngày đầu?",
            "Ba sản phẩm đầu ra cụ thể bạn nên bàn giao vào cuối Ngày 15 là gì?"
        ],
        "key_terms": ["Genba", "VSM", "Downtime", "Six Big Losses", "BOM", "ADKAR", "Scrap"],
        "doc_key": "lean_muda",
        "interview_category": "ERP/MES & Quản Lý Genba"
    },
    {
        "id": "L8.2",
        "module_id": "M8",
        "title": "Bài 8.2: Ngày 16–45 — Tự Động Hóa Báo Cáo 1-Chạm, Bắn Quick-Win & Khoanh Vùng Top 3 Mỏ Vàng",
        "duration": "45 phút",
        "prereq": "Bài 8.1",
        "objectives": [
            "Xây xong hệ thống tổng hợp báo cáo OEE / OLE / BOM Variance tự động 1-chạm bằng Power Query / Python / Power BI.",
            "Triển khai thành công 1–2 dự án Quick-Win (chi phí thấp, hiệu quả ngay) tạo uy tín với cả Xưởng lẫn Ban Giám đốc.",
            "Hoàn thiện Bản đồ Cost Deployment & Chọn đúng 1 dây chuyền mẫu (Pilot Line) cho dự án đột phá 45 ngày sau."
        ],
        "core_theory": (
            "1. **Tạo dấu ấn năng lực dữ liệu ngay Tháng 1:** Phát huy thế mạnh [[Power Query]] / [[Python]] / [[Power BI]] xây bộ công cụ tự động gom nhật ký ca 4 xưởng, vẽ [[Loss Tree]] & [[Pareto]] 80/20 hàng tuần — giúp Giám đốc và Quản đốc có bức tranh minh bạch mà không tốn thêm 1 phút nhập liệu của tổ trưởng!\n"
            "2. **Thực hiện 2 Quick-Win 'ghi điểm nhanh' (tạo bước Desire trong [[ADKAR]]):**\n"
            "   • *Quick-Win 1 (cho Công nhân):* Xe đẩy đồ nghề SMED 5S có bảng Shadow Board, hoặc quy ước đèn [[Andon]] Vàng gọi xe nâng cấp rulo trước 15 phút giúp công nhân đỡ chạy đi tìm đồ.\n"
            "   • *Quick-Win 2 (cho Ban Giám đốc):* Đảo lịch [[Color Sequencing]] (Sáng → Tối) cùng Phòng Kế hoạch & tách rõ 3 thùng phế màu — thấy ngay giảm giờ đổi màu & tăng giá trị thu hồi phế liệu tốn 0 đồng!\n"
            "3. **Thu thập Baseline cho Dự án Pilot lớn:** Quay video [[SMED]] dây chuyền Đùn cổ chai; lấy 30 ngày dữ liệu chiều dày/đường kính phòng Lab chạy [[Minitab]] tính [[Cpk]] định lượng chính xác [[Copper Give-away]] & [[Over-thickness]]; lập bảng [[Cost Deployment]] chọn ĐÚNG 1 dự án ăn tiền nhất để tập trung đánh dứt điểm ở Ngày 46–90!"
        ),
        "worked_example": (
            "• **Báo cáo giữa kỳ thử việc (Ngày 45) trình Giám đốc Nhà máy:** 1 trang [[A3]] gọn đẹp gồm: (1) Dashboard OEE/BOM tự động đã chạy thực tế (rút thời gian báo cáo 2 ngày → 5 phút), (2) Kết quả 2 Quick-Win đã tiết kiệm tức thì, (3) Bản đồ [[Cost Deployment]] chỉ ra Top 3 mỏ vàng bằng VNĐ và đề xuất Project Charter chạy Pilot 45 ngày tiếp theo!"
        ),
        "hands_on_drill": (
            "• **Lập kế hoạch 30 ngày (Ngày 16–45):** Tự gạch ra 4 mốc tuần (Tuần 3, 4, 5, 6) mỗi tuần 1 đầu ra cụ thể đo đếm được để đánh dấu tích dần trong Tab `🧭 Lộ Trình Nắm Bắt`!"
        ),
        "checkpoints": [
            "Tại sao ở giai đoạn Ngày 16–45 cần làm ít nhất 1 Quick-Win giải quyết trực tiếp nỗi khổ của công nhân?",
            "Tại sao phải chốt xong đường cơ sở (Baseline 30 ngày) trước khi bắt đầu thay đổi trên dây chuyền Pilot?",
            "Những phòng ban nào cần cùng ký xác nhận đơn giá vật tư trong bảng Cost Deployment?"
        ],
        "key_terms": ["Power Query", "Power BI", "Cost Deployment", "Pareto", "Color Sequencing", "SMED", "Minitab", "Cpk", "A3"],
        "doc_key": "oe_field_execution_case_test",
        "interview_category": "Hoạch Định Năng Lực, Điều Độ & Chi Phí"
    },
    {
        "id": "L8.3",
        "module_id": "M8",
        "title": "Bài 8.3: Ngày 46–90 — Dẫn Dắt Dự Án Pilot, Chứng Minh t-test & ROI, Khóa Chuẩn LSW/LPA Qua Thử Việc Xuất Sắc",
        "duration": "45 phút",
        "prereq": "Bài 8.2",
        "objectives": [
            "Thực thi thành công dự án Pilot (SMED máy đùn hoặc giảm phế Over-thickness/Copper Give-away) có sự đồng hành của xưởng.",
            "Chứng minh khoa học hiệu quả Trước–Sau bằng Minitab (2-Sample t-test p < 0.05) và xác nhận Hard Savings với Kế toán.",
            "Khóa chặt kết quả bằng SOP/OPL, Control Plan, LSW/LPA và trình Báo cáo A3 tổng kết 90 ngày thuyết phục Ban Giám đốc."
        ],
        "core_theory": (
            "1. **Tổ chức chạy Pilot bài bản (Ngày 46–70):**\n"
            "   • Chọn đúng 1 dây chuyền có tổ trưởng cởi mở nhất làm **Kaizen Blitz 5 ngày** (ví dụ triển khai trọn bộ SMED đổi màu/tiết diện hoặc tinh chỉnh SPC giảm nhựa bọc dư qua [[MOC / ECN]]).\n"
            "   • Đo đủ dữ liệu 20–30 lượt/ca sau cải tiến để đối sánh công bằng với Baseline 30 ngày trước đó.\n"
            "2. **Xác nhận kép Khoa học + Tài chính (Ngày 71–80):**\n"
            "   • Khoa học: Chạy [[2-Sample t-test]] trên [[Minitab]] xác nhận `[[p-value]] < 0.05` và [[Cpk]] ≥ 1.33–1.67.\n"
            "   • Tài chính: Mời Phòng Kế toán kiểm tra độc lập số kg nhựa/đồng tiết kiệm & giờ máy cổ chai tăng thêm, chốt con số **Hard Savings (VNĐ/tháng)** & [[Payback]].\n"
            "3. **Khóa chuẩn & Tổng kết 90 ngày (Ngày 81–90):**\n"
            "   • Ban hành [[SOP]] trực quan 1 trang (OPL), cập nhật [[Control Plan]] & MBOM ERP, đưa vào lịch [[LSW]] tổ trưởng & phiếu [[LPA]] hàng tuần.\n"
            "   • Trình bày Báo cáo [[A3]] tổng kết 90 ngày + Lộ trình nhân rộng sang các dây chuyền còn lại cho 6–12 tháng tới (gắn thẳng với [[Hoshin Kanri]] của nhà máy)!"
        ),
        "worked_example": (
            "• **Bản tổng kết 90 ngày 'không thể chối từ' của Chuyên viên OE CADIVI:** (1) Đã vận hành báo cáo OEE/OLE/BOM tự động toàn nhà máy; (2) Máy Đùn Pilot #1 giảm thời gian đổi màu từ 52p → 16p (-69%, `p = 0.000`), giảm phế nhựa đầu ca 65%, tiết kiệm thực được Kế toán xác nhận 48 triệu/tháng (576 triệu/năm — lớn gấp gần 3 lần tổng chi phí lương năm của vị trí OE!); (3) Đã khóa chuẩn OPL + LSW + LPA sẵn sàng nhân rộng sang 5 máy đùn còn lại trong Quý tiếp theo!"
        ),
        "hands_on_drill": (
            "• **Hoàn thiện Bản cam kết 90 ngày cá nhân:** Tóm tắt toàn bộ Học phần 8 thành 3 gạch đầu dòng ngắn gọn (30 ngày đầu – 60 ngày – 90 ngày) để sẵn sàng trả lời tự tin nếu Giám đốc CADIVI hỏi trong buổi phỏng vấn: *'Nếu nhận việc ngày mai, kế hoạch 90 ngày đầu của em là gì?'*"
        ),
        "checkpoints": [
            "Vì sao bắt buộc phải mời Phòng Kế toán xác nhận chéo số tiền Hard Savings trước khi trình bày Báo cáo 90 ngày?",
            "Bốn công cụ nào phải hoàn thành ở tuần cuối (Ngày 81–90) để đảm bảo cải tiến không bao giờ bị tụt về như cũ?",
            "Bạn đã tự tin trình bày mạch lạc lộ trình 30–60–90 ngày của mình trong 90 giây chưa?"
        ],
        "key_terms": ["SMED", "MOC / ECN", "2-Sample t-test", "p-value", "Cpk", "ROI", "Payback", "Control Plan", "LSW", "LPA", "A3", "Hoshin Kanri"],
        "doc_key": "oe_field_execution_case_test",
        "interview_category": "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE"
    },
]


def get_all_modules():
    """Trả về danh sách 8 Học phần (Modules) theo đúng trình tự từ Zero → Chuyên gia."""
    return MODULES


def get_all_lessons():
    """Trả về toàn bộ 32 bài học tuần tự trong Giáo trình OE CADIVI."""
    return LESSONS


def get_lesson(lesson_id):
    """Lấy chi tiết 1 bài học theo mã (vd: 'L1.1', 'L4.2')."""
    if not lesson_id:
        return None
    lid = lesson_id.strip().upper()
    for l in LESSONS:
        if l["id"].upper() == lid:
            return l
    return None


def get_lessons_by_module(module_id=None):
    """Lọc danh sách bài học theo mã Học phần (hoặc tất cả nếu None/'ALL')."""
    if not module_id or module_id == "ALL":
        return LESSONS
    return [l for l in LESSONS if l["module_id"] == module_id]
