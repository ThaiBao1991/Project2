# -*- coding: utf-8 -*-
"""
interview_bank.py — Ngân Hàng Câu Hỏi Phỏng Vấn & Tình Huống Thực Chiến Tinh Gọn & Dây Cáp Điện (OE)
Được thiết kế chuyên sâu cho Chuyên viên Tối ưu Quy trình (OE — CADIVI),
Kỹ sư Cải tiến Sản xuất (Lean / Continuous Improvement Engineer),
Kỹ sư Quản lý Sản xuất (Industrial Engineer), và Quản lý Nhà máy.

Bao gồm 128 câu hỏi không trùng lặp, chia làm 17 nhóm chủ đề cốt lõi:
1. OEE & 6 Tổn Thất Lớn (Six Big Losses) (6 câu)
2. OLE & Năng Suất Lao Động (Overall Labor Effectiveness) (5 câu)
3. Cân Bằng Chuyền & Takt Time (Line Balancing) (6 câu)
4. SMED & Rút Ngắn Thời Gian Chuyển Đổi (6 câu)
5. 7 Lãng Phí (TIMWOOD) & 5S / Kaizen (6 câu)
6. Poka-Yoke & Chống Lỗi (5 câu)
7. Định Mức BOM & Hao Phí Vật Tư (5 câu)
8. SPC, Năng Lực Quy Trình & Minitab (Cp/Cpk) (6 câu)
9. Bố Trí Mặt Bằng (Plant Layout) & Luồng 1 Sản Phẩm (5 câu)
10. ERP/MES, Dữ Liệu Sản Xuất & Xử Lý Sự Cố Genba (6 câu)
11. Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI) (12 câu)
12. OE, Six Sigma (DMAIC), TOC, TPM & PFMEA (10 câu)
13. Hoạch Định Năng Lực, Điều Độ & Chi Phí (7 câu)
14. Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE (10 câu)
15. Câu Hỏi Hỏi Ngược Nhà Tuyển Dụng CADIVI (5 câu)
16. Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành (12 câu)
17. Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2 (16 câu)
"""

import re

_FORMULA_STRIP_RE = re.compile(r"\[\[(?:[^|\]]+\|)?([^\]]+)\]\]")

