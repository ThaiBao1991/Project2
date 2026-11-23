#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
term_glossary.py — Kho Từ Điển Thuật Ngữ Chuyên Sâu OE, Sản Xuất Tinh Gọn & Ngành Dây Cáp Điện (CADIVI)
Cung cấp định nghĩa chi tiết từ cơ bản đến chuyên sâu, công thức/tiêu chuẩn, khả năng áp dụng
thực tế tại Nhà máy CADIVI Miền Trung, ví dụ số liệu cụ thể và bộ máy nhận diện siêu tốc
(Click-Anywhere Hyperlink Engine) dùng chung cho toàn bộ ứng dụng JobDetail.
"""

import re
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


# =====================================================================
# KHO TỪ ĐIỂN THUẬT NGỮ TOÀN DIỆN (82 THUẬT NGỮ CỐT LÕI OE & CADIVI)
# =====================================================================
GLOSSARY = {
    # =================================================================
    # NHÓM 1: HỆ THỐNG SỐ HÓA, DỮ LIỆU & PHẦN MỀM CHUYÊN DỤNG
    # =================================================================
    "MES": {
        "term": "MES",
        "full_name": "Manufacturing Execution System — Hệ thống Điều hành Thực thi Sản xuất",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["MES", "Manufacturing Execution System"],
        "case_sensitive": ["MES"],
        "short_desc": "Phần mềm tầng 3 (ISA-95) điều hành trực tiếp tầng xưởng theo thời gian thực, kết nối giữa ERP và PLC/máy móc.",
        "definition": (
            "MES là hệ thống phần mềm quản lý, giám sát và điều phối toàn bộ hoạt động sản xuất trực tiếp tại phân xưởng theo thời gian thực (từng phút/từng giây). "
            "Nếu ERP là 'bộ não lập kế hoạch kinh doanh' (cấp ngày/tuần), PLC/SCADA là 'hệ thần kinh cảm biến' tại từng chiếc máy, thì MES chính là 'tổng chỉ huy tại hiện trường' "
            "giúp biến nhà xưởng từ 'hộp đen giấy tờ' thành bức tranh số hóa minh bạch: lệnh nào đang chạy máy nào, chạy bao nhiêu mét, dừng máy bao lâu vì lỗi gì, và truy xuất phả hệ từng cuộn hàng."
        ),
        "formula_or_spec": (
            "• Vị trí chuẩn ISA-95: Tầng 3 (Giữa Tầng 4 ERP và Tầng 1–2 PLC/SCADA).\n"
            "• 4 trụ cột chức năng: (1) Điều độ lệnh SX (Dispatching), (2) Đo OEE/Downtime tự động, (3) Kiểm soát chất lượng & phế phẩm In-line, (4) Truy xuất nguồn gốc (Lot Traceability)."
        ),
        "cadivi_application": (
            "Tại Nhà máy CADIVI Miền Trung, MES có thể áp dụng xuyên suốt 4 phân xưởng Kéo – Bện – Đùn – Đóng gói:\n"
            "1. Nhận Lệnh Sản Xuất (Work Order) từ ERP/SAP kèm mã cáp (vd: CXV 3x50+1x25) và định mức BOM đẩy thẳng xuống màn hình HMI cạnh máy đùn/kéo.\n"
            "2. Đọc trực tiếp xung đếm mét từ Encoder, đường kính từ Laser Gauge và số lỗi từ Spark Tester để tính OEE tự động theo mét/phút (chấm dứt ghi sổ ca dễ sai lệch).\n"
            "3. Khóa Poka-Yoke quét Barcode rulo đồng đầu vào: quét sai tiết diện → MES không cho mở khóa máy bện/đùn.\n"
            "4. Truy xuất ngược 100% phả hệ (Lot Genealogy): từ 1 cuộn cáp xuất công trình biết chính xác chạy máy đùn nào, ca nào, lô hạt nhựa XLPE nào và lô đồng rod nào."
        ),
        "cadivi_example": (
            "Ví dụ thực tế trên Dây chuyền Đùn PVC số 3 tại CADIVI: Khi máy dừng quá 2 phút, màn hình MES tại máy tự bật hộp chọn mã lý do dừng (Đổi màu / Thay rulo / Đứt dây / Lỗi Spark). "
            "Cuối ca, thay vì công nhân ghi tay 105,000m (lệch thực tế), MES chốt tự động từ Encoder: 102,600m đạt + 2,400m phế startup, đồng bộ thẳng về ERP để tính ngay BOM Variance ngày hôm sau."
        ),
        "related": ["ERP", "SAP PP", "SCADA", "PLC", "ISA-95", "OEE", "Barcode", "BOM"],
        "doc_key": "erp_mes"
    },
    "ERP": {
        "term": "ERP",
        "full_name": "Enterprise Resource Planning — Hệ thống Hoạch định Nguồn lực Doanh nghiệp",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["ERP", "Enterprise Resource Planning"],
        "case_sensitive": ["ERP"],
        "short_desc": "Hệ thống quản trị tổng thể cấp doanh nghiệp (tầng 4 ISA-95) quản lý đơn hàng, mua sắm NVL, tồn kho, BOM và kế toán giá thành.",
        "definition": (
            "ERP là nền tảng phần mềm tích hợp toàn bộ dữ liệu quản trị của doanh nghiệp (Kinh doanh, Kế hoạch, Mua hàng, Kho, Sản xuất, Kế toán, Nhân sự) vào một cơ sở dữ liệu thống nhất. "
            "Trong nhà máy, phân hệ sản xuất của ERP (như SAP PP) quản lý cây định mức BOM, quy trình công đoạn (Routing), phát hành Lệnh Sản Xuất (Work Order) và tính giá thành sản phẩm (COGS)."
        ),
        "formula_or_spec": (
            "• Chu kỳ vận hành: Cấp Ngày / Tuần / Tháng (Tầng 4 ISA-95).\n"
            "• Đối soát chuẩn: Xuất kho NVL (Goods Issue) vs Nhập kho Thành phẩm (Goods Receipt) × Định mức MBOM = BOM Variance."
        ),
        "cadivi_application": (
            "Tại CADIVI Miền Trung, Chuyên viên OE khai thác dữ liệu ERP hằng tuần/tháng để:\n"
            "1. Trích xuất bảng định mức MBOM chuẩn (kg đồng/km, kg nhựa/km) của hàng trăm mã dây dân dụng & cáp lực.\n"
            "2. Đối chiếu chênh lệch nguyên vật liệu thực tế xuất kho so với lý thuyết BOM theo từng Lệnh Sản Xuất để phát hiện rò rỉ đồng/nhựa.\n"
            "3. Lấy dữ liệu đơn hàng bán hàng & tồn kho để lập kế hoạch hoạch định năng lực thô (RCCP) và lịch chạy chiến dịch (Campaign Scheduling)."
        ),
        "cadivi_example": (
            "Ví dụ: Đầu tháng OE xuất báo cáo từ ERP cho Lệnh SX 10 km cáp CXV 3x50+1x25 → ERP báo định mức đồng là 15,620 kg, nhưng kho xuất thực tế 15,940 kg (lệch +320 kg ≈ 80 triệu đồng). "
            "Từ tín hiệu ERP này, OE lập tức xuống máy kéo/bện/đùn điều tra nguyên nhân Copper Give-away và phế đầu-đuôi."
        ),
        "related": ["SAP PP", "MES", "BOM", "RCCP", "ISA-95", "Cycle Counting"],
        "doc_key": "erp_mes"
    },
    "SAP PP": {
        "term": "SAP PP",
        "full_name": "SAP Production Planning — Phân hệ Hoạch định & Kiểm soát Sản xuất trên SAP ERP",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["SAP PP", "SAP ERP", "SAP"],
        "case_sensitive": ["SAP PP", "SAP ERP", "SAP"],
        "short_desc": "Phân hệ quản lý kế hoạch sản xuất, BOM, Routing, Work Center và hạch toán lệnh sản xuất của phần mềm SAP.",
        "definition": (
            "SAP PP là module sản xuất chuẩn toàn cầu thuộc hệ thống SAP ERP, quản lý 4 dữ liệu chủ (Master Data) cốt lõi: "
            "Material Master (Mã vật tư/thành phẩm), BOM (Định mức vật tư), Work Center (Tổ máy/công suất giờ máy) và Routing (Trình tự công đoạn & thời gian chuẩn)."
        ),
        "formula_or_spec": (
            "• Luồng chuẩn SAP PP: Sales Order → MRP (Hoạch định NVL) → Planned Order → Production Order → Goods Issue → Confirmation (Chốt sản lượng) → Goods Receipt → Variance Settlement."
        ),
        "cadivi_application": (
            "Tại nhà máy quy mô lớn như CADIVI, OE phối hợp phòng Kế hoạch & Kế toán cập nhật dữ liệu chuẩn Routing (tốc độ đùn m/phút, thời gian đổi mã SMED, định biên công nhân) "
            "và MBOM (kèm hệ số xoắn Lay-up Factor) lên hệ thống ERP/SAP để hạch toán giá thành chính xác và tính tải năng lực tự động."
        ),
        "cadivi_example": (
            "Ví dụ: Sau dự án SMED rút thời gian đổi màu máy đùn từ 55 phút xuống 12 phút, OE cập nhật lại Setup Time trong Routing trên ERP/SAP PP → Hệ thống tự tính tăng công suất khả dụng của Work Center máy đùn thêm +14% để Kinh doanh nhận thêm đơn hàng."
        ),
        "related": ["ERP", "MES", "BOM", "RCCP", "SMED"],
        "doc_key": "erp_mes"
    },
    "SCADA": {
        "term": "SCADA",
        "full_name": "Supervisory Control and Data Acquisition — Hệ thống Giám sát Điều khiển & Thu thập Dữ liệu",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["SCADA"],
        "case_sensitive": ["SCADA"],
        "short_desc": "Hệ thống tầng 2 (ISA-95) giao tiếp với PLC để hiển thị, điều khiển thông số máy móc và lưu lịch sử vận hành.",
        "definition": (
            "SCADA là hệ thống phần mềm giám sát và điều khiển công nghiệp (thường đi kèm màn hình cảm ứng HMI tại máy), thu thập tín hiệu trực tiếp từ các bộ điều khiển PLC, cảm biến nhiệt độ, áp suất, tốc độ động cơ và hiển thị biểu đồ xu hướng theo thời gian thực."
        ),
        "formula_or_spec": (
            "• Tầng 2 trong ISA-95; giao thức công nghiệp phổ biến: Modbus TCP, OPC-UA, Profinet, MQTT.\n"
            "• Tốc độ lấy mẫu: 0.1 – 5 giây/lần."
        ),
        "cadivi_application": (
            "Trên dây chuyền đùn bọc cáp PVC/XLPE và máy kéo thô RBD hiện đại (Đức/Nhật) tại CADIVI:\n"
            "1. Giám sát liên tục nhiệt độ 5–6 vùng nòng đùn (Barrel Zones), áp suất đầu đùn, dòng điện motor trục vít, tốc độ m/phút và nhiệt độ nước làm mát.\n"
            "2. Lưu sẵn bộ công thức thông số chuẩn (Recipe) cho từng mã dây để nạp 1-chạm khi đổi mã (SMED).\n"
            "3. Đẩy dữ liệu tốc độ và trạng thái Chạy/Dừng/Cảnh báo lên hệ thống MES/Power BI để tính OEE không cần nhập tay."
        ),
        "cadivi_example": (
            "Ví dụ: Nhờ trích xuất log SCADA nhiệt độ vùng đùn 3 trong 7 ngày trên máy đùn số 4, OE phát hiện nhiệt độ dao động ±12°C vào ca đêm do lỗi cảm biến thermocouple — nguyên nhân gây lỗi hạt cháy Spark Tester."
        ),
        "related": ["PLC", "MES", "ISA-95", "Extruder", "Laser Gauge", "Spark Tester"],
        "doc_key": "erp_mes"
    },
    "PLC": {
        "term": "PLC",
        "full_name": "Programmable Logic Controller — Bộ Điều Khiển Logic Khả Trình",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["PLC"],
        "case_sensitive": ["PLC"],
        "short_desc": "Bộ não điều khiển tự động phần cứng máy công nghiệp (Siemens, Mitsubishi, Omron...) đọc cảm biến và điều khiển động cơ/van.",
        "definition": (
            "PLC là máy tính công nghiệp chuyên dụng chịu được môi trường nóng, bụi, rung tại phân xưởng, thực thi vòng lặp điều khiển chính xác đến mili-giây: "
            "đọc tín hiệu đầu vào từ cảm biến (quang, áp suất, encoder, công tắc hành trình) và xuất lệnh đóng/ngắt động cơ, biến tần, xi-lanh khí nén hay còi đèn Andon."
        ),
        "formula_or_spec": (
            "• Tầng 1 trong ISA-95; chu kỳ quét (Scan Cycle): 1 – 20 mili-giây.\n"
            "• Tín hiệu OE hay khai thác từ PLC: Bit Run/Stop, Bit Alarm Code, Xung đếm mét Encoder, Analog Speed (m/min)."
        ),
        "cadivi_application": (
            "Tại Nhà máy CADIVI, PLC điều khiển đồng bộ tốc độ giữa trục vít đùn – bộ kéo Capstan – cụm thu dây Take-up để lớp nhựa không bị giật cục; "
            "đồng thời là nguồn dữ liệu 'sự thật tuyệt đối' (Single Source of Truth) giúp OE phát hiện dừng máy vi mô (< 5 phút), đếm mét chính xác và xây cơ cấu khóa liên động Poka-Yoke chống gian lận."
        ),
        "cadivi_example": (
            "Ví dụ: Gắn bộ đọc tín hiệu xung từ PLC máy bện Buncher về máy tính OE giúp phát hiện máy có 14 lần vi dừng 1–3 phút mỗi ca do kẹt dẫn hướng sợi (tổn thất 28 phút/ca mà công nhân không hề ghi vào sổ ca!)."
        ),
        "related": ["SCADA", "MES", "ISA-95", "Poka-Yoke", "OEE", "Andon"],
        "doc_key": "erp_mes"
    },
    "ISA-95": {
        "term": "ISA-95",
        "full_name": "Tiêu Chuẩn Kiến Trúc Tích Hợp Tự Động Hóa Nhà Máy 5 Tầng (IEC 62264)",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["ISA-95"],
        "case_sensitive": ["ISA-95"],
        "short_desc": "Mô hình kim tự tháp chuẩn quốc tế phân rõ vai trò 5 tầng từ Cảm biến (Tầng 0) → PLC (1) → SCADA (2) → MES (3) → ERP (4).",
        "definition": (
            "ISA-95 là tiêu chuẩn quốc tế định nghĩa ranh giới chức năng và luồng trao đổi dữ liệu giữa hệ thống quản trị doanh nghiệp (IT/ERP) và hệ thống điều khiển tự động tại xưởng (OT/PLC/SCADA), "
            "tránh chồng chéo khi doanh nghiệp triển khai chuyển đổi số nhà máy."
        ),
        "formula_or_spec": (
            "• Tầng 0: Quy trình vật lý (Dây cáp, máy móc) | Tầng 1: Cảm biến/PLC | Tầng 2: SCADA/HMI | Tầng 3: MES | Tầng 4: ERP."
        ),
        "cadivi_application": (
            "Giúp Chuyên viên OE CADIVI vạch lộ trình số hóa từng bước đúng chuẩn (không nhầm lẫn giữa chức năng ERP và MES) khi phối hợp với phòng IT/MES của Tổng công ty CADIVI."
        ),
        "cadivi_example": (
            "Ví dụ: Khi lập dự án kết nối tự động 6 máy đùn, OE vẽ sơ đồ ISA-95 phân rõ: Encoder & Spark Tester (Tầng 1) → Edge Gateway OPC-UA (Tầng 2) → Phần mềm MES tính OEE (Tầng 3) → Đồng bộ lệnh SX & BOM về SAP ERP (Tầng 4)."
        ),
        "related": ["MES", "ERP", "SCADA", "PLC"],
        "doc_key": "erp_mes"
    },
    "Minitab": {
        "term": "Minitab",
        "full_name": "Minitab Statistical Software — Phần Mềm Thống Kê Chất Lượng & Six Sigma Chuẩn Công Nghiệp",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["Minitab"],
        "case_sensitive": [],
        "short_desc": "Phần mềm thống kê số 1 cho kỹ sư OE/Six Sigma dùng để vẽ biểu đồ SPC, tính Cp/Cpk, MSA Gage R&R, kiểm định t-test/ANOVA và DOE.",
        "definition": (
            "Minitab là phần mềm phân tích dữ liệu thống kê chuyên dụng cho cải tiến chất lượng và sản xuất tinh gọn (Lean Six Sigma). "
            "Thay vì phán đoán cảm tính 'chắc là máy tốt hơn rồi', Minitab giúp kỹ sư OE chứng minh bằng toán học xác suất (p-value, độ lệch chuẩn σ, năng lực quy trình Cpk) "
            "rằng quy trình có đang ổn định hay không, nguyên nhân nào thực sự gây lỗi và cải tiến Trước–Sau có thực sự hiệu quả không."
        ),
        "formula_or_spec": (
            "• 5 công cụ Minitab OE dùng nhiều nhất:\n"
            "  1. Stat → Control Charts (Xbar-R, I-MR, p-chart)\n"
            "  2. Stat → Quality Tools → Capability Analysis (Cp, Cpk, Pp, Ppk)\n"
            "  3. Stat → Quality Tools → Gage Study (Gage R&R Crossed)\n"
            "  4. Stat → Basic Statistics → 2-Sample t / Paired t / ANOVA\n"
            "  5. Stat → DOE (Design of Experiments tìm thông số tối ưu)"
        ),
        "cadivi_application": (
            "Tại Nhà máy CADIVI Miền Trung, Minitab trực tiếp tạo ra giá trị tiền tỷ ở 4 bài toán:\n"
            "1. Phân tích năng lực chiều dày cách điện PVC/XLPE (Capability Analysis): đo Cpk để thu hẹp độ lệch chuẩn, giúp hạ lớp nhựa bọc dư (Over-thickness) sát chuẩn TCVN mà không bị lỗi mỏng.\n"
            "2. Phân tích điện trở & đường kính sợi đồng kéo để triệt tiêu Copper Give-away.\n"
            "3. Chạy kiểm định 2-Sample t-test / ANOVA chứng minh hiệu quả dự án cải tiến Trước–Sau (p-value < 0.05) khi báo cáo Ban Giám đốc.\n"
            "4. Đánh giá hệ thống đo phòng Lab (MSA Gage R&R < 10%) đối với panme, kính hiển vi đo mặt cắt, cầu đo điện trở."
        ),
        "cadivi_example": (
            "Ví dụ tại dây chuyền đùn dây VC 2.5 mm²: Sau khi gắn Laser Gauge hồi tiếp kín, OE nhập 100 mẫu đường kính Trước (μ=3.46mm, σ=0.055mm) và 100 mẫu Sau (μ=3.36mm, σ=0.020mm) vào Minitab. "
            "Minitab trả về Cpk mới = 1.33 và 2-Sample t-test có p-value = 0.000 → Khẳng định chắc chắn >99.9% dự án giúp giảm 0.10mm đường kính thừa, tiết kiệm 1.1 tấn PVC/tháng/máy."
        ),
        "related": ["SPC", "Cpk", "Ppk", "Gage R&R", "2-Sample t-test", "ANOVA", "Six Sigma", "Over-thickness"],
        "doc_key": "minitab_spc"
    },
    "Power BI": {
        "term": "Power BI",
        "full_name": "Microsoft Power BI — Nền Tảng Trực Quan Hóa Dữ Liệu & Dashboard Quản Trị Thông Minh",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["Power BI", "PowerBI"],
        "case_sensitive": [],
        "short_desc": "Công cụ BI xây dựng Dashboard tương tác tự động cập nhật OEE, OLE, Pareto dừng máy, phế phẩm và BOM Variance cho nhà máy.",
        "definition": (
            "Power BI là nền tảng phân tích kinh doanh (Business Intelligence) của Microsoft cho phép kết nối trực tiếp vào thư mục Excel, SQL Server, ERP hay MES, "
            "mô hình hóa dữ liệu theo Star Schema, viết công thức DAX tính toán động và hiển thị thành các bảng điều khiển (Dashboard) tương tác trực quan trên máy tính, TV xưởng và điện thoại."
        ),
        "formula_or_spec": (
            "• Kiến trúc chuẩn: Power Query (ETL làm sạch) → Star Schema (Fact/Dim) → DAX Measures (OEE/OLE/BOM) → Visual Dashboard + Scheduled Refresh Gateway."
        ),
        "cadivi_application": (
            "Tại CADIVI Miền Trung, Chuyên viên OE xây Dashboard Power BI 3 tầng:\n"
            "1. Tầng Giám đốc: Theo dõi xu hướng OEE, OLE, sản lượng tấn đồng/km cáp, % phế đồng trần/đồng dính nhựa và chênh lệch BOM theo tháng.\n"
            "2. Tầng Quản đốc/OE: Biểu đồ Pareto 80/20 nguyên nhân dừng máy đùn/kéo/bện, Heatmap so sánh hiệu suất Ca 1 – Ca 2 – Ca 3, lọc tức thì theo từng máy.\n"
            "3. Tầng Theo dõi Kaizen: So sánh Before–After các dự án SMED và tổng giá trị tiết kiệm ROI lũy kế."
        ),
        "cadivi_example": (
            "Ví dụ: Thay vì mỗi thứ Hai mất nửa ngày tổng hợp slide PowerPoint báo cáo giao ban, OE thiết lập Power BI kết nối thẳng thư mục nhật ký ca của 4 phân xưởng qua Power Query → "
            "07:00 sáng tự động Refresh, Giám đốc bấm 1 click lọc ngay máy đùn nào có OEE < 65% để chỉ đạo gỡ nghẽn."
        ),
        "related": ["Power Query", "DAX", "OEE", "OLE", "BOM", "MES"],
        "doc_key": "powerbi_mfg"
    },
    "Power Query": {
        "term": "Power Query",
        "full_name": "Microsoft Power Query (M Language) — Công Cụ Tự Động Gom & Làm Sạch Dữ Liệu (ETL)",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["Power Query"],
        "case_sensitive": [],
        "short_desc": "Công cụ tích hợp sẵn trong Excel & Power BI giúp gom tự động hàng trăm file báo cáo ca chỉ bằng 1 nút Refresh.",
        "definition": (
            "Power Query là bộ máy ETL (Extract – Transform – Load) có sẵn trong tab Data của Excel và trong Power BI. "
            "Nó ghi lại toàn bộ các bước làm sạch dữ liệu (gom file trong thư mục, bỏ dòng trống, Unpivot bảng ngang thành dọc, ghép bảng định mức BOM) thành chuỗi thao tác tự động, xử lý mượt hàng triệu dòng vượt giới hạn 1 triệu dòng của sheet Excel."
        ),
        "formula_or_spec": (
            "• Luồng thao tác: Data → Get Data → From File → From Folder → Combine & Transform → Unpivot → Merge Queries → Load to Data Model."
        ),
        "cadivi_application": (
            "Đặc biệt hữu ích ngay trong 30 ngày đầu vào CADIVI nếu các tổ Kéo/Bện/Đùn vẫn đang ghi báo cáo sản lượng từng ca trên nhiều file Excel rời rạc: "
            "OE chỉ cần gom vào 1 thư mục chung và dùng Power Query nối tự động thành 1 bảng Fact chuẩn sạch không bao giờ copy-paste nhầm."
        ),
        "cadivi_example": (
            "Ví dụ: 4 phân xưởng × 3 ca × 26 ngày = 312 sheet nhật ký ca/tháng. Trước đây nhân viên thống kê mất 2 ngày copy-paste tay; "
            "sau khi OE thiết lập Power Query Folder Connector, toàn bộ 312 file được làm sạch, Unpivot mã lỗi dừng máy và tính OEE trong đúng 3 giây!"
        ),
        "related": ["Power BI", "DAX", "VBA", "OEE", "Pareto"],
        "doc_key": "excel_mfg"
    },
    "DAX": {
        "term": "DAX",
        "full_name": "Data Analysis Expressions — Ngôn Ngữ Công Thức Phân Tích Trong Power BI & Power Pivot",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["DAX"],
        "case_sensitive": ["DAX"],
        "short_desc": "Ngôn ngữ viết các chỉ số đo lường động (Measures) như OEE, OLE, BOM Variance, Pareto lũy kế trong Power BI/Excel Data Model.",
        "definition": (
            "DAX là ngôn ngữ công thức chuyên dụng trong Power BI và Excel Power Pivot để tính toán tổng hợp động theo ngữ cảnh bộ lọc (Filter Context). "
            "Khác với công thức ô Excel cố định, một Measure DAX tính OEE tự động đúng cho cả 1 ca, 1 máy, 1 phân xưởng hay toàn nhà máy khi người dùng bấm chọn Slicer."
        ),
        "formula_or_spec": (
            "• Hàm xương sống: DIVIDE(), SUMX(), CALCULATE(), RELATED(), ALLSELECTED(), VAR ... RETURN.\n"
            "• Quy tắc: KHÔNG bao giờ tính trung bình cộng của cột OEE% (Average of Averages bị sai toán học!) — PHẢI dùng DAX tính tổng tử số chia tổng mẫu số."
        ),
        "cadivi_example": (
            "Ví dụ: Viết Measure `Performance_Cable_Rate = DIVIDE(SUMX(Fact_Prod, DIVIDE(TotalMeters, RELATED(Dim_SKU[IdealSpeed]))), ActualOperatingMin)` "
            "để tính chính xác Hiệu suất tốc độ mét/phút trên đồng thời nhiều mã cáp có tốc độ chuẩn khác nhau (từ 25 m/phút đến 400 m/phút)."
        ),
        "cadivi_application": (
            "Giúp OE CADIVI tính chính xác tuyệt đối OEE tổng hợp đa mã cáp, tính tỷ lệ hao hụt đồng/nhựa theo trọng số khối lượng và vẽ biểu đồ Pareto 80/20 tự động thay đổi theo bộ lọc ca/tháng."
        ),
        "related": ["Power BI", "Power Query", "OEE", "BOM", "Pareto"],
        "doc_key": "powerbi_mfg"
    },
    "VBA": {
        "term": "VBA",
        "full_name": "Visual Basic for Applications — Ngôn Ngữ Lập Trình Macro Tự Động Hóa Excel/Access",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["VBA", "Macro VBA"],
        "case_sensitive": ["VBA"],
        "short_desc": "Công cụ viết kịch bản tự động hóa thao tác lặp lại trong Excel/Access như xuất PDF báo cáo ca, kiểm tra lỗi nhập liệu, gửi email định kỳ.",
        "definition": (
            "VBA là ngôn ngữ lập trình tích hợp sẵn trong bộ Microsoft Office (Excel, Access) cho phép tự động hóa mọi thao tác lặp đi lặp lại: "
            "đọc/ghi file dữ liệu máy đo, định dạng bảng báo cáo, xuất PDF hàng loạt và tạo form nhập liệu có kiểm tra ràng buộc (Poka-Yoke nhập liệu)."
        ),
        "formula_or_spec": (
            "• Mở trình soạn thảo trong Excel: Alt + F11 → Insert Module.\n"
            "• Kết hợp tối ưu: Power Query/Python xử lý dữ liệu nặng + VBA xử lý tự động hóa giao diện nhập liệu/in ấn/xuất PDF trực tiếp trong Excel sẵn có của xưởng."
        ),
        "cadivi_application": (
            "Đây là thế mạnh trực tiếp trong CV của bạn (đã rút báo cáo khách hàng từ 3–7 ngày xuống 2 giờ và nhập liệu OGP từ 120 phút xuống 15 phút)! "
            "Tại CADIVI, bạn có thể áp dụng ngay để tạo Form nhập nhật ký ca chống nhập sai mã lỗi/số âm, tự động tổng hợp báo cáo OEE/BOM sáng hằng ngày và xuất PDF gửi Ban Giám đốc trong 1 click."
        ),
        "cadivi_example": (
            "Ví dụ: Viết Macro VBA cho sổ giao ca xưởng đùn: khi Tổ trưởng chọn mã cáp `VC 2.5`, Excel tự khóa tốc độ chuẩn 350 m/phút và cảnh báo đỏ ngay nếu tổng thời gian chạy + dừng ≠ 450 phút/ca, chấm dứt 100% lỗi sai số cộng trừ."
        ),
        "related": ["Power Query", "Power BI", "Barcode", "OEE", "BOM"],
        "doc_key": "excel_mfg"
    },
    "AutoCAD": {
        "term": "AutoCAD",
        "full_name": "Autodesk AutoCAD — Phần Mềm Thiết Kế Bản Vẽ Kỹ Thuật 2D/3D & Mặt Bằng Nhà Xưởng",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["AutoCAD"],
        "case_sensitive": [],
        "short_desc": "Phần mềm CAD tiêu chuẩn để vẽ bố trí mặt bằng nhà xưởng (Plant Layout), sơ đồ Spaghetti, hành lang cầu trục và thiết kế đồ gá Poka-Yoke.",
        "definition": (
            "AutoCAD là phần mềm vẽ kỹ thuật chính xác theo tỷ lệ thực 1:1. Đối với Chuyên viên OE/IE, AutoCAD dùng để đo chính xác diện tích phân xưởng, "
            "mô phỏng phương án sắp xếp lại dây chuyền (Layout Optimization), đo tổng chiều dài quãng đường di chuyển trên sơ đồ Spaghetti và phác thảo bản vẽ đồ gá cải tiến/xe đẩy SMED gửi xưởng cơ khí gia công."
        ),
        "formula_or_spec": (
            "• Lệnh OE hay dùng: PLINE + LIST (đo chính xác chiều dài đường Spaghetti), AREA (tính diện tích m² tiết kiệm), LAYER (tách lớp máy móc / lối xe nâng / đường đi bộ / vùng đệm WIP)."
        ),
        "cadivi_application": (
            "Tại CADIVI Miền Trung, AutoCAD giúp OE:\n"
            "1. Quy hoạch lại khu đệm siêu thị rulo (WIP Supermarket) giữa xưởng Kéo – Bện – Đùn đảm bảo bán kính quay đầu xe nâng ≥ 3.5m và nằm trọn trong vùng phủ cầu trục 2–5 tấn.\n"
            "2. Vẽ sơ đồ Spaghetti và thiết kế lại chuyền chữ U/L cho khu đóng cuộn khoanh 100m.\n"
            "3. Phác thảo xe đồ nghề SMED 5S di động và bàn thao tác chuẩn Ergonomics."
        ),
        "cadivi_example": (
            "Ví dụ: Dùng lệnh PLINE trên bản vẽ AutoCAD khu đóng gói dây dân dụng, OE đo được công nhân đi bộ 5.8 km/ca. Sau khi vẽ phương án xoay máy cuộn + lắp giá Flow Rack cấp thùng carton, quãng đường rút xuống 1.9 km/ca (-67%) và tiết kiệm 45 m² mặt bằng."
        ),
        "related": ["Spaghetti", "5S", "Ergonomics", "SMED", "WIP"],
        "doc_key": "autocad_layout"
    },
    "Barcode": {
        "term": "Barcode",
        "full_name": "Barcode / QR Code & RFID — Hệ Thống Nhận Dạng & Truy Xuất Tự Động Tại Xưởng",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["Barcode", "QR Code", "RFID", "mã vạch"],
        "case_sensitive": ["RFID"],
        "short_desc": "Công nghệ quét mã vạch/QR/RFID thay thế ghi chép tay để ghi nhận sản lượng, chống nhầm rulo (Poka-Yoke) và truy xuất nguồn gốc tức thì.",
        "definition": (
            "Hệ thống Barcode/QR gắn mã định danh duy nhất cho từng rulo nguyên liệu, rulo bán thành phẩm, lệnh sản xuất và nhân viên vận hành. "
            "Chỉ 1 thao tác quét súng trong 0.5 giây thay thế toàn bộ việc viết sổ tay thủ công, loại bỏ nhầm lẫn mã hàng và giúp dữ liệu đi thẳng vào Excel/MES."
        ),
        "formula_or_spec": (
            "• Thông tin chuẩn trên Tem QR Rulo Cáp: [Mã Lệnh SX] | [Mã Cáp/Tiết Diện] | [Số Serial Rulo] | [Chiều Dài mét] | [Khối Lượng kg] | [Máy/Ca/Người Chạy]."
        ),
        "cadivi_application": (
            "Cầu nối trực tiếp từ kinh nghiệm triển khai quét mã vạch công đoạn RE7 tại Fujikura của bạn sang CADIVI:\n"
            "1. Quản lý vị trí & FIFO kho rulo WIP (tìm đúng rulo dưới 2 phút).\n"
            "2. Poka-Yoke quét rulo trước khi nạp vào máy bện/máy đùn chống nhầm tiết diện đồng hoặc nhầm loại nhựa PVC/XLPE.\n"
            "3. Ghi nhận tự động năng suất lao động OLE và tỷ lệ lỗi theo từng công đoạn/ca."
        ),
        "cadivi_example": (
            "Ví dụ: Dán tem mã vạch chịu dầu cho 300 rulo thép luân chuyển giữa Kéo – Bện – Đùn. Mỗi khi máy bện hoàn thành, thợ quét tem rulo → tự in phiếu mét + nhập vị trí ô kệ → máy đùn quét nhận rulo xác thực đúng mã BOM rồi mới chạy."
        ),
        "related": ["MES", "Poka-Yoke", "OLE", "WIP", "VBA"],
        "doc_key": "erp_mes"
    },

    # =================================================================
    # NHÓM 2: CÁC CHỈ SỐ HIỆU SUẤT CỐT LÕI (OEE, TEEP, OLE, KPI)
    # =================================================================
    "OEE": {
        "term": "OEE",
        "full_name": "Overall Equipment Effectiveness — Hiệu Suất Sử Dụng Thiết Bị Tổng Thể",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["OEE", "Overall Equipment Effectiveness"],
        "case_sensitive": ["OEE"],
        "short_desc": "Thước đo vàng quốc tế đo tỷ lệ thời gian máy móc thực sự tạo ra sản phẩm đạt chuẩn (OEE = Availability × Performance × Quality).",
        "definition": (
            "OEE là chỉ số cốt lõi nhất của Chuyên viên OE nhằm đo lường tổng thể mức độ khai thác máy móc so với khả năng lý thuyết trong thời gian kế hoạch chạy máy. "
            "OEE bóc tách trọn vẹn 6 tổn thất lớn (Six Big Losses) thành 3 thành phần: Độ sẵn sàng (A — máy có chạy không?), Hiệu suất tốc độ (P — máy chạy có đúng tốc độ thiết kế không?) và Chất lượng (Q — làm ra có đạt chuẩn không?)."
        ),
        "formula_or_spec": (
            "• OEE = Availability (A) × Performance (P) × Quality (Q)\n"
            "  - A = Thời gian chạy thực / Thời gian kế hoạch (bắt lỗi Hỏng máy & Đổi mã SMED)\n"
            "  - P (ngành cáp) = Tổng chiều dài (m) / (Thời gian chạy thực × Tốc độ chuẩn m/phút) (bắt lỗi Vi dừng & Chạy chậm)\n"
            "  - Q = Chiều dài đạt chuẩn / Tổng chiều dài đùn ra (bắt lỗi Phế startup & Lỗi Spark/Lệch tâm)\n"
            "• Mốc chuẩn: < 50% (Báo động) | 60–70% (Trung bình) | ≥ 85% (World-Class)."
        ),
        "cadivi_application": (
            "Tại Nhà máy CADIVI Miền Trung, OEE PHẢI được đo theo tốc độ tuyến tính (mét/phút) cho các dây chuyền Kéo – Bện – Đùn thay vì đếm theo cái, "
            "và ưu tiên siết chặt OEE ≥ 85% cho các máy ĐIỂM NGHẼN (Bottleneck như dây chuyền Đùn bọc chủ lực, Máy kéo thô RBD) chứ không ép đẩy OEE mù quáng ở máy phụ trợ gây tồn kho WIP."
        ),
        "cadivi_example": (
            "Ví dụ Dây chuyền Đùn PVC Ø70mm chạy dây VC 2.5mm² (tốc độ chuẩn 350 m/phút, ca 450 phút kế hoạch): Dừng đổi màu/thay rulo/Spark hết 90 phút → A = 360/450 = 80.0%; "
            "Đùn ra 108,000m (chạy trung bình 300 m/phút) → P = 108,000/(360×350) = 85.7%; Phế startup & lỗi 5,400m → Q = 102,600/108,000 = 95.0% → OEE = 65.14%. "
            "Áp dụng SMED + hạ nhiệt nước làm mát Chiller nâng OEE lên 84.6% (+30% sản lượng không mua máy mới!)."
        ),
        "related": ["TEEP", "OLE", "SMED", "TPM", "TOC", "Spark Tester", "MES"],
        "doc_key": "oee"
    },
    "TEEP": {
        "term": "TEEP",
        "full_name": "Total Effective Equipment Performance — Hiệu Suất Thiết Bị Toàn Phần Theo Lịch 24/7",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["TEEP", "Total Effective Equipment Performance"],
        "case_sensitive": ["TEEP"],
        "short_desc": "Chỉ số đo năng lực khai thác máy tính trên tổng 24 giờ × 7 ngày, dùng để thẩm định xem có thực sự cần mua thêm máy mới (CAPEX) hay không.",
        "definition": (
            "Trong khi OEE chỉ tính trên thời gian có lịch chạy máy (vd: 1 hoặc 2 ca/ngày), TEEP tính trên toàn bộ 168 giờ/tuần (24/7). "
            "TEEP phơi bày 'công suất ẩn' bị bỏ trống vào ca đêm, ngày nghỉ hoặc khi thiếu đơn hàng."
        ),
        "formula_or_spec": (
            "• TEEP = OEE × Loading Factor\n"
            "• Loading Factor = Thời gian lên kế hoạch chạy máy / Tổng thời gian lịch 24/7 (168 giờ/tuần)."
        ),
        "cadivi_application": (
            "Dùng cho Chuyên viên OE khi thẩm định đề xuất mua thêm máy kéo/máy bện/máy đùn hàng chục tỷ đồng tại CADIVI: "
            "trước khi duyệt CAPEX mua máy mới, luôn kiểm tra TEEP xem nhà máy đã khai thác hết ca 2/ca 3 và đã đẩy OEE qua SMED/TPM chưa."
        ),
        "cadivi_example": (
            "Ví dụ: Xưởng đề xuất mua thêm 1 máy bện Rigid 8 tỷ vì máy cũ đạt OEE = 82%. OE tính TEEP: máy đang chạy 2 ca × 7.5h × 6 ngày = 90h/tuần → Loading = 90/168 = 53.6% → TEEP = 43.9%. "
            "Chỉ cần mở thêm ca 3 (tăng lên 135h/tuần) sẽ tăng ngay +50% sản lượng mà tiết kiệm trọn vẹn 8 tỷ đồng vốn đầu tư!"
        ),
        "related": ["OEE", "CAPEX", "RCCP", "ROI"],
        "doc_key": "oee"
    },
    "OLE": {
        "term": "OLE",
        "full_name": "Overall Labor Effectiveness — Hiệu Quả Sử Dụng Lao Động Toàn Diện",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["OLE", "Overall Labor Effectiveness"],
        "case_sensitive": ["OLE"],
        "short_desc": "Chỉ số đo hiệu quả khai thác sức lao động trực tiếp (OLE = Hiện diện × Hiệu suất thao tác × Chất lượng tay nghề), chỉ số bắt buộc trong JD CADIVI.",
        "definition": (
            "OLE là phiên bản tương ứng của OEE dành cho con người. Một nhà máy có thể có OEE máy rất cao nhưng vẫn lỗ tiền lương nếu OLE thấp (tốn quá nhiều công nhân phục vụ 1 máy, công nhân chờ xe nâng cấp rulo, thao tác thừa hoặc làm lỗi phải cuộn lại). "
            "OLE đo lường trực tiếp chất lượng công tác tổ chức phân công, cân bằng chuyền, huấn luyện TWI và thiết kế bàn thao tác Ergonomics."
        ),
        "formula_or_spec": (
            "• OLE = Availability (Hiện diện) × Utilization/Performance (Hiệu suất thao tác) × Quality (Chất lượng tay nghề)\n"
            "  - A_labor = Thời gian thực tế đứng vị trí thao tác / Thời gian trả lương phân công\n"
            "  - U_labor = (Sản lượng × Định mức thời gian chuẩn SAM) / Thời gian thực tế thao tác\n"
            "  - Q_labor = Sản phẩm không lỗi thao tác / Tổng sản phẩm thao tác\n"
            "• Thang chuẩn: < 60% (Báo động) | 60–75% (Trung bình) | 75–85% (Tốt) | > 85% (World-Class)."
        ),
        "cadivi_application": (
            "Tại CADIVI Miền Trung, OLE đặc biệt quan trọng ở 2 khu vực:\n"
            "1. Khu Kéo tinh & Máy bện Buncher: tối ưu tỷ lệ người/máy bằng Biểu đồ Người–Máy (Man-Machine Chart — chuyển từ 1 người đứng 2 máy lên 1 người đứng 3 máy).\n"
            "2. Tổ Đóng cuộn khoanh 100m, bọc màng co nhiệt, dán tem & xếp pallet (thâm dụng lao động thủ công cao): áp dụng Time Study, Yamazumi và Ergonomics để tăng sản lượng/người mà công nhân lại đỡ mệt."
        ),
        "cadivi_example": (
            "Ví dụ tại tổ Đóng cuộn 100m dây dân dụng (10 người × 450p = 4,500 phút công): mất 290 phút công do đi trễ & họp đột xuất (A=93.6%); "
            "làm 1,850 cuộn với định mức 2.0 phút công/cuộn (U=87.9%); 55 cuộn lỗi màng co/nhãn phải bọc lại (Q=97.0%) → Line OLE = 79.8% (tương đương thất thoát ~47 triệu VNĐ quỹ lương/tháng trên 1 tổ!)."
        ),
        "related": ["OEE", "Time Study", "Man-Machine Chart", "Yamazumi", "LBE", "Ergonomics", "TWI"],
        "doc_key": "ole"
    },
    "Time Study": {
        "term": "Time Study",
        "full_name": "Time & Motion Study — Nghiên Cứu Thời Gian & Thao Tác (Thiết Lập Định Mức Chuẩn SAM)",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Time Study", "Motion Study", "Time & Motion Study", "SAM"],
        "case_sensitive": ["SAM"],
        "short_desc": "Kỹ thuật bấm giờ/quay video bóc tách cử động (VA / NNVA / NVA) để xây dựng định mức thời gian chuẩn (SAM) và tài liệu Standard Work.",
        "definition": (
            "Time & Motion Study là kỹ năng cốt lõi của kỹ sư IE/OE: quan sát thực tế, bấm giờ (hoặc quay video) 10–20 chu kỳ lặp lại, loại bỏ ngoại lệ, nhân hệ số đánh giá nhịp độ (Rating Factor) "
            "và cộng phụ cấp mệt mỏi/sinh lý (Allowances 10–15%) để xác lập Thời gian Chuẩn (Standard Time / SAM). Đồng thời phân tách từng thao tác thành VA (Tạo giá trị), NNVA (Cần thiết) và NVA (Lãng phí phải xóa)."
        ),
        "formula_or_spec": (
            "• Normal Time (NT) = Observed Time (OT) × Rating Factor (RF)\n"
            "• Standard Time (ST / SAM) = Normal Time × (1 + Allowance %)"
        ),
        "cadivi_application": (
            "Thế mạnh sẵn có của bạn từ dự án Canon INEX (60s → 30s) tại Mabuchi! Tại CADIVI, bạn dùng Time Study để:\n"
            "1. Bóc tách từng giây thao tác nạp rulo máy bện và đổi màu/thay khuôn máy đùn (làm đầu vào cho SMED).\n"
            "2. Đo chu kỳ thực tế khâu đóng cuộn/bọc màng co/dán tem để thiết lập định mức công nhân chuẩn (SAM) tính OLE.\n"
            "3. Xây dựng tài liệu Thao tác chuẩn (Standard Work / SOP) đào tạo đồng bộ giữa 3 ca."
        ),
        "cadivi_example": (
            "Ví dụ: Quay video 15 chu kỳ thao tác tháo-lắp rulo trên máy bện Buncher: OT trung bình = 7.2 phút, RF = 100%, Allowance = 11% → ST = 8.0 phút/lần. "
            "Trong đó phát hiện 2.4 phút (30% NVA) chỉ để đi tìm kìm cắt và chờ xe đẩy rulo → cắt bỏ ngay NVA đưa chu kỳ về 5.6 phút."
        ),
        "related": ["OLE", "SMED", "Yamazumi", "Man-Machine Chart", "Ergonomics"],
        "doc_key": "ole"
    },
    "Man-Machine Chart": {
        "term": "Man-Machine Chart",
        "full_name": "Biểu Đồ Người – Máy (Multiple Activity Chart — Tối Ưu 1 Người Đứng Nhiều Máy)",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Man-Machine Chart", "Biểu đồ Người–Máy", "Biểu đồ Người-Máy", "Multi-Machine"],
        "case_sensitive": [],
        "short_desc": "Công cụ trực quan hóa thời gian bận/rảnh đồng thời của Công nhân và Máy móc để xác định số máy tối ưu 1 người đứng (Multi-machine tending).",
        "definition": (
            "Man-Machine Chart vẽ song song dòng thời gian của công nhân (thao tác nạp/tháo, di chuyển, chờ) và dòng thời gian của từng máy (tự chạy, dừng chờ người) trong cùng 1 chu kỳ. "
            "Nhờ đó kỹ sư OE tìm ra số máy tối ưu N để tối đa hóa OLE của người mà không gây hiện tượng 'máy chờ người' làm tụt OEE."
        ),
        "formula_or_spec": (
            "• Số máy tối đa lý thuyết 1 công nhân đứng:\n"
            "  N = (a + T) / (a + w)\n"
            "  (a: thời gian thao tác máy dừng; T: thời gian máy tự chạy; w: thời gian di chuyển & kiểm tra giữa các máy)."
        ),
        "cadivi_application": (
            "Ứng dụng kinh điển tại xưởng Kéo trung/kéo tinh và xưởng Bện xoắn đôi (Buncher) của CADIVI — nơi máy tự chạy liên tục 25–45 phút mới đầy 1 rulo nên 1 thợ hoàn toàn có thể đứng 3–4 máy."
        ),
        "cadivi_example": (
            "Ví dụ xưởng Bện Buncher CADIVI: a = 8 phút (đổi rulo + nối dây), w = 2 phút (đi sang máy kế), T = 32 phút (máy tự chạy) → N = (8+32)/(8+2) = 4 máy. "
            "Để dự phòng giao thoa xử lý đứt sợi, OE chốt 1 người đứng 3 máy (tăng từ 2 lên 3 máy) → OLE tăng +50%, tiết kiệm 33% nhân công trực tiếp!"
        ),
        "related": ["OLE", "OEE", "Time Study", "Buncher", "Shojinka"],
        "doc_key": "ole"
    },
    "Takt Time": {
        "term": "Takt Time",
        "full_name": "Takt Time — Nhịp Điệu Nhu Cầu Khách Hàng",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Takt Time"],
        "case_sensitive": [],
        "short_desc": "Khoảng thời gian tối đa cho phép để xuất xưởng 1 đơn vị sản phẩm nhằm đáp ứng đúng tiến độ đơn hàng của thị trường.",
        "definition": (
            "Takt Time (tiếng Đức: 'nhịp trống') không phải là tốc độ máy hay năng lực nhà máy, mà là NHỊP ĐIỆU CỦA THỊ TRƯỜNG quyết định: "
            "cứ mỗi bao nhiêu giây/phút thì nhà máy PHẢI hoàn thành 1 sản phẩm (hoặc 1 cuộn 100m / 1 km cáp) để giao hàng đúng hạn mà không sản xuất thừa."
        ),
        "formula_or_spec": (
            "• Takt Time = Thời gian làm việc khả dụng trong ca / Nhu cầu sản lượng khách hàng trong ca\n"
            "• Nguyên tắc vàng: Cycle Time của trạm chậm nhất (Bottleneck) phải ≤ Takt Time (thường đặt Target CT = 90–95% Takt Time)."
        ),
        "cadivi_application": (
            "Tại CADIVI, OE dùng Takt Time để cân bằng chuyền tổ Đóng cuộn khoanh 100m dây dân dụng và tính tốc độ mét/phút mục tiêu trên dây chuyền đùn nhằm đáp ứng kế hoạch giao hàng tháng."
        ),
        "cadivi_example": (
            "Ví dụ: Kế hoạch xuất 1,100 cuộn dây VC 1.5 (100m/cuộn) trong 1 ca 440 phút (26,400 giây) → Takt Time = 26,400 / 1,100 = 24 giây/cuộn. "
            "Nếu trạm buộc dây & dán tem đang mất 28 giây/cuộn (> 24s) → Chắc chắn trễ giao hàng, bắt buộc phải cải tiến cân bằng chuyền!"
        ),
        "related": ["Cycle Time", "Lead Time", "Yamazumi", "LBE", "Smoothness Index"],
        "doc_key": "ole"
    },
    "Cycle Time": {
        "term": "Cycle Time",
        "full_name": "Cycle Time — Thời Gian Chu Kỳ Gia Công Thực Tế",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Cycle Time"],
        "case_sensitive": [],
        "short_desc": "Thời gian thực tế cần thiết để 1 công đoạn hoặc dây chuyền hoàn thành xong 1 sản phẩm/cuộn hàng (quyết định bởi trạm nghẽn nhất).",
        "definition": (
            "Cycle Time (CT) là khoảng thời gian thực tế đo được bằng đồng hồ bấm giờ tại xưởng giữa 2 sản phẩm hoàn chỉnh liên tiếp đi ra khỏi trạm hoặc cuối dây chuyền. "
            "Cycle Time phản ánh NĂNG LỰC THỰC TẾ của quá trình, dùng để so sánh với Takt Time (nhu cầu khách hàng)."
        ),
        "formula_or_spec": (
            "• Cycle Time toàn chuyền = max(CT_trạm_1, CT_trạm_2, ..., CT_trạm_n) = CT của trạm Bottleneck.\n"
            "• Với dây chuyền liên tục (đùn/kéo cáp): CT cho 1 cuộn 100m = 100m / Tốc độ chạy thực tế (m/phút)."
        ),
        "cadivi_application": (
            "Đo Cycle Time từng công đoạn tại tổ đóng cuộn khoanh, nạp rulo máy bện và thử nghiệm mẫu phòng Lab để tìm đúng nút cổ chai cần giải tỏa."
        ),
        "cadivi_example": (
            "Ví dụ: Trên dây chuyền đóng gói dây dân dụng, CT máy cuộn = 18s, CT dán tem/buộc dây = 28s, CT bọc màng co = 20s → Cycle Time toàn chuyền bị khóa cứng ở 28s (chỉ ra tối đa 128 cuộn/giờ thay vì 200 cuộn/giờ)."
        ),
        "related": ["Takt Time", "Lead Time", "Yamazumi", "LBE", "TOC"],
        "doc_key": "ole"
    },
    "Lead Time": {
        "term": "Lead Time",
        "full_name": "Production Lead Time — Tổng Thời Gian Lưu Chuyển Đơn Hàng Từ Đầu Đến Cuối",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Lead Time"],
        "case_sensitive": [],
        "short_desc": "Tổng thời gian từ lúc đồng rod/vật tư nhập xưởng đến khi thành phẩm cáp hoàn chỉnh xuất kho (gồm cả thời gian nằm chờ WIP).",
        "definition": (
            "Lead Time là toàn bộ quãng thời gian sản phẩm đi xuyên qua nhà máy — bao gồm thời gian gia công thực sự (Value-Added Time, thường chỉ chiếm 5–10%) "
            "CỘNG VỚI toàn bộ thời gian rulo nằm xếp hàng chờ đợi giữa các xưởng Kéo – Bện – Đùn – Xông XLPE – QC (chiếm tới 90–95%)."
        ),
        "formula_or_spec": (
            "• Định luật Little (Little's Law): Lead Time = Tồn kho WIP / Tốc độ xuất xưởng (Throughput).\n"
            "• Hiệu quả Chuỗi giá trị (PCE%) = (Tổng VA Time / Tổng Lead Time) × 100%."
        ),
        "cadivi_application": (
            "Rút ngắn Lead Time là vũ khí cạnh tranh số 1 cho các đơn hàng dự án cáp lực CXV/DSTA của CADIVI Miền Trung: cắt giảm thời gian rulo chờ giữa các phân xưởng và chờ bể xông hơi XLPE giúp giao hàng nhanh gấp 2–3 lần đối thủ."
        ),
        "cadivi_example": (
            "Ví dụ trên VSM lô 10 km cáp CXV 3x50+1x25: Tổng thời gian chạy máy thật chỉ 27.5 giờ (1.15 ngày), nhưng tổng Lead Time hiện trạng là 12 ngày (PCE = 9.55%). "
            "Nhờ giới hạn kho đệm CONWIP và áp dụng SMED, Lead Time giảm còn 4.2 ngày!"
        ),
        "related": ["VSM", "WIP", "Cycle Time", "Takt Time", "Kanban", "Silane"],
        "doc_key": "lean_muda"
    },
    "Yamazumi": {
        "term": "Yamazumi",
        "full_name": "Yamazumi Chart — Biểu Đồ Xếp Chồng Thao Tác Cân Bằng Chuyền",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Yamazumi", "Yamazumi Chart"],
        "case_sensitive": [],
        "short_desc": "Biểu đồ cột xếp chồng chia màu Xanh (VA) – Vàng (NNVA) – Đỏ (NVA) so với đường ngang Takt Time để tái phân bổ công việc cân bằng chuyền.",
        "definition": (
            "Yamazumi (tiếng Nhật: 'chồng núi') là biểu đồ cột thể hiện tổng thời gian công việc của từng công nhân/trạm trên dây chuyền, "
            "trong đó mỗi cột được chia thành các khối thao tác nhỏ tô 3 màu (VA xanh, NNVA vàng, NVA đỏ) đặt cạnh đường chuẩn Takt Time để cắt gọt lãng phí và san sẻ tải giữa các trạm."
        ),
        "formula_or_spec": (
            "• 4 bước dùng Yamazumi: (1) Vẽ cột từng trạm + đường Takt Time → (2) Xóa khối Đỏ (NVA) → (3) San sẻ khối thao tác từ trạm vượt Takt sang trạm thấp hơn → (4) Giảm bớt số trạm/người thừa."
        ),
        "cadivi_application": (
            "Áp dụng cực hiệu quả cho khu Đóng cuộn khoanh 100m, khu Dán nhãn/Đóng thùng và Phòng Lab kiểm tra mẫu đầu vào/đầu ra tại CADIVI."
        ),
        "cadivi_example": (
            "Ví dụ: Tái cân bằng chuyền đóng gói 5 trạm từ chu kỳ lệch [24s, 42s, 18s, 35s, 26s] (LBE=69.05%) thành [29s, 28s, 25s, 28s, 26s] nhờ san sẻ bước dán tem & gá sẵn → LBE nhảy vọt lên 93.79%, mượt hóa toàn chuyền!"
        ),
        "related": ["LBE", "Smoothness Index", "Takt Time", "OLE", "Time Study"],
        "doc_key": "ole"
    },
    "LBE": {
        "term": "LBE",
        "full_name": "Line Balancing Efficiency — Hiệu Suất Cân Bằng Dây Chuyền",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["LBE", "Line Balancing Efficiency", "Line Balancing"],
        "case_sensitive": ["LBE"],
        "short_desc": "Chỉ số phần trăm đo mức độ phân bổ đều khối lượng công việc giữa các trạm/công nhân trên dây chuyền (mục tiêu ≥ 85%).",
        "definition": (
            "LBE đánh giá tỷ lệ thời gian làm việc hữu ích của toàn dây chuyền so với tổng thời gian bị khóa theo nhịp của trạm chậm nhất (Bottleneck). "
            "LBE thấp có nghĩa là rất nhiều công nhân đang phải đứng chờ rảnh rỗi trong khi 1–2 trạm bị quá tải."
        ),
        "formula_or_spec": (
            "• LBE (%) = [ Tổng Cycle Time tất cả các trạm / (Số trạm × Cycle Time trạm lớn nhất) ] × 100%\n"
            "• Chuẩn Lean: LBE ≥ 85% (dưới 75% là mất cân bằng nghiêm trọng)."
        ),
        "cadivi_application": (
            "Đo và tối ưu cân bằng tải cho tổ đóng cuộn khoanh dây dân dụng và tổ chuẩn bị rulo/đóng kiện xuất hàng tại CADIVI Miền Trung."
        ),
        "cadivi_example": (
            "Ví dụ tổ đóng cuộn 4 người có CT các trạm là [18s, 28s, 20s, 16s] → Tổng CT = 82s → LBE = 82 / (4 × 28) = 73.2%. "
            "Sau cải tiến rút còn 3 người [19s, 20s, 18s] → LBE = 57 / (3 × 20) = 95.0%!"
        ),
        "related": ["Yamazumi", "Smoothness Index", "OLE", "Takt Time", "Cycle Time"],
        "doc_key": "ole"
    },
    "Smoothness Index": {
        "term": "Smoothness Index",
        "full_name": "Smoothness Index (SI) — Chỉ Số Độ Mượt Mà Của Dây Chuyền",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Smoothness Index"],
        "case_sensitive": [],
        "short_desc": "Chỉ số đo độ chênh lệch tải giữa các trạm so với trạm nút thắt (SI càng tiến về 0 thì dây chuyền càng đồng đều, không áp lực cục bộ).",
        "definition": (
            "Smoothness Index (SI) bổ trợ cho LBE bằng cách đo độ phân tán áp lực công việc giữa các công nhân trên chuyền. "
            "SI = 0 có nghĩa là tất cả các trạm có chu kỳ làm việc bằng nhau tuyệt đối, triệt tiêu hoàn toàn hiện tượng đói hàng (Starvation) và nghẽn hàng (Blocking)."
        ),
        "formula_or_spec": (
            "• SI = sqrt( Tổng [ (CT_max - CT_i)² ] )\n"
            "• Đơn vị: giây (càng nhỏ gần 0 càng tốt)."
        ),
        "cadivi_application": (
            "Dùng song song với LBE trong báo cáo Trước–Sau cải tiến cân bằng chuyền để chứng minh áp lực làm việc của công nhân tổ đóng gói đã đồng đều, giảm mệt mỏi cuối ca."
        ),
        "cadivi_example": (
            "Ví dụ: Tái cân bằng 5 trạm từ [24, 42, 18, 35, 26] xuống [29, 28, 25, 28, 26] giúp SI giảm mạnh từ 34.71 giây xuống chỉ còn 5.20 giây!"
        ),
        "related": ["LBE", "Yamazumi", "OLE", "Takt Time"],
        "doc_key": "ole"
    },

    # =================================================================
    # NHÓM 3: SẢN XUẤT TINH GỌN (LEAN), SMED, 5S, VSM, POKA-YOKE
    # =================================================================
    "Lean": {
        "term": "Lean",
        "full_name": "Lean Manufacturing — Hệ Thống Sản Xuất Tinh Gọn (Gốc Toyota Production System)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Lean", "Lean Manufacturing", "TPS"],
        "case_sensitive": ["TPS"],
        "short_desc": "Triết lý quản trị sản xuất tập trung loại bỏ 8 loại lãng phí (TIMWOODS), rút ngắn Lead Time và tạo dòng chảy liên tục theo nhu cầu khách hàng.",
        "definition": (
            "Lean Manufacturing là hệ thống phương pháp quản trị xuất phát từ Toyota (TPS), dựa trên 5 nguyên tắc: Xác định giá trị → Vẽ bản đồ chuỗi giá trị (VSM) → Tạo dòng chảy → Thiết lập hệ thống Kéo (Pull/Kanban) → Hoàn thiện liên tục (Kaizen). "
            "Mục tiêu tối thượng của Lean là tăng tốc độ chuyển hóa nguyên vật liệu thành tiền mặt bằng cách xóa bỏ MỌI hoạt động không tạo giá trị mà khách hàng không trả tiền."
        ),
        "formula_or_spec": (
            "• 8 Lãng phí (TIMWOODS): Transportation, Inventory, Motion, Waiting, Overproduction (Nguy hiểm #1), Overprocessing, Defects, Skills Unused.\n"
            "• 2 trụ cột Ngôi nhà TPS: Just-In-Time (Đúng lúc) & Jidoka (Chất lượng tại nguồn)."
        ),
        "cadivi_application": (
            "Là nhiệm vụ cốt lõi ghi rõ trong JD CADIVI Miền Trung: triển khai đồng bộ 5S, SMED đổi màu máy đùn, VSM giảm tồn kho rulo WIP, Poka-Yoke chống lỗi đứt sợi/nhầm rulo và phong trào Kaizen tại 4 phân xưởng."
        ),
        "cadivi_example": (
            "Ví dụ: Áp dụng Lean toàn chuỗi cho dòng cáp lực CXV tại CADIVI cắt giảm 65% rulo bán thành phẩm nằm chờ trên sàn, rút Lead Time từ 12 ngày xuống 4.2 ngày và giảm 50% thời gian chuyển đổi máy đùn."
        ),
        "related": ["VSM", "5S", "SMED", "Kaizen", "Poka-Yoke", "Kanban", "Jidoka", "Six Sigma"],
        "doc_key": "lean_muda"
    },
    "SMED": {
        "term": "SMED",
        "full_name": "Single-Minute Exchange of Die — Kỹ Thuật Chuyển Đổi Nhanh Khuôn/Mã Hàng Dưới 10 Phút",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["SMED", "Single-Minute Exchange of Die", "Changeover"],
        "case_sensitive": ["SMED"],
        "short_desc": "Phương pháp 4 bước của Shigeo Shingo giúp rút ngắn thời gian dừng máy chuyển đổi khuôn/màu nhựa/tiết diện giảm 50–85%.",
        "definition": (
            "SMED là hệ thống kỹ thuật phân tách thời gian chuyển đổi thành Thao tác Trong (Internal — chỉ làm khi máy dừng) và Thao tác Ngoài (External — làm được khi máy vẫn đang chạy), "
            "sau đó chuyển tối đa thao tác Trong ra Ngoài và cơ khí hóa thao tác Trong còn lại (kẹp 1 chạm, đầu tự định tâm, phối hợp song song 2 người F1 Pit-stop)."
        ),
        "formula_or_spec": (
            "• 4 Giai đoạn Shingo: (0) Quay video hiện trạng → (1) Tách Internal vs External → (2) Chuyển Internal thành External → (3) Tinh gọn cơ khí mọi thao tác.\n"
            "• Thời gian Changeover tính từ sản phẩm ĐẠT cuối lô A đến sản phẩm ĐẠT đầu lô B ở tốc độ chuẩn!"
        ),
        "cadivi_application": (
            "Vũ khí số 1 cho Chuyên viên OE CADIVI tại Dây chuyền Đùn bọc cáp & Máy Bện:\n"
            "1. Sấy nóng trước bộ đầu Chày–Cối (Crosshead/Tip-Die) ở tủ sấy ngoài đạt 160°C trước khi máy dừng.\n"
            "2. Sấy sẵn hạt nhựa màu mới trong phễu hút di động, kết hợp lập lịch Chuỗi Màu (Color Sequencing) và Hợp chất xả trục vít (Purging Compound).\n"
            "3. Dùng đầu chữ thập tháo lắp nhanh tự định tâm + lưu Recipe thông số trên PLC + xe đồ nghề 5S ngay cạnh máy."
        ),
        "cadivi_example": (
            "Ví dụ thực chiến trên máy đùn Ø70mm CADIVI đổi từ dây VC 4.0 Đen sang VC 2.5 Trắng: áp dụng SMED + Color Sequencing + sấy trước đầu đùn rút thời gian dừng máy từ 55 phút xuống 12 phút (-78.2%) và giảm nhựa xả purge từ 25 kg xuống 6 kg/lần!"
        ),
        "related": ["Color Sequencing", "Purging", "Crosshead", "OEE", "5S", "Extruder"],
        "doc_key": "smed"
    },
    "VSM": {
        "term": "VSM",
        "full_name": "Value Stream Mapping — Bản Đồ Chuỗi Giá Trị (Hiện Trạng & Tương Lai)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["VSM", "Value Stream Mapping", "Value Stream Map"],
        "case_sensitive": ["VSM"],
        "short_desc": "Sơ đồ trực quan vẽ cả dòng vật tư và dòng thông tin từ NVL đến khách hàng để phơi bày tồn kho WIP, Lead Time và chọn đúng điểm Kaizen.",
        "definition": (
            "VSM là công cụ cấp hệ thống giúp nhìn toàn cảnh nhà máy (Door-to-Door) thay vì nhìn rời rạc từng chiếc máy. "
            "Kỹ sư OE đi ngược từ khâu giao hàng về kho NVL để vẽ Current State Map (phơi bày Lead Time, điểm ùn tắc WIP, C/O, OEE từng bước) rồi thiết kế Future State Map tinh gọn kèm kế hoạch hành động 90 ngày."
        ),
        "formula_or_spec": (
            "• Thanh thời gian đáy VSM: Tầng trên = Thời gian chờ WIP (ngày) | Tầng dưới = Thời gian gia công VA (phút/giờ).\n"
            "• Process Cycle Efficiency (PCE) = Total VA Time / Total Lead Time × 100%."
        ),
        "cadivi_application": (
            "Ngay trong 2 tuần đầu Onboarding tại CADIVI Miền Trung, OE vẽ VSM cho 2 họ sản phẩm đại diện: (1) Dây dân dụng VC và (2) Cáp lực CXV để nhìn rõ rulo đang nằm chờ nhiều nhất ở công đoạn nào (Kéo→Bện hay Đùn→Xông XLPE→Ghép lõi)."
        ),
        "cadivi_example": (
            "Ví dụ VSM cáp CXV 3x50+1x25: Current State có VA Time = 27.5 giờ nhưng Lead Time = 12 ngày (PCE = 9.55% do rulo chờ 3 ngày trước máy đùn và 1.5 ngày trước bể Sauna). Future State thiết lập siêu thị Kanban cắt Lead Time còn 4.2 ngày (PCE = 27.3%)."
        ),
        "related": ["Lead Time", "WIP", "Lean", "Kanban", "TOC", "SMED"],
        "doc_key": "lean_muda"
    },
    "5S": {
        "term": "5S",
        "full_name": "5S — Seiri (Sàng lọc), Seiton (Sắp xếp), Seiso (Sạch sẽ), Seiketsu (Săn sóc), Shitsuke (Sẵn sàng)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["5S"],
        "case_sensitive": ["5S"],
        "short_desc": "Nền tảng quản trị trực quan tại hiện trường xưởng giúp loại bỏ đồ thừa, tìm dụng cụ trong 30 giây và phát hiện lỗi máy qua việc vệ sinh.",
        "definition": (
            "5S không phải là 'quét dọn vệ sinh cho sạch đẹp đón khách', mà là hệ thống quản trị trực quan (Visual Management) nhằm tạo trật tự chuẩn hóa sao cho mọi bất thường (rò dầu, thiếu dụng cụ, rulo để sai khu vực, phế liệu lẫn lộn) đập ngay vào mắt trong vòng 3 giây."
        ),
        "formula_or_spec": (
            "• S1 Sàng lọc (Thẻ đỏ Red Tag) → S2 Sắp xếp (Kẻ vạch, Shadow Board) → S3 Sạch sẽ = Kiểm tra (Thẻ Fuguai báo hỏng sớm) → S4 Chuẩn hóa Audit → S5 Kỷ luật duy trì."
        ),
        "cadivi_application": (
            "Tại CADIVI Miền Trung: (1) Shadow Board treo cờ lê/khuôn Chày-Cối ngay sát máy đùn hỗ trợ SMED; (2) Phân vùng sơn sàn rulo Đạt (Xanh) – Chờ QC (Vàng) – Phế/Cách ly (Đỏ); (3) Thùng phân loại phế đồng trần vs đồng dính nhựa theo mã màu; (4) Lau chùi phát hiện sớm rò nhũ tương kéo đồng & bụi bám mắt Laser Gauge."
        ),
        "cadivi_example": (
            "Ví dụ: Dán thẻ đỏ Red Tag dọn 42 rulo hỏng & 18 bộ khuôn mòn cũ quanh khu máy đùn, lập xe đồ nghề 5S có bóng dụng cụ giúp giảm thời gian tìm dụng cụ đổi khuôn từ 8 phút về 0 phút!"
        ),
        "related": ["Lean", "SMED", "TPM", "Genba", "Poka-Yoke"],
        "doc_key": "lean_muda"
    },
    "Kaizen": {
        "term": "Kaizen",
        "full_name": "Kaizen — Cải Tiến Liên Tục Từng Bước Nhỏ Mỗi Ngày (Kai = Thay đổi, Zen = Tốt hơn)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Kaizen", "Kaikaku", "Teian"],
        "case_sensitive": [],
        "short_desc": "Văn hóa cải tiến liên tục chi phí thấp huy động toàn bộ công nhân & kỹ sư tại xưởng xóa bỏ từng lãng phí nhỏ mỗi ngày.",
        "definition": (
            "Kaizen là triết lý cải tiến nhỏ, liên tục, chi phí thấp (thậm chí 0 đồng) với sự tham gia của tất cả mọi người từ Giám đốc đến công nhân đứng máy. "
            "Phân biệt: Kaizen (cải tiến nhỏ liên tục), Kaikaku (đột phá nhanh trong 3–5 ngày Kaizen Blitz như chuyển đổi SMED) và Kakushin (đổi mới công nghệ/đầu tư lớn)."
        ),
        "formula_or_spec": (
            "• Hệ thống Teian Kaizen hiệu quả: Phiếu A5 đơn giản 3 ô (Vấn đề – Ý tưởng – Lợi ích) + Phản hồi trong 48 giờ + Thưởng nóng tức thì + Vinh danh hàng tuần."
        ),
        "cadivi_application": (
            "Xây dựng phong trào cải tiến tại CADIVI Miền Trung bắt đầu từ các Quick-Win giúp giảm mệt mỏi cho thợ đứng máy kéo/bện/đùn và tổ chức các sự kiện Kaizen Blitz 5 ngày giải quyết dứt điểm từng nút thắt OEE."
        ),
        "cadivi_example": (
            "Ví dụ: Một thợ đóng cuộn đề xuất gắn thêm con lăn dẫn hướng & bàn nâng cơ khí để không phải cúi nhấc cuộn dây 15 kg từ sàn lên máy co màng — chi phí chế tạo 800,000đ nhưng tăng tốc độ đóng gói +12% và hết đau lưng."
        ),
        "related": ["Lean", "5S", "PDCA", "A3", "Genba"],
        "doc_key": "lean_muda"
    },
    "Poka-Yoke": {
        "term": "Poka-Yoke",
        "full_name": "Poka-Yoke — Cơ Chế Chống Sai Lỗi Tự Động (Mistake-Proofing)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Poka-Yoke", "Poka Yoke"],
        "case_sensitive": [],
        "short_desc": "Thiết kế cơ khí hoặc cảm biến/phần mềm ngăn không cho con người thao tác nhầm hoặc dừng máy tức thì ngay khi phát sinh lỗi.",
        "definition": (
            "Poka-Yoke là giải pháp kỹ thuật loại bỏ sự phụ thuộc vào trí nhớ hay sự cẩn thận chủ quan của con người (vì con người mệt mỏi ca đêm chắc chắn sẽ có lúc nhầm). "
            "Có 2 cấp độ: Cảnh báo (Warning — đèn/còi báo) và Kiểm soát/Ngắt mạch (Control — khóa máy không cho chạy tiếp nếu sai, hiệu quả nhất)."
        ),
        "formula_or_spec": (
            "• Quy luật chi phí lỗi 1 – 10 – 100: Chặn lỗi tại nguồn bằng Poka-Yoke tốn 1 đồng; phát hiện ở trạm sau tốn 10 đồng; lọt ra khách hàng tốn 100 đồng!"
        ),
        "cadivi_application": (
            "5 Poka-Yoke ứng dụng cực mạnh tại CADIVI Miền Trung:\n"
            "1. Cảm biến đứt sợi ngắt PLC máy bện trong 0.5s (chống ruột dẫn thiếu sợi).\n"
            "2. Quét Barcode rulo xác thực đúng tiết diện đồng/nhựa trước khi mở khóa máy.\n"
            "3. Khóa liên động cửa lồng máy bện (an toàn tuyệt đối).\n"
            "4. Spark Tester liên động phun mực màu đánh dấu tọa độ lỗi thủng cách điện.\n"
            "5. Giá cắm khuôn Chày-Cối mã màu + rãnh định hình chống lấy nhầm size."
        ),
        "cadivi_example": (
            "Ví dụ: Gắn công tắc liên động nhiệt độ tủ sấy Hopper Dryer với nút chạy máy đùn — nếu hạt PVC chưa sấy đủ 75°C trong 45 phút, máy đùn báo vàng không cho chạy, triệt tiêu 100% lỗi bọt khí Spark do quên bật sấy ca đêm!"
        ),
        "related": ["Jidoka", "Andon", "Spark Tester", "Barcode", "PLC", "Lean"],
        "doc_key": "lean_muda"
    },
    "Jidoka": {
        "term": "Jidoka",
        "full_name": "Jidoka — Tự Động Hóa Có Trí Tuệ Con Người (Autonomation / Dừng Ngay Khi Có Lỗi)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Jidoka"],
        "case_sensitive": [],
        "short_desc": "Trụ cột chất lượng của Toyota TPS: máy móc tự phát hiện bất thường và TỰ ĐỘNG DỪNG để không sản xuất hàng loạt phế phẩm.",
        "definition": (
            "Jidoka kết hợp giữa tự động hóa và trí tuệ phát hiện lỗi: tách con người khỏi việc đứng canh máy thụ động (giúp 1 người đứng nhiều máy) bằng cách trang bị cảm biến để máy tự dừng và bật đèn Andon ngay khi phát hiện đứt sợi, quá nhiệt hay sai đường kính."
        ),
        "formula_or_spec": (
            "• Tam giác chất lượng TPS: Poka-Yoke (Phát hiện) → Jidoka (Tự dừng ngay, không truyền lỗi) → Andon (Gọi hỗ trợ xử lý gốc rễ)."
        ),
        "cadivi_application": (
            "Cốt lõi của các dây chuyền chạy tốc độ cao (300–800 m/phút) tại CADIVI: chỉ cần chậm dừng 1 phút khi bị lệch tâm hoặc thủng Spark là hỏng ngay 500 mét đồng bọc nhựa!"
        ),
        "cadivi_example": (
            "Ví dụ: Cài đặt liên động Jidoka giữa Laser Gauge và PLC máy đùn — nếu đường kính ngoài vượt quá dung sai ±0.08 mm liên tục quá 3 giây, máy tự động chuyển sang chế độ giảm tốc báo động Andon đỏ thay vì chạy tiếp tạo ra cả rulo phế phẩm."
        ),
        "related": ["Poka-Yoke", "Andon", "Laser Gauge", "Spark Tester", "Man-Machine Chart"],
        "doc_key": "lean_muda"
    },
    "Andon": {
        "term": "Andon",
        "full_name": "Andon — Hệ Thống Đèn Tháp, Âm Thanh & Bảng Cảnh Báo Trực Quan Sự Cố Hiện Trường",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Andon"],
        "case_sensitive": [],
        "short_desc": "Hệ thống truyền thông tức thời tại xưởng (đèn Xanh/Vàng/Đỏ + màn hình TV) báo ngay máy nào đang gặp sự cố cần hỗ trợ.",
        "definition": (
            "Andon là công cụ quản trị trực quan giúp bất kỳ ai bước vào phân xưởng cũng biết ngay trong 3 giây dây chuyền nào đang chạy bình thường (Xanh), sắp hết vật tư/đổi mã (Vàng) hay đang dừng sự cố/lỗi chất lượng (Đỏ) cần Quản đốc và Bảo trì ứng cứu ngay."
        ),
        "formula_or_spec": (
            "• Quy ước màu chuẩn: Xanh (Đang chạy đạt chuẩn) | Vàng (Cần hỗ trợ/Cấp rulo/Đổi mã) | Đỏ (Dừng sự cố/Lỗi chất lượng) | Trắng (Đang bảo trì/Chờ kế hoạch)."
        ),
        "cadivi_application": (
            "Lắp đèn tháp 3 màu nối PLC trên các máy kéo thô RBD, máy bện và máy đùn lớn ở CADIVI Miền Trung; kết hợp TV Andon hiển thị tốc độ m/phút hiện tại so với Target của từng dây chuyền."
        ),
        "cadivi_example": (
            "Ví dụ: Khi rulo đồng cấp đầu vào còn dưới 10 phút chạy, đèn Andon máy đùn chuyển Vàng báo tài xế xe nâng (Water Spider) chở rulo mới tới sát máy trước khi hết dây — xóa 100% thời gian dừng máy chờ xe nâng."
        ),
        "related": ["Jidoka", "Poka-Yoke", "Water Spider", "MES", "OEE"],
        "doc_key": "erp_mes"
    },
    "Kanban": {
        "term": "Kanban",
        "full_name": "Kanban / Pull System — Hệ Thống Kéo Điều Tiết Vật Tư & Bán Thành Phẩm Bằng Tín Hiệu Trực Quan",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Kanban", "CONWIP", "Supermarket"],
        "case_sensitive": ["CONWIP"],
        "short_desc": "Cơ chế 'công đoạn sau dùng đến đâu, công đoạn trước mới sản xuất bù đến đó' thông qua thẻ rút hoặc giới hạn ô sàn rulo.",
        "definition": (
            "Kanban (tiếng Nhật: 'thẻ tín hiệu') là trái tim của hệ thống Kéo (Pull System) và Just-In-Time. "
            "Thay vì đẩy hàng ồ ạt theo kế hoạch dự báo gây ùn tắc WIP, mỗi ô siêu thị đệm (Supermarket) có giới hạn Min/Max cố định — khi đầy thì máy trước DỪNG, khi xuống mức Min thì phát tín hiệu sản xuất bù đúng số lượng."
        ),
        "formula_or_spec": (
            "• Số thẻ Kanban = [ Nhu cầu trung bình/ngày × Lead Time bổ sung × (1 + Hệ số an toàn) ] / Sức chứa 1 rulo/thùng."
        ),
        "cadivi_application": (
            "Chấm dứt nghịch lý 'sàn chất đầy rulo nhưng máy đùn vẫn thiếu đúng mã cần chạy' tại CADIVI bằng Siêu thị Rulo WIP có vạch giới hạn (CONWIP) giữa Kéo → Bện → Đùn và Kanban 2 thùng cho kho vật tư phụ (tem, màng co, mực in, lưới lọc)."
        ),
        "cadivi_example": (
            "Ví dụ: Kẻ đúng 6 ô sơn sàn siêu thị rulo ruột 2.5mm² giữa máy kéo và máy đùn. Khi đủ 6 rulo, máy kéo chuyển mã khác không kéo thừa; khi máy đùn lấy đi rulo thứ 3, thẻ Kanban báo máy kéo chạy bù đúng 3 rulo."
        ),
        "related": ["Two-Bin Kanban", "WIP", "VSM", "Heijunka", "Water Spider", "Lean"],
        "doc_key": "lean_muda"
    },
    "Two-Bin Kanban": {
        "term": "Two-Bin Kanban",
        "full_name": "Two-Bin Kanban — Hệ Thống Cấp Vật Tư Tiêu Hao Hai Thùng Tự Động",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Two-Bin Kanban", "Two-bin Kanban", "Kanban hai thùng", "Kanban 2 thùng"],
        "case_sensitive": [],
        "short_desc": "Đặt 2 thùng vật tư (Thùng A đang dùng + Thùng B dự phòng); hết thùng A đặt vỏ trống làm tín hiệu kho cấp bù đúng định mức.",
        "definition": (
            "Mô hình quản lý vật tư nhóm C cực kỳ đơn giản nhưng hiệu quả 100%: mỗi trạm có 2 khay giống nhau, khi khay 1 hết thì kéo khay 2 lên dùng ngay mà không gián đoạn sản xuất, đồng thời vỏ khay 1 trở thành thẻ Kanban để người cấp vật tư bổ sung đầy lại."
        ),
        "formula_or_spec": (
            "• Sức chứa mỗi thùng = Nhu cầu tiêu thụ trong thời gian bổ sung từ kho × (1 + 20% dự phòng)."
        ),
        "cadivi_application": (
            "Áp dụng tại CADIVI cho các vật tư tiêu hao hay gây dừng vặt: lưới lọc đầu đùn (Screen Pack), cuộn màng co nhiệt, dây rút nhựa, tem nhãn chống hàng giả, ống nối đồng, bao bì carton."
        ),
        "cadivi_example": (
            "Ví dụ: Đặt 2 khay lưới lọc Screen Pack 60-mesh ngay cạnh máy đùn số 2. Hết khay 1, thợ đẩy khay rỗng ra vạch vàng → nhân viên kho đi tuần mỗi 2 giờ nhìn thấy tự cấp bù, công nhân không phải bỏ máy đi bộ 100m xin phiếu kho!"
        ),
        "related": ["Kanban", "Water Spider", "Kitting", "BOM"],
        "doc_key": "bom_cost"
    },
    "Heijunka": {
        "term": "Heijunka",
        "full_name": "Heijunka — San Phẳng Kế Hoạch & Cơ Cấu Sản Xuất (Production Leveling)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Heijunka", "Product Wheel"],
        "case_sensitive": [],
        "short_desc": "San đều khối lượng và nhịp độ sản xuất theo chu kỳ đều đặn (Bánh xe sản xuất) để xóa quá tải cuối tháng (Muri) và giảm đổi mã.",
        "definition": (
            "Heijunka triệt tiêu tình trạng đầu tháng rảnh rỗi cuối tháng tăng ca dồn dập (gây hỏng máy, mệt mỏi, lỗi chất lượng cao) bằng cách chia đều sản lượng và sắp xếp các họ sản phẩm chạy theo một chu kỳ lặp lại cố định (Product Wheel / Campaign Scheduling)."
        ),
        "formula_or_spec": (
            "• 3M của Toyota: Muda (Lãng phí) – Mura (Biến động thất thường) – Muri (Quá tải ép buộc). Heijunka tấn công trực tiếp vào Mura và Muri!"
        ),
        "cadivi_application": (
            "Tại CADIVI Miền Trung, kết hợp Heijunka + Bánh xe sản xuất (Product Wheel) cho nhóm dây dân dụng chạy tuần hoàn theo chuỗi tiết diện & chuỗi màu Sáng → Tối mỗi tuần giúp giảm 50% số lần đổi mã máy đùn."
        ),
        "cadivi_example": (
            "Ví dụ: Cố định bánh xe máy đùn số 1: Thứ 2–3 chạy VC 1.5 & 2.5 (Trắng→Vàng→Đỏ→Xanh→Đen); Thứ 4–5 chạy VC 4.0 & 6.0; Thứ 6 chạy các đơn đặc biệt → Năng lực thực tế tăng +18% không cần tăng ca!"
        ),
        "related": ["Color Sequencing", "SMED", "Kanban", "RCCP", "Lean"],
        "doc_key": "lean_muda"
    },
    "WIP": {
        "term": "WIP",
        "full_name": "Work-In-Process — Tồn Kho Bán Thành Phẩm Đang Dở Dang Trên Xưởng",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["WIP", "Work-In-Process"],
        "case_sensitive": ["WIP"],
        "short_desc": "Toàn bộ rulo sợi kéo, rulo ruột bện, lõi cách điện đang nằm chờ trên sàn xưởng giữa các công đoạn chưa thành thành phẩm.",
        "definition": (
            "WIP là lượng bán thành phẩm đang nằm dở dang trên chuyền. Theo định luật Little, WIP càng phình to thì Lead Time càng kéo dài, chôn vốn lưu động (đặc biệt đồng có giá rất cao!), chiếm mặt bằng, tăng rủi ro oxy hóa/va đập móp rulo và che giấu hàng lỗi."
        ),
        "formula_or_spec": (
            "• Little's Law: WIP = Throughput (Tốc độ xuất xưởng) × Lead Time."
        ),
        "cadivi_application": (
            "Với giá đồng ~250 triệu/tấn, chỉ cần dư 40 tấn rulo bán thành phẩm nằm chờ trên sàn giữa Kéo – Bện – Đùn là nhà máy đang bị chôn chết 10 TỶ ĐỒNG vốn lưu động! OE CADIVI quản trị WIP bằng mức trần CONWIP & FIFO Barcode."
        ),
        "cadivi_example": (
            "Ví dụ: Giảm tồn kho rulo WIP trước khu máy đùn từ 5 ngày tồn xuống 1.5 ngày tồn giúp giải phóng hơn 25 tấn đồng lưu động (~6.2 tỷ VNĐ) và mở rộng thêm 120 m² lối đi an toàn 5S."
        ),
        "related": ["Lead Time", "VSM", "Kanban", "Barcode", "5S"],
        "doc_key": "lean_muda"
    },
    "Genba": {
        "term": "Genba",
        "full_name": "Genba (Gemba) & Nguyên Tắc 3 Thực (Genba – Genbutsu – Genjitsu)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Genba", "Gemba", "Genbutsu", "Genjitsu"],
        "case_sensitive": [],
        "short_desc": "Nguyên tắc cốt lõi của kỹ sư OE: luôn trực tiếp xuống hiện trường sản xuất (Genba), cầm tận tay hiện vật lỗi (Genbutsu) và xem số liệu thật (Genjitsu).",
        "definition": (
            "Genba (tiếng Nhật: 'nơi sự thật diễn ra') là mặt sàn phân xưởng nơi sản phẩm thực sự được tạo ra. "
            "Kỹ sư OE giỏi không bao giờ ngồi phòng máy lạnh đoán nguyên nhân lỗi qua lời kể; họ trực tiếp xuống xưởng quan sát cả ca ngày lẫn ca đêm, cầm mẫu lỗi soi kỹ và đo bằng số liệu khách quan."
        ),
        "formula_or_spec": (
            "• 3 Thực (San-Gen-Shugi): Genba (Hiện trường thật) + Genbutsu (Hiện vật thật) + Genjitsu (Dữ liệu/Thực trạng thật)."
        ),
        "cadivi_application": (
            "Bắt buộc với Chuyên viên OE CADIVI: đi Genba Walk hằng ngày qua 4 phân xưởng Kéo – Bện – Đùn – Đóng gói, cầm trực tiếp đầu sợi đồng đứt/mặt cắt nhựa thủng Spark soi kính hiển vi để chốt đúng nguyên nhân gốc."
        ),
        "cadivi_example": (
            "Ví dụ: Báo cáo giấy ghi máy đùn chạy chậm do 'nhựa khó đùn', nhưng khi OE xuống Genba đứng cạnh máng nước 20 phút đo bằng súng hồng ngoại mới phát hiện nước làm mát nóng 38°C (chứ không phải do hạt nhựa!)."
        ),
        "related": ["5 Whys", "Ishikawa", "Kaizen", "5S", "8D"],
        "doc_key": "lean_muda"
    },
    "Spaghetti": {
        "term": "Spaghetti",
        "full_name": "Spaghetti Diagram — Sơ Đồ Đường Đi Chằng Chịt (Phân Tích Quãng Đường Di Chuyển)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Spaghetti", "Spaghetti Diagram"],
        "case_sensitive": [],
        "short_desc": "Bản vẽ nét liền mô phỏng toàn bộ lộ trình di chuyển của công nhân hoặc xe nâng trên mặt bằng xưởng để triệt tiêu lãng phí đi lại & vận chuyển.",
        "definition": (
            "Spaghetti Diagram ghi lại từng bước di chuyển thực tế của người thao tác hoặc rulo vật tư trên bản vẽ mặt bằng tỷ lệ chuẩn. "
            "Bức vẽ ban đầu thường rối như đĩa mì Ý (Spaghetti), phơi bày những quãng đường đi bộ 4–8 km/ca hoàn toàn vô ích và là bằng chứng trực quan cực mạnh để thuyết phục Ban Giám đốc duyệt cải tiến Layout."
        ),
        "formula_or_spec": (
            "• KPI đo lường Trước–Sau: Tổng quãng đường (mét/ca), Số lượt cắt ngang đường xe nâng (an toàn), Thời gian đi bộ NVA (phút/ca)."
        ),
        "cadivi_application": (
            "Áp dụng vẽ cho (1) công nhân đóng cuộn khoanh 100m, (2) lộ trình xe nâng chở rulo giữa xưởng Kéo – Bện – Đùn – Kho và (3) thao tác di chuyển lấy đồ nghề khi đổi khuôn máy đùn."
        ),
        "cadivi_example": (
            "Ví dụ: Vẽ Spaghetti trên AutoCAD cho thợ đóng cuộn khoanh phát hiện đi bộ 5.8 km/ca. Sắp xếp lại máy + đặt giá cấp thùng/tem tại chỗ (Point-of-Use) rút còn 1.9 km/ca (-67%), năng suất tổ tăng +22%."
        ),
        "related": ["AutoCAD", "OLE", "Ergonomics", "5S", "Lean"],
        "doc_key": "autocad_layout"
    },
    "Shojinka": {
        "term": "Shojinka",
        "full_name": "Shojinka — Tổ Chức Lao Động Linh Hoạt Đa Năng Theo Biến Động Đơn Hàng",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Shojinka"],
        "case_sensitive": [],
        "short_desc": "Khả năng co giãn linh hoạt số lượng công nhân trên chuyền (ví dụ từ 5 người xuống 3 người khi đơn hàng giảm) nhờ đào tạo đa kỹ năng và chuyền chữ U.",
        "definition": (
            "Khi đơn hàng giảm 30%, sai lầm phổ biến là vẫn giữ nguyên số công nhân cho làm chậm lại (làm tăng giá thành nhân công/sản phẩm). "
            "Shojinka bố trí lại phạm vi trạm công việc theo bảng Standard Work cho số nhân sự tối ưu đúng bằng Tổng thời gian thao tác chia Takt Time mới, và điều chuyển người dư sang Kaizen/TPM hoặc xưởng cao điểm."
        ),
        "formula_or_spec": (
            "• Số người cần thiết N = làm tròn lên( Tổng thời gian thao tác / Takt Time mới ).\n"
            "• Điều kiện cần: Ma trận kỹ năng đa năng (Multi-skill Matrix) + Layout chữ U / liên hoàn."
        ),
        "cadivi_application": (
            "Nhu cầu dây dân dụng & cáp dự án tại CADIVI Miền Trung có tính mùa vụ (cao điểm xây dựng vs mùa mưa bão miền Trung) → Shojinka giúp điều phối nhân sự linh hoạt giữa tổ đóng cuộn, tổ bện và hỗ trợ 5S/TPM mà vẫn giữ vững OLE."
        ),
        "cadivi_example": (
            "Ví dụ: Mùa thấp điểm đơn hàng cuộn 100m giảm 30% (Takt Time tăng từ 20s lên 28.5s) → Tổ đóng cuộn co từ 4 người xuống 3 người (vẫn giữ nhịp thao tác chuẩn 25s/cuộn), 1 người dư luân chuyển hỗ trợ máy bện."
        ),
        "related": ["OLE", "TWI", "Takt Time", "Man-Machine Chart", "AutoCAD"],
        "doc_key": "ole"
    },
    "Water Spider": {
        "term": "Water Spider",
        "full_name": "Water Spider (Mizusumashi) — Nhân Viên Tiếp Vật Tư Lưu Động Theo Chu Kỳ Cố Định",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Water Spider", "Mizusumashi"],
        "case_sensitive": [],
        "short_desc": "Người chuyên trách chạy tuyến cố định (Milk-run) cấp rulo, hạt nhựa, tem nhãn, bao bì tận máy để thợ chính không bao giờ phải rời vị trí.",
        "definition": (
            "Thay vì để 10 thợ máy tay nghề cao phải dừng máy tự đi tìm xe nâng, lấy hạt nhựa hay lấy thùng carton (gây mất cả OEE máy lẫn OLE người), "
            "nhà máy bố trí 1 nhân viên Water Spider đi theo tuyến tuần hoàn cố định (mỗi 20–30 phút) để cấp đầy vật tư đầu vào và gom thành phẩm/phế liệu đầu ra."
        ),
        "formula_or_spec": (
            "• Nguyên tắc: Thợ chính tập trung 100% thao tác VA tại máy; Water Spider gom toàn bộ thao tác NNVA vận chuyển."
        ),
        "cadivi_application": (
            "Áp dụng cực hiệu quả tại khu máy đùn (cấp bao hạt nhựa đã sấy, thu hồi vỏ thùng phế, đổi rulo rỗng/đầy) và khu đóng cuộn khoanh 100m tại CADIVI Miền Trung."
        ),
        "cadivi_example": (
            "Ví dụ: Bố trí 1 nhân viên Water Spider phục vụ đồng thời 5 dây chuyền đùn: mỗi 30 phút tuần tra kiểm tra phễu nhựa và rulo dự phòng → Xóa sạch 25 phút/ca/máy dừng chờ vật tư, nâng OEE ngay +5.5%!"
        ),
        "related": ["Kanban", "Two-Bin Kanban", "OLE", "OEE", "Andon"],
        "doc_key": "ole"
    },
    "Ergonomics": {
        "term": "Ergonomics",
        "full_name": "Ergonomics — Công Thái Học & Nhân Trắc Học Thiết Kế Trạm Làm Việc",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Ergonomics", "Golden Zone"],
        "case_sensitive": [],
        "short_desc": "Thiết kế chiều cao bàn, tầm với Golden Zone (≤ 40 cm) và thiết bị trợ lực giúp công nhân không mỏi lưng/cổ tay và duy trì năng suất cuối ca.",
        "definition": (
            "Ergonomics nghiên cứu sự phù hợp giữa cơ thể con người với máy móc/bàn thao tác. Năng suất công nhân thường tụt 15–20% vào 2 giờ cuối ca không phải vì lười, mà vì tích tụ mệt mỏi cơ xương do phải cúi gập lưng, với tay quá xa hay nâng vác nặng."
        ),
        "formula_or_spec": (
            "• Vùng thao tác vàng (Golden Zone): Bán kính với tay ≤ 40 cm, ngang thắt lưng đến giữa ngực, góc cúi lưng < 20°.\n"
            "• Độ cao bàn: Việc chính xác (+5–10cm trên khuỷu) | Việc nhẹ (-5–10cm) | Việc dùng lực/đóng gói nặng (-15–20cm)."
        ),
        "cadivi_application": (
            "Rất thiết thực ở CADIVI tại tổ đóng cuộn khoanh (cuộn dây đồng nặng 5–20 kg — cần bàn nâng thủy lực/con lăn cao ngang thắt lưng), trạm nạp rulo máy bện (xe nâng rulo tự lựa) và phòng Lab cắt mẫu đo kiểm."
        ),
        "cadivi_example": (
            "Ví dụ: Nâng độ cao giá đặt cuộn thành phẩm từ mặt sàn lên bàn con lăn cao 75 cm tại tổ đóng gói CADIVI giúp xóa 400 lần cúi gập lưng/người/ca, giảm tỷ lệ mệt mỏi cuối ca và tăng sản lượng đóng gói +14%."
        ),
        "related": ["OLE", "Time Study", "Spaghetti", "Kaizen"],
        "doc_key": "ole"
    },
    "TWI": {
        "term": "TWI",
        "full_name": "Training Within Industry — Chương Trình Đào Tạo Chuẩn Tại Hiện Trường (JI – JM – JR)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["TWI", "Training Within Industry"],
        "case_sensitive": ["TWI"],
        "short_desc": "Phương pháp đào tạo thực chiến giúp Tổ trưởng huấn luyện công nhân mới nhanh thạo việc (JI), cải tiến thao tác (JM) và dẫn dắt đội ngũ (JR).",
        "definition": (
            "TWI là nền tảng đào tạo hiện trường của Toyota gồm 3 trụ cột: Job Instruction (JI — 4 bước kèm tay chỉ việc chuẩn xác kèm lý do an toàn), "
            "Job Methods (JM — dạy công nhân tự đặt câu hỏi 5W1H cải tiến thao tác) và Job Relations (JR — kỹ năng quản lý con người không gây xung đột)."
        ),
        "formula_or_spec": (
            "• 4 bước TWI-JI: (1) Chuẩn bị tâm lý người học → (2) Làm mẫu & giải thích Điểm then chốt (Key Points + Lý do) → (3) Cho học viên làm thử & tự nói lại Key Points → (4) Theo dõi kèm cặp."
        ),
        "cadivi_application": (
            "Giúp CADIVI Miền Trung rút ngắn thời gian đào tạo thợ mới đứng máy kéo/bện/đùn từ 2 tháng xuống 3 tuần, giảm chênh lệch tay nghề giữa Ca 1 và Ca 3 và giảm lỗi thao tác làm tụt OLE."
        ),
        "cadivi_example": (
            "Ví dụ: Áp dụng TWI-JI chuẩn hóa bước hàn đối đầu nối đồng rod (Butt Welding) cho 8 thợ mới xưởng kéo → tỷ lệ đứt mối hàn giảm từ 1.2 lần/tấn xuống còn 0.1 lần/tấn chỉ sau 2 tuần!"
        ),
        "related": ["OLE", "Shojinka", "Time Study", "Kaizen"],
        "doc_key": "ole"
    },

    # =================================================================
    # NHÓM 4: SIX SIGMA, SPC, THỐNG KÊ, TOC, TPM, PFMEA & TÀI CHÍNH ROI
    # =================================================================
    "OE": {
        "term": "OE",
        "full_name": "Operational Excellence — Xuất Sắc Vận Hành / Tối Ưu Quy Trình Tổng Thể",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["OE", "Operational Excellence"],
        "case_sensitive": ["OE"],
        "short_desc": "Hệ thống quản trị vận hành đỉnh cao tích hợp IE + Lean + Six Sigma + Dữ liệu/Số hóa + Văn hóa quản trị hàng ngày để tạo hiệu quả bền vững.",
        "definition": (
            "Operational Excellence (OE) là tầng quản trị bao trùm hơn cả Lean hay Six Sigma đơn lẻ. "
            "Mục tiêu của Chuyên viên OE là xây dựng một nhà máy vận hành ổn định, minh bạch bằng dữ liệu (OEE, OLE, BOM, RCCP), "
            "nơi mọi nhân viên đều nhìn thấy dòng chảy giá trị và chủ động khắc phục ngay khi dòng chảy bị đứt gãy."
        ),
        "formula_or_spec": (
            "• Công thức OE = Nền tảng IE (Đo chuẩn) + Lean (Tốc độ dòng chảy & Xóa lãng phí) + Six Sigma (Giảm biến thiên & Lỗi) + Daily Management (Tier 1–2–3 SQDC) + ROI Tài chính."
        ),
        "cadivi_application": (
            "Chính là chức danh tuyển dụng tại Nhà máy CADIVI Miền Trung (CareerViet 35C8613F): đóng vai trò 'bác sĩ vận hành & kiến trúc sư dữ liệu' tối ưu toàn diện Thiết bị (OEE), Nhân lực (OLE), Vật tư (BOM đồng/nhựa) và Chi phí sản xuất."
        ),
        "cadivi_example": (
            "Ví dụ 90 ngày đầu của Chuyên viên OE tại CADIVI: Tháng 1 chuẩn hóa dữ liệu OEE/OLE/BOM tự động → Tháng 2 dẫn dắt Pilot SMED máy đùn & giảm nhựa Over-thickness → Tháng 3 chứng minh ROI bằng t-test và nhân rộng toàn nhà máy."
        ),
        "related": ["Lean", "Six Sigma", "DMAIC", "OEE", "OLE", "TOC", "TPM", "ROI"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "Six Sigma": {
        "term": "Six Sigma",
        "full_name": "Six Sigma — Phương Pháp Luận Quản Trị Chất Lượng Dựa Trên Thống Kê (Giảm Biến Thiên)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Six Sigma"],
        "case_sensitive": [],
        "short_desc": "Phương pháp kỷ luật dựa trên dữ liệu và toán học thống kê để thu hẹp độ biến thiên (σ) của quy trình, kéo tỷ lệ khuyết tật về mức cực thấp (< 3.4 DPMO).",
        "definition": (
            "Nếu Lean tập trung làm quy trình NHANH hơn (xóa lãng phí), thì Six Sigma tập trung làm quy trình CHÍNH XÁC & ỔN ĐỊNH hơn (thu hẹp độ lệch chuẩn σ). "
            "Kết hợp Lean Six Sigma giải quyết đồng thời cả tốc độ (OEE/Lead Time) lẫn độ chính xác chất lượng/chi phí (Cpk, Scrap)."
        ),
        "formula_or_spec": (
            "• Mức 3 Sigma: 66,807 lỗi/triệu (DPMO) | Mức 4 Sigma (Cpk=1.33): 6,210 DPMO (dài hạn) / 63 PPM (ngắn hạn) | Mức 6 Sigma: ≤ 3.4 DPMO (99.99966% đạt chuẩn)."
        ),
        "cadivi_application": (
            "Điểm cộng lớn trong JD CADIVI (chứng chỉ Green Belt): dùng tư duy Six Sigma thu hẹp độ dao động đường kính sợi đồng (xóa Copper Give-away) và độ dao động chiều dày lớp nhựa PVC/XLPE (xóa Over-thickness & lỗi Spark)."
        ),
        "cadivi_example": (
            "Ví dụ: Áp dụng Lean Six Sigma DMAIC trên dây chuyền đùn số 4 thu hẹp độ lệch chuẩn đường kính cách điện từ σ=0.055mm xuống σ=0.020mm, giảm tỷ lệ phế từ 3.8% xuống 0.78% và tiết kiệm >900 triệu/năm."
        ),
        "related": ["DMAIC", "SPC", "Minitab", "Cpk", "2-Sample t-test", "PFMEA"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "DMAIC": {
        "term": "DMAIC",
        "full_name": "Define – Measure – Analyze – Improve – Control (Chu Trình 5 Pha Dự Án Six Sigma)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["DMAIC"],
        "case_sensitive": ["DMAIC"],
        "short_desc": "Lộ trình 5 pha bài bản giải quyết các bài toán chất lượng/hao phí phức tạp không rõ nguyên nhân gốc trong nhà máy.",
        "definition": (
            "DMAIC là quy trình 5 bước chuẩn mực để giải quyết tận gốc các vấn đề mãn tính: "
            "Define (Chốt phạm vi & mục tiêu tài chính VNĐ), Measure (Kiểm chuẩn đo MSA & thu dữ liệu nền), Analyze (Chứng minh thống kê nguyên nhân X gây Y), Improve (Thử nghiệm tối ưu & chạy Pilot), Control (Khóa kết quả bằng Control Plan & SPC)."
        ),
        "formula_or_spec": (
            "• Hàm chuyển đổi lõi của DMAIC: Y = f(X1, X2, ..., Xk) — tìm đúng 2–3 biến đầu vào X sống còn quyết định đầu ra Y."
        ),
        "cadivi_application": (
            "Khung sườn tiêu chuẩn để Chuyên viên OE CADIVI dẫn dắt các dự án lớn kéo dài 2–3 tháng như: Giảm phế phẩm đùn bọc cáp, Giảm tần suất đứt sợi đồng máy kéo tinh, Giảm hao hụt vượt BOM nhựa XLPE."
        ),
        "cadivi_example": (
            "Ví dụ DMAIC giảm phế đùn cáp: D (mục tiêu 3.8%→<1%) → M (Gage R&R=6.2%, Pareto lỗi) → A (ANOVA chứng minh nhiệt vùng 3 + độ ẩm nhựa là gốc rễ) → I (hiệu chuẩn PID + sấy bắt buộc 75°C) → C (2-Sample t-test p=0.000 + Control Plan)."
        ),
        "related": ["Six Sigma", "Minitab", "Gage R&R", "ANOVA", "2-Sample t-test", "PFMEA"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "SPC": {
        "term": "SPC",
        "full_name": "Statistical Process Control — Kiểm Soát Quá Trình Bằng Thống Kê",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["SPC", "Statistical Process Control", "Xbar-R", "I-MR"],
        "case_sensitive": ["SPC"],
        "short_desc": "Dùng biểu đồ kiểm soát (Xbar-R, I-MR, p-chart) phân biệt sai số ngẫu nhiên vs bất thường để ngăn phế phẩm ngay khi đang chạy máy.",
        "definition": (
            "SPC theo dõi liên tục thông số chất lượng ngay trong lúc sản xuất bằng đường giới hạn kiểm soát ±3σ (UCL/LCL) — KHÁC VỚI dung sai bản vẽ (USL/LSL)! "
            "Nhờ đó kỹ sư phát hiện xu hướng mòn khuôn hay trôi nhiệt độ TRƯỚC KHI sản phẩm bị vượt dung sai thành phế phẩm, đồng thời tránh sai lầm chỉnh máy thái quá (Tampering)."
        ),
        "formula_or_spec": (
            "• Dữ liệu liên tục nhóm 2–9 mẫu → Xbar-R | Mẫu đơn n=1 → I-MR | Tỷ lệ lỗi % → p-chart | Số lỗi/km cáp → u-chart.\n"
            "• Giới hạn kiểm soát: UCL = μ + 3σ | LCL = μ - 3σ."
        ),
        "cadivi_application": (
            "Áp dụng trực tiếp tại CADIVI để kiểm soát: (1) Đường kính sợi đồng kéo (phát hiện mòn khuôn PCD kịp thời), (2) Đường kính ngoài & độ dày cách điện từ Laser Gauge, (3) Điện trở ruột dẫn 20°C trong phòng Lab."
        ),
        "cadivi_example": (
            "Ví dụ: Biểu đồ Xbar-R đường kính sợi đồng kéo Ø1.78mm báo 6 điểm liên tiếp tăng dần từ 1.778 lên 1.786mm (vi phạm Nelson Rule 3 dù chưa vượt trần 1.795mm) → OE yêu cầu thay khuôn PCD ngay giờ nghỉ ca, ngăn chặn 2 tấn đồng bị Copper Give-away!"
        ),
        "related": ["Minitab", "Cpk", "Ppk", "Nelson Rules", "Laser Gauge", "Gage R&R"],
        "doc_key": "minitab_spc"
    },
    "Cpk": {
        "term": "Cpk",
        "full_name": "Process Capability Index (Cpk & Cp) — Chỉ Số Năng Lực Quá Trình Ngắn Hạn",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Cpk", "Cp", "Cp/Cpk"],
        "case_sensitive": ["Cpk", "Cp"],
        "short_desc": "Thước đo toán học xem quy trình sản xuất có đủ chính xác và nằm đúng tâm để đáp ứng dung sai kỹ thuật (USL/LSL) hay không (chuẩn ≥ 1.33).",
        "definition": (
            "Cp chỉ đo độ hẹp (tiềm năng ổn định) của máy mà không xét lệch tâm; còn Cpk đo năng lực THỰC TẾ có tính đến mức độ lệch tâm so với cận trên USL và cận dưới LSL. "
            "Nếu Cp cao nhưng Cpk thấp → máy rất tốt, chỉ bị chỉnh lệch tâm (chỉnh offset là đạt chuẩn ngay, không tốn tiền sửa máy!)."
        ),
        "formula_or_spec": (
            "• Cp = (USL - LSL) / (6σ)\n"
            "• Cpk = min[ (USL - μ)/(3σ) , (μ - LSL)/(3σ) ]\n"
            "• Mốc chuẩn: < 1.00 (Không đạt, sinh phế) | 1.00–1.33 (Rủi ro) | ≥ 1.33 (Đạt chuẩn công nghiệp 4σ, <63 PPM) | ≥ 1.67 (World-Class)."
        ),
        "cadivi_application": (
            "Công cụ quyết định để OE CADIVI trả lời câu hỏi: 'Có thể hạ chiều dày nhựa bọc trung bình xuống sát chuẩn TCVN để tiết kiệm tiền mà vẫn an toàn 100% không?' — chỉ được hạ tâm khi Cpk ≥ 1.33!"
        ),
        "cadivi_example": (
            "Ví dụ dây VC 2.5mm² (LSL=3.28mm, USL=3.52mm): Khi σ giảm từ 0.055mm về 0.020mm nhờ Laser Gauge, dù hạ đường kính trung bình μ xuống 3.36mm, Cpk vẫn đạt (3.36-3.28)/(3×0.020) = 1.33 (an toàn tuyệt đối, tiết kiệm 1.1 tấn nhựa/tháng/máy)."
        ),
        "related": ["Ppk", "SPC", "Minitab", "Over-thickness", "Laser Gauge"],
        "doc_key": "minitab_spc"
    },
    "Ppk": {
        "term": "Ppk",
        "full_name": "Process Performance Index (Ppk & Pp) — Chỉ Số Hiệu Suất Quá Trình Dài Hạn",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Ppk", "Pp"],
        "case_sensitive": ["Ppk", "Pp"],
        "short_desc": "Chỉ số đánh giá năng lực tổng thể dài hạn (gồm cả biến động giữa các ca, các lô nguyên liệu và thay đổi nhiệt độ môi trường).",
        "definition": (
            "Khác với Cpk dùng độ lệch chuẩn nội bộ trong từng nhóm nhỏ (Within σ — năng lực ngắn hạn lý tưởng), "
            "Ppk dùng độ lệch chuẩn tổng thể của toàn bộ dữ liệu thu thập (Overall s). Nếu Cpk = 1.60 mà Ppk chỉ = 0.95 → máy móc tốt trong từng ca nhưng bị lệch rất mạnh GIỮA các ca hoặc GIỮA các lô hạt nhựa!"
        ),
        "formula_or_spec": (
            "• Ppk = min[ (USL - μ)/(3 × s_overall) , (μ - LSL)/(3 × s_overall) ]\n"
            "• Chuẩn phê duyệt lô sản xuất mới (PPAP): thường yêu cầu Ppk ≥ 1.67."
        ),
        "cadivi_application": (
            "OE CADIVI so sánh Cpk vs Ppk trên dữ liệu 1 tháng của máy đùn/máy kéo để phát hiện sự khác biệt tay nghề giữa Ca 1 – Ca 2 – Ca 3 hoặc sự không đồng đều giữa các lô hạt nhựa/đồng rod đầu vào."
        ),
        "cadivi_example": (
            "Ví dụ: Đo chiều dày vỏ cáp CXV suốt 30 ngày cho Cpk = 1.48 nhưng Ppk = 1.02 → OE phân tầng theo ca và phát hiện Ca 3 tự ý tăng tốc độ kéo thêm 10% làm mỏng lớp vỏ so với Ca 1!"
        ),
        "related": ["Cpk", "SPC", "Minitab", "ANOVA"],
        "doc_key": "minitab_spc"
    },
    "Gage R&R": {
        "term": "Gage R&R",
        "full_name": "MSA — Gage Repeatability & Reproducibility (Phân Tích Độ Tin Cậy Hệ Thống Đo Lường)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Gage R&R", "%GRR"],
        "case_sensitive": [],
        "short_desc": "Thí nghiệm kiểm chứng xem sai số dữ liệu đến từ bản thân sản phẩm hay do chính dụng cụ đo (Repeatability) và người đo khác nhau (Reproducibility).",
        "definition": (
            "Trước khi tin tưởng vào bất kỳ số liệu SPC/Cpk hay báo cáo cải tiến nào, kỹ sư OE bắt buộc phải kiểm định hệ thống đo bằng MSA Gage R&R (chuẩn: 10 mẫu × 3 người đo × 3 lần lặp). "
            "Nếu %GRR > 30%, dữ liệu đo bị nhiễu nặng và hoàn toàn vô giá trị!"
        ),
        "formula_or_spec": (
            "• Repeatability (Độ lặp lại): 1 người đo nhiều lần cùng 1 mẫu (đánh giá DỤNG CỤ).\n"
            "• Reproducibility (Độ tái lập): Nhiều người đo cùng 1 mẫu (đánh giá NGƯỜI ĐO/SOP).\n"
            "• Tiêu chuẩn: %GRR < 10% (Xuất sắc) | 10–30% (Tạm chấp nhận) | > 30% (HỎNG, phải sửa ngay)."
        ),
        "cadivi_application": (
            "Phát huy thế mạnh nền tảng Phòng Kiểm tra (Mabuchi) của bạn tại Phòng Lab CADIVI: kiểm định Gage R&R cho thước đo chiều dày cách điện, máy chiếu mặt cắt, panme đo sợi đồng và cầu đo điện trở trước khi chạy dự án Six Sigma."
        ),
        "cadivi_example": (
            "Ví dụ: 3 nhân viên QC đo chiều dày cách điện nhựa PVC mềm cho %GRR = 34% (chủ yếu do Reproducibility cao vì người bóp panme mạnh làm lún nhựa mềm, người bóp nhẹ). Chuyển sang đo không tiếp xúc bằng kính hiển vi/máy chiếu kéo %GRR xuống 5.8%!"
        ),
        "related": ["Minitab", "SPC", "DMAIC", "Cpk"],
        "doc_key": "minitab_spc"
    },
    "Nelson Rules": {
        "term": "Nelson Rules",
        "full_name": "Nelson Rules / Western Electric Rules — Các Quy Tắc Cảnh Báo Bất Thường Sớm Trên Biểu Đồ SPC",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Nelson Rules", "Western Electric"],
        "case_sensitive": [],
        "short_desc": "Bộ quy tắc nhận diện tín hiệu sai số đặc biệt (lệch tâm, trôi xu hướng, lẫn 2 nguồn máy) trên biểu đồ Xbar-R trước khi phát sinh phế phẩm.",
        "definition": (
            "Ngay cả khi các điểm đo chưa vượt ra khỏi cận dung sai, các mẫu hình phi ngẫu nhiên trên biểu đồ kiểm soát vẫn báo hiệu quy trình đang mất ổn định. "
            "Nelson Rules quy chuẩn hóa các dấu hiệu này thành quy tắc tự động cảnh báo trên Minitab/MES."
        ),
        "formula_or_spec": (
            "• 4 Quy tắc hay dùng nhất:\n"
            "  - Rule 1: 1 điểm vượt ngoài 3σ (UCL/LCL) → Dừng máy kiểm tra ngay.\n"
            "  - Rule 2: 9 điểm liên tiếp nằm 1 phía đường tâm → Quy trình bị lệch tâm.\n"
            "  - Rule 3: 6 điểm liên tiếp tăng dần hoặc giảm dần → Xu hướng trôi/mòn khuôn.\n"
            "  - Rule 4: 14 điểm dao động răng cưa lên xuống → Lẫn dữ liệu 2 máy/2 công nhân."
        ),
        "cadivi_application": (
            "Cài đặt cảnh báo Nelson Rule 2 & Rule 3 cho dữ liệu đường kính sợi đồng máy kéo (phát hiện mòn khuôn PCD) và đường kính bọc cách điện Laser Gauge (phát hiện trôi nhiệt độ đùn)."
        ),
        "cadivi_example": (
            "Ví dụ: Đường kính vỏ cáp CXV ghi nhận 9 điểm đo liên tiếp đều nằm trên đường tâm +0.04mm (vi phạm Rule 2) → Hệ thống cảnh báo thợ kiểm tra lại áp suất đầu đùn trước khi gây lãng phí nhựa cả ca."
        ),
        "related": ["SPC", "Minitab", "Cpk", "Laser Gauge"],
        "doc_key": "minitab_spc"
    },
    "2-Sample t-test": {
        "term": "2-Sample t-test",
        "full_name": "Two-Sample t-test & Paired t-test — Kiểm Định Giả Thuyết So Sánh 2 Nhóm Trước & Sau Cải Tiến",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["2-Sample t-test", "Paired t-test", "t-test"],
        "case_sensitive": [],
        "short_desc": "Phép kiểm định thống kê chứng minh sự khác biệt trung bình Trước vs Sau cải tiến (p-value < 0.05) là hiệu quả thật chứ không phải ăn may ngẫu nhiên.",
        "definition": (
            "Một chuyên viên OE chuyên nghiệp không bao giờ chỉ trừ hai số trung bình rồi tuyên bố thành công. "
            "2-Sample t-test xét đồng thời cả độ chênh lệch trung bình, độ lệch chuẩn và cỡ mẫu để tính xác suất p-value nhằm kết luận khoa học với độ tin cậy ≥ 95%."
        ),
        "formula_or_spec": (
            "• Giả thuyết H0: μ_trước = μ_sau (không đổi) | H1: μ_sau tốt hơn.\n"
            "• Quy tắc quyết định: p-value < 0.05 → Bác bỏ H0, cải tiến CÓ Ý NGHĨA THỐNG KÊ!"
        ),
        "cadivi_application": (
            "Dùng trực tiếp cho hạng mục trong JD CADIVI: 'Thu thập và phân tích dữ liệu trước và sau cải tiến, đánh giá hiệu quả giải pháp tối ưu' — giúp báo cáo của bạn thuyết phục tuyệt đối Ban Giám đốc."
        ),
        "cadivi_example": (
            "Ví dụ: Sau cải tiến SMED trên máy đùn số 2, lấy 20 lần đổi mã Trước (TB 54.2p, SD 6.1p) và 20 lần Sau (TB 13.4p, SD 2.2p) chạy 2-Sample t-test trên Minitab/Python → p-value = 0.000 (< 0.05) → Chứng minh chắc chắn giảm 40.8 phút/lần đổi mã!"
        ),
        "related": ["ANOVA", "Minitab", "DMAIC", "Six Sigma", "ROI"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "ANOVA": {
        "term": "ANOVA",
        "full_name": "Analysis of Variance — Phân Tích Phương Sai So Sánh Từ 3 Nhóm Trở Lên",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["ANOVA"],
        "case_sensitive": ["ANOVA"],
        "short_desc": "Phép kiểm định thống kê so sánh đồng thời hiệu suất/chất lượng của ≥ 3 nhóm (ví dụ Ca 1 vs Ca 2 vs Ca 3, hoặc 4 máy đùn, 3 nhà cung ứng nhựa).",
        "definition": (
            "Khi cần so sánh từ 3 nhóm trở lên, việc chạy nhiều phép t-test từng cặp sẽ làm phình to sai số thống kê. "
            "ANOVA phân tích tỷ số biến động GIỮA các nhóm trên biến động NỘI BỘ từng nhóm (chỉ số F và p-value) để chỉ đích danh có sự khác biệt thực sự giữa các ca, các máy hay các lô vật tư hay không."
        ),
        "formula_or_spec": (
            "• Nếu p-value < 0.05 → Ít nhất 1 nhóm khác biệt có ý nghĩa; chạy tiếp Tukey Pairwise Comparison trên Minitab để chỉ đích danh nhóm nào kém nhất."
        ),
        "cadivi_application": (
            "So sánh tỷ lệ lỗi Spark giữa 3 nhà cung ứng hạt nhựa PVC; so sánh tốc độ/OEE giữa Ca 1 – Ca 2 – Ca 3; so sánh độ giãn dài sợi đồng giữa 4 máy kéo tinh tại CADIVI."
        ),
        "cadivi_example": (
            "Ví dụ: Chạy One-Way ANOVA so sánh tỷ lệ phế đùn của 3 ca trong 60 ngày cho p = 0.002; biểu đồ Tukey chỉ ra Ca 3 (2.9%) cao hơn hẳn Ca 1 (1.1%) và Ca 2 (1.2%) → OE tập trung đi Genba ca đêm tìm ra lỗi thiếu sấy nhựa."
        ),
        "related": ["2-Sample t-test", "Minitab", "DMAIC", "Ppk"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "TOC": {
        "term": "TOC",
        "full_name": "Theory of Constraints — Lý Thuyết Điểm Nghẽn (Eliyahu Goldratt)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["TOC", "Theory of Constraints"],
        "case_sensitive": ["TOC"],
        "short_desc": "Triết lý tập trung mọi nguồn lực vào ĐÚNG 1 điểm nghẽn (Bottleneck) quyết định sản lượng toàn nhà máy theo 5 bước và cơ chế Drum-Buffer-Rope.",
        "definition": (
            "TOC chỉ ra rằng sức mạnh của cả một dây chuyền chỉ bằng mắt xích yếu nhất (Bottleneck). "
            "Tiết kiệm 1 giờ ở máy phụ trợ là 'ảo ảnh' (không tạo thêm đồng doanh thu nào), còn mất 1 giờ ở máy điểm nghẽn là MẤT TRẮNG 1 giờ sản lượng của toàn bộ nhà máy!"
        ),
        "formula_or_spec": (
            "• 5 Bước TOC: (1) Identify (Tìm điểm nghẽn) → (2) Exploit (Khai thác tối đa 0 đồng) → (3) Subordinate (Bắt khâu khác phục tùng — Drum-Buffer-Rope) → (4) Elevate (Đầu tư mở rộng) → (5) Repeat (Lặp lại)."
        ),
        "cadivi_application": (
            "Giúp OE CADIVI không sa đà cải tiến dàn trải: tìm đúng nút thắt (thường là dây chuyền Đùn vỏ lớn hoặc Bể xông XLPE), giữ nút thắt chạy xuyên giờ ăn ca, làm SMED trước tiên ở đó và điều tiết tốc độ Kéo/Bện phía trước theo cơ chế Drum-Buffer-Rope."
        ),
        "cadivi_example": (
            "Ví dụ từ bảng RCCP CADIVI: Công đoạn Đùn tải 116.4% (điểm nghẽn), còn Kéo thô chỉ tải 72.3%. Theo TOC, OE dồn 100% dự án SMED & bảo trì phòng ngừa vào máy Đùn thay vì tăng tốc máy Kéo (tránh chất thêm núi WIP)."
        ),
        "related": ["RCCP", "OEE", "SMED", "WIP", "VSM"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "TPM": {
        "term": "TPM",
        "full_name": "Total Productive Maintenance — Bảo Trì Năng Suất Toàn Diện (8 Trụ Cột)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["TPM", "Total Productive Maintenance"],
        "case_sensitive": ["TPM"],
        "short_desc": "Hệ thống bảo trì huy động cả thợ vận hành (tự bảo dưỡng Jishu Hozen) lẫn thợ bảo trì chuyên nghiệp nhằm đạt 0 hỏng máy đột xuất, 0 phế phẩm, 0 tai nạn.",
        "definition": (
            "TPM phá bỏ tư duy cũ 'Tôi vận hành – Anh sửa máy'. Công nhân đứng máy chịu trách nhiệm bảo trì tự quản hàng ngày (lau chùi là kiểm tra, tra dầu, siết ốc, dán thẻ Fuguai), "
            "giải phóng đội Bảo trì chuyên nghiệp tập trung vào Bảo trì phòng ngừa (PM) và Bảo trì dự đoán (PdM) theo cảm biến rung/nhiệt."
        ),
        "formula_or_spec": (
            "• 8 Trụ cột TPM (trên nền 5S): Bảo trì tự quản (AM/Jishu Hozen), Bảo trì kế hoạch (PM), Cải tiến trọng điểm (KK), Bảo trì chất lượng (QM), Quản lý thiết bị mới, Đào tạo, TPM văn phòng, An toàn/Môi trường (SHE)."
        ),
        "cadivi_application": (
            "Sống còn cho các dây chuyền chạy liên tục đắt tiền tại CADIVI như Máy kéo thô RBD, Dây chuyền đùn PVC/XLPE và đặc biệt dây chuyền lưu hóa CCV (dừng hỏng đột xuất 1 lần gây đông cứng nhựa trong nòng mất nửa ngày vệ sinh!)."
        ),
        "cadivi_example": (
            "Ví dụ: Triển khai Checklist Jishu Hozen 5 phút đầu ca cho thợ máy kéo RBD (kiểm tra pH/mức nhũ tương, tiếng ồn bạc đạn, độ mòn puli) + lịch PM thay khuôn theo tấn đồng giúp tăng MTBF từ 70 giờ lên 165 giờ!"
        ),
        "related": ["MTBF", "MTTR", "OEE", "5S", "RBD", "CCV"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "MTBF": {
        "term": "MTBF",
        "full_name": "Mean Time Between Failures — Thời Gian Trung Bình Giữa Hai Lần Hỏng Hóc",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["MTBF"],
        "case_sensitive": ["MTBF"],
        "short_desc": "Chỉ số đo ĐỘ TIN CẬY của thiết bị trong TPM (MTBF càng CAO thì máy chạy càng bền bỉ, ít dừng sự cố đột xuất).",
        "definition": (
            "MTBF đo khoảng thời gian vận hành trung bình trước khi máy gặp sự cố hỏng hóc phải dừng sản xuất. "
            "MTBF tăng chứng tỏ công tác bảo trì phòng ngừa (PM), bảo trì tự quản và chất lượng sửa chữa đang đi đúng hướng."
        ),
        "formula_or_spec": (
            "• MTBF (giờ) = Tổng thời gian máy vận hành thực tế / Tổng số lần dừng hỏng đột xuất."
        ),
        "cadivi_application": (
            "Theo dõi riêng MTBF cho từng máy chủ lực tại CADIVI (máy kéo RBD, máy bện Rigid, máy đùn lớn) để biết máy nào 'hay đổ bệnh mãn tính' cần đại tu hoặc thay phụ tùng chuẩn."
        ),
        "cadivi_example": (
            "Ví dụ: Máy đùn số 2 tháng 10 chạy 420 giờ, hỏng đột xuất 6 lần → MTBF = 70 giờ. Sau khi thay vòng bi hộp số & siết lịch vệ sinh lọc dầu, tháng 11 chạy 440 giờ chỉ hỏng 2 lần → MTBF tăng lên 220 giờ (+214%!)."
        ),
        "related": ["MTTR", "TPM", "OEE"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "MTTR": {
        "term": "MTTR",
        "full_name": "Mean Time To Repair — Thời Gian Trung Bình Để Sửa Chữa Phục Hồi Máy",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["MTTR"],
        "case_sensitive": ["MTTR"],
        "short_desc": "Chỉ số đo TỐC ĐỘ PHỤC HỒI của đội bảo trì khi máy gặp sự cố (MTTR càng THẤP thì tổn thất Availability của OEE càng nhỏ).",
        "definition": (
            "MTTR đo tổng thời gian trung bình từ lúc máy báo hỏng cho đến khi bảo trì chẩn đoán, lấy phụ tùng, thay thế, chạy thử xong và bàn giao lại cho sản xuất. "
            "Giảm MTTR đòi hỏi quản lý tốt kho phụ tùng chiến lược (Spare Parts) và tài liệu xử lý lỗi nhanh."
        ),
        "formula_or_spec": (
            "• MTTR (giờ) = Tổng thời gian dừng sửa chữa sự cố / Tổng số lần dừng hỏng đột xuất."
        ),
        "cadivi_application": (
            "Tại CADIVI, các lỗi thường gây kéo dài MTTR là chờ mua điện trở gia nhiệt nòng đùn, cảm biến thermocouple, phớt dầu máy kéo hoặc biến tần → OE phân tích Pareto lỗi hỏng để thiết lập tồn kho an toàn phụ tùng chiến lược."
        ),
        "cadivi_example": (
            "Ví dụ: Trước đây cháy vòng gia nhiệt đầu đùn mất 3.5 giờ sửa do chờ tìm hàng; sau khi đặt tủ phụ tùng dự phòng Min/Max sẵn tại xưởng và SOP tháo lắp nhanh, MTTR giảm xuống còn 45 phút!"
        ),
        "related": ["MTBF", "TPM", "OEE"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "PFMEA": {
        "term": "PFMEA",
        "full_name": "Process Failure Mode and Effects Analysis — Phân Tích Sai Lỗi & Tác Động Quá Trình",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["PFMEA", "FMEA", "RPN"],
        "case_sensitive": ["PFMEA", "FMEA", "RPN"],
        "short_desc": "Công cụ phòng ngừa rủi ro theo từng bước sản xuất bằng cách chấm điểm Mức độ nghiêm trọng (S), Tần suất (O), Khả năng phát hiện (D) → RPN = S×O×D.",
        "definition": (
            "PFMEA là phương pháp rà soát chủ động mọi dạng sai lỗi có thể xảy ra ở từng công đoạn TRƯỚC KHI lỗi bùng phát thành phế phẩm hàng loạt. "
            "Theo chuẩn AIAG-VDA mới, ngoài tổng điểm RPN, mọi hạng mục có Severity ≥ 9 (nguy cơ mất an toàn điện/cháy nổ) BẮT BUỘC ưu tiên hành động cao nhất bất kể RPN cao hay thấp."
        ),
        "formula_or_spec": (
            "• RPN = Severity (S: 1–10) × Occurrence (O: 1–10) × Detection (D: 1–10)\n"
            "• Nguyên tắc giảm rủi ro: Khó giảm S → tập trung giảm O (phòng ngừa nguyên nhân) và giảm D (tăng cảm biến Poka-Yoke/kiểm tra trực tuyến)."
        ),
        "cadivi_application": (
            "Lập bảng PFMEA cho các dây chuyền trọng yếu tại CADIVI (như đùn cách điện cáp trung thế/chậm cháy, ủ đồng, ghép lõi) để chủ động khóa rủi ro lệch tâm, bọt khí, đứt sợi hay sai điện trở."
        ),
        "cadivi_example": (
            "Ví dụ PFMEA công đoạn đùn XLPE: Lỗi 'Cách điện lệch tâm quá mỏng' có S=9 (nguy cơ phóng điện chập cháy), O=4, D=5 (chỉ đo mẫu cuối cuộn) → RPN=180. "
            "Giải pháp: Lắp Laser Eccentricity Gauge trực tuyến kéo D từ 5 xuống 2 → RPN giảm còn 72!"
        ),
        "related": ["Six Sigma", "DMAIC", "Laser Gauge", "Spark Tester", "Poka-Yoke"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "RCCP": {
        "term": "RCCP",
        "full_name": "Rough-Cut Capacity Planning — Hoạch Định Năng Lực Sản Xuất Thô",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["RCCP", "Capacity Planning"],
        "case_sensitive": ["RCCP"],
        "short_desc": "Bài toán đối chiếu Nhu cầu giờ máy của đơn hàng với Năng lực khả dụng thực tế (đã nhân OEE lịch sử) ở từng phân xưởng để dự báo quá tải.",
        "definition": (
            "RCCP trả lời câu hỏi chiến lược của Ban Giám đốc: 'Với đơn hàng tháng tới, nhà máy có đủ công suất làm kịp không và công đoạn nào sẽ bị nghẽn?'. "
            "Sai lầm chết người khi tính năng lực là nhân với 100% công suất thiết kế — OE chuẩn PHẢI nhân với OEE thực tế lịch sử!"
        ),
        "formula_or_spec": (
            "• Giờ khả dụng thực tế = Số máy × Số ca × Giờ kế hoạch/ca × Số ngày × OEE lịch sử\n"
            "• Tỷ lệ tải (Load %) = (Giờ máy yêu cầu của đơn hàng / Giờ khả dụng thực tế) × 100%\n"
            "• Ngưỡng cảnh báo: Load > 85–90% bắt đầu rủi ro trễ giao hàng."
        ),
        "cadivi_application": (
            "Trực tiếp đáp ứng gạch đầu dòng #1 trong JD CADIVI ('phân tích năng lực, năng suất sản xuất'): quy đổi kế hoạch tấn đồng/km cáp sang nhu cầu giờ máy ở đủ 5 khâu Kéo thô – Kéo tinh – Bện – Đùn lõi – Ghép lõi/Đùn vỏ."
        ),
        "cadivi_example": (
            "Ví dụ đơn hàng 300 tấn cáp tháng tới: RCCP chỉ ra Kéo thô tải 72.3%, Bện 86.9%, nhưng Đùn cách điện tải 116.4% (thiếu 166 giờ máy) → OE tham mưu chỉ mở tăng cường ca 3 + chạy SMED cho đúng nhóm máy Đùn, không tăng ca tràn lan cả xưởng."
        ),
        "related": ["OEE", "TOC", "TEEP", "Heijunka", "ERP"],
        "doc_key": "cable_cost_capacity"
    },
    "CAPEX": {
        "term": "CAPEX",
        "full_name": "Capital Expenditure — Chi Phí Đầu Tư Tài Sản Cố Định / Mua Sắm Thiết Bị Mới",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["CAPEX", "OPEX"],
        "case_sensitive": ["CAPEX", "OPEX"],
        "short_desc": "Vốn đầu tư dài hạn mua máy móc, thiết bị đo tự động hoặc nâng cấp dây chuyền (khác với OPEX là chi phí vận hành/bảo trì thường xuyên).",
        "definition": (
            "CAPEX là các khoản đầu tư tài sản lớn cần Ban Giám đốc phê duyệt dựa trên hiệu quả hoàn vốn (ROI, Payback Period, TEEP). "
            "Chuyên viên OE giỏi luôn biết 2 việc: (1) Tránh CAPEX lãng phí khi có thể tăng năng lực bằng Lean/SMED/TEEP, và (2) Lập hồ sơ thẩm định CAPEX sắc bén khi đầu tư thực sự mang lại hoàn vốn nhanh."
        ),
        "formula_or_spec": (
            "• Total CAPEX = Giá thiết bị + Vận chuyển/Thuế + Lắp đặt/Đồ gá + Đào tạo.\n"
            "• Nguyên tắc: Luôn tách rạch ròi Hard Savings (tiền tươi kế toán duyệt) khỏi Soft Savings."
        ),
        "cadivi_application": (
            "Kết nối trực tiếp kinh nghiệm thẩm định đầu tư máy đo tại Mabuchi của bạn sang CADIVI khi đề xuất mua cảm biến Laser Gauge, đầu đùn tự định tâm, bộ Dual Take-up hay thiết bị phòng Lab."
        ),
        "cadivi_example": (
            "Ví dụ: Đề xuất đầu tư 960 triệu lắp 2 bộ Laser Gauge Closed-loop (OPEX 3 triệu/tháng), tạo Hard Savings 96.8 triệu/tháng tiền nhựa & phế đồng → Tiết kiệm ròng 93.8 triệu/tháng → Hoàn vốn chỉ 10.2 tháng!"
        ),
        "related": ["ROI", "Payback", "TEEP", "Laser Gauge"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "ROI": {
        "term": "ROI",
        "full_name": "Return on Investment — Tỷ Suất Hoàn Vốn / Hiệu Quả Kinh Tế Dự Án Cải Tiến",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["ROI", "Return on Investment"],
        "case_sensitive": ["ROI"],
        "short_desc": "Thước đo tài chính quy đổi mọi kết quả kỹ thuật (giảm phút đổi mã, giảm % phế nhựa/đồng) thành số tiền lợi nhuận thực sự thu về trên vốn bỏ ra.",
        "definition": (
            "Ngôn ngữ của kỹ sư là giây/mét/%, còn ngôn ngữ của Ban Giám đốc là ĐỒNG TIỀN (VNĐ). "
            "ROI dịch toàn bộ nỗ lực cải tiến OE sang tỷ suất sinh lời tài chính minh bạch, có xác nhận chéo với phòng Kế toán để chứng minh giá trị dự án."
        ),
        "formula_or_spec": (
            "• ROI (%) = [ (Lợi ích ròng thu được - Tổng chi phí đầu tư) / Tổng chi phí đầu tư ] × 100%."
        ),
        "cadivi_application": (
            "Đáp ứng trực tiếp yêu cầu JD CADIVI ('đánh giá hiệu quả của các giải pháp tối ưu'): mỗi dự án SMED, giảm Over-thickness hay cải tiến đồ gá đều phải chốt bằng bảng tính ROI có kiểm chứng Trước–Sau."
        ),
        "cadivi_example": (
            "Ví dụ: Dự án SMED máy đùn tốn 45 triệu chế tạo tủ sấy đầu khuôn + xe đồ nghề 5S, nhưng giảm 19 kg nhựa purge/lần × 60 lần/tháng × 30,000đ = tiết kiệm 34.2 triệu/tháng → Năm đầu mang lại ROI trên 800%!"
        ),
        "related": ["Payback", "CAPEX", "2-Sample t-test", "A3"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "Payback": {
        "term": "Payback",
        "full_name": "Payback Period — Thời Gian Hoàn Vốn Đầu Tư",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["Payback", "Payback Period", "hoàn vốn"],
        "case_sensitive": [],
        "short_desc": "Số tháng (hoặc năm) cần thiết để dòng tiền tiết kiệm ròng thu hồi đủ 100% số vốn đầu tư ban đầu.",
        "definition": (
            "Payback Period là chỉ số tài chính trực quan nhất mà Giám đốc nhà máy luôn hỏi đầu tiên khi xem đề xuất đầu tư thiết bị cải tiến. "
            "Tại hầu hết nhà máy sản xuất ở Việt Nam, dự án cải tiến có Payback dưới 12–18 tháng thường rất dễ được phê duyệt."
        ),
        "formula_or_spec": (
            "• Payback Period (tháng) = Tổng Vốn Đầu Tư (CAPEX) / Tiết Kiệm Ròng Hàng Tháng (Net Hard Savings).\n"
            "• Luôn tính kèm 3 kịch bản độ nhạy (Thận trọng 70% – Cơ sở 100% – Tích cực 120%)."
        ),
        "cadivi_application": (
            "Trình bày hồ sơ đầu tư nâng cấp thiết bị tại CADIVI Miền Trung một cách thận trọng, minh bạch, có ký xác nhận đơn giá với Kế toán và sản lượng với phòng Kế hoạch."
        ),
        "cadivi_example": (
            "Ví dụ: Đầu tư 960 triệu cho hệ thống đo Laser Closed-loop với tiết kiệm ròng cơ sở 93.8 triệu/tháng → Payback = 10.23 tháng (ngay cả kịch bản thận trọng đạt 70% mục tiêu cũng chỉ hoàn vốn 14.6 tháng!)."
        ),
        "related": ["ROI", "CAPEX", "TEEP"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "Pareto": {
        "term": "Pareto",
        "full_name": "Pareto Chart (Quy Tắc 80/20) — Biểu Đồ Ưu Tiên Xử Lý Nguyên Nhân Cốt Lõi",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Pareto", "Pareto Chart", "80/20"],
        "case_sensitive": [],
        "short_desc": "Biểu đồ cột xếp giảm dần kèm đường cong tích lũy % giúp chỉ đích danh ~20% nguyên nhân gây ra ~80% tổn thất dừng máy hoặc phế phẩm.",
        "definition": (
            "Dựa trên nguyên lý Vilfredo Pareto (80/20), biểu đồ Pareto giúp Chuyên viên OE tập trung nguồn lực hữu hạn vào 2–3 'thủ phạm lớn nhất' (Vital Few) thay vì dàn trải xử lý hàng chục lỗi lặt vặt (Trivial Many)."
        ),
        "formula_or_spec": (
            "• Cột trái: Tần suất hoặc Giá trị thiệt hại (phút dừng / triệu đồng) xếp từ CAO xuống THẤP.\n"
            "• Đường cong phải: % Tích lũy (0% → 100%); cắt mốc 80% để chốt danh sách ưu tiên xử lý."
        ),
        "cadivi_application": (
            "Công cụ số 1 trong báo cáo tháng OE tại CADIVI: vẽ Pareto theo (1) Phút dừng máy từng phân xưởng, (2) Tiền chênh lệch BOM theo mã NVL (đồng/PVC/XLPE), (3) Phân loại nguyên nhân lỗi Spark/đứt sợi."
        ),
        "cadivi_example": (
            "Ví dụ Pareto 1,800 phút dừng máy đùn trong tháng: Top 3 gồm Đổi màu/Purge (35%) + Thay Chày-Cối chỉnh tâm (25%) + Thay rulo (20%) đã chiếm đúng 80% tổng thời gian dừng máy → Tập trung giải quyết đúng 3 mục này!"
        ),
        "related": ["Ishikawa", "5 Whys", "OEE", "BOM", "Power BI"],
        "doc_key": "excel_mfg"
    },
    "Ishikawa": {
        "term": "Ishikawa",
        "full_name": "Ishikawa Diagram (Fishbone / Biểu Đồ Xương Cá 4M1E) — Phân Tích Nguyên Nhân & Hệ Quả",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Ishikawa", "Fishbone", "Xương cá"],
        "case_sensitive": [],
        "short_desc": "Công cụ động não có hệ thống phân loại mọi nguyên nhân tiềm ẩn gây lỗi theo 6 nhánh: Man – Machine – Material – Method – Measurement – Environment.",
        "definition": (
            "Biểu đồ Xương cá giúp nhóm liên phòng ban (Sản xuất, Kỹ thuật, Bảo trì, QC, OE) không bỏ sót nguyên nhân tiềm ẩn khi điều tra sự cố phức tạp. "
            "Sau khi liệt kê đầy đủ trên các nhánh xương cá, đội OE sẽ dùng dữ liệu thực tế & 5 Whys để loại trừ và xác minh đúng nguyên nhân gốc."
        ),
        "formula_or_spec": (
            "• 6 nhánh 5M1E: Man (Con người), Machine (Máy/Khuôn), Material (Đồng/Nhựa), Method (SOP/Nhiệt độ/Tốc độ), Measurement (Thiết bị đo), Mother Nature/Environment (Nhiệt độ/Độ ẩm xưởng)."
        ),
        "cadivi_application": (
            "Họp phân tích nguyên nhân gốc tại CADIVI cho các bài toán đa biến như: 'Đứt sợi đồng lặp lại trên máy kéo RBD', 'Lỗi thủng Spark tăng đột biến ca đêm', hoặc 'Bề mặt vỏ cáp bị sần'."
        ),
        "cadivi_example": (
            "Ví dụ Xương cá lỗi 'Đứt sợi máy kéo': Material (tạp chất oxit đồng rod, lỗi mối hàn) | Machine (mòn khuôn PCD, rãnh puli) | Method (sai drafting ratio, nồng độ nhũ tương lệch) | Man (hàn quá nhiệt)."
        ),
        "related": ["5 Whys", "Pareto", "8D", "A3", "Genba"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "5 Whys": {
        "term": "5 Whys",
        "full_name": "5 Whys — Kỹ Thuật Hỏi 'Tại Sao?' 5 Lần Truy Tìm Nguyên Nhân Gốc Rễ (Root Cause)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["5 Whys", "5 Why"],
        "case_sensitive": [],
        "short_desc": "Kỹ thuật đào sâu liên tiếp qua các lớp triệu chứng bề mặt cho đến khi chạm đúng lỗ hổng quy trình gốc để lỗi không bao giờ tái diễn.",
        "definition": (
            "Nếu chỉ xử lý triệu chứng bề mặt (ví dụ: thay cầu chì cháy, nhắc nhở công nhân cẩn thận hơn), lỗi sẽ quay lại sau vài ngày. "
            "5 Whys buộc đội điều tra hỏi ngược liên tục theo chuỗi nhân–quả có bằng chứng hiện trường (Genba) để tìm ra nguyên nhân hệ thống."
        ),
        "formula_or_spec": (
            "• Kiểm tra ngược logic ('Bởi vì ... nên ...'): nếu đọc xuôi từ Why 5 lên Why 1 thấy hợp lý 100% và có chứng cứ vật lý → Đã trúng Root Cause!"
        ),
        "cadivi_application": (
            "Áp dụng bắt buộc trong mọi báo cáo sự cố dừng máy lớn (> 30 phút), sự cố lỗi Spark hàng loạt hoặc khiếu nại khách hàng tại CADIVI Miền Trung."
        ),
        "cadivi_example": (
            "Ví dụ tại xưởng đùn: (1) Tại sao lỗi Spark tăng? Vì có bọt khí trong lớp nhựa PVC. (2) Tại sao có bọt khí? Vì hạt nhựa bị ẩm. (3) Tại sao ẩm? Vì sấy chưa đủ nhiệt 75°C. (4) Tại sao chưa đủ nhiệt? Vì ca đêm bật máy sấy muộn. (5) Tại sao bật muộn? Vì thiếu bộ hẹn giờ tự sấy & khóa liên động Poka-Yoke!"
        ),
        "related": ["Ishikawa", "8D", "A3", "PDCA", "Genba"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "8D": {
        "term": "8D",
        "full_name": "Eight Disciplines of Problem Solving — Quy Trình 8 Bước Giải Quyết Sự Cố Chất Lượng Nghiêm Trọng",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["8D", "8D Report"],
        "case_sensitive": ["8D"],
        "short_desc": "Chuẩn báo cáo 8 bước xử lý lỗi nghiêm trọng/khiếu nại khách hàng, nổi bật với bước D3 Ngăn chặn khẩn cấp và D5/D6 Khắc phục tận gốc.",
        "definition": (
            "8D là quy trình kỷ luật chuẩn công nghiệp (ô tô, điện-điện tử, cáp điện xuất khẩu) đảm bảo vừa cô lập bảo vệ khách hàng ngay trong 24 giờ (D3 Containment), "
            "vừa tìm gốc rễ (D4), xử lý triệt để (D5–D6), nhân rộng phòng ngừa sang mọi máy khác (D7) và khen thưởng đội nhóm (D8)."
        ),
        "formula_or_spec": (
            "• D1 Lập đội → D2 Mô tả lỗi (5W2H) → D3 Cô lập khẩn cấp (24h) → D4 Root Cause (5 Whys) → D5 Chọn đối sách gốc → D6 Triển khai & Kiểm chứng → D7 Ngăn tái diễn/Nhân rộng → D8 Chúc mừng & Đóng."
        ),
        "cadivi_application": (
            "Phối hợp giữa OE và QA/QC khi xử lý khiếu nại lô cáp công trình (ví dụ: rách vỏ, lỗi điện trở hoặc thiếu mét cuộn xuất xưởng)."
        ),
        "cadivi_example": (
            "Ví dụ khi phát hiện lô cáp lỗi chiều dài thiếu 3m/cuộn: D3 phong tỏa ngay kho xuất kiểm đếm lại 100% lô; D4 phát hiện trượt bánh xe Encoder đo mét do mòn cao su; D5–D6 thay bánh xe bọc PU + lắp sensor đối chiếu; D7 đưa vào lịch PM hiệu chuẩn Encoder toàn bộ 8 máy đùn."
        ),
        "related": ["A3", "PDCA", "5 Whys", "Ishikawa", "PFMEA"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "A3": {
        "term": "A3",
        "full_name": "Toyota A3 Report — Báo Cáo Dự Án Cải Tiến Cô Đọng Trên Một Trang Giấy A3",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["A3", "A3 Report"],
        "case_sensitive": ["A3"],
        "short_desc": "Khuôn mẫu trình bày toàn bộ câu chuyện cải tiến (Bối cảnh → Hiện trạng → Mục tiêu → Phân tích gốc → Kế hoạch → Kết quả ROI) gói gọn trên 1 trang A3 trực quan.",
        "definition": (
            "Báo cáo A3 là công cụ giao tiếp chiến lược chuẩn của người làm OE: ép buộc tư duy phải sắc nét, trực quan hóa bằng biểu đồ (Pareto, VSM, Xương cá, Before–After) "
            "để Ban Giám đốc đọc hiểu toàn bộ dự án trong 3 phút và ra quyết định phê duyệt ngay lập tức."
        ),
        "formula_or_spec": (
            "• Cột trái (Vấn đề): (1) Bối cảnh → (2) Hiện trạng số liệu → (3) Mục tiêu → (4) Phân tích gốc rễ.\n"
            "• Cột phải (Giải pháp): (5) Đối sách cải tiến → (6) Kế hoạch thực thi (Who-What-When) → (7) Theo dõi kết quả & Chuẩn hóa."
        ),
        "cadivi_application": (
            "Dùng A3 làm mẫu chuẩn khi trình bày mọi đề xuất Kaizen, SMED và tổng kết kết quả thử việc 60–90 ngày trước Giám đốc Nhà máy CADIVI Miền Trung."
        ),
        "cadivi_example": (
            "Ví dụ: Tóm tắt trọn vẹn dự án 'Giảm thời gian đổi màu máy đùn số 1 từ 55p → 12p, tiết kiệm 34 triệu/tháng' trên 1 tờ A3 duy nhất kèm ảnh hiện trường Trước–Sau và bảng bấm giờ SMED."
        ),
        "related": ["PDCA", "8D", "Kaizen", "ROI", "5 Whys"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "PDCA": {
        "term": "PDCA",
        "full_name": "Plan – Do – Check – Act (Chu Trình Deming Cải Tiến Liên Tục)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["PDCA"],
        "case_sensitive": ["PDCA"],
        "short_desc": "Vòng tròn tư duy khoa học 4 bước (Lập kế hoạch → Làm thử → Kiểm tra đối chiếu → Chuẩn hóa & Lặp lại) làm xương sống cho mọi hoạt động cải tiến.",
        "definition": (
            "Chu trình PDCA đảm bảo cải tiến không bao giờ bị làm nửa vời rồi bỏ ngỏ: luôn bắt đầu bằng mục tiêu & kế hoạch có số liệu (Plan), chạy thử quy mô nhỏ (Do), kiểm chứng dữ liệu thực tế đạt mục tiêu chưa (Check), và khóa thành tiêu chuẩn SOP nếu thành công hoặc điều chỉnh lại nếu chưa đạt (Act)."
        ),
        "formula_or_spec": (
            "• Plan (Xác định vấn đề, phân tích gốc, lập đối sách) → Do (Triển khai Pilot) → Check (Đo Before–After) → Act (Chuẩn hóa SOP & Nhân rộng)."
        ),
        "cadivi_application": (
            "Vận hành đều đặn theo chu kỳ tuần/tháng trong các cuộc họp giao ban Tier 2 tại CADIVI để đảm bảo mọi điểm Đỏ trên bảng OEE/BOM đều được theo đuổi đến khi xanh trở lại."
        ),
        "cadivi_example": (
            "Ví dụ: P (đặt mục tiêu giảm lỗi Spark < 2 lỗi/10km bằng sấy nhựa 75°C) → D (chạy thử 5 ca trên máy đùn số 2) → C (đo thực tế giảm còn 1.4 lỗi/10km) → A (ban hành SOP sấy bắt buộc cho cả 6 máy đùn)."
        ),
        "related": ["A3", "DMAIC", "Kaizen", "8D"],
        "doc_key": "oe_six_sigma_dmaic"
    },

    # =================================================================
    # NHÓM 5: ĐỊNH MỨC BOM, KHO VẬT TƯ & HAO PHÍ ĐẶC THÙ CÁP ĐIỆN
    # =================================================================
    "BOM": {
        "term": "BOM",
        "full_name": "Bill of Materials — Cây Định Mức Nguyên Vật Liệu Kỹ Thuật & Sản Xuất (EBOM / MBOM / SBOM)",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["BOM", "EBOM", "MBOM", "SBOM", "BOM Variance"],
        "case_sensitive": ["BOM", "EBOM", "MBOM", "SBOM"],
        "short_desc": "Bảng kê định mức chi tiết toàn bộ NVL (đồng, nhựa, độn, băng thép, bao bì) + hao phí công nghệ chuẩn để sản xuất 1 đơn vị thành phẩm.",
        "definition": (
            "BOM là xương sống kiểm soát giá thành và mua sắm vật tư của nhà máy. Trong đó EBOM do thiết kế R&D lập, "
            "MBOM do kỹ thuật sản xuất/OE lập (bổ sung thứ tự công đoạn, vật tư phụ và tỷ lệ hao hụt công nghệ chuẩn), còn SBOM dùng cho đóng gói thương mại. "
            "Chênh lệch giữa NVL xuất thực tế và định mức MBOM gọi là BOM Variance."
        ),
        "formula_or_spec": (
            "• Qty Variance = NVL Xuất Thực Tế - (Sản Lượng Đạt × Định Mức MBOM)\n"
            "• Cost Variance = Qty Variance × Đơn Giá NVL (Variance > 0 là vượt định mức, ăn mòn lợi nhuận!)."
        ),
        "cadivi_application": (
            "Cực kỳ sống còn tại CADIVI vì Đồng/Nhôm + Nhựa chiếm tới 80–88% giá thành cáp! OE theo dõi sát cây BOM đa tầng của cáp lực (CXV/CVV/DSTA), "
            "đảm bảo MBOM đã tính đúng hệ số xoắn bện (Lay-up Factor), tách rạch ròi hao phí công nghệ tự nhiên vs hao phí bất thường và đối soát 3 điểm cuối mỗi lệnh SX."
        ),
        "cadivi_example": (
            "Ví dụ BOM 1 km cáp CXV 3x50+1x25: Đồng ~1,562 kg (~78% giá trị NVL), XLPE ~114 kg, PVC vỏ ~385 kg, độn PP ~35 kg. "
            "Chỉ cần sai lệch BOM đồng +1% trên sản lượng 400 tấn/tháng là nhà máy mất trắng 1 tỷ VNĐ/tháng!"
        ),
        "related": ["Copper Give-away", "Over-thickness", "Lay-up Factor", "Cut-Length", "ERP", "Cycle Counting"],
        "doc_key": "bom_cost"
    },
    "Kitting": {
        "term": "Kitting",
        "full_name": "Kitting — Kỹ Thuật Soạn Sẵn Bộ Vật Tư Đồng Bộ Theo Lệnh Sản Xuất",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["Kitting"],
        "case_sensitive": [],
        "short_desc": "Kho chuẩn bị trước trọn bộ vật tư/phụ kiện đúng định mức cho 1 lệnh sản xuất rồi giao xuống máy để vừa chống thất thoát vừa chống quên bước.",
        "definition": (
            "Thay vì để vật tư rời rạc ngổn ngang quanh dây chuyền dễ thất thoát và lấy nhầm, kho soạn sẵn một bộ (Kit) chứa đúng số lượng phụ kiện theo BOM của lệnh sản xuất. "
            "Kitting đóng vai trò như một Poka-Yoke kiểm soát vật tư ngay tại trạm."
        ),
        "formula_or_spec": (
            "• 1 Kit = Toàn bộ vật tư phụ theo đúng 1 Work Order (nếu chạy xong mà thừa hoặc thiếu vật tư trong Kit → lập tức phát hiện sai sót!)."
        ),
        "cadivi_application": (
            "Áp dụng tại CADIVI cho các lệnh sản xuất cáp dự án (soạn sẵn trọn bộ tem nhãn, phiếu kiểm tra, đầu bịt chống ẩm cáp, màng bọc rulo gỗ đúng số lượng rulo của đơn hàng) và bộ phụ kiện đổi khuôn SMED."
        ),
        "cadivi_example": (
            "Ví dụ: Soạn sẵn Khay Kitting đổi mã máy đùn gồm đúng cặp Chày-Cối đã sấy, lưới lọc mới và thẻ Recipe cho 3 lệnh chạy trong ca → Giảm 100% thời gian chờ đi lấy phụ kiện."
        ),
        "related": ["BOM", "Two-Bin Kanban", "SMED", "Poka-Yoke"],
        "doc_key": "bom_cost"
    },
    "Cycle Counting": {
        "term": "Cycle Counting",
        "full_name": "Cycle Counting ABC — Kiểm Kê Luân Phiên Theo Phân Loại Giá Trị ABC",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["Cycle Counting", "Cycle Counting ABC"],
        "case_sensitive": [],
        "short_desc": "Kiểm đếm luân phiên hằng tuần/tháng các nhóm vật tư giá trị cao (Nhóm A như đồng rod, hạt nhựa XLPE) mà không phải dừng nhà máy cuối năm.",
        "definition": (
            "Thay vì cả năm mới dừng xưởng kiểm kê một lần (phát hiện mất hàng từ 8 tháng trước không thể truy gốc), Cycle Counting phân loại vật tư theo quy tắc ABC: "
            "Nhóm A (20% mã chiếm 80% giá trị) đếm hàng tuần; Nhóm B đếm hàng tháng; Nhóm C đếm hàng quý — giữ độ chính xác tồn kho ERP (RIA) ≥ 98.5%."
        ),
        "formula_or_spec": (
            "• Record Inventory Accuracy (RIA) = (Số mã khớp thực tế / Tổng số mã kiểm) × 100% ≥ 98.5%."
        ),
        "cadivi_application": (
            "Bắt buộc tại kho đồng rod, kho hạt nhựa PVC/XLPE/LSZH và khu cân phế liệu đồng trần/đồng dính nhựa của CADIVI để phát hiện ngay chênh lệch cân đong hoặc nhầm lẫn phiếu xuất kho trong vòng 1 tuần."
        ),
        "cadivi_example": (
            "Ví dụ: Kiểm kê Cycle Counting nhóm A (đồng rod + đồng phế + hạt XLPE) mỗi chiều thứ Sáu giúp phát hiện ngay sai số cân bàn 1.5% ở khu cân phế liệu đồng, tránh thất thoát hàng trăm triệu cuối năm."
        ),
        "related": ["BOM", "ERP", "Copper Give-away"],
        "doc_key": "bom_cost"
    },
    "Copper Give-away": {
        "term": "Copper Give-away",
        "full_name": "Copper Give-away — Hao Phí Đồng 'Cho Không' Khách Hàng Do Kéo Thừa Đường Kính",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Copper Give-away", "Copper Giveaway", "dư đồng"],
        "case_sensitive": [],
        "short_desc": "Lượng kim loại đồng tiêu hao vượt chuẩn định mức BOM do mòn khuôn kéo hoặc chỉnh dung sai an toàn quá rộng, dù điện trở IEC vốn đã dư đạt.",
        "definition": (
            "Tiêu chuẩn IEC 60228 đánh giá ruột dẫn theo ĐIỆN TRỞ TỐI ĐA (Ω/km ở 20°C), không bắt buộc đường kính to thừa. "
            "Khi khuôn kéo đồng bị mòn rộng ra dù chỉ +0.01 mm, khối lượng đồng tăng theo bình phương đường kính (D²) khiến nhà máy 'biếu không' hàng tấn đồng mỗi tháng mà khách hàng không trả thêm 1 xu nào!"
        ),
        "formula_or_spec": (
            "• Tỷ lệ dư đồng (%) = [ (D_thực² / D_chuẩn²) - 1 ] × 100%\n"
            "• Kéo dư 0.01 mm trên sợi Ø 1.78 mm → Dư +1.127% khối lượng đồng!"
        ),
        "cadivi_application": (
            "MỎ VÀNG TIẾT KIỆM SỐ 1 của Chuyên viên OE tại CADIVI Miền Trung! Kiểm soát bằng cách lập lịch thay khuôn kéo PCD theo định mức tấn đồng, theo dõi biểu đồ SPC đường kính sợi kéo và đối chiếu liên tục với dữ liệu đo điện trở 20°C từ phòng Lab."
        ),
        "cadivi_example": (
            "Ví dụ tại xưởng kéo sản lượng 200 tấn đồng/tháng (250 triệu đ/tấn): để khuôn mòn kéo sợi Ø1.78mm thành Ø1.79mm (+1.127%) làm bốc hơi 2.25 tấn đồng/tháng = 563 triệu VNĐ/tháng (~6.76 TỶ/năm)!"
        ),
        "related": ["Over-thickness", "IEC 60228", "RBD", "BOM", "SPC"],
        "doc_key": "cable_cost_capacity"
    },
    "Over-thickness": {
        "term": "Over-thickness",
        "full_name": "Compound Over-thickness — Hao Phí Bọc Dư Chiều Dày Nhựa Cách Điện / Vỏ Cáp",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Over-thickness", "bọc dư nhựa"],
        "case_sensitive": [],
        "short_desc": "Lượng nhựa PVC/XLPE/LSZH bị đùn dày thừa so với thiết kế do độ lệch tâm lớn hoặc không có kiểm soát SPC/Laser Gauge, gây thất thoát hàng tỷ đồng/năm.",
        "definition": (
            "Tiêu chuẩn TCVN/IEC quy định chặt chiều dày điểm mỏng nhất (t_min ≥ 0.9×t_nom - 0.1 mm). "
            "Khi đầu đùn bị lệch tâm (Eccentricity cao) hoặc máy đùn dao động mạnh (Cpk < 1.0), thợ đứng máy buộc phải 'bọc dày trừ hao' thêm +0.08 đến +0.15 mm để không bị QC trả hàng — tạo ra khoản lãng phí Overprocessing cực lớn."
        ),
        "formula_or_spec": (
            "• Khối lượng nhựa (kg/km) = π × (D_trong + t) × t × ρ_nhựa\n"
            "• Chỉ cần bọc dư +0.08 mm trên dây dân dụng VC 2.5mm² (t=0.80mm) đã làm tăng hơn +13% lượng nhựa PVC!"
        ),
        "cadivi_application": (
            "MỎ VÀNG TIẾT KIỆM SỐ 2 tại CADIVI Miền Trung: áp dụng đầu đùn tự định tâm (Self-centering Crosshead), gắn Laser Diameter & Eccentricity Gauge hồi tiếp kín (Closed-loop) và chạy Minitab SPC kéo Cpk ≥ 1.33 để đưa lớp nhựa về sát chuẩn thiết kế."
        ),
        "cadivi_example": (
            "Ví dụ mã dây VC 2.5mm² sản lượng 5,000 km/tháng: bọc dư từ 0.80mm lên 0.88mm tốn thêm 1.23 kg PVC/km = 6,150 kg/tháng × 32,000đ = 196.8 triệu VNĐ/tháng (~2.36 TỶ/năm) chỉ trên 1 mã hàng!"
        ),
        "related": ["Copper Give-away", "Laser Gauge", "Crosshead", "Cpk", "IEC 60502", "Minitab"],
        "doc_key": "cable_cost_capacity"
    },
    "Lay-up Factor": {
        "term": "Lay-up Factor",
        "full_name": "Lay-up / Stranding Factor (Hệ Số Xoắn Bện Ruột Dẫn & Ghép Lõi)",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Lay-up Factor", "Stranding Factor", "hệ số xoắn"],
        "case_sensitive": [],
        "short_desc": "Hệ số tăng chiều dài thực tế của sợi đồng/lõi pha khi xoắn hình lò xo (thường 1.015 – 1.035), bắt buộc phải có khi lập BOM cáp nhiều sợi.",
        "definition": (
            "Khi bện xoắn các sợi đồng quanh tâm (hoặc ghép xoắn 3–4 lõi pha thành cáp lực) theo bước xoắn h (Lay Length), mỗi sợi đơn đi theo đường xoắn ốc nên chiều dài vật lý luôn DÀI HƠN chiều dài đoạn cáp thẳng. "
            "Bước xoắn h càng ngắn (xoắn càng chặt) thì hệ số xoắn k càng lớn, tốn nhiều đồng hơn nhưng cáp mềm dẻo hơn."
        ),
        "formula_or_spec": (
            "• k_xoắn = sqrt( 1 + (π × D_vòng_xoắn / h)² )\n"
            "• Giá trị thực tế: Ruột đặc 1 sợi k = 1.00 | Ruột bện 7–61 sợi k ≈ 1.015 – 1.035 (+1.5% đến +3.5% đồng)."
        ),
        "cadivi_application": (
            "OE CADIVI kiểm tra bước xoắn thực tế trên máy bện Buncher/Rigid Strander so với bản vẽ kỹ thuật: nếu máy chỉnh bước xoắn ngắn hơn chuẩn sẽ vừa tốn đồng vượt BOM vừa làm giảm tốc độ mét/phút của máy bện!"
        ),
        "cadivi_example": (
            "Ví dụ: Nếu máy bện cáp 50mm² chỉnh bước xoắn quá dày làm hệ số xoắn tăng từ 1.020 lên 1.032 (+1.2% đồng), trên 100 tấn đồng bện sẽ làm âm BOM ngay 1.2 tấn đồng (~300 triệu VNĐ)!"
        ),
        "related": ["BOM", "Buncher", "Rigid Strander", "Copper Give-away"],
        "doc_key": "cable_cost_capacity"
    },
    "Cut-Length": {
        "term": "Cut-Length",
        "full_name": "Cut-Length / Cutting Stock Optimization — Tối Ưu Chiều Dài Rulo & Ghép Cắt Đơn Hàng",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Cut-Length", "Cutting Stock", "Remnant"],
        "case_sensitive": [],
        "short_desc": "Bài toán lập lịch chiều dài bện/đùn ngược từ đơn hàng và ghép tổ hợp cắt trên rulo nhằm triệt tiêu mẩu cáp ngắn thừa (Remnant Scrap).",
        "definition": (
            "Trong sản xuất cáp điện, khách hàng công trình đặt nhiều độ dài rulo khác nhau (300m, 500m, 850m, 1,000m). "
            "Nếu không tính chiều dài đồng bộ từ công đoạn bện hoặc không tối ưu ghép đoạn cắt, mỗi rulo dễ dư ra mẩu cáp lẻ 80–200m không bán được phải chuyển phế đồng dính nhựa (lỗ 20–30% giá trị)."
        ),
        "formula_or_spec": (
            "• Backward Length Planning: L_bện = Tổng L_đơn_ghép + L_hao_đầu_đuôi_đùn (10–20m) + Dự phòng sai số Encoder (≤ 0.3%).\n"
            "• Công cụ giải tối ưu tổ hợp: Excel Solver hoặc Python (PuLP Linear Programming)."
        ),
        "cadivi_application": (
            "Đặc biệt quan trọng cho dòng cáp lực hạ thế/trung thế tiết diện lớn (50–300 mm²) tại CADIVI Miền Trung — nơi chỉ 100m cáp thừa CXV 3x240 có giá trị lên tới cả trăm triệu đồng!"
        ),
        "cadivi_example": (
            "Ví dụ: Thay vì bện mặc định đầy rulo 2,150m cho đơn cắt cuộn 500m (dư 150m phế!), OE áp dụng Backward Planning bện đúng 2,015m (4×500m + 15m startup) + hiệu chuẩn Encoder đo mét → Giảm 85% mẩu cáp thừa!"
        ),
        "related": ["BOM", "RCCP", "Rigid Strander", "VBA"],
        "doc_key": "cable_cost_capacity"
    },

    # =================================================================
    # NHÓM 6: 9 NHÓM MÁY MÓC, CÔNG NGHỆ & TIÊU CHUẨN DÂY CÁP ĐIỆN CADIVI
    # =================================================================
    "RBD": {
        "term": "RBD",
        "full_name": "Rod Breakdown Machine — Máy Kéo Thô Đồng / Nhôm (Công Đoạn Đầu Tiên)",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["RBD", "Rod Breakdown", "Máy kéo thô", "Wire Drawing"],
        "case_sensitive": ["RBD"],
        "short_desc": "Máy kéo công suất lớn (200–500 kW) kéo thanh đồng rod Ø 8.0 mm (hoặc nhôm Ø 9.5 mm) xuống Ø 1.38–4.5 mm qua 9–13 cấp khuôn PCD.",
        "definition": (
            "RBD là 'cửa ngõ' công nghệ của nhà máy dây cáp điện: kéo thanh kim loại thô qua dãy khuôn kim cương nhân tạo (PCD) ngập trong bể dung dịch nhũ tương làm mát/bôi trơn tốc độ 15–35 m/s, "
            "thường tích hợp bộ ủ điện trở liên tục (In-line Annealer) và cụm thu dây kép tự động sang cuộn không dừng máy."
        ),
        "formula_or_spec": (
            "• Đầu vào: Đồng rod Ø 8.0 mm (Cu ≥ 99.99%) / Nhôm rod Ø 9.5 mm → Đầu ra: Ø 1.38 – 4.5 mm.\n"
            "• KPI OE chuẩn ngành: Breaks/Ton (số lần đứt sợi trên 1 tấn đồng kéo, mục tiêu < 0.2 lần/tấn) & kWh/tấn."
        ),
        "cadivi_application": (
            "Cung cấp toàn bộ sợi đồng/nhôm nền cho cả Nhà máy CADIVI Miền Trung. Trọng tâm OE tại RBD: giảm đứt sợi (kiểm soát nhũ tương, mối hàn Butt Weld, lịch thay khuôn PCD), chống Copper Give-away và tận dụng giờ điện thấp điểm ca đêm."
        ),
        "cadivi_example": (
            "Ví dụ: Theo dõi KPI Breaks/Ton phát hiện máy RBD số 1 đứt 0.9 lần/tấn (gây dừng xỏ lại 18p/lần). Soi kính hiển vi thấy đầu đứt dạng xước kéo → lọc ly tâm bể nhũ tương loại mạt đồng & thay sớm bộ khuôn mòn kéo Breaks/Ton về 0.15 lần/tấn!"
        ),
        "related": ["Annealing", "Copper Give-away", "TPM", "OEE", "IEC 60228"],
        "doc_key": "cable_mfg_machines"
    },
    "Annealing": {
        "term": "Annealing",
        "full_name": "Annealing (Ủ Mềm Kim Loại — In-line Resistance Annealer & Lò Ủ Chuông Bell Furnace)",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Annealing", "Annealer", "Lò ủ", "ủ đồng"],
        "case_sensitive": [],
        "short_desc": "Công đoạn xử lý nhiệt phục hồi độ dẻo (giãn dài 20–30%) và độ dẫn điện (≥ 100% IACS) cho sợi đồng bị hóa bền cứng sau khi kéo nguội.",
        "definition": (
            "Kéo nguội qua hàng chục khuôn làm mạng tinh thể đồng bị biến dạng và cứng giòn (Work Hardening), điện trở suất tăng cao. "
            "Công đoạn Ủ tái kết tinh đồng bằng 1 trong 2 cách: Ủ liên tục bằng dòng điện (In-line Annealer trong buồng hơi nước) hoặc Ủ mẻ trong lò chuông chân không/khí Nitơ (Bell Furnace 250–380°C)."
        ),
        "formula_or_spec": (
            "• Yêu cầu chất lượng sau ủ: Độ giãn dài (Elongation) ≥ 20–30%, Độ dẫn điện ≥ 100% IACS, bề mặt sáng bóng không oxy hóa đen, không dính vòng sợi (Stickiness)."
        ),
        "cadivi_application": (
            "Tại CADIVI: nếu ủ non → sợi cứng gãy ở máy bện & rớt điện trở IEC 60228; nếu ủ già → sợi dính bết rulo hoặc kéo giãn nhỏ tiết diện. Với lò ủ chuông, OE tối ưu xếp đầy tải mẻ (Full-load) và chạy vào khung giờ điện thấp điểm!"
        ),
        "cadivi_example": (
            "Ví dụ: Tối ưu lịch xếp rulo lò ủ chuông từ mức tải trung bình 68% lên 95% và chuyển 80% mẻ ủ sang khung 22:00–04:00 giúp giảm ngay 24% chi phí điện năng công đoạn ủ!"
        ),
        "related": ["RBD", "IEC 60228", "Buncher", "Rigid Strander"],
        "doc_key": "cable_mfg_machines"
    },
    "Buncher": {
        "term": "Buncher",
        "full_name": "Double Twist Bunching Machine — Máy Bện Xoắn Đôi Tốc Độ Cao",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Buncher", "Double Twist Buncher", "máy bện xoắn đôi"],
        "case_sensitive": [],
        "short_desc": "Máy bện cánh cung quay tốc độ cao tạo 2 vòng xoắn mỗi vòng quay, chuyên sản xuất ruột dẫn đồng mềm nhiều sợi mảnh cho dây dân dụng (VCm, VCmd).",
        "definition": (
            "Máy bện xoắn đôi (cỡ rulo thu Ø 500/630/800 mm) kéo đồng thời hàng chục sợi đồng mảnh (Ø 0.15–0.40 mm) từ giàn nhả dây Pay-off đi qua cánh cung quay 3,000–6,000 vòng/phút để bện thành ruột mềm. "
            "Máy chạy tự động hoàn toàn trong 25–45 phút mỗi rulo nên là điểm lý tưởng áp dụng mô hình 1 công nhân đứng nhiều máy."
        ),
        "formula_or_spec": (
            "• Sản phẩm điển hình: Dây mềm dân dụng VCm, VCmd, VCmt (Class 5 theo IEC 60228).\n"
            "• Điểm kiểm soát: Cảm biến đứt sợi Poka-Yoke, bước xoắn (Lay-up Factor) và đồng đều lực căng từng sợi."
        ),
        "cadivi_application": (
            "Trọng tâm OE tại khu máy Buncher CADIVI: (1) Tối ưu Man-Machine Chart lên 1 thợ đứng 3–4 máy; (2) Giảm thời gian nạp giàn rulo bằng xe đổi rulo nhanh SMED; (3) Kiểm soát phế đồng trần do đứt sợi."
        ),
        "cadivi_example": (
            "Ví dụ: Cải tiến xe cấp rulo 2 tầng kết hợp Man-Machine Chart chuyển từ 1 người/2 máy sang 1 người/3 máy trên dãy 12 máy Buncher → Giải phóng ngay 2 nhân sự chuyển sang tổ đóng gói đang thiếu người mà sản lượng bện không giảm!"
        ),
        "related": ["Man-Machine Chart", "Rigid Strander", "Lay-up Factor", "Poka-Yoke", "OLE"],
        "doc_key": "cable_mfg_machines"
    },
    "Rigid Strander": {
        "term": "Rigid Strander",
        "full_name": "Rigid Frame Strander & Tubular Strander — Máy Bện Lồng Cứng & Bện Ống Cáp Lực",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Rigid Strander", "Rigid Frame Strander", "Tubular Strander", "máy bện lồng cứng", "bện nén"],
        "case_sensitive": [],
        "short_desc": "Máy bện cỡ lớn (12+18+24+30 rulo) sản xuất ruột dẫn cáp lực đồng/nhôm 7–61 sợi tiết diện tới 300–630 mm², hỗ trợ bện nén tròn & bện rẻ quạt.",
        "definition": (
            "Rigid Frame Strander chứa hàng chục rulo sợi đồng/nhôm bố trí trên các lồng quay cứng đồng tâm, cho phép bện đồng thời nhiều lớp ruột dẫn cáp lực cỡ lớn. "
            "Khi gắn khuôn ép nén (Compacting Die/Rollers), ruột dẫn đạt hệ số điền đầy > 90% (ruột bện nén tròn Compacted Round hoặc rẻ quạt Sector-shaped) giúp giảm đường kính ngoài 8–10%!"
        ),
        "formula_or_spec": (
            "• Lợi ích công nghệ Bện nén (Compacted Stranding): Giảm đường kính ruột dẫn 8–10% → Tiết kiệm trực tiếp 10–15% nhựa XLPE/PVC bọc ngoài!"
        ),
        "cadivi_application": (
            "Xương sống sản xuất cáp điện lực hạ thế & trung thế tới 300 mm² tại Nhà máy CADIVI Miền Trung. Điểm đánh OE: SMED rút thời gian nạp 37–61 rulo (Side-loader), tính Cut-Length chống thừa mẩu cáp và kiểm soát hệ số xoắn Lay-up Factor."
        ),
        "cadivi_example": (
            "Ví dụ: Thời gian nạp 37 rulo trên máy Rigid mất 75 phút/lần do nạp từng rulo thủ công. Chuẩn hóa tổ 2 người song song + chuẩn bị sẵn bộ rulo bằng chiều dài trên khay nạp bên ngoài rút xuống còn 32 phút (-57%)!"
        ),
        "related": ["Buncher", "Lay-up Factor", "Cut-Length", "SMED", "IEC 60228"],
        "doc_key": "cable_mfg_machines"
    },
    "Extruder": {
        "term": "Extruder",
        "full_name": "Cable Extrusion Line — Dây Chuyền Đùn Bọc Cách Điện & Bọc Vỏ Cáp (PVC / XLPE / PE / LSZH)",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Extruder", "Extrusion", "máy đùn", "Dây chuyền Đùn"],
        "case_sensitive": [],
        "short_desc": "Trái tim và nút thắt quan trọng nhất của nhà máy cáp (dài 25–60m): nung chảy dẻo hạt nhựa qua trục vít ép bọc lên ruột dẫn đồng/nhôm với độ chính xác ±0.01 mm.",
        "definition": (
            "Dây chuyền đùn hoàn chỉnh gồm 10 cụm nối tiếp: Pay-off nhả dây → Bộ gia nhiệt ruột đồng (Pre-heater) → Máy đùn trục vít (Single-screw Ø50–150mm, 4–6 vùng nhiệt) → Đầu chữ thập (Crosshead Tip & Die) → Laser Gauge → Máng nước làm mát → Spark Tester → Máy in phun → Bộ kéo Capstan → Cụm thu dây kép tự động (Dual Take-up)."
        ),
        "formula_or_spec": (
            "• Nhiệt độ đùn điển hình: PVC (140–185°C) | XLPE Silane (160–210°C) | Nước làm mát (≤ 25°C).\n"
            "• Tốc độ đùn: Dây dân dụng VC 1.5–2.5 (300–800 m/phút) | Cáp lực lớn CXV (15–80 m/phút)."
        ),
        "cadivi_application": (
            "Khu vực tạo ra tác động ROI lớn nhất cho Chuyên viên OE CADIVI: (1) SMED đổi màu/tiết diện + Color Sequencing + Purging; (2) Laser Closed-loop + SPC xóa Over-thickness nhựa; (3) Triệt tiêu lỗi Spark & phế đồng dính nhựa đầu ca; (4) Giảm điện năng Idle Heating."
        ),
        "cadivi_example": (
            "Ví dụ: Chỉ 1 dự án đồng bộ trên dây chuyền đùn Ø70mm (SMED 55p→12p + Chiller nước lạnh nâng tốc độ 300→330 m/phút + Laser Gauge giảm 0.08mm nhựa dư) giúp nâng OEE từ 65% lên 84.6% và tiết kiệm > 2 tỷ/năm!"
        ),
        "related": ["Crosshead", "Laser Gauge", "Spark Tester", "SMED", "Color Sequencing", "Purging", "Over-thickness", "XLPE", "PVC"],
        "doc_key": "cable_mfg_machines"
    },
    "Crosshead": {
        "term": "Crosshead",
        "full_name": "Extrusion Crosshead & Tip/Die — Đầu Chữ Thập & Bộ Chày–Cối Định Hình Lớp Cách Điện",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Crosshead", "Tip & Die", "Tip/Die", "Chày-Cối", "Chày–Cối", "đầu chữ thập"],
        "case_sensitive": [],
        "short_desc": "Bộ phận bẻ góc dòng nhựa nóng chảy 90° bao quanh ruột dẫn đồng tại đầu máy đùn; quyết định độ đồng tâm (Eccentricity) và thời gian đổi mã SMED.",
        "definition": (
            "Đầu chữ thập chứa Chày dẫn dây (Tip/Core tube) và Cối định hình ngoài (Die). "
            "Có 2 loại: Đầu truyền thống (phải vặn 4–8 ốc căn tâm thủ công rất tốn thời gian SMED và dễ lệch tâm) và Đầu tự định tâm (Self-centering Crosshead — tháo lắp nhanh, độ đồng tâm > 95% ngay khi lắp)."
        ),
        "formula_or_spec": (
            "• Độ đồng tâm (Concentricity %) = (Chiều dày mỏng nhất t_min / Chiều dày lớn nhất t_max) × 100% (mục tiêu ≥ 90–95%)."
        ),
        "cadivi_application": (
            "Cải tiến đắt giá trong SMED tại CADIVI: chuẩn bị bộ Crosshead/Tip-Die dự phòng, vệ sinh sạch nhựa cháy và sấy nóng trước lên 160°C trong tủ nhiệt đặt cạnh máy đùn để thay lắp trong 3.5 phút thay vì 20 phút!"
        ),
        "cadivi_example": (
            "Ví dụ: Đầu tư nâng cấp đầu Self-centering Crosshead + tủ sấy ngoài trên dây chuyền đùn chủ lực cắt giảm 16 phút/lần đổi tiết diện và thu hẹp độ lệch tâm từ 14% xuống dưới 4%, giúp giảm ngay 6% lượng nhựa bọc dư."
        ),
        "related": ["Extruder", "SMED", "Over-thickness", "Laser Gauge"],
        "doc_key": "cable_mfg_machines"
    },
    "Spark Tester": {
        "term": "Spark Tester",
        "full_name": "High-Frequency Spark Tester — Thiết Bị Thử Thủng Cách Điện Cao Áp Trực Tuyến",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Spark Tester", "Spark Test", "Spark Fault", "Spark"],
        "case_sensitive": [],
        "short_desc": "Thiết bị Poka-Yoke bắt buộc đặt ngay sau máng làm mát dây chuyền đùn, phóng điện áp cao 3–25 kV phát hiện tức thì lỗ mọt khí, dị vật hay chỗ nhựa mỏng thủng.",
        "definition": (
            "Dây cáp vừa bọc nhựa và làm nguội chạy qua điện cực chuỗi hạt thép của Spark Tester mang điện áp cao tần (3 kV – 25 kV tùy loại cáp). "
            "Nếu lớp cách điện có bất kỳ lỗ kim (Pinhole), bọt khí, hạt cháy dẫn điện hay gai sợi đồng đâm ra, tia lửa điện lập tức phóng xuống ruột đồng nối đất → Máy đếm lỗi, bật còi Andon, phun mực đánh dấu hoặc dừng chuyền."
        ),
        "formula_or_spec": (
            "• Điện áp thử phổ biến (IEC 62230): Dây dân dụng 0.6–0.8mm → 5–6 kV | Cáp hạ thế XLPE/PVC → 10–15 kV.\n"
            "• KPI chất lượng đùn: Số lỗi Spark / 10 km dây (mục tiêu < 0.5 lỗi/10km)."
        ),
        "cadivi_application": (
            "Chuyên viên OE CADIVI lấy dữ liệu đếm lỗi từ Spark Tester làm đầu vào cho dự án DMAIC: cắt đúng vị trí đánh dấu lỗi soi kính hiển vi phân loại (Bọt khí ẩm nhựa vs Hạt cháy quá nhiệt vs Gai đồng đứt vs Mỏng lệch tâm) để xử lý triệt để."
        ),
        "cadivi_example": (
            "Ví dụ: Tỷ lệ lỗi Spark tăng vọt lên 15 lỗi/10 km trên dây VCm 1.5mm². OE cắt 20 điểm lỗi soi mặt cắt phát hiện 75% do gai sợi đồng mảnh bị xước khi qua puli dẫn hướng → thay puli sứ trơn giúp lỗi Spark rơi về 0.3 lỗi/10 km!"
        ),
        "related": ["Extruder", "Poka-Yoke", "Jidoka", "PFMEA", "DMAIC", "MES"],
        "doc_key": "cable_mfg_machines"
    },
    "Laser Gauge": {
        "term": "Laser Gauge",
        "full_name": "Laser Diameter & Eccentricity Gauge — Cảm Biến Laser Đo Đường Kính & Độ Lệch Tâm Trực Tuyến",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Laser Gauge", "Laser Diameter", "Eccentricity Gauge"],
        "case_sensitive": [],
        "short_desc": "Thiết bị đo quang học không tiếp xúc (hãng Sikora/Zumbach) đo đường kính ngoài & độ đồng tâm 1,000 lần/giây, nối vòng kín tự chỉnh tốc độ Capstan.",
        "definition": (
            "Laser Gauge quét chùm tia laser 2–3 trục lên dây cáp đang chạy tốc độ hàng trăm mét/phút để đo liên tục đường kính ngoài chính xác tới ±0.002 mm (và dùng cảm ứng/X-ray đo độ lệch tâm ruột đồng). "
            "Ở chế độ Closed-loop Feedback, tín hiệu từ Laser Gauge tự động tăng/giảm tốc độ kéo Capstan để giữ đường kính luôn bám sát tâm mục tiêu."
        ),
        "formula_or_spec": (
            "• Độ chính xác: ±0.002 mm | Tần suất đo: 500–2,000 lần/giây.\n"
            "• Nối thẳng vào PLC/MES xuất biểu đồ SPC Xbar-R thời gian thực."
        ),
        "cadivi_application": (
            "Thiết bị hoàn vốn nhanh nhất (Payback < 12 tháng) trong các đề xuất CAPEX của OE tại CADIVI: thu hẹp độ lệch chuẩn σ giúp giảm 5–10% lượng nhựa PVC/XLPE bọc dư (Over-thickness) và giảm phế startup đầu ca."
        ),
        "cadivi_example": (
            "Ví dụ: Gắn bộ điều khiển hồi tiếp kín Laser Gauge → Capstan trên dây chuyền đùn dây VC 2.5mm² giảm σ từ 0.055mm xuống 0.020mm, tiết kiệm 1.1 tấn PVC/tháng (~420 triệu VNĐ/năm/1 dây chuyền)."
        ),
        "related": ["Over-thickness", "Extruder", "SPC", "Cpk", "CAPEX", "Jidoka"],
        "doc_key": "cable_mfg_machines"
    },
    "Color Sequencing": {
        "term": "Color Sequencing",
        "full_name": "Color Sequencing — Lập Lịch Chuỗi Màu Sáng Đến Tối Cho Máy Đùn Bọc Cáp",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Color Sequencing", "Chuỗi màu", "Chuỗi Màu"],
        "case_sensitive": [],
        "short_desc": "Nguyên tắc xếp lệnh sản xuất máy đùn theo thứ tự màu Trắng → Vàng → Xanh lá → Đỏ → Xanh dương → Đen để cắt giảm 60–70% thời gian & nhựa xả purging.",
        "definition": (
            "Trong công nghệ đùn nhựa, chuyển từ màu SÁNG sang màu TỐI (vd: Vàng → Đỏ → Đen) chỉ cần xả rất ít nhựa là sạch màu ngay; "
            "ngược lại chuyển từ ĐEN sang TRẮNG buộc phải tháo vệ sinh hoặc xả bỏ 25–40 kg nhựa hỗn hợp mới hết vệt đen! Color Sequencing tối ưu thứ tự chạy trong điều độ để triệt tiêu các lần đổi ngược Tối → Sáng."
        ),
        "formula_or_spec": (
            "• Chuỗi màu vàng ngành cáp: Tự nhiên/Trắng → Vàng → Xanh lá/Vàng-Xanh → Đỏ → Xanh dương → Xám → Nâu → Đen (hết vòng mới xả mạnh 1 lần duy nhất)."
        ),
        "cadivi_application": (
            "Cải tiến 0 ĐỒNG mang lại hiệu quả tức thì ngay trong tháng đầu tiên của OE tại CADIVI Miền Trung bằng cách phối hợp phòng Kế hoạch/Điều độ sắp lại thứ tự Lệnh Sản Xuất trong ngày/tuần."
        ),
        "cadivi_example": (
            "Ví dụ: Xếp lại lịch 5 màu dây dân dụng trong ngày theo đúng chuỗi Sáng → Tối giúp cắt giảm thời gian đổi màu trung bình từ 22 phút xuống 6 phút/lần và giảm 65% lượng nhựa xả phế mỗi tuần!"
        ),
        "related": ["SMED", "Purging", "Heijunka", "Extruder", "OEE"],
        "doc_key": "smed"
    },
    "Purging": {
        "term": "Purging",
        "full_name": "Purging & Purging Compound — Quy Trình & Hợp Chất Xả Làm Sạch Trục Vít Máy Đùn",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Purging", "Purging Compound", "Purge Scrap", "xả nhựa"],
        "case_sensitive": [],
        "short_desc": "Thao tác đẩy sạch nhựa cũ còn tồn trong nòng/trục vít khi đổi màu hoặc đổi loại nhựa (PVC ↔ XLPE) bằng hạt xả chuyên dụng để giảm phế và thời gian dừng máy.",
        "definition": (
            "Khi kết thúc lô màu cũ, trong nòng xy-lanh và rãnh trục vít máy đùn vẫn còn vài kg nhựa nóng chảy bám dính. "
            "Dùng hạt nhựa nguyên sinh thường để đẩy sạch màu đen rất chậm và tốn 20–35 kg nhựa phế (Purge Scrap). Dùng hợp chất Purging Compound chuyên dụng tạo lực cọ rửa cơ học/hóa học giúp sạch màu nhanh gấp 3 lần."
        ),
        "formula_or_spec": (
            "• Lưu ý an toàn cực kỳ quan trọng: TUYỆT ĐỐI không để nhựa PVC lẫn với nhựa XLPE/PE ở nhiệt độ cao (>200°C) vì PVC sẽ cháy phân hủy sinh khí axit HCl ăn mòn trục vít và gây nổ áp suất!"
        ),
        "cadivi_application": (
            "Theo dõi riêng KPI 'kg Purge Scrap / lần đổi mã' trên từng máy đùn CADIVI và chuẩn hóa SOP dùng Purging Compound kết hợp Color Sequencing."
        ),
        "cadivi_example": (
            "Ví dụ: Khi bắt buộc chuyển từ Đen sang Trắng cuối chu kỳ tuần, dùng 3 kg Purging Compound thay cho 28 kg PVC nguyên sinh rút thời gian xả từ 24 phút xuống 7 phút và giảm ngay 80% rác nhựa trộn màu!"
        ),
        "related": ["Color Sequencing", "SMED", "Extruder", "PVC", "XLPE"],
        "doc_key": "smed"
    },
    "XLPE": {
        "term": "XLPE",
        "full_name": "Cross-Linked Polyethylene — Nhựa Cách Điện Polyetylen Khâu Mạch Chịu Nhiệt Cao (90°C)",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["XLPE"],
        "case_sensitive": ["XLPE"],
        "short_desc": "Vật liệu cách điện cao cấp cho cáp điện lực hạ thế (CXV) và trung/cao thế, chịu nhiệt vận hành 90°C và ngắn mạch 250°C nhờ liên kết ngang 3 chiều.",
        "definition": (
            "Nhựa PE thường là nhựa nhiệt dẻo dễ chảy mềm khi nóng; sau khi được 'khâu mạch' (Cross-linking bằng công nghệ Silane hoặc Peroxide CCV), các mạch phân tử liên kết thành mạng lưới 3 chiều nhiệt rắn giúp tăng khả năng tải dòng điện, chịu nhiệt 90°C và chịu va đập/hóa chất vượt trội so với PVC."
        ),
        "formula_or_spec": (
            "• Khối lượng riêng ρ ≈ 0.92–0.94 g/cm³ (nhẹ hơn PVC ~1.42 g/cm³).\n"
            "• Phép thử chất lượng bắt buộc tại Lab: Hot Set Test (Thử độ giãn biến dạng nhiệt ở 200°C kiểm tra đạt độ khâu mạch)."
        ),
        "cadivi_application": (
            "Sản phẩm chủ lực giá trị cao của CADIVI Miền Trung (dòng cáp CXV, AXV, cáp trung thế). OE cần lưu ý đặc thù: XLPE sau khi khâu mạch KHÔNG THỂ nấu chảy tái chế như PVC → Phế phẩm XLPE là tổn thất mất trắng, phải kiểm soát cực chặt phế startup & lịch bể xông Sauna!"
        ),
        "cadivi_example": (
            "Ví dụ: Tối ưu quy trình chạy liên hoàn và kiểm soát độ dày XLPE bằng Laser Gauge cho dòng cáp CXV 3x50+1x25 giúp giảm 45% lượng nhựa XLPE phế không tái chế được."
        ),
        "related": ["Silane", "CCV", "PVC", "Extruder", "IEC 60502", "Over-thickness"],
        "doc_key": "cable_mfg_machines"
    },
    "PVC": {
        "term": "PVC",
        "full_name": "Polyvinyl Chloride — Nhựa Cách Điện & Vỏ Bọc Phổ Biến Cho Dây Dân Dụng & Cáp Hạ Thế",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["PVC"],
        "case_sensitive": ["PVC"],
        "short_desc": "Vật liệu nhựa nhiệt dẻo (chịu nhiệt 70°C, ρ ≈ 1.38–1.48 g/cm³) dùng làm cách điện dây dân dụng (VC, VCm) và vỏ bọc bảo vệ ngoài cáp lực (CVV, CXV).",
        "definition": (
            "PVC là hợp chất nhựa nhiệt dẻo pha trộn phụ gia hóa dẻo, ổn định nhiệt, chống cháy và bột màu — dễ gia công đùn tốc độ cao, chống cháy lan khá tốt và giá thành kinh tế. "
            "Nhược điểm công nghệ: rất nhạy với quá nhiệt (cháy phân hủy tạo hạt đen dẫn điện gây lỗi Spark) và dễ hút ẩm gây bọt khí nếu không sấy kỹ."
        ),
        "formula_or_spec": (
            "• Nhiệt độ làm việc cáp PVC: 70°C (ngắn mạch 160°C) | Khối lượng riêng ρ ≈ 1.38–1.48 g/cm³.\n"
            "• Có thể băm nghiền nhựa xả sạch (Granulator) tái sử dụng làm lớp độn bên trong (nhưng tuyệt đối không lẫn vào cách điện chính)."
        ),
        "cadivi_application": (
            "Chiếm khối lượng tiêu thụ nhựa lớn nhất tại Nhà máy CADIVI Miền Trung (toàn bộ dây dân dụng VC/VCm và vỏ bọc ngoài CVV/CXV). Trọng tâm OE: sấy kiểm soát độ ẩm, tránh cháy nhựa dừng máy lâu, Color Sequencing và giảm Over-thickness."
        ),
        "cadivi_example": (
            "Ví dụ: Gắn bộ sấy Hopper Dryer 75°C và khóa nhiệt độ các vùng nòng đùn PVC ổn định ±2°C giảm 70% phế phẩm bọt khí và hạt cháy đen trên dây dân dụng."
        ),
        "related": ["XLPE", "LSZH", "Extruder", "Spark Tester", "Over-thickness"],
        "doc_key": "cable_mfg_machines"
    },
    "LSZH": {
        "term": "LSZH",
        "full_name": "Low Smoke Zero Halogen (LSZH / LSHF) — Vỏ Bọc Chậm Cháy Không Khói Độc Halogen",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["LSZH", "LSHF"],
        "case_sensitive": ["LSZH", "LSHF"],
        "short_desc": "Vật liệu bọc cáp an toàn cao cấp (dùng cho cao ốc, bệnh viện, sân bay, tàu điện) khi cháy sinh cực ít khói và không tỏa khí độc axit HCl như PVC.",
        "definition": (
            "Khác với PVC chứa Clo (khi cháy sinh khói đen đặc và khí axit HCl gây ngạt), hợp chất LSZH/LSHF sử dụng phụ gia khoáng hydroxide nhôm/magie tự giải phóng hơi nước dập lửa, đảm bảo tầm nhìn thoát hiểm khi hỏa hoạn."
        ),
        "formula_or_spec": (
            "• Tiêu chuẩn thử nghiệm: IEC 60332 (Chậm cháy), IEC 60754 (Không khí axit halogen), IEC 61034 (Độ truyền sáng khói ≥ 60%).\n"
            "• Độ nhớt nhựa cao hơn PVC → Đòi hỏi trục vít chuyên dụng (tỷ số nén thấp) và kiểm soát nhiệt độ cực nhạy (quá 165–175°C dễ sinh bọt khí!)."
        ),
        "cadivi_application": (
            "Dòng sản phẩm biên lợi nhuận cao đang tăng trưởng mạnh tại CADIVI. OE cần thiết lập cửa sổ thông số đùn riêng (Recipe) và lịch chạy chiến dịch riêng vì tốc độ đùn LSZH thấp hơn PVC và giá hạt nhựa đắt gấp 1.5–2 lần."
        ),
        "cadivi_example": (
            "Ví dụ: Nếu lấy tốc độ chuẩn của vỏ PVC (45 m/phút) áp sang tính OEE cho vỏ LSZH (tốc độ thiết kế chỉ 25 m/phút) sẽ làm méo mó hoàn toàn chỉ số Performance → OE phải phân tách Ideal Speed riêng theo loại nhựa trên bảng Dim_CableSKU."
        ),
        "related": ["PVC", "XLPE", "Extruder", "IEC 60502"],
        "doc_key": "cable_mfg_machines"
    },
    "Silane": {
        "term": "Silane",
        "full_name": "Silane Cross-Linking (Bể Nước Nóng / Phòng Xông Hơi Sauna Khâu Mạch XLPE)",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Silane", "Sauna"],
        "case_sensitive": [],
        "short_desc": "Công nghệ khâu mạch XLPE bằng hơi ẩm/nước nóng 80–90°C sau khi đùn (phổ biến cho cáp hạ thế CXV), dễ tạo điểm chờ WIP nếu không lập lịch đồng bộ.",
        "definition": (
            "Ruột dẫn được đùn bọc hợp chất PE ghép Silane + xúc tác trên máy đùn thường, sau đó các rulo lõi được đưa vào bể nước nóng hoặc phòng xông hơi Sauna ở 80–90°C trong 4–12 giờ để hơi nước khuếch tán tạo liên kết ngang XLPE hoàn chỉnh."
        ),
        "formula_or_spec": (
            "• Nhiệt độ xông: 80–90°C | Thời gian: 4–12 giờ tùy chiều dày cách điện.\n"
            "• Kiểm tra đạt chuẩn: Hot Set Test tại Phòng Lab (độ giãn dưới tải ở 200°C ≤ 175%, biến dạng dư ≤ 15%)."
        ),
        "cadivi_application": (
            "Điểm cực dễ phát sinh tắc nghẽn Lead Time tại nhà máy cáp hạ thế như CADIVI Miền Trung: nếu máy đùn đẩy rulo ra lẻ tẻ mà bể Sauna phải chờ gom đủ mẻ mới đóng cửa xông sẽ làm kéo dài Lead Time thêm 1–2 ngày!"
        ),
        "cadivi_example": (
            "Ví dụ: Đồng bộ lịch chạy 3 lõi pha Đỏ–Vàng–Xanh vào cùng 1 mẻ xông Sauna (lấp đầy ≥ 90% dung tích bể) vừa cắt giảm 20 giờ chờ WIP, vừa tiết kiệm 18% năng lượng gia nhiệt hơi nước!"
        ),
        "related": ["XLPE", "CCV", "Lead Time", "WIP", "VSM"],
        "doc_key": "cable_mfg_machines"
    },
    "CCV": {
        "term": "CCV",
        "full_name": "Catenary Continuous Vulcanization — Dây Chuyền Lưu Hóa Liên Tục Cáp Trung/Cao Thế",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["CCV", "CCV Line"],
        "case_sensitive": ["CCV"],
        "short_desc": "Dây chuyền đùn 3 lớp đồng thời (bán dẫn trong – XLPE – bán dẫn ngoài) đi qua ống lưu hóa áp suất khí Nitơ dài 80–120m cho cáp trung thế/cao thế.",
        "definition": (
            "Khác với Silane xông hơi theo mẻ, CCV thực hiện đùn 3 lớp đồng thời và lưu hóa khâu mạch trực tiếp bằng nhiệt độ cao (~350–400°C) và áp suất khí Nitơ (10–12 bar) trong đường ống cong dạng dây xích (Catenary) để cách điện tuyệt đối không bọt khí, đạt chuẩn phóng điện cục bộ (PD)."
        ),
        "formula_or_spec": (
            "• Cấu tạo 3 lớp đồng đùn: Inner Semicon + XLPE Insulation + Outer Semicon.\n"
            "• Đặc trưng OE: Chi phí khởi động/dừng máy CỰC ĐẮT (tốn hàng trăm mét cáp phế startup) → Bắt buộc chạy chiến dịch dài (Campaign Run) và TPM ở mức độ tin cậy cao nhất!"
        ),
        "cadivi_application": (
            "Dành cho phân khúc cáp lực trung thế/cao thế trong hệ sinh thái CADIVI. OE tập trung bảo vệ độ khả dụng (TPM, MTBF cao, nguồn điện dự phòng) và gom đơn hàng chạy chiến dịch liên tục nhiều ngày không tắt ống."
        ),
        "cadivi_example": (
            "Ví dụ: Gom các đơn hàng cáp trung thế cùng tiết diện 24kV chạy liên tiếp 5 ngày trên dây chuyền CCV thay vì chia 3 đợt lẻ giúp tiết kiệm ngay ~1,200 mét cáp khởi động phế phẩm!"
        ),
        "related": ["XLPE", "Silane", "TPM", "Heijunka", "IEC 60502"],
        "doc_key": "cable_mfg_machines"
    },
    "DSTA": {
        "term": "DSTA",
        "full_name": "Double Steel Tape Armoring (DSTA / SWA / DATA) — Công Đoạn Giáp Bảo Vệ Cáp Ngầm",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["DSTA", "SWA", "DATA", "Armoring", "giáp băng thép"],
        "case_sensitive": ["DSTA", "SWA", "DATA"],
        "short_desc": "Công đoạn quấn 2 lớp băng thép mạ kẽm (DSTA), băng nhôm (DATA) hoặc bện sợi thép (SWA) quanh lõi ghép để bảo vệ cáp chôn ngầm chống va đập cơ học.",
        "definition": (
            "Đối với cáp điện lực đi ngầm dưới đất, sau khi ghép các lõi pha (Drum Twister) và bọc lớp đệm trong (Inner Sheath), cáp đi qua đầu quấn băng thép 2 lớp chồng mí (DSTA — cho cáp nhiều lõi) "
            "hoặc 2 lớp băng nhôm không từ tính (DATA — cho cáp 1 lõi tránh tổn thất dòng điện xoáy) trước khi đùn lớp vỏ bảo vệ PVC/PE ngoài cùng."
        ),
        "formula_or_spec": (
            "• Ký hiệu CADIVI điển hình: `CXV/DSTA 3×50+1×25-0.6/1kV` (Đồng – XLPE – Giáp 2 băng thép – Vỏ PVC).\n"
            "• Kiểm soát OE: Độ chồng mí băng thép (Overlap) đúng chuẩn IEC, tốc độ thay cuộn băng thép (hàn nối nhanh SMED) và đồng bộ chiều dài 4 lõi trước ghép."
        ),
        "cadivi_application": (
            "Phân khúc cáp công trình trọng điểm của CADIVI Miền Trung. Điểm nóng OE là quản lý chính xác chiều dài 3 pha + 1 trung tính trước ghép lõi (tránh 1 lõi ngắn gây cắt bỏ cả 3 lõi kia = lỗ gấp 4 lần!)."
        ),
        "cadivi_example": (
            "Ví dụ: Gắn máy hàn điểm cầm tay (Spot Welder) ngay tại đầu giáp DSTA và chuẩn bị sẵn cuộn băng thép dự phòng trên trục kép giúp rút thời gian dừng thay băng thép từ 15 phút xuống 4 phút."
        ),
        "related": ["Cut-Length", "IEC 60502", "BOM", "SMED"],
        "doc_key": "cable_mfg_machines"
    },
    "IEC 60228": {
        "term": "IEC 60228",
        "full_name": "IEC 60228 / TCVN 6612 — Tiêu Chuẩn Quốc Tế Về Ruột Dẫn Của Cáp Cách Điện",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["IEC 60228", "TCVN 6612"],
        "case_sensitive": [],
        "short_desc": "Tiêu chuẩn gốc quy định phân cấp ruột dẫn (Class 1, 2, 5, 6) và trần ĐIỆN TRỞ 1 CHIỀU TỐI ĐA ở 20°C (Ω/km) — nền tảng bài toán chống Copper Give-away.",
        "definition": (
            "IEC 60228 (tương đương TCVN 6612) là tiêu chuẩn bắt buộc đối với mọi loại dây & cáp điện CADIVI. "
            "Điểm quan trọng nhất OE phải hiểu: tiêu chuẩn KHÓA CHẶT ĐẶC TÍNH ĐIỆN (Điện trở DC tối đa tại 20°C), chứ không ép đường kính đồng phải to thừa — miễn đạt điện trở trần và cấu trúc tối thiểu là đạt chuẩn!"
        ),
        "formula_or_spec": (
            "• Ví dụ trần điện trở ruột đồng 20°C (IEC 60228):\n"
            "  - 1.5 mm² (Class 1/2): ≤ 12.1 Ω/km | 2.5 mm²: ≤ 7.41 Ω/km | 50 mm² (Class 2): ≤ 0.387 Ω/km.\n"
            "• Quy đổi nhiệt độ đo thực t (°C) về 20°C: R_20 = R_t / [ 1 + 0.00393 × (t - 20) ]."
        ),
        "cadivi_application": (
            "OE kết hợp Phòng Lab thống kê giá trị điện trở thực tế (R_20) của từng mã dây so với trần IEC 60228: nếu R_20 thực tế đang thấp hơn trần tới 4–5% (dư biên an toàn quá lớn) nghĩa là nhà máy đang kéo đồng quá to (Copper Give-away)!"
        ),
        "cadivi_example": (
            "Ví dụ: Dây VC 2.5mm² có trần IEC 60228 là 7.41 Ω/km, nhưng 90 ngày dữ liệu Lab cho R_20 trung bình chỉ 7.05 Ω/km (dư 4.8% biên). Hiệu chỉnh lại đường kính khuôn kéo tinh đưa R_20 về mục tiêu an toàn 7.22 Ω/km (Cpk ≥ 1.5) tiết kiệm hàng tỷ tiền đồng/năm!"
        ),
        "related": ["Copper Give-away", "RBD", "Annealing", "IEC 60502", "Cpk"],
        "doc_key": "cable_mfg_machines"
    },
    "IEC 60502": {
        "term": "IEC 60502",
        "full_name": "IEC 60502 / TCVN 5935 — Tiêu Chuẩn Cáp Điện Lực Cách Điện Dạng Đùn (1 kV – 30 kV)",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["IEC 60502", "TCVN 5935", "TCVN 6610", "IEC 60332"],
        "case_sensitive": [],
        "short_desc": "Bộ tiêu chuẩn quy định chiều dày cách điện/vỏ tối thiểu, thử cao áp, thử lão hóa và thử cháy lan cho cáp điện lực CADIVI.",
        "definition": (
            "IEC 60502-1 (cáp hạ thế 0.6/1 kV – 3 kV) và IEC 60502-2 (cáp trung thế 6–30 kV), cùng TCVN 6610 (dây dân dụng 450/750V) quy định toàn bộ yêu cầu kích thước hình học, điện áp chịu đựng và cơ lý tính vỏ bọc."
        ),
        "formula_or_spec": (
            "• Công thức vàng chiều dày điểm mỏng nhất cách điện (IEC 60502):\n"
            "  t_min ≥ 0.9 × t_nom - 0.1 mm  (Và t_trung_bình ≥ t_nom).\n"
            "• Chiều dày điểm mỏng nhất vỏ bọc ngoài PVC: t_min ≥ 0.85 × t_nom - 0.1 mm."
        ),
        "cadivi_application": (
            "Cơ sở pháp lý kỹ thuật để Chuyên viên OE thiết lập giới hạn LSL/Target trên hệ thống Laser Gauge & biểu đồ SPC tại xưởng đùn, giúp tối ưu giảm nhựa Over-thickness mà vẫn đảm bảo 100% cuộn cáp đạt chuẩn TCVN/IEC."
        ),
        "cadivi_example": (
            "Ví dụ: Cáp CXV 50mm² có chiều dày XLPE danh định t_nom = 1.0 mm → theo IEC 60502, điểm mỏng nhất t_min phải ≥ 0.80 mm. Dùng Laser Gauge giữ độ đồng tâm > 95% cho phép cài t_trung_bình = 1.02 mm thay vì 1.15 mm như trước!"
        ),
        "related": ["Over-thickness", "IEC 60228", "XLPE", "PVC", "Laser Gauge", "SPC"],
        "doc_key": "cable_mfg_machines"
    },
    "STAR": {
        "term": "STAR",
        "full_name": "STAR Interview Method — Cấu Trúc Trả Lời Phỏng Vấn Hành Vi (Situation – Task – Action – Result)",
        "category": "Kỹ Năng Phỏng Vấn & Quản Trị Thay Đổi",
        "aliases": ["STAR"],
        "case_sensitive": ["STAR"],
        "short_desc": "Khung trả lời phỏng vấn sắc bén nhất giúp kể lại các dự án cải tiến/xử lý xung đột mạch lạc trong 90–120 giây với số liệu định lượng thuyết phục.",
        "definition": (
            "STAR giúp ứng viên tránh kể chuyện lan man hay nói lý thuyết suông bằng 4 nấc rõ ràng: "
            "Situation (Bối cảnh/nỗi đau ban đầu 15%), Task (Nhiệm vụ của RIÊNG bạn 15%), Action (Hành động kỹ thuật cụ thể bạn đã làm 50% — phần quan trọng nhất!), Result (Kết quả đo lường được Trước–Sau & bài học 20%)."
        ),
        "formula_or_spec": (
            "• Tỷ lệ thời lượng vàng (2 phút): S (15s) → T (15s) → A (60s — dùng đại từ 'em đã trực tiếp...') → R (30s — con số trung thực!)."
        ),
        "cadivi_application": (
            "Dùng STAR để kể 4 câu chuyện đinh trong CV của bạn trước hội đồng CADIVI: (1) Time Study Canon INEX 60s→30s & đồ gá 1→16 mẫu, (2) Tự động hóa báo cáo Python/VBA 3 ngày→2h & OGP 120p→15p, (3) Quét barcode công đoạn RE7 tại Fujikura, (4) Xử lý phản kháng/xung đột hiện trường."
        ),
        "cadivi_example": (
            "Ví dụ chốt Result chuẩn mực: 'Kết quả là thời gian đo hạng mục giảm 50% từ 60 xuống 30 giây, sức chứa mỗi lượt gá tăng từ 1 lên 16 mẫu (em luôn tách rõ đây là sức chứa lượt gá giúp giảm gá lặp lại, không thổi phồng thành năng suất tăng 16 lần).'"
        ),
        "related": ["OE", "Time Study", "VBA", "Barcode", "ROI"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "SOP": {
        "term": "SOP",
        "full_name": "Standard Operating Procedure & OPL — Quy Trình Thao Tác Chuẩn & Bài Học Một Trang",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["SOP", "OPL", "Visual SOP"],
        "case_sensitive": ["SOP", "OPL"],
        "short_desc": "Tài liệu hướng dẫn từng bước trực quan (có hình ảnh) khóa chặt thành quả cải tiến để 3 ca thao tác đồng nhất 100%, không quay lại thói quen cũ.",
        "definition": (
            "Không có chuẩn hóa (SOP) thì mọi dự án Kaizen/SMED sẽ bị 'trượt dốc' quay về cách làm cũ chỉ sau 1 tháng. "
            "SOP chuẩn Lean là bản hướng dẫn ngắn gọn, nhiều hình ảnh Đúng/Sai treo ngay tại máy; OPL (One-Point Lesson) là tờ A4 dạy đúng 1 điểm kỹ thuật cốt lõi trong 5 phút đầu ca."
        ),
        "formula_or_spec": (
            "• Quy tắc viết SOP hiện trường: 70% hình ảnh chụp thực tế + mũi tên chỉ điểm kiểm tra, 30% chữ ngắn gọn rõ số liệu (nhiệt độ, lực siết, tốc độ)."
        ),
        "cadivi_application": (
            "Ban hành Visual SOP tại CADIVI cho: quy trình đổi màu SMED máy đùn (kèm sơ đồ 2 người song song), quy trình hàn đối đầu đồng rod, quy trình sấy hạt nhựa PVC/XLPE và bảng kiểm Jishu Hozen 5 phút."
        ),
        "cadivi_example": (
            "Ví dụ: Treo bảng OPL 1 trang chụp hình 'Cách kiểm tra độ sạch đầu Chày-Cối & gắn vòng nhiệt đúng chuẩn' ngay cạnh tủ sấy SMED giúp công nhân Ca 3 làm đúng 100% như Ca 1."
        ),
        "related": ["Time Study", "TWI", "SMED", "5S", "PDCA"],
        "doc_key": "smed"
    },
    "KPI": {
        "term": "KPI",
        "full_name": "Key Performance Indicator — Chỉ Số Đo Lường Hiệu Suất Trọng Yếu (Hệ Thống SQDC)",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["KPI", "SQDC"],
        "case_sensitive": ["KPI", "SQDC"],
        "short_desc": "Hệ thống thước đo định lượng mục tiêu vận hành theo 4 trụ cột SQDC (An toàn – Chất lượng – Giao hàng – Chi phí) giúp biến chiến lược thành hành động hàng ngày.",
        "definition": (
            "KPI là các con số cốt lõi phản ánh sức khỏe thực sự của nhà máy. Sai lầm phổ biến là đặt KPI cục bộ mâu thuẫn nhau (vd: thưởng sản lượng tấn cho xưởng kéo khiến xưởng kéo chạy thừa tạo núi WIP!). "
            "KPI chuẩn OE phải cân bằng đủ 4 góc SQDC: Safety – Quality – Delivery – Cost."
        ),
        "formula_or_spec": (
            "• Bộ KPI vàng của OE Nhà máy Cáp: OEE (%), OLE (%), Breaks/Ton (Kéo), Spark/10km (Đùn), Bare vs Insulated Copper Scrap (%), BOM Variance (%), Changeover Time (phút), On-Time Delivery (%)."
        ),
        "cadivi_application": (
            "Thiết lập bảng KPI trực quan Tier 1–2–3 tại CADIVI Miền Trung có ngưỡng Xanh (Đạt) / Đỏ (Chưa đạt) rõ ràng, gắn trực tiếp với hành động khắc phục PDCA."
        ),
        "cadivi_example": (
            "Ví dụ: Đổi KPI xưởng Bện từ 'Tổng tấn bện/ca' sang 'Tỷ lệ giao rulo đúng lịch máy Đùn (Schedule Adherence ≥ 95%)' giúp giảm ngay 50% rulo WIP chất đống mà máy đùn không bao giờ đói hàng."
        ),
        "related": ["OEE", "OLE", "OE", "Power BI", "PDCA"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "Excel": {
        "term": "Excel",
        "full_name": "Microsoft Excel Nâng Cao (Power Query, Pivot Table, Solver, Data Model, VBA)",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["Excel", "Pivot Table", "Excel Solver"],
        "case_sensitive": [],
        "short_desc": "Công cụ phân tích phổ cập nhất tại nhà máy: từ bảng tính nhật ký ca, gom dữ liệu Power Query, Pareto 80/20 đến tối ưu cắt rulo bằng Solver.",
        "definition": (
            "Trong môi trường sản xuất thực tế, Excel nâng cao (kết hợp Power Query, Pivot Table, XLOOKUP, Data Model và Solver/VBA) là vũ khí nhanh nhất và linh hoạt nhất để Chuyên viên OE xây dựng công cụ theo dõi OEE, OLE, RCCP và BOM Variance ngay từ tuần đầu tiên mà không phải chờ đầu tư phần mềm."
        ),
        "formula_or_spec": (
            "• Quy tắc Tidy Data: Dữ liệu thô 1 chiều không Merge Cells → Power Query làm sạch → Data Model tính DAX → Pivot Chart / Pareto."
        ),
        "cadivi_application": (
            "Ứng dụng mọi ngày tại CADIVI: gom nhật ký ca 4 phân xưởng bằng Power Query, chạy Excel Solver giải bài toán ghép cắt chiều dài rulo (Cut-Length), tính bảng RCCP năng lực tháng và xuất báo cáo PDF tự động."
        ),
        "cadivi_example": (
            "Ví dụ: Thiết kế file Excel Template tính RCCP & OEE tổng hợp kết nối Power Query giúp rút thời gian tổng hợp báo cáo tuần của toàn nhà máy từ 4 giờ xuống 2 phút!"
        ),
        "related": ["Power Query", "VBA", "Power BI", "Cut-Length", "RCCP"],
        "doc_key": "excel_mfg"
    },
    "Python": {
        "term": "Python",
        "full_name": "Python Cho Kỹ Sư OE (Pandas, OpenPyXL, SciPy, PuLP — Tự Động Hóa & Phân Tích Dữ Liệu Lớn)",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["Python", "Pandas"],
        "case_sensitive": [],
        "short_desc": "Ngôn ngữ lập trình giúp tự động xử lý hàng trăm file log máy đo/nhật ký ca, chạy kiểm định thống kê t-test/ANOVA và giải bài toán tối ưu cắt rulo trong vài giây.",
        "definition": (
            "Khi dữ liệu sản xuất phình to hàng trăm nghìn dòng hoặc nằm rải rác trong hàng trăm file xuất thô từ máy đo Lab/PLC/ERP, Python (`pandas`, `openpyxl`, `scipy.stats`, `pulp`) giúp tự động hóa 100% quy trình ETL, tính Cpk, kiểm định t-test và xuất báo cáo chuẩn không lỗi nhập tay."
        ),
        "formula_or_spec": (
            "• Bộ thư viện vàng OE: pandas (làm sạch & tổng hợp) | openpyxl (xuất Excel đẹp) | scipy.stats (t-test, ANOVA, Cpk) | pulp (tối ưu Cut-Length & lập lịch)."
        ),
        "cadivi_application": (
            "Lợi thế cạnh tranh hiếm có trong CV của bạn so với ứng viên OE thuần truyền thống! Tại CADIVI, bạn dùng Python gom log Laser Gauge/Lab, tự động phát hiện bất thường SPC/BOM và giải bài toán Cutting Stock tiết kiệm mẩu cáp thừa."
        ),
        "cadivi_example": (
            "Ví dụ: Script Python đọc tự động 300 file kết quả đo phòng Lab trong 4 giây, tự tính điện trở quy về 20°C, vẽ biểu đồ Cpk và xuất bảng cảnh báo mã dây nào đang dư đồng Copper Give-away > 1.5%."
        ),
        "related": ["VBA", "Excel", "Power BI", "Minitab", "Cut-Length"],
        "doc_key": "excel_mfg"
    },
    "DOE": {
        "term": "DOE",
        "full_name": "Design of Experiments — Thiết Kế Thí Nghiệm Tìm Cửa Sổ Thông Số Vận Hành Tối Ưu",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["DOE", "Design of Experiments"],
        "case_sensitive": ["DOE"],
        "short_desc": "Phương pháp thí nghiệm khoa học thay đổi đồng thời nhiều biến đầu vào (nhiệt độ, tốc độ vít, nước làm mát) để tìm tổ hợp thông số tốt nhất và hiệu ứng tương tác.",
        "definition": (
            "Cách thử truyền thống 'mỗi lần chỉ chỉnh 1 biến' (OFAT) vừa tốn rất nhiều phế phẩm thử nghiệm vừa bỏ sót sự tương tác giữa các biến (vd: tăng tốc độ đùn phải đi kèm tăng nhiệt vùng đầu và giảm nhiệt nước làm mát). "
            "DOE (Full/Fractional Factorial, Response Surface trên Minitab) chỉ cần chạy đúng 8–16 tổ hợp thử nghiệm chuẩn để tìm chính xác 'điểm ngọt' vận hành."
        ),
        "formula_or_spec": (
            "• Thiết kế 2^k Factorial (k=3 yếu tố, mỗi yếu tố 2 mức Thấp/Cao) → Chỉ cần 8 lần chạy thử đã đánh giá đủ cả 3 tác động chính lẫn 4 tương tác cặp!"
        ),
        "cadivi_application": (
            "Tìm cửa sổ thông số tối ưu (Optimal Operating Window) trên máy đùn cáp nhựa LSZH hoặc XLPE để cân bằng đồng thời tốc độ m/phút cao nhất, bề mặt bóng đẹp nhất và 0 lỗi Spark."
        ),
        "cadivi_example": (
            "Ví dụ: Chạy DOE 2^3 trên máy đùn dây VC 2.5 (Tốc độ 320 vs 360 m/phút × Nhiệt đầu 165 vs 175°C × Nước mát 22 vs 32°C) → Tìm ra tổ hợp tối ưu [355 m/phút, 170°C, 22°C] tăng +15% tốc độ mà lỗi Spark < 0.2/10km!"
        ),
        "related": ["Minitab", "DMAIC", "Six Sigma", "Extruder", "ANOVA"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "Six Big Losses": {
        "term": "Six Big Losses",
        "full_name": "Six Big Losses — 6 Tổn Thất Lớn Của Thiết Bị (Gốc Rễ Phân Tích OEE & TPM)",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Six Big Losses", "6 tổn thất lớn", "6 Tổn Thất Lớn"],
        "case_sensitive": [],
        "short_desc": "6 nhóm nguyên nhân ăn mòn OEE: (1) Hỏng máy, (2) Đổi mã/Setup, (3) Vi dừng <5p, (4) Giảm tốc độ, (5) Phế khởi động, (6) Phế khi đang chạy.",
        "definition": (
            "Hệ thống phân loại chuẩn quốc tế chia toàn bộ thời gian lãng phí của máy móc thành 6 giỏ rõ ràng tương ứng với 3 trụ cột OEE (2 cho Availability, 2 cho Performance, 2 cho Quality), giúp đội OE lập danh mục mã dừng máy (Downtime Reason Codes) khoa học."
        ),
        "formula_or_spec": (
            "• Availability: (1) Equipment Breakdown + (2) Setup & Adjustments (SMED)\n"
            "• Performance: (3) Minor Stoppages (<5p) + (4) Reduced Speed\n"
            "• Quality: (5) Startup Rejects + (6) Production Defects."
        ),
        "cadivi_application": (
            "Chuẩn hóa danh mục 6 tổn thất lớn đặc thù cho sổ ca & MES tại CADIVI: (1) Hỏng cơ/điện/đứt dây, (2) Đổi màu/Chày-Cối/Thay rulo, (3) Kẹt dẫn hướng/Vi dừng, (4) Chạy giảm tốc do nước nóng/rung rulo, (5) Phế đầu ca & xả purge, (6) Lỗi Spark/Lệch tâm."
        ),
        "cadivi_example": (
            "Ví dụ: Gắn 6 mã nhóm tổn thất vào báo cáo máy đùn giúp Giám đốc nhìn thấy ngay 60% tổn thất nằm ở nhóm (2) Đổi mã và nhóm (4) Giảm tốc độ, thay vì cứ nghĩ do hỏng máy!"
        ),
        "related": ["OEE", "TPM", "SMED", "Pareto"],
        "doc_key": "oee"
    },
    "TIMWOOD": {
        "term": "TIMWOOD",
        "full_name": "TIMWOOD / TIMWOODS — 7 (+1) Loại Lãng Phí Kinh Điển Trong Sản Xuất Tinh Gọn (Muda)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["TIMWOOD", "TIMWOODS", "Muda", "7 lãng phí", "8 lãng phí"],
        "case_sensitive": ["TIMWOOD", "TIMWOODS"],
        "short_desc": "Từ khóa ghi nhớ 8 lãng phí sản xuất: Transport, Inventory, Motion, Waiting, Overproduction (#1 nguy hiểm nhất), Overprocessing, Defects và Skills Unused.",
        "definition": (
            "Muda (lãng phí) là mọi hoạt động tiêu tốn tiền bạc, điện năng, nhân lực nhưng không làm tăng giá trị sản phẩm dưới góc nhìn khách hàng. "
            "Trong đó Overproduction (Sản xuất thừa) nguy hiểm nhất vì nó sinh ra và che giấu toàn bộ 6 loại lãng phí còn lại."
        ),
        "formula_or_spec": (
            "• T (Vận chuyển) | I (Tồn kho WIP) | M (Thao tác thừa) | W (Chờ đợi) | O (SX thừa) | O (Gia công thừa) | D (Phế phẩm) | S (Lãng phí trí tuệ công nhân)."
        ),
        "cadivi_application": (
            "Dùng làm kính lúp khi đi Genba Walk ở CADIVI: soi Overprocessing (bọc dư nhựa Over-thickness & kéo dư đồng Copper Give-away), Inventory (núi rulo WIP), Waiting (máy đùn chờ xe nâng/chờ QC), Defects (phế đồng dính nhựa)."
        ),
        "cadivi_example": (
            "Ví dụ buổi đi Genba Waste Walk 60 phút tại khu Đùn & Đóng gói CADIVI có thể chụp ảnh nhận diện ngay 12 điểm TIMWOOD cụ thể để đưa vào kế hoạch Kaizen tháng."
        ),
        "related": ["Lean", "5S", "VSM", "Over-thickness", "Copper Give-away"],
        "doc_key": "lean_muda"
    },
    "One-Piece Flow": {
        "term": "One-Piece Flow",
        "full_name": "One-Piece Flow (Continuous Flow) — Dòng Chảy Liên Tục Một Sản Phẩm",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["One-Piece Flow", "One-piece flow", "Luồng một sản phẩm", "Luồng 1 sản phẩm"],
        "case_sensitive": [],
        "short_desc": "Chế độ sản xuất từng đơn vị/cuộn liên tục chuyển thẳng sang trạm kế tiếp không chất đống theo lô lớn, giúp rút Lead Time và lộ lỗi tức thì.",
        "definition": (
            "Trái ngược với sản xuất theo lô lớn (Batch & Queue — làm xong cả 500 cuộn mới đẩy sang bước sau), One-Piece Flow chuyển sản phẩm đi ngay sau khi hoàn tất 1 bước. "
            "Nếu có lỗi xảy ra, trạm sau phát hiện ngay ở sản phẩm đầu tiên thay vì hỏng cả lô 500 chiếc!"
        ),
        "formula_or_spec": (
            "• 4 điều kiện tiên quyết: (1) SMED đổi mã cực nhanh, (2) TPM máy tin cậy cao, (3) Poka-Yoke chất lượng tại nguồn, (4) Cân bằng chuyền gần Takt Time."
        ),
        "cadivi_application": (
            "Ứng dụng trực tiếp ở dây chuyền liên hoàn 'Kéo + Ủ trực tuyến (In-line Annealer)' và dây chuyền đóng gói dây dân dụng 'Máy cuộn tự động → Dán tem → Bọc màng co → Đóng thùng' tại CADIVI."
        ),
        "cadivi_example": (
            "Ví dụ: Kết nối máy cuộn 100m thẳng sang băng tải máy bọc màng co theo luồng 1 cuộn (bỏ xe đẩy chất đống 50 cuộn trung gian) giúp phát hiện lỗi chữ in phun ngay ở cuộn thứ 1 thay vì lỗi cả 50 cuộn!"
        ),
        "related": ["Lean", "WIP", "SMED", "AutoCAD", "FIFO"],
        "doc_key": "autocad_layout"
    },
    "FIFO": {
        "term": "FIFO",
        "full_name": "First-In, First-Out — Nguyên Tắc Nhập Trước Xuất Trước (FIFO Lane)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["FIFO"],
        "case_sensitive": ["FIFO"],
        "short_desc": "Làn lưu trữ có sức chứa giới hạn đảm bảo rulo đồng/hạt nhựa sản xuất hoặc nhập kho trước PHẢI được dùng trước, tránh oxy hóa đồng & tồn kho chết.",
        "definition": (
            "FIFO Lane là làn đệm vật lý (kẻ vạch hoặc giá trượt con lăn) có 1 đầu vào và 1 đầu ra riêng biệt cùng giới hạn sức chứa tối đa (vd: tối đa 5 rulo). "
            "Nó ngăn chặn tình trạng 'rulo mới làm đặt ngoài cùng lấy dùng trước, rulo cũ nằm sâu trong góc bị oxy hóa đen đồng suốt 2 tháng'!"
        ),
        "formula_or_spec": (
            "• Giới hạn vật lý FIFO Lane: Khi làn đầy Max → Công đoạn trước DỪNG đẩy hàng (chống sản xuất thừa & chống Blocking)."
        ),
        "cadivi_application": (
            "Cực kỳ thiết yếu tại CADIVI cho (1) Kho hạt nhựa XLPE Silane (có hạn sử dụng chống hút ẩm sớm!), (2) Kho rulo sợi đồng sau ủ (để lâu dễ oxy hóa xỉn màu khó bám nhựa) và (3) Kho thành phẩm xuất hàng."
        ),
        "cadivi_example": (
            "Ví dụ: Thiết kế làn FIFO 2 lối (1 đầu đẩy vào, 1 đầu lấy ra) cho kho hạt XLPE Silane kết hợp nhãn ngày nhập giúp loại bỏ 100% lỗi nhựa quá hạn lưu kho bị khâu mạch sớm trong nòng đùn!"
        ),
        "related": ["Kanban", "WIP", "Barcode", "XLPE", "Silane"],
        "doc_key": "lean_muda"
    },
    "Capstan": {
        "term": "Capstan",
        "full_name": "Capstan & Caterpillar Haul-off — Bộ Kéo Cáp & Đồng Bộ Tốc Độ Tuyến Tính",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Capstan", "Caterpillar"],
        "case_sensitive": [],
        "short_desc": "Cụm kéo quyết định tốc độ tuyến tính (m/phút), độ căng dây và đường kính lớp nhựa bọc của toàn dây chuyền đùn/bện cáp.",
        "definition": (
            "Capstan (dạng bánh quay cho dây nhỏ tốc độ cao) hoặc Caterpillar (dạng băng xích kẹp 2 mặt cho cáp lực tiết diện lớn không bị móp vỏ) tạo lực kéo ổn định rút cáp xuyên qua đầu đùn và máng nước làm mát. "
            "Khi tốc độ trục vít giữ cố định: tăng tốc độ Capstan → lớp nhựa mỏng đi; giảm tốc độ Capstan → lớp nhựa dày lên."
        ),
        "formula_or_spec": (
            "• Tích hợp Encoder đo chiều dài mét và nhận tín hiệu hồi tiếp tự động từ Laser Gauge (Closed-loop Control)."
        ),
        "cadivi_application": (
            "Tại CADIVI, OE kiểm tra trượt đai cao su Caterpillar / bánh Capstan (gây sai số đếm mét 1–2% dẫn tới thiếu chiều dài cuộn!) và kết nối đồng bộ Laser Gauge → Capstan để giữ dung sai đường kính ±0.01 mm."
        ),
        "cadivi_example": (
            "Ví dụ: Thay đệm cao su mòn trên Caterpillar dây chuyền bọc vỏ CXV và hiệu chuẩn Encoder định kỳ hàng tháng giúp xóa sai số trượt mét 1.4%, chấm dứt lỗi cắt thiếu hụt đơn rulo 1,000m."
        ),
        "related": ["Extruder", "Laser Gauge", "Cut-Length", "Over-thickness"],
        "doc_key": "cable_mfg_machines"
    },
    "Butt Welder": {
        "term": "Butt Welder",
        "full_name": "Cold/Flash Butt Welder — Máy Hàn Đối Đầu Nối Sợi Đồng & Nhôm",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Butt Welder", "Butt Welding", "hàn đối đầu"],
        "case_sensitive": [],
        "short_desc": "Thiết bị hàn nối đầu cuộn đồng rod mới với đuôi cuộn cũ (hàn điện trở nóng chảy hoặc hàn ép nguội) giúp máy kéo & máy đùn chạy liên tục không dừng.",
        "definition": (
            "Butt Welder ép chặt 2 đầu sợi đồng/nhôm và phóng dòng điện lớn (hoặc ép nguội áp suất cao với sợi mảnh) để nối thành một sợi liên tục, sau đó mài phẳng bavia mối hàn và ủ nhẹ tại chỗ để mối hàn đủ dẻo chui lọt qua toàn bộ dãy khuôn kéo."
        ),
        "formula_or_spec": (
            "• Yêu cầu sống còn: Độ bền kéo mối hàn đạt ≥ 85–90% thân sợi và không có vết cháy/bavia → Nếu hàn lỗi, 100% sẽ bị đứt sợi ngay khi chui vào khuôn kéo hoặc đầu đùn!"
        ),
        "cadivi_application": (
            "Kết hợp với Dual Pay-off (nhả dây kép) và Accumulator (bộ tích dây) tại CADIVI để triệt tiêu thời gian dừng thay rulo trên máy kéo RBD và máy đùn bọc dây dân dụng."
        ),
        "cadivi_example": (
            "Ví dụ: Chuẩn hóa SOP hàn đối đầu + kiểm tra lực uốn thử mối hàn tại xưởng kéo RBD giảm 80% sự cố đứt tại mối hàn, cứu lại 40 phút dừng máy xỏ khuôn mỗi ngày!"
        ),
        "related": ["RBD", "SMED", "Extruder", "TWI"],
        "doc_key": "cable_mfg_machines"
    },
    "Multi-wire": {
        "term": "Multi-wire",
        "full_name": "Multi-Wire Drawing Machine — Máy Kéo Tinh Nhiều Sợi Song Song (8 – 24 Sợi)",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Multi-wire", "Multi-Wire", "kéo nhiều sợi", "kéo tinh"],
        "case_sensitive": [],
        "short_desc": "Máy kéo hiện đại kéo đồng thời 8, 16 hoặc 24 sợi đồng mảnh (Ø 0.15–0.50 mm) song song ở tốc độ 20–35 m/s, năng suất gấp chục lần máy kéo đơn.",
        "definition": (
            "Máy kéo nhiều sợi tích hợp bộ ủ điện trở đồng bộ cho cả 16–24 sợi chạy song song, tạo ra rulo nhiều sợi đồng đều lực căng cung cấp thẳng cho máy bện Buncher làm dây mềm dân dụng VCm/VCmd."
        ),
        "formula_or_spec": (
            "• Nỗi đau OEE lớn nhất: Chỉ cần ĐỨT 1 TRONG 16 SỢI là toàn bộ 15 sợi còn lại phải dừng máy theo → Quản lý đồng bộ tuổi thọ cả dàn 16 bộ khuôn PCD là tối quan trọng!"
        ),
        "cadivi_application": (
            "Tại CADIVI, OE áp dụng chiến lược thay khuôn đồng bộ theo nhóm (Group Die Replacement) thay vì hỏng sợi nào thay sợi đó, kết hợp kiểm soát lọc mịn bể nhũ tương để giảm tối đa số lần dừng xỏ lại 16 sợi."
        ),
        "cadivi_example": (
            "Ví dụ: Chuyển từ 'đứt sợi nào thay khuôn sợi đó' sang thay trọn bộ khuôn Multi-wire theo chu kỳ PM 15 tấn đồng giúp giảm tần suất dừng máy từ 6 lần/ca xuống 1.5 lần/ca, đẩy OEE máy kéo tinh từ 64% lên 82%!"
        ),
        "related": ["RBD", "Annealing", "Buncher", "TPM", "OEE"],
        "doc_key": "cable_mfg_machines"
    },
    "Drum Twister": {
        "term": "Drum Twister",
        "full_name": "Drum Twister & Laying-Up Machine — Máy Ghép Lõi Cáp Nhiều Pha",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Drum Twister", "Laying-up", "ghép lõi"],
        "case_sensitive": [],
        "short_desc": "Máy chập xoắn 2, 3 hoặc 4 lõi pha cách điện (kèm dây độn PP và băng quấn định hình) thành cụm lõi cáp tròn đều trước khi giáp thép và bọc vỏ ngoài.",
        "definition": (
            "Drum Twister sử dụng rulo thu lớn vừa quay tròn thu cáp vừa tự xoay trục để tạo bước xoắn ghép các lõi pha cáp lực (vd: 3 lõi pha Đỏ–Vàng–Xanh + 1 lõi trung tính Đen của cáp CXV 3x50+1x25) với tốc độ cao hơn hẳn máy ghép lồng kiểu cũ."
        ),
        "formula_or_spec": (
            "• Quy tắc sống còn: Chiều dài 4 rulo lõi đầu vào PHẢI ĐỒNG BỘ chênh lệch < 0.5% — nếu 1 rulo lõi ngắn hơn 40m thì phải cắt bỏ 40m ở CẢ 3 LÕI KIA (thiệt hại × 4)!"
        ),
        "cadivi_application": (
            "OE CADIVI siết đồng bộ chiều dài từ công đoạn đùn lõi (hiệu chuẩn Encoder đo mét) và áp dụng SMED nạp 4 rulo lõi song song bằng cầu trục."
        ),
        "cadivi_example": (
            "Ví dụ: Lệch chiều dài giữa 3 lõi pha trước ghép trung bình 25m/mẻ (tốn 75m lõi đồng bọc XLPE phế/mẻ!). Hiệu chuẩn lại Encoder 3 máy đùn lõi đưa sai lệch về < 4m/mẻ, tiết kiệm > 80 triệu/tháng."
        ),
        "related": ["DSTA", "Cut-Length", "XLPE", "BOM"],
        "doc_key": "cable_mfg_machines"
    },
    "Kelvin Bridge": {
        "term": "Kelvin Bridge",
        "full_name": "Kelvin Double Bridge / Micro-Ohmmeter — Cầu Đo Điện Trở Ruột Dẫn Chính Xác Cao",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Kelvin Bridge", "Micro-ohmmeter", "cầu đo điện trở"],
        "case_sensitive": [],
        "short_desc": "Thiết bị phòng Lab QA/QC đo điện trở 1 chiều rất nhỏ (đến micro-ohm) của đoạn mẫu ruột dẫn 1 mét, quy đổi về 20°C đối chiếu chuẩn IEC 60228.",
        "definition": (
            "Ruột dẫn đồng tiết diện lớn (50–300 mm²) có điện trở cực nhỏ (vài trăm micro-ohm/mét) nên đồng hồ VOM thường không thể đo được vì sai số điện trở tiếp xúc kẹp đo. "
            "Cầu Kelvin dùng kỹ thuật đo 4 dây (4-wire sensing) loại bỏ hoàn toàn điện trở dây đo và tiếp xúc."
        ),
        "formula_or_spec": (
            "• Yêu cầu môi trường phòng Lab: Ổn định nhiệt độ phòng 20–25°C và để mẫu đồng cân bằng nhiệt ít nhất 1–2 giờ trước khi đo; quy đổi chính xác về R_20 theo hệ số nhiệt đồng 0.00393 /°C."
        ),
        "cadivi_application": (
            "OE CADIVI sử dụng dữ liệu đo cầu Kelvin hàng ngày từ Phòng Lab không chỉ để kiểm duyệt xuất xưởng, mà làm nguồn dữ liệu SPC tối ưu giảm Copper Give-away (kéo sát biên an toàn điện trở IEC 60228)."
        ),
        "cadivi_example": (
            "Ví dụ: Dùng Python tự động trích xuất dữ liệu cầu Kelvin của 200 lô dây dân dụng trong quý phát hiện độ tinh khiết đồng nhập rất tốt (101.2% IACS), cho phép hạ nhẹ mục tiêu đường kính khuôn kéo giảm 0.6% đồng tiêu hao mà 100% vẫn đạt chuẩn!"
        ),
        "related": ["IEC 60228", "Copper Give-away", "Annealing", "Gage R&R"],
        "doc_key": "cable_mfg_machines"
    },
    "Hot Set Test": {
        "term": "Hot Set Test",
        "full_name": "Hot Set Test (IEC 60811-507) — Phép Thử Biến Dạng Nhiệt Kiểm Tra Độ Khâu Mạch XLPE",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Hot Set Test", "Hot Set"],
        "case_sensitive": [],
        "short_desc": "Phép thử phòng Lab treo quả nặng lên mẫu nhựa XLPE trong tủ nhiệt 200°C suốt 15 phút để kiểm chứng quá trình lưu hóa Silane/CCV đã đạt chuẩn hay chưa.",
        "definition": (
            "Nếu nhựa XLPE chưa khâu mạch đủ (xông hơi Sauna chưa đủ giờ hoặc thiếu xúc tác), khi gặp nhiệt độ 200°C mẫu sẽ giãn dài quá mức hoặc đứt rơi ngay. "
            "Hot Set Test là 'giấy thông hành bắt buộc' trước khi cho phép đưa các rulo lõi XLPE sang công đoạn ghép lõi và bọc vỏ."
        ),
        "formula_or_spec": (
            "• Điều kiện thử chuẩn IEC 60502: 200°C ± 3°C, tải trọng 20 N/cm², thời gian 15 phút.\n"
            "• Ngưỡng ĐẠT: Độ giãn dài dưới tải ≤ 175% | Độ giãn dư sau khi tháo tải & làm nguội ≤ 15%."
        ),
        "cadivi_application": (
            "Liên quan trực tiếp đến Lead Time tại CADIVI: nếu mẫu Hot Set không đạt phải đưa cả mẻ rulo vào xông Sauna lại thêm 6–8 tiếng, gây trễ toàn bộ lệnh ghép lõi phía sau → OE kiểm soát chặt nhiệt độ/độ ẩm bể Sauna & tỷ lệ pha trộn xúc tác."
        ),
        "cadivi_example": (
            "Ví dụ: Theo dõi kết quả Hot Set Test giúp OE tối ưu thời gian xông Sauna từ 10 giờ (dư thừa theo thói quen cũ) xuống 7 giờ chuẩn hóa (vẫn đạt độ giãn < 80%), tăng +42% năng lực thông qua của bể xông mà không tốn tiền mở rộng bể!"
        ),
        "related": ["XLPE", "Silane", "CCV", "IEC 60502", "Lead Time"],
        "doc_key": "cable_mfg_machines"
    },
    "Hopper Dryer": {
        "term": "Hopper Dryer",
        "full_name": "Hopper Dryer — Phễu Sấy Hút Ẩm Hạt Nhựa Đùn Bọc Cáp",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Hopper Dryer", "máy sấy hạt nhựa", "sấy hạt nhựa"],
        "case_sensitive": [],
        "short_desc": "Thiết bị sấy khô hơi ẩm bám trên hạt nhựa PVC/LSZH/XLPE trước khi nạp vào trục vít máy đùn — chốt chặn số 1 ngăn lỗi bọt khí thủng Spark Tester.",
        "definition": (
            "Khí hậu miền Trung (Đà Nẵng) có độ ẩm không khí rất cao, đặc biệt mùa mưa. Hạt nhựa hút ẩm khi đi vào nòng đùn 170°C sẽ bốc hơi nước tức thì tạo hàng nghìn lỗ mọt khí siêu nhỏ làm thủng cách điện khi qua Spark Tester và rỗ bề mặt vỏ."
        ),
        "formula_or_spec": (
            "• Chế độ sấy phổ biến: Nhựa PVC (70–80°C trong 45–60 phút) | Nhựa LSZH (70–75°C có hút ẩm Dehumidifier).\n"
            "• Ứng dụng SMED: Dùng phễu sấy di động bên ngoài sấy sẵn màu mới để chuyển sang máy đùn là chạy ngay (0 phút chờ sấy!)."
        ),
        "cadivi_application": (
            "Giải pháp chi phí cực thấp nhưng triệt tiêu trực tiếp hai vấn đề đau đầu nhất của xưởng đùn CADIVI Miền Trung: lỗi Spark do bọt khí mùa ẩm và thời gian chờ sấy nhựa khi đổi màu SMED."
        ),
        "cadivi_example": (
            "Ví dụ: Gắn đồng hồ hẹn giờ tự khởi động Hopper Dryer trước ca 45 phút + khóa liên động nhiệt độ giảm 65% lỗi Spark bọt khí vào ca đêm mùa mưa."
        ),
        "related": ["Extruder", "Spark Tester", "PVC", "LSZH", "SMED"],
        "doc_key": "cable_mfg_machines"
    },
    "SEC": {
        "term": "SEC",
        "full_name": "Specific Energy Consumption (kWh / Tấn) — Chỉ Số Cường Độ Tiêu Thụ Điện Năng Sản Xuất",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["SEC", "kWh/tấn", "Idle Heating"],
        "case_sensitive": ["SEC"],
        "short_desc": "Số kWh điện tiêu tốn để sản xuất ra 1 tấn đồng/cáp thành phẩm — thước đo tối ưu chi phí năng lượng Overhead cực lớn trong nhà máy dây cáp điện.",
        "definition": (
            "Nhà máy dây cáp điện tiêu thụ điện năng rất lớn cho động cơ kéo thô (200–500 kW), dòng điện ủ đồng, điện trở nòng đùn (50–150 kW/máy), lò ủ chuông và hệ thống Chiller/máy nén khí. "
            "Chỉ số SEC (kWh/tấn) và tỷ lệ phụ tải giờ cao điểm/thấp điểm quyết định trực tiếp sức cạnh tranh giá thành."
        ),
        "formula_or_spec": (
            "• SEC = Tổng Điện Năng Tiêu Thụ Phân Xưởng (kWh) / Tổng Sản Lượng Đạt Chuẩn (Tấn).\n"
            "• Giá điện sản xuất giờ cao điểm ≈ 2.5 – 3.0 × Giá điện giờ thấp điểm (22:00 – 04:00)!"
        ),
        "cadivi_application": (
            "OE CADIVI kéo giảm SEC và hóa đơn tiền điện qua 4 mũi nhọn: (1) Xóa Idle Heating (đùn bật nhiệt chờ rulo/đổi mã), (2) Bọc áo cách nhiệt nòng Barrel (-15–25% điện nhiệt), (3) Dịch chuyển lò ủ/RBD nặng sang giờ thấp điểm, (4) Xử lý rò rỉ khí nén & nâng OEE."
        ),
        "cadivi_example": (
            "Ví dụ: Gắn áo bảo ôn cách nhiệt cho 4 nòng máy đùn lớn + xếp lịch chạy lò ủ chuông khung 22:00–04:00 giúp giảm SEC 9% và tiết kiệm hơn 120 triệu VNĐ tiền điện/tháng!"
        ),
        "related": ["OEE", "Extruder", "RBD", "Annealing", "ROI"],
        "doc_key": "cable_cost_capacity"
    },

    # =================================================================
    # NHÓM 7: HOẠCH ĐỊNH S&OP/MPS/MRP/CRP, TỒN KHO, FPY/RTY, LOTO/ISO, NHÔM/FR & STANDARD COST
    # =================================================================
    "S&OP": {
        "term": "S&OP",
        "full_name": "Sales & Operations Planning — Hoạch Định Bán Hàng & Vận Hành Tổng Thể",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["S&OP", "Sales & Operations Planning"],
        "case_sensitive": ["S&OP"],
        "short_desc": "Quy trình họp cân đối hàng tháng giữa Kinh doanh – Kế hoạch – Sản xuất – Tài chính tầm nhìn 3–18 tháng theo họ sản phẩm (tấn đồng/nhôm).",
        "definition": (
            "S&OP là tầng hoạch định cao nhất giúp đồng bộ hóa dự báo đơn hàng thương mại với năng lực thực tế của nhà máy, ngân sách mua đồng/nhựa và kế hoạch tuyển nhân lực/mở ca trước nhiều tháng."
        ),
        "formula_or_spec": (
            "• Chu kỳ 5 bước hàng tháng: Thu thập dữ liệu → Kế hoạch Nhu cầu (Demand) → Kế hoạch Cung ứng/Năng lực (Supply) → Họp giải quyết lệch tải (Pre-S&OP) → Chốt với Ban Giám đốc."
        ),
        "cadivi_application": (
            "Tại CADIVI Miền Trung, Chuyên viên OE cung cấp năng lực khả dụng thực tế (đã nhân OEE lịch sử) theo từng nhóm dây dân dụng/cáp lực/cáp nhôm cho cuộc họp S&OP để dự báo sớm mùa cao điểm."
        ),
        "cadivi_example": (
            "Ví dụ: Nhờ dự báo S&OP quý III tăng 30% đơn hàng cáp lực CXV, nhà máy chủ động tuyển và đào tạo TWI trước 6 tuần để mở thêm ca 3 máy đùn thay vì nước đến chân mới cuống."
        ),
        "related": ["MPS", "MRP", "RCCP", "CRP", "Hoshin Kanri"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "MPS": {
        "term": "MPS",
        "full_name": "Master Production Schedule — Lịch Trình Sản Xuất Tổng Thể",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["MPS", "Master Production Schedule"],
        "case_sensitive": ["MPS"],
        "short_desc": "Kế hoạch chi tiết theo từng mã cáp (SKU) và từng tuần: sản xuất mã gì, bao nhiêu km và hoàn thành tuần nào (tầm nhìn 4–12 tuần).",
        "definition": (
            "MPS chuyển hóa kế hoạch tổng quát theo tấn từ S&OP thành lịch sản xuất cụ thể cho từng mã thành phẩm (SKU), đóng vai trò đầu vào trực tiếp để kiểm tra tải thô RCCP và chạy bùng nổ vật tư MRP."
        ),
        "formula_or_spec": (
            "• Thiết lập vùng Đóng băng (Frozen Zone 1–2 tuần tới) để tránh chen đơn gấp phá vỡ lịch Color Sequencing máy đùn!"
        ),
        "cadivi_application": (
            "OE phối hợp phòng Kế hoạch CADIVI kiểm tra tính khả thi của MPS bằng RCCP và nhóm lệnh theo Bánh xe sản xuất (Product Wheel) để giảm thời gian dừng đổi mã."
        ),
        "cadivi_example": (
            "Ví dụ: Khóa cứng Frozen Zone 48 giờ trong MPS cho 4 máy đùn chủ lực giúp giảm 45% số lần cắt ngang đổi mã đột xuất và nâng OEE thêm +7%."
        ),
        "related": ["S&OP", "MRP", "RCCP", "CRP", "Heijunka"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "MRP": {
        "term": "MRP",
        "full_name": "Material Requirements Planning — Hoạch Định Nhu Cầu Nguyên Vật Liệu",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["MRP", "Material Requirements Planning"],
        "case_sensitive": ["MRP"],
        "short_desc": "Thuật toán trong ERP bùng nổ cây BOM từ lịch MPS trừ tồn kho khả dụng để tính chính xác ngày đặt & số lượng đồng rod, hạt nhựa, rulo.",
        "definition": (
            "MRP trả lời 3 câu hỏi sống còn cho kho và mua hàng: Cần mua/sản xuất vật tư gì? Số lượng bao nhiêu? Và PHẢI có mặt tại xưởng vào ngày nào để không dừng máy?"
        ),
        "formula_or_spec": (
            "• 3 đầu vào bắt buộc của MRP: (1) MPS + (2) Cây MBOM chuẩn (độ chính xác ≥ 99%) + (3) Tồn kho thực tế chính xác (RIA ≥ 98.5% nhờ Cycle Counting)."
        ),
        "cadivi_application": (
            "Nếu MBOM tại CADIVI thiếu hệ số xoắn Lay-up Factor hoặc tồn kho thực tế bị lệch, MRP sẽ đặt thiếu đồng/nhựa gây dừng chuyền! OE chịu trách nhiệm giữ dữ liệu MBOM và Lead Time công đoạn luôn chuẩn."
        ),
        "cadivi_example": (
            "Ví dụ: Cập nhật đúng hệ số xoắn 1.022 và hao hụt startup 1.2% vào MBOM trong ERP giúp MRP tính đặt đúng lượng hạt nhựa XLPE Silane, xóa hoàn toàn tình trạng thiếu nhựa giữa chừng lệnh chạy."
        ),
        "related": ["MPS", "BOM", "ERP", "Cycle Counting", "Safety Stock", "ROP"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "CRP": {
        "term": "CRP",
        "full_name": "Capacity Requirements Planning — Hoạch Định Năng Lực Chi Tiết Từng Máy",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["CRP", "Capacity Requirements Planning"],
        "case_sensitive": ["CRP"],
        "short_desc": "Kiểm tra tải giờ máy chi tiết theo từng thiết bị cụ thể (vd: Máy Đùn 1 vs Máy Đùn 2) và từng ca sau khi đã bùng nổ MRP và Routing.",
        "definition": (
            "Trong khi RCCP kiểm tra tải nhanh theo nhóm công đoạn, CRP tính toán chi tiết giờ chạy + giờ đổi mã SMED trên TỪNG CHIẾC MÁY cụ thể theo từng ngày/ca để cân bằng tải cục bộ."
        ),
        "formula_or_spec": (
            "• Giờ tải máy chi tiết = (Số mét lệnh SX / Tốc độ thực m/phút) + Thời gian đổi mã SMED dự kiến + Thời gian PM định kỳ."
        ),
        "cadivi_application": (
            "Phát hiện tình trạng mất cân bằng tải giữa các máy đùn khác cỡ trục vít (Ø65 vs Ø90 vs Ø120) tại CADIVI để điều chuyển mã dây tương thích sang máy rảnh hơn."
        ),
        "cadivi_example": (
            "Ví dụ: CRP tuần cho thấy Máy Đùn Ø90 quá tải 128% trong khi Máy Đùn Ø70 chỉ tải 62% → Điều độ chuyển các mã dây CV 6–10mm² sang chạy máy Ø70 giúp cả hai máy cân bằng quanh 88%!"
        ),
        "related": ["RCCP", "MPS", "MRP", "OEE", "SMED"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "Safety Stock": {
        "term": "Safety Stock",
        "full_name": "Safety Stock — Tồn Kho An Toàn Chống Biến Động Nhu Cầu & Trễ Giao Hàng",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["Safety Stock", "tồn kho an toàn"],
        "case_sensitive": [],
        "short_desc": "Lượng vật tư/thành phẩm dự trữ tối thiểu tính theo xác suất thống kê để bảo vệ nhà máy không bị dừng chuyền khi đơn hàng tăng đột biến hoặc nhà cung ứng trễ hẹn.",
        "definition": (
            "Thay vì trữ tồn kho 'theo cảm tính càng nhiều càng yên tâm' (gây chôn hàng chục tỷ đồng vốn), Safety Stock tính định lượng dựa trên độ lệch chuẩn biến động nhu cầu, thời gian giao hàng (Lead Time) và hệ số mức phục vụ Z."
        ),
        "formula_or_spec": (
            "• Safety Stock = Z × σ_demand × sqrt(Lead Time)\n"
            "• Mức phục vụ 95% → Z = 1.65 | Mức 98% → Z = 2.05 | Mức 99% → Z = 2.33."
        ),
        "cadivi_application": (
            "Áp dụng tính mức đệm khoa học cho kho hạt nhựa PVC/XLPE/LSZH, băng thép DSTA, phụ tùng chiến lược bảo trì và kho thành phẩm dây dân dụng nhóm AX tại CADIVI."
        ),
        "cadivi_example": (
            "Ví dụ kho XLPE CADIVI: Tiêu thụ 2.0 tấn/ngày (σ = 0.4 tấn), Lead Time cung ứng 9 ngày, mức phục vụ 95% (Z=1.65) → Safety Stock = 1.65 × 0.4 × 3 = 1.98 tấn (giảm từ mức trữ cảm tính 6 tấn xuống 2 tấn, giải phóng vốn!)."
        ),
        "related": ["ROP", "ABC-XYZ", "MRP", "Kanban"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "ROP": {
        "term": "ROP",
        "full_name": "Reorder Point — Điểm Đặt Hàng Lại Tự Động",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["ROP", "Reorder Point"],
        "case_sensitive": ["ROP"],
        "short_desc": "Mức tồn kho ngưỡng báo hiệu phải lập tức phát đơn đặt mua (hoặc lệnh sản xuất bù) để hàng kịp về kho đúng lúc chạm Safety Stock.",
        "definition": (
            "ROP là tín hiệu đặt hàng định lượng giúp kho vận hành tự động, không bao giờ xảy ra cảnh 'dùng hết sạch mới tá hỏa gọi mua gấp'."
        ),
        "formula_or_spec": (
            "• ROP = (Nhu cầu tiêu thụ TB/ngày × Lead Time giao hàng) + Safety Stock."
        ),
        "cadivi_application": (
            "Thiết lập ROP cho vật tư tiêu hao xưởng cáp (lưới lọc Screen Pack, khuôn kéo PCD, băng Mica, dầu nhũ tương, rulo gỗ) và nguyên liệu hạt nhựa chính."
        ),
        "cadivi_example": (
            "Ví dụ: Nhựa XLPE tiêu thụ 2 tấn/ngày, giao hàng 9 ngày, Safety Stock 2 tấn → ROP = (2 × 9) + 2 = 20 tấn. Khi ERP báo tồn chạm 20 tấn → Tự động phát yêu cầu mua hàng ngay!"
        ),
        "related": ["Safety Stock", "MRP", "ABC-XYZ", "Two-Bin Kanban"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "ABC-XYZ": {
        "term": "ABC-XYZ",
        "full_name": "Ma Trận Phân Loại ABC–XYZ (Runner – Repeater – Stranger)",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["ABC-XYZ", "Runner", "Repeater", "Stranger"],
        "case_sensitive": ["ABC-XYZ"],
        "short_desc": "Phân nhóm 9 ô kết hợp Giá trị doanh thu (A/B/C) với Độ ổn định nhu cầu (X ổn định / Y mùa vụ / Z thất thường) để chọn đúng chiến lược MTS hay MTO.",
        "definition": (
            "Không thể áp 1 chính sách sản xuất chung cho cả dây dân dụng bán mỗi ngày lẫn cáp dự án 1 năm đặt 2 lần! "
            "Ma trận ABC-XYZ phân tách rõ nhóm AX (Runners — chạy tồn kho MTS/Kanban), AY/BY (Repeaters — chạy theo bánh xe Heijunka) và AZ/CZ (Strangers — chỉ sản xuất khi có đơn MTO + SMED)."
        ),
        "formula_or_spec": (
            "• X: Hệ số biến thiên CV = σ/μ < 0.25 (rất đều) | Y: 0.25–0.50 (biến động vừa) | Z: > 0.50 (thất thường)."
        ),
        "cadivi_application": (
            "Tối ưu cơ cấu sản xuất tại CADIVI Miền Trung giữa dây dân dụng VC/VCm (AX Runners) và cáp lực công trình CXV/DSTA/Mica FR (AZ Strangers), giảm 40% tồn kho thành phẩm chậm luân chuyển."
        ),
        "cadivi_example": (
            "Ví dụ: Tách riêng top 15 mã dây dân dụng nhóm AX (chiếm 68% sản lượng) duy trì siêu thị MTS xuất giao ngay → Kinh doanh không bao giờ phải cắt ngang máy đùn đòi chạy gấp!"
        ),
        "related": ["Safety Stock", "ROP", "Heijunka", "Cycle Counting", "SMED"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "Milk Run": {
        "term": "Milk Run",
        "full_name": "Milk Run — Tuyến Xe Vận Chuyển Tuần Hoàn Giao Nhận Đa Điểm Theo Lịch Cố Định",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Milk Run", "Milk-run"],
        "case_sensitive": [],
        "short_desc": "Tuyến xe nâng/xe kéo chạy vòng tròn theo khung giờ cố định (mỗi 30–60p) vừa giao vật tư mới vừa thu hồi rulo rỗng/phế liệu trên cùng 1 chuyến.",
        "definition": (
            "Thay vì gọi xe nâng chạy lẻ tẻ 1 chiều (đi có hàng – về xe không gây lãng phí 50% hành trình và tắc đường xưởng), Milk Run tổ chức xe chạy vòng tuần hoàn như xe giao sữa buổi sáng: đi 1 vòng qua tất cả các máy."
        ),
        "formula_or_spec": (
            "• Nguyên tắc: Tần suất cố định (vd: mỗi 30 phút) × Số lượng cấp nhỏ (Small Lot) × Ghép giao hàng + thu vỏ rulo rỗng 2 chiều."
        ),
        "cadivi_application": (
            "Áp dụng cho đội xe nâng rulo và xe cấp hạt nhựa/bao bì tại CADIVI Miền Trung để giảm mật độ xe nâng chạy lộn xộn trong xưởng (tăng an toàn EHS) và xóa thời gian chờ rulo."
        ),
        "cadivi_example": (
            "Ví dụ: Thiết lập tuyến Milk Run chạy mỗi 30 phút qua 6 máy đùn (giao bao nhựa mới + rulo rỗng, thu rulo thành phẩm + thùng phế đồng) giúp giảm từ 3 xe nâng chạy rối loạn xuống 2 xe an toàn, đúng giờ!"
        ),
        "related": ["Water Spider", "Kanban", "Spaghetti", "EHS"],
        "doc_key": "lean_muda"
    },
    "FPY": {
        "term": "FPY",
        "full_name": "First Pass Yield — Tỷ Lệ Sản Phẩm Đạt Chuẩn Ngay Từ Lần Đầu Tiên",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["FPY", "First Pass Yield", "FTY", "RFT"],
        "case_sensitive": ["FPY", "FTY", "RFT"],
        "short_desc": "Tỷ lệ phần trăm sản phẩm đi qua 1 công đoạn đạt tiêu chuẩn ngay lập tức mà KHÔNG cần cắt nối, sửa chữa (Rework) hay chạy lại.",
        "definition": (
            "Khác với Final Yield (tính cả hàng lỗi đã được âm thầm sửa lại rồi gộp chung vào hàng đạt), FPY phản ánh trung thực sức khỏe thực sự của công đoạn và phơi bày toàn bộ chi phí làm lại bị che giấu."
        ),
        "formula_or_spec": (
            "• FPY (%) = [ (Tổng đầu vào - Phế phẩm Scrap - Hàng phải sửa Rework) / Tổng đầu vào ] × 100%."
        ),
        "cadivi_application": (
            "Đo FPY riêng từng công đoạn Kéo – Ủ – Bện – Đùn – Ghép lõi tại CADIVI (tính cả cuộn phải đem sang cuộn cắt bỏ đoạn thủng Spark là không đạt FPY!) để không bị che giấu chi phí Rework."
        ),
        "cadivi_example": (
            "Ví dụ: Ca máy đùn chạy 20 rulo, 18 rulo đạt thẳng, 2 rulo có 1 điểm Spark phải đưa sang máy Rewind cắt bỏ 10m nối/chia cuộn → Final Yield vẫn báo 99% nhưng FPY thực chất chỉ là 18/20 = 90%!"
        ),
        "related": ["RTY", "Scrap", "DPMO", "OEE"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "RTY": {
        "term": "RTY",
        "full_name": "Rolled Throughput Yield — Hiệu Suất Đạt Thẳng Toàn Chuỗi Công Đoạn",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["RTY", "Rolled Throughput Yield", "Hidden Factory"],
        "case_sensitive": ["RTY"],
        "short_desc": "Tích nhân FPY của tất cả các công đoạn nối tiếp nhau — phơi bày tác động cộng dồn khủng khiếp của lỗi qua nhiều khâu ('Nhà máy ẩn').",
        "definition": (
            "Một đơn hàng cáp lực đi qua 6–7 công đoạn độc lập. Dù mỗi công đoạn chỉ lỗi 2–3%, xác suất để một mét cáp đi trót lọt từ đồng rod đến thành phẩm không dính lỗi ở bất kỳ khâu nào lại tụt xuống rất thấp — đó chính là bản chất của RTY."
        ),
        "formula_or_spec": (
            "• RTY = FPY_1 × FPY_2 × FPY_3 × ... × FPY_n\n"
            "• Ví dụ 6 công đoạn mỗi khâu 97%: RTY = 0.97⁶ = 83.3% (16.7% đơn hàng rơi vào Hidden Factory!)."
        ),
        "cadivi_application": (
            "Chỉ số cấp Giám đốc nhà máy để OE CADIVI nhìn tổng lực chất lượng xuyên suốt từ Kéo → Ủ → Bện → Đùn lõi → Xông XLPE → Ghép lõi → Đùn vỏ, ưu tiên nâng khâu có FPY thấp nhất trước."
        ),
        "cadivi_example": (
            "Ví dụ cáp CXV qua 6 khâu (98%×99%×97%×95%×96%×97%) có RTY = 83.27%. Chỉ cần nâng FPY khâu Đùn XLPE từ 95% lên 98.5% và Ghép lõi lên 98.5% lập tức đẩy RTY toàn chuỗi lên 88.6%!"
        ),
        "related": ["FPY", "Six Sigma", "DPMO", "Scrap"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "DPMO": {
        "term": "DPMO",
        "full_name": "Defects Per Million Opportunities (DPMO & PPM) — Số Lỗi Trên Một Triệu Cơ Hội",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["DPMO", "PPM"],
        "case_sensitive": ["DPMO", "PPM"],
        "short_desc": "Thước đo chuẩn hóa mức độ khuyết tật trong Six Sigma giúp so sánh công bằng chất lượng giữa dây đơn giản (VC) và cáp lực phức tạp nhiều lớp (CXV/DSTA).",
        "definition": (
            "PPM đếm số sản phẩm hỏng trên 1 triệu sản phẩm; còn DPMO chia thêm cho số cơ hội gây lỗi (Opportunities) trên mỗi sản phẩm để quy đổi ra Sigma Level chuẩn quốc tế."
        ),
        "formula_or_spec": (
            "• DPMO = [ Tổng số lỗi / (Số đơn vị kiểm tra × Số cơ hội lỗi mỗi đơn vị) ] × 1,000,000\n"
            "• 3 Sigma ≈ 66,807 DPMO | 4 Sigma ≈ 6,210 DPMO | 5 Sigma ≈ 233 DPMO | 6 Sigma ≤ 3.4 DPMO."
        ),
        "cadivi_application": (
            "Chuẩn hóa báo cáo chất lượng OE & QA/QC tại CADIVI khi so sánh hiệu suất chất lượng giữa phân xưởng dây dân dụng và phân xưởng cáp lực đa lớp."
        ),
        "cadivi_example": (
            "Ví dụ: Kiểm tra 1,000 cuộn cáp, mỗi cuộn có 5 hạng mục CTQ (điện trở, chiều dày, đường kính, Spark, in chữ = 5,000 cơ hội), phát hiện 12 lỗi → DPMO = (12/5,000)×1,000,000 = 2,400 DPMO (~4.32 Sigma)."
        ),
        "related": ["Six Sigma", "Cpk", "FPY", "RTY", "CTQ"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "SIPOC": {
        "term": "SIPOC",
        "full_name": "Suppliers – Inputs – Process – Outputs – Customers (Sơ Đồ Ranh Giới Quy Trình 1 Trang)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["SIPOC"],
        "case_sensitive": ["SIPOC"],
        "short_desc": "Bảng tổng quan 5 cột bắt buộc trong pha Define của dự án DMAIC giúp chốt rõ phạm vi bắt đầu–kết thúc, đầu vào–đầu ra và khách hàng của quy trình.",
        "definition": (
            "SIPOC giúp cả nhóm dự án liên phòng ban (Sản xuất, Kỹ thuật, Kho, QC, OE) đứng cùng một góc nhìn về ranh giới quy trình cần cải tiến (chỉ gồm 5–7 bước lớn) trước khi lao vào thu thập dữ liệu chi tiết."
        ),
        "formula_or_spec": (
            "• S (Nhà cung ứng / Công đoạn trước) → I (Đầu vào NVL/Thông số) → P (5–7 bước chính) → O (Sản phẩm/Dữ liệu ra) → C (Khách hàng / Công đoạn sau)."
        ),
        "cadivi_application": (
            "Vẽ ngay trong ngày đầu khởi động dự án DMAIC tại CADIVI (ví dụ dự án giảm phế đùn XLPE: S=Xưởng Bện & Kho nhựa → I=Rulo đồng bện + Hạt XLPE + Recipe → P=Nạp→Sấy→Đùn→Làm mát→Spark→Thu cuộn → O=Rulo lõi XLPE → C=Bể Sauna & Ghép lõi)."
        ),
        "cadivi_example": (
            "Ví dụ: Nhờ bảng SIPOC, đội dự án máy đùn nhận ra đầu vào rulo từ xưởng bện thiếu dữ liệu chiều dài thực là 1 trong 3 nguyên nhân gây phế đuôi cuộn ngay từ khâu Define!"
        ),
        "related": ["DMAIC", "VOC", "CTQ", "VSM", "Control Plan"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "VOC": {
        "term": "VOC",
        "full_name": "Voice of Customer (VOC) & Voice of Business (VOB) — Tiếng Nói Khách Hàng & Doanh Nghiệp",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["VOC", "VOB", "Voice of Customer"],
        "case_sensitive": ["VOC", "VOB"],
        "short_desc": "Yêu cầu và kỳ vọng thực sự của khách hàng công trình/đại lý (VOC) và mục tiêu lợi nhuận của Ban Giám đốc (VOB) — điểm khởi đầu của mọi dự án OE.",
        "definition": (
            "Cải tiến OE không phải để làm đẹp lý thuyết, mà phải trực tiếp giải quyết nỗi đau của khách hàng (giao hàng nhanh, không lỗi cách điện, đủ mét, giá cạnh tranh) và mục tiêu kinh doanh (giảm giá thành, tăng biên lợi nhuận)."
        ),
        "formula_or_spec": (
            "• Cây chuyển hóa chuẩn Six Sigma: VOC (Mong muốn chung) → Driver (Yếu tố cốt lõi) → CTQ (Thông số đo được có cận USL/LSL)."
        ),
        "cadivi_application": (
            "Dịch các phản hồi từ đại lý/chủ đầu tư điện lực (vd: 'Dây dễ tuốt vỏ, không bị rối cuộn, giao đủ mét đúng hẹn') thành chỉ tiêu CTQ kỹ thuật kiểm soát ngay trên máy đùn & máy cuộn CADIVI."
        ),
        "cadivi_example": (
            "Ví dụ: VOC khách hàng công trình 'Vỏ cáp CXV khó bóc tách khi đấu nối tủ điện' → Dịch thành CTQ 'Lực bám dính cách điện/vỏ trong dải tiêu chuẩn' → Hiệu chỉnh nhiệt độ Pre-heater ruột đồng & góc cối đùn!"
        ),
        "related": ["CTQ", "SIPOC", "DMAIC", "Hoshin Kanri"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "CTQ": {
        "term": "CTQ",
        "full_name": "Critical to Quality — Đặc Tính Kỹ Thuật Trọng Yếu Quyết Định Chất Lượng Sản Phẩm",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["CTQ", "Critical to Quality"],
        "case_sensitive": ["CTQ"],
        "short_desc": "Các thông số định lượng đo đếm được có giới hạn dung sai rõ ràng (điện trở 20°C, chiều dày min, 0 lỗi Spark, độ giãn dài) quyết định sản phẩm Đạt hay Hỏng.",
        "definition": (
            "CTQ là kết quả chuyển hóa cụ thể từ VOC sang ngôn ngữ kỹ thuật để đưa vào bản vẽ quy cách, biểu đồ SPC, Control Plan và đánh giá năng lực Cpk."
        ),
        "formula_or_spec": (
            "• 5 CTQ kinh điển của 1 mã cáp điện CADIVI: (1) Điện trở R_20 ≤ trần IEC 60228, (2) Chiều dày t_min ≥ 0.9×t_nom - 0.1mm, (3) 0 lỗi Spark, (4) Độ bền kéo/giãn dài & Hot Set đạt, (5) Đủ chiều dài mét (±0.3%)."
        ),
        "cadivi_application": (
            "Mọi biểu đồ SPC, kế hoạch kiểm tra Lab và dự án DMAIC tại CADIVI đều phải bám chặt vào đúng 3–5 thông số CTQ này để không đo lan man tốn công vô ích."
        ),
        "cadivi_example": (
            "Ví dụ: Xác định đúng CTQ của dự án dây VC 2.5mm² là 'Đường kính ngoài 3.36 ± 0.08 mm & 0 lỗi Spark/cuộn' giúp tập trung 100% nguồn lực cải tiến vào Laser Gauge và Hopper Dryer."
        ),
        "related": ["VOC", "SIPOC", "Control Plan", "Cpk", "IEC 60228", "IEC 60502"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "Control Plan": {
        "term": "Control Plan",
        "full_name": "Process Control Plan — Kế Hoạch Kiểm Soát Quá Trình (Khóa Chặt Thành Quả Pha Control)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Control Plan"],
        "case_sensitive": [],
        "short_desc": "Bảng quy định chi tiết tại từng công đoạn: kiểm soát thông số nào (X/Y), dung sai bao nhiêu, đo bằng máy gì, tần suất lấy mẫu và PHẢI LÀM GÌ khi vượt ngưỡng (Reaction Plan).",
        "definition": (
            "Control Plan là tài liệu sống kết nối trực tiếp từ PFMEA và dự án DMAIC sang vận hành hàng ngày tại xưởng — đảm bảo thành quả cải tiến được duy trì vĩnh viễn ngay cả khi Chuyên viên OE đã chuyển sang dự án khác."
        ),
        "formula_or_spec": (
            "• Cột bắt buộc: Công đoạn | Thông số CTQ/Máy | Giới hạn chuẩn | Thiết bị đo | Cỡ mẫu & Tần suất | Phương pháp kiểm soát (SPC/Poka-Yoke) | Kế hoạch phản ứng khi lỗi (Reaction Plan)."
        ),
        "cadivi_application": (
            "Bắt buộc ban hành và dán tại máy sau mỗi dự án cải tiến tại CADIVI (ví dụ: Control Plan dây chuyền đùn PVC quy định rõ nhiệt độ sấy 75°C kiểm mỗi 2 giờ, Laser Gauge theo dõi liên tục, nếu vượt ±0.06mm dừng chỉnh ngay)."
        ),
        "cadivi_example": (
            "Ví dụ: Sau dự án DMAIC giảm phế đùn từ 3.8% xuống 0.78%, OE đưa tần suất hiệu chuẩn cảm biến nhiệt PID và kiểm tra độ ẩm hạt nhựa vào Control Plan → Giữ tỷ lệ phế ổn định < 0.9% suốt 12 tháng liền!"
        ),
        "related": ["PFMEA", "DMAIC", "SPC", "SOP", "ISO 9001"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "7 QC Tools": {
        "term": "7 QC Tools",
        "full_name": "Seven Basic Tools of Quality — 7 Công Cụ Kiểm Soát Chất Lượng Cổ Điển (Kaoru Ishikawa)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["7 QC Tools", "7 công cụ QC"],
        "case_sensitive": [],
        "short_desc": "Bộ 7 công cụ trực quan kinh điển giải quyết tới 90% sự cố chất lượng & năng suất tại hiện trường xưởng mà không cần toán học quá phức tạp.",
        "definition": (
            "Gồm: (1) Phiếu kiểm tra Check Sheet, (2) Biểu đồ tần suất Histogram, (3) Biểu đồ Pareto 80/20, (4) Biểu đồ Xương cá Ishikawa, (5) Biểu đồ phân tán Scatter, (6) Biểu đồ kiểm soát SPC và (7) Phân tầng dữ liệu Stratification."
        ),
        "formula_or_spec": (
            "• Lộ trình dùng nhanh tại xưởng: Check Sheet (Thu số) → Stratification & Pareto (Chọn lỗi số 1) → Ishikawa (Tìm nguyên nhân) → Histogram & Scatter (Kiểm chứng) → SPC (Duy trì)."
        ),
        "cadivi_application": (
            "Bộ công cụ đào tạo căn bản tốt nhất mà Chuyên viên OE CADIVI có thể truyền đạt lại cho các Tổ trưởng và nhóm Kaizen phân xưởng để ai cũng biết giải quyết vấn đề bằng số liệu."
        ),
        "cadivi_example": (
            "Ví dụ: Dạy Tổ trưởng xưởng kéo dùng Check Sheet + Pareto + Phân tầng theo Ca giúp tổ tự phát hiện 70% vụ đứt sợi xảy ra ở đúng cấp khuôn số 6 trên máy kéo tinh số 2!"
        ),
        "related": ["Pareto", "Ishikawa", "Histogram", "Scatter", "SPC"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "Histogram": {
        "term": "Histogram",
        "full_name": "Histogram — Biểu Đồ Tần Suất Phân Bố Dữ Liệu Liên Tục",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Histogram"],
        "case_sensitive": [],
        "short_desc": "Biểu đồ cột cho thấy hình dáng phân phối thực tế của dữ liệu đo (tâm ở đâu, xòe rộng hay hẹp, có bị lệch 1 bên hay tách 2 đỉnh do trộn 2 máy/2 ca không).",
        "definition": (
            "Chỉ nhìn con số trung bình (Mean) rất dễ bị lừa! Biểu đồ Histogram phơi bày hình dáng phân bố dữ liệu so với 2 vạch cận dung sai LSL/USL: phân bố hình chuông chuẩn, phân bố lệch (Skewed) hay phân bố 2 đỉnh (Bimodal — dấu hiệu 2 ca chỉnh máy khác nhau!)."
        ),
        "formula_or_spec": (
            "• Dấu hiệu vàng cần soi trên Histogram: (1) Tâm so với Target, (2) Bề rộng so với LSL–USL, (3) Hình 2 đỉnh (Bimodal → phải phân tầng tách theo Ca/Máy/Lô NVL!)."
        ),
        "cadivi_application": (
            "Vẽ nhanh trên Excel/Minitab cho dữ liệu đường kính bọc cách điện, điện trở ruột dẫn và thời gian chuyển đổi SMED tại CADIVI để kiểm tra tính ổn định trước khi tính Cpk."
        ),
        "cadivi_example": (
            "Ví dụ: Histogram đường kính dây VC 2.5mm² xuất hiện 2 đỉnh rõ rệt tại 3.35mm và 3.44mm → Phân tầng ngay phát hiện Ca 1 chỉnh theo chuẩn mới, còn Ca 2 vẫn giữ thói quen bọc dày cũ!"
        ),
        "related": ["7 QC Tools", "SPC", "Cpk", "Box-Cox", "Minitab"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "Scatter": {
        "term": "Scatter",
        "full_name": "Scatter Plot & Correlation — Biểu Đồ Phân Tán & Hệ Số Tương Quan (r)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Scatter", "Scatter Plot", "Correlation"],
        "case_sensitive": [],
        "short_desc": "Biểu đồ chấm tọa độ (X, Y) kiểm tra xem biến đầu vào X (vd: tốc độ máy, nhiệt độ nước) có kéo theo biến đầu ra Y (lỗi Spark, độ dày) tăng/giảm cùng nhau không.",
        "definition": (
            "Scatter Plot trực quan hóa mối liên hệ giữa 2 biến số liên tục, kèm hệ số tương quan Pearson r (từ -1 đến +1). Lưu ý: tương quan mạnh (|r| > 0.7) là manh mối cực mạnh, sau đó kiểm chứng thêm bằng Regression/DOE để chốt nhân–quả."
        ),
        "formula_or_spec": (
            "• r tiến về +1: Tương quan thuận mạnh | r tiến về -1: Tương quan nghịch mạnh | r ≈ 0: Không có liên hệ tuyến tính."
        ),
        "cadivi_application": (
            "Chuyên viên OE CADIVI dùng Scatter kiểm chứng nhanh các giả thuyết hiện trường: Nhiệt độ nước Cooling Trough vs Độ nhám vỏ; Tốc độ kéo vs Tần suất đứt sợi; Nhiệt độ đùn vs Độ giãn dài nhựa."
        ),
        "cadivi_example": (
            "Ví dụ: Vẽ Scatter giữa Nhiệt độ nước máng làm mát (20°C → 38°C) và Số lỗi trầy xước bề mặt vỏ cho hệ số r = +0.86 (p < 0.001) → Chứng minh ngay cần bảo trì Chiller giữ nước ≤ 25°C!"
        ),
        "related": ["Regression", "7 QC Tools", "Minitab", "Cooling Trough"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "Chi-Square": {
        "term": "Chi-Square",
        "full_name": "Chi-Square Test (Kiểm Định Chi Bình Phương) — So Sánh Tỷ Lệ Lỗi Dữ Liệu Định Tính",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Chi-Square", "Chi-square"],
        "case_sensitive": [],
        "short_desc": "Phép kiểm định thống kê trên bảng đếm (Đạt / Lỗi) để chứng minh tỷ lệ lỗi có thực sự khác nhau giữa các ca, các máy hay các nhà cung ứng vật tư hay không.",
        "definition": (
            "Khi dữ liệu không phải là con số đo liên tục (mm, giây) mà là dữ liệu đếm thuộc tính (số cuộn Đạt vs số cuộn Lỗi Spark giữa 3 nhà cung ứng hạt nhựa), ta không dùng t-test/ANOVA mà dùng kiểm định Chi-Square."
        ),
        "formula_or_spec": (
            "• Minitab: Stat → Tables → Chi-Square Test for Association.\n"
            "• Nếu p-value < 0.05 → Tỷ lệ lỗi thực sự phụ thuộc vào nhóm (Nhà cung ứng / Ca / Máy)!"
        ),
        "cadivi_application": (
            "Chứng minh bằng chứng thống kê sắc bén với phòng Mua hàng/Nhà cung ứng khi một lô đồng rod hay lô hạt nhựa PVC gây tỷ lệ cuộn lỗi cao bất thường tại CADIVI."
        ),
        "cadivi_example": (
            "Ví dụ: So sánh số cuộn lỗi Spark của Nhà cung ứng nhựa A (4/500 cuộn) vs B (21/500 cuộn) bằng Chi-Square cho p-value = 0.0006 (< 0.05) → Đủ bằng chứng yêu cầu đổi lô/khiếu nại nhà cung ứng B!"
        ),
        "related": ["2-Sample t-test", "ANOVA", "Minitab", "DMAIC"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "Regression": {
        "term": "Regression",
        "full_name": "Regression Analysis — Phân Tích Hồi Quy Dự Báo & Định Lượng Tác Động Đầu Vào",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Regression", "hồi quy"],
        "case_sensitive": [],
        "short_desc": "Mô hình toán học y = a + b·x (tuyến tính/đa biến) định lượng chính xác khi thay đổi 1 đơn vị tốc độ/nhiệt độ thì sản lượng, điện năng hay chiều dày nhựa thay đổi bao nhiêu.",
        "definition": (
            "Hồi quy giúp Chuyên viên OE vượt qua mức mô tả sang mức DỰ BÁO: xây phương trình liên hệ giữa tốc độ vít, tốc độ kéo Capstan và đường kính ngoài (hoặc dự báo điện năng kWh theo sản lượng tấn), đánh giá độ khớp bằng hệ số R²."
        ),
        "formula_or_spec": (
            "• R² (R-squared) càng gần 100% (thường > 75–80%) chứng tỏ các biến đầu vào X giải thích rất tốt biến động của đầu ra Y; p-value < 0.05 xác nhận hệ số hồi quy có ý nghĩa."
        ),
        "cadivi_application": (
            "Xây mô hình dự báo tiêu thụ điện năng (Baseline ISO 50001: kWh = Định mức không tải + b × Tấn đồng) và mô hình tìm tốc độ đùn tối ưu tại CADIVI."
        ),
        "cadivi_example": (
            "Ví dụ: Chạy hồi quy điện năng 12 tháng của xưởng Kéo ra phương trình `kWh = 18,500 + 215 × Tấn_Đồng` (R² = 91%) → Phơi bày ngay khoản điện chạy không tải 18,500 kWh/tháng cần cắt giảm!"
        ),
        "related": ["Scatter", "Minitab", "DOE", "ISO 50001", "SEC"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "Box-Cox": {
        "term": "Box-Cox",
        "full_name": "Box-Cox & Johnson Transformation — Biến Đổi Dữ Liệu Phi Chuẩn Về Phân Phối Chuẩn",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Box-Cox", "Johnson Transformation"],
        "case_sensitive": [],
        "short_desc": "Kỹ thuật chuyển đổi toán học trong Minitab khi dữ liệu đo (như độ lệch tâm, thời gian đổi mã SMED) bị lệch không tuân theo phân phối chuẩn (Anderson-Darling p < 0.05).",
        "definition": (
            "Công thức Cpk truyền thống chỉ đúng khi dữ liệu tuân theo phân phối chuẩn hình chuông. Nhiều thông số kỹ thuật có ranh giới tự nhiên ≥ 0 (như độ lệch tâm, độ nhám, thời gian chờ) luôn bị lệch phải — phải biến đổi Box-Cox/Johnson hoặc dùng phân tích Nonnormal (Weibull/Lognormal) để không tính ra Cpk ảo!"
        ),
        "formula_or_spec": (
            "• Minitab: Stat → Quality Tools → Capability Analysis → Normal (chọn nút Transform → Box-Cox) HOẶC chọn Capability Analysis (Nonnormal)."
        ),
        "cadivi_application": (
            "Dùng trong Minitab khi phân tích năng lực độ lệch tâm (Eccentricity ≥ 0) của máy đùn cáp hoặc phân tích thời gian đổi mã SMED tại CADIVI để báo cáo Cpk/Ppk chuẩn xác học thuật."
        ),
        "cadivi_example": (
            "Ví dụ: Dữ liệu độ lệch tâm vỏ cáp có P-value Anderson-Darling = 0.004 (phi chuẩn lệch phải). Dùng Box-Cox (λ = 0.5) đưa về chuẩn (P = 0.42) mới tính ra Ppk thật = 1.28 thay vì con số ảo 1.75!"
        ),
        "related": ["Minitab", "Cpk", "Ppk", "Histogram", "SPC"],
        "doc_key": "minitab_spc"
    },
    "LOTO": {
        "term": "LOTO",
        "full_name": "Lockout / Tagout — Quy Trình Khóa Nguồn Năng Lượng & Treo Thẻ An Toàn",
        "category": "An Toàn Công Nghiệp, EHS & Tiêu Chuẩn ISO",
        "aliases": ["LOTO", "Lockout/Tagout", "Lockout"],
        "case_sensitive": ["LOTO"],
        "short_desc": "Quy trình an toàn bắt buộc 6 bước: ngắt cầu dao/van khí, gắn ổ khóa cá nhân + thẻ tên và thử bấm khởi động (Zero Energy) trước khi sửa máy hay đổi khuôn SMED.",
        "definition": (
            "LOTO ngăn chặn tuyệt đối thảm họa người khác vô tình bấm nút khởi động máy khi kỹ thuật viên đang thò tay vào tháo khuôn máy đùn, nạp lồng máy bện hay bảo trì hộp số máy kéo."
        ),
        "formula_or_spec": (
            "• Nguyên tắc '1 Người – 1 Ổ Khóa – 1 Chìa Khóa': Không bao giờ dùng chung khóa hay nhờ người khác mở hộ; BẮT BUỘC bấm thử nút Start kiểm tra Zero Energy!"
        ),
        "cadivi_application": (
            "Bắt buộc tích hợp thẳng vào mọi bản SOP chuyển đổi nhanh SMED (đặc biệt kịch bản 2 người song song F1 Pit-stop) và bảo trì PM tại Nhà máy CADIVI Miền Trung."
        ),
        "cadivi_example": (
            "Ví dụ: Khi 2 thợ phối hợp thay đầu Chày-Cối máy đùn hoặc thay khuôn máy kéo RBD, cả 2 cùng móc ổ khóa riêng lên kẹp Hasp ở tủ điện chính → Tuyệt đối không thể bật nguồn khi 1 người vẫn đang ở sau máy!"
        ),
        "related": ["EHS", "ISO 45001", "SMED", "TPM", "SOP"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "EHS": {
        "term": "EHS",
        "full_name": "Environment, Health & Safety — Quản Lý An Toàn, Sức Khỏe Nghề Nghiệp & Môi Trường",
        "category": "An Toàn Công Nghiệp, EHS & Tiêu Chuẩn ISO",
        "aliases": ["EHS", "HSE", "SHE"],
        "case_sensitive": ["EHS", "HSE", "SHE"],
        "short_desc": "Hệ thống đảm bảo an toàn lao động (máy quay tốc độ cao, cầu trục rulo 5 tấn, nhiệt 200°C, thử cao áp) và bảo vệ môi trường xưởng sản xuất.",
        "definition": (
            "Mọi cải tiến năng suất của OE đều phải tuân thủ tuyệt đối tiêu chuẩn EHS (chữ S trong SQDC). Không bao giờ tháo bỏ rào chắn an toàn, công tắc liên động cửa hay chạy vượt tải cầu trục chỉ để tăng thêm vài % OEE!"
        ),
        "formula_or_spec": (
            "• Tháp kiểm soát mối nguy (Hierarchy of Controls): Loại bỏ → Thay thế → Kỹ thuật/Che chắn (Poka-Yoke an toàn) → Hành chính (SOP/LOTO) → PPE bảo hộ (găng chống nhiệt, nút tai, giày mũi thép)."
        ),
        "cadivi_application": (
            "5 điểm nóng EHS tại Nhà máy CADIVI Miền Trung: (1) Nâng hạ rulo 1–5 tấn bằng cầu trục/xe nâng, (2) Vùng nhiệt 200°C máy đùn & lò ủ, (3) Khu thử cao áp HV/Spark Test, (4) Tiếng ồn >85 dB khu kéo/bện, (5) Xử lý nhũ tương dầu thải & hút khói PVC."
        ),
        "cadivi_example": (
            "Ví dụ: Thiết kế lại làn đường xe nâng chở rulo rộng ≥ 3.5m có vạch sơn phân cách & gương cầu lồi giao lộ, tách biệt hoàn toàn khỏi lối đi bộ xanh giúp đạt 0 sự cố va chạm xe nâng trong năm!"
        ),
        "related": ["LOTO", "ISO 45001", "ISO 14001", "5S", "Ergonomics"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "ISO 9001": {
        "term": "ISO 9001",
        "full_name": "ISO 9001:2015 — Tiêu Chuẩn Quốc Tế Về Hệ Thống Quản Lý Chất Lượng (QMS)",
        "category": "An Toàn Công Nghiệp, EHS & Tiêu Chuẩn ISO",
        "aliases": ["ISO 9001"],
        "case_sensitive": [],
        "short_desc": "Nền tảng quản trị chất lượng theo hướng tiếp cận quá trình, tư duy dựa trên rủi ro, chuẩn hóa tài liệu SOP/Control Plan và cải tiến liên tục PDCA.",
        "definition": (
            "ISO 9001 đảm bảo mọi quy trình trong nhà máy (từ nhận đơn hàng, kiểm đầu vào, sản xuất, thử nghiệm xuất xưởng đến xử lý khiếu nại) đều được văn bản hóa rõ ràng, thực thi nhất quán và có bằng chứng truy xuất."
        ),
        "formula_or_spec": (
            "• Liên kết OE: Mọi cải tiến quy trình, thay đổi định mức, SOP mới hay hành động khắc phục 8D/CAPA đều phải cập nhật đồng bộ vào hệ thống tài liệu ISO 9001."
        ),
        "cadivi_application": (
            "CADIVI áp dụng nghiêm ngặt ISO 9001 trên toàn hệ thống nhà máy. Chuyên viên OE phối hợp phòng QA cập nhật SOP/Control Plan sau mỗi dự án Kaizen để vượt qua mọi đợt đánh giá nội bộ & khách hàng."
        ),
        "cadivi_example": (
            "Ví dụ: Sau khi thay đổi quy trình đổi khuôn SMED máy đùn, OE trình ký ban hành bản sửa đổi SOP (Rev.02) và đào tạo ký xác nhận theo đúng thủ tục kiểm soát tài liệu ISO 9001."
        ),
        "related": ["Control Plan", "SOP", "PDCA", "ISO 14001", "ISO 45001", "ISO 50001"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "ISO 14001": {
        "term": "ISO 14001",
        "full_name": "ISO 14001:2015 — Tiêu Chuẩn Quốc Tế Về Hệ Thống Quản Lý Môi Trường (EMS)",
        "category": "An Toàn Công Nghiệp, EHS & Tiêu Chuẩn ISO",
        "aliases": ["ISO 14001"],
        "case_sensitive": [],
        "short_desc": "Quản lý kiểm soát chất thải nguy hại (dầu nhũ tương kéo đồng thải, giẻ lau dầu), khí thải/bụi nhựa PVC và tối ưu tái chế rác nhựa sản xuất.",
        "definition": (
            "ISO 14001 giúp nhà máy giảm thiểu tác động môi trường và chi phí xử lý chất thải. Thực tế nhiều dự án Lean/OE (giảm nhựa xả purging, lọc tái sử dụng dầu nhũ tương, giảm phế đồng bọc nhựa) tạo lợi ích kép: vừa giảm giá thành vừa đạt mục tiêu xanh ISO 14001!"
        ),
        "formula_or_spec": (
            "• Nguyên tắc 3R trong nhà máy: Reduce (Giảm phát sinh phế tại nguồn — ưu tiên #1) → Reuse (Lọc tuần hoàn nước/nhũ tương) → Recycle (Băm nhựa sạch tái dùng lớp độn)."
        ),
        "cadivi_application": (
            "Tại CADIVI Miền Trung (KCN Hòa Cầm): kiểm soát lọc ly tâm kéo dài tuổi thọ bể nhũ tương kéo đồng gấp đôi (giảm 50% lượng dầu thải nguy hại) và giảm nhựa xả Purging qua Color Sequencing."
        ),
        "cadivi_example": (
            "Ví dụ: Lắp hệ thống lọc ly tâm + tách váng dầu cho bể nhũ tương máy kéo RBD kéo dài chu kỳ thay dầu từ 3 tháng lên 7 tháng — vừa tiết kiệm 180 triệu/năm tiền dầu mới vừa giảm 55% chi phí thuê xử lý chất thải nguy hại!"
        ),
        "related": ["EHS", "Drawing Emulsion", "Purging", "ISO 45001", "ISO 50001"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "ISO 45001": {
        "term": "ISO 45001",
        "full_name": "ISO 45001:2018 — Tiêu Chuẩn Hệ Thống Quản Lý An Toàn & Sức Khỏe Nghề Nghiệp (OH&S)",
        "category": "An Toàn Công Nghiệp, EHS & Tiêu Chuẩn ISO",
        "aliases": ["ISO 45001"],
        "case_sensitive": [],
        "short_desc": "Chuẩn mực quốc tế về nhận diện mối nguy (HIRA), phòng ngừa tai nạn lao động, bệnh nghề nghiệp (tiếng ồn, đau cơ xương) và chuẩn hóa LOTO tại xưởng.",
        "definition": (
            "ISO 45001 yêu cầu nhà máy chủ động đánh giá rủi ro mối nguy trước khi thay đổi bất kỳ máy móc hay quy trình sản xuất nào (Management of Change) để đạt mục tiêu Zero Accidents."
        ),
        "formula_or_spec": (
            "• Chỉ số đo lường an toàn: LTIR (Lost Time Injury Rate), số vụ Near-Miss (Suýt tai nạn) được báo cáo và xử lý phòng ngừa sớm."
        ),
        "cadivi_application": (
            "Mỗi dự án cải tiến Layout, SMED hay tự động hóa của OE tại CADIVI đều phải kèm mục đánh giá an toàn (LOTO, che chắn lồng máy bện, độ ồn, tư thế Ergonomics) đạt chuẩn ISO 45001."
        ),
        "cadivi_example": (
            "Ví dụ: Trước khi chạy thử phương án 1 công nhân đứng 3 máy bện Buncher, OE cùng cán bộ EHS đánh giá lối đi không vướng dây/rulo và kiểm tra hoạt động 100% công tắc liên động cửa lồng quay."
        ),
        "related": ["EHS", "LOTO", "Ergonomics", "ISO 14001", "ISO 9001"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "ISO 50001": {
        "term": "ISO 50001",
        "full_name": "ISO 50001:2018 — Tiêu Chuẩn Hệ Thống Quản Lý Năng Lượng Nhà Máy (EnMS)",
        "category": "An Toàn Công Nghiệp, EHS & Tiêu Chuẩn ISO",
        "aliases": ["ISO 50001"],
        "case_sensitive": [],
        "short_desc": "Khung quản trị tiết kiệm điện năng bài bản bằng đường cơ sở hồi quy (EnB), chỉ số EnPI (kWh/tấn) và kiểm toán các cụm tiêu thụ điện lớn (SEU).",
        "definition": (
            "ISO 50001 giúp doanh nghiệp sản xuất nặng giảm bền vững 5–15% hóa đơn tiền điện mỗi năm thông qua đo lường chi tiết các khu vực dùng điện trọng yếu (Significant Energy Uses — SEU) và tối ưu vận hành."
        ),
        "formula_or_spec": (
            "• Chỉ số hiệu suất năng lượng (EnPI) = SEC = kWh / Tấn sản phẩm.\n"
            "• 4 SEU lớn nhất nhà máy cáp: Động cơ kéo RBD, Điện trở nòng máy đùn, Lò ủ chuông/Bể Sauna và Hệ thống Khí nén/Chiller."
        ),
        "cadivi_application": (
            "Sân chơi ghi điểm cực mạnh cho Chuyên viên OE CADIVI: gắn đồng hồ phụ cho máy lớn, chạy hồi quy tách điện không tải, lắp áo cách nhiệt nòng đùn, lắp biến tần VFD và dịch lịch chạy lò ủ sang giờ thấp điểm!"
        ),
        "cadivi_example": (
            "Ví dụ: Áp dụng kiểm toán SEU theo ISO 50001 phát hiện 12 điểm rò khí nén + tình trạng bật nhiệt máy đùn chờ rulo 1.8h/ngày → Khắc phục tiết kiệm 145 triệu VNĐ tiền điện/tháng!"
        ),
        "related": ["SEC", "VFD", "Regression", "ISO 14001", "Extruder"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "ACSR": {
        "term": "ACSR",
        "full_name": "Aluminum Conductor Steel Reinforced — Dây Nhôm Trần Lõi Thép Truyền Tải Điện",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["ACSR", "nhôm lõi thép"],
        "case_sensitive": ["ACSR"],
        "short_desc": "Dây dẫn trần dùng cho đường dây truyền tải trên không cao thế/trung thế: lõi trong bằng sợi thép mạ kẽm chịu lực kéo căng, các lớp ngoài bện sợi nhôm dẫn điện.",
        "definition": (
            "Nhôm rất nhẹ nhưng sức bền kéo thấp nên không chịu nổi khoảng vượt cột điện xa; kết hợp lõi thép cường độ cao ở tâm và các lớp sợi nhôm bện xoắn bên ngoài tạo ra dây ACSR vừa nhẹ vừa cực bền cơ học."
        ),
        "formula_or_spec": (
            "• Cấu trúc điển hình: vd `ACSR 120/19` (120 mm² nhôm / 19 mm² lõi thép) bện trên máy Rigid Frame Strander / Tubular Strander.\n"
            "• Khối lượng riêng Nhôm = 2.703 g/cm³ | Thép = 7.80 g/cm³."
        ),
        "cadivi_application": (
            "Sản phẩm cung cấp trực tiếp cho ngành điện lực EVN tại khu vực Miền Trung – Tây Nguyên từ Nhà máy CADIVI Miền Trung. OE lưu ý kiểm soát lực căng đồng đều giữa lớp thép và lớp nhôm, và tuyệt đối cách ly phế liệu nhôm khỏi đồng!"
        ),
        "cadivi_example": (
            "Ví dụ: Kiểm soát chặt bước xoắn (Lay-up Factor) lớp nhôm ngoài dây ACSR 240/32 giúp đạt chuẩn điện trở/lực kéo đứt mà không vượt định mức nhôm 1.5%."
        ),
        "related": ["ABC Cable", "IACS", "Rigid Strander", "Lay-up Factor"],
        "doc_key": "cable_mfg_machines"
    },
    "ABC Cable": {
        "term": "ABC Cable",
        "full_name": "Aerial Bundled Cable — Cáp Nhôm Vặn Xoắn Treo Trên Không Cách Điện XLPE Đen",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["ABC Cable", "cáp ABC", "Aerial Bundled Cable"],
        "case_sensitive": [],
        "short_desc": "Cáp phân phối điện hạ thế/trung thế treo cột ngoài trời (2–4 lõi ruột nhôm bọc cách điện XLPE đen chống tia UV vặn xoắn lại, không cần vỏ bọc ngoài).",
        "definition": (
            "Cáp ABC thay thế dần dây trần ở khu dân cư/đô thị nhằm đảm bảo an toàn chống phóng điện, chống câu móc và chịu nắng mưa gió bão miền Trung nhờ lớp XLPE pha muội than (Carbon Black ≥ 2%) chống tia cực tím UV."
        ),
        "formula_or_spec": (
            "• Ký hiệu CADIVI: `ABC 4×50-0.6/1kV` (4 lõi nhôm bện nén 50 mm² bọc XLPE đen có gân nổi phân biệt pha 1, 2, 3 và trung tính).\n"
            "• Yêu cầu nhận diện pha: Đùn tạo gân nổi (Ribs) sắc nét dọc chiều dài vỏ lõi để thợ điện đấu nối đúng pha."
        ),
        "cadivi_application": (
            "Một trong những dòng sản phẩm sản lượng lớn của CADIVI Miền Trung cấp cho các công ty Điện lực miền Trung. OE tập trung tối ưu bện nén ruột nhôm (tiết kiệm XLPE), tốc độ đùn lõi và đồng bộ chiều dài 4 lõi trước ghép xoắn!"
        ),
        "cadivi_example": (
            "Ví dụ: Đồng bộ hiệu chuẩn bánh xe Encoder đo mét trên 4 lõi cáp ABC 4×50 (phân biệt rõ với phân loại tồn kho ABC trong Cycle Counting) giúp giảm mẩu cắt lệch chiều dài đuôi rulo khi ghép xoắn từ 30m xuống còn 5m/mẻ, tiết kiệm > 180 kg nhôm & nhựa XLPE đen mỗi tháng!"
        ),
        "related": ["ACSR", "XLPE", "Drum Twister", "IACS", "Over-thickness"],
        "doc_key": "cable_mfg_machines"
    },
    "Mica FR": {
        "term": "Mica FR",
        "full_name": "Fire-Resistant Mica Tape Cable (CXV/FR — IEC 60331) — Cáp Chống Cháy Quấn Băng Mica",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Mica FR", "băng Mica", "cáp chống cháy"],
        "case_sensitive": [],
        "short_desc": "Dòng cáp an toàn cao cấp quấn 2 lớp băng khoáng Mica chịu lửa quanh ruột đồng trước khi bọc XLPE/LSZH, duy trì cấp điện 90–180 phút trong đám cháy 950°C.",
        "definition": (
            "Khác với cáp chậm cháy (chỉ không lan lửa), cáp chống cháy FR bắt buộc phải TIẾP TỤC DẪN ĐIỆN khi đang bị ngọn lửa thiêu trực tiếp (cho hệ thống bơm chữa cháy, thang máy thoát hiểm, đèn khẩn cấp) nhờ lớp băng Mica cách điện ở 1,000°C."
        ),
        "formula_or_spec": (
            "• Tiêu chuẩn thử cháy: IEC 60331 (750–830°C trong 90–180 phút) / BS 6387 CWZ (950°C + phun nước + va đập).\n"
            "• Yêu cầu quấn băng Mica: Chồng mí (Overlap) ≥ 50% đều khít, không rách gãy."
        ),
        "cadivi_application": (
            "Phân khúc giá trị gia tăng rất cao của CADIVI. Băng Mica giòn dễ rách khi chạy tốc độ cao → OE kiểm soát chặt lực căng đầu quấn băng (Taping Head), cảm biến đứt băng Poka-Yoke và tốc độ chuẩn riêng."
        ),
        "cadivi_example": (
            "Ví dụ: Cân chỉnh lại phanh hãm từ & con lăn dẫn băng trên máy quấn Mica kết hợp cảm biến đứt băng dừng trong 0.5s giảm số lần đứt băng từ 8 lần/ca xuống 1 lần/ca!"
        ),
        "related": ["LSZH", "XLPE", "Poka-Yoke", "IEC 60502"],
        "doc_key": "cable_mfg_machines"
    },
    "Partial Discharge": {
        "term": "Partial Discharge",
        "full_name": "Partial Discharge (PD) Test — Thử Nghiệm Đo Phóng Điện Cục Bộ Cáp Trung/Cao Thế",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Partial Discharge", "phóng điện cục bộ"],
        "case_sensitive": [],
        "short_desc": "Phép thử bắt buộc trong phòng chắn nhiễu Faraday cho cáp trung thế XLPE nhằm phát hiện các bọt khí/khuyết tật siêu nhỏ (cỡ micromet) có thể gây nổ cáp sau vài năm vận hành.",
        "definition": (
            "Khi đặt điện áp thử cao (thường 1.73 U0 – 2 U0) lên cuộn cáp trung thế, nếu trong lớp cách điện XLPE có bọt khí li ti hoặc tạp chất dẫn điện, các tia phóng điện vi mô (đo bằng đơn vị picocoulomb — pC) sẽ xảy ra cục bộ và phá hủy dần cách điện theo thời gian."
        ),
        "formula_or_spec": (
            "• Tiêu chuẩn IEC 60502-2: Mức phóng điện cục bộ đo được tại điện áp thử phải ≤ 5 pC (thậm chí ≤ 2 pC với cáp cao thế)."
        ),
        "cadivi_application": (
            "Đầu ra kiểm chứng tối hậu chất lượng đùn 3 lớp dây chuyền CCV và độ sạch hạt nhựa XLPE/lưới lọc Screen Pack tại hệ thống nhà máy CADIVI."
        ),
        "cadivi_example": (
            "Ví dụ: Nếu 1 cuộn cáp trung thế 24kV rớt phép thử PD (> 10 pC), OE truy ngược MES ngay để kiểm tra độ ẩm/bụi phòng cấp hạt nhựa sạch và tình trạng rách lưới Screen Pack ca chạy hôm đó!"
        ),
        "related": ["CCV", "XLPE", "Screen Pack", "Water Immersion", "IEC 60502"],
        "doc_key": "cable_mfg_machines"
    },
    "Water Immersion": {
        "term": "Water Immersion",
        "full_name": "Water Immersion High-Voltage Withstand Test — Thử Cao Áp Ngâm Nước Cách Điện Cáp",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Water Immersion", "thử cao áp ngâm nước", "ngâm nước"],
        "case_sensitive": [],
        "short_desc": "Ngâm toàn bộ cuộn dây/lõi cáp trong bể nước kiểm soát nhiệt độ và đặt điện áp xoay chiều cao thế (2.5–3.5 kV+) để kiểm chứng cách điện 100% không đánh thủng.",
        "definition": (
            "Nước đóng vai trò điện cực bao phủ 100% bề mặt ngoài của dây cáp; nếu có bất kỳ điểm nứt, rỗ khí hay mỏng cách điện nào bị lọt qua Spark Tester, dòng điện cao áp sẽ đánh thủng ngay trong bể nước."
        ),
        "formula_or_spec": (
            "• Điều kiện chuẩn TCVN 6610 / IEC 60502: Ngâm nước ≥ 1 giờ ở 20±5°C → Đặt điện áp thử 2.5 kV (dây dân dụng) đến 3.5 kV (cáp 0.6/1kV) trong 5–15 phút — yêu cầu 0 đánh thủng!"
        ),
        "cadivi_application": (
            "Phép thử thường quy quan trọng tại Phòng Lab CADIVI Miền Trung; OE theo dõi Lead Time chờ ngâm nước & thử cao áp tại Lab để không làm ách tắc kho xuất hàng cuối tháng."
        ),
        "cadivi_example": (
            "Ví dụ: Lập lịch gom mẫu gửi Lab thử cao áp ngâm nước theo khung giờ cố định (10h, 15h, 21h) kết hợp chuẩn bị sẵn đầu tuốt mẫu giảm thời gian chờ cấp giấy xuất xưởng từ 6 giờ xuống 2 giờ!"
        ),
        "related": ["Spark Tester", "Partial Discharge", "IEC 60502", "Lead Time"],
        "doc_key": "cable_mfg_machines"
    },
    "IACS": {
        "term": "IACS",
        "full_name": "International Annealed Copper Standard — Chuẩn Quốc Tế Về Độ Dẫn Điện Kim Loại (% IACS)",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["IACS"],
        "case_sensitive": ["IACS"],
        "short_desc": "Thước đo độ dẫn điện quy chuẩn lấy đồng ủ tinh khiết ở 20°C làm mốc 100% IACS (đồng thanh tốt đạt 100.5–101.5% IACS; nhôm kỹ thuật đạt ~61% IACS).",
        "definition": (
            "Độ tinh khiết kim loại và chất lượng ủ quyết định trực tiếp % IACS. Đồng nhập khẩu có % IACS càng cao (vd: 101.2% thay vì 99.8%) thì điện trở suất càng thấp — cho phép nhà máy thiết kế đường kính sợi đồng gọn hơn mà vẫn dư chuẩn IEC 60228!"
        ),
        "formula_or_spec": (
            "• Mốc 100% IACS tương ứng điện trở suất 0.017241 Ω·mm²/m ở 20°C.\n"
            "• Tăng +1% IACS độ tinh khiết đồng cho phép tiết kiệm ~1% khối lượng đồng tiêu hao (giảm Copper Give-away)!"
        ),
        "cadivi_application": (
            "OE CADIVI phân tích tương quan giữa % IACS của từng nhà cung ứng đồng rod đầu vào với bài toán Copper Give-away để tham mưu cho phòng Mua hàng chọn nhà cung ứng có tổng chi phí sở hữu (TCO) thấp nhất."
        ),
        "cadivi_example": (
            "Ví dụ: Đồng rod nhà cung ứng A đắt hơn 0.3% nhưng đạt 101.3% IACS (so với B chỉ 99.9% IACS) → Dùng đồng A giúp kéo gọn hơn 1.2% khối lượng đồng/km, tính ra LÃI RÒNG thêm 0.9% tổng chi phí đồng!"
        ),
        "related": ["IEC 60228", "Copper Give-away", "Annealing", "Kelvin Bridge", "ACSR"],
        "doc_key": "cable_mfg_machines"
    },
    "PCD": {
        "term": "PCD",
        "full_name": "Polycrystalline Diamond Die — Khuôn Kéo Sợi Kim Cương Nhân Tạo Đa Tinh Thể",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["PCD", "khuôn PCD", "khuôn kéo"],
        "case_sensitive": ["PCD"],
        "short_desc": "Khuôn kéo lõi kim cương nhân tạo siêu cứng dùng trong máy kéo đồng/nhôm — quyết định trực tiếp độ bóng sợi, tỷ lệ đứt sợi và mức dư đồng Copper Give-away.",
        "definition": (
            "Mỗi dây chuyền kéo có 9 đến 24 cấp khuôn PCD giảm đường kính liên tục. Theo thời gian kéo hàng chục tấn kim loại ở tốc độ 20–35 m/s, lỗ khuôn bị mài mòn rộng ra hoặc xước hình oval — nếu chậm thay/đánh bóng lại sẽ gây đứt sợi và kéo thừa đường kính đồng."
        ),
        "formula_or_spec": (
            "• Góc côn giảm tiết diện (Reduction Angle): Đồng thường 16–18° | Nhôm 18–22°.\n"
            "• Khi khuôn mòn vượt dung sai đường kính → Mang đi mài mở rộng lên cỡ khuôn lớn hơn kế tiếp (Die Re-polishing) để tái sử dụng nhiều vòng đời!"
        ),
        "cadivi_application": (
            "Quản lý vòng đời bộ khuôn PCD theo sản lượng tấn kéo (PM) tại xưởng Kéo CADIVI là đòn bẩy số 1 chống cả 2 tổn thất lớn nhất: Đứt sợi (OEE) và Copper Give-away (BOM)."
        ),
        "cadivi_example": (
            "Ví dụ: Đánh mã số quản lý từng viên khuôn PCD trên Excel/MES, quy định rút mài lại ngay khi kéo đủ 40 tấn đồng hoặc đường kính chạm +0.006mm giúp tiết kiệm > 300 triệu/tháng tiền đồng dư!"
        ),
        "related": ["RBD", "Multi-wire", "Copper Give-away", "Drawing Emulsion", "TPM"],
        "doc_key": "cable_mfg_machines"
    },
    "Drawing Emulsion": {
        "term": "Drawing Emulsion",
        "full_name": "Wire Drawing Emulsion — Dung Dịch Nhũ Tương Bôi Trơn & Làm Mát Kéo Dây",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Drawing Emulsion", "nhũ tương"],
        "case_sensitive": [],
        "short_desc": "Hỗn hợp dầu tổng hợp/khoáng pha nước tuần hoàn trong máy kéo đồng/nhôm giúp giảm ma sát qua khuôn PCD, giải nhiệt và cuốn trôi mạt kim loại mịn.",
        "definition": (
            "Ma sát khi kéo đồng tốc độ 30 m/s sinh nhiệt cực lớn. Dung dịch nhũ tương phải được kiểm soát chặt 4 thông số: Nồng độ (%), Độ pH, Nhiệt độ (°C) và Độ sạch (lọc mạt đồng mịn); sai lệch bất kỳ thông số nào cũng làm cháy khuôn, xước sợi và đứt dây hàng loạt."
        ),
        "formula_or_spec": (
            "• Ngưỡng kiểm soát điển hình (Kéo đồng RBD): Nồng độ 7–10% | pH 7.8–8.8 | Nhiệt độ 35–42°C | Tuyệt đối dùng hệ bể riêng cho Đồng và Nhôm!"
        ),
        "cadivi_application": (
            "Đưa kiểm tra khúc xạ kế nồng độ, pH và nhiệt độ bể nhũ tương vào bảng kiểm Bảo trì tự quản (Jishu Hozen) hàng ngày của xưởng Kéo CADIVI."
        ),
        "cadivi_example": (
            "Ví dụ: Gắn thêm máy lọc ly tâm tách mạt đồng mịn cho bể nhũ tương RBD vừa giảm 60% lỗi đứt sợi do xước khuôn, vừa kéo dài tuổi thọ dầu từ 3 lên 7 tháng (tiết kiệm kép + chuẩn ISO 14001)."
        ),
        "related": ["RBD", "PCD", "ISO 14001", "TPM"],
        "doc_key": "cable_mfg_machines"
    },
    "Pay-off": {
        "term": "Pay-off",
        "full_name": "Pay-Off & Dancer Tension Control — Cụm Nhả Dây Đầu Vào & Bộ Giữ Lực Căng",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Pay-off", "Dual Pay-off", "Dancer"],
        "case_sensitive": [],
        "short_desc": "Cụm xả cuộn đồng/rulo đầu vào dây chuyền (loại đơn hoặc kép Dual Pay-off) kết hợp tay cân lực căng Dancer giúp sợi vào máy đùn/bện êm, không giật đứt.",
        "definition": (
            "Lực căng đầu vào dao động sẽ làm dây đồng bị co giãn lúc to lúc nhỏ, khiến máy đùn bọc ra đường kính vỏ lượn sóng và dễ đứt sợi nhôm/đồng mềm. Cụm Dual Pay-off (2 vị trí rulo) cho phép hàn nối sẵn đuôi cuộn 1 với đầu cuộn 2 để chạy xuyên suốt không dừng máy!"
        ),
        "formula_or_spec": (
            "• Cấu hình tối ưu SMED cho dây dân dụng: Dual Pay-off + Butt Welder + Accumulator → Thời gian dừng thay rulo đầu vào = 0 giây!"
        ),
        "cadivi_application": (
            "Áp dụng trên các dây chuyền đùn nhanh dây VC/VCm tại CADIVI Miền Trung để xóa sạch 20–30 phút/ca dừng thay rulo đồng cấp liệu."
        ),
        "cadivi_example": (
            "Ví dụ: Khai thác đúng tính năng Dual Pay-off kết hợp hàn nối đầu cuộn trên máy đùn số 1 giúp xóa 24 phút dừng thay rulo/ca, nâng Availability từ 80% lên 85.3% ngay lập tức!"
        ),
        "related": ["Take-up", "Accumulator", "Butt Welder", "Extruder", "SMED"],
        "doc_key": "cable_mfg_machines"
    },
    "Take-up": {
        "term": "Take-up",
        "full_name": "Dual Automatic Take-Up / Portal Take-Up — Cụm Thu Cuộn Thành Phẩm Tự Động",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Take-up", "Dual Take-up", "Portal Take-up"],
        "case_sensitive": [],
        "short_desc": "Cụm cuối dây chuyền cuộn cáp gọn gàng vào rulo theo bước rải dây (Traverse); loại Dual Automatic tự cắt & chuyển sang rulo rỗng không cần dừng máy đùn.",
        "definition": (
            "Đối với dây dân dụng chạy 300–800 m/phút, nếu mỗi khi đầy 1 rulo lại phải giảm tốc dừng máy để thay rulo sẽ mất rất nhiều thời gian và tạo phế startup. Dual Automatic Take-up tự động gạt dây sang trục rulo số 2 ở tốc độ cao, tăng OEE vượt trội."
        ),
        "formula_or_spec": (
            "• Lưu ý kỹ thuật: Chỉnh chuẩn bộ rải dây (Traverse Pitch) để các lớp cáp xếp khít phẳng trên rulo, không bị kẹt rãnh làm đứt dây khi xả ra ở công đoạn sau!"
        ),
        "cadivi_application": (
            "Chuẩn hóa kích cỡ rulo thu theo bội số đơn hàng (Cut-Length) trên cụm Dual Take-up và Portal Take-up (loại cổng nâng thủy lực cho rulo cáp lực 3–5 tấn) tại CADIVI."
        ),
        "cadivi_example": (
            "Ví dụ: Đồng bộ chiều dài tự cắt chuyển rulo trên Dual Take-up đúng 4,000m (bội số chẵn 40 cuộn × 100m) giúp tổ đóng cuộn phía sau không bao giờ bị dư mẩu lẻ 45m cuối rulo!"
        ),
        "related": ["Pay-off", "Accumulator", "Cut-Length", "Extruder", "OEE"],
        "doc_key": "cable_mfg_machines"
    },
    "Accumulator": {
        "term": "Accumulator",
        "full_name": "Wire / Cable Accumulator — Bộ Tích Dây Đệm Cho Phép Chạy Không Dừng Máy",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Accumulator", "bộ tích dây"],
        "case_sensitive": [],
        "short_desc": "Giàn bánh ròng rọc di động chứa sẵn 50–150 mét dây đệm, tự động nhả dây nuôi máy đùn trong 15–30 giây lúc thợ hàn nối cuộn đầu vào hoặc sang rulo đầu ra.",
        "definition": (
            "Accumulator đóng vai trò như 'bể chứa điều hòa' trên dây chuyền đùn/kéo liên tục: khi đầu vào dừng 20 giây để hàn nối cuộn đồng mới, giàn ròng rọc thu lại nhả dây đệm ra để máy đùn vẫn chạy đều tốc độ 300 m/phút không hề bị gián đoạn!"
        ),
        "formula_or_spec": (
            "• Thời gian đệm khả dụng (giây) = Tổng chiều dài dây tích trữ (m) / Tốc độ máy (m/giây)."
        ),
        "cadivi_application": (
            "Kết hợp giữa Dual Pay-off và Máy đùn tại CADIVI giúp loại bỏ hoàn toàn phế startup mỗi lần hết rulo đồng đầu vào (vì không phải dừng-chạy lại máy đùn!)."
        ),
        "cadivi_example": (
            "Ví dụ: Bộ Accumulator chứa 120m dây trên máy đùn chạy 240 m/phút (4 m/s) cho thợ 30 giây thoải mái bấm hàn nối cuộn mới mà máy đùn không mất 1 mét phế khởi động nào!"
        ),
        "related": ["Pay-off", "Take-up", "Butt Welder", "Extruder", "OEE"],
        "doc_key": "cable_mfg_machines"
    },
    "Screen Pack": {
        "term": "Screen Pack",
        "full_name": "Screen Pack & Breaker Plate — Lưới Lọc Cặn & Tấm Chặn Tạo Áp Đầu Máy Đùn",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Screen Pack", "Breaker Plate", "lưới lọc"],
        "case_sensitive": [],
        "short_desc": "Bộ lưới thép mịn (vd: 40/80/100 mesh) đặt trước đầu chữ thập máy đùn giúp chặn dị vật/hạt nhựa chưa chảy và tạo áp suất ngược làm dẻo hóa nhựa đồng đều.",
        "definition": (
            "Nếu Screen Pack bị tắc bẩn, áp suất đầu đùn tăng vọt làm giảm sản lượng kg/giờ, tăng nhiệt ma sát gây cháy nhựa PVC và buộc phải dừng máy tháo thay. Nếu lưới bị rách, tạp chất chui thẳng vào lớp cách điện gây lỗi thủng Spark Tester & rớt PD!"
        ),
        "formula_or_spec": (
            "• Chỉ dấu cần thay lưới: Áp suất đầu đùn (Head Pressure) tăng quá +25–30% so với mốc lưới sạch.\n"
            "• Giải pháp SMED/OEE: Dùng bộ đổi lưới nhanh (Hydraulic Screen Changer) hoặc thay định kỳ theo tấn nhựa đúng lúc đổi mã!"
        ),
        "cadivi_application": (
            "Tích hợp lịch thay Screen Pack đúng vào lần đổi mã SMED tại CADIVI để không bị dừng đột xuất giữa mẻ chạy cáp dài, đồng thời quản lý tồn kho lưới bằng Two-Bin Kanban."
        ),
        "cadivi_example": (
            "Ví dụ: Gộp thao tác thay Screen Pack vào đúng lần đổi màu cuối ca (thay vì chờ nghẹt mới dừng giữa ca) giúp giảm 15 phút Downtime đột xuất và giảm 40% lỗi tạp chất Spark!"
        ),
        "related": ["Extruder", "Crosshead", "Spark Tester", "Partial Discharge", "Two-Bin Kanban"],
        "doc_key": "cable_mfg_machines"
    },
    "Masterbatch": {
        "term": "Masterbatch",
        "full_name": "Color Masterbatch Dosing — Công Nghệ Cấp Hạt Màu Đậm Đặc Trực Tiếp Tại Cổ Phễu Đùn",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Masterbatch"],
        "case_sensitive": [],
        "short_desc": "Sử dụng 1 loại nhựa nền tự nhiên duy nhất + bộ định lượng trộn 1–3% hạt màu đậm đặc ngay cổ trục vít, giúp giảm 70% tồn kho màu và tăng tốc đổi màu SMED.",
        "definition": (
            "Thay vì mua và trữ tồn kho riêng 10 loại bao nhựa PVC pha sẵn 10 màu khác nhau, nhà máy chỉ cần trữ PVC nền tự nhiên số lượng lớn và gắn phễu định lượng (Gravimetric/Volumetric Doser) rải 1–3% hạt màu Masterbatch đúng tỷ lệ ngay cổ máy đùn."
        ),
        "formula_or_spec": (
            "• Tỷ lệ pha điển hình: 1.0% – 3.0% Masterbatch + 97–99% nhựa nền tự nhiên (Natural PVC/PE)."
        ),
        "cadivi_application": (
            "Cực kỳ tối ưu cho xưởng dây dân dụng đa màu (Đỏ, Vàng, Xanh, Trắng, Đen, Vàng-Xanh) tại CADIVI Miền Trung: vừa giảm vốn tồn kho nhựa, vừa cắt giảm mạnh nhựa xả Purging khi đổi màu!"
        ),
        "cadivi_example": (
            "Ví dụ: Chuyển từ PVC pha màu sẵn sang nhựa nền + Masterbatch trên 2 máy đùn dây dân dụng giúp giảm từ 14 mã tồn kho nhựa xuống còn 2 mã nhựa nền và rút thời gian đổi màu thêm 35%!"
        ),
        "related": ["Color Sequencing", "Purging", "SMED", "Extruder", "PVC"],
        "doc_key": "smed"
    },
    "Cooling Trough": {
        "term": "Cooling Trough",
        "full_name": "Multi-Stage Cooling Trough & Chiller — Máng Nước Làm Mát Nhiều Vùng Sau Đầu Đùn",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Cooling Trough", "máng làm mát", "Chiller"],
        "case_sensitive": [],
        "short_desc": "Hệ thống máng nước tuần hoàn (dài 10–30m) nối Chiller/Tháp giải nhiệt làm nguội nhanh lớp nhựa sau khi ra khỏi đầu đùn trước khi qua Capstan & Spark Tester.",
        "definition": (
            "Khả năng giải nhiệt của máng nước thường là GIỚI HẠN VẬT LÝ quyết định tốc độ chạy tối đa (m/phút) của dây chuyền đùn! Với nhựa XLPE/PE dày, vùng 1 phải dùng nước ấm (50–65°C) rồi giảm dần xuống nước lạnh (≤ 25°C) để tránh sốc nhiệt gây co rút và rỗ khí bên trong."
        ),
        "formula_or_spec": (
            "• Mốc vận hành chuẩn mùa nóng miền Trung: Nhiệt độ nước lạnh hồi về Chiller/máng cuối phải ≤ 25°C; nếu vọt lên 35–40°C công nhân buộc phải giảm tốc độ đùn 15–20% (tụt Performance OEE!)."
        ),
        "cadivi_application": (
            "Đặc biệt nhạy cảm vào mùa hè nắng nóng tại Đà Nẵng (nhiệt độ xưởng > 36°C): OE kiểm tra định kỳ hiệu suất Tháp giải nhiệt/Chiller và tẩy cáu cặn bộ trao đổi nhiệt để giữ vững tốc độ đùn chuẩn."
        ),
        "cadivi_example": (
            "Ví dụ: Vệ sinh tẩy cáu cặn tháp giải nhiệt & hiệu chỉnh van Chiller kéo nhiệt độ nước máng từ 37°C xuống 23°C giúp máy đùn VC 2.5 nâng tốc độ ổn định từ 300 lên 335 m/phút (+11.6% sản lượng ca!)."
        ),
        "related": ["Extruder", "OEE", "Capstan", "Scatter", "XLPE"],
        "doc_key": "cable_mfg_machines"
    },
    "Tensile": {
        "term": "Tensile",
        "full_name": "Universal Tensile Testing Machine — Máy Thử Kéo Đứt & Độ Giãn Dài Vạn Năng",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Tensile", "Elongation", "độ giãn dài", "kéo đứt"],
        "case_sensitive": [],
        "short_desc": "Thiết bị Lab QA/QC đo lực kéo đứt (MPa / N/mm²) và độ giãn dài (%) của sợi đồng/nhôm sau ủ và mẫu vỏ nhựa PVC/XLPE trước & sau lão hóa nhiệt.",
        "definition": (
            "Máy kéo vạn năng kẹp 2 đầu mẫu sợi kim loại hoặc mẫu quả tạ nhựa cắt từ vỏ cáp rồi kéo giãn với tốc độ chuẩn cho đến khi đứt, ghi lại biểu đồ Ứng suất – Biến dạng để kiểm chuẩn cơ tính theo IEC 60811 / IEC 60228."
        ),
        "formula_or_spec": (
            "• Tham khảo chuẩn: Sợi đồng ủ mềm giãn dài ≥ 20–30% | Nhựa PVC cách điện: Tensile ≥ 12.5 MPa, Elongation ≥ 150% | Nhựa XLPE: Tensile ≥ 12.5 MPa, Elongation ≥ 200%."
        ),
        "cadivi_application": (
            "Nếu kết quả Tensile/Elongation sợi đồng thấp → báo lỗi ủ đồng non; nếu mẫu nhựa PVC giòn giãn dài kém → kiểm tra ngay nhiệt độ đùn quá cao làm cháy phân hủy hoặc trộn quá nhiều nhựa tái chế!"
        ),
        "cadivi_example": (
            "Ví dụ: Phát hiện độ giãn dài vỏ PVC tụt xuống 135% (gần rớt chuẩn 150%) trên máy đùn số 3 → Truy ngược dữ liệu SCADA thấy vùng nhiệt 4 chạy thừa +15°C làm giòn nhựa, chỉnh lại lập tức đạt 210%!"
        ),
        "related": ["Aging Oven", "Annealing", "IEC 60502", "PVC", "XLPE"],
        "doc_key": "cable_mfg_machines"
    },
    "Aging Oven": {
        "term": "Aging Oven",
        "full_name": "Thermal Aging Oven — Tủ Sấy Lão Hóa Nhiệt Kiểm Tra Tuổi Thọ Vật Liệu Cách Điện",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Aging Oven", "lão hóa nhiệt", "tủ lão hóa"],
        "case_sensitive": [],
        "short_desc": "Tủ sấy tuần hoàn không khí chính xác cao (80–150°C trong 7 ngày) mô phỏng tuổi thọ vận hành 20–30 năm của vỏ nhựa PVC/XLPE theo chuẩn IEC 60811.",
        "definition": (
            "Mẫu nhựa cắt từ cáp được đặt trong Aging Oven ở nhiệt độ cao nhiều ngày liên tục để kiểm tra mức suy giảm lực kéo đứt và độ giãn dài sau lão hóa (không được thay đổi quá ±20–25% so với trước lão hóa), bảo đảm cáp CADIVI bền bỉ hàng chục năm."
        ),
        "formula_or_spec": (
            "• Chuẩn thử phổ biến: PVC ở 80–100°C × 168 giờ (7 ngày) | XLPE ở 135°C × 168 giờ.\n"
            "• Độ biến thiên độ bền kéo & giãn dài sau lão hóa phải nằm trong khoảng ±20% đến ±25%."
        ),
        "cadivi_application": (
            "OE lưu ý khi đánh giá đổi nhà cung ứng hạt nhựa giá rẻ (Cost Reduction): TUYỆT ĐỐI không chỉ nhìn rẻ hơn 5% mà phải chờ đủ kết quả Aging Oven & Hot Set Test đạt chuẩn 100% mới phê duyệt thay đổi BOM!"
        ),
        "cadivi_example": (
            "Ví dụ: Khi thử nghiệm công thức nhựa PVC mới tiết kiệm 4% giá thành, phép thử Aging Oven 7 ngày giúp phát hiện nhựa mới mất hóa dẻo quá nhanh sau lão hóa → Chặn kịp rủi ro khiếu nại hàng loạt!"
        ),
        "related": ["Tensile", "Hot Set Test", "PVC", "XLPE", "IEC 60502"],
        "doc_key": "cable_mfg_machines"
    },
    "VFD": {
        "term": "VFD",
        "full_name": "Variable Frequency Drive (Inverter) — Biến Tần Điều Khiển Tốc Độ & Tiết Kiệm Điện Động Cơ",
        "category": "An Toàn Công Nghiệp, EHS & Tiêu Chuẩn ISO",
        "aliases": ["VFD", "Inverter", "biến tần"],
        "case_sensitive": ["VFD"],
        "short_desc": "Thiết bị điện tử công suất điều chỉnh tần số cấp cho động cơ xoay chiều để điều tốc mượt (máy kéo/đùn/bện) và tiết kiệm 20–40% điện cho bơm nước/quạt/máy nén khí.",
        "definition": (
            "Theo định luật đồng dạng bơm-quạt, công suất điện tiêu thụ tỷ lệ với LẬP PHƯƠNG tốc độ quay (P ~ n³). Chỉ cần dùng VFD giảm tốc độ quạt tháp giải nhiệt hay bơm nước làm mát xuống 80% khi tải nhẹ, điện năng tiêu thụ giảm ngay gần 50%!"
        ),
        "formula_or_spec": (
            "• Định luật bơm/quạt: Giảm 20% tốc độ (0.8n) → Công suất điện = 0.8³ = 0.512 (tiết kiệm tới ~48.8% điện năng!)."
        ),
        "cadivi_application": (
            "Dự án CAPEX tiết kiệm năng lượng (ISO 50001) có thời gian hoàn vốn cực nhanh (8–14 tháng) tại CADIVI: lắp VFD cho máy nén khí trục vít, bơm tuần hoàn nước máng đùn và quạt tháp giải nhiệt."
        ),
        "cadivi_example": (
            "Ví dụ: Đầu tư 180 triệu lắp biến tần VFD cho hệ thống bơm nước giải nhiệt 55 kW và quạt tháp giải nhiệt chạy non tải ca đêm giúp giảm 28% điện bơm, hoàn vốn chỉ sau 9.5 tháng!"
        ),
        "related": ["ISO 50001", "SEC", "CAPEX", "Payback", "Cooling Trough"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "Standard Cost": {
        "term": "Standard Cost",
        "full_name": "Standard Costing & Cost Variance — Kế Toán Giá Thành Định Mức & Phân Tách Biến Động Chi Phí",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["Standard Cost", "Standard Costing", "Cost Variance", "Absorption", "Overhead"],
        "case_sensitive": [],
        "short_desc": "Hệ thống giá thành mục tiêu (NVL chuẩn + Nhân công chuẩn + Định phí Overhead chuẩn) dùng để đối chiếu thực tế cuối tháng thành 3 cột: Giá mua (Price), Định mức (Usage) và Sản lượng hấp thụ (Absorption).",
        "definition": (
            "Standard Cost là cầu nối ngôn ngữ giữa Chuyên viên OE và phòng Kế toán Giá thành. Nó giúp tách bạch rõ yếu tố khách quan thị trường (giá đồng LME tăng) khỏi yếu tố vận hành nội bộ xưởng (hao phí đồng/nhựa, OEE/OLE tụt)."
        ),
        "formula_or_spec": (
            "• Total Variance = Price Variance (Mua hàng) + Usage/Efficiency Variance (Xưởng & OE) + Volume/Absorption Variance (Công suất OEE)."
        ),
        "cadivi_application": (
            "Giúp OE CADIVI chủ động đọc báo cáo P&L / Giá thành xưởng hàng tháng cùng Kế toán, bảo vệ xưởng trước biến động giá đồng LME và tập trung dự án cải tiến vào đúng khoản Usage Variance lớn nhất."
        ),
        "cadivi_example": (
            "Ví dụ: Tháng 10 giá thành cáp CXV tăng +6%: OE bóc tách +4.8% do giá đồng LME tăng (Price Variance), +1.2% do phế đồng dính nhựa & nhựa Over-thickness (Usage Variance) → Đề xuất đúng dự án cắt phần +1.2% này!"
        ),
        "related": ["BOM", "ROI", "Copper Give-away", "Over-thickness", "OEE"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "Hoshin Kanri": {
        "term": "Hoshin Kanri",
        "full_name": "Hoshin Kanri & Catchball — Triển Khai Chiến Lược Liên Kết Từ Tổng Công Ty Xuống Phân Xưởng",
        "category": "Kỹ Năng Phỏng Vấn & Quản Trị Thay Đổi",
        "aliases": ["Hoshin Kanri", "Catchball", "X-Matrix"],
        "case_sensitive": [],
        "short_desc": "Hệ thống 'kim chỉ nam' biến mục tiêu chiến lược 1–3 năm của Ban Lãnh đạo thành kế hoạch dự án OE và KPI hàng ngày ở từng phân xưởng thông qua đối thoại 2 chiều Catchball.",
        "definition": (
            "Nhiều nhà máy có chiến lược rất hay ở phòng họp nhưng xuống phân xưởng mỗi tổ lại chạy một hướng khác nhau. Hoshin Kanri dùng bảng X-Matrix liên kết chặt: Mục tiêu dài hạn ↔ Mục tiêu năm ↔ Dự án OE đột phá ↔ KPI đo lường ↔ Người chịu trách nhiệm."
        ),
        "formula_or_spec": (
            "• Cơ chế Catchball (Tung – Hứng bóng): Lãnh đạo nêu đích đến (What) → Quản đốc/OE đề xuất cách làm & nguồn lực khả thi (How) → Thống nhất cam kết 2 chiều."
        ),
        "cadivi_application": (
            "Mô hình phối hợp chuẩn giữa khối OE Tổng công ty CADIVI với Ban Giám đốc Nhà máy CADIVI Miền Trung và các Quản đốc phân xưởng Kéo – Bện – Đùn."
        ),
        "cadivi_example": (
            "Ví dụ: Mục tiêu năm của Công ty 'Giảm 8% chi phí chuyển đổi & hao phí' được phân rã qua Catchball thành 3 dự án cụ thể tại Nhà máy Miền Trung: SMED máy đùn (-3%), giảm Over-thickness (-3%) và nâng OLE đóng cuộn (-2%)."
        ),
        "related": ["OE", "KPI", "ADKAR", "A3", "PDCA"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "ADKAR": {
        "term": "ADKAR",
        "full_name": "ADKAR Change Management Model — Mô Hình 5 Bước Quản Trị Thay Đổi Con Người",
        "category": "Kỹ Năng Phỏng Vấn & Quản Trị Thay Đổi",
        "aliases": ["ADKAR", "Change Management"],
        "case_sensitive": ["ADKAR"],
        "short_desc": "5 nấc tâm lý bắt buộc để giải tỏa phản kháng của Quản đốc & công nhân khi áp dụng quy trình mới: Awareness – Desire – Knowledge – Ability – Reinforcement.",
        "definition": (
            "70% dự án Lean/MES thất bại không phải vì kỹ thuật sai mà vì CON NGƯỜI phản kháng thay đổi. Mô hình ADKAR (Prosci) giúp Chuyên viên OE chẩn đoán chính xác người xưởng đang vướng ở khâu nào (chưa hiểu lý do, chưa muốn làm hay chưa biết cách làm) để gỡ đúng nút."
        ),
        "formula_or_spec": (
            "• A (Nhận thức lý do) → D (Mong muốn qua Quick-Win) → K (Kiến thức qua TWI/SOP) → A (Thực hành kèm cặp) → R (Củng cố qua Audit & Thưởng)."
        ),
        "cadivi_application": (
            "Bí quyết thành công cho Chuyên viên OE mới vào CADIVI khi làm việc với các Quản đốc/thợ đứng máy 15–20 năm kinh nghiệm: không ép lý thuyết mà tạo Quick-Win gỡ vất vả cho họ trước (Desire) rồi đồng hành cùng đứng tên thành tích!"
        ),
        "cadivi_example": (
            "Ví dụ: Khi thợ máy đùn ngại ghi mã dừng máy mới, OE rút gọn thao tác xuống chỉ quét 1 phát Barcode (giảm gánh nặng) + chứng minh dữ liệu đó giúp Bảo trì sửa nhanh lỗi máy họ hay kêu ca → Tỷ lệ tuân thủ đạt 98% sau 2 tuần!"
        ),
        "related": ["Hoshin Kanri", "TWI", "Genba", "Kaizen", "STAR"],
        "doc_key": "planning_quality_ehs_cost"
    },
    "Visual Management": {
        "term": "Visual Management",
        "full_name": "Visual Management & Shadow Board — Quản Trị Trực Quan Hiện Trường & Bảng Bóng Dụng Cụ",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Visual Management", "Shadow Board", "quản trị trực quan"],
        "case_sensitive": [],
        "short_desc": "Biến phân xưởng thành không gian 'tự biết nói': nhìn 3 giây thấy ngay trạng thái Xanh/Đỏ, mức tồn kho Min/Max, vạch sơn sàn và thiếu dụng cụ nào trên bảng Shadow Board.",
        "definition": (
            "Quản trị trực quan là nguyên lý trung tâm của 5S và Lean: làm cho chuẩn mực và bất thường hiển thị rõ ràng bằng màu sắc, vạch kẻ, đồng hồ giới hạn Xanh–Đỏ và bảng SQDC để không cần hỏi hay lật sổ mới biết máy đang ổn hay đang lỗi."
        ),
        "formula_or_spec": (
            "• Quy tắc 3 giây – 3 mét: Đứng cách xa 3 mét, trong vòng 3 giây phải biết ngay trạm đó có đang ĐẠT chuẩn hay có BẤT THƯỜNG!"
        ),
        "cadivi_application": (
            "Triển khai ngay trong 30–60 ngày đầu tại CADIVI: Shadow Board bộ cờ lê/Chày-Cối cạnh máy đùn, vạch xanh/đỏ trên đồng hồ áp suất & nhiệt độ nước máng, bảng SQDC tổ và vạch giới hạn ô siêu thị rulo."
        ),
        "cadivi_example": (
            "Ví dụ: Sơn vạch xanh (20–25°C) và đỏ (>28°C) ngay trên đồng hồ nhiệt độ nước máng làm mát giúp bất kỳ công nhân hay Quản đốc đi ngang qua cũng phát hiện ngay Chiller gặp sự cố trong 2 giây!"
        ),
        "related": ["5S", "Andon", "KPI", "SMED", "Kanban"],
        "doc_key": "lean_muda"
    },
    "Downtime": {
        "term": "Downtime",
        "full_name": "Planned vs Unplanned Downtime — Thời Gian Dừng Máy Kế Hoạch & Đột Xuất",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Downtime", "dừng máy", "Minor Stoppage", "Micro-stop"],
        "case_sensitive": [],
        "short_desc": "Mọi khoảng thời gian máy ngừng tạo ra sản phẩm trong ca làm việc — được phân mã rõ ràng (Đổi mã SMED, Hỏng máy, Đứt sợi, Chờ vật tư, Lỗi Spark) để vẽ Pareto tấn công.",
        "definition": (
            "Downtime chia làm 2 nhóm lớn: Dừng kế hoạch (ăn ca, bảo trì PM định kỳ — trừ khỏi mẫu số OEE) và Dừng ngoài kế hoạch (Breakdown, Setup/Đổi màu, Thiếu rulo — trừ thẳng vào Availability của OEE). Các cú dừng < 5 phút gọi là Vi dừng (Minor Stoppage / Micro-stop) làm tụt Performance."
        ),
        "formula_or_spec": (
            "• Availability = (Planned Production Time - Unplanned Downtime) / Planned Production Time."
        ),
        "cadivi_application": (
            "Nhiệm vụ nền tảng của OE CADIVI trong tháng đầu: chuẩn hóa bảng 12–15 Mã Lý Do Dừng Máy (Downtime Reason Codes) ngắn gọn thống nhất giữa Kéo – Bện – Đùn để chống tình trạng ghi chung chung 'Chờ kế hoạch'."
        ),
        "cadivi_example": (
            "Ví dụ: Sau khi tách rõ mã 'Dừng đổi màu', 'Dừng thay rulo', 'Dừng đứt sợi' và 'Dừng chờ xe nâng', báo cáo Pareto chỉ đích danh 20% Downtime máy đùn là do chờ xe nâng chứ không phải hỏng máy!"
        ),
        "related": ["OEE", "Six Big Losses", "Pareto", "SMED", "MTTR"],
        "doc_key": "oee"
    },
    "Scrap": {
        "term": "Scrap",
        "full_name": "Scrap & Rework — Phế Phẩm Hủy Bỏ & Hàng Lỗi Phải Làm Lại",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["Scrap", "Rework", "Scrap Rate", "phế phẩm"],
        "case_sensitive": [],
        "short_desc": "Vật tư/sản phẩm không đạt tiêu chuẩn phải cắt loại (Scrap) hoặc tốn thêm công/máy để sang cuộn cắt nối sửa lại (Rework) — khoản thất thoát trực tiếp nặng nhất ngành cáp.",
        "definition": (
            "Trong ngành dây cáp điện, Scrap bắt buộc phải chia rõ 3 giỏ riêng: (1) Phế đồng trần (thu hồi ~94%), (2) Phế đồng dính nhựa (chỉ thu hồi ~75–82%, lỗ cực nặng!) và (3) Phế nhựa xả Purging/startup. Rework (cuộn lại cắt bỏ đoạn Spark) làm lãng phí kép cả giờ máy lẫn nhân công OLE."
        ),
        "formula_or_spec": (
            "• Scrap Rate (%) = [ Khối lượng (hoặc mét) Phế phẩm / Tổng Khối lượng (hoặc mét) Đưa vào SX ] × 100%."
        ),
        "cadivi_application": (
            "Thiết lập nguyên tắc 'Cân phế tại nguồn cuối mỗi ca' theo 3 thùng mã màu (Đỏ = Đồng trần, Vàng = Đồng dính nhựa, Xanh = Nhựa sạch) giúp OE CADIVI kiểm soát chính xác BOM Variance từng máy."
        ),
        "cadivi_example": (
            "Ví dụ: Tách riêng báo cáo phế đồng dính nhựa giúp phát hiện 65% lượng phế này đến từ đoạn khởi động đầu ca (Startup Scrap) trên máy đùn → Lưu Recipe chuẩn PLC giúp cắt giảm 50% lượng phế này ngay trong tháng 2!"
        ),
        "related": ["BOM", "FPY", "RTY", "Purging", "Cut-Length", "OEE"],
        "doc_key": "bom_cost"
    },
    "Work Combination Table": {
        "term": "Work Combination Table",
        "full_name": "Standardized Work Combination Table (SWCT) — Bảng Phối Hợp Thao Tác Người & Máy Chuẩn",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Work Combination Table", "SWCT", "Standardized Work"],
        "case_sensitive": ["SWCT"],
        "short_desc": "Biểu mẫu chuẩn Toyota kết hợp Thời gian thao tác tay (nét liền), Thời gian máy tự chạy (nét đứt) và Thời gian đi bộ (nét sóng) so với đường dọc Takt Time.",
        "definition": (
            "SWCT là 1 trong 3 biểu mẫu nền tảng của Công việc Chuẩn (Standardized Work — cùng với Bảng năng lực công đoạn và Sơ đồ chuẩn thao tác). Nó giúp kỹ sư IE/OE chứng minh trực quan sự tương tác giữa công nhân, máy móc và bước chân đi lại."
        ),
        "formula_or_spec": (
            "• 3 yếu tố bắt buộc của Standardized Work: (1) Takt Time, (2) Trình tự thao tác chuẩn (Work Sequence), (3) Tồn kho WIP chuẩn trên chuyền (Standard WIP)."
        ),
        "cadivi_application": (
            "Áp dụng lập bảng SWCT tại CADIVI cho các trạm bán tự động như tổ Đóng cuộn khoanh 100m (kết hợp thời gian máy tự cuộn với thời gian tay dán tem/chuẩn bị thùng) và thao tác đứng nhiều máy bện."
        ),
        "cadivi_example": (
            "Ví dụ: Vẽ SWCT cho công nhân vận hành máy cuộn tự động phát hiện trong 18 giây máy tự chạy công nhân đang đứng nhìn không làm gì → Chuyển thao tác gấp hộp & dán sẵn tem vào đúng 18 giây máy chạy đó, tăng năng suất +30%!"
        ),
        "related": ["Time Study", "Man-Machine Chart", "Takt Time", "OLE", "SOP"],
        "doc_key": "ole"
    },
    # =================================================================
    # NHÓM 8: CÔNG NGHỆ ĐÙN SÂU, ĐỨT SỢI, CÁP CHUYÊN DỤNG & OE THỰC ĐỊA
    # =================================================================
    "L/D Ratio": {
        "term": "L/D Ratio",
        "full_name": "Extruder Screw Length-to-Diameter Ratio — Tỷ Lệ Chiều Dài / Đường Kính Trục Vít Đùn & Tỷ Số Nén",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["L/D Ratio", "tỷ lệ L/D", "tỷ số nén", "Compression Ratio"],
        "case_sensitive": [],
        "short_desc": "Thông số thiết kế cốt lõi của trục vít máy đùn cáp (chiều dài L chia đường kính D), quyết định khả năng hóa dẻo, trộn đều màu và chống cháy xém nhựa.",
        "definition": (
            "Trục vít ngắn (L/D = 20:1 – 24:1, tỷ số nén thấp 2.0–2.5:1) dành cho nhựa PVC nhạy nhiệt để giảm thời gian lưu tránh cháy phân hủy HCl; "
            "còn nhựa PE/XLPE cần trục vít dài hơn (L/D = 25:1 – 30:1, có vùng Barrier/Mixing, tỷ số nén 2.8–3.5:1) để nhựa nóng chảy đồng nhất ở tốc độ cao."
        ),
        "formula_or_spec": (
            "• L/D = Chiều dài phần có rãnh trục vít (L) / Đường kính ngoài trục vít (D)\n"
            "• Compression Ratio = Thể tích rãnh vùng Nạp liệu (Feed) / Thể tích rãnh vùng Định lượng (Metering)."
        ),
        "cadivi_application": (
            "Khi nhà máy CADIVI Miền Trung muốn chuyển một máy đùn PVC sang chạy thử XLPE hoặc LSZH để giải tỏa điểm nghẽn RCCP, OE và Kỹ thuật bắt buộc kiểm tra trục vít L/D thay vì ép chạy chung gây cháy nhựa hoặc rỗ khí."
        ),
        "cadivi_example": (
            "Ví dụ: Chạy hạt LSZH (rất nhạy lực cắt nhiệt) trên trục vít PE tỷ số nén cao 3.4:1 làm nhiệt độ khối nhựa vọt quá 175°C gây rộp vỏ; đổi sang trục vít Barrier nén thấp 2.2:1 giúp tăng tốc độ đùn +28% và giảm phế Spark về 0!"
        ),
        "related": ["Extruder", "Melt Pressure", "PVC", "XLPE", "LSZH"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "Melt Pressure": {
        "term": "Melt Pressure",
        "full_name": "Extruder Melt Pressure & Melt Temperature — Áp Suất & Nhiệt Độ Nhựa Nóng Chảy Đầu Đùn",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Melt Pressure", "Melt Temperature", "Back Pressure", "áp suất nóng chảy"],
        "case_sensitive": [],
        "short_desc": "Cặp tín hiệu 'nhịp tim' đo ngay trước lưới lọc Screen Pack của máy đùn, báo sớm tình trạng nghẹt lưới, quá nhiệt cắt trượt và dao động đường kính cáp.",
        "definition": (
            "Melt Pressure (bar hoặc MPa) phản ánh lực cản dòng nhựa qua tấm lưới lọc và đầu Crosshead; Melt Temperature (°C) là nhiệt độ thực của khối nhựa (thường cao hơn nhiệt cài đặt vỏ Barrel 10–25°C do ma sát cắt của trục vít)."
        ),
        "formula_or_spec": (
            "• Ngưỡng cảnh báo: Khi Melt Pressure tăng dần +25–30% so với đầu ca ở cùng tốc độ trục vít → Lưới lọc Screen Pack đã bẩn nghẹt cần lên lịch thay!\n"
            "• Nếu Melt Pressure dao động nhịp nhàng (Surging ±15 bar) → Đường kính cáp sẽ biến thiên hình sin (Cpk tụt mạnh)."
        ),
        "cadivi_application": (
            "Kết nối cảm biến Melt Pressure & Melt Temperature lên PLC/SCADA/MES tại CADIVI để chuyển từ thay lưới lọc chữa cháy (khi đã rách lưới gây lỗi PD) sang bảo trì dự đoán theo điều kiện thực (CBM)."
        ),
        "cadivi_example": (
            "Ví dụ: Theo dõi đồ thị Melt Pressure máy đùn XLPE số 2 thấy áp suất tăng từ 180 bar lên 245 bar sau 42 giờ chạy → Lập lịch thay Screen Pack đúng cuối ca chiều trùng lần đổi mã SMED, tránh hoàn toàn sự cố dừng đột xuất giữa ca đêm!"
        ),
        "related": ["Extruder", "Screen Pack", "L/D Ratio", "CBM / PdM", "SPC"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "DDR": {
        "term": "DDR",
        "full_name": "Draw-Down Ratio (DDR) & Draw-Ratio Balance (DRB) — Tỷ Lệ Kéo Rút & Cân Bằng Kéo Màng Đùn Ống",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["DDR", "DRB", "Draw-Down Ratio", "Draw-Ratio Balance", "Tube Tooling", "Pressure Tooling"],
        "case_sensitive": ["DDR", "DRB"],
        "short_desc": "Tỷ số diện tích tiết diện vòng nhựa rời miệng cối đùn so với tiết diện lớp cách điện/vỏ thành phẩm sau khi kéo giãn — chìa khóa chọn đúng cặp Chày–Cối.",
        "definition": (
            "Trong đùn ống (Tube Tooling — dùng phổ biến cho bọc vỏ PVC/XLPE), nhựa thoát ra thành ống lớn hơn cáp rồi bị lực kéo Capstan + hút chân không kéo rút ôm sát vào lõi. Nếu DDR quá lớn, nhựa bị kéo căng quá mức gây rách, giảm độ giãn dài và co ngót đầu cáp; nếu DRB lệch khỏi 1.0, bề mặt dễ nhăn hoặc rỗ."
        ),
        "formula_or_spec": (
            "• DDR = (D_die² - D_tip²) / (D_cable² - D_core²)\n"
            "• DRB = (D_die / D_cable) / (D_tip / D_core)  (Chuẩn tối ưu: DRB = 0.95 – 1.08)\n"
            "• DDR khuyến nghị: PVC thường 1.5 – 2.5 | PE/XLPE thường 1.3 – 2.2 | LSZH thường 1.2 – 1.8."
        ),
        "cadivi_application": (
            "OE CADIVI chuẩn hóa bảng chọn cặp Chày–Cối (Tip & Die Matrix) cho từng tiết diện cáp theo DDR/DRB chuẩn để công nhân không tự ý lắp cối quá lớn gây tốn nhựa khởi động và hỏng độ bám vỏ."
        ),
        "cadivi_example": (
            "Ví dụ: Dây chuyền bọc vỏ cáp CXV 4×25 bị nứt vỏ khi thử uốn lạnh → Tính lại phát hiện đang dùng cối quá rộng (DDR = 3.6 vượt xa ngưỡng 2.2); thay đúng cối chuẩn DDR = 1.9 hết hẳn lỗi nứt và giảm nhựa Over-thickness 4%!"
        ),
        "related": ["Extruder", "Crosshead", "Sharkskin", "Over-thickness", "PVC"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "Sharkskin": {
        "term": "Sharkskin",
        "full_name": "Sharkskin / Melt Fracture — Khuyết Tật Sần Da Cá Mập & Vỡ Dòng Nhựa Khi Đùn Tốc Độ Cao",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Sharkskin", "Melt Fracture", "Bambooing", "sần da cá mập"],
        "case_sensitive": [],
        "short_desc": "Hiện tượng bề mặt vỏ cáp sần sùi như da cá mập hoặc gợn đốt tre (Bambooing) do ứng suất cắt tại miệng cối vượt giới hạn tới hạn khi tăng tốc độ đùn.",
        "definition": (
            "Khi OE cố gắng đẩy tốc độ đường dây (Performance OEE) lên quá cao mà không điều chỉnh nhiệt độ miệng cối (Die Temperature), độ nhớt nhựa tăng cao gây trượt dính bất ổn ngay mép cối đùn, tạo bề mặt nhám mờ hoặc gợn sóng mất thẩm mỹ và giảm độ bền điện môi."
        ),
        "formula_or_spec": (
            "• Nguyên nhân vật lý: Ứng suất cắt thành cối vượt ngưỡng tới hạn (> 0.1 – 0.14 MPa với PE/XLPE).\n"
            "• 3 cách xử lý chuẩn: (1) Tăng nhẹ nhiệt độ Die 5–10°C, (2) Tăng khe hở Die/DDR hợp lý, (3) Dùng phụ gia trợ gia công PPA (Polymer Processing Aid)."
        ),
        "cadivi_application": (
            "Tránh bẫy 'ép tăng tốc độ đùn lấy OEE Performance rồi làm sần vỏ gây tụt Quality' tại CADIVI; OE phối hợp Kỹ thuật công nghệ thiết lập cửa sổ công nghệ (Process Window) trên Minitab DOE."
        ),
        "cadivi_example": (
            "Ví dụ: Nâng tốc độ bọc vỏ HDPE từ 60 lên 85 m/phút xuất hiện sần Sharkskin → Tăng nhiệt miệng cối thêm +8°C và bổ sung 0.5% phụ gia PPA giúp chạy êm ở 85 m/phút, tăng sản lượng +41% với bề mặt bóng mịn!"
        ),
        "related": ["Extruder", "DDR", "Die Drool", "OEE", "DOE"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "Die Drool": {
        "term": "Die Drool",
        "full_name": "Die Drool / Die Build-up — Hiện Tượng Đóng Cặn Nhựa Cháy Tại Miệng Cối Đùn",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Die Drool", "Die Build-up", "đóng cặn miệng cối"],
        "case_sensitive": [],
        "short_desc": "Nhựa phân hủy, chất độn hoặc phụ gia tích tụ dần quanh mép ngoài cối đùn rồi bất ngờ rơi bám lên vỏ cáp đang chạy, gây cục u hoặc thủng Spark Tester.",
        "definition": (
            "Thường xảy ra khi đùn nhựa PVC độn nhiều CaCO3, nhựa LSZH chứa nhiều chất chống cháy vô cơ (ATH/MDH) hoặc hạt nhựa bị ẩm. Công nhân phải liên tục dùng dao đồng gạt cặn (nguy cơ mất an toàn & xước vỏ) hoặc dừng máy vệ sinh (giảm Availability)."
        ),
        "formula_or_spec": (
            "• Phòng ngừa gốc: Sấy khô hạt nhựa đủ giờ (Hopper Dryer), vát mép thoát miệng cối đúng góc 45°, đánh bóng gương lòng cối và dùng trục vít giảm cắt trượt."
        ),
        "cadivi_application": (
            "Nguyên nhân hàng đầu gây dừng vặt (Minor Stoppages) trên chuyền đùn vỏ PVC và cáp chống cháy LSZH tại CADIVI."
        ),
        "cadivi_example": (
            "Ví dụ: Chuyền đùn vỏ LSZH cứ 45 phút phải giảm tốc gạt cặn Die Drool làm mất 12% OEE → Đánh bóng phủ Chrome lòng cối + giảm nhiệt vùng cuối 5°C kéo dài chu kỳ chạy sạch lên > 6 giờ liên tục!"
        ),
        "related": ["Extruder", "Sharkskin", "LSZH", "CaCO3 Filler", "Hopper Dryer"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "Regrind": {
        "term": "Regrind",
        "full_name": "PVC / Polymer Regrind — Nhựa Nghiền Tái Chế Từ Phế Đầu Ca & Tỷ Lệ Pha Trộn",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["Regrind", "nhựa nghiền", "nhựa tái chế"],
        "case_sensitive": [],
        "short_desc": "Phế phẩm nhựa PVC sạch (đoạn xả purge sạch, vỏ tuốt không dính đồng) được băm nghiền thành hạt tái chế để pha lại ở tỷ lệ kiểm soát cho lớp độn hoặc vỏ ngoài phù hợp.",
        "definition": (
            "Nhựa PVC nhiệt dẻo có thể tái chế nghiền lại (Regrind), nhưng sau mỗi lần qua nhiệt, chuỗi polymer bị lão hóa một phần và dễ lẫn bụi/tạp chất. Ngược lại, nhựa XLPE sau khi lưu hóa liên kết ngang là nhựa nhiệt rắn KHÔNG thể nấu chảy đùn lại làm cách điện!"
        ),
        "formula_or_spec": (
            "• Nguyên tắc chất lượng: Tuyệt đối KHÔNG dùng Regrind cho lớp cách điện chịu điện áp cao (XLPE/cách điện chính); chỉ xét tỷ lệ pha kiểm soát (vd: 5–15% sạch cùng màu) cho lớp độn trong hoặc vỏ ngoài nếu đạt 100% thử nghiệm cơ lý Aging/Tensile theo TCVN/IEC."
        ),
        "cadivi_application": (
            "OE CADIVI quản trị phân loại sạch phế nhựa ngay tại máy đùn (tách riêng PVC sạch cùng màu vs PVC đen/bẩn vs XLPE không tái chế được) để tối ưu giá trị thu hồi phế liệu trong bài toán BOM & Standard Cost."
        ),
        "cadivi_example": (
            "Ví dụ: Thay vì đổ lẫn nhựa xả purge PVC trắng với PVC đen bẩn bán phế giá rẻ 4,000đ/kg, phân loại sạch ngay tại nguồn giúp tái sử dụng làm lớp độn trong đạt chuẩn, thu hồi giá trị tương đương 18,000đ/kg (lợi > 65 triệu/tháng)!"
        ),
        "related": ["BOM", "Scrap", "PVC", "XLPE", "Purging"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "Wire Break Forensics": {
        "term": "Wire Break Forensics",
        "full_name": "Wire Break Forensics — Phân Tích Mặt Gãy Đứt Sợi Đồng/Nhôm Để Truy Gốc Sự Cố Kéo Sợi",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Wire Break Forensics", "phân tích mặt gãy", "phân loại đứt sợi"],
        "case_sensitive": [],
        "short_desc": "Kỹ thuật soi kính lúp/kính hiển vi đầu sợi đồng bị đứt trên máy kéo RBD/Multi-wire để xác định chính xác nguyên nhân do đồng Rod đầu vào, khuôn PCD hay thao tác hàn.",
        "definition": (
            "Mỗi nguyên nhân đứt sợi để lại một 'dấu vân tay cơ học' riêng biệt trên đầu gãy: gãy chén-côn (Cup-and-Cone) do quá lực kéo/khuôn mòn/bôi trơn kém; gãy có hạt cứng tạp chất (Inclusion) hoặc vết gấp vảy đồng (Sliver/Lap) do phôi đồng Rod IQC; gãy phẳng giòn ngay mối hàn (Weld Break) do hàn đối đầu lệch tâm hoặc quên ủ mối hàn."
        ),
        "formula_or_spec": (
            "• 4 nhóm mặt gãy kinh điển: (1) Cup-and-Cone (Quá tải căng/Khuôn), (2) Inclusion/Porosity (Tạp chất phôi đồng Rod), (3) Weld Break (Mối hàn Butt Welder), (4) Chevron/Central Burst (Góc côn khuôn sai / Nhũ tương hỏng)."
        ),
        "cadivi_application": (
            "OE CADIVI thiết lập 'Bảng Mẫu Ảnh Mặt Gãy Đứt Sợi' ngay tại xưởng Kéo để tổ trưởng phân loại đúng mã nguyên nhân vào MES — chấm dứt tranh cãi giữa Xưởng Kéo, Phòng Bảo trì khuôn và Phòng Mua hàng đồng Rod."
        ),
        "cadivi_example": (
            "Ví dụ: Máy kéo Multi-wire đứt sợi tăng vọt lên 12 lần/ca (gây mất 22% OEE) → Soi kính hiển vi 20 đầu gãy thấy 75% là dạng Inclusion tạp chất oxit → Truy lô đồng Rod nhà cung cấp B, lập báo cáo 8D yêu cầu bồi thường và đổi lô ngay!"
        ),
        "related": ["Cup-and-Cone", "RBD", "Multi-wire", "PCD", "ASTM B49", "Drawing Emulsion"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "Cup-and-Cone": {
        "term": "Cup-and-Cone",
        "full_name": "Cup-and-Cone Ductile Fracture — Mặt Gãy Dẻo Hình Chén–Côn Khi Kéo Sợi Quá Lực Căng",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Cup-and-Cone", "chén-côn", "chén côn"],
        "case_sensitive": [],
        "short_desc": "Dạng gãy dẻo điển hình (một đầu lõm hình chén, đầu kia nhọn hình nón) chứng tỏ vật liệu đồng tốt nhưng lực kéo căng thực tế đã vượt giới hạn bền kéo.",
        "definition": (
            "Khi sợi đồng bị thắt cổ chai rồi đứt theo hình chén-côn đối xứng, phôi đồng không có tạp chất mà sự cố xuất phát từ dây chuyền: kẹt rulo cấp (Pay-off), sai tỷ lệ giảm tiết diện giữa các cấp khuôn PCD, khuôn mòn gây ma sát lớn hoặc nhũ tương kéo mất độ bôi trơn."
        ),
        "formula_or_spec": (
            "• Dấu hiệu nhận diện: Thắt tiết diện rõ rệt (Necking), góc nghiêng mép 45°, bề mặt mờ mịn đối xứng → Kiểm tra ngay bộ khuôn PCD, độ trượt Capstan và nồng độ nhũ tương!"
        ),
        "cadivi_application": (
            "Giúp kỹ sư OE & vận hành CADIVI khoanh vùng tức thì 100% nguyên nhân nội bộ xưởng Kéo (máy/khuôn/nhũ tương) thay vì mất 3 ngày đổ lỗi cho nhà cung cấp đồng."
        ),
        "cadivi_example": (
            "Ví dụ: Ghi nhận 8 lần đứt Cup-and-Cone liên tiếp ở sợi số 5 máy Multi-wire → Kiểm tra phát hiện vòi phun nhũ tương nhánh số 5 bị tắc mạt đồng làm tăng ma sát khuôn; thông vòi xong chạy thông 24 giờ không đứt sợi nào!"
        ),
        "related": ["Wire Break Forensics", "PCD", "Drawing Emulsion", "Tensile", "RBD"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "Solar Cable": {
        "term": "Solar Cable",
        "full_name": "Solar Photovoltaic Cable (H1Z2Z2-K — EN 50618 / IEC 62930) — Cáp Năng Lượng Mặt Trời",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Solar Cable", "H1Z2Z2-K", "H1Z2Z2", "cáp năng lượng mặt trời", "EN 50618"],
        "case_sensitive": ["H1Z2Z2-K", "H1Z2Z2"],
        "short_desc": "Dòng cáp DC 1,500V cao cấp của CADIVI dùng cho điện mặt trời áp mái & trang trại: ruột đồng mềm mạ thiếc, 2 lớp cách điện–vỏ XLPO chịu UV/Ozone tuổi thọ ≥ 25 năm.",
        "definition": (
            "Khác với dây dân dụng VC/CV thông thường, cáp Solar H1Z2Z2-K phải chịu nhiệt độ làm việc 90–120°C, nắng gió khắc nghiệt ngoài trời 25 năm, chống cháy LSZH và kháng nước/axit/kiềm — thường được liên kết ngang bằng chiếu xạ E-beam hoặc Silane đặc chủng."
        ),
        "formula_or_spec": (
            "• Cấu trúc chuẩn EN 50618: Ruột đồng mềm Class 5 mạ thiếc (Tinned Copper) + Cách điện XLPO + Vỏ XLPO chống UV/LSZH.\n"
            "• Điện áp định mức: 1.5 kV DC (max 1.8 kV DC); nhiệt độ ruột dẫn 90°C liên tục (120°C trong 20,000 giờ)."
        ),
        "cadivi_application": (
            "Miền Trung (Đà Nẵng, Quảng Nam, Ninh Thuận, Bình Định...) là thủ phủ điện mặt trời — dòng cáp Solar mang biên lợi nhuận cao tại CADIVI; OE cần tối ưu tốc độ đùn đồng thời 2 lớp (Tandem/Co-extrusion) và kiểm soát độ đồng tâm lớp vỏ mỏng."
        ),
        "cadivi_example": (
            "Ví dụ: Tối ưu lịch chạy gom đơn (Campaign Scheduling) cáp Solar H1Z2Z2-K 4.0 & 6.0 mm² Đỏ/Đen theo chuỗi màu giúp giảm phế nhựa XLPO đắt tiền tới 45% mỗi đợt sản xuất!"
        ),
        "related": ["Tinned Copper", "E-beam", "LSZH", "XLPE", "Color Sequencing"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "Tinned Copper": {
        "term": "Tinned Copper",
        "full_name": "Tinned Copper Conductor — Ruột Dẫn Đồng Mạ Thiếc Chống Oxy Hóa & Ăn Mòn",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Tinned Copper", "đồng mạ thiếc"],
        "case_sensitive": [],
        "short_desc": "Sợi đồng được phủ một lớp thiếc siêu mỏng bên ngoài nhằm chống đen oxy hóa, chống ăn mòn hơi muối biển và dễ hàn thiếc cho cáp Solar, cáp tàu biển, cáp chống nhiễu.",
        "definition": (
            "Đồng trần khi tiếp xúc không khí ẩm mặn ven biển hoặc nhiệt độ cao sẽ nhanh chóng bị oxy hóa đen làm tăng điện trở tiếp xúc. Phủ lớp thiếc mỏng (điện phân hoặc nhúng nóng) bảo vệ lõi đồng bền bỉ nhiều thập kỷ."
        ),
        "formula_or_spec": (
            "• Lưu ý tiêu chuẩn IEC 60228: Điện trở DC tối đa của ruột đồng mạ thiếc được phép cao hơn ~1–2% so với đồng trần cùng tiết diện do độ dẫn điện của thiếc thấp hơn đồng."
        ),
        "cadivi_application": (
            "Sử dụng cho cáp Solar H1Z2Z2-K, lưới bện chống nhiễu cáp điều khiển và cáp cho công trình ven biển miền Trung tại CADIVI; OE kiểm soát chặt tránh xước lớp mạ thiếc qua puly dẫn hướng khi bện."
        ),
        "cadivi_example": (
            "Ví dụ: Thay puly dẫn hướng thép cứng bị rãnh mòn bằng puly gốm Ceramic trên máy bện Buncher cáp Solar giúp loại bỏ 100% lỗi trầy lớp mạ thiếc và bám mạt thiếc lên cảm biến!"
        ),
        "related": ["Solar Cable", "Braiding", "IEC 60228", "Buncher"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "E-beam": {
        "term": "E-beam",
        "full_name": "Electron-Beam Irradiation Crosslinking — Liên Kết Ngang Nhựa Bằng Chiếu Xạ Chùm Tia Điện Tử",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["E-beam", "chiếu xạ chùm tia điện tử", "Electron-Beam"],
        "case_sensitive": [],
        "short_desc": "Công nghệ bắn chùm tia điện tử năng lượng cao xuyên qua lớp cách điện XLPO/XLPE ở nhiệt độ thường để tạo mạng liên kết ngang cực bền mà không cần bể nước nóng hay lò hơi.",
        "definition": (
            "So với ủ hơi ẩm Silane (mất 12–48 giờ chờ phản ứng) hay CCV hơi/nitơ áp suất cao, công nghệ E-beam tạo liên kết ngang đồng đều tức thì cho dây tiết diện nhỏ/trung bình (cáp Solar PV, dây ô tô, dây chịu nhiệt 125–150°C) và không có hơi ẩm dư."
        ),
        "formula_or_spec": (
            "• Liều chiếu xạ (Irradiation Dose): Thường 80 – 180 kGy tùy công thức nhựa và chiều dày cách điện.\n"
            "• Xác nhận đạt chuẩn bằng phép thử độ giãn dài nóng Hot Set Test (IEC 60811-507)."
        ),
        "cadivi_application": (
            "Góc nhìn OE: Khâu chiếu xạ E-beam có chi phí đầu tư/gia công ngoài rất lớn (nút thắt thời gian Lead Time nếu phải chuyển rulo đi chiếu xạ) → OE phải lập lịch gom lô tối ưu tải rulo và đồng bộ vận chuyển."
        ),
        "cadivi_example": (
            "Ví dụ: Gom đơn cáp Solar 4mm² và 6mm² đóng đầy rulo chuẩn cùng bề rộng để 1 lượt chạy máy chiếu xạ đạt hiệu suất phủ tia 92% thay vì 65%, giảm 24% chi phí chiếu xạ trên mỗi km cáp!"
        ),
        "related": ["Solar Cable", "Silane", "CCV", "Hot Set Test", "Lead Time"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "Braiding": {
        "term": "Braiding",
        "full_name": "Copper Wire Braiding & Copper Tape Screening — Bện Lưới Đồng & Quấn Băng Đồng Chống Nhiễu",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Braiding", "bện lưới đồng", "quấn băng đồng", "Copper Tape Screening", "màn chắn đồng"],
        "case_sensitive": [],
        "short_desc": "Công đoạn tạo lớp màn chắn điện từ (EMI Shield) quanh cụm lõi cáp điều khiển/tín hiệu (`DVV/Sc`, `CVV/Sc`) hoặc cáp trung thế để chống nhiễu và thoát dòng ngắn mạch.",
        "definition": (
            "Máy bện lưới (Braiding Machine) có 16 hoặc 24 suốt sợi đồng nhỏ (0.15–0.25 mm) đan chéo liên tục quanh lõi cáp với mật độ phủ (Optical Coverage) thường ≥ 80–85%. Đây là công đoạn chạy rất chậm (thường chỉ 2–8 m/phút) nên rất dễ thành nút thắt cổ chai toàn xưởng!"
        ),
        "formula_or_spec": (
            "• Tỷ lệ phủ lưới quang học (Optical Coverage K) ≥ 80% – 85% theo tiêu chuẩn cáp điều khiển.\n"
            "• Đặc trưng OE: 1 công nhân thường đứng vận hành đồng thời 4–8 máy Braiding (mô hình Man-Machine Chart điển hình)."
        ),
        "cadivi_application": (
            "Tại xưởng cáp điều khiển/chống nhiễu CADIVI, OE áp dụng Man-Machine Chart, chuẩn hóa đánh suốt đồng đều chiều dài (tránh 24 suốt hết lệch giờ phải dừng máy 24 lần!) và cảm biến đứt sợi Poka-Yoke."
        ),
        "cadivi_example": (
            "Ví dụ: Đồng bộ chiều dài đánh suốt trên máy Rewinder để cả 24 suốt bện lưới hết gần cùng thời điểm (chỉ dừng 1 lần thay trọn bộ Kit 24 suốt thay vì dừng lẻ tẻ 16 lần) → Nâng OEE nhóm máy Braiding từ 58% lên 79%!"
        ),
        "related": ["Man-Machine Chart", "Kitting", "Tinned Copper", "TOC", "Poka-Yoke"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "Water-Blocking": {
        "term": "Water-Blocking",
        "full_name": "Longitudinal Water-Blocking Tape & Swelling Yarn — Băng & Sợi Trương Nở Chống Thấm Dọc Cáp Ngầm",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["Water-Blocking", "băng chống thấm", "Swelling Yarn", "chống thấm dọc"],
        "case_sensitive": [],
        "short_desc": "Vật liệu chứa bột siêu thấm (SAP) quấn quanh lõi cáp ngầm trung thế; khi vỏ cáp bị xước ngập nước, băng lập tức trương nở thành gel bịt kín đường nước lan dọc lõi.",
        "definition": (
            "Cáp ngầm chôn đất ở vùng mưa bão ngập úng miền Trung nếu bị cuốc xẻng làm rách vỏ, nước sẽ luồn theo khe sợi đồng gây ăn mòn và phá hỏng hàng trăm mét cáp (hiện tượng Water Treeing trong XLPE). Băng/sợi Water-Blocking cô lập vùng ngập chỉ trong vài chục centimet."
        ),
        "formula_or_spec": (
            "• Yêu cầu bảo quản: CỰC KỲ KỴ ẨM! Độ ẩm kho cao làm băng tự trương nở vón cục trước khi chạy máy → Phải bọc kín túi chống ẩm + kiểm soát FIFO kho vật tư."
        ),
        "cadivi_application": (
            "Kiểm soát độ ẩm kho, định mức độ chồng mí quấn băng (Overlap 15–25% theo BOM) và cảm biến đứt băng trên máy ghép lõi cáp ngầm dự án điện lực."
        ),
        "cadivi_example": (
            "Ví dụ: Tủ bảo quản kín có đồng hồ ẩm kế (< 50% RH) đặt cạnh máy quấn băng chống thấm giúp giảm phế cuộn băng bị vón ẩm từ 7% xuống 0%!"
        ),
        "related": ["FIFO", "BOM", "Drum Twister", "XLPE", "Mica FR"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "CaCO3 Filler": {
        "term": "CaCO3 Filler",
        "full_name": "Calcium Carbonate Filler & Compound Formulation — Chất Độn CaCO3 & Hệ Công Thức Nhựa PVC",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["CaCO3 Filler", "CaCO3", "chất độn"],
        "case_sensitive": ["CaCO3"],
        "short_desc": "Bột đá CaCO3 được phối trộn vào hợp chất nhựa PVC (cùng chất hóa dẻo, ổn định nhiệt) để cân bằng chi phí giá thành, độ cứng và tính công nghệ khi đùn.",
        "definition": (
            "Hàm lượng CaCO3 tăng làm giảm giá thành mỗi kg nhựa PVC, nhưng đồng thời làm TĂNG tỷ trọng (Specific Gravity — tức mỗi km cáp lại tốn nhiều kg nhựa hơn!), giảm độ bền kéo giãn (Tensile/Elongation) và dễ gây đóng cặn Die Drool."
        ),
        "formula_or_spec": (
            "• Bẫy kinh tế OE bắt buộc biết: Giá nhựa tính theo VNĐ/kg, nhưng cáp bọc theo THỂ TÍCH (cm³/km)!\n"
            "• Chi phí nhựa thực / km = Thể tích bọc (dm³/km) × Tỷ trọng (kg/dm³) × Đơn giá (VNĐ/kg)."
        ),
        "cadivi_application": (
            "OE CADIVI luôn đánh giá bài toán đổi công thức nhựa dựa trên Chi phí trên mỗi mét khối (Volume Cost = Giá/kg × Tỷ trọng) thay vì chỉ nhìn đơn giá rẻ trên mỗi kg!"
        ),
        "cadivi_example": (
            "Ví dụ: Hạt PVC loại B rẻ hơn loại A 2% theo giá/kg (24,500 vs 25,000đ/kg), nhưng do độn nhiều CaCO3 nên tỷ trọng nặng hơn 6% (1.54 vs 1.45 g/cm³) → Thực tế bọc 1 km cáp bằng nhựa B lại ĐẮT HƠN nhựa A gần 4%!"
        ),
        "related": ["Specific Gravity", "PVC", "BOM", "Die Drool", "Tensile"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "Specific Gravity": {
        "term": "Specific Gravity",
        "full_name": "Polymer Specific Gravity (Density) — Tỷ Trọng Hạt Nhựa & Quy Đổi Khối Lượng Theo Thể Tích",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["Specific Gravity", "tỷ trọng nhựa"],
        "case_sensitive": [],
        "short_desc": "Khối lượng riêng của nhựa (g/cm³): yếu tố nhân trực tiếp quyết định số kg nhựa tiêu hao cho 1 km cáp điện và ảnh hưởng thẳng đến BOM Variance.",
        "definition": (
            "Tỷ trọng tiêu chuẩn của các loại nhựa ngành cáp khác nhau rất lớn: PE/XLPE chỉ khoảng 0.92–0.94 g/cm³, PVC cách điện khoảng 1.35–1.45 g/cm³, PVC vỏ khoảng 1.42–1.55 g/cm³, còn LSZH chống cháy thường nặng 1.45–1.60 g/cm³."
        ),
        "formula_or_spec": (
            "• Khối lượng nhựa (kg/km) = 0.7854 × (D_ngoài² - D_trong²) × Tỷ trọng (g/cm³)\n"
            "• Nếu tỷ trọng lô nhựa nhập tăng +0.04 g/cm³ (+2.8%), định mức BOM sẽ tự động báo âm (vượt kg) dù chiều dày bọc đo đúng y chuẩn!"
        ),
        "cadivi_application": (
            "Khi phân tích BOM Variance nhựa tại CADIVI, OE luôn tách rõ 2 nguyên nhân: (1) Đùn quá dày Over-thickness (lỗi vận hành/SPC) vs (2) Tỷ trọng lô hạt nhựa thực tế cao hơn tỷ trọng thiết kế trong BOM (lỗi IQC/cập nhật BOM)."
        ),
        "cadivi_example": (
            "Ví dụ: Tháng 9 xưởng đùn vỏ PVC bị vượt định mức BOM +2.5% dù dữ liệu Laser Gauge chuẩn tuyệt đối → Kiểm tra COA phòng Lab phát hiện lô hạt PVC mới có tỷ trọng 1.52 thay vì 1.48 trong ERP!"
        ),
        "related": ["CaCO3 Filler", "BOM", "Over-thickness", "PVC", "XLPE"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "ASTM B49": {
        "term": "ASTM B49",
        "full_name": "ASTM B49 Copper Redraw Rod & IQC — Tiêu Chuẩn Đồng Rod 8mm Đầu Vào & Kiểm Tra COA",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["ASTM B49", "COA", "IQC", "đồng Rod"],
        "case_sensitive": ["ASTM B49", "COA", "IQC"],
        "short_desc": "Tiêu chuẩn quốc tế quy định chất lượng cuộn đồng thanh Ø 8.0 mm nguyên liệu đầu vào cho nhà máy kéo cáp (độ tinh khiết Cu ≥ 99.90%, độ dẫn ≥ 100% IACS, hàm lượng oxy & thử xoắn).",
        "definition": (
            "Mỗi lô đồng Rod 8mm nhập về nhà máy đều đi kèm Chứng chỉ phân tích (COA — Certificate of Analysis) và phải qua kiểm tra đầu vào (IQC): kiểm tra hàm lượng oxy (ETP Cu ~200–400 ppm), bề mặt không vết gấp/xước, độ dẫn điện % IACS và thử xoắn (Twist Test) để phát hiện sớm nguy cơ đứt sợi khi kéo."
        ),
        "formula_or_spec": (
            "• Đồng ETP chuẩn ASTM B49: Cu ≥ 99.90%, độ dẫn điện ≥ 100.0% IACS (thực tế tốt đạt 100.8–101.5% IACS), độ giãn dài ≥ 30%."
        ),
        "cadivi_application": (
            "OE CADIVI đối chiếu dữ liệu COA từng lô đồng Rod (IQC) với tần suất đứt sợi trên máy kéo RBD/Multi-wire và mức Copper Give-away để đánh giá nhà cung ứng bằng số liệu định lượng."
        ),
        "cadivi_example": (
            "Ví dụ: Liên kết mã lô đồng Rod trên Barcode ERP với nhật ký đứt sợi máy kéo giúp phát hiện 70% ca đứt sợi trong tháng rơi đúng vào 2 lô có hàm lượng tạp chất/oxit cận ngưỡng!"
        ),
        "related": ["IACS", "RBD", "Wire Break Forensics", "Copper Give-away", "IEC 60228"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "QCVN 4": {
        "term": "QCVN 4",
        "full_name": "QCVN 4:2009/BKHCN & Dấu Hợp Quy CR — Quy Chuẩn Kỹ Thuật Quốc Gia Về An Toàn Thiết Bị Điện (Dây Cáp Bọc PVC)",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "aliases": ["QCVN 4", "hợp quy CR", "QCVN 4:2009"],
        "case_sensitive": ["QCVN 4"],
        "short_desc": "Quy chuẩn kỹ thuật quốc gia bắt buộc của Việt Nam đối với dây và cáp điện bọc PVC điện áp danh định đến 450/750V (gắn dấu hợp quy CR trước khi lưu thông thị trường).",
        "definition": (
            "Khác với TCVN (tự nguyện áp dụng trừ khi được viện dẫn), QCVN 4 là quy chuẩn pháp lý BẮT BUỘC của Bộ KH&CN nhằm bảo đảm an toàn điện chống cháy nổ cho dây dân dụng (VC, VCm, VCmd, VCmt). Sản phẩm vi phạm điện trở ruột dẫn, chiều dày cách điện hay chịu điện áp sẽ bị thu hồi và phạt nặng."
        ),
        "formula_or_spec": (
            "• Dẫn chiếu trực tiếp bộ tiêu chuẩn TCVN 6610 (IEC 60227) & TCVN 6612 (IEC 60228) → Bắt buộc kiểm soát chặt chiều dày cách điện min, điện trở DC 20°C và thử cao áp."
        ),
        "cadivi_application": (
            "Mọi cải tiến tiết kiệm đồng/nhựa của OE CADIVI PHẢI nằm tuyệt đối bên trong vùng an toàn pháp lý của QCVN 4 / TCVN 6610 (tuyệt đối không hạ quá sát biên gây rủi ro rớt mẫu thanh tra thị trường!)."
        ),
        "cadivi_example": (
            "Ví dụ: Khi giảm Over-thickness dây VC 2.5 mm², OE luôn khóa cận dưới kiểm soát nội bộ cao hơn chuẩn QCVN 4 tối thiểu 3σ (+0.05 mm biên an toàn) để bảo đảm 100% mẫu kiểm định đột xuất đều đạt chuẩn CR!"
        ),
        "related": ["IEC 60228", "IEC 60502", "Copper Give-away", "Over-thickness", "ISO 9001"],
        "doc_key": "cable_extrusion_wire_forensics"
    },
    "Work Sampling": {
        "term": "Work Sampling",
        "full_name": "Work Sampling (Ratio Delay Study — L.H.C. Tippett) — Phương Pháp Lấy Mẫu Công Việc Ngẫu Nhiên",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Work Sampling", "lấy mẫu công việc", "Ratio Delay"],
        "case_sensitive": [],
        "short_desc": "Kỹ thuật IE quan sát tức thời theo các mốc thời gian ngẫu nhiên (hàng trăm lượt chụp nhanh) để xác định tỷ lệ % thời gian làm việc tạo giá trị vs chờ đợi mà không cần bấm giờ liên tục.",
        "definition": (
            "Khi công việc có chu kỳ dài hoặc không lặp lại đều đặn (như công nhân đứng 3 máy bện, tài xế xe nâng chở rulo, thợ bảo trì cơ điện, nhân viên kho thành phẩm), Time Study bấm giờ liên tục rất tốn công và gây áp lực tâm lý. Work Sampling dùng xác suất thống kê để đo cực nhanh và chính xác!"
        ),
        "formula_or_spec": (
            "• Công thức tính số lượng quan sát cần thiết (độ tin cậy 95%, Z = 1.96):\n"
            "  N = [ Z² × p × (1 - p) ] / e²\n"
            "• Ví dụ: Ước lượng tỷ lệ thời gian chờ p = 0.25, sai số tuyệt đối cho phép e = ±0.03 (±3%):\n"
            "  N = [ 1.96² × 0.25 × 0.75 ] / 0.03² = 800 lượt quan sát (5 người × 160 lượt trong 5 ngày!)."
        ),
        "cadivi_application": (
            "Vũ khí thực địa cực mạnh của OE CADIVI để đo tỷ lệ bận thực sự của tổ xe nâng/cầu trục, tổ bảo trì (Wrench Time) và nhóm công nhân chạy nhiều máy kéo/bện trong 1 tuần mà không gây phản cảm cho xưởng."
        ),
        "cadivi_example": (
            "Ví dụ: Lấy mẫu Work Sampling 800 lượt trên 4 xe nâng xưởng cáp phát hiện 34% thời gian là 'chạy không tải & đi tìm vị trí rulo trống' → Vẽ lại tuyến Milk Run và gắn bảng sơ đồ vị trí kho rulo giúp đáp ứng thêm 30% sản lượng mà không cần mua thêm xe nâng!"
        ),
        "related": ["Time Study", "OLE", "Wrench Time", "Milk Run", "Man-Machine Chart"],
        "doc_key": "oe_field_execution_case_test"
    },
    "Cost Deployment": {
        "term": "Cost Deployment",
        "full_name": "WCM Cost Deployment — Triển Khai Ma Trận Tổn Thất Sang Tiền (Ngôn Ngữ Tài Chính Của OE)",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["Cost Deployment", "WCM", "World Class Manufacturing"],
        "case_sensitive": ["WCM"],
        "short_desc": "Trụ cột chiến lược của hệ quản trị WCM: liên kết từng tổn thất kỹ thuật tại hiện trường (dừng máy, phế đồng, dư nhựa, điện năng, tăng ca) sang giá trị VNĐ cụ thể để chọn dự án ưu tiên.",
        "definition": (
            "Thay vì liệt kê 30 vấn đề hiện trường cảm tính, Cost Deployment lập chuỗi Ma trận A (Xác định tổn thất tại từng xưởng) → Ma trận B (Tách tổn thất gốc vs tổn thất hệ quả) → Ma trận C (Quy đổi sang tiền VNĐ theo Standard Cost) → Ma trận D (Xếp hạng dự án theo tỉ số Lợi ích/Chi phí — B/C Ratio)."
        ),
        "formula_or_spec": (
            "• Thứ tự ra quyết định: Tổng tổn thất VNĐ lớn nhất × Khả năng giải quyết nhanh (Ease of Implementation) × Chi phí đầu tư thấp → Dự án ưu tiên #1!"
        ),
        "cadivi_application": (
            "Giúp Chuyên viên OE CADIVI nói chung ngôn ngữ với Giám đốc Nhà máy và Kế toán trưởng: mọi đề xuất SMED, SPC hay bố trí lại Layout đều nằm trên cùng 1 bản đồ tiền VNĐ minh bạch."
        ),
        "cadivi_example": (
            "Ví dụ: Lập bản đồ Cost Deployment quý 1 cho thấy: (1) Over-thickness nhựa = 195 tr/tháng, (2) Phế đồng dính nhựa đổi mã = 110 tr/tháng, (3) Đứt sợi máy kéo = 85 tr/tháng, (4) Bóng đèn/khí nén = 22 tr/tháng → Dồn 80% nguồn lực đánh ngay mục (1) & (2)!"
        ),
        "related": ["Loss Tree", "Standard Cost", "ROI", "Pareto", "Hoshin Kanri"],
        "doc_key": "oe_field_execution_case_test"
    },
    "Loss Tree": {
        "term": "Loss Tree",
        "full_name": "OEE Waterfall & Loss Tree — Cây Phân Rã Tổn Thất Sản Xuất (Thác Nước Thời Gian & Chi Phí)",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Loss Tree", "OEE Waterfall", "cây tổn thất"],
        "case_sensitive": [],
        "short_desc": "Sơ đồ thác nước bóc tách 100% thời gian lịch (8,760 giờ/năm) hoặc 100% chi phí chuyển đổi xuống từng nhánh tổn thất nhỏ (không tải, dừng kế hoạch, hỏng máy, đổi mã, giảm tốc, phế phẩm).",
        "definition": (
            "Loss Tree đảm bảo mọi phút thời gian và mọi đồng chi phí đều có 'chủ sở hữu' rõ ràng (Production, Maintenance, Planning, Quality) — không còn vùng mờ 'tổn thất khác' bị bỏ quên."
        ),
        "formula_or_spec": (
            "• Thác nước thời gian: Calendar Time (100%) − Không có đơn hàng − Bảo trì kế hoạch − Dừng sự cố (Breakdown) − Đổi mã (SMED) − Giảm tốc/Dừng vặt − Phế phẩm = Thời gian tạo giá trị ròng (Net Productive Time = TEEP!)."
        ),
        "cadivi_application": (
            "Vẽ biểu đồ OEE Waterfall trên Power BI mỗi tháng cho 4 phân xưởng Kéo – Bện – Đùn – Đóng gói tại CADIVI Miền Trung để Ban Giám đốc nhìn 1 biểu đồ hiểu trọn sức khỏe nhà máy."
        ),
        "cadivi_example": (
            "Ví dụ: OEE Waterfall xưởng Đùn cho thấy trong 35% tổn thất OEE thì Đổi màu/tiết diện chiếm 14%, Dừng vặt/thay rulo 9%, Chạy chậm hơn tốc độ chuẩn 7% và Phế khởi động 5% → Biết chính xác phải làm SMED trước!"
        ),
        "related": ["OEE", "TEEP", "Cost Deployment", "Six Big Losses", "Power BI"],
        "doc_key": "oe_field_execution_case_test"
    },
    "LSW": {
        "term": "LSW",
        "full_name": "Leader Standard Work — Công Việc Chuẩn Hóa Dành Cho Cấp Quản Lý (Tổ Trưởng / Quản Đốc / Giám Đốc)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["LSW", "Leader Standard Work"],
        "case_sensitive": ["LSW"],
        "short_desc": "Danh mục kiểm tra theo khung giờ cố định hàng ngày/tuần của Tổ trưởng & Quản đốc (chạy Genba Walk, kiểm tra bảng SQDCM, chốt hành động lệch chuẩn) để duy trì cải tiến bền vững.",
        "definition": (
            "Standard Work của công nhân quy định cách làm ra sản phẩm; còn Leader Standard Work (LSW) quy định cách người quản lý kiểm tra và duy trì hệ thống! Khoảng 80% thời gian của Tổ trưởng, 50% của Quản đốc và 25% của Giám đốc xưởng nên được chuẩn hóa nhịp nhàng theo LSW."
        ),
        "formula_or_spec": (
            "• Cấu trúc LSW Tổ trưởng (ví dụ): 06:00 Họp đầu ca 5p (Tier 1) → 07:00 Kiểm tra thông số Recipe & 5S đầu ca → 10:00 Rà soát tốc độ m/phút & phế giữa ca → 13:30 Chốt sản lượng & bàn giao ca."
        ),
        "cadivi_application": (
            "Là chìa khóa vàng giúp các dự án SMED, 5S và SPC của OE CADIVI không bao giờ bị 'sớm nở tối tàn' sau khi kết thúc giai đoạn Pilot."
        ),
        "cadivi_example": (
            "Ví dụ: Bổ sung 1 dòng kiểm tra 2 phút vào phiếu LSW đầu ca của Tổ trưởng xưởng Đùn: 'Xác nhận đã sấy trước đầu Tip/Die cho lệnh kế tiếp trên lịch' → Duy trì thời gian đổi mã < 15 phút suốt cả năm!"
        ),
        "related": ["LPA", "SOP", "Visual Management", "Genba", "ADKAR"],
        "doc_key": "oe_field_execution_case_test"
    },
    "LPA": {
        "term": "LPA",
        "full_name": "Layered Process Audit — Kiểm Tra Quy Trình Phân Tầng Đa Cấp (Tổ Trưởng → Quản Đốc → Giám Đốc)",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["LPA", "Layered Process Audit", "kiểm tra phân tầng"],
        "case_sensitive": ["LPA"],
        "short_desc": "Hệ thống kiểm tra ngắn (5–10 phút/lượt) lặp lại ở nhiều cấp quản lý trên cùng các điểm trọng yếu (An toàn LOTO, 5S, Recipe, Control Plan) để ngăn hành vi làm tắt tái diễn.",
        "definition": (
            "Khác với đánh giá ISO mỗi năm 1 lần (dễ đối phó giấy tờ), LPA chia nhỏ thành 8–12 câu hỏi Có/Không đi thẳng xuống máy: Tầng 1 (Tổ trưởng kiểm mỗi ngày), Tầng 2 (Quản đốc/OE kiểm mỗi tuần), Tầng 3 (Giám đốc nhà máy kiểm 2 tuần/lần)."
        ),
        "formula_or_spec": (
            "• 3 tầng LPA chuẩn: Layer 1 (Hàng ngày — Tổ trưởng) | Layer 2 (Hàng tuần — Quản đốc / OE / QA) | Layer 3 (2 tuần–Tháng — Ban Giám đốc).\n"
            "• Mọi điểm Không Đạt (No) bắt buộc khắc phục ngay tại chỗ hoặc mở hành động có người chịu trách nhiệm & hạn chót."
        ),
        "cadivi_application": (
            "Gắn kết trực tiếp Ban Giám đốc và các cấp quản lý CADIVI Miền Trung vào văn hóa tuân thủ LOTO, 5S, hiệu chuẩn Spark Tester/Laser Gauge và quy trình SMED."
        ),
        "cadivi_example": (
            "Ví dụ: Phiếu LPA 10 câu hỏi tại máy đùn có mục 'Spark Tester đã test mẫu lỗ kim chuẩn đầu ca chưa?' và 'Thùng phế đồng trần không lẫn nhựa?' → Tỷ lệ tuân thủ tăng từ 62% lên 96% sau 6 tuần!"
        ),
        "related": ["LSW", "Control Plan", "5S", "LOTO", "ISO 9001"],
        "doc_key": "oe_field_execution_case_test"
    },
    "Escalation Matrix": {
        "term": "Escalation Matrix",
        "full_name": "Andon Escalation Matrix & Response SLA — Ma Trận Leo Thang Sự Cố Hiện Trường Theo Thời Gian",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Escalation Matrix", "Andon Escalation", "ma trận leo thang", "leo thang sự cố"],
        "case_sensitive": [],
        "short_desc": "Quy ước minh bạch ai phải có mặt trong bao nhiêu phút khi máy dừng hoặc lỗi liên tiếp (5 phút: Tổ trưởng → 15 phút: Bảo trì/Kỹ thuật → 30 phút: Quản đốc/OE → 60 phút: Giám đốc).",
        "definition": (
            "Nếu không có Ma trận leo thang sự cố, một máy đùn dừng vì lỗi nhiệt hay hỏng cảm biến có thể nằm chờ hàng giờ vì tổ trưởng tự loay hoay sửa không dám báo cấp trên. Escalation Matrix nén thời gian phản hồi MTTR xuống mức tối thiểu!"
        ),
        "formula_or_spec": (
            "• Khung SLA mẫu xưởng cáp:\n"
            "  - Mức 1 (0–5 phút dừng): Công nhân bật đèn Andon → Tổ trưởng có mặt.\n"
            "  - Mức 2 (5–15 phút): Gọi Bảo trì cơ điện / Kỹ thuật công nghệ hỗ trợ.\n"
            "  - Mức 3 (15–30 phút): Báo Quản đốc phân xưởng & OE/Kế hoạch điều phối tải.\n"
            "  - Mức 4 (> 60 phút hoặc sự cố an toàn/chất lượng lô lớn): Báo Giám đốc Nhà máy!"
        ),
        "cadivi_application": (
            "Kết hợp đèn Andon / cảnh báo Zalo-MES tự động trên các máy cổ chai (máy kéo thô RBD, máy đùn cáp lực) tại CADIVI Miền Trung để cắt mạnh thời gian chờ xử lý sự cố (MTTR)."
        ),
        "cadivi_example": (
            "Ví dụ: Áp dụng Escalation Matrix SLA 5–15–30 phút cho 4 máy đùn cổ chai rút thời gian chờ Bảo trì có mặt từ trung bình 22 phút xuống còn 6 phút, tăng Availability thêm +3.8%!"
        ),
        "related": ["Andon", "MTTR", "Jidoka", "LSW", "Downtime"],
        "doc_key": "oe_field_execution_case_test"
    },
    "Learning Curve": {
        "term": "Learning Curve",
        "full_name": "Wright's Learning Curve (80% Rule) — Đường Cong Học Việc Trong Sản Xuất",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Learning Curve", "đường cong học việc"],
        "case_sensitive": [],
        "short_desc": "Quy luật thực nghiệm cho thấy mỗi khi sản lượng tích lũy của một công việc lặp lại tăng gấp đôi, thời gian thao tác trên mỗi đơn vị sẽ giảm theo một tỷ lệ cố định (thường còn 80–90%).",
        "definition": (
            "Dùng để dự báo năng suất thực tế của công nhân mới tuyển (đang trong thời gian đào tạo TWI) hoặc khi xưởng lần đầu chạy một dòng cáp cấu trúc phức tạp (như cáp chống cháy Mica FR hay cáp ngầm giáp thép), tránh đặt KPI quá sức gây sốc hoặc lập kế hoạch giao hàng bị trễ."
        ),
        "formula_or_spec": (
            "• Y_n = Y_1 × n^b   (với b = ln(Tỷ lệ học việc r) / ln(2); ví dụ r = 80% → b = -0.3219)\n"
            "• Ý nghĩa r = 80%: Đơn vị #1 mất 100p → #2 mất 80p → #4 mất 64p → #8 mất 51.2p."
        ),
        "cadivi_application": (
            "OE CADIVI áp dụng khi tính năng lực RCCP và định biên nhân sự cho các đợt tuyển công nhân mới mùa cao điểm hoặc đưa dây chuyền đùn/bện mới vào vận hành."
        ),
        "cadivi_example": (
            "Ví dụ: Công nhân mới tổ Đóng cuộn khoanh 100m tuần 1 đạt 65% định mức chuẩn → Áp dụng lộ trình đào tạo TWI + Learning Curve dự báo đạt 82% ở tuần 2 và 95%+ ở tuần 4 để phòng Kế hoạch xếp tải chuẩn xác!"
        ),
        "related": ["TWI", "OLE", "Time Study", "Headcount Planning", "RCCP"],
        "doc_key": "oe_field_execution_case_test"
    },
    "PM Compliance": {
        "term": "PM Compliance",
        "full_name": "Preventive Maintenance Compliance & Schedule Compliance — Tỷ Lệ Tuân Thủ Bảo Trì Phòng Ngừa",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["PM Compliance", "Schedule Compliance", "tuân thủ bảo trì"],
        "case_sensitive": [],
        "short_desc": "Chỉ số đo tỷ lệ % đầu việc bảo trì phòng ngừa (PM) được hoàn thành đúng hạn trong cửa sổ ±10% chu kỳ — chỉ số dẫn báo (Leading Indicator) quyết định trực tiếp MTBF & Breakdown.",
        "definition": (
            "Rất nhiều nhà máy có lịch bảo trì trên giấy rất đẹp, nhưng khi đơn hàng gấp thì Sản xuất từ chối giao máy cho Bảo trì làm PM → Kết quả 2 tuần sau máy gãy trục giữa ca làm mất hẳn 2 ngày sản xuất!"
        ),
        "formula_or_spec": (
            "• PM Compliance (%) = (Số đầu việc PM hoàn thành đúng hạn / Tổng số đầu việc PM theo lịch tháng) × 100%\n"
            "• Chuẩn World-Class: PM Compliance ≥ 90% | Tỷ lệ Bảo trì có kế hoạch (Planned Work) ≥ 80% (chữa cháy đột xuất < 20%)."
        ),
        "cadivi_application": (
            "OE CADIVI phối hợp Kế hoạch & Cơ Điện khóa khung giờ bảo trì PM hàng tuần vào lịch MPS/CRP (đặc biệt thay vòng bi đầu bện, vệ sinh bầu lọc dầu máy kéo RBD, hiệu chuẩn cảm biến nhiệt máy đùn)."
        ),
        "cadivi_example": (
            "Ví dụ: Khi PM Compliance xưởng Kéo & Bện tăng từ 55% lên 92% nhờ chốt lịch giao máy cố định sáng Chủ nhật, số giờ dừng đột xuất (Breakdown) giảm 48% chỉ sau 1 quý!"
        ),
        "related": ["TPM", "MTBF", "MTTR", "Wrench Time", "CBM / PdM"],
        "doc_key": "oe_field_execution_case_test"
    },
    "Wrench Time": {
        "term": "Wrench Time",
        "full_name": "Maintenance Wrench Time (Hands-on-Tool Time) — Tỷ Lệ Thời Gian Thực Tác Nghiệp Bảo Trì",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Wrench Time", "thời gian thực tác nghiệp"],
        "case_sensitive": [],
        "short_desc": "Tỷ lệ % thời gian trong ca mà kỹ thuật viên bảo trì thực sự cầm dụng cụ sửa chữa/bảo dưỡng thiết bị (không tính thời gian chờ lệnh, đi tìm phụ tùng, chờ giao máy hay đi lại).",
        "definition": (
            "Ở nhà máy bảo trì bị động (chữa cháy), Wrench Time thường chỉ đạt 25–35% do thợ bảo trì mất quá nhiều thời gian tìm vòng bi/phụ tùng kho, chờ giấy phép LOTO hoặc đi bộ giữa các phân xưởng. Mức đẳng cấp thế giới đạt 55–65% nhờ lập kế hoạch bảo trì (Maintenance Planning & Kitting) tốt!"
        ),
        "formula_or_spec": (
            "• Wrench Time (%) = (Thời gian thao tác kỹ thuật trực tiếp trên máy / Tổng thời gian làm việc của thợ bảo trì) × 100%\n"
            "• Thường đo bằng phương pháp Work Sampling trong 1–2 tuần."
        ),
        "cadivi_application": (
            "Thay vì xin tuyển thêm thợ bảo trì khi xưởng CADIVI Miền Trung phàn nàn sửa máy chậm, OE dùng Work Sampling đo Wrench Time, tổ chức kho phụ tùng 5S + soạn sẵn bộ Kit vật tư bảo trì (dây curoa, bạc đạn, điện trở nhiệt) để tăng gấp rưỡi năng lực đội Cơ Điện!"
        ),
        "cadivi_example": (
            "Ví dụ: Nâng Wrench Time đội bảo trì 8 người từ 32% lên 48% nhờ chuẩn bị sẵn xe đẩy Kitting phụ tùng cho lệnh PM định kỳ → Tương đương có thêm sức làm việc của 4 thợ bảo trì miễn phí!"
        ),
        "related": ["Work Sampling", "PM Compliance", "TPM", "MTTR", "Kitting"],
        "doc_key": "oe_field_execution_case_test"
    },
    "CBM / PdM": {
        "term": "CBM / PdM",
        "full_name": "Condition-Based & Predictive Maintenance — Bảo Trì Theo Tình Trạng & Bảo Trì Dự Đoán (Nhiệt Ảnh, Rung, Siêu Âm)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["CBM / PdM", "CBM", "PdM", "Predictive Maintenance", "bảo trì dự đoán"],
        "case_sensitive": ["CBM", "PdM"],
        "short_desc": "Thay vì đợi hỏng mới sửa (Breakdown) hoặc thay sớm gây lãng phí (Time-based PM), dùng camera nhiệt ảnh, đo rung động vòng bi và siêu âm để phát hiện sớm hỏng hóc trước khi máy dừng.",
        "definition": (
            "Theo đường cong P–F (Potential Failure → Functional Failure), trước khi bạc đạn máy kéo hay tụ điện tủ biến tần nổ hẳn, nó đã phát ra tín hiệu sớm qua sóng siêu âm (vài tháng trước), rung động (vài tuần trước) và tăng nhiệt độ cục bộ (vài ngày trước)."
        ),
        "formula_or_spec": (
            "• 4 công cụ PdM hiệu quả nhất tại nhà máy cáp: (1) Camera ảnh nhiệt soi tủ điện/vòng bi/đầu đùn, (2) Máy đo rung động bạc đạn máy kéo & bện, (3) Siêu âm phát hiện rò rỉ khí nén, (4) Phân tích dầu bôi trơn hộp số."
        ),
        "cadivi_application": (
            "Đầu tư cực thấp (1 máy ảnh nhiệt + bút đo rung chỉ vài chục triệu) nhưng cứu được những sự cố dừng máy kéo thô RBD hay cháy tủ biến tần gây thiệt hại hàng trăm triệu đồng tại CADIVI!"
        ),
        "cadivi_example": (
            "Ví dụ: Soi camera nhiệt định kỳ hàng tháng tủ điện máy đùn số 3 phát hiện đầu cos khởi động từ điện trở nòng nóng 105°C (các pha khác 42°C) → Siết lại đầu cos trong giờ nghỉ trưa, ngăn chặn 1 vụ cháy tủ điện mất 3 ngày sản xuất!"
        ),
        "related": ["TPM", "PM Compliance", "MTBF", "Melt Pressure", "ISO 50001"],
        "doc_key": "oe_field_execution_case_test"
    },
    "MOC / ECN": {
        "term": "MOC / ECN",
        "full_name": "Management of Change (MOC) & Engineering Change Notice (ECN/ECO) — Quy Trình Kiểm Soát Thay Đổi Kỹ Thuật",
        "category": "An Toàn Công Nghiệp, EHS & Tiêu Chuẩn ISO",
        "aliases": ["MOC / ECN", "MOC", "ECN", "ECO", "Management of Change"],
        "case_sensitive": ["MOC", "ECN", "ECO"],
        "short_desc": "Quy trình phê duyệt liên phòng ban bắt buộc trước khi thay đổi bất kỳ yếu tố nào (công thức nhựa, nhà cung cấp đồng, tốc độ máy, khuôn mới, cải tiến cơ khí) để không tạo rủi ro ẩn.",
        "definition": (
            "Nhiều sự cố chất lượng hàng loạt xảy ra vì 1 bộ phận 'tự ý cải tiến' (vd: đổi hạt nhựa rẻ hơn, chỉnh tăng tốc độ máy, đổi cấu trúc gá) mà không thông báo cho QA/QC, An toàn EHS, Bảo trì và Kế toán cập nhật BOM/Control Plan."
        ),
        "formula_or_spec": (
            "• Luồng MOC/ECN chuẩn 5 bước: (1) Đề xuất thay đổi → (2) Đánh giá rủi ro chéo (Kỹ thuật – QA – EHS – BOM) → (3) Chạy thử nghiệm lô nhỏ (Pilot Trial) & kiểm định Lab → (4) Phê duyệt chính thức → (5) Cập nhật đồng bộ SOP, Control Plan, BOM ERP & đào tạo xưởng!"
        ),
        "cadivi_application": (
            "Bắt buộc tuân thủ trong mọi dự án cải tiến OE tại CADIVI (nhất là khi điều chỉnh dung sai giảm Copper Give-away, giảm Over-thickness hay đổi bộ Chày-Cối SMED) để đáp ứng chuẩn ISO 9001 & QCVN 4."
        ),
        "cadivi_example": (
            "Ví dụ: Trước khi nhân rộng công thức giảm chiều dày bọc PVC mục tiêu từ 1.25 xuống 1.16 mm cho toàn bộ 6 máy đùn, OE mở phiếu MOC chạy thử 3 lô, đo đủ 30 mẫu phòng Lab đạt Cpk ≥ 1.67 rồi mới cập nhật đồng bộ MBOM trên SAP!"
        ),
        "related": ["ISO 9001", "Control Plan", "PFMEA", "BOM", "QCVN 4"],
        "doc_key": "oe_field_execution_case_test"
    },
    "Headcount Planning": {
        "term": "Headcount Planning",
        "full_name": "Manufacturing Headcount & Shift Staffing Planning — Hoạch Định Định Biên Nhân Sự & Mô Hình Ca Kíp",
        "category": "Hoạch Định Năng Lực, BOM & Chi Phí",
        "aliases": ["Headcount Planning", "định biên nhân sự", "3 ca 4 kíp", "định biên"],
        "case_sensitive": [],
        "short_desc": "Bài toán tính chính xác số công nhân cần thiết cho từng phân xưởng theo sản lượng mục tiêu, mô hình chạy máy (1 người nhiều máy), tỷ lệ vắng mặt và giới hạn tăng ca Luật Lao động VN.",
        "definition": (
            "Nếu tính định biên chỉ lấy Tổng giờ công / 8 giờ thì xưởng sẽ luôn thiếu người do quên hệ số vắng mặt/nghỉ phép (Absenteeism 5–8%), hiệu suất công nhân thực tế (OLE) và ràng buộc Luật Lao động Việt Nam (tăng ca tối đa 40 giờ/tháng, 200–300 giờ/năm)."
        ),
        "formula_or_spec": (
            "• Định biên công nhân = [ Tổng giờ công tiêu chuẩn yêu cầu / (Giờ làm thực/người × OLE mục tiêu) ] × (1 + Hệ số dự phòng nghỉ phép/vắng mặt 7%)\n"
            "• Chạy liên tục 24/7 (lò CCV / máy đùn cao điểm): Áp dụng mô hình 3 Ca – 4 Kíp (3 kíp chạy luân phiên 8h, 1 kíp nghỉ xoay vòng đảm bảo sức khỏe & đúng luật!)."
        ),
        "cadivi_application": (
            "OE CADIVI lập mô hình định biên nhân sự hàng tháng/quý trình Ban Giám đốc khi sản lượng tăng mùa cao điểm xây dựng — ưu tiên tăng OLE & đứng đa máy trước khi tuyển mới hoặc tăng ca đắt đỏ."
        ),
        "cadivi_example": (
            "Ví dụ: Khi đơn hàng cáp lực tăng 25%, thay vì tăng ca toàn xưởng vượt trần 40h/tháng (tốn phụ cấp 150–200%), OE lập phương án điều chuyển 4 công nhân đa kỹ năng từ khu Kéo dư tải sang mở Ca 3 cục bộ cho riêng 2 máy Đùn cổ chai!"
        ),
        "related": ["OLE", "RCCP", "Man-Machine Chart", "Takt Time", "Learning Curve"],
        "doc_key": "oe_field_execution_case_test"
    },
    # =================================================================
    # NHÓM 9: 12 THUẬT NGỮ TÁCH ĐỘC LẬP (CHỐNG SELF-LINK & ĐÀO SÂU CHUYÊN BIỆT)
    # =================================================================
    "Green Belt": {
        "term": "Green Belt",
        "full_name": "Lean Six Sigma Green Belt / Black Belt — Hệ Thống Cấp Bậc Đai Chuyên Gia Cải Tiến",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Green Belt", "Black Belt", "Yellow Belt"],
        "case_sensitive": [],
        "short_desc": "Hệ thống chứng chỉ chuyên môn quốc tế (White → Yellow → Green → Black → Master Black Belt) xác nhận năng lực dẫn dắt dự án cải tiến DMAIC và phân tích thống kê.",
        "definition": (
            "Hệ thống đai Six Sigma mô phỏng theo võ thuật nhằm phân tầng rõ vai trò trong nhà máy: White/Yellow Belt dành cho công nhân & tổ trưởng tham gia nhóm Kaizen; Green Belt dành cho Chuyên viên OE/IE/QA dẫn dắt dự án DMAIC liên phòng ban sử dụng Minitab (Cpk, t-test, ANOVA, PFMEA); Black Belt chuyên trách dự án phức tạp xuyên nhà máy (DOE, hồi quy đa biến, tiết kiệm hàng tỷ đồng/năm)."
        ),
        "formula_or_spec": (
            "• White/Yellow Belt: Hiểu 7 QC Tools, 5S, 8 Lãng phí, hỗ trợ thu thập số liệu.\n"
            "• Green Belt (Điểm cộng lớn JD CADIVI OE): Chủ trì dự án DMAIC 2–4 tháng, thành thạo Minitab SPC/Cpk/t-test/MSA, ROI rõ ràng.\n"
            "• Black Belt: Chuyên gia toàn thời gian, làm chủ DOE/Regression/Cost Deployment, đào tạo & kèm cặp Green Belt."
        ),
        "cadivi_application": (
            "Trong JD CADIVI Miền Trung, 'có Lean Six Sigma Green Belt' là lợi thế cạnh tranh lớn. Kể cả khi chưa thi chứng chỉ quốc tế ASQ/IASSC, bạn vẫn ghi điểm tuyệt đối nếu chứng minh được tư duy & thực chiến đúng chuẩn Green Belt (DMAIC + Minitab + ROI)."
        ),
        "cadivi_example": (
            "Ví dụ 1 (Phỏng vấn): Trình bày bài toán giảm 50% thời gian đo Canon INEX theo đúng khung 5 pha DMAIC thay vì kể lan man giúp hội đồng thấy rõ năng lực chuẩn Green Belt.\n"
            "Ví dụ 2 (Tại CADIVI): Một dự án cấp Green Belt điển hình tại nhà máy cáp là giảm tỷ lệ phế phẩm đùn XLPE từ 3.5% xuống dưới 1.0% trong 90 ngày, tiết kiệm 600–900 triệu VNĐ/năm."
        ),
        "related": ["Six Sigma", "Lean Six Sigma", "DMAIC", "Minitab", "OE"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "Lean Six Sigma": {
        "term": "Lean Six Sigma",
        "full_name": "Lean Six Sigma (LSS) — Phương Pháp Luận Kết Hợp Tốc Độ Tinh Gọn (Lean) & Độ Chính Xác Thống Kê (Six Sigma)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Lean Six Sigma", "LSS"],
        "case_sensitive": ["LSS"],
        "short_desc": "Hợp nhất sức mạnh xóa lãng phí tăng tốc độ của Lean với sức mạnh giảm biến thiên xóa khuyết tật của Six Sigma — bộ khung xương sống của mọi Chuyên viên OE hiện đại.",
        "definition": (
            "Nếu chỉ làm Lean mà bỏ qua Six Sigma, chuyền chạy rất nhanh nhưng vẫn có thể tạo ra sản phẩm lệch chuẩn/không ổn định; nếu chỉ làm Six Sigma mà quên Lean, sản phẩm rất chính xác nhưng tồn kho WIP chất đống và đổi mã mất cả giờ. Lean Six Sigma giải quyết đồng thời cả hai: Nhanh – Gọn – Ổn định – Chi phí thấp nhất!"
        ),
        "formula_or_spec": (
            "• Lean = Tăng tốc dòng chảy (Giảm Lead Time, xóa 8 Lãng phí, SMED, 5S, Kanban).\n"
            "• Six Sigma = Thu hẹp độ lệch chuẩn σ (Giảm lỗi, tăng Cpk, kiểm định thống kê DMAIC).\n"
            "• Quy tắc vàng thực chiến: Luôn làm Lean trước (ổn định 5S, chuẩn hóa SOP, giảm hỗn loạn) rồi mới đưa Six Sigma vào tinh chỉnh thông số bằng Minitab!"
        ),
        "cadivi_application": (
            "Tại CADIVI Miền Trung, dây chuyền cáp vừa cần tốc độ cao & đổi mã nhanh (Lean/SMED) vừa phải khống chế sai số đồng/nhựa ở mức phần trăm milimet (Six Sigma/SPC) — vì thế Lean Six Sigma là bộ công cụ chuẩn xác nhất."
        ),
        "cadivi_example": (
            "Ví dụ 1 (Đời sống): Một quán phở dùng Lean để bố trí bếp gọn gàng ra bát trong 2 phút (nhanh), kết hợp Six Sigma dùng muôi định lượng chuẩn để 1,000 bát đều ngon y hệt nhau (ổn định).\n"
            "Ví dụ 2 (Tại CADIVI): Kết hợp SMED (Lean) cắt thời gian đổi màu máy đùn 55p → 12p và SPC/DMAIC (Six Sigma) thu hẹp độ lệch chuẩn chiều dày vỏ từ 0.055mm → 0.020mm trên cùng một dây chuyền!"
        ),
        "related": ["Lean", "Six Sigma", "Green Belt", "DMAIC", "OE"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "HMI": {
        "term": "HMI",
        "full_name": "Human-Machine Interface — Màn Hình Giao Tiếp Người – Máy Trên Dây Chuyền Sản Xuất",
        "category": "Hệ Thống Số Hóa & Phần Mềm",
        "aliases": ["HMI"],
        "case_sensitive": ["HMI"],
        "short_desc": "Màn hình cảm ứng gắn trực tiếp trên tủ điều khiển máy kéo, máy bện, máy đùn cáp cho phép công nhân xem tốc độ, nhiệt độ, nạp Recipe và ghi nhận mã dừng máy.",
        "definition": (
            "HMI là cầu nối trực tiếp giữa người công nhân và bộ điều khiển PLC tại từng máy đơn lẻ (khác với SCADA giám sát tập trung nhiều máy trên máy tính trung tâm). Thiết kế màn hình HMI trực quan, khóa quyền chỉnh sửa thông số công nghệ và tích hợp nạp công thức chạy máy (Recipe) là công cụ Poka-Yoke cực mạnh."
        ),
        "formula_or_spec": (
            "• Phân quyền chuẩn trên HMI: Cấp 1 Công nhân (Start/Stop, chọn mã dừng máy, nạp Recipe) | Cấp 2 Kỹ thuật/OE (Cài đặt giới hạn nhiệt, Recipe chuẩn) | Cấp 3 Bảo trì (Chẩn đoán I/O, hiệu chuẩn cảm biến)."
        ),
        "cadivi_application": (
            "Trên các máy đùn bọc cáp & máy kéo hiện đại tại CADIVI, HMI hiển thị tức thời nhiệt độ 6 vùng nòng đùn, tốc độ mét/phút, áp suất Melt Pressure, đường kính Laser Gauge và số lỗi Spark Tester."
        ),
        "cadivi_example": (
            "Ví dụ 1 (Đời sống): Màn hình cảm ứng bảng điều khiển trên ô tô hiển thị tốc độ, nhiệt độ động cơ và cảnh báo áp suất lốp chính là một dạng HMI.\n"
            "Ví dụ 2 (Tại CADIVI): Cài sẵn thư viện 50 Recipe chuẩn theo mã cáp trên HMI máy đùn + khóa mật khẩu vùng nhiệt giúp giảm thời gian nhập tay thông số khi đổi mã SMED từ 6 phút xuống 15 giây và xóa sạch lỗi cài nhầm nhiệt!"
        ),
        "related": ["PLC", "SCADA", "MES", "Poka-Yoke", "SMED"],
        "doc_key": "erp_mes"
    },
    "MSA": {
        "term": "MSA",
        "full_name": "Measurement System Analysis — Phân Tích Toàn Diện Hệ Thống Đo Lường (Độ Chụm, Độ Đúng, Tuyến Tính, Ổn Định)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["MSA", "Measurement System Analysis"],
        "case_sensitive": ["MSA"],
        "short_desc": "Bộ phương pháp kiểm chứng toàn diện thiết bị đo, người đo và quy trình đo trước khi phân tích dữ liệu — bảo đảm 'dữ liệu đầu vào đáng tin cậy' trong pha Measure.",
        "definition": (
            "Nhiều dự án cải tiến thất bại hoàn toàn vì tin vào dữ liệu đo bị sai lệch do thước mòn, người đo bóp quá tay hoặc máy đo chưa hiệu chuẩn. MSA đánh giá đủ 5 đặc tính của hệ thống đo: Bias (độ chệch so chuẩn), Linearity (tuyến tính trên toàn dải đo), Stability (ổn định theo thời gian), Repeatability (độ lặp lại của thiết bị) và Reproducibility (độ tái lập giữa các người đo — 2 yếu tố cuối chính là Gage R&R!)."
        ),
        "formula_or_spec": (
            "• MSA cho dữ liệu liên tục (mm, Ω, lực kéo): Bias + Stability + Linearity + Gage R&R (%GRR < 10% đạt chuẩn, 10–30% cân nhắc, > 30% loại bỏ).\n"
            "• MSA cho dữ liệu định tính (Đạt/Lỗi bằng mắt — Attribute Agreement Analysis): Hệ số Kappa ≥ 0.75 (tốt ≥ 0.90)."
        ),
        "cadivi_application": (
            "Cực kỳ sát thế mạnh Phòng Kiểm tra (Canon INEX / OGP / Keyence) của bạn! Tại CADIVI, OE chạy MSA cho thước Panme đo chiều dày nhựa, kính hiển vi đo độ đồng tâm, máy Laser Gauge và đánh giá độ đồng thuận kiểm tra ngoại quan vỏ cáp (Attribute MSA) giữa 3 ca QC."
        ),
        "cadivi_example": (
            "Ví dụ 1 (Đời sống): Cân sức khỏe nhà bạn luôn nặng hơn chuẩn +2 kg (lỗi Bias) hoặc mỗi lần bước lên nhảy lệch 1.5 kg (lỗi Repeatability) → Dù bạn ăn kiêng thế nào, số đo cũng đánh lừa bạn!\n"
            "Ví dụ 2 (Tại CADIVI): Trước dự án giảm Over-thickness vỏ PVC, chạy MSA phát hiện 3 KCS dùng thước Panme cơ bóp lực tay khác nhau gây sai lệch tới ±0.04 mm (%GRR = 36% không đạt) → Đổi sang dùng kính hiển vi quang học đo lát cắt giảm %GRR xuống 6.8%!"
        ),
        "related": ["Gage R&R", "Minitab", "SPC", "DMAIC", "Laser Gauge"],
        "doc_key": "minitab_spc"
    },
    "p-value": {
        "term": "p-value",
        "full_name": "p-value (Probability Value) — Giá Trị Xác Suất Kiểm Định Giả Thuyết Thống Kê",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["p-value", "giá trị p"],
        "case_sensitive": [],
        "short_desc": "Thước đo xác suất (từ 0 đến 1) cho biết kết quả cải tiến đo được có khả năng do ăn may ngẫu nhiên hay thực sự có ý nghĩa thống kê (ngưỡng vàng p < 0.05).",
        "definition": (
            "Trong kiểm định giả thuyết (t-test, ANOVA, Chi-Square, hồi quy trên Minitab), giả thuyết gốc H0 cho rằng 'không có sự khác biệt nào giữa Trước và Sau cải tiến'. Giá trị p-value đo xác suất ta quan sát thấy dữ liệu chênh lệch như hiện tại nếu H0 đúng. Quy tắc dễ nhớ nhất của dân Six Sigma: 'If p is low, the null must go!' (p < 0.05 → Bác bỏ H0 → Khẳng định sự khác biệt là THẬT với độ tin cậy 95%!)."
        ),
        "formula_or_spec": (
            "• p < 0.05 (5%): Có ý nghĩa thống kê — cải tiến THỰC SỰ tạo ra khác biệt (không phải ngẫu nhiên).\n"
            "• p < 0.01 (1%): Ý nghĩa thống kê rất mạnh (độ tin cậy 99%).\n"
            "• p ≥ 0.05: Chưa đủ bằng chứng thống kê (có thể do mẫu quá ít, biến thiên quá lớn hoặc giải pháp chưa thực sự hiệu quả)."
        ),
        "cadivi_application": (
            "Là 'tấm khiên khoa học' bắt buộc khi Chuyên viên OE CADIVI báo cáo kết quả Trước–Sau cải tiến trước Ban Giám đốc và các Quản đốc xưởng có tính phản biện cao."
        ),
        "cadivi_example": (
            "Ví dụ 1 (Đời sống): Tung đồng xu 10 lần ra cả 10 lần mặt ngửa có p-value = 0.00098 (< 0.05) → Đủ bằng chứng khẳng định đồng xu bị gian lận chứ không thể do ngẫu nhiên!\n"
            "Ví dụ 2 (Tại CADIVI): Chạy thử quy trình sấy nhựa mới làm giảm lỗi Spark trung bình từ 4.2 xuống 1.8 lỗi/10km. Chạy 2-Sample t-test trên Minitab ra p-value = 0.003 (< 0.05) → Khẳng định vững chắc quy trình mới thực sự hiệu quả để nhân rộng cả 6 máy đùn!"
        ),
        "related": ["2-Sample t-test", "ANOVA", "Chi-Square", "Minitab", "DMAIC"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "Drum-Buffer-Rope": {
        "term": "Drum-Buffer-Rope",
        "full_name": "Drum – Buffer – Rope (DBR) — Cơ Chế Điều Độ Sản Xuất Đồng Bộ Theo Điểm Nghẽn (TOC)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Drum-Buffer-Rope", "DBR"],
        "case_sensitive": ["DBR"],
        "short_desc": "Mô hình điều độ thực chiến của Lý thuyết Điểm Nghẽn (TOC): Trống (Drum) gõ nhịp theo máy cổ chai, Đệm (Buffer) bảo vệ cổ chai không đói hàng, Dây kéo (Rope) kìm đầu vào chống ứ đọng WIP.",
        "definition": (
            "Nếu để máy kéo thô phía đầu chuyền chạy hết công suất 100% trong khi máy đùn phía sau chậm hơn 30%, xưởng sẽ ngập ngụa hàng trăm rulo bán thành phẩm chắn hết lối đi. DBR giải quyết dứt điểm: (1) Drum = lịch chạy chi tiết của đúng máy cổ chai (Xưởng Đùn); (2) Buffer = vùng đệm thời gian/tồn kho an toàn (vd: 1 ca rulo đồng bện) đặt ngay trước máy cổ chai để sự cố ở khâu kéo/bện không làm cổ chai ngừng chạy; (3) Rope = tín hiệu cấp lệnh cho máy đầu chuyền chỉ thả đồng rod vào đúng bằng nhịp máy cổ chai tiêu thụ!"
        ),
        "formula_or_spec": (
            "• Drum (Nhịp trống) = Công suất điểm nghẽn Bottleneck.\n"
            "• Buffer (Vùng đệm) = Tồn kho bảo vệ cổ chai (Green / Yellow / Red Zone).\n"
            "• Rope (Sợi dây kéo) = Tốc độ thả vật tư đầu chuyền = Nhịp Drum (triệt tiêu Overproduction & WIP)."
        ),
        "cadivi_application": (
            "Áp dụng xuất sắc tại CADIVI Miền Trung nơi Xưởng Kéo & Bện thường dư tải hơn Xưởng Đùn cách điện: dùng lịch chạy Xưởng Đùn làm Drum điều phối ngược về Bện và Kéo."
        ),
        "cadivi_example": (
            "Ví dụ 1 (Đời sống): Một đoàn lính hành quân đường rừng — anh lính chậm nhất quyết định tốc độ cả đoàn (Drum); đặt khoảng cách đệm nhỏ phía trước anh ta (Buffer); buộc sợi dây từ anh ta lên anh đi đầu (Rope) để cả đoàn không bị đứt quãng!\n"
            "Ví dụ 2 (Tại CADIVI): Đặt Buffer chuẩn 12 rulo đồng bện trước chuyền Đùn CXV và nối tín hiệu Rope về xưởng Bện giúp giảm 42% tồn kho rulo bán thành phẩm nằm chờ trên sàn trong khi OEE máy đùn không bị mất 1 phút đói hàng nào!"
        ),
        "related": ["TOC", "Bottleneck", "WIP", "Pull System", "RCCP"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "Bottleneck": {
        "term": "Bottleneck",
        "full_name": "Production Bottleneck (Constraint) — Điểm Nghẽn Cổ Chai Quyết Định Công Suất Toàn Hệ Thống",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Bottleneck", "điểm nghẽn", "cổ chai"],
        "case_sensitive": [],
        "short_desc": "Công đoạn hoặc máy móc có năng lực thực tế thấp nhất so với nhu cầu đơn hàng — 1 giờ mất đi ở điểm nghẽn là 1 giờ mất vĩnh viễn của cả nhà máy!",
        "definition": (
            "Giống như cổ chai nước quyết định tốc độ nước chảy ra bất kể thân chai to cỡ nào, trong nhà máy 7 công đoạn nối tiếp, sản lượng xuất xưởng tối đa luôn bị khóa chặt bởi công đoạn có tải cao nhất (> 95–100%). Nhận diện sai điểm nghẽn và đi cải tiến máy đang dư tải là sai lầm lãng phí nguồn lực lớn nhất của người làm OE."
        ),
        "formula_or_spec": (
            "• Dấu hiệu nhận diện Bottleneck tại Genba: (1) Tải RCCP/CRP > 100%, (2) Trước máy luôn ùn ứ núi rulo WIP chờ chạy, (3) Công đoạn ngay sau máy đó thường xuyên thiếu hàng chờ đợi.\n"
            "• Nguyên tắc vàng: Tăng 1 giờ ở máy KHÔNG phải cổ chai = Ảo ảnh (0 đồng doanh thu thêm); tăng 1 giờ ở Bottleneck = Tăng trực tiếp lợi nhuận cả nhà máy!"
        ),
        "cadivi_application": (
            "Tại CADIVI Miền Trung, điểm nghẽn có thể dịch chuyển theo mùa đơn hàng (mùa dây dân dụng hay nghẽn ở Máy Đùn tốc độ cao/Đóng cuộn; mùa cáp lực dự án hay nghẽn ở Đùn XLPE/Lò lưu hóa/Bện giáp DSTA) → OE phải rà soát bảng RCCP hàng tháng để bắt đúng điểm nghẽn hiện hành."
        ),
        "cadivi_example": (
            "Ví dụ 1 (Đời sống): Cầu vượt chỉ có 1 làn xe giữa đại lộ 6 làn — mở rộng đại lộ lên 8 làn cũng chẳng giải quyết được kẹt xe chừng nào chưa mở rộng đúng cây cầu đó!\n"
            "Ví dụ 2 (Tại CADIVI): Báo cáo RCCP tháng 10 cho thấy Kéo tải 75%, Bện tải 86%, Đùn cách điện tải 116% → Dồn toàn lực làm SMED + mở Ca 3 cục bộ cho riêng Đùn cách điện giúp tăng sản lượng giao hàng toàn nhà máy +18%!"
        ),
        "related": ["TOC", "Drum-Buffer-Rope", "RCCP", "Cycle Time", "WIP"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "Jishu Hozen": {
        "term": "Jishu Hozen",
        "full_name": "Jishu Hozen (Autonomous Maintenance) — Bảo Trì Tự Quản Bởi Chính Người Công Nhân Vận Hành (Trụ Cột #1 TPM)",
        "category": "OE, Six Sigma, TOC & Quản Trị Rủi Ro",
        "aliases": ["Jishu Hozen", "Autonomous Maintenance", "bảo trì tự quản"],
        "case_sensitive": [],
        "short_desc": "Trao quyền và đào tạo công nhân đứng máy tự thực hiện vệ sinh, kiểm tra, tra dầu, siết ốc hàng ngày ('Lau chùi chính là Kiểm tra') để phát hiện bất thường trước khi máy hỏng nặng.",
        "definition": (
            "Trong mô hình truyền thống 'Tôi vận hành, anh bảo trì sửa', công nhân cứ chạy máy đến khi gãy trục mới gọi thợ cơ điện. Jishu Hozen xóa bỏ ranh giới đó qua 7 bước chuẩn Nhật (từ vệ sinh ban đầu gắn thẻ Fuguai → loại bỏ nguồn bẩn → lập tiêu chuẩn CIL: Cleaning – Inspection – Lubrication → kiểm tra tổng quát) giúp thợ bảo trì rảnh tay tập trung vào bảo trì dự đoán & đại tu kỹ thuật cao."
        ),
        "formula_or_spec": (
            "• Bộ 3 hoạt động hàng ngày CIL (5–10 phút đầu/cuối ca): Cleaning (Lau sạch bụi nhựa/dầu) – Inspection (Soi rò dầu, lỏng ốc, nóng bất thường) – Lubrication (Bôi trơn đúng điểm & mức dầu).\n"
            "• Quy ước trực quan: Dán tem chỉ vạch nhiệt độ, vạch mức dầu xanh/đỏ, dấu sơn thẳng hàng trên bu-lông để nhìn 3 giây biết ngay có lỏng ốc hay không!"
        ),
        "cadivi_application": (
            "Triển khai cực kỳ hiệu quả cho công nhân đứng máy kéo RBD, máy bện và máy đùn tại CADIVI: kiểm tra mắt đọc Laser Gauge, vòi phun nhũ tương, mức dầu hộp số, lưới phễu hút nhựa trước khi bấm nút chạy ca."
        ),
        "cadivi_example": (
            "Ví dụ 1 (Đời sống): Người lái xe tự kiểm tra lốp, nước rửa kính và đèn cảnh báo mỗi sáng thay vì chờ xe nổ máy nằm đường mới gọi cứu hộ!\n"
            "Ví dụ 2 (Tại CADIVI): Sau 2 tháng áp dụng phiếu CIL 7 phút đầu ca trên 6 máy bện Buncher (lau sạch bụi đồng bám cảm biến đứt sợi + kiểm tra độ căng đai), số lần dừng vặt cảm biến báo giả giảm 68%!"
        ),
        "related": ["TPM", "5S", "Red Tag", "PM Compliance", "MTBF"],
        "doc_key": "oe_six_sigma_dmaic"
    },
    "Red Tag": {
        "term": "Red Tag",
        "full_name": "Red Tagging & Fuguai Tag — Chiến Dịch Gắn Thẻ Đỏ Sàng Lọc 5S & Thẻ Bất Thường Thiết Bị TPM",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Red Tag", "Fuguai", "thẻ đỏ 5S", "thẻ bất thường"],
        "case_sensitive": [],
        "short_desc": "Kỹ thuật gắn thẻ màu trực quan ngay tại hiện trường: Thẻ Đỏ (Red Tag) dùng để sàng lọc vật thừa trong 5S, còn Thẻ Fuguai (Trắng/Đỏ) dùng để đánh dấu điểm hỏng hóc nhỏ trên máy trong TPM.",
        "definition": (
            "Khi đi dọn xưởng 5S hoặc vệ sinh máy TPM, công nhân hay ngại tự ý vứt bỏ đồ cũ hoặc quên mất chỗ máy bị rò dầu/thiếu ốc. Chiến dịch gắn thẻ biến mọi vật thừa và mọi khiếm khuyết vô hình thành 'nhiệm vụ hiện hữu có hạn chót': đồ gắn Red Tag được đưa về Khu vực giữ đồ Thẻ Đỏ (Red Tag Holding Area) 30 ngày — không ai nhận sẽ thanh lý; điểm hỏng gắn thẻ Fuguai Trắng (công nhân tự xử lý) hoặc Đỏ (giao Bảo trì xử lý)."
        ),
        "formula_or_spec": (
            "• Thông tin bắt buộc trên thẻ: Ngày gắn, Tên vật/Vị trí máy, Mô tả bất thường, Người phát hiện, Bộ phận xử lý & Hạn chót (Due Date).\n"
            "• Theo dõi tỷ lệ đóng thẻ (Tag Closure Rate ≥ 85%/tháng) ngay trên bảng SQDCM."
        ),
        "cadivi_application": (
            "Giải phóng mặt bằng kẹt rulo thừa/khuôn cũ không còn dùng trong xưởng CADIVI bằng chiến dịch Red Tag 5S và huy động công nhân phát hiện hàng trăm điểm rò rỉ khí nén/nhũ tương/lỏng nắp che bằng thẻ Fuguai."
        ),
        "cadivi_example": (
            "Ví dụ 1 (Đời sống): Dán nhãn ngày lên những đồ ít dùng trong nhà kho gia đình — sau 6 tháng chưa từng đụng tới thì đem cho hoặc thanh lý để nhà rộng thoáng!\n"
            "Ví dụ 2 (Tại CADIVI): Một ngày chiến dịch Red Tag & Fuguai ở phân xưởng Đùn thu gom 42 bộ Chày–Cối hỏng cũ chắn lối đi và phát hiện 31 điểm rò khí nén + thiếu ốc chắn an toàn, giúp giải phóng 35 m² mặt bằng và xử lý dứt điểm 90% thẻ trong 2 tuần!"
        ),
        "related": ["5S", "Jishu Hozen", "TPM", "Visual Management", "Genba"],
        "doc_key": "lean_muda"
    },
    "Pull System": {
        "term": "Pull System",
        "full_name": "Pull Production System vs Push System — Hệ Thống Sản Xuất Kéo Theo Nhu Cầu Thực Tế",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Pull System", "hệ thống kéo", "Push vs Pull"],
        "case_sensitive": [],
        "short_desc": "Nguyên tắc 'công đoạn sau tiêu thụ đến đâu mới phát tín hiệu kéo công đoạn trước sản xuất bù đúng lượng đó', xóa bỏ căn bệnh sản xuất đẩy (Push) gây ùn ứ tồn kho.",
        "definition": (
            "Trong hệ thống Đẩy (Push), mỗi xưởng chỉ chăm chăm chạy theo kế hoạch dự báo hoặc chạy lấy sản lượng cao nhất để đẹp KPI cục bộ rồi đẩy hàng sang xưởng sau bất kể xưởng sau có cần hay không → sinh ra núi tồn kho WIP, kẹt lối đi, lỗi phát hiện muộn hàng chục tấn. Hệ thống Kéo (Pull) đảo ngược dòng tín hiệu từ đơn hàng khách hàng / công đoạn cuối ngược về đầu chuyền qua thẻ Kanban hoặc ô giới hạn sàn."
        ),
        "formula_or_spec": (
            "• Push = Chạy theo dự báo (Forecast) → Dễ dư hàng chậm bán, thiếu hàng đang cần.\n"
            "• Pull = Chạy theo tín hiệu tiêu thụ thực (Consumption Signal) + Giới hạn WIP tối đa (WIP Cap)."
        ),
        "cadivi_application": (
            "Áp dụng mô hình lai Pull-Push (Decoupling Point) thông minh tại CADIVI: Dây dân dụng bán chạy (VC 1.5–4.0 mm² — nhóm AX) chạy Pull theo siêu thị tồn kho Min/Max; Cáp lực dự án đặc thù (CXV/DSTA — nhóm CZ) kéo theo lệnh đơn hàng MTO kết hợp Drum-Buffer-Rope!"
        ),
        "cadivi_example": (
            "Ví dụ 1 (Đời sống): Siêu thị chỉ bổ sung thêm sữa lên kệ đúng bằng số hộp khách vừa mua (Pull), không bao giờ chất đầy sữa ra giữa lối đi vì nhà máy sữa sản xuất dư (Push)!\n"
            "Ví dụ 2 (Tại CADIVI): Kẻ 10 ô vàng giới hạn WIP (Pull Floor Kanban) giữa xưởng Bện và xưởng Đùn dây VC: khi cả 10 ô đã đầy rulo đồng bện, xưởng Bện tự động chuyển sang bện mã cáp khác đang trống ô thay vì bện tràn ra hành lang!"
        ),
        "related": ["Kanban", "Two-Bin Kanban", "WIP", "Drum-Buffer-Rope", "Lean"],
        "doc_key": "lean_muda"
    },
    "Campaign Scheduling": {
        "term": "Campaign Scheduling",
        "full_name": "Campaign Scheduling (Product Wheel) — Lập Lịch Chạy Gom Đợt Theo Họ Sản Phẩm & Chuỗi Tối Ưu Chuyển Đổi",
        "category": "Lean Manufacturing & Cải Tiến",
        "aliases": ["Campaign Scheduling", "lịch chạy gom đợt", "gom đơn"],
        "case_sensitive": [],
        "short_desc": "Kỹ thuật điều độ gom các đơn hàng cùng loại nhựa, cùng tiết diện hoặc xếp theo trình tự màu Sáng → Tối thành từng 'chiến dịch' (Campaign) để cắt giảm tối đa số lần dừng chuyển đổi máy.",
        "definition": (
            "Trong ngành công nghệ liên tục như đùn bọc cáp điện, chuyển đổi giữa 2 họ nhựa khác nhau (PVC ↔ XLPE ↔ LSZH) hoặc đổi từ màu Đen sang màu Trắng tốn hàng giờ dừng máy và hàng chục kg nhựa xả Purge. Campaign Scheduling sắp xếp lịch chạy thông minh theo vòng tròn chu kỳ cố định (Product Wheel) cân bằng giữa chi phí đổi mã và chi phí tồn kho."
        ),
        "formula_or_spec": (
            "• Quy tắc sắp lịch vàng xưởng Đùn: (1) Gom cùng loại nhựa (PVC / XLPE / LSZH) → (2) Xếp tiết diện tăng dần hoặc giảm dần để ít phải tháo đổi đầu Crosshead → (3) Xếp màu Sáng → Tối (Trắng → Vàng → Đỏ → Xanh → Đen)."
        ),
        "cadivi_application": (
            "Đòn bẩy nâng OEE nhanh nhất gần như tốn 0 đồng CAPEX tại CADIVI Miền Trung — chỉ cần OE phối hợp Phòng Kế hoạch sửa lại thuật toán xếp thứ tự lệnh sản xuất hàng tuần."
        ),
        "cadivi_example": (
            "Ví dụ 1 (Đời sống): Tiệm giặt ủi gom toàn bộ đồ trắng giặt trước rồi mới giặt đồ màu nhạt và cuối cùng là đồ đen — vừa sạch màu vừa không phải tráng máy liên tục!\n"
            "Ví dụ 2 (Tại CADIVI): Tổ chức lịch chạy gom đợt theo chu kỳ 1 tuần cho dòng dây VCm 1.5–4.0 mm² (6 màu) giúp giảm số lần đổi màu ngược Tối → Sáng từ 14 lần/tháng xuống 2 lần/tháng, thu về thêm 11 giờ máy đùn và tiết kiệm 280 kg nhựa xả mỗi tháng!"
        ),
        "related": ["Heijunka", "Color Sequencing", "SMED", "MPS", "Purging"],
        "doc_key": "smed"
    },
    "Standard Work": {
        "term": "Standard Work",
        "full_name": "Standardized Work — Công Việc Chuẩn Hóa (Nền Tảng Của Mọi Cải Tiến Kaizen)",
        "category": "Chỉ Số Hiệu Suất & Năng Suất",
        "aliases": ["Standard Work", "công việc chuẩn"],
        "case_sensitive": [],
        "short_desc": "Phương pháp làm việc tốt nhất, an toàn nhất và ổn định nhất ở thời điểm hiện tại — gồm 3 thành phần bắt buộc: Takt Time, Trình tự thao tác chuẩn và Tồn kho WIP chuẩn.",
        "definition": (
            "Taiichi Ohno (cha đẻ Toyota Production System) khẳng định: 'Không có Chuẩn thì không thể có Kaizen!' Nếu Ca 1, Ca 2 và Ca 3 mỗi người chạy máy đùn hoặc đổi khuôn theo một kiểu riêng thì năng suất và chất lượng sẽ trồi sụt hỗn loạn. Standard Work không phải là văn bản cất tủ kính mà là chuẩn mực sống được treo ngay tại máy và liên tục cập nhật tốt hơn sau mỗi Kaizen."
        ),
        "formula_or_spec": (
            "• 3 yếu tố bắt buộc của Standard Work (khác với SOP chỉ có mô tả bước làm):\n"
            "  1. Takt Time (Nhịp yêu cầu của khách hàng).\n"
            "  2. Work Sequence (Trình tự thao tác tối ưu từng giây).\n"
            "  3. Standard WIP (Số lượng bán thành phẩm chuẩn tối thiểu trên chuyền để dòng chảy mượt)."
        ),
        "cadivi_application": (
            "Xây dựng Standard Work tại CADIVI cho các khâu nhiều thao tác tay như tổ Đóng cuộn khoanh 100m, quy trình đổi khuôn SMED máy đùn, thao tác hàn nối đầu sợi đồng Butt Welder và thao tác kiểm tra mẫu phòng Lab."
        ),
        "cadivi_example": (
            "Ví dụ 1 (Đời sống): Phi công luôn chạy bảng kiểm chuẩn (Checklist) theo đúng trình tự trước khi cất cánh — dù bay 20 năm vẫn tuân thủ để đạt tỷ lệ sai sót gần bằng 0!\n"
            "Ví dụ 2 (Tại CADIVI): Chuẩn hóa thao tác quấn màng co & dán tem cuộn dây VC 100m giữa 3 ca rút chênh lệch sản lượng giữa ca cao nhất và thấp nhất từ 28% xuống còn dưới 5%!"
        ),
        "related": ["SOP", "Work Combination Table", "Time Study", "LSW", "Kaizen"],
        "doc_key": "ole"
    },
}


# Nạp tự động dữ liệu làm sâu toàn diện (định nghĩa phân tích, 2–3 ví dụ thực tế & sai lầm cần tránh) cho toàn bộ 202 thuật ngữ
try:
    import glossary_enrichment as _glossary_enrichment
    _glossary_enrichment.apply_enrichment(GLOSSARY)
except Exception:
    pass


# =====================================================================
# BỘ MÁY NHẬN DIỆN THUẬT NGỮ LAI 2 TẦNG:
#   TẦNG 1: CÔNG THỨC TƯỜNG MINH KIỂU HYPERLINK [[TermKey|Text Hiển Thị]] (CHÍNH XÁC 100%, 0 NHẦM NGHĨA)
#   TẦNG 2: AUTO-DETECT REGEX FALLBACK CHO VĂN BẢN THƯỜNG (NHƯ JD GỐC DÁN TỪ WEB)
# =====================================================================
_EXPLICIT_FORMULA_RE = re.compile(r"\[\[([^\]|]+?)(?:\|([^\]]+?))?\]\]")
_COMPILED_REGEX = None
_EXACT_ALIAS_MAP = {}
_LOWER_ALIAS_MAP = {}


def _build_matcher():
    """Biên dịch 1 biểu thức Regex duy nhất cho toàn bộ từ điển (chạy 1 lần, tốc độ < 2ms/20KB)."""
    global _COMPILED_REGEX, _EXACT_ALIAS_MAP, _LOWER_ALIAS_MAP
    if _COMPILED_REGEX is not None:
        return

    alias_entries = []
    seen_pairs = set()

    for key, info in GLOSSARY.items():
        cs_set = set(info.get("case_sensitive", []))
        aliases = list(info.get("aliases", []))
        if info["term"] not in aliases:
            aliases.insert(0, info["term"])

        for alias in aliases:
            a = alias.strip()
            if not a:
                continue
            is_cs = (a in cs_set)
            pair_id = (a if is_cs else a.lower(), is_cs)
            if pair_id in seen_pairs:
                continue
            seen_pairs.add(pair_id)
            alias_entries.append((a, key, is_cs))

            if is_cs:
                _EXACT_ALIAS_MAP[a] = key
            else:
                _LOWER_ALIAS_MAP[a.lower()] = key

    # Sắp xếp cụm từ DÀI NHẤT lên trước để khớp cụm dài ưu tiên
    alias_entries.sort(key=lambda x: len(x[0]), reverse=True)

    pattern_parts = []
    for a, _key, is_cs in alias_entries:
        escaped = re.escape(a)
        if is_cs:
            pattern_parts.append(escaped)
        else:
            pattern_parts.append(f"(?i:{escaped})")

    full_pattern = r"(?<!\w)(?:" + "|".join(pattern_parts) + r")(?!\w)"
    _COMPILED_REGEX = re.compile(full_pattern)


def find_term_spans(text):
    """
    Tìm toàn bộ vị trí xuất hiện của các thuật ngữ từ điển trong đoạn văn bản thuần.
    Trả về danh sách tuple: [(start_idx, end_idx, matched_text, canonical_key), ...]
    """
    if not text:
        return []
    _build_matcher()
    spans = []
    for m in _COMPILED_REGEX.finditer(text):
        matched = m.group(0)
        key = _EXACT_ALIAS_MAP.get(matched) or _LOWER_ALIAS_MAP.get(matched.lower())
        if key:
            spans.append((m.start(), m.end(), matched, key))
    return spans


def parse_rich_segments(text, auto_detect=True):
    """
    Phân tích chuỗi có thể chứa công thức tường minh [[TermKey|DisplayText]] hoặc [[TermKey]]
    kết hợp tự động nhận diện thuật ngữ cho phần văn bản thường còn lại.
    Trả về danh sách: [(display_text, canonical_key_or_None), ...]
    """
    if not text:
        return []
    _build_matcher()
    segments = []

    def _append_plain(plain_chunk):
        if not plain_chunk:
            return
        if not auto_detect:
            segments.append((plain_chunk, None))
            return
        spans = find_term_spans(plain_chunk)
        if not spans:
            segments.append((plain_chunk, None))
            return
        pos = 0
        for s, e, matched, key in spans:
            if s > pos:
                segments.append((plain_chunk[pos:s], None))
            segments.append((matched, key))
            pos = e
        if pos < len(plain_chunk):
            segments.append((plain_chunk[pos:], None))

    cursor = 0
    for m in _EXPLICIT_FORMULA_RE.finditer(text):
        if m.start() > cursor:
            _append_plain(text[cursor:m.start()])
        raw_key = m.group(1).strip()
        display = (m.group(2) or raw_key).strip()
        info = get_term(raw_key)
        if info:
            segments.append((display, info["term"]))
        else:
            # Nếu key chưa tồn tại trong từ điển, giữ nguyên chữ hiển thị sạch
            segments.append((display, None))
        cursor = m.end()

    if cursor < len(text):
        _append_plain(text[cursor:])

    return segments


def strip_term_formulas(text):
    """Giải mã toàn bộ công thức [[TermKey|DisplayText]] thành văn bản thuần sạch đẹp khi Copy."""
    if not text:
        return ""
    return _EXPLICIT_FORMULA_RE.sub(lambda m: (m.group(2) or m.group(1)).strip(), text)


def term_anchor_id(term_key):
    """Tạo neo liên kết Markdown (anchor slug) ổn định cho từng thuật ngữ."""
    slug = re.sub(r"[^a-z0-9]+", "-", term_key.lower().strip()).strip("-")
    return f"term-{slug}"


def convert_formulas_to_markdown_links(text):
    """Chuyển đổi công thức [[TermKey|DisplayText]] sang Hyperlink Markdown nội bộ [DisplayText](#term-slug)."""
    if not text:
        return ""

    def _repl(m):
        raw_key = m.group(1).strip()
        display = (m.group(2) or raw_key).strip()
        info = get_term(raw_key)
        if info:
            return f"[{display}](#{term_anchor_id(info['term'])})"
        return display

    return _EXPLICIT_FORMULA_RE.sub(_repl, text)


def get_term(term_or_alias):
    """Tra cứu thông tin đầy đủ của một thuật ngữ theo key hoặc bất kỳ alias nào."""
    if not term_or_alias:
        return None
    _build_matcher()
    q = term_or_alias.strip()
    if q in GLOSSARY:
        return GLOSSARY[q]
    key = _EXACT_ALIAS_MAP.get(q) or _LOWER_ALIAS_MAP.get(q.lower())
    if key:
        return GLOSSARY.get(key)
    # Fallback tìm khớp không phân biệt hoa thường trên key chính
    ql = q.lower()
    for k, v in GLOSSARY.items():
        if k.lower() == ql or v["term"].lower() == ql:
            return v
    return None


def get_all_terms():
    """Trả về danh sách toàn bộ thuật ngữ sắp xếp theo tên."""
    return [GLOSSARY[k] for k in sorted(GLOSSARY.keys(), key=lambda x: x.lower())]


def get_categories():
    """Trả về danh sách các nhóm chủ đề thuật ngữ."""
    cats = ["Tất cả nhóm"]
    for info in GLOSSARY.values():
        c = info.get("category", "")
        if c and c not in cats:
            cats.append(c)
    return cats


def search_terms(keyword="", category="Tất cả nhóm"):
    """Lọc nhanh thuật ngữ theo từ khóa và nhóm chủ đề."""
    kw = (keyword or "").strip().lower()
    results = []
    for info in get_all_terms():
        if category and category != "Tất cả nhóm" and info.get("category") != category:
            continue
        if kw:
            haystack = " ".join([
                info.get("term", ""),
                info.get("full_name", ""),
                " ".join(info.get("aliases", [])),
                info.get("short_desc", ""),
                info.get("definition", ""),
                info.get("cadivi_application", ""),
            ]).lower()
            if kw not in haystack:
                continue
        results.append(info)
    return results
