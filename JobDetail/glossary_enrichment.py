# -*- coding: utf-8 -*-
"""
glossary_enrichment.py — Kho Dữ Liệu Làm Sâu Toàn Diện Cho Toàn Bộ 202 Thuật Ngữ OE & Dây Cáp Điện CADIVI.

Mỗi thuật ngữ được bổ sung chiều sâu bài giảng mini gồm:
  - definition_deep: Giải thích cặn kẽ từ gốc, cơ chế hoạt động, phân biệt khái niệm dễ nhầm.
  - cadivi_application_deep: Chỉ rõ phân xưởng áp dụng, phòng ban phối hợp & kịch bản thực tế tại CADIVI Miền Trung.
  - examples_deep: 2–3 ví dụ cụ thể giàu số liệu (gồm ví dụ trực quan đời sống + ví dụ tính toán CADIVI + kịch bản hiện trường).
  - common_mistakes: Các sai lầm kinh điển người mới/nhà máy hay mắc & mẹo xử lý chuẩn chuyên gia OE.
  - lesson_id: Mã bài học tương ứng trong Giáo Trình OE A–Z (oe_curriculum.py).

Lưu ý định dạng: 100% Unicode thuần, KHÔNG dùng dấu '$', KHÔNG dùng '**' hay '[[' bên trong nội dung làm giàu
để tránh rò rỉ cú pháp thô ra giao diện hoặc file Markdown.
"""

ENRICHMENTS = {
    # =========================================================================
    # CHUNK 1: HỆ THỐNG SỐ HÓA (16) + CHỈ SỐ HIỆU SUẤT (19) + QUẢN TRỊ & AN TOÀN ISO (11)
    # =========================================================================
    "MES": {
        "lesson_id": "L6.2",
        "definition_extra": (
            "\n• Bản chất phân tầng: Nếu ERP là 'bộ não kinh doanh' đứng ở tầng văn phòng (lập kế hoạch tháng/tuần, tính tiền lương, kế toán tồn kho) và PLC là 'dây thần kinh' gắn trực tiếp trên động cơ máy, thì MES chính là 'hệ thần kinh trung ương' ở giữa — chuyển lệnh sản xuất từ ERP xuống từng máy và thu ngược từng mét cáp, từng giây dừng máy, từng cuộn phế liệu theo thời gian thực (real-time).\n"
            "• 4 trụ cột cốt lõi của MES chuẩn MESA-11: (1) Điều độ & Giao lệnh máy (Dispatching), (2) Thu thập dữ liệu tự động từ cảm biến/PLC (Data Acquisition), (3) Quản lý chất lượng & SPC trực tuyến (Quality Management), (4) Truy xuất nguồn gốc phả hệ lô hàng (Genealogy / Traceability)."
        ),
        "cadivi_application_extra": (
            "\n• Phân xưởng triển khai trọng điểm: Ưu tiên gắn đầu tiên ở Xưởng Đùn bọc cách điện/vỏ (nút thắt công suất) và Xưởng Kéo thô RBD, sau đó mở rộng sang Xưởng Bện và Đóng cuộn.\n"
            "• Phối hợp liên phòng ban: OE định nghĩa chuẩn mã lý do dừng máy (Downtime Codes) và công thức OEE/Scrap; Cơ điện kết nối tín hiệu chạy/dừng từ PLC/Encoder/Spark Tester; IT & nhà cung cấp MES dựng giao diện màn hình nhập liệu tại máy; Kế hoạch & Kế toán đối chiếu số liệu đóng lệnh về ERP."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Giống như ứng dụng Grab/Be theo dõi tài xế theo từng giây trên bản đồ (MES), khác với bảng kế hoạch doanh thu tháng của Giám đốc (ERP) và bàn đạp ga/phanh trên xe (PLC).\n"
            "\n• Ví dụ 2 (Tính toán hiệu quả tại CADIVI): Trước khi có MES, 6 máy đùn ghi tay sổ ca mất 25 phút/ca/tổ trưởng và tỷ lệ quên ghi các lần dừng vặt dưới 5 phút lên tới 35% (làm OEE báo cáo ảo 82% trong khi thực tế chỉ 67%). Khi kết nối xung Encoder & cảm biến chạy máy vào MES, dữ liệu đổ về Power BI tức thì sau 10 giây, tiết kiệm 150 giờ nhập liệu/tháng và phơi bày ngay 42 giờ dừng vặt/tháng để OE xử lý.\n"
            "\n• Ví dụ 3 (Truy xuất lỗi khẩn cấp): Khi khách hàng dự án phản ánh 1 cuộn cáp CXV 3×50 bị rỗ vỏ, chỉ cần quét mã vạch rulo trên MES trong 15 giây là truy ngược ra ngay cuộn cáp chạy ở Máy Đùn số 3, Ca 2 ngày 14/05, dùng lô hạt nhựa XLPE số L-204 và tổ trưởng vận hành nào — khoanh vùng kiểm tra đúng 8 cuộn cùng lô thay vì thu hồi cả 200 cuộn!"
        ),
        "common_mistakes": (
            "1. Bẫy 'Số hóa sự hỗn loạn': Triển khai MES khi bảng mã lỗi dừng máy còn 80 mã rườm rà, định mức tốc độ chuẩn chưa đo đạc → Công nhân chọn đại 'Lỗi khác' làm dữ liệu rác 100%.\n"
            "2. Mẹo OE: Trước khi đầu tư MES đắt tiền, hãy chuẩn hóa quy trình nhập liệu & bảng mã dừng máy (tối đa 12–15 mã chuẩn theo 6 Big Losses) bằng Excel/Power Query trong 2–3 tháng rồi mới chuyển lên phần mềm MES!"
        )
    },
    "ERP": {
        "lesson_id": "L6.2",
        "definition_extra": (
            "\n• Bản chất tích hợp: Thay vì Phòng Mua hàng dùng 1 file Excel, Kho dùng 1 phần mềm riêng, Sản xuất ghi sổ giấy và Kế toán nhập lại hóa đơn (lệch số liên tục), ERP gom tất cả vào MỘT cơ sở dữ liệu duy nhất (Single Source of Truth): khi kho xuất 2 tấn đồng cho lệnh SX, tồn kho giảm ngay, giá trị dở dang (WIP) tăng ngay và phòng Mua hàng thấy ngay chạm điểm ROP cần mua bổ sung.\n"
            "• Các phân hệ cốt lõi liên quan trực tiếp đến OE: PP (Hoạch định sản xuất, BOM, Routing), MM (Quản lý vật tư & tồn kho), QM (Kiểm soát chất lượng IQC/OQC), PM (Bảo trì thiết bị), CO (Kế toán giá thành Standard Cost)."
        ),
        "cadivi_application_extra": (
            "\n• Vai trò của OE trên ERP: OE là người kiểm toán độ sạch của Master Data (Cây định mức MBOM, Tốc độ định mức Routing, Tỷ lệ hao phí chuẩn Scrap Factor). Nếu Master Data trên ERP sai lệch 2%, toàn bộ báo cáo giá thành và hoạch định vật tư MRP cả nhà máy sẽ sai dây chuyền!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Giống như hệ thống ngân hàng lõi — khi bạn quẹt thẻ mua hàng, số dư tài khoản, tin nhắn SMS và sao kê cuối tháng tự động cập nhật đồng bộ ngay lập tức mà không ai phải cộng sổ tay.\n"
            "\n• Ví dụ 2 (Thực tế tại CADIVI): Rà soát dữ liệu Routing trên ERP cho thấy tốc độ chuẩn của máy đùn dây VC 2.5 đang để con số cũ năm 2020 là 240 m/phút (trong khi máy sau nâng cấp chạy được 320 m/phút) → Làm hệ thống CRP báo ảo xưởng đang quá tải 115%! Cập nhật lại đúng Master Data giúp kế hoạch giao hàng chính xác hơn ngay lập tức."
        ),
        "common_mistakes": (
            "1. Nhầm lẫn ERP với MES: Ép kế toán/thủ kho nhập tay từng phút dừng máy vào ERP — ERP không sinh ra để quản trị theo giây dưới xưởng.\n"
            "2. Bỏ quên kiểm toán Master Data: Đổi công thức nhựa hoặc cải tiến tốc độ máy xong nhưng quên cập nhật MBOM/Routing trên ERP khiến báo cáo BOM Variance bị lệch ảo nhiều tháng liền."
        )
    },
    "SAP PP": {
        "lesson_id": "L6.2",
        "definition_extra": (
            "\n• Cấu trúc 4 dữ liệu gốc (Master Data) bắt buộc OE phải nắm trong SAP PP: (1) Material Master (Mã hàng đồng, nhựa, bán thành phẩm, thành phẩm), (2) BOM (Định mức nguyên vật liệu), (3) Work Center (Năng lực từng máy kéo/bện/đùn + đơn giá giờ máy), (4) Routing (Trình tự công đoạn & thời gian chạy chuẩn/đổi mã).\n"
            "• Luồng vận hành 1 lệnh sản xuất chuẩn: MRP tạo Planned Order → Chuyển thành Production Order (CO01) → Xuất kho vật tư Goods Issue (MIGO) → Xác nhận sản lượng & phế Confirmation (CO11N) → Nhập kho thành phẩm Goods Receipt → Quyết toán chênh lệch giá thành Variance Settlement."
        ),
        "cadivi_application_extra": (
            "\n• Phối hợp thực chiến: OE khai thác báo cáo lệnh sản xuất (COOIS / CO14) từ SAP PP đổ vào Power Query / Power BI để phân tích chênh lệch vật tư thực tế vs chuẩn (BOM Variance) và chênh lệch giờ máy thực tế vs Routing trên từng dây chuyền CADIVI."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Giống như phiếu chế biến món ăn chuẩn của chuỗi nhà hàng lớn — quy định rõ nguyên liệu (BOM), bếp nào nấu (Work Center), các bước & số phút nấu (Routing) để tính đúng giá vốn mỗi đĩa ăn.\n"
            "\n• Ví dụ 2 (Thực tế tại CADIVI): Đối chiếu màn hình xác nhận lệnh CO11N cho 10 lệnh sản xuất cáp CXV 3×50 phát hiện xưởng chỉ ghi nhận tổng phế phẩm chung mà không tách 'Phế đồng trần' vs 'Phế đồng dính nhựa' → OE đề xuất tách 2 mã Reason Code phế trên SAP PP giúp Kế toán hạch toán thu hồi đồng chính xác thêm hàng trăm triệu đồng/quý."
        ),
        "common_mistakes": (
            "1. Backflushing mù quáng: Cấu hình ERP tự động trừ kho theo định mức chuẩn (Backflush) mà không cân phế thực tế cuối ca → Trên máy tính lúc nào BOM Variance cũng bằng 0 đẹp như mơ, đến cuối năm kiểm kê kho lại hụt hàng chục tấn đồng!\n"
            "2. Chậm đóng lệnh (TECO) dẫn tới chi phí dở dang kéo sang tháng sau làm méo báo cáo giá thành."
        )
    },
    "SCADA": {
        "lesson_id": "L6.2",
        "definition_extra": (
            "\n• Phân biệt SCADA vs HMI vs MES: HMI chỉ đứng điều khiển 1 máy đơn lẻ tại chỗ; SCADA gom tín hiệu từ hàng loạt PLC/cảm biến (nhiệt độ, áp suất, dòng điện, tốc độ) của cả phân xưởng lên màn hình trung tâm phòng điều hành kèm chức năng cảnh báo sự cố (Alarm) và lưu đồ thị xu hướng lịch sử (Historian); còn MES gắn các thông số máy đó với Lệnh sản xuất, Mã khách hàng, OEE và Giá thành."
        ),
        "cadivi_application_extra": (
            "\n• Ứng dụng đắt giá nhất tại CADIVI: Giám sát tập trung hệ thống phụ trợ tiêu thụ điện lớn (Tháp giải nhiệt Chiller, Máy nén khí, Bể nhũ tương kéo đồng, Lò ủ chuông, Bể xông XLPE) và đồ thị nhiệt độ/áp suất đầu đùn nhiều vùng trên các dây chuyền cáp trung thế CCV."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Phòng điều độ điện lực quốc gia nhìn màn hình lớn theo dõi điện áp và đóng cắt trạm biến áp toàn vùng — đó chính là SCADA.\n"
            "\n• Ví dụ 2 (Thực tế tại CADIVI): Xuất dữ liệu Historian từ SCADA nhiệt độ nước máng làm mát (Cooling Trough) 30 ngày cho thấy cứ từ 13:00–16:00 trưa nắng Đà Nẵng, nhiệt độ nước vọt từ 24°C lên 34°C trùng khớp 100% khung giờ vỏ cáp bị trầy xước và công nhân phải hạ tốc độ đùn xuống 20%!"
        ),
        "common_mistakes": (
            "1. Lắp SCADA để 'ngắm cho đẹp' trên TV phòng họp mà không đặt ngưỡng cảnh báo tự động (Alarm Threshold) và không xuất log dữ liệu cho OE chạy phân tích tương quan Scatter/SPC."
        )
    },
    "HMI": {
        "lesson_id": "L6.2",
        "definition_extra": (
            "\n• Kiến trúc giao diện tốt theo chuẩn OE: Một màn hình HMI chuẩn công nghiệp phải giúp công nhân đứng cách 1 mét đọc được ngay trong 3 giây: Máy đang chạy hay dừng (Xanh/Đỏ), Tốc độ thực tế so với Tốc độ chuẩn (vd: 295 / 320 m/phút), Đường kính thực đo từ Laser Gauge so với cận USL/LSL, và số lần báo lỗi Spark Tester trong cuộn."
        ),
        "cadivi_application_extra": (
            "\n• Ứng dụng tại CADIVI Miền Trung: Chuẩn hóa thư viện công thức chạy máy (Recipe Library) nạp 1-chạm trên HMI máy đùn & máy kéo, đồng thời phân quyền mật khẩu để ngăn thói quen công nhân tự ý vặn tăng nhiệt độ nòng hoặc giảm tốc độ kéo theo cảm tính."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Đời sống): Bảng đồng hồ điện tử trên xe hơi hiển thị tốc độ, cảnh báo nhiệt độ động cơ, mức nhiên liệu và nút chọn chế độ lái Eco/Sport.\n"
            "\n• Ví dụ 2 (Tính toán tại CADIVI): Khóa quyền cài đặt thủ công 7 vùng nhiệt độ trên HMI máy đùn Ø90 và chuyển sang quét Barcode lệnh sản xuất tự nạp Recipe chuẩn giúp cắt thời gian cài thông số từ 8 phút xuống 20 giây và xóa 100% sự cố cháy nhựa do gõ nhầm 210°C thành 240°C.\n"
            "\n• Ví dụ 3 (Thu thập Downtime tại nguồn): Thêm 1 màn hình pop-up 12 nút chọn lý do dừng máy ngay trên HMI (máy dừng quá 2 phút tự hiện bảng bắt buộc chọn lý do trước khi chạy tiếp) giúp độ chính xác dữ liệu OEE tăng từ 65% lên 97%."
        ),
        "common_mistakes": (
            "1. Dùng chung 1 mật khẩu Admin cho cả xưởng khiến công nhân tự ý chỉnh thông số phá vỡ cửa sổ công nghệ đã chốt trong Control Plan.\n"
            "2. Màn hình HMI toàn tiếng Trung/Đức không có nhãn hướng dẫn tiếng Việt (Visual OPL) bên cạnh khiến thợ mới dễ bấm nhầm."
        )
    },
    "PLC": {
        "lesson_id": "L6.2",
        "definition_extra": (
            "\n• Bản chất công nghiệp: Khác với máy tính văn phòng dễ treo Windows khi nóng bụi, PLC (như Siemens S7-1200/1500, Mitsubishi FX/Q, Omron, Allen-Bradley) là máy tính điều khiển siêu bền chạy vòng lặp thời gian thực tính bằng mili-giây (1–10 ms) để điều khiển biến tần động cơ, đóng ngắt điện trở nhiệt, đọc xung Encoder đo mét và dừng máy khẩn cấp khi cảm biến đứt dây tác động."
        ),
        "cadivi_application_extra": (
            "\n• Tương tác của OE với PLC: OE không nhất thiết phải lập trình PLC sâu như kỹ sư Tự động hóa, nhưng cần hiểu cách lấy tín hiệu từ PLC (qua cổng Ethernet OPC-UA/Modbus hoặc rơ-le tiếp điểm khô) để đo tự động giờ chạy máy, tốc độ mét/phút và kích hoạt các cơ cấu Poka-Yoke tự dừng máy."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Đời sống): Bộ mạch điều khiển máy giặt tự động đo mực nước, quay lồng đúng số vòng, ngắt điện khi mở nắp an toàn — trong nhà máy, PLC làm đúng vai trò đó ở quy mô cực lớn và chính xác đến từng mili-giây.\n"
            "\n• Ví dụ 2 (Thực tế tại CADIVI): Gắn thêm 1 tín hiệu từ máy đo Laser Gauge nối về PLC máy đùn để tự động điều chỉnh tốc độ bánh kéo Capstan theo vòng kín (Closed-loop PID) giữ đường kính ngoài dây VC 2.5 ổn định trong ±0.015 mm thay vì công nhân phải canh vặn chiết áp bằng tay!"
        ),
        "common_mistakes": (
            "1. Ngại đụng vào dữ liệu máy vì sợ phải thay PLC mới tốn hàng trăm triệu — thực tế với các máy kéo/bện đời cũ không có cổng mạng, OE vẫn có thể gắn bộ đọc tín hiệu dòng điện CT hoặc cảm biến quang giá chỉ vài trăm nghìn đồng để đo trạng thái chạy/dừng tự động!"
        )
    },
    "ISA-95": {
        "lesson_id": "L6.2",
        "definition_extra": (
            "\n• Hiểu gọn Kim tự tháp 5 tầng ISA-95 (ANSI/ISA-95):\n"
            "  - Tầng 0 (Physical Process): Quy trình vật lý thực tế (sợi đồng đang kéo, nhựa đang chảy, dây cáp đang chạy).\n"
            "  - Tầng 1 (Sensors & Actuators): Cảm biến nhiệt, Laser Gauge, Spark Tester, Encoder đo mét, biến tần VFD.\n"
            "  - Tầng 2 (Control — PLC / HMI / SCADA): Điều khiển máy chạy tự động theo mili-giây và giám sát thông số vận hành.\n"
            "  - Tầng 3 (MOM / MES): Điều hành sản xuất theo ca/giờ — OEE, truy xuất rulo, quản lý bảo trì, Lab QA/QC.\n"
            "  - Tầng 4 (Business — ERP / SAP): Hoạch định S&OP/MPS/MRP, tài chính kế toán, mua bán hàng theo ngày/tuần/tháng."
        ),
        "cadivi_application_extra": (
            "\n• Giá trị cho OE CADIVI: Dùng mô hình ISA-95 làm bản đồ lộ trình chuyển đổi số nhà máy từng bước — biết rõ nhà máy đang ở tầng nào (ví dụ đã có Tầng 1–2 PLC & Tầng 4 ERP nhưng đang trống Tầng 3 MES) để đề xuất dự án lấp đúng khoảng trống chi phí thấp nhất."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như phân cấp trong công ty: Công nhân trực tiếp làm (Tầng 0–1) → Tổ trưởng điều khiển tại chỗ (Tầng 2) → Quản đốc/OE điều hành sản xuất cả xưởng (Tầng 3) → Ban Giám đốc quản trị tài chính & hợp đồng (Tầng 4).\n"
            "\n• Ví dụ 2 (Tại CADIVI): Dùng Python/Excel Power Query đóng vai trò 'Mini-MES Tầng 3' tạm thời kết nối file log xuất từ máy đùn (Tầng 2) với định mức BOM xuất từ ERP (Tầng 4) giúp tự động hóa báo cáo OEE/BOM trong 2 tuần với chi phí 0 đồng phần mềm!"
        ),
        "common_mistakes": (
            "1. Bỏ nhảy cóc tầng (mua phần mềm báo cáo Tầng 4/BI cực đẹp nhưng Tầng 1–2 không có cảm biến đếm mét hay đo dừng máy chuẩn → Dữ liệu đầu vào vẫn nhập tay sai lệch)."
        )
    },
    "Minitab": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Vai trò số 1 trong giới OE & Six Sigma: Excel rất mạnh về tổng hợp bảng biểu tài chính/sản lượng, nhưng khi cần chứng minh thống kê khoa học (phân phối chuẩn hay không, Cpk/Ppk thực tế bao nhiêu, sai khác Trước–Sau có ý nghĩa p < 0.05 không, tìm yếu tố nhiệt độ/tốc độ nào gây lỗi nhiều nhất qua DOE/ANOVA), Minitab là phần mềm tiêu chuẩn vàng toàn cầu vì chỉ cần 3 cú click là ra đầy đủ biểu đồ và kết luận chuẩn xác.\n"
            "• 6 nhóm công cụ Minitab OE CADIVI dùng nhiều nhất: (1) Capability Analysis (Cp/Cpk/Ppk), (2) Control Charts (Xbar-R, I-MR, P-chart), (3) MSA (Gage R&R & Attribute Agreement), (4) Hypothesis Tests (2-Sample t-test, Paired t-test, One-Way ANOVA, Chi-Square), (5) Regression & Correlation, (6) DOE (Thiết kế thí nghiệm tối ưu công nghệ đùn)."
        ),
        "cadivi_application_extra": (
            "\n• Sử dụng thường xuyên tại CADIVI Miền Trung cùng Phòng Lab QA/QC: Lấy dữ liệu đo chiều dày vỏ bọc 30–100 mẫu chạy Capability Analysis định lượng mức nhựa bọc dư Over-thickness; lấy dữ liệu đứt sợi 3 nhà cung cấp đồng chạy ANOVA tìm nhà cung cấp ổn định nhất; lấy dữ liệu đổi mã 30 ngày Trước–Sau chạy 2-Sample t-test bảo vệ dự án SMED trước Giám đốc."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Kiểm chứng dự án SMED): Thời gian đổi màu máy đùn 25 lần trước SMED trung bình 48.5 phút (σ = 9.2p), sau SMED 25 lần trung bình 16.4 phút (σ = 2.8p). Chạy Stat → Basic Statistics → 2-Sample t trên Minitab cho p-value = 0.000 (< 0.05) → Khẳng định khoa học cải tiến giảm thực 32.1 phút/lần!\n"
            "\n• Ví dụ 2 (Giảm Over-thickness dây CXV): Chạy Stat → Quality Tools → Capability Analysis (Normal) trên 60 mẫu chiều dày XLPE (LSL = 1.07 mm) cho thấy trung bình μ = 1.24 mm, σ = 0.035 mm, Cpk = 1.62 → Chứng minh quá trình đang chạy thừa an toàn tới +0.07 mm so với mức mục tiêu chuẩn 1.17 mm (vẫn giữ Cpk ≥ 1.33) — mở khóa tiết kiệm > 1.2 tỷ VNĐ tiền hạt nhựa/năm!"
        ),
        "common_mistakes": (
            "1. Chạy thẳng Cp/Cpk khi dữ liệu KHÔNG phân phối chuẩn (Non-normal, vd: thời gian dừng máy bị lệch phải) mà quên kiểm tra Normality Test (Anderson-Darling p < 0.05) hoặc quên dùng phép biến đổi Box-Cox.\n"
            "2. Nhìn p-value < 0.05 rồi mừng vội mà quên kiểm tra ý nghĩa thực tiễn (Practical Significance: giảm được 0.2 giây trên chu kỳ 10 phút dù p < 0.05 cũng không đáng đầu tư tiền!)."
        )
    },
    "Power BI": {
        "lesson_id": "L6.4",
        "definition_extra": (
            "\n• Vì sao Power BI thay thế báo cáo Excel tĩnh ở nhà máy hiện đại? Thay vì mỗi sáng OE phải copy-paste 15 file nhật ký ca rồi gửi email ảnh chụp PDF chết cứng, Power BI kết nối trực tiếp thư mục dữ liệu / CSDL SQL / ERP, tự động làm sạch (Power Query), mô hình hóa theo Star Schema (bảng Fact sản lượng/dừng máy nối với bảng Dim Ngày/Máy/Ca/Mã cáp) và cập nhật Dashboard tương tác chỉ bằng 1 nút Refresh (hoặc lịch tự động qua On-premises Gateway).\n"
            "• Thiết kế Dashboard 3 tầng chuẩn nhà máy: Tầng 1 Ban Giám đốc (Tổng OEE, Sản lượng tấn/km, BOM Variance VNĐ, Xu hướng tháng) → Tầng 2 Quản đốc/OE (So sánh từng xưởng/máy, Pareto Top 5 lỗi dừng máy & phế) → Tầng 3 Tổ trưởng (Chi tiết theo từng ca, từng lệnh sản xuất, drill-down tới tận cuộn lỗi)."
        ),
        "cadivi_application_extra": (
            "\n• Lợi thế cực lớn của ứng viên OE: Biến toàn bộ số liệu rời rạc từ Xưởng Kéo – Bện – Đùn – Đóng gói tại CADIVI Miền Trung thành hệ thống quản trị trực quan thời gian thực, rút thời gian tổng hợp báo cáo tuần từ 1–2 ngày xuống còn 5 phút."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Giống như bảng táp-lô máy bay hiển thị đồng thời độ cao, tốc độ, nhiên liệu và cảnh báo động cơ trên 1 màn hình duy nhất thay vì phi công phải lật 5 cuốn sổ giấy.\n"
            "\n• Ví dụ 2 (Tại CADIVI): Dựng trang Dashboard 'OEE & BOM Xưởng Đùn' với 4 bộ lọc (Tháng, Máy Đùn 1–6, Ca 1–3, Nhóm Cáp PVC/XLPE): Giám đốc bấm chọn 'Máy Đùn số 4' lập tức thấy ngay OEE tụt 61% chủ yếu do Ca 3 bị dừng đổi màu 48 phút/lần và phế nhựa vượt định mức +4.2%!"
        ),
        "common_mistakes": (
            "1. Nhồi nhét 15 biểu đồ rối mắt trên 1 trang mà không có thông điệp hành động (nhà quản lý cần nhìn 5 giây biết ngay điểm nào Đỏ và phải làm gì!).\n"
            "2. Dùng cột tính sẵn Average của OEE từng ca thay vì viết DAX Measure chia Tổng Operating / Tổng Planned (gây sai lệch trọng số cực nghiêm trọng!)."
        )
    },
    "Power Query": {
        "lesson_id": "L6.3",
        "definition_extra": (
            "\n• Bản chất công cụ ETL (Extract – Transform – Load) có sẵn miễn phí trong cả Excel và Power BI: Mọi thao tác làm sạch dữ liệu thủ công bạn hay làm lặp đi lặp lại mỗi sáng (gộp 30 file nhật ký ca trong 1 thư mục, xóa dòng trống, tách cột mã cáp, sửa lỗi định dạng ngày dd/mm/yyyy, Unpivot bảng ngang thành bảng dọc, nối mã BOM) được Power Query ghi lại thành chuỗi bước tự động (ngôn ngữ M). Tháng sau có thêm 30 file mới, bạn chỉ cần bỏ vào thư mục và bấm 1 nút 'Refresh All'!"
        ),
        "cadivi_application_extra": (
            "\n• Áp dụng ngay trong 30 ngày đầu thử việc tại CADIVI Miền Trung: Hầu hết nhà máy sản xuất ở Việt Nam đều có hàng chục file Excel báo cáo ca riêng lẻ của từng tổ/xưởng — Power Query (Folder Connector) giúp OE hợp nhất toàn bộ mà không cần thay đổi thói quen nhập liệu của tổ trưởng ngay lập tức."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như máy xay sinh tố tự động — bạn chỉ cần thả trái cây mới (file Excel mới) vào rồi bấm nút là ra ly sinh tố chuẩn vị, không phải gọt cắt bằng tay lại từ đầu mỗi ngày.\n"
            "\n• Ví dụ 2 (Liên hệ kinh nghiệm CV & CADIVI): Tương tự việc bạn từng tự động hóa tổng hợp dữ liệu khách hàng từ 3 ngày xuống 2 giờ và dữ liệu OGP từ 120 phút xuống 15 phút/ngày — tại CADIVI, dùng Power Query gộp 90 file nhật ký ca/tháng của 4 phân xưởng giúp rút thời gian làm báo cáo OEE/BOM tháng từ 2 ngày xuống 3 phút và triệt tiêu 100% lỗi copy-paste nhầm ô!"
        ),
        "common_mistakes": (
            "1. Sửa trực tiếp bằng tay vào bảng kết quả đầu ra của Power Query — lần bấm Refresh kế tiếp mọi chỉnh sửa tay sẽ bị ghi đè mất sạch! Mọi quy tắc chuẩn hóa phải viết bên trong các bước Transform của Power Query."
        )
    },
    "DAX": {
        "lesson_id": "L6.4",
        "definition_extra": (
            "\n• Khác biệt cốt lõi giữa công thức Excel và DAX (Data Analysis Expressions): Excel tính từng ô (A1 + B1), còn DAX tính động trên toàn bộ cột/bảng theo ngữ cảnh bộ lọc hiện tại (Filter Context — khi người dùng bấm chọn Ca 1 hay Máy số 2, mọi Measure DAX tự tính lại chuẩn xác theo đúng trọng số!).\n"
            "• 5 hàm DAX xương sống cho OE: SUM, DIVIDE (tự chống lỗi chia cho 0), CALCULATE (thay đổi điều kiện lọc, vd: tính OEE tháng trước so với tháng này), SUMX (nhân từng dòng rồi cộng tổng, vd: Khối lượng phế × Đơn giá từng mã vật tư), ALL / RANKX (vẽ biểu đồ Pareto 80/20 tích lũy động!)."
        ),
        "cadivi_application_extra": (
            "\n• Dùng để xây dựng bộ chỉ số chuẩn quản trị nhà máy CADIVI trên Power BI & Excel Power Pivot: OEE mét/phút chuẩn trọng số, Scrap % theo kg & theo VNĐ, BOM Cost Variance, OEE tháng này vs tháng trước (MoM) và biểu đồ Pareto nguyên nhân dừng máy tự động co giãn khi lọc theo từng xưởng."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tránh lỗi sai trọng số OEE): Ca 1 chạy 400 phút đạt OEE 90%, Ca 2 chỉ chạy thử 40 phút đạt OEE 40%. Nếu dùng AVERAGE sẽ ra sai 65%! Viết DAX Measure: Availability = DIVIDE(SUM(Fact[RunMin]), SUM(Fact[PlanMin])) tự động tính đúng theo trọng số thời gian thực!\n"
            "\n• Ví dụ 2 (Tính BOM Variance VNĐ trên từng mã cáp): BOM_Loss_VND = SUMX(Fact_Order, (Fact_Order[Actual_Kg] - Fact_Order[Good_Km] * RELATED(Dim_BOM[Std_Kg_Per_Km])) * RELATED(Dim_Material[Unit_Price])) — chỉ 1 dòng DAX tính tức thì lỗ/lãi vật tư của hàng nghìn lệnh sản xuất!"
        ),
        "common_mistakes": (
            "1. Dùng phép chia `/` thay vì `DIVIDE(a, b, 0)` gây lỗi `Infinity` làm hỏng cả biểu đồ khi có máy nghỉ bảo trì (Planned Time = 0).\n"
            "2. Tạo quá nhiều Calculated Column lưu cứng làm phình dung lượng file thay vì viết Measure động."
        )
    },
    "VBA": {
        "lesson_id": "L6.3",
        "definition_extra": (
            "\n• Vai trò thực tế trong môi trường nhà máy: Dù Python và Power BI rất hiện đại, Excel vẫn là ngôn ngữ phổ biến nhất trên máy tính của Tổ trưởng, Kế hoạch và Kế toán nhà máy (không cần cài đặt thêm môi trường IT). VBA Macro cho phép bạn tạo nút bấm '1-Chạm' ngay trên file Excel quen thuộc để tự động tách phiếu lệnh sản xuất, xuất báo cáo PDF gửi email giao ban sáng, kiểm tra lỗi nhập liệu form ca và khóa vùng công thức."
        ),
        "cadivi_application_extra": (
            "\n• Vũ khí lợi thế trực tiếp từ CV của bạn: Đã có kinh nghiệm thực chiến viết VBA/Excel/Access tại Mabuchi → Áp dụng ngay tại CADIVI Miền Trung để tự động chuẩn hóa mẫu báo cáo ca của các tổ, tự xuất phiếu tính BOM cắt rulo (Cut-Length) và báo cáo tuần gửi Quản đốc/Ban Giám đốc."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tự động xuất báo cáo ca sáng): Viết 1 nút Macro trên file tổng hợp sáng 07:30 tự động kiểm tra các ô nhập thiếu, tô đỏ máy có OEE < 65% hoặc phế > 2%, xuất riêng 4 trang PDF cho 4 Quản đốc xưởng chỉ trong 5 giây thay vì mất 45 phút mỗi sáng.\n"
            "\n• Ví dụ 2 (Khống chế nhập liệu sạch): Dùng sự kiện Worksheet_Change kiểm tra ngay khi tổ trưởng nhập Downtime > 480 phút hoặc quên chọn mã lý do dừng máy thì hiện cảnh báo nhắc điền đúng ngay tại nguồn!"
        ),
        "common_mistakes": (
            "1. Quên lưu file dưới đuôi `.xlsm` (lưu nhầm `.xlsx` làm mất sạch code Macro!).\n"
            "2. Viết code vòng lặp từng ô trên 50,000 dòng mà quên tắt `Application.ScreenUpdating = False` khiến Excel chạy chậm hàng phút — xử lý dữ liệu lớn nên kết hợp Power Query hoặc mảng (Array) trong bộ nhớ!"
        )
    },
    "AutoCAD": {
        "lesson_id": "L3.2",
        "definition_extra": (
            "\n• Tại sao Chuyên viên OE nhà máy cáp điện cần biết AutoCAD 2D? Dây chuyền kéo sợi và đùn bọc cáp có chiều dài cực lớn (25–65 mét/chuyền), kết hợp khu vực lưu trữ rulo gỗ nặng 1–5 tấn, đường di chuyển xe nâng rộng ≥ 3.5m và hành lang cẩu trục (Overhead Crane). Mọi ý tưởng tái bố trí mặt bằng (Plant Layout) hay rút ngắn quãng đường vận chuyển (Spaghetti Diagram) đều phải vẽ chính xác theo tỷ lệ thật 1:1 trên AutoCAD để kiểm chứng bán kính quay đầu xe nâng và an toàn PCCC trước khi di dời máy!"
        ),
        "cadivi_application_extra": (
            "\n• Thực tế tại CADIVI Miền Trung: Dùng bản vẽ mặt bằng tổng thể nhà xưởng (`.dwg`) tách riêng từng Layer: Layer Mặt bằng cột/tường, Layer Máy móc hiện trạng, Layer Khu vực WIP/Rulo, Layer Luồng di chuyển người & xe nâng (Spaghetti Hiện trạng vs Tương lai), Layer An toàn PCCC/Lối thoát hiểm."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Vẽ Spaghetti Diagram định lượng): Vẽ đường di chuyển của 1 rulo đồng từ Xưởng Kéo → Xưởng Bện → Xưởng Đùn → Kho thành phẩm trên AutoCAD rồi dùng lệnh `LIST` / `MEASUREGEOM` đo chính xác tổng chiều dài hành trình = 485 mét/rulo → Đề xuất hoán đổi vị trí khu đệm trung gian rút xuống còn 210 mét/rulo (giảm 56.7% lãng phí vận chuyển!).\n"
            "\n• Ví dụ 2 (Thiết kế trạm Đóng cuộn khoanh chữ U): Vẽ lại bố trí bàn dán tem, máy co màng và pallet thành cụm chữ U bán kính thao tác < 1.2m giúp công nhân giảm 60% bước đi bộ thừa mỗi ca!"
        ),
        "common_mistakes": (
            "1. Vẽ Layout chỉ nhìn kích thước thân máy mà quên vùng không gian bảo trì (phải chừa tối thiểu 1.2–1.5m phía sau đầu đùn để rút trục vít ra vệ sinh!) và bán kính quay vòng xe nâng chở rulo 2m.\n"
            "2. Vẽ tất cả lên cùng Layer 0 gây rối không thể tắt/bật so sánh Hiện trạng vs Đề xuất khi trình chiếu Ban Giám đốc."
        )
    },
    "Barcode": {
        "lesson_id": "L6.2",
        "definition_extra": (
            "\n• Bản chất công nghệ định danh tự động (Auto-ID): Gồm 3 cấp phổ biến trong sản xuất: (1) Mã vạch 1D (Code 128 — rẻ, quét nhanh mã lệnh/mã cuộn), (2) Mã QR 2D (chứa được nhiều thông tin: Mã cáp, Chiều dài mét, Khối lượng, Ca, Máy, Lô đồng/nhựa, vẫn quét được khi rách nhẹ 15–30%), (3) Thẻ RFID (đọc không cần nhìn thấy, gắn vĩnh viễn lên rulo thép tái sử dụng hàng trăm vòng).\n"
            "• Giá trị kép: Vừa giảm 90% thời gian ghi chép nhập liệu (OLE), vừa là cơ chế Poka-Yoke chống lấy nhầm nguyên liệu/nhầm rulo!"
        ),
        "cadivi_application_extra": (
            "\n• Điểm sáng liên hệ CV của bạn: Bạn đã có kinh nghiệm thực chiến triển khai quét Barcode tại công đoạn RE7 Fujikura thay sổ tay! Tại CADIVI Miền Trung, áp dụng ngay mô hình dán thẻ QR/Barcode chịu dầu trên từng rulo bán thành phẩm (từ lúc kéo sợi xong → bện → đùn → nhập kho) để kiểm soát FIFO, chiều dài thực và truy xuất nguồn gốc 100%."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Quầy thu ngân siêu thị quét tít 1 giây ra đúng tên hàng, đơn giá và trừ kho tự động — không bao giờ gõ nhầm giá tiền bằng tay.\n"
            "\n• Ví dụ 2 (Poka-Yoke tại máy đùn CADIVI): Trước khi nạp bao hạt nhựa lên phễu máy đùn, công nhân bắt buộc quét mã QR lệnh sản xuất và mã QR bao nhựa — nếu quét nhầm hạt PVC thường vào lệnh chạy cáp chống cháy LSZH, màn hình báo ĐỎ khóa lệnh ngay lập tức!"
        ),
        "common_mistakes": (
            "1. In tem giấy thường dán lên rulo đồng dính dầu nhũ tương → Chỉ 2 giờ sau tem mờ nhòe không quét được! Xưởng cáp phải dùng tem nhựa PVC/PP chống dầu hoặc thẻ nhựa treo móc gắn mã QR."
        )
    },
    "Excel": {
        "lesson_id": "L6.3",
        "definition_extra": (
            "\n• Phân biệt Excel Văn phòng vs Excel Kỹ sư OE Chuyên nghiệp: Người dùng phổ thông chỉ gõ bảng thủ công và dùng VLOOKUP rời rạc; Kỹ sư OE dùng bộ tứ sức mạnh trong Excel gồm: (1) Hàm động nâng cao (`XLOOKUP`, `SUMIFS`, `INDEX-MATCH`, `AGGREGATE`, `LET`), (2) Pivot Table + Slicer phân tích đa chiều trong 30 giây, (3) Power Query + Data Model xử lý hàng triệu dòng vượt giới hạn 1 triệu dòng sheet, (4) Analysis ToolPak & Solver tối ưu bài toán cắt rulo Cut-Length và kiểm định thống kê nhanh khi không có Minitab."
        ),
        "cadivi_application_extra": (
            "\n• Công cụ tác chiến số 1 hàng ngày và cũng là bài thi thực hành phổ biến nhất trong phỏng vấn Vòng 2 vị trí OE CADIVI: Xây dựng file tính OEE m/phút, biểu đồ Pareto 80/20, bảng tính BOM Variance, hoạch định năng lực RCCP và bài toán cắt ghép chiều dài rulo (Excel Solver)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tối ưu Cut-Length bằng Excel Solver): Đơn hàng yêu cầu cắt các đoạn 400m, 550m, 650m từ rulo tiêu chuẩn 2,000m. Dùng Excel Solver (Linear Programming) tìm ra phương án ghép đoạn tối ưu giảm tỷ lệ mẩu cắt thừa từ 7.5% xuống còn 1.1%!\n"
            "\n• Ví dụ 2 (Kiểm tra nhanh dữ liệu 5 ca máy đùn): Dùng `SUMIFS` tách tổng thời gian dừng theo từng nhóm lý do và `Pivot Table` sắp xếp giảm dần + thêm cột `% Tích lũy` để vẽ biểu đồ Pareto 80/20 chỉ trong 2 phút ngay trong buổi test tuyển dụng!"
        ),
        "common_mistakes": (
            "1. Gộp ô (Merge Cells) trong bảng dữ liệu nguồn khiến Pivot Table, sắp xếp và Power Query bị lỗi hoàn toàn.\n"
            "2. Tính OEE tổng tuần bằng cách lấy `AVERAGE(OEE_Ca1:OEE_Ca15)` thay vì tính từ tổng giờ chạy / tổng giờ kế hoạch!"
        )
    },
    "Python": {
        "lesson_id": "L6.3",
        "definition_extra": (
            "\n• Tại sao biết Python là 'vũ khí khác biệt tuyệt đối' của bạn khi ứng tuyển OE CADIVI? Khi xử lý hàng trăm file log cảm biến Laser Gauge / máy đo OGP / báo cáo ca nặng hàng chục MB mà Excel bị đơ treo, 30 dòng code Python (`pandas`, `openpyxl`, `scipy`, `pulp`) chạy vèo trong 2 giây để làm sạch dữ liệu, tự chạy kiểm định t-test/Cpk, giải bài toán tối ưu cắt rulo (Cutting Stock) và xuất thẳng file Excel báo cáo có sẵn biểu đồ đẹp mắt!"
        ),
        "cadivi_application_extra": (
            "\n• Điểm nhấn CV Phan Thanh Thái Bảo: Bạn đã chứng minh năng lực tự viết công cụ Python/VBA/Access rút báo cáo khách hàng 3–7 ngày xuống 2 giờ và nhập liệu OGP 120 phút xuống 15 phút/ngày tại Mabuchi → Mang thẳng tư duy tự động hóa này vào CADIVI Miền Trung để xây công cụ phân tích nhật ký đùn/kéo và tối ưu cắt rulo tự động."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tự động hóa phân tích dữ liệu Laser Gauge): Đọc file CSV 50,000 điểm đo đường kính/ca xuất ra từ máy đo Laser Sikora bằng `pandas`, tự động loại đoạn tăng giảm tốc đầu-đuôi cuộn, tính `μ`, `σ`, `Cpk`, định lượng chính xác số kg nhựa bọc dư `Over-thickness` và xuất báo cáo trong 1.5 giây!\n"
            "\n• Ví dụ 2 (Tối ưu lịch cắt rulo bằng thư viện PuLP): Nhập danh sách 25 đơn hàng đoạn lẻ vào script Python tối ưu hóa tổ hợp cắt giúp giảm mẩu thừa đồng/nhựa tiết kiệm hàng trăm triệu đồng mỗi năm."
        ),
        "common_mistakes": (
            "1. Viết script Python quá phức tạp chỉ mình tác giả chạy được (phụ thuộc môi trường code) mà không đóng gói thành file `.exe` đơn giản hoặc xuất kết quả ra file Excel/Power BI cho Quản đốc/Kế toán dễ sử dụng hàng ngày."
        )
    },
    "OEE": {
        "lesson_id": "L2.1",
        "definition_extra": (
            "\n• Bản chất dễ hiểu nhất: OEE trả lời câu hỏi 'Trong tổng thời gian ta LÊN KẾ HOẠCH cho máy chạy, có bao nhiêu % thời gian máy thực sự tạo ra sản phẩm ĐẠT CHUẨN ở đúng tốc độ tối đa thiết kế?'\n"
            "• 3 trụ cột tách bạch 3 loại tổn thất: Availability (A — Máy có chạy không hay đang đứng im hỏng/đổi mã?), Performance (P — Khi chạy máy có đạt đúng tốc độ chuẩn không hay bị chậm/dừng vặt?), Quality (Q — Sản phẩm chạy ra có đạt chuẩn ngay không hay bị phế cắt bỏ?).\n"
            "• Phân biệt sống còn: OEE dây chuyền rời rạc (cơ khí/lắp ráp) tính theo 'chiếc / giây'; còn OEE dây chuyền liên tục ngành Dây Cáp Điện CADIVI tính theo 'mét / phút' (Line Speed)!"
        ),
        "cadivi_application_extra": (
            "\n• Trọng tâm đo lường số 1 trong JD OE CADIVI: Áp dụng đo OEE riêng cho từng nhóm thiết bị chủ lực (Kéo thô RBD, Kéo tinh Multi-wire, Bện Buncher/Rigid, Đùn bọc PVC/XLPE, Giáp băng thép DSTA). Luôn đặt OEE cạnh OLE và kế hoạch giao hàng (OTIF) để tránh bẫy chạy mã dễ lấy OEE cao nhưng khách hàng không cần!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Bạn dự định chạy xe 4 tiếng (Planned) ở tốc độ chuẩn 60 km/h (lý thuyết đi 240 km). Thực tế dừng nghỉ sửa xe mất 1 tiếng (chỉ chạy 3 tiếng → A = 75%); lúc chạy kẹt xe nên chỉ đi 45 km/h (3h đi được 135 km so với 180 km → P = 75%); trong 135 km có 15 km đi lạc phải quay lại (chỉ 120 km đúng đường → Q = 88.9%). Hiệu quả thực OEE = 75% × 75% × 88.9% = 50% (chỉ đi được 120/240 km lý thuyết)!\n"
            "\n• Ví dụ 2 (Tính OEE máy đùn dây VC 2.5 tại CADIVI): Ca 480p − 30p ăn ca = 450p kế hoạch; dừng đổi màu & sự cố 90p → chạy 360p (A = 80.0%). Tốc độ chuẩn 350 m/phút; thực chạy 108,000m (P = 108,000 / [360×350] = 85.71%). Phế cắt bỏ 5,400m → đạt 102,600m (Q = 95.0%). OEE = 80% × 85.71% × 95% = 65.14%.\n"
            "\n• Ví dụ 3 (Cạm bẫy OEE cao nhưng công ty vẫn lỗ): Máy đùn đạt OEE 89% nhờ chạy liên tục 1 mã dây VC trắng suốt 5 ngày không đổi màu → Kho chất đống hàng chưa bán được trong khi đơn hàng cáp CXV khách cần gấp lại trễ hạn!"
        ),
        "common_mistakes": (
            "1. Loại trừ thời gian đổi mã (Setup/SMED) ra khỏi Downtime làm Availability đẹp giả tạo — theo chuẩn quốc tế, đổi mã BẮT BUỘC tính là tổn thất Availability để thúc đẩy làm SMED!\n"
            "2. Hạ thấp tốc độ chuẩn (Ideal Speed) xuống theo thói quen chạy chậm của công nhân để làm Performance đạt ảo 98–100%.\n"
            "3. Tính OEE tháng bằng trung bình cộng các ca thay vì chia tổng thực tế cho tổng kế hoạch."
        )
    },
    "TEEP": {
        "lesson_id": "L2.1",
        "definition_extra": (
            "\n• Bản chất phân biệt OEE vs TEEP: OEE chỉ đánh giá hiệu quả TRONG thời gian nhà máy mở ca chạy (vd: 1 ca 8 tiếng/ngày = 40 giờ/tuần), còn TEEP nhìn trên TOÀN BỘ 100% thời gian lịch 24 giờ × 7 ngày = 168 giờ/tuần (8,760 giờ/năm) vì máy móc vẫn nằm chiếm mặt bằng và tính khấu hao cả khi tắt điện ban đêm hay Chủ nhật!\n"
            "• Vai trò quyết định của TEEP: Là công cụ tối thượng để Ban Giám đốc đánh giá 'Nhà máy còn dư công suất tiềm ẩn bao nhiêu?' trước khi ký duyệt hàng tỷ đồng mua máy mới (CAPEX)."
        ),
        "cadivi_application_extra": (
            "\n• Ứng dụng tại CADIVI Miền Trung: Khi phân xưởng đề xuất mua thêm dây chuyền đùn hoặc máy kéo mới vì 'OEE đã đạt 80%, không còn chạy nổi nữa', OE lập tức tính TEEP để kiểm tra tỷ lệ huy động ca (Loading Factor) — có thể chỉ cần tăng từ 2 ca lên 3 ca 4 kíp cục bộ là tăng +50% sản lượng mà tiết kiệm hàng tỷ đồng đầu tư!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Bạn mua chiếc xe tải giao hàng nhưng chỉ chạy 6 tiếng/ngày, 5 ngày/tuần (30/168 giờ = 17.9% thời gian lịch). Dù lúc chạy bạn lái rất hiệu quả (OEE = 85%), thực chất chiếc xe chỉ tạo giá trị TEEP = 85% × 17.9% = 15.2% thời gian sở hữu!\n"
            "\n• Ví dụ 2 (Bài toán CAPEX tại CADIVI): Máy bện lồng cứng Rigid Strander đang chạy 2 ca × 26 ngày = 390 giờ kế hoạch / 720 giờ lịch tháng (Loading = 54.2%), OEE = 74% → TEEP = 40.1%. Thay vì chi 4 tỷ mua máy bện thứ hai, nâng OEE lên 82% và mở thêm ca 3 (3 ca 4 kíp) đẩy TEEP lên 68%, tăng gần +70% sản lượng với chi phí đầu tư gần bằng 0!"
        ),
        "common_mistakes": (
            "1. Dùng TEEP để đánh giá KPI thưởng phạt của Tổ trưởng ca — Tổ trưởng không quyết định được việc công ty có mở ca 3 hay có đơn hàng không! Tổ trưởng chịu trách nhiệm về OEE, còn Giám đốc & Kế hoạch chịu trách nhiệm về TEEP/Loading."
        )
    },
    "OLE": {
        "lesson_id": "L2.2",
        "definition_extra": (
            "\n• Bản chất sống còn: OEE đo xem MÁY có làm việc hiệu quả không, còn OLE đo xem CON NGƯỜI có đang tạo ra giá trị tối ưu không! Một xưởng có OEE máy đạt 85% nhưng phải bố trí tới 3 công nhân đứng phục vụ 1 máy (trong khi chuẩn chỉ cần 1 người đứng 2 máy) thì OLE cực thấp và chi phí nhân công đội lên gấp 6 lần!\n"
            "• 3 trụ cột OLE chuẩn: (1) Availability = Thời gian làm việc thực tế / Thời gian chấm công (mất do chờ vật tư, chờ lệnh, họp kéo dài); (2) Performance/Utilization = (Sản lượng × Thời gian chuẩn SAM) / Thời gian làm việc thực tế (mất do thao tác thừa Motion, chuyền mất cân bằng); (3) Quality = Sản lượng đạt chuẩn / Tổng sản lượng (mất do thao tác lỗi phải làm lại)."
        ),
        "cadivi_application_extra": (
            "\n• Trọng tâm đo lường tại CADIVI Miền Trung (ghi rõ trong JD): Đặc biệt hiệu quả ở các khu vực thâm dụng lao động hoặc đứng nhiều máy như: Tổ Đóng cuộn khoanh 100m (cuộn, dán tem, màng co, đóng gói), Tổ vận hành đa máy Kéo tinh / Bện Buncher / Bện lưới Braiding, và Tổ hoàn thiện đóng rulo gỗ."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Tiệm rửa xe có 4 nhân viên cùng đứng loay hoay rửa 1 chiếc ô tô mất 30 phút (tổng 120 phút công, nhiều lúc 2 người đứng nhìn chờ vòi xịt) thay vì phân công rõ từng bước để 2 người rửa xong trong 20 phút (40 phút công — OLE tăng gấp 3 lần mà nhân viên lại đỡ va chạm nhau!).\n"
            "\n• Ví dụ 2 (Tính OLE 1 ca tổ Đóng cuộn 10 người tại CADIVI): 10 người × 450p = 4,500 phút công kế hoạch; chờ rulo dây & chờ tem mất 290 phút công → Thực làm 4,210p (A = 93.56%). Chuẩn SAM = 2.0 phút/cuộn, làm được 1,850 cuộn → Thời gian tạo giá trị = 3,700p (P = 3,700/4,210 = 87.89%). Trong đó 55 cuộn dán sai tem/rách màng phải làm lại → Đạt 1,795 cuộn (Q = 97.03%). OLE = 93.56% × 87.89% × 97.03% = 79.79% → Thất thoát 910 phút công/ca (~47 triệu tiền lương/tháng)!"
        ),
        "common_mistakes": (
            "1. Hiểu sai rằng nâng OLE là 'ép công nhân chạy bán sống bán chết' — hoàn toàn sai! Nâng OLE chuẩn Lean là xóa thời gian chờ vật tư, sắp xếp lại dụng cụ trong vùng vàng Ergonomics, cân bằng chuyền Yamazumi và chuẩn hóa thao tác để công nhân làm NHẸ HƠN nhưng tạo ra nhiều sản lượng hơn!"
        )
    },
    "Time Study": {
        "lesson_id": "L2.2",
        "definition_extra": (
            "\n• Quy trình bấm giờ chuẩn công nghiệp 6 bước: (1) Chia nhỏ công việc thành các nguyên công rõ điểm đầu–cuối (5–30 giây/bước), (2) Quay video & bấm giờ tối thiểu 10–30 chu kỳ (loại bỏ ngoại lai bất thường), (3) Tính Thời gian quan sát trung bình (Observed Time), (4) Đánh giá tốc độ tay nghề (Performance Rating — chuẩn 100%; người làm nhanh hơn chuẩn 110%, chậm hơn 90%) → Normal Time = Observed × Rating, (5) Cộng hệ số phụ cấp (Allowances thường 12–15%: nhu cầu cá nhân 5% + mệt mỏi cơ bản 4% + đứng/bê nặng/nóng ồn 3–6%) → Ra Thời gian chuẩn SAM (Standard Allowed Minutes), (6) Phân loại 3 nhóm VA (tạo giá trị) – NNVA (cần thiết nhưng không tăng giá trị) – NVA (lãng phí cần cắt bỏ ngay)."
        ),
        "cadivi_application_extra": (
            "\n• Thế mạnh thực chiến từ CV của bạn (Canon INEX 60s → 30s tại Mabuchi): Áp dụng trực tiếp ngay tháng đầu tại CADIVI để đo bấm giờ đổi mã SMED trên máy đùn, lập định mức SAM tổ Đóng cuộn khoanh 100m, đo thời gian hàn đối đầu Butt Welder và đo thời gian lấy/thử mẫu phòng Lab QA/QC."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tính SAM chi tiết cho 1 cuộn dây VC 100m): Quan sát 20 chu kỳ đóng gói cuộn dây mất trung bình 52 giây, công nhân tay nghề khá (Rating = 105%) → Normal Time = 52 × 1.05 = 54.6 giây. Cộng phụ cấp cá nhân + đứng thao tác + nóng xưởng = 15% → SAM = 54.6 × 1.15 = 62.79 giây/cuộn (≈ 1.047 phút/cuộn → Định mức chuẩn 1 ca 450p = 430 cuộn/người!).\n"
            "\n• Ví dụ 2 (Liên hệ thực chiến Canon INEX): Bóc tách từng giây thao tác gá đặt và đo thủ công 60s/hạng mục, chuyển sang đồ gá 16 mẫu + tự động đo rút xuống 30s/hạng mục (-50% thời gian đo) — đúng bản chất tách NVA và chuẩn hóa thao tác của Time & Motion Study!"
        ),
        "common_mistakes": (
            "1. Đứng sau lưng công nhân bấm đồng hồ mà không giải thích trước mục đích → Công nhân lo sợ bị cắt lương sẽ cố tình làm chậm hoặc căng thẳng sai số liệu! Luôn trao đổi minh bạch với Tổ trưởng & công nhân rằng đo để tìm chỗ vất vả, loại bỏ thao tác chờ đợi giúp họ làm nhàn hơn.\n"
            "2. Quên cộng Allowances (phụ cấp mệt mỏi/vệ sinh) khiến định mức không khả thi trong ca 8 tiếng thực tế."
        )
    },
    "Standard Work": {
        "lesson_id": "L3.1",
        "definition_extra": (
            "\n• Phân biệt sắc bén giữa SOP và Standard Work: SOP (Standard Operating Procedure) mô tả CÁCH LÀM từng bước về mặt kỹ thuật và an toàn; còn Standard Work là bộ chuẩn năng suất động của Toyota GẮN CHẶT với nhịp thị trường (Takt Time) gồm đủ 3 chân kiềng: (1) Takt Time, (2) Trình tự thao tác chuẩn theo giây (Work Sequence), (3) Tồn kho WIP chuẩn tối thiểu (Standard WIP) — khi đơn hàng tăng/giảm làm Takt Time thay đổi, Standard Work phải được cập nhật lại ngay!"
        ),
        "cadivi_application_extra": (
            "\n• Ứng dụng tại CADIVI Miền Trung: Triển khai ở mọi điểm có sự chênh lệch lớn giữa 3 ca làm việc — tổ Đóng cuộn khoanh 100m, quy trình đổi khuôn/màu SMED 2 người song song trên máy đùn, quy trình thay bộ 24 suốt bện lưới Braiding và quy trình kiểm mẫu đầu ca phòng Lab."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Đội thay lốp xe đua F1 thực hiện đúng Standard Work từng 0.5 giây — mỗi người đứng đúng vị trí, làm đúng 1 trình tự cố định nên thay 4 bánh xe chỉ mất 2.2 giây với xác suất lỗi gần 0.\n"
            "\n• Ví dụ 2 (Tại CADIVI): Khảo sát 3 ca tổ Đóng cuộn dây VC 2.5 thấy Ca 1 đóng 440 cuộn, Ca 2 đóng 390 cuộn, Ca 3 chỉ 320 cuộn vì mỗi ca tự xếp bàn và trình tự dán tem/co màng khác nhau → Quan sát quay video lấy cách tối ưu nhất lập Standard Work trực quan + đào tạo TWI giúp cả 3 ca đều đạt ổn định 430–450 cuộn/ca!"
        ),
        "common_mistakes": (
            "1. Viết Standard Work ngồi trong phòng lạnh mà không xuống hiện trường làm thử cùng công nhân — kết quả là tài liệu đẹp nhưng bất khả thi tại máy.\n"
            "2. Coi Standard Work là bất biến — chuẩn mực chỉ là điểm tựa để lần Kaizen tiếp theo đẩy lên chuẩn mới cao hơn."
        )
    },
    "Man-Machine Chart": {
        "lesson_id": "L2.3",
        "definition_extra": (
            "\n• Bản chất công cụ IE kinh điển: Biểu đồ gồm 2 cột song song theo trục thời gian (giây/phút): cột Người (đang thao tác tay vs đang đứng chờ máy) và các cột Máy 1, Máy 2, Máy 3... (đang dừng chờ người gá đặt vs đang tự chạy tự động). Nhìn vào các khoảng trắng (thời gian nhàn rỗi) trên biểu đồ, kỹ sư OE tính ngay được số máy tối ưu 1 công nhân có thể đứng vận hành đồng thời mà không làm máy chờ lâu hay công nhân kiệt sức!"
        ),
        "cadivi_application_extra": (
            "\n• Cực kỳ đắt giá tại nhà máy cáp điện CADIVI: Hầu hết máy Kéo tinh Multi-wire, máy Bện Buncher, máy Quấn băng Mica FR và máy Bện lưới Braiding đều có chu kỳ máy tự chạy rất dài (30–90 phút/rulo) trong khi thao tác người thay rulo chỉ mất 5–8 phút → Mô hình 1 người đứng đa máy (Multi-Machine Handling) là mỏ vàng nâng OLE!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Ở nhà bạn bật máy giặt (45 phút), trong lúc máy tự chạy bạn đi nấu cơm (20 phút) và quét nhà (15 phút) — thay vì ngồi nhìn lồng máy giặt quay 45 phút rồi mới đi nấu cơm!\n"
            "\n• Ví dụ 2 (Tính toán 1 người đứng nhiều máy Bện Buncher tại CADIVI): Mỗi rulo máy bện tự chạy M = 42 phút, thao tác công nhân thay rulo/hàn nối/ghi tem L = 8 phút, đi bộ giữa 2 máy W = 1 phút. Số máy lý thuyết tối ưu N = (L + M) / (L + W) = (8 + 42) / (8 + 1) = 5.55 → Bố trí 1 công nhân đứng 3–4 máy (chừa dự phòng xử lý đứt sợi đột xuất) giúp tăng OLE gấp đôi, giảm 50% chi phí nhân công trực tiếp trên mỗi km ruột bện!\n"
            "\n• Ví dụ 3 (Kết hợp lệch pha khởi động): Nếu cả 4 máy bện cùng hết rulo đúng 1 thời điểm (8:00), 3 máy sẽ phải nằm chết chờ người thay (Interference Loss) → Xếp lịch lệch pha khởi động cách nhau 12 phút để công nhân thay tuần tự từng máy, OEE cả 4 máy giữ vững > 88%!"
        ),
        "common_mistakes": (
            "1. Xếp quá sát lý thuyết (vd: tính ra 5.5 máy liền giao luôn 6 máy) mà quên tính xác suất 2 máy cùng đứt sợi 1 lúc (Machine Interference) làm OEE cả cụm máy rớt thảm hại!"
        )
    },
    "Takt Time": {
        "lesson_id": "L2.3",
        "definition_extra": (
            "\n• Bản chất dễ hiểu: Takt trong tiếng Đức nghĩa là 'nhịp gõ của nhạc trưởng'. Takt Time KHÔNG phải là tốc độ máy chạy, mà là NHỊP ĐÒI HỎI CỦA KHÁCH HÀNG — tức cứ mỗi bao nhiêu giây/phút dây chuyền phải xuất ra 1 sản phẩm (hoặc 1 cuộn/1 km cáp) để giao kịp đơn hàng mà không thừa không thiếu!\n"
            "• So sánh 3 nhịp hay nhầm nhất: Takt Time = Nhịp khách hàng yêu cầu; Cycle Time = Thời gian thực tế trạm đang làm; Lead Time = Tổng thời gian từ lúc thả đồng rod đầu vào đến khi cáp thành phẩm lên xe giao hàng."
        ),
        "cadivi_application_extra": (
            "\n• Ứng dụng tại CADIVI Miền Trung: Làm 'vạch đỏ chuẩn' trên biểu đồ Yamazumi ở tổ Đóng cuộn khoanh 100m, trạm đóng rulo xuất hàng và tính nhịp cung ứng của xưởng Đùn/Bện theo đơn hàng tháng của kinh doanh."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Quán bánh mì bán 240 ổ trong 4 tiếng sáng (14,400 giây) → Takt Time = 14,400 / 240 = 60 giây/ổ. Nghĩa là cứ mỗi 60 giây phải ra 1 ổ; nếu kẹp mất 80 giây thì khách xếp hàng dài bỏ đi, nếu kẹp 20 giây làm sẵn để đó thì bánh nguội ỉu (lãng phí Overproduction)!\n"
            "\n• Ví dụ 2 (Tính toán tổ Đóng cuộn dây VC 100m tại CADIVI): Nhu cầu giao hàng 1 ca là 900 cuộn, thời gian làm việc ròng 1 ca = 450 phút = 27,000 giây → Takt Time = 27,000 / 900 = 30 giây/cuộn. Để an toàn trước dừng vặt, OE đặt Target Cycle Time = 90% × Takt = 27 giây/cuộn làm mục tiêu cân bằng các trạm!"
        ),
        "common_mistakes": (
            "1. Quên trừ thời gian nghỉ ăn ca, họp đầu ca 5p và vệ sinh 5S cuối ca 10p khỏi Thời gian khả dụng khi tính Takt Time → Ra nhịp ảo quá thư thả, cuối ca không kịp hàng!\n"
            "2. Nhầm Takt Time với Cycle Time: Bạn KHÔNG thể 'cải tiến làm giảm Takt Time' vì Takt Time do nhu cầu thị trường quyết định — bạn chỉ cải tiến Cycle Time để bám sát hoặc nhỏ hơn Takt Time!"
        )
    },
    "Cycle Time": {
        "lesson_id": "L2.3",
        "definition_extra": (
            "\n• Phân biệt 3 dạng Cycle Time cần rõ ràng trong báo cáo OE:\n"
            "  1. Ideal Cycle Time (Chu kỳ thiết kế lý thuyết nhanh nhất của máy — dùng để tính Performance OEE).\n"
            "  2. Actual Cycle Time (Thời gian thực tế đo được bằng đồng hồ bấm giờ từ sản phẩm đạt A đến sản phẩm đạt B ngay sau nó).\n"
            "  3. Bottleneck Cycle Time (Cycle Time của trạm chậm nhất trên dây chuyền — chính là tốc độ xuất hàng thực tế của toàn bộ chuyền!)."
        ),
        "cadivi_application_extra": (
            "\n• Đo trực tiếp trên từng trạm tổ Đóng cuộn khoanh 100m, trạm quấn màng/dán tem, trạm kiểm tra điện trở & Spark phòng Lab, và quy đổi từ tốc độ tuyến tính máy đùn/kéo (`Cycle Time 1 cuộn 100m = 100 / Tốc độ m/phút`) tại CADIVI Miền Trung."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Đọc nhanh dây chuyền 4 trạm đóng cuộn): Trạm 1 Cuộn dây = 24s, Trạm 2 Cắt & Buộc = 35s, Trạm 3 Bọc màng co = 22s, Trạm 4 Dán tem & Xếp pallet = 19s → Bottleneck Cycle Time = 35 giây/cuộn (dù Trạm 4 siêu nhanh 19s thì cả chuyền cũng chỉ xuất được 1 cuộn mỗi 35 giây!).\n"
            "\n• Ví dụ 2 (Quy đổi trên máy đùn dây dân dụng CADIVI): Máy đùn chạy dây VC 2.5 ở tốc độ thực 300 m/phút → Cycle Time cho mỗi khoanh 100m = 100 / 300 = 0.333 phút = 20 giây/khoanh → Tổ đóng gói phía sau bắt buộc có Cycle Time ≤ 20 giây/khoanh nếu không muốn dây ùn ứ tắc nghẽn!"
        ),
        "common_mistakes": (
            "1. Chỉ bấm giờ 1–2 lần rồi chốt Cycle Time — phải đo tối thiểu 10–20 chu kỳ ở các thời điểm đầu ca, giữa ca, cuối ca để nắm được cả độ biến thiên thực tế."
        )
    },
    "Lead Time": {
        "lesson_id": "L3.2",
        "definition_extra": (
            "\n• Bản chất dễ sốc khi vẽ VSM: Trong hầu hết nhà máy truyền thống, tổng thời gian gia công thực sự tạo giá trị (Process Time — đồng thực sự đang được kéo, bện, đùn) chỉ chiếm 5% – 10% tổng Lead Time! Còn tới 90% – 95% Lead Time là thời gian bán thành phẩm nằm im trên sàn chờ xếp hàng (Queue/WIP), chờ đổi mã, chờ bể xông XLPE hoặc chờ phòng Lab xuất giấy!\n"
            "• Định luật Little (Little's Law — nền tảng của Factory Physics): `Lead Time = WIP / Throughput` → Muốn rút ngắn Lead Time giao hàng một nửa mà không phải mua máy nhanh gấp đôi, cách mạnh nhất là cắt giảm tồn kho bán thành phẩm WIP nằm chờ giữa các xưởng!"
        ),
        "cadivi_application_extra": (
            "\n• Lợi thế cạnh tranh đơn hàng dự án của CADIVI Miền Trung: Khách hàng điện lực và nhà thầu xây dựng thường chọn nhà cung cấp giao hàng nhanh nhất. Rút Lead Time cáp lực CXV từ 12 ngày xuống 4–5 ngày giúp CADIVI thắng thầu lớn mà không cần hạ giá bán!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Bạn đi khám bệnh ở bệnh viện mất tổng cộng 3 tiếng (Lead Time = 180 phút), trong đó bác sĩ thực sự khám và kê đơn chỉ mất 10 phút (Value-Added Time = 5.5%) — 170 phút còn lại là xếp hàng chờ lấy số, chờ gọi tên, chờ kết quả!\n"
            "\n• Ví dụ 2 (Tại CADIVI): Đơn hàng cáp CXV 3×50 có tổng thời gian máy chạy thực sự qua 6 công đoạn chỉ 18 giờ, nhưng tổng Lead Time hiện trạng lên tới 11 ngày (264 giờ, PCE = 6.8%) do rulo nằm chờ 2 ngày trước máy đùn, 3 ngày chờ gom đủ mẻ bể xông XLPE và 1.5 ngày chờ Lab thử cao áp → Áp dụng SMED + chia lô nhỏ + lịch gom mẫu Lab cố định kéo Lead Time xuống 4.2 ngày!"
        ),
        "common_mistakes": (
            "1. Cố ép máy chạy nhanh thêm 10% (giảm được 1.8 giờ Process Time) trong khi bỏ mặc 9 ngày rulo nằm chờ trên sàn — tốn công mà Lead Time giao hàng gần như chẳng đổi!"
        )
    },
    "Yamazumi": {
        "lesson_id": "L2.3",
        "definition_extra": (
            "\n• Bản chất trực quan (tiếng Nhật: 'chất thành đống'): Mỗi trạm/công nhân là 1 cột xếp chồng các khối thao tác nhỏ bên trong, được tô bằng 3 màu chuẩn Lean: Màu Xanh lá = VA (tạo giá trị thật), Màu Vàng = NNVA (cần thiết phụ trợ như cầm dụng cụ), Màu Đỏ = NVA (lãng phí đi lại/tìm đồ/chờ đợi). Vẽ 1 đường ngang đỏ là Takt Time cắt ngang tất cả các cột → Nhìn 2 giây thấy ngay trạm nào đang quá tải (vượt đường Takt) và trạm nào đang rảnh (thấp hơn Takt) để cắt bỏ phần Đỏ rồi san sẻ các khối thao tác sang cho đều!"
        ),
        "cadivi_application_extra": (
            "\n• Công cụ chủ lực cho các chuyền nhiều thao tác thủ công tại CADIVI Miền Trung: Tổ Đóng cuộn khoanh 100m dây dân dụng, tổ lắp phụ kiện/đóng gỗ rulo cáp xuất xưởng, tổ chuẩn bị đầu mẫu thử nghiệm Lab và phân công 2 người đổi mã SMED."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Cân bằng chuyền 5 trạm đóng cuộn tại CADIVI): Takt Time = 30s. Hiện trạng: Trạm 1 = 29s, Trạm 2 = 28s, Trạm 3 = 14s, Trạm 4 = 25s, Trạm 5 = 11s (Tổng 107s, LBE = 73.8%, tốn 5 người). Sau khi xóa 11s thao tác thừa màu Đỏ (còn 96s) và san lại các khối thao tác đều vào 4 cột (25s – 24s – 24s – 23s) → Giảm từ 5 xuống 4 người (tiết kiệm 20% nhân công) mà năng suất tăng lên từ 29s xuống 25s/cuộn (+16%), LBE vọt lên 96%!"
        ),
        "common_mistakes": (
            "1. Chỉ cộng dồn 1 cục tổng thời gian mỗi trạm mà không chia nhỏ theo từng nguyên công VA/NNVA/NVA → Không biết tách khối nhỏ nào để chuyển sang trạm bên cạnh!\n"
            "2. Quên tính ràng buộc thứ tự công nghệ (Precedence — không thể dán tem lên màng co trước khi bọc màng co!)."
        )
    },
    "LBE": {
        "lesson_id": "L2.3",
        "definition_extra": (
            "\n• Bản chất đo độ đồng đều của dây chuyền: LBE (Line Balancing Efficiency) đo xem trong tổng thời gian trả lương cho tất cả các trạm trên chuyền, có bao nhiêu % là thời gian làm việc hữu ích và bao nhiêu % bị mất đi vì các trạm nhanh phải ngồi chờ trạm chậm nhất (Balance Delay = 100% − LBE).\n"
            "• Thang chuẩn công nghiệp: LBE ≥ 85% là tốt (World-Class ≥ 90%); LBE 70–84% cần san tải lại bằng Yamazumi; LBE < 70% là chuyền mất cân bằng nghiêm trọng đang lãng phí nặng nhân công!"
        ),
        "cadivi_application_extra": (
            "\n• Dùng đánh giá trước và sau cải tiến tổ Đóng cuộn/Đóng gói thành phẩm tại CADIVI, cũng như cân đối năng lực giữa các công đoạn liên hoàn (ví dụ đồng bộ tốc độ giữa máy đùn vỏ và máy thu cuộn/in phun/đóng khoanh tự động)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Chuyền rửa bát 3 người: người 1 cọ 60s, người 2 tráng 20s, người 3 lau 20s. Tổng làm thực = 100s, nhưng người 2 và 3 mỗi người ngồi chơi 40s chờ người 1! LBE = 100 / (3 × 60) = 55.6% (lãng phí mất 44.4% tiền công!).\n"
            "\n• Ví dụ 2 (Số liệu tại CADIVI): Chuyền đóng gói 5 công nhân có tổng thời gian thao tác 118 giây, trạm nghẽn dài nhất 34 giây → LBE = 118 / (5 × 34) = 69.4%. Sau khi tái bố trí Yamazumi về 4 công nhân (trạm dài nhất 30 giây, tổng 112 giây) → LBE = 112 / (4 × 30) = 93.3% (nhảy vọt +23.9% hiệu suất cân bằng)!"
        ),
        "common_mistakes": (
            "1. Đánh giá LBE chỉ bằng mắt mà quên kết hợp Smoothness Index (SI) — có những chuyền LBE 82% nhưng 1 trạm vất vả 100% còn 1 trạm chỉ 50% gây bất mãn nội bộ công nhân."
        )
    },
    "Smoothness Index": {
        "lesson_id": "L2.3",
        "definition_extra": (
            "\n• Ý nghĩa cặp đôi với LBE: Trong khi LBE đo hiệu suất trung bình theo %, Smoothness Index (SI) đo độ gập ghềnh / chênh lệch tải giữa các công nhân tính bằng đơn vị giây. Nếu mọi trạm có thời gian làm việc bằng nhau tuyệt đối thì `SI = 0` (hoàn hảo 100% công bằng, không ai quá tải, không ai ngồi chơi!). SI càng lớn chứng tỏ độ chênh giữa người bận nhất và người rảnh nhất càng cao."
        ),
        "cadivi_application_extra": (
            "\n• Rất hữu ích khi thuyết phục công nhân và tổ trưởng CADIVI chấp nhận phương án cân bằng chuyền mới: chứng minh bằng con số SI giảm mạnh rằng sự phân công mới công bằng hơn, giảm áp lực cho công nhân đứng trạm nghẽn!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tính trực tiếp): 4 trạm có thời gian [30s, 29s, 28s, 27s] (CT_max = 30s) → SI = √[(0)² + (1)² + (2)² + (3)²] = √14 = 3.74 giây (cực mượt!). Ngược lại chuyền [30s, 30s, 29s, 12s] có SI = √[0 + 0 + 1 + 324] = 18.03 giây (chênh lệch quá lớn ở trạm 4!).\n"
            "\n• Ví dụ 2 (Tại CADIVI): Cân bằng lại tổ đóng cuộn 5 trạm từ [34s, 22s, 18s, 30s, 14s] (SI = 28.4s) sang 4 trạm [29s, 28s, 28s, 27s] (SI = 2.45s) — giảm hơn 11 lần độ lệch tải, giúp không khí làm việc trong tổ hòa thuận và năng suất ổn định suốt ca!"
        ),
        "common_mistakes": (
            "1. So sánh trực tiếp SI giữa hai phương án có số trạm hoàn toàn khác nhau mà quên nhìn đồng thời LBE và tổng nhân sự tiết kiệm được."
        )
    },
    "KPI": {
        "lesson_id": "L3.4",
        "definition_extra": (
            "\n• Phân biệt sống còn giữa KPI Dẫn Báo (Leading Indicator) và KPI Kết Quả (Lagging Indicator): OEE, Giá thành/km, Phế phẩm tháng là Lagging (chỉ biết sau khi chuyện đã rồi); còn PM Compliance, Tỷ lệ hoàn thành kiểm tra LPA, Số lượng cải tiến Kaizen, Thời gian đổi mã từng lượt là Leading (tác động trực tiếp để kéo kết quả tương lai đi lên!).\n"
            "• Khung bộ chỉ số SQDCM chuẩn nhà máy: S (Safety — An toàn/Tai nạn/Near-miss), Q (Quality — RTY/Spark/Khiếu nại), D (Delivery — OTIF giao đúng hạn/OEE), C (Cost — BOM Variance/OLE/kWh trên tấn), M (Morale — Đi làm đủ/Đề xuất Kaizen/Đa kỹ năng)."
        ),
        "cadivi_application_extra": (
            "\n• Triển khai hệ thống giao ban phân tầng Tier 1 (Tổ trưởng 5p đầu ca) → Tier 2 (Quản đốc/OE 15p lúc 09:00) → Tier 3 (Ban Giám đốc CADIVI Miền Trung hàng tuần) xoay quanh đúng 5 chữ SQDCM để mọi phòng ban nhìn chung một bức tranh số liệu."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Cân nặng cuối tháng là Lagging KPI (đã xảy ra); số bước đi bộ và lượng calo ăn mỗi ngày là Leading KPI (giúp bạn chủ động thay đổi kết quả!).\n"
            "\n• Ví dụ 2 (Tại CADIVI): Đưa Leading KPI 'Tỷ lệ tuân thủ chuỗi màu Color Sequencing ≥ 90%' và 'PM Compliance ≥ 90%' lên bảng Tier 2 giúp kéo Lagging KPI 'OEE xưởng Đùn' tăng bền vững từ 65% lên 77% sau 1 quý!"
        ),
        "common_mistakes": (
            "1. Đặt quá nhiều KPI (25–30 chỉ số) khiến quản lý bị ngợp — mỗi cấp chỉ nên tập trung 5–7 KPI cốt lõi (SQDCM).\n"
            "2. Đặt KPI xung đột giữa các phòng ban: ví dụ thưởng Sản xuất theo tổng tấn sản lượng thô mà không gắn với BOM Variance & Kế hoạch giao hàng → Xưởng sẽ chạy toàn mã cáp to dễ chạy, bỏ bê mã dây nhỏ khách đang chờ!"
        )
    },
    "Six Big Losses": {
        "lesson_id": "L2.1",
        "definition_extra": (
            "\n• Bản chất cầu nối giữa con số OEE và hành động hiện trường: Biết OEE = 65% chưa cho bạn biết phải sửa cái gì — nhưng khi phân rã 35% tổn thất kia thành 6 Tổn thất lớn của TPM (2 tổn thất Availability: Hỏng máy đột xuất Breakdown & Đổi mã Setup; 2 tổn thất Performance: Dừng vặt Minor Stops < 5p & Chạy chậm Reduced Speed; 2 tổn thất Quality: Phế khởi động Startup Rejects & Phế trong khi chạy Production Defects), bạn sẽ biết ngay phải dùng vũ khí nào (Breakdown → TPM/PdM; Setup → SMED; Chạy chậm → Công nghệ/Chiller; Phế → SPC/Poka-Yoke)!"
        ),
        "cadivi_application_extra": (
            "\n• Dịch thẳng 6 Tổn thất lớn sang ngôn ngữ nhà máy cáp CADIVI: (1) Breakdown = Đứt dây curoa, hỏng biến tần, cháy điện trở nhiệt; (2) Setup = Đổi màu nhựa, đổi tiết diện Tip/Die, thay rulo; (3) Minor Stops = Đứt sợi đồng kéo, tắc phễu nhựa, kẹt thanh dẫn; (4) Reduced Speed = Ghìm tốc độ đùn vì nước làm mát nóng hoặc sợ lỗi Spark; (5) Startup Rejects = Đoạn dây đồng bọc nhựa xả đầu ca khi chỉnh tâm & đổi màu; (6) Production Defects = Lỗi thủng Spark, lệch tâm, mờ chữ in phun, đứt băng Mica."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Ưu tiên nguồn lực tại CADIVI): Phân loại 90 phút tổn thất ca máy đùn vào 6 nhóm thấy: Setup đổi màu = 35p (39%), Thay rulo = 24p (27%), Chạy chậm mất tương đương 45p quy đổi (20%) → Đánh ngay vào Setup bằng SMED & Color Sequencing là gỡ được hơn 1/3 tổng tổn thất tức thì!\n"
            "\n• Ví dụ 2 (Tách bạch Phế khởi động vs Phế khi chạy): Nhiều xưởng gộp chung 1 cột 'Phế phẩm = 3.2%'. Khi tách ra thấy 2.4% là Phế khởi động mỗi lần đổi mã (giải bằng SMED/Recipe PLC) còn chỉ 0.8% là lỗi khi chạy ổn định (giải bằng SPC) → Nhờ tách đúng 6 Big Losses mà chọn trúng giải pháp ngay!"
        ),
        "common_mistakes": (
            "1. Ghi chung chung 1 dòng 'Dừng máy kỹ thuật = 60 phút' mà không phân loại theo 6 Big Losses → Không bao giờ vẽ được Pareto tìm gốc rễ!"
        )
    },
    "Downtime": {
        "lesson_id": "L2.1",
        "definition_extra": (
            "\n• Phân loại chuẩn 3 tầng Downtime để không gây tranh cãi giữa các phòng ban:\n"
            "  1. Scheduled / Planned Shutdown (Không tính vào OEE, chỉ ảnh hưởng TEEP): Nghỉ lễ Tết, không có đơn hàng, nghỉ ăn ca nếu không có người thay phiên, đại tu bảo trì theo kế hoạch năm.\n"
            "  2. Unplanned Major Downtime (≥ 5 phút — tính vào Availability OEE): Hỏng cơ/điện đột xuất, dừng đổi mã/đổi màu, chờ vật tư/rulo, chờ Lab duyệt mẫu đầu ca.\n"
            "  3. Minor Stoppages / Micro-stops (< 5 phút — tính vào Performance OEE): Dừng gạt cặn Die Drool, chỉnh lệch dây, reset cảm biến báo giả — thường bị công nhân bỏ sót không ghi sổ tay!"
        ),
        "cadivi_application_extra": (
            "\n• Chuẩn hóa Bảng Mã Lý Do Dừng Máy (12–15 mã chuẩn gọn) dùng thống nhất giữa 4 phân xưởng Kéo – Bện – Đùn – Đóng gói tại CADIVI Miền Trung và gắn chủ sở hữu rõ ràng (Mã Sản xuất / Mã Bảo trì / Mã Kế hoạch / Mã Chất lượng / Mã Vật tư)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Chuyến bay bị trễ 45 phút — hãng hàng không phân rõ mã nguyên nhân: Thời tiết (bất khả kháng), Kỹ thuật máy bay (Bảo trì), Chờ hành khách/hành lý (Mặt đất) để xử lý đúng khâu.\n"
            "\n• Ví dụ 2 (Phát hiện 'Lỗ đen' Downtime tại CADIVI): So sánh nhật ký tay xưởng Kéo ghi tổng dừng 35 phút/ca với log tự động từ biến tần PLC ghi dừng 88 phút/ca → Phát hiện 53 phút bị biến mất là hàng chục lần dừng vặt 2–4 phút gỡ rối dây & thông vòi nhũ tương mà công nhân thấy lặt vặt nên không ghi!"
        ),
        "common_mistakes": (
            "1. Tạo mã 'Dừng máy khác' mà không bắt buộc ghi chú — chỉ sau 1 tháng, 40% thời gian dừng máy sẽ bị tống hết vào mục 'Khác'!\n"
            "2. Dùng nhật ký dừng máy để phạt trừ lương công nhân → Công nhân sẽ giấu lỗi hoặc ghi sai mã để đối phó, làm hỏng hoàn toàn dữ liệu OE."
        )
    },
    "Work Combination Table": {
        "lesson_id": "L2.3",
        "definition_extra": (
            "\n• Bộ 3 biểu mẫu chuẩn hóa Toyota (Standardized Work Forms): (1) Process Capacity Sheet (Bảng năng lực tối đa từng máy), (2) Standardized Work Combination Table — SWCT (phối hợp theo trục giây giữa thao tác tay nét liền, máy tự chạy nét đứt, đi bộ nét sóng và đường đỏ dọc Takt Time), (3) Standardized Work Chart (Sơ đồ vị trí máy, đường đi, điểm kiểm tra chất lượng & an toàn).\n"
            "• Giá trị đặc biệt của SWCT: Cho thấy trực quan ngay những giây 'máy đang tự chạy' để kỹ sư OE gài các thao tác phụ trợ (gấp thùng, dán tem, chuẩn bị rulo kế tiếp) vào đúng khoảng thời gian máy chạy tự động!"
        ),
        "cadivi_application_extra": (
            "\n• Rất sát cho trạm bán tự động tại CADIVI: Máy cuộn khoanh tự động 100m, máy cắt đoạn dây, tổ vận hành cụm 3 máy bện Buncher hoặc máy thử điện áp phòng Lab."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Barista bấm máy pha Espresso tự chảy trong 25 giây — trong đúng 25 giây nét đứt đó, họ lấy cốc, đánh sữa và chuẩn bị nắp thay vì đứng khoanh tay nhìn cà phê chảy!\n"
            "\n• Ví dụ 2 (Tại CADIVI): Lập bảng SWCT cho công nhân máy cuộn khoanh dây VC 100m (thao tác tay đặt đầu dây & lấy cuộn = 14s, máy tự cuộn = 18s, dán tem & bỏ bao = 10s; tổng 42s > Takt 30s). Đưa bước dán tem & lồng túi cho cuộn trước vào đúng 18s máy tự cuộn → Chu kỳ thực rút từ 42s xuống còn 24s (nhỏ hơn Takt 30s, tăng năng suất +75% không cần mua thêm máy cuộn!)."
        ),
        "common_mistakes": (
            "1. Quên đo và vẽ đường sóng 'Thời gian đi bộ' giữa các máy khiến tổng chu kỳ trên thực tế dài hơn trên giấy 15–20%."
        )
    },
    "Work Sampling": {
        "lesson_id": "L2.2",
        "definition_extra": (
            "\n• Nguyên lý toán học của L.H.C. Tippett: Dựa trên phân phối nhị thức — nếu bạn đi quan sát ngẫu nhiên một nhóm nhân sự đủ nhiều lượt (thường 400–1,000 lượt chụp nhanh), tỷ lệ phần trăm số lần bạn bắt gặp họ đang làm hoạt động X sẽ hội tụ rất sát về tỷ lệ % thời gian thực tế họ dành cho hoạt động X trong suốt ca làm việc!\n"
            "• Ưu thế vượt trội so với Time Study bấm giờ: (1) Một kỹ sư OE có thể khảo sát cùng lúc 10–15 công nhân hoặc cả đội xe nâng/bảo trì, (2) Không phải đứng kè kè bấm giờ gây khó chịu tâm lý, (3) Chi phí khảo sát chỉ bằng 1/5 so với bấm giờ liên tục!"
        ),
        "cadivi_application_extra": (
            "\n• Dùng cực kỳ hiệu quả tại CADIVI Miền Trung cho 3 đối tượng khó bấm giờ truyền thống: (1) Đội xe nâng & cầu trục vận chuyển rulo giữa 4 phân xưởng, (2) Đội kỹ thuật Cơ Điện bảo trì (đo chỉ số Wrench Time), (3) Nhóm công nhân đứng đa máy Kéo tinh / Bện Buncher / Bện lưới Braiding."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Muốn biết cả tuần cửa hàng có hay để khách chờ tính tiền không, bạn không cần ngồi quay camera 168 giờ — chỉ cần cài đồng hồ báo thức ngẫu nhiên 20 lần/ngày nhìn ra quầy đúng tích tắc đó rồi đánh dấu, sau 1 tháng sẽ có số liệu thống kê cực chuẩn!\n"
            "\n• Ví dụ 2 (Đo đội 4 xe nâng xưởng cáp CADIVI): Cần sai số ±3% ở độ tin cậy 95%, ước lượng thời gian chạy rỗng/chờ p = 0.30 → N = (1.96² × 0.30 × 0.70) / 0.03² = 897 lượt quan sát (~45 lượt đi tuyến/ngày trong 5 ngày). Kết quả thực tế: Chở hàng có ích 52%, Chạy không tải 22%, Chờ tìm rulo/kẹt lối 16%, Bảo dưỡng/nghỉ 10% → Tối ưu tuyến Milk Run và đánh mã vị trí kho rulo giải phóng ngay 25% năng lực xe nâng mà không tốn 700 triệu mua xe mới!"
        ),
        "common_mistakes": (
            "1. Đi quan sát theo giờ cố định tròn trĩnh (đúng 08:00, 09:00, 10:00) → Dễ trùng đúng nhịp nghỉ/giao ca hoặc công nhân đoán trước được giờ bạn tới làm sai lệch mẫu! Bắt buộc dùng bảng số ngẫu nhiên chọn mốc phút quan sát.\n"
            "2. Quan sát quá ít lượt (< 100 lượt) rồi vội kết luận sai số lên tới ±10%."
        )
    },
    "Loss Tree": {
        "lesson_id": "L5.4",
        "definition_extra": (
            "\n• Bản chất trực quan hóa toàn cảnh: Một nhà máy có thể có tới 50 báo cáo lẻ tẻ khiến không ai nhìn thấy rừng cây. Loss Tree (Cây tổn thất) / OEE Waterfall (Biểu đồ thác nước) gom toàn bộ 100% thời gian lịch (hoặc 100% tổng chi phí sản xuất) vào cột đầu tiên bên trái, rồi trừ dần từng nấc tổn thất lớn đến nhỏ cho đến khi còn lại phần Giá trị hữu ích ròng bên phải.\n"
            "• Nguyên tắc MECE (Không trùng lặp, không bỏ sót): Mọi phút dừng máy hay mọi đồng thất thoát chỉ nằm ở ĐÚNG 1 nhánh và có ĐÚNG 1 phòng ban chịu trách nhiệm cải tiến."
        ),
        "cadivi_application_extra": (
            "\n• Là trang đầu tiên (Executive Summary) trên báo cáo tháng OE gửi Ban Giám đốc CADIVI Miền Trung: kết hợp Thác nước Thời gian (từ 720 giờ lịch → TEEP) song song với Thác nước Tiền VNĐ (từ tổng chi phí NVL + chuyển đổi → từng nhánh tổn thất đồng, nhựa, điện, nhân công)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Biểu đồ thác nước chi tiêu lương tháng: Lương 18 triệu − Tiền nhà 3.5tr − Ăn uống 4tr − Đi lại 1.5tr − Mua sắm ngẫu hứng 3.5tr = Tiết kiệm 5.5tr → Nhìn phát thấy ngay nhánh 'Mua sắm ngẫu hứng' là nơi cần cắt đầu tiên!\n"
            "\n• Ví dụ 2 (OEE Waterfall Xưởng Đùn CADIVI): Thời gian kế hoạch 100% (450p/ca) − Đổi màu/tiết diện 12.2% − Hỏng sự cố/nghẹt lưới 6.7% − Thay rulo 5.3% − Giảm tốc độ & dừng vặt 10.8% − Phế khởi động & Spark 3.8% = OEE ròng 61.2% → Rõ ràng 2 thanh tổn thất cao nhất là Đổi màu (SMED) và Giảm tốc độ (làm mát/công nghệ)!"
        ),
        "common_mistakes": (
            "1. Vẽ cây tổn thất xong để treo tường chứ không liên kết xuống danh sách Dự án hành động (Action Plan), người chủ trì và tiến độ giảm từng nhánh theo từng quý."
        )
    },
    "Learning Curve": {
        "lesson_id": "L2.4",
        "definition_extra": (
            "\n• Quy luật tâm lý – cơ học của T.P. Wright: Con người và tổ chức luôn làm nhanh hơn nhờ tích lũy kinh nghiệm và sửa lỗi lặp lại. Trong sản xuất công nghiệp, tỷ lệ học việc thường rơi vào 80% – 90% (tỷ lệ 80% nghĩa là khi tổng số sản phẩm đã làm tăng gấp đôi — từ 1 lên 2, 2 lên 4, 4 lên 8, 8 lên 16 — thì thời gian làm 1 sản phẩm giảm xuống còn 80% so với trước, tức giảm 20% mỗi lần nhân đôi sản lượng!).\n"
            "• Đường cong phẳng dần theo thời gian: Giai đoạn đầu tiến bộ cực nhanh, sau vài tuần sẽ chạm tiệm cận thời gian chuẩn SAM."
        ),
        "cadivi_application_extra": (
            "\n• Ứng dụng thực tế tại CADIVI Miền Trung: (1) Lập kế hoạch công suất chính xác khi tuyển mới công nhân mùa cao điểm hoặc luân chuyển công nhân sang máy mới, (2) Dự báo thời gian đổi mã SMED những tuần đầu áp dụng quy trình mới, (3) Ước lượng sản lượng chạy thử nghiệm dòng cáp mới (như cáp Solar H1Z2Z2-K hay cáp chống cháy Mica FR)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Lần đầu tiên bạn tự lắp 1 chiếc bàn IKEA mất 60 phút; chiếc thứ 2 còn 48 phút (80%); chiếc thứ 4 còn 38.4 phút; chiếc thứ 8 còn 30.7 phút!\n"
            "\n• Ví dụ 2 (Dự báo năng suất công nhân mới tổ Đóng cuộn CADIVI): Công nhân mới ngày đầu đóng được 250 cuộn/ca (đạt 58% định mức chuẩn 430 cuộn). Áp dụng đường cong học việc 85% kèm đào tạo TWI bài bản, OE dự báo Tuần 1 đạt ~65%, Tuần 2 đạt ~80%, Tuần 3 đạt ~90% và Tuần 4 đạt 100% — giúp phòng Kế hoạch xếp định biên chính xác không bị hụt hàng giao khách!"
        ),
        "common_mistakes": (
            "1. Kỳ vọng công nhân mới vào ngày thứ 3 phải chạy bằng 100% tốc độ thợ 5 năm kinh nghiệm → Gây áp lực quá tải, tạo ra hàng loạt lỗi chất lượng/an toàn và tỷ lệ nghỉ việc cao!\n"
            "2. Nhầm rằng cứ chạy mãi thời gian sẽ giảm về 0 — thực tế mọi thao tác đều có giới hạn vật lý (Standard Time / tốc độ thiết kế máy)."
        )
    },
    "STAR": {
        "lesson_id": "L7.3",
        "definition_extra": (
            "\n• Cấu trúc kể chuyện phỏng vấn hành vi thuyết phục nhất (phân bổ thời lượng vàng 15% – 15% – 50% – 20%):\n"
            "  - S (Situation — 15%): Bối cảnh cụ thể, quy mô vấn đề ban đầu có con số (nhanh gọn trong 2–3 câu).\n"
            "  - T (Task — 15%): Nhiệm vụ & mục tiêu rõ ràng giao cho CHÍNH BẠN.\n"
            "  - A (Action — 50% — Quan trọng nhất!): Từng bước kỹ thuật & quản trị BẠN đã trực tiếp làm (dùng chữ 'Tôi đã...', không nói chung chung 'Chúng tôi đã...'; nêu rõ công cụ Time Study, Python, Pareto, thuyết phục con người như thế nào).\n"
            "  - R (Result — 20%): Kết quả định lượng Trước → Sau trung thực, kiểm chứng được + bài học bạn rút ra để áp dụng sang CADIVI!"
        ),
        "cadivi_application_extra": (
            "\n• Vũ khí ghi điểm tuyệt đối của bạn (Phan Thanh Thái Bảo) trước Ban Giám đốc CADIVI Miền Trung: Chuẩn bị sẵn 4 câu chuyện STAR sắc bén từ Mabuchi & Fujikura, nói trung thực từng con số đã xác minh và kết nối thẳng vào bài toán thực tế của nhà máy cáp điện."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Câu chuyện STAR #1 — Time Study & Đồ gá Canon INEX tại Mabuchi): S: Đo thủ công 1 hạng mục mất 60 giây, thao tác gá 1 mẫu/lượt lặp lại gây nghẽn tiến độ kiểm tra. T: Tìm giải pháp rút ngắn thời gian đo và giảm thao tác gá. A: Tôi thực hiện Time Study so sánh đo tay vs tự động trên Canon INEX, đồng thời thiết kế cải tiến bệ đồ gá từ 1 lên 16 mẫu/lượt gá và chuẩn hóa hướng dẫn thao tác. R: Giảm 50% thời gian đo (60s → 30s/hạng mục), tăng sức chứa mỗi lượt gá lên 16 mẫu (nói rõ: giảm thao tác gá lặp lại, không thổi phồng thành năng suất 16×).\n"
            "\n• Ví dụ 2 (Câu chuyện STAR #2 — Tự động hóa dữ liệu Python/VBA): S: Báo cáo dữ liệu khách hàng mất 3–7 ngày/tháng và nhập liệu OGP tốn 120 phút/ngày dễ sai sót. T: Tự động hóa luồng xử lý dữ liệu không tốn ngân sách mua phần mềm. A: Tôi tự xây công cụ bằng Python/VBA/Excel/Access tự đọc file máy đo, kiểm tra lỗi và xuất biểu mẫu chuẩn. R: Rút báo cáo tháng từ 3–7 ngày xuống 2 giờ và nhập liệu OGP từ 120 phút xuống 15 phút/ngày (-87.5%) → Sẵn sàng áp dụng ngay cho báo cáo OEE/BOM 4 phân xưởng CADIVI!"
        ),
        "common_mistakes": (
            "1. Kể quá dài phần Bối cảnh (Situation) mất 3 phút mà chỉ nói qua loa phần Hành động (Action) và không có số liệu Kết quả (Result).\n"
            "2. Thổi phồng số liệu (vd: nói nhầm bệ đo 1→16 mẫu thành tăng năng suất 16 lần) hoặc tiết lộ số tiền ROI mật chưa được công ty cũ cho phép công bố — hội đồng kỹ sư sẽ soi ra ngay lập tức!"
        )
    },
    "Hoshin Kanri": {
        "lesson_id": "L3.4",
        "definition_extra": (
            "\n• Bản chất 'Chiếc la bàn chiến lược' (tiếng Nhật: Hoshin = Phương hướng, Kanri = Quản trị): Rất nhiều công ty Ban Giám đốc đặt mục tiêu năm 'Giảm 8% giá thành sản xuất', nhưng xuống tới phân xưởng thì mỗi tổ lại làm một kiểu không liên quan. Hoshin Kanri dùng Ma trận chữ X (X-Matrix) trên đúng 1 trang giấy để nối thẳng 4 cạnh: Mục tiêu 3–5 năm (Nam) ↔ Mục tiêu đột phá năm nay (Tây) ↔ Các dự án OE trọng điểm hàng quý (Bắc) ↔ Chỉ số KPI đo lường & Người chịu trách nhiệm (Đông)!\n"
            "• Cơ chế Catchball (Tung – Hứng bóng): Không áp đặt mục tiêu 1 chiều từ trên xuống mà trao đổi 2 chiều giữa Giám đốc – Quản đốc – OE để đảm bảo mục tiêu vừa tham vọng vừa đủ nguồn lực thực thi."
        ),
        "cadivi_application_extra": (
            "\n• Nâng tầm Chuyên viên OE CADIVI từ 'người đi sửa lỗi vặt' thành 'cánh tay phải chiến lược của Giám đốc Nhà máy': giúp kết nối mục tiêu tổng của Tập đoàn GELEX / CADIVI xuống từng dự án SMED, SPC, BOM và bảng SQDCM hàng ngày ở Hòa Cầm."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như đội chèo thuyền 8 người — Hoshin Kanri giúp cả 8 người nhìn về đúng 1 đích và chèo cùng 1 nhịp thay vì mỗi người ra sức chèo theo 1 hướng riêng!\n"
            "\n• Ví dụ 2 (Sơ đồ X-Matrix mẫu tại CADIVI Miền Trung): Mục tiêu năm 'Giảm 5% chi phí chuyển đổi & hao phí NVL' → Chẻ thành 3 dự án ưu tiên: (1) SMED máy đùn nâng OEE 65%→76% (Chủ trì: OE + Xưởng Đùn), (2) SPC kéo Cpk chiều dày vỏ ≥ 1.5 giảm Over-thickness (OE + QA), (3) Số hóa báo cáo OEE/BOM tự động (OE + IT) → Theo dõi hàng tháng bằng biểu đồ Bowling Chart (Xanh/Đỏ)!"
        ),
        "common_mistakes": (
            "1. Đưa vào X-Matrix tới 20 dự án ưu tiên cùng lúc — 'cái gì cũng ưu tiên nghĩa là chẳng có gì ưu tiên'! Một nhà máy chỉ nên chọn 3–5 đột phá trọng điểm (Vital Few) mỗi năm."
        )
    },
    "ADKAR": {
        "lesson_id": "L3.4",
        "definition_extra": (
            "\n• Bản chất Quản trị Thay đổi con người (mô hình Prosci): Thống kê toàn cầu cho thấy 70% dự án Lean/OE thất bại KHÔNG phải vì công thức toán sai, mà vì con người tại xưởng ngầm phản đối hoặc làm đối phó. ADKAR chỉ ra rằng một tổ chức chỉ thay đổi khi TỪNG CÁ NHÂN đi qua đủ 5 bậc thang tuần tự:\n"
            "  1. Awareness (Nhận thức): Hiểu TẠI SAO phải thay đổi (và hậu quả nếu giữ nguyên).\n"
            "  2. Desire (Mong muốn): Tự nguyện muốn tham gia vì thấy lợi ích cho chính mình.\n"
            "  3. Knowledge (Kiến thức): Biết CÁCH làm quy trình/công cụ mới.\n"
            "  4. Ability (Năng lực): Làm thuần thục được thực tế trên máy.\n"
            "  5. Reinforcement (Củng cố): Hệ thống thưởng, LPA và LSW giữ thói quen mới bền lâu."
        ),
        "cadivi_application_extra": (
            "\n• Kỹ năng mềm sống còn ở CADIVI Miền Trung: Nhiều tổ trưởng và công nhân làm nghề cáp 10–15 năm có tâm lý ngại bị kỹ sư trẻ xuống 'bắt lỗi' hoặc sợ cải tiến xong bị tăng định mức/cắt tăng ca. ADKAR là kịch bản hóa giải từng nút thắt tâm lý đó!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Bạn muốn người thân tập thể dục — nếu chỉ mua tặng đôi giày (Knowledge) khi họ chưa thấy nguy cơ bệnh tật (Awareness) và chưa thích tập (Desire), đôi giày sẽ phủ bụi sau 3 ngày!\n"
            "\n• Ví dụ 2 (Hóa giải phản kháng khi làm SMED tại CADIVI): Thay vì ngay tuần đầu đứng bấm giờ soi lỗi công nhân, OE lắng nghe nỗi khổ của họ trước (Awareness/Desire: 'Mỗi lần đổi khuôn nặng 40kg phải khiêng tay đau lưng và đổi màu lâu hay phải tăng ca Chủ nhật'), làm ngay xe đẩy dụng cụ có bánh xe + giá treo 5S giúp họ đỡ đau lưng trước (tạo Desire!), rồi mới huấn luyện OPL tại máy (Knowledge), chạy thử Pilot cùng tổ trưởng uy tín nhất (Ability) và đề xuất thưởng nóng tổ đạt kỷ lục đổi mã < 15p (Reinforcement)!"
        ),
        "common_mistakes": (
            "1. Nhảy thẳng vào bước 3 (mở lớp đào tạo SOP dày 20 trang) trong khi bỏ qua bước 1 & 2 (công nhân không hiểu vì sao phải đổi và nghĩ đổi chỉ thêm việc cho họ) → Học xong lại làm theo thói quen cũ ngay ngày hôm sau!"
        )
    },
    "LOTO": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất bảo vệ tính mạng tuyệt đối: LOTO (Lockout = Khóa cơ học nguồn năng lượng bằng ổ khóa riêng; Tagout = Gắn thẻ cảnh báo ghi rõ Tên – SĐT – Giờ – Lý do) ngăn chặn thảm họa một người đang thò tay vào buồng máy bện/đầu đùn/tủ điện trong khi người khác tưởng máy rảnh liền bấm nút khởi động!\n"
            "• Nguyên tắc bất di bất dịch '1 Người – 1 Khóa – 1 Chìa': Nếu có 3 người (1 cơ khí, 1 điện, 1 vận hành) cùng sửa 1 máy kéo RBD, phải dùng càng khóa đa lỗ (Hasp) gắn đủ cả 3 ổ khóa cá nhân — CHỈ khi người cuối cùng ra khỏi vùng nguy hiểm và tự mở khóa của mình thì máy mới được cấp điện lại!"
        ),
        "cadivi_application_extra": (
            "\n• Bắt buộc 100% trong nhà máy dây cáp điện CADIVI ở các khu vực rủi ro chết người: (1) Thay lưới lọc Screen Pack & vệ sinh đầu đùn nóng 200°C, (2) Thay khuôn PCD / gỡ rối dây trong buồng máy kéo RBD & máy bện quay tốc độ cao, (3) Bể thử cao áp ngâm nước Water Immersion & phòng thử PD/Spark Tester, (4) Sửa chữa cầu trục & tủ biến tần."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Trước khi tự thay ổ cắm điện ở nhà, bạn ngắt cầu dao tổng, dán băng keo cảnh báo 'Đang sửa điện, cấm bật!' và dùng bút thử điện chạm kiểm tra chắc chắn hết điện (bước Try-Out Zero Energy) rồi mới đụng tay vào dây đồng!\n"
            "\n• Ví dụ 2 (Áp dụng LOTO trong dự án SMED tại CADIVI): Khi thiết kế quy trình đổi bộ Chày–Cối máy đùn 12 phút, OE tích hợp sẵn trạm treo khóa LOTO cá nhân ngay sát tủ điện máy đùn (mất đúng 25 giây để khóa & thử Try-Out) — vừa rút mạnh thời gian đổi mã vừa đảm bảo 100% an toàn không ai bị khởi động nhầm trục vít!"
        ),
        "common_mistakes": (
            "1. Chỉ bấm nút Dừng Khẩn Cấp (E-Stop) trên bảng điều khiển mà tưởng là an toàn — nút E-Stop chỉ ngắt mạch điều khiển chứ KHÔNG cô lập nguồn điện chính hay áp suất khí nén/thủy lực!\n"
            "2. Bỏ qua bước 6 (Try-Out: bấm nút Start thử xác nhận Zero Energy rồi trả về OFF) — nhiều tai nạn xảy ra vì ngắt nhầm cầu dao của máy bên cạnh!"
        )
    },
    "EHS": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất 'An toàn là số 1 — Không có bất kỳ ngoại lệ nào': EHS (Environment – Health – Safety) bao trùm quản trị rủi ro tai nạn lao động, bệnh nghề nghiệp (điếc do tiếng ồn > 85 dB, đau cột sống do nâng rulo, hít khói nhựa) và bảo vệ môi trường (xử lý nước thải, dầu nhũ tương, khí thải nhựa, rác nguy hại).\n"
            "• Tháp kiểm soát rủi ro 5 bậc (Hierarchy of Controls — từ mạnh nhất đến yếu nhất): (1) Loại bỏ mối nguy (Elimination), (2) Thay thế ít nguy hiểm hơn (Substitution), (3) Kiểm soát kỹ thuật (Engineering — rào chắn liên động Interlock, chụp hút khói, cảm biến rèm quang), (4) Kiểm soát hành chính (SOP, biển cảnh báo, LOTO), (5) Bảo hộ cá nhân PPE (biện pháp cuối cùng, không bao giờ là biện pháp duy nhất!)."
        ),
        "cadivi_application_extra": (
            "\n• Mối liên kết chặt chẽ giữa OE và EHS tại CADIVI: Mọi dự án cải tiến Layout AutoCAD (phân luồng người đi bộ và xe nâng chở rulo 3 tấn), cải tiến tốc độ máy, cải tiến SMED hay thiết kế đồ gá đều BẮT BUỘC có chữ ký đánh giá rủi ro (JSA/HIRA) cùng bộ phận EHS trước khi chạy thử."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Áp dụng Tháp 5 bậc tại xưởng Kéo CADIVI): Khu máy kéo sợi & bện ồn 92 dB — thay vì chỉ phát nút tai PPE (bậc 5 yếu nhất), OE phối hợp Cơ điện đóng kín nắp chụp cách âm (bậc 3 Engineering Controls) kéo độ ồn xuống 81 dB vừa bảo vệ thính giác vừa giảm mệt mỏi tăng OLE!\n"
            "\n• Ví dụ 2 (Tư duy Near-Miss): Một cuộn rulo gỗ lăn trượt khỏi nêm kê trên sàn nghiêng nhưng may mắn chưa trúng ai (Sự cố suýt tai nạn — Near-Miss). OE lập tức chế tạo thanh nêm thép có khóa chống trượt gắn cố định cho toàn bộ khu đệm rulo trước khi xảy ra tai nạn thật!"
        ),
        "common_mistakes": (
            "1. Nối tắt (Bypass) công tắc cửa rào an toàn máy bện hoặc bỏ chụp che máy đùn để thao tác đổi mã nhanh hơn vài chục giây — đây là hành vi vi phạm nghiêm trọng nhất trong mọi nhà máy chuyên nghiệp!"
        )
    },
    "ISO 9001": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất Hệ thống Quản lý Chất lượng (QMS — phiên bản hiện hành ISO 9001:2015): ISO 9001 không tự quy định chiều dày vỏ cáp là mấy milimet (việc đó do IEC/TCVN quy định), mà quy định cách nhà máy vận hành kỷ luật và nhất quán dựa trên 7 nguyên tắc: Hướng vào khách hàng, Vai trò lãnh đạo, Tham gia của mọi người, Tiếp cận theo quá trình, Cải tiến liên tục (PDCA), Quyết định dựa trên bằng chứng dữ liệu, và Quản lý mối quan hệ.\n"
            "• Các điều khoản OE tương tác nhiều nhất: Điều khoản 7.1.5 (Hiệu chuẩn thiết bị đo lường), 8.5 (Kiểm soát sản xuất & truy xuất nguồn gốc), 8.7 (Kiểm soát sản phẩm không phù hợp NCR), 9.1 (Đo lường phân tích dữ liệu), 10.2 (Hành động khắc phục CAPA)."
        ),
        "cadivi_application_extra": (
            "\n• Tại CADIVI Miền Trung, ISO 9001 là khung pháp lý giúp OE khóa chặt mọi thành quả cải tiến: sau mỗi dự án Kaizen/DMAIC thành công, OE bắt buộc cập nhật vào hệ thống tài liệu kiểm soát (SOP, Control Plan, Biểu mẫu ghi chép) để cả nhà máy duy trì đồng bộ và vượt qua các đợt đánh giá giám sát hàng năm."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Giống như chuẩn vận hành của chuỗi cà phê lớn — dù bạn uống ở Đà Nẵng hay TP.HCM, quy trình kiểm tra nguyên liệu, công thức pha và xử lý khi khách phàn nàn đều có chuẩn rõ ràng nhất quán.\n"
            "\n• Ví dụ 2 (Tại CADIVI): Khi phát hiện lô cáp lỗi in phun mờ chữ, quy trình ISO 9001 yêu cầu: (1) Cô lập ngay khu vực hàng lỗi NCR tránh xuất nhầm khách, (2) Truy gốc 5 Whys & lập CAPA khắc phục đầu phun mực + lắp cảm biến kiểm tra độ nét, (3) Đánh giá lại hiệu lực sau 30 ngày!"
        ),
        "common_mistakes": (
            "1. Biến ISO 9001 thành 'núi giấy tờ đối phó đoàn đánh giá' (làm 1 đằng, viết quy trình 1 nẻo) — OE giỏi phải viết SOP ngắn gọn trực quan 1–2 trang (OPL/Visual SOP) để công nhân thực sự dùng hàng ngày!"
        )
    },
    "ISO 14001": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất Hệ thống Quản lý Môi trường (EMS — ISO 14001:2015): Yêu cầu nhà máy nhận diện toàn bộ khía cạnh tác động môi trường (nước thải công nghiệp, khí thải lò hơi/đùn nhựa, chất thải nguy hại, tiếng ồn, tiêu thụ tài nguyên) và tuân thủ chặt chẽ Luật Bảo vệ Môi trường thông qua chu trình PDCA giảm phát thải tại nguồn."
        ),
        "cadivi_application_extra": (
            "\n• Rất gắn với dự án tiết kiệm vật tư của OE CADIVI (Green Lean): Giảm phế phẩm đồng/nhựa nghĩa là giảm trực tiếp rác công nghiệp; quản lý tốt bể lọc tinh nhũ tương kéo đồng giúp kéo dài tuổi thọ dầu từ 6 tháng lên 18 tháng (giảm mạnh chi phí thuê đơn vị xử lý chất thải nguy hại!)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tại Xưởng Kéo CADIVI): Lắp hệ thống lọc ly tâm & kiểm tra pH/nồng độ dầu Drawing Emulsion hàng tuần giúp tái tuần hoàn sạch mạt đồng, giảm 60% lượng dầu nhũ tương thải nguy hại phải thuê tiêu hủy mỗi năm (vừa đạt ISO 14001 vừa tiết kiệm > 150 triệu VNĐ/năm!).\n"
            "\n• Ví dụ 2 (Tại Xưởng Đùn): Tối ưu nhiệt độ nòng đùn & hút xử lý mùi khói nhựa PVC/XLPE qua tháp hấp phụ than hoạt tính giúp môi trường làm việc trong xưởng sạch mùi và vượt chuẩn quan trắc khí thải định kỳ."
        ),
        "common_mistakes": (
            "1. Chỉ chú trọng xử lý rác ở cuối đường ống (tốn rất nhiều tiền xử lý rác) thay vì dùng tư duy Lean/OE giảm phát sinh phế phẩm và rò rỉ ngay tại máy sản xuất!"
        )
    },
    "ISO 45001": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất Hệ thống Quản lý An toàn & Sức khỏe Nghề nghiệp (OHSMS — ISO 45001:2018, thay thế OHSAS 18001): Chuyển dịch tư duy từ 'xử lý sau khi có tai nạn' sang chủ động nhận diện mối nguy (HIRA), loại bỏ rủi ro ngay từ khâu thiết kế quy trình/mặt bằng và bắt buộc có sự tham vấn trực tiếp của người công nhân tại hiện trường."
        ),
        "cadivi_application_extra": (
            "\n• Đan xen chặt chẽ với Lean/Ergonomics tại CADIVI Miền Trung: Giảm thao tác cúi nâng rulo nặng (Ergonomics), tách luồng người đi bộ có hàng rào bảo vệ khỏi luồng xe nâng 3 tấn, áp dụng LOTO 6 bước và quản trị sự cố suýt tai nạn (Near-Miss)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Cải tiến Ergonomics gắn ISO 45001 tại CADIVI): Công nhân đóng cuộn dây 20 kg phải cúi gập lưng bê từ sàn lên pallet 150 lần/ca (nguy cơ thoát vị đĩa đệm cao) → Lắp bàn nâng thủy lực giữ mặt pallet luôn ở vùng vàng cao 85 cm giúp vừa giảm 100% chấn thương lưng vừa tăng tốc độ xếp pallet +18%!\n"
            "\n• Ví dụ 2 (An toàn máy móc): Đánh giá HIRA phát hiện thợ vận hành máy bện có thể mở cửa lồng khi trống bện vẫn còn quán tính quay 15 giây → Gắn khóa liên động có trễ thời gian (Time-Delay Interlock) chỉ mở được cửa khi tốc độ trục = 0 vòng/phút!"
        ),
        "common_mistakes": (
            "1. Chỉ đổ lỗi 'do công nhân bất cẩn' mỗi khi xảy ra tai nạn — theo tư duy ISO 45001 & Poka-Yoke, phải thiết kế lại máy móc/quy trình sao cho kể cả khi con người mệt mỏi cũng không thể gặp tai nạn!"
        )
    },
    "ISO 50001": {
        "lesson_id": "L5.4",
        "definition_extra": (
            "\n• Bản chất Hệ thống Quản lý Năng lượng (EnMS — ISO 50001:2018): Khác với việc hô khẩu hiệu 'nhớ tắt đèn khi ra về', ISO 50001 đòi hỏi quản trị năng lượng bằng số liệu định lượng khoa học:\n"
            "  1. Xác định các điểm tiêu thụ năng lượng trọng yếu SEU (Significant Energy Uses — chiếm 80% hóa đơn điện nhà máy).\n"
            "  2. Lập Đường cơ sở năng lượng (EnB — Energy Baseline) và Chỉ số hiệu suất năng lượng `EnPI = SEC = kWh / Tấn sản phẩm`.\n"
            "  3. Tối ưu kỹ thuật & điều độ giờ thấp điểm để kéo giảm EnPI bền vững hàng năm."
        ),
        "cadivi_application_extra": (
            "\n• Mỏ vàng chi phí Overhead thứ 2 ngay sau NVL tại CADIVI Miền Trung! Động cơ máy kéo thô RBD (250–350 kW), dàn điện trở nòng đùn 180–220°C, lò ủ, bể xông XLPE, Chiller và máy nén khí tạo ra hóa đơn tiền điện nhiều tỷ đồng mỗi năm → OE am hiểu ISO 50001 sẽ tạo dấu ấn cực lớn!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Giống như theo dõi mức tiêu hao xăng của xe (6.5 lít/100km thay vì 9 lít/100km) bằng cách bơm lốp đủ áp suất, bảo dưỡng lọc gió và không nổ máy chờ không tải.\n"
            "\n• Ví dụ 2 (Dịch chuyển phụ tải giờ thấp điểm tại CADIVI): Giá điện giờ cao điểm (~3,100đ/kWh) đắt gấp ~2.8 lần giờ thấp điểm 22:00–04:00 (~1,100đ/kWh). Lập lịch chạy lò ủ chuông và bể gia nhiệt xông XLPE vào khung 22:00–04:00 giúp giảm ngay 120–180 triệu VNĐ tiền điện/tháng mà không tốn 1 đồng đầu tư thiết bị!\n"
            "\n• Ví dụ 3 (Bọc áo cách nhiệt nòng đùn + giảm Idle Heating): Bọc áo bảo ôn cách nhiệt cho 6 nòng máy đùn và cắt thời gian chờ nhiệt không tải lúc đổi mã giúp giảm 18% điện gia nhiệt (tương đương ~55 triệu/tháng)."
        ),
        "common_mistakes": (
            "1. Chỉ nhìn tổng số kWh điện tăng/giảm tuyệt đối mà quên chia cho sản lượng tấn cáp (`kWh/tấn`) — tháng chạy nhiều đơn hàng thì tổng điện tăng là bình thường, điều quan trọng là cường độ điện năng trên mỗi tấn cáp phải GIẢM!"
        )
    },
    "VFD": {
        "lesson_id": "L5.4",
        "definition_extra": (
            "\n• Bản chất vật lý tiết kiệm điện kỳ diệu (Định luật Đồng dạng — Affinity Laws): Với các tải bơm nước làm mát (Cooling Trough), quạt tháp giải nhiệt và quạt hút khí, công suất tiêu thụ tỷ lệ với LẬP PHƯƠNG tốc độ quay (`P ∝ N³`)! Nghĩa là khi lắp biến tần VFD giảm tốc độ quạt/bơm xuống còn 80% lúc non tải, lượng điện tiêu thụ giảm xuống còn `0.8³ = 51.2%` — TIẾT KIỆM GẦN 50% ĐIỆN NĂNG!\n"
            "• Ngoài tiết kiệm điện, VFD còn giúp khởi động êm (Soft Start), đồng bộ chính xác tốc độ tuyến tính giữa trục vít đùn – bánh kéo Capstan – trống thu dây Take-up để giữ dung sai đường kính cáp cực ổn định."
        ),
        "cadivi_application_extra": (
            "\n• Ứng dụng kép tại CADIVI Miền Trung: (1) Dự án tiết kiệm năng lượng ISO 50001 (lắp VFD cho bơm nước làm mát, quạt tháp giải nhiệt, máy nén khí), (2) Dự án ổn định chất lượng & bảo trì (nâng cấp đồng bộ tốc độ động cơ kéo/bện/đùn chống giật đứt sợi)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Điều hòa Inverter (chính là dùng biến tần VFD) chạy êm ở tốc độ thấp duy trì nhiệt độ ổn định nên tiết kiệm 35–50% tiền điện so với điều hòa thường cứ đóng/ngắt cục nóng hết công suất!\n"
            "\n• Ví dụ 2 (Tính toán ROI lắp VFD tại CADIVI): Lắp biến tần VFD (vốn đầu tư 85 triệu) cho cụm bơm tuần hoàn nước giải nhiệt 45 kW chạy non tải vào ca đêm/mùa mát giúp giảm trung bình 12 kW × 16 giờ/ngày × 26 ngày = 4,992 kWh/tháng ≈ 11 triệu VNĐ/tháng → Hoàn vốn Payback chỉ 7.7 tháng!"
        ),
        "common_mistakes": (
            "1. Lắp VFD nhưng bỏ mặc cài đặt cố định ở tần số 50 Hz suốt 24/24 (không gắn cảm biến áp suất/nhiệt độ điều khiển phản hồi PID) → Tốn tiền mua biến tần mà không tiết kiệm được đồng điện nào!"
        )
    },
    "MOC / ECN": {
        "lesson_id": "L4.5",
        "definition_extra": (
            "\n• Bản chất chốt chặn an toàn & chất lượng: Mọi sự cố thu hồi hàng loạt hay tai nạn nghiêm trọng trong nhà máy thường bắt nguồn từ một 'thay đổi nhỏ không báo ai' (vd: mua hạt nhựa nhà cung cấp mới rẻ hơn, chỉnh giảm chiều dày bọc, đổi tốc độ đùn cao hơn, hàn thêm cơ cấu kẹp SMED). MOC (Management of Change) / ECN (Engineering Change Notice) buộc mọi thay đổi phải qua thẩm định chéo 4 góc (Kỹ thuật – QA/QC – EHS – BOM/Kế toán) và chạy thử lô nhỏ trước khi cho chạy đại trà."
        ),
        "cadivi_application_extra": (
            "\n• Quy trình bắt buộc cho mọi dự án OE tại CADIVI Miền Trung (đặc biệt khi chỉnh dung sai mục tiêu giảm Copper Give-away / Over-thickness liên quan đến quy chuẩn pháp lý bắt buộc QCVN 4 & IEC 60502)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Trong ngành hàng không, bất kỳ thay đổi nhỏ nào về loại ốc vít hay phần mềm đều phải qua hội đồng kỹ thuật kiểm thử bay mẫu và cập nhật sổ tay bảo dưỡng rồi mới được áp dụng cho cả đội bay.\n"
            "\n• Ví dụ 2 (Quy trình MOC thực tế tại CADIVI): OE đề xuất giảm chiều dày mục tiêu lớp vỏ PVC dây CXV từ 1.25 mm xuống 1.17 mm nhờ lắp Laser Gauge Closed-loop → Mở phiếu MOC: (1) QA xác nhận vẫn cao hơn cận min IEC 60502 (1.07 mm) trên 3σ, (2) Chạy thử 3 cuộn gửi Lab đo đủ Tensile/Spark/Water Immersion đạt 100%, (3) Giám đốc ký duyệt ECN, (4) Cập nhật đồng bộ MBOM trên ERP & Control Plan tại máy!"
        ),
        "common_mistakes": (
            "1. Cải tiến xong ở xưởng nhưng quên gửi ECN cho phòng Kế toán/ERP cập nhật định mức MBOM → Số liệu tiết kiệm vật tư không được ghi nhận chính thức vào giá thành chuẩn.\n"
            "2. Tự ý thay đổi công thức nhựa/tốc độ mà không chạy lô Pilot dẫn tới rớt bài thử lão hóa nhiệt Aging Oven 7 ngày sau khi đã sản xuất hàng chục km cáp!"
        )
    },
}


ENRICHMENTS.update({
    # =========================================================================
    # CHUNK 2: LEAN MANUFACTURING & CẢI TIẾN (30) + HOẠCH ĐỊNH, BOM & CHI PHÍ (21)
    # =========================================================================
    "Lean": {
        "lesson_id": "L3.1",
        "definition_extra": (
            "\n• 5 Nguyên tắc vàng của Lean Thinking (Womack & Jones):\n"
            "  1. Xác định Giá trị (Value) từ góc nhìn khách hàng (khách hàng chỉ trả tiền cho thao tác biến đổi đồng/nhựa thành cáp đạt chuẩn, KHÔNG trả tiền cho việc bạn bê rulo đi lòng vòng hay chờ đổi màu!).\n"
            "  2. Vẽ Chuỗi giá trị (Value Stream) để phơi bày toàn bộ bước không tạo giá trị (Muda).\n"
            "  3. Tạo Dòng chảy liên tục (Flow) — giảm lô lớn, giảm dừng chờ, giảm WIP.\n"
            "  4. Thiết lập Hệ thống Kéo (Pull) — công đoạn sau cần mới kéo công đoạn trước chạy.\n"
            "  5. Theo đuổi Sự hoàn hảo (Perfection) qua văn hóa Kaizen hàng ngày.\n"
            "• Bộ 3 kẻ thù của Lean (3M): Muda (Lãng phí), Mura (Bất ổn/Dao động — đầu tháng nhàn cuối tháng chạy điên cuồng), Muri (Quá tải máy & người)."
        ),
        "cadivi_application_extra": (
            "\n• Trọng tâm cốt lõi mục 4 trong JD OE CADIVI: Áp dụng tổng hợp 5S, VSM, SMED, Poka-Yoke, Pull/Kanban, Standard Work xuyên suốt 4 phân xưởng Kéo – Bện – Đùn – Đóng gói tại Hòa Cầm để rút Lead Time và giải phóng dòng tiền tồn kho đồng/nhựa."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Đi siêu thị thanh toán — xếp hàng 15 phút (Muda chờ đợi), nhân viên chạy đi hỏi giá món mất tem (Muda di chuyển), quầy lúc trống lúc ùn ứ cuối tuần (Mura). Áp dụng Lean là quét mã vạch chuẩn, bố trí quầy thanh toán tự động và san khung giờ khuyến mãi!\n"
            "\n• Ví dụ 2 (Tại CADIVI): Chuyển dây chuyền dây dân dụng VC 2.5 từ đẩy từng lô lớn 50 km/màu (gây kẹt 120 rulo chờ trước máy đùn) sang lô nhỏ linh hoạt nhờ SMED + Pull Floor Kanban giúp cắt giảm 55% tồn kho WIP và rút Lead Time giao hàng từ 10 ngày xuống 4 ngày!"
        ),
        "common_mistakes": (
            "1. Hiểu nhầm Lean là 'cắt giảm nhân sự' (L.E.A.N = Less Employees Are Needed) → Gây phản kháng dữ dội dưới xưởng! Lean đúng nghĩa là giải phóng nhân sự khỏi thao tác lãng phí để mở rộng sản lượng và nhận thêm đơn hàng mới.\n"
            "2. Chỉ làm 5S quét dọn hình thức mà bỏ qua dòng chảy Flow, SMED và Pull."
        )
    },
    "SMED": {
        "lesson_id": "L3.3",
        "definition_extra": (
            "\n• Định nghĩa chuẩn thời gian chuyển đổi: Tính từ thời điểm ra sản phẩm ĐẠT CHUẨN cuối cùng của lô A cho đến khi ra sản phẩm ĐẠT CHUẨN đầu tiên của lô B ở tốc độ danh định (bao gồm cả thời gian chạy thử, đo chỉnh đường kính và đoạn dây xả phế đầu ca!).\n"
            "• 4 Giai đoạn chuyển hóa của Shigeo Shingo:\n"
            "  - Bước 1: Quay video hiện trạng, tách từng thao tác nhỏ.\n"
            "  - Bước 2: Phân biệt rạch ròi Thao tác Trong (Internal — bắt buộc dừng máy) vs Thao tác Ngoài (External — làm được khi máy đang chạy!). Chỉ riêng việc đưa thao tác Ngoài ra trước khi dừng máy đã giảm ngay 30–50% Downtime!\n"
            "  - Bước 3: Chuyển thao tác Trong thành Ngoài (vd: sấy nóng trước đầu Chày–Cối ở tủ phụ bên ngoài; soạn sẵn hạt nhựa đã sấy trên phễu di động).\n"
            "  - Bước 4: Tinh gọn phần Trong còn lại (đầu đùn tự định tâm, chốt kẹp 1 chạm, 2 người làm song song kiểu F1 Pit-stop, nạp Recipe tự động trên HMI)."
        ),
        "cadivi_application_extra": (
            "\n• Đòn bẩy số 1 cho Xưởng Đùn & Xưởng Bện tại CADIVI Miền Trung: Rút ngắn thời gian đổi màu nhựa/đổi tiết diện máy đùn không chỉ tăng trực tiếp OEE Availability mà còn cắt giảm 60–75% lượng nhựa xả Purge Scrap và dây đồng dính nhựa phế đầu ca!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Đội thay lốp xe đua F1 hoàn thành thay 4 bánh xe trong 2.2 giây vì mọi dụng cụ, lốp mới sấy nóng sẵn đều được chuẩn bị sẵn trước khi xe dừng (External) và 14 người thao tác song song (Parallel) bằng súng tháo 1 ốc trung tâm (One-touch)!\n"
            "\n• Ví dụ 2 (Tại máy đùn CADIVI): Đổi từ dây VC 4.0 Đen sang VC 2.5 Trắng ban đầu mất 55 phút & xả 25 kg nhựa → Áp dụng Color Sequencing (Trắng → Đen), tủ sấy sẵn đầu Tip/Die bên ngoài, đầu tự định tâm và nạp Recipe PLC rút xuống còn 12 phút (-78.2%) và chỉ còn 6 kg nhựa xả, tiết kiệm hàng trăm triệu đồng/năm!\n"
            "\n• Ví dụ 3 (Tại máy kéo sợi): Chuẩn bị sẵn bộ khuôn PCD mới đã lắp trong cassette dự phòng bên ngoài giúp đổi dải tiết diện kéo giảm từ 40 phút xuống 11 phút!"
        ),
        "common_mistakes": (
            "1. Vội vàng xin tiền mua đầu đùn tháo nhanh hàng trăm triệu ngay bước đầu trong khi công nhân vẫn đang dừng máy rồi mới đi kho tìm cờ-lê và hạt nhựa (chưa làm bước tách External tốn 0 đồng!).\n"
            "2. Quên áp dụng quy trình khóa an toàn LOTO khi làm nhanh SMED."
        )
    },
    "VSM": {
        "lesson_id": "L3.2",
        "definition_extra": (
            "\n• Bản chất 'Bản đồ chụp X-quang toàn nhà máy': Khác với sơ đồ quy trình thông thường chỉ vẽ các hộp công việc, VSM vẽ đồng thời 3 dòng chảy trên cùng 1 tờ giấy A3 cho một họ sản phẩm (Product Family): (1) Dòng Thông tin ở phía trên (Đơn hàng khách hàng → Kế hoạch MRP → Lệnh sản xuất xuống xưởng), (2) Dòng Vật tư ở giữa (từ Nhà cung cấp → từng công đoạn có đủ dữ liệu C/T, C/O đổi mã, OEE, số người, số rulo WIP nằm chờ giữa các khâu → Giao khách hàng), (3) Đường răng cưa Thời gian ở đáy so sánh Tổng Lead Time với Thời gian tạo giá trị thực (VA Time) để tính tỷ lệ hiệu quả chuỗi `PCE = VA Time / Lead Time`!"
        ),
        "cadivi_application_extra": (
            "\n• Bước khởi đầu bắt buộc trong 30 ngày đầu của OE tại CADIVI Miền Trung: Chọn 1 họ sản phẩm chủ lực (vd: Cáp lực hạ thế CXV hoặc Dây dân dụng VC) đi bộ ngược dòng từ Kho xuất về Kho đồng Rod để vẽ Current State VSM, khoanh tròn các 'ngôi sao Kaizen Burst' (chỗ ùn ứ WIP, chỗ đổi mã lâu, chỗ lệch kế hoạch) rồi thiết kế Future State VSM mục tiêu 6 tháng!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Khi kẹt xe toàn thành phố, bạn dùng ảnh chụp Flycam từ trên cao (VSM) để thấy rõ ngã tư nào đang tắc gây ùn cả 5 tuyến đường thay vì chỉ đứng nhìn 1 đoạn hẻm nhỏ!\n"
            "\n• Ví dụ 2 (VSM cáp lực CXV tại CADIVI): Hiện trạng có 7 công đoạn với Tổng Process Time = 21 giờ, nhưng tổng Lead Time = 12 ngày (288 giờ, PCE chỉ 7.3%) do ùn rulo trước máy đùn (3.5 ngày) và chờ gom mẻ bể xông XLPE (3 ngày). Thiết kế Future State VSM với SMED + Pull Buffer + gom lịch xông XLPE theo ngày rút Lead Time xuống 4.2 ngày (PCE tăng gần gấp 3 lên 21%)!"
        ),
        "common_mistakes": (
            "1. Ngồi phòng máy lạnh hỏi số liệu trên ERP để vẽ VSM thay vì đích thân đi bộ xuống xưởng đếm từng rulo WIP thật (số liệu thực tế tại sàn thường khác xa ERP!).\n"
            "2. Vẽ xong Current State VSM thật đẹp rồi treo lên tường cho oai mà không vẽ Future State VSM và không lập kế hoạch hành động cho các Kaizen Burst."
        )
    },
    "5S": {
        "lesson_id": "L3.1",
        "definition_extra": (
            "\n• Hiểu đúng bản chất 5 chữ S chuẩn công nghiệp Nhật (KHÔNG chỉ là quét nhà lau sàn!):\n"
            "  - S1 Seiri (Sàng lọc): Phân loại cái Cần vs Không Cần bằng chiến dịch Red Tag — loại bỏ sạch vật thừa khỏi hiện trường.\n"
            "  - S2 Seiton (Sắp xếp): 'Mỗi thứ 1 chỗ, mỗi chỗ 1 thứ' — kẻ vạch sơn sàn phân vùng, bảng bóng dụng cụ Shadow Board để ai cũng tìm được đồ trong 30 giây và nhìn 3 giây biết ngay thiếu món gì.\n"
            "  - S3 Seiso (Sạch sẽ): Lau chùi máy móc là để KIỂM TRA phát hiện rò dầu, nứt dây curoa, lỏng ốc (gắn chặt với Jishu Hozen!).\n"
            "  - S4 Seiketsu (Săn sóc): Tiêu chuẩn hóa màu sơn sàn, nhãn nhận diện, lịch vệ sinh 5 phút cuối ca.\n"
            "  - S5 Shitsuke (Sẵn sàng/Kỷ luật): Biến thành thói quen tự giác duy trì qua kiểm tra phân tầng LPA và chấm điểm 5S minh bạch."
        ),
        "cadivi_application_extra": (
            "\n• Nền móng của mọi cải tiến khác tại CADIVI Miền Trung: Không có 5S thì không thể làm SMED (mất 15 phút tìm cờ-lê/bộ Chày–Cối), không thể kiểm soát BOM (lẫn đồng trần với đồng dính nhựa), và dễ mất an toàn xe nâng (rulo để tràn ra đường đi)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Hộp dụng cụ sửa xe có khoét xốp đúng hình dáng từng cờ-lê — mở nắp ra mất 1 giây biết ngay thiếu cây cờ-lê số 14, không bao giờ phải lục tung cả thùng!\n"
            "\n• Ví dụ 2 (Tại Xưởng Đùn CADIVI): Đóng xe đẩy SMED có bảng Shadow Board treo đúng bộ cờ-lê, dao đồng cạo nhựa, cảm biến dự phòng và giá đánh số từng cỡ Tip/Die đặt ngay sát đầu máy → Cắt ngay 9 phút lãng phí đi tìm đồ nghề mỗi lần đổi mã!\n"
            "\n• Ví dụ 3 (Phân loại phế liệu 5S bằng mã màu): 3 thùng phế sơn 3 màu cố định ngay chân máy: Xanh = Đồng trần tinh khiết (~94% giá trị thu hồi), Vàng = Đồng dính nhựa, Xám = Nhựa purge sạch tái chế → Chấm dứt cảnh vứt lẫn gây mất hàng trăm triệu đồng giá trị thu hồi mỗi năm!"
        ),
        "common_mistakes": (
            "1. Chỉ tổ chức 'tổng vệ sinh 5S' rầm rộ trước ngày có khách VIP hoặc đoàn đánh giá ISO tới, xong hôm sau lại bừa bộn như cũ vì thiếu S4 (chuẩn hóa) và S5 (LPA hàng tuần)."
        )
    },
    "Red Tag": {
        "lesson_id": "L3.1",
        "definition_extra": (
            "\n• Phân biệt 2 loại thẻ trực quan quan trọng nhất trong xưởng Lean/TPM:\n"
            "  1. Thẻ Đỏ 5S (Red Tag): Dán lên vật tư, khuôn cũ, rulo hỏng, dụng cụ không rõ công dụng tại xưởng → Di chuyển vào 'Khu tập kết Thẻ Đỏ' trong 15–30 ngày; quá hạn không bộ phận nào chứng minh cần dùng sẽ lập biên bản thanh lý/trả kho.\n"
            "  2. Thẻ Bất Thường Fuguai (TPM): Dùng khi công nhân vệ sinh máy phát hiện lỗi nhỏ (rò dầu hộp số, kính đồng hồ áp suất mờ, thiếu bulông nắp che, rò khí nén): Thẻ Trắng (Tổ vận hành tự xử lý trong ca) vs Thẻ Đỏ (Chuyển Phòng Cơ Điện xử lý kèm hạn chót)."
        ),
        "cadivi_application_extra": (
            "\n• Hoạt động Quick-Win cực hiệu quả trong 30 ngày đầu của OE tại CADIVI: Dễ huy động công nhân cùng làm, kết quả nhìn thấy rõ ngay bằng mắt (ảnh Trước–Sau) tạo niềm tin mạnh với Quản đốc và Ban Giám đốc."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Chiến dịch Red Tag kho khuôn): Rà soát giá khuôn kéo và đầu Chày–Cối xưởng Đùn phát hiện 38 bộ đã mòn/ngừng sản xuất từ 3 năm trước đang chiếm 40% không gian giá để → Gắn Red Tag chuyển thanh lý giúp sắp xếp lại toàn bộ bộ khuôn đang dùng theo đúng thứ tự tiết diện 1.5 → 300 mm²!\n"
            "\n• Ví dụ 2 (Thẻ Fuguai chống rò khí nén): Một ngày đi kiểm tra máy bằng thẻ Fuguai ở phân xưởng Kéo & Đùn gắn được 27 thẻ rò khí nén & lỏng nắp bảo vệ, xử lý xong 25 thẻ trong 10 ngày giúp tiết kiệm ~18 triệu tiền điện máy nén khí/tháng!"
        ),
        "common_mistakes": (
            "1. Gắn hàng trăm thẻ Đỏ/Fuguai phủ kín xưởng nhưng KHÔNG có kế hoạch đóng thẻ (Tag Closure Rate < 30%) → Công nhân mất niềm tin, nghĩ rằng báo lỗi cũng chẳng ai sửa!"
        )
    },
    "Kaizen": {
        "lesson_id": "L3.1",
        "definition_extra": (
            "\n• Bản chất văn hóa cải tiến liên tục (Kai = Thay đổi, Zen = Tốt hơn): Khác với Kaikaku (đổi mới đột phá tốn vốn đầu tư lớn mua dây chuyền mới), Kaizen tập trung vào hàng trăm cải tiến nhỏ, chi phí cực thấp hoặc 0 đồng do chính người trực tiếp đứng máy và kỹ sư OE đề xuất mỗi tuần — cộng dồn lại tạo sức mạnh khổng lồ không đối thủ nào sao chép được!\n"
            "• 2 hình thức triển khai song song: (1) Daily Kaizen / Teian (đề xuất sáng kiến thường ngày của từng công nhân, duyệt thưởng nhanh trong 7 ngày), (2) Kaizen Blitz / Kaizen Event (chiến dịch tập trung 3–5 ngày liên tục cùng liên phòng ban xử lý dứt điểm 1 nút thắt như SMED máy đùn hay Layout tổ đóng cuộn)."
        ),
        "cadivi_application_extra": (
            "\n• OE CADIVI đóng vai trò 'nhạc trưởng Kaizen': Xây mẫu phiếu Kaizen 1 trang cực đơn giản (Ảnh Trước – Ảnh Sau – Chi phí – Lợi ích), trực tiếp hỗ trợ công nhân tính toán số liệu tiết kiệm để trình duyệt thưởng nóng minh bạch hàng tháng."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Dán 1 miếng móc treo chìa khóa ngay cửa ra vào tốn 5,000đ nhưng mỗi sáng không bao giờ mất 5 phút tìm chìa khóa — đó là tinh thần Kaizen!\n"
            "\n• Ví dụ 2 (Kaizen nhỏ chi phí gần 0 đồng tại CADIVI): Công nhân máy đùn đề xuất hàn thêm 1 máng trượt nghiêng bằng thép phế liệu dưới miệng xả nhựa đầu đùn rơi thẳng vào thùng đựng nước nguội thay vì phải cúi xúc nhựa nóng dưới sàn → Giảm 100% nguy cơ bỏng tay và cắt 4 phút vệ sinh mỗi lần đổi màu!\n"
            "\n• Ví dụ 3 (Kaizen Blitz 5 ngày): Tập trung nhóm 6 người (OE + Quản đốc Đùn + Cơ điện + Tổ trưởng) suốt 5 ngày trên máy đùn số 1 để rút thời gian đổi mã từ 55p xuống 12p rồi nhân rộng toàn xưởng."
        ),
        "common_mistakes": (
            "1. Bắt công nhân viết hồ sơ sáng kiến dài 5 trang Word đầy công thức → Không ai muốn nộp sáng kiến! Hãy để công nhân chụp ảnh gửi Zalo hoặc điền 5 dòng giấy, còn việc chuẩn hóa số liệu là của OE.\n"
            "2. Ngâm hồ sơ thưởng Kaizen 6 tháng không trả lời khiến phong trào tắt ngấm."
        )
    },
    "Poka-Yoke": {
        "lesson_id": "L3.1",
        "definition_extra": (
            "\n• Bản chất 'Chống sai lỗi bằng thiết kế' (Shigeo Shingo): Con người dù giỏi đến đâu khi mệt mỏi vào 3 giờ sáng ca đêm cũng có lúc sơ ý! Thay vì dán tờ giấy 'Chú ý làm cẩn thận!' rồi phạt công nhân, Poka-Yoke thiết kế cơ cấu cơ khí hoặc cảm biến sao cho hoặc không thể lắp/làm sai được (Ngăn ngừa — Prevention), hoặc vừa sai là máy dừng báo còi ngay lập tức (Phát hiện — Detection).\n"
            "• 3 phương pháp thiết kế Poka-Yoke kinh điển: (1) Phương pháp Tiếp xúc (cữ định vị bất đối xứng — cắm ngược không vào), (2) Phương pháp Đếm cố định (đủ số lần/mét mới cho qua bước sau), (3) Phương pháp Trình tự bước (phải quét Barcode đúng loại nhựa rồi khóa mới mở cấp liệu)."
        ),
        "cadivi_application_extra": (
            "\n• 5 Poka-Yoke thực chiến cực kỳ hữu ích tại nhà máy CADIVI: (1) Quét Barcode bao nhựa khớp lệnh SX chống nạp nhầm PVC/XLPE/LSZH, (2) Cảm biến đứt sợi đồng & đứt băng Mica tự dừng máy trong 0.5s, (3) Cữ định vị bất đối xứng chống lắp ngược Chày–Cối, (4) Spark Tester tự đánh dấu phun sơn vị trí thủng cách điện, (5) Camera/cảm biến kiểm tra mực in phun chữ trên vỏ cáp."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Ổ cắm USB-A hay thẻ SIM điện thoại có vát 1 góc chéo — bạn không thể nào cắm ngược chiều được; máy rút tiền ATM bắt rút thẻ ra trước khi trả tiền để không bao giờ quên thẻ!\n"
            "\n• Ví dụ 2 (Poka-Yoke giảm phế tại CADIVI): Trước đây máy in phun chữ lên vỏ cáp hết mực lúc 2 giờ sáng, công nhân không để ý chạy suốt 12 km dây không có chữ CADIVI (phải tuốt bỏ hoặc đóng lại tốn hàng chục triệu!). Lắp cảm biến quang kiểm tra độ tương phản vạch chữ nối PLC tự dừng máy sau 5 mét không có chữ — chi phí chỉ 8 triệu, triệt tiêu 100% lỗi quên mực mãi mãi!"
        ),
        "common_mistakes": (
            "1. Coi 'nhắc nhở nhân viên tập trung hơn' hoặc 'thêm 1 người đứng kiểm tra 100% bằng mắt' là Poka-Yoke — kiểm tra bằng mắt chỉ bắt được khoảng 80–85% lỗi và tốn nhân công, hoàn toàn KHÔNG phải Poka-Yoke!"
        )
    },
    "Jidoka": {
        "lesson_id": "L3.1",
        "definition_extra": (
            "\n• Một trong 2 trụ cột vĩ đại của Toyota Production System (cùng với Just-In-Time): Jidoka nghĩa là 'Tự động hóa có trí tuệ con người' (Autonomation). Máy tự động bình thường khi gặp lỗi vẫn cứ chạy ầm ầm đẻ ra 1,000 sản phẩm hỏng liên tiếp; còn máy có Jidoka tự phát hiện bất thường → TỰ DỪNG NGAY LẬP TỨC → Bật đèn Andon gọi người tới xử lý tận gốc!\n"
            "• Lợi ích kép kỳ diệu: (1) Chất lượng được xây dựng ngay trong công đoạn (không truyền lỗi sang khâu sau), (2) Tách rời con người khỏi việc phải đứng 'canh chừng máy' — 1 công nhân có thể đứng 3–6 máy an toàn!"
        ),
        "cadivi_application_extra": (
            "\n• Nền tảng để triển khai mô hình 1 người đứng nhiều máy (Man-Machine Chart) tại xưởng Kéo tinh Multi-wire, xưởng Bện Buncher, xưởng Bện lưới Braiding và dây chuyền Đùn tự động tại CADIVI Miền Trung."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Lịch sử gốc Toyota): Sakichi Toyoda phát minh máy dệt tự động dừng tức thì khi đứt chỉ 1 sợi chỉ — nhờ đó 1 công nhân quản được 20 máy dệt thay vì 1 máy mà không tạo ra cả cuộn vải rách!\n"
            "\n• Ví dụ 2 (Tại CADIVI): Trang bị cảm biến đứt sợi + cảm biến rung lệch rulo + Laser Gauge vượt dung sai tự dừng máy trên cụm 4 máy bện Buncher cho phép 1 công nhân vận hành đồng thời 4 máy mà tỷ lệ phế bung sợi giảm gần về 0!"
        ),
        "common_mistakes": (
            "1. Công nhân ngại phiền khi máy tự dừng báo lỗi nên lấy băng keo dán chết cảm biến hoặc tắt chế độ tự dừng → Phá hủy hoàn toàn cơ chế Jidoka! OE phải theo dõi và xử lý nguyên nhân gốc làm máy hay dừng chứ không được tắt cảm biến."
        )
    },
    "Andon": {
        "lesson_id": "L3.4",
        "definition_extra": (
            "\n• Bản chất tín hiệu trực quan tức thời: Andon là hệ thống đèn tháp 3–4 màu (Xanh = Chạy bình thường; Vàng = Cần hỗ trợ vật tư/kiểm tra sớm nhưng máy chưa dừng; Đỏ = Máy dừng sự cố/chất lượng cần ứng cứu ngay; Trắng/Xanh dương = Đang đổi mã hoặc Bảo trì PM) kết hợp bảng LED tổng xưởng hoặc cảnh báo tự động lên điện thoại/MES.\n"
            "• Sức mạnh thực sự của Andon nằm ở văn hóa hỗ trợ kịp thời: Khi công nhân kéo dây/bấm nút Andon, cấp trên chạy xuống GIÚP xử lý trong 5 phút chứ KHÔNG phải xuống để mắng mỏ!"
        ),
        "cadivi_application_extra": (
            "\n• Triển khai tại 4 phân xưởng dài rộng của CADIVI Miền Trung (nhiều máy đùn dài 40–50m che khuất tầm nhìn): Đèn tháp Andon đặt trên cao + bảng LED treo giữa xưởng giúp Tổ trưởng, Bảo trì và Xe nâng nhìn từ xa 50 mét thấy ngay máy nào sắp hết rulo đồng hoặc đang dừng sự cố!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Đèn Vàng chống đói vật tư tại CADIVI): Quy ước khi rulo đồng xả (Pay-off) trên máy đùn chỉ còn 15% dây, công nhân bấm đèn Andon Vàng (gọi xe nâng Milk Run chở rulo mới tới đặt sẵn) → Khi rulo cũ hết, rulo mới đã nằm sẵn bên cạnh, giảm thời gian chờ xe nâng từ 12 phút về 0 phút!\n"
            "\n• Ví dụ 2 (Đèn Đỏ gắn Escalation Matrix): Máy đùn báo Đỏ quá 5 phút tự gửi tin nhắn Zalo/MES cho Tổ trưởng, quá 15 phút tự báo Kỹ thuật Cơ Điện & Quản đốc → Rút ngắn MTTR phản ứng sự cố hơn 60%!"
        ),
        "common_mistakes": (
            "1. Lắp đèn Andon đỏ rực cả xưởng nhưng chẳng ai chạy tới xử lý trong 30 phút (thiếu Escalation Matrix SLA) → Đèn Andon biến thành 'đèn trang trí Giáng Sinh' vô dụng!"
        )
    },
    "Kanban": {
        "lesson_id": "L3.2",
        "definition_extra": (
            "\n• Bản chất 'tấm thẻ điều độ tự động' (tiếng Nhật: Biển hiệu): Thay vì phòng Kế hoạch phải chạy xuống từng xưởng hò hét 'chạy thêm 5 rulo VC 2.5 đi!', Kanban dùng tín hiệu vật lý (thẻ kẹp rulo, ô kẻ vạch vàng trên sàn, thùng rỗng, hoặc e-Kanban trên màn hình) để tự động kích hoạt sản xuất/cấp hàng đúng số lượng khi và chỉ khi khâu sau đã dùng bớt.\n"
            "• Công thức tính số lượng thẻ Kanban tối ưu (giới hạn tồn kho WIP chuẩn): `N = [ D × L × (1 + SF) ] / C` (trong đó D = nhu cầu/ngày, L = Lead Time bổ sung, SF = hệ số an toàn 10–20%, C = sức chứa 1 rulo/thùng)."
        ),
        "cadivi_application_extra": (
            "\n• Rất phù hợp tại CADIVI Miền Trung cho: (1) Điều tiết rulo bán thành phẩm giữa Xưởng Kéo ↔ Xưởng Bện ↔ Xưởng Đùn đối với các cỡ dây dân dụng sản lượng đều (VC 1.5, 2.5, 4.0 mm²), (2) Cấp phát phụ kiện đóng gói, tem nhãn, bao bì, hạt màu Masterbatch bằng Two-Bin Kanban."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tính số ô sàn Kanban giữa Xưởng Bện và Đùn dây VC 2.5): Xưởng Đùn tiêu thụ D = 16 rulo/ngày; thời gian Bện bổ sung L = 0.5 ngày; hệ số an toàn SF = 0.25 (25%); mỗi ô chứa C = 1 rulo → Số ô Kanban = [16 × 0.5 × 1.25] / 1 = 10 ô sơn vàng trên sàn! Cứ trống 3 ô là Xưởng Bện tự chạy bù 3 rulo; đủ 10 ô thì dừng chuyển mã khác!\n"
            "\n• Ví dụ 2 (Trực quan đời sống): Ngăn đựng lon nước trong tủ lạnh mini — khi bạn lấy uống hết 4 lon thấy đáy khay trống mới đi mua đúng 1 lốc 6 lon bổ sung thay vì chất đầy 5 thùng ngoài phòng khách."
        ),
        "common_mistakes": (
            "1. Áp dụng Kanban siêu thị cứng nhắc cho các mã cáp dự án đặc thù 1 năm mới đặt 1 lần (nhóm Z — MTO) → Gây tồn kho chết hàng trăm triệu đồng! Kanban siêu thị chỉ dùng cho mã hàng tiêu thụ đều đặn (nhóm X/Y)."
        )
    },
    "Pull System": {
        "lesson_id": "L3.2",
        "definition_extra": (
            "\n• Khác biệt cốt lõi về dòng thông tin & dòng tiền: Trong mô hình Đẩy (Push), phòng Kế hoạch phát lệnh độc lập xuống cả 4 phân xưởng cùng lúc dựa trên dự báo — nếu Xưởng Đùn bị hỏng máy 1 ngày thì Xưởng Kéo & Bện vẫn cứ chạy đẩy tiếp hàng chục rulo dồn cục kín lối đi. Trong mô hình Kéo (Pull), chỉ phát lệnh chính ở điểm chốt (Pacemaker — thường là Xưởng Đùn/Hoàn thiện) rồi kéo ngược về phía trước qua Kanban/WIP Cap.\n"
            "• Chọn điểm tách Push–Pull (Decoupling Point) thông minh: Với dây dân dụng VC/CV bán đại trà → Siêu thị thành phẩm kéo theo tồn kho Min/Max (MTS Pull); với cáp lực dự án đặt riêng theo chiều dài → Kéo theo đơn hàng từ kho đồng/bán thành phẩm chuẩn (ATO/MTO Pull)."
        ),
        "cadivi_application_extra": (
            "\n• Giúp Ban Giám đốc CADIVI Miền Trung giải phóng hàng tỷ đồng vốn lưu động đang 'nằm ngủ' dưới dạng rulo đồng bán thành phẩm chất cao giữa các xưởng, đồng thời rút ngắn mạnh thời gian giao hàng."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Quán cơm bình dân nấu sẵn một núi món từ sáng sớm rồi đẩy ra bán (Push — chiều ế phải bỏ) vs Nhà hàng nấu tươi ngay khi khách gọi món trên nguyên liệu đã sơ chế sẵn (Pull — luôn nóng ngon, không thừa phế!).\n"
            "\n• Ví dụ 2 (Tại CADIVI): Thiết lập giới hạn trần WIP tối đa (CONWIP = 18 rulo) giữa khu Kéo tinh và khu Bện dây dân dụng giúp giảm 45% diện tích chiếm dụng sàn và giảm 100% lỗi rulo đồng để lâu bị đen oxy hóa trước khi kịp đưa vào bện!"
        ),
        "common_mistakes": (
            "1. Cố ép áp dụng Pull 100% khi thời gian đổi mã SMED còn mất 60 phút và máy đùn hay hỏng vặt — Pull sẽ làm xưởng bị đứt hàng liên tục! Phải làm song song SMED + TPM để dòng chảy đủ tin cậy rồi mới kéo mượt được."
        )
    },
    "Two-Bin Kanban": {
        "lesson_id": "L5.1",
        "definition_extra": (
            "\n• Hệ thống kiểm soát tồn kho đơn giản và thông minh nhất thế giới cho vật tư nhóm C (giá trị nhỏ nhưng tiêu thụ liên tục): Đặt đúng 2 thùng giống hệt nhau tại vị trí làm việc — công nhân chỉ lấy dùng ở Thùng 1 (đặt phía trước). Khi Thùng 1 vừa hết sạch, công nhân kéo Thùng 2 lên dùng ngay (lượng hàng trong Thùng 2 được tính đủ dùng trong suốt Lead Time chờ kho cấp mới + Safety Stock), đồng thời bỏ Thùng 1 rỗng (có gắn sẵn mã thẻ vật tư) ra khay thu hồi để xe Milk Run tự động mang về kho cấp đầy!"
        ),
        "cadivi_application_extra": (
            "\n• Áp dụng tức thì trong 1 tuần đầu tại CADIVI Miền Trung cho toàn bộ vật tư phụ dễ thất thoát hoặc hay gây dừng máy bất ngờ: tem nhãn cuộn dây, màng co PVC, đầu bịt chống ẩm cáp, băng keo, túi chống ẩm, găng tay bảo hộ, lưới lọc Screen Pack, mực in phun và dung môi rửa đầu phun."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Bạn mua sẵn 2 bình nước lọc 20 lít ở nhà — bình 1 uống hết thì lắp bình 2 lên dùng ngay và gọi đại lý giao đúng 1 bình mới bổ sung, không bao giờ khát nước giữa đêm mà cũng không chất 10 bình chật nhà!\n"
            "\n• Ví dụ 2 (Tại Tổ Đóng cuộn CADIVI): Tổ tiêu thụ trung bình 1,000 tem nhãn/ngày, kho in bổ sung mất 2 ngày, cộng đệm 1 ngày = 3,000 tem/thùng → Đặt 2 khay mỗi khay 3,000 tem ngay bàn dán tem giúp chấm dứt hoàn toàn cảnh công nhân phải dừng đóng gói chạy sang kho xin tem và xóa sạch việc ghi phiếu lĩnh vật tư lặt vặt mỗi ngày!"
        ),
        "common_mistakes": (
            "1. Công nhân bốc đồng thời cả 2 thùng cùng lúc (không rút hết Thùng 1 rồi mới đụng Thùng 2) → Phá vỡ tín hiệu đặt hàng lại! Cần dán vạch đỏ hoặc xếp 2 thùng trước–sau trên giá trượt nghiêng FIFO."
        )
    },
    "Heijunka": {
        "lesson_id": "L5.1",
        "definition_extra": (
            "\n• Bản chất 'Triệt tiêu sự thất thường Mura': Trong nhiều nhà máy, 20 ngày đầu tháng xưởng chạy túc tắc 60% công suất rồi 10 ngày cuối tháng chạy tăng ca điên cuồng 130% để kịp chốt doanh số tháng → Kết quả: máy quá tải hỏng hóc, công nhân mệt mỏi tạo phế phẩm, tiền phụ cấp tăng ca vọt gấp đôi! Heijunka san phẳng cả Sản lượng (Volume Leveling) lẫn Chủng loại mã hàng (Mix Leveling) đều đặn theo từng tuần/ngày bằng hộp Heijunka Box hoặc Bánh xe sản xuất (Product Wheel)."
        ),
        "cadivi_application_extra": (
            "\n• Phối hợp giữa OE – Phòng Kinh doanh – Phòng Kế hoạch tại CADIVI Miền Trung: Phân tách rõ đơn hàng tiêu chuẩn đều (chạy theo Bánh xe sản xuất cố định từng tuần: Thứ 2–3 chạy VC 1.5–2.5, Thứ 4–5 chạy VC 4.0–6.0, Thứ 6 chạy CVV...) với phần công suất đệm (15–20%) dành riêng cho đơn hàng dự án đột xuất!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Con rùa đi đều đặn mỗi giờ 5 km sẽ về đích ổn định và ít tốn sức hơn con thỏ nằm ngủ nửa ngày rồi chạy nước rút kiệt sức hụt hơi!\n"
            "\n• Ví dụ 2 (Tại CADIVI): Chuyển lịch chạy dây dân dụng 5 tiết diện từ chạy dồn cục mỗi tháng 1 lần (tồn kho đỉnh điểm 3 tuần bán hàng) sang chu kỳ Bánh xe sản xuất lặp lại mỗi tuần (nhờ SMED đã rút đổi mã còn 12p) giúp giảm 58% tồn kho thành phẩm và cắt 40% giờ tăng ca cuối tháng!"
        ),
        "common_mistakes": (
            "1. Áp dụng san phẳng đổi mã liên tục mỗi ngày khi chưa làm SMED → Số lần chuyển đổi tăng gấp 4 lần làm sụp đổ OEE! SMED luôn là điều kiện tiên quyết để thực hiện Heijunka thành công."
        )
    },
    "Campaign Scheduling": {
        "lesson_id": "L3.3",
        "definition_extra": (
            "\n• Bản chất tối ưu hóa đặc thù ngành công nghiệp quá trình (cáp điện, nhựa, hóa chất, sơn): Thay vì chạy lộn xộn theo thứ tự đơn hàng ai gọi trước chạy trước (sáng chạy PVC đen → trưa chạy XLPE trắng → chiều quay lại PVC đỏ), Campaign Scheduling gom các lệnh sản xuất có cùng gốc polymer, tiết diện gần nhau và xếp chuỗi màu Sáng → Tối thành một 'chiến dịch liên hoàn' tối ưu chi phí chuyển đổi.\n"
            "• Thiết kế Ma trận thời gian chuyển đổi (Changeover Matrix): Lập bảng vuông `N × N` thể hiện chính xác số phút dừng & số kg nhựa xả khi đổi từ Họ A sang Họ B để làm đầu vào cho Kế hoạch xếp lịch tối ưu!"
        ),
        "cadivi_application_extra": (
            "\n• Giải pháp tạo hiệu quả tài chính nhanh nhất cho OE CADIVI Miền Trung (làm được ngay tháng thứ 1–2 mà không cần mua sắm thiết bị) bằng cách chuẩn hóa quy tắc lập lịch tuần cùng Phòng Kế hoạch & Xưởng Đùn."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Ma trận chuyển đổi xưởng Đùn): Đổi PVC Trắng → Đen mất 10p / 4 kg purge; Đổi ngược Đen → Trắng mất 45p / 24 kg purge; Đổi PVC ↔ XLPE mất 90p tháo rửa trục vít! Xếp Campaign 1 chiều giúp tiết kiệm ngay 80% tổn thất chuyển đổi.\n"
            "\n• Ví dụ 2 (Gom đơn cáp Solar/LSZH tại CADIVI): Nhựa LSZH và XLPO Solar đắt gấp 2.5–3 lần PVC thường — gom toàn bộ đơn hàng cáp LSZH trong tuần chạy nối đuôi liên tục trong 2 ngày cố định giúp cắt giảm 60% phế nhựa chuyển đổi so với chạy rải rác từng đơn nhỏ!"
        ),
        "common_mistakes": (
            "1. Gom chiến dịch quá dài (vd: gom 1 tháng mới chạy màu Trắng 1 lần) khiến khách hàng phải chờ quá lâu hoặc kho phải trữ quá nhiều tồn kho → Phải cân bằng chu kỳ Campaign theo nguyên tắc Product Wheel (thường 1–2 tuần/vòng)."
        )
    },
    "WIP": {
        "lesson_id": "L3.2",
        "definition_extra": (
            "\n• Bản chất 'Con dao hai lưỡi' của Tồn kho Bán thành phẩm (Work-In-Process): Một lượng WIP Buffer nhỏ và có kiểm soát trước điểm nghẽn (DBR) là cần thiết để máy cổ chai không bị đói hàng; nhưng núi WIP khổng lồ nằm la liệt giữa các xưởng lại là kẻ thù số 1 vì: (1) Chôn hàng chục tỷ đồng tiền mặt mua đồng/nhựa, (2) Kéo dài Lead Time theo Định luật Little (`LT = WIP / Throughput`), (3) Che giấu lỗi chất lượng (kéo lỗi 20 rulo đồng rồi 4 ngày sau đùn mới phát hiện!), (4) Gây đen oxy hóa sợi đồng trần và cản trở đường xe nâng."
        ),
        "cadivi_application_extra": (
            "\n• Theo dõi chỉ số Số ngày tồn WIP (`WIP Days = Tổng tấn WIP trên sàn / Sản lượng tấn mỗi ngày`) ngay tại 4 xưởng CADIVI Miền Trung: mục tiêu đưa WIP từ 8–10 ngày xuống còn 2–3 ngày bán thành phẩm sạch gọn trong đúng các ô vạch sàn."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Đường cao tốc có quá nhiều xe cùng đổ vào (WIP quá cao) thì tốc độ cả đoàn giảm về 10 km/h và thời gian về nhà tăng gấp 4 lần; kiểm soát đèn vào cao tốc giữ lượng xe vừa phải thì ai cũng về nhà cực nhanh!\n"
            "\n• Ví dụ 2 (Chi phí tài chính của WIP tại CADIVI): Giảm lượng rulo đồng bán thành phẩm nằm chờ trên sàn từ 90 tấn xuống 45 tấn (với giá đồng ~250 triệu/tấn) giúp giải phóng ngay 11.25 tỷ VNĐ vốn lưu động (tiết kiệm ~900 triệu tiền lãi vay/năm ở lãi suất 8%) + giải phóng hơn 200 m² mặt bằng xưởng!"
        ),
        "common_mistakes": (
            "1. Cho các công đoạn đầu (Kéo thô RBD, Bện) chạy liên tục cho 'đẹp chỉ số OEE cá nhân' dù xưởng Đùn phía sau đã chất đầy rulo không nhận kịp — tạo ra núi WIP giả tạo!"
        )
    },
    "Genba": {
        "lesson_id": "L8.1",
        "definition_extra": (
            "\n• Triết lý '3 Thực' (San-Gen-Shugi) của Nhật Bản — kim chỉ nam sống còn của Chuyên viên OE:\n"
            "  1. Genba (Hiện trường thực tế): Nơi giá trị thực sự được tạo ra (dưới xưởng Kéo, Bện, Đùn, Đóng gói — KHÔNG phải phòng họp hay màn hình Excel!).\n"
            "  2. Genbutsu (Hiện vật thực tế): Cầm tận tay sợi đồng đứt soi kính lúp, cầm mảnh vỏ cáp bị sần, đo tận mắt chiếc rulo bị méo bích.\n"
            "  3. Genjitsu (Sự thật & Dữ liệu thực tế): Kiểm chứng bằng con số thực đo tại chỗ chứ không tin vào lời truyền miệng 'chắc là do nhựa ẩm'!\n"
            "• Nguyên tắc Genba Walk hiệu quả: Xuống xưởng với tâm thế Hỏi mở – Lắng nghe – Tôn trọng công nhân, KHÔNG xuống để 'bắt lỗi cảnh sát'!"
        ),
        "cadivi_application_extra": (
            "\n• Ghi rõ trong yêu cầu JD CADIVI: Làm việc On-site 100% bám sát hiện trường tại KCN Hòa Cầm. Kỹ sư OE xuất sắc dành ít nhất 40–50% thời gian mỗi ngày ở dưới xưởng (kể cả định kỳ khảo sát Ca 2 & Ca 3 ban đêm để thấy các vấn đề thật không bao giờ lộ ra vào ca hành chính!)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Bác sĩ giỏi không bao giờ chỉ đọc tin nhắn mô tả rồi kê đơn mà phải trực tiếp khám mạch, nghe phổi và xem phim X-quang của bệnh nhân.\n"
            "\n• Ví dụ 2 (Giá trị của đi Genba ca đêm tại CADIVI): Sổ báo cáo ngày nào cũng ghi Ca 3 đạt tốc độ chậm hơn Ca 1 tới 15% vì 'máy yếu'. OE trực tiếp ở lại đi Genba lúc 01:00 sáng phát hiện thực tế tổ trưởng Ca 3 thiếu xe nâng trực đêm nên công nhân phải tự đẩy tay rulo và chờ người đi lấy hạt nhựa mất 40 phút/ca — giải quyết chỉ bằng bố trí chuẩn bị sẵn vật tư trước giờ giao ca!"
        ),
        "common_mistakes": (
            "1. Đi Genba theo kiểu 'cưỡi ngựa xem hoa' đi lướt qua lối đi chính 5 phút không dừng lại quan sát quá trình thật (Taiichi Ohno Circle: đứng yên quan sát 1 máy trọn vẹn 30 phút sẽ thấy hàng chục lãng phí!)."
        )
    },
    "Spaghetti": {
        "lesson_id": "L3.2",
        "definition_extra": (
            "\n• Bản chất trực quan gây 'sốc nhận thức': Dùng bút màu vẽ từng đường di chuyển thực tế của công nhân, xe nâng/rulo vật tư, hoặc phiếu chứng từ lên bản vẽ mặt bằng xưởng AutoCAD trong 1 chu kỳ sản xuất. Nếu mặt bằng bố trí kém, các nét vẽ sẽ đan chéo chồng chéo hệt như một đĩa mì Ý (Spaghetti) — giúp mọi người nhìn 1 giây thấy ngay hàng trăm mét đi bộ và vận chuyển thừa thãi (Muda Transportation & Motion)!\n"
            "• Luôn đi kèm số liệu đo tổng chiều dài (mét/ca hoặc km/tháng) Trước vs Sau cải tiến Layout."
        ),
        "cadivi_application_extra": (
            "\n• Áp dụng cho 2 cấp độ tại CADIVI Miền Trung: (1) Cấp Toàn Nhà Máy (đo đường đi xe nâng chở rulo từ Kho đồng → Kéo → Ủ → Bện → Đùn → Lab → Kho thành phẩm), (2) Cấp Trạm Làm Việc (đo bước chân công nhân khi đổi khuôn SMED máy đùn hoặc đóng cuộn khoanh 100m)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Vẽ đường đi lại trong căn bếp có tủ lạnh đặt tận phòng khách còn bếp nấu ở cuối nhà — chỉ nấu 1 bữa tối mà đi bộ hết 800 mét!\n"
            "\n• Ví dụ 2 (Tại máy đùn CADIVI): Vẽ Spaghetti quá trình đổi mã 55 phút của 2 công nhân phát hiện họ đi bộ qua lại giữa máy đùn – tủ dụng cụ – kho đầu khuôn – bảng cân tổng cộng 640 mét (tốn 11 phút đi bộ vô ích!). Gom xe đẩy SMED + tủ sấy đầu khuôn đặt cách đầu đùn 2 mét rút quãng đường đi bộ xuống còn 95 mét (-85%)!"
        ),
        "common_mistakes": (
            "1. Chỉ vẽ đường đi bằng nét nguệch ngoạc cảm tính mà không đếm số lượt đi qua từng đoạn và không tính ra tổng số mét/ngày & giờ công tiết kiệm được để thuyết phục duyệt chi phí di dời!"
        )
    },
    "Shojinka": {
        "lesson_id": "L2.4",
        "definition_extra": (
            "\n• Bản chất 'Linh hoạt hóa nhân lực theo biến động cầu thị trường' (tiếng Nhật: Linh hoạt số người): Khác với dây chuyền cứng nhắc lúc nào cũng bắt buộc 6 người dù đơn hàng giảm một nửa (khiến chi phí nhân công/sản phẩm tăng gấp đôi!), Shojinka kết hợp Layout chữ U + Công nhân đa kỹ năng (Skill Matrix / TWI) + Standard Work linh hoạt để khi nhu cầu cao thì bố trí 5 người (Takt 20s), khi nhu cầu thấp mùa vắng đơn thì thu gọn mượt mà về 3 người (Takt 33s) mà mỗi người vẫn đạt hiệu suất OLE cao!"
        ),
        "cadivi_application_extra": (
            "\n• Rất thiết thực cho đặc thù mùa vụ xây dựng của CADIVI Miền Trung (quý 3–4 đơn hàng dự án & dân dụng bùng nổ, sau Tết âm lịch đơn hàng thường chậm lại): dùng Ma trận đa kỹ năng công nhân để linh hoạt điều chuyển giữa Kéo – Bện – Đóng cuộn theo đúng tải RCCP từng tháng!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Quầy thu ngân siêu thị giờ thấp điểm mở 2 quầy (3 nhân viên khác quay vào xếp hàng lên kệ), đến giờ tan tầm đông khách lập tức mở đủ 6 quầy trong 1 phút!\n"
            "\n• Ví dụ 2 (Tại Tổ Đóng cuộn CADIVI): Thiết kế chuyền đóng gói chữ U kèm 3 kịch bản Standard Work chuẩn cho 3 người (600 cuộn/ca), 4 người (850 cuộn/ca) và 5 người (1,100 cuộn/ca) — giúp điều tiết linh hoạt nhân sự theo đúng sản lượng máy đùn từng ngày mà không bao giờ thừa người ngồi chơi!"
        ),
        "common_mistakes": (
            "1. Không đào tạo chéo kỹ năng (Ma trận Skill Matrix chỉ có đúng 1 người biết chạy máy đùn XLPE hoặc máy bện Rigid) — chỉ cần người đó nghỉ ốm 2 ngày là cả dây chuyền tê liệt!"
        )
    },
    "Water Spider": {
        "lesson_id": "L3.2",
        "definition_extra": (
            "\n• Bản chất 'Chuyên môn hóa người tiếp liệu' (tiếng Nhật: Mizusumashi — Con nhện nước chạy lướt linh hoạt trên mặt hồ): Công nhân đứng máy có tay nghề cao sinh ra để vận hành thiết bị tạo giá trị, KHÔNG phải để dừng máy đi tìm rulo, khuân bao nhựa, lấy tem hay dọn phế liệu! Water Spider là nhân sự tiếp liệu chuyên trách chạy theo tuyến chuẩn định kỳ (Milk Run) cấp đủ nguyên liệu, rulo trống, bộ khuôn SMED tận tay công nhân đứng máy và thu hồi thành phẩm/phế liệu về kho."
        ),
        "cadivi_application_extra": (
            "\n• Cực kỳ phù hợp với quy mô 4 phân xưởng CADIVI Miền Trung: 1–2 nhân sự Water Spider (kết hợp xe nâng/xe kéo rulo) phục vụ cả cụm 6 máy đùn hoặc 8 máy bện giúp giữ chân công nhân kỹ thuật đứng máy 100% thời gian, tăng mạnh cả OEE lẫn OLE!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Trong phòng mổ bệnh viện, bác sĩ phẫu thuật chính (công nhân đứng máy) không bao giờ tự chạy ra kho lấy dao mổ hay bông băng — y tá phụ mổ (Water Spider) đưa sẵn đúng dụng cụ ngay tích tắc cần dùng!\n"
            "\n• Ví dụ 2 (Tính toán tại Xưởng Đùn CADIVI): Trước đây 6 thợ máy đùn mỗi ca đều bỏ máy đi lấy hạt nhựa, màu Masterbatch và tìm rulo trống mất trung bình 35 phút/người (tổng 210 phút công kỹ thuật & 120 phút dừng máy!). Bố trí 1 nhân viên Water Spider chạy tuyến Milk Run mỗi 45 phút giúp tăng sản lượng cả 6 máy đùn thêm +8.5%, giá trị tạo thêm lớn gấp 6 lần tiền lương 1 nhân sự tiếp liệu!"
        ),
        "common_mistakes": (
            "1. Biến Water Spider thành 'nhân viên sai vặt chạy loạn xạ' ai gọi đâu chạy đó (chữa cháy) thay vì chạy theo lịch tuyến chuẩn (Standard Work Milk Run) kết hợp tín hiệu Kanban/đèn Andon Vàng!"
        )
    },
    "Ergonomics": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất 'Thiết kế công việc vừa vặn với cơ thể con người' (Nhân trắc học): Khi công nhân phải cúi gập lưng liên tục, với tay quá vai, xoay vặn cột sống hay bê vật nặng 25 kg hàng trăm lần mỗi ca, năng suất buổi chiều (14:00–17:00) sẽ sụt 20–30% do mệt mỏi và tỷ lệ lỗi chất lượng/chấn thương tăng vọt!\n"
            "• 3 nguyên tắc vàng Ergonomics tại trạm làm việc: (1) Vùng thao tác Vàng (Golden Zone — ngang tầm khuỷu tay đến ngực, bán kính với tay ≤ 40 cm), (2) Không cúi nâng vật > 15 kg từ sát sàn (dùng bàn nâng thủy lực / palăng cẩu rulo), (3) Chiếu sáng đủ chuẩn (≥ 300–500 Lux tại điểm kiểm tra vỏ cáp) & thảm chống mỏi chân khi đứng lâu."
        ),
        "cadivi_application_extra": (
            "\n• Quick-Win lấy trọn trái tim công nhân xưởng CADIVI (tạo bước Desire trong ADKAR!): Cải thiện điều kiện làm việc ở khu xếp cuộn dây dân dụng 15–25 kg, khu cấp bao hạt nhựa 25 kg lên phễu máy đùn (thay leo thang đổ tay bằng máy hút chân không tự động), khu thao tác tháo lắp đầu đùn nặng."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Kê màn hình laptop lên đúng tầm mắt và đặt ghế vừa chiều cao bàn giúp bạn làm việc 8 tiếng không đau cổ vai gáy.\n"
            "\n• Ví dụ 2 (Tại Xưởng Đùn CADIVI): Trước đây công nhân phải vác bao nhựa 25 kg leo 5 bậc thang đổ vào phễu trên cao 25 lần/ca (mất 50 phút & cực kỳ nguy hiểm trượt ngã). Lắp phễu hút chân không tự động đặt ngay mặt sàn giúp công nhân chỉ cắt miệng bao ở tầm hông — vừa xóa 100% rủi ro tai nạn vừa giảm 40 phút công/ca!"
        ),
        "common_mistakes": (
            "1. Cố tăng năng suất bằng cách ép công nhân thao tác trong tư thế gò bó bất tự nhiên — có thể nhanh hơn 1 tuần đầu nhưng tháng sau công nhân đau lưng xin nghỉ việc hàng loạt!"
        )
    },
    "TWI": {
        "lesson_id": "L2.4",
        "definition_extra": (
            "\n• Bản chất hệ thống đào tạo nghề tại hiện trường kinh điển (Training Within Industry — nền móng của Toyota từ thập niên 1950), gồm 3 học phần cốt lõi:\n"
            "  1. JI (Job Instruction — Hướng dẫn công việc 4 bước): Chuẩn bị tâm lý người học → Trình bày & giải thích rõ 'Bước chính – Điểm mấu chốt (Key Points) – Lý do Tại sao' → Cho người học làm thử và đọc lại điểm mấu chốt → Theo dõi kèm cặp giảm dần.\n"
            "  2. JM (Job Methods — Cải tiến phương pháp): Đặt câu hỏi 5W1H để loại bỏ, gộp, đổi thứ tự, đơn giản hóa thao tác.\n"
            "  3. JR (Job Relations — Quan hệ con người): Cách xử lý xung đột và xây dựng lòng tin giữa Tổ trưởng và công nhân.\n"
            "• Châm ngôn bất hủ của TWI-JI: 'Nếu người học chưa học được, thì người dạy chưa dạy tốt!'"
        ),
        "cadivi_application_extra": (
            "\n• Giải quyết căn bệnh 'thợ cũ dạy thợ mới bằng cách đứng nhìn rồi tự mò' tại CADIVI Miền Trung — dùng phiếu phân rã công việc JBS (Job Breakdown Sheet) và Ma trận Kỹ năng (Skill Matrix 4 mức L1–L4) rút ngắn 50% thời gian đào tạo công nhân mới đứng máy kéo/bện/đùn!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Khi dạy buộc nút dây an toàn, chỉ làm nhanh cho xem 1 lần rồi bảo 'làm đi' thì người học sẽ quên ngay; nhưng tách thành 3 Bước chính + giải thích TẠI SAO phải luồn vòng thứ hai để không tuột rồi cho họ tự làm lại 3 lần thì nhớ suốt đời!\n"
            "\n• Ví dụ 2 (Đào tạo hàn nối sợi đồng Butt Welder tại CADIVI): Lập bảng JBS TWI-JI nêu rõ 4 bước & 3 điểm mấu chốt (cắt mặt đầu vuông 90° → kẹp đồng tâm → bắt buộc bấm nút ủ lại mối hàn 3 giây để chống giòn) giúp giảm 75% lỗi đứt mối hàn (Weld Break) ở công nhân mới vào nghề!"
        ),
        "common_mistakes": (
            "1. Giao hết việc đào tạo công nhân mới cho công nhân lâu năm nhưng không có bảng chuẩn JBS — thợ cũ truyền lại luôn cả những 'thói quen làm tắt' sai quy trình của họ!"
        )
    },
    "SOP": {
        "lesson_id": "L3.1",
        "definition_extra": (
            "\n• Bản chất 'Sổ tay hướng dẫn chuẩn hóa thao tác': SOP (Standard Operating Procedure) mô tả rõ ràng, không mơ hồ từng bước thực hiện 1 công việc từ chuẩn bị an toàn, cài đặt máy, kiểm tra chất lượng đến xử lý sự cố. Trong nhà máy Lean hiện đại, xu hướng chuyển từ SOP toàn chữ dài 15 trang sang Visual SOP & OPL (One-Point Lesson — Bài học 1 điểm chỉ dài đúng 1 trang A4 có 70% hình ảnh chụp thật mũi tên Đỏ/Xanh và 30% chữ ngắn gọn) treo ngay tại máy!"
        ),
        "cadivi_application_extra": (
            "\n• Chuẩn hóa tài liệu sau mọi dự án cải tiến của OE CADIVI: SOP đổi màu SMED máy đùn, OPL kiểm tra mẫu lỗ kim đầu ca trên Spark Tester, OPL phân loại 3 thùng phế đồng/nhựa, OPL vệ sinh mắt đọc Laser Gauge và OPL 6 bước LOTO."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Tờ hướng dẫn thoát hiểm bằng hình vẽ minh họa đặt sau ghế máy bay — không cần đọc 10 trang chữ, nhìn 10 giây ai cũng hiểu ngay cách đeo mặt nạ dưỡng khí!\n"
            "\n• Ví dụ 2 (Tại CADIVI): Chuyển quy trình khởi động máy đùn XLPE từ văn bản Word 12 trang cất trong tủ văn phòng thành 2 tờ Visual SOP ép plastic dán ngay bên cạnh màn hình HMI (có hình chụp rõ đồng hồ nhiệt, nút xả purge, vạch kiểm tra đầu đùn) → Tỷ lệ làm đúng trình tự ở ca đêm tăng từ 68% lên 96%!"
        ),
        "common_mistakes": (
            "1. Viết SOP bằng những câu chung chung như 'Vặn chặt vừa tay', 'Sấy nhựa cho đến khi khô' — SOP chuẩn phải có con số đo lường cụ thể: 'Siết lực 25 N·m', 'Sấy 75°C trong 3 giờ, độ ẩm ≤ 0.05%'!"
        )
    },
    "TIMWOOD": {
        "lesson_id": "L3.1",
        "definition_extra": (
            "\n• 8 Loại Lãng Phí Kinh Điển (TIMWOODS — mở rộng từ 7 Muda của Toyota thêm chữ S thứ 8):\n"
            "  1. T — Transportation (Vận chuyển thừa): Xe nâng chở rulo chạy vòng vèo giữa các xưởng.\n"
            "  2. I — Inventory (Tồn kho thừa): Núi rulo đồng/nhựa nằm chờ quá mức gây chôn vốn.\n"
            "  3. M — Motion (Thao tác/Đi lại thừa của người): Công nhân cúi với, đi tìm dụng cụ/đầu cối.\n"
            "  4. W — Waiting (Chờ đợi): Máy chờ rulo, người chờ máy/chờ Bảo trì/chờ Lab duyệt mẫu.\n"
            "  5. O — Overproduction (Sản xuất thừa — NGUY HIỂM NHẤT vì đẻ ra 6 lãng phí kia!): Chạy dư mã dây chưa có đơn để lấy OEE cao.\n"
            "  6. O — Overprocessing (Gia công thừa): Bọc nhựa dày hơn tiêu chuẩn (Over-thickness), kéo đồng to hơn chuẩn (Copper Give-away), nhập cùng 1 số liệu 3 lần vào 3 sổ khác nhau!\n"
            "  7. D — Defects (Phế phẩm & Sửa lỗi): Thủng Spark, đứt sợi, phế đồng dính nhựa, cắt mẩu thừa.\n"
            "  8. S — Skills Unused (Lãng phí trí tuệ con người): Không lắng nghe sáng kiến Kaizen từ chính thợ đứng máy 10 năm kinh nghiệm!"
        ),
        "cadivi_application_extra": (
            "\n• Dùng bảng kiểm 8 Lãng phí TIMWOODS làm 'kính lúp' mỗi khi đi Genba Walk ở CADIVI Miền Trung: đi 1 vòng xưởng Kéo/Bện/Đùn/Đóng gói luôn mang theo tờ giấy ghi chép đủ 8 ô để bắt tại trận mọi lãng phí ẩn!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Overprocessing đặc thù CADIVI): Đùn lớp vỏ PVC dày 1.32 mm trong khi tiêu chuẩn IEC chỉ cần tối thiểu 1.07 mm — khách hàng KHÔNG trả thêm 1 xu nào cho 0.25 mm nhựa bọc thừa đó, mỗi năm nhà máy 'tặng miễn phí' hơn 2 tỷ đồng tiền nhựa!\n"
            "\n• Ví dụ 2 (Waiting & Motion): Tổ trưởng ghi sổ giấy, cuối ca gõ lại lên Excel, sáng hôm sau kế hoạch lại gõ tiếp lên ERP (Overprocessing + Waiting) → Tự động hóa Power Query/MES xóa sạch 3 bước nhập trùng!"
        ),
        "common_mistakes": (
            "1. Quên mất lãng phí thứ 6 (Overprocessing — làm thừa hơn yêu cầu như Copper Give-away / Over-thickness) và thứ 5 (Overproduction — chạy thừa mã chưa cần) trong khi đây mới là 2 kẻ ăn mòn lợi nhuận lớn nhất của nhà máy dây cáp điện!"
        )
    },
    "One-Piece Flow": {
        "lesson_id": "L3.2",
        "definition_extra": (
            "\n• Bản chất 'Dòng chảy 1 sản phẩm' vs 'Sản xuất theo lô lớn (Batch & Queue)': Thay vì Trạm 1 đóng xong cả 100 cuộn chất đống lên pallet rồi mới đẩy sang Trạm 2 dán tem (mất rất lâu mới ra được cuộn đầu tiên, nếu Trạm 1 làm sai thì hỏng luôn cả 100 cuộn!), One-Piece Flow chuyển từng 1 cuộn (hoặc 1 lô cực nhỏ) chảy liên tục qua từng bước nối tiếp — sản phẩm đầu tiên hoàn thiện cực nhanh, phát hiện lỗi ngay ở cuộn số 1 và tồn kho WIP giữa các trạm bằng 0!"
        ),
        "cadivi_application_extra": (
            "\n• Áp dụng trực tiếp tại Tổ Đóng cuộn khoanh 100m dây dân dụng (Cuộn dây → Tự động chuyển băng tải sang Dán tem → Qua buồng co màng nhiệt → Xếp thùng luôn trong 1 dòng liên tục) và các dây chuyền liên hoàn Tandem (Kéo tinh + Ủ liên tục + Đùn cách điện liền tuyến) tại CADIVI."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan — Thí nghiệm Gấp phong bì kinh điển): Gấp 10 lá thư, cho vào 10 phong bì, dán 10 tem (mỗi bước 5s). Làm kiểu Batch: phải chờ tới giây thứ 105 mới xong lá thư đầu tiên! Làm kiểu One-Piece Flow (3 người chuyền tay từng lá): ngay giây thứ 15 đã hoàn thiện lá thư đầu tiên (Lead Time ngắn hơn 7 lần!) và nếu phong bì bị rách sẽ phát hiện ngay ở lá số 1!\n"
            "\n• Ví dụ 2 (Tại Tổ Đóng gói CADIVI): Nối máy cuộn khoanh trực tiếp với băng tải máy co màng (One-Piece Flow) giúp giảm tồn kho dây chờ co màng từ 400 cuộn xuống còn 3 cuộn và giảm ngay 2 thao tác bê lên–đặt xuống!"
        ),
        "common_mistakes": (
            "1. Áp dụng cứng nhắc One-Piece Flow (lô = 1 cuộn) cho máy đùn cáp khi đổi mã vẫn mất 40 phút — với công đoạn có Setup lớn, phải áp dụng lô nhỏ tối ưu (Small Batch Flow) kết hợp SMED chứ không thể đổi mã sau mỗi 1 cuộn!"
        )
    },
    "FIFO": {
        "lesson_id": "L5.1",
        "definition_extra": (
            "\n• Bản chất 'Nhập trước – Xuất trước' (First-In, First-Out — mở rộng cho vật tư có hạn dùng là FEFO: Hết hạn trước – Xuất trước): Đảm bảo không có cuộn đồng, bao nhựa hay cuộn băng chống thấm nào bị đẩy lùi vào góc tường nằm suốt 6 tháng dẫn tới oxy hóa đen đồng, hút ẩm vón cục nhựa XLPE Silane (hạn dùng rất ngắn sau khi mở bao!), hoặc giòn rách băng Mica.\n"
            "• Cách biến FIFO thành tự động (Poka-Yoke): Dùng làn FIFO Lane có lối vào ở đầu sau và lối ra ở đầu trước (xe nâng nạp rulo từ phía sau, lấy ra từ phía trước — không thể nào lấy nhầm rulo mới nhất!)."
        ),
        "cadivi_application_extra": (
            "\n• Sống còn tại CADIVI Miền Trung với 3 nhóm vật tư 'nhạy thời gian' cao: (1) Hạt nhựa XLPE Silane (rất dễ tự đóng rắn trước nếu để kho ẩm lâu), (2) Rulo đồng trần sau kéo/ủ (để quá 48–72 giờ trong khí hậu ẩm Đà Nẵng dễ bị đen oxy hóa), (3) Băng chống thấm Water-Blocking & băng Mica FR."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Kệ sữa tươi ở siêu thị luôn đẩy hộp mới nhập ra phía sau, để hộp nhập trước ra mặt ngoài để không có hộp nào bị quá hạn sử dụng nằm sâu trong góc.\n"
            "\n• Ví dụ 2 (Tại Kho Hạt Nhựa CADIVI): Kẻ 2 làn FIFO riêng cho hạt XLPE kèm bảng thẻ màu theo tháng nhập kho (Tháng lẻ thẻ Vàng, Tháng chẵn thẻ Xanh) giúp xóa 100% tình trạng bao nhựa tồn kho quá 6 tháng bị giảm chất lượng lưu hóa rớt Hot Set Test!"
        ),
        "common_mistakes": (
            "1. Xếp rulo sát tường theo kiểu 1 lối vào–ra duy nhất (LIFO — Vào sau Ra trước) khiến rulo cũ nhất bị kẹt mãi trong cùng nhiều tuần liền!"
        )
    },
    "Milk Run": {
        "lesson_id": "L3.2",
        "definition_extra": (
            "\n• Bản chất 'Chuyến xe buýt vật tư chạy đúng tuyến, đúng giờ' (lấy hình ảnh xe giao sữa truyền thống sáng nào cũng chạy vòng tròn giao chai sữa đầy và thu hồi vỏ chai rỗng trên cùng 1 chuyến): Thay vì 10 máy gọi xe nâng rời rạc chạy đi chạy về không tải 50% quãng đường, 1 xe kéo/xe nâng Milk Run chạy theo đúng 1 lộ trình khép kín mỗi 30–60 phút: vừa cấp rulo đồng, hạt nhựa, tem nhãn cho các máy, vừa thu gom rulo rỗng và thùng phế liệu về kho trên cùng 1 vòng xe!"
        ),
        "cadivi_application_extra": (
            "\n• Giải pháp cực kỳ tiết kiệm chi phí vận chuyển nội bộ tại khuôn viên rộng lớn của Nhà máy CADIVI Miền Trung (KCN Hòa Cầm): chuẩn hóa tuyến xe nâng / xe kéo vật tư giữa Kho nguyên liệu – 4 Phân xưởng – Khu tập kết phế liệu – Kho thành phẩm."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Xe buýt thành phố chạy đúng tuyến 15 phút/chuyến chở được 40 người cùng lúc hiệu quả và ít tắc đường hơn 40 chiếc taxi chạy chéo nhau loạn xạ!\n"
            "\n• Ví dụ 2 (Tại CADIVI): Chuyển 3 xe nâng từ chế độ 'ai gọi thì chạy' sang 2 tuyến Milk Run cố định 45 phút/vòng (kèm 1 xe nâng dự phòng cho rulo nặng > 3 tấn) giúp giảm 38% tổng km xe nâng chạy không tải/ngày, tăng an toàn giao thông xưởng và cắt 70% thời gian máy đùn chờ vật tư!"
        ),
        "common_mistakes": (
            "1. Thiết kế tuyến Milk Run không đồng bộ với mức tồn kho đệm tại máy (ví dụ chu kỳ tuyến 60 phút nhưng thùng nhựa tại máy chỉ đủ chạy 40 phút → máy hết nhựa trước khi xe kịp vòng tới!)."
        )
    },
    "Visual Management": {
        "lesson_id": "L3.1",
        "definition_extra": (
            "\n• Quy tắc vàng '3 giây – 3 mét': Bất kỳ ai (kể cả Giám đốc mới bước vào xưởng) đứng cách xa 3 mét nhìn vào trong vòng 3 giây phải biết ngay trạng thái hiện tại là Bình thường (Xanh) hay Bất thường (Đỏ) mà không cần hỏi ai hay mở máy tính tra Excel!\n"
            "• Các công cụ Quản trị Trực quan phổ biến nhất: Vạch sơn sàn phân vùng (Xanh = lối đi người, Vàng = vùng WIP, Đỏ = vùng hàng lỗi NCR), Bảng bóng dụng cụ Shadow Board, Vạch xanh/đỏ trên đồng hồ nhiệt/áp suất, Bảng sản lượng theo giờ (Hour-by-Hour Board) và Bảng SQDCM."
        ),
        "cadivi_application_extra": (
            "\n• Áp dụng toàn xưởng CADIVI Miền Trung: Dán vạch xanh giới hạn bình thường lên đồng hồ áp suất Melt Pressure, đồng hồ nhiệt nước làm mát (≤ 25°C xanh / > 30°C đỏ), vạch mức dầu hộp số máy kéo, và bảng Hour-by-Hour ghi sản lượng mét/giờ cạnh từng máy đùn."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Đèn giao thông Xanh–Vàng–Đỏ và vạch kẻ đường giúp hàng triệu người đi lại trật tự mỗi ngày mà không cần đọc luật bằng chữ giữa ngã tư!\n"
            "\n• Ví dụ 2 (Bảng Hour-by-Hour tại máy đùn CADIVI): Kẻ bảng trắng lớn ghi mục tiêu sản lượng từng giờ (vd: 18 km/giờ). Nếu 09:00 chỉ đạt 12 km → tô ĐỎ và ghi ngay lý do (vd: 'nghẹt lưới lọc 18p') để Tổ trưởng & OE phát hiện can thiệp ngay trong ca thay vì chờ cuối tháng xem báo cáo mới biết bị hụt sản lượng!"
        ),
        "common_mistakes": (
            "1. Dán đầy bảng biểu chữ nhỏ li ti chi chít số liệu nhưng không có mục tiêu (Target) và không tô màu Xanh/Đỏ phân biệt Đạt/Không đạt → Không ai muốn đọc!"
        )
    },
    "LSW": {
        "lesson_id": "L3.4",
        "definition_extra": (
            "\n• Bản chất 'Kỷ luật hóa thói quen lãnh đạo hiện trường': Công nhân có Standard Work làm ra sản phẩm; nhưng nếu Tổ trưởng, Quản đốc và OE mỗi ngày đi làm chỉ chạy theo chữa cháy tùy hứng thì mọi chuẩn 5S, SMED, SPC sẽ sụp đổ chỉ sau vài tuần! Leader Standard Work (LSW) là tờ lịch kiểm tra cố định theo giờ/ngày/tuần buộc từng cấp quản lý phải đích thân xuống Genba xác nhận quá trình đang chạy đúng chuẩn (tỷ lệ thời gian theo LSW chuẩn: Tổ trưởng 70–80%, Quản đốc 50%, Giám đốc xưởng 25%)."
        ),
        "cadivi_application_extra": (
            "\n• Chìa khóa biến văn hóa OE thành DNA bền vững tại CADIVI Miền Trung: OE thiết kế tờ LSW gọn nhẹ 1 trang cho Tổ trưởng từng phân xưởng Kéo – Bện – Đùn – Đóng gói tích hợp kiểm tra An toàn LOTO, 5S, kiểm chuẩn Spark/Laser, tủ sấy đầu khuôn SMED và cập nhật bảng Hour-by-Hour."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Huấn luyện viên thể thao chuyên nghiệp luôn có giáo án kiểm tra cố định mỗi ngày (khởi động → đo nhịp tim → bài tập kỹ thuật → tổng kết) thay vì hôm thích thì tập, hôm bận thì bỏ!\n"
            "\n• Ví dụ 2 (Phiếu LSW Tổ trưởng Xưởng Đùn CADIVI): 06:00 Họp 5p đầu ca → 06:30 Xác nhận mẫu test Spark Tester & Recipe đúng lệnh → 09:00 Kiểm tra tủ sấy đã sấy sẵn Tip/Die cho lệnh chiều chưa → 11:00 Kiểm tra thùng phế đồng trần không lẫn nhựa → 13:45 Chốt sản lượng & bàn giao Ca 2. Chỉ mất 25 phút/ca nhưng giữ vững OEE & SMED suốt cả năm!"
        ),
        "common_mistakes": (
            "1. Làm phiếu LSW dài tới 50 mục chi li như bản thẩm vấn khiến Tổ trưởng ngồi văn phòng đánh dấu tích khống cho xong chuyện! LSW chuẩn chỉ nên gồm 8–12 điểm cốt tử kiểm được ngay tại máy."
        )
    },
    "LPA": {
        "lesson_id": "L3.4",
        "definition_extra": (
            "\n• Bản chất 'Kiểm tra chéo đa tầng chống làm tắt': Thay vì chờ 1 năm phòng QA mới đánh giá nội bộ ISO 1 lần, LPA (Layered Process Audit) là chuỗi kiểm tra nhanh (chỉ 5–10 phút) trên cùng một bộ câu hỏi trọng yếu lặp lại ở 3–4 cấp bậc quản lý:\n"
            "  - Layer 1 (Hàng ngày): Tổ trưởng kiểm tra trực tiếp từng máy trong ca.\n"
            "  - Layer 2 (Hàng tuần): Quản đốc / Kỹ sư OE / QA kiểm tra ngẫu nhiên các tổ.\n"
            "  - Layer 3 (2 tuần / Hàng tháng): Giám đốc Nhà máy đích thân đi kiểm tra 1–2 chuyền!\n"
            "• Hiệu ứng tâm lý kỳ diệu: Khi công nhân thấy chính Giám đốc nhà máy cũng đích thân xuống hỏi về khóa LOTO, mẫu test Spark và xe đồ nghề SMED, cả nhà máy lập tức hiểu cải tiến là chuyện THẬT chứ không phải phong trào nhất thời!"
        ),
        "cadivi_application_extra": (
            "\n• Câu trả lời phỏng vấn xuất sắc nhất tại CADIVI khi được hỏi 'Làm sao duy trì thành quả cải tiến?': Đề xuất triển khai LPA 10 câu hỏi Có/Không (tập trung An toàn LOTO, Kiểm chuẩn Spark/Laser, Recipe PLC, Phân loại 3 thùng phế & 5S) gắn với bảng theo dõi tỷ lệ tuân thủ trên Power BI."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Trong chuỗi khách sạn 5 sao, nhân viên dọn phòng kiểm tra phòng mỗi ngày (L1), giám sát tầng kiểm mẫu mỗi tuần (L2), tổng quản lý kiểm đột xuất hàng tháng (L3) — đảm bảo tiêu chuẩn không bao giờ đi xuống!\n"
            "\n• Ví dụ 2 (Phiếu LPA Xưởng Đùn CADIVI): Câu 1: Có khóa LOTO khi vệ sinh lưới lọc? Câu 2: Đã test mẫu lỗ kim Spark Tester đầu ca? Câu 3: Đầu Tip/Die cho lệnh kế tiếp đã nằm trong tủ sấy 160°C? Câu 4: Thùng phế đồng trần không lẫn nhựa? → Sau 2 tháng duy trì LPA, điểm tuân thủ tăng từ 64% lên 96% và lỗi lọt khách hàng giảm một nửa!"
        ),
        "common_mistakes": (
            "1. Dùng kết quả LPA để trừ lương công nhân → Xưởng sẽ giấu lỗi hoặc đối phó khi thấy sếp đi xuống! LPA phải tập trung 'sửa quy trình & hỗ trợ công nhân bỏ rào cản' để họ dễ làm đúng hơn."
        )
    },
    "Escalation Matrix": {
        "lesson_id": "L3.4",
        "definition_extra": (
            "\n• Bản chất 'Quy ước ứng cứu khẩn cấp có đồng hồ đếm ngược (SLA)': Trong nhiều xưởng sản xuất, khi máy cổ chai bị sự cố, công nhân đứng loay hoay 20 phút không sửa được mới gọi Tổ trưởng, Tổ trưởng loay hoay thêm 30 phút mới báo Bảo trì, 2 tiếng sau Quản đốc mới biết thì đã mất trắng nửa ca sản lượng! Escalation Matrix định nghĩa minh bạch 4 mốc thời gian leo thang bắt buộc để đúng người có đủ thẩm quyền & chuyên môn có mặt ngay lập tức."
        ),
        "cadivi_application_extra": (
            "\n• Ưu tiên gắn ngay trên các máy điểm nghẽn (Bottleneck) tại CADIVI Miền Trung như Máy kéo thô RBD, Máy đùn cáp lực CXV/XLPE và Dây chuyền giáp thép DSTA để nén mạnh chỉ số MTTR (thời gian khắc phục sự cố)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Quy trình cấp cứu y tế — y tá sơ cứu phút 0–5, bác sĩ trực xử lý phút 5–15, vượt thẩm quyền lập tức hội chẩn trưởng khoa phút 15–30 để cứu sống bệnh nhân kịp giờ vàng!\n"
            "\n• Ví dụ 2 (Ma trận SLA cho 4 Máy Đùn Cổ Chai CADIVI): Dừng 0–5p: Tổ trưởng kiểm tra tại máy → Quá 5p chưa chạy lại: Báo ngay Cơ điện/Kỹ thuật công nghệ → Quá 15p: Báo Quản đốc & OE điều phối lệnh sang máy dự phòng → Quá 60p hoặc lỗi chất lượng lô lớn: Báo trực tiếp Giám đốc Nhà máy! Kết quả rút thời gian dừng chờ hỗ trợ từ 24 phút xuống còn 6 phút/sự cố!"
        ),
        "common_mistakes": (
            "1. Treo bảng Escalation Matrix lên tường nhưng tổ trưởng vẫn sợ bị sếp mắng nếu báo lên cấp trên → Phải tạo văn hóa 'Báo sớm = Khen thưởng vì bảo vệ sản lượng; Giấu sự cố đến khi trễ đơn hàng mới là lỗi!'"
        )
    },
    "RCCP": {
        "lesson_id": "L5.1",
        "definition_extra": (
            "\n• Bản chất 'Bài kiểm tra sức khỏe năng lực thô ở tầng MPS': Trước khi Phòng Kinh doanh và Giám đốc cam kết nhận một lô đơn hàng 350 tấn cáp cho tháng tới, RCCP (Rough-Cut Capacity Planning) quy đổi nhanh toàn bộ sản lượng kế hoạch (tấn/km) thành giờ máy yêu cầu tại các công đoạn trọng yếu (Kéo – Bện – Đùn – Lưu hóa – Giáp – Đóng gói) rồi so sánh với Giờ máy khả dụng thực tế (đã nhân với OEE lịch sử thực tế, KHÔNG lấy 100% lý thuyết!) để phát hiện sớm công đoạn nào quá tải (> 100%) ngay từ khi còn trên giấy!"
        ),
        "cadivi_application_extra": (
            "\n• Một trong những báo cáo chiến lược quan trọng nhất của OE trình Ban Giám đốc CADIVI Miền Trung mỗi kỳ lập kế hoạch tháng/quý (mục 7 trong JD: 'báo cáo định hướng về sản xuất, năng lực...')."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Chủ nhà hàng nhận đặt tiệc 300 khách cuối tuần — tính nhanh bếp chính chỉ nấu tối đa 220 suất (tải 136% QUÁ TẢI!) → Quyết định ngay từ thứ Ba phải thuê thêm 2 phụ bếp hoặc chia 2 khung giờ phục vụ thay vì để đến tối thứ Bảy mới vỡ trận!\n"
            "\n• Ví dụ 2 (Tính RCCP 300 tấn cáp tại CADIVI): Mỗi máy có 26 ngày × 2 ca × 7.5h = 390h kế hoạch/tháng. Xưởng Đùn có 4 máy, OEE lịch sử 65% → Giờ khả dụng ròng = 4 × 390 × 65% = 1,014h. Đơn hàng cần 1,180h → Tải Load = 116.4% (thiếu 166h!). Phương án OE: (1) SMED nâng OEE 65%→74% lấy lại +140h, (2) Mở Ca 3 cục bộ cho riêng 1 máy đùn trong 1 tuần — tuyệt đối KHÔNG tăng ca Xưởng Kéo đang chỉ 72% tải!"
        ),
        "common_mistakes": (
            "1. Tính năng lực khả dụng bằng `Số máy × 24h × 30 ngày` (quên nhân OEE thực tế 65–75%) → Báo ảo 'đủ tải thừa sức' rồi đến giữa tháng vỡ tiến độ giao hàng hàng loạt!"
        )
    },
    "CAPEX": {
        "lesson_id": "L5.4",
        "definition_extra": (
            "\n• Phân biệt rạch ròi CAPEX vs OPEX trong quản trị tài chính nhà máy:\n"
            "  - CAPEX (Capital Expenditure — Chi phí Đầu tư Vốn): Tiền mua tài sản cố định dùng dài hạn nhiều năm (> 1 năm, giá trị lớn như máy đùn mới 5 tỷ, bộ đo Laser Gauge 420 triệu, xe nâng 700 triệu, phần mềm MES), được ghi nhận tài sản và khấu hao dần hàng năm.\n"
            "  - OPEX (Operating Expenditure — Chi phí Vận hành): Tiền chi thường xuyên duy trì sản xuất hàng tháng (lương công nhân, điện nước, đồng/nhựa, vật tư bảo trì thay thế, dầu nhũ tương).\n"
            "• Nguyên tắc vàng OE: Luôn ưu tiên tối ưu không tốn CAPEX (Lean, SMED, nâng OEE/TEEP, tăng ca cục bộ) trước khi đề xuất mua sắm CAPEX!"
        ),
        "cadivi_application_extra": (
            "\n• Gắn chặt với mục 5 JD CADIVI ('đánh giá hiệu quả kỹ thuật và hiệu quả kinh tế ROI') và thế mạnh thẩm định đầu tư thiết bị từ CV của bạn: lập hồ sơ thuyết minh CAPEX chặt chẽ (TEEP chứng minh đã khai thác hết công suất hiện hữu + Hard Savings + Payback + 3 kịch bản độ nhạy)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Mua chiếc xe tải 800 triệu là CAPEX; tiền đổ xăng, thay nhớt và trả lương tài xế hàng tháng là OPEX.\n"
            "\n• Ví dụ 2 (Tránh CAPEX lãng phí tại CADIVI): Xưởng xin CAPEX 4.5 tỷ mua thêm máy đùn số 7 vì 'chạy hết công suất'. OE kiểm tra thấy OEE 6 máy hiện tại mới 62% (đổi màu mất 50p/lần) → Chỉ cần đầu tư CAPEX nhỏ 250 triệu (tủ sấy đầu khuôn + xe SMED + Laser Gauge) nâng OEE lên 78% đã sinh ra sản lượng tương đương mua thêm hẳn 1.5 máy đùn mới, tiết kiệm > 4 tỷ đồng vốn đầu tư!"
        ),
        "common_mistakes": (
            "1. Chỉ tính giá mua máy ban đầu khi lập hồ sơ CAPEX mà quên các chi phí ẩn đi kèm: phí vận chuyển/lắp đặt, nâng cấp trạm biến áp điện, đào tạo vận hành và chi phí phụ tùng bảo trì hàng năm (OPEX tăng thêm)."
        )
    },
    "ROI": {
        "lesson_id": "L5.4",
        "definition_extra": (
            "\n• Bản chất thước đo '1 đồng bỏ ra thu về mấy đồng lãi?': ROI (Return on Investment) đánh giá hiệu quả sinh lời bằng % của một dự án cải tiến hoặc mua sắm thiết bị.\n"
            "• Phân biệt sống còn trong thuyết trình trước Kế toán trưởng:\n"
            "  - Hard Savings (Tiền tươi thực sự giảm trên sổ Kế toán): Giảm kg đồng/nhựa phế liệu, giảm kWh điện, giảm giờ tăng ca trả lương thật, tránh phải mua máy mới.\n"
            "  - Soft Savings (Lợi ích gián tiếp — KHÔNG cộng gộp chung vào ROI để xin tiền!): Tiết kiệm 30 phút thời gian làm báo cáo của nhân viên lương cố định (không cắt giảm lương thực tế), tăng uy tín thương hiệu, xưởng sạch đẹp hơn."
        ),
        "cadivi_application_extra": (
            "\n• Yêu cầu trực tiếp mục 5 trong JD OE CADIVI: Mọi dự án cải tiến Trước–Sau của bạn đều cần bảng tính ROI minh bạch được Phòng Kế toán xác nhận đơn giá vật tư/nhân công đầu vào — đây cũng là cách bạn trình bày kinh nghiệm thẩm định đầu tư ở Mabuchi một cách chuyên nghiệp mà không tiết lộ số liệu mật!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tính ROI dự án lắp Laser Gauge Closed-loop tại CADIVI): Tổng vốn đầu tư = 420 triệu VNĐ. Tiết kiệm Hard Savings nhựa Over-thickness 3.0 tấn/tháng × 32 triệu = 96 triệu/tháng → 1 năm tiết kiệm 1,152 triệu; trừ chi phí bảo trì/hiệu chuẩn 32 triệu/năm → Lợi ích ròng năm 1 = 1,120 triệu. ROI năm đầu = [(1,120 - 420) / 420] × 100% = +166.7% (hoàn vốn trong 4.4 tháng)!\n"
            "\n• Ví dụ 2 (Đánh giá bằng 3 kịch bản độ nhạy): Luôn trình bày Kịch bản Thận trọng (đạt 60% mục tiêu) – Cơ sở (100%) – Lạc quan (120%) để chứng minh kể cả trong trường hợp xấu nhất dự án vẫn hoàn vốn dưới 12 tháng!"
        ),
        "common_mistakes": (
            "1. Gộp Soft Savings (như 'giảm mệt mỏi ước tính 100 triệu/tháng') vào bảng ROI trình Kế toán trưởng → Bị bác bỏ ngay lập tức vì không chứng minh được trên dòng tiền thật!\n"
            "2. Tự tính đơn giá đồng/nhựa theo cảm tính thay vì lấy đúng đơn giá Standard Cost của Phòng Kế toán."
        )
    },
    "Payback": {
        "lesson_id": "L5.4",
        "definition_extra": (
            "\n• Bản chất 'Bao lâu thì thu hồi đủ vốn bỏ ra?': Payback Period (Thời gian hoàn vốn) là chỉ số Giám đốc nhà máy sản xuất hỏi đầu tiên trước khi đọc các chỉ số phức tạp như NPV/IRR! Trong ngành sản xuất Việt Nam, các dự án cải tiến OE có Payback < 6 tháng gần như được duyệt ngay lập tức; 6–12 tháng rất khả thi; > 24 tháng cần thẩm định chiết khấu dòng tiền NPV/IRR chặt chẽ."
        ),
        "cadivi_application_extra": (
            "\n• Áp dụng cho mọi đề xuất đầu tư thiết bị cải tiến tại CADIVI (máy hàn đối đầu Butt Welder, tủ sấy Tip/Die SMED, biến tần VFD, máy đo Laser Gauge, cảm biến Poka-Yoke, hệ thống hút hạt nhựa tự động)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Hoàn vốn siêu nhanh cho tủ sấy SMED): Đầu tư 1 tủ sấy nóng sẵn đầu Chày–Cối + 2 xe đẩy 5S tốn 65 triệu VNĐ. Nhờ giảm phế đầu ca 18 kg nhựa/lần × 25 lần/tháng × 30,000đ = 13.5 triệu/tháng + thêm 15 giờ chạy máy cổ chai (lợi ích biên 18 triệu/tháng) → Tổng tiết kiệm 31.5 triệu/tháng → Payback = 65 / 31.5 = 2.06 tháng!\n"
            "\n• Ví dụ 2 (Lưu ý rà soát CV cá nhân): Với bài toán hoàn vốn đơn giản `1,200 triệu / 350 triệu = 3.43 tháng`, luôn nhớ kiểm tra kỹ xem 350 triệu đã trừ chi phí vận hành/khấu hao hay chưa (Tiết kiệm ròng vs gộp) và chỉ công bố phương pháp tính khi số liệu công ty cũ chưa được phép tiết lộ!"
        ),
        "common_mistakes": (
            "1. Lấy Doanh thu tăng thêm chia cho Vốn đầu tư thay vì lấy Lợi nhuận gộp / Tiết kiệm chi phí ròng (vì tăng doanh thu 1 tỷ cáp điện thì đã tốn 850 triệu mua đồng và nhựa rồi — lợi ích ròng thực chỉ khoảng 100–150 triệu!)."
        )
    },
    "BOM": {
        "lesson_id": "L5.2",
        "definition_extra": (
            "\n• Phân biệt 3 loại cây BOM trong nhà máy cáp điện:\n"
            "  - EBOM (Engineering BOM — Phòng Kỹ thuật R&D lập): Khối lượng lý thuyết thuần túy theo bản vẽ thiết kế sản phẩm.\n"
            "  - MBOM (Manufacturing BOM — OE/Sản xuất dùng chạy ERP): Cấu trúc đa tầng theo từng công đoạn thực tế (Tầng 1: Đồng Rod 8mm → Tầng 2: Sợi đồng kéo → Tầng 3: Ruột đồng bện có nhân hệ số xoắn Lay-up Factor → Tầng 4: Lõi bọc XLPE + hao phí công nghệ chuẩn đầu-đuôi → Tầng 5: Cáp ghép lõi/giáp DSTA/vỏ PVC + độn PP + rulo gỗ).\n"
            "  - SBOM (Sales/Packaging BOM): Bao gồm thêm tem nhãn, màng co, thùng carton, pallet giao hàng.\n"
            "• Tại sao BOM là 'tử huyệt' ở CADIVI? Vì Nguyên vật liệu Đồng/Nhôm/Nhựa chiếm tới 80% – 88% tổng giá thành cáp — chỉ cần kiểm soát BOM lệch 1% đã tương đương biến động hàng tỷ đồng lợi nhuận!"
        ),
        "cadivi_application_extra": (
            "\n• Ghi rõ mục 7 JD CADIVI ('báo cáo định hướng về định mức BOM, vật tư'): OE đối soát định kỳ chênh lệch thực xuất vs MBOM (BOM Variance), tách rạch ròi Hao phí công nghệ (tự nhiên phải có) vs Hao phí vận hành bất thường (Copper Give-away, Over-thickness, lỗi Spark, mẩu cắt Cut-Length)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Công thức làm 1 ổ bánh mì chuẩn (BOM) cần 120g bột + 15g bơ + 5g men (hao hụt dính cối 3%). Nếu làm 100 ổ mà xuất kho hết 14 kg bột thay vì 12.36 kg → Lệch BOM +1.64 kg phải kiểm tra xem thợ cân quá tay (Over-thickness) hay làm cháy bỏ (Scrap)!\n"
            "\n• Ví dụ 2 (BOM cáp lực CXV 3×50+1×25 tại CADIVI): Định mức chuẩn 1 km cần ~1,562 kg Đồng (đã nhân Lay-up Factor xoắn), ~114 kg XLPE, ~385 kg PVC vỏ, ~35 kg độn PP. Lệnh sản xuất 10 km đạt chuẩn xuất thực 15,850 kg đồng → Vượt định mức +230 kg đồng × 250,000đ = thiệt hại 57.5 triệu VNĐ chỉ riêng 1 lệnh!"
        ),
        "common_mistakes": (
            "1. Quên nhân Hệ số xoắn bện (Lay-up Factor 1.02–1.05) khi lập MBOM ruột bện & ghép lõi → Định mức ERP lúc nào cũng thiếu hụt giả tạo 3% dù công nhân chạy chuẩn!\n"
            "2. Đem so vật tư thực xuất với Tổng mét chạy (gồm cả phế) thay vì Sản lượng Đạt nhập kho → Che giấu sạch tổn thất phế phẩm!"
        )
    },
    "Kitting": {
        "lesson_id": "L5.1",
        "definition_extra": (
            "\n• Bản chất 'Chuẩn bị trọn bộ đồng bộ trước khi chạy máy': Thay vì cấp vật tư rời từng thùng lớn xuống chuyền (công nhân tự bốc dễ thừa thiếu, dễ lắp nhầm mã hoặc mất thời gian tìm đồ), nhân viên kho/Water Spider soạn sẵn từng Khay/Xe Kit chứa ĐÚNG chủng loại và ĐÚNG số lượng linh kiện/phụ kiện cho 1 lệnh sản xuất hoặc 1 lần đổi mã SMED/bảo trì PM.\n"
            "• Lợi ích 3 trong 1: (1) Xóa 100% thời gian công nhân/thợ bảo trì đi tìm đồ (tăng OLE & Wrench Time), (2) Chống nhầm vật tư (Poka-Yoke), (3) Chạy xong lệnh mà trên khay còn dư món nào là phát hiện quên lắp ngay tức khắc!"
        ),
        "cadivi_application_extra": (
            "\n• Áp dụng xuất sắc tại 3 nơi ở CADIVI Miền Trung: (1) Khay Kitting đổi mã SMED máy đùn (Chày–Cối đã sấy, lưới lọc Screen Pack mới, thẻ Recipe, mẫu màu chuẩn), (2) Bộ Kit 24 suốt đồng đánh đều chiều dài cho máy Bện lưới Braiding, (3) Xe Kitting phụ tùng cho lệnh Bảo trì PM định kỳ của Phòng Cơ Điện."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Hộp nguyên liệu nấu lẩu đã sơ chế sẵn đúng định lượng rau, thịt, nước dùng — về nhà chỉ việc bật bếp nấu trong 10 phút, không bao giờ quên mua hành hay thừa nửa bó rau!\n"
            "\n• Ví dụ 2 (Kitting bảo trì PM tại CADIVI): Kho phụ tùng soạn sẵn 1 thùng Kit cho lịch PM cuối tuần của máy kéo RBD (đúng 4 vòng bi, 2 phớt dầu, 1 dây curoa, 1 can dầu chuẩn) giao sẵn trước 16:00 thứ Sáu → Thợ Cơ Điện giảm 40% thời gian chạy đi chạy lại kho, nâng Wrench Time từ 32% lên 49%!"
        ),
        "common_mistakes": (
            "1. Dùng Kitting cho cả vật tư siêu rẻ tiêu thụ hàng loạt như tem nhãn hay màng co (làm tăng công soạn kho không cần thiết) — nhóm đó nên dùng Two-Bin Kanban!"
        )
    },
    "Cycle Counting": {
        "lesson_id": "L5.1",
        "definition_extra": (
            "\n• Bản chất 'Kiểm kê luân phiên thông minh thay vì dừng nhà máy cuối năm': Kiểm kê tổng cuối năm vừa phải dừng xưởng 2–3 ngày mất sản lượng, vừa chỉ phát hiện mất hàng khi sự việc đã trôi qua 8 tháng không thể truy gốc! Cycle Counting chia toàn bộ mã hàng kho thành 3 nhóm ABC theo giá trị sử dụng năm: Nhóm A (20% mã chiếm 75–80% tiền — kiểm đếm mỗi tuần/2 tuần), Nhóm B (30% mã chiếm 15% tiền — kiểm mỗi tháng), Nhóm C (50% mã chiếm 5% tiền — kiểm mỗi quý/6 tháng) để giữ Độ chính xác tồn kho ERP (RIA) ≥ 98.5% quanh năm!"
        ),
        "cadivi_application_extra": (
            "\n• Sống còn tại Kho Đồng Rod, Kho Hạt Nhựa XLPE/PVC/LSZH và Kho Rulo Thành phẩm CADIVI Miền Trung: Nếu tồn kho trên ERP sai lệch 5%, lệnh chạy MRP sẽ đặt thiếu nhựa làm dừng máy hoặc mua dư hàng chục tấn chôn vốn!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Bạn kiểm tra số tiền trong ví và tài khoản ngân hàng chính (Nhóm A) mỗi vài ngày, kiểm tra tủ quần áo (Nhóm B) mỗi tháng, còn đống ốc vít/đinh nhỏ trong hộp đồ nghề (Nhóm C) nửa năm mới nhìn một lần!\n"
            "\n• Ví dụ 2 (Tại Kho Nhựa CADIVI): Áp dụng Cycle Counting mỗi sáng thứ Hai cân đối soát 10 mã hạt nhựa Nhóm A (XLPE, LSZH, PVC chính) chỉ mất 45 phút nhưng giúp nâng độ chính xác sổ sách ERP (RIA) từ 89% lên 99.1% và phát hiện ngay 1 lỗi nhập trùng phiếu xuất kho ngay trong tuần!"
        ),
        "common_mistakes": (
            "1. Chỉ điều chỉnh số tồn trên máy tính cho khớp với kho thực tế rồi bỏ qua mà KHÔNG tìm nguyên nhân gốc rễ (5 Whys) vì sao bị lệch (do cân sai, xuất không quét mã hay BOM sai?)."
        )
    },
    "SEC": {
        "lesson_id": "L5.4",
        "definition_extra": (
            "\n• Bản chất thước đo Cường độ Năng lượng chuẩn (Specific Energy Consumption = kWh / Tấn cáp hoặc kWh / Km cáp): Trong nhà máy dây cáp điện, hóa đơn tiền điện là khoản chi phí sản xuất chung (Overhead) lớn nhất — và biến động mạnh theo hiệu suất vận hành OEE! Khi máy đùn chạy êm liên tục ở OEE 80%, điện nền giữ nhiệt 180°C được chia cho sản lượng lớn nên SEC thấp; ngược lại khi máy dừng đổi màu 1 giờ mà vẫn bật nóng nòng đùn (Idle Heating) và chạy lại phế phẩm, SEC tăng vọt 20–30%!"
        ),
        "cadivi_application_extra": (
            "\n• Trọng tâm kết hợp OE & ISO 50001 tại CADIVI Miền Trung: Gắn đồng hồ công tơ điện riêng (Sub-metering) cho các nhóm tải lớn (Máy kéo thô RBD, Dàn máy đùn, Lò ủ/Bể xông XLPE, Chiller, Máy nén khí) để theo dõi SEC từng tháng trên Power BI."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Cùng chiếc ô tô chạy 100 km — đi đường trường êm đều tốn 6 lít xăng (SEC thấp), đi tắc đường dừng đèn đỏ nổ máy tại chỗ liên tục tốn 11 lít xăng (SEC tăng gần gấp đôi!).\n"
            "\n• Ví dụ 2 (Tính tiết kiệm SEC tại CADIVI): Nhà máy sản xuất 400 tấn cáp/tháng, SEC hiện trạng 520 kWh/tấn (= 208,000 kWh/tháng ≈ 457 triệu VNĐ tiền điện). Nhờ bọc áo cách nhiệt nòng đùn, vá 25 điểm rò khí nén, lắp VFD bơm giải nhiệt và nâng OEE giảm Idle Heating, kéo SEC xuống 460 kWh/tấn (-11.5%) → Tiết kiệm trực tiếp 53 triệu VNĐ tiền điện/tháng (> 630 triệu/năm)!"
        ),
        "common_mistakes": (
            "1. So sánh SEC giữa tháng chạy toàn cáp lực tiết diện lớn 240 mm² (kéo ít cấp khuôn, rất nhẹ điện/tấn) với tháng chạy toàn dây dân dụng mảnh 1.5 mm² (kéo 20 cấp khuôn, tốn điện/tấn gấp đôi!) — phải theo dõi SEC chuẩn hóa theo từng nhóm sản phẩm!"
        )
    },
    "S&OP": {
        "lesson_id": "L5.1",
        "definition_extra": (
            "\n• Bản chất 'Cuộc họp đồng thuận cấp lãnh đạo mỗi tháng' (Sales & Operations Planning — tầm nhìn 3 đến 18 tháng): Rất nhiều doanh nghiệp mắc bệnh 'Kinh doanh hứa giao bất chấp năng lực, Xưởng chạy không kịp, Mua hàng nhập đồng chậm, Tài chính thiếu dòng tiền'. Chu trình S&OP 5 bước hàng tháng (Thu thập dữ liệu → Họp Dự báo Cầu Demand Review → Họp Năng lực Cung Supply Review/RCCP → Họp Cân bằng Tiền & Lợi nhuận Pre-S&OP → Cuộc họp Ban Giám đốc chốt 1 Kế hoạch Duy nhất Executive S&OP) giúp toàn bộ công ty chạy chung MỘT bộ số!"
        ),
        "cadivi_application_extra": (
            "\n• Vai trò của OE CADIVI trong chu trình S&OP: Cung cấp đầu vào khách quan và đáng tin cậy nhất cho bước Supply Review — chính là bảng năng lực thực tế từng phân xưởng (RCCP theo tấn/km & OEE thực), dự báo điểm nghẽn 3 tháng tới và các phương án mở rộng ca/đầu tư kịp thời."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Gia đình họp cuối tháng cân đối thu nhập (Cung) với kế hoạch chi tiêu/du lịch 6 tháng tới (Cầu) để không rơi vào cảnh giữa năm vỡ nợ hoặc hết tiền đột xuất.\n"
            "\n• Ví dụ 2 (Tại CADIVI): Trong cuộc họp S&OP tháng 8, Kinh doanh dự báo quý 4 đơn hàng cáp nhôm ABC & cáp lực CXV điện lực sẽ tăng +40%. Nhờ cảnh báo RCCP sớm của OE từ tháng 8, nhà máy có đủ 60 ngày để đặt mua trước đồng/nhôm Rod nhập khẩu, bảo trì đại tu trước 2 máy đùn chủ lực và tuyển đào tạo sẵn 1 kíp công nhân 3 ca 4 kíp!"
        ),
        "common_mistakes": (
            "1. Biến cuộc họp S&OP thành buổi họp chữa cháy giải quyết đơn hàng gấp tuần này — S&OP phải nhìn tầm trung hạn (3–18 tháng) theo nhóm sản phẩm (tấn/nhóm cáp), còn đơn hàng ngày/tuần thuộc tầng MPS & điều độ xưởng!"
        )
    },
    "MPS": {
        "lesson_id": "L5.1",
        "definition_extra": (
            "\n• Bản chất 'Bản hợp đồng cam kết giữa Kinh doanh và Nhà máy' (Master Production Schedule — tầm nhìn 4–12 tuần): Nếu S&OP nói chung chung 'Tháng 10 sản xuất 350 tấn cáp hạ thế', thì MPS bóc tách cụ thể đến từng mã hàng thành phẩm SKU và từng tuần: Tuần 40 sản xuất 15 km CXV 3×50+1×25, 80 km VC 2.5 Trắng, 40 km ABC 4×50... MPS chính là đầu vào trực tiếp để ERP chạy tính toán vật tư MRP và kiểm tra tải thô RCCP.\n"
            "• Khái niệm hàng rào thời gian (Time Fence): Khoảng 1–2 tuần gần nhất là 'Vùng đóng băng (Frozen Zone)' — hạn chế tối đa chèn đơn làm vỡ lịch Campaign Scheduling & tăng dừng đổi mã SMED!"
        ),
        "cadivi_application_extra": (
            "\n• OE CADIVI giám sát chỉ số Tuân thủ Kế hoạch (MPS Adherence / Schedule Attainment ≥ 85–90%) và phân tích nguyên nhân gốc mỗi khi lịch MPS bị xé nát do chèn đơn gấp hoặc thiếu vật tư."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Thực đơn chi tiết từng món cho từng ngày trong tuần của bếp ăn công nghiệp (MPS), là cơ sở để sáng sớm đi chợ mua chính xác bao nhiêu kg thịt/rau (MRP).\n"
            "\n• Ví dụ 2 (Ổn định Frozen Zone tại CADIVI): Trước đây Kinh doanh gọi điện đổi lịch máy đùn giữa ca 8–10 lần/tuần khiến công nhân phải xả nhựa đổi mã đột xuất mất 12 giờ/tuần. Thiết lập quy tắc đóng băng MPS 72 giờ (trừ đơn khẩn có Giám đốc duyệt) giúp OEE máy đùn tăng ngay +6.5%!"
        ),
        "common_mistakes": (
            "1. Nhồi đơn hàng vượt 120% công suất vào MPS mà không kiểm tra RCCP (Overstated MPS) → Làm toàn bộ lịch mua hàng MRP bị rối loạn và đơn nào cũng trễ hạn dây chuyền!"
        )
    },
    "MRP": {
        "lesson_id": "L5.1",
        "definition_extra": (
            "\n• Bản chất 'Cỗ máy phá rã định mức BOM theo thời gian' (Material Requirements Planning): MRP trả lời đúng 3 câu hỏi sống còn: Cần vật tư GÌ? Bao nhiêu? Và phải có mặt LÚC NÀO? dựa trên 3 đầu vào bắt buộc: (1) Kế hoạch MPS, (2) Cây định mức MBOM đa tầng (kèm hệ số xoắn & hao phí chuẩn), (3) Hồ sơ tồn kho hiện có & đơn hàng đang về (Inventory Record).\n"
            "• Logic bù trừ ngược theo Lead Time (Backward Scheduling): Nếu tuần 4 phải giao cáp vỏ PVC, đùn vỏ mất 3 ngày, đùn lõi mất 4 ngày, kéo/bện mất 3 ngày → MRP tự tính lùi ngày phải xuất đồng Rod từ kho vào đầu tuần 2!"
        ),
        "cadivi_application_extra": (
            "\n• Mối quan hệ sống còn giữa OE và MRP tại CADIVI: MRP chạy theo nguyên lý 'Rác vào → Rác ra' (Garbage In, Garbage Out)! Muốn MRP chạy chuẩn trên ERP, OE phải đảm bảo 3 chân kiềng sạch 98%+: BOM chính xác (MBOM), Tồn kho chính xác (Cycle Counting RIA ≥ 98.5%), và Lead Time thực tế chuẩn xác!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Chủ nhật nấu tiệc cần 10 kg gà, kiểm tủ lạnh đang có sẵn 3 kg, đặt giao hàng mất 1 ngày → MRP báo: 'Sáng thứ Bảy phải đặt mua đúng 7 kg gà!'\n"
            "\n• Ví dụ 2 (Tính toán MRP cho 10 km cáp CXV 3×50 tại CADIVI): Định mức MBOM cần 15.62 tấn đồng + 1.14 tấn XLPE + 3.85 tấn PVC. Tồn kho khả dụng đang có 6.0 tấn đồng (trừ 2.0 tấn đã giữ cho đơn khác = còn ròng 4.0 tấn), đơn mua đang về 5.0 tấn → MRP tự phát yêu cầu mua bổ sung ròng = 15.62 − 4.0 − 5.0 = 6.62 tấn đồng Rod trước Lead Time nhà cung cấp!"
        ),
        "common_mistakes": (
            "1. Tin rằng MRP tự biết máy có đủ công suất chạy hay không — MRP truyền thống giả định năng lực máy là VÔ HẠN! Vì vậy bắt buộc phải chạy kèm RCCP (ở tầng MPS) và CRP (sau MRP) để kiểm tra quá tải máy!"
        )
    },
    "CRP": {
        "lesson_id": "L5.1",
        "definition_extra": (
            "\n• Phân biệt sắc bén RCCP vs CRP: RCCP (Hoạch định năng lực thô) chỉ ước lượng nhanh theo tháng ở cấp nhóm máy cổ chai từ MPS; còn CRP (Capacity Requirements Planning — Hoạch định năng lực chi tiết) lấy TOÀN BỘ lệnh sản xuất chi tiết đã sinh từ MRP (kể cả lệnh đang chạy dở dang trên sàn) nhân với thời gian chạy + thời gian đổi mã SMED trên từng Routing để dựng biểu đồ tải giờ máy chi tiết theo từng máy đơn lẻ, từng ngày/ca!"
        ),
        "cadivi_application_extra": (
            "\n• Giúp bộ phận Điều độ & OE CADIVI nhìn rõ tuần tới Máy Đùn số 1 đang quá tải 130% trong khi Máy Đùn số 3 cùng cỡ trục vít chỉ chạy 65% để lập tức san tải (Load Leveling) hoặc sắp xếp lịch bảo trì PM vào đúng khe trống!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): RCCP giống như kiểm tra xem nhà hàng có đủ bàn cho 200 khách cả tuần hay không; còn CRP là sơ đồ xếp chỗ chi tiết từng khung giờ 18:00–20:00 bàn số 1 đến bàn số 20 để không bị 2 đoàn khách đặt trùng cùng 1 bàn!\n"
            "\n• Ví dụ 2 (San tải CRP tại Xưởng Bện CADIVI): Biểu đồ CRP tuần 42 cho thấy máy Bện Rigid #1 quá tải 128% (thiếu 24 giờ máy) trong khi Rigid #2 còn trống 30 giờ → Điều độ chuyển 2 lệnh bện ruột 70 mm² sang Rigid #2, vừa giao đúng hạn vừa tiết kiệm 100% chi phí tăng ca Chủ nhật!"
        ),
        "common_mistakes": (
            "1. Dữ liệu Routing trong ERP để sai thời gian Setup (vd: thực tế đổi màu mất 45p nhưng ERP để mặc định 10p) khiến biểu đồ CRP báo sai lệch hoàn toàn tải thực tế của xưởng Đùn!"
        )
    },
    "Safety Stock": {
        "lesson_id": "L5.1",
        "definition_extra": (
            "\n• Bản chất 'Túi khí bảo hiểm chống đứt gãy sản xuất': Nếu nhu cầu khách hàng ngày nào cũng y hệt nhau và nhà cung cấp đồng/nhựa không bao giờ giao trễ dù 1 giờ thì ta cần Safety Stock = 0. Nhưng thực tế nhu cầu luôn dao động (`σ_D`) và tàu biển nhập hạt nhựa XLPE/đồng Rod có thể chậm thông quan (`σ_LT`) → Safety Stock là lượng dự trữ khoa học tính theo phân phối chuẩn (hệ số Z theo mức phục vụ Service Level: 90% → Z = 1.28; 95% → Z = 1.65; 98% → Z = 2.05; 99% → Z = 2.33) để cân bằng tối ưu giữa Chi phí tồn kho và Rủi ro dừng xưởng!"
        ),
        "cadivi_application_extra": (
            "\n• Tại CADIVI Miền Trung: Tính Safety Stock khoa học theo công thức thống kê (thay vì ước lượng cảm tính 'cứ trữ dư 1 tháng cho chắc ăn' gây chôn hàng chục tỷ đồng!) cho Đồng Rod, Nhôm Rod, Hạt nhựa XLPE/PVC/LSZH, Băng Mica FR và Dây dân dụng bán chạy."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Thời gian đi làm bình thường 25 phút, nhưng thỉnh thoảng kẹt xe thêm 10 phút → Bạn đi sớm trước 35 phút (10 phút dự phòng chính là Safety Stock thời gian để đạt mức đúng giờ 95%!).\n"
            "\n• Ví dụ 2 (Tính toán Safety Stock hạt nhựa XLPE tại CADIVI): Tiêu thụ trung bình D̄ = 4.0 tấn/ngày (độ lệch chuẩn σ_D = 0.8 tấn/ngày), Lead Time nhập hàng LT = 12 ngày (độ lệch chuẩn trễ tàu σ_LT = 2 ngày), mục tiêu phục vụ 95% (Z = 1.65) → SS = 1.65 × √(12 × 0.8² + 4.0² × 2²) = 1.65 × √(7.68 + 64) = 1.65 × 8.47 = 14.0 tấn (giảm từ mức trữ cảm tính 30 tấn xuống 14 tấn, giải phóng ngay > 900 triệu tiền vốn lưu động!)."
        ),
        "common_mistakes": (
            "1. Dùng chung 1 mức tồn kho an toàn '30 ngày' cho mọi mã hàng bất kể mã đó dễ mua trong nước (Lead Time 2 ngày) hay nhập khẩu châu Âu (Lead Time 45 ngày)!\n"
            "2. Không cập nhật lại Safety Stock mỗi 6 tháng khi độ ổn định Lead Time nhà cung cấp thay đổi."
        )
    },
    "ROP": {
        "lesson_id": "L5.1",
        "definition_extra": (
            "\n• Bản chất 'Vạch đỏ báo đổ xăng': Reorder Point (Điểm đặt hàng lại) là mực tồn kho cụ thể mà ngay khi tổng tồn khả dụng (Tồn trong kho + Hàng đã đặt đang trên đường về − Hàng đã giữ cho lệnh SX) chạm xuống bằng hoặc thấp hơn vạch đó, hệ thống ERP hoặc thẻ kho phải lập tức phát đơn đặt mua mới để lô hàng mới về đến cổng nhà máy ĐÚNG LÚC lượng tồn cũ vừa chạm mức Safety Stock!"
        ),
        "cadivi_application_extra": (
            "\n• Thiết lập tham số ROP tự động trên phân hệ ERP MM cho toàn bộ hạt nhựa PVC/XLPE/LSZH, bột màu Masterbatch, băng thép DSTA, băng Mica FR và phụ kiện đóng gói tại CADIVI Miền Trung."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Bình xăng xe máy còn 1 lít (đủ chạy 40 km) thì đèn báo vàng bật sáng nhắc đi đổ xăng ngay — đó chính là điểm ROP của xe máy!\n"
            "\n• Ví dụ 2 (Tính ROP hạt nhựa XLPE tại CADIVI): Tiêu thụ bình quân 4.0 tấn/ngày, Lead Time giao hàng 12 ngày, Safety Stock đã tính là 14.0 tấn → ROP = (4.0 × 12) + 14.0 = 62.0 tấn. Ngay khi tồn khả dụng tụt xuống ≤ 62 tấn, phòng Mua hàng phát PO đặt mua mới!"
        ),
        "common_mistakes": (
            "1. Quên cộng thêm 'Hàng đã đặt đang trên đường về' (Open PO) khi so sánh với ROP → Dẫn tới ngày nào thấy kho dưới 62 tấn cũng đặt mua trùng thêm 1 đơn nữa, tháng sau hàng về ngập kho!"
        )
    },
    "ABC-XYZ": {
        "lesson_id": "L5.1",
        "definition_extra": (
            "\n• Bản chất Ma trận phân khúc tồn kho 9 ô (3×3) vượt trội hơn hẳn phân loại ABC đơn lẻ:\n"
            "  - Trục ABC (Giá trị tiêu thụ năm = Sản lượng × Đơn giá): A = 70–80% tiền (rất đắt), B = 15–20%, C = 5% (rất rẻ).\n"
            "  - Trục XYZ (Độ ổn định nhu cầu theo Hệ số biến thiên `CV = σ / μ`): X (Runner — `CV < 0.5`, nhu cầu cực đều), Y (Repeater — `CV 0.5–1.0`, có mùa vụ), Z (Stranger — `CV > 1.0`, bất thường/đơn dự án).\n"
            "• Chiến lược vàng cho từng ô: AX (Đồng Rod, dây VC 1.5–4.0) → Chạy Pull/Kanban, giao hàng JIT tần suất cao, tồn kho cực tinh gọn; AZ (Cáp trung thế đặc chủng, Mica FR) → Tuyệt đối MTO (chỉ mua/sản xuất khi có đơn hàng đặt cọc); CX (Tem nhãn, màng co, ốc vít) → Dùng Two-Bin Kanban tự động!"
        ),
        "cadivi_application_extra": (
            "\n• Giúp OE & Kế hoạch CADIVI Miền Trung giải dứt điểm mâu thuẫn kinh điển: vừa không bị hết hàng dây dân dụng bán chạy (AX), vừa không bị tồn kho chết hàng chục tỷ đồng cáp dự án ít người mua (AZ/CZ)!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Phân khúc danh mục 120 mã cáp tại CADIVI): Chạy bảng Excel phân tích 12 tháng doanh số thấy chỉ 18 mã nhóm AX (dây dân dụng VC/VCm & cáp CVV phổ thông) chiếm tới 62% sản lượng nhưng nhu cầu cực đều (CV = 0.22) → Đưa 18 mã này vào sản xuất theo Bánh xe Heijunka & tồn kho siêu thị Min/Max; 45 mã nhóm AZ/BZ (cáp dự án đặc biệt) chuyển 100% sang MTO!"
        ),
        "common_mistakes": (
            "1. Xếp loại ABC chỉ dựa trên Đơn giá 1 kg thay vì Tổng giá trị tiêu thụ cả năm (`Đơn giá × Số lượng dùng năm`) — có phụ gia rất đắt/kg nhưng cả năm chỉ dùng 5 kg thì vẫn là nhóm C!"
        )
    },
    "Standard Cost": {
        "lesson_id": "L5.4",
        "definition_extra": (
            "\n• Bản chất 'Thước đo kiểm toán lợi nhuận sản xuất': Đầu năm tài chính, Kế toán phối hợp Kỹ thuật & OE thiết lập Giá thành Định mức (Standard Cost) cho mỗi km cáp dựa trên MBOM chuẩn, giờ công chuẩn và đơn giá chuẩn. Cuối mỗi tháng, so sánh Chi phí Thực tế phát sinh với Standard Cost và tách rõ 4 loại chênh lệch (Variance) để quy đúng trách nhiệm:\n"
            "  1. Material Price Variance = (Giá mua thực − Giá chuẩn) × Lượng mua → Trách nhiệm Phòng Mua hàng / biến động giá đồng sàn LME.\n"
            "  2. Material Usage / Yield Variance = (Lượng dùng thực − Định mức chuẩn) × Giá chuẩn → Mặt trận #1 của OE (Copper Give-away, Over-thickness, phế Scrap)!\n"
            "  3. Labor Efficiency Variance = (Giờ công thực − Giờ công chuẩn) × Lương chuẩn → Mặt trận #2 của OE (OLE, cân bằng chuyền, giảm tăng ca).\n"
            "  4. Overhead Absorption Variance → Mặt trận #3 của OE (tăng OEE làm tăng mẫu số sản lượng, kéo giảm khấu hao & điện cố định trên mỗi km cáp!)."
        ),
        "cadivi_application_extra": (
            "\n• Vũ khí giúp Chuyên viên OE CADIVI nói chuyện ngang hàng với Kế toán trưởng và Giám đốc Nhà máy: không đổ lỗi cho giá đồng thế giới tăng mà chỉ đích danh phần Usage Variance & Efficiency Variance mà xưởng kiểm soát được!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tách Price vs Usage Variance đồng tại CADIVI): Tháng 11 chi phí đồng vượt dự toán +1.4 tỷ VNĐ. Giám đốc tưởng xưởng làm hỏng nhiều đồng! OE tách Standard Cost Variance chỉ ra: +1.15 tỷ là do giá đồng LME tăng từ 240tr lên 248tr/tấn (Price Variance — yếu tố thị trường), còn phần xưởng thực sự tiêu hao vượt định mức (Usage Variance) là +250 triệu (+1.04 tấn đồng do đùn phế đầu ca & dư đường kính) → Đánh đúng vào 250 triệu đó!\n"
            "\n• Ví dụ 2 (Hiệu ứng Overhead Absorption): Khấu hao + lương gián tiếp xưởng Đùn cố định 600 triệu/tháng. Khi OEE 65% chạy 2,000 km cáp → Định phí = 300,000đ/km. Khi OE đẩy OEE lên 78% chạy 2,400 km cáp → Định phí giảm xuống còn 250,000đ/km (lãi thêm ngay 50,000đ/km × 2,400 km = 120 triệu/tháng tiền lãi phân bổ)!"
        ),
        "common_mistakes": (
            "1. Dùng một bộ Standard Cost cũ từ 3 năm trước chưa cập nhật định mức thực tế sau khi đã cải tiến công nghệ khiến báo cáo tháng nào cũng báo 'lãi ảo' trên giấy!"
        )
    },
    "Scrap": {
        "lesson_id": "L5.3",
        "definition_extra": (
            "\n• Phân biệt sống còn 2 khái niệm Scrap vs Rework và 3 tầng phế liệu ngành dây cáp điện:\n"
            "  - Scrap (Phế phẩm không thể bán thành phẩm chính): Phải cắt bỏ bán phế liệu hoặc bóc tách thu hồi đồng.\n"
            "  - Rework (Hàng sửa lại): Cuộn cáp bị 1 điểm Spark phải đưa sang máy Rewind cắt bỏ đoạn hỏng rồi chia thành 2 cuộn ngắn — vẫn tốn thêm công, điện, mất giá trị đơn hàng nhưng hay bị giấu khỏi báo cáo Scrap!\n"
            "• 3 Nhóm Phế liệu đặc thù CADIVI (bắt buộc cân tách riêng từng nhóm!):\n"
            "  1. Đồng trần sạch (từ máy kéo/ủ/bện chưa bọc nhựa): Tỷ lệ thu hồi giá trị cực cao (~92–95% giá đồng mới).\n"
            "  2. Đồng dính nhựa (từ máy đùn/Spark/đổi mã — NGUY HIỂM NHẤT!): Tốn công bóc tuốt hoặc bán phế đồng vỏ mất 18–25% giá trị đồng + mất trắng 100% tiền nhựa & công điện kéo–bện trước đó!\n"
            "  3. Nhựa xả Purge / nhựa cắt rìa: PVC sạch có thể nghiền tái chế Regrind; XLPE đã lưu hóa gần như mất trắng giá trị!"
        ),
        "cadivi_application_extra": (
            "\n• Trọng tâm kiểm soát hàng ngày của OE CADIVI: Luôn đo phế phẩm bằng cả tỷ lệ % khối lượng lẫn giá trị thiệt hại ròng VNĐ (Net Scrap Loss = Giá thành sản xuất − Giá bán thu hồi phế liệu) để không đánh đồng 100 kg đồng trần với 100 kg cáp XLPE hỏng!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (So sánh thiệt hại ròng 100 kg phế tại CADIVI): 100 kg đồng trần đứt ở xưởng Kéo (giá trị gốc 25.5 triệu, bán thu hồi/nấu lại 24.0 triệu → Lỗ ròng 1.5 triệu). Ngược lại 100 kg cáp đồng bọc XLPE hỏng ở máy Đùn (giá trị gốc 26 triệu, bán phế/bóc tuốt thu hồi chỉ 19.5 triệu → Lỗ ròng 6.5 triệu — ĐẮT GẤP 4.3 LẦN!).\n"
            "\n• Ví dụ 2 (Tách Startup Scrap vs Running Scrap): Khi tách riêng 2 mã phế tại xưởng Đùn phát hiện 68% lượng đồng dính nhựa đến từ đoạn xả chỉnh tâm khi khởi động/đổi mã → Đầu tư đầu đùn tự định tâm + lưu Recipe PLC cắt giảm ngay 50% tổng phế đồng dính nhựa!"
        ),
        "common_mistakes": (
            "1. Chỉ tính tỷ lệ Scrap theo kg chung chung khiến xưởng ưu tiên sửa lỗi 100 kg phế nhựa rẻ tiền (lỗ 2 triệu) mà bỏ qua 100 kg cáp đồng bọc hỏng (lỗ 6.5 triệu)!"
        )
    },
    "Regrind": {
        "lesson_id": "L4.4",
        "definition_extra": (
            "\n• Bản chất hóa học polymer quyết định khả năng tái chế:\n"
            "  - Nhựa Nhiệt Dẻo (Thermoplastic: PVC, PE chưa lưu hóa): Có cấu trúc mạch thẳng, khi gia nhiệt lại vẫn nóng chảy mềm ra nên có thể băm nghiền sạch (Regrind) pha trộn lại ở tỷ lệ kiểm soát cho các lớp ít yêu cầu khắt khe về điện môi (lớp độn trong, vỏ bảo vệ ngoài nếu qua kiểm định Lab).\n"
            "  - Nhựa Nhiệt Rắn (Thermoset: XLPE đã lưu hóa liên kết ngang): Các mạch phân tử đã khóa chặt thành mạng không gian 3 chiều — KHÔNG THỂ nấu chảy đùn lại làm cách điện!"
        ),
        "cadivi_application_extra": (
            "\n• OE CADIVI thiết lập quy chuẩn phân loại nhựa sạch ngay tại chân máy đùn (PVC sạch phân theo màu sáng/tối, tuyệt đối không dính bụi sàn/dầu mỡ/mạt đồng) kết hợp quy trình kiểm soát pha trộn có phê duyệt kỹ thuật (MOC) để tối đa hóa giá trị thu hồi mà giữ vững 100% chất lượng QCVN 4 / IEC."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Sáp nến (nhiệt dẻo như PVC) chảy ra vẫn đúc lại thành cây nến mới được; còn bánh mì đã nướng chín (nhiệt rắn như XLPE đã lưu hóa) thì không bao giờ nhào lại thành bột tươi được nữa!\n"
            "\n• Ví dụ 2 (Hiệu quả tài chính phân loại nhựa sạch tại CADIVI): Mỗi tháng xưởng Đùn xả 4.5 tấn nhựa purge PVC. Trước đây gom lẫn với nhựa đen & rác sàn bán phế giá 4,000đ/kg (thu 18 triệu). Sau khi bố trí thùng riêng tách được 3.5 tấn PVC sạch nghiền tái sử dụng cho lớp độn trong đạt chuẩn (thay thế hạt mới 22,000đ/kg), mang lại giá trị ròng thêm +63 triệu VNĐ/tháng!"
        ),
        "common_mistakes": (
            "1. Dùng nhựa nghiền Regrind cho lớp cách điện chính hoặc pha quá tỷ lệ không qua thử nghiệm Aging Oven/Tensile → Nhựa bị phân hủy nhiệt gây thủng Spark Tester và giòn nứt vỏ cáp ngoài công trình!"
        )
    },
    "Specific Gravity": {
        "lesson_id": "L4.4",
        "definition_extra": (
            "\n• Bản chất vật lý dễ làm sập giá thành cáp: Nhựa được mua theo KHỐI LƯỢNG (VNĐ/kg) nhưng lại được đùn bọc lên sợi dây theo THỂ TÍCH (cm³/km) theo hình vành khăn! Do đó khối lượng nhựa tiêu tốn cho 1 km cáp tỷ lệ thuận trực tiếp với Tỷ trọng (Specific Gravity — g/cm³): `M_nhựa (kg/km) = 0.7854 × (D_ngoài² − D_trong²) × Specific_Gravity`.\n"
            "• Dải tỷ trọng chuẩn ngành cáp: PE/XLPE: 0.92–0.94 g/cm³ | PVC cách điện: 1.35–1.45 g/cm³ | PVC vỏ: 1.42–1.55 g/cm³ | LSZH chống cháy: 1.45–1.60 g/cm³."
        ),
        "cadivi_application_extra": (
            "\n• 2 ứng dụng bắt buộc của OE CADIVI: (1) Thẩm định chào giá nhà cung cấp hạt nhựa mới bằng Chi phí trên mỗi mét khối (Volume Cost = Đơn giá/kg × Tỷ trọng) chứ không nhìn đơn giá/kg, (2) Kiểm toán BOM Variance khi xưởng kêu 'đùn đúng chiều dày mà vẫn báo vượt định mức kg nhựa'!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Bẫy giá rẻ hơn nhưng thực tế ĐẮT hơn): Nhà cung cấp A bán PVC giá 25,000đ/kg, tỷ trọng 1.44 → Volume Cost = 36,000đ/lít nhựa. Nhà cung cấp B chào rẻ hơn 2.5% là 24,375đ/kg nhưng độn nhiều bột đá nên tỷ trọng 1.53 → Volume Cost = 37,294đ/lít (+3.6% ĐẮT HƠN!). Nếu không biết Specific Gravity, công ty mua nhựa B tưởng tiết kiệm mà thực tế lỗ hàng trăm triệu/năm!\n"
            "\n• Ví dụ 2 (Truy lỗi BOM Variance ảo): Kiểm tra COA phòng Lab phát hiện lô PVC mới tỷ trọng tăng từ 1.45 lên 1.50 (+3.4%) → Giải thích ngay 100% phần chênh lệch BOM tháng đó không phải do công nhân đùn dày!"
        ),
        "common_mistakes": (
            "1. Phòng Mua hàng chỉ so sánh cột 'Đơn giá VNĐ/kg' trên bảng báo giá nhựa mà bỏ quên cột 'Tỷ trọng (Density/SG)' trong phiếu thông số kỹ thuật TDS/COA!"
        )
    },
    "Cost Deployment": {
        "lesson_id": "L5.4",
        "definition_extra": (
            "\n• Bản chất 'Định vị nguồn tiền thất thoát' — Trụ cột trung tâm của hệ quản trị World Class Manufacturing (WCM): Cost Deployment dùng chuỗi ma trận khoa học để liên kết trực tiếp giữa Kỹ thuật hiện trường và Báo cáo tài chính:\n"
            "  - Ma trận A: Liệt kê toàn bộ tổn thất tại từng công đoạn (dừng máy, phế, dư đồng, dư nhựa, điện, lao động).\n"
            "  - Ma trận B: Phân biệt Tổn thất Gốc (Causal Loss — vd: khuôn PCD mòn) vs Tổn thất Hệ quả (Resultant Loss — vd: đứt sợi + dư đường kính đồng + giảm tốc độ).\n"
            "  - Ma trận C: Quy đổi từng tổn thất gốc ra VNĐ/tháng theo Standard Cost.\n"
            "  - Ma trận D: Tính tỷ số Lợi ích/Chi phí (B/C) & độ khó triển khai để chọn Top 3–5 dự án OE ăn tiền lớn nhất triển khai trước!"
        ),
        "cadivi_application_extra": (
            "\n• Là bản đồ ưu tiên tối thượng cho Chuyên viên OE CADIVI Miền Trung mỗi quý: trình 1 bảng duy nhất cho Ban Giám đốc và Kế toán trưởng cùng ký thống nhất dự án trọng điểm, chấm dứt tình trạng làm cải tiến dàn trải không ra hiệu quả tài chính rõ rệt."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như thợ sửa ống nước kiểm tra căn nhà đang bị rò 5 chỗ — đo tốc độ chảy từng chỗ để vá ngay ống vỡ phun 100 lít/giờ trước thay vì mất cả ngày đi siết vòi nhỏ giọt 1 lít/giờ!\n"
            "\n• Ví dụ 2 (Bảng Cost Deployment Quý 1 tại CADIVI): (1) Over-thickness nhựa = 195 tr/tháng, (2) Copper Give-away = 165 tr/tháng, (3) Phế đồng dính nhựa đổi mã = 110 tr/tháng, (4) Đứt sợi kéo thô = 85 tr/tháng, (5) Rò khí nén = 24 tr/tháng → Tập trung 80% nguồn lực đánh dứt điểm mục (1), (2), (3) mang về > 3 tỷ VNĐ tiết kiệm/năm!"
        ),
        "common_mistakes": (
            "1. Đếm trùng tiền (Double Counting) giữa Tổn thất Gốc và Tổn thất Hệ quả trong Ma trận C → Phồng to con số tiết kiệm dự kiến, đến cuối dự án Kế toán đối chiếu không thấy đủ tiền!"
        )
    },
    "Headcount Planning": {
        "lesson_id": "L2.4",
        "definition_extra": (
            "\n• Bản chất bài toán hoạch định định biên nhân sự khoa học: Không bao giờ lấy `Tổng giờ công / 8 giờ` một cách ngây thơ! Một mô hình định biên chuẩn cho nhà máy sản xuất tại Việt Nam bắt buộc tính đủ 5 biến số:\n"
            "  1. Khối lượng sản phẩm & định mức công chuẩn (SAM hoặc tỷ lệ đứng đa máy Man-Machine).\n"
            "  2. Hiệu suất lao động mục tiêu thực tế (OLE — thường 75–85%, không phải 100%).\n"
            "  3. Tỷ lệ nghỉ phép năm / ốm đau / đào tạo dự phòng (Absenteeism Buffer thường 6–8%).\n"
            "  4. Đường cong học việc (Learning Curve) cho nhân sự mới tuyển.\n"
            "  5. Ràng buộc Luật Lao động Việt Nam: Giờ làm chuẩn 48h/tuần, tăng ca tối đa 40h/tháng & 200h/năm (tối đa 300h/năm với ngành đặc thù được phép) → Khi cần chạy liên tục 24/7 bắt buộc tổ chức mô hình 3 Ca – 4 Kíp!"
        ),
        "cadivi_application_extra": (
            "\n• OE CADIVI lập bảng định biên hàng quý theo kế hoạch S&OP/RCCP cho 4 phân xưởng: chứng minh rõ khi nào cần tăng năng suất OLE/đứng đa máy, khi nào cần luân chuyển công nhân đa kỹ năng (Shojinka) và khi nào mới thực sự cần tuyển mới."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tính định biên Tổ Đóng cuộn 100m tại CADIVI): Kế hoạch 1 ngày = 4,800 cuộn (SAM = 1.1 phút/cuộn → Tổng công chuẩn = 5,280 phút). Thời gian ròng 1 ca = 450 phút, OLE thực tế = 82% → Mỗi người tạo được 450 × 82% = 369 phút chuẩn/ca. Số người cần có mặt = 5,280 / 369 = 14.3 người. Nhân hệ số dự phòng nghỉ phép 7% → 14.3 × 1.07 = 15.3 → Định biên chuẩn 16 công nhân (chia 2 ca × 8 người/ca)!\n"
            "\n• Ví dụ 2 (Mở rộng 3 Ca – 4 Kíp cho máy đùn cổ chai mùa cao điểm): Thay vì bắt 2 kíp tăng ca vượt trần 40h/tháng (vừa phạm luật vừa trả lương 150–200%), dùng 4 kíp luân phiên (3 kíp chạy 8h/ca, 1 kíp nghỉ xoay vòng) giúp máy chạy 168 giờ/tuần, tăng +50% sản lượng mà công nhân vẫn đủ sức khỏe!"
        ),
        "common_mistakes": (
            "1. Tính định biên quên hệ số dự phòng nghỉ phép/ốm đau (Absenteeism) khiến chỉ cần 2 người xin nghỉ ốm là dây chuyền đóng gói thiếu người bị nghẽn ngay!\n"
            "2. Luôn chọn cách dễ nhất là 'xin tuyển thêm người' thay vì giải bài toán nâng OLE & đứng đa máy trước."
        )
    },
})


ENRICHMENTS.update({
    # =========================================================================
    # CHUNK 3: OE, SIX SIGMA, TOC, TPM & QUẢN TRỊ RỦI RO (45 THUẬT NGỮ)
    # =========================================================================
    "OE": {
        "lesson_id": "L1.1",
        "definition_extra": (
            "\n• Bản chất hệ quản trị tổng thể (Operational Excellence): Không phải là tên một công cụ đơn lẻ mà là hệ điều hành sản xuất đỉnh cao kết nối 4 mảnh ghép: (1) Chiến lược & Con người (Hoshin Kanri, ADKAR, LSW, văn hóa Genba), (2) Tốc độ & Dòng chảy (Lean, VSM, SMED, Pull/Kanban), (3) Chính xác & Ổn định (Six Sigma DMAIC, SPC, Minitab, TPM), (4) Dữ liệu & Tài chính (OEE/OLE, BOM Variance, Cost Deployment, Power BI/MES, ROI).\n"
            "• Sự khác biệt về tầm nhìn: Người làm sản xuất truyền thống lo 'hôm nay chạy đủ mét chưa?'; Chuyên viên OE lo 'làm sao ngày mai chạy nhanh hơn, ít tốn đồng/nhựa hơn, ít mệt hơn và bền vững mãi mãi!'"
        ),
        "cadivi_application_extra": (
            "\n• Đúng tên vị trí ứng tuyển tại Nhà máy CADIVI Miền Trung (KCN Hòa Cầm, Đà Nẵng): Chuyên viên OE làm cầu nối giữa Ban Giám đốc – 4 Phân xưởng Kéo/Bện/Đùn/Đóng gói – Kỹ thuật – Bảo trì – QA/QC – Kế hoạch – Kế toán để triển khai văn hóa cải tiến định lượng toàn nhà máy."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Một đội bóng muốn vô địch không chỉ cần cầu thủ chạy nhanh (Lean) hay sút chính xác (Six Sigma) mà cần cả chiến thuật, phân tích video dữ liệu đối thủ, thể lực và kỷ luật tập luyện hàng ngày — tổng thể đó chính là Operational Excellence!\n"
            "\n• Ví dụ 2 (Chuỗi tác động OE tại CADIVI trong 1 quý): Xây Dashboard OEE/BOM tự động (tốn 0đ) → Dùng Cost Deployment chọn 2 mũi nhọn lớn nhất (SMED máy đùn + SPC giảm Over-thickness) → Sau 90 ngày nâng OEE xưởng Đùn 65%→76%, giảm nhựa bọc dư 2.8% mang về > 1.5 tỷ VNĐ/năm và khóa chuẩn bằng LSW/LPA!"
        ),
        "common_mistakes": (
            "1. Nghĩ OE chỉ là 'người đi nhắc 5S' hoặc 'nhân viên thống kê làm báo cáo Excel thụ động' — OE thực thụ phải trực tiếp dẫn dắt các dự án tạo ra Hard Savings (tiền thật trên sổ Kế toán)!\n"
            "2. Dùng búa tạ đập ruồi: mở dự án Six Sigma dài 4 tháng cho vấn đề chỉ cần 1 buổi Kaizen 5S."
        )
    },
    "Six Sigma": {
        "lesson_id": "L4.2",
        "definition_extra": (
            "\n• Giải thích bản chất toán học cực kỳ dễ hiểu (từ con số 0):\n"
            "  - Mọi quy trình sản xuất đều có độ biến thiên tự nhiên biểu diễn bằng hình chuông phân phối chuẩn với Giá trị trung bình (μ) ở giữa và Độ lệch chuẩn (σ — đọc là Sigma) đo độ rộng/phân tán của dữ liệu.\n"
            "  - Khách hàng cho phép sản phẩm nằm giữa Cận dưới (LSL) và Cận trên (USL). Nếu độ lệch chuẩn σ nhỏ đến mức từ tâm μ ra tới cận dung sai chứa vừa khít 6 lần σ (tức khoảng dung sai rộng bằng 12σ), quy trình đạt trình độ Six Sigma!\n"
            "  - Ngay cả khi chạy dài hạn nhiều tháng làm tâm quy trình bị trôi lệch tự nhiên ±1.5σ (1.5 Sigma Shift), xác suất sản phẩm lọt ra ngoài chuẩn vẫn chỉ tối đa 3.4 lỗi trên 1 triệu cơ hội (3.4 DPMO) — tương đương 99.99966% đạt chuẩn!\n"
            "• So sánh thang bậc Sigma thực tế (để cảm nhận sức mạnh của 6 Sigma):\n"
            "  - Mức 2 Sigma: 308,537 DPMO (30.8% lỗi — nhà máy sắp phá sản).\n"
            "  - Mức 3 Sigma (Cpk ≈ 1.0): 66,807 DPMO (6.7% lỗi — mức trung bình thấp).\n"
            "  - Mức 4 Sigma (Cpk ≈ 1.33): 6,210 DPMO dài hạn / 63 PPM ngắn hạn (chuẩn mục tiêu tối thiểu cho hầu hết nhà máy sản xuất công nghiệp).\n"
            "  - Mức 5 Sigma (Cpk ≈ 1.67): 233 DPMO (nhà máy xuất sắc).\n"
            "  - Mức 6 Sigma (Cpk ≈ 2.0): ≤ 3.4 DPMO (hàng không, y tế, linh kiện siêu chính xác).\n"
            "• Phương trình tư duy cốt lõi `Y = f(X)`: Đầu ra lỗi (Y — vd: chiều dày vỏ cáp dao động) là hàm số của các yếu tố đầu vào (X — nhiệt độ nòng, độ ẩm nhựa, tốc độ Capstan, độ mòn khuôn). Six Sigma đi tìm đúng 2–3 biến X quan trọng nhất (Vital Few X's) để kiểm soát chặt thay vì kiểm tra mò ở đầu ra Y!"
        ),
        "cadivi_application_extra": (
            "\n• Tại Nhà máy CADIVI Miền Trung, Six Sigma giải quyết trực diện 3 bài toán ăn tiền lớn nhất mà Lean không tự giải được:\n"
            "  1. Thu hẹp độ dao động (σ) đường kính sợi đồng kéo thô/tinh → Cho phép kéo tâm đường kính sát cận dưới điện trở IEC 60228 an toàn, xóa Copper Give-away tiết kiệm nhiều tỷ đồng/năm.\n"
            "  2. Thu hẹp độ dao động (σ) chiều dày lớp nhựa cách điện & vỏ PVC/XLPE → Xóa Over-thickness nhựa thừa mà vẫn bảo đảm 100% không bị mỏng dưới chuẩn IEC 60502 / QCVN 4.\n"
            "  3. Truy tìm nguyên nhân biến thiên phức tạp gây lỗi thủng Spark Tester, lỗi rớt Hot Set Test XLPE hoặc lỗi phóng điện cục bộ PD trên cáp trung thế thông qua 5 pha DMAIC và phần mềm Minitab!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống — Bắn cung & Giao hàng): Giả sử quán pizza cam kết giao hàng trong 30 ± 5 phút (từ 25 đến 35 phút). Quán A giao lúc 15 phút, lúc 45 phút (trung bình đúng 30 phút nhưng σ = 10 phút quá lớn → 50% khách phàn nàn!). Quán B chuẩn hóa bếp giúp giao từ 28 đến 32 phút (σ = 0.8 phút → đạt chuẩn Six Sigma: gần như 100% khách hài lòng!). Đó là bản chất thu hẹp biến thiên của Six Sigma!\n"
            "\n• Ví dụ 2 (Tính toán chi tiết tại máy đùn cáp CADIVI): Dây chuyền đùn số 4 bọc cách điện XLPE có chuẩn tối thiểu LSL = 1.07 mm. Trước cải tiến, độ lệch chuẩn quá lớn `σ = 0.055 mm`, công nhân buộc phải chỉnh chạy dày trung bình tới `μ = 1.26 mm` để né lỗi mỏng (dư tới +0.19 mm nhựa, nhưng vẫn dính phế 3.8% do những điểm bị lệch tâm!). Áp dụng dự án DMAIC thu hẹp biến thiên xuống `σ = 0.020 mm` (nhờ Laser Closed-loop + sấy nhựa + bảo trì Chiller): khi đó chỉ cần chỉnh trung bình `μ = 1.15 mm` là vẫn an toàn trên 4σ (Cpk = 1.67), tỷ lệ phế rớt từ 3.8% xuống 0.78% và tiết kiệm ngay 0.11 mm nhựa bọc thừa (~950 triệu VNĐ/năm trên 1 dây chuyền)!\n"
            "\n• Ví dụ 3 (So sánh 99% vs 99.99966% trong ngành điện lực): Nếu 1 nhà máy dây cáp tự hào 'đạt 99% chất lượng' (chỉ cỡ 3.8 Sigma), nghĩa là trong 10,000 cuộn cáp xuất ra thị trường vẫn có tới 100 cuộn bị lỗi cách điện có nguy cơ gây chạm chập cháy nổ công trình! Áp dụng tư duy Six Sigma kéo lỗi trên các hạng mục an toàn điện (Spark/PD/Water Immersion) về mức cận 0 bảo vệ thương hiệu quốc gia CADIVI!"
        ),
        "common_mistakes": (
            "1. Nhầm rằng 'mọi quy trình trong nhà máy đều phải đạt đúng 6 Sigma = 3.4 DPMO': Hoàn toàn sai! Đạt 6 Sigma tốn chi phí kiểm soát rất cao — với kích thước vỏ cáp/đường kính đồng, đạt 4–5 Sigma (Cpk 1.33–1.67) đã tối ưu kinh tế; chỉ các tiêu chí an toàn cháy nổ/cao áp mới cần ép sát 6 Sigma.\n"
            "2. Lao vào chạy Minitab Six Sigma mà bỏ qua bước kiểm tra độ tin cậy thước đo (MSA Gage R&R) và bỏ qua bước làm sạch 5S/chuẩn hóa SOP của Lean trước."
        )
    },
    "Lean Six Sigma": {
        "lesson_id": "L4.2",
        "definition_extra": (
            "\n• Lộ trình phối hợp thực chiến giữa 2 nửa não của Lean Six Sigma:\n"
            "  - Nửa Lean giải quyết các vấn đề biết rõ nguyên nhân & cần tốc độ: ùn ứ WIP, đổi màu 55 phút, đi lại thừa, chờ vật tư → công cụ 5S, VSM, SMED, Kanban, Yamazumi.\n"
            "  - Nửa Six Sigma giải quyết các vấn đề chưa biết chắc nguyên nhân gốc & có biến thiên phức tạp: phế phẩm Spark nhảy thất thường giữa các ca, sai số chiều dày lớn, đứt sợi đồng khó giải thích → công cụ DMAIC, MSA, Minitab SPC, ANOVA, DOE."
        ),
        "cadivi_application_extra": (
            "\n• Chuẩn năng lực cốt lõi được nhắc đích danh trong JD tuyển dụng OE CADIVI Miền Trung: kết hợp linh hoạt Lean cho mục tiêu Năng suất (OEE/OLE/Lead Time) và Six Sigma cho mục tiêu Chất lượng & Tiết kiệm vật tư (Cpk/BOM/RTY)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Dự án kép tại Xưởng Đùn CADIVI): Dùng SMED (Lean) rút đổi mã từ 55p → 12p để tăng sản lượng +20%, đồng thời dùng DMAIC + SPC (Six Sigma) thu hẹp độ lệch chuẩn chiều dày vỏ từ 0.055 → 0.020 mm để tiết kiệm 3.2% hạt nhựa PVC/XLPE trên chính sản lượng tăng thêm đó!\n"
            "\n• Ví dụ 2 (Cách chọn công cụ nhanh khi đi phỏng vấn): Nếu hội đồng đưa bài toán 'máy chờ rulo lâu, lối đi bừa bộn' → dùng Lean (5S, Milk Run, Kanban); nếu đưa bài toán 'lỗi thủng cách điện 4% nhưng không biết do nhựa, nhiệt hay tốc độ' → dùng Six Sigma (DMAIC, ANOVA, DOE)!"
        ),
        "common_mistakes": (
            "1. Dùng Lean đơn thuần cố đẩy tốc độ máy đùn tăng nhanh nhưng bỏ qua Six Sigma → Bề mặt bị sần Sharkskin, độ lệch tâm tăng làm phế phẩm tăng vọt!"
        )
    },
    "Green Belt": {
        "lesson_id": "L4.2",
        "definition_extra": (
            "\n• Chi tiết lộ trình năng lực của 1 Chuyên viên OE đạt tầm Green Belt:\n"
            "  - Khả năng tự chủ: Trực tiếp lập Project Charter, dẫn dắt nhóm dự án 4–6 người (Sản xuất + Kỹ thuật + QA + Bảo trì), thu thập và làm sạch dữ liệu, chạy thành thạo Minitab (Cpk, MSA, t-test, ANOVA, Regression, Control Chart) và bảo vệ báo cáo A3/ROI trước Ban Giám đốc.\n"
            "  - Thời gian & tác động dự án Green Belt điển hình: Kéo dài 2–4 tháng, đem lại tiết kiệm thực (Hard Savings) từ 300 triệu – 1.5 tỷ VNĐ/dự án trong nhà máy sản xuất quy mô vừa và lớn."
        ),
        "cadivi_application_extra": (
            "\n• Điểm cộng lớn ghi trực tiếp trong JD CADIVI Miền Trung ('có Lean Six Sigma Green Belt là điểm cộng lớn'): kể cả trước khi lấy chứng chỉ ASQ/IASSC, bạn hoàn toàn có thể chứng minh trình độ tương đương Green Belt qua cách cấu trúc dự án cải tiến tại Mabuchi & giải Case Study CADIVI bằng đúng 5 pha DMAIC + p-value!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trình bày thành tích chuẩn Green Belt khi phỏng vấn): Thay vì nói 'em từng cải tiến đồ gá đo nhanh hơn', hãy trình bày đủ 5 pha DMAIC: Định lượng baseline 60s/hạng mục (Define/Measure) → Phân tích thao tác gá 1 mẫu gây lãng phí lặp lại (Analyze) → Cải tiến bệ đo 16 mẫu + Canon INEX giảm 50% thời gian đo còn 30s (Improve) → Lập hướng dẫn chuẩn hóa cho nhóm kiểm tra (Control)!\n"
            "\n• Ví dụ 2 (Dự án Green Belt đầu tiên gợi ý cho 90 ngày tại CADIVI): Chọn 1 dây chuyền đùn chủ lực đang có tỷ lệ phế & thời gian đổi mã cao nhất → Dẫn dắt dự án Green Belt giảm 40% thời gian chuyển đổi & giảm 2% nhựa dư Over-thickness."
        ),
        "common_mistakes": (
            "1. Chạy theo học thuộc lý thuyết thi lấy bằng Green Belt trên giấy nhưng chưa từng tự tay mở file Excel/Minitab phân tích dữ liệu thật từ hiện trường xưởng!"
        )
    },
    "DMAIC": {
        "lesson_id": "L4.2",
        "definition_extra": (
            "\n• Bảng kiểm đầu ra bắt buộc (Tollgate Review) cho từng pha trong 5 pha DMAIC:\n"
            "  - D (Define): Project Charter + VOC/CTQ + SIPOC → Sếp duyệt phạm vi & mục tiêu tiền.\n"
            "  - M (Measure): Data Collection Plan + MSA Gage R&R (%GRR < 10%) + Baseline Cpk/OEE/RTY.\n"
            "  - A (Analyze): Ishikawa + PFMEA + Kiểm định thống kê (t-test/ANOVA/Scatter/Chi-Square với p < 0.05) chốt đúng 2–3 nguyên nhân gốc!\n"
            "  - I (Improve): Brainstorming/DOE chọn giải pháp tối ưu + Chạy Pilot Trial + Chứng minh Trước–Sau & ROI.\n"
            "  - C (Control): Control Plan + SPC + Poka-Yoke + SOP/OPL + LSW/LPA + Bàn giao vận hành!"
        ),
        "cadivi_application_extra": (
            "\n• Khung xương chuẩn cho mọi dự án cải tiến lớn kéo dài 1–3 tháng tại CADIVI Miền Trung (giảm phế đùn XLPE, giảm đứt sợi máy kéo Multi-wire, giảm chênh lệch BOM đồng/nhựa) và là mẫu trình bày báo cáo A3 cực kỳ chuyên nghiệp."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống — Giảm hóa đơn điện gia đình): D (Giảm tiền điện từ 2.5tr xuống 1.6tr/tháng) → M (Gắn ổ cắm đo kWh từng thiết bị 1 tuần) → A (Phát hiện máy lạnh phòng ngủ cũ rò gas & tủ lạnh hở ron chiếm 75% điện) → I (Thay ron tủ lạnh & vệ sinh nạp gas máy lạnh) → C (Theo dõi app điện lực EVN mỗi tuần và đặt lịch vệ sinh 6 tháng/lần)!\n"
            "\n• Ví dụ 2 (DMAIC xử lý đứt sợi đồng tại CADIVI): D: Giảm đứt sợi máy kéo tinh từ 8.5 xuống < 2 lần/ca → M: Kiểm tra độ chính xác bộ đếm đứt sợi & thu mẫu 100 đầu gãy → A: Phân loại mặt gãy (70% Cup-and-Cone do khuôn mòn & nồng độ nhũ tương tụt dưới 3%) → I: Thay khuôn đúng chu kỳ tấn kéo + tự động châm nhũ tương giữ 5% → C: Đưa kiểm tra khúc xạ kế nhũ tương đầu ca vào Control Plan & LPA!"
        ),
        "common_mistakes": (
            "1. 'Nhảy cóc thẳng từ D sang I' (chưa đo MSA, chưa phân tích số liệu đã vội kết luận 'chắc do nhựa kém, mua máy sấy mới đi!') — 80% dự án chữa cháy thất bại vì nhảy qua bước M và A!"
        )
    },
    "SPC": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Bản chất 'Cảnh báo sớm trước khi tạo phế phẩm': Kiểm tra cuối chuyền truyền thống giống như 'khám nghiệm tử thi' (hàng đã hỏng rồi mới nhặt bỏ); còn SPC (Statistical Process Control) vẽ liên tục đường trung bình và độ dao động lên biểu đồ có Cận kiểm soát trên/dưới (`UCL / LCL = μ ± 3σ` — tiếng nói của QUÁ TRÌNH) nằm gọn bên trong Cận dung sai (`USL / LSL` — tiếng nói của KHÁCH HÀNG) để phát hiện dấu hiệu máy đang trôi lệch ngay khi sản phẩm VẪN CÒN ĐẠT CHUẨN!\n"
            "• Chọn đúng biểu đồ kiểm soát: Dữ liệu đo liên tục nhóm 2–5 mẫu (chiều dày 4 hướng lát cắt cáp) → Xbar-R Chart; Dữ liệu liên tục đo lẻ từng cuộn (điện trở 1 cuộn, chiều dài) → I-MR Chart; Dữ liệu đếm tỷ lệ % lỗi → P-Chart; Số lỗi trên mỗi km cáp (lỗi Spark/10km) → U-Chart."
        ),
        "cadivi_application_extra": (
            "\n• Triển khai cực kỳ mạnh tại CADIVI Miền Trung cho: Đường kính sợi đồng sau kéo (bắt khuôn PCD mòn từ sớm), Đường kính ngoài cáp từ Laser Gauge, Chiều dày vỏ bọc PVC/XLPE, và số lỗi Spark Tester trên 10 km dây."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Bạn lái xe trên đường cao tốc có 2 vạch sơn trắng làn đường (UCL/LCL) nằm bên trong lan can sắt bảo vệ (USL/LSL) — vừa thấy bánh xe chạm vạch sơn (cảnh báo SPC) bạn đã đánh nhẹ tay lái vào giữa ngay, không bao giờ chờ đâm vào lan can (tạo phế phẩm)!\n"
            "\n• Ví dụ 2 (SPC phát hiện khuôn kéo đồng mòn tại CADIVI): Vẽ biểu đồ I-MR đường kính sợi đồng kéo 1.78 mm sau mỗi rulo thấy 7 điểm liên tiếp tăng dần từ 1.778 → 1.781 → 1.785 mm (vi phạm Nelson Rule 3 dù chưa vượt cận khách hàng!) → Thay ngay bộ khuôn PCD cuối ca giúp chặn đứng 40 tấn đồng kéo thừa Copper Give-away!"
        ),
        "common_mistakes": (
            "1. Nhầm lẫn giữa Control Limits (UCL/LCL) với Specification Limits (USL/LSL) — vẽ thẳng cận dung sai khách hàng lên biểu đồ kiểm soát làm mất hoàn toàn khả năng cảnh báo sớm!\n"
            "2. Điều chỉnh máy liên tục sau mỗi 1 điểm đo dao động ngẫu nhiên bình thường (Tampering / Over-adjustment) — việc chỉnh tay liên tục theo nhiễu tự nhiên lại làm độ biến thiên σ TĂNG GẤP ĐÔI!"
        )
    },
    "Cpk": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Phân biệt cực dễ nhớ giữa Cp và Cpk bằng hình ảnh 'Đậu xe vào gara':\n"
            "  - Cp (Process Potential): So sánh chiều rộng gara (`USL − LSL`) với chiều rộng chiếc xe (`6σ`). Nếu `Cp = 1.5`, gara rộng gấp rưỡi xe → xe HOÀN TOÀN có khả năng đậu gọn (máy tốt, độ chụm cao!). Nhưng Cp KHÔNG quan tâm bạn có đậu xe sát tường bên phải hay không!\n"
            "  - Cpk (Process Capability Index): Tính khoảng cách từ tâm xe (`μ`) đến bức tường gần nhất (`min[(USL−μ)/3σ, (μ−LSL)/3σ]`). Nếu gara rất rộng (`Cp = 1.67`) nhưng tài xế đậu lệch sát tường phải (`Cpk = 0.70`) → Cánh cửa xe vẫn va tường gây xước (tạo phế phẩm hoặc bọc nhựa dư Over-thickness)!\n"
            "• Ngưỡng chuẩn quốc tế: `Cpk < 1.0` (Không đạt — đang tạo phế!); `1.0 ≤ Cpk < 1.33` (Tạm chấp nhận nhưng cần theo dõi sát); `Cpk ≥ 1.33` (Đạt chuẩn 4 Sigma công nghiệp); `Cpk ≥ 1.67` (Xuất sắc 5 Sigma)."
        ),
        "cadivi_application_extra": (
            "\n• Chỉ số thống kê quan trọng số 1 khi OE CADIVI chứng minh đủ điều kiện an toàn để hạ tâm chiều dày bọc nhựa (xóa Over-thickness) hoặc hạ tâm đường kính sợi đồng (xóa Copper Give-away) qua quy trình MOC!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tính cụ thể chiều dày cách điện dây VC 2.5): Chuẩn `0.80 ± 0.12 mm` (`LSL = 0.68`, `USL = 0.92`). Đo 50 mẫu: `μ = 0.87 mm`, `σ = 0.025 mm` → `Cp = 0.24 / (6×0.025) = 1.60` (máy đùn cực ổn định!), nhưng `Cpk = (0.92 − 0.87) / (3×0.025) = 0.67` (kém vì đang chạy lệch cao +0.07 mm gây tốn nhựa!). Chỉ cần hiệu chỉnh lại tốc độ Capstan kéo tâm về `μ = 0.80 mm` → `Cpk` lập tức nhảy lên `1.60` (đạt xuất sắc mà tốn 0 đồng đầu tư)!\n"
            "\n• Ví dụ 2 (Chiều dày tối thiểu chỉ có 1 cận LSL): Với chuẩn IEC chỉ quy định cận dưới `t_min = 1.07 mm`, ta dùng `Cpl = (μ − LSL) / (3σ) ≥ 1.33` để tìm chính xác chiều dày mục tiêu tiết kiệm nhựa nhất: `μ_target = LSL + 4σ`!"
        ),
        "common_mistakes": (
            "1. Tính Cpk khi quy trình CHƯA ổn định thống kê (SPC đang nhảy loạn xạ Out-of-control) hoặc dữ liệu lệch không chuẩn (Non-normal) → Con số Cpk ra sai hoàn toàn!\n"
            "2. Thấy Cpk thấp liền xin mua máy mới mà không nhìn Cp (nếu Cp cao, Cpk thấp thì chỉ cần chỉnh tâm Offset tốn 0 đồng!)."
        )
    },
    "Ppk": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Phân biệt dứt điểm Cpk vs Ppk (câu hỏi phỏng vấn Six Sigma hay gặp nhất!):\n"
            "  - Cpk dùng độ lệch chuẩn trong nhóm ngắn hạn (`σ_within`) — chỉ đo dao động tức thời bên trong cùng 1 ca/1 lô nhựa → Phản ánh năng lực tốt nhất máy có thể đạt được nếu giữ ổn định các điều kiện.\n"
            "  - Ppk dùng độ lệch chuẩn toàn bộ dài hạn (`σ_overall`) gom dữ liệu qua nhiều ngày, 3 ca vận hành, nhiều lô hạt nhựa khác nhau → Phản ánh chất lượng thực sự mà khách hàng nhận được!\n"
            "• Cách đọc cặp đôi Cpk vs Ppk: Nếu `Cpk = 1.65` (rất cao) nhưng `Ppk = 0.92` (thấp) → Bản thân máy móc rất tốt, nhưng có chênh lệch lớn giữa Ca 1 – Ca 2 – Ca 3 hoặc giữa các lô nguyên liệu/mỗi lần cài máy sau đổi mã!"
        ),
        "cadivi_application_extra": (
            "\n• Áp dụng khi OE CADIVI kiểm tra dữ liệu 30 ngày đo đường kính/chiều dày phòng Lab: so sánh Cpk trong từng ca vs Ppk gộp cả tháng để chẩn đoán chính xác lỗi do máy hay do chênh lệch thao tác giữa 3 ca!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan — Bắn bia 3 ngày): Ngày 1 bạn bắn 10 phát chụm sát nhau ở góc trên trái (Cpk ngày rất cao); Ngày 2 bắn chụm sát ở góc dưới phải (Cpk ngày cũng cao); Ngày 3 bắn chụm ở giữa → Gộp cả 3 ngày lại thì đạn rải khắp bia (`Ppk` rất thấp vì mỗi ngày chỉnh thước ngắm một kiểu!).\n"
            "\n• Ví dụ 2 (Tại Xưởng Đùn CADIVI): Phân tích 30 ngày vỏ cáp CVV ra `Cpk = 1.58` nhưng `Ppk = 0.95` → Phân tầng theo ca thấy Ca 1 chạy tâm 1.18 mm, Ca 2 chạy 1.24 mm, Ca 3 chạy 1.30 mm vì không khóa Recipe chuẩn trên HMI! Sau khi khóa Recipe dùng chung cả 3 ca, `Ppk` vọt lên 1.48!"
        ),
        "common_mistakes": (
            "1. Chỉ lấy 15 mẫu đo liên tiếp trong 10 phút rồi báo cáo đó là Ppk dài hạn — để tính Ppk tin cậy cần thu thập tối thiểu 30–100 mẫu trải dài qua nhiều ca, nhiều ngày và nhiều lô nguyên liệu!"
        )
    },
    "Gage R&R": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Cấu trúc thí nghiệm Gage R&R kinh điển trên Minitab (quy tắc 10 × 3 × 3 = 90 phép đo): Chọn 10 sản phẩm đại diện cho toàn dải biến thiên thực tế, cho 3 người kiểm tra (Appraisers) đo lặp lại mỗi sản phẩm 3 lần theo thứ tự ngẫu nhiên (không cho biết kết quả lần trước).\n"
            "• Tách rõ 2 thành phần sai số đo:\n"
            "  - Repeatability (Độ lặp lại — EV): Cùng 1 người, cùng 1 máy, đo cùng 1 mẫu nhiều lần vẫn ra số khác nhau → Lỗi do thiết bị đo (thước lỏng, cảm biến nhiễu).\n"
            "  - Reproducibility (Độ tái lập — AV): Người A và Người B đo cùng 1 mẫu lại ra 2 số lệch nhau → Lỗi do con người / thiếu SOP đo (người bóp thước Panme mạnh tay, người bóp nhẹ tay!)."
        ),
        "cadivi_application_extra": (
            "\n• Thế mạnh trực tiếp từ nền tảng Phòng Kiểm tra (Mabuchi) của bạn: Chạy Gage R&R trên Minitab trước mọi dự án cải tiến đo lường tại CADIVI (thước đo chiều dày nhựa, cầu đo điện trở Kelvin Bridge, máy đo đường kính Laser, cân kiểm tra phế)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): 3 người dùng thước dây vải mềm (dễ giãn) để đo chiều dài đoạn dây — người kéo căng tay đo ra 99.5 cm, người thả lỏng đo ra 101.0 cm (lỗi Reproducibility AV cực lớn!). Đổi sang thước thép chuẩn kèm cữ chặn thì cả 3 người đo giống hệt nhau!\n"
            "\n• Ví dụ 2 (Gage R&R đo chiều dày vỏ PVC tại CADIVI): Chạy 10 mẫu × 3 KCS × 3 lần trên Panme cơ ra `%GRR = 34.2%` (vượt ngưỡng 30% — trong đó Reproducibility AV chiếm 26% do lực kẹp nhựa PVC mềm khác nhau giữa 3 KCS!). Chuyển sang đo không tiếp xúc bằng kính hiển vi quang học (Profile Projector) kéo `%GRR` xuống còn `6.4%` (đạt xuất sắc < 10%)!"
        ),
        "common_mistakes": (
            "1. Chọn 10 mẫu giống hệt nhau từ 1 đoạn cáp dài 1 mét để làm Gage R&R → Biến thiên sản phẩm (Part-to-Part) quá bé khiến `%StudyVar GRR` bị thổi phồng giả tạo lên 80%! Phải chọn 10 mẫu trải đều dải sản xuất thực tế.\n"
            "2. Quên kiểm tra chỉ số `ndc` (Number of Distinct Categories — cần `ndc ≥ 5`) bên cạnh `%GRR`."
        )
    },
    "MSA": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Toàn cảnh 5 trụ cột của Hệ thống Phân tích Đo lường (MSA — AIAG Standard):\n"
            "  1. Bias (Độ chệch): Sai lệch giữa trung bình đo và giá trị chuẩn (kiểm bằng mẫu chuẩn Master Gauge).\n"
            "  2. Linearity (Độ tuyến tính): Sai số có đổi khi đo vật nhỏ (dây 1.5 mm²) vs vật to (cáp 300 mm²) không?\n"
            "  3. Stability (Độ ổn định): Máy đo có bị trôi theo thời gian/nhiệt độ phòng không?\n"
            "  4. Repeatability & Reproducibility (Gage R&R): Cho dữ liệu đo bằng số (Variable Data).\n"
            "  5. Attribute Agreement Analysis (Kappa): Cho dữ liệu kiểm tra ngoại quan Đạt/Hỏng bằng mắt thường (so sánh giữa các KCS với nhau và với chuyên gia chuẩn — cần `Kappa ≥ 0.75`)."
        ),
        "cadivi_application_extra": (
            "\n• Tại CADIVI Miền Trung: Ngoài Gage R&R cho thiết bị đo kích thước/điện trở, OE còn chạy Attribute MSA (Kappa) cho hạng mục kiểm tra bằng mắt dễ cãi nhau giữa Sản xuất và QA như: độ mờ chữ in phun vỏ cáp, mức độ sần vỏ nhựa, vết xước sợi đồng!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Attribute MSA kiểm tra chữ in phun vỏ cáp CADIVI): Cho 3 KCS đánh giá mù 30 mẫu đoạn vỏ cáp (gồm 15 Đạt, 15 Lỗi mờ chữ) lặp 2 lần → Ban đầu `Kappa = 0.52` (mỗi ca tự định nghĩa 'mờ' một kiểu!). Sau khi lập Bảng Mẫu Ranh Giới (Boundary Sample) trưng bày ảnh thật 'Mờ chấp nhận tối đa' vs 'Mờ loại bỏ', chạy lại Attribute MSA đạt `Kappa = 0.91`!\n"
            "\n• Ví dụ 2 (Kiểm tra Bias cầu đo điện trở): Dùng điện trở mẫu chuẩn quốc gia 1.0000 Ω kiểm tra đầu tuần đảm bảo cầu đo Kelvin Bridge không bị lệch Bias làm sai bài toán Copper Give-away."
        ),
        "common_mistakes": (
            "1. Đánh đồng 'đã có tem hiệu chuẩn (Calibration) hàng năm' nghĩa là đã đạt MSA — Calibration chỉ kiểm tra độ đúng (Bias) của bản thân thiết bị trong phòng chuẩn, KHÔNG đo sai số thao tác của người đo (Reproducibility) ở môi trường xưởng!"
        )
    },
    "Nelson Rules": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Bản chất 8 Quy tắc phát hiện 'Biến thiên bất thường (Special Cause)' trên biểu đồ SPC — trong đó 4 quy tắc OE CADIVI dùng hàng ngày:\n"
            "  - Rule 1: 1 điểm vượt ra ngoài đường `±3σ` (sự cố đột biến tức thời: mất nhiệt, rách lưới, kẹt kéo).\n"
            "  - Rule 2: 9 điểm liên tiếp nằm cùng 1 phía của đường tâm `μ` (dịch chuyển tâm quá trình: đổi lô nhựa mới có tỷ trọng khác, đổi ca vận hành chỉnh lại tốc độ!).\n"
            "  - Rule 3: 6 điểm liên tiếp tăng dần hoặc giảm dần đều (dấu hiệu mòn dần: mòn khuôn kéo PCD, nghẹt dần lưới lọc Screen Pack, tăng dần nhiệt nước làm mát buổi trưa!).\n"
            "  - Rule 4: 14 điểm liên tiếp nhảy lên–xuống luân phiên răng cưa (hai nguồn dữ liệu trộn lẫn hoặc công nhân chỉnh máy quá tay Over-adjustment!)."
        ),
        "cadivi_application_extra": (
            "\n• Bật sẵn Rule 1–4 trong Minitab và trên phần mềm giám sát Laser Gauge / SPC của CADIVI để cảnh báo công nhân & kỹ thuật xử lý sớm từ khi sản phẩm chưa hề tạo ra mét phế phẩm nào."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Rule 3 bắt khuôn PCD mòn): Đường kính sợi đồng kéo đo mỗi 2 giờ là 1.776 → 1.778 → 1.780 → 1.782 → 1.785 → 1.787 mm (6 điểm tăng liên tiếp báo hiệu Rule 3!). Dù cận trên là 1.795 mm chưa bị lỗi, xưởng lập lịch thay khuôn ngay cuối ca chặn đứng phế & dư đồng!\n"
            "\n• Ví dụ 2 (Rule 2 phát hiện lệch giữa 2 ca): Vừa chuyển giao từ Ca 1 sang Ca 2, 9 điểm đo chiều dày vỏ liên tiếp nhảy lên nằm trên đường tâm → Phát hiện ngay thợ Ca 2 tự ý hạ tốc độ Capstan cho dễ chạy làm tăng Over-thickness!"
        ),
        "common_mistakes": (
            "1. Bật cùng lúc cả 8 Nelson Rules trên dữ liệu nhạy làm hệ thống kêu báo động giả (False Alarm) liên tục — thực tế sản xuất chuẩn thường bật ưu tiên Rule 1, 2, 3 (và thêm 4 khi cần)."
        )
    },
    "2-Sample t-test": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Bản chất khoa học chống 'kết luận cảm tính': Giả sử trước SMED đổi màu trung bình 45p, sau SMED đo 5 lần được 39p — làm sao biết giảm 6 phút này là do giải pháp thực sự tốt hay chỉ do 5 lần đo sau tình cờ gặp toàn mã dễ? `2-Sample t-test` tính toán đồng thời mức chênh trung bình, độ phân tán σ của hai nhóm, và cỡ mẫu n để trả ra giá trị `p-value` kết luận chắc chắn với độ tin cậy 95%!\n"
            "• Phân biệt 2-Sample t-test vs Paired t-test: Dùng 2-Sample t-test cho 2 tập mẫu độc lập (30 ca Trước cải tiến vs 30 ca Sau cải tiến); dùng Paired t-test khi đo lặp trên CÙNG 1 đối tượng (đo cùng 15 rulo trước và sau khi qua lò ủ)."
        ),
        "cadivi_application_extra": (
            "\n• Yêu cầu trực tiếp mục 5 JD CADIVI ('Thu thập và phân tích dữ liệu Trước & Sau cải tiến'): Mọi báo cáo kết thúc dự án Pilot của bạn đều nên kèm 1 trang đồ thị Boxplot + kết quả `2-Sample t-test` xuất từ Minitab hoặc Python (`scipy.stats.ttest_ind`)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Chứng minh cải tiến SMED tại CADIVI): Nhóm Trước (n = 25 lần đổi mã): μ1 = 48.2p, s1 = 8.5p. Nhóm Sau (n = 25 lần): μ2 = 15.6p, s2 = 2.9p. Chạy 2-Sample t-test trên Minitab ra T = 18.1, p-value = 0.000 (< 0.05) với khoảng tin cậy 95% mức giảm thực là [28.9 ; 36.3 phút/lần] → Thuyết phục tuyệt đối Ban Giám đốc nhân rộng toàn xưởng!\n"
            "\n• Ví dụ 2 (Khi p-value > 0.05 cứu công ty khỏi mua nhầm phụ gia đắt tiền): Nhà cung cấp chào phụ gia mới bảo giúp tăng tốc độ đùn +10%. Chạy thử 10 ca đối chiếu bằng 2-Sample t-test ra p-value = 0.34 (> 0.05) → Chứng minh không có cải thiện thật, từ chối mua tiết kiệm 400 triệu/năm!"
        ),
        "common_mistakes": (
            "1. Dùng t-test khi dữ liệu bị lệch cực mạnh có nhiều điểm ngoại lai mà không kiểm tra Normality/Boxplot (trường hợp dữ liệu lệch mạnh nên dùng kiểm định phi tham số Mann-Whitney U Test!)."
        )
    },
    "p-value": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Cách giải thích p-value cực dễ nhớ cho cả người không chuyên toán:\n"
            "  - Mọi phép kiểm định đều bắt đầu từ Giả thuyết Gốc `H0` ('Không có gì thay đổi / Hai nhóm giống nhau / Cải tiến không có tác dụng').\n"
            "  - `p-value` là xác suất xảy ra sự chênh lệch lớn như số liệu bạn vừa đo được NẾU `H0` đúng (tức là xác suất kết quả đẹp đó chỉ do 'ăn may ngẫu nhiên').\n"
            "  - Ngưỡng cắt chuẩn công nghiệp `α = 0.05` (5%): Khi `p-value < 0.05`, khả năng ăn may dưới 5% → Đủ bằng chứng khoa học bác bỏ `H0` và tuyên bố cải tiến / sự khác biệt là THẬT!\n"
            "• Lưu ý quan trọng: `p-value < 0.05` chỉ nói về Ý nghĩa Thống kê; Chuyên viên OE luôn phải kiểm tra thêm Ý nghĩa Thực tiễn (Practical Significance) — mức giảm đó có đáng giá tiền VNĐ hay không!"
        ),
        "cadivi_application_extra": (
            "\n• Xuất hiện trong mọi bảng kết quả Minitab của OE CADIVI: 2-Sample t-test (Trước–Sau SMED), ANOVA (so sánh 3 ca / 4 máy đùn / 3 nhà cung cấp đồng), Chi-Square (tỷ lệ lỗi Spark giữa các ca), Normality Test (kiểm phân phối chuẩn trước khi tính Cpk), Regression (mức tương quan nhiệt độ–đường kính)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Đọc bảng ANOVA 3 ca xưởng Đùn): So sánh độ lệch tâm trung bình 3 ca cho `p-value = 0.004 (< 0.05)` → Khẳng định chắc chắn có ít nhất 1 ca đang vận hành khác biệt rõ rệt cần xuống Genba chuẩn hóa lại SOP!\n"
            "\n• Ví dụ 2 (Normality Test — Cẩn thận ngược chiều!): Khi chạy kiểm tra phân phối chuẩn Anderson-Darling trước khi tính Cpk, `H0` là 'Dữ liệu CÓ phân phối chuẩn' → Lúc này ta lại MONG `p-value ≥ 0.05` (dữ liệu chuẩn); nếu `p-value < 0.05` nghĩa là dữ liệu KHÔNG chuẩn, cần dùng Box-Cox!"
        ),
        "common_mistakes": (
            "1. Đọc nhầm chiều p-value ở bài kiểm tra phân phối chuẩn Normality Test (tưởng p < 0.05 là tốt trong khi p < 0.05 nghĩa là dữ liệu KHÔNG chuẩn!).\n"
            "2. Thu mẫu quá lớn (10,000 điểm đo) làm chênh lệch cực nhỏ 0.001 mm cũng ra p = 0.000 nhưng hoàn toàn vô nghĩa về mặt kinh tế."
        )
    },
    "ANOVA": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Tại sao không chạy nhiều lần t-test mà phải dùng ANOVA (Analysis of Variance) khi so sánh ≥ 3 nhóm? Nếu bạn có 4 máy đùn và đem chạy t-test từng cặp (6 cặp), xác suất mắc sai lầm báo động giả cộng dồn vọt từ 5% lên tới 26.5%! One-Way ANOVA kiểm tra đồng thời cả 4 máy chỉ bằng 1 phép tính tỷ số phương sai `F = Phương sai Giữa các nhóm / Phương sai Trong nội bộ từng nhóm` (nếu `p-value < 0.05`, dùng thêm Tukey Post-hoc Test trên Minitab để chỉ đích danh máy nào khác biệt!)."
        ),
        "cadivi_application_extra": (
            "\n• Cực kỳ phổ biến tại nhà máy nhiều máy song song như CADIVI Miền Trung: so sánh chất lượng giữa 3 Ca sản xuất, so sánh độ ổn định chiều dày giữa 6 Máy đùn, so sánh tần suất đứt sợi giữa 3 Nhà cung cấp Đồng Rod, hoặc so sánh độ bền kéo giữa 4 lô hạt nhựa PVC!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): So sánh điểm kiểm tra của 3 lớp A, B, C — nếu điểm bên trong mỗi lớp rất đều nhau nhưng điểm trung bình lớp C thấp hẳn xuống thì ANOVA cho F rất lớn và `p < 0.05`, chỉ đích danh lớp C cần hỗ trợ!\n"
            "\n• Ví dụ 2 (So sánh 3 nhà cung cấp đồng Rod tại CADIVI): Đo điện trở suất & số lần đứt sợi trên 30 cuộn mỗi nhà cung cấp A, B, C chạy One-Way ANOVA trên Minitab ra `p = 0.001` và Tukey Test chỉ rõ Nhà cung cấp C có tỷ lệ đứt sợi cao gấp 2.4 lần A & B → Đưa bằng chứng khoa học cho Phòng Mua hàng điều chỉnh tỷ trọng đặt hàng!"
        ),
        "common_mistakes": (
            "1. Quên kiểm tra tính đồng nhất phương sai (Test for Equal Variances) trước khi đọc kết quả ANOVA chuẩn — nếu 1 máy dao động rộng gấp 5 lần máy kia, phải dùng Welch's ANOVA trong Minitab!"
        )
    },
    "TOC": {
        "lesson_id": "L5.3",
        "definition_extra": (
            "\n• 5 Bước Tập Trung Liên Tục (Five Focusing Steps) kinh điển của Eliyahu Goldratt (tác giả cuốn 'The Goal'):\n"
            "  1. Identify (Xác định): Tìm chính xác đâu là ĐÚNG 1 điểm nghẽn cổ chai (Bottleneck) đang khóa sản lượng cả nhà máy.\n"
            "  2. Exploit (Khai thác tối đa — 0 đồng CAPEX): Bảo đảm cổ chai không mất 1 phút vô ích (ăn ca xoay vòng không tắt máy cổ chai, chạy SMED ngay trên cổ chai, chỉ đưa phôi đạt 100% vào cổ chai không để cổ chai gia công hàng lỗi!).\n"
            "  3. Subordinate (Đồng bộ hóa toàn xưởng theo cổ chai): Các công đoạn dư tải phía trước phải giảm nhịp chạy theo đúng tốc độ cổ chai (cơ chế Drum-Buffer-Rope) để không sinh núi WIP!\n"
            "  4. Elevate (Nâng cấp công suất cổ chai): CHỈ sau khi đã khai thác cạn Bước 2 mà vẫn thiếu tải mới đầu tư mở Ca 3, gia công ngoài hoặc mua thêm máy!\n"
            "  5. Prevent Inertia (Lặp lại — Chống sức ỳ): Khi cổ chai cũ được giải phóng, điểm nghẽn mới sẽ dịch chuyển sang công đoạn khác → Quay lại Bước 1!"
        ),
        "cadivi_application_extra": (
            "\n• Kim chỉ nam giúp OE CADIVI Miền Trung KHÔNG BAO GIỜ lãng phí thời gian đi cải tiến những công đoạn đang dư tải mà dồn toàn lực vào đúng điểm nghẽn (thường là Xưởng Đùn hoặc Giáp băng thép/Lưu hóa) để tạo tăng trưởng sản lượng & lợi nhuận nhanh nhất!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tính bằng tiền tại CADIVI): Xưởng Đùn đang là cổ chai (116% tải), mỗi giờ chạy máy tạo ra 12 triệu VNĐ giá trị đóng góp (Throughput). Nhờ Bước 2 Exploit (ăn ca luân phiên không tắt máy đùn + SMED giảm đổi mã 30p/ca), mỗi ngày cứu được thêm 2 giờ chạy cổ chai = +24 triệu/ngày ≈ +624 triệu VNĐ giá trị đóng góp/tháng mà tốn 0 đồng mua máy!\n"
            "\n• Ví dụ 2 (Dịch chuyển cổ chai — Bước 5): Sau khi Xưởng Đùn nâng OEE từ 65% → 80% hết nghẽn, cổ chai dịch chuyển sang Xưởng Bện (tải vọt lên 104%) → OE lập tức chuyển trọng tâm dự án Quý 2 sang Xưởng Bện!"
        ),
        "common_mistakes": (
            "1. Nhảy thẳng từ Bước 1 (thấy xưởng Đùn quá tải) sang Bước 4 (xin 5 tỷ mua máy đùn mới) mà bỏ qua Bước 2 Exploit (trong khi máy đùn cũ đang có OEE chỉ 62%)!"
        )
    },
    "Drum-Buffer-Rope": {
        "lesson_id": "L5.3",
        "definition_extra": (
            "\n• Chi tiết vận hành 3 vùng màu Quản trị Đệm (Buffer Management) của DBR:\n"
            "  - Vùng Xanh (Buffer đầy 67–100%): Cổ chai an toàn tuyệt đối, không cần can thiệp.\n"
            "  - Vùng Vàng (Buffer còn 34–66%): Theo dõi sát tiến độ các rulo đang chạy ở Xưởng Kéo/Bện.\n"
            "  - Vùng Đỏ (Buffer tụt dưới 33%): Cảnh báo khẩn cấp! Toàn bộ Xưởng Bện/Kéo & Bảo trì phải ưu tiên số 1 đẩy nhanh các rulo cho máy Đùn cổ chai trước khi máy Đùn bị đói hàng!"
        ),
        "cadivi_application_extra": (
            "\n• Áp dụng xuất sắc tại CADIVI Miền Trung giữa chuỗi Kéo (nhanh) → Bện (nhanh) → Đùn cách điện (Drum cổ chai): thay vì để rulo tràn ngập lối đi, chỉ duy trì 1 Buffer chuẩn (vd: 1 ca rulo đồng bện) ngay trước máy Đùn và nối dây Rope về lệnh xả đồng Rod đầu chuyền!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tính kích thước Buffer chuẩn): Xưởng Đùn chạy trung bình 12 rulo/ca; thời gian khắc phục sự cố tối đa của Xưởng Bện là 4 giờ (0.5 ca) → Đặt Buffer chuẩn 8–10 rulo trước máy Đùn (Xanh: 7–10 rulo; Vàng: 4–6 rulo; Đỏ: ≤ 3 rulo) — vừa bảo vệ tuyệt đối 0 phút đói hàng cổ chai vừa cắt giảm 50% lượng tồn kho WIP cũ!\n"
            "\n• Ví dụ 2 (Kiểm soát dây Rope): Khi Xưởng Đùn tiêu thụ xong 1 rulo đồng bện, hệ thống phát tín hiệu Rope cho Xưởng Kéo thả đúng 1 rulo đồng tương ứng vào chuyền!"
        ),
        "common_mistakes": (
            "1. Đặt Buffer sai vị trí (đặt tồn kho đệm ở SAU điểm nghẽn thay vì TRƯỚC điểm nghẽn) — đặt đệm sau cổ chai không hề bảo vệ được cổ chai khi máy phía trước bị hỏng!"
        )
    },
    "Bottleneck": {
        "lesson_id": "L5.3",
        "definition_extra": (
            "\n• 3 Cách nhận diện nhanh Bottleneck ngay trong ngày đầu xuống xưởng (không cần chờ phần mềm phức tạp):\n"
            "  1. Nhìn bằng mắt tại Genba: Công đoạn nào luôn có hàng dài rulo bán thành phẩm (WIP) xếp hàng chờ chạy phía trước nó và công đoạn ngay phía sau nó hay than thiếu hàng?\n"
            "  2. Kiểm tra dữ liệu RCCP/CRP: Công đoạn nào có tỷ lệ `Giờ yêu cầu / Giờ khả dụng thực tế` lớn nhất (≥ 95–100%)?\n"
            "  3. Đo Cycle Time dây chuyền: Trạm nào có Cycle Time dài nhất trên biểu đồ Yamazumi?\n"
            "• Quy luật vàng tài chính: Chi phí 1 giờ dừng ở máy KHÔNG phải cổ chai chỉ là chút điện/nhân công; nhưng chi phí 1 giờ dừng ở Bottleneck = Doanh thu ròng của CẢ NHÀ MÁY trong 1 giờ đó!"
        ),
        "cadivi_application_extra": (
            "\n• Ưu tiên phân bổ nguồn lực tại CADIVI Miền Trung: Ưu tiên số 1 cho Bottleneck mọi quyền lợi — lịch bảo trì PM chặt chẽ nhất, cảm biến Andon/MES gắn đầu tiên, đội SMED tập trung đầu tiên, Escalation Matrix SLA 5 phút và ăn ca luân phiên không tắt máy!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Chuyến leo núi 5 người — cả đoàn chỉ có thể lên đỉnh bằng tốc độ của người đi chậm nhất (Bottleneck); giúp người đi nhanh nhất mang bớt balo là vô ích nếu không san balo giúp người đi chậm nhất!\n"
            "\n• Ví dụ 2 (Tại CADIVI): Chuyền cáp lực CXV 3×50 có Kéo (450 kg/h), Bện (380 kg/h), Đùn XLPE (240 kg/h), Ghép lõi & Vỏ (320 kg/h) → Bottleneck duy nhất là Đùn XLPE (240 kg/h). Tập trung cải tiến tăng tốc độ & SMED Đùn XLPE lên 290 kg/h giúp sản lượng cả dây chuyền tăng ngay +20.8%!"
        ),
        "common_mistakes": (
            "1. Đi làm dự án Kaizen rầm rộ nâng tốc độ máy Kéo (đang dư 30% tải) rồi báo cáo 'tăng năng suất 25%' trong khi tổng lượng cáp xuất kho của công ty chẳng tăng thêm được 1 mét nào!"
        )
    },
    "TPM": {
        "lesson_id": "L6.1",
        "definition_extra": (
            "\n• Toàn cảnh 8 Trụ cột TPM (Total Productive Maintenance — Viện JIPM Nhật Bản) xây trên nền tảng 5S:\n"
            "  1. Bảo trì tự quản (Jishu Hozen — công nhân làm CIL hàng ngày).\n"
            "  2. Cải tiến trọng điểm (Kobetsu Kaizen — xóa 6 Big Losses).\n"
            "  3. Bảo trì có kế hoạch (Planned Maintenance — PM/PdM đạt 0 Breakdown).\n"
            "  4. Bảo trì chất lượng (Quality Maintenance — khóa điều kiện máy để 0 phế phẩm).\n"
            "  5. Quản lý thiết bị sớm (Early Equipment Management — thiết kế máy mới dễ sửa/dễ SMED).\n"
            "  6. Đào tạo & Huấn luyện (Training & Education — nâng tay nghề cơ-điện cho vận hành).\n"
            "  7. TPM văn phòng (Office TPM — xóa lãng phí giấy tờ/kế hoạch).\n"
            "  8. An toàn, Sức khỏe & Môi trường (SHE — 0 tai nạn, 0 ô nhiễm)."
        ),
        "cadivi_application_extra": (
            "\n• Cực kỳ thiết thực với đặc thù thiết bị nặng, tốc độ cao, chạy liên tục 2–3 ca của CADIVI Miền Trung: kết nối Phòng Sản Xuất và Phòng Cơ Điện thành 1 đội thống nhất thay vì đổ lỗi 'vận hành phá máy' vs 'bảo trì sửa chậm'!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Chăm sóc sức khỏe chủ động bằng ăn uống điều độ & khám định kỳ (TPM) luôn rẻ và khỏe hơn nhiều so với đợi đột quỵ mới vào phòng cấp cứu (Breakdown Maintenance)!\n"
            "\n• Ví dụ 2 (Tại Xưởng Kéo & Đùn CADIVI): Sau 6 tháng triển khai 3 trụ cột đầu TPM (5S + Jishu Hozen CIL + Planned Maintenance PM Compliance ≥ 90%), thời gian dừng máy sự cố đột xuất giảm từ 9.5% xuống 3.2% và kéo MTBF tăng gấp đôi từ 45 giờ lên 110 giờ chạy máy liên tục!"
        ),
        "common_mistakes": (
            "1. Giao hết chương trình TPM cho riêng Phòng Bảo trì làm một mình — chữ 'T' (Total) trong TPM nghĩa là TOÀN BỘ nhà máy từ Giám đốc đến công nhân đứng máy đều phải tham gia!"
        )
    },
    "Jishu Hozen": {
        "lesson_id": "L6.1",
        "definition_extra": (
            "\n• 7 Bước triển khai chuẩn Bảo trì Tự quản Jishu Hozen (không nhảy bước):\n"
            "  - Bước 1: Tổng vệ sinh ban đầu (phát hiện lỗi ẩn & gắn thẻ Fuguai).\n"
            "  - Bước 2: Xử lý tận gốc nguồn phát sinh bụi bẩn/rò rỉ & vị trí khó vệ sinh (Hard-to-Access).\n"
            "  - Bước 3: Lập tiêu chuẩn tạm thời CIL (Cleaning – Inspection – Lubrication) mất 5–10 phút/ca.\n"
            "  - Bước 4–5: Đào tạo công nhân hiểu cấu tạo khí nén/điện/truyền động để tự kiểm tra tổng quát.\n"
            "  - Bước 6–7: Chuẩn hóa quản trị trực quan toàn khu vực & tự quản hoàn toàn."
        ),
        "cadivi_application_extra": (
            "\n• Triển khai tại CADIVI giúp giải phóng đội thợ Cơ Điện khỏi hàng trăm việc lặt vặt (siết lỏng ốc, châm dầu, lau cảm biến bẩn) để họ tập trung vào bảo trì dự đoán PdM và cải tiến thiết bị lớn."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Phiếu CIL 7 phút đầu ca máy đùn CADIVI): (1) Lau sạch kính mắt đọc Laser Gauge tránh báo sai đường kính, (2) Kiểm tra mức dầu hộp giảm tốc trong vạch xanh, (3) Xả nước đọng bộ lọc khí nén, (4) Nghe tiếng kêu bất thường vòng bi quạt làm mát nòng.\n"
            "\n• Ví dụ 2 (Xử lý nguồn bẩn — Bước 2): Thay vì bắt công nhân ca nào cũng phải quét 3 kg hạt nhựa rơi vãi quanh phễu máy đùn, OE chế tạo tấm phễu hứng kín khít triệt tiêu 100% nguồn rơi vãi ngay từ gốc!"
        ),
        "common_mistakes": (
            "1. Biến Jishu Hozen thành việc đẩy hết việc nặng của thợ Bảo trì sang cho công nhân đứng máy mà KHÔNG đào tạo an toàn điện/LOTO và KHÔNG cấp đủ dụng cụ kiểm tra trực quan."
        )
    },
    "MTBF": {
        "lesson_id": "L6.1",
        "definition_extra": (
            "\n• Bản chất đo Độ tin cậy (Reliability) của thiết bị: MTBF (Mean Time Between Failures) trả lời câu hỏi 'Trung bình máy chạy êm được bao nhiêu GIỜ thì lại hỏng đột xuất 1 lần?'. MTBF càng CAO chứng tỏ máy càng bền bỉ, bảo trì phòng ngừa PM & Jishu Hozen càng tốt!\n"
            "• Lưu ý quan trọng: Chỉ tính các lần Hỏng sự cố đột xuất (Unplanned Breakdown); KHÔNG gộp dừng đổi mã SMED, dừng chờ vật tư hay bảo trì kế hoạch PM vào mẫu số số lần hỏng!"
        ),
        "cadivi_application_extra": (
            "\n• Theo dõi cặp đôi MTBF (càng cao càng tốt) & MTTR (càng thấp càng tốt) trên từng máy trọng yếu tại CADIVI Miền Trung (Máy kéo thô RBD, Máy đùn 1–6, Máy bện Rigid, Lò CCV) để đánh giá hiệu quả bảo trì cùng Phòng Cơ Điện."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Xe máy cũ cứ đi 200 km lại chết máy 1 lần (`MTBF = 200 km`) — dù sửa nhanh 10 phút cũng cực kỳ khó chịu; xe bảo dưỡng tốt đi 15,000 km không hỏng vặt (`MTBF = 15,000 km`)!\n"
            "\n• Ví dụ 2 (Tính MTBF máy kéo thô RBD trong tháng tại CADIVI): Tháng 10 máy chạy thực tế 420 giờ, xảy ra 6 lần hỏng sự cố (đứt dây curoa, lỗi biến tần, kẹt bơm dầu) → `MTBF = 420 / 6 = 70 giờ/lần hỏng`. Sau 1 quý áp dụng bảo trì dự đoán PdM (đo rung + ảnh nhiệt), số lần hỏng giảm còn 2 lần trên 440 giờ → `MTBF` tăng hơn 3 lần lên `220 giờ`!"
        ),
        "common_mistakes": (
            "1. Dùng tổng thời gian lịch 720 giờ làm tử số thay vì Thời gian máy thực sự chạy (Operating Time) → Máy nằm nghỉ không có đơn hàng cả tuần cũng làm MTBF tăng ảo!"
        )
    },
    "MTTR": {
        "lesson_id": "L6.1",
        "definition_extra": (
            "\n• Bản chất đo Tốc độ khôi phục (Maintainability) khi sự cố xảy ra: MTTR (Mean Time To Repair) tính từ lúc máy dừng vì hỏng hóc cho đến khi máy chạy lại ra sản phẩm ĐẠT CHUẨN — bao gồm trọn vẹn 4 đoạn thời gian: (1) Thời gian chờ phát hiện & gọi Bảo trì, (2) Thời gian chẩn đoán tìm ra nguyên nhân hỏng, (3) Thời gian đi tìm phụ tùng & sửa chữa, (4) Thời gian chạy thử bàn giao lại cho Sản xuất!"
        ),
        "cadivi_application_extra": (
            "\n• Cách OE CADIVI cắt giảm MTTR xuống một nửa: Rút đoạn (1) bằng đèn Andon + Escalation Matrix SLA 5 phút; rút đoạn (2) bằng Sổ tay chẩn đoán lỗi nhanh (Troubleshooting Tree) tại máy; rút đoạn (3) bằng kho phụ tùng 5S + trữ sẵn phụ tùng cốt yếu (điện trở nhiệt, dây curoa, cảm biến nhiệt cặp nhiệt điện, vòng bi chuẩn)!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Phân tách 4 đoạn MTTR sự cố cháy điện trở nhiệt máy đùn CADIVI): Tổng dừng 65 phút = Chờ báo Bảo trì 15p + Đo tìm điện trở hỏng 12p + Chạy đi tìm mua/tìm kho điện trở 20p + Thay & gia nhiệt lại 18p! Sau khi gắn cảnh báo Andon, dán sơ đồ đánh số vùng nhiệt 1–6 rõ ràng và dự trữ sẵn 2 vòng điện trở ngay tủ phụ tùng xưởng → MTTR rút xuống còn 24 phút (-63%)!\n"
            "\n• Ví dụ 2 (Liên hệ với Availability): `Availability kỹ thuật = MTBF / (MTBF + MTTR)` → Vừa tăng MTBF vừa giảm MTTR sẽ đẩy OEE Availability tăng mạnh bền vững!"
        ),
        "common_mistakes": (
            "1. Chỉ bấm giờ từ lúc thợ bảo trì cầm cờ-lê tháo ốc đến lúc siết xong ốc (bỏ quên 20 phút máy nằm chờ thợ tới và 15 phút chờ gia nhiệt chạy lại) → Che giấu 60% thời gian chết thực sự!"
        )
    },
    "PFMEA": {
        "lesson_id": "L4.2",
        "definition_extra": (
            "\n• Bản chất 'Phòng bệnh trước khi bệnh xảy ra' (Process Failure Mode and Effects Analysis): Phân tích có hệ thống TỪNG công đoạn trong quy trình sản xuất để trả lời 5 câu hỏi: (1) Bước này có thể hỏng theo kiểu nào (Failure Mode)? (2) Hậu quả với khách hàng/công đoạn sau nặng cỡ nào (S — Severity, 1–10)? (3) Nguyên nhân gây ra & tần suất xảy ra cỡ nào (O — Occurrence, 1–10)? (4) Hiện tại ta có kiểm soát phát hiện tốt không (D — Detection, 1–10, 10 là không phát hiện được)? (5) Tính điểm rủi ro `RPN = S × O × D` (hoặc mức ưu tiên Action Priority: High / Medium / Low theo chuẩn mới AIAG-VDA) và lập đối sách hạ thấp O và D ngay!\n"
            "• Lưu ý sống còn về chuẩn AIAG-VDA mới: Nếu `Severity = 9 hoặc 10` (rủi ro cháy nổ/giật điện/an toàn nghiêm trọng), BẮT BUỘC ưu tiên xử lý ngay kể cả khi RPN tổng nhỏ!"
        ),
        "cadivi_application_extra": (
            "\n• Bắt buộc dùng khi CADIVI đưa dòng cáp mới vào sản xuất (Solar H1Z2Z2-K, Mica FR, cáp trung thế XLPE), khi lắp dây chuyền mới, hoặc trong pha Analyze của dự án DMAIC & trước khi duyệt MOC/ECN."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tính RPN tại máy đùn cách điện XLPE CADIVI): Lỗi 'Hạt nhựa ẩm gây lỗ kim thủng cách điện' → Hậu quả: S = 8 (rớt thử cao áp/nguy cơ chập cháy), Tần suất hiện tại: O = 6 (thỉnh thoảng quên sấy đủ giờ), Phát hiện: D = 5 (Spark Tester phát hiện nhưng đã tạo phế) → `RPN = 8 × 6 × 5 = 240` (Rất cao!). Đối sách OE: Lắp Hopper Dryer tự động + khóa liên động PLC không cho chạy máy nếu chưa đủ nhiệt/giờ sấy → Hạ O từ 6 → 2, D từ 5 → 2 → `RPN mới = 8 × 2 × 2 = 32` (-87% rủi ro!).\n"
            "\n• Ví dụ 2 (Phân biệt DFMEA vs PFMEA): DFMEA do phòng R&D phân tích lỗi thiết kế kết cấu cáp; PFMEA do OE/Kỹ thuật sản xuất phân tích lỗi phát sinh trong quá trình chế tạo (kéo, bện, đùn, đóng gói)."
        ),
        "common_mistakes": (
            "1. Ngồi một mình trong phòng tự chấm điểm S-O-D cho xong hồ sơ audit ISO rồi cất tủ — PFMEA phải là 'tài liệu sống' làm cùng nhóm liên phòng ban (Sản xuất + QA + Bảo trì + Kỹ thuật) và cập nhật lại ngay mỗi khi có sự cố 8D hay khiếu nại khách hàng!"
        )
    },
    "Pareto": {
        "lesson_id": "L4.1",
        "definition_extra": (
            "\n• Bản chất Quy luật 80/20 (Vilfredo Pareto & Joseph Juran — 'Số ít trọng yếu vs Số nhiều thứ yếu'): Trong mọi nhà máy, khoảng 80% tổng số giờ dừng máy hoặc 80% tổng thiệt hại phế phẩm bằng tiền luôn xuất phát từ chỉ khoảng 20% số nguyên nhân gốc rễ! Biểu đồ Pareto gồm các cột xếp giảm dần từ trái sang phải kết hợp đường cong `% Tích lũy` từ 0% đến 100%, giúp OE chỉ đích danh 2–3 nguyên nhân lớn nhất cần đánh trước.\n"
            "• Kỹ thuật Pareto lồng nhau (Nested / Multi-level Pareto): Vẽ Pareto Cấp 1 tìm Xưởng tổn thất lớn nhất (Xưởng Đùn) → Vẽ Pareto Cấp 2 trong Xưởng Đùn tìm Loại lỗi lớn nhất (Đổi màu) → Vẽ Pareto Cấp 3 tìm Máy cụ thể nào đổi màu lâu nhất (Máy Đùn #2 & #4)!"
        ),
        "cadivi_application_extra": (
            "\n• Biểu đồ xuất hiện đầu tiên trong gần như mọi báo cáo tuần/tháng OE tại CADIVI Miền Trung: Pareto Nguyên nhân Downtime, Pareto Thiệt hại Phế liệu VNĐ (không chỉ kg!), Pareto Mã cáp vượt BOM cao nhất và Pareto Dạng mặt gãy đứt sợi đồng."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Mở tủ quần áo ra bạn sẽ thấy 80% thời gian bạn chỉ mặc đi mặc lại 20% số bộ đồ yêu thích nhất!\n"
            "\n• Ví dụ 2 (Pareto Downtime theo phút vs theo VNĐ tại CADIVI): Nếu đếm theo SỐ LẦN dừng máy thì 'Đứt sợi máy kéo tinh' đứng #1 (40 lần × 3 phút = 120 phút), nhưng nếu vẽ Pareto theo TỔNG THIỆT HẠI VNĐ thì 'Đổi màu máy đùn cổ chai' đứng #1 (12 lần × 45 phút = 540 phút + 250 kg nhựa purge = 95 triệu)! Luôn nhớ vẽ Pareto có trọng số theo Phút hoặc Tiền VNĐ thay vì chỉ đếm số lần!"
        ),
        "common_mistakes": (
            "1. Để cột 'Nguyên nhân khác (Others)' đứng cao nhất bên trái biểu đồ — cột 'Khác' luôn phải đặt cuối cùng bên phải, và nếu nó chiếm > 15% thì phải xuống xưởng tách nhỏ ra!"
        )
    },
    "Ishikawa": {
        "lesson_id": "L4.1",
        "definition_extra": (
            "\n• Bản chất 'Bản đồ truy tìm nguyên nhân 6M có cấu trúc' (Biểu đồ Xương Cá — Kaoru Ishikawa): Thay vì họp phân tích lỗi cứ nói chuyện lan man đổ lỗi qua lại, cả nhóm ghi Vấn đề (Đầu cá bên phải) rồi vẽ 6 xương lớn đại diện cho 6 nguồn gốc có thể gây lỗi trong sản xuất: Man (Con người/tay nghề/ca), Machine (Máy móc/khuôn/áp suất), Material (Đồng Rod/hạt nhựa/độ ẩm), Method (SOP/Recipe/trình tự), Measurement (Thước đo/Laser Gauge/hiệu chuẩn), Mother Nature / Environment (Nhiệt độ/độ ẩm xưởng/nước làm mát).\n"
            "• Bước quyết định không được quên: Sau khi vẽ xong 20 nhánh xương cá, BẮT BUỘC khoanh tròn 3–5 nguyên nhân nghi ngờ lớn nhất rồi xuống xưởng kiểm chứng bằng số liệu thực (t-test/ANOVA/thử nghiệm) — Xương cá chỉ là giả thuyết, KHÔNG phải kết luận cuối cùng!"
        ),
        "cadivi_application_extra": (
            "\n• Dùng trong mọi cuộc họp xử lý sự cố chất lượng/dừng máy liên phòng ban (8D, DMAIC pha Analyze, báo cáo A3) tại CADIVI Miền Trung để không bỏ sót bất kỳ góc nhìn nào (đặc biệt hay bỏ sót 2 xương Measurement và Environment như độ ẩm mùa mưa Đà Nẵng!)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Xương cá lỗi 'Thủng cách điện Spark Tester máy đùn XLPE' tại CADIVI): Man (công nhân chưa sấy đủ giờ ca đêm) · Machine (rách lưới Screen Pack, nhiệt đầu đùn quá cao gây Scorch) · Material (hạt nhựa XLPE hút ẩm hoặc lẫn tạp chất bụi) · Method (lưu nhựa trong nòng lâu lúc đổi mã) · Measurement (Spark Tester đặt điện áp thử quá chuẩn hoặc hiệu chuẩn sai) · Environment (phòng nạp nhựa mở cửa hở bụi & ẩm 85%).\n"
            "\n• Ví dụ 2 (Kết hợp Ishikawa + 5 Whys): Sau khi khoanh nhánh nghi ngờ nhất là 'Hạt nhựa ẩm', tiếp tục đào sâu 5 Whys trên nhánh đó để tìm tận gốc hỏng bộ sấy Hopper Dryer!"
        ),
        "common_mistakes": (
            "1. Vẽ biểu đồ xương cá cực kỳ rậm rạp 40 nhánh rồi dừng ở đó không thu thập dữ liệu kiểm chứng xem nhánh nào mới là thủ phạm thật!"
        )
    },
    "5 Whys": {
        "lesson_id": "L4.1",
        "definition_extra": (
            "\n• Bản chất 'Đào tới gốc rễ hệ thống thay vì vá triệu chứng bề mặt' (Sakichi Toyoda): Hỏi liên tiếp câu hỏi 'Tại sao?' khoảng 5 lần (có thể 3 hoặc 7 lần miễn là chạm tới gốc quy trình có thể khắc phục triệt để). Quy tắc kiểm chứng ngược Therefore Test (Kiểm tra 'Do đó'): Đọc ngược từ Why 5 lên Why 1 bằng từ 'Do đó...' phải tạo thành chuỗi nhân quả logic chặt chẽ 100%!\n"
            "• Nguyên tắc vàng: KHÔNG BAO GIỜ dừng lại ở 'Vì công nhân quên / bất cẩn' — hãy hỏi tiếp thêm 1 câu 'Tại sao quy trình cho phép công nhân quên mà không có cảnh báo Poka-Yoke?'"
        ),
        "cadivi_application_extra": (
            "\n• Công cụ bắt buộc trong mọi biên bản phân tích sự cố dừng máy > 30 phút, khiếu nại khách hàng 8D, và sự cố an toàn Near-Miss tại Nhà máy CADIVI Miền Trung."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (5 Whys kinh điển tại Xưởng Kéo CADIVI — Lỗi đứt sợi đồng liên tục): (1) Tại sao máy kéo dừng? Vì sợi đồng bị đứt giữa chừng. (2) Tại sao sợi đứt? Soi mặt gãy Cup-and-Cone do ma sát quá lớn ở khuôn số 14. (3) Tại sao ma sát quá lớn? Vòi phun dầu nhũ tương số 14 bị tắc nghẽn. (4) Tại sao vòi phun bị tắc? Bể nhũ tương nhiều mạt đồng nhỏ lọt qua lưới lọc. (5) Tại sao mạt đồng lọt qua? Lưới lọc tinh bị rách nhưng chưa có lịch kiểm tra thay định kỳ (PM) → Gốc rễ hệ thống: Bổ sung hạng mục kiểm tra/thay túi lọc tinh vào lịch PM hàng tuần + gắn đồng hồ đo áp suất bơm nhũ tương!\n"
            "\n• Ví dụ 2 (5 Whys lỗi thiếu 3m/cuộn dây): Thiếu mét → Bánh xe Encoder trượt → Cao su bánh xe mòn bóng → Chưa có lịch thay cao su & đối chiếu chiều dài chuẩn định kỳ → Đưa vào Control Plan hiệu chuẩn Encoder mỗi tuần!"
        ),
        "common_mistakes": (
            "1. Đổ lỗi cá nhân ở Why 2 ('Tại sao lỗi? Vì anh A quên bật sấy → Phạt anh A & nhắc nhở rút kinh nghiệm') → Tuần sau anh B lại quên y hệt! Phải đào sâu tới thiếu sót của quy trình/thiết kế Poka-Yoke."
        )
    },
    "8D": {
        "lesson_id": "L4.2",
        "definition_extra": (
            "\n• Chi tiết 8 kỷ luật giải quyết sự cố chuẩn toàn cầu (Ford / Ô tô / Công nghiệp điện):\n"
            "  - D0: Chuẩn bị & đánh giá khẩn cấp.\n"
            "  - D1: Thành lập đội liên phòng ban (Team).\n"
            "  - D2: Mô tả chính xác vấn đề (5W2H + Is / Is-Not).\n"
            "  - D3: Hành động ngăn chặn tức thời (Interim Containment Action — ICA): Phong tỏa kho, sàng lọc 100% bảo vệ khách hàng ngay trong 24h!\n"
            "  - D4: Xác định Nguyên nhân gốc (Root Cause — 5 Whys/Ishikawa) — phân biệt rõ Occurrence Root Cause (tại sao lỗi sinh ra?) và Escape Root Cause (tại sao QC để lọt lỗi ra ngoài?).\n"
            "  - D5: Chọn & kiểm chứng Hành động Khắc phục vĩnh viễn (PCA).\n"
            "  - D6: Triển khai PCA & gỡ bỏ biện pháp tạm D3.\n"
            "  - D7: Phòng ngừa tái diễn ngang (Yokoten — nhân rộng sang các máy/dòng cáp tương tự, cập nhật PFMEA & Control Plan).\n"
            "  - D8: Ghi nhận & khen thưởng nhóm dự án."
        ),
        "cadivi_application_extra": (
            "\n• Áp dụng tại CADIVI Miền Trung cho 2 chiều: (1) Xử lý khiếu nại khách hàng dự án điện lực/đại lý lớn một cách chuyên nghiệp, (2) Yêu cầu nhà cung cấp đồng Rod / hạt nhựa lập báo cáo 8D bồi thường khi lô nguyên liệu gây đứt sợi/lỗi PD hàng loạt!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Phân biệt sắc bén D3 Containment vs D5 Corrective Action): Nhà bị dột nước khi mưa — đặt cái xô hứng nước cho khỏi ướt sàn là D3 (Ngăn chặn tạm thời); leo lên mái thay viên ngói vỡ và chống thấm là D5 (Khắc phục vĩnh viễn); kiểm tra thay luôn toàn bộ các viên ngói cũ nứt ở phòng bên cạnh là D7 (Phòng ngừa ngang)!\n"
            "\n• Ví dụ 2 (Báo cáo 8D tại CADIVI cho lỗi cuộn dây thiếu 3m): D3: Phong tỏa kho xuất kiểm đếm lại 100% lô dây cùng ngày chạy máy đó trong 24h → D4: Tìm ra bánh xe Encoder mòn trượt (Occurrence) và thiếu bước đo đối chiếu thước chuẩn đầu ca (Escape) → D5–D6: Thay bánh xe bọc PU chống trượt + lắp cảm biến kiểm chéo → D7: Nhân rộng thay bánh xe PU & lịch hiệu chuẩn cho toàn bộ 8 máy đùn!"
        ),
        "common_mistakes": (
            "1. Nhầm lẫn D3 (kiểm tra 100% bằng mắt tạm thời) là D5 (khắc phục gốc rễ) rồi đóng luôn báo cáo 8D — dẫn tới 2 tháng sau lỗi cũ lặp lại y nguyên!"
        )
    },
    "A3": {
        "lesson_id": "L7.2",
        "definition_extra": (
            "\n• Bản chất 'Tư duy cô đọng của Toyota gói gọn trên đúng 1 trang giấy A3': Thay vì nộp báo cáo PowerPoint 45 slide dài dòng khiến Giám đốc không nắm được trọng tâm, Báo cáo A3 buộc người viết phải tư duy cực kỳ sắc nét theo dòng chảy PDCA từ trên xuống dưới, từ trái sang phải:\n"
            "  - Cột Trái (Hiểu sâu vấn đề — Plan): (1) Bối cảnh & Tầm quan trọng kinh doanh, (2) Hiện trạng bằng biểu đồ/số liệu thực, (3) Mục tiêu SMART, (4) Phân tích Nguyên nhân gốc (Pareto/Ishikawa/5 Whys).\n"
            "  - Cột Phải (Giải quyết & Duy trì — Do/Check/Act): (5) Đối sách khắc phục nhắm trúng gốc rễ, (6) Kế hoạch thực thi (Ai – Làm gì – Khi nào), (7) Kết quả Trước–Sau (t-test/ROI) & Chuẩn hóa theo dõi."
        ),
        "cadivi_application_extra": (
            "\n• Là mẫu báo cáo 'thương hiệu cá nhân' xuất sắc nhất cho Chuyên viên OE CADIVI: dùng đúng 1 tờ A3 trình bày đề xuất dự án Pilot ngày thứ 45 và tổng kết thành tích qua thử việc ngày thứ 90 trước Giám đốc Nhà máy!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như tờ sơ yếu lý lịch CV 1 trang chuẩn — mọi con số biết nói và biểu đồ cốt lõi hiện hết trong tầm mắt, đọc 3 phút hiểu trọn câu chuyện và ký duyệt ngay!\n"
            "\n• Ví dụ 2 (Tờ A3 Dự án SMED Máy Đùn #1 CADIVI): Cột trái thể hiện Biểu đồ Pareto Downtime (Đổi màu 55p chiếm 42%) + Mục tiêu giảm về < 15p trong 60 ngày + Bảng 6 thao tác Internal/External; Cột phải trình bày 4 đối sách (Color Sequencing, Tủ sấy Tip/Die 65tr, Xe 5S, Recipe HMI) + Biểu đồ cột Trước 55p → Sau 12p (`p = 0.000`, Payback 2.1 tháng) + Lịch LPA hàng tuần!"
        ),
        "common_mistakes": (
            "1. Nhồi chữ dày đặc cỡ chữ 8pt kín mít tờ A3 không có nổi 1 biểu đồ hay hình ảnh hiện trường — A3 tốt phải có ít nhất 50% là biểu đồ trực quan, bảng số liệu và ảnh chụp Trước–Sau!"
        )
    },
    "PDCA": {
        "lesson_id": "L4.2",
        "definition_extra": (
            "\n• Vòng tròn cải tiến khoa học bất hủ của W. Edwards Deming (còn gọi là PDSA — Plan-Do-Study-Act): Mọi hoạt động quản trị nhà máy (từ ISO 9001, 14001, 45001, 50001 đến Kaizen và Hoshin Kanri) đều xoay quanh 4 góc phần tư:\n"
            "  - Plan (Hoạch định): Xác định vấn đề, phân tích gốc rễ, lập kế hoạch & mục tiêu đo được.\n"
            "  - Do (Thực hiện): Chạy thử nghiệm quy mô nhỏ (Pilot) đúng kế hoạch.\n"
            "  - Check (Kiểm tra): Đối chiếu dữ liệu thực tế sau chạy thử với mục tiêu ban đầu (Đạt hay Chưa đạt? Tại sao?).\n"
            "  - Act (Hành động chuẩn hóa): Nếu Đạt → Chuẩn hóa SOP/Control Plan & nhân rộng toàn xưởng; nếu Chưa đạt → Điều chỉnh giả thuyết quay lại vòng Plan mới!"
        ),
        "cadivi_application_extra": (
            "\n• Vận hành liên tục trong các cuộc họp giao ban tuần tại CADIVI Miền Trung để mọi điểm Đỏ trên bảng OEE/BOM đều phải đóng kín đủ 4 bước PDCA (tuyệt đối không có chuyện chỉ dừng ở P–D rồi quên luôn bước C–A!)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Nấu một món mới — tìm công thức (Plan) → nấu thử 1 nồi nhỏ (Do) → nếm thử xem mặn nhạt ra sao (Check) → ghi lại công thức chuẩn để lần sau nấu tiệc lớn (Act)!\n"
            "\n• Ví dụ 2 (Vòng PDCA giảm lỗi Spark trên máy đùn #2 CADIVI): P: Đặt mục tiêu kéo lỗi Spark từ 4.5 xuống < 2 lỗi/10km bằng sấy hạt PVC 75°C trong 3 giờ → D: Chạy thử 10 ca trên máy đùn #2 → C: Đo thực tế giảm còn 1.3 lỗi/10km (đạt vượt mục tiêu!) → A: Ban hành SOP sấy bắt buộc và lắp đồng hồ hẹn giờ sấy cho toàn bộ 6 máy đùn!"
        ),
        "common_mistakes": (
            "1. Mắc bệnh 'P–D–P–D' (lập kế hoạch xong làm thử rồi bỏ đấy nhảy sang việc khác, KHÔNG BAO GIỜ quay lại Check hiệu quả và Act chuẩn hóa)!"
        )
    },
    "DOE": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Bản chất 'Thí nghiệm khoa học đa yếu tố' (Design of Experiments): Cách thử nghiệm kiểu cũ gọi là OFAT (One-Factor-At-a-Time) — chỉnh từng thông số một (tăng nhiệt trước, rồi mới tăng tốc độ) vừa tốn cực nhiều lần chạy thử vừa KHÔNG BAO GIỜ phát hiện được Hiệu ứng Tương tác (Interaction Effect) giữa 2 thông số! DOE (Full Factorial `2^k`, Fractional Factorial, Response Surface trên Minitab) thay đổi đồng thời nhiều yếu tố theo ma trận trực giao chuẩn xác để tìm ra chính xác điểm ngọt công nghệ (Process Window) chỉ với rất ít mẻ chạy thử!"
        ),
        "cadivi_application_extra": (
            "\n• Vũ khí cấp cao của OE & Kỹ thuật Công nghệ CADIVI khi tối ưu các bài toán phức tạp: đẩy tốc độ đùn tối đa mà không bị sần Sharkskin, tối ưu độ bám dính/dễ tuốt vỏ cáp CXV, tối ưu nhiệt độ–thời gian bể xông Silane đạt Hot Set Test với điện năng thấp nhất."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống — Nướng bánh): Nhiệt độ lò (180°C vs 200°C) và Thời gian nướng (20p vs 30p) tương tác chặt với nhau — nhiệt cao + thời gian dài thì cháy, nhiệt thấp + thời gian ngắn thì sống! Ma trận DOE `2² = 4` mẻ thử cho thấy ngay tổ hợp tối ưu nhất!\n"
            "\n• Ví dụ 2 (DOE `2³ = 8` mẻ thử trên dây chuyền đùn vỏ HDPE CADIVI): Khảo sát đồng thời 3 yếu tố ở 2 mức Thấp/Cao: Nhiệt Die (185 vs 200°C), Tốc độ đường dây (65 vs 85 m/p), Nhiệt nước làm mát (22 vs 32°C) → Biểu đồ Main Effects & Interaction Plot trên Minitab chỉ rõ tổ hợp (200°C – 85 m/p – 22°C) giúp tăng tốc độ +30% mà độ nhám bề mặt & co ngót vỏ đạt chuẩn 100%!"
        ),
        "common_mistakes": (
            "1. Chạy thí nghiệm DOE theo thứ tự cố định không ngẫu nhiên hóa (Randomize) và không lặp lại điểm tâm (Center Points) làm nhiễu thời gian/nhiệt độ môi trường phá hỏng kết quả phân tích!"
        )
    },
    "FPY": {
        "lesson_id": "L4.1",
        "definition_extra": (
            "\n• Bản chất 'Chất lượng trung thực không trang điểm' (First Pass Yield / Right First Time): Nếu xưởng đùn chạy 100 cuộn dây, trong đó 85 cuộn đạt thẳng còn 15 cuộn dính lỗi Spark phải chở sang máy Rewind cắt bỏ đoạn lỗi nối/chia lại thành cuộn ngắn đạt chuẩn rồi nhập kho — báo cáo Final Yield cuối tháng vẫn khoe '99% đạt chuẩn!', che giấu toàn bộ 15% nhân công, giờ máy và điện năng bị đốt trong khu sửa lỗi! FPY tính thẳng: chỉ 85/100 = 85% đạt ngay lần đầu!"
        ),
        "cadivi_application_extra": (
            "\n• OE CADIVI đưa chỉ số FPY song song với Scrap Rate vào bảng theo dõi từng phân xưởng để lôi 'Nhà máy ẩn' (máy Rewind cắt lỗi, nhân công bóc vỏ sửa lỗi, lô phải xông lại XLPE) ra ánh sáng!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Thi bằng lái xe — lớp 20 người cuối cùng cả 20 người đều có bằng (Final Yield = 100%), nhưng có 6 người phải thi lại lần 2–3 mới đậu → FPY thực chất chỉ là 14/20 = 70%!\n"
            "\n• Ví dụ 2 (Tại Xưởng Đùn CADIVI): Ca máy đùn chạy 25 rulo dây VC, 22 rulo đạt thẳng 0 lỗi Spark, 3 rulo có 1–2 điểm Spark phải đem sang máy cuộn lại cắt loại đoạn thủng → FPY = 22/25 = 88.0% (dù tỷ lệ mét phế cắt bỏ chỉ 0.6%, thực chất 12% rulo đã tốn thêm công & giờ máy sửa lại!)."
        ),
        "common_mistakes": (
            "1. Chỉ thưởng KPI cho xưởng theo Final Yield khiến tổ trưởng âm thầm dựng cả 1 tổ 'sửa hàng lỗi chui' phía sau chuyền mà Ban Giám đốc không hề hay biết chi phí đang phình to!"
        )
    },
    "RTY": {
        "lesson_id": "L4.1",
        "definition_extra": (
            "\n• Hiệu ứng nhân xác suất gây giật mình của dây chuyền nhiều công đoạn (Rolled Throughput Yield): Trong ngành dây cáp điện, sản phẩm phải đi xuyên qua 6–7 công đoạn nối tiếp độc lập. Nếu mỗi công đoạn đạt FPY = 96% (nhìn riêng từng xưởng thấy rất cao!), thì xác suất để 1 đơn hàng đi trọn 6 công đoạn KHÔNG dính bất kỳ sự cố/rework nào tụt xuống chỉ còn `0.96⁶ = 78.3%` — nghĩa là gần 22% tổng sản lượng bị kẹt vào 'Nhà máy ẩn' (Hidden Factory)!"
        ),
        "cadivi_application_extra": (
            "\n• Chỉ số cấp Giám đốc nhà máy giúp OE CADIVI Miền Trung nhìn tổng lực chất lượng xuyên suốt từ Kéo → Ủ → Bện → Đùn lõi → Lưu hóa → Ghép lõi/DSTA → Đùn vỏ/Lab thay vì nhìn rời rạc từng xưởng."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tính toán RTY 6 công đoạn cáp CXV 3×50 tại CADIVI): Kéo (98%) × Ủ/Bện (99%) × Đùn XLPE (97%) × Lưu hóa (95%) × Ghép lõi/DSTA (96%) × Đùn vỏ & Lab (97%) → `RTY = 0.98 × 0.99 × 0.97 × 0.95 × 0.96 × 0.97 = 83.27%`!\n"
            "\n• Ví dụ 2 (Tác động đòn bẩy): Thay vì cố nâng khâu Ủ/Bện đã rất cao (99% → 99.5%), OE tập trung đánh vào 2 khâu FPY thấp nhất là Lưu hóa (95% → 98.5%) và Ghép lõi (96% → 98.5%) → Đẩy RTY toàn chuỗi nhảy vọt từ 83.27% lên 88.57%!"
        ),
        "common_mistakes": (
            "1. Tính RTY bằng cách lấy trung bình cộng của 6 chỉ số FPY (97%) thay vì NHÂN tích của chúng (83.27%) → Tự đánh lừa Ban Giám đốc rằng nhà máy đang rất ổn!"
        )
    },
    "DPMO": {
        "lesson_id": "L4.1",
        "definition_extra": (
            "\n• Phân biệt sắc bén PPM vs DPMO:\n"
            "  - PPM (Parts Per Million): Đếm số sản phẩm hỏng trên 1 triệu sản phẩm (vd: 5 cuộn lỗi / 1,000 cuộn = 5,000 PPM). Nhược điểm: không công bằng khi so sánh 1 sợi dây đơn giản (chỉ có 2 tiêu chí dễ lỗi) với 1 cuộn cáp ngầm giáp thép trung thế (có tới 12 tiêu chí có thể lỗi!).\n"
            "  - DPMO (Defects Per Million Opportunities): Chia thêm cho Số cơ hội gây lỗi (Opportunities) trên mỗi đơn vị sản phẩm → Cho phép quy đổi chuẩn hóa sang Sigma Level để so sánh chất lượng giữa mọi phân xưởng và mọi ngành nghề trên thế giới!"
        ),
        "cadivi_application_extra": (
            "\n• Dùng để chuẩn hóa bảng xếp hạng chất lượng giữa Phân xưởng Dây dân dụng (ít lớp, ít cơ hội lỗi) và Phân xưởng Cáp lực/Chống cháy (nhiều lớp, nhiều cơ hội lỗi) tại CADIVI Miền Trung."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tính cụ thể tại Phòng Lab CADIVI): Kiểm tra 1,000 cuộn cáp lực, mỗi cuộn có 5 hạng mục CTQ độc lập (điện trở ruột dẫn, chiều dày cách điện, đường kính ngoài, thử cao áp Spark/Ngâm nước, độ rõ chữ in phun → tổng `1,000 × 5 = 5,000` cơ hội lỗi). Phát hiện tổng cộng 12 lỗi → `DPMO = (12 / 5,000) × 1,000,000 = 2,400 DPMO` (tương đương ~4.32 Sigma!).\n"
            "\n• Ví dụ 2 (Cạm bẫy 'thổi phồng cơ hội'): Không được tự ý chia nhỏ thành 500 cơ hội ảo để làm con số DPMO đẹp giả tạo — số cơ hội phải thống nhất chặt chẽ theo đúng các tiêu chí CTQ khách hàng quan tâm!"
        ),
        "common_mistakes": (
            "1. Đánh đồng 1 cuộn cáp bị cả 2 lỗi (vừa mờ chữ vừa mỏng vỏ) là 1 lỗi duy nhất khi tính DPMO — DPMO đếm tổng số khuyết tật (Defects = 2) chứ không đếm số sản phẩm (Defectives = 1)!"
        )
    },
    "SIPOC": {
        "lesson_id": "L4.2",
        "definition_extra": (
            "\n• Bản chất 'Bản đồ ranh giới dự án trên 1 trang giấy' (pha Define của DMAIC): Gồm đúng 5 cột từ trái sang phải (nhưng khi vẽ chuyên gia thường đi ngược từ giữa ra ngoài: vẽ 5–7 bước chính P trước → xác định đầu ra O & khách hàng C → xác định đầu vào I & nhà cung ứng S!).\n"
            "• Giá trị cực lớn: Chặn đứng căn bệnh 'phình phạm vi dự án' (Scope Creep) ngay từ ngày đầu và giúp cả 5 phòng ban cùng thấy rõ đầu vào từ xưởng trước ảnh hưởng trực tiếp tới đầu ra xưởng sau."
        ),
        "cadivi_application_extra": (
            "\n• Bắt buộc lập ở ngày đầu tiên mỗi khi OE CADIVI khởi động dự án DMAIC hoặc Kaizen Blitz liên phòng ban (vd: Dự án giảm phế đùn XLPE, Dự án rút ngắn Lead Time phòng Lab)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan — SIPOC pha 1 ly cà phê): S (Nhà cung cấp hạt cà phê, sữa, nước lọc) → I (18g bột cà phê, 50ml nước sôi, đá) → P (Xay hạt → Nén phin → Rót nước sôi → Pha sữa → Thêm đá) → O (1 ly cà phê sữa đá chuẩn vị) → C (Khách hàng uống cà phê).\n"
            "\n• Ví dụ 2 (SIPOC công đoạn Đùn lõi XLPE tại CADIVI): S (Xưởng Bện, Kho nhựa, Cơ điện) → I (Rulo đồng bện đủ mét, hạt XLPE Silane đã sấy, Recipe chuẩn, bộ Chày–Cối) → P (1. Lắp rulo & nối dây → 2. Sấy & nạp hạt → 3. Đùn & đo Laser → 4. Làm mát & Spark → 5. Thu cuộn & dán mã QR) → O (Rulo lõi XLPE đạt chuẩn chiều dày & 0 Spark) → C (Bể xông lưu hóa Sauna & Xưởng Ghép lõi)!"
        ),
        "common_mistakes": (
            "1. Vẽ cột Process (P) chi tiết quá mức thành 35 bước nhỏ li ti (biến SIPOC thành lưu đồ Flowchart) — cột P của SIPOC chuẩn chỉ nên gồm 5 đến 7 bước lớn!"
        )
    },
    "VOC": {
        "lesson_id": "L4.2",
        "definition_extra": (
            "\n• Bản chất 'Điểm khởi nguồn của mọi giá trị': VOC (Voice of Customer — mong muốn của khách hàng đại lý, nhà thầu điện lực, công đoạn kế tiếp trong xưởng) và VOB (Voice of Business — mục tiêu lợi nhuận, tồn kho, giá thành của Ban Giám đốc CADIVI). Khách hàng thường nói bằng ngôn ngữ cảm tính ('dây khó tuốt vỏ quá', 'giao hàng chậm quá', 'giá cao quá') — nhiệm vụ của OE là dịch VOC thành các chỉ tiêu kỹ thuật đo được bằng con số (CTQ)!"
        ),
        "cadivi_application_extra": (
            "\n• Giúp OE CADIVI chọn dự án cải tiến đánh trúng nỗi đau thật của khách hàng & Ban Giám đốc (tránh cải tiến những thứ rất kỹ thuật nhưng chẳng khách hàng nào quan tâm)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Cây chuyển hóa VOC → Driver → CTQ tại CADIVI): VOC nhà thầu điện: 'Cáp CXV khó bóc lớp vỏ ngoài khi đấu nối tủ điện' → Driver: Độ bám dính lớp vỏ & đường kính đồng tâm → CTQ kỹ thuật: 'Dùng kiểu đùn ống Tube Tooling chuẩn DDR 1.6–2.0, lực bóc vỏ trong dải chuẩn N/cm, không dính chảy vào lõi cách điện'.\n"
            "\n• Ví dụ 2 (VOB Ban Giám đốc → CTQ OE): VOB: 'Giảm 5% chi phí sản xuất' → CTQ: 'Tỷ lệ phế đồng dính nhựa < 0.8%, độ dày nhựa trung bình không vượt t_min + 4σ, OEE máy đùn ≥ 76%'!"
        ),
        "common_mistakes": (
            "1. Tự suy đoán khách hàng muốn gì mà không phỏng vấn trực tiếp phòng Kinh doanh, bộ phận CSKH hoặc Quản đốc công đoạn sau (khách hàng nội bộ!)."
        )
    },
    "CTQ": {
        "lesson_id": "L4.2",
        "definition_extra": (
            "\n• Bản chất 'Chuyển lời nói chung chung thành thông số có cận dung sai đo được' (Critical to Quality): Một CTQ đạt chuẩn phải có đủ 3 yếu tố: (1) Chỉ tiêu đo cụ thể + đơn vị (mm, Ω/km, pC, phút, %), (2) Cận mục tiêu & Dung sai trên/dưới (`Target / LSL / USL`), (3) Cách định nghĩa thế nào là Lỗi (Defect Definition) không thể tranh cãi!"
        ),
        "cadivi_application_extra": (
            "\n• Bộ CTQ cốt lõi của 1 cuộn cáp điện CADIVI: (1) Điện trở ruột dẫn DC 20°C ≤ trần IEC 60228, (2) Chiều dày cách điện/vỏ min ≥ `0.9×t_nom − 0.1 mm`, (3) Độ đồng tâm ≥ 85–90%, (4) Số lỗi Spark = 0, (5) Độ giãn dài nóng Hot Set XLPE đạt chuẩn, (6) Chiều dài thực trên rulo không thiếu mét (`≥ 0%` đến `+0.5%`), (7) Chữ in phun sắc nét rõ chuẩn."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): VOC khách ăn phở là 'Phở phải nóng và ngon' (mơ hồ) → Dịch sang CTQ bếp chuẩn: 'Nhiệt độ nước dùng lúc bưng ra ≥ 85°C, lượng thịt 80 ± 5g, thời gian ra món ≤ 4 phút'!\n"
            "\n• Ví dụ 2 (Tại máy đùn CADIVI): Chuyển câu 'bọc nhựa cho đều và tiết kiệm' thành CTQ rõ ràng: 'Đường kính ngoài dây VC 2.5 = 3.45 ± 0.05 mm, chiều dày min ≥ 0.72 mm, Cpk ≥ 1.33' → Dễ dàng đưa vào Minitab SPC và Control Plan!"
        ),
        "common_mistakes": (
            "1. Liệt kê 30 chỉ tiêu CTQ ngang hàng nhau làm công nhân và QA bị quá tải — chỉ chọn 3–5 thông số sống còn thực sự quyết định đạt/hỏng (Critical Few)!"
        )
    },
    "Control Plan": {
        "lesson_id": "L4.2",
        "definition_extra": (
            "\n• Bản chất 'Bản kế hoạch phòng thủ giữ vững chất lượng dài hạn' (pha Control của DMAIC & yêu cầu cốt lõi IATF/ISO): Control Plan là 1 bảng chuẩn hóa chi tiết cho TỪNG bước công đoạn gồm các cột bắt buộc: Tên bước → Thông số sản phẩm (CTQ) & Thông số máy cần giữ (Nhiệt, Áp suất, Tốc độ) → Cận chuẩn USL/LSL → Dụng cụ đo (Laser Gauge, Kính hiển vi, Spark) → Cỡ mẫu & Tần suất đo (liên tục hay mỗi 2 giờ/đầu cuộn) → Phương pháp kiểm soát (SPC/Checklist) → và quan trọng nhất: Kế Hoạch Phản Ứng (Reaction Plan) ghi rõ khi lệch chuẩn thì công nhân phải dừng máy, cô lập hàng nghi ngờ từ cuộn nào và gọi ai!"
        ),
        "cadivi_application_extra": (
            "\n• Gắn trực tiếp vào từng dây chuyền Kéo – Ủ – Bện – Đùn – Ghép lõi – Phòng Lab tại CADIVI Miền Trung để bảo đảm kể cả khi thay công nhân mới hay đổi ca đêm, quy trình vẫn cho ra sản phẩm đồng đều như một!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (1 dòng Control Plan chuẩn tại máy đùn XLPE CADIVI): Bước: Đùn cách điện | Thông số máy: Nhiệt độ sấy hạt 75±5°C & Áp suất Melt Pressure ≤ 220 bar | Thông số SP: Chiều dày cách điện ≥ 1.07 mm, đồng tâm ≥ 90% | Dụng cụ: Laser Gauge + Kính hiển vi đầu cuộn | Tần suất: Laser liên tục 100%, đo lát cắt đầu mỗi rulo | Reaction Plan: Nếu áp suất > 230 bar → báo Tổ trưởng lên lịch thay Screen Pack cuối rulo; nếu chiều dày < 1.10 mm → dừng máy hiệu chỉnh ngay và kiểm lại đoạn cáp từ mốc đo trước!\n"
            "\n• Ví dụ 2 (Kết hợp Control Plan với PFMEA): Mọi rủi ro có RPN cao trong PFMEA đều phải có ít nhất 1 biện pháp phòng ngừa/phát hiện được khóa chặt trong Control Plan!"
        ),
        "common_mistakes": (
            "1. Cột Reaction Plan chỉ ghi 1 câu sáo rỗng 'Báo tổ trưởng xử lý' mà KHÔNG nói rõ có dừng máy không, có cô lập hàng đã chạy từ lần đo trước không, chỉnh thông số gì!"
        )
    },
    "7 QC Tools": {
        "lesson_id": "L4.1",
        "definition_extra": (
            "\n• Bộ 7 vũ khí kinh điển của Kaoru Ishikawa (giải quyết tới 95% vấn đề chất lượng & năng suất thực tế tại nhà máy mà chưa cần tới toán cao cấp!):\n"
            "  1. Check Sheet (Phiếu kiểm tra): Thu thập dữ liệu nhanh, chuẩn ngay tại nguồn.\n"
            "  2. Pareto Chart: Tập trung vào 20% nguyên nhân gây 80% tổn thất.\n"
            "  3. Ishikawa / Fishbone (Xương cá 6M): Động não liệt kê nguyên nhân theo hệ thống.\n"
            "  4. Histogram: Nhìn hình dạng phân bố dữ liệu (đều, lệch hay 2 đỉnh).\n"
            "  5. Scatter Plot (Biểu đồ phân tán): Kiểm chứng tương quan giữa nguyên nhân X và kết quả Y.\n"
            "  6. Stratification (Phân tầng): Tách dữ liệu theo Ca/Máy/Lô vật tư để lật mặt nguyên nhân ẩn.\n"
            "  7. Control Chart (Biểu đồ kiểm soát SPC): Giám sát ổn định theo thời gian thực."
        ),
        "cadivi_application_extra": (
            "\n• Nền tảng đào tạo bắt buộc cho đội ngũ Tổ trưởng, KCS và công nhân nòng cốt (nhóm QCC — Quality Control Circle) tại CADIVI Miền Trung để cả xưởng cùng biết nói chuyện bằng dữ liệu!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Chuỗi phối hợp cả 7 công cụ xử lý lỗi phế máy đùn CADIVI): Dùng Check Sheet ghi lỗi 2 tuần → Vẽ Pareto thấy 'Lệch tâm vỏ cáp' chiếm 55% → Dùng Stratification tách theo máy thấy tập trung 80% ở Máy Đùn #3 → Vẽ Histogram thấy phân bố 2 đỉnh giữa Ca 1 và Ca 3 → Vẽ Ishikawa & Scatter tìm ra tương quan mạnh giữa nhiệt độ nước làm mát với độ lệch tâm → Sửa Chiller và khóa theo dõi bằng Control Chart Xbar-R!"
        ),
        "common_mistakes": (
            "1. Học thuộc lòng tên 7 công cụ để trả lời phỏng vấn nhưng không biết nối chúng thành một chuỗi điều tra từ Thu thập (Check Sheet) → Chọn trọng tâm (Pareto) → Truy gốc (Stratification/Ishikawa/Scatter) → Duy trì (Control Chart)!"
        )
    },
    "Histogram": {
        "lesson_id": "L4.1",
        "definition_extra": (
            "\n• Bản chất 'Chụp ảnh hình dáng phân bố dữ liệu': Con số trung bình (`Mean`) rất dễ lừa người (ví dụ trung bình chiều dày vỏ là 1.20 mm rất đẹp, nhưng thực tế 1 nửa chạy 1.00 mm bị mỏng lỗi còn 1 nửa chạy 1.40 mm bị dày tốn nhựa!). Histogram chia dữ liệu thành các cột khoảng giá trị để nhìn 3 giây thấy ngay 4 hình dạng cảnh báo:\n"
            "  - Hình chuông cân đối (Normal): Quá trình tự nhiên, ổn định.\n"
            "  - Hình 2 đỉnh (Bimodal — 2 ngọn núi): Chắc chắn đang trộn lẫn 2 nguồn khác nhau (2 ca chỉnh khác nhau, 2 lô nhựa, hoặc 2 máy đùn!).\n"
            "  - Hình vách đá cắt cụt (Cliff-like): Dấu hiệu công nhân đã tự lọc vứt mẫu lỗi đi trước khi giao dữ liệu cho OE!\n"
            "  - Hình lệch phải/trái (Skewed): Dữ liệu bị chặn 1 đầu (vd: thời gian dừng máy luôn ≥ 0 nên lệch phải)."
        ),
        "cadivi_application_extra": (
            "\n• Bước kiểm tra trực quan đầu tiên trong Excel / Minitab trước khi tính Cpk hay chạy t-test trên mọi tập dữ liệu đo đường kính đồng, chiều dày nhựa, điện trở hay thời gian đổi mã tại CADIVI."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Phát hiện 2 ca chỉnh tâm khác nhau qua Histogram 2 đỉnh): Vẽ Histogram 120 mẫu chiều dày vỏ cáp CXV thấy 1 đỉnh ở 1.15 mm và 1 đỉnh ở 1.29 mm → Phân tầng ngay theo ca phát hiện Ca 1 và Ca 2 đang dùng 2 bộ thông số tốc độ khác nhau!\n"
            "\n• Ví dụ 2 (Bắt tại trận lọc số liệu bằng Histogram cắt cụt): Dữ liệu phòng đo gửi lên có cột bên trái bị cắt thẳng đứng ngay tại `LSL = 1.07 mm` không có lấy 1 mẫu nào nhỏ hơn → Dấu hiệu số liệu đã bị lọc bỏ mẫu lỗi trước khi nhập báo cáo!"
        ),
        "common_mistakes": (
            "1. Vẽ Histogram với quá ít mẫu (< 30 mẫu) hoặc chọn số cột (Bins) quá ít/quá nhiều làm biến dạng hoàn toàn hình thù phân bố."
        )
    },
    "Scatter": {
        "lesson_id": "L4.1",
        "definition_extra": (
            "\n• Bản chất kiểm chứng trực quan mối liên hệ giữa 2 biến số liên tục X (nguyên nhân nghi ngờ) và Y (kết quả đầu ra): Mỗi cặp đo `(X, Y)` là 1 chấm trên mặt phẳng tọa độ.\n"
            "• Đọc hệ số tương quan Pearson `r` (từ `-1` đến `+1`):\n"
            "  - `r` gần `+1` (≥ +0.7): Tương quan thuận mạnh (X tăng → Y tăng rõ rệt).\n"
            "  - `r` gần `-1` (≤ -0.7): Tương quan nghịch mạnh (X tăng → Y giảm rõ rệt).\n"
            "  - `r` gần `0` (-0.3 đến +0.3): Gần như không liên quan tuyến tính!\n"
            "• Quy tắc vàng thống kê: Tương quan (Correlation) chưa chắc đã là Nhân quả (Causation) — luôn phải kiểm chứng lại bằng cơ chế vật lý hoặc thử nghiệm thực tế!"
        ),
        "cadivi_application_extra": (
            "\n• Dùng trong pha Analyze tại CADIVI để kiểm chứng ngay các giả thuyết của xưởng: Nhiệt độ nước máng làm mát (X) vs Độ méo/lệch tâm vỏ cáp (Y); Tốc độ kéo (X) vs Nhiệt độ sợi đồng (Y); % IACS đồng đầu vào (X) vs Khối lượng đồng tiêu hao/km (Y)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan — Cảnh giác tương quan giả): Thống kê thấy số người ăn kem (X) tăng tỷ lệ thuận cực mạnh (`r = +0.92`) với số người bị cháy nắng (Y) — không phải ăn kem gây cháy nắng mà cả 2 cùng do yếu tố thứ 3 là Trời nắng nóng!\n"
            "\n• Ví dụ 2 (Tại Xưởng Đùn CADIVI): Xưởng nghi ngờ tốc độ đùn nhanh gây tăng lỗi Spark. Vẽ Scatter 40 ca giữa Tốc độ (X) và Lỗi Spark (Y) ra `r = 0.12` (không liên quan!), nhưng vẽ giữa Độ ẩm không khí xưởng (X) và Lỗi Spark (Y) lại ra `r = +0.84` → Xác định đúng thủ phạm là độ ẩm hạt nhựa, không cần giảm tốc độ máy!"
        ),
        "common_mistakes": (
            "1. Kết luận 'không có liên hệ' khi `r ≈ 0` mà quên nhìn đồ thị Scatter — có những quan hệ phi tuyến hình chữ U (vd: nhiệt đùn quá thấp lẫn quá cao đều gây lỗi bề mặt!) khiến `r` tuyến tính gần bằng 0 dù quan hệ cực chặt!"
        )
    },
    "Chi-Square": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Bản chất kiểm định thống kê dành riêng cho Dữ liệu Đếm / Phân loại (Attribute / Categorical Data: Đạt vs Lỗi, Có vs Không, Ca 1/2/3, Nhà cung cấp A/B/C): Khi dữ liệu không phải là con số đo mm hay giây mà là bảng đếm tần suất (Contingency Table), ta KHÔNG dùng được t-test hay ANOVA — lúc này Chi-Square Test (`χ²`) trên Minitab/Excel sẽ kiểm tra xem tỷ lệ % lỗi giữa các nhóm có thực sự khác nhau (`p-value < 0.05`) hay chỉ do ngẫu nhiên!"
        ),
        "cadivi_application_extra": (
            "\n• Rất hay dùng tại CADIVI Miền Trung cho các dữ liệu phân loại: So sánh tỷ lệ cuộn Đạt/Lỗi Spark giữa 3 ca; so sánh tỷ lệ rớt thử cao áp ngâm nước giữa 2 nhà cung cấp hạt nhựa PVC; so sánh tỷ lệ đứt sợi theo nhóm mặt gãy giữa 3 nhà cung cấp đồng Rod!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (So sánh tỷ lệ cuộn lỗi giữa 3 Ca tại CADIVI): Trong 1 tháng, Ca 1 có 8 lỗi / 400 cuộn (2.0%), Ca 2 có 10 lỗi / 400 cuộn (2.5%), Ca 3 có 26 lỗi / 400 cuộn (6.5%). Chạy Stat → Tables → Chi-Square Test trên Minitab cho `p-value = 0.001 (< 0.05)` → Khẳng định chắc chắn Ca 3 đang có vấn đề hệ thống thực sự chứ không phải xui xẻo!\n"
            "\n• Ví dụ 2 (Kiểm chứng Poka-Yoke): Trước lắp cảm biến đứt băng Mica có 18 cuộn lỗi / 200 cuộn; sau lắp còn 2 cuộn lỗi / 200 cuộn → Chi-Square ra `p = 0.0002` chứng minh hiệu quả tuyệt đối!"
        ),
        "common_mistakes": (
            "1. Dùng bảng tỷ lệ % (2.0%, 6.5%) đưa vào Chi-Square thay vì nhập số đếm nguyên thực tế (8 cuộn lỗi, 392 cuộn đạt) → Kết quả p-value sẽ sai hoàn toàn!"
        )
    },
    "Regression": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Bản chất 'Tìm phương trình toán học dự báo Y theo X' (`Y = b0 + b1·X1 + b2·X2 + ...`): Trong khi Scatter mới chỉ cho thấy X và Y có đi cùng nhau không, Phân tích Hồi quy (Regression) xây dựng công thức toán học chính xác để dự báo 'Nếu tôi tăng X thêm 1 đơn vị thì Y thay đổi chính xác bao nhiêu đơn vị?'.\n"
            "• 2 chỉ số bắt buộc phải đọc trên Minitab: (1) `p-value < 0.05` (mô hình & hệ số có ý nghĩa thống kê), (2) `R-sq (R²)` từ 0%–100% cho biết các biến X giải thích được bao nhiêu % sự biến động của Y (trong sản xuất `R² ≥ 70%` là mô hình dự báo rất tốt!)."
        ),
        "cadivi_application_extra": (
            "\n• Ứng dụng thực chiến cao cấp của OE CADIVI: Dựng phương trình dự báo điện năng tiêu thụ `kWh` theo tấn sản lượng & tiết diện cáp (đường cơ sở năng lượng EnB cho ISO 50001), hoặc dự báo chiều dày vỏ cáp theo tỷ số `Tốc độ trục vít / Tốc độ Capstan`!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Đường cơ sở năng lượng ISO 50001 tại CADIVI): Chạy hồi quy giữa Sản lượng X (tấn/tháng) và Tổng điện năng Y (kWh/tháng) ra phương trình: `Y = 48,000 + 380 × X` (`R² = 91.5%`, `p = 0.000`). Con số `48,000 kWh` chính là điện năng nền không tải (Base Load) (chiếu sáng, rò khí nén, Chiller/đùn chờ nhiệt) dù không sản xuất tấn cáp nào vẫn mất tiền — mục tiêu vàng để OE cắt giảm!\n"
            "\n• Ví dụ 2 (Dự báo thời gian đổi mã): Hồi quy cho thấy chênh lệch nhiệt độ và độ đậm màu giải thích tới 82% thời gian xả nhựa Purge."
        ),
        "common_mistakes": (
            "1. Ngoại suy vượt xa vùng dữ liệu đã đo (vd: đo dữ liệu chạy 200–400 tấn rồi thay X = 1,000 tấn vào công thức dự báo) và quên kiểm tra biểu đồ phần dư (Residual Plots)!"
        )
    },
    "Box-Cox": {
        "lesson_id": "L4.3",
        "definition_extra": (
            "\n• Bản chất 'Bộ chuyển đổi chuẩn hóa dữ liệu bị lệch (Non-Normal Data)': Rất nhiều dữ liệu thực tế trong sản xuất (như độ lệch tâm vỏ cáp — luôn ≥ 0, thời gian đổi mã SMED, thời gian sửa máy MTTR) bị lệch đuôi sang phải nên KHÔNG theo phân phối chuẩn hình chuông (Normality Test `p < 0.05`). Nếu cứ cố áp công thức Cpk chuẩn bình thường sẽ ra kết quả sai lệch thảm hại! Phép biến đổi Box-Cox (`Y' = Y^λ` hoặc `ln(Y)` khi `λ = 0`) kéo dữ liệu về phân phối chuẩn đối xứng để tính chính xác Cpk/SPC trên Minitab!"
        ),
        "cadivi_application_extra": (
            "\n• Kỹ thuật 'ăn điểm chuyên gia Minitab' tại CADIVI khi phân tích năng lực quy trình cho các chỉ tiêu 1 cận bị lệch tự nhiên như: Độ lệch tâm cách điện (Eccentricity mm), Thời gian chuyển đổi SMED, hay Mức phóng điện cục bộ PD (pC)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như dùng kính lúp đặc biệt biến một bức ảnh bị méo góc trở nên thẳng hàng cân đối để đo đạc chính xác kích thước bên trong!\n"
            "\n• Ví dụ 2 (Tính Cpk độ lệch tâm vỏ cáp trên Minitab): Độ lệch tâm đo trên 60 mẫu dao động từ 0.01 đến 0.14 mm (bị lệch phải, Anderson-Darling `p = 0.002 < 0.05`). Bật tùy chọn `Transform → Box-Cox (Optimal λ = 0 — dùng ln(Y))` trong Minitab Capability Analysis giúp tính ra `Cpk = 1.41` chính xác thay vì con số ảo sai lệch `0.95` nếu để nguyên dữ liệu lệch!"
        ),
        "common_mistakes": (
            "1. Dùng Box-Cox khi dữ liệu có giá trị ≤ 0 (toán học Box-Cox yêu cầu toàn bộ giá trị đầu vào phải dương `Y > 0`; nếu có số 0 hoặc số âm phải dùng Johnson Transformation hoặc phân tích phân phối Weibull/Lognormal!)."
        )
    },
    "PM Compliance": {
        "lesson_id": "L6.1",
        "definition_extra": (
            "\n• Bản chất 'Kỷ luật thực thi bảo trì phòng ngừa' (Quy tắc 10% chuẩn SMRP): Một đầu việc PM định kỳ 30 ngày chỉ được tính là 'Đúng hạn' nếu hoàn thành trong cửa sổ ±3 ngày (±10% chu kỳ). Nếu làm sớm quá thì lãng phí vật tư, làm trễ quá thì máy có nguy cơ hỏng trước khi kịp bảo dưỡng!\n"
            "• Cặp chỉ số song sinh với PM Compliance: Schedule Compliance (tỷ lệ hoàn thành đúng lịch bảo trì tuần ≥ 85%) và Planned vs Reactive Ratio (≥ 80% công việc là có kế hoạch, < 20% là chữa cháy đột xuất!)."
        ),
        "cadivi_application_extra": (
            "\n• OE CADIVI đóng vai trò trọng tài công bằng giữa Phòng Sản Xuất (hay giữ máy chạy đơn hàng không chịu giao cho Bảo trì làm PM) và Phòng Cơ Điện (cần khung giờ PM cố định trong lịch MPS/CRP hàng tuần) để nâng PM Compliance lên ≥ 90%."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Định kỳ 5,000 km phải thay nhớt xe máy — nếu bận quá cứ cố chạy đến 9,000 km mới thay (PM Compliance kém) thì đến 8,500 km bó máy tốn tiền sửa gấp 20 lần tiền thay nhớt!\n"
            "\n• Ví dụ 2 (Tại CADIVI): Chốt khung 'Cửa sổ Bảo trì Vàng' cố định 4 giờ mỗi sáng Chủ nhật xen kẽ từng cụm máy kéo/đùn vào lịch MPS → Đẩy PM Compliance từ 58% lên 93%, giúp giảm 48% sự cố Breakdown đột xuất giữa ca trong quý tiếp theo!"
        ),
        "common_mistakes": (
            "1. Đạt PM Compliance 100% 'trên giấy' bằng cách tick đại vào danh sách kiểm tra mà không thực sự mở máy thay lọc/bôi trơn — luôn kiểm chéo PM Compliance với xu hướng giảm Breakdown thực tế (MTBF phải tăng!)."
        )
    },
    "Wrench Time": {
        "lesson_id": "L6.1",
        "definition_extra": (
            "\n• Bản chất 'Hiệu suất sử dụng thời gian thực của kỹ thuật viên bảo trì' (Hands-on-Tool Time): Trong 8 tiếng đi làm của 1 thợ Cơ Điện nhà máy truyền thống, đo thực tế bằng Work Sampling thường gây sốc — họ chỉ dành khoảng 25–35% thời gian thực sự cầm dụng cụ sửa/bảo dưỡng máy! Còn 65–75% thời gian bị đốt vào: chờ lệnh giao việc, đi bộ sang kho chờ thủ kho tìm bạc đạn/điện trở, chờ sản xuất bàn giao máy & làm thủ tục LOTO, hoặc đi lấy thiếu cờ-lê phải quay lại xưởng bảo trì!\n"
            "• Mục tiêu thực tế đẳng cấp thế giới: 55% – 65% (không bao giờ là 100% vì thợ bảo trì vẫn cần thời gian di chuyển, an toàn LOTO và bàn giao)."
        ),
        "cadivi_application_extra": (
            "\n• Giải pháp không tốn tiền tuyển thêm người cho Phòng Cơ Điện CADIVI Miền Trung: Dùng OE Work Sampling đo Wrench Time, tổ chức kho phụ tùng 5S theo mã máy, soạn sẵn bộ Kitting phụ tùng PM trước 1 ngày và chuẩn hóa xe đẩy dụng cụ di động!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Bài toán nhân lực kỳ diệu tại CADIVI): Đội Cơ Điện có 8 kỹ thuật viên, Wrench Time hiện tại = 32% (tương đương 8 × 0.32 = 2.56 người làm kỹ thuật liên tục). Sau khi áp dụng Kitting phụ tùng PM + 5S kho vật tư + lập lịch giao máy rõ ràng nâng Wrench Time lên 48% (= 3.84 người) → Tăng thêm +50% năng lực bảo trì tương đương tuyển miễn phí thêm 4 thợ giỏi!\n"
            "\n• Ví dụ 2 (Lưu ý giao tiếp): Giống như OLE, đo Wrench Time là để phơi bày các rào cản hành chính/kho vận đang làm khổ anh em thợ bảo trì, tuyệt đối không dùng để soi mói phạt cá nhân thợ!"
        ),
        "common_mistakes": (
            "1. Nghĩ Wrench Time thấp là do 'thợ bảo trì lười biếng' — thực tế > 85% nguyên nhân lãng phí Wrench Time thuộc về hệ thống lập kế hoạch bảo trì kém và quản lý kho phụ tùng lộn xộn!"
        )
    },
    "CBM / PdM": {
        "lesson_id": "L6.1",
        "definition_extra": (
            "\n• Tiến hóa 4 thế hệ bảo trì công nghiệp (từ tệ nhất đến đỉnh cao):\n"
            "  1. Reactive / Breakdown (Hỏng mới sửa): Rẻ lúc bình thường nhưng thiệt hại cực nặng khi máy cổ chai gãy trục giữa mùa cao điểm.\n"
            "  2. Preventive — PM (Thay định kỳ theo lịch): Tốt hơn nhưng hay thay lãng phí linh kiện vẫn còn dùng tốt, hoặc vẫn hỏng sớm hơn lịch.\n"
            "  3. Condition-Based / Predictive Maintenance (CBM / PdM): Theo dõi trực tiếp 'dấu hiệu sinh tồn' của máy (đường cong P–F: Siêu âm → Rung động → Dầu bôi trơn → Nhiệt độ nóng → Nghe tiếng kêu → Hỏng hẳn!) để thay đúng linh kiện, đúng lúc trước khi hỏng!\n"
            "  4. Prescriptive / AIoT: Hệ thống tự chẩn đoán và lên lệnh đặt phụ tùng bảo trì tự động."
        ),
        "cadivi_application_extra": (
            "\n• Chi phí đầu tư siêu thấp nhưng hiệu quả cứu nguy cực cao tại CADIVI Miền Trung: (1) Camera ảnh nhiệt soi tủ điện biến tần/điện trở đùn/vòng bi mỗi tháng, (2) Bút đo rung động bạc đạn máy kéo thô RBD & máy bện, (3) Thiết bị siêu âm phát hiện rò rỉ khí nén, (4) Theo dõi xu hướng Melt Pressure máy đùn trên MES!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Xét nghiệm máu định kỳ phát hiện chỉ số đường huyết mới hơi cao (Điểm P trên đường cong P–F) để điều chỉnh ăn uống ngay, tránh đợi nhập viện cấp cứu (Điểm F)!\n"
            "\n• Ví dụ 2 (Cứu cháy tủ điện máy đùn CADIVI): Đầu tư 1 camera ảnh nhiệt cầm tay giá ~25 triệu đồng — lần soi định kỳ đầu tiên phát hiện 1 đầu cos cầu dao tổng máy đùn số 3 nóng bất thường 108°C (so với 41°C hai pha còn lại) do lỏng tiếp điểm → Siết lại trong 15 phút nghỉ trưa, ngăn chặn 1 vụ cháy tủ điện mất 3 ngày sản xuất trị giá > 300 triệu!"
        ),
        "common_mistakes": (
            "1. Mua thiết bị đo rung/ảnh nhiệt đắt tiền về đo xong lưu ảnh trong thẻ nhớ mà KHÔNG có quy trình lập lệnh sửa chữa (Work Order) xử lý các điểm bất thường phát hiện được!"
        )
    },
})



ENRICHMENTS.update({
    # =========================================================================
    # CHUNK 4: CÔNG NGHỆ DÂY CÁP ĐIỆN & MÁY MÓC ĐẶC THÙ CADIVI (60 THUẬT NGỮ)
    # =========================================================================
    "Copper Give-away": {
        "lesson_id": "L5.2",
        "definition_extra": (
            "\n• Bản chất 'Biếu không vàng ròng cho khách hàng': Đồng chiếm 65–82% tổng giá thành sản xuất cáp điện. Tiêu chuẩn IEC 60228 KHÔNG quy định chặt đường kính mm của lõi đồng mà chỉ quy định Điện trở DC tối đa tại 20°C (Ω/km) — đồng nghĩa chỉ cần điện trở đạt chuẩn là dây đạt chất lượng! Tuy nhiên, do khuôn kéo bị mòn dần theo ca hoặc công nhân cài dư đường kính 'cho chắc ăn đỡ rớt điện trở', sợi đồng bị kéo to hơn thiết kế chỉ 0.01–0.02 mm — về mặt tiết diện (tỷ lệ bình phương đường kính D²) đã làm thừa 1.5–3% khối lượng đồng nguyên chất mà khách hàng không trả thêm 1 xu nào!\n"
            "• Công thức tính nhanh % đồng thừa: % Give-away = [(D_thực / D_chuẩn)² − 1] × 100%."
        ),
        "cadivi_application_extra": (
            "\n• Đòn bẩy tài chính số 1 của Chuyên viên OE tại CADIVI Miền Trung: Chỉ cần kéo giảm Copper Give-away bình quân từ +1.8% xuống +0.4% (giữ cận dưới cách ngưỡng rớt điện trở IEC 60228 an toàn trên 3σ bằng SPC + quản lý tuổi thọ khuôn PCD), nhà máy 1,000 tấn đồng/năm tiết kiệm ngay ~14 tấn đồng ≈ 3.3–3.8 tỷ VNĐ/năm!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Bạn bán ly trà sữa cam kết dung tích 500 ml, nhưng nhân viên nào cũng rót đầy 520 ml 'cho chắc không bị khách mắng' → Cứ 25 ly bạn tự mất không 1 ly nguyên liệu!\n"
            "\n• Ví dụ 2 (Tính toán số liệu tại CADIVI): Dây VC 2.5 mm² (7 sợi Ø0.67 mm) — nếu khuôn kéo mòn khiến đường kính thực tăng từ 0.670 mm lên 0.678 mm (chỉ +0.008 mm, bằng 1/10 sợi tóc!), tiết diện tăng (0.678/0.670)² − 1 = +2.40%! Với sản lượng 200 tấn đồng/năm cho riêng mã dây này (giá đồng ~250 triệu/tấn), chỉ 0.008 mm mòn khuôn đã đốt mất 4.8 tấn đồng = 1.2 TỶ VNĐ/năm!"
        ),
        "common_mistakes": (
            "1. Cố ép giảm đường kính đồng sát sàn mà KHÔNG kiểm tra độ dẫn điện IACS của đồng Rod đầu vào (đồng độ tinh khiết thấp hơn 100.5% IACS sẽ rớt điện trở Kelvin Bridge dù đúng đường kính!).\n"
            "2. Không đồng bộ quy trình MOC/ECN khi điều chỉnh đường kính mục tiêu kéo sợi."
        )
    },
    "Over-thickness": {
        "lesson_id": "L5.2",
        "definition_extra": (
            "\n• Bản chất 'Bọc nhựa thừa để che giấu độ dao động máy đùn': Theo IEC 60502, chiều dày vỏ/cách điện phải thỏa đồng thời 2 điều kiện: (1) Chiều dày trung bình ≥ chiều dày danh định t_nom, và (2) Chiều dày tại điểm mỏng nhất t_min ≥ (0.9 × t_nom − 0.1 mm). Khi trục vít máy đùn cũ dao động áp suất hoặc đầu Crosshead chỉnh lệch tâm (Concentricity < 85%), công nhân sợ rớt t_min nên vặn tăng chiều dày trung bình lên thêm +0.10 đến +0.20 mm — tiêu tốn hàng chục tấn hạt PVC/XLPE/LSZH vô ích mỗi tháng!"
        ),
        "cadivi_application_extra": (
            "\n• Mục tiêu dự án Six Sigma DMAIC kinh điển tại Xưởng Đùn CADIVI Miền Trung: Đầu tiên phải thu hẹp độ lệch chuẩn σ (làm sạch Screen Pack, kiểm soát nhiệt độ/Melt Pressure, chỉnh đồng tâm Crosshead đạt ≥ 92%, gắn vòng kín Laser Gauge Closed-loop), SAU ĐÓ mới dịch tâm mục tiêu (Target Shift) xuống sát t_nom để thu hồi tiền nhựa an toàn!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Sơn một bức tường yêu cầu dày tối thiểu 1 mm — nếu thợ quét chỗ dày chỗ mỏng (độ biến thiên lớn) thì phải quét trung bình dày 1.5 mm mới không hở chân tường, tốn thêm 50% tiền sơn!\n"
            "\n• Ví dụ 2 (Tính toán tại CADIVI): Cáp CXV 4×16 mm² có vỏ PVC chuẩn dày 1.80 mm nhưng thực tế đang đùn trung bình 2.02 mm (+12.2% Over-thickness) do lệch tâm đầu đùn. Sau khi lắp đầu tự định tâm & Laser Gauge kéo σ từ 0.08 mm xuống 0.025 mm, đưa chiều dày trung bình về 1.84 mm (vẫn giữ Cpk > 1.5 so với t_min) → Giảm 9.8% tiêu hao PVC, tiết kiệm ~420 triệu VNĐ/năm chỉ trên 1 dây chuyền!"
        ),
        "common_mistakes": (
            "1. Cấm tuyệt đối hành vi hạ chiều dày mục tiêu TRƯỚC KHI thu hẹp độ dao động σ — hạ sớm sẽ làm thủng Spark Tester hàng loạt và vi phạm pháp lý QCVN 4!"
        )
    },
    "Lay-up Factor": {
        "lesson_id": "L5.2",
        "definition_extra": (
            "\n• Bản chất hình học xoắn ốc (Helical Geometry): Khi xoắn nhiều sợi đồng thành ruột bện (Stranding) hoặc ghép 3–4 lõi cáp cách điện thành cáp nhiều lõi (Laying-up), mỗi sợi đi theo đường xoắn ốc 3D chứ không đi thẳng — vì vậy để tạo ra 1,000 m cáp thành phẩm, chiều dài thực của mỗi sợi/lõi tiêu hao luôn LỚN HƠN 1,000 m (thường từ 1.015 đến 1.045, tức tốn thêm 1.5% – 4.5% vật liệu)!\n"
            "• Công thức vật lý chuẩn: Hệ số xoắn K = √[ 1 + (π × D_pitch / Lay_Length)² ] (trong đó Lay_Length là bước xoắn — bước xoắn càng ngắn/xoắn càng chặt thì K càng lớn, tốn đồng & nhựa càng nhiều!)."
        ),
        "cadivi_application_extra": (
            "\n• Vũ khí bí mật khi kiểm toán định mức MBOM tại CADIVI Miền Trung: Nếu Phòng Kỹ thuật/ERP tính thiếu Lay-up Factor (để K = 1.00 thay vì 1.025), xưởng sẽ luôn bị báo âm định mức 2.5% oan uổng! Ngược lại, nếu công nhân chỉnh bước xoắn quá ngắn hơn tiêu chuẩn cho phép, nhà máy bị mất thêm 0.8–1.5% đồng/nhựa âm thầm trên mỗi km cáp!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Quấn 1 sợi dây quanh chiếc đũa dài 20 cm — khi tháo sợi dây ra đo thẳng, sợi dây chắc chắn dài hơn 20 cm; quấn càng nhiều vòng (bước xoắn ngắn) thì sợi dây càng tốn dài hơn!\n"
            "\n• Ví dụ 2 (Tính toán tại CADIVI): Cáp 4 lõi có đường kính vòng tâm D_pitch = 24 mm, bước xoắn chuẩn Lay_Length = 420 mm → K = √[1 + (3.1416 × 24 / 420)²] = 1.0160 (+1.60% vật liệu). Nếu vận hành chỉnh sai tỷ số bánh răng máy Drum Twister làm bước xoắn ngắn còn 300 mm → K vọt lên 1.0311 (+3.11%), làm đội thêm +1.51% cả đồng lẫn nhựa cách điện trên toàn bộ đơn hàng!"
        ),
        "common_mistakes": (
            "1. Dùng chung 1 hệ số Lay-up Factor cố định 1.02 cho mọi cỡ cáp trên ERP thay vì tính riêng theo đường kính từng lớp bện (lớp ngoài có D_pitch lớn hơn lớp trong nên K lớn hơn!)."
        )
    },
    "Cut-Length": {
        "lesson_id": "L5.2",
        "definition_extra": (
            "\n• Bản chất bài toán tối ưu cắt đoạn (1D Cutting Stock Problem): Trong sản xuất cáp điện lực cho dự án, khách hàng đặt các đoạn lẻ rất khác nhau (vd: 320 m, 480 m, 650 m, 1,100 m) trong khi rulo bán thành phẩm từ máy kéo/bện/đùn có chiều dài chuẩn cố định (vd: 2,000 m hoặc 3,000 m). Nếu cắt nối tùy tiện, cuối mỗi rulo sẽ dư ra các khúc cáp ngắn 30–120 m không bán được cho ai (End-piece / Remnant Scrap), phải tuốt bỏ đồng với chi phí cực đắt!\n"
            "• Cách giải quyết chuẩn OE: Lập thuật toán tổ hợp cắt (Excel Solver / Python Linear Programming) ghép các đoạn đặt hàng khớp tối đa với chiều dài rulo và đồng bộ ngay từ lệnh xuất rulo Xưởng Kéo/Bện!"
        ),
        "cadivi_application_extra": (
            "\n• Rất cấp thiết tại Xưởng Đóng Cuộn & Phòng Kế Hoạch CADIVI Miền Trung (chuyên phục vụ nhiều dự án điện lực, chung cư, khu công nghiệp miền Trung với chiều dài đặt hàng lẻ đa dạng)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Bạn có thanh sắt dài 6 m và cần cắt các thanh 2.4 m và 1.8 m. Nếu cắt 2.4 + 2.4 = 4.8 m sẽ dư bỏ 1.2 m (phế 20%); nếu ghép 2.4 + 1.8 + 1.8 = 6.0 m sẽ đạt phế 0%!\n"
            "\n• Ví dụ 2 (Tại CADIVI): Đơn hàng cáp CXV 3×95+1×50 có 6 đoạn: 620 m, 580 m, 450 m, 350 m, 750 m, 250 m chạy trên rulo chuẩn 1,500 m. Cắt theo thứ tự đơn hàng gây dư 2 khúc lẻ 170 m & 130 m (tốn > 110 triệu phế phẩm!). Chạy Excel Solver gom tổ hợp Rulo 1 (620 + 580 + 250 = 1,450 m) và Rulo 2 (750 + 450 + 350 = 1,550 m đặt chạy đúng 1,560 m ngay từ khâu bện) → Giảm phế Cut-Length từ 9.5% xuống còn < 1.2%!"
        ),
        "common_mistakes": (
            "1. Chỉ tính cắt đoạn ở khâu cuối (Đóng cuộn) mà không đẩy tổng chiều dài mục tiêu ngược lên cho khâu Xưởng Bện & Xưởng Đùn chạy đúng chiều dài đặt riêng."
        )
    },
    "RBD": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Công đoạn mở đầu quyết định toàn bộ chất lượng và chi phí nhà máy cáp điện: Máy kéo thô RBD (Rod Breakdown Machine) nhận cuộn đồng thanh Ø8.0 mm (Copper Rod chuẩn ASTM B49, nặng 3–4 tấn/cuộn) kéo liên tục qua chuỗi 9–13 khuôn kéo kim cương (PCD) ngập trong dung dịch nhũ tương làm mát để thu nhỏ đường kính xuống Ø1.38 – Ø3.50 mm với tốc độ cực cao 20–32 m/giây (tương đương > 100 km/giờ!), tích hợp ngay bộ ủ điện liên tục Inline Annealer ở đầu ra.\n"
            "• Nguyên lý bảo toàn thể tích: Khi tiết diện đồng giảm đi 20% qua mỗi khuôn kéo, tốc độ tuyến tính của sợi đồng phải tăng vọt tương ứng (+25%) qua từng trục Puly trượt (Slip Capstan) — chỉ cần sai tỷ lệ trượt hoặc cạn nhũ tương là đứt sợi ngay lập tức!"
        ),
        "cadivi_application_extra": (
            "\n• Thường là máy công suất lớn, tiêu thụ điện mạnh nhất tại Xưởng Kéo CADIVI Miền Trung: OE tập trung tối ưu OEE máy RBD (giảm đứt sợi, giảm thời gian hàn nối cuộn đồng bằng Butt Welder và đổi rulo Take-up bằng Dual Take-up) và quản lý điện năng kWh/tấn đồng."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như thợ làm mì kéo tay — từ một khối bột dày Ø8 mm kéo dần qua nhiều nấc nhỏ hơn để thành sợi mì mảnh dài gấp 16–30 lần nhưng khối lượng đồng không đổi!\n"
            "\n• Ví dụ 2 (Tính toán năng suất RBD tại CADIVI): Kéo đồng Rod Ø8.0 mm xuống Ø2.0 mm (tỷ lệ giãn dài = (8/2)² = 16 lần — 1 mét đồng Rod thành 16 mét sợi Ø2.0 mm!). Ở tốc độ ra 25 m/s (= 1,500 m/phút), sản lượng lý thuyết đạt ~2.5 tấn/giờ. Mỗi lần đứt sợi dừng máy 18 phút để xâu lại 11 khuôn kéo làm bốc hơi ngay 750 kg sản lượng đồng!"
        ),
        "common_mistakes": (
            "1. Chỉ đo tốc độ m/phút mà quên theo dõi điện năng kWh/tấn và tỷ lệ đứt sợi/tấn (Breaks per Ton) — mốc chuẩn xuất sắc của máy RBD là < 0.3 lần đứt/tấn đồng!"
        )
    },
    "Annealing": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất luyện kim 'Hồi sinh độ dẻo & độ dẫn điện': Khi sợi đồng bị kéo nguội qua khuôn kéo RBD/Multi-wire, cấu trúc tinh thể bị nén biến dạng mạnh (hiện tượng hóa bền nguội — Work Hardening) khiến sợi đồng trở nên CỨNG, GIÒN (độ giãn dài tụt từ 30% xuống chỉ còn 1–2% — bẻ nhẹ là gãy!) và ĐIỆN TRỞ TĂNG thêm 2–3%. Công đoạn Ủ (Annealing) nung nóng sợi đồng lên ~450–550°C trong môi trường hơi nước/khí bảo vệ chống oxy hóa để tinh thể tái kết tinh — trả lại độ mềm dẻo (độ giãn dài ≥ 20–25%) và độ dẫn điện 100% IACS!\n"
            "• 2 công nghệ phổ biến: (1) Ủ liên tục trên dây chuyền kéo (Inline Resistance Annealer — phóng dòng điện DC hàng ngàn Ampe trực tiếp qua sợi đồng đang chạy), (2) Ủ mẻ trong lò chuông chân không/khí Nitơ (Bell Furnace)."
        ),
        "cadivi_application_extra": (
            "\n• Kiểm soát chất lượng sống còn tại Xưởng Kéo CADIVI Miền Trung: Điện áp ủ phải tự động tỷ lệ theo bình phương tốc độ kéo! Nếu ủ thiếu nhiệt → dây cứng lò xo, gãy sợi khi bện & tăng điện trở; nếu ủ quá nhiệt → sợi đồng cháy đen bề mặt, bết dính lớp trên rulo không xả ra được (Stickiness)!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Bẻ đi bẻ lại 1 sợi kẽm 5 lần nó sẽ cứng lại rồi gãy đôi (biến cứng nguội); nung đỏ rồi để nguội đúng cách kim loại sẽ mềm dẻo trở lại như ban đầu!\n"
            "\n• Ví dụ 2 (Sự cố thực tế tại xưởng kéo CADIVI): Vào thời điểm tăng tốc và giảm tốc dừng máy RBD, bộ điều khiển điện áp ủ đáp ứng chậm 0.8 giây gây ra 40 mét sợi đầu/cuối rulo bị ủ non (cứng) làm máy bện Buncher công đoạn sau liên tục bị bung sợi! Chỉnh lại đường cong đồng bộ điện áp ủ (Ramp Curve) trên PLC giảm ngay 80% lỗi đứt sợi ở Xưởng Bện."
        ),
        "common_mistakes": (
            "1. Bỏ qua kiểm tra chất lượng nước/hơi bảo vệ chống oxy hóa trong ống ủ Inline → Sợi đồng ra khỏi máy vẫn mềm nhưng bị xỉn nâu đen chỉ sau 24 giờ nằm chờ trong kho!"
        )
    },
    "Buncher": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất công nghệ xoắn tốc độ siêu cao (Double-Twist Buncher): Thay vì quay nặng nề cả giàn rulo đồng cấp dây, máy Buncher giữ cố định các rulo xả (Pay-off) đứng bên ngoài và chỉ quay một cánh cung nhẹ (Flyer/Bow) vòng quanh rulo thu dây đặt bên trong lồng máy — mỗi 1 vòng quay của cánh cung tạo ra ĐÚNG 2 bước xoắn (Double Twist)! Nhờ đó tốc độ xoắn đạt 4,000 – 7,000 vòng xoắn/phút, chuyên dùng để bện ruột đồng mềm cấp 5 (Class 5 — hàng chục sợi mảnh Ø0.20–0.40 mm) và dây dân dụng tiết diện nhỏ (0.5 – 6.0 mm²)."
        ),
        "cadivi_application_extra": (
            "\n• Máy trụ cột sản xuất dây mềm VCm, dây đôi VCmd và ruột dây dân dụng tại Xưởng Bện CADIVI Miền Trung: Rất lý tưởng để áp dụng bài toán Man-Machine Chart (1 công nhân đứng đồng thời 4–6 máy Buncher có gắn cảm biến đứt sợi Jidoka) nhằm nâng vọt chỉ số OLE!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Khi bạn cầm một bó 32 sợi chỉ mảnh xoắn đều lại thành 1 sợi dây dù mềm chắc mà vẫn uốn cong dễ dàng — máy Buncher làm đúng việc đó ở tốc độ 6,000 xoắn/phút!\n"
            "\n• Ví dụ 2 (Tối ưu OLE cụm máy Buncher tại CADIVI): Cụm 8 máy Buncher trước đây bố trí 4 công nhân (1 người/2 máy, OLE chỉ 51%). Sau khi chuẩn hóa giàn xả Pay-off chống rối, lắp cảm biến đứt sợi tự dừng + đèn Andon trên cao và vẽ Man-Machine Chart, 2 công nhân đứng gọn 8 máy (1 người/4 máy), OLE tăng từ 51% lên 79% và giải phóng 2 nhân sự sang hỗ trợ Xưởng Đùn!"
        ),
        "common_mistakes": (
            "1. Căng lực xả giữa các rulo Pay-off không đều nhau → Tạo ra lỗi 'lồng chim' (Birdcaging) hoặc một vài sợi chùng lòi ra ngoài bó dây làm thủng cách điện khi qua máy đùn!"
        )
    },
    "Rigid Strander": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Cỗ máy bện đồng tâm sức mạnh lớn cho cáp lực': Khác với máy Buncher xoắn bó tự do dùng cho dây nhỏ mềm, Rigid Frame Strander (máy bện lồng cứng) đặt từng rulo sợi đồng lớn (Ø1.5 – Ø3.5 mm) ngay trên các khung lồng thép quay đồng trục (thường cấu hình 1+6+12+18+24 = 61 sợi) — các lồng quay ngược chiều nhau để bện từng lớp sợi đồng tâm cực chặt, kết hợp bộ ép nén (Compacting Roller) ép chặt ruột tròn hoặc ép rẻ quạt (Sector-shaped) đạt chuẩn ruột cấp 2 (IEC 60228 Class 2) cho cáp trung/hạ thế 16 mm² đến 630 mm²!"
        ),
        "cadivi_application_extra": (
            "\n• Tài sản đắt tiền và thường là nút thắt công suất đổi mã của Xưởng Bện cáp lực CADIVI: Thay nạp đồng thời 36–61 rulo đồng vào các lồng quay là bài toán SMED kinh điển (nếu làm thủ công từng cuộn mất 60–90 phút, còn áp dụng hệ thống nạp hàng loạt Side-loader + xe kitting rulo đồng bộ rút xuống dưới 20 phút!)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Lợi ích kép của ruột ép nén Compact trên Rigid Strander): Ép nén ruột cáp CXV 185 mm² làm giảm đường kính ngoài của ruột đồng từ 17.5 mm xuống 15.8 mm (-9.7%) → Giúp tiết kiệm ngay 8–10% lượng nhựa cách điện XLPE, băng bọc và vỏ PVC ở các công đoạn đùn phía sau!\n"
            "\n• Ví dụ 2 (SMED tại Rigid Strander CADIVI): Trước đây 1 người tự đẩy nạp lần lượt 37 rulo mất 72 phút/lần đổi cỡ cáp. Chuẩn hóa quy trình Pit-stop 2 người + soạn sẵn toàn bộ 37 rulo có chiều dài bằng nhau (Equal-length Pay-off) trên giá trượt trước khi máy dừng → Rút thời gian nạp xuống 24 phút (-66.7%) và giảm 70% đồng dư thừa cuối rulo!"
        ),
        "common_mistakes": (
            "1. Nạp các rulo đồng có chiều dài chênh lệch nhau vào cùng một lồng máy Rigid Strander → Rulo ngắn nhất hết trước buộc phải dừng cả cỗ máy 61 cuộn để nối dây hoặc bỏ phí toàn bộ phần đồng còn lại trên 36 rulo kia!"
        )
    },
    "Extruder": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Trái tim tạo hình cách điện & vỏ bảo vệ cáp điện': Máy đùn nhựa (Single-Screw Extruder) nhận hạt nhựa rắn từ phễu (Hopper), đẩy dọc theo trục vít quay bên trong nòng thép gia nhiệt qua 3 vùng chức năng liên tiếp: (1) Vùng cấp liệu (Feed Zone — vận chuyển hạt rắn), (2) Vùng nén & nóng chảy (Compression/Transition Zone — vừa nén ép tăng áp vừa gia nhiệt biến hạt rắn thành nhựa nóng chảy đồng nhất nhờ ma sát trượt + điện trở nòng), (3) Vùng định lượng (Metering Zone — ổn định lưu lượng và áp suất Melt Pressure đẩy nhựa qua lưới lọc Screen Pack vào đầu chữ T Crosshead bọc đều lên ruột đồng đang chạy ngang!)."
        ),
        "cadivi_application_extra": (
            "\n• Công đoạn cổ chai (Bottleneck) số 1 tại Nhà máy CADIVI Miền Trung (chiếm phần lớn cơ hội tăng OEE, giảm Over-thickness và giảm phế SMED): Mỗi dây chuyền đùn là một hệ thống đồng bộ dài 30–60 mét gồm Pay-off → Pre-heater → Máy đùn chính/phụ → Đầu Crosshead → Laser Gauge → Máng nước Cooling Trough → Spark Tester → Máy in chữ → Capstan → Take-up!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Giống chiếc máy đùn làm bún/xúc xích — trục xoắn quay liên tục đẩy nguyên liệu nóng dẻo đi qua khuôn định hình tròn ở đầu ra, chỉ khác là máy đùn cáp luồn thêm sợi đồng chạy xuyên qua tâm khuôn cùng lúc!\n"
            "\n• Ví dụ 2 (Đồng bộ hóa tốc độ trên máy đùn CADIVI): Máy đùn PVC Ø90 mm đang chạy dây VC 2.5 ở 300 m/phút, nhiệt độ 5 vùng 155–160–165–170–175°C. Khi nhiệt độ vùng 3 bị hỏng cảm biến tụt 15°C, độ nhớt nhựa tăng làm áp suất Melt Pressure nhảy vọt, gây sần bề mặt Sharkskin và lệch đường kính vượt USL — hệ thống SCADA/MES cảnh báo kịp giúp thợ dừng sửa cặp nhiệt điện thay vì chạy hỏng cả 10 km dây!"
        ),
        "common_mistakes": (
            "1. Dùng chung 1 trục vít thiết kế cho nhựa PVC để chạy hạt XLPE/LSZH ở tốc độ cao (trục vít PVC có tỷ lệ nén và chiều sâu rãnh khác XLPE → gây quá nhiệt cháy nhựa Scorching hoặc trộn không đều!)."
        )
    },
    "Crosshead": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Đầu chữ T quyết định độ đồng tâm & độ bám dính lớp bọc': Đầu đùn vuông góc (Crosshead) bẻ hướng dòng nhựa nóng chảy 90° từ nòng máy đùn để bọc bao quanh lõi đồng chạy thẳng xuyên tâm qua bộ đôi Chày (Tip / Core Tube) và Cối (Die / Die Ring).\n"
            "• 2 kỹ thuật bọc bắt buộc OE phải phân biệt rõ:\n"
            "  1. Bọc Ống (Tubing / Draw-down): Đầu Chày thò ngang hoặc nhô nhẹ qua mặt Cối — nhựa tạo thành ống mỏng rồi bị kéo giãn (DDR) ôm sát vào lõi cáp nhờ lực hút chân không (dùng cho vỏ cáp nhiều lõi để dễ tuốt vỏ khi thi công!).\n"
            "  2. Bọc Áp Lực (Pressure Tooling): Đầu Chày thụt sâu bên trong Cối — nhựa nóng chảy ép áp suất trực tiếp lấp đầy các khe rãnh giữa các sợi đồng (dùng cho cách điện cáp lực/trung thế cần bám chặt chống thấm nước!)."
        ),
        "cadivi_application_extra": (
            "\n• Điểm trọng tâm của mọi dự án SMED và giảm Over-thickness tại CADIVI Miền Trung: Chuyển đổi từ đầu chỉnh tay 4 con ốc (mất 15–20 phút vừa chạy xả nhựa vừa vặn ốc lấy tâm!) sang đầu Tự định tâm (Self-Centering Crosshead) giúp độ đồng tâm đạt ngay ≥ 94% và cắt 70% phế đầu ca!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Khi bọc ống co nhiệt quanh bó dây, bạn có thể để nó ôm gọn vừa khít ngoài (Tubing) hoặc bơm keo lấp kín mọi kẽ hở bên trong (Pressure).\n"
            "\n• Ví dụ 2 (Tại Xưởng Đùn CADIVI): Đùn lớp vỏ ngoài PVC cho cáp 4 lõi CXV bị lỗi công nhân lắp nhầm bộ Chày–Cối kiểu Pressure thay vì Tubing → Vỏ nhựa dính chặt cứng vào 4 lõi bên trong, khách hàng thi công không tuốt được vỏ trả về 2 km cáp! Áp dụng Poka-Yoke khắc laser ký hiệu 'P' (Pressure) vs 'T' (Tubing) kèm mã màu ngay trên thân Chày–Cối chấm dứt 100% lỗi lắp nhầm."
        ),
        "common_mistakes": (
            "1. Không gia nhiệt trước (Pre-heat) bộ Chày–Cối dự phòng ở tủ sấy bên ngoài trước khi lắp vào đầu Crosshead → Khi lắp bộ khuôn nguội vào máy nóng phải chờ 25 phút ổn định nhiệt mới chạy được!"
        )
    },
    "Spark Tester": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất 'Cổng soi sét 100% trực tuyến phát hiện lỗ kim cách điện': Đặt ngay sau máng nước làm mát trên dây chuyền đùn (và trên máy đánh cuộn kiểm tra), thiết bị Spark Tester cho sợi cáp chạy xuyên qua màn chuỗi hạt bi kim loại (Bead Chain) mang điện áp cao tần (thường 3 kV – 25 kV tùy độ dày cách điện theo IEC 62230) trong khi lõi đồng được nối đất. Nếu cách điện bị rỗ khí, nứt vi mô, thủng lỗ kim (Pinhole) hay lẫn tạp chất dẫn điện nhỏ bằng đầu kim, tia lửa điện cao áp sẽ phóng đánh thủng ngay điểm đó → Máy đếm lỗi tức thì, phun mực đánh dấu vị trí và kích hoạt dừng máy/cảnh báo MES!"
        ),
        "cadivi_application_extra": (
            "\n• Hàng rào bảo vệ chất lượng & an toàn sinh mạng khách hàng tại CADIVI: Mọi cuộn dây dân dụng VC/CV và lõi cáp điện lực 100% phải đi qua Spark Tester hiệu chuẩn hàng ca bằng thanh thử lỗ kim chuẩn (Fault Simulator Bead) trước khi xuất xưởng."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như dùng đèn pin siêu sáng soi trong phòng tối qua tấm áo mưa — bất kỳ lỗ kim nhỏ li ti nào mà mắt thường không nhìn thấy đều lập tức lóe tia sáng báo vị trí chính xác!\n"
            "\n• Ví dụ 2 (Tích hợp Jidoka tại CADIVI): Kết nối tín hiệu xung đếm lỗi từ Spark Tester về PLC/MES: cài ngưỡng nếu trong 500 mét dây xuất hiện ≥ 2 lỗi Spark liên tiếp, máy đùn tự động bật đèn Andon Đỏ và dừng máy để kiểm tra lọc nhựa/ẩm hạt nhựa ngay thay vì chạy hỏng nốt 4,500 mét còn lại trên rulo!"
        ),
        "common_mistakes": (
            "1. Quên nối đất (Grounding) lõi đồng ở đầu xả Pay-off hoặc tiếp địa kém → Spark Tester vẫn bật đèn xanh đẹp nhưng thực chất KHÔNG BAO GIỜ phát hiện được lỗ thủng (100% lọt lỗi ra thị trường!).\n"
            "2. Nhầm lẫn Spark Tester thay thế được phép thử ngâm nước Water Immersion ở Phòng Lab."
        )
    },
    "Laser Gauge": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Đôi mắt laser đo đường kính chính xác 1 micron ở tốc độ 1,000 m/phút': Đầu đo Laser 2 trục (X–Y) hoặc 3 trục quét chùm tia laser tốc độ hàng nghìn lần/giây qua sợi cáp đang chạy mà KHÔNG cần chạm vào bề mặt nhựa còn nóng mềm, đo chính xác tức thời cả Đường kính ngoài (OD) lẫn Độ méo ovan (Ovality) với độ phân giải ±0.001 mm!\n"
            "• Đỉnh cao tự động hóa (Closed-loop Control): Nối tín hiệu Laser Gauge trực tiếp về PLC điều chỉnh tự động tốc độ bánh kéo Capstan hoặc vòng quay trục vít máy đùn — khi OD hơi tăng +0.01 mm, PLC tự nhích tốc độ kéo lên 0.3% kéo đường kính quay về tâm chuẩn ngay lập tức!"
        ),
        "cadivi_application_extra": (
            "\n• Công cụ số 1 để triệt tiêu Over-thickness và đẩy Cpk đường kính > 1.67 tại Xưởng Đùn CADIVI Miền Trung: Đồng thời đẩy dữ liệu đo liên tục mỗi giây lên SCADA/MES để tự động vẽ biểu đồ SPC Xbar-R mà không cần công nhân cắt dây đo Panme thủ công!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Hiệu quả lắp vòng kín Closed-loop tại CADIVI): Trước đây công nhân dùng Panme đo tay 2 lần/rulo nên phải để biên độ an toàn dày hơn chuẩn +0.12 mm (lãng phí nhựa ~8%). Sau khi kích hoạt vòng kín Laser Gauge → Capstan PLC, độ dao động đường kính thu hẹp xuống ±0.015 mm, giảm tiêu hao nhựa 6.5% và hoàn vốn đầu tư bộ Laser Gauge chỉ trong 5.5 tháng!\n"
            "\n• Ví dụ 2 (Bảo vệ độ chính xác): Gắn kèm bộ thổi khí nén khô (Air Wipe) ngay trước đầu đo Laser Gauge giúp thổi sạch giọt nước bám từ máng làm mát — tránh hiện tượng giọt nước đánh lừa tia laser báo sai tăng đường kính ảo!"
        ),
        "common_mistakes": (
            "1. Không hiệu chuẩn định kỳ bằng trục dưỡng chuẩn (Calibration Pin) và để kính quang học dính bụi nhựa/hơi nước làm số đo trôi lệch (Bias) kéo cả lô dây sai kích thước!"
        )
    },
    "Color Sequencing": {
        "lesson_id": "L3.3",
        "definition_extra": (
            "\n• Bản chất 'Nghệ thuật xếp lịch theo bánh xe sắc tố (Light-to-Dark Wheel)': Trong đùn bọc dây điện, đổi từ màu SÁNG sang màu TỐI (vd: Trắng → Vàng → Xanh lá → Đỏ → Xanh dương → Đen) chỉ cần đẩy rất ít nhựa (3–5 kg, mất 5–8 phút) là màu tối phủ sạch hoàn toàn màu sáng; ngược lại, đổi từ màu TỐI sang màu SÁNG (Đen → Trắng) buộc phải xả lượng nhựa cực lớn (20–35 kg, mất 30–50 phút), thậm chí phải tháo nòng vệ sinh đầu Crosshead vì chỉ 1 hạt muội than Carbon Black sót lại cũng làm dây trắng bị vệt sọc xám phế phẩm!"
        ),
        "cadivi_application_extra": (
            "\n• Cải tiến chi phí 0 đồng mang lại ROI cao nhất tức thì tại Phòng Kế Hoạch & Xưởng Đùn CADIVI Miền Trung: Kết hợp Campaign Scheduling gom đơn hàng theo chu kỳ vòng màu cố định mỗi 3–5 ngày (Trắng → Vàng → Xanh/Đỏ → Đen → chạy nhựa tẩy Purging 1 lần duy nhất cuối chu kỳ rồi quay lại Trắng!)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Khi vẽ màu nước mà chỉ có 1 cốc nước rửa cọ — bạn tô màu Vàng trước rồi sang Cam, Đỏ, Đen thì nước rất ít đục; nếu tô Đen trước rồi muốn tô Vàng thì phải thay nước rửa cọ 5 lần mới sạch!\n"
            "\n• Ví dụ 2 (Tính tiền tiết kiệm thực tế tại CADIVI): Máy đùn dây VC có 18 lần đổi màu/tuần. Trước đây Kế hoạch xếp ngẫu nhiên theo giờ chốt đơn hàng (có tới 7 lần đổi ngược Tối → Sáng tốn trung bình 24 kg nhựa xả/lần). Sau khi thiết lập Luật Bánh Xe Màu (chỉ 1 lần đổi Đen → Trắng vào chiều thứ Bảy), lượng nhựa xả Purge giảm từ 290 kg/tuần xuống 85 kg/tuần (-70.7%) và tăng thêm 7.5 giờ máy chạy mỗi tuần hoàn toàn MIỄN PHÍ!"
        ),
        "common_mistakes": (
            "1. Xếp lịch đúng bánh xe màu rồi nhưng phòng Kinh doanh cứ xen ngang đơn hàng gấp màu Trắng vào giữa ca đang chạy màu Đen mà không tính chi phí ẩn đổi màu (Changeover Cost) để đàm phán lại ngày giao!"
        )
    },
    "Purging": {
        "lesson_id": "L3.3",
        "definition_extra": (
            "\n• Bản chất 'Tẩy rửa lòng máy đùn giữa 2 mẻ vật liệu/màu sắc': Khi chuyển màu nhựa (đặc biệt Đen → Trắng) hoặc chuyển chủng loại nhựa khác nhiệt độ nóng chảy (PVC → XLPE/LSZH), nhựa cũ bám dính dọc thành rãnh trục vít và đầu Crosshead phải được đẩy sạch ra ngoài bằng nhựa nguyên sinh hoặc hợp chất tẩy chuyên dụng (Purging Compound — chứa hạt mài mềm/chất hoạt động bề mặt tạo lực cọ sạch gấp 4 lần nhựa thường).\n"
            "• Quy tắc an toàn hóa học sống còn: TUYỆT ĐỐI KHÔNG cho nhựa PVC chạm trực tiếp với nhựa chứa hợp chất nhạy hoặc để PVC nằm im trong nòng quá nóng > 190°C — PVC phân hủy sinh khí Axit Clohydric (HCl) ăn mòn rỗ nòng thép và gây cháy đen (Carbonization)!"
        ),
        "cadivi_application_extra": (
            "\n• Nằm trong nhóm phế phẩm có thể cắt giảm nhanh nhất của Xưởng Đùn CADIVI: OE cân đo riêng mã phế 'Purge Scrap' (tách khỏi phế lỗi chất lượng) và theo dõi định mức kg nhựa purge/lần chuyển đổi theo từng cặp màu."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (So sánh dùng Purging Compound tại CADIVI): Đổi từ vỏ cáp PVC Đen sang PVC Vàng bằng nhựa PVC thường mất 38 phút và xả ra 28 kg nhựa phế (~1.1 triệu tiền nhựa + 38 phút dừng máy). Dùng 2.5 kg hạt Purging Compound chuyên dụng (giá ~250 nghìn) kết hợp kỹ thuật nâng/hạ tốc độ trục vít xung nhịp (Speed Cycling) chỉ mất 11 phút và xả tổng cộng 6 kg → Tiết kiệm ròng > 600 nghìn + 27 phút OEE mỗi lần đổi!"
        ),
        "common_mistakes": (
            "1. Xả purge xong vứt chung đống nhựa sạch với rác dầu mỡ dưới sàn thay vì hứng riêng vào khay inox sạch để nghiền tái chế (Regrind) dùng cho lớp nhựa đệm độn (Bedding) của cáp nhiều lõi!"
        )
    },
    "XLPE": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Nhựa Polyethylene liên kết ngang — Vua cách điện cáp lực hiện đại': Hạt nhựa PE thường là nhựa nhiệt dẻo (nóng trên 100°C là chảy nhão như sáp nến). Nhờ quá trình khâu mạch hóa học/vật lý (Cross-linking bằng Silane, Peroxide CCV hoặc tia điện tử E-beam), các chuỗi polymer dài được nối chéo với nhau thành mạng lưới 3 chiều giống cấu trúc cao su lưu hóa → Chuyển từ nhựa nhiệt dẻo thành nhựa NHIỆT RẮN!\n"
            "• Ưu thế vượt trội so với PVC: Nhiệt độ vận hành lõi liên tục tới 90°C (PVC chỉ 70°C), chịu ngắn mạch tới 250°C trong 5 giây (PVC chỉ 160°C) → Cùng một tiết diện ruột đồng, cáp XLPE tải được dòng điện CAO HƠN 20–25% so với cáp PVC, độ bền cách điện và tuổi thọ lên tới 30–40 năm!"
        ),
        "cadivi_application_extra": (
            "\n• Sản phẩm chủ lực đem lại doanh thu và biên lợi nhuận cao tại CADIVI Miền Trung (cáp lực hạ thế CXV, cáp vặn xoắn ABC, cáp trung thế 24kV/35kV): OE phải nắm cực chắc sự khác biệt công nghệ giữa XLPE Silane (hạ thế — xông hơi nóng/nước nóng 70–90°C) và XLPE Peroxide (trung thế — ống lưu hóa CCV khí Nitơ áp suất cao) vì nó ảnh hưởng trực tiếp tới Lead Time và nút thắt công suất!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan đời sống): Nhựa PE thường giống như bát mì sợi rời — gặp nóng là trượt chảy ra; XLPE giống như mạng lưới đánh cá đan nút chặt mọi giao điểm — gặp nhiệt 200°C vẫn giữ nguyên phom dáng không chảy nhỏ giọt!\n"
            "\n• Ví dụ 2 (Bài toán OE tại CADIVI): Nhựa XLPE sau khi đã khâu mạch thành nhiệt rắn KHÔNG THỂ nấu chảy tái chế (Regrind) lại được như PVC! Vì vậy mỗi 1% giảm phế đầu ca SMED hay giảm Over-thickness trên dây chuyền đùn XLPE có giá trị tiết kiệm thực tế CAO GẤP ĐÔI so với dây chuyền PVC!"
        ),
        "common_mistakes": (
            "1. Lưu kho bao hạt XLPE Silane đã xé miệng quá lâu ngoài không khí ẩm Đà Nẵng → Hạt bị tự khâu mạch sớm (Pre-curing/Scorching) ngay trong phễu làm sần vỏ (Sharkskin) và nghẹt sạch lưới lọc Screen Pack!"
        )
    },
    "PVC": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Vật liệu phổ thông đa dụng nhất ngành dây cáp điện': Polyvinyl Chloride (PVC) tinh khiết vốn cứng như ống nước, khi phối trộn thêm chất hóa dẻo (Plasticizer như DOP/DOTP), chất ổn định nhiệt (Heat Stabilizer không chì Ca-Zn), chất độn CaCO3 và phụ gia chậm cháy sẽ tạo ra hạt nhựa PVC mềm dẻo dùng bọc cách điện dây dân dụng (VC, CV) và lớp vỏ bảo vệ ngoài (Sheath) cho cáp CXV!\n"
            "• Ưu nhược điểm công nghiệp: Giá thành hợp lý, chống cháy lan tự tắt tốt nhờ chứa nguyên tố Clo, dễ đùn gia công và tái chế được nhựa purge sạch; nhưng nhược điểm là nhiệt độ vận hành tối đa chỉ 70°C và khi cháy sinh khói đen đặc + khí axit HCl ăn mòn (nên công trình kín đông người phải chuyển sang LSZH!)."
        ),
        "cadivi_application_extra": (
            "\n• Chiếm tỷ trọng sản lượng tấn nhựa lớn nhất tại CADIVI Miền Trung: OE tập trung kiểm soát tỷ trọng riêng (Specific Gravity — thường 1.38–1.55 g/cm³ vì tỷ trọng ảnh hưởng trực tiếp kg nhựa tiêu hao/km trên BOM!), nhiệt độ gia công tránh cháy sém (Scorch) và tỷ lệ tái chế nhựa purge sạch hợp lệ."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Bẫy tỷ trọng PVC trong kiểm toán BOM CADIVI): Công thức tính khối lượng nhựa đùn = Thể tích lớp nhựa × Tỷ trọng (g/cm³). Nếu nhà cung cấp giao lô hạt PVC vỏ có tỷ trọng tăng từ 1.42 lên 1.49 g/cm³ (+4.9% do tăng bột đá CaCO3 rẻ tiền!), dù chiều dày đùn ĐÚNG CHUẨN từng 0.01 mm, định mức BOM theo kg vẫn bị đội âm +4.9%!\n"
            "\n• Ví dụ 2 (Kiểm soát chất lượng): Khi máy đùn PVC phải dừng đột xuất > 15 phút do mất điện hoặc đứt dây, công nhân bắt buộc phải hạ nhiệt độ nòng về mức Standby (120–130°C) và xả nhựa cũ ra để tránh PVC phân hủy cháy đen ăn mòn trục vít."
        ),
        "common_mistakes": (
            "1. Chỉ kiểm soát chiều dày mm trên máy đùn mà quên kiểm tra tỷ trọng (g/cm³) của từng lô hạt PVC nhập kho IQC — nguyên nhân số 1 gây lệch BOM Variance khó hiểu cuối tháng!"
        )
    },
    "LSZH": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Nhựa Ít Khói – Không Halogen bảo vệ sinh mạng khi hỏa hoạn' (Low Smoke Zero Halogen, còn gọi HFFR/LSOH): Thay vì dùng Clo/Brom như PVC, nhựa LSZH dùng nền Polyolefin (PE/EVA) trộn hàm lượng cực cao (55–65% khối lượng!) bột khoáng ngậm nước không độc (như Nhôm Hydroxit ATH hoặc Magie Hydroxit MDH). Khi xảy ra cháy, khoáng chất phân hủy giải phóng HƠI NƯỚC làm mát dập lửa, tỏa khói trắng cực mỏng (độ truyền sáng > 60% giúp người kẹt tìm thấy lối thoát hiểm!) và khí thải không có axit ăn mòn thiết bị điện tử!"
        ),
        "cadivi_application_extra": (
            "\n• Dòng cáp cao cấp tăng trưởng cực nhanh của CADIVI cho sân bay, metro, bệnh viện, khách sạn 5 sao, trung tâm dữ liệu (Data Center): Tuy nhiên LSZH RẤT KHÓ ĐÙN (độ nhớt cao, rất dễ hút ẩm, cực nhạy quá nhiệt trên 165–175°C làm phân hủy ATH sinh bọt rỗ khí!) nên tốc độ máy đùn chỉ đạt 40–60% so với PVC — OE phải cài Routing tốc độ riêng và quy trình sấy Hopper Dryer chuẩn cho mã LSZH!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Trong vụ cháy tòa nhà cao tầng, đa số nạn nhân tử vong do ngạt khói đen và khí độc chứ không phải do lửa — cáp LSZH đảm bảo khi cháy vẫn nhìn rõ lối thoát hiểm và không tạo khí axit hủy hoại hệ thống máy chủ!\n"
            "\n• Ví dụ 2 (Xử lý lỗi phồng rộp vỏ LSZH tại CADIVI): Khi chạy cáp chống cháy FR-LSZH, vỏ cáp nổi bọt khí li ti và hay bị Die Drool đóng cặn đầu khuôn → OE khảo sát phát hiện công nhân để trục vít quay quá nhanh (sinh nhiệt ma sát vượt 180°C làm ATH xả hơi nước ngay trong nòng!) và dùng trục vít tỷ số nén cao của PVC. Chuyển sang trục vít nén thấp (Compression Ratio ~1.2:1) + kiểm soát nhiệt độ nóng chảy ≤ 165°C giúp tốc độ tăng +22% và tỷ lệ phế rỗ khí giảm từ 7.5% xuống 0.6%!"
        ),
        "common_mistakes": (
            "1. Để chung Routing tốc độ đùn của cáp LSZH ngang bằng cáp PVC trên ERP → Làm kế hoạch giao hàng CRP bị trễ nặng và tính sai giá thành giờ máy!"
        )
    },
    "Silane": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Công nghệ khâu mạch XLPE bằng độ ẩm cực kinh tế cho cáp hạ thế' (Sioplas / Monosil Process): Hạt nhựa PE được ghép nhánh phân tử Silane (Vinyltrimethoxysilane) kết hợp 5% hạt xúc tác (Catalyst Masterbatch — tỷ lệ 95:5) rồi đùn bọc lõi cáp trên máy đùn thông thường giống PVC. Sau khi đùn xong, cuộn cáp được đưa vào bể xông nước nóng 80–90°C hoặc phòng xông hơi bão hòa (Sauna Room) trong 4–12 giờ — phân tử nước khuếch tán vào lớp nhựa kích hoạt phản ứng thủy phân và ngưng tụ tạo cầu nối Siloxane Si–O–Si khâu mạch chặt thành XLPE đạt chuẩn Hot Set Test!"
        ),
        "cadivi_application_extra": (
            "\n• Công nghệ cốt lõi sản xuất hàng loạt cáp hạ thế CXV & cáp vặn xoắn ABC tại CADIVI Miền Trung: Điểm nút thắt OE cần tối ưu chính là khâu chờ gom mẻ vào Phòng Xông Hơi (Sauna) — đây thường là nơi gây tồn kho WIP lớn nhất và kéo dài Lead Time tới 2–3 ngày trên sơ đồ VSM!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như keo dán kính Silicone hoặc xi măng — khi mới bóp ra còn mềm dẻo dễ tạo hình, nhưng khi gặp hơi ẩm không khí/nước sẽ phản ứng đóng rắn tạo mạng lưới bền chắc không còn chảy lại được nữa!\n"
            "\n• Ví dụ 2 (Rút ngắn Lead Time bể xông Silane tại CADIVI): Khảo sát VSM thấy rulo lõi XLPE chờ gom đủ 12 rulo mới bật lò xông 1 lần (gây chờ WIP 36 giờ) và công nhân cài thời gian xông dư 10 giờ cho cả cáp vỏ mỏng 0.7 mm lẫn vỏ dày 1.8 mm! OE phân nhóm lịch xông theo độ dày lớp cách điện (mỏng 4h, dày 8h) theo chu kỳ cố định mỗi ca giúp giảm 52% tồn kho WIP và tiết kiệm 18% năng lượng đốt lò hơi!"
        ),
        "common_mistakes": (
            "1. Trộn trước hạt nền Silane và hạt xúc tác Catalyst rồi để ngoài không khí > 2 giờ trước khi đùn → Xảy ra phản ứng khâu mạch sớm trong phễu gây bít lưới Screen Pack và sần nhám bề mặt dây!"
        )
    },
    "CCV": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Dây chuyền đùn 3 lớp đồng thời & lưu hóa ống cong cho cáp trung/cao thế' (Catenary Continuous Vulcanization): Để làm cáp điện lực 24kV – 110kV chịu điện áp khổng lồ mà không bị phóng điện cục bộ (Partial Discharge), dây chuyền CCV sử dụng 3 máy đùn nối chung vào 1 đầu đùn 3 lớp (Triple Extrusion Head) bọc đồng thời trong 1 lần chạy: Lớp bán dẫn trong + Lớp cách điện XLPE Peroxide siêu sạch + Lớp bán dẫn ngoài! Ngay sau đầu đùn, sợi cáp đi thẳng vào ống thép hình dây xích nghiêng (Catenary Tube) dài 80–150 mét bơm khí Nitơ siêu tinh khiết áp suất 10–14 bar, nhiệt độ 300–400°C để lưu hóa khâu mạch tức thì, rồi sang đoạn làm nguội áp suất cao — giữ lớp cách điện tròn tuyệt đối và KHÔNG có bọt khí vi mô!"
        ),
        "cadivi_application_extra": (
            "\n• Dây chuyền triệu đô, giá trị gia tăng cao nhất trong hệ sinh thái CADIVI: Khởi động/dừng 1 lần dây chuyền CCV tốn hàng trăm kg nhựa siêu sạch và 4–6 giờ ổn định nhiệt áp! Vì vậy chiến lược OE cho CCV là tối ưu Campaign Scheduling chạy liên tục 24/7 (dùng công nghệ đổi rulo không dừng và nối lõi bay nếu có) để tối đa hóa TEEP và giữ phế khởi động dưới mức tối thiểu!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Khi bơm bóng bay dưới áp suất nước sâu, mọi bong bóng khí nhỏ bên trong đều bị ép tiêu biến hoàn toàn — ống khí Nitơ áp suất 12 bar của dây chuyền CCV làm đúng vai trò ép triệt tiêu mọi lỗ khí micro-void trong cách điện cáp 24kV!\n"
            "\n• Ví dụ 2 (Tối ưu lịch chạy CCV): Gom các đơn hàng cáp trung thế cùng cấp điện áp 24kV chạy nối tiếp nhau trong 1 chiến dịch 5 ngày liên tục (thay vì bật tắt lò 3 lần/tuần) giúp cắt giảm ngay 65% lượng phế nhựa XLPE siêu sạch khởi động/kết thúc mẻ và tiết kiệm hàng trăm triệu đồng mỗi tháng!"
        ),
        "common_mistakes": (
            "1. Cho phép cắt nhỏ lô chạy dây chuyền CCV theo từng đơn hàng lẻ vài trăm mét → Chi phí phế khởi động và thời gian xả nhiệt ống CCV sẽ ăn sạch 100% lợi nhuận đơn hàng!"
        )
    },
    "DSTA": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Lớp áo giáp băng thép kép bảo vệ cáp chôn ngầm' (Double Steel Tape Armoured — mã CADIVI phổ biến là CXV/DATA cho cáp 1 lõi dùng băng nhôm, và CXV/DSTA cho cáp 3–4 lõi dùng băng thép): Quấn 2 lớp băng thép mạ kẽm (dày 0.2 – 0.8 mm) xoắn ốc lệch pha nhau (lớp trên phủ kín khe hở của lớp dưới — tối thiểu độ phủ 100%) bên ngoài lớp bọc đệm (Bedding) và bên dưới lớp vỏ ngoài PVC để chống va đập cơ học, chống cuốc xẻng đào đất và chống chuột bọ gặm nhấm!\n"
            "• Lưu ý điện từ học cực quan trọng: Cáp 1 lõi xoay chiều (Single-core AC) KHÔNG BAO GIỜ được quấn băng thép DSTA (vì thép là vật liệu sắt từ gây dòng điện xoáy Eddy Current nung nóng chảy cáp!) mà bắt buộc phải dùng băng NHÔM không từ tính (DATA) hoặc sợi nhôm (AWA)!"
        ),
        "cadivi_application_extra": (
            "\n• Công đoạn máy bọc giáp (Armouring Machine) tại Xưởng Cáp Lực CADIVI: Điểm OE cần theo dõi là chiều dài cuộn băng thép (giảm số lần dừng hàn nối cuộn băng thép trong 1 rulo cáp), góc quấn & lực căng đồng đều tránh hở khe băng hoặc bóp méo lõi cáp bên trong."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như lớp áo giáp vảy thép xếp chồng lên nhau của hiệp sĩ — hai lớp băng thép lệch khe giúp không có một kẽ hở nào để đất đá sắc nhọn đâm xuyên vào ruột cáp khi chôn ngầm!\n"
            "\n• Ví dụ 2 (Cải tiến OEE máy quấn giáp DSTA tại CADIVI): Thay cuộn băng thép khổ nhỏ dạng bánh (Pad Coil — chỉ dài 400 m, phải dừng máy hàn nối 4 lần/rulo cáp) sang cuộn băng thép quấn chéo Traverse Wound Coil dài 2,500 m → Giảm 80% số lần dừng hàn nối băng, nâng OEE máy quấn giáp từ 58% lên 74%!"
        ),
        "common_mistakes": (
            "1. Dùng băng thép có độ dày quá mỏng hoặc khe quấn vượt quá 50% bề rộng băng theo IEC 60502 → Rớt bài kiểm tra ngoại quan/nghiệm thu dự án điện lực."
        )
    },
    "IEC 60228": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Kinh Thánh quốc tế về Ruột Dẫn Cáp Điện Cách Điện' (tương đương TCVN 6612 tại Việt Nam): Quy định dải tiết diện danh định tiêu chuẩn (0.5, 0.75, 1.0, 1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240, 300, 400, 500, 630... mm²) và phân loại 4 Cấp ruột dẫn theo độ mềm dẻo:\n"
            "  - Class 1: Ruột đồng/nhôm đặc 1 sợi cứng (Solid — vd dây VC đặc).\n"
            "  - Class 2: Ruột bện nhiều sợi cứng/ép nén (Stranded — vd dây CV, cáp CXV lắp cố định).\n"
            "  - Class 5: Ruột bện rất nhiều sợi đồng mảnh mềm dẻo (Flexible — vd dây VCm dùng cho thiết bị di động).\n"
            "  - Class 6: Ruột siêu mềm (Extra-flexible — dây hàn, dây robot).\n"
            "• Điều khoản 'VÀNG' cho OE: Tiêu chuẩn chỉ khống chế ĐIỆN TRỞ DC tối đa tại 20°C (vd: 1.5 mm² đồng ≤ 12.1 Ω/km; 2.5 mm² ≤ 7.41 Ω/km; 50 mm² ≤ 0.387 Ω/km), KHÔNG ép cứng đường kính sợi phải to đúng bằng tiết diện hình học danh định — đó là căn cứ hợp pháp để tối ưu Copper Give-away!"
        ),
        "cadivi_application_extra": (
            "\n• Căn cứ kỹ thuật gốc để OE & Phòng Kỹ thuật CADIVI thiết kế đường kính kéo sợi tối ưu và xây dựng định mức đồng MBOM chuẩn xác cho toàn bộ danh mục sản phẩm."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tính đường kính đồng tối ưu theo IEC 60228 tại CADIVI): Dây đồng 2.5 mm² Class 2 yêu cầu R_max(20°C) = 7.41 Ω/km. Với đồng nguyên chất độ dẫn 101% IACS (điện trở suất 0.01707 Ω·mm²/m), tiết diện thực tối thiểu cần để đạt 7.41 Ω/km chỉ khoảng ~2.36 mm² (chưa kể hệ số bện ~1.015)! Nếu thiết kế an toàn mục tiêu ở 2.43 mm² (đạt điện trở ~7.18 Ω/km, cách giới hạn 7.41 hơn 3%) thay vì kéo dư 2.55 mm², nhà máy hợp pháp tiết kiệm ~4.7% đồng trên mỗi km dây mà vẫn đạt 100% chuẩn IEC 60228 & QCVN 4!"
        ),
        "common_mistakes": (
            "1. Đọc nhầm bảng điện trở giữa ruột đồng trần (Plain Copper) và ruột đồng mạ thiếc (Tinned Copper — được phép có điện trở cao hơn ~1–2%) hoặc nhầm giữa Class 2 và Class 5!"
        )
    },
    "IEC 60502": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Bộ tiêu chuẩn xương sống cho Cáp Điện Lực Cách Điện Đùn từ 1 kV đến 30 kV' (tương đương TCVN 5935 tại Việt Nam), chia làm 2 phần chính:\n"
            "  - IEC 60502-1: Cáp lực hạ thế điện áp danh định 0.6/1 kV và 1.8/3 kV (như các dòng cáp CXV, CVV, CXV/DSTA của CADIVI).\n"
            "  - IEC 60502-2: Cáp lực trung thế 6 kV đến 30 kV (vd: cáp trung thế 24kV CXV/S/DSTA).\n"
            "• Quy định cốt lõi OE bắt buộc thuộc lòng về chiều dày cách điện & vỏ:\n"
            "  - Cách điện (Insulation): Chiều dày trung bình t_avg ≥ t_nom; điểm mỏng nhất t_min ≥ 0.9 × t_nom − 0.1 mm.\n"
            "  - Vỏ ngoài (Oversheath PVC/PE): Điểm mỏng nhất t_min ≥ 0.85 × t_nom − 0.1 mm (riêng vỏ bọc có giáp thép ≥ 0.80 × t_nom − 0.2 mm)."
        ),
        "cadivi_application_extra": (
            "\n• Cơ sở pháp lý tối thượng để OE thiết lập cận giới hạn dưới (LSL) trong biểu đồ SPC Minitab, thẩm định dự án giảm Over-thickness và chạy thử nghiệm tiêu chuẩn xuất xưởng tại CADIVI Miền Trung."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Tính cận LSL chuẩn IEC 60502-1 cho cáp CXV 50 mm²): Chiều dày cách điện XLPE danh định t_nom = 1.0 mm → Điểm mỏng nhất cho phép t_min = 0.9 × 1.0 − 0.1 = 0.80 mm! Khi OE cài thông số SPC trên máy đùn, phải kiểm soát ĐỒNG THỜI 2 cận: Trung bình ≥ 1.00 mm VÀ Điểm mỏng nhất ≥ 0.80 mm (cài giới hạn cảnh báo nội bộ ≥ 0.85 mm để Cpk ≥ 1.33)."
        ),
        "common_mistakes": (
            "1. Áp nhầm công thức t_min của Vỏ ngoài (0.85×t_nom − 0.1) sang Cách điện (0.9×t_nom − 0.1) → Gây rớt mẫu thử nghiệm QC/Quatest cực kỳ nghiêm trọng!"
        )
    },
    "Capstan": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Bánh kéo chủ lực quyết định tốc độ tuyến tính & lực căng toàn dây chuyền': Dù ở máy kéo sợi RBD, máy bện Strander hay máy đùn Extruder, Capstan chính là cơ cấu kéo chủ động kéo sợi đồng/cáp đi qua khuôn kéo hoặc đầu đùn với tốc độ cực kỳ ổn định!\n"
            "• 3 loại phổ biến trong nhà máy cáp:\n"
            "  1. Wheel / Drum Capstan (Bánh kéo tròn — sợi cáp quấn 3–6 vòng quanh tang trống để tạo ma sát kéo cực lớn ở máy kéo sợi & dây nhỏ).\n"
            "  2. Caterpillar / Belt Capstan (Băng xích kẹp song song 2 mặt — dùng cho cáp lực tiết diện lớn không thể uốn cong bán kính nhỏ mà không làm bẹp vỏ cáp!).\n"
            "  3. Dual-Wheel Capstan (Tang kéo đôi có rãnh tách sợi tránh cọ xước vỏ cáp)."
        ),
        "cadivi_application_extra": (
            "\n• Vị trí gắn bộ đếm xung tốc độ & chiều dài chuẩn (Encoder) kết nối MES tại CADIVI: Mọi sai số trượt (Slip) hay mòn đai cao su Caterpillar trên Capstan đều gây ra 2 hậu quả lớn — (1) Sai số chiều dài cuộn cáp giao khách hàng (thiếu mét bị phạt, thừa mét bị mất trắng đồng!), (2) Biến thiên đường kính vỏ cáp liên tục!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Thất thoát ẩn từ bánh đo mét Capstan tại CADIVI): Bánh xe đo mét đặt cạnh Capstan bị mòn đường kính ngoài đi 0.8% mà không hiệu chuẩn định kỳ → Máy báo đã đủ 100.0 m nhưng thực tế cắt ra 100.8 m trên mọi cuộn dây dân dụng! Với 50,000 cuộn/tháng, nhà máy tự động 'tặng không' 40,000 mét dây đồng mỗi tháng!"
        ),
        "common_mistakes": (
            "1. Siết lực ép băng xích Caterpillar quá mạnh để chống trượt khi vỏ cáp còn ấm từ máng làm mát → Bóp dẹt vỏ cáp thành hình ovan (Ovality lỗi) và để lại vết hằn răng cao su dọc thân cáp!"
        )
    },
    "Butt Welder": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Máy hàn giáp mối điện trở / hàn ép nguội nối liên tục 2 cuộn đồng': Trong sản xuất cáp điện, cuộn đồng Rod Ø8.0 mm có khối lượng hữu hạn (~3–4 tấn); khi gần hết cuộn A, thợ đứng máy cắt phẳng đầu cuộn A và cuộn B, kẹp vào máy hàn Butt Welder — dùng dòng điện lớn nung nóng chảy tức thời 2 mặt đầu rồi ép mạnh dính liền thành 1 sợi liên tục (sau đó mài phẳng bavia và ủ mềm mối hàn), hoặc dùng máy hàn ép nguội (Cold Pressure Welder) cho sợi mảnh dưới Ø2.0 mm.\n"
            "• Vai trò sống còn với OEE: Nếu không có mối hàn chắc khỏe, mỗi khi hết 1 cuộn đồng phải dừng máy RBD xâu lại toàn bộ 11 khuôn kéo mất 20 phút; ngược lại, nếu mối hàn bị giòn/bọt khí sẽ gãy ngang trong khuôn kéo (Weld Break) làm dừng máy đột xuất!"
        ),
        "cadivi_application_extra": (
            "\n• Điểm kiểm soát chất lượng mối hàn trọng yếu tại Xưởng Kéo CADIVI Miền Trung: Phân tích Wire Break Forensics thường chỉ ra 20–35% sự cố đứt sợi máy kéo bắt nguồn trực tiếp từ kỹ thuật hàn Butt Welder chưa chuẩn (lệch tâm, chưa mài hết bavia, hoặc quên bước ủ mối hàn)!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như nối 2 đoạn ống nhựa nhiệt PPR thành 1 đoạn liền khối chắc ngang thân ống gốc — nếu ép lệch tâm hay bụi bẩn lọt vào mặt nối thì kéo căng là đứt ngay đúng chỗ hàn!\n"
            "\n• Ví dụ 2 (Chuẩn hóa SOP hàn Butt Welder tại CADIVI): Thống kê Pareto sự cố máy RBD thấy 9 lần đứt/tuần đều gãy ngay tại mối hàn (nhìn bằng kính lúp thấy mặt gãy phẳng có lỗ rỗ). Chuẩn hóa lại SOP: làm sạch đầu đồng bằng cồn/giũa sạch dầu, kiểm tra lực ép kẹp, áp dụng chu trình ủ mối hàn 2 bước và kiểm thử bẻ cong 90° mẫu hàn đầu ca → Giảm lỗi đứt mối hàn từ 9 lần xuống còn < 1 lần/tuần!"
        ),
        "common_mistakes": (
            "1. Dùng cùng 1 chế độ dòng hàn cho đồng Ø8.0 mm và nhôm Ø9.5 mm hoặc không vệ sinh kẹp đồng dẫn điện bị oxy hóa (gây tiếp xúc kém, mối hàn không ngấu)."
        )
    },
    "Multi-wire": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Máy kéo tinh đa sợi siêu năng suất': Thay vì kéo từng sợi đồng đơn lẻ 1 đường dây tốn điện và tốn nhân công, máy kéo Multi-wire (thường 8, 12, 16 hoặc 24 sợi chạy song song cùng lúc!) nhận đồng thời 8–16 sợi đồng trung gian Ø1.38–2.0 mm (từ máy RBD) kéo song song qua các dàn khuôn kim cương PCD thu nhỏ đồng loạt xuống Ø0.15 – Ø0.50 mm với tốc độ 20–35 m/giây, ủ mềm đồng thời toàn bộ và thu chung lên 1 rulo hoặc tách rulo!\n"
            "• Quy luật khắc nghiệt của Multi-wire (Xác suất nối tiếp!): Vì 16 sợi chạy chung 1 hệ thống, chỉ cần ĐÚNG 1 SỢI đứt là cả 16 sợi phải dừng máy cùng lúc — vì vậy độ đồng nhất kích thước khuôn PCD và độ sạch nhũ tương Drawing Emulsion trên máy Multi-wire khắt khe gấp 10 lần máy đơn sợi!"
        ),
        "cadivi_application_extra": (
            "\n• Công cụ tăng năng suất khổng lồ cho dòng dây mềm VCm và ruột đồng nhiều sợi tại CADIVI: 1 máy Multi-wire 16 sợi cho năng suất tương đương 12–16 máy kéo đơn truyền thống nhưng chỉ tốn 1 công nhân đứng máy và giảm 40% điện năng/kg đồng!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Kéo 16 sợi dây diều song song bằng 1 tay quay — năng suất gấp 16 lần nhưng nếu chỉ 1 trong 16 sợi bị rối vướng cành cây thì bạn buộc phải dừng cả 16 sợi lại để gỡ!\n"
            "\n• Ví dụ 2 (Quản lý bộ khuôn Matched Die Set tại CADIVI): Máy Multi-wire 12 sợi hay bị đứt lặp đi lặp lại ở vị trí dây số 4 và số 9. OE đo kiểm tra bằng máy đo đường kính khuôn phát hiện thợ thay lẻ từng khuôn hỏng khiến tỷ lệ nén giữa 12 sợi lệch nhau > 1.5% (gây chùng/căng lệch tốc độ trên cùng trục Capstan!). Áp dụng quy chuẩn thay đồng bộ cả bộ Matched Die Set (dung sai giữa các khuôn trong cùng hàng ≤ 0.002 mm) giúp giảm 65% số lần đứt sợi!"
        ),
        "common_mistakes": (
            "1. Thay lẻ 1 khuôn mới keng vào giữa dàn 15 khuôn đã mòn → Sợi đi qua khuôn mới chạy tốc độ khác hẳn 15 sợi còn lại nên đứt liên hoàn không rõ nguyên nhân!"
        )
    },
    "Drum Twister": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Cỗ máy ghép lõi hạng nặng cho cáp lực nhiều lõi tiết diện lớn' (Laying-up / Cabling Machine): Khi cần ghép 3–4 lõi cáp CXV lớn (vd: 3×240+1×120 mm², nặng nhiều tấn/km) cùng sợi độn (Filler) và quấn băng cố định (Binder Tape), việc quay các rulo xả khổng lồ nặng 5 tấn là bất khả thi. Drum Twister giữ các rulo xả đặt cố định trên sàn và quay chính CẢ CỤM CÀNG THU DÂY (Rotating Take-up Drum) kèm bánh kéo Caterpillar quay quanh trục ngang để xoắn ghép 4 lõi êm ái không bị xoắn vặn nội ứng suất (đặc biệt tối ưu cho lõi ép rẻ quạt Sector-shaped)!"
        ),
        "cadivi_application_extra": (
            "\n• Thiết bị xương sống công đoạn Ghép Lõi (Laying-up) tại phân xưởng Cáp Lực CADIVI: OE tối ưu 3 yếu tố trên Drum Twister — (1) Chuẩn hóa bước xoắn Lay-up Factor tránh lãng phí đồng/nhựa, (2) SMED đổi rulo xả/thu bằng cần trục cẩu & hệ thống kẹp thủy lực, (3) Đồng bộ chiều dài 4 rulo lõi từ Xưởng Đùn để không bị dư 1 lõi lẻ cuối rulo!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Đồng bộ 4 lõi trước Drum Twister tại CADIVI): Khi ghép cáp 3×120+1×70 mm², 3 rulo lõi pha dài lần lượt 1,050 m, 1,020 m, 995 m và rulo trung tính dài 1,080 m → Tổng chiều dài cáp thành phẩm chỉ cắt được đúng theo rulo ngắn nhất (995 m!), làm dư bỏ lãng phí 55 m + 25 m + 85 m = 165 m lõi cáp đồng đã bọc XLPE cực đắt! Áp dụng lệnh chiều dài chuẩn đồng bộ trên MES + hiệu chuẩn bánh đo mét máy đùn đưa độ lệch chiều dài giữa 4 rulo về < ±5 m, tiết kiệm hàng trăm triệu đồng/năm!"
        ),
        "common_mistakes": (
            "1. Cài đặt sai hướng xoay định vị lõi rẻ quạt (Pre-spiral / Back-twist) làm cáp 4 lõi sau ghép bị vặn méo gồ ghề, không tròn đều khi đi vào máy bọc giáp/đùn vỏ ngoài!"
        )
    },
    "Kelvin Bridge": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất 'Cầu đo 4 dây độ chính xác cực cao cho điện trở siêu nhỏ' (Kelvin Double Bridge / Micro-ohmmeter): Một đoạn mẫu cáp đồng 1 mét tiết diện 240 mm² có điện trở chỉ khoảng 0.000075 Ω (75 micro-ohm!) — nhỏ hơn hàng trăm lần so với điện trở tiếp xúc của chính đầu kẹp cá sấu và dây đo đồng hồ vạn năng thông thường! Cầu đo Kelvin sử dụng nguyên lý 4 đầu cực tách biệt (2 kẹp dòng điện C1–C2 bên ngoài cấp dòng chuẩn, 2 lưỡi dao đo điện áp P1–P2 bên trong dài đúng 1,000 mm có tổng trở cực lớn nên không có dòng chạy qua) → Triệt tiêu 100% sai số điện trở dây đo & tiếp xúc kẹp!\n"
            "• Quy đổi nhiệt độ bắt buộc: Điện trở kim loại thay đổi ~0.393% mỗi 1°C! Do đó kết quả đo ở nhiệt độ phòng t°C (vd: 28°C tại Đà Nẵng) PHẢI nhân hệ số hiệu chỉnh về chuẩn 20°C: R_20 = R_t / [1 + 0.00393 × (t − 20)]."
        ),
        "cadivi_application_extra": (
            "\n• Thiết bị kiểm tra bắt buộc tại Phòng Thí Nghiệm QA/QC CADIVI Miền Trung cho mọi lô kéo sợi, bện ruột và cáp thành phẩm để xác nhận tuân thủ IEC 60228 / TCVN 6612 và cấp dữ liệu đầu vào cho dự án tối ưu Copper Give-away!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Sai số thảm họa nếu quên hiệu chỉnh nhiệt độ 20°C): Đo 1 mét mẫu ruột cáp 50 mm² trong phòng nhiệt độ 30°C được R_30 = 0.395 Ω/km. Nếu nhìn vội so với chuẩn IEC 60228 (≤ 0.387 Ω/km) sẽ tưởng nhầm RỚT CHUẨN và ra lệnh dừng xưởng tăng cỡ đồng oan! Quy đổi đúng về 20°C: R_20 = 0.395 / [1 + 0.00393 × (30 − 20)] = 0.380 Ω/km → ĐẠT CHUẨN 100%!\n"
            "\n• Ví dụ 2 (Gage R&R với cầu Kelvin): Đảm bảo mẫu đồng được để ổn định nhiệt trong phòng Lab ít nhất 30 phút sau khi mới kéo nóng ra khỏi máy để tránh sai số nhiệt độ lõi bên trong!"
        ),
        "common_mistakes": (
            "1. Kẹp mẫu cáp còn nóng (50°C vừa cắt từ máy đùn/ủ) lên cầu Kelvin đo ngay trong khi nhập nhiệt độ phòng 25°C vào công thức quy đổi → Báo điện trở cao ảo tới +10%!"
        )
    },
    "Hot Set Test": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất 'Bài thi sống còn xác nhận nhựa XLPE đã thực sự khâu mạch đạt chuẩn' (theo IEC 60811-507): Cắt mẫu cách điện XLPE hình quả tạ (Dumbbell), đánh dấu khoảng cách chuẩn 20 mm, treo quả nặng tạo ứng suất kéo 20 N/cm² (0.20 MPa) bên trong tủ sấy nhiệt độ cực cao 200°C trong đúng 15 phút!\n"
            "• 2 tiêu chí ĐẠT bắt buộc:\n"
            "  1. Độ giãn dài dưới tải tại 200°C (Hot Elongation under load): PHẢI ≤ 175% (nếu nhựa chưa khâu mạch tốt sẽ chảy đứt ngay trong 2 phút đầu!).\n"
            "  2. Độ giãn dư vĩnh viễn sau khi tháo tải & làm nguội (Permanent Set): PHẢI ≤ 15% (giống dây thun tốt — thả ra phải co hồi về gần chiều dài ban đầu!)."
        ),
        "cadivi_application_extra": (
            "\n• Chỉ tiêu bắt buộc phê duyệt xuất xưởng mọi lô cáp XLPE Silane (hạ thế CXV/ABC) và XLPE Peroxide (trung thế CCV) tại Phòng Lab CADIVI Miền Trung — là nút thắt quyết định thời điểm kết thúc chu kỳ xông hơi phòng Sauna!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Treo 1 quả tạ nhỏ vào sợi mì chưa luộc kỹ vs sợi dây thun cao su bền nhiệt trong lò nướng 200°C — nhựa PE thường chảy đứt rụng ngay lập tức, còn nhựa XLPE khâu mạch chuẩn chỉ giãn nhẹ rồi co lại nguyên vẹn!\n"
            "\n• Ví dụ 2 (Ứng dụng OE giảm thời gian chờ xông hơi tại CADIVI): Thí nghiệm DOE lấy mẫu Hot Set Test tại các mốc 4h, 6h, 8h, 10h xông hơi cho cáp XLPE dày 1.2 mm cho thấy ngay tại mốc 6 giờ, Hot Elongation đã đạt 68% (quá tốt so với trần 175%) và Permanent Set đạt 4% (≤ 15%) → OE đề xuất rút thời gian xông chuẩn từ 10 giờ xuống 6.5 giờ, tăng +50% công suất phòng xông mà không tốn 1 đồng đầu tư mua thêm nồi hơi!"
        ),
        "common_mistakes": (
            "1. Rớt Hot Set Test rồi vội đổ lỗi cho nhà cung cấp hạt nhựa mà quên kiểm tra xem công nhân có quên bật bơm định lượng 5% hạt xúc tác Catalyst hay nhiệt độ bể xông bị hụt xuống 55°C hay không!"
        )
    },
    "Hopper Dryer": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Phễu sấy hút ẩm tách nước khỏi hạt nhựa trước khi vào nòng đùn': Nhiều loại nhựa kỹ thuật dùng trong cáp điện (đặc biệt LSZH, Nylon PA, TPU, một số dòng PVC đặc biệt và hạt màu Masterbatch) có tính hút ẩm mạnh trong khí hậu nhiệt đới ẩm Đà Nẵng. Nếu hạt nhựa chứa dù chỉ 0.15% hơi nước chui vào nòng máy đùn nóng 170°C, nước sẽ hóa hơi tức thời nở thể tích gấp 1,600 lần → Tạo hàng loạt bọt khí nổ rỗ bề mặt vỏ cáp, thủng cách điện Spark Tester và suy giảm độ bền kéo Tensile!"
        ),
        "cadivi_application_extra": (
            "\n• Thiết bị phụ trợ không thể thiếu gắn trên nóc máy đùn tại CADIVI Miền Trung (đặc biệt mùa mưa bão miền Trung độ ẩm không khí > 85–90%): OE đưa thông số Nhiệt độ sấy + Thời gian sấy tối thiểu (vd: 70–80°C trong 2–4 giờ) vào bảng Control Plan và kiểm tra LPA hàng ca!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Chiên cá khi cá còn ướt nước sẽ nổ dầu tung tóe — đưa hạt nhựa còn ẩm vào nòng máy đùn 170°C cũng gây hiện tượng 'nổ hơi nước' tạo rỗ li ti khắp vỏ cáp y hệt vậy!\n"
            "\n• Ví dụ 2 (SMED kết hợp Hopper Dryer tại CADIVI): Trước đây đổi mã cáp LSZH phải dừng máy chờ 2 tiếng sấy hạt nhựa mới trên phễu gắn cố định. OE thiết kế 2 phễu sấy di động có bánh xe (External Pre-drying) sấy sẵn hạt lô kế tiếp trong lúc máy đang chạy lô cũ → Cắt giảm trọn vẹn 120 phút thời gian chờ sấy về 0 phút!"
        ),
        "common_mistakes": (
            "1. Bật sấy hạt XLPE Silane bằng phễu sấy khí nóng thông thường không tách ẩm (không phải Dehumidifying Dryer) hoặc sấy quá lâu ở nhiệt độ cao → Kích hoạt khâu mạch sớm ngay trên phễu làm hỏng toàn bộ mẻ nhựa!"
        )
    },
    "ACSR": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Dây nhôm trần lõi thép truyền tải điện đường dây trên không' (Aluminium Conductor Steel Reinforced — mã CADIVI là As / ACSR): Kết hợp hoàn hảo ưu điểm của 2 kim loại — Lõi giữa gồm 1 hoặc 7 sợi dây THÉP mạ kẽm chịu toàn bộ lực kéo căng khổng lồ giữa 2 cột điện cao thế cách nhau 200–500 mét; các lớp bọc xoắn bên ngoài gồm sợi NHÔM độ tinh khiết cao (EC Grade ≥ 61% IACS) nhẹ bằng 1/3 đồng đảm nhiệm dẫn điện chính (nhờ hiệu ứng bề mặt Skin Effect dòng điện xoay chiều tập trung chạy lớp ngoài)!\n"
            "• Cấu trúc phổ biến: Vd ACSR 240/32 nghĩa là 240 mm² nhôm dẫn điện (26 sợi) + 32 mm² lõi thép chịu lực (7 sợi), có bơm mỡ chịu nhiệt chống ăn mòn kẽm/nhôm bên trong lõi."
        ),
        "cadivi_application_extra": (
            "\n• Dòng sản phẩm dự án điện lực (EVN / Tổng Công ty Điện lực Miền Trung EVNCPC) có khối lượng tấn rất lớn tại CADIVI Miền Trung: Yêu cầu kiểm soát chặt lực kéo đứt tổ hợp (UTS), độ bám kẽm lớp thép, khối lượng mỡ chống ăn mòn và cân bằng tải trên dây chuyền kéo nhôm & máy bện Rigid Strander!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như cột bê tông cốt thép — thép ở giữa chịu lực kéo gánh sức nặng cả nhịp dây treo dài hàng trăm mét qua đồi núi bão gió miền Trung, còn nhôm bên ngoài nhẹ và rẻ lo phần dẫn điện!\n"
            "\n• Ví dụ 2 (Tối ưu chất lượng tại CADIVI): Khi bện dây ACSR có bơm mỡ chống gỉ cho dự án vùng ven biển Đà Nẵng – Quảng Nam, nếu lượng mỡ bơm dư chảy tràn ra lớp sợi nhôm ngoài cùng sẽ bị EVN từ chối nghiệm thu do bám bụi gây phóng điện vầng quang! Gắn van định lượng mỡ tự động đồng bộ tốc độ máy bện giúp khống chế đúng định mức g/m và loại bỏ 100% lỗi tràn mỡ."
        ),
        "common_mistakes": (
            "1. Dùng chung máy kéo/khuôn kéo đồng để kéo nhôm mà không vệ sinh tuyệt đối sạch mạt đồng → Hạt bụi đồng bám vào bề mặt nhôm tạo ra pin điện hóa ăn mòn rỗ sợi nhôm cực nhanh ngoài trời!"
        )
    },
    "ABC Cable": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Cáp vặn xoắn treo trên không' (Aerial Bundled Cable — mã CADIVI phổ biến là LV-ABC 2×16, 4×50, 4×95 mm²): Gồm 2 đến 4 lõi dây nhôm bện ép nén bọc lớp cách điện XLPE màu ĐEN chứa 2–2.5% muội than Carbon Black chống tia cực tím UV mặt trời, được vặn xoắn chặt vào nhau tạo thành 1 bó treo trực tiếp lên cột điện hạ thế mà không cần sứ cách điện cồng kềnh!\n"
            "• Ưu điểm vượt trội so với dây trần cũ: An toàn tuyệt đối (cây cối quẹt vào hay bão miền Trung thổi cành cây đè lên KHÔNG bị chập nổ mất điện!), chống câu móc trộm điện, lắp đặt gọn đẹp mỹ quan đô thị và nhận diện từng pha bằng gân nổi (Ribs — 1 gân, 2 gân, 3 gân, trơn) ngay trên vỏ XLPE!"
        ),
        "cadivi_application_extra": (
            "\n• Mặt hàng chủ lực phục vụ ngành điện lực Miền Trung – Tây Nguyên tại Nhà máy CADIVI Hòa Cầm: Quy trình gồm Kéo nhôm → Bện nén ruột nhôm → Đùn cách điện XLPE Đen có gân nổi → Xông hơi Silane → Ghép xoắn bó cáp trên máy Drum Twister/Planetary Strander!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Những bó cáp màu đen xoắn thừng 4 sợi chạy dọc các trụ điện đường phố Việt Nam chịu nắng mưa quanh năm chính là cáp vặn xoắn ABC!\n"
            "\n• Ví dụ 2 (Cải tiến SMED & năng suất cáp ABC tại CADIVI): Vì cả 4 lõi cáp ABC đều dùng 1 loại nhựa XLPE Đen duy nhất (chỉ khác nhau số gân nổi 0–1–2–3 gân trên khuôn Cối Die để phân biệt pha), OE thiết kế lịch chạy Campaign liên tục 4 lõi chỉ cần tháo nhanh vòng Cối tạo gân (5 phút) mà KHÔNG cần xả nhựa Purging — tăng OEE máy đùn thêm +9%!"
        ),
        "common_mistakes": (
            "1. Hàm lượng muội than Carbon Black thấp dưới 2% hoặc phân tán kém → Cáp ABC treo ngoài nắng gay gắt miền Trung chỉ 2–3 năm bị nứt chân chim giòn vỏ cách điện, rớt bài thử lão hóa UV!"
        )
    },
    "Mica FR": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Lá chắn chống cháy 950°C bảo vệ mạch điện khẩn cấp khi hỏa hoạn' (Mica Tape — Fire Resistant Cable theo chuẩn IEC 60331): Băng Mica làm từ khoáng chất Silicat thiên nhiên (Phlogopite/Muscovite) dán trên lưới sợi thủy tinh, chịu nhiệt độ ngọn lửa trực tiếp tới 750–950°C suốt 90–180 phút! Băng được quấn xoắn chồng mép (Overlap 30–50%) 1–2 lớp trực tiếp lên ruột đồng TRƯỚC KHI bọc cách điện XLPE/LSZH. Khi đám cháy thiêu rụi toàn bộ lớp vỏ nhựa bên ngoài thành tro, lớp băng Mica gốm hóa vẫn ôm chặt lấy ruột đồng không bị chập mạch — giữ cho hệ thống bơm nước chữa cháy, thang máy thoát hiểm và đèn Exit tiếp tục hoạt động suốt 3 giờ cứu người!"
        ),
        "cadivi_application_extra": (
            "\n• Dòng cáp chống cháy cao cấp (CXV/FR, CXV/FRT) của CADIVI cho chung cư cao tầng, bệnh viện, trung tâm thương mại: Điểm kiểm soát OE tại máy quấn băng Mica (Taping Machine) là tốc độ quấn tối ưu, tỷ lệ chồng mép (Overlap ≥ 30–50% — chồng quá ít rớt thử lửa IEC 60331, chồng quá dày tốn băng Mica đắt tiền & làm tăng đường kính lõi dẫn tới tốn thêm nhựa XLPE bọc ngoài!) và cảm biến dừng tức thì khi đứt băng."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như bọc một lớp áo chịu lửa của lính cứu hỏa sát vào lõi đồng — dù ngọn lửa 950°C đốt cháy sạch lớp áo nhựa bên ngoài, điện vẫn thông suốt bình thường!\n"
            "\n• Ví dụ 2 (Tối ưu BOM băng Mica tại CADIVI): Khảo sát 5 máy quấn băng Mica phát hiện góc quấn bị lệch khiến độ chồng mép thực tế lên tới 62% thay vì chuẩn kỹ thuật 40% (dùng dư +35% băng Mica và tăng đường kính lõi thêm +0.35 mm làm đội thêm nhựa XLPE!). Hiệu chuẩn lại bảng tra góc quấn & bánh răng tỷ số theo từng cỡ lõi giúp tiết kiệm ~280 triệu VNĐ băng Mica + nhựa/năm!"
        ),
        "common_mistakes": (
            "1. Bỏ qua cảm biến hết băng/đứt băng Mica trên máy quấn tốc độ cao → Chạy hổng mất 30 mét không có băng Mica bên trong lớp cách điện XLPE mà mắt thường bên ngoài KHÔNG THỂ nhìn thấy!"
        )
    },
    "Partial Discharge": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất 'Cơn bão tia sét vi mô âm thầm phá hủy cáp trung/cao thế từ bên trong' (Phóng điện cục bộ — PD, đơn vị đo picocoulomb pC): Bên trong lớp cách điện XLPE dày của cáp 24kV–110kV, nếu tồn tại dù chỉ 1 bọt khí siêu nhỏ (Micro-void), 1 hạt tạp chất bẩn cỡ 0.1 mm hoặc 1 gai nhọn trên lớp bán dẫn, điện trường cực mạnh tập trung tại đó sẽ gây ra các tia phóng điện nhỏ li ti lặp đi lặp lại hàng trăm lần mỗi giây! Tia phóng điện này không làm nổ cáp ngay hôm nay, nhưng sẽ ăn mòn dần tạo thành rễ cây điện (Electrical Treeing) làm nổ tung đường dây ngầm sau 1–3 năm vận hành!\n"
            "• Tiêu chuẩn nghiệm thu cực khắt khe (IEC 60502-2): Thử nghiệm trong phòng lồng Faraday chống nhiễu ở mức điện áp 1.73 × U0 → Cường độ phóng điện cục bộ PHẢI ≤ 5 pC (thậm chí ≤ 2 pC với cáp cao thế)!"
        ),
        "cadivi_application_extra": (
            "\n• Phép thử xuất xưởng bắt buộc 100% trên mọi rulo cáp trung thế 24kV/35kV của CADIVI: Là thước đo tối hậu đánh giá độ sạch của môi trường nạp hạt nhựa XLPE (Cleanroom), độ đồng nhất dây chuyền CCV và độ nhẵn giao diện lớp bán dẫn!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như một vết nứt tóc nhỏ li ti bên trong đập thủy điện — lúc mới xây chưa vỡ ngay, nhưng áp lực nước rỉ thấm ngày đêm sẽ làm vỡ toang cả con đập sau vài năm!\n"
            "\n• Ví dụ 2 (Truy xuất lỗi PD bằng MES): Rulo cáp 24kV đo PD vọt lên 14 pC (> chuẩn 5 pC). Kỹ thuật cắt khoanh vùng đo định vị (TDR) thấy vị trí lỗi nằm đúng mét thứ 420 — truy ngược log dây chuyền CCV trên MES phát hiện tại đúng thời điểm chạy mét 420, áp suất khí Nitơ ống lưu hóa bị sụt đột ngột từ 12 bar xuống 7.5 bar trong 20 giây gây bọt khí trong lớp XLPE!"
        ),
        "common_mistakes": (
            "1. Cho công nhân dùng tay trần dính mồ hôi/bụi bẩn hoặc mở bao hạt nhựa XLPE trung thế ngoài xưởng bụi thay vì hệ thống cấp liệu kín (Closed-loop Vacuum Conveyor) trong phòng sạch!"
        )
    },
    "Water Immersion": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất 'Bài thử đánh thủng cao áp toàn thân trong bể nước điện cực': Theo IEC 60502 / TCVN 5935 / QCVN 4, toàn bộ cuộn cáp mẫu (hoặc từng lõi cách điện không có màn chắn kim loại) được ngâm chìm hoàn toàn trong bể nước (thường nhiệt độ phòng hoặc 20°C trong tối thiểu 1 giờ để nước thấm len vào mọi vết nứt vi mô — nước đóng vai trò điện cực âm bao phủ 100% mọi ngóc ngách bề mặt vỏ cáp!), sau đó đặt điện áp xoay chiều cao thế (vd: 3.5 kV cho cáp 0.6/1 kV; 2.0–2.5 kV cho dây dân dụng 450/750V) liên tục trong 5–15 phút giữa lõi đồng và bể nước → KHÔNG được phép phóng điện đánh thủng (No Breakdown)!\n"
            "• Khác biệt so với Spark Tester: Spark Tester chỉ quét lướt qua điểm đó trong vài mili-giây ở trạng thái khô; Water Immersion thử áp lực điện trường liên tục trong môi trường nước thấm suốt 5–15 phút để bắt cả các khuyết tật 'nứt gần thủng' (Near-pinhole) hay vùng cách điện quá mỏng!"
        ),
        "cadivi_application_extra": (
            "\n• Bài thử nghiệm bắt buộc tại Phòng Lab QA/QC CADIVI trước khi cấp giấy chứng nhận xuất xưởng (Test Report) và phục vụ đánh giá chứng nhận hợp quy QCVN 4."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Spark Tester giống như kiểm tra áo mưa bằng cách xịt tia nước nhanh qua 1 giây; Water Immersion giống như ngâm hẳn chiếc áo mưa dưới bể nước 1 giờ để chắc chắn 100% không có điểm nào bị rỉ ẩm xuyên qua!\n"
            "\n• Ví dụ 2 (Tối ưu dòng chảy Lab tại CADIVI): Nhờ bố trí 2 bể ngâm nước luân phiên (1 bể đang ngâm ủ nước 1h trong khi bể kia đang thử cao áp) theo tư duy tách thao tác Ngoài (SMED), năng lực thông qua mẫu của Phòng Lab tăng gấp đôi từ 12 cuộn/ca lên 24 cuộn/ca!"
        ),
        "common_mistakes": (
            "1. Để hai đầu mẫu cáp lòi lên khỏi mặt nước quá ngắn (< 20–30 cm) hoặc dính ướt → Gây phóng điện bề mặt dọc đầu mẫu (Flashover) làm nhầm tưởng cáp bị thủng cách điện!"
        )
    },
    "IACS": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Thước đo vàng quốc tế về Độ Dẫn Điện của Kim Loại' (International Annealed Copper Standard): Năm 1913, quốc tế chọn 1 mẫu đồng ủ tinh khiết tiêu chuẩn có điện trở suất 0.017241 Ω·mm²/m ở 20°C làm mốc chuẩn 100% IACS. Nhờ công nghệ điện phân tinh luyện hiện đại ngày nay (đồng Cathode tinh khiết 99.99% chuẩn LME Grade A), đồng thanh Rod đạt độ dẫn điện tới 100.5% – 101.8% IACS! Ngược lại, nhôm dẫn điện chuẩn EC đạt ~61–62% IACS, còn thép chỉ đạt ~10–15% IACS.\n"
            "• Ý nghĩa tài chính khổng lồ với OE cáp điện: Tăng độ dẫn điện đồng đầu vào từ 100.0% lên 101.5% IACS nghĩa là bạn được phép giảm hợp pháp ~1.5% khối lượng đồng mà điện trở cáp vẫn đạt nguyên chuẩn IEC 60228!"
        ),
        "cadivi_application_extra": (
            "\n• Chỉ số IQC bắt buộc kiểm tra trên mỗi lô đồng Rod Ø8.0 mm nhập về Nhà máy CADIVI Miền Trung: Chênh lệch chỉ 1% IACS giữa 2 nhà cung cấp đồng Rod tưởng nhỏ nhưng tương đương giá trị hàng tỷ đồng đồng nguyên liệu trên quy mô cả năm!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Bài toán mua hàng Total Cost of Ownership tại CADIVI): Nhà cung cấp A bán đồng Rod rẻ hơn 1 triệu/tấn nhưng độ dẫn điện thực đo chỉ 99.6% IACS; Nhà cung cấp B đắt hơn 1 triệu/tấn nhưng đạt ổn định 101.4% IACS (+1.8% độ dẫn điện, tức tiết kiệm được 1.8% khối lượng đồng × 250 triệu/tấn = 4.5 triệu/tấn!). Chọn Nhà cung cấp B giúp CADIVI LÃI RÒNG thêm 3.5 triệu/tấn!"
        ),
        "common_mistakes": (
            "1. Phòng Mua hàng chỉ nhìn đơn giá đồng/tấn rẻ nhất mà không nhân chéo với chỉ số % IACS thực đo — mua đồng tạp chất cao (IACS thấp) buộc xưởng phải kéo sợi to hơn để đạt điện trở, cuối cùng tốn tiền hơn nhiều!"
        )
    },
    "PCD": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Khuôn kéo kim cương đa tinh thể — Công cụ tạo hình sợi đồng quyết định dung sai & chi phí': Khuôn kéo dây (Drawing Die) có phần lõi làm từ tinh thể kim cương nhân tạo thiêu kết áp suất cực cao (Polycrystalline Diamond — PCD, độ cứng gần bằng kim cương tự nhiên nhưng chống nứt vỡ tốt hơn đơn tinh thể!), khoan lỗ siêu chính xác gồm 4 vùng hình học: Vùng vào (Entrance) → Vùng côn nén biến dạng (Reduction Cone góc 14–18°) → Vùng định cỡ chuẩn đường kính (Bearing Zone dài ~30–40% D) → Vùng thoát (Back Relief).\n"
            "• Chu kỳ sống kinh tế (Re-polishing): Khi khuôn PCD kéo được 15–40 tấn đồng, lỗ khuôn sẽ mòn to dần ra (+0.005 đến +0.015 mm gây Copper Give-away!) → Thay vì vứt bỏ, xưởng bảo trì khuôn đem đánh bóng doa rộng (Re-polish) sang cỡ đường kính kế tiếp lớn hơn để tái sử dụng tới 5–8 vòng đời!"
        ),
        "cadivi_application_extra": (
            "\n• Quản trị Phòng Khuôn (Die Shop) là dự án OE cực hiệu quả tại Xưởng Kéo CADIVI: Thiết lập vòng đời khuôn chuẩn (tấn đồng/khuôn), theo dõi từng mã khuôn bằng mã vạch/Excel và kiểm tra bằng kính hiển vi/máy đo đường kính khuôn trước khi giao xuống máy RBD/Multi-wire."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Khuôn kéo PCD giống như đầu phun bút máy siêu cứng — kéo hàng trăm km đồng đi qua vẫn giữ đường kính tròn nhẵn gương, nhưng nếu chạy quá hạn không bảo dưỡng đánh bóng thì nét mực (sợi đồng) sẽ to dần gây hao mực (Copper Give-away) và dễ rách giấy (đứt sợi)!\n"
            "\n• Ví dụ 2 (Đầu tư PCD thay khuôn hợp kim Tungsten Carbide WC tại CADIVI): Khuôn hợp kim WC rẻ gấp 6 lần nhưng kéo chỉ 1.5 tấn đồng đã mòn loe +0.015 mm, buộc dừng máy thay khuôn liên tục. Chuyển 100% các khuôn định cỡ cuối (Finishing Die) sang PCD bền gấp 20 lần giúp giảm 75% lần dừng thay khuôn và thu hẹp độ lệch đường kính đồng xuống ±0.003 mm!"
        ),
        "common_mistakes": (
            "1. Tiết kiệm sai chỗ bằng cách cố kéo quá hạn tuổi thọ khuôn PCD (để tạo rãnh mòn 'Wear Ring' quá sâu) → Khi mang đi đánh bóng lại bị nứt vỡ lõi kim cương không tái sử dụng được nữa, lại gây xước đứt sợi hàng loạt!"
        )
    },
    "Drawing Emulsion": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Máu tuần hoàn bôi trơn – làm mát – rửa mạt của Xưởng Kéo Sợi': Dung dịch nhũ tương kéo đồng là hỗn hợp dầu tổng hợp/bán tổng hợp pha với nước khử ion (Deionized Water) theo nồng độ nghiêm ngặt (thường 8–12% cho kéo thô RBD, 3–6% cho kéo trung/tinh Multi-wire), thực hiện đồng thời 3 nhiệm vụ sống còn: (1) Bôi trơn màng mỏng giảm ma sát giữa đồng và khuôn PCD (giảm điện năng & chống xước sợi), (2) Hấp thụ nhiệt ma sát khổng lồ sinh ra ở tốc độ 30 m/s, (3) Cuốn trôi bột đồng mịn (Copper Fines) ra khỏi lỗ khuôn và đưa qua hệ thống lọc giấy/lắng ly tâm!"
        ),
        "cadivi_application_extra": (
            "\n• Điểm kiểm tra hàng ngày (Daily TPM / Autonomous Maintenance) của Xưởng Kéo CADIVI Miền Trung với 5 thông số vàng: Nồng độ dầu (đo bằng khúc xạ kế Refractometer), Độ pH (chuẩn 8.2–9.0 — tụt pH < 7.8 là dấu hiệu nhiễm khuẩn thối dầu gây ăn mòn đồng!), Độ dẫn điện nước (Conductivity), Nhiệt độ bể (35–45°C) và Hàm lượng bột đồng mịn lơ lửng."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như dầu nhớt trong động cơ xe máy — nếu để cạn, quá bẩn cặn kim loại hoặc biến chất, dù động cơ đắt tiền đến mấy cũng nhanh chóng nóng bó máy và hỏng xéc-măng!\n"
            "\n• Ví dụ 2 (Cứu tỷ lệ đứt sợi máy Multi-wire CADIVI): Vào mùa hè nắng nóng Đà Nẵng, tỷ lệ đứt sợi máy kéo tinh bất ngờ tăng gấp 3 lần. OE lấy mẫu kiểm tra bể nhũ tương thấy nồng độ tụt xuống chỉ còn 1.8% (do thợ châm thêm nước máy thường bù bay hơi mà quên châm dầu!), độ dẫn điện vọt lên 1,800 µS/cm và vi khuẩn làm pH rớt xuống 7.2 → Vệ sinh bể, pha lại chuẩn 4.5% bằng nước mềm DI và gắn bộ lọc tự động giúp giảm đứt sợi xuống dưới 0.2 lần/tấn ngay ngày hôm sau!"
        ),
        "common_mistakes": (
            "1. Châm trực tiếp nước giếng/nước máy cứng (nhiều Canxi/Magie) vào bể nhũ tương thay vì nước mềm/DI → Sinh xà phòng kết tủa màu xanh bám tắc sạch lỗ khuôn kéo PCD và làm đen bề mặt sợi đồng!"
        )
    },
    "Pay-off": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Cụm xả dây đầu vào đảm bảo lực căng mượt và cấp liệu không dừng': Đặt ở vị trí đầu tiên của mọi dây chuyền (kéo, bện, đùn, bọc giáp, đóng cuộn), bộ xả Pay-off giữ cuộn đồng/rulo bán thành phẩm và nhả dây vào máy với lực căng ổn định. Gồm các dạng chính:\n"
            "  - Passive / Flyer Pay-off (Xả thụ động qua cần quay/phanh ma sát — dùng cho dây mảnh tốc độ cao).\n"
            "  - Driven / Portal Pay-off (Xả chủ động có động cơ biến tần & cần Dancer giữ lực căng không đổi — dùng cho rulo cáp nặng hàng tấn trên máy đùn/Drum Twister).\n"
            "  - Dual Pay-off (Xả đôi 2 rulo có sẵn mối nối đầu-cuối — khi rulo 1 vừa hết dây tự động chuyển mượt sang rulo 2 mà KHÔNG phải dừng máy đùn!)."
        ),
        "cadivi_application_extra": (
            "\n• Công cụ đắc lực để loại bỏ Minor Stops & nâng OEE Availability trên dây chuyền đùn dây dân dụng tốc độ cao tại CADIVI Miền Trung: Nâng cấp từ xả đơn (dừng 10–12 phút mỗi khi hết rulo đồng) lên Dual Pay-off + Accumulator giúp chạy liên tục nhiều giờ liền không ngắt quãng!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như hai cuộn giấy vệ sinh lắp cạnh nhau — cuộn 1 hết là chuyển sang dùng ngay cuộn 2 không gián đoạn, trong lúc đó người phục vụ kịp thay cuộn 1 mới vào sẵn!\n"
            "\n• Ví dụ 2 (Tính toán ROI nâng cấp Dual Pay-off tại CADIVI): Máy đùn dây VC 1.5 chạy tốc độ 400 m/phút, cứ 25 phút hết 1 rulo lõi đồng phải dừng 8 phút thay rulo & nối dây (mất tới 24% thời gian máy + 15 m dây phế mỗi lần dừng!). Lắp cụm xả đôi Dual Pay-off kết hợp hàn nối sẵn ở bên ngoài (External Setup) giúp Availability nhảy từ 68% lên 87% và cắt 100% phế dừng khởi động lại!"
        ),
        "common_mistakes": (
            "1. Đặt phanh lực căng Pay-off quá lớn trên dây đồng mềm đã ủ → Làm giãn kéo mỏng ruột đồng ngay trước đầu đùn, gây rớt điện trở DC IEC 60228 dù khâu kéo sợi đã làm rất chuẩn!"
        )
    },
    "Take-up": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Cụm thu cuốn thành phẩm cuối dây chuyền': Đặt ở cuối mỗi máy kéo, bện, đùn, bọc giáp — thu cuộn sợi đồng/cáp thành phẩm lên rulo thép/gỗ với cơ cấu rải dây (Traversing Unit) xếp từng vòng dây thẳng hàng khít đều nhau, đồng bộ chính xác lực căng với Capstan qua cần điều áp (Dancer).\n"
            "• Công nghệ tối ưu OEE: Máy thu đôi tự động đổi rulo (Dual Automatic Take-up) tự cắt dây và chuyển móc sang rulo rỗng bên cạnh ở tốc độ tới 800–1,200 m/phút mà KHÔNG cần giảm tốc dây chuyền đùn — xóa sổ hoàn toàn thời gian dừng đổi rulo cuối máy!"
        ),
        "cadivi_application_extra": (
            "\n• Yếu tố quyết định trực tiếp độ ổn định của công đoạn KẾ TIẾP tại CADIVI: Nếu máy kéo/bện thu dây lên rulo Take-up bị rối chéo lớp (Cross-over), bó dây kẹt mép rulo hoặc quá lỏng → Công đoạn xả Pay-off tiếp theo sẽ đứt sợi liên tục!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Cuộn chỉ may hay cuộn dây câu — nếu cuốn xếp đều từng lớp khít nhau thì lúc kéo ra cực mượt; nếu cuốn rối đè chồng chéo thì cứ kéo vài mét lại kẹt cục đứt dây!\n"
            "\n• Ví dụ 2 (Lỗi rải dây Take-up tại CADIVI): Bộ cảm biến đảo chiều hành trình rải dây (Traverse Limit Switch) trên máy kéo trung bị lệch 15 mm khiến dây chất đống ở sát thành rulo rồi tụt xuống khe hở → Gây kẹt đứt sợi 12 lần/tuần ở Xưởng Bện. Chỉnh chuẩn hành trình rải dây + thêm điểm kiểm tra vào Checklist PM hàng tuần dứt điểm 100% sự cố!"
        ),
        "common_mistakes": (
            "1. Dùng rulo thu Take-up bị cong vênh mép bích hoặc nứt lõi (không kiểm soát bảo trì rulo) → Ở tốc độ quay cao gây rung lắc dữ dội hỏng ổ bi trục máy và trầy xước vỏ cáp!"
        )
    },
    "Accumulator": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Kho đệm dây di động (Dàn Puly dự trữ) giúp dây chuyền chạy không ngừng nghỉ': Gồm hai dàn bánh xe Puly đối diện nhau (1 dàn cố định, 1 dàn trượt di động nâng hạ bằng khí nén/đối trọng), chứa sẵn bên trong 50 – 300 mét dây đang chạy. Khi đầu vào Pay-off cần dừng 20–40 giây để nối cuộn đồng mới, hoặc đầu ra Take-up cần giảm tốc đổi rulo thành phẩm, dàn Puly tự động co hẹp hoặc giãn rộng ra để nhả/hút lượng dây dự trữ — giữ cho trái tim máy đùn (Extruder) ở giữa tiếp tục chạy ĐỀU ĐẶN ở 100% tốc độ danh định!"
        ),
        "cadivi_application_extra": (
            "\n• Chìa khóa kỹ thuật kết hợp với Dual Pay-off / Dual Take-up để biến dây chuyền đùn dây dân dụng CADIVI từ chạy gián đoạn (Batch) sang chạy liên tục (Continuous Flow) — vừa tăng mạnh OEE vừa xóa sạch hàng chục mét nhựa phế mỗi lần dừng/chạy lại!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như bồn nước dự trữ đặt trên sân thượng — dù máy bơm dưới đất tạm ngừng 2 phút để chuyển nguồn nước, vòi sen trong nhà vẫn chảy đều áp lực không hề bị ngắt!\n"
            "\n• Ví dụ 2 (Tính thời gian đệm của Accumulator tại CADIVI): Dây chuyền đùn dây CV 2.5 chạy tốc độ 300 m/phút (= 5 m/giây), lắp dàn Accumulator sức chứa 180 mét dây → Cho phép công nhân đầu vào có trọn vẹn 180 / 5 = 36 giây dư dả để cắt nối đầu rulo mới mà máy đùn chính không cần giảm tốc độ dù chỉ 1 m/phút!"
        ),
        "common_mistakes": (
            "1. Bỏ qua bảo dưỡng bạc đạn của 20–30 bánh Puly nhỏ trên dàn Accumulator — chỉ cần 2 bánh Puly bị kẹt rỉ không quay trơn là lực ma sát tăng vọt làm xước vỏ nhựa mới đùn hoặc kéo giãn mỏng sợi đồng!"
        )
    },
    "Screen Pack": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Bộ lưới thép lọc tạp chất & tạo áp suất ngược ổn định cho máy đùn': Là cụm 2–4 tấm lưới inox đan mịn xếp chồng từ thô đến siêu mịn (vd: 40 / 80 / 120 / 40 Mesh — số Mesh càng lớn lỗ lưới càng nhỏ!) đặt tựa trên tấm chắn đục lỗ (Breaker Plate) nằm giữa đầu trục vít và cổ đầu Crosshead.\n"
            "• 2 chức năng kép cực kỳ quan trọng: (1) Lọc chặn 100% tạp chất rắn, hạt nhựa chưa nóng chảy (Gels), hạt nhựa cháy đen hoặc vụn kim loại trước khi vào đầu khuôn (ngăn lỗi thủng Spark Tester & sọc bề mặt!), (2) Tạo áp suất ngược (Back Pressure / Melt Pressure) giúp trục vít trộn nhuyễn đồng nhất nhựa nóng chảy!"
        ),
        "cadivi_application_extra": (
            "\n• Điểm kiểm soát trực tiếp liên quan đến Melt Pressure, SMED và chất lượng cách điện tại Xưởng Đùn CADIVI Miền Trung: Theo dõi đồ thị Melt Pressure để thay lưới chủ động đúng lúc (hoặc nâng cấp bộ thay lưới thủy lực nhanh Hydraulic Screen Changer để thay lưới trong < 2 phút thay vì tháo cả đầu máy 30 phút!)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như rây lọc bột mịn trước khi đổ khuôn làm bánh — vừa loại sạch cục bột vón, vỏ trấu vừa giúp dòng bột chảy xuống khuôn thật mịn đều không bị tắc!\n"
            "\n• Ví dụ 2 (Cảnh báo tắc lưới từ Melt Pressure tại CADIVI): Áp suất Melt Pressure ban đầu sau khi lắp bộ lưới mới 40/100/40 Mesh là 185 bar. Sau 18 giờ chạy nhựa tái chế/XLPE, áp suất leo lên 275 bar (+49%) làm giảm 15% sản lượng đùn và tăng nhiệt ma sát gây cháy nhựa! Đặt ngưỡng chuẩn cảnh báo trên HMI/SCADA ở mức 250 bar (thay lưới định kỳ) giúp ổn định tốc độ và chấm dứt vỡ lưới rách ngang!"
        ),
        "common_mistakes": (
            "1. Công nhân tự ý bỏ bớt tấm lưới mịn (100–120 Mesh) để chạy cho nhẹ áp suất đỡ phải thay lưới → Dẫn tới lọt hạt tạp chất vào lớp cách điện gây lỗi thủng Spark Tester tăng vọt!"
        )
    },
    "Masterbatch": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Hạt cô đặc màu sắc & phụ gia kỹ thuật cao': Thay vì mua riêng hàng chục tấn nhựa PVC/XLPE pha sẵn từng màu (gây tồn kho khổng lồ và đọng vốn cho 10 mã màu khác nhau!), nhà máy cáp điện mua nhựa nền tự nhiên không màu (Natural Resin) rồi định lượng pha thêm 1–3% hạt màu đậm đặc (Color Masterbatch) hoặc phụ gia (UV Masterbatch, Catalyst Masterbatch, Antistatic...) ngay tại phễu máy đùn bằng bộ cấp liệu định lượng (Gravimetric/Volumetric Dosing Unit)!"
        ),
        "cadivi_application_extra": (
            "\n• Công cụ đắc lực giúp Phòng Kho & Kế Hoạch CADIVI giảm mạnh tồn kho SKU nhựa (Postponement Strategy): Chỉ cần trữ 1 mã hạt XLPE/PVC Natural số lượng lớn + vài chục kg hạt màu Masterbatch Đỏ/Vàng/Xanh/Đen/Trắng để linh hoạt đáp ứng mọi đơn hàng trong tích tắc!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như tiệm sơn pha màu bằng máy tính — chỉ cần trữ thùng sơn trắng gốc cộng mấy lọ tinh màu đậm đặc là pha được ngay hàng trăm màu khác nhau mà không phải tồn kho 100 thùng sơn pha sẵn!\n"
            "\n• Ví dụ 2 (Chống lệch màu & lãng phí Masterbatch tại CADIVI): Trước đây công nhân tự dùng ca múc trộn tay hạt màu Masterbatch (tỷ lệ dao động từ 1.2% lúc nhạt màu bị QC bắt làm lại đến 3.5% gây tốn gấp đôi tiền hạt màu đắt tiền ~120,000đ/kg!). Lắp bộ định lượng tự động Volumetric Doser khống chế chuẩn xác 1.8% đồng đều theo vòng quay trục vít giúp cắt 35% chi phí Masterbatch và triệt tiêu 100% lỗi lệch tông màu dây!"
        ),
        "common_mistakes": (
            "1. Dùng hạt màu Masterbatch nền nhựa PVC pha vào hạt nhựa nền XLPE (không tương thích hóa học!) → Tạo các hạt vón cục màu loang lổ, giảm mạnh độ giãn dài khi kéo đứt Tensile và gây thủng cách điện!"
        )
    },
    "Cooling Trough": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Máng nước làm mát quyết định phom dáng, ứng suất nội và tốc độ tối đa máy đùn': Ngay khi sợi cáp bọc nhựa nóng 160–200°C rời khỏi đầu Crosshead, nó đi qua hệ thống máng nước dài 10–35 mét để định hình rắn lớp nhựa trước khi chạm vào bánh kéo Capstan và cuộn lên rulo Take-up.\n"
            "• Nguyên tắc làm mát phân tầng chuẩn kỹ thuật (Graded Cooling): Với lớp cách điện dày (XLPE/HDPE dày > 1.5 mm), KHÔNG ĐƯỢC sốc lạnh nước 15°C ngay từ mét đầu tiên! Sốc lạnh làm vỏ ngoài đóng cứng ngay trong khi lớp nhựa sát lõi đồng bên trong vẫn nóng chảy → Khi lớp trong nguội co rút sau sẽ tạo ra LỖ RỖ CHÂN KHÔNG (Shrinkage Voids) ở sát ruột đồng và biến dạng co rút đầu dây (Shrinkback)! Thay vào đó, máng 1 phải dùng nước ấm 50–65°C, máng 2 nước 35–40°C, máng 3 mới làm nguội sâu 20–25°C!"
        ),
        "cadivi_application_extra": (
            "\n• Nút thắt ẩn giới hạn tốc độ đùn tại CADIVI Miền Trung vào mùa nắng nóng Đà Nẵng (tháng 5–8): Khi nước làm mát nóng vượt 32°C, vỏ cáp ra khỏi máng vẫn mềm dính nên công nhân bắt buộc phải hạ tốc độ máy đùn xuống 15–25% (làm tụt OEE Performance nặng nề!)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Nướng 1 chiếc bánh dày mà bật lửa quá to làm vỏ ngoài cháy cứng trong khi ruột bên trong còn sống — làm nguội cáp dày bị sốc lạnh cũng tạo ra ứng suất kéo rỗng ruột bên trong y hệt vậy!\n"
            "\n• Ví dụ 2 (Tăng +18% tốc độ đùn nhờ cải tạo Cooling Trough tại CADIVI): Dây chuyền đùn cáp lực 4×25 mm² bị giới hạn ở 32 m/phút vì cuối máng nước nhiệt độ vỏ cáp vẫn 58°C (cuộn lên rulo bị bết dính vỏ!). OE kiểm tra phát hiện béc phun bị nghẹt cặn vôi và không có vách ngăn đảo dòng nước. Vệ sinh hệ thống phun sương áp lực + bổ sung thêm 4 mét máng phụ kết nối Chiller giúp hạ nhiệt vỏ ra còn 36°C và nâng tốc độ chuẩn lên 38 m/phút (+18.7% sản lượng)!"
        ),
        "common_mistakes": (
            "1. Quên kiểm tra độ sạch của bộ thổi khô khí nén (Air Wipe) ở cuối máng nước → Nước đọng theo cáp đi vào Spark Tester (gây báo lỗi giả liên tục!) và làm nhoè chữ máy in phun trên vỏ cáp!"
        )
    },
    "Tensile": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất 'Bài thử độ bền kéo đứt & độ giãn dài kiểm chứng cơ lý nhựa & kim loại' (IEC 60811-501): Kẹp mẫu nhựa cắt hình quả tạ (Dumbbell) hoặc mẫu ống nhựa cách điện đã rút lõi đồng lên máy kéo nén vạn năng (Universal Testing Machine — UTM), kéo đều với tốc độ chuẩn (vd: 250 mm/phút) đến khi đứt để đo đồng thời 2 chỉ số:\n"
            "  1. Độ bền kéo đứt (Tensile Strength — N/mm² hay MPa): Sức chịu lực tối đa trước khi đứt (vd: XLPE & PVC chuẩn thường yêu cầu ≥ 12.5 MPa).\n"
            "  2. Độ giãn dài khi đứt (Elongation at Break — %): Độ dẻo dai chịu uốn kéo của vật liệu (vd: XLPE ≥ 200%, PVC ≥ 150%, LSZH ≥ 125%)."
        ),
        "cadivi_application_extra": (
            "\n• Phép thử cơ lý nền tảng tại Phòng Lab QA/QC CADIVI để thẩm định chất lượng hạt nhựa đầu vào (IQC), giám sát độ ổn định công nghệ đùn (nếu nhiệt độ đùn sai hoặc độn quá nhiều bột đá CaCO3 thì Tensile & Elongation tụt thảm hại!) và chứng nhận hợp chuẩn QCVN 4 / IEC 60502."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Kéo thử một sợi dây thun mới (chịu lực tốt & giãn dài gấp 3 lần mới đứt) vs sợi dây thun pha nhiều bột độn kém chất lượng (kéo nhẹ mới giãn chút đã đứt phựt!).\n"
            "\n• Ví dụ 2 (Phát hiện nhà cung cấp gian lận bột đá qua Tensile tại CADIVI): Một lô hạt nhựa PVC vỏ giá rẻ hơn 5% mới nhập về cho kết quả Tensile = 11.2 MPa (rớt chuẩn ≥ 12.5 MPa) và Elongation chỉ 118% (rớt chuẩn ≥ 150%). Kiểm tra tỷ trọng & hàm lượng tro (Ash Content) phát hiện tỷ lệ CaCO3 lên tới 42% vượt ngưỡng cho phép → QC chặn ngay từ khâu IQC trước khi đưa xuống xưởng!"
        ),
        "common_mistakes": (
            "1. Dùng lưỡi dao dập mẫu Dumbbell bị cùn mẻ tạo vết khứa li ti ở mép mẫu nhựa → Gây đứt sớm giả tạo ở điểm khứa (Notch Effect), làm rớt chỉ tiêu Elongation oan!"
        )
    },
    "Aging Oven": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất 'Cỗ máy thời gian nén 30 năm tuổi thọ cáp vào trong 7 ngày thử nghiệm' (Tủ thử lão hóa nhiệt theo IEC 60811-401): Thay vì chờ 20 năm mới biết vỏ cáp có bị giòn nứt hay không, Phòng Lab đặt các mẫu cách điện/vỏ cáp treo trong tủ sấy tuần hoàn khí nóng tốc độ trao đổi khí chuẩn (8–20 lần/giờ) ở nhiệt độ cực cao (vd: 100°C cho PVC, 135°C cho XLPE) suốt 7 ngày (168 giờ) liên tục! Sau đó mang ra kéo thử Tensile & Elongation so sánh với mẫu chưa lão hóa:\n"
            "• Tiêu chí ĐẠT (IEC 60502): Độ bền kéo và độ giãn dài sau lão hóa KHÔNG được suy giảm quá ±20% (PVC) hoặc ±25% (XLPE) so với trước lão hóa — chứng minh nhựa không bị bay hơi chất hóa dẻo và không bị oxy hóa giòn gãy trong suốt vòng đời công trình!"
        ),
        "cadivi_application_extra": (
            "\n• Hàng rào chất lượng bắt buộc mỗi khi Phòng Mua Hàng/Kỹ Thuật/OE đề xuất đổi nhà cung cấp hạt nhựa, đổi công thức phối trộn hoặc đổi thông số nhiệt độ đùn (bắt buộc qua quy trình MOC/ECN chờ đủ 7 ngày kết quả Aging Oven trước khi sản xuất đại trà!)."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như để một ống nước nhựa ngoài nắng gắt nhiều năm sẽ trở nên giòn rụm bóp nhẹ là vỡ vụn — tủ Aging Oven mô phỏng nhanh chính quá trình oxy hóa đó trong đúng 168 giờ!\n"
            "\n• Ví dụ 2 (Bài học MOC tại CADIVI): Khi thử nghiệm nhà cung cấp hạt nhựa PVC mới, kết quả kéo thử ngay ngày đầu (Unaged) rất đẹp (Tensile 15.8 MPa, Elongation 220%), nhưng sau 7 ngày trong Aging Oven 100°C, chất hóa dẻo rẻ tiền bay hơi hết làm Elongation tụt xuống còn 95% (biến thiên -56.8%, RỚT NẶNG!) → Quy trình MOC đã cứu nhà máy khỏi nguy cơ thu hồi hàng chục tỷ đồng cáp lỗi sau 1 năm lắp đặt!"
        ),
        "common_mistakes": (
            "1. Cho chạy đại trà ngay khi vừa thấy kết quả Tensile ngày đầu đạt mà không đợi kết quả lão hóa Aging Oven 7 ngày!"
        )
    },
    "L/D Ratio": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Tỷ số hình học quyết định năng lực trộn nóng chảy & tốc độ tối đa của Trục Vít máy đùn': Là tỷ số giữa Chiều dài phần có rãnh xoắn của trục vít (L) chia cho Đường kính ngoài của trục vít (D) — ví dụ máy đùn Ø90 mm có trục vít dài 2,250 mm thì L/D = 25:1.\n"
            "• Quy luật công nghệ đùn cáp:\n"
            "  - L/D ngắn (20:1 – 22:1): Phù hợp nhựa PVC và cao su nhạy nhiệt (thời gian nhựa nằm trong nòng ngắn để tránh phân hủy cháy nhiệt!).\n"
            "  - L/D dài (24:1 – 30:1): Phù hợp nhựa XLPE, HDPE, PE (cần quãng đường trộn & nén dài để nhựa đồng nhất tuyệt đối, chạy tốc độ sản lượng cao và áp suất Melt Pressure ổn định!)."
        ),
        "cadivi_application_extra": (
            "\n• Cơ sở kỹ thuật bắt buộc để OE phân bổ đúng mã sản phẩm vào đúng máy đùn (Machine-Product Allocation Matrix) khi lập kế hoạch CRP/RCCP và thẩm định mua sắm CAPEX máy đùn mới tại CADIVI Miền Trung!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Một đoạn ống trộn dài hơn giúp khuấy đều đường vào nước kỹ hơn nhưng nếu khuấy chất dễ hỏng vì nóng quá lâu lại có nguy cơ bị khét — chọn đúng tỷ số L/D là cân bằng giữa 'trộn kỹ' và 'không quá nhiệt'!\n"
            "\n• Ví dụ 2 (Phân bổ máy thông minh tại CADIVI): Xưởng Đùn có Máy #2 (L/D = 20:1) và Máy #4 (L/D = 26:1). Trước đây Kế hoạch xếp ngẫu nhiên làm Máy #2 chạy XLPE bị trộn không đều phải hạ tốc độ còn 60%, còn Máy #4 chạy PVC bị hay cháy sém đầu nòng! OE lập ma trận phân tuyến cứng: Máy #2 chuyên PVC/LSZH, Máy #4 chuyên XLPE/PE → Cả 2 máy cùng tăng tốc độ chạy chuẩn lên +16% và giảm hẳn phế cháy nhựa!"
        ),
        "common_mistakes": (
            "1. Nghĩ mọi máy đùn cùng đường kính trục vít Ø90 mm đều giống hệt nhau và có cùng năng suất trên mọi loại nhựa (bỏ qua L/D Ratio và tỷ số nén Compression Ratio!)."
        )
    },
    "Melt Pressure": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Huyết áp của máy đùn nhựa' (Áp suất nhựa nóng chảy, đo bằng cảm biến áp suất màng thép đặt ngay trước lưới lọc Screen Pack và trước đầu Crosshead, đơn vị bar hoặc MPa — thường vận hành ở 100 – 350 bar!): Chỉ số Melt Pressure phản ánh tức thời sức khỏe toàn bộ máy đùn:\n"
            "  - Áp suất tăng đều dần theo giờ chạy → Lưới lọc Screen Pack đang bẩn dần (tín hiệu chuẩn để lập kế hoạch thay lưới CBM!).\n"
            "  - Áp suất nhảy vọt đột ngột (> 400–450 bar) → Tắc lưới nghiêm trọng hoặc nhựa bị đông nguội/cháy khâu mạch sớm trong đầu đùn (nguy cơ vỡ chốt an toàn Rupture Disc hoặc hỏng hộp số!).\n"
            "  - Áp suất dao động lên xuống hình sin (Surging ±15–30 bar) → Trục vít mòn, phễu cấp liệu bị vòm nghẽn (Bridging) hoặc vùng cấp liệu quá nóng → Gây biến thiên đường kính vỏ cáp liên tục!"
        ),
        "cadivi_application_extra": (
            "\n• Thông số số 1 cần đưa lên SCADA/MES và biểu đồ SPC trực tuyến của các dây chuyền đùn CADIVI Miền Trung: Ổn định được độ dao động Melt Pressure (≤ ±3–5 bar) chính là chìa khóa kéo độ lệch chuẩn đường kính xuống cực nhỏ để xóa Over-thickness!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như chỉ số huyết áp của cơ thể người — huyết áp ổn định 120 mmHg là cơ thể khỏe mạnh; tăng vọt lên 190 mmHg là dấu hiệu tắc nghẽn mạch máu cực kỳ nguy hiểm cần xử lý ngay!\n"
            "\n• Ví dụ 2 (Chẩn đoán lỗi Surging tại CADIVI): Đường kính dây VC 4.0 trên Laser Gauge cứ dao động phập phồng ±0.06 mm theo chu kỳ 12 giây. OE kéo dữ liệu Melt Pressure thấy áp suất cũng nhảy sóng từ 195 ↔ 228 bar cùng đúng nhịp 12 giây! Kiểm tra phát hiện nhiệt độ vùng cấp liệu Zone 1 bị cài quá cao (155°C thay vì 135°C) làm hạt nhựa chảy sớm dính bết vào cổ trục vít trượt cấp liệu! Hạ Zone 1 xuống 135°C làm Melt Pressure phẳng lặng ở 210 ± 2 bar và Cpk đường kính nhảy từ 0.89 lên 1.62!"
        ),
        "common_mistakes": (
            "1. Để hỏng cảm biến Melt Pressure hàng tháng trời không sửa mà vẫn cho chạy máy đùn 'mù áp suất' → Tới khi tắc lưới nổ tấm an toàn hoặc cháy trục vít thiệt hại hàng trăm triệu đồng!"
        )
    },
    "DDR": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Tỷ số kéo giãn ống nhựa nóng khi bọc ống Tubing' (Draw-Down Ratio): Là tỷ số giữa Tiết diện vòng hình khuyên của khe hở Chày–Cối (Die/Tip Annulus) chia cho Tiết diện thực của lớp vỏ nhựa sau khi bị kéo giãn ôm sát vào cáp:\n"
            "  DDR = (D_die² − D_tip²) / (D_cáp² − D_lõi²).\n"
            "• Ý nghĩa cực kỳ quan trọng của DDR & DRB (Draw Ratio Balance):\n"
            "  - Mỗi loại nhựa có 1 'cửa sổ vàng' DDR riêng (vd: PVC thường 1.5 – 2.5; PE/XLPE thường 2.0 – 3.5; LSZH rất nhạy giãn nên chỉ cho phép DDR nhỏ 1.1 – 1.6!).\n"
            "  - Nếu chọn bộ Chày–Cối quá lớn so với cỡ cáp làm DDR vượt ngưỡng cho phép → Ống nhựa bị kéo căng quá mức gây đứt rách ống nhựa (Cone Break), sần vỏ, co rút mạnh đầu dây (Shrinkback) và giảm độ bền chịu nứt ứng suất!"
        ),
        "cadivi_application_extra": (
            "\n• Kiến thức chuyên gia giúp OE CADIVI chuẩn hóa Thư viện chọn bộ Chày–Cối (Tip & Die Selection Table) khoa học bằng Excel — chấm dứt tình trạng công nhân 'tận dụng đại bộ Cối có sẵn trên bàn' gây lỗi bề mặt và rách nhựa liên tục!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Khi bạn kéo màng bọc thực phẩm bọc quanh hộp thức ăn — kéo căng vừa phải (DDR chuẩn) thì màng phẳng đẹp ôm khít; kéo căng quá đà (DDR quá lớn) thì màng bị rách toạc hoặc co bật mép lại!\n"
            "\n• Ví dụ 2 (Tính toán chọn bộ Chày–Cối cho vỏ cáp LSZH tại CADIVI): Đùn vỏ cáp LSZH có D_lõi = 12.0 mm, D_cáp = 15.0 mm (tiết diện vỏ = 15² − 12² = 81). Công nhân lấy đại bộ Cối cũ D_die = 20.0 mm, D_tip = 13.5 mm → DDR = (20² − 13.5²) / 81 = 2.69 (quá cao so với trần 1.5 của LSZH → liên tục rách ống nhựa!). Đổi đúng bộ Cối D_die = 16.8 mm, D_tip = 13.0 mm → DDR = 1.40 (vào đúng cửa sổ vàng) → Chạy êm mượt tăng tốc độ thêm +25%!"
        ),
        "common_mistakes": (
            "1. Đổi sang nhựa LSZH nhưng vẫn giữ nguyên bảng chọn Chày–Cối cũ của nhựa PVC (vốn có DDR 2.0–2.5) → Làm phế rách vỏ và nhăn bề mặt tăng vọt!"
        )
    },
    "Sharkskin": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Lỗi bề mặt vỏ cáp sần nhám như da cá mập' (Sharkskin Melt Fracture): Khi nhựa nóng chảy có độ nhớt cao (đặc biệt LLDPE, XLPE, HDPE, LSZH) bị ép đi qua khe hở Cối đùn (Die Land) với tốc độ trượt bề mặt (Wall Shear Stress) vượt ngưỡng tới hạn (thường > 0.10 – 0.14 MPa), lớp nhựa ngoài cùng sát thành khuôn bị dính rồi giật xé liên tục (Stick-Slip) ngay tại mép thoát khuôn → Tạo ra hàng loạt gợn sóng nhăn li ti vuông góc với chiều chạy cáp, làm vỏ cáp mờ đục, sần sùi mất thẩm mỹ và dễ gây tập trung ứng suất nứt vỏ!\n"
            "• 4 giải pháp kỹ thuật xử lý triệt để theo thứ tự ưu tiên: (1) Tăng nhẹ nhiệt độ riêng vùng Đầu khuôn Die (+10 đến +20°C để giảm độ nhớt tức thì tại thành khuôn!), (2) Mở rộng khe hở Die Gap (tăng nhẹ DDR trong giới hạn an toàn), (3) Bổ sung 0.5–1% phụ gia trợ gia công PPA (Polymer Processing Aid — tráng 1 lớp màng trượt siêu mỏng lên lòng Cối thép), (4) Chỉ hạ tốc độ đùn khi đã thử 3 cách trên!"
        ),
        "cadivi_application_extra": (
            "\n• Lỗi bề mặt phổ biến nhất cản trở việc đẩy tăng tốc độ máy đùn cáp XLPE/PE/ABC/LSZH tại CADIVI Miền Trung: Hiểu rõ cơ chế vật lý Sharkskin giúp OE phối hợp Kỹ thuật xử lý đúng thuốc mà KHÔNG phải chấp nhận giảm tốc độ chạy máy (bảo vệ OEE Performance)!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Khi bạn bóp kem đánh răng quá mạnh qua một lỗ nhỏ xíu hoặc lúc trời lạnh kem đặc quánh — dòng kem ra bị gợn nhăn sần sùi thay vì trơn bóng mịn!\n"
            "\n• Ví dụ 2 (Khắc phục Sharkskin tăng +20% tốc độ đùn cáp ABC tại CADIVI): Khi đẩy tốc độ đùn lõi XLPE cáp ABC từ 110 lên 135 m/phút thì bề mặt xuất hiện vân Sharkskin mờ nhám. Thay vì chịu thua hạ về 105 m/phút, OE cùng Kỹ thuật tăng nhiệt độ vùng Die từ 190°C lên 205°C và dùng đầu Cối có góc dẫn mượt dài hơn (kết hợp 0.5% PPA) → Vỏ cáp bóng mịn ở 135 m/phút (+22.7% năng suất!)!"
        ),
        "common_mistakes": (
            "1. Nhầm lỗi Sharkskin (vân nhăn đều mịn quanh chu vi do trượt khuôn) với lỗi hạt nhựa bị ẩm (lỗ rỗ bọt khí nổ rải rác không đều) hoặc nhựa cháy Scorch (hạt cứng lợn cợn nổi cục!) → Chữa sai bệnh làm hỏng thêm cả mẻ!"
        )
    },
    "Die Drool": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Hiện tượng nhựa đùn đóng cặn rỉ bẩn quanh mép miệng Cối' (Die Build-up / Die Lip Plate-out): Trong quá trình đùn liên tục (đặc biệt với nhựa nhiều chất độn như LSZH, PVC giàu CaCO3, hoặc PE pha phụ gia/màu không đồng nhất), các thành phần phân tử lượng thấp, sáp bôi trơn, bột độn hoặc nhựa bị phân hủy tách pha tích tụ dần thành cục cặn bám quanh mép ngoài miệng Cối (Die Lip). Tới khi cục cặn đủ to, nó tự bong ra dính chặt vào vỏ cáp đang chạy (tạo cục lồi khuyết tật xấu xí, có thể gây lỗi kích thước & Spark Tester!), buộc công nhân phải dừng máy cạo miệng khuôn liên tục!"
        ),
        "cadivi_application_extra": (
            "\n• Nguyên nhân phổ biến gây Minor Stops (dừng vặt 2–5 phút cứ mỗi 1–2 giờ) trên dây chuyền đùn vỏ PVC & cáp LSZH tại CADIVI Miền Trung: OE phân tích log dừng vặt để phối hợp Kỹ thuật chỉnh góc vát mép khuôn, nhiệt độ Die và chất lượng sấy hạt nhựa."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như cục sơn khô đóng dần quanh miệng vòi chai keo sữa — càng bóp lâu cục cặn càng dày rồi bất chợt rụng xuống làm lem bẩn bề mặt sản phẩm!\n"
            "\n• Ví dụ 2 (Xử lý Die Drool trên chuyền cáp LSZH tại CADIVI): Dây chuyền đùn vỏ LSZH phải dừng 6 lần/ca để công nhân dùng dao đồng gạt cục cặn Die Drool (mất 35 phút/ca & gây 8 điểm lỗi vỏ dính cặn). Kiểm tra thấy mép khuôn Cối có góc sắc 90° bị xước và nhiệt độ miệng khuôn thấp hơn thân khuôn 10°C. Đánh bóng mạ Chrome gương lòng Cối, vát nhẹ mép thoát 30° và giữ nhiệt độ Die Lip cao hơn thân +5°C giúp kéo dài thời gian chạy sạch từ 1.2 giờ lên > 8 giờ liên tục!"
        ),
        "common_mistakes": (
            "1. Công nhân dùng dao sắt/tuốc-nơ-vít thép cứng để cạo cặn Die Drool trên miệng Cối thép → Làm xước rỗ mép khuôn tạo ra 'ổ bám nhựa' mới làm Die Drool ngày càng nặng hơn! Luôn BẮT BUỘC dùng dao bằng ĐỒNG THAU (Brass Scraper) mềm hơn thép khuôn!"
        )
    },
    "Wire Break Forensics": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Khoa học pháp y chẩn đoán nguyên nhân gốc đứt sợi đồng dưới kính hiển vi': Mỗi sự cố đứt sợi trên máy kéo RBD hay Multi-wire đều để lại một 'dấu vân tay hình học' duy nhất trên 2 đầu sợi bị gãy! Thay vì đoán mò hay đổ lỗi lẫn nhau giữa Xưởng Kéo – Phòng Khuôn – Nhà cung cấp đồng Rod, kỹ sư OE/Kỹ thuật soi đầu sợi đứt dưới kính lúp/kính hiển vi 20×–50× phân loại chính xác ngay 6 nhóm nguyên nhân kinh điển:\n"
            "  1. Cup-and-Cone (Hình cốc – hình nón) → Tạp chất oxit/rỗng khí bên trong đồng Rod đầu vào hoặc quá tải nén khuôn!\n"
            "  2. Vết gãy kéo vuốt nhọn như kim (Tensile Necking) → Kẹt puly, rulo xả vướng, hoặc quá lực căng Take-up/Annealer!\n"
            "  3. Vết cắt chéo chữ V / Vảy cá (Crow's Feet / Chevron) → Hỏng khuôn kéo PCD, mòn rãnh, hoặc thiếu bôi trơn Emulsion!\n"
            "  4. Gãy phẳng giòn có rỗ → Lỗi mối hàn Butt Welder!\n"
            "  5. Cháy rỗ vết hồ quang (Arcing Mark) → Đánh lửa chập điện trên tang ủ Inline Annealer!\n"
            "  6. Vết cấn xước cơ học (Mechanical Nick/Sliver) → Va đập trong quá trình vận chuyển cuộn đồng Rod!"
        ),
        "cadivi_application_extra": (
            "\n• Vũ khí giải quyết vấn đề đỉnh cao tại Xưởng Kéo CADIVI Miền Trung: Xây dựng 'Bảng Mẫu Nhận Diện 6 Hình Thái Đứt Sợi' (Visual Reference Chart) gắn ngay cạnh máy RBD & Multi-wire + lưu giữ mẫu sợi đứt gắn thẻ mã lỗi để chạy Pareto 80/20 hàng tuần!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như bác sĩ pháp y nhìn hình dạng vết thương là xác định chính xác hung khí gây án — kỹ sư OE nhìn hình dạng đầu dây đứt là biết ngay lỗi do Đồng Rod, do Khuôn PCD, do Nhũ tương hay do Mối hàn!\n"
            "\n• Ví dụ 2 (Chiến thắng Pareto tại Xưởng Kéo CADIVI): Trước đây cả xưởng cứ cãi nhau 'đứt sợi là tại đồng Rod kém'. OE thu thập 45 đầu sợi đứt trong 2 tuần mang soi kính hiển vi 30× — kết quả bất ngờ: chỉ 15% là Cup-and-Cone (lỗi đồng Rod), còn tới 48% là vết hồ quang cháy trên tang ủ Annealer và 27% là lỗi mối hàn Butt Welder! Tập trung bảo trì đánh bóng cổ góp tang ủ + đào tạo lại hàn giúp giảm 68% số lần đứt sợi chỉ sau 3 tuần!"
        ),
        "common_mistakes": (
            "1. Công nhân vứt ngay 2 đầu dây đứt vào thùng phế trước khi giữ mẫu phân loại → Mất sạch bằng chứng hiện trường, không thể làm phân tích nguyên nhân gốc RCA!"
        )
    },
    "Cup-and-Cone": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Dấu vân tay kinh điển của đứt kéo dẻo trung tâm (Central Burst / Inclusion Break)': Khi kéo sợi đồng qua khuôn PCD, nếu ở tâm sợi đồng có lẫn hạt tạp chất cứng không biến dạng (như hạt oxit đồng Cu2O, hạt xỉ gốm từ lò đúc đồng Rod) hoặc khi góc khuôn kéo quá lớn + tỷ lệ nén không đúng gây ứng suất kéo âm ở tâm sợi, vết nứt bắt đầu hình thành ngay tâm lõi rồi lan tỏa tạo thành 1 đầu lõm hình chiếc CỐC (Cup) và đầu kia lồi hình chiếc NÓN (Cone) khớp khít vào nhau!"
        ),
        "cadivi_application_extra": (
            "\n• Bằng chứng kỹ thuật đanh thép nhất để Phòng QA/Mua Hàng CADIVI làm việc khiếu nại bảo hành (Supplier Claim) với nhà cung cấp đồng Rod Ø8.0 mm (nếu kính hiển vi phát hiện hạt tạp chất đen nằm ngay đáy chén Cup!), hoặc để kiểm tra lại góc côn khuôn kéo PCD tại xưởng!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Phân biệt chính xác nguồn gốc Cup-and-Cone): Nếu đáy hình Cốc sạch bóng đồng đều và đứt lặp lại trên nhiều cuộn đồng của các nhà cung cấp khác nhau → Lỗi do góc khuôn kéo PCD quá rộng hoặc tỷ lệ giảm tiết diện quá thấp (Central Bursting — sửa ngay chuỗi khuôn!). Nếu đáy Cốc có hạt tạp chất đen/xỉ và chỉ tập trung trên 1 lô đồng Rod cụ thể → Khiếu nại ngay lô đồng Rod theo tiêu chuẩn ASTM B49!"
        ),
        "common_mistakes": (
            "1. Thấy đứt kiểu Cup-and-Cone là lập tức kết luận 100% do đồng Rod bẩn mà quên kiểm tra chuỗi tỷ lệ giảm tiết diện khuôn kéo (nếu góc côn > 20° và mức giảm mỗi nấc < 12%, ngay cả đồng siêu tinh khiết cũng vẫn bị nứt tâm Cup-and-Cone!)."
        )
    },
    "Solar Cable": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Cáp chuyên dụng điện mặt trời chuẩn châu Âu EN 50618 / H1Z2Z2-K tuổi thọ 25 năm ngoài trời': Khác hoàn toàn dây điện dân dụng thông thường, cáp Solar phải phơi nắng mưa, tia cực tím UV gay gắt, khí Ozone và dải nhiệt độ khắc nghiệt từ −40°C đến +90°C (l lõi tới 120°C) liên tục 25 năm ở điện áp một chiều DC tới 1,500V!\n"
            "• Cấu tạo đặc thù 3 tầng bảo vệ: (1) Ruột đồng mềm Class 5 MẠ THIẾC (Tinned Copper — chống oxy hóa đen lõi trong môi trường ẩm nóng), (2) Cách điện XLPO/XLPE LSZH khâu mạch bằng chùm tia điện tử E-beam, (3) Vỏ ngoài XLPO/LSZH khâu mạch E-beam chống UV, chống axit/kiềm và chống cháy lan!"
        ),
        "cadivi_application_extra": (
            "\n• Dòng sản phẩm năng lượng tái tạo chiến lược của CADIVI tại thị trường Miền Trung – Tây Nguyên (thủ phủ điện mặt trời áp mái & nhà máy điện mặt trời Việt Nam): Yêu cầu quản lý chặt đường kính lớp mạ thiếc, hệ số đùn 2 lớp đồng thời (Tandem/Co-extrusion) và lịch vận chuyển/chiếu xạ E-beam tối ưu Lead Time."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Nếu dùng dây điện dân dụng PVC bình thường lắp trên mái tôn dưới nắng 60°C Đà Nẵng, chỉ sau 2–3 năm vỏ dây sẽ nứt toác gây rò điện DC 1,000V cực kỳ dễ cháy mái nhà — cáp Solar H1Z2Z2-K được thiết kế để đứng vững 25 năm liên tục!\n"
            "\n• Ví dụ 2 (Tối ưu năng suất đùn cáp Solar CADIVI): Sử dụng dây chuyền đùn kép đồng đùn (Co-extrusion: 2 máy đùn nối 1 đầu chữ T bọc đồng thời cả lớp cách điện trong + lớp vỏ ngoài màu Đen/Đỏ trong 1 lần chạy duy nhất!) giúp giảm 50% số công đoạn vận chuyển rulo và cắt giảm 45% thời gian chuyển đổi so với chạy 2 lần tách biệt!"
        ),
        "common_mistakes": (
            "1. Dùng nhựa XLPE Silane thường thay cho hợp chất XLPO chuyên dụng chuẩn EN 50618 cho cáp Solar → Rớt bài thử chống tia UV 720 giờ, thử ngập axit/kiềm và thử kháng Ozone!"
        )
    },
    "Tinned Copper": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Sợi đồng phủ lớp áo giáp Thiếc siêu mỏng chống ăn mòn hóa học & tăng độ bám hàn' (Đồng mạ thiếc): Phủ một lớp thiếc nguyên chất (Sn ≥ 99.9%) dày khoảng 0.5 – 2.5 micron lên bề mặt sợi đồng (bằng phương pháp nhúng nóng Hot-dip Tinning hoặc mạ điện phân liên tục Electro-tinning).\n"
            "• 3 lợi ích công nghiệp cốt lõi: (1) Chống oxy hóa đen đồng trong môi trường ven biển hơi muối, độ ẩm cao, khí lưu huỳnh (dùng cho cáp Solar, cáp tàu biển, cáp khai thác mỏ, lưới chống nhiễu Braiding), (2) Ngăn phản ứng hóa học giữa đồng và lưu huỳnh trong vỏ cao su EPR/CSP, (3) Giúp bấm đầu cos & hàn thiếc cực kỳ ăn mối hàn không bị rỉ tiếp xúc!"
        ),
        "cadivi_application_extra": (
            "\n• Nguyên liệu quan trọng cho dòng cáp Solar, cáp tàu biển và cáp điều khiển có lưới chống nhiễu tại CADIVI: Cần kiểm soát nghiêm ngặt lớp mạ (bài thử ngâm dung dịch Persulfate kiểm tra độ phủ kín) và tốc độ kéo/bện êm để KHÔNG làm trầy bong lớp thiếc mỏng!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Sợi đồng trần để ngoài không khí biển vài tháng sẽ xỉn đen xanh gỉ đồng (tăng điện trở tiếp xúc gây phát nhiệt cháy mối nối); sợi đồng mạ thiếc vẫn sáng bạc bóng loáng suốt hàng chục năm!\n"
            "\n• Ví dụ 2 (Kiểm soát BOM & giá thành): Đồng mạ thiếc đắt hơn đồng trần ~6–10% và điện trở cho phép theo IEC 60228 cao hơn đồng trần ~1–2% — OE phải tách riêng mã vật tư và định mức Scrap đồng mạ thiếc trên ERP để không trộn lẫn khi thu hồi phế liệu!"
        ),
        "common_mistakes": (
            "1. Để đồng mạ thiếc chạy qua khuôn/puly bị xước nhám ở máy bện Buncher hoặc máy dệt lưới Braiding → Làm tróc lớp thiếc lộ lõi đồng đỏ bên trong, rớt bài thử hóa chất chống ăn mòn!"
        )
    },
    "E-beam": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Công nghệ khâu mạch cách điện bằng máy gia tốc chùm tia điện tử tốc độ ánh sáng' (Electron Beam Cross-linking): Sau khi cáp (vd: cáp Solar EN 50618, cáp ô tô, cáp tàu biển, cáp chịu nhiệt 125–150°C) được đùn nguội bằng hạt nhựa nền pha phụ gia nhạy bức xạ, cuộn cáp được cho chạy tốc độ cao xuyên qua chùm tia electron năng lượng cao (1.5 – 3.0 MeV) phát ra từ máy gia tốc đặt trong hầm chắn bê tông chì. Chùm tia electron đập gãy liên kết C–H để các chuỗi polymer lập tức khóa chéo trực tiếp C–C thành mạng lưới XLPO siêu bền ở nhiệt độ phòng — KHÔNG cần nhiệt độ cao, KHÔNG cần hơi nước hay hóa chất Peroxide!"
        ),
        "cadivi_application_extra": (
            "\n• Công nghệ đỉnh cao cho nhóm cáp Solar, cáp đặc chủng chịu nhiệt & chống cháy xuất khẩu của CADIVI: Điểm OE cần quản trị là lập kế hoạch gom lô chiếu xạ (Batching theo liều lượng kGy chuẩn — thường 120–180 kGy) để đảm bảo mọi đoạn cáp hấp thụ đủ liều bức xạ đồng đều (không thiếu liều gây rớt Hot Set, không quá liều gây giòn vỏ) và rút Lead Time quay vòng!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (So sánh 3 công nghệ khâu mạch XLPE): Silane (rẻ, dùng cho hạ thế CXV/ABC, mất 4–12h xông hơi) vs CCV Peroxide (dùng cho trung/cao thế 24–110kV, đùn lưu hóa nóng áp suất cao) vs E-beam (khâu mạch nguội siêu sạch, không tồn dư hóa chất, chịu nhiệt tới 125–150°C cho cáp Solar & cáp đặc chủng)!\n"
            "\n• Ví dụ 2 (Kiểm soát chất lượng E-beam): Gắn thẻ đo liều bức xạ (Dosimeter Film) đầu và cuối mỗi rulo cáp khi chạy qua máy chiếu xạ để ghi nhận bằng chứng khách quan liều thực đạt 150 ± 10 kGy cho hồ sơ xuất xưởng EN 50618!"
        ),
        "common_mistakes": (
            "1. Bố trí đường chạy chiếu xạ không đồng đều hai mặt (Under-beam Scanning) trên cáp tiết diện lớn → Mặt trên bị quá liều giòn vỏ, mặt đáy bị thiếu liều rớt Hot Set Test!"
        )
    },
    "Braiding": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Công nghệ đan lưới bện giáp/chống nhiễu điện từ (EMI Shielding)': Máy đan lưới (High-speed Rotary/Maypole Braiding Machine — thường 16, 24 hoặc 36 suốt cuộn Bobbin chạy đan chéo nhau kiểu bím tóc!) đan các sợi đồng trần, đồng mạ thiếc hoặc sợi thép mảnh thành lớp lưới ống bao bọc quanh bó lõi cáp điều khiển/tín hiệu (vd: cáp điều khiển CVV-S, cáp chống nhiễu cho nhà máy tự động hóa PLC/biến tần).\n"
            "• Thông số vàng về chất lượng & giá thành: Mật độ che phủ quang học (Optical Coverage — thường yêu cầu ≥ 80% hoặc ≥ 85% theo tiêu chuẩn) phụ thuộc vào số suốt Bobbin, số sợi mỗi suốt, đường kính sợi và góc đan (Braid Angle chuẩn 25°–45°)!"
        ),
        "cadivi_application_extra": (
            "\n• Công đoạn có tốc độ tuyến tính chậm nhất xưởng (thường chỉ 3–12 m/phút!) nên luôn là Nút Thắt Cổ Chai (Bottleneck) của dòng cáp điều khiển & cáp tín hiệu chống nhiễu: Rất phù hợp để OE triển khai mô hình 1 công nhân vận hành đồng thời 6–10 máy Braiding (Man-Machine Chart + Jidoka tự dừng khi đứt sợi hoặc hết suốt) và chuẩn hóa tốc độ quấn Bobbin dự phòng (SMED)!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như máy dệt ống vớ lưới hoặc bện dây dù bọc ngoài ống dẫn nước inox — các sợi chạy chéo hai chiều tạo thành lớp lưới vừa bảo vệ cơ học vừa chắn nhiễu điện từ nhưng cáp vẫn uốn cong mềm dẻo dễ dàng!\n"
            "\n• Ví dụ 2 (Tối ưu BOM & OEE máy Braiding tại CADIVI): Khảo sát 6 máy đan lưới đồng mạ thiếc thấy thợ chỉnh bước đan dày hơn chuẩn khiến độ che phủ thực tế lên tới 93% (trong khi yêu cầu chỉ ≥ 85%) → Làm máy chạy CHẬM ĐI 22% (tụt sản lượng!) và TỐN THÊM 14% đồng mạ thiếc đắt tiền! Chỉnh lại bánh răng bước đan về mục tiêu 87% (cách cận 85% an toàn) giúp TĂNG ngay +22% công suất cổ chai và tiết kiệm > 300 triệu tiền đồng mạ thiếc/năm!"
        ),
        "common_mistakes": (
            "1. Quấn các suốt Bobbin có chiều dài không đều nhau → Suốt ngắn hết trước buộc phải dừng cả máy 24 suốt để thay lẻ liên tục làm tụt thê thảm OEE máy đan lưới!"
        )
    },
    "Water-Blocking": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Công nghệ chống thấm nước dọc trục bảo vệ cáp điện ngầm & vùng ngập lụt' (Longitudinal Water Blocking): Nếu cáp lực chôn ngầm bị rách vỏ ở 1 điểm, nước ngầm có thể len dọc theo khe hở giữa các sợi đồng hoặc dưới lớp màn chắn chạy xa hàng trăm mét làm ăn mòn toàn tuyến cáp và gây hiện tượng 'Rễ cây nước' (Water Treeing — nguyên nhân nổ cáp trung thế!). Công nghệ chống thấm chèn sợi/băng bột siêu hút nước (Super Absorbent Polymer — SAP / Swellable Tape & Yarn) vào các khe lõi: vừa chạm nước, hạt polymer nở trương thể tích gấp 50–100 lần thành lớp gel đặc kín chặn đứng 100% dòng nước trong vòng vài chục cm (đạt thử nghiệm ngâm áp lực cột nước 1 mét suốt 24 giờ không rỉ nước quá 3 mét)!"
        ),
        "cadivi_application_extra": (
            "\n• Rất giá trị cho các dự án cáp ngầm khu đô thị ven biển, vùng trũng ngập lụt miền Trung của CADIVI: Yêu cầu bảo quản băng/sợi chống thấm trong túi kín chống ẩm (vì chỉ cần gặp không khí quá ẩm 90% là băng đã tự hút ẩm giảm hiệu lực trương nở!) và kiểm soát độ căng quấn băng đồng đều."
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Chính là chất hạt siêu thấm nằm bên trong tã bỉm trẻ em — gặp nước lập tức phồng nở thành lớp gel khóa chặt chất lỏng không cho chảy lan đi đâu được nữa!\n"
            "\n• Ví dụ 2 (Quản lý kho vật tư Water-Blocking tại CADIVI): Quy định FIFO nghiêm ngặt và đóng kín lại túi hút chân không ngay sau khi kết thúc ca cho cuộn băng bán dẫn chống thấm (Semi-conductive Water-blocking Tape) đang dùng dở — chấm dứt tình trạng băng bị ẩm mốc vón bột gây rớt thử nghiệm chống thấm nước dọc IEC 60502-2!"
        ),
        "common_mistakes": (
            "1. Dùng nhầm băng chống thấm CÁCH ĐIỆN vào vị trí cần băng chống thấm BÁN DẪN (bọc ngoài màn chắn đồng cáp trung thế) → Gây phóng điện cục bộ Partial Discharge hỏng cả cuộn cáp!"
        )
    },
    "CaCO3 Filler": {
        "lesson_id": "L1.3",
        "definition_extra": (
            "\n• Bản chất 'Bột đá Canxi Cacbonat siêu mịn — Chất độn giảm giá thành nhưng là con dao hai lưỡi trong nhựa PVC': Bột đá CaCO3 (chiếm 15–35% công thức hạt PVC, kích thước hạt siêu mịn 1–3 micron được tráng phủ Axit Stearic) có giá chỉ bằng ~1/5 đến 1/8 giá hạt nhựa nền PVC Resin — giúp hạ giá thành công thức nhựa, tăng độ cứng định hình bề mặt và giảm co ngót. Tuy nhiên, nếu trộn quá tay (> 35–40%) sẽ gây 3 tác hại nặng nề: (1) Đẩy tỷ trọng nhựa (Specific Gravity) tăng vọt (làm tốn nhiều kg nhựa/km hơn khi tính theo thể tích bọc!), (2) Giảm mạnh độ giãn dài khi đứt Tensile & cách điện, (3) Bột đá cứng gây mài mòn nhanh trục vít/nòng máy đùn và tăng cặn Die Drool!"
        ),
        "cadivi_application_extra": (
            "\n• Bài toán tối ưu Giá thành thực trên từng MÉT CÁP (Cost per Volume — VNĐ/lít nhựa, KHÔNG phải VNĐ/kg!) mà Chuyên viên OE CADIVI phải cực kỳ tỉnh táo khi thẩm định phương án giảm giá vật liệu cùng Phòng Mua Hàng & R&D!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Bẫy toán học VNĐ/kg vs VNĐ/lít cực kinh điển tại nhà máy cáp!): Hạt PVC loại A giá 30,000đ/kg, tỷ trọng 1.40 kg/lít → Chi phí thực cho 1 lít lớp vỏ cáp = 30,000 × 1.40 = 42,000đ/lít. Hạt PVC loại B trộn nhiều bột đá CaCO3 bán 'rẻ hơn' giá 28,500đ/kg (-5%), nhưng tỷ trọng nặng lên 1.54 kg/lít → Chi phí thực cho 1 lít lớp vỏ cáp = 28,500 × 1.54 = 43,890đ/lít — ĐẮT HƠN LOẠI A tới +4.5%, chưa kể còn mòn trục vít và yếu cơ lý hơn!"
        ),
        "common_mistakes": (
            "1. Đánh giá rẻ/đắt của hạt nhựa bọc cáp chỉ dựa trên đơn giá VNĐ/kg mà quên nhân với Tỷ trọng (VNĐ/kg × Specific Gravity = VNĐ/dm³) — vì dây cáp bọc theo THỂ TÍCH (mm chiều dày), không phải theo kg!"
        )
    },
    "ASTM B49": {
        "lesson_id": "L1.2",
        "definition_extra": (
            "\n• Bản chất 'Tiêu chuẩn quốc tế Mỹ quy định chất lượng Đồng Thanh Cán Nóng Ø8.0 mm (Copper Redraw Rod) đầu vào cho nhà máy kéo cáp': Quy định toàn diện 5 nhóm chỉ tiêu khắt khe mà cuộn đồng Rod Ø8.0 mm nhập kho phải đạt trước khi đưa lên máy kéo thô RBD:\n"
            "  1. Thành phần hóa học: Đồng tinh khiết ≥ 99.90% – 99.95% (ETP — Electrolytic Tough Pitch, hàm lượng Oxy kiểm soát chặt 150–400 ppm để tránh giòn!).\n"
            "  2. Độ dẫn điện tối thiểu: ≥ 100.0% IACS (hàng cao cấp thường ≥ 101.0% IACS).\n"
            "  3. Độ giãn dài tối thiểu: ≥ 30% (đảm bảo dẻo kéo tới sợi siêu mảnh 0.15 mm không đứt).\n"
            "  4. Độ dày lớp oxit bề mặt (Surface Oxide): Cực mỏng (< 500–1,000 Angstrom) và sạch vảy cán (nếu dày oxit sẽ làm mòn nát khuôn PCD và bít lọc bể nhũ tương!).\n"
            "  5. Phép thử xoắn ngược (Reverse Twist Test): Xoắn thuận/ngược không tách vết nứt dọc (Seam/Sliver)."
        ),
        "cadivi_application_extra": (
            "\n• Tiêu chuẩn gốc để Phòng Mua Hàng, QA IQC và OE CADIVI Miền Trung đánh giá chất lượng đồng Rod đầu vào từ các nhà cung cấp (như đồng nhập khẩu, đồng cán liên tục Southwire/Contirod) và làm căn cứ khiếu nại khi xảy ra lỗi đứt sợi Cup-and-Cone!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Giống như tiêu chuẩn chọn bột mì loại 1 trước khi làm sợi mì siêu mảnh — bột lẫn vỏ trấu hay ẩm vón cục thì dù máy làm mì có đắt tiền đến mấy sợi mì kéo ra cũng đứt vụn!\n"
            "\n• Ví dụ 2 (Thẩm định IQC tại CADIVI): Khi chạy thử lô đồng Rod từ nhà cung cấp mới, OE theo dõi 2 chỉ số đầu vào (ASTM B49 IACS & Reverse Twist) song song với 2 chỉ số tại xưởng (Breaks/Ton trên máy RBD & tỷ lệ mòn khuôn PCD) — phát hiện lô đồng có lớp oxit bề mặt dày làm tăng tốc độ mòn khuôn PCD gấp 1.8 lần và làm bùn bể nhũ tương đen kịt chỉ sau 3 ngày!"
        ),
        "common_mistakes": (
            "1. Chỉ đọc giấy Chứng nhận xuất xưởng (COA) do nhà cung cấp gửi kèm mà không thực hiện test xoắn (Twist Test) và đo độ dẫn điện IACS thực tế trên mẫu cắt tại kho IQC!"
        )
    },
    "QCVN 4": {
        "lesson_id": "L1.4",
        "definition_extra": (
            "\n• Bản chất 'Quy chuẩn Kỹ thuật Quốc gia BẮT BUỘC về An Toàn Thiết Bị Điện và Dây Cáp Điện tại Việt Nam' (QCVN 4:2009/BKHCN cùng sửa đổi bổ sung 1:2016/BKHCN do Bộ Khoa học & Công nghệ ban hành): Khác với tiêu chuẩn tự nguyện (TCVN/IEC), QCVN 4 là QUY ĐỊNH PHÁP LÝ BẮT BUỘC — mọi dây điện dân dụng bọc PVC cách điện điện áp danh định đến và bằng 450/750V (dây VC, VCm, VCmd, CV...) lưu thông tại thị trường Việt Nam PHẢI được chứng nhận hợp quy, gắn dấu CR và vượt qua đầy đủ các bài thử an toàn bắt buộc:\n"
            "  1. Điện trở ruột dẫn (không được ăn gian rút lõi đồng gây phát nhiệt cháy nhà!).\n"
            "  2. Chiều dày cách điện & vỏ bọc tối thiểu (t_min không được mỏng hơn giới hạn!).\n"
            "  3. Thử nghiệm điện áp ngâm nước Water Immersion không đánh thủng.\n"
            "  4. Độ bền kéo đứt & lão hóa nhiệt Tensile / Aging Oven.\n"
            "  5. Thử nghiệm không lan truyền lửa (Flame Retardance)."
        ),
        "cadivi_application_extra": (
            "\n• 'Lằn ranh đỏ bất khả xâm phạm' đối với Chuyên viên OE tại CADIVI Miền Trung: CADIVI là thương hiệu quốc gia uy tín số 1 Việt Nam về dây cáp điện — mọi dự án OE tối ưu giảm Copper Give-away hay giảm Over-thickness PHẢI tuyệt đối tôn trọng trần pháp lý QCVN 4 với biên an toàn thống kê Cpk ≥ 1.33 và có phê duyệt MOC/QA chính thức!"
        ),
        "examples_extra": (
            "\n• Ví dụ 1 (Trực quan): Tiêu chuẩn ISO là điểm cộng uy tín doanh nghiệp tự phấn đấu, còn QCVN 4 giống như giấy đăng kiểm an toàn giao thông — không đạt QCVN 4 là VI PHẠM PHÁP LUẬT, cấm tuyệt đối lưu thông ra thị trường!\n"
            "\n• Ví dụ 2 (Kỷ luật OE tại CADIVI): Khi tính toán phương án tiết kiệm đồng và nhựa trên dây dân dụng VC 2.5 mm², OE luôn đưa điều khoản 'Tuân thủ 100% QCVN 4 (Dấu CR) với biên độ an toàn ≥ 3σ' lên dòng đầu tiên của bản trình bày A3 — tạo sự tin tưởng tuyệt đối với Giám đốc Nhà máy và Trưởng phòng QA/QC!"
        ),
        "common_mistakes": (
            "1. Đề xuất phương án cắt giảm vật liệu cực đoan sát mép sàn để khoe con số tiết kiệm đẹp trên giấy nhưng đẩy tỷ lệ mẫu có nguy cơ rớt QCVN 4 khi cơ quan quản lý thị trường lấy mẫu đột xuất — sai lầm hủy diệt uy tín thương hiệu CADIVI!"
        )
    },
})


def apply_enrichment(glossary_dict):
    """Tự động ghép toàn bộ dữ liệu làm sâu (định nghĩa mở rộng, ví dụ thực tế, sai lầm cần tránh, mã bài học) vào GLOSSARY."""
    for key, ext in ENRICHMENTS.items():
        info = glossary_dict.get(key)
        if not info:
            continue
        def_extra = ext.get("definition_extra", "")
        if def_extra and def_extra not in info.get("definition", ""):
            info["definition"] = info.get("definition", "").rstrip() + def_extra
        app_extra = ext.get("cadivi_application_extra", "")
        if app_extra and app_extra not in info.get("cadivi_application", ""):
            info["cadivi_application"] = info.get("cadivi_application", "").rstrip() + app_extra
        ex_extra = ext.get("examples_extra", "")
        if ex_extra and ex_extra not in info.get("cadivi_example", ""):
            info["cadivi_example"] = info.get("cadivi_example", "").rstrip() + ex_extra
        if ext.get("common_mistakes"):
            info["common_mistakes"] = ext["common_mistakes"]
        if ext.get("lesson_id"):
            info["lesson_id"] = ext["lesson_id"]