QUESTIONS = [
    # =========================================================================
    # CHỦ ĐỀ 1: OEE & 6 TỔN THẤT LỚN (SIX BIG LOSSES)
    # =========================================================================
    {
        "id": "q_oee_01",
        "category": "OEE & 6 Tổn Thất Lớn",
        "type": "Tình Huống Thực Chiến",
        "question": "Máy đột dập dập vỏ linh kiện đạt OEE lên tới 88%, nhưng chuyền lắp ráp phía sau liên tục bị thiếu hàng (Line Starvation). Bạn phân tích nguyên nhân và xử lý như thế nào?",
        "key_points": (
            "• Phân tích điểm mấu chốt:\n"
            "  1. OEE cao cục bộ ở một công đoạn không đồng nghĩa với năng suất toàn chuỗi giá trị (Value Stream) cao. Có thể máy đang dập các mã hàng chưa cần gấp (Overproduction) hoặc lịch chạy không ăn khớp với Takt Time lắp ráp.\n"
            "  2. Hiện tượng Đói hàng (Starvation) chứng tỏ dòng chảy gián đoạn do: Kích thước lô (Batch size) quá lớn khiến chuyền sau phải chờ dập xong cả lô mới có hàng, hoặc thời gian Setup/đổi khuôn lâu, hoặc tỷ lệ hàng lỗi (Scrap) của máy dập phát hiện muộn ở trạm sau.\n"
            "• Giải pháp triển khai:\n"
            "  - Chuyển từ đẩy (Push) sang kéo (Pull) bằng cách thiết lập Siêu thị đệm (Supermarket) có mức tồn kho Min/Max và thẻ rút Kanban.\n"
            "  - Giảm kích thước lô (Batch Size) tại máy đột dập bằng cách áp dụng SMED để đổi khuôn nhanh dưới 10 phút, sản xuất bám sát Takt Time chuyền lắp ráp.\n"
            "  - Đo lường OEE theo kế hoạch nhu cầu thực tế (Schedule-based OEE) thay vì chỉ chạy hết công suất máy."
        )
    },
    {
        "id": "q_oee_02",
        "category": "OEE & 6 Tổn Thất Lớn",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Sự khác biệt cốt lõi giữa OEE (Overall Equipment Effectiveness) và TEEP (Total Effective Equipment Performance) là gì? Khi nào nhà máy nên áp dụng chỉ số TEEP?",
        "key_points": (
            "• Khác biệt công thức & thời gian nền tảng:\n"
            "  - OEE lấy mẫu số là Thời gian Vận hành Kế hoạch (Planned Operating Time, ví dụ: ca 8 tiếng trừ 40 phút nghỉ = 440 phút).\n"
            "  - TEEP lấy mẫu số là Toàn bộ Thời gian Lịch 24/7 (All Calendar Time = 24 giờ × 7 ngày = 168 giờ/tuần).\n"
            "  - Công thức: TEEP = OEE × Tỷ lệ Sử dụng Thời gian (Loading = Planned Time / Total Time).\n"
            "• Khi nào nên sử dụng TEEP:\n"
            "  - Khi doanh nghiệp muốn đánh giá năng lực tiềm tàng mở rộng sản xuất mà không cần mua thêm máy móc mới (chuyển từ chạy 1 ca sang 2 hoặc 3 ca).\n"
            "  - Phục vụ thẩm định dự án đầu tư CAPEX: Khi Giám đốc yêu cầu mua thêm máy móc bạc tỷ, chỉ số TEEP sẽ chứng minh máy hiện tại có thực sự kịch trần công suất hay vẫn đang nhàn rỗi nhiều giờ trong tuần."
        )
    },
    {
        "id": "q_oee_03",
        "category": "OEE & 6 Tổn Thất Lớn",
        "type": "Tình Huống Thực Chiến",
        "question": "Bài toán thực tế: Một máy CNC chạy ca 8 giờ (480 phút), nghỉ giữa ca 40 phút. Trong ca dừng 30 phút vì hỏng dao cắt và 20 phút để căn chỉnh phôi. Chu kỳ lý thuyết là 15 giây/sản phẩm. Thực tế làm ra 920 sản phẩm, phát hiện 46 phế phẩm. Hãy tính OEE và chỉ ra điểm nghẽn lớn nhất?",
        "key_points": (
            "• Tính toán từng thành phần:\n"
            "  1. Thời gian kế hoạch = 480 - 40 = 440 phút.\n"
            "  2. Tổng Downtime = 30 + 20 = 50 phút → Thời gian chạy thực = 440 - 50 = 390 phút (23,400 giây).\n"
            "     → A (Availability) = 390 / 440 = 88.64%.\n"
            "  3. Thời gian lý thuyết sản xuất 920 sp = 920 × 15s = 13,800 giây.\n"
            "     → P (Performance) = 13,800 / 23,400 = 58.97%.\n"
            "  4. Số sản phẩm đạt chuẩn = 920 - 46 = 874 sp.\n"
            "     → Q (Quality) = 874 / 920 = 95.00%.\n"
            "  5. OEE = 88.64% × 58.97% × 95.00% = 49.66%.\n"
            "• Nhận xét & Hành động:\n"
            "  - Điểm nghẽn nghiêm trọng nhất là Năng suất P (58.97%), gây mất mát tới hơn 41% công suất khi máy đang chạy! Cần điều tra tốc độ máy bị ghìm do đâu (mòn dao, phôi cứng bất thường, công nhân thao tác chậm, hoặc các vi dừng dưới 2 phút)."
        )
    },
    {
        "id": "q_oee_04",
        "category": "OEE & 6 Tổn Thất Lớn",
        "type": "Phân Tích Sâu",
        "question": "Hiện tượng 'Dừng máy vi mô' (Minor Stoppage / Idling dưới 5 phút) rất phổ biến nhưng công nhân không ghi chép vào sổ báo cáo vì thời gian ngắn. Là kỹ sư cải tiến, bạn làm cách nào để phát hiện, đo lường và triệt tiêu?",
        "key_points": (
            "• Bản chất vấn đề:\n"
            "  - Các dừng máy < 5 phút (kẹt phôi, cảm biến bẩn, lệch khay, lau chùi ngắn) thường tích lũy 60 - 120 phút mỗi ca, làm suy giảm trực tiếp chỉ số Performance (P) trong OEE mà không thể hiện trên biểu đồ Downtime (A).\n"
            "• Giải pháp phát hiện & đo lường:\n"
            "  1. Gắn cảm biến IoT / bộ đếm xung PLC tại ngõ ra sản phẩm để ghi nhận chu kỳ từng nhịp. Khi khoảng cách giữa 2 sản phẩm vượt ngưỡng 1.5 × Ideal Cycle Time mà không có tín hiệu tắt máy, hệ thống tự động ghi nhận là Vi dừng.\n"
            "  2. Thực hiện video recording (quay video liên tục 2 giờ) tại trạm làm việc kết hợp biểu đồ thời gian chuyển động (Cycle Time Variation Chart) để bóc tách các điểm nghẽn thao tác.\n"
            "• Giải pháp triệt tiêu:\n"
            "  - Chuẩn hóa việc vệ sinh bề mặt máng trượt và sensor (5S Seiso).\n"
            "  - Cải tiến cơ cấu dẫn hướng (Guide rail) chống kẹt phôi theo nguyên lý Poka-Yoke."
        )
    },
    {
        "id": "q_oee_05",
        "category": "OEE & 6 Tổn Thất Lớn",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Khi xác định Chu kỳ lý thuyết (Ideal Cycle Time) để tính OEE, bạn nên lấy theo thông số thiết kế của nhà sản xuất máy (Nameplate) hay kỷ lục tốt nhất thực tế từng đạt (Best Demonstrated)?",
        "key_points": (
            "• Nguyên tắc chuẩn mực quốc tế:\n"
            "  - Luôn chọn chu kỳ nhanh nhất có thể đạt được (tốc độ thiết kế Nameplate từ nhà sản xuất máy) để không bao giờ che giấu lãng phí.\n"
            "• Cảnh báo sai lầm thường gặp:\n"
            "  - Nếu lấy con số trung bình trong quá khứ hoặc hạ thấp chuẩn tốc độ để OEE báo cáo trên giấy đạt trên 85%, nhà máy đang tự 'ru ngủ' và bỏ qua cơ hội cải tiến.\n"
            "• Trường hợp ngoại lệ kỹ thuật:\n"
            "  - Chỉ điều chỉnh chu kỳ thiết kế khi có phê duyệt kỹ thuật chính thức (Engineering Change), ví dụ: thay đổi vật liệu cứng hơn làm dao cắt bắt buộc phải giảm vận tốc vòng quay, hoặc gia công sản phẩm có dung sai khắt khe hơn."
        )
    },
    {
        "id": "q_oee_06",
        "category": "OEE & 6 Tổn Thất Lớn",
        "type": "Phân Tích Sâu",
        "question": "Tổng Giám đốc đặt chỉ tiêu năm mới: 'Toàn bộ máy móc trong mọi phân xưởng phải đạt OEE trên 85% (World-Class OEE)'. Quan điểm của bạn về mục tiêu này thế nào?",
        "key_points": (
            "• Phân tích góc nhìn chiến lược Lean:\n"
            "  1. Mục tiêu OEE = 85% cho TẤT CẢ các máy là một sai lầm phổ biến và gây nguy hiểm cho dòng tiền doanh nghiệp.\n"
            "  2. Theo Lý thuyết Điểm nghẽn (Theory of Constraints - TOC), chỉ có công đoạn Điểm nghẽn (Bottleneck / PACEMAKER) mới cần tối đa hóa OEE để duy trì sản lượng xuất khẩu.\n"
            "  3. Đối với các máy phụ trợ (Non-bottleneck), nếu đẩy OEE lên 85-90% sẽ tạo ra núi tồn kho bán thành phẩm (WIP) khổng lồ, tắc nghẽn mặt bằng và làm chôn vốn lưu động.\n"
            "• Đề xuất điều chỉnh thông minh:\n"
            "  - Phân loại tài sản máy móc: Nhóm A (Nút thắt) quản trị OEE khắt khe ≥ 85%; Nhóm B (Máy phụ trợ) quản trị theo độ linh hoạt chuyển đổi (SMED) và tính sẵn sàng đúng lúc (Just-in-Time Availability)."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 2: OLE & NĂNG SUẤT LAO ĐỘNG (OVERALL LABOR EFFECTIVENESS)
    # =========================================================================
    {
        "id": "q_ole_01",
        "category": "OLE & Năng Suất Lao Động",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Chỉ số OLE (Overall Labor Effectiveness) là gì? Trong một chuyền lắp ráp bán tự động thâm dụng lao động, tại sao OLE lại quan trọng hơn OEE?",
        "key_points": (
            "• Định nghĩa OLE:\n"
            "  - OLE đo lường toàn diện hiệu quả sử dụng nguồn nhân lực trực tiếp sản xuất, gồm 3 thành phần: Sẵn sàng (Availability) × Hiệu suất thao tác (Performance) × Chất lượng tay nghề (Quality).\n"
            "• Tại sao quan trọng hơn OEE ở chuyền thâm dụng lao động:\n"
            "  - Trên chuyền bán tự động, chi phí nhân công trực tiếp chiếm tỷ trọng lớn trong giá thành sản phẩm.\n"
            "  - Thiết bị có thể chạy hoàn hảo không hỏng hóc (OEE cao), nhưng nếu công nhân đi lại tìm linh kiện, đổi ca chậm, thao tác thừa, hoặc thao tác sai làm hỏng sản phẩm thì năng suất toàn chuyền vẫn thấp và chi phí phế phẩm tăng cao.\n"
            "  - OLE phản ánh trung thực năng lực huấn luyện, phân công lao động, và thiết kế trạm làm việc (Workstation Ergonomics)."
        )
    },
    {
        "id": "q_ole_02",
        "category": "OLE & Năng Suất Lao Động",
        "type": "Phân Tích Sâu",
        "question": "Hãy nêu các nguyên nhân thực tế gây suy giảm từng thành phần trong OLE (Availability, Performance, Quality) và biện pháp phòng ngừa tương ứng?",
        "key_points": (
            "• Suy giảm Availability (Sẵn sàng):\n"
            "  - Nguyên nhân: Đi muộn, nghỉ phép không báo trước, họp giao ban đầu ca kéo dài, chờ cấp phát vật tư từ kho, đổi ca trễ.\n"
            "  - Khắc phục: Chuẩn hóa cuộc họp 5 phút đầu ca (Daily Standup), lập ma trận kỹ năng đa năng (Multi-skill Matrix) để sẵn sàng bù người khi vắng mặt.\n"
            "• Suy giảm Performance (Hiệu suất thao tác):\n"
            "  - Nguyên nhân: Công nhân mới chưa quen tay, thao tác thừa (cúi nhặt chi tiết dưới sàn), mệt mỏi thể chất cuối ca, chuyền phân bổ công việc không đều.\n"
            "  - Khắc phục: Đào tạo phương pháp TWI (Training Within Industry), thiết kế lại bàn thao tác chuẩn Ergonomics, cân bằng chuyền (Line Balancing).\n"
            "• Suy giảm Quality (Chất lượng):\n"
            "  - Nguyên nhân: Quên bước kiểm tra, gắn ngược chiều linh kiện, dùng nhầm ốc vít khác thông số kỹ thuật.\n"
            "  - Khắc phục: Áp dụng Poka-Yoke cơ học và hình ảnh bảng thao tác chuẩn trực quan (Visual SOP)."
        )
    },
    {
        "id": "q_ole_03",
        "category": "OLE & Năng Suất Lao Động",
        "type": "Tình Huống Thực Chiến",
        "question": "Báo cáo OLE của phân xưởng chỉ đạt 64% do công nhân thường xuyên phải chờ linh kiện từ kho. Quản đốc đổ lỗi cho kho chậm chạp, còn thủ kho lại đổ lỗi do bộ phận Mua hàng cấp thiếu. Là kỹ sư cải tiến, bạn hòa giải và giải quyết gốc rễ vấn đề này thế nào?",
        "key_points": (
            "• Nguyên tắc làm việc Lean:\n"
            "  - 'Không đổ lỗi cho con người, hãy tấn công quy trình và lỗ hổng hệ thống' (Attack the process, not the person).\n"
            "• Các bước hành động cụ thể tại hiện trường Genba:\n"
            "  1. Thu thập dữ liệu thực tế: Cùng 3 bên ngồi lại tại khu vực tiếp nhận vật tư, đo lường thời gian chờ đợi (Waiting time), tần suất thiếu vật tư theo từng mã hàng (SKU).\n"
            "  2. Thiết lập quy trình Water Spider (Mizusumashi / Người cấp vật tư lưu động): Không để công nhân tự rời trạm chạy vào kho lấy hàng; thay vào đó, nhân viên Water Spider giao vật tư tận bàn theo chu kỳ cố định (ví dụ mỗi 30 phút một lần).\n"
            "  3. Triển khai cơ chế Thẻ rút Kanban hai thùng (Two-bin Kanban): Khi thùng 1 hết, công nhân chuyển thùng 2 lên dùng, thùng rỗng đóng vai trò tín hiệu trực quan để kho cấp đầy bù trước khi chuyền hết hàng.\n"
            "  4. Thống nhất SLA (Cam kết thời gian phản hồi) giữa Sản xuất - Kho - Thu mua và hiển thị cảnh báo Andon trên màn hình theo dõi."
        )
    },
    {
        "id": "q_ole_04",
        "category": "OLE & Năng Suất Lao Động",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Làm thế nào để đo lường chính xác 'Hao phí lao động' (Labor Loss) và tỷ lệ Value-Added (VA) vs Non-Value-Added (NVA) của từng công nhân trên chuyền sản xuất?",
        "key_points": (
            "• Phương pháp thực hiện Time & Motion Study:\n"
            "  1. Ghi hình video quy trình thao tác của công nhân qua 10 - 20 chu kỳ lặp lại liên tiếp.\n"
            "  2. Bóc tách từng cử động chi tiết theo bảng Therbligs hoặc phương pháp MOST (Maynard Operation Sequence Technique).\n"
            "• Phân loại 3 nhóm thời gian thao tác:\n"
            "  - VA (Value-Added): Thao tác làm thay đổi hình dáng, cơ tính, lắp ráp trực tiếp mà khách hàng sẵn sàng trả tiền (ví dụ: siết ốc, hàn mạch).\n"
            "  - NNVA (Necessary Non-Value-Added): Thao tác không tạo giá trị trực tiếp nhưng bắt buộc theo quy trình hiện tại (ví dụ: mở túi nilon bao bì, kiểm tra bằng mắt).\n"
            "  - NVA (Pure Waste): Lãng phí tuyệt đối cần loại bỏ ngay (đi lại lấy dụng cụ, chờ máy chạy, nhặt chi tiết bị rơi, sửa lỗi).\n"
            "• Mục tiêu định lượng: Đẩy tỷ lệ VA từ mức thông thường (15 - 25%) lên trên 50% bằng cách đưa linh kiện về trong tầm với 40cm của công nhân."
        )
    },
    {
        "id": "q_ole_05",
        "category": "OLE & Năng Suất Lao Động",
        "type": "Tình Huống Thực Chiến",
        "question": "Dữ liệu OLE cho thấy năng suất ca đêm (22:00 - 06:00) luôn thấp hơn ca ngày từ 12% đến 18%, đồng thời tỷ lệ lỗi phế phẩm tăng gấp đôi. Bạn sẽ áp dụng các công cụ Lean nào để điều tra và khắc phục?",
        "key_points": (
            "• Điều tra hiện trường ban đêm (Genba Night Shift):\n"
            "  - Kỹ sư cải tiến bắt buộc phải trực tiếp có mặt vào ca đêm từ 01:00 đến 04:00 để quan sát thực tế chứ không chỉ nhìn báo cáo giấy.\n"
            "• Phân tích nguyên nhân bằng biểu đồ Xương cá (Ishikawa) & 5 Why:\n"
            "  - Man (Con người): Nhịp sinh học suy giảm, công nhân buồn ngủ, thiếu giám sát chặt chẽ so với ca ngày.\n"
            "  - Machine (Máy móc): Ca đêm nhiệt độ giảm làm độ nhớt dầu thủy lực thay đổi gây sai số hành trình dập.\n"
            "  - Environment (Môi trường): Ánh sáng tại một số trạm kiểm tra không đủ độ Lux quy chuẩn (dưới 500 Lux) dẫn đến sót lỗi ngoại quan.\n"
            "• Biện pháp giải quyết:\n"
            "  1. Tăng cường chiếu sáng cục bộ bằng đèn LED tại các điểm kiểm tra chất lượng trọng yếu.\n"
            "  2. Bố trí thời gian nghỉ ngắn (Micro-break 5-10 phút) vào khung giờ 02:30 sáng kèm theo bài tập vận động nhẹ giãn cơ.\n"
            "  3. Tăng cường thiết bị chống lỗi Poka-Yoke cảm biến để không phụ thuộc hoàn toàn vào mắt nhìn chủ quan khi công nhân mệt mỏi."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 3: CÂN BẰNG CHUYỀN & TAKT TIME (LINE BALANCING)
    # =========================================================================
    {
        "id": "q_lb_01",
        "category": "Cân Bằng Chuyền & Takt Time",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Takt Time, Cycle Time và Lead Time khác nhau như thế nào? Nêu công thức tính Takt Time khi khách hàng yêu cầu 1,200 sản phẩm/ngày trong ca làm việc 8 giờ có 40 phút nghỉ?",
        "key_points": (
            "• Phân biệt rõ 3 khái niệm thời gian:\n"
            "  - Takt Time: Nhịp điệu nhu cầu của thị trường (Bao lâu khách hàng mua 1 sản phẩm). Đây là con số do thị trường quyết định, không do nhà máy tự chọn.\n"
            "  - Cycle Time: Thời gian thực tế để chuyền hoàn thành xong 1 sản phẩm. Được quyết định bởi năng lực của trạm chậm nhất (Bottleneck).\n"
            "  - Lead Time: Tổng thời gian từ khi nguyên vật liệu đầu vào được đưa vào chuyền đến khi sản phẩm hoàn chỉnh ra khỏi chuyền (bao gồm cả thời gian chờ trong hàng đợi).\n"
            "• Bài toán tính Takt Time:\n"
            "  1. Thời gian làm việc thực tế = (8 giờ × 60 phút) - 40 phút nghỉ = 440 phút = 26,400 giây.\n"
            "  2. Nhu cầu khách hàng = 1,200 sản phẩm.\n"
            "  3. Takt Time = 26,400 giây / 1,200 sản phẩm = 22 giây/sản phẩm.\n"
            "  → Cứ mỗi 22 giây, chuyền phải xuất xưởng đúng 1 sản phẩm đạt chuẩn."
        )
    },
    {
        "id": "q_lb_02",
        "category": "Cân Bằng Chuyền & Takt Time",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Chỉ số Hiệu suất Cân bằng Chuyền (Line Balancing Efficiency - LBE) được tính như thế nào? Khi LBE của một chuyền chỉ đạt 68%, bạn áp dụng biểu đồ Yamazumi chart ra sao để tái cân bằng trên 85%?",
        "key_points": (
            "• Công thức tính LBE:\n"
            "  - LBE = (Tổng thời gian chu kỳ của tất cả các trạm) / (Số lượng trạm × Thời gian chu kỳ của trạm nút thắt Bottleneck) × 100%.\n"
            "• Ứng dụng Yamazumi Chart (Biểu đồ xếp chồng thao tác):\n"
            "  1. Vẽ cột thời gian cho từng công đoạn, phân loại màu: Xanh (Thao tác tạo giá trị VA), Vàng (Cần thiết nhưng không tạo giá trị NNVA), Đỏ (Lãng phí NVA).\n"
            "  2. Vẽ đường nằm ngang đại diện cho Takt Time (hoặc Target Cycle Time).\n"
            "  3. Cắt gọt phần màu Đỏ (loại bỏ lãng phí đi lại, tìm kiếm).\n"
            "  4. San sẻ thao tác: Chuyển các bước lắp ráp đơn giản từ trạm quá tải (Bottleneck) sang trạm rảnh rỗi lân cận.\n"
            "  5. Gộp các trạm có thời gian quá ngắn hoặc dồn tải để giảm bớt 1 vị trí nhân sự, nâng LBE lên trên 85%."
        )
    },
    {
        "id": "q_lb_03",
        "category": "Cân Bằng Chuyền & Takt Time",
        "type": "Tình Huống Thực Chiến",
        "question": "Trên chuyền sản xuất có trạm dập ren là Nút cổ chai (Bottleneck) với Cycle time là 38 giây, trong khi Takt time yêu cầu là 28 giây. Ban giám đốc không duyệt ngân sách mua thêm máy dập ren thứ hai. Bạn xử lý như thế nào để chuyền không bị đứt đoạn sản lượng?",
        "key_points": (
            "• Các bước đột phá không cần CAPEX lớn:\n"
            "  1. Tách Internal vs External: Công nhân đang phải tự chuẩn bị phôi và lau bavia sau khi dập. Hãy tách thao tác chuẩn bị phôi sang khâu trước đó hoặc bố trí đồ gá cấp phôi tự động (Gravity chute).\n"
            "  2. Tinh gọn chu kỳ dập: Phân tích hành trình máy dập. Nếu bàn dập đang lùi về điểm chết trên quá xa, hãy điều chỉnh cữ hành trình ngắn lại (Shorten stroke distance), tiết kiệm ngay 4-6 giây chu kỳ.\n"
            "  3. Kỹ thuật Outsourcing / Chạy trước ca: Cho trạm dập ren này khởi động chạy sớm hơn 1 giờ trước khi toàn chuyền vào ca để tạo sẵn một lượng đệm WIP có kiểm soát (Buffer stock).\n"
            "  4. Cải tiến dụng cụ cắt: Thay mũi taro cao cấp phủ TiN/TiAlN để tăng vận tốc cắt lên 25% mà không làm giảm tuổi thọ mũi khoan."
        )
    },
    {
        "id": "q_lb_04",
        "category": "Cân Bằng Chuyền & Takt Time",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Chỉ số Smoothness Index (SI - Chỉ số Mượt mà) của chuyền là gì? Ý nghĩa khác nhau giữa LBE và SI trong việc đánh giá sự ổn định của dây chuyền sản xuất?",
        "key_points": (
            "• Bản chất toán học của Smoothness Index (SI):\n"
            "  - SI = Căn bậc hai của tổng bình phương chênh lệch giữa chu kỳ từng trạm so với trạm Bottleneck lớn nhất:\n"
            "    SI = sqrt( sum( (Max_Cycle_Time - Cycle_Time_i)^2 ) ).\n"
            "• Khác biệt với LBE:\n"
            "  - LBE càng cao càng tốt (gần 100%), phản ánh tổng thể thời gian không bị lãng phí.\n"
            "  - SI càng nhỏ càng tốt (gần 0), phản ánh mức độ đồng đều tuyệt đối giữa các trạm. Một chuyền có thể có LBE khá cao nhưng SI vẫn lớn nếu một vài trạm quá tải cục bộ nằm xen kẽ các trạm rảnh rỗi.\n"
            "• Mục tiêu Lean: SI càng tiến về 0 thì áp lực công việc giữa các công nhân càng cân bằng, giảm căng thẳng thể chất và triệt tiêu tích tụ bán thành phẩm dọc chuyền."
        )
    },
    {
        "id": "q_lb_05",
        "category": "Cân Bằng Chuyền & Takt Time",
        "type": "Tình Huống Thực Chiến",
        "question": "Làm thế nào để phân biệt và kiểm soát hiện tượng 'Line Starvation' (Đói hàng) và 'Line Blocking' (Nghẽn tắc hàng) giữa 2 công đoạn kế tiếp nhau trên dây chuyền?",
        "key_points": (
            "• Phân biệt hiện tượng:\n"
            "  - Starvation (Đói hàng): Trạm phía sau phải dừng chờ vì trạm phía trước chưa làm xong chi tiết để chuyển tới.\n"
            "  - Blocking (Nghẽn hàng): Trạm phía trước đã làm xong sản phẩm nhưng không thể đẩy đi tiếp vì trạm phía sau đang bận hoặc khu vực trung chuyển (buffer) đã đầy kín chỗ.\n"
            "• Cơ chế kiểm soát theo Lean TPS:\n"
            "  - Áp dụng cơ chế FIFO Lane có giới hạn sức chứa vật lý cố định (ví dụ tối đa 3 khay hàng).\n"
            "  - Khi trạm sau bị trễ, khay hàng thứ 3 đầy sẽ tự động ngắt cữ công tắc cơ học của trạm trước, buộc trạm trước dừng lại (tránh sản xuất thừa).\n"
            "  - Đèn tháp tín hiệu Andon chuyển vàng/đỏ để kỹ thuật viên chuyền lập tức can thiệp hỗ trợ trạm đang gặp khó khăn."
        )
    },
    {
        "id": "q_lb_06",
        "category": "Cân Bằng Chuyền & Takt Time",
        "type": "Phân Tích Sâu",
        "question": "Khi nhu cầu thị trường đột ngột giảm 30%, Takt time của chuyền tăng từ 30 giây lên 43 giây. Bạn sẽ tái thiết kế chuyền và bố trí lại số lượng nhân sự như thế nào theo nguyên lý Shojinka (Lao động linh hoạt)?",
        "key_points": (
            "• Sai lầm cần tránh:\n"
            "  - Giữ nguyên số công nhân và cho chạy chậm lại hoặc cho nghỉ chờ giữa giờ. Điều này làm chi phí nhân công trên mỗi đơn vị sản phẩm tăng vọt và hình thành thói quen thao tác lề mề.\n"
            "• Giải pháp Shojinka (Lao động linh hoạt đa năng):\n"
            "  1. Tính lại số nhân sự tối ưu: N = Tổng thời gian thao tác / Takt time mới.\n"
            "  2. Tái cấu trúc phân công: Gộp công việc của 2 trạm gần nhau cho 1 công nhân phụ trách (ví dụ từ chuyền 10 người giảm xuống còn 7 người).\n"
            "  3. Chuyển đổi công nhân dôi dư sang các dự án Kaizen, bảo dưỡng phòng ngừa TPM, hoặc hỗ trợ các phân xưởng khác đang quá tải.\n"
            "  4. Khi đơn hàng tăng trở lại, quy trình tách trạm diễn ra dễ dàng theo bảng phân công công việc chuẩn (Standardized Work Chart) đã được văn bản hóa."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 4: SMED & RÚT NGẮN THỜI GIAN CHUYỂN ĐỔI (SETUP TIME REDUCTION)
    # =========================================================================
    {
        "id": "q_smed_01",
        "category": "SMED & Rút Ngắn Chuyển Đổi",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Trình bày 4 giai đoạn kinh điển trong phương pháp SMED (Single-Minute Exchange of Die) do TS. Shigeo Shingo sáng lập?",
        "key_points": (
            "• 4 giai đoạn chuẩn mực SMED:\n"
            "  1. Giai đoạn 0 (Hiện trạng chưa phân loại): Thời gian chuyển đổi lộn xộn, máy dừng hoàn toàn trong khi công nhân đi tìm dụng cụ, nâng khuôn, chỉnh ốc.\n"
            "  2. Giai đoạn 1 (Tách biệt Internal & External): Phân loại rạch ròi việc nào CẦN máy dừng mới làm được (Internal) và việc nào CÓ THỂ làm khi máy vẫn đang chạy hàng cũ (External).\n"
            "  3. Giai đoạn 2 (Chuyển đổi Internal thành External): Cải tiến kỹ thuật để các bước đang dừng máy chuyển sang làm trước khi dừng máy (như sấy khuôn trước, chuẩn bị bu-lông, gá sẵn dao phay vào đầu kẹp dự phòng).\n"
            "  4. Giai đoạn 3 (Hợp lý hóa mọi thao tác còn lại): Tối ưu các bước Internal (dùng chốt gài 1 chạm, vặn ốc một vòng) và tối ưu External (bảng dụng cụ bánh xe 5S di động, giảm thời gian đi lại)."
        )
    },
    {
        "id": "q_smed_02",
        "category": "SMED & Rút Ngắn Chuyển Đổi",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Phân biệt 'Chuyển đổi bên trong' (Internal Setup) và 'Chuyển đổi bên ngoài' (External Setup)? Hãy nêu 3 ví dụ thực tế về việc chuyển thao tác Internal thành External?",
        "key_points": (
            "• Định nghĩa ranh giới:\n"
            "  - Internal Setup: Thao tác chỉ có thể thực hiện khi máy ĐÃ DỪNG HẲN (ví dụ: tháo khuôn cũ ra khỏi bàn máy, lắp khuôn mới vào trục ép).\n"
            "  - External Setup: Thao tác có thể thực hiện khi MÁY VẪN ĐANG VẬN HÀNH sản xuất lô cũ (ví dụ: lấy khuôn mới từ kho về sát máy, chuẩn bị sẵn bu-lông, lục giác, kiểm tra bản vẽ).\n"
            "• 3 ví dụ thực tế chuyển đổi Internal → External:\n"
            "  1. Gia nhiệt trước khuôn ép nhựa (Pre-heating): Thay vì lắp khuôn vào máy mới bật điện trở sấy chờ 40 phút, hãy làm trạm sấy điện phụ trợ bên ngoài để khuôn đạt nhiệt độ 80°C sẵn trước khi gá lên máy.\n"
            "  2. Cài đặt dao cắt trước bằng thiết bị đo Tool Presetter: Dao phay CNC được đo chiều dài và set offset sẵn tại bàn nguội bên ngoài, chỉ cần lắp vào mâm dao là chạy ngay, không cần rà phôi thủ công.\n"
            "  3. Chuẩn bị nguyên liệu nhựa sấy sẵn trong phễu di động và đẩy sát máy trước giờ đổi mã."
        )
    },
    {
        "id": "q_smed_03",
        "category": "SMED & Rút Ngắn Chuyển Đổi",
        "type": "Tình Huống Thực Chiến",
        "question": "Thời gian đổi khuôn máy ép nhựa hiện tại là 85 phút khiến nhà máy phải chạy lô lớn (Large Batch) để bù chi phí dừng máy. Hãy lập kế hoạch 5 ngày Kaizen SMED để rút thời gian này xuống dưới 15 phút?",
        "key_points": (
            "• Kế hoạch hành động 5 ngày Kaizen SMED:\n"
            "  - Ngày 1: Quay video toàn cảnh 2 góc nhìn trong suốt quá trình đổi khuôn 85 phút. Không can thiệp, ghi nhận chân thực mọi cử động.\n"
            "  - Ngày 2: Họp toàn đội (Kỹ sư, thợ vận hành, thợ bảo dưỡng), bóc tách từng giây trên video vào bảng phân tích SMED. Xác định các lãng phí đi tìm lục giác, cẩu khuôn, chờ nóng máy.\n"
            "  - Ngày 3: Tách toàn bộ việc tìm khuôn, chuẩn bị ống nước làm mát, nâng khuôn sang External. Đầu tư xe đẩy dụng cụ chuyên dụng ngay cạnh máy.\n"
            "  - Ngày 4: Cải tiến cơ khí: Thay thế bu-lông ren dài bằng cơ cấu kẹp thủy lực (Quick-clamp) hoặc chốt gài chữ U. Đánh dấu cữ vạch màu cố định thay vì căn chỉnh thước đo.\n"
            "  - Ngày 5: Chạy thử nghiệm lần 1, bấm giờ, chuẩn hóa thao tác thành tài liệu SOP có hình ảnh trực quan và gắn thẻ kiểm tra trước khi đổi khuôn (Checklist)."
        )
    },
    {
        "id": "q_smed_04",
        "category": "SMED & Rút Ngắn Chuyển Đổi",
        "type": "Phân Tích Sâu",
        "question": "Kỹ thuật 'Cơ cấu kẹp một chạm' (One-touch clamping) và cơ cấu chuẩn hóa bu-lông (U-shaped washers / Pear-shaped holes) giúp loại bỏ lãng phí vặn ren ốc như thế nào trong SMED?",
        "key_points": (
            "• Triết lý cơ học Shingo:\n"
            "  - 'Vặn ốc ren chỉ thực sự sinh ra lực siết cố định ở vòng quay cuối cùng; toàn bộ các vòng xoay trước đó chỉ là di chuyển không tải lãng phí!'.\n"
            "• Các cơ cấu triệt tiêu vòng xoay ốc:\n"
            "  1. Lỗ hình quả lê (Pear-shaped hole) kết hợp long đen chữ U (U-washer): Bu-lông chỉ cần nới lỏng đúng 1 vòng quay là có thể trượt chi tiết ra ngoài mà không cần tháo hẳn đai ốc.\n"
            "  2. Chốt côn / Chốt nêm (Wedge clamp): Dùng búa gõ nhẹ 1 nhịp chốt nêm hoặc cần gạt khí nén để khóa chặt vị trí thay cho việc siết 4 bu-lông dài.\n"
            "  3. Khóa cam (Cam-action clamp): Gạt tay gạt theo góc 90 độ là tạo đủ lực kẹp phôi định vị.\n"
            "• Kết quả: Rút ngắn thời gian tháo siết từ 15 phút xuống dưới 45 giây cho mỗi lần thay đồ gá."
        )
    },
    {
        "id": "q_smed_05",
        "category": "SMED & Rút Ngắn Chuyển Đổi",
        "type": "Tình Huống Thực Chiến",
        "question": "Phương pháp 'Thao tác song song' (Parallel Operations) tổ chức hai kỹ thuật viên đổi khuôn phối hợp nhịp nhàng như thế nào để vừa an toàn vừa giảm 50% thời gian máy dừng?",
        "key_points": (
            "• Mô hình Đội đua xe F1 (Pit-stop Concept):\n"
            "  - Trong đường hầm đua F1, thay 4 lốp xe chỉ mất 2.5 giây nhờ sự phối hợp đồng bộ của nhiều chuyên gia. Đổi khuôn máy công nghiệp cũng áp dụng nguyên lý tương tự.\n"
            "• Phân chia trách nhiệm chuẩn hóa giữa 2 kỹ thuật viên A & B:\n"
            "  - Kỹ thuật viên A (Chính): Đảm nhiệm bên bảng điều khiển máy, tháo hệ thống kẹp khuôn trước, kết nối mạch điện cảm biến và điều chỉnh thông số.\n"
            "  - Kỹ thuật viên B (Phụ): Đồng thời đứng phía sau máy, tháo ống nước làm mát, nới lỏng kẹp khuôn sau, chuẩn bị móc cẩu.\n"
            "• Quy tắc an toàn bắt buộc:\n"
            "  - Phải có quy ước khẩu lệnh hoặc tín hiệu cờ tay trước khi kích hoạt bấm nút hạ cẩu hoặc đóng kẹp máy ép.\n"
            "  - Thực hiện Lockout/Tagout (LOTO) đúng quy định an toàn điện và áp lực trước khi đưa tay vào vùng nguy hiểm."
        )
    },
    {
        "id": "q_smed_06",
        "category": "SMED & Rút Ngắn Chuyển Đổi",
        "type": "Phân Tích Sâu",
        "question": "Làm thế nào để duy trì bền vững kết quả SMED sau Kaizen mà không bị công nhân quay lại thói quen thao tác lề mề, tuỳ tiện cũ?",
        "key_points": (
            "• Các trụ cột duy trì kết quả (Sustainability):\n"
            "  1. Chuẩn hóa quy trình thao tác chuẩn (SOP): Dán bản hướng dẫn phân công công việc trực quan (kèm ảnh chụp và sơ đồ di chuyển chân) ngay trên thân máy.\n"
            "  2. Ghi nhận thời gian Setup trên bảng theo dõi hàng ngày (Changeover Tracking Board): Mỗi lần đổi khuôn đều phải bấm giờ và ghi công khai số phút. Nếu vượt ngưỡng chuẩn (ví dụ quá 12 phút), kỹ thuật viên phải ghi rõ lý do bất thường.\n"
            "  3. Cơ chế thưởng Kaizen & Đánh giá năng lực: Đưa kỹ năng đổi khuôn nhanh vào tiêu chí nâng bậc lương nghề nghiệp cho kỹ thuật viên.\n"
            "  4. Định kỳ Audit 5S dụng cụ đổi khuôn: Đảm bảo xe đồ nghề luôn đủ dụng cụ chuyên dụng, không bị mượn đi nơi khác làm mất tích."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 5: 7 LÃNG PHÍ (TIMWOOD) & 5S / KAIZEN
    # =========================================================================
    {
        "id": "q_waste_01",
        "category": "7 Lãng Phí (TIMWOOD) & 5S",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Kể tên 7 loại lãng phí trong sản xuất theo Lean (TIMWOOD)? Trong môi trường nhà máy sản xuất tại Việt Nam, loại lãng phí nào nguy hiểm nhất và thường bị che giấu?",
        "key_points": (
            "• 7 loại lãng phí kinh điển (TIMWOOD):\n"
            "  1. T - Transportation (Vận chuyển thừa).\n"
            "  2. I - Inventory (Tồn kho dư thừa: nguyên liệu, bán thành phẩm WIP, thành phẩm).\n"
            "  3. M - Motion (Thao tác thừa, cúi gập, vươn người, tìm kiếm).\n"
            "  4. W - Waiting (Chờ đợi: chờ máy, chờ vật tư, chờ phê duyệt).\n"
            "  5. O - Overproduction (Sản xuất thừa / Làm sớm hơn nhu cầu).\n"
            "  6. O - Overprocessing (Gia công thừa / Yêu cầu quá mức tiêu chuẩn khách hàng).\n"
            "  7. D - Defects (Phế phẩm, lỗi, làm lại - Rework).\n"
            "• Lãng phí nguy hiểm nhất: OVERPRODUCTION (Sản xuất thừa).\n"
            "  - Lý do: Nó là 'Mẹ đẻ của mọi lãng phí khác'. Khi sản xuất thừa, nhà máy phải tốn kho chứa (Inventory), tốn xe nâng vận chuyển (Transportation), tốn bao bì đóng gói (Overprocessing), che giấu các khuyết tật chất lượng (Defects) cho đến tận nhiều tuần sau mới phát hiện ra, và làm chôn vùi dòng tiền doanh nghiệp."
        )
    },
    {
        "id": "q_waste_02",
        "category": "7 Lãng Phí (TIMWOOD) & 5S",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Lãng phí thứ 8 trong Lean (Waste of Unused Human Potential - Tài năng chưa được tận dụng) là gì? Bạn làm thế nào để xây dựng phong trào đóng góp ý tưởng cải tiến từ công nhân trực tiếp?",
        "key_points": (
            "• Định nghĩa lãng phí thứ 8:\n"
            "  - Không lắng nghe, không khai thác kiến thức, kinh nghiệm và sự sáng tạo của lực lượng lao động trực tiếp tại xưởng — những người hiểu rõ chiếc máy nhất.\n"
            "• Cơ chế khơi dậy ý tưởng cải tiến (Teian Kaizen):\n"
            "  1. Biểu mẫu Teian cực kỳ đơn giản: Tờ phiếu A5 chỉ gồm 3 ô: (1) Khó khăn hiện tại là gì? (2) Ý tưởng sửa đổi thế nào? (3) Lợi ích mang lại.\n"
            "  2. Quy tắc phản hồi nhanh trong 48 giờ: Bất kỳ đề xuất nào gửi lên đều phải được Quản đốc/Kỹ sư CI phản hồi duyệt hoặc giải thích lý do từ chối trong vòng 2 ngày làm việc.\n"
            "  3. Thưởng ngay bằng tiền mặt nhỏ (Instant Reward): Khen thưởng ngay 50.000đ - 100.000đ cho mỗi ý tưởng được chấp nhận thực hiện, vinh danh trên bảng tin nhà máy hàng tuần.\n"
            "  4. Trao quyền thực hiện (Empowerment): Khuyến khích công nhân cùng tham gia tự tay chế tạo các cữ gá cải tiến đơn giản."
        )
    },
    {
        "id": "q_waste_03",
        "category": "7 Lãng Phí (TIMWOOD) & 5S",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Sự khác biệt giữa Sơ đồ Hiện trạng (Current State Map) và Sơ đồ Tương lai (Future State Map) trong Bản đồ Chuỗi Giá trị (Value Stream Mapping - VSM)? Chỉ số mấu chốt trên thanh thời gian (Timeline) là gì?",
        "key_points": (
            "• Khác biệt bản chất:\n"
            "  - Current State Map: Chụp lại bức tranh thực tế trần trụi của dòng thông tin và dòng vật tư hiện tại, phơi bày toàn bộ đống phế phẩm, kho đệm tắc nghẽn, thời gian chờ đợi.\n"
            "  - Future State Map: Bức tranh thiết kế chuỗi giá trị tinh gọn sau khi đã áp dụng Takt time, luồng 1 sản phẩm liên tục (Continuous Flow), siêu thị kéo Kanban và lịch sản xuất Heijunka san phẳng.\n"
            "• Chỉ số mấu chốt trên Timeline:\n"
            "  - Dòng dưới: Thời gian gia công tạo giá trị (Processing Time / Value-Added Time, thường chỉ tính bằng giây hoặc phút, ví dụ: 240 giây).\n"
            "  - Dòng trên: Tổng thời gian sản xuất Lead Time (bao gồm thời gian phôi nằm chờ trong kho, thường tính bằng ngày hoặc tuần, ví dụ: 18 ngày).\n"
            "  - Tỷ lệ Hiệu quả Chuỗi giá trị: PCE (Process Cycle Efficiency) = Total VA Time / Total Lead Time. Ở các xưởng truyền thống, tỷ lệ này thường dưới 5%!"
        )
    },
    {
        "id": "q_waste_04",
        "category": "7 Lãng Phí (TIMWOOD) & 5S",
        "type": "Phân Tích Sâu",
        "question": "Phân biệt 5S chuẩn mực của Nhật Bản với 'Dọn dẹp vệ sinh thông thường'. Làm thế nào để chuyển đổi từ bước Seiso (Sạch sẽ) sang triết lý 'Làm sạch là Kiểm tra' (Cleaning is Inspection)?",
        "key_points": (
            "• 5S không phải là cầm chổi quét nhà trước giờ thanh tra:\n"
            "  - Dọn vệ sinh thông thường chỉ làm bề mặt trông có vẻ sạch sẽ.\n"
            "  - 5S là một hệ thống quản trị trực quan (Visual Management) nhằm loại bỏ dị vật, chuẩn hóa trật tự và lập tức phát hiện sự cố bất thường (Abnormality) khi mới chớm phát sinh.\n"
            "• Triết lý 'Làm sạch là Kiểm tra' (Cleaning is Inspection):\n"
            "  1. Khi công nhân dùng giẻ lau chùi từng ngóc ngách của thân máy, mắt họ quan sát và tay họ cảm nhận được: tiếng kêu lạ, độ rung bất thường, đai ốc bị rơ lỏng, dầu nhớt bắt đầu rò rỉ qua phớt chắn bụi.\n"
            "  2. Thiết lập thẻ FUGUAI (Thẻ đỏ bất thường): Bất kỳ điểm hở, rò rỉ hay mối nguy nào phát hiện được khi lau chùi đều được dán thẻ đánh số để bảo trì xử lý trước khi máy đổ bệnh dừng ca.\n"
            "  3. Triệt tiêu nguồn gây bẩn (Source of contamination): Thay vì ngày nào cũng lau dầu tràn, hãy làm máng hứng dầu hoặc thay gioăng mới."
        )
    },
    {
        "id": "q_waste_05",
        "category": "7 Lãng Phí (TIMWOOD) & 5S",
        "type": "Tình Huống Thực Chiến",
        "question": "Khi ban lãnh đạo công bố triển khai Lean Manufacturing, công nhân và tổ trưởng rỉ tai nhau phản đối vì sợ rằng Lean sẽ 'Tối ưu định biên, vắt kiệt sức lao động và sa thải người thừa'. Bạn sẽ truyền thông và giải tỏa nỗi sợ hãi này như thế nào?",
        "key_points": (
            "• Chiến lược truyền thông minh bạch & đồng cảm:\n"
            "  1. Cam kết không sa thải vì Lean (No-Layoff Policy due to Lean): Cần ban lãnh đạo cam kết rõ ràng bằng văn bản: Mục tiêu của Lean là loại bỏ thao tác mệt nhọc, nguy hiểm và lãng phí vô ích, KHÔNG PHẢI để đuổi người. Nhân sự dôi dư do cải tiến sẽ được điều phối sang mở rộng dây chuyền mới hoặc đào tạo nâng cao.\n"
            "  2. Thay đổi cách tiếp cận: Bắt đầu dự án Kaizen từ việc cải thiện điều kiện làm việc của chính họ (ví dụ: làm bàn nâng phôi để công nhân không phải cúi gập lưng vác nặng 20kg, lắp quạt thông gió làm mát).\n"
            "  3. Thu hút sự tham gia từ đầu: Để chính người công nhân trực tiếp vẽ lại thao tác của họ và tự đề xuất phương án. Khi họ thấy công việc trở nên nhẹ nhàng, an toàn hơn mà lương thưởng vẫn giữ nguyên, họ sẽ trở thành đại sứ Lean tích cực nhất."
        )
    },
    {
        "id": "q_waste_06",
        "category": "7 Lãng Phí (TIMWOOD) & 5S",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Phân biệt Kaizen (Cải tiến nhỏ liên tục), Kaikaku (Cải cách đổi mới đột phá) và Kakushin (Đổi mới tái cấu trúc) trong chiến lược sản xuất?",
        "key_points": (
            "• 3 cấp độ chuyển đổi sản xuất:\n"
            "  - Kaizen (Cải tiến liên tục): Bước đi nhỏ, chi phí thấp hoặc bằng 0, do toàn bộ nhân viên tham gia thực hiện mỗi ngày (ví dụ: làm khay để dụng cụ 5S, đổi vị trí công tắc).\n"
            "  - Kaikaku (Cải cách triệt để): Dự án đột phá quy mô lớn, tái cấu trúc toàn diện một phân xưởng hoặc một dây chuyền trong thời gian ngắn (ví dụ: đập bỏ bố trí layout cũ để chuyển sang chuyền chữ U, giảm 50% diện tích xưởng trong 1 tuần Kaizen Blitz).\n"
            "  - Kakushin (Đổi mới cách mạng): Thay đổi toàn bộ công nghệ cốt lõi hoặc mô hình sản phẩm (ví dụ: chuyển từ gia công cơ khí truyền thống sang in 3D kim loại, chuyển đổi số toàn diện tự động hóa bằng robot AGV).\n"
            "• Nguyên tắc kết hợp: Kaikaku tạo ra một bước nhảy vọt về nền tảng, sau đó Kaizen liên tục bảo vệ thành quả và tối ưu hóa hàng ngày."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 6: POKA-YOKE & CƠ CHẾ CHỐNG LỖI (MISTAKE PROOFING)
    # =========================================================================
    {
        "id": "q_poka_01",
        "category": "Poka-Yoke & Chống Lỗi",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Khái niệm Poka-Yoke là gì? Phân biệt giữa 2 cấp độ: Poka-Yoke cảnh báo (Warning) và Poka-Yoke kiểm soát/ngắt mạch (Control)? Cho ví dụ thực tế mỗi loại?",
        "key_points": (
            "• Định nghĩa Poka-Yoke (Mistake-proofing):\n"
            "  - Cơ chế thiết kế thông minh nhằm ngăn ngừa con người phạm sai lầm (Fail-safe), hoặc nếu lỡ có thao tác sai thì hệ thống tự động phát hiện ngay lập tức trước khi trở thành phế phẩm.\n"
            "• 2 cấp độ Poka-Yoke:\n"
            "  1. Poka-Yoke Cảnh báo (Warning Poka-Yoke): Phát tín hiệu âm thanh (còi réo) hoặc ánh sáng (đèn nhấp nháy) để báo hiệu thao tác sai, nhưng máy VẪN CÓ THỂ CHẠY TIẾP nếu người dùng phớt lờ.\n"
            "     - Ví dụ: Còi báo khi quên thắt dây an toàn trên xe ô tô, hoặc đèn đỏ nhấp nháy khi công nhân nhặt sai mã linh kiện từ giá kệ.\n"
            "  2. Poka-Yoke Kiểm soát / Ngắt mạch (Control Poka-Yoke - Cấp độ cao hơn):\n"
            "     - Cơ cấu vật lý hoặc liên động điện tử NGĂN CHẶN TUYỆT ĐỐI không cho máy hoạt động hoặc không cho phôi đi tiếp nếu thao tác sai.\n"
            "     - Ví dụ: Cổng cắm thẻ SIM điện thoại có một góc vát chéo, nếu gắn ngược chiều thì không thể nào nhét khay SIM vào được; máy dập chỉ kích hoạt khi cả 2 tay cùng nhấn 2 nút đồng thời (Two-hand safety control)."
        )
    },
    {
        "id": "q_poka_02",
        "category": "Poka-Yoke & Chống Lỗi",
        "type": "Phân Tích Sâu",
        "question": "So sánh chi phí và hiệu quả giữa 'Kiểm tra cuối chuyền' (Final QC), 'Kiểm tra chất lượng tại trạm' (In-line QC) và 'Poka-Yoke tại nguồn' (Source Inspection)?",
        "key_points": (
            "• Quy luật chi phí lỗi 1-10-100 (Rule of Ten):\n"
            "  1. Poka-Yoke tại nguồn (Source Inspection - Chi phí 1 USD):\n"
            "     - Lỗi được ngăn chặn ngay trước khi xảy ra thao tác sai (ví dụ chốt định vị không cho lắp ngược). Chi phí khắc phục rẻ nhất, phế phẩm bằng 0, không tốn thời gian kiểm tra lại.\n"
            "  2. Kiểm tra tại trạm (In-line QC - Chi phí 10 USD):\n"
            "     - Sản phẩm vừa làm xong được test ngay tại trạm tiếp theo. Nếu lỗi, phát hiện sau 1 chu kỳ, chỉ hỏng 1 chi tiết và dừng chuyền cảnh báo ngay.\n"
            "  3. Kiểm tra cuối chuyền (Final Inspection - Chi phí 100 USD):\n"
            "     - Sai lầm phổ biến nhất! QC cuối chuyền chỉ có chức năng lọc rác chứ không sinh ra chất lượng. Khi QC cuối chuyền phát hiện lỗi thì hàng trăm linh kiện trước đó đã bị làm hỏng, tiêu tốn vật tư, nhân công tháo dỡ sửa lại (Rework), và nguy cơ cao lọt phế phẩm tới tay khách hàng."
        )
    },
    {
        "id": "q_poka_03",
        "category": "Poka-Yoke & Chống Lỗi",
        "type": "Tình Huống Thực Chiến",
        "question": "Tình huống: Công nhân thường xuyên lắp ngược chiều gioăng cao su O-ring trong cụm van thủy lực, dẫn đến rò rỉ dầu khi test xuất xưởng. Hãy thiết kế 3 giải pháp Poka-Yoke từ mức chi phí thấp nhất đến tự động hóa?",
        "key_points": (
            "• 3 phương án thiết kế Poka-Yoke theo thang chi phí:\n"
            "  1. Giải pháp Mức 1 (Chi phí gần như bằng 0 - Màu sắc & Hình ảnh trực quan):\n"
            "     - Yêu cầu nhà cung ứng gioăng dập một dải màu dạ quang (hoặc viền xanh) ở mặt trên của gioăng. Tại bàn làm việc dán ảnh mẫu trực quan 1:1, nếu lắp đúng thì viền xanh ngửa lên trên.\n"
            "  2. Giải pháp Mức 2 (Chi phí thấp - Đồ gá định hình cơ khí Asymmetric Fixture):\n"
            "     - Cải tiến rãnh lắp gioăng trên thân van có một gờ định vị nhỏ lệch tâm (Asymmetry Pin). Gioăng mới được thiết kế khuyết rãnh tương ứng, chỉ có thể ấn vào khi xoay đúng góc, nếu lắp ngược sẽ bị cấn vồng lên không đóng nắp được.\n"
            "  3. Giải pháp Mức 3 (Tự động hóa - Cảm biến quang học / Machine Vision):\n"
            "     - Trạm siết ốc tự động tích hợp Camera Vision AI chụp ảnh bề mặt van. Nếu gioăng bị thiếu hoặc lắp ngược chiều rãnh thoát dầu, hệ thống PLC khóa trục siết ốc, phát cảnh báo Andon không cho xả phôi sang công đoạn sau."
        )
    },
    {
        "id": "q_poka_04",
        "category": "Poka-Yoke & Chống Lỗi",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Mối liên hệ tương hỗ giữa Jidoka (Tự động hóa có trí tuệ con người), Hệ thống Andon và Poka-Yoke trong triết lý sản xuất Toyota (TPS)?",
        "key_points": (
            "• Tam giác chất lượng TPS:\n"
            "  1. Poka-Yoke: Là 'vũ khí kỹ thuật' (cảm biến, cữ gá, công tắc giới hạn) phát hiện tức thì sự bất thường hoặc ngăn lỗi cơ học.\n"
            "  2. Jidoka (Tự động hóa thông minh): Là 'nguyên tắc vận hành'. Khi Poka-Yoke phát hiện bất thường, máy móc hoặc con người lập tức DỪNG DÂY CHUYỀN NGAY LẬP TỨC để không truyền chi tiết lỗi sang khâu sau.\n"
            "  3. Andon: Là 'kênh truyền thông trực quan'. Khi dừng dây chuyền, hệ thống đèn tháp và âm thanh chuông Andon được kích hoạt báo hiệu chính xác trạm nào đang gặp sự cố để kỹ sư cải tiến và bảo trì chạy tới hỗ trợ giải quyết nguyên nhân gốc rễ trong vòng 3 phút."
        )
    },
    {
        "id": "q_poka_05",
        "category": "Poka-Yoke & Chống Lỗi",
        "type": "Tình Huống Thực Chiến",
        "question": "Sau khi bạn gắn cảm biến quang Poka-Yoke để kiểm tra công nhân đã bắt đủ 4 bu-lông, công nhân đã lấy băng keo dán che mắt cảm biến để máy chạy cho nhanh mà không cần bắt ốc. Bạn xử lý hành vi vô hiệu hóa này như thế nào?",
        "key_points": (
            "• Phân tích hành vi & tư duy giải quyết:\n"
            "  - Nếu công nhân tìm cách bypass Poka-Yoke, nguyên nhân 90% là do thiết kế cơ cấu Poka-Yoke quá rườm rà, làm tăng chu kỳ thao tác khiến họ không kịp sản lượng, hoặc quy trình kiểm tra gây ức chế.\n"
            "• Giải pháp đồng bộ:\n"
            "  1. Cải tiến kỹ thuật chống can thiệp (Anti-tamper Design):\n"
            "     - Thay cảm biến che quang thông thường bằng cảm biến áp lực hoặc tô vít điện thông minh (Smart Electric Screwdriver) có bộ đếm xung lực siết (Torque & Angle Control). Chỉ khi súng bắn đủ 4 lần đạt mô-men xoắn chuẩn 3.5 N.m thì PLC mới tự động nhả chốt khóa phôi.\n"
            "     - Lập trình PLC kiểm tra trạng thái chuyển đổi logic: Cảm biến phải có chu kỳ BẬT -> TẮT -> BẬT cho mỗi phôi. Nếu cảm biến luôn BẬT liên tục quá 30 giây (do bị dán băng dính), PLC báo lỗi Tamper Error và khóa máy.\n"
            "  2. Đối thoại và tái cân bằng tải công việc cho công nhân để họ không bị áp lực thời gian dẫn đến hành vi gian lận."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 7: ĐỊNH MỨC BOM & HAO PHÍ VẬT TƯ (BOM & SCRAP CONTROL)
    # =========================================================================
    {
        "id": "q_bom_01",
        "category": "Định Mức BOM & Hao Phí",
        "type": "Khái Niệm Cốt Lõi",
        "question": "BOM (Bill of Materials) là gì? Phân biệt sự khác nhau giữa Engineering BOM (EBOM), Manufacturing BOM (MBOM) và Sales BOM (SBOM)?",
        "key_points": (
            "• Định nghĩa BOM:\n"
            "  - Cây danh mục định mức toàn diện liệt kê tất cả nguyên vật liệu thô, chi tiết, cụm lắp ráp, bao bì và số lượng chính xác cần thiết để sản xuất 1 đơn vị sản phẩm hoàn chỉnh.\n"
            "• Phân biệt 3 loại BOM:\n"
            "  1. EBOM (Engineering BOM - Bản vẽ thiết kế R&D):\n"
            "     - Do phòng thiết kế/R&D tạo ra từ phần mềm CAD. Phản ánh chức năng cấu tạo của sản phẩm theo dạng mô hình hình học, chưa tính đến các yếu tố đóng gói hay quy trình xưởng.\n"
            "  2. MBOM (Manufacturing BOM - Định mức sản xuất thực tế):\n"
            "     - Do phòng Kỹ thuật công nghệ (PE/IE) lập ra phục vụ sản xuất. Bổ sung các vật tư phụ trợ không có trên bản vẽ (như dầu bôi trơn, keo dán, dung môi làm sạch, màng co bao bì) và phản ánh đúng thứ tự quy trình lắp ráp từng công đoạn, có tính tỷ lệ hao hụt định mức (Yield Scrap Factor).\n"
            "  3. SBOM (Sales BOM - Định mức bán hàng):\n"
            "     - Cấu hình sản phẩm bán cho khách hàng (ví dụ: máy tính đóng gói kèm sạc, dây cáp, sách hướng dẫn, thùng carton)."
        )
    },
    {
        "id": "q_bom_02",
        "category": "Định Mức BOM & Hao Phí",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Tỷ lệ hao hụt định mức (Scrap Rate / Yield Loss) được cấu thành từ những yếu tố nào? Làm thế nào để phân biệt giữa 'Hao phí công nghệ tự nhiên' và 'Hao phí bất thường do vận hành'?",
        "key_points": (
            "• Phân biệt 2 nhóm hao hụt vật tư:\n"
            "  1. Hao phí công nghệ tự nhiên (Inherent / Engineering Loss):\n"
            "     - Lượng vật tư bắt buộc phải mất đi do đặc thù phương pháp gia công kỹ thuật (ví dụ: mạt sắt khi tiện phay, phôi đầu thừa đuôi thọt khi cắt thanh nhôm định hình 6m thành các đoạn 450mm, cuống keo nhựa nằm trong kênh dẫn khuôn ép).\n"
            "     - Được đo đạc chính xác và tính sẵn vào định mức MBOM chuẩn.\n"
            "  2. Hao phí bất thường do vận hành (Operational / Abnormal Scrap):\n"
            "     - Phát sinh do con người hoặc máy móc sai hỏng: phôi bị trầy xước bề mặt, khoan sai vị trí, chỉnh máy phung phí vật tư test đầu ca, rơi vỡ linh kiện, ẩm mốc linh kiện trong kho.\n"
            "     - Là mục tiêu tối thượng mà Kỹ sư Cải tiến phải triệt tiêu qua biểu đồ Pareto nguyên nhân phế phẩm."
        )
    },
    {
        "id": "q_bom_03",
        "category": "Định Mức BOM & Hao Phí",
        "type": "Tình Huống Thực Chiến",
        "question": "Báo cáo tài chính cho thấy chi phí nguyên vật liệu thực tế vượt định mức BOM 4.2% trong tháng qua, làm bốc hơi hơn 300 triệu đồng lợi nhuận. Là Kỹ sư cải tiến, bạn tiến hành điều tra truy tìm nguyên nhân gốc rễ theo các bước nào?",
        "key_points": (
            "• Quy trình 5 bước điều tra chênh lệch BOM Variance:\n"
            "  1. Phân loại Pareto 80/20: Trích xuất dữ liệu từ phần mềm ERP (SAP/Oracle), lọc ra top 5 mã nguyên vật liệu có giá trị chênh lệch lớn nhất (thường là linh kiện đắt tiền như vi điều khiển, thép tấm cuộn, dây đồng mạ vàng).\n"
            "  2. Đối chiếu số liệu 3 điểm (Three-point Check): Kiểm tra chéo giữa (a) Số lượng mua vào từ hóa đơn kho, (b) Số lượng xuất kho ra chuyền, và (c) Số lượng thành phẩm hoàn thành nhân với định mức BOM.\n"
            "  3. Điều tra hiện trường Genba:\n"
            "     - Kiểm tra trạm Setup đầu ca: Công nhân có chỉnh cữ máy làm hỏng quá nhiều mẫu thử mà không ghi phiếu báo hủy (Scrap Ticket)?\n"
            "     - Kiểm tra kích thước phôi đầu vào: Nhà cung ứng có cấp thép mỏng/dày hơn dung sai danh định làm tăng trọng lượng dập?\n"
            "  4. Kiểm tra việc làm lại (Rework): Công nhân làm hỏng cụm linh kiện nhưng tự ý lấy linh kiện mới thay thế mà không hạch toán.\n"
            "  5. Cập nhật lại định mức BOM hoặc siết chặt kiểm soát xuất kho theo đúng lệnh sản xuất (Work Order Allocation)."
        )
    },
    {
        "id": "q_bom_04",
        "category": "Định Mức BOM & Hao Phí",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Phương pháp Kiểm kê luân phiên (Cycle Counting) kết hợp phân loại ABC giúp duy trì độ chính xác tồn kho BOM (Record Accuracy) trên 98% như thế nào so với kiểm kê cả năm một lần?",
        "key_points": (
            "• Hạn chế của kiểm kê truyền thống cuối năm (Annual Physical Inventory):\n"
            "  - Phải dừng nhà máy nhiều ngày, nhân lực mệt mỏi, phát hiện sai lệch lớn nhưng không thể tìm lại nguyên nhân vì đã xảy ra từ 8 tháng trước.\n"
            "• Chiến lược Cycle Counting theo phân loại ABC:\n"
            "  - Nhóm A (20% mã hàng chiếm 80% giá trị - vi mạch, động cơ, kim loại quý): Được kiểm đếm chu kỳ liên tục mỗi tuần một lần.\n"
            "  - Nhóm B (30% mã hàng chiếm 15% giá trị - khuôn gá, linh kiện phụ): Kiểm đếm mỗi tháng một lần.\n"
            "  - Nhóm C (50% mã hàng chiếm 5% giá trị - ốc vít, bu-lông, băng keo): Kiểm đếm mỗi quý một lần.\n"
            "• Lợi ích vượt trội:\n"
            "  - Không cần dừng xưởng, phát hiện sai sót số liệu ngay trong ngày để điều chỉnh BOM trên phần mềm ERP, đảm bảo độ chính xác dữ liệu luôn đạt ≥ 98%."
        )
    },
    {
        "id": "q_bom_05",
        "category": "Định Mức BOM & Hao Phí",
        "type": "Tình Huống Thực Chiến",
        "question": "Kỹ thuật 'Kitting' (Soạn linh kiện theo bộ) và 'Kanban hai thùng' (Two-bin Kanban) giúp ngăn chặn tình trạng thất thoát và nhầm lẫn vật tư trên chuyền lắp ráp như thế nào?",
        "key_points": (
            "• Cơ chế Kitting (Soạn cụm theo bộ):\n"
            "  - Thay vì để các bao tải ốc vít hoặc thùng linh kiện ngổn ngang cạnh dây chuyền, kho chuẩn bị trước một khay kitting chứa đúng số lượng chi tiết cho 1 sản phẩm (hoặc 1 lệnh sản xuất 10 chiếc).\n"
            "  - Nếu sau khi lắp xong mà trên khay còn thừa 1 chiếc ốc vít, công nhân lập tức biết mình đã quên siết ốc (Chức năng tự kiểm tra Poka-Yoke).\n"
            "• Cơ chế Two-bin Kanban (Kanban 2 thùng cho vật tư tiêu hao):\n"
            "  - Thùng 1 đặt trên giá thao tác để công nhân sử dụng. Thùng 2 đặt dự phòng phía sau.\n"
            "  - Khi thùng 1 cạn, công nhân dời thùng 2 lên dùng và chuyển thùng rỗng 1 về khay hoàn trả. Nhân viên Water Spider nhìn thấy thùng rỗng sẽ mang vào kho cấp đầy lại theo đúng số lượng định mức, ngăn ngừa việc tích trữ vật tư riêng lẻ tại xưởng."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 8: SPC, NĂNG LỰC QUY TRÌNH & MINITAB (Cp / Cpk)
    # =========================================================================
    {
        "id": "q_spc_01",
        "category": "SPC, Minitab & Cp/Cpk",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Chỉ số Cp và Cpk khác nhau ở điểm nào? Trong trường hợp Cp = 1.68 nhưng Cpk = 0.82, điều đó phản ánh thực trạng gì của máy móc gia công và bạn phải hành động ra sao?",
        "key_points": (
            "• Bản chất công thức:\n"
            "  - Cp = (USL - LSL) / (6 × Sigma): Phản ánh độ biến động (độ phân tán bề rộng) của quy trình, không quan tâm vị trí trung bình có bị lệch tâm hay không.\n"
            "  - Cpk = min( (USL - Trung bình) / 3Sigma , (Trung bình - LSL) / 3Sigma ): Phản ánh năng lực thực tế có tính đến độ lệch tâm so với dung sai thiết kế.\n"
            "• Phân tích trường hợp Cp = 1.68 và Cpk = 0.82:\n"
            "  - Cp = 1.68 (> 1.33): Máy móc gia công có độ ổn định và độ lặp lại rất cao, dao động bề rộng cực hẹp (tiềm năng World-Class).\n"
            "  - Nhưng Cpk = 0.82 (< 1.0): Quy trình đang sinh ra phế phẩm vì giá trị trung bình bị LỆCH TÂM nghiêm trọng về một phía dung sai (tiệm cận sát vách USL hoặc LSL)!\n"
            "• Hành động cần làm ngay:\n"
            "  - Không cần thay máy mới hay sửa chữa lớn. Chỉ cần điều chỉnh bù trừ gốc tọa độ (Offset / Zero adjustment) trên bộ điều khiển CNC hoặc chỉnh cữ gá để kéo giá trị trung bình về lại đúng tâm danh định."
        )
    },
    {
        "id": "q_spc_02",
        "category": "SPC, Minitab & Cp/Cpk",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Sự khác biệt giữa Cpk (Năng lực tiềm năng - Within Subgroup) và Ppk (Hiệu suất tổng thể - Overall Variation)? Khi nào khách hàng ô tô (chuẩn IATF 16949) bắt buộc chứng nhận Ppk ≥ 1.67?",
        "key_points": (
            "• Phân biệt Cpk vs Ppk:\n"
            "  - Cpk dùng độ lệch chuẩn nội bộ nhóm (Within Sigma - s-bar / d2), loại bỏ các biến động dài hạn giữa các lô. Phản ánh máy móc có thể làm tốt đến mức nào trong điều kiện lý tưởng ngắn hạn.\n"
            "  - Ppk dùng độ lệch chuẩn tổng thể (Overall Sample Standard Deviation - s), tính toán trên toàn bộ dữ liệu lịch sử gộp chung cả biến động nhiệt độ, thay đổi ca làm việc, các lô nguyên liệu khác nhau.\n"
            "• Khi nào khách hàng ô tô yêu cầu Ppk ≥ 1.67:\n"
            "  - Trong giai đoạn phê duyệt sản xuất hàng loạt PPAP (Production Part Approval Process), nhà máy phải chạy thử lô sản xuất ban đầu (Initial Production Run từ 300 sản phẩm liên tục).\n"
            "  - Vì quy trình mới chưa có đủ dữ liệu ổn định dài hạn nên khách hàng đòi hỏi Ppk khắt khe (thường là ≥ 1.67, tương đương 0.6 PPM phế phẩm) để đảm bảo độ tin cậy tuyệt đối."
        )
    },
    {
        "id": "q_spc_03",
        "category": "SPC, Minitab & Cp/Cpk",
        "type": "Phân Tích Sâu",
        "question": "Các quy tắc phát hiện tín hiệu bất thường trên biểu đồ kiểm soát Xbar-R theo chuẩn Western Electric / Nelson Rules (ví dụ: 1 điểm vượt 3-Sigma, 9 điểm liên tiếp lệch về 1 phía)?",
        "key_points": (
            "• Các quy tắc cảnh báo sớm nguyên nhân đặc biệt (Special Causes):\n"
            "  1. Rule 1: Có 1 điểm duy nhất vượt ra ngoài giới hạn kiểm soát trên UCL hoặc dưới LCL (Vùng ngoài 3-Sigma). → Biến động đột biến cực đoan (gãy mũi dao, công nhân nhầm phôi).\n"
            "  2. Rule 2: Có 9 điểm liên tiếp cùng nằm về một phía của đường tâm trung bình (Center Line). → Quy trình đã bị dịch chuyển tâm (Tool wear - dao mòn dần, nhiệt độ máy tăng dần).\n"
            "  3. Rule 3: Có 6 điểm liên tiếp tăng dần đều hoặc giảm dần đều. → Xu hướng trôi dạt (Drift trend).\n"
            "  4. Rule 4: Có 14 điểm liên tiếp dao động lên xuống xen kẽ (hình răng cưa). → Hiện tượng lấy mẫu từ 2 nguồn máy khác nhau hoặc 2 công nhân khác nhau gộp chung.\n"
            "• Hành động: Khi vi phạm bất kỳ quy tắc nào, kỹ thuật viên phải dừng chuyền kiểm tra ngay, không chờ phế phẩm phát sinh mới xử lý."
        )
    },
    {
        "id": "q_spc_04",
        "category": "SPC, Minitab & Cp/Cpk",
        "type": "Tình Huống Thực Chiến",
        "question": "Phân tích hệ thống đo lường (Gage R&R - MSA): Tỷ lệ %GRR bao nhiêu là đạt yêu cầu? Nếu kết quả phân tích cho thấy %GRR = 36% do thành phần Reproducibility quá cao, nguyên nhân cốt lõi từ đâu?",
        "key_points": (
            "• Tiêu chuẩn đánh giá %GRR (Gage Repeatability & Reproducibility):\n"
            "  - Dưới 10%: Hệ thống đo lường tuyệt vời (Acceptable).\n"
            "  - 10% đến 30%: Có thể chấp nhận tùy theo mức độ quan trọng của đặc tính sản phẩm và chi phí thiết bị.\n"
            "  - Trên 30%: KHÔNG ĐẠT (Unacceptable). Kết quả đo không đáng tin cậy, dữ liệu đo bị nhiễu do chính dụng cụ hoặc người đo.\n"
            "• Phân tích khi Reproducibility (Độ tái lập) quá cao:\n"
            "  - Repeatability (Độ lặp lại) cao: Lỗi do bản thân thiết bị đo (thước kẹp bị mòn lỏng cơ khí).\n"
            "  - Reproducibility cao: Lỗi do SỰ KHÁC BIỆT GIỮA CÁC NGƯỜI ĐO (Appraiser Variation)!\n"
            "• Nguyên nhân gốc rễ & Khắc phục:\n"
            "  - Mỗi công nhân cầm thước theo một góc nghiêng khác nhau, hoặc lực bóp ngàm kẹp khác nhau (người siết mạnh tay, người đo lỏng tay).\n"
            "  - Khắc phục: Đào tạo lại thao tác đo chuẩn, chuyển sang dùng panme có bánh cóc trợ lực (Ratchet stop) hoặc đồ gá cố định vị trí đo."
        )
    },
    {
        "id": "q_spc_05",
        "category": "SPC, Minitab & Cp/Cpk",
        "type": "Phân Tích Sâu",
        "question": "Khi kiểm tra dữ liệu kích thước trong Minitab phát hiện dữ liệu không tuân theo phân phối chuẩn (Non-normal Distribution, P-value < 0.05 trong bài test Anderson-Darling), bạn xử lý như thế nào trước khi tính toán năng lực quy trình?",
        "key_points": (
            "• Sai lầm cần tránh:\n"
            "  - Nếu dữ liệu không chuẩn mà vẫn dùng công thức thông thường để tính Cpk, kết quả sẽ bị sai lệch hoàn toàn và cho ra tỷ lệ lỗi ảo.\n"
            "• Quy trình xử lý dữ liệu phi chuẩn trong Minitab:\n"
            "  1. Kiểm tra bản chất vật lý của thông số: Một số thông số vốn dĩ phi chuẩn tự nhiên (ví dụ: độ nhám bề mặt, độ đảo tròn, độ phẳng, thời gian chờ... luôn có ranh giới tự nhiên là số dương ≥ 0).\n"
            "  2. Áp dụng phép biến đổi Box-Cox (Box-Cox Transformation) hoặc biến đổi Johnson (Johnson Transformation) trong Minitab để đưa dữ liệu về dạng tiệm cận chuẩn.\n"
            "  3. Nếu không thể biến đổi, sử dụng phương pháp phân tích phi chuẩn theo các hàm phân phối phù hợp: Weibull, Lognormal, Gamma trong menu 'Capability Analysis (Nonnormal)'.\n"
            "  4. Báo cáo chỉ số Ppk tương ứng từ phân phối phi chuẩn để đảm bảo tính khách quan."
        )
    },
    {
        "id": "q_spc_06",
        "category": "SPC, Minitab & Cp/Cpk",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Phân biệt 'Sai số ngẫu nhiên' (Common Cause) và 'Sai số đặc biệt' (Special Cause). Sai lầm nghiêm trọng nhất của người kỹ sư khi can thiệp vào quy trình đang có sai số ngẫu nhiên là gì (Quy luật Phễu Deming - Funnel Experiment)?",
        "key_points": (
            "• Khác biệt bản chất:\n"
            "  - Common Cause (Nguyên nhân thông thường): Biến động vốn có của hệ thống do tiếng ồn rung nhẹ, chênh lệch nhiệt độ môi trường tự nhiên. Ổn định và có thể dự báo được.\n"
            "  - Special Cause (Nguyên nhân đặc biệt): Sự cố bất ngờ ngoài dự kiến như gãy mũi khoan, đổi nhầm cuộn phôi sai mã, công nhân chưa qua đào tạo.\n"
            "• Sai lầm 'Can thiệp thái quá' (Tampering / Funnel Experiment):\n"
            "  - Khi quy trình đang kiểm soát ổn định (chỉ có sai số ngẫu nhiên), nhưng người kỹ sư cứ thấy một mẫu đo hơi lệch về bên phải là lập tức vặn ốc chỉnh máy sang bên trái. Sau đó mẫu tiếp theo rơi sang trái lại vặn chỉnh sang phải.\n"
            "  - Kết quả: Theo Thí nghiệm chiếc phễu của TS. Deming, hành động can thiệp thái quá này làm TĂNG GẤP ĐÔI BIẾN ĐỘNG của hệ thống và biến một quy trình đang ổn định thành một đống phế phẩm hỗn loạn!"
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 9: BỐ TRÍ MẶT BẰNG (PLANT LAYOUT) & LUỒNG 1 SẢN PHẨM
    # =========================================================================
    {
        "id": "q_layout_01",
        "category": "Bố Trí Mặt Bằng & Luồng 1 Sản Phẩm",
        "type": "Khái Niệm Cốt Lõi",
        "question": "So sánh 3 mô hình bố trí mặt bằng sản xuất: Bố trí theo công nghệ (Process/Functional Layout), Bố trí theo sản phẩm (Cellular/Product Layout) và Bố trí vị trí cố định (Fixed-Position)?",
        "key_points": (
            "• So sánh 3 dạng mặt bằng:\n"
            "  1. Process / Functional Layout (Bố trí theo công nghệ):\n"
            "     - Gom các máy cùng loại vào một khu: Phân xưởng tiện, phân xưởng phay, phân xưởng sơn. Thích hợp cho đơn hàng lẻ, đa dạng chủng loại nhưng nhược điểm là tồn kho WIP cực lớn, quãng đường di chuyển phôi lòng vòng hàng km.\n"
            "  2. Cellular / Product Layout (Bố trí theo nhóm sản phẩm / Chuyền tế bào):\n"
            "     - Bố trí các máy móc khác loại theo đúng trình tự lắp ráp sản phẩm (Tiện -> Phay -> Rửa -> Kiểm tra). Tối ưu hóa dòng chảy, giảm Lead time 80%, tồn kho WIP tối thiểu.\n"
            "  3. Fixed-Position Layout (Bố trí cố định):\n"
            "     - Sản phẩm nằm cố định tại một chỗ vì quá to nặng (đóng tàu thủy, lắp ráp máy bay), máy móc và con người di chuyển quanh sản phẩm."
        )
    },
    {
        "id": "q_layout_02",
        "category": "Bố Trí Mặt Bằng & Luồng 1 Sản Phẩm",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Tại sao bố trí chuyền hình chữ U (U-shaped Cell) lại được coi là chuẩn mực tối ưu nhất cho sản xuất Lean so với bố trí đường thẳng (I-line)?",
        "key_points": (
            "• Ưu điểm vượt trội của chuyền chữ U:\n"
            "  1. Điểm đầu (Nhận phôi) và Điểm cuối (Xuất thành phẩm) nằm sát cạnh nhau: Một công nhân có thể vừa nạp phôi vừa lấy thành phẩm đóng gói, dễ dàng kiểm soát nhịp Takt Time.\n"
            "  2. Linh hoạt điều chỉnh số lượng lao động (Shojinka): Khi đơn hàng giảm, 1 công nhân đa năng có thể đứng ở đáy chữ U để bao quát thao tác cả 2 nhánh chuyền đối diện nhau mà chỉ cần quay người 180 độ, không tốn bước chân đi bộ.\n"
            "  3. Giao tiếp trực quan (Visual Communication): Các công nhân nhìn thấy nhau trong lòng chữ U, dễ dàng tương trợ khi đồng nghiệp bị nghẽn việc (hỗ trợ Andon).\n"
            "  4. Tiết kiệm diện tích mặt bằng xưởng lên tới 25-35% so với chuyền thẳng dài."
        )
    },
    {
        "id": "q_layout_03",
        "category": "Bố Trí Mặt Bằng & Luồng 1 Sản Phẩm",
        "type": "Phân Tích Sâu",
        "question": "Khái niệm 'Luồng một sản phẩm' (One-Piece Flow): Các điều kiện tiên quyết bắt buộc phải đạt được trước khi nhà máy có thể vận hành trơn tru luồng 1 sản phẩm mà không bị tắc nghẽn?",
        "key_points": (
            "• Định nghĩa One-Piece Flow:\n"
            "  - Phương thức sản xuất trong đó mỗi chi tiết sau khi làm xong lập tức được chuyển ngay sang công đoạn kế tiếp, không tích tụ thành lô (Batch size = 1).\n"
            "• Các điều kiện tiên quyết bắt buộc:\n"
            "  1. Thời gian chuyển đổi mã hàng cực ngắn (SMED < 10 phút): Nếu mỗi lần đổi mã mất 1 tiếng thì không thể nào chạy lô 1 sản phẩm.\n"
            "  2. Độ tin cậy máy móc tuyệt đối (TPM cao, độ khả dụng A > 95%): Vì không có kho đệm WIP, một máy hỏng sẽ làm cả dây chuyền dừng ngay lập tức.\n"
            "  3. Chất lượng tại nguồn hoàn hảo (Poka-Yoke & Zero Defect): Không được phép có lỗi vì lỗi sẽ làm đứt xích dòng chảy.\n"
            "  4. Thao tác công nhân được chuẩn hóa (Standardized Work): Chu kỳ thời gian giữa các trạm phải cực kỳ đồng đều tiệm cận Takt Time."
        )
    },
    {
        "id": "q_layout_04",
        "category": "Bố Trí Mặt Bằng & Luồng 1 Sản Phẩm",
        "type": "Tình Huống Thực Chiến",
        "question": "Lưu đồ Spaghetti (Spaghetti Diagram) là gì? Quy trình thu thập dữ liệu quãng đường di chuyển của công nhân/vật tư và cách bạn rút ngắn 40-60% quãng đường thừa?",
        "key_points": (
            "• Khái niệm & Quy trình vẽ Spaghetti Diagram:\n"
            "  1. In bản vẽ mặt bằng nhà xưởng tỷ lệ thực lên giấy A3.\n"
            "  2. Cầm bảng kẹp đi theo sau công nhân trong 1 ca làm việc trọn vẹn, dùng bút vẽ lại từng bước chân họ di chuyển: đi lấy ốc vít, đi mượn cờ lê, đi sang kho phôi, đi vứt rác.\n"
            "  3. Bức vẽ thu được thường chằng chịt, rối ren như một đĩa mì Ý (Spaghetti), phơi bày việc công nhân phải đi bộ từ 4 đến 8 km mỗi ca!\n"
            "• Giải pháp rút ngắn quãng đường:\n"
            "  - Dời các giá kệ chứa linh kiện phụ về đặt ngay dưới gầm bàn thao tác trong bán kính 0.5 mét.\n"
            "  - Bố trí máng trượt trọng lực (Gravity chute) chuyển chi tiết tự động giữa 2 trạm.\n"
            "  - Thay đổi vị trí máy móc từ phân tán sang liên hoàn, cắt giảm ngay 50% quãng đường đi bộ vô ích."
        )
    },
    {
        "id": "q_layout_05",
        "category": "Bố Trí Mặt Bằng & Luồng 1 Sản Phẩm",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Ứng dụng nguyên lý Nhân trắc học (Ergonomics) trong thiết kế trạm làm việc: Vùng thao tác vàng (Golden Zone), độ cao mặt bàn chuẩn và tác động của nó tới năng suất lao động?",
        "key_points": (
            "• Nguyên tắc Ergonomics cốt lõi:\n"
            "  1. Vùng thao tác vàng (Golden Zone): Khu vực nằm trong khoảng từ ngang thắt lưng đến giữa ngực, cẳng tay gập 90 độ, bán kính với tay không quá 40cm. Toàn bộ linh kiện và công cụ thao tác thường xuyên (tần suất > 10 lần/giờ) PHẢI nằm trọn trong vùng này để công nhân không phải kiễng chân hoặc cúi gập lưng.\n"
            "  2. Độ cao mặt bàn chuẩn:\n"
            "     - Công việc lắp ráp chính xác: Mặt bàn cao hơn khuỷu tay 5-10cm để có điểm tựa cẳng tay.\n"
            "     - Công việc lắp ráp nhẹ: Mặt bàn thấp hơn khuỷu tay 5-10cm.\n"
            "     - Công việc dùng lực nặng: Mặt bàn thấp hơn khuỷu tay 15-20cm để tận dụng trọng lượng thân trên.\n"
            "• Lợi ích: Triệt tiêu các chứng đau cơ xương khớp nghề nghiệp (MSDs), giảm tỷ lệ nghỉ ốm, nâng năng suất thao tác lên 15%."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 10: ERP/MES, DỮ LIỆU SẢN XUẤT & XỬ LÝ SỰ CỐ GENBA
    # =========================================================================
    {
        "id": "q_it_01",
        "category": "ERP/MES & Quản Lý Genba",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Hệ thống Quản lý Thực thi Sản xuất (MES - Manufacturing Execution System) đóng vai trò trung gian gì giữa ERP (như SAP, Oracle) và hệ thống SCADA/PLC dưới tầng xưởng?",
        "key_points": (
            "• Kiến trúc phân tầng ISA-95 tiêu chuẩn:\n"
            "  - Tầng 4 (Kế hoạch kinh doanh - ERP): Quản lý đơn hàng, kế hoạch mua hàng, tài chính, định mức BOM vĩ mô (chu kỳ cập nhật tính theo ngày/tuần).\n"
            "  - Tầng 3 (Thực thi phân xưởng - MES): Cầu nối thời gian thực! Tiếp nhận Lệnh sản xuất (Work Order) từ ERP rồi phân bổ xuống từng máy, kiểm soát phả hệ sản phẩm (Traceability), OEE tức thì, công đoạn gia công, lịch sử chất lượng theo từng phút/giây.\n"
            "  - Tầng 1 & 2 (Điều khiển tự động - PLC/SCADA): Thu thập xung tín hiệu cảm biến, nhiệt độ, áp suất, vận tốc động cơ từ thiết bị máy móc.\n"
            "• Vai trò sống còn của MES: Biến phân xưởng từ 'hộp đen' thiếu minh bạch thành bức tranh số hóa thời gian thực, ngăn chặn dữ liệu giả mạo."
        )
    },
    {
        "id": "q_it_02",
        "category": "ERP/MES & Quản Lý Genba",
        "type": "Tình Huống Thực Chiến",
        "question": "Dữ liệu sản lượng trên bảng báo cáo viết tay của công nhân ghi làm được 1,100 sản phẩm, nhưng dữ liệu đếm xung từ cảm biến PLC gửi lên hệ thống MES chỉ ghi nhận 930 sản phẩm. Bạn điều tra và xử lý sự lệch pha 170 sản phẩm này thế nào?",
        "key_points": (
            "• Phương pháp truy tìm sự thật khách quan:\n"
            "  1. Kiểm tra kỹ thuật cảm biến đếm: Cảm biến quang có bị bụi bám làm mất xung? Khoảng cách giữa 2 phôi quá sát nhau làm cảm biến chỉ đếm 1 lần cho 2 sản phẩm? Test thủ công 50 sản phẩm qua máy để xác minh độ chính xác 100% của sensor.\n"
            "  2. Kiểm tra hiện trường vật lý: Đếm số lượng sản phẩm thực tế đang nằm trong sọt thành phẩm và kiểm tra số phế phẩm trong thùng hủy.\n"
            "  3. Đối chất với công nhân & tổ trưởng: Nhiều trường hợp công nhân ghi khống sản lượng để đủ KPI ca hoặc bù vào số hàng đã làm lỗi giấu dưới gầm bàn.\n"
            "  4. Giải pháp gốc rễ: Đồng bộ hóa quy trình quét mã vạch (Barcode/QR code scanning) từng sản phẩm khi đóng thùng, dữ liệu MES chốt tự động, loại bỏ hoàn toàn việc nhập liệu thủ công bằng sổ sách."
        )
    },
    {
        "id": "q_it_03",
        "category": "ERP/MES & Quản Lý Genba",
        "type": "Tình Huống Thực Chiến",
        "question": "Phương châm '3 Thực' của người Nhật (Genba - Hiện trường thực tế, Genbutsu - Hiện vật thực tế, Genjitsu - Hiện trạng dữ liệu thực tế). Hãy kể một tình huống bạn giải quyết sự cố sản xuất thành công nhờ bám sát Genba?",
        "key_points": (
            "• Khung trả lời STAR ấn tượng:\n"
            "  - Situation (Bối cảnh): Phòng họp báo cáo máy hàn siêu âm liên tục bị rách mép vải không dệt, tỷ lệ lỗi 12%. Mọi người ngồi phòng máy lạnh suy đoán do dao cùn hoặc điện áp không ổn định.\n"
            "  - Genba & Genbutsu: Bạn từ chối ngồi nghe phỏng đoán, trực tiếp xuống xưởng, cầm kính lúp soi mẫu vải rách (Hiện vật thực) và đứng quan sát máy chạy suốt 45 phút (Hiện trường thực).\n"
            "  - Genjitsu (Dữ liệu thực): Bạn phát hiện cứ mỗi lần quạt công nghiệp phía đối diện xoay về hướng máy hàn thì mép vải bị gió thổi bay phất phơ lệch khỏi cữ 2mm trước khi đầu hàn ép xuống.\n"
            "  - Action & Result: Làm một tấm mica chắn gió trị giá 50.000đ lắp quanh vùng hàn. Tỷ lệ lỗi rách mép vải lập tức giảm từ 12% xuống 0.1% ngay trong ca đó mà không tốn tiền thay linh kiện đắt tiền."
        )
    },
    {
        "id": "q_it_04",
        "category": "ERP/MES & Quản Lý Genba",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Trong phương pháp giải quyết vấn đề 8D (Eight Disciplines of Problem Solving), hãy phân biệt rõ sự khác nhau giữa D3 (Hành động ngăn chặn khẩn cấp - Containment) và D5/D6 (Hành động khắc phục nguyên nhân gốc rễ - Corrective Action)?",
        "key_points": (
            "• Phân biệt rõ ranh giới:\n"
            "  - D3 (Containment Action - Băng bó vết thương khẩn cấp):\n"
            "    * Mục đích: CÁCH LY NGUY HIỂM NGAY LẬP TỨC để hàng lỗi không thể thoát ra ngoài đến tay khách hàng hoặc công đoạn sau.\n"
            "    * Ví dụ: Dừng xuất xưởng, phong tỏa toàn bộ kho hàng, huy động nhân viên kiểm tra 100% bằng mắt tại chỗ trong vòng 24 giờ.\n"
            "  - D5 & D6 (Corrective Action - Chữa trị tận gốc rễ căn bệnh):\n"
            "    * Mục đích: TRIỆT TIÊU NGUYÊN NHÂN GỐC (Root Cause) để lỗi đó không bao giờ có cơ hội tái diễn trong tương lai.\n"
            "    * Ví dụ: Cải tiến lại bản vẽ cơ khí, lắp thêm chốt Poka-Yoke, sửa đổi chương trình PLC, cập nhật tài liệu đào tạo SOP."
        )
    },
    {
        "id": "q_it_05",
        "category": "ERP/MES & Quản Lý Genba",
        "type": "Tình Huống Thực Chiến",
        "question": "Làm thế nào để xây dựng một Dashboard thời gian thực (Real-time Manufacturing Dashboard) hiển thị OEE, nhịp độ sản xuất và cảnh báo dừng máy hiệu quả cho Giám đốc nhà máy và Trưởng ca?",
        "key_points": (
            "• Kiến trúc giải pháp hiển thị trực quan (Visual Factory):\n"
            "  1. Tầng thu thập: Bộ điều khiển IoT (Raspberry Pi / Edge Gateway) đọc trạng thái ngõ ra PLC (Run, Stop, Alarm, Product Count).\n"
            "  2. Tầng xử lý & cơ sở dữ liệu: Đẩy dữ liệu qua giao thức MQTT/WebSocket về cơ sở dữ liệu chuỗi thời gian (InfluxDB hoặc PostgreSQL).\n"
            "  3. Tầng giao diện hiển thị (Power BI / Grafana / Web Custom):\n"
            "     - Màn hình TV lớn treo trên xưởng cho Trưởng ca: Hiển thị thanh tiến độ sản xuất so với Target theo giờ, màu sắc đèn tháp (Xanh/Vàng/Đỏ), đồng hồ đếm ngược Takt Time, và nguyên nhân máy dừng trên 5 phút.\n"
            "     - Màn hình cho Ban Giám đốc: Biểu đồ xu hướng OEE toàn nhà máy trong 30 ngày, cơ cấu tổn thất lớn nhất (Six Big Losses), bảng xếp hạng hiệu quả từng chuyền sản xuất."
        )
    },
    {
        "id": "q_it_06",
        "category": "ERP/MES & Quản Lý Genba",
        "type": "Phân Tích Sâu",
        "question": "Giữa việc 'Đầu tư công nghệ chuyển đổi số 4.0 đắt tiền' và 'Tối ưu hóa chuẩn hóa quy trình Lean thủ công', bạn sẽ ưu tiên việc nào trước trong một nhà máy sản xuất truyền thống? Tại sao?",
        "key_points": (
            "• Nguyên lý kinh điển: 'Số hóa một quy trình rác thì bạn chỉ thu được một quy trình rác số hóa nhanh hơn!' (Automating a mess only gives you an automated mess).\n"
            "• Thứ tự ưu tiên chiến lược:\n"
            "  1. Bước 1: Áp dụng LEAN để dọn dẹp mặt bằng, triệt tiêu 7 lãng phí, chuẩn hóa thao tác làm việc (SOP), cân bằng chuyền và thiết lập kỷ luật 5S cơ bản.\n"
            "  2. Bước 2: Khi quy trình đã mượt mà, ổn định và không còn lãng phí dư thừa, lúc này mới đưa CÔNG NGHỆ SỐ HÓA (IoT, MES, Robot, AI Vision) vào để khuếch đại hiệu quả và duy trì sự kiểm soát tự động.\n"
            "  - Kết luận: Lean là 'gốc rễ của phương pháp', Công nghệ là 'đòn bẩy tăng tốc'. Một người kỹ sư cải tiến giỏi luôn bắt đầu từ việc tối ưu hóa quy trình tinh gọn trước khi đề xuất chi tiền mua sắm công nghệ."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 11: CÔNG NGHỆ & MÁY MÓC DÂY CÁP ĐIỆN (CADIVI)
    # =========================================================================
    {
        "id": "q_cable_01",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Trình bày chuỗi quy trình công nghệ sản xuất dây và cáp điện hoàn chỉnh tại một nhà máy như CADIVI Miền Trung (từ đồng rod nguyên liệu đến thành phẩm xuất xưởng) và chỉ ra 3 công đoạn trọng yếu dễ phát sinh điểm nghẽn nhất?",
        "key_points": (
            "• Chuỗi 7 công đoạn công nghệ cốt lõi:\n"
            "  1. Tiếp nhận nguyên liệu: Đồng rod Ø 8.0 mm (độ tinh khiết ≥ 99.99% Cu, IACS ≥ 100%) / Nhôm rod Ø 9.5 mm và hạt nhựa cách điện (PVC, XLPE, PE, LSZH).\n"
            "  2. Kéo sợi (Wire Drawing): Máy kéo thô (RBD) → kéo trung → kéo tinh/kéo nhiều sợi (Multi-wire) để giảm đường kính sợi theo quy cách.\n"
            "  3. Ủ mềm (Annealing): Ủ liên tục (In-line Resistance Annealer) hoặc lò ủ chuông khí bảo vệ để phục hồi độ giãn dài và độ dẫn điện.\n"
            "  4. Bện ruột dẫn (Stranding / Bunching): Bện xoắn đôi (Buncher) cho dây mềm hoặc bện lồng cứng/bện ống (Rigid/Tubular Strander) cho cáp lực (7, 19, 37, 61 sợi, bện nén tròn/rẻ quạt tới 300 mm²).\n"
            "  5. Đùn bọc cách điện (Insulation Extrusion) & Khâu mạch XLPE (CCV hoặc Silane + Bể nước nóng/Sauna).\n"
            "  6. Ghép lõi (Laying-up / Drum Twister), giáp băng thép/sợi thép (DSTA/SWA cho cáp ngầm) & Đùn bọc vỏ bảo vệ (Sheathing).\n"
            "  7. Thử nghiệm QA/QC (điện trở ruột dẫn 20°C, thử cao áp, phóng điện cục bộ PD, kéo đứt, lão hóa) & Đóng cuộn khoanh 100m / Rulo gỗ.\n"
            "• 3 điểm nghẽn kinh điển ngành cáp:\n"
            "  - (1) Dây chuyền Đùn bọc cách điện/vỏ (tốn thời gian đổi màu, xả nhựa purging, dễ lệch tâm & phế startup).\n"
            "  - (2) Công đoạn Kéo tinh/Kéo thô (đứt sợi làm dừng máy đột ngột, thay khuôn PCD).\n"
            "  - (3) Công đoạn Bện nhiều sợi & Đóng cuộn thành phẩm (nhiều thao tác gá rulo, mất cân bằng lao động OLE)."
        )
    },
    {
        "id": "q_cable_02",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "type": "Tình Huống Thực Chiến",
        "question": "Máy kéo thô (Rod Breakdown - RBD) và máy kéo tinh (Multi-wire Drawing) liên tục xảy ra hiện tượng 'Đứt sợi đồng' (Wire Break) trung bình 4 lần/ca, khiến OEE sụt giảm nghiêm trọng. Bạn phân tích nguyên nhân gốc bằng 4M và xử lý thế nào?",
        "key_points": (
            "• Phân tích nguyên nhân gốc theo 4M đặc thù kéo dây đồng:\n"
            "  - Material (Vật liệu): Đồng rod đầu vào chứa tạp chất oxit đồng (inclusion), bọt khí, hoặc mối hàn nối đầu cuộn (Butt Weld) bị giòn/không mài phẳng bavia.\n"
            "  - Machine (Máy & Khuôn kéo): Khuôn kéo PCD bị mòn, xước lòng khuôn hoặc phân bổ tỷ lệ giảm diện tích giữa các cấp khuôn (Drafting / Reduction Ratio) bị lệch làm căng cục bộ; puli dẫn hướng bị rãnh mòn gây kẹt sợi.\n"
            "  - Method (Công nghệ bôi trơn/nhiệt): Dung dịch nhũ tương (Drawing Emulsion) sai nồng độ, pH lệch, bẩn nhiều mạt đồng mịn hoặc nhiệt độ bể dầu tăng cao (> 45°C) làm mất màng bôi trơn.\n"
            "  - Man (Thao tác): Kỹ thuật viên hàn nối đồng rod quá nhiệt gây cháy mối hàn hoặc xỏ dây sai thứ tự khuôn.\n"
            "• Giải pháp OE có thể đo lường:\n"
            "  1. Soi kính hiển vi đầu sợi bị đứt (Fracture Morphology): Đầu đứt hình chén-nón (Cup-and-cone) → do lỗi tạp chất đồng rod; Đầu đứt nhọn kéo giãn → do quá lực căng/mòn khuôn; Đứt tại mối hàn → chuẩn hóa SOP máy hàn đối đầu.\n"
            "  2. Lập lịch thay bộ khuôn theo định mức tấn đồng (PM theo sản lượng) kết hợp lọc ly tâm bể nhũ tương hàng ngày.\n"
            "  3. Theo dõi chỉ số KPI chuẩn ngành: 'Số lần đứt sợi / 1 tấn đồng kéo' (Breaks per Ton), đặt mục tiêu giảm về < 0.2 lần/tấn."
        )
    },
    {
        "id": "q_cable_03",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Tại sao sợi đồng sau khi kéo nguội bắt buộc phải qua công đoạn Ủ (Annealing)? Nếu nhiệt độ/dòng điện ủ quá thấp hoặc quá cao thì gây hậu quả gì cho các công đoạn sau và tiêu chuẩn IEC 60228?",
        "key_points": (
            "• Bản chất luyện kim của công đoạn Ủ đồng:\n"
            "  - Trong quá trình kéo nguội qua hàng chục khuôn liên tiếp, mạng tinh thể đồng bị biến dạng và hóa bền biến dạng (Work Hardening) → Sợi đồng trở nên cứng, giòn, độ giãn dài giảm mạnh và điện trở suất tăng lên.\n"
            "  - Ủ làm tái kết tinh mạng tinh thể đồng, khôi phục độ mềm dẻo (độ giãn dài đạt 20–30%) và đưa độ dẫn điện đạt chuẩn ≥ 100% IACS.\n"
            "• Hậu quả khi thông số ủ sai:\n"
            "  - Ủ NON (Dòng/Nhiệt quá thấp): Sợi còn cứng, độ giãn dài thấp → khi sang máy bện dễ bật lò xo (spring-back), gãy sợi khi uốn cáp, điện trở ruột dẫn cao có nguy cơ không đạt IEC 60228.\n"
            "  - Ủ GIÀ (Dòng/Nhiệt quá cao): Sợi quá mềm dễ bị kéo giãn làm nhỏ đường kính cục bộ (tăng điện trở), cháy bề mặt hoặc dính bết các vòng sợi trên rulo (Stickiness trong lò ủ chuông) khiến công đoạn bện bị đứt dây hàng loạt; nếu thiếu khí bảo vệ/hơi nước sẽ bị oxy hóa đen bề mặt đồng."
        )
    },
    {
        "id": "q_cable_04",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "type": "Phân Tích Sâu",
        "question": "Trong ngành sản xuất dây cáp điện, 'Copper Give-away' (Hao phí đồng cho không) và 'Compound Over-thickness' (Bọc dư chiều dày nhựa) là gì? Vì sao tối ưu 2 khoản này thường mang lại lợi nhuận lớn hơn cả việc tăng tốc độ máy?",
        "key_points": (
            "• Cơ cấu giá thành ngành cáp điện:\n"
            "  - Đồng/Nhôm chiếm tới 60–75% giá thành sản phẩm; Nhựa cách điện/vỏ PVC, XLPE chiếm 15–25%; Chi phí nhân công & điện năng chỉ chiếm khoảng 5–10%.\n"
            "• Copper Give-away (Dư đồng):\n"
            "  - Tiêu chuẩn IEC 60228 quy định chất lượng ruột dẫn theo ĐIỆN TRỞ TỐI ĐA (Ω/km ở 20°C), không bắt buộc đường kính to thừa. Nếu máy kéo mòn khuôn hoặc công nhân để đường kính sợi đồng to hơn danh định chỉ +0.01 mm (dư ~1% khối lượng đồng), với nhà máy tiêu thụ 500 tấn đồng/tháng (~250 triệu đ/tấn), 1% dư đồng làm 'bốc hơi' tới 1.25 TỶ ĐỒNG mỗi tháng!\n"
            "• Compound Over-thickness (Bọc dư nhựa cách điện/vỏ):\n"
            "  - Khi máy đùn có độ lệch tâm lớn (Eccentricity cao) hoặc dao động đường kính mạnh (Cpk < 1.0), công nhân buộc phải chỉnh bọc dày thêm +0.08 đến +0.15 mm để 'điểm mỏng nhất' không rớt chuẩn TCVN/IEC.\n"
            "  - Giải pháp OE: Áp dụng SPC + Cảm biến Laser đo đường kính & độ lệch tâm trực tuyến (Closed-loop Control) để thu hẹp độ biến thiên (Cpk ≥ 1.33), đưa chiều dày nhựa trung bình tiệm cận sát biên giới thiết kế tối ưu — tiết kiệm hàng tỷ đồng nhựa mỗi năm mà chất lượng vẫn đạt chuẩn 100%."
        )
    },
    {
        "id": "q_cable_05",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Giải thích ý nghĩa của 'Hệ số xoắn bện' (Lay-up / Stranding Factor) khi tính định mức BOM ruột dẫn nhiều sợi và so sánh công nghệ bện tròn thường vs bện nén ép chặt (Compacted Round Stranding)?",
        "key_points": (
            "• Hệ số xoắn bện (Stranding / Take-up Factor — k):\n"
            "  - Khi bện xoắn các sợi đồng đơn quanh lõi theo bước xoắn h (Lay Length) và đường kính vòng xoắn D, chiều dài thực tế của mỗi sợi đơn luôn DÀI HƠN chiều dài đoạn cáp thành phẩm:\n"
            "    k = sqrt(1 + (π × D / h)²), thường dao động từ 1.015 đến 1.035 (tăng 1.5% – 3.5% chiều dài đồng).\n"
            "  - Nếu lập định mức BOM mà quên nhân hệ số xoắn k, báo cáo cuối tháng sẽ luôn báo 'âm kho đồng' ảo dù xưởng không làm hỏng!\n"
            "• So sánh Bện tròn thường vs Bện nén ép chặt (Compacted Stranding):\n"
            "  - Bện nén dùng khuôn ép (Compacting Die) hoặc cặp con lăn ép ngay tại điểm hội tụ để làm phẳng các khe hở giữa các sợi đồng (hệ số điền đầy tăng từ ~75% lên >90%).\n"
            "  - Lợi ích kinh tế cực lớn: Đường kính ngoài của ruột dẫn giảm 8–10% ở cùng tiết diện dẫn điện → Tiết kiệm trực tiếp 10–15% lượng nhựa cách điện XLPE/PVC và vật liệu độn/vỏ bọc ở các công đoạn sau, đồng thời chống thấm dọc tốt hơn."
        )
    },
    {
        "id": "q_cable_06",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "type": "Tình Huống Thực Chiến",
        "question": "Trên dây chuyền Đùn bọc cách điện PVC, thiết bị Spark Tester (Thử cao áp trực tuyến) liên tục báo lỗi đánh thủng cách điện (Pinhole / Spark Fault) với tần suất 15 lỗi/10 km dây. Bạn dẫn dắt tổ sản xuất điều tra và khắc phục thế nào?",
        "key_points": (
            "• Bản chất Spark Tester:\n"
            "  - Dùng điện áp cao tần (thường 3 kV – 15 kV tùy độ dày cách điện) phóng qua chổi chuỗi hạt thép tiếp xúc bề mặt dây đang chạy. Nếu có lỗ mọt khí, dị vật kim loại hoặc chỗ nhựa mỏng quá mức, tia lửa điện đánh thủng vào ruột đồng và máy lập tức đếm lỗi/dừng dây.\n"
            "• 5 nguyên nhân gốc phổ biến cần kiểm tra tại Genba:\n"
            "  1. Hạt nhựa PVC bị ẩm (chưa sấy đạt độ ẩm chuẩn) → bay hơi nước trong nòng đùn tạo bọt khí (Void/Pinhole).\n"
            "  2. Nhiệt độ vùng gia nhiệt (Barrel Zone 1–5 / Crosshead) quá cao gây cháy phân hủy PVC (Burning/Scorching tạo hạt đen dẫn điện) hoặc quá thấp làm nhựa chưa dẻo hóa đều.\n"
            "  3. Tạp chất / bụi kim loại lẫn vào phễu cấp nhựa tái sinh hoặc lưới lọc (Screen Pack) bị rách không giữ được cặn.\n"
            "  4. Ruột đồng có gai/bavia sợi đứt lòi ra đâm thủng lớp cách điện (hay gặp ở dây nhiều sợi mềm).\n"
            "  5. Độ lệch tâm (Eccentricity) lớn khiến một bên vỏ quá mỏng.\n"
            "• Hành động OE: Cắt đúng vị trí lỗi Spark đưa lên kính hiển vi/OGP soi mặt cắt ngang để phân loại lỗi (bọt khí vs hạt cháy vs gai đồng vs mỏng lệch tâm) → lập Pareto 80/20 xử lý đúng nguyên nhân số 1."
        )
    },
    {
        "id": "q_cable_07",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "type": "Tình Huống Thực Chiến",
        "question": "Thời gian chuyển đổi (Changeover) trên máy đùn bọc cáp khi đổi màu nhựa và đổi tiết diện hiện mất 55 phút và thải ra 25 kg nhựa xả (Purge Scrap) cùng 150m đồng bọc phế. Bạn áp dụng SMED và điều độ thế nào để rút xuống dưới 15 phút?",
        "key_points": (
            "• Kết hợp 2 mũi nhọn: Điều độ thông minh (Scheduling) + Kỹ thuật SMED:\n"
            "  1. Lập lịch theo Chuỗi Màu (Color Sequencing) & Họ Tiết Diện: Sắp xếp lệnh chạy trong ngày đi từ màu Sáng → Tối (Trắng → Vàng → Xanh lá → Đỏ → Xanh dương → Đen) và theo thứ tự tiết diện liền kề → Giảm 60–70% lượng nhựa xả và thời gian vệ sinh trục vít.\n"
            "  2. Tách External Setup: Chuẩn bị và sấy sẵn hạt nhựa màu mới trong phễu hút di động; lắp và sấy nóng trước bộ Đầu Chày-Cối (Crosshead / Tip & Die) ở tủ sấy bên ngoài đạt 160°C sẵn sàng trước khi máy dừng.\n"
            "  3. Giảm Internal Setup: Dùng đầu chữ thập tháo lắp nhanh (Quick-change Self-centering Crosshead không cần chỉnh ốc tâm thủ công), dùng Hợp chất xả trục vít (Purging Compound) giúp làm sạch màu cũ nhanh gấp 3 lần nhựa thường.\n"
            "  4. Giảm phế khởi động (Startup Scrap): Lưu sẵn bộ công thức thông số nhiệt độ/tốc độ vít/tốc độ kéo (Recipe) trên PLC theo từng mã cáp để máy đạt dung sai đường kính chỉ sau 15–20m đầu tiên."
        )
    },
    {
        "id": "q_cable_08",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "type": "Phân Tích Sâu",
        "question": "Tại sao trong nhà máy cáp điện, việc quản lý phân loại 'Phế liệu đồng trần' (Bare Copper Scrap) tách biệt hoàn toàn với 'Phế liệu đồng dính nhựa' (Insulated Copper Scrap) lại là KPI sống còn về chi phí?",
        "key_points": (
            "• Chênh lệch giá trị thu hồi tài chính cực lớn:\n"
            "  - Đồng trần sạch (từ công đoạn kéo, ủ, bện) có giá trị thu hồi tái chế đạt ~93–96% giá đồng nguyên liệu mới.\n"
            "  - Đồng đã bọc nhựa PVC/XLPE (từ công đoạn đùn, bọc vỏ, cắt đầu-đuôi) phải tốn thêm chi phí nhân công/máy tuốt băm tách nhựa, hao hụt khối lượng và lẫn tạp chất nên giá trị thu hồi chỉ còn ~75–82% (mất trắng 15–20% giá trị đồng!).\n"
            "• Chiến lược kiểm soát OE:\n"
            "  1. Theo dõi riêng 2 chỉ số: Bare Copper Scrap % và Insulated Copper Scrap % theo từng máy, từng ca.\n"
            "  2. Triển khai Poka-Yoke kiểm tra chất lượng ruột dẫn TRƯỚC khi đưa vào máy đùn (không bao giờ bọc nhựa lên cuộn đồng đã bị lỗi bện, lỗi điện trở hoặc thiếu chiều dài!).\n"
            "  3. Áp dụng nguyên tắc 'Cân phế tại nguồn': Mỗi máy có thùng rác mã màu riêng (Đỏ = Đồng trần, Vàng = Đồng bọc nhựa, Xanh = Nhựa xả sạch có thể nghiền tái sử dụng lớp độn), cân và nhập ERP cuối mỗi ca để tính BOM Variance chính xác."
        )
    },
    {
        "id": "q_cable_09",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "type": "Tình Huống Thực Chiến",
        "question": "Bài toán 'Tối ưu cắt chiều dài rulo' (Cut-Length / Cutting Stock Problem): Công đoạn bện tạo ra rulo dài 2,150m nhưng đơn hàng khách chỉ lấy cuộn 500m, khiến mỗi rulo luôn dư 150m cáp lẻ khó bán (Remnant Scrap). Chuyên viên OE giải quyết bài toán này ra sao?",
        "key_points": (
            "• Bản chất tổn thất:\n"
            "  - Mẩu cáp ngắn 80–200m dư sau cắt là 'Tồn kho chết' (Dead Stock) hoặc phải bán phế liệu với mức lỗ 20–30% giá trị đồng.\n"
            "• 4 giải pháp tối ưu Cut-Length:\n"
            "  1. Kế hoạch kéo/bện ngược từ đơn hàng (Backward Length Planning): Thay vì bện đầy rulo theo cảm tính, tính chiều dài chuẩn bội số của chiều dài xuất xưởng cộng đúng lượng bù hao hụt công nghệ (ví dụ: 4 × 500m + 15m hao đầu-đuôi đùn = 2,015m thay vì 2,150m).\n"
            "  2. Dùng mô hình toán học tối ưu tổ hợp cắt (Excel Solver / Python PuLP Cutting Stock) để ghép các đơn lẻ (vd: 300m + 500m + 1,200m = 2,000m) vào chung một mẻ đùn dài.\n"
            "  3. Kiểm chuẩn đồng hồ đếm mét (Length Counter Calibration) định kỳ trên máy bện & máy đùn: sai số đếm mét 1–2% trên cuộn 2,000m sẽ gây thiếu 20–40m (phải cắt bỏ cả cuộn 500m cuối!).\n"
            "  4. Thiết lập kho tồn mẩu ngắn (Remnant Database) trên ERP/Excel để bộ phận điều độ ưu tiên lấy mẩu dư cắt cho các đơn nhỏ trước khi phát lệnh chạy mới."
        )
    },
    {
        "id": "q_cable_10",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Phân biệt 2 công nghệ lưu hóa/khâu mạch cách điện XLPE phổ biến trong nhà máy cáp điện: Dây chuyền CCV (Catenary Continuous Vulcanization) và công nghệ Silane XLPE (Bể nước nóng / Phòng xông hơi Sauna)? Tác động của chúng tới Lead Time và WIP?",
        "key_points": (
            "• Công nghệ Silane XLPE (Moisture Cross-linking — phổ biến cho cáp hạ thế 0.6/1kV tại nhiều nhà máy CADIVI):\n"
            "  - Đùn bọc nhựa PE ghép Silane trên máy đùn thường → Sau đó đưa các rulo lõi vào Bể nước nóng (~80–90°C) hoặc Phòng xông hơi (Sauna) từ 4–12 giờ để xảy ra phản ứng khâu mạch hóa học.\n"
            "  - Tác động OE: Tạo ra điểm dừng chờ giữa công đoạn Đùn lõi và Ghép lõi (tăng WIP rulo và Lead Time), dễ tắc nghẽn nếu bể xông hơi nhỏ; cần tối ưu lịch xếp mẻ bể Sauna và kiểm soát độ ẩm/nhiệt độ để không phải xông lại.\n"
            "• Công nghệ CCV (Khâu mạch liên tục bằng Peroxide trong ống áp suất khí Nitơ nhiệt độ cao — dùng cho cáp trung thế/cao thế):\n"
            "  - Quá trình đùn 3 lớp (bán dẫn trong – cách điện XLPE – bán dẫn ngoài) và lưu hóa diễn ra liên tục trong 1 lượt chạy.\n"
            "  - Tác động OE: Chi phí khởi động/dừng máy và xả nhựa CỰC ĐẮT → Bắt buộc chạy theo chiến dịch dài (Campaign Run), kiểm soát bảo trì phòng ngừa TPM cực chặt để không dừng máy đột ngột giữa chừng."
        )
    },
    {
        "id": "q_cable_11",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Các phép thử QA/QC trọng yếu trong phòng thí nghiệm dây cáp điện (theo TCVN 5935 / IEC 60502 / IEC 60228) là gì, và Chuyên viên OE sử dụng dữ liệu từ phòng Lab như thế nào để cải tiến sản xuất?",
        "key_points": (
            "• 5 nhóm phép thử bắt buộc trong Lab cáp điện:\n"
            "  1. Điện trở ruột dẫn 1 chiều quy về 20°C (Cầu Kelvin / Micro-ohmmeter theo IEC 60228) → đánh giá độ tinh khiết đồng, độ ủ và tiết diện thực.\n"
            "  2. Kích thước hình học cách điện/vỏ bọc (chiều dày trung bình, chiều dày điểm mỏng nhất, độ lệch tâm) đo bằng kính hiển vi/máy chiếu Profile Projector.\n"
            "  3. Cơ lý tính trước và sau lão hóa nhiệt (Máy kéo đứt Tensile + Tủ sấy Aging Oven): đo lực kéo đứt (MPa) & độ giãn dài (%).\n"
            "  4. Thử nghiệm điện áp cao (HV Withstand Test ngâm nước, Spark Test, đo phóng điện cục bộ PD đối với cáp trung thế).\n"
            "  5. Thử nghiệm đặc thù: Thử biến dạng nhiệt (Hot Set Test cho XLPE kiểm tra độ khâu mạch), thử cháy lan (IEC 60332), thử độ đậm đặc khói/khí halogen (cho cáp LSHF/LSZH).\n"
            "• Cách OE khai thác dữ liệu Lab:\n"
            "  - Không chỉ dừng ở 'Đạt / Không đạt (Pass/Fail)'! OE lấy số liệu đo liên tục (điện trở thực tế so với trần IEC, chiều dày thực tế so với min IEC) đưa vào Minitab tính Cpk để tối ưu thu hẹp biên độ dư đồng (Copper Give-away) và dư nhựa (Over-thickness)."
        )
    },
    {
        "id": "q_cable_12",
        "category": "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
        "type": "Phân Tích Sâu",
        "question": "Trong nhà máy CADIVI Miền Trung có sự đa dạng lớn từ dây dân dụng (VC, VCm, VCmt) chạy số lượng cực lớn đến cáp lực hạ thế/trung thế tiết diện tới 300 mm² chạy theo dự án. Chiến lược OE áp dụng cho 2 dòng sản phẩm này khác nhau thế nào?",
        "key_points": (
            "• Dòng 1 — Dây dân dụng (High-Volume, Low-Mix: VC, VCm, VCmd cuộn 100m):\n"
            "  - Đặc trưng: Nhu cầu ổn định, sản lượng mét cực lớn, cạnh tranh khốc liệt về giá thành.\n"
            "  - Trọng tâm OE: Tối đa hóa tốc độ đùn & kéo (OEE Performance), áp dụng hệ thống Kéo/Siêu thị thành phẩm (Make-to-Stock + Kanban), tự động hóa khâu cuộn khoanh/bọc màng co để nâng OLE, và siết từng 0.01 mm nhựa/đồng bằng SPC.\n"
            "• Dòng 2 — Cáp lực & Cáp công trình tiết diện lớn (High-Mix, Low-Volume: CXV, CVV, DSTA lên đến 300 mm²):\n"
            "  - Đặc trưng: Đơn hàng dự án đa dạng quy cách/chiều dài rulo, thời gian đổi mã dài, rulo rất nặng (1–5 tấn).\n"
            "  - Trọng tâm OE: Áp dụng Make-to-Order (MTO), SMED rút ngắn thời gian nạp rulo/đổi khuôn bện-đùn, tối ưu Cut-Length chống thừa mẩu cáp, rút ngắn Lead Time tổng bằng VSM & TOC, và tối ưu điều phối cầu trục/kho đệm rulo WIP."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 12: OE, SIX SIGMA (DMAIC), TOC, TPM & PFMEA
    # =========================================================================
    {
        "id": "q_oe_01",
        "category": "OE, Six Sigma (DMAIC), TOC, TPM & PFMEA",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Phân biệt sự khác nhau và mối liên kết giữa 4 khái niệm: Operational Excellence (OE), Lean Manufacturing, Six Sigma và Industrial Engineering (IE)?",
        "key_points": (
            "• Phân biệt rõ vai trò từng trụ cột:\n"
            "  1. Industrial Engineering (IE — Kỹ thuật Công nghiệp): Nền tảng kỹ thuật cơ sở: Time & Motion Study, định mức lao động, thiết kế Layout, cân bằng chuyền, Ergonomics, hoạch định năng lực.\n"
            "  2. Lean Manufacturing (Sản xuất Tinh gọn): Tập trung vào TỐC ĐỘ DÒNG CHẢY và LOẠI BỎ LÃNG PHÍ (8 Wastes, VSM, 5S, SMED, Kanban, Pull) để giảm Lead Time.\n"
            "  3. Six Sigma: Tập trung vào GIẢM ĐỘ BIẾN THIÊN (Variation) và TRIỆT TIÊU KHUYẾT TẬT (Defects < 3.4 DPMO) bằng tư duy thống kê chặt chẽ (DMAIC, SPC, DOE, Hypothesis Testing).\n"
            "  4. Operational Excellence (OE — Xuất sắc Vận hành): Là TẦNG HỆ THỐNG TỔNG THỂ bao trùm cả IE + Lean + Six Sigma + Văn hóa quản trị hàng ngày (Daily Management System) + Chiến lược kinh doanh (Hoshin Kanri), nhằm tạo ra năng lực vận hành bền vững, chi phí tối ưu và giao hàng chuẩn xác."
        )
    },
    {
        "id": "q_oe_02",
        "category": "OE, Six Sigma (DMAIC), TOC, TPM & PFMEA",
        "type": "Tình Huống Thực Chiến",
        "question": "Hãy trình bày cụ thể cách bạn triển khai 1 dự án Lean Six Sigma theo chu trình 5 pha DMAIC để giảm tỷ lệ phế phẩm đùn bọc cách điện từ 3.8% xuống dưới 1.0% trong 3 tháng?",
        "key_points": (
            "• Lộ trình 5 pha DMAIC chuẩn Green Belt:\n"
            "  - D (Define — Xác định): Lập Project Charter (Mục tiêu giảm Scrap từ 3.8% → <1.0%, tiết kiệm dự kiến X triệu/năm), vẽ SIPOC và xác định CTQ (Critical to Quality: đường kính ngoài, chiều dày min, 0 lỗi Spark).\n"
            "  - M (Measure — Đo lường): Kiểm định hệ thống đo (MSA Gage R&R < 10%), thu thập dữ liệu nền 30 ngày (Baseline), phân tầng lỗi bằng biểu đồ Pareto, tính năng lực quy trình hiện tại (Cpk/Sigma Level).\n"
            "  - A (Analyze — Phân tích): Vẽ biểu đồ Xương cá (Fishbone), làm PFMEA chọn ra top X nguyên nhân tiềm ẩn (nhiệt độ vùng 3, độ ẩm hạt PVC, tốc độ vít, mòn đầu cối) → Dùng kiểm định giả thuyết (t-test, ANOVA, Regression) chứng minh thống kê nguyên nhân nào thực sự tác động (p-value < 0.05).\n"
            "  - I (Improve — Cải tiến): Chạy thí nghiệm thiết kế (DOE) tìm cửa sổ thông số tối ưu (nhiệt độ, tốc độ, sấy hạt), áp dụng Poka-Yoke/SMED và chạy thử Pilot Line kiểm chứng kết quả bằng 2-Sample t-test Trước–Sau.\n"
            "  - C (Control — Kiểm soát): Khóa chặt kết quả bằng Control Plan, biểu đồ SPC theo ca, cập nhật SOP/OPL và bàn giao quy trình kiểm soát cho Quản đốc theo dõi liên tục 3 tháng."
        )
    },
    {
        "id": "q_oe_03",
        "category": "OE, Six Sigma (DMAIC), TOC, TPM & PFMEA",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Trình bày 5 bước tập trung của Lý thuyết Điểm nghẽn (Theory of Constraints - TOC của Eliyahu Goldratt) và cách áp dụng cơ chế Drum-Buffer-Rope (DBR) trong nhà máy nhiều công đoạn?",
        "key_points": (
            "• 5 Bước Tập Trung (5 Focusing Steps of TOC):\n"
            "  1. Identify (Xác định): Tìm đúng điểm nghẽn duy nhất quyết định sản lượng toàn nhà máy (ví dụ: dây chuyền Đùn bọc vỏ số 2 luôn có hàng rulo chờ ùn tắc phía trước).\n"
            "  2. Exploit (Khai thác tối đa): Bóc sạch mọi lãng phí tại điểm nghẽn mà chưa cần mua máy mới (ăn ca luân phiên không tắt máy, SMED, QC đầu vào kỹ để điểm nghẽn không bao giờ gia công hàng lỗi).\n"
            "  3. Subordinate (Bắt các khâu khác phục tùng): Điều chỉnh nhịp chạy của các máy Kéo/Bện phía trước khớp với nhịp điểm nghẽn để không chất núi WIP.\n"
            "  4. Elevate (Nâng cấp năng lực): Nếu khai thác hết vẫn thiếu công suất → mới đầu tư mở thêm ca, nâng cấp tốc độ hoặc mua máy mới.\n"
            "  5. Repeat (Lặp lại): Khi điểm nghẽn cũ được giải tỏa, điểm nghẽn mới sẽ xuất hiện ở công đoạn khác — quay lại Bước 1, không để sức ỳ làm hỏng hệ thống.\n"
            "• Cơ chế Drum-Buffer-Rope (Trống – Đệm – Dây kéo): Điểm nghẽn gõ nhịp sản xuất (Drum); đặt kho đệm thời gian an toàn ngay trước điểm nghẽn để nó không bao giờ bị đói hàng (Buffer); và kéo dây tín hiệu (Rope) báo cho công đoạn đầu tiên chỉ nhả nguyên liệu đúng bằng tốc độ điểm nghẽn tiêu thụ."
        )
    },
    {
        "id": "q_oe_04",
        "category": "OE, Six Sigma (DMAIC), TOC, TPM & PFMEA",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Tính và giải thích 2 chỉ số độ tin cậy thiết bị cốt lõi trong TPM: MTBF (Mean Time Between Failures) và MTTR (Mean Time To Repair)? Làm sao cải thiện cả hai chỉ số này?",
        "key_points": (
            "• Định nghĩa & Công thức:\n"
            "  - MTBF (Thời gian trung bình giữa 2 lần hỏng — đo ĐỘ TIN CẬY): MTBF = Tổng thời gian chạy máy / Số lần hỏng hóc đột xuất. (MTBF càng CAO càng tốt).\n"
            "  - MTTR (Thời gian trung bình để sửa chữa — đo TỐC ĐỘ PHỤC HỒI): MTTR = Tổng thời gian dừng sửa chữa / Số lần hỏng hóc đột xuất. (MTTR càng THẤP càng tốt).\n"
            "  - Ví dụ: Trong tháng máy chạy 400 giờ và hỏng 8 lần với tổng thời gian sửa 12 giờ → MTBF = 50 giờ/lần; MTTR = 1.5 giờ/lần.\n"
            "• Giải pháp nâng cao:\n"
            "  - Tăng MTBF: Triển khai Bảo trì tự quản (Jishu Hozen), bảo trì phòng ngừa PM đúng hạn, giám sát rung/nhiệt độ bạc đạn động cơ bằng cảm biến bảo trì dự đoán (PdM), triệt tiêu nguyên nhân gốc lỗi lặp lại.\n"
            "  - Giảm MTTR: Lưu sẵn phụ tùng chiến lược (Critical Spare Parts: vòng bi, điện trở gia nhiệt, cảm biến nhiệt thermocouple, dây curoa), chuẩn hóa tài liệu xử lý sự cố nhanh (Troubleshooting Guide) và đào tạo thợ bảo trì."
        )
    },
    {
        "id": "q_oe_05",
        "category": "OE, Six Sigma (DMAIC), TOC, TPM & PFMEA",
        "type": "Phân Tích Sâu",
        "question": "PFMEA (Process Failure Mode and Effects Analysis) là gì? Cách tính chỉ số rủi ro RPN và tại sao chuẩn AIAG-VDA mới không chỉ nhìn vào tổng điểm RPN đơn thuần?",
        "key_points": (
            "• Bản chất PFMEA:\n"
            "  - Công cụ phân tích rủi ro phòng ngừa theo từng bước quy trình để phát hiện lỗi tiềm ẩn TRƯỚC KHI sản xuất hàng loạt.\n"
            "• Công thức RPN truyền thống:\n"
            "  - RPN = Severity (S — Mức độ nghiêm trọng 1–10) × Occurrence (O — Tần suất xảy ra 1–10) × Detection (D — Khả năng phát hiện 1–10).\n"
            "  - Ví dụ trên máy đùn cáp: Lỗi 'Cách điện bị lệch tâm mỏng hơn chuẩn TCVN' → S = 9 (nguy cơ chập cháy điện mất an toàn), O = 4, D = 5 (chỉ cắt mẫu kiểm tra đầu/cuộn cuộn) → RPN = 180 (Cao, phải hành động ngay bằng cách gắn thiết bị đo độ lệch tâm trực tuyến kéo D xuống 2!).\n"
            "• Cảnh báo theo chuẩn AIAG-VDA mới (Action Priority - AP):\n"
            "  - Không được chỉ dựa vào RPN! Ví dụ Lỗi A có S=10, O=2, D=2 (RPN=40 — nguy cơ cháy nổ chết người!) nguy hiểm hơn rất nhiều so với Lỗi B có S=4, O=5, D=5 (RPN=100 — chỉ trầy nhẹ vỏ ngoài). Do đó PHẢI ưu tiên hành động ngay cho mọi mục có Severity ≥ 9 bất kể RPN thấp."
        )
    },
    {
        "id": "q_oe_06",
        "category": "OE, Six Sigma (DMAIC), TOC, TPM & PFMEA",
        "type": "Tình Huống Thực Chiến",
        "question": "Sau 1 dự án Kaizen trên máy đùn, dữ liệu 15 ngày trước cải tiến có tỷ lệ phế trung bình là 2.4%, 15 ngày sau cải tiến là 2.1%. Làm sao bạn chứng minh trước Ban Giám đốc rằng mức giảm 0.3% này là kết quả thật của cải tiến chứ không phải dao động ngẫu nhiên?",
        "key_points": (
            "• Sai lầm của người làm cải tiến nghiệp dư:\n"
            "  - Chỉ trừ 2 con số trung bình (2.4% - 2.1% = 0.3%) rồi vội kết luận 'thành công', trong khi độ lệch chuẩn dao động từng ngày vốn đã là ±0.6%!\n"
            "• Phương pháp kiểm chứng khoa học (Statistical Hypothesis Testing):\n"
            "  1. Đặt giả thuyết: H0 (Không có sự khác biệt thực sự giữa trước và sau) vs H1 (Phế phẩm sau cải tiến thực sự giảm có ý nghĩa).\n"
            "  2. Kiểm tra tính chuẩn của dữ liệu (Normality Test — Anderson-Darling) trên Minitab/Python (`scipy.stats`).\n"
            "  3. Nếu dữ liệu chuẩn: Chạy kiểm định **2-Sample t-test** (hoặc Mann-Whitney U test nếu phi chuẩn; 2-Proportions Test nếu dùng tỷ lệ lỗi đếm).\n"
            "  4. Đọc chỉ số **p-value** (với mức ý nghĩa α = 0.05):\n"
            "     - Nếu p-value < 0.05 → Bác bỏ H0, khẳng định chắc chắn ≥ 95% cải tiến có hiệu quả thực sự!\n"
            "     - Nếu p-value ≥ 0.05 → Chưa đủ bằng chứng thống kê, cần tiếp tục thu thập thêm mẫu hoặc tối ưu sâu hơn trước khi báo cáo ROI."
        )
    },
    {
        "id": "q_oe_07",
        "category": "OE, Six Sigma (DMAIC), TOC, TPM & PFMEA",
        "type": "Tình Huống Thực Chiến",
        "question": "Khi đề xuất Ban Giám đốc đầu tư một thiết bị cải tiến tự động (ví dụ: hệ thống đo đường kính/độ lệch tâm Laser hoặc máy đo tự động trị giá 1.2 tỷ VNĐ), bạn trình bày bài toán tài chính ROI và Payback Period như thế nào để thuyết phục được phòng Kế toán & Giám đốc?",
        "key_points": (
            "• Cấu trúc 1 bản thuyết minh CAPEX chuẩn OE (không bao giờ chỉ nêu con số cảm tính):\n"
            "  1. Tổng vốn đầu tư đầy đủ (Total CAPEX): Giá máy + thuế/lắp đặt + đồ gá/phần mềm + chi phí đào tạo + chi phí bảo trì hàng năm (OPEX).\n"
            "  2. Bóc tách Lợi ích ròng (Hard Savings vs Soft Savings):\n"
            "     - Hard Savings (Tiền tươi thật — kế toán công nhận): Giảm vật tư nhựa/đồng phế phẩm (kg × đơn giá), giảm giờ tăng ca thực tế, giảm số nhân công luân chuyển sang chuyền mới thiếu người.\n"
            "     - Soft Savings (Lợi ích gián tiếp — ghi chú riêng, KHÔNG gộp chung để thổi phồng Payback): Giảm thời gian chờ báo cáo, tăng uy tín khách hàng.\n"
            "  3. Công thức minh bạch:\n"
            "     - Thời gian hoàn vốn đơn giản (Payback Period) = Tổng vốn đầu tư / Tiết kiệm ròng hằng tháng (hoặc hằng năm).\n"
            "     - ROI 1 năm (%) = (Lợi ích ròng năm 1 - Chi phí vận hành) / Tổng vốn đầu tư × 100%.\n"
            "  4. Phân tích độ nhạy 3 kịch bản (Thận trọng / Cơ sở / Tích cực) để chứng minh ngay cả ở kịch bản thận trọng dự án vẫn hoàn vốn dưới 18–24 tháng."
        )
    },
    {
        "id": "q_oe_08",
        "category": "OE, Six Sigma (DMAIC), TOC, TPM & PFMEA",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Phân biệt khi nào nên dùng chu trình PDCA, Báo cáo A3 (Toyota A3 Report) và Quy trình 8D (Eight Disciplines) trong vận hành nhà máy?",
        "key_points": (
            "• Phân biệt đúng công cụ theo bối cảnh:\n"
            "  - PDCA (Plan–Do–Check–Act): Vòng tròn tư duy cải tiến nền tảng cho mọi hoạt động hàng ngày và Kaizen quy mô nhỏ/vừa, lặp liên tục không dừng.\n"
            "  - Báo cáo A3 (Toyota A3 Thinking): Tóm gọn toàn bộ một dự án cải tiến/giải quyết vấn đề nội bộ trên ĐÚNG 1 TỜ GIẤY A3 (Bối cảnh → Hiện trạng → Mục tiêu → Phân tích gốc → Kế hoạch đối sách → Theo dõi kết quả). Cực mạnh để trình bày nhanh cho Ban Giám đốc và huấn luyện tư duy logic.\n"
            "  - Báo cáo 8D: Tiêu chuẩn bắt buộc cho SỰ CỐ CHẤT LƯỢNG NGHIÊM TRỌNG / KHIẾU NẠI KHÁCH HÀNG (nhấn mạnh bước D3 Containment cô lập lô lỗi ngay trong 24h, D5/D6 Corrective Action và D7 Prevent Recurrence nhân rộng sang các dây chuyền tương tự)."
        )
    },
    {
        "id": "q_oe_09",
        "category": "OE, Six Sigma (DMAIC), TOC, TPM & PFMEA",
        "type": "Phân Tích Sâu",
        "question": "Trong sản xuất liên tục như kéo sợi và đùn bọc cáp, luôn có sự đánh đổi (Trade-off) giữa 'Tăng tốc độ chạy máy' (Performance) và 'Tỷ lệ phế phẩm / Đứt sợi' (Quality & Availability). Làm sao tìm điểm vận hành tối ưu nhất?",
        "key_points": (
            "• Tư duy tối ưu toàn cục (Total Effective Output & Unit Cost):\n"
            "  - Tăng tốc độ máy đùn từ 300 lên 400 m/phút nhưng làm lỗi Spark tăng từ 0.5% lên 5% và đứt dây thêm 30 phút/ca → Thực tế sản lượng ĐẠT CHUẨN (Good Meters/Hour) lại GIẢM và chi phí phế liệu đồng-nhựa tăng vọt!\n"
            "• Cách tìm điểm ngọt vận hành (Optimal Operating Window):\n"
            "  1. Thiết kế thí nghiệm thực tế (DOE — Design of Experiments) thử nghiệm theo các bậc tốc độ (vd: 300 – 330 – 360 – 390 m/phút) kết hợp điều chỉnh đồng bộ nhiệt độ vùng đùn & nhiệt độ nước làm mát.\n"
            "  2. Đo đồng thời 3 hàm mục tiêu tại mỗi bậc: (a) Sản lượng mét đạt chuẩn/giờ, (b) Tỷ lệ phế phẩm & Cpk đường kính, (c) Điện năng tiêu thụ kWh/km.\n"
            "  3. Vẽ đường cong chi phí đơn vị (Cost per km) để chọn dải tốc độ tối ưu nhất về mặt kinh tế, sau đó khóa thành thông số chuẩn (Standard Parameter Sheet) trên PLC."
        )
    },
    {
        "id": "q_oe_10",
        "category": "OE, Six Sigma (DMAIC), TOC, TPM & PFMEA",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Hệ thống Quản trị Hàng ngày Đa tầng (Tiered Daily Management System — Tier 1, Tier 2, Tier 3) vận hành thế nào để các bảng KPI OEE/OLE tại nhà máy thực sự phát huy tác dụng thay vì chỉ treo cho đẹp?",
        "key_points": (
            "• Cấu trúc họp nhanh đứng (Daily Tier Meetings) chuẩn OE:\n"
            "  - Tier 1 (Cấp Tổ/Chuyền — 5–10 phút đầu ca, do Tổ trưởng chủ trì): Xem kết quả SQDC (Safety – Quality – Delivery – Cost) của ca trước, điểm danh nhân sự, phân công xử lý các vấn đề nhỏ trong tầm tay, báo cáo vấn đề vượt thẩm quyền lên Tier 2.\n"
            "  - Tier 2 (Cấp Phân xưởng — 15 phút buổi sáng, do Quản đốc + OE + Bảo trì + QC + Kế hoạch): Giải quyết các điểm nghẽn chuyển từ Tier 1 (máy hỏng lặp lại, thiếu vật tư, OEE dưới ngưỡng mục tiêu), phân rõ 'Ai làm – Việc gì – Hạn chót (Who–What–When)'.\n"
            "  - Tier 3 (Cấp Nhà máy — 15 phút hàng ngày/tuần, Giám đốc nhà máy + các Trưởng phòng): Quyết định nguồn lực liên phòng ban, tiến độ các dự án Kaizen trọng điểm và đơn hàng chiến lược.\n"
            "• Nguyên tắc sống còn: Bảng KPI phải có ngưỡng Xanh/Đỏ trực quan; bất kỳ ngày nào có chỉ số Đỏ BẮT BUỘC phải có thẻ hành động khắc phục đi kèm, không chỉ đọc số cho xong."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 13: HOẠCH ĐỊNH NĂNG LỰC, ĐIỀU ĐỘ & CHI PHÍ SẢN XUẤT
    # =========================================================================
    {
        "id": "q_cap_01",
        "category": "Hoạch Định Năng Lực, Điều Độ & Chi Phí",
        "type": "Tình Huống Thực Chiến",
        "question": "Ban Giám đốc hỏi: 'Tháng tới phòng Kinh doanh nhận thêm đơn hàng 120 tấn cáp lực CXV, nhà máy hiện tại có đủ năng lực đáp ứng không?'. Là Chuyên viên OE, bạn tính toán Hoạch định Năng lực Thô (RCCP) theo những bước nào?",
        "key_points": (
            "• 5 bước tính Năng lực Sản xuất (Rough-Cut Capacity Planning — RCCP):\n"
            "  1. Quy đổi sản lượng thương mại sang Nhu cầu Giờ máy (Required Machine Hours) ở TỪNG công đoạn (Kéo thô RBD → Kéo trung → Bện ruột → Đùn cách điện → Bể xông XLPE → Ghép lõi → Đùn vỏ) dựa trên tốc độ chuẩn (m/phút hoặc kg/giờ) và số lượng lần đổi mã dự kiến.\n"
            "  2. Tính Năng lực Khả dụng Thực tế (Demonstrated Capacity) của từng nhóm máy = Số máy × Số ca × Giờ kế hoạch/ca × Số ngày làm việc × OEE thực tế lịch sử (TUYỆT ĐỐI không nhân với 100% công suất lý thuyết!).\n"
            "  3. Tính Tỷ lệ Tải (Load % = Giờ máy yêu cầu / Giờ máy khả dụng) cho từng công đoạn.\n"
            "  4. Nhận diện công đoạn quá tải (> 85–90% tải → rủi ro trễ giao hàng) và công đoạn dư tải.\n"
            "  5. Đề xuất phương án cân bằng cụ thể cho Giám đốc: tăng ca cục bộ ở đúng công đoạn nút thắt (thay vì tăng ca cả xưởng), gộp lệnh giảm thời gian đổi mã SMED, hoặc gia công ngoài/điều chuyển giữa các nhà máy trong hệ thống CADIVI."
        )
    },
    {
        "id": "q_cap_02",
        "category": "Hoạch Định Năng Lực, Điều Độ & Chi Phí",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Lập lịch theo Chiến dịch (Campaign Scheduling) và Công nghệ Nhóm (Group Technology) giúp tăng năng lực sản xuất thực tế cho nhà máy cáp điện thêm 15–20% mà không tốn tiền đầu tư máy móc như thế nào?",
        "key_points": (
            "• Thực trạng lãng phí điều độ phổ biến:\n"
            "  - Điều độ phát lệnh theo kiểu 'ai giục trước chạy trước' → Máy đùn sáng chạy dây 1.5 Đen, trưa đổi sang 2.5 Trắng, chiều lại đổi sang 1.5 Đỏ → Mỗi ngày mất 2–3 giờ chỉ để tháo khuôn và xả nhựa purging!\n"
            "• Nguyên lý Campaign Scheduling & Group Technology:\n"
            "  1. Nhóm các mã hàng có chung vật liệu nhựa (PVC riêng, XLPE riêng, LSZH riêng), chung đường kính trục vít/bộ khuôn và sắp xếp theo chuỗi màu Sáng → Tối.\n"
            "  2. Cố định 'Bánh xe sản xuất' (Product Wheel) theo chu kỳ tuần (vd: Thứ 2–3 chạy nhóm dây dân dụng tiết diện nhỏ; Thứ 4–5 chạy nhóm tiết diện trung; Thứ 6 chạy nhóm đặc biệt/cáp lực).\n"
            "  3. Kết quả: Thời gian dừng đổi mã giảm 50%, lượng nhựa purge giảm 60%, giải phóng ngay 15–20% thời gian chạy máy thực tế để nhận thêm đơn hàng."
        )
    },
    {
        "id": "q_cap_03",
        "category": "Hoạch Định Năng Lực, Điều Độ & Chi Phí",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Cấu trúc giá thành sản xuất (Manufacturing Cost Breakdown) của một nhà máy dây cáp điện gồm những thành phần nào? Chuyên viên OE có thể tác động mạnh nhất vào những khoản mục chi phí nào?",
        "key_points": (
            "• 3 nhóm cấu thành Giá thành Sản xuất (COGS):\n"
            "  1. Nguyên vật liệu trực tiếp (Direct Material — ~80–88%): Đồng/Nhôm rod (60–75%), hạt nhựa PVC/XLPE/LSZH (15–25%), băng thép/băng quấn/rulo bao bì.\n"
            "  2. Nhân công trực tiếp (Direct Labor — ~4–7%): Lương công nhân đứng máy kéo, bện, đùn, đóng cuộn, tăng ca.\n"
            "  3. Chi phí sản xuất chung (Manufacturing Overhead — ~6–12%): Điện năng vận hành máy & lò ủ/đùn (rất lớn!), khấu hao máy móc, vật tư tiêu hao (khuôn kéo PCD, dầu nhũ tương, lưới lọc), bảo trì.\n"
            "• Thứ tự đòn bẩy giảm chi phí hiệu quả nhất của OE:\n"
            "  - Đòn bẩy #1 (Tác động lớn nhất): Giảm Copper Give-away, giảm nhựa Over-thickness, giảm tỷ lệ phế đồng dính nhựa và phế startup/cut-length.\n"
            "  - Đòn bẩy #2: Giảm chi phí điện năng (kWh/tấn đồng) qua tối ưu chạy đầy tải, giảm thời gian máy đùn bật gia nhiệt chờ không tải (Idle Heating), tối ưu hệ thống khí nén/Chiller.\n"
            "  - Đòn bẩy #3: Tăng OEE (giảm khấu hao phân bổ trên mỗi km cáp) & tăng OLE qua Man-Machine Chart (1 người đứng nhiều máy)."
        )
    },
    {
        "id": "q_cap_04",
        "category": "Hoạch Định Năng Lực, Điều Độ & Chi Phí",
        "type": "Tình Huống Thực Chiến",
        "question": "Làm thế nào để tối ưu mô hình '1 công nhân vận hành nhiều máy' (Multi-Machine Tending) ở khu vực máy kéo sợi hoặc máy bện bằng Biểu đồ Người–Máy (Man-Machine Chart)?",
        "key_points": (
            "• Phương pháp lập Biểu đồ Người–Máy (Man-Machine / Multiple Activity Chart):\n"
            "  1. Đo tách bạch 2 thành phần thời gian cho 1 chu kỳ chạy của 1 máy (vd: máy bện Buncher):\n"
            "     - Thời gian thao tác công nhân bắt buộc (a — nạp rulo, hàn nối, bấm chạy): 8 phút.\n"
            "     - Thời gian công nhân di chuyển & kiểm tra giữa các máy (w): 2 phút.\n"
            "     - Thời gian máy tự chạy độc lập không cần người đứng cạnh (T — máy chạy hết 1 rulo): 32 phút.\n"
            "  2. Tính số máy tối ưu 1 người có thể đứng (N):\n"
            "     - N = (a + T) / (a + w) = (8 + 32) / (8 + 2) = 40 / 10 = 4 máy.\n"
            "  3. Đánh giá giao thoa máy (Machine Interference — xác suất 2 máy dừng cùng lúc): Nếu đứng 4 máy làm thời gian chờ máy tăng cao ở công đoạn điểm nghẽn, chốt phương án tối ưu là **1 công nhân đứng 3 máy** (công nhân bận 75%, có 25% thời gian đệm xử lý sự cố đứt sợi & kiểm tra chất lượng, không để máy phải chờ người!)."
        )
    },
    {
        "id": "q_cap_05",
        "category": "Hoạch Định Năng Lực, Điều Độ & Chi Phí",
        "type": "Tình Huống Thực Chiến",
        "question": "Khu vực sàn giữa công đoạn Kéo đồng, Bện ruột và Đùn bọc luôn chất đầy hàng trăm rulo bán thành phẩm (WIP) chiếm kín lối đi, nhưng máy đùn vẫn thường xuyên phải dừng chờ 'không có đúng mã rulo cần chạy'. Bạn xử lý nghịch lý này thế nào?",
        "key_points": (
            "• Chẩn đoán gốc rễ nghịch lý 'Thừa WIP nhưng vẫn đói hàng':\n"
            "  - Công đoạn Kéo và Bện đang chạy theo hệ thống ĐẨY (Push) — thấy mã nào dễ chạy/lô to thì chạy lấy sản lượng tấn để đạt KPI thưởng ca, tạo ra hàng chục rulo chưa cần dùng ngay trong khi các mã rulo mà máy Đùn sắp cần lại chưa bện kịp.\n"
            "  - Ngoài ra, quản lý vị trí rulo kém (không đánh mã địa chỉ/FIFO) làm xe nâng mất 20 phút đi tìm rulo.\n"
            "• Giải pháp 3 bước của OE:\n"
            "  1. Thiết lập Siêu thị Rulo WIP có giới hạn sức chứa vật lý (CONWIP / Kanban Board) kẻ vạch rõ ràng theo nhóm tiết diện — đầy vạch thì máy trước DỪNG, không cho bện thừa.\n"
            "  2. Chuyển KPI xưởng Kéo/Bện từ 'Tổng tấn sản lượng' sang 'Tỷ lệ hoàn thành đúng lịch kéo của máy Đùn (Schedule Adherence %)'.\n"
            "  3. Gắn thẻ Barcode/QR cố định trên mỗi rulo thép để quét nhập vị trí (Location Tracking), đảm bảo 100% FIFO và tìm rulo dưới 2 phút."
        )
    },
    {
        "id": "q_cap_06",
        "category": "Hoạch Định Năng Lực, Điều Độ & Chi Phí",
        "type": "Tình Huống Thực Chiến",
        "question": "Hóa đơn tiền điện nhà máy tăng 14% trong quý vừa qua dù sản lượng tấn đồng chỉ tăng 5%. Là Chuyên viên OE, bạn phân tích và đề xuất giải pháp tiết kiệm năng lượng (kWh/tấn) như thế nào?",
        "key_points": (
            "• Chỉ số đo lường chuẩn: Cường độ năng lượng **SEC (Specific Energy Consumption = kWh / tấn sản phẩm)** theo từng phân xưởng.\n"
            "• 5 'hố đen' lãng phí điện đặc thù nhà máy cáp điện:\n"
            "  1. Máy đùn bật điện trở gia nhiệt nòng/đầu đùn ở 170–200°C chờ đợi hàng giờ trong lúc chờ rulo hoặc đổi mã (Idle Heating Loss) — tốn điện cực lớn!\n"
            "  2. Lò ủ chuông và bể xông hơi XLPE chạy non tải (mẻ chỉ xếp 50% sức chứa rulo) hoặc gioăng cửa hở thất thoát nhiệt.\n"
            "  3. Rò rỉ khí nén ở các van khớp nối (khí nén là nguồn năng lượng đắt nhất nhà máy; chỉ 1 lỗ rò 3mm tốn hàng trăm triệu tiền điện/năm).\n"
            "  4. Chạy các máy công suất lớn (máy kéo thô RBD, máy đùn lớn) vào giờ CAO ĐIỂM điện lực (giá điện gấp 2.5–3 lần giờ thấp điểm) cho các lệnh không gấp.\n"
            "• Hành động OE: Gắn đồng hồ điện phụ (Sub-meter) cho cụm máy lớn, lập lịch chuyển các mẻ ủ/kéo nặng sang khung giờ thấp điểm ca đêm, kiểm toán rò rỉ khí nén bằng siêu âm và bọc cách nhiệt nòng máy đùn (Insulation Jackets — giảm 15–25% điện gia nhiệt)."
        )
    },
    {
        "id": "q_cap_07",
        "category": "Hoạch Định Năng Lực, Điều Độ & Chi Phí",
        "type": "Phân Tích Sâu",
        "question": "Phòng Kinh doanh liên tục chen 'Đơn hàng gấp' (Rush Order) phá vỡ lịch sản xuất máy đùn giữa chừng, khiến thời gian đổi mã và phế phẩm xả nhựa tăng gấp đôi. Bạn điều phối xử lý xung đột này giữa Kinh doanh và Sản xuất ra sao?",
        "key_points": (
            "• Tư duy hệ thống — không nói 'Không' cứng nhắc mà dùng DỮ LIỆU CHI PHÍ để ra quyết định:\n"
            "  1. Định lượng rõ 'Chi phí phá vỡ lịch' (Cost of Schedule Disruption): Mỗi lần cắt ngang máy đùn mất X phút dừng máy + Y kg nhựa purge + Z đồng công suất bị mất → minh bạch con số này với Kinh doanh và Ban Giám đốc.\n"
            "  2. Phân loại sản phẩm theo mô hình ABC-XYZ (Runner – Repeater – Stranger): Các mã dây bán chạy (Runners) duy trì kho đệm an toàn (MTS) để xuất giao ngay không bao giờ phải phá lịch máy.\n"
            "  3. Thiết lập 'Lịch đóng băng' (Frozen Schedule Window — ví dụ đóng băng 24–48 giờ tới) cho các dây chuyền nút thắt, đồng thời dành sẵn 1 khe thời gian dự phòng (Reserved Rush Slot — khoảng 10% công suất) hoặc 1 dây chuyền linh hoạt SMED chuyên xử lý đơn lẻ gấp."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 14: PHỎNG VẤN HÀNH VI (STAR) & PHẢN BIỆN CV OE
    # =========================================================================
    {
        "id": "q_star_01",
        "category": "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE",
        "type": "Tình Huống Thực Chiến",
        "question": "Hãy giới thiệu bản thân trong 2 phút sao cho đánh trúng trọng tâm vị trí Chuyên viên Tối ưu Quy trình (OE) tại Nhà máy CADIVI Miền Trung?",
        "key_points": (
            "• Công thức 3 phần (Hiện tại → Thành tích định lượng → Liên kết CADIVI):\n"
            "  1. Định vị (25s): 'Em là kỹ sư Cơ khí, hiện là Nhóm trưởng Phòng Kiểm tra tại Mabuchi Motor Đà Nẵng, và trước đó có 2 năm làm Quản lý & Cải tiến Sản xuất tại Fujikura Automotive (ngành dây dẫn ô tô). Điểm giao thoa mạnh nhất của em là bám sát hiện trường xưởng, đo lường bằng Time Study/dữ liệu thực và tự xây công cụ tự động hóa báo cáo.'\n"
            "  2. Thành tích định lượng (60s): Nêu 3 kết quả thật đo được:\n"
            "     - Thực hiện Time Study & cải tiến phương pháp đo Canon INEX giảm 50% thời gian đo (60 → 30 giây/hạng mục), cải tiến đồ gá từ 1 lên 16 mẫu/lượt gá.\n"
            "     - Tự phát triển công cụ Python/VBA/Excel rút thời gian tổng hợp báo cáo khách hàng từ 3–7 ngày xuống 2 giờ/tháng và nhập dữ liệu máy OGP từ 120 phút xuống 15 phút/ngày (giảm 87.5%).\n"
            "     - Tại Fujikura, triển khai quét mã vạch công đoạn RE7 thay sổ tay để truy xuất lỗi, năng suất theo công đoạn và người thao tác.\n"
            "  3. Lý do chọn CADIVI OE (35s): 'Em muốn tập trung toàn thời gian vào bài toán OE tại một nhà máy sản xuất quy mô lớn như CADIVI Miền Trung — nơi em có thể kết hợp nền tảng cơ khí, kinh nghiệm môi trường sản xuất Nhật Bản và khả năng phân tích dữ liệu để tối ưu OEE, OLE, SMED và hao phí BOM đồng/nhựa.'"
        )
    },
    {
        "id": "q_star_02",
        "category": "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE",
        "type": "Tình Huống Thực Chiến",
        "question": "Câu hỏi xoáy CV: 'Bạn đang làm Nhóm trưởng Phòng Kiểm tra (QC) tại Mabuchi Motor, chưa từng trực tiếp vận hành nhà máy dây cáp điện. Điều gì đảm bảo bạn sẽ làm tốt vị trí Chuyên viên Tối ưu Quy trình (OE) tại CADIVI?'",
        "key_points": (
            "• Cách hóa giải điểm nghi ngại thành lợi thế cạnh tranh:\n"
            "  1. Khẳng định điểm chung cốt lõi: 'OE không phải là công việc đứng máy thay thợ vận hành, mà là năng lực phương pháp luận — đo thời gian (Time Study), phân tích dữ liệu (OEE/OLE/SPC/BOM), nhận diện lãng phí, cải tiến đồ gá/thao tác và chuẩn hóa quy trình. Những kỹ năng này em đã trực tiếp làm và ra số liệu thực tế nhiều năm.'\n"
            "  2. Liên kết kinh nghiệm ngành dây dẫn & đo kiểm: 'Trước Mabuchi, em từng làm Cải tiến Sản xuất 2 năm tại Fujikura Automotive chuyên về dây dẫn điện, rất quen với việc thống kê sản lượng, tỷ lệ lỗi theo công đoạn/mã hàng và số hóa dữ liệu xưởng bằng barcode. Ngoài ra, kinh nghiệm đo kiểm chính xác (OGP, Canon INEX, Keyence) giúp em đọc hiểu nhanh dữ liệu phòng Lab cáp điện (độ dày cách điện, lệch tâm, điện trở) để tối ưu dung sai nhựa/đồng.'\n"
            "  3. Cam kết học nhanh công nghệ cáp: 'Em đã chủ động tìm hiểu chuỗi công nghệ Kéo–Ủ–Bện–Đùn PVC/XLPE–Spark Test của CADIVI và cam kết trong 2 tuần đầu bám sát hiện trường Genba để nắm vững đặc thù từng dây chuyền.'"
        )
    },
    {
        "id": "q_star_03",
        "category": "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE",
        "type": "Tình Huống Thực Chiến",
        "question": "Câu hỏi kiểm tra độ trung thực số liệu CV: 'Trong CV bạn ghi cải tiến bệ đo từ 1 lên 16 mẫu/lượt gá và rút thời gian đo Canon INEX từ 60 xuống 30 giây. Vậy có phải năng suất tăng 16 lần hoặc giảm 50% số người không?'",
        "key_points": (
            "• Điểm cộng CỰC LỚN khi trả lời chính xác, khiêm tốn và đúng chuẩn tư duy kỹ sư OE:\n"
            "  - Trả lời dứt khoát: 'KHÔNG ạ! Em luôn tách bạch rất rõ hai con số để không báo cáo ảo:'\n"
            "  1. 'Tăng từ 1 lên 16 mẫu/lượt gá là TĂNG SỨC CHỨA MỖI LẦN GÁ (Batch Fixture Capacity), giúp cắt giảm thao tác gá đặt lặp đi lặp lại, thời gian chạy về gốc và thời gian chờ người thao tác — KHÔNG suy diễn thành tăng năng suất 16 lần vì máy vẫn cần thời gian quét đo từng mẫu.'\n"
            "  2. 'Rút từ 60 xuống 30 giây/hạng mục là giảm 50% thời gian đo trên hạng mục đó; còn tổng số giờ công hay số người tiết kiệm thực tế phải tính theo tổng khối lượng đo, thời gian chuẩn bị mẫu, báo cáo và các hạng mục đo khác.'\n"
            "  → Câu trả lời này chứng minh tư duy số liệu sắc bén, trung thực tuyệt đối — phẩm chất quan trọng nhất của người làm OE!"
        )
    },
    {
        "id": "q_star_04",
        "category": "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE",
        "type": "Tình Huống Thực Chiến",
        "question": "Hãy chia sẻ cách bạn đã dùng Python, VBA và Excel/Access để tự động hóa dữ liệu sản xuất/đo kiểm, và bạn thấy kỹ năng này sẽ giải quyết bài toán cụ thể nào ngay tại CADIVI Miền Trung?",
        "key_points": (
            "• Trả lời theo mô hình STAR:\n"
            "  - Situation/Task: Việc tổng hợp dữ liệu từ máy đo OGP mất 120 phút/ngày và tổng hợp báo cáo gửi khách hàng định kỳ mất 3–7 ngày/tháng do thao tác copy-paste thủ công dễ sai sót.\n"
            "  - Action: Tự viết tool bằng Python/VBA chuẩn hóa cấu trúc file xuất thô, tự động kiểm tra bất thường dữ liệu, tính chỉ số và xuất báo cáo chuẩn.\n"
            "  - Result: Giảm nhập liệu OGP từ 120 xuống 15 phút/ngày (-87.5%), báo cáo tháng xuống còn 2 giờ, sai số nhập tay về 0.\n"
            "• Ứng dụng ngay vào JD CADIVI (35C8613F):\n"
            "  - Gom tự động file báo cáo ca từ nhiều tổ Kéo/Bện/Đùn để tính tức thì OEE (theo mét/phút), OLE, Pareto nguyên nhân dừng máy và chênh lệch BOM vật tư đồng/nhựa mỗi sáng thay vì chờ cuối tháng mới biết lỗ ở đâu."
        )
    },
    {
        "id": "q_star_05",
        "category": "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE",
        "type": "Tình Huống Thực Chiến",
        "question": "Tình huống xung đột hiện trường: Bạn là người mới vào CADIVI, khi bạn đề xuất thay đổi quy trình đổi mã máy đùn (SMED), một Quản đốc phân xưởng 20 năm kinh nghiệm gạt phắt đi: 'Cậu mới vào biết gì về máy đùn cáp mà đòi chỉ tôi? Xưa giờ chạy vậy vẫn ra hàng!'. Bạn ứng xử thế nào?",
        "key_points": (
            "• Nghệ thuật Quản trị Thay đổi (Change Management) & Tôn trọng Genba:\n"
            "  1. Tuyệt đối KHÔNG tranh cãi lý thuyết hay dùng quyền Ban Giám đốc ép xuống.\n"
            "  2. Hạ cái tôi, công nhận chuyên môn thực chiến của anh Quản đốc: 'Anh có 20 năm kinh nghiệm chạy máy đùn, chắc chắn anh hiểu máy hơn em gấp nhiều lần. Em không xuống đây để chỉ lại cách chạy máy, mà em xuống để đo xem đoạn nào anh em thợ đang vất vả nhất để em hỗ trợ gỡ khó.'\n"
            "  3. Bắt đầu từ 'Nỗi đau của chính họ' (Quick Win): Hỏi xem tổ đang bực nhất chuyện gì (ví dụ: mỗi lần đổi khuôn phải đi tìm cờ lê, nâng khuôn nặng mỏi lưng, hay chờ kho cấp nhựa lâu) → làm cải tiến giúp họ NHẸ VIỆC hơn trước.\n"
            "  4. Dùng bằng chứng thực tế trên 1 máy mẫu (Pilot Line) cùng anh Quản đốc đứng tên đồng tác giả dự án. Khi thấy kết quả giảm mệt mỏi và tăng thưởng năng suất cho tổ, anh ấy sẽ trở thành đồng minh mạnh nhất."
        )
    },
    {
        "id": "q_star_06",
        "category": "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE",
        "type": "Tình Huống Thực Chiến",
        "question": "Nếu phát hiện số liệu ghi chép dừng máy hoặc sản lượng trong sổ ca của phân xưởng bị 'làm đẹp' (ví dụ: giấu thời gian hỏng máy vào mục 'chờ kế hoạch' để báo cáo OEE cao hơn thực tế), bạn xử lý thế nào?",
        "key_points": (
            "• Nguyên tắc vàng của OE: 'Dữ liệu sai dẫn tới quyết định sai' — nhưng phải xử lý khéo léo để không gây thù địch:\n"
            "  1. Xác minh chéo khách quan trước khi kết luận: Đối chiếu đồng hồ đếm mét trên máy/PLC, sản lượng nhập kho thực tế, phiếu cân phế liệu và tiêu thụ điện/vật tư.\n"
            "  2. Tìm hiểu động cơ đằng sau việc làm đẹp số liệu: Thường do KPI phạt nặng khi OEE thấp nên tổ trưởng sợ bị trừ thưởng mới che giấu lỗi!\n"
            "  3. Báo cáo trung thực & Đề xuất giải pháp hệ thống: Làm việc riêng với Quản đốc trước trên tinh thần 'tìm tổn thất để gỡ khó, không tìm lỗi để phạt'; thống nhất lại bảng định nghĩa mã dừng máy (Downtime Reason Code) rõ ràng, và đề xuất dần chuyển sang ghi nhận tự động qua cảm biến/barcode/MES để dữ liệu minh bạch khách quan."
        )
    },
    {
        "id": "q_star_07",
        "category": "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE",
        "type": "Tình Huống Thực Chiến",
        "question": "Kể về một dự án cải tiến bạn từng đề xuất nhưng thất bại hoặc gặp phản kháng mạnh. Bạn đã rút ra bài học gì?",
        "key_points": (
            "• Cách trả lời STAR trưởng thành (tránh câu sáo rỗng 'em chưa từng thất bại'):\n"
            "  - Chọn 1 tình huống thật (ví dụ: thiết kế biểu mẫu ghi nhận dữ liệu hoặc công cụ tự động mới quá chi tiết nhiều cột nhập liệu khiến công nhân dưới chuyền thấy rườm rà và bỏ không ghi, hoặc thử nghiệm đồ gá phiên bản 1 bị vướng thao tác tay).\n"
            "  - Bài học rút ra: (1) Mọi giải pháp OE phải được đồng thiết kế cùng người trực tiếp thao tác (Co-design tại Genba), (2) Quy tắc 'Đơn giản hóa trước khi số hóa' — thao tác càng ít chạm (như quét 1 phát barcode thay vì gõ 5 ô) thì tỷ lệ tuân thủ mới đạt 100%, (3) Luôn chạy thử Pilot quy mô nhỏ, nhận phản hồi chỉnh sửa nhanh rồi mới nhân rộng."
        )
    },
    {
        "id": "q_star_08",
        "category": "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE",
        "type": "Tình Huống Thực Chiến",
        "question": "Nếu nhận việc Chuyên viên OE tại Nhà máy CADIVI Miền Trung, hãy trình bày cụ thể Kế hoạch hành động 30 – 60 – 90 ngày đầu tiên của bạn?",
        "key_points": (
            "• Kế hoạch 30–60–90 ngày sắc nét, thực tế:\n"
            "  - 30 Ngày đầu (Học & Chuẩn hóa Dữ liệu): Bám Genba đủ 4 khu vực Kéo – Bện – Đùn – Lab/Đóng gói; học quy trình, BOM, tiêu chuẩn TCVN/IEC và hệ thống báo cáo hiện hành; rà soát độ tin cậy số liệu OEE/OLE/Downtime/Scrap; tạo quan hệ tin cậy với Quản đốc, Tổ trưởng, Bảo trì và QC.\n"
            "  - 60 Ngày (Phân tích & Chạy Pilot Quick-Win): Chuẩn hóa template/Dashboard tự động theo dõi OEE (m/phút), OLE và Pareto tổn thất/hao phí BOM bằng Excel Power Query/Power BI/Python; chọn đúng 1 dây chuyền điểm nghẽn (ví dụ 1 máy đùn chủ lực) để triển khai dự án Pilot đầu tiên (SMED đổi màu hoặc giảm phế startup/over-thickness) có đo lường Trước–Sau.\n"
            "  - 90 Ngày (Chứng minh ROI & Chuẩn hóa Nhân rộng): Báo cáo tổng kết hiệu quả kinh tế Trước–Sau có kiểm định thống kê cho Ban Giám đốc; khóa thành SOP/OPL đào tạo tổ sản xuất; lập danh mục lộ trình dự án Kaizen 6 tháng tiếp theo cho toàn nhà máy."
        )
    },
    {
        "id": "q_star_09",
        "category": "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE",
        "type": "Phân Tích Sâu",
        "question": "Khi bạn từng tham gia thẩm định hiệu quả đầu tư thiết bị (ví dụ dự án ~1.2 tỷ VNĐ), hội đồng hỏi: 'Làm sao bạn chắc chắn con số tiết kiệm hàng tháng là chính xác và không bị phòng ban khác phản bác?'",
        "key_points": (
            "• Cách trả lời thể hiện bản lĩnh tài chính & kiểm soát rủi ro:\n"
            "  1. Nguồn số liệu có ký xác nhận chéo (Cross-functional Sign-off): Thời gian đo kiểm lấy từ Time Study thực tế; sản lượng lấy từ phòng Kế hoạch; đơn giá nhân công/vật tư/điện năng lấy từ phòng Kế toán — không tự ước lượng một mình.\n"
            "  2. Tách rõ tiết kiệm ròng thực (Net Realized Savings) sau khi trừ chi phí khấu hao, điện năng, bảo trì và thời gian học việc (Ramp-up).\n"
            "  3. Thực hiện chạy kiểm chứng thực tế sau đầu tư 3 tháng (Post-Implementation Audit) so sánh Actual vs Plan để chứng minh độ tin cậy."
        )
    },
    {
        "id": "q_star_10",
        "category": "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE",
        "type": "Tình Huống Thực Chiến",
        "question": "Trong công việc OE, bạn cùng lúc nhận 5 yêu cầu gấp: Giám đốc hỏi báo cáo BOM tháng, xưởng đùn báo máy giảm tốc độ, tổ đóng gói thiếu người, phòng kế hoạch cần tính lại năng lực và sắp có đợt audit 5S. Bạn sắp xếp thứ tự ưu tiên thế nào?",
        "key_points": (
            "• Áp dụng Ma trận Eisenhower kết hợp Tác động Giá trị (Impact vs Effort) & Thứ tự SQDC:\n"
            "  1. Safety & Dừng chuyền nghiêm trọng trước: Kiểm tra nhanh sự cố máy đùn giảm tốc độ (ảnh hưởng trực tiếp sản lượng & chất lượng ngay trong ca — phối hợp kỹ thuật/bảo trì khoanh vùng trong 30 phút).\n"
            "  2. Hạn chót lãnh đạo (Deadline cứng): Hoàn tất báo cáo BOM & tính năng lực (tận dụng hệ thống template/script tự động để xuất số nhanh, chính xác).\n"
            "  3. Điều phối ngắn hạn: Hỗ trợ tổ trưởng đóng gói cân bằng tải tạm thời theo Ma trận kỹ năng đa năng.\n"
            "  4. Lập kế hoạch dài hơi: Đưa chuẩn bị Audit 5S vào lịch checklist phân công cụ thể cho các tổ trưởng thực hiện đồng bộ, không ôm đồm làm thay xưởng."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 15: CÂU HỎI CHIẾN LƯỢC HỎI NGƯỢC NHÀ TUYỂN DỤNG CADIVI
    # =========================================================================
    {
        "id": "q_rev_01",
        "category": "Câu Hỏi Hỏi Ngược Nhà Tuyển Dụng CADIVI",
        "type": "Phân Tích Sâu",
        "question": "[Hỏi Giám đốc Nhà máy / Trưởng phòng OE] 'Trong 6 đến 12 tháng tới, đâu là chỉ số hoặc nút thắt lớn nhất mà Nhà máy CADIVI Miền Trung kỳ vọng vị trí Chuyên viên OE này tập trung giải quyết đầu tiên?'",
        "key_points": (
            "• Tại sao câu hỏi này cực kỳ ghi điểm:\n"
            "  - Cho thấy bạn có tư duy định hướng kết quả (Result-oriented), không làm cải tiến lan man mà muốn bám sát ưu tiên chiến lược của nhà máy.\n"
            "  - Giúp bạn biết ngay 'nỗi đau thật' của CADIVI Miền Trung hiện tại là OEE máy đùn/kéo, hao phí đồng/nhựa, thời gian chuyển đổi SMED hay năng suất đóng gói — để bạn điều chỉnh kế hoạch 90 ngày chuẩn xác ngay khi nhận việc."
        )
    },
    {
        "id": "q_rev_02",
        "category": "Câu Hỏi Hỏi Ngược Nhà Tuyển Dụng CADIVI",
        "type": "Phân Tích Sâu",
        "question": "[Hỏi về hệ thống dữ liệu] 'Hiện tại nhà máy mình đang thu thập dữ liệu sản lượng, dừng máy OEE và hao phí vật tư BOM hoàn toàn tự động qua ERP/MES hay vẫn đang kết hợp ghi chép nhật ký ca và Excel ạ?'",
        "key_points": (
            "• Tại sao câu hỏi này ghi điểm:\n"
            "  - Thể hiện sự am hiểu thực tế vận hành nhà máy tại Việt Nam (không ảo tưởng mọi thứ đã 4.0 hoàn hảo).\n"
            "  - Nếu nhà máy vẫn đang dùng nhiều file Excel/sổ ca rời rạc → đây là cơ hội vàng để bạn nhấn mạnh lại thế mạnh Python/VBA/Power Query/Power BI giúp tự động hóa ngay trong tháng đầu tiên!"
        )
    },
    {
        "id": "q_rev_03",
        "category": "Câu Hỏi Hỏi Ngược Nhà Tuyển Dụng CADIVI",
        "type": "Phân Tích Sâu",
        "question": "[Hỏi về cơ chế phối hợp] 'Tại CADIVI Miền Trung, Chuyên viên OE nằm trong cơ cấu trực thuộc Ban Giám đốc nhà máy hay phòng Kỹ thuật/Kế hoạch, và cơ chế phối hợp với Quản đốc phân xưởng cùng đội OE của Tổng công ty diễn ra như thế nào ạ?'",
        "key_points": (
            "• Tại sao câu hỏi này ghi điểm:\n"
            "  - Chứng tỏ bạn hiểu rõ đặc thù làm OE: hiệu quả của cải tiến phụ thuộc rất lớn vào cơ chế bảo trợ của lãnh đạo (Management Sponsorship) và sự phối hợp liên phòng ban.\n"
            "  - Giúp bạn hiểu rõ quyền hạn thực thi, lộ trình báo cáo và cách tương tác giữa Nhà máy Miền Trung với khối OE Tổng công ty CADIVI."
        )
    },
    {
        "id": "q_rev_04",
        "category": "Câu Hỏi Hỏi Ngược Nhà Tuyển Dụng CADIVI",
        "type": "Phân Tích Sâu",
        "question": "[Hỏi về văn hóa cải tiến] 'Phong trào 5S và Kaizen tại các phân xưởng hiện đang ở giai đoạn nào (mới khởi động, đã có bảng đánh giá định kỳ hay đã gắn với cơ chế thưởng thi đua), và khó khăn lớn nhất khi duy trì là gì ạ?'",
        "key_points": (
            "• Tại sao câu hỏi này ghi điểm:\n"
            "  - Thể hiện bạn thực sự có kinh nghiệm triển khai Lean/5S tại nhà máy (biết rằng 'làm 5S ban đầu thì dễ, duy trì bền vững S4-S5 mới khó').\n"
            "  - Giúp bạn đánh giá độ trưởng thành văn hóa Lean tại nhà máy trước khi quyết định nhận offer."
        )
    },
    {
        "id": "q_rev_05",
        "category": "Câu Hỏi Hỏi Ngược Nhà Tuyển Dụng CADIVI",
        "type": "Phân Tích Sâu",
        "question": "[Hỏi về tiêu chí thành công thử việc] 'Sau 2 tháng thử việc, những kết quả cụ thể nào sẽ khiến anh/chị đánh giá rằng việc tuyển dụng em vào vị trí Chuyên viên OE này là một quyết định hoàn toàn đúng đắn?'",
        "key_points": (
            "• Tại sao câu hỏi này ghi điểm tuyệt đối cuối buổi phỏng vấn:\n"
            "  - Khẳng định sự tự tin, cam kết minh bạch bằng KPI cụ thể và tinh thần chịu trách nhiệm cao.\n"
            "  - Khi người phỏng vấn trả lời câu này, họ đang vô thức hình dung bạn đã là nhân viên chính thức trong đội ngũ của họ!"
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 16: KẾ HOẠCH S&OP/MRP/CRP, FPY/RTY, AN TOÀN LOTO/ISO & STANDARD COST
    # =========================================================================
    {
        "id": "q_plan_01",
        "category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Trình bày chuỗi phân tầng hoạch định sản xuất [[S&OP]] → [[MPS]] → [[MRP]] → [[RCCP]] → [[CRP]] và vai trò phối hợp của Chuyên viên [[OE]] trong chuỗi này?",
        "key_points": (
            "• 5 tầng hoạch định chuẩn quốc tế (APICS):\n"
            "  1. [[S&OP]] (3–18 tháng): Cân đối dự báo bán hàng tổng thể (theo tấn đồng/họ cáp) với tổng công suất nhà máy.\n"
            "  2. [[MPS]] (4–12 tuần): Lịch sản xuất tổng thể theo từng mã cáp SKU và tuần giao hàng.\n"
            "  3. [[RCCP]]: Kiểm tra nhanh xem MPS có vượt năng lực các công đoạn nút thắt (như máy đùn) không.\n"
            "  4. [[MRP]]: Bùng nổ cây [[BOM]] để tính chính xác ngày đặt/nhập đồng rod, nhôm rod, hạt PVC/XLPE, rulo gỗ.\n"
            "  5. [[CRP]]: Kiểm tra tải chi tiết từng máy cụ thể theo từng ca để điều độ phát lệnh sản xuất.\n"
            "• Vai trò của OE: Cung cấp dữ liệu đầu vào CHUẨN XÁC (OEE lịch sử, tốc độ m/phút thực tế, thời gian đổi mã SMED, định mức MBOM đúng hệ số xoắn) để toàn bộ chuỗi kế hoạch không bị 'ảo trên giấy'."
        )
    },
    {
        "id": "q_plan_02",
        "category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Sự khác biệt giữa [[FPY]] (First Pass Yield) và [[RTY]] (Rolled Throughput Yield)? Vì sao báo cáo từng công đoạn đều đạt 96–98% nhưng nhà máy vẫn đối mặt 'Nhà máy ẩn' (Hidden Factory) gây đội chi phí?",
        "key_points": (
            "• Phân biệt rõ:\n"
            "  - [[FPY]]: Tỷ lệ đạt ngay lần đầu tại 1 công đoạn riêng lẻ (chưa tính hàng sửa lại [[Rework]]).\n"
            "  - [[RTY]]: Tích nhân xác suất FPY của toàn chuỗi công đoạn nối tiếp (RTY = FPY_1 × FPY_2 × ... × FPY_n).\n"
            "• Ví dụ nhà máy cáp qua 6 công đoạn (Kéo 98% × Ủ 99% × Bện 97% × Đùn XLPE 95% × Ghép lõi 96% × Đùn vỏ 97%):\n"
            "  - RTY chỉ đạt 83.27% — nghĩa là gần 17% dòng sản xuất đã phải dừng cắt nối, sang cuộn lại hoặc hủy phế (Hidden Factory) mà chỉ số kiểm tra cuối chuyền thường che khuất!\n"
            "• Hành động OE: Luôn đo và báo cáo RTY thay vì chỉ nhìn Final Yield để ép cải tiến chất lượng ngay tại nguồn."
        )
    },
    {
        "id": "q_plan_03",
        "category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành",
        "type": "Tình Huống Thực Chiến",
        "question": "Cuối tháng phòng Kế toán báo giá thành sản xuất thực tế của xưởng vượt [[Standard Cost|giá thành định mức]] +7.5% và quy trách nhiệm cho phân xưởng. Là Chuyên viên [[OE]], bạn phân tách biến động này như thế nào để bảo vệ tính công bằng và chỉ đúng điểm cần sửa?",
        "key_points": (
            "• Phân tách chuẩn kế toán quản trị thành 3 thành phần rõ ràng:\n"
            "  1. Price Variance (Biến động giá mua NVL): Do giá đồng LME/hạt nhựa thế giới tăng → Thuộc biến động thị trường / Mua hàng, XƯỞNG KHÔNG CHỊU LỖI.\n"
            "  2. Usage / Efficiency Variance (Biến động định mức & năng suất): Do xưởng kéo dư đồng ([[Copper Give-away]]), bọc dư nhựa ([[Over-thickness]]), phế [[Spark Tester]] hoặc tốn giờ công tăng ca → TRÁCH NHIỆM TRỰC TIẾP CỦA XƯỞNG & OE.\n"
            "  3. Overhead Absorption Variance (Hấp thụ định phí): Khi sản lượng thực tế thấp hơn kế hoạch (do thiếu đơn hoặc [[OEE]] tụt), chi phí khấu hao & quản lý cố định phân bổ trên mỗi km cáp tăng vọt.\n"
            "• Giá trị OE: Minh bạch 3 cột này giúp Ban Giám đốc xử đúng người đúng việc và tập trung hành động vào đúng Usage Variance."
        )
    },
    {
        "id": "q_plan_04",
        "category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành",
        "type": "Tình Huống Thực Chiến",
        "question": "Khi triển khai dự án [[SMED]] 2 người phối hợp song song đổi khuôn [[Crosshead]] trên máy đùn 180°C và máy bện lồng cứng, bạn đảm bảo quy trình an toàn [[LOTO]] và [[EHS]] như thế nào để tuyệt đối không xảy ra tai nạn lao động?",
        "key_points": (
            "• Nguyên tắc bất di bất dịch: 'Nhanh nhưng KHÔNG BAO GIỜ đánh đổi An toàn' (Safety First trong [[KPI|SQDC]]).\n"
            "• 6 bước [[LOTO]] bắt buộc trong SOP SMED:\n"
            "  1. Dừng máy chuẩn và cắt cầu dao nguồn chính / khóa van khí nén.\n"
            "  2. CẢ 2 kỹ thuật viên đều gắn ổ khóa cá nhân + thẻ tên lên kẹp khóa đa điểm (Hasp) — chỉ khi cả 2 cùng ra khỏi vùng nguy hiểm và tự mở khóa của mình mới cấp điện lại được.\n"
            "  3. Thử bấm Start (Try-out) xác nhận trạng thái Zero Energy.\n"
            "  4. Trang bị PPE chịu nhiệt (găng tay chống bỏng 250°C, kính bảo hộ) khi tháo đầu đùn nóng và tuân thủ tải trọng móc cẩu rulo theo chuẩn [[ISO 45001]]."
        )
    },
    {
        "id": "q_plan_05",
        "category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành",
        "type": "Khái Niệm Cốt Lõi",
        "question": "So sánh đặc thù sản xuất giữa cáp ruột đồng và cáp ruột nhôm ([[ACSR]], [[ABC Cable|cáp nhôm ABC]]) tại Nhà máy CADIVI Miền Trung? Chuyên viên OE cần chú ý những rủi ro nào khi tối ưu dây chuyền nhôm?",
        "key_points": (
            "• 4 khác biệt kỹ thuật & vận hành sống còn:\n"
            "  1. Cơ tính & lực kéo đứt: Nhôm mềm và bền kéo thấp hơn đồng nhiều → Cực nhạy với lực căng (Tension) ở bộ [[Pay-off]] / [[Dancer]] / [[Capstan]]; dễ bị kéo giãn làm nhỏ tiết diện (tăng điện trở) hoặc đứt sợi.\n"
            "  2. Khối lượng riêng & Độ dẫn điện: Nhôm nhẹ (2.703 g/cm³ vs đồng 8.89 g/cm³) và độ dẫn ~61% [[IACS]] (đồng ≥ 100% [[IACS]]) → Để dẫn cùng dòng điện, tiết diện cáp nhôm phải lớn hơn cáp đồng.\n"
            "  3. Cách ly hoàn toàn bể dầu & máy móc: Nhôm tạo lớp oxit cứng gây mòn khuôn [[PCD]] nhanh và TUYỆT ĐỐI không dùng chung bể [[Drawing Emulsion]] hay lẫn mạt phế liệu với đồng (nhiễm tạp làm hỏng chất lượng phế thu hồi!).\n"
            "  4. Cáp [[ACSR]] (lõi thép chịu lực) & [[ABC Cable|cáp ABC]] (vặn xoắn treo ngoài trời vỏ XLPE đen chống UV) có tốc độ chuẩn & bước xoắn riêng biệt khi lập BOM và tính OEE."
        )
    },
    {
        "id": "q_plan_06",
        "category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Kết hợp phân loại [[ABC-XYZ]] (Runner – Repeater – Stranger) với công thức [[Safety Stock]] & [[ROP]] như thế nào để vừa không bao giờ thiếu vật tư dừng máy, vừa không ôm tồn kho dư thừa?",
        "key_points": (
            "• Chiến lược theo 2 trục Giá trị (A–B–C) × Độ ổn định nhu cầu (X–Y–Z):\n"
            "  - Nhóm AX (Runners — Dây dân dụng bán chạy & đồng rod, PVC chuẩn): Nhu cầu ổn định → Áp dụng Make-to-Stock + [[Safety Stock]] thấp + đặt hàng tự động theo [[ROP]] & [[Kanban]].\n"
            "  - Nhóm AZ/BZ (Strangers — Cáp dự án [[Mica FR]], cáp lực cỡ lớn 300mm²): Nhu cầu thất thường → Áp dụng Make-to-Order (không trữ tồn kho thành phẩm!), dồn nguồn lực vào [[SMED]] & rút [[Lead Time]].\n"
            "• Công thức chuẩn: Safety Stock = Z × σ_demand × sqrt(Lead Time); ROP = (Nhu cầu TB/ngày × Lead Time) + Safety Stock."
        )
    },
    {
        "id": "q_plan_07",
        "category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Phân biệt vai trò của 4 bộ tiêu chuẩn hệ thống quản lý tại nhà máy hiện đại: [[ISO 9001]], [[ISO 14001]], [[ISO 45001]] và [[ISO 50001]] đối với công việc hàng ngày của Chuyên viên OE?",
        "key_points": (
            "• Liên kết trực tiếp OE với 4 hệ thống ISO:\n"
            "  1. [[ISO 9001]] (Chất lượng): OE chuẩn hóa [[SOP]], [[Control Plan]], kiểm định đo lường [[Gage R&R]] và duy trì bằng chứng cải tiến liên tục.\n"
            "  2. [[ISO 14001]] (Môi trường): Giảm rác thải nhựa [[Purging]], giảm tiêu hao [[Drawing Emulsion]] thải và kiểm soát khí/bụi khu đùn.\n"
            "  3. [[ISO 45001]] (An toàn [[EHS]]): Tích hợp [[LOTO]] vào mọi quy trình [[SMED]], cải thiện [[Ergonomics]] & hành lang cầu trục/xe nâng.\n"
            "  4. [[ISO 50001]] (Năng lượng): Thiết lập đường cơ sở [[SEC|kWh/tấn]], lắp biến tần [[VFD]], bọc cách nhiệt nòng đùn và tối ưu lịch chạy giờ thấp điểm."
        )
    },
    {
        "id": "q_plan_08",
        "category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Kể tên đủ [[7 QC Tools|7 Công cụ QC cổ điển]] và cho biết công cụ nào dùng để chứng minh mối quan hệ nhân–quả giữa nhiệt độ nước [[Cooling Trough]] và tỷ lệ lỗi bề mặt vỏ cáp?",
        "key_points": (
            "• 7 Công cụ QC cổ điển: (1) Check Sheet, (2) [[Histogram]], (3) [[Pareto]], (4) [[Ishikawa]] (Xương cá), (5) [[Scatter]] (Biểu đồ phân tán), (6) [[SPC]] Control Chart, (7) Stratification (Phân tầng).\n"
            "• Công cụ kiểm tra tương quan 2 biến liên tục (Nhiệt độ nước làm mát vs Tỷ lệ lỗi/Độ nhám):\n"
            "  - Dùng **Biểu đồ phân tán [[Scatter]]** kết hợp tính hệ số tương quan r và chạy **Hồi quy [[Regression]]** (kiểm tra R² và p-value < 0.05) trên [[Minitab]] để định lượng chính xác mức tăng nhiệt gây tăng lỗi bao nhiêu %."
        )
    },
    {
        "id": "q_plan_09",
        "category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành",
        "type": "Phân Tích Sâu",
        "question": "Kỹ thuật [[Masterbatch]] (cấp hạt màu trực tiếp tại cổ phễu đùn) giúp giải quyết đồng thời bài toán tồn kho nhựa và thời gian đổi màu [[SMED]] như thế nào so với mua hạt nhựa PVC đã pha sẵn màu?",
        "key_points": (
            "• Hạn chế của hạt nhựa pha sẵn màu: Phải trữ tồn kho riêng 8–10 mã bao nhựa cho 8–10 màu khác nhau (tăng vốn tồn kho, dễ dư màu hiếm hết hạn) và mỗi lần đổi màu phải hút cạn toàn bộ phễu lớn.\n"
            "• Ưu điểm của [[Masterbatch]] (Hạt nền PVC tự nhiên/không màu + Bộ định lượng hạt màu đậm đặc 1–3% gắn ngay cổ họng máy đùn):\n"
            "  1. Cắt giảm 60–70% số mã tồn kho nhựa nền (chỉ cần trữ 1 loại PVC nền tự nhiên với khối lượng lớn, mua giá tốt hơn!).\n"
            "  2. Đổi màu cực nhanh: chỉ cần đổi phễu định lượng nhỏ chứa 2–5% hạt màu, giảm mạnh nhựa xả [[Purging]] và rút ngắn thời gian [[SMED]]."
        )
    },
    {
        "id": "q_plan_10",
        "category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành",
        "type": "Phân Tích Sâu",
        "question": "Khi nào cần dùng thử nghiệm [[Partial Discharge|phóng điện cục bộ (PD)]] và thử nghiệm [[Water Immersion|cao áp ngâm nước]]? Nếu lô cáp trung thế XLPE không đạt chuẩn PD (vượt 5 pC), nguyên nhân gốc thường nằm ở đâu trên dây chuyền?",
        "key_points": (
            "• Phân biệt 2 phép thử Lab:\n"
            "  - [[Water Immersion]]: Dùng phổ biến cho dây dân dụng & cáp hạ thế (ngâm cuộn cáp trong bể nước thử cao áp chịu đựng phát hiện thủng cách điện).\n"
            "  - [[Partial Discharge|PD Test]]: Bắt buộc cho cáp trung thế/cao thế XLPE (6–35 kV) trong phòng chắn nhiễu để đo phóng điện vi mô bên trong lớp cách điện.\n"
            "• Nguyên nhân gốc gây rớt PD: Bọt khí siêu nhỏ (Micro-voids) trong lớp XLPE do hạt nhựa nhiễm ẩm/bụi, độ bám dính kém hoặc gợn nhấp nhô tại mặt tiếp giáp lớp bán dẫn trong/ngoài trên dây chuyền [[CCV]], hoặc lưới lọc [[Screen Pack]] bị rách lọt tạp chất."
        )
    },
    {
        "id": "q_plan_11",
        "category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Giải thích quy trình [[Hoshin Kanri]] (Triển khai chiến lược theo chính sách) & cơ chế Catchball, cùng mô hình [[ADKAR]] trong quản trị thay đổi tại nhà máy sản xuất?",
        "key_points": (
            "• [[Hoshin Kanri]] & Catchball:\n"
            "  - Là phương pháp kết nối mục tiêu chiến lược 1–3 năm của Ban Lãnh đạo Tổng công ty thành các dự án OE cụ thể và KPI hàng ngày ở từng tổ máy (bảng X-Matrix).\n"
            "  - Catchball (Tung–Hứng bóng): Thay vì áp đặt chỉ tiêu một chiều, lãnh đạo và Quản đốc/OE trao đổi qua lại về tính khả thi, nguồn lực và lộ trình để mọi cấp cùng đồng thuận cam kết.\n"
            "• Mô hình [[ADKAR]] (5 bước dẫn dắt con người chấp nhận cải tiến mới):\n"
            "  - Awareness (Hiểu lý do cần đổi) → Desire (Muốn thay đổi nhờ Quick-Win) → Knowledge (Được đào tạo [[TWI]]/[[SOP]]) → Ability (Thực hành thành thạo) → Reinforcement (Duy trì bền vững qua Audit & thưởng)."
        )
    },
    {
        "id": "q_plan_12",
        "category": "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành",
        "type": "Tình Huống Thực Chiến",
        "question": "Cáp chống cháy [[Mica FR]] đang có tỷ lệ dừng máy quấn băng Mica cao (đứt băng 8 lần/ca) và phế phẩm tăng. Bạn tiếp cận phân tích và chuẩn hóa lại công đoạn này theo tư duy [[OE]] ra sao?",
        "key_points": (
            "• Phân tích hiện trường Genba tại máy quấn băng Mica:\n"
            "  1. Kiểm tra lực căng đầu quấn (Taping Head Tension) & độ đồng tâm trục cuộn băng: lực căng không đều hoặc phanh hãm rít làm băng Mica giòn bị xé rách khi máy tăng tốc.\n"
            "  2. Kiểm tra góc quấn & độ chồng mí (Overlap ≥ 50% theo chuẩn chống cháy IEC 60331) cùng bề mặt ruột đồng (gai đồng đứt sẽ rạch rách băng ngay lập tức!).\n"
            "  3. Lắp cảm biến đứt băng [[Poka-Yoke]] dừng máy trong 0.5s, chuẩn hóa bảo quản cuộn băng Mica chống ẩm và lập [[Control Plan]] + bảng tốc độ chuẩn cho từng tiết diện cáp FR."
        )
    },

    # =========================================================================
    # CHỦ ĐỀ 17: ĐÙN CÁP CHUYÊN SÂU, ĐỨT SỢI, THỰC ĐỊA LSW/WCM & TEST VÒNG 2 (16 CÂU)
    # =========================================================================
    {
        "id": "q_adv_01",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Phân Tích Sâu",
        "question": "Tại sao không thể dùng chung một trục vít máy đùn ([[L/D Ratio]]) của nhựa [[PVC]] để chạy nhựa [[XLPE]] hoặc [[LSZH]]? Nếu cố chạy chung sẽ xảy ra hậu quả gì?",
        "key_points": (
            "• Khác biệt bản chất lưu biến:\n"
            "  1. [[PVC]] nhạy nhiệt, dễ phân hủy sinh khí axit HCl ăn mòn nòng nếu lưu quá lâu → cần trục vít ngắn hơn (`L/D 20–24:1`), tỷ số nén vừa (`2.0–2.5:1`).\n"
            "  2. PE/[[XLPE]] cần hóa dẻo đồng nhất ở tốc độ cao → cần trục vít dài (`L/D 25–30:1`, vùng Barrier, tỷ số nén `2.8–3.5:1`).\n"
            "  3. [[LSZH]] chứa hàm lượng chất độn chống cháy vô cơ cao, cực kỳ nhạy nhiệt cắt trượt → cần trục vít nén thấp (`1.8–2.3:1`).\n"
            "• Hậu quả chạy sai trục vít: Quá nhiệt ma sát gây cháy xém Scorch, bọt khí Voids, sần [[Sharkskin]] hoặc tắc chết nòng đùn; OE bắt buộc kiểm tra tương thích trục vít khi lập lịch san tải [[RCCP]]."
        )
    },
    {
        "id": "q_adv_02",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Tình Huống Thực Chiến",
        "question": "Khi theo dõi đồng hồ [[Melt Pressure]] trên máy đùn cáp thấy áp suất tăng dần +30% trong ca hoặc dao động nhịp nhàng ±15 bar (Surging), bạn chẩn đoán điều gì và xử lý ra sao?",
        "key_points": (
            "• Đọc chẩn đoán từ tín hiệu [[Melt Pressure]]:\n"
            "  1. Tăng đều +25–30% ở cùng vòng quay trục vít: Lưới lọc [[Screen Pack]] đã tích bẩn/nhựa cháy gây cản dòng → lên lịch thay lưới lọc ngay cuối lệnh sản xuất (tránh rách lưới gây tạp chất rớt [[Partial Discharge|PD]] hoặc quá áp vỡ đĩa an toàn).\n"
            "  2. Dao động chu kỳ ±15 bar (Surging): Vùng cấp liệu bị trượt hoặc nhiệt độ vùng nạp/trục vít không ổn định → làm đường kính cáp trên [[Laser Gauge]] biến thiên hình sin khiến [[Cpk]] tụt mạnh.\n"
            "• Giải pháp OE: Đưa tín hiệu Melt Pressure & Melt Temperature lên [[MES]] đặt ngưỡng cảnh báo bảo trì dự đoán ([[CBM / PdM]]) để thay lưới chủ động đúng dịp đổi mã [[SMED]]."
        )
    },
    {
        "id": "q_adv_03",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Khái Niệm Cốt Lõi",
        "question": "[[DDR|Draw-Down Ratio (DDR)]] và DRB trong đùn bọc cáp là gì? Phân biệt nhanh Đùn Ép (Pressure Tooling) và Đùn Ống (Tube Tooling).",
        "key_points": (
            "• Phân biệt 2 kiểu đầu Chày–Cối (Tip & Die):\n"
            "  1. Đùn Ép (Pressure Tooling): Chày thụt vào trong cối, nhựa ép mạnh bám chặt vào khe sợi lõi (dùng khi cần điền đầy hoặc bám dính cao).\n"
            "  2. Đùn Ống (Tube Tooling): Chày ngang miệng cối tạo ống nhựa rồi kéo rút + hút chân không ôm sát lõi (chạy tốc độ cao, đều độ dày, thợ điện dễ tuốt vỏ).\n"
            "• Ý nghĩa [[DDR]] & DRB: `DDR = (D_die² - D_tip²) / (D_cable² - D_core²)` (PVC chuẩn 1.5–2.5; PE/XLPE 1.3–2.2; DRB tối ưu 0.95–1.08). Chọn cối quá rộng làm DDR quá cao gây ứng suất dư, co ngót đầu cáp, nứt lạnh và lãng phí nhựa [[Over-thickness]]."
        )
    },
    {
        "id": "q_adv_04",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Tình Huống Thực Chiến",
        "question": "Khi bạn đề xuất tăng tốc độ máy đùn thêm +20% để nâng OEE Performance, bề mặt vỏ cáp xuất hiện sần nhám mờ ([[Sharkskin]]) và đóng cặn mép cối ([[Die Drool]]). Bạn xử lý thế nào?",
        "key_points": (
            "• Hiểu bản chất để không đánh đổi Quality lấy Performance:\n"
            "  1. [[Sharkskin]] xảy ra khi ứng suất cắt tại miệng cối vượt ngưỡng tới hạn do tốc độ cao & độ nhớt lớn.\n"
            "  2. [[Die Drool]] do nhựa ẩm, bột độn [[CaCO3 Filler]] hoặc nhiệt cắt quá cao tích tụ ngoài mép cối rồi rơi bám lên vỏ cáp gây cục u/lỗi [[Spark Tester]].\n"
            "• 4 bước giải quyết chuẩn OE + Kỹ thuật:\n"
            "  - Kiểm tra sấy hạt nhựa đạt chuẩn trên [[Hopper Dryer]] (triệt độ ẩm).\n"
            "  - Tăng nhẹ nhiệt độ miệng cối Die `+5–10°C`, đánh bóng/vát mép thoát 45° lòng cối và kiểm tra lại tỷ lệ [[DDR]].\n"
            "  - Thử nghiệm [[DOE]] (Minitab) tìm tốc độ tối ưu kết hợp phụ gia trợ gia công PPA 0.5% rồi khóa thành cửa sổ công nghệ mới qua quy trình [[MOC / ECN]]."
        )
    },
    {
        "id": "q_adv_05",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Phân Tích Sâu",
        "question": "Phòng Mua hàng đề xuất chuyển sang hạt [[PVC]] loại B rẻ hơn 2.5% giá/kg (do độn thêm [[CaCO3 Filler]]) nhưng [[Specific Gravity|tỷ trọng]] tăng từ 1.45 lên 1.54 g/cm³. Với tư cách OE, bạn đồng ý hay phản đối?",
        "key_points": (
            "• Phản đối dựa trên bài toán Chi Phí Theo Thể Tích (Volume Cost)!\n"
            "  1. Cáp điện bọc theo THỂ TÍCH (chiều dày × chu vi × km), KHÔNG bọc theo kg.\n"
            "  2. Tỷ trọng tăng từ 1.45 lên 1.54 (+6.21%) nghĩa là mỗi km cáp sẽ phải tiêu tốn nhiều hơn +6.21% khối lượng nhựa!\n"
            "  3. Nhân chéo hiệu ứng giá: `0.975 (giá giảm 2.5%) × 1.0621 (tốn kg hơn 6.21%) = 1.0355` → Thực tế CHI PHÍ NHỰA TRÊN MỖI KM CÁP ĐẮT THÊM +3.55%!\n"
            "• Rủi ro cộng thêm: Tăng [[CaCO3 Filler]] còn làm dễ đóng cặn [[Die Drool]], tăng mòn trục vít và dễ trượt phép thử độ giãn dài [[Tensile]]/[[Aging Oven]]."
        )
    },
    {
        "id": "q_adv_06",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Tình Huống Thực Chiến",
        "question": "Xưởng Kéo sợi [[Multi-wire]] bị đứt sợi đồng liên tục làm [[OEE]] tụt xuống 58%. Xưởng đổ lỗi cho đồng Rod kém, còn Mua hàng bảo do máy/khuôn. Bạn dùng kỹ thuật gì để phân xử khách quan 100%?",
        "key_points": (
            "• Áp dụng [[Wire Break Forensics]] (Phân tích mặt gãy đầu sợi dưới kính hiển vi):\n"
            "  1. Thu thập 20–30 đầu sợi đứt liên tiếp, phân loại định lượng bằng biểu đồ [[Pareto]]:\n"
            "     - Mặt gãy hình [[Cup-and-Cone]] (thắt cổ chai đối xứng) → Lỗi nội bộ xưởng Kéo (khuôn [[PCD]] mòn, vòi [[Drawing Emulsion|nhũ tương]] tắc, lực căng kẹt rulo).\n"
            "     - Mặt gãy dẹt có tạp chất cứng / vảy gấp (Inclusion / Sliver) → Lỗi đồng Rod đầu vào (đối chiếu COA theo chuẩn [[ASTM B49]] và lập [[8D|báo cáo 8D]] với nhà cung cấp).\n"
            "     - Mặt gãy phẳng giòn ngay mối hàn (Weld Break) → Lỗi thao tác hàn đối đầu [[Butt Welder]] hoặc quên ủ mềm sau hàn.\n"
            "• Chuẩn hóa bảng mẫu ảnh mặt gãy nhập mã lỗi lên [[MES]] để xử lý đúng gốc rễ, chấm dứt tranh cãi cảm tính."
        )
    },
    {
        "id": "q_adv_07",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Khái Niệm Cốt Lõi",
        "question": "Trình bày đặc thù sản xuất & điểm cần tối ưu OE đối với [[Solar Cable|Cáp Năng Lượng Mặt Trời H1Z2Z2-K]] và công đoạn bện lưới đồng chống nhiễu ([[Braiding]]) tại CADIVI.",
        "key_points": (
            "• Với [[Solar Cable]] (EN 50618, DC 1,500V, tuổi thọ 25 năm):\n"
            "  - Ruột đồng mềm mạ thiếc ([[Tinned Copper]]) dễ xước lớp mạ → kiểm soát puly dẫn bằng gốm, lực căng đều; lớp cách điện/vỏ kép XLPO đắt tiền → gom đơn [[Color Sequencing]] (Đỏ/Đen) và tối ưu tải rulo khi chiếu xạ [[E-beam]] để giảm chi phí & [[Lead Time]].\n"
            "• Với công đoạn [[Braiding]] (bện lưới 16–24 suốt cho cáp điều khiển chống nhiễu):\n"
            "  - Tốc độ cực chậm (2–8 m/phút) dễ thành cổ chai → Áp dụng [[Man-Machine Chart]] (1 công nhân đứng 4–8 máy) và đồng bộ chiều dài đánh suốt [[Kitting]] để cả 24 suốt hết cùng lúc thay 1 lần, thay vì dừng máy 16 lần/ca!"
        )
    },
    {
        "id": "q_adv_08",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Tình Huống Thực Chiến",
        "question": "Làm sao phân loại & quản trị phế nhựa [[Regrind]] trong nhà máy dây cáp điện để vừa tối ưu chi phí [[BOM]], vừa không vi phạm tiêu chuẩn chất lượng [[QCVN 4]] / [[IEC 60502]]?",
        "key_points": (
            "• Phân biệt rạch ròi 2 họ nhựa:\n"
            "  1. [[XLPE]] sau lưu hóa là nhựa nhiệt rắn → KHÔNG thể nghiền đùn tái chế lại làm cách điện.\n"
            "  2. [[PVC]] là nhựa nhiệt dẻo → có thể nghiền tái chế ([[Regrind]]) nếu phân loại sạch ngay tại nguồn.\n"
            "• 3 nguyên tắc vàng quản trị Regrind của OE:\n"
            "  - Tuyệt đối KHÔNG dùng Regrind cho lớp cách điện chịu điện áp hay dây dân dụng chịu quản lý bắt buộc [[QCVN 4]] nếu chưa qua phê duyệt [[MOC / ECN]] & test Lab đạt 100% [[Tensile]]/[[Aging Oven]].\n"
            "  - Chỉ xem xét dùng tỷ lệ kiểm soát (5–15% nhựa sạch không dính đồng, cùng màu) cho lớp độn trong hoặc sản phẩm phù hợp tiêu chuẩn kỹ thuật.\n"
            "  - Tách riêng thùng phế PVC sạch vs PVC lẫn đồng/bẩn ngay tại máy đùn để tối đa hóa giá trị thu hồi phế liệu."
        )
    },
    {
        "id": "q_adv_09",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Phân Tích Sâu",
        "question": "Khi nào OE nên dùng [[Work Sampling]] thay cho bấm giờ [[Time Study]]? Trình bày công thức cỡ mẫu và ví dụ áp dụng tại nhà máy CADIVI.",
        "key_points": (
            "• Khi nào chọn [[Work Sampling]]: Cho công việc chu kỳ dài, biến động hoặc không lặp đều (công nhân đứng đa máy kéo/bện, đội xe nâng kho rulo, đội bảo trì cơ điện, kho thành phẩm) — đo nhanh, ít tốn nhân lực khảo sát và không gây căng thẳng cho người bị bấm giờ.\n"
            "• Công thức cỡ mẫu (tin cậy 95%, Z = 1.96): `N = [ Z² × p × (1 - p) ] / e²`. Ví dụ ước lượng thời gian chờ p = 0.25, sai số e = ±0.03 → `N = 800 lượt` quan sát ngẫu nhiên.\n"
            "• Ví dụ CADIVI: Chụp mẫu 800 lượt trên 4 xe nâng xưởng cáp phát hiện 34% thời gian chạy rỗng/tìm rulo → thiết kế tuyến [[Milk Run]] & sơ đồ vị trí kho rulo giải quyết nghẽn cấp liệu mà không cần mua thêm xe nâng!"
        )
    },
    {
        "id": "q_adv_10",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Phân Tích Sâu",
        "question": "[[Loss Tree|OEE Waterfall / Loss Tree]] và [[Cost Deployment]] (WCM) giúp Chuyên viên OE thuyết phục Ban Giám đốc duyệt dự án ưu tiên nhanh hơn cách báo cáo truyền thống như thế nào?",
        "key_points": (
            "• Khác biệt tư duy:\n"
            "  - Báo cáo truyền thống chỉ nêu 20 vấn đề rời rạc bằng % hoặc số phút → Giám đốc khó quyết định nên rót tiền & người vào đâu trước.\n"
            "  - [[Loss Tree]] phân rã 100% thời gian lịch thành từng nhánh tổn thất rõ chủ sở hữu; [[Cost Deployment]] quy đổi thẳng từng nhánh đó sang **VNĐ/tháng** theo [[Standard Cost]].\n"
            "• Ví dụ CADIVI: Đặt lên cùng 1 bảng thấy [[Over-thickness]] nhựa mất 195 tr/tháng, [[Copper Give-away]] mất 165 tr/tháng, phế đổi mã mất 110 tr/tháng, còn rò khí nén mất 24 tr/tháng → Ban Giám đốc phê duyệt tập trung nguồn lực đánh ngay 2 mũi nhọn đầu tiên trong vòng 5 phút!"
        )
    },
    {
        "id": "q_adv_11",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Tình Huống Thực Chiến",
        "question": "Dự án [[SMED]] và [[5S]] của bạn chạy rất đẹp tháng đầu, nhưng 2 tháng sau khi bạn sang xưởng khác thì mọi thứ lại tụt về như cũ. Bạn thiết kế hệ thống gì để duy trì bền vững?",
        "key_points": (
            "• Không thể dựa vào trí nhớ hay thiện chí mà phải khóa bằng Bộ 3 Quản trị Duy trì:\n"
            "  1. [[LSW]] (Leader Standard Work): Nhúng 2–3 hạng mục kiểm tra đầu ca (tủ sấy Tip/Die, xe đồ nghề 5S, bảng giờ) vào lịch kiểm tra bắt buộc hàng ngày của Tổ trưởng & Quản đốc.\n"
            "  2. [[LPA]] (Layered Process Audit): Kiểm tra phân tầng 3 cấp (Tổ trưởng hàng ngày → Quản đốc/OE hàng tuần → Giám đốc 2 tuần/lần) bằng phiếu 8–10 câu Có/Không đi thẳng xuống máy.\n"
            "  3. [[Visual Management]] & [[ADKAR]] (bước Reinforcement): Công khai biểu đồ xu hướng đổi mã/OEE ngay bảng chuyền, gắn thưởng nóng tổ/ca khi giữ chuẩn 30 ngày liên tiếp và phản hồi ngay khi lệch chuẩn."
        )
    },
    {
        "id": "q_adv_12",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Tình Huống Thực Chiến",
        "question": "Phân xưởng phàn nàn mỗi lần máy đùn hỏng gọi Bảo trì chờ 25–30 phút mới có người tới, còn Bảo trì than thiếu người ngập đầu sửa chữa. Bạn giải bài toán này bằng chỉ số và cơ chế nào?",
        "key_points": (
            "• 3 bước xử lý đồng bộ không đổ lỗi:\n"
            "  1. Lập [[Escalation Matrix]] có SLA rõ ràng (0–5p Tổ trưởng → 5–15p Bảo trì → 15–30p Quản đốc/OE → >60p Giám đốc) kết hợp đèn [[Andon]]/cảnh báo [[MES]] cho máy cổ chai.\n"
            "  2. Dùng [[Work Sampling]] đo [[Wrench Time]] của đội Bảo trì: nếu chỉ ~30% do mất thời gian tìm bạc đạn/điện trở → chuẩn hóa kho phụ tùng 5S + soạn sẵn bộ [[Kitting]] cho các lỗi lặp lại.\n"
            "  3. Nâng [[PM Compliance]] lên ≥ 90% (khóa giờ giao máy PM cố định trên lịch [[MPS]]) và áp dụng [[CBM / PdM]] (camera nhiệt ảnh tủ điện, đo rung bạc đạn) để cắt 50% sự cố chữa cháy đột xuất!"
        )
    },
    {
        "id": "q_adv_13",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Tình Huống Thực Chiến",
        "question": "Đề Test Thực Hành Vòng 2: Cho bảng log 5 ca máy đùn dây VC 2.5mm² (tốc độ chuẩn 320 m/p, 450p/ca), tổng dừng 275p, sản lượng 548,000m, phế 14,000m. Cách tính OEE tổng 5 ca đúng và bẫy Excel thường gặp là gì?",
        "key_points": (
            "• Tính chuẩn trên TỔNG dữ liệu gốc (tuyệt đối KHÔNG lấy `AVERAGE` của 5 con số OEE từng ca!):\n"
            "  1. `Planned Time = 5 × 450 = 2,250p` → `Operating Time = 2,250 - 275 = 1,975p` → `A = 1,975 / 2,250 = 87.78%`.\n"
            "  2. `P = 548,000 / (1,975 × 320) = 548,000 / 632,000 = 86.71%` (tốc độ thực bình quân 277.5 m/p).\n"
            "  3. `Good Length = 548,000 - 14,000 = 534,000m` → `Q = 534,000 / 548,000 = 97.45%`.\n"
            "  4. `OEE = 87.78% × 86.71% × 97.45% = 74.16%`.\n"
            "• 3 bẫy Excel cần tránh: (1) Lấy trung bình cộng % các ca sai trọng số, (2) Quên trừ nghỉ ăn ca khỏi Planned Time, (3) So sánh BOM với tổng mét đùn (548 km) thay vì sản lượng ĐẠT (534 km) làm che giấu phế phẩm!"
        )
    },
    {
        "id": "q_adv_14",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Tình Huống Thực Chiến",
        "question": "Khi sản lượng CADIVI tăng đột biến +35% mùa cao điểm, xưởng Đùn quá tải 122% nhưng bị ràng buộc KHÔNG mua máy mới và KHÔNG tăng ca vượt trần 40 giờ/người/tháng. Bạn lập phương án [[Headcount Planning]] & năng lực thế nào?",
        "key_points": (
            "• Phương án 4 mũi nhọn tuân thủ [[TOC]] & Luật Lao động VN:\n"
            "  1. Không tăng ca dàn trải ở xưởng Kéo/Đóng gói đang dư tải (tránh sinh [[WIP]]).\n"
            "  2. Khai thác ngay tại máy Đùn cổ chai: gom đơn cùng tiết diện + [[Color Sequencing]] + [[SMED]] nâng OEE máy đùn từ ~66% lên 75% (giải phóng ngay ~13% giờ máy ròng miễn phí).\n"
            "  3. Bố trí [[Headcount Planning|3 Ca – 4 Kíp]] cục bộ cho riêng 2 máy Đùn nút thắt bằng cách điều chuyển tạm công nhân đa kỹ năng từ xưởng dư tải + tính [[Learning Curve]] cho nhân sự bổ sung khâu đóng gói đơn giản.\n"
            "  4. Khóa [[Escalation Matrix]] 5 phút & giữ đệm 1 ca bán thành phẩm trước máy Đùn để máy không bao giờ đói hàng."
        )
    },
    {
        "id": "q_adv_15",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Phân Tích Sâu",
        "question": "Trước khi nhân rộng một cải tiến giảm chiều dày bọc nhựa hoặc thay đổi bộ khuôn đùn cho cả 6 máy tại CADIVI, bạn cần chạy quy trình [[MOC / ECN]] như thế nào để bảo đảm an toàn pháp lý [[QCVN 4]]?",
        "key_points": (
            "• Quy trình 5 bước kiểm soát thay đổi [[MOC / ECN]] bắt buộc:\n"
            "  1. Lập hồ sơ đề xuất thay đổi nêu rõ thông số cũ–mới và mục tiêu kinh tế/kỹ thuật.\n"
            "  2. Đánh giá rủi ro liên phòng ban ([[PFMEA]] với Kỹ thuật, QA/QC, [[EHS]], Kế toán BOM) — đảm bảo cận dưới kiểm soát nội bộ cao hơn chuẩn bắt buộc [[QCVN 4]] / [[IEC 60502]] tối thiểu `3σ`.\n"
            "  3. Chạy thử nghiệm lô nhỏ (Pilot Trial 1 máy) và gửi đủ mẫu phòng Lab đo chiều dày, [[Spark Tester]], [[Water Immersion]], [[Tensile]]/[[Aging Oven]], tính [[Cpk]] ≥ 1.33–1.67.\n"
            "  4. Phê duyệt chính thức bằng văn bản.\n"
            "  5. Cập nhật đồng bộ [[SOP]], [[Control Plan]], MBOM trên [[ERP]] và đào tạo công nhân trước khi chạy hàng loạt."
        )
    },
    {
        "id": "q_adv_16",
        "category": "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2",
        "type": "Tình Huống Thực Chiến",
        "question": "Khi hội đồng hỏi về thành tích thẩm định ROI thiết bị ở công ty cũ (~1.2 tỷ) và kỳ vọng mức lương 16–18 triệu tại CADIVI Miền Trung, bạn trả lời thế nào vừa thuyết phục vừa chuyên nghiệp?",
        "key_points": (
            "• Nguyên tắc ứng xử số liệu CV (Trung thực & Bảo mật):\n"
            "  1. Với thành tích Canon INEX (60s → 30s/hạng mục, giảm 50% thời gian đo) và bệ đo (1 → 16 mẫu/lượt gá): nhấn mạnh đây là tối ưu thao tác & tăng sức chứa mỗi lượt gá, KHÔNG thổi phồng thành tăng năng suất 16 lần hay cắt 50% nhân sự.\n"
            "  2. Với dự án thẩm định đầu tư thiết bị: tôn trọng bảo mật tài chính công ty cũ, tập trung trình bày **PHƯƠNG PHÁP LUẬN** thẩm định [[ROI]] / [[Payback]] (tách Hard Savings vs Soft Savings, đối chiếu Kế toán, chạy 3 kịch bản độ nhạy Thận trọng–Cơ sở–Lạc quan).\n"
            "• Về kỳ vọng thu nhập tại CADIVI (16–18 triệu + thưởng năm/phụ cấp): thể hiện rõ sự tìm hiểu về tổng thu nhập năm của hệ thống CADIVI/GELEX, khẳng định sẵn sàng bắt đầu trong khung ngân sách phù hợp năng lực và cam kết tạo ra giá trị tiết kiệm thực (Hard Savings) vượt xa chi phí lương ngay trong 90 ngày đầu!"
        )
    }
]

# Danh sách danh mục chuẩn
CATEGORIES = [
    "Tất cả chủ đề",
    "OEE & 6 Tổn Thất Lớn",
    "OLE & Năng Suất Lao Động",
    "Cân Bằng Chuyền & Takt Time",
    "SMED & Rút Ngắn Chuyển Đổi",
    "7 Lãng Phí (TIMWOOD) & 5S",
    "Poka-Yoke & Chống Lỗi",
    "Định Mức BOM & Hao Phí",
    "SPC, Minitab & Cp/Cpk",
    "Bố Trí Mặt Bằng & Luồng 1 Sản Phẩm",
    "ERP/MES & Quản Lý Genba",
    "Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)",
    "OE, Six Sigma (DMAIC), TOC, TPM & PFMEA",
    "Hoạch Định Năng Lực, Điều Độ & Chi Phí",
    "Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE",
    "Câu Hỏi Hỏi Ngược Nhà Tuyển Dụng CADIVI",
    "Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành",
    "Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2"
]


def get_all_questions():
    """Trả về toàn bộ danh sách câu hỏi phỏng vấn thực chiến (128 câu)."""
    return QUESTIONS


def get_categories():
    """Trả về danh sách 17 chủ đề + Tất cả chủ đề."""
    return CATEGORIES


def get_questions_by_category(category_name):
    """Lọc câu hỏi theo chủ đề."""
    if not category_name or category_name == "Tất cả chủ đề":
        return QUESTIONS
    return [q for q in QUESTIONS if q.get("category") == category_name]


def search_questions(keyword):
    """Tìm kiếm câu hỏi theo từ khóa trong câu hỏi hoặc gợi ý trả lời (hỗ trợ cả văn bản thuần & công thức [[Key|Text]])."""
    if not keyword or not keyword.strip():
        return QUESTIONS
    kw = keyword.strip().lower()
    results = []
    for q in QUESTIONS:
        q_text = q.get("question", "").lower()
        kp_text = q.get("key_points", "").lower()
        cat = q.get("category", "").lower()
        q_type = q.get("type", "").lower()
        if kw in q_text or kw in kp_text or kw in cat or kw in q_type:
            results.append(q)
        else:
            stripped_q = _FORMULA_STRIP_RE.sub(r"\1", q_text)
            stripped_kp = _FORMULA_STRIP_RE.sub(r"\1", kp_text)
            if kw in stripped_q or kw in stripped_kp:
                results.append(q)
    return results
