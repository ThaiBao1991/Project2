# -*- coding: utf-8 -*-
"""
interview_bank.py — Ngân Hàng Câu Hỏi Phỏng Vấn & Tình Huống Thực Chiến Tinh Gọn
Được thiết kế chuyên sâu cho Kỹ sư Cải tiến Sản xuất (Lean / Continuous Improvement Engineer),
Kỹ sư Quản lý Sản xuất (Industrial Engineer), và Quản lý Nhà máy.

Bao gồm 56 câu hỏi không trùng lặp, chia làm 10 nhóm chủ đề cốt lõi:
1. OEE & 6 Tổn Thất Lớn (Six Big Losses) (6 câu)
2. OLE & Năng Suất Lao Động (Overall Labor Effectiveness) (5 câu)
3. Cân Bằng Chuyền & Takt Time (Line Balancing) (6 câu)
4. SMED & Rút Ngắn Thời Gian Chuyển Đổi (6 câu)
5. 7 Lãng Phí (TIMWOOD) & 5S / Kaizen (6 câu)
6. Poka-Yoke & Cơ Chế Chống Lỗi (5 câu)
7. Định Mức BOM & Hao Phí Vật Tư (5 câu)
8. SPC, Năng Lực Quy Trình & Minitab (Cp/Cpk) (6 câu)
9. Bố Trí Mặt Bằng (Plant Layout) & Luồng 1 Sản Phẩm (5 câu)
10. ERP/MES, Dữ Liệu Sản Xuất & Xử Lý Sự Cố Genba (6 câu)
"""

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
    "ERP/MES & Quản Lý Genba"
]


def get_all_questions():
    """Trả về toàn bộ danh sách 56 câu hỏi."""
    return QUESTIONS


def get_categories():
    """Trả về danh sách 10 chủ đề."""
    return CATEGORIES


def get_questions_by_category(category_name):
    """Lọc câu hỏi theo chủ đề."""
    if not category_name or category_name == "Tất cả chủ đề":
        return QUESTIONS
    return [q for q in QUESTIONS if q.get("category") == category_name]


def search_questions(keyword):
    """Tìm kiếm câu hỏi theo từ khóa trong câu hỏi hoặc gợi ý trả lời."""
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
    return results
