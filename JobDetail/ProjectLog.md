# Nhật Ký Dự Án (ProjectLog) — JobDetail Intelligence Hub

Tài liệu nhật ký theo dõi kiến trúc, tiến độ và kiểm thử của phân hệ `JobDetail`.

---

## 2026-11-17 — Khởi Tạo Dự Án JobDetail Intelligence Hub

### 1. Bối Cảnh & Mục Tiêu
- Người dùng yêu cầu tạo mới dự án `JobDetail` với mục tiêu:
  * Đưa ra các nội dung có thể nắm được về công việc từ đơn giản đến chi tiết.
  * Cung cấp các tài liệu và nội dung cần nắm với một JD được nhập vào.
  * Hỗ trợ lưu trữ và tra cứu đa chiều.
- Tuân thủ nghiêm ngặt các quy chuẩn:
  * `job_detail_analysis_rules.md`: Mô hình 5 Tầng Kiến Thức (Tổng quan, Ma trận kỹ năng, Lộ trình Onboarding, Tài liệu chính thống, Câu hỏi phỏng vấn).
  * `python_desktop_standards.md` & `customtkinter_perf_ui`: Giao diện CustomTkinter 60fps zero-lag, Treeview dark theme Catppuccin Mocha.
  * `encoding_rules.md`: Chuẩn hóa UTF-8 toàn diện trên Windows.

### 2. Các Thành Phần Đã Triển Khai
- **`job_storage.py`**:
  * Sử dụng CSDL SQLite local (`job_detail.db`) với các chỉ mục tăng tốc tìm kiếm.
  * Đầy đủ CRUD: thêm, sửa, xóa, ghi chú cá nhân, cập nhật trạng thái.
  * Tìm kiếm tức thì theo từ khóa, lọc theo Level, Category, Status.
  * Hàm `export_job_markdown(job_id)` trích xuất báo cáo Markdown 5 tầng chi tiết chuẩn đẹp.
- **`job_analyzer.py`**:
  * Chế độ *Offline Smart Rule-based Engine*: Tự động bóc tách thực thể (Title, Company, Level, Category), nhận diện công nghệ, tự sinh lộ trình 3 chặng và ánh xạ official docs, sách kinh điển, từ khóa vàng tra cứu.
  * Chế độ *Gemini AI Engine*: Gọi REST API chính thức với temperature=0.2 và output JSON schema.
- **`JobDetailApp.py`**:
  * Desktop UI chuyên nghiệp, responsive dual-pane:
    - Sidebar: Instant search debounced 150ms, bộ lọc combobox Level & Ngành, bảng Treeview Dark Mode mượt mà.
    - Detail View: Header bar với các badge màu sắc, 6 Tab tương ứng 5 tầng kiến thức + Ghi chú cá nhân & raw JD.
    - Modal dialog thêm JD mới chạy luồng nền `threading.Thread`, không bao giờ đơ giao diện.
    - Nút mở web trực tiếp cho các Official Docs, nút Copy Markdown vào clipboard, nút lưu file `.md`.
  * Khởi tạo sẵn 2 JD mẫu chất lượng cao (Senior Python Backend & Junior React Frontend) khi CSDL mới tạo.
- **`test_job_storage.py` & `test_job_analyzer.py`**:
  * 100% unit tests passed (CRUD, search, filtering, export markdown, offline NLP extraction).
- **`Run_JobDetail.bat` & `requirements.txt` & `README.md`**: Bộ launcher và tài liệu hoàn chỉnh.

### 3. Kết Quả Kiểm Thử (Definition of Done)
- Build/Syntax Check: `python -m py_compile` không có lỗi.
- Unit Tests: `test_job_storage.py` (4/4 passed), `test_job_analyzer.py` (4/4 passed).
- Data Persistence: SQLite hoạt động ổn định, dữ liệu lưu trữ bền vững.
- Đồng bộ Rules & Skills: Đã đồng bộ 27 Skills và 11 Rules sang kho trung tâm và toàn cục máy tính qua `sync_skills_rules.py --push-all`.

---

## 2026-11-17 (Nâng cấp) — Mở Rộng Kho Dữ Liệu Offline Sản Xuất / Lean & Tối Ưu Bố Cục UI

### 1. Bối Cảnh & Phản Hồi Từ Người Dùng
- Tiếp nhận JD thực tế về Kỹ sư Cải tiến Sản xuất (Lean / OEE / OLE / SMED / BOM).
- Phản hồi giao diện: Tiêu đề dài bị tràn ngang đè lên các nút thao tác; badge lương bị cắt cụt; thiếu bộ lọc ngành Sản xuất; cần bổ sung đầy đủ hệ sinh thái phần mềm chuyên dụng và bộ câu hỏi phỏng vấn thực chiến đồ sộ.

### 2. Các Cải Tiến Đã Thực Hiện
- **Giao diện Desktop (`JobDetailApp.py`)**:
  * Tách biệt thanh công cụ (Action Bar) và tiêu đề công việc thành 2 hàng độc lập; tiêu đề có `wraplength=800` tự co giãn xuống dòng mà không bao giờ bị đè nút.
  * Bố cục lại hàng Badges thông tin: Hiển thị đầy đủ, thoáng đãng, mức lương hiển thị trọn vẹn không bị co cắt.
  * Bổ sung tùy chọn ngành nghề trong bộ lọc: `"Sản Xuất (Manufacturing)"`, `"Lean / IE"`, `"Supply Chain"`.
  * Tích hợp mục "Hệ Sinh Thái Phần Mềm Hỗ Trợ Chuyên Dụng" trong Tab Kho Tài Liệu (Excel Power Query/VBA, Power BI, Minitab, AutoCAD, SAP/MES) có nút mở tài liệu web 1-chạm.
- **Bộ máy Offline thông minh (`job_analyzer.py`)**:
  * Mở rộng kho từ điển `TECH_CATALOG` với đầy đủ các tri thức về Lean, 5S, Kaizen, VSM, OEE, OLE, SMED, BOM, Power BI, Minitab, AutoCAD, ERP/MES.
  * Tự động sinh lộ trình Onboarding 3 chặng chuyên sâu theo đặc thù nhà xưởng sản xuất (Genba, Pilot Line, Line Balancing).
- **Cơ sở dữ liệu (`job_detail.db`)**:
  * Cập nhật hồ sơ công việc ID 1 với bộ dữ liệu toàn diện 100%: 8 câu hỏi phỏng vấn & tình huống thực chiến có lời giải chi tiết, đầy đủ phần mềm hỗ trợ và lộ trình hành động.
- **Kiểm thử**: Đạt 4/4 test `test_job_storage.py`, 4/4 test `test_job_analyzer.py`, `py_compile` không lỗi, đồng bộ toàn cục thành công.

---

## 2026-11-18 — Bản Địa Hóa 100% Tri Thức Offline (Zero-Internet Architecture)

### 1. Bối Cảnh & Phản Hồi Từ Người Dùng
- Người dùng nhận xét dữ liệu và liên kết tài liệu trước đây vẫn phụ thuộc vào Internet (mở trình duyệt qua URL bên ngoài). Trong môi trường nhà máy, phòng sạch hoặc khi không có mạng, người dùng không thể học tập hay tra cứu được.
- Mục tiêu: Chuyển đổi toàn diện sang kiến trúc **100% Offline**, tích hợp sẵn toàn bộ cẩm nang chuyên sâu, công thức, quy trình SOP và hướng dẫn thực hành cục bộ ngay trong ứng dụng, có thể xem và làm chủ mọi tình huống mà không cần kết nối mạng.

### 2. Các Thành Phần & Cải Tiến Đã Triển Khai
- **Module Cẩm Nang Kỹ Thuật Độc Lập (`offline_knowledge.py`)**:
  * Xây dựng kho 16 cẩm nang Markdown chuyên sâu chuẩn công nghiệp:
    1. `oee`: Cẩm nang toàn diện OEE, Six Big Losses, công thức chi tiết, ví dụ ca 8 tiếng.
    2. `ole`: Cẩm nang OLE, phương pháp Time & Motion Study, Takt Time, Cycle Time, cân bằng chuyền Yamazumi.
    3. `smed`: 4 bước kỹ thuật SMED (Shigeo Shingo), tách Internal vs External, cữ gá 1 chạm, kịch bản 2 người song song.
    4. `lean_muda`: 7 Lãng phí (TIMWOOD), 5S, Kaizen, VSM, cơ cấu chống sai Poka-Yoke.
    5. `bom_cost`: Cấu trúc cây BOM, phân tích hao phí công nghệ vs hao phí lỗi, kiểm soát theo lô, Pareto 80/20.
    6. `excel_mfg`: Power Query gom file folder tự động, unpivot ca làm việc, biểu đồ Pareto, macro VBA báo cáo ca.
    7. `powerbi_mfg`: Mô hình Star Schema nhà máy, công thức DAX tính Availability, Performance, Quality, Scrap Rate.
    8. `minitab_spc`: Kiểm soát quá trình SPC (Xbar-R, I-MR), tính toán năng lực quá trình Cp/Cpk/Pp/Ppk.
    9. `autocad_layout`: Thiết kế mặt bằng xưởng tinh gọn, chuyền chữ U, luồng 1 sản phẩm, sơ đồ Spaghetti.
    10. `erp_mes`: Kiến trúc phân tầng ISA-95, PLC/SCADA -> MES ghi nhận máy thời gian thực -> SAP PP hạch toán chi phí.
    11. `python_core`: Kiến trúc CPython, cơ chế GIL, IO-bound vs CPU-bound, Data structures $O(1)$, PEP8, Typing.
    12. `react_fe`: Virtual DOM, thuật toán Reconciliation, Hooks rules, Stale closure trap, useMemo/useCallback, Concurrent mode.
    13. `docker_devops`: Multi-stage builds giảm kích thước 95%, quy tắc cache layer, Compose networking, Healthchecks.
    14. `sql_db`: Bản chất B-Tree index, Leftmost prefix rule, cơ chế MVCC, khắc phục lỗi N+1 Query.
    15. `redis_cache`: Cache-aside pattern, giải pháp phòng chống Cache Breakdown, Avalanche, Penetration, Distributed Lock.
    16. `git_vcs`: Quy tắc vàng Rebase vs Merge, điều tra bug bằng `git bisect`, giải quyết xung đột an toàn.
  * Cung cấp các API: `get_offline_doc(doc_id)`, `search_offline_docs(keyword)`, `get_all_offline_docs()`.
- **Trình Đọc Cẩm Nang Nội Bộ (`OfflineDocViewer` trong `JobDetailApp.py`)**:
  * Cửa sổ modal chuyên dụng (Toplevel) với typography rõ nét (Consolas / Segoe UI), chia đoạn Markdown trực quan.
  * Tích hợp nút Copy nội dung cẩm nang vào Clipboard và nút Đóng tiện lợi.
- **Tối Ưu Trải Nghiệm Người Dùng Tab Kho Tài Liệu**:
  * Bổ sung Badge trạng thái: `🟢 100% Offline Mode` tại thanh tiêu đề.
  * Banner 10 nút bấm xem nhanh cẩm nang phản hồi tức thì dưới 10ms. Tự động chuyển đổi giữa Bộ Cẩm Nang Sản Xuất và Bộ Cẩm Nang Công Nghệ Thông Tin tùy theo ngành nghề của JD đang chọn.
  * Mọi hàng Phần mềm và Tài liệu chính thống đều có nút chính `[📖 Đọc Cẩm Nang]` màu xanh nổi bật, ánh xạ trực tiếp `doc_key` để mở cẩm nang tương ứng, giữ nút `[🌐 Web]` làm lựa chọn phụ khi có Internet.
- **Bộ Máy Phân Tích Offline Thông Minh (`job_analyzer.py`)**:
  * Tự động gán `doc_key` cho toàn bộ các mục tài liệu và phần mềm phát hiện được.
  * Tự động sinh danh mục `offline_guides` phù hợp cho từng hồ sơ công việc.
- **Cơ Sở Dữ Liệu SQLite (`job_detail.db`)**:
  * Cập nhật hồ sơ ID 1 (Kỹ Sư Cải Tiến Sản Xuất) với đầy đủ liên kết 10 cẩm nang offline.
  * Bổ sung sẵn 2 hồ sơ công việc mẫu đa dạng (Senior Python Backend & Junior React Frontend) để tra cứu tức thì.
- **Kiểm Thử Toàn Diện**:
  * 9/9 unit tests đạt chuẩn 100% trong 0.394s.
  * `py_compile` không có bất kỳ lỗi cú pháp nào.

---

## 2026-11-18 (Nâng cấp) — Trực Quan Hóa Khung Hộp Toán Học & Khắc Phục Lỗi Hiển Thị LaTeX

### 1. Bối Cảnh & Phản Hồi Từ Người Dùng
- Người dùng phản ánh công thức toán học trong cẩm nang bị lỗi hiển thị (các chuỗi LaTeX thô như `$\rightarrow$`, `\frac{380}{440}`, `\times`, `\mathbf{...}` in trực tiếp lên màn hình máy tính do CustomTkinter không có bộ biên dịch KaTeX).
- Yêu cầu: Làm sao để toàn bộ công thức toán học, bài toán thực tế và tính toán mẫu (như Case Study OEE, OLE, BOM, SPC) hiển thị rõ ràng, mạch lạc, thẩm mỹ và chuyên nghiệp.

### 2. Các Cải Tiến Đã Thực Hiện
- **Dữ liệu cẩm nang (`offline_knowledge.py`)**:
  * Chuyển đổi 100% các công thức toán từ mã LaTeX thô sang **Khung Hộp Toán Học Trực Quan (Visual Math Box)** bằng ký tự Unicode và đường kẻ phân số ngang `───`, dấu nhân `×`, mũi tên `→`, dấu bất đẳng thức `≥`, `≤` và ký tự Hy Lạp `σ`, `μ`.
  * Trình bày phân tầng từng bước: (1) Dữ liệu ban đầu, (2) Công thức chữ, (3) Thế số cụ thể, (4) Kết quả và nhận xét chuyên gia Lean/Six Sigma.
  * Áp dụng đồng bộ cho toàn bộ 16 cẩm nang (OEE ca 8 tiếng, OLE 3 thành phần, Takt Time & Line Balancing LBE, BOM Variance, Minitab Cp/Cpk...).
- **Trình đọc cẩm nang (`OfflineDocViewer` trong `JobDetailApp.py`)**:
  * Tích hợp cơ chế **Rich Syntax Tagging**: Tiêu đề `#`, `##`, `###` được tô màu Sapphire/Mint/Yellow nổi bật.
  * Khối công thức và khung hộp (`┌─`, `│`, `└─`, ```` ````) được hiển thị bằng font **Monospace `Consolas`** căn chỉnh lề và gạch phân số thẳng hàng tuyệt đối 100% trên nền xám tối `#181825`.
  * Bổ sung hàm lọc tự động `_sanitize_math_markup`: Tự động nhận diện và làm sạch mọi ký hiệu LaTeX còn sót lại thành ký tự Unicode chuẩn trước khi đưa lên màn hình.
- **Kiểm thử**: Đạt 9/9 tests passed (100%), `py_compile` 0 lỗi cú pháp.

---

## 2026-11-18 (Nâng cấp) — Xóa Bỏ Lỗi KeyError: 'surface2', Xây Dựng Ngân Hàng 56 Câu Hỏi Phỏng Vấn Thực Chiến & Nâng Cấp Bộ Lọc Đa Chiều

### 1. Bối Cảnh & Phản Hồi Từ Người Dùng
- Khi bấm nút `[📖 Đọc Cẩm Nang]`, ứng dụng ném lỗi `KeyError: 'surface2'` tại `tb.tag_config("divider", font=("Consolas", 10), foreground=THEME["surface2"])`, làm đứt quãng trải nghiệm mở cẩm nang ("Nội dung đang mất").
- Người dùng yêu cầu:
  * Khắc phục triệt để lỗi hiển thị nội dung.
  * Bổ sung đầy đủ nội dung, thêm kho câu hỏi đa dạng tối thiểu 50 câu không trùng lặp từ cơ bản đến nâng cao.
  * Thiết lập vòng lặp kiểm tra (Test Loop), hoàn thiện test case và kiểm tra toàn diện đến khi hoàn toàn sạch lỗi.

### 2. Các Thành Phần & Cải Tiến Đã Triển Khai
- **Khắc phục lỗi KeyError: 'surface2' trong `JobDetailApp.py`**:
  * Thêm token `"surface2": "#585b70"` vào bảng màu chuẩn Catppuccin Mocha `THEME`.
  * Áp dụng kỹ thuật truy xuất an toàn `THEME.get("surface2", THEME["surface1"])` trong `_render_styled_content`.
  * Xác nhận `OfflineDocViewer` mở toàn bộ 16 cẩm nang không còn bất kỳ lỗi nào.
- **Xây dựng Ngân Hàng 56 Câu Hỏi Phỏng Vấn & Tình Huống Thực Chiến (`interview_bank.py`)**:
  * 100% không trùng lặp, chia làm 10 nhóm chủ đề công nghiệp cốt lõi:
    1. *OEE & 6 Tổn Thất Lớn (Six Big Losses)* (6 câu)
    2. *OLE & Năng Suất Lao Động (Overall Labor Effectiveness)* (5 câu)
    3. *Cân Bằng Chuyền & Takt Time (Line Balancing)* (6 câu)
    4. *SMED & Rút Ngắn Thời Gian Chuyển Đổi* (6 câu)
    5. *7 Lãng Phí (TIMWOOD) & 5S / Kaizen* (6 câu)
    6. *Poka-Yoke & Cơ Chế Chống Lỗi (Mistake Proofing)* (5 câu)
    7. *Định Mức BOM & Hao Phí Vật Tư* (5 câu)
    8. *SPC, Năng Lực Quy Trình & Minitab (Cp/Cpk)* (6 câu)
    9. *Bố Trí Mặt Bằng (Plant Layout) & Luồng 1 Sản Phẩm* (5 câu)
    10. *ERP/MES, Dữ Liệu Sản Xuất & Xử Lý Sự Cố Genba* (6 câu)
  * Mỗi câu hỏi có cấu trúc: `id`, `category`, `type` (*Tình Huống Thực Chiến* | *Khái Niệm Cốt Lõi* | *Phân Tích Sâu*), nội dung câu hỏi sâu sắc, và khung `key_points` chi tiết gồm công thức, số liệu, quy trình hành động tại xưởng.
- **Nâng cấp UI Tab "❓ Phỏng Vấn & Thực Chiến" trong `JobDetailApp.py`**:
  * Bổ sung thanh điều khiển phía trên gồm:
    - Ô tìm kiếm tức thì theo từ khóa câu hỏi, gợi ý trả lời, danh mục.
    - ComboBox chọn lọc theo 10 chủ đề công nghiệp.
    - Badge hiển thị số lượng trực quan (`Hiển thị: X / Y câu hỏi`).
  * Render thẻ câu hỏi với viền phân cách, badge phân loại màu sắc (Peach / Mauve / Blue / Green), khung gợi ý trả lời nền xám tối `#181825` chuyên nghiệp.
- **Tích hợp Bộ Phân Tích & CSDL**:
  * `job_analyzer.py`: Kết nối `interview_bank` tự động nạp trọn vẹn 56 câu hỏi khi phân tích JD thuộc lĩnh vực Sản xuất / Lean / IE.
  * `job_detail.db`: Cập nhật bản ghi Job ID 1 chứa đủ 56 câu hỏi trong SQLite.
- **Vòng lặp kiểm thử tự động (`test_qa_and_viewer.py`)**:
  * 12/12 unit test mới pass 100%: Kiểm tra số lượng $\ge 50$ (56 câu), kiểm tra ID và text không trùng lặp, kiểm tra đầy đủ trường dữ liệu, kiểm tra lọc danh mục, tìm kiếm, kiểm tra render headless cả 16 cẩm nang và test tương tác UI của `JobDetailApp`.
  * Toàn bộ 21/21 unit test của toàn dự án chạy thành công trong 3.419s không một lỗi phát sinh.

---

## 2026-11-18 (Nâng cấp) — Nâng Cấp Toàn Diện Tri Thức OLE & Hệ Thống Cẩm Nang Tinh Gọn Từ Basic Đến Expert (Kèm 3 Case Study Thực Chiến)

### 1. Bối Cảnh & Mục Tiêu
- Người dùng phản hồi: Kiến thức OLE và các mảng kỹ thuật liên quan còn chưa đầy đủ, thiếu các ví dụ tính toán thực tế để dễ nắm bắt. Yêu cầu hệ thống tri thức phải được biên soạn chỉnh chu, phân tầng bài bản từ **Cơ Bản (Basic) $\rightarrow$ Trung Cấp (Intermediate) $\rightarrow$ Nâng Cao (Advanced) $\rightarrow$ Chuyên Gia (Expert)**.

### 2. Các Thành Phần & Cải Tiến Đã Hoàn Thành
- **Cẩm nang OLE Đẳng Cấp Công Nghiệp (`offline_knowledge.py`)**:
  * Dung lượng tăng vọt từ 3,534 ký tự lên **20,713 ký tự**, phân tầng 4 cấp bậc rõ rệt:
    1. *Tầng 1 (Basic)*: Bản chất OLE, vì sao OEE cao vẫn lỗ nếu OLE thấp, so sánh OLE vs OEE vs OPE vs Năng suất đơn thuần, 3 trụ cột (Availability, Utilization, Quality), thang đo xếp hạng quốc tế (<60% đến >85%).
    2. *Tầng 2 (Intermediate)*: Ma trận đối chiếu 6 Tổn thất lao động lớn (Six Big Labor Losses) tương ứng với Six Big Losses của máy móc; Phương pháp bấm giờ Time & Motion Study (Therbligs, MOST, hệ số phụ cấp Allowances); Phân loại 3 nhóm thời gian thao tác (VA, NNVA, NVA).
    3. *Tầng 3 (Advanced - 3 Case Study Thực Chiến Có Lời Giải Chi Tiết)*:
       - **Case Study 1**: Tính OLE cho 1 công nhân ca 8h (Availability = 90.91%, Utilization = 80.00%, Quality = 95.00% $\rightarrow$ OLE = 69.09%) kèm 3 giải pháp Kaizen dứt điểm.
       - **Case Study 2**: Tính Line OLE cho dây chuyền 10 công nhân (Line Availability = 93.56%, Line Utilization = 87.89%, Line Quality = 97.03% $\rightarrow$ Line OLE = 79.79%) và bài toán chi phí lương thất thoát hơn 47 triệu VNĐ/tháng.
       - **Case Study 3**: Cân bằng chuyền 5 trạm, biểu đồ Yamazumi, tính Smoothness Index (SI), tái phân bổ thao tác đưa LBE từ 69.05% lên 93.79% và giảm SI từ 34.71s về 5.20s.
    4. *Tầng 4 (Expert)*: Nhân trắc học Ergonomics (Vùng thao tác vàng Golden Zone bán kính 40cm, chiều cao mặt bàn); Kiến trúc số hóa MES/RFID quẹt thẻ thời gian thực; Tích hợp hạch toán giá thành biến đổi lương trong SAP ERP; Đào tạo kỹ năng đa năng TWI (JI, JM, JR).
- **Nâng cấp chuyên sâu các cẩm nang sản xuất cốt lõi**:
  * `oee`: Bổ sung phân biệt OEE vs TEEP, Case Study mở rộng công suất 24/7 tiết kiệm 3.5 tỷ VNĐ CAPEX, triệt tiêu vi dừng và 8 trụ cột TPM.
  * `smed`: Bổ sung bảng 10 bước đổi khuôn máy ép nhựa từ 85 phút xuống 8 phút 40 giây (giảm 89.8%), quy trình song song 2 người F1 Pit-stop, 6 cơ cấu gá kẹp 1 chạm.
  * `bom_cost`: Bổ sung bài toán BOM Variance cho lô 10,000 cụm van cơ khí, bóc tách Scrap công nghệ vs bất thường, cơ chế Kitting, Two-bin Kanban và kiểm kê Cycle Counting ABC.
  * `minitab_spc`: Bổ sung Case Study trục tiện 25mm ($C_p=1.33$ nhưng $C_{pk}=0.80$ do lệch tâm 0.04mm và cách chỉnh offset), 4 quy tắc Nelson Rules, MSA Gage R&R.
- **Cơ sở dữ liệu & Kiểm thử**:
  * Cập nhật CSDL `job_detail.db` Job ID 1 với các cẩm nang mới.
  * Mở rộng `test_qa_and_viewer.py` thêm 2 test cases kiểm tra độ sâu 4 tầng kiến thức và các Case Study.
  * Toàn bộ 23/23 unit test pass 100% trong 3.300s. Đã đồng bộ toàn cục qua `sync_skills_rules.py --push-all`.

---

## 2026-11-18 (Nâng cấp) — Triệt Tiêu 100% Ký Hiệu LaTeX Thô & Lỗi Escape Chuỗi Python (Toàn Bộ 16 Cẩm Nang & 56 Câu Hỏi)

### 1. Bối Cảnh & Phản Hồi Từ Người Dùng
- Người dùng phát hiện lỗi hiển thị công thức trong mục Phân tích Chi phí Lương: các ký hiệu `\times`, `\text`, `\rightarrow` bị trình thông dịch Python dịch nhầm thành các ký tự điều khiển (`\t` -> Tab `	imes`, `	ext`; `\r` -> Carriage Return `ightarrow`), kèm theo các dấu `$...$` thô.

### 2. Các Cải Tiến Đã Thực Hiện
- **Làm sạch toàn diện `offline_knowledge.py` & `interview_bank.py`**:
  * Loại bỏ sạch sẽ 100% các ký hiệu `\times`, `\text`, `\rightarrow`, `\phi`, `\mu`, `\sigma`, `\ge`, `\le`, `\pm`, `\frac` và toàn bộ dấu `$` khỏi toàn bộ 16 cẩm nang và 56 câu hỏi.
  * Thay thế đồng bộ bằng các ký tự Unicode thuần sắc nét: `×`, `→`, `Ø`, `μ`, `σ`, `≥`, `≤`, `±`.
  * Đoạn Chi phí Lương được chuẩn hóa sạch đẹp:
    ```text
    • Tổng thời gian lãng phí trong ca = 4,500 - (1,795 × 2.0) = 4,500 - 3,590 = 910 phút công (15.17 giờ công).
    • Với đơn giá lương nhân công trung bình 60,000 VNĐ/giờ, ca làm việc này đã làm thất thoát:
      • Chi Phí Thất Thoát = 15.17 giờ × 60,000 VNĐ = 910,200 VNĐ / ca
    • Một tháng chạy 2 ca × 26 ngày → Nhà máy mất hơn **47,300,000 VNĐ** tiền lương vô ích trên duy nhất 1 dây chuyền này!
    ```
- **Nâng cấp hàm lọc phòng thủ `_sanitize_math_markup` trong `JobDetailApp.py`**:
  * Tự động nhận diện và gọt bỏ triệt để mọi biến thể escape `\text`, `	ext`, `\times`, `	imes`, `\rightarrow`, `ightarrow` và các dấu `$` phòng ngừa dữ liệu đầu vào.
- **Cập nhật CSDL SQLite (`job_detail.db`)**:
  * Đồng bộ lại dữ liệu Job ID 1 với toàn bộ ngân hàng câu hỏi và cẩm nang sạch 100%.
- **Kiểm thử tự động nâng cấp (`test_qa_and_viewer.py`)**:
  * Bổ sung assertion quét toàn bộ văn bản 16 cẩm nang và 56 câu hỏi xác nhận không còn token LaTeX hay dấu `$` nào.
  * Toàn bộ 24/24 unit test chạy đạt chuẩn 100% trong 3.941 giây.

---

## 2026-11-21 (Nâng cấp lớn) — Bổ Sung Toàn Diện Tri Thức Chuyên Ngành Dây Cáp Điện (OE — Nhà Máy CADIVI Miền Trung, CareerViet `35C8613F`)

### 1. Bối Cảnh & Mục Tiêu
- Đối chiếu trực tiếp JD CareerViet `35C8613F`: **Chuyên Viên Tối Ưu Quy Trình (OE)** — **Công ty Cổ phần Dây Cáp Điện Việt Nam (CADIVI) – Nhà máy CADIVI Miền Trung** (Đường số 2, KCN Hòa Cầm, Cẩm Lệ, Đà Nẵng; lương 16–18 triệu + thưởng/phụ cấp).
- Người dùng đánh giá dữ liệu cũ còn chung chung (chỉ có ví dụ cơ khí/nhựa/điện tử), thiếu toàn bộ đặc thù công nghệ & máy móc dây cáp điện, thiếu các mảng nâng cao (Six Sigma DMAIC, TOC, TPM, PFMEA, RCCP, kiểm định thống kê & thẩm định ROI) và thiếu câu hỏi phỏng vấn sát thực tế CADIVI + phản biện CV.

### 2. Các Thành Phần & Cải Tiến Đã Triển Khai
- **Kho Cẩm Nang 100% Offline (`offline_knowledge.py`) — Mở rộng từ 16 → 19 Cẩm Nang (138,844 ký tự, 0 lỗi escape/LaTeX)**:
  * **Thêm mới 3 cẩm nang 4 tầng (Basic → Intermediate → Advanced → Expert)**:
    1. `cable_mfg_machines` (16,914 ký tự): Bách khoa quy trình 7 công đoạn & **9 nhóm máy móc nhà máy dây cáp điện CADIVI** (Kéo thô RBD, Kéo trung/tinh/nhiều sợi, Ủ liên tục & Lò ủ chuông, Bện Buncher/Tubular/Rigid Frame Strander, Dây chuyền Đùn PVC/PE/XLPE/LSZH + Laser Gauge + Spark Tester, Lưu hóa XLPE CCV/Silane-Sauna, Ghép lõi & Giáp băng thép DSTA/SWA, Máy cuộn khoanh/rulo, Phòng Lab QA/QC theo TCVN/IEC 60228/60502/60332 & Hệ thống phụ trợ), kèm ma trận lỗi công nghệ và điểm đánh OE từng máy.
    2. `oe_six_sigma_dmaic` (10,238 ký tự): Phân biệt OE/Lean/Six Sigma/IE, Hệ quản trị Tier 1–2–3 SQDC, 5 bước TOC (Drum-Buffer-Rope), TPM (MTBF/MTTR), PFMEA tính RPN cho máy đùn, Case Study 5 pha DMAIC giảm phế đùn cáp (3.8% → 0.78%), bản đồ chọn kiểm định thống kê (t-test/ANOVA/Chi-Square/p-value) và bài toán CAPEX/ROI/Payback Period.
    3. `cable_cost_capacity` (7,580 ký tự): Công thức khối lượng đồng/nhôm (kèm hệ số xoắn bện Lay-up Factor) và nhựa hình vành khăn, bài toán định lượng **Copper Give-away (+0.01mm → 6.76 tỷ/năm)** & **Over-thickness (+0.08mm → 2.36 tỷ/năm)**, hoạch định năng lực thô **RCCP** (nhận diện nút thắt Đùn tải 116.4%), tối ưu **Cut-Length** rulo và giảm điện năng `kWh/tấn`.
  * **Nâng cấp chiều sâu 4 tầng & bổ sung Case Study ngành Cáp Điện cho 10 cẩm nang sản xuất hiện có**:
    - `oee`: Case Study OEE tính theo **tốc độ mét/phút** trên máy đùn bọc PVC (65.14% → 84.6%).
    - `ole`: Case Study 4 **Biểu đồ Người–Máy (Man-Machine Chart: 1 người đứng 3 máy bện Buncher)** & tối ưu OLE tổ đóng cuộn khoanh 100m.
    - `smed`: Case Study SMED đổi màu & tiết diện máy đùn bọc cáp (55p → 12p: Color Sequencing, Purging Compound, sấy sẵn Tip/Die, Dual Pay-off/Take-up & Butt Welder).
    - `lean_muda`: Mở rộng 4 tầng với 8 lãng phí TIMWOODS xưởng cáp, VSM Current → Future State cáp lực `CXV` (Lead Time 12 → 4.2 ngày, PCE 9.55% → 27.3%), 5S & 5 Poka-Yoke xưởng cáp.
    - `bom_cost`: Bổ sung BOM đa tầng cáp lực `CXV 3×50+1×25` & phân tách phế đồng trần (~94% thu hồi) vs đồng dính nhựa (~75–82%).
    - `excel_mfg`, `powerbi_mfg`, `minitab_spc`, `autocad_layout`, `erp_mes`: Mở rộng toàn diện 4 tầng gắn trực tiếp nhà máy cáp (DAX OEE mét/phút & BOM Variance, Laser Gauge SPC + 2-Sample t-test, Layout chuyền dài 35–60m + cầu trục 5 tấn + SLP, ISA-95 PLC/Spark/Laser → MES → ERP + Barcode rulo).
  * **Dọn sạch 100% lỗi escape tiềm ẩn**: Sửa triệt để lỗi `\frac` biến thành `\x0c` (form-feed), `C_{pk}`, dấu `}` thừa, `\ ` và `\%` trong `offline_knowledge.py`.
- **Ngân Hàng Phỏng Vấn Thực Chiến (`interview_bank.py`) — Mở rộng từ 56 → 100 Câu Hỏi Không Trùng Lặp (15 Chủ Đề)**:
  * Giữ nguyên 56 câu nền tảng (10 chủ đề) + bổ sung **44 câu chuyên sâu mới (5 chủ đề)**:
    - *Công Nghệ & Máy Móc Dây Cáp Điện (CADIVI)* (12 câu)
    - *OE, Six Sigma (DMAIC), TOC, TPM & PFMEA* (10 câu)
    - *Hoạch Định Năng Lực, Điều Độ & Chi Phí* (7 câu)
    - *Phỏng Vấn Hành Vi (STAR) & Phản Biện CV OE* (10 câu — gắn thực tế kinh nghiệm Mabuchi + Fujikura)
    - *Câu Hỏi Hỏi Ngược Nhà Tuyển Dụng CADIVI* (5 câu)
- **Bộ Phân Tích (`job_analyzer.py`) & Giao Diện (`JobDetailApp.py`)**:
  * Mở rộng `TECH_CATALOG` với từ khóa & alias cho Dây cáp điện (`cable_mfg`), OE/Six Sigma (`six_sigma`), Năng lực/Chi phí (`capacity_cost`).
  * Nâng cấp Tab Kho Tài Liệu hiển thị đủ **13 nút cẩm nang Offline Sản Xuất & Cáp Điện**, cập nhật `_resolve_doc_key()` và `_sanitize_math_markup()`.
  * Khắc phục tràn ngang (clipping) ở Tab Ma Trận Kỹ Năng và mục Từ Khóa Vàng bằng lưới 2 cột co giãn có `wraplength`.
- **Cơ Sở Dữ Liệu (`job_detail.db`) & File Tổng Hợp (`CamNang_ToanDien_OE_CADIVI_MienTrung.md`)**:
  * Cập nhật **Job ID 1** đúng chuẩn vị trí **Chuyên Viên Tối Ưu Quy Trình (OE) — Nhà Máy CADIVI Miền Trung** (5 tầng kiến thức đầy đủ + 13 cẩm nang + 100 câu hỏi + Ghi chú chiến lược ứng tuyển cá nhân hóa).
  * Xuất file cẩm nang tổng hợp độc lập [CamNang_ToanDien_OE_CADIVI_MienTrung.md](file:///c:/Users/games/Desktop/Project/Python/Python%20MyWork/Project2/JobDetail/CamNang_ToanDien_OE_CADIVI_MienTrung.md) (253,083 ký tự, 3,299 dòng, 0 ký tự điều khiển lỗi, 0 dấu `$`).
- **Kiểm Thử Toàn Diện (Gate 2)**:
  * `py_compile` 8/8 file `.py` thành công 0 lỗi.
  * 24/24 unit tests (`test_job_storage.py`, `test_job_analyzer.py`, `test_qa_and_viewer.py`) đạt chuẩn 100%, bao gồm kiểm tra 19 cẩm nang, 100 câu hỏi không trùng lặp, quét ký tự escape/LaTeX, render headless 19/19 cẩm nang trên `OfflineDocViewer` và kiểm thử tương tác UI lọc/tìm kiếm 100 câu trên `JobDetailApp`.

---

## 2026-11-22 (Nâng cấp lớn) — Tối Ưu Tốc Độ Load Zero-Lag (Nhanh Gấp 264×) & Từ Điển Click-Anywhere 110 Thuật Ngữ OE/CADIVI

### 1. Bối Cảnh & Mục Tiêu
- Đo benchmark thực tế phát hiện nút thắt nặng: mỗi lần chọn hồ sơ (`_display_job_detail(1)`) mất **3,255.7 ms** (trong đó riêng Tab Phỏng vấn dựng 700 widget CTk Canvas mất **2,559.2 ms**, và ứng dụng render đồng thời cả 6 tab ngay khi chưa bấm xem).
- Người dùng yêu cầu: cải thiện mạnh tốc độ load, đồng thời bổ sung chi tiết định nghĩa, khả năng áp dụng & ví dụ thực tế tại CADIVI sao cho **bấm vào bất kỳ từ chuyên ngành nào (như `MES`, `Minitab`, `OEE`, `SMED`, `XLPE`, `Spark Tester`...) ở bất kỳ đâu đều mở ra định nghĩa đầy đủ ngay lập tức**.

### 2. Các Thành Phần & Cải Tiến Đã Triển Khai
- **Module Từ Điển & Bộ Nhận Diện Siêu Tốc (`term_glossary.py`)**:
  * Xây dựng **110 thuật ngữ độc nhất (0 trùng lặp)** phủ trọn hệ thống số hóa/phần mềm (`MES`, `ERP`, `SAP PP`, `SCADA`, `PLC`, `ISA-95`, `Minitab`, `Power BI`, `Power Query`, `DAX`, `VBA`, `AutoCAD`, `Excel`, `Python`, `Barcode`), chỉ số hiệu suất (`OEE`, `TEEP`, `OLE`, `Time Study`, `Man-Machine Chart`, `Takt Time`, `Cycle Time`, `Lead Time`, `Yamazumi`, `LBE`, `Smoothness Index`, `KPI`, `Six Big Losses`), Lean/Six Sigma/TOC/TPM/PFMEA/ROI (`SMED`, `VSM`, `5S`, `Kaizen`, `Poka-Yoke`, `Jidoka`, `Andon`, `Kanban`, `Two-Bin Kanban`, `Heijunka`, `WIP`, `Genba`, `Spaghetti`, `Shojinka`, `Water Spider`, `Ergonomics`, `TWI`, `OE`, `Six Sigma`, `DMAIC`, `SPC`, `Cpk`, `Ppk`, `Gage R&R`, `Nelson Rules`, `2-Sample t-test`, `ANOVA`, `DOE`, `TOC`, `TPM`, `MTBF`, `MTTR`, `PFMEA`, `RCCP`, `CAPEX`, `ROI`, `Payback`, `Pareto`, `Ishikawa`, `5 Whys`, `8D`, `A3`, `PDCA`, `SOP`, `TIMWOOD`, `One-Piece Flow`, `FIFO`, `STAR`), và công nghệ/máy móc/tiêu chuẩn ngành Dây Cáp Điện CADIVI (`BOM`, `Kitting`, `Cycle Counting`, `Copper Give-away`, `Over-thickness`, `Lay-up Factor`, `Cut-Length`, `RBD`, `Annealing`, `Buncher`, `Rigid Strander`, `Multi-wire`, `Extruder`, `Crosshead`, `Capstan`, `Butt Welder`, `Spark Tester`, `Laser Gauge`, `Color Sequencing`, `Purging`, `XLPE`, `PVC`, `LSZH`, `Silane`, `CCV`, `Drum Twister`, `DSTA`, `Kelvin Bridge`, `Hot Set Test`, `Hopper Dryer`, `IEC 60228`, `IEC 60502`, `SEC`).
  * Mỗi thuật ngữ có đủ 6 phần: Tóm tắt 10s, Định nghĩa & Bản chất, Công thức/Thông số/Tiêu chuẩn, Khả năng áp dụng tại Nhà máy CADIVI Miền Trung, Ví dụ số liệu thực tế tại CADIVI, và Thuật ngữ liên quan + liên kết mở thẳng Cẩm nang gốc.
  * Biên dịch 1 Regex duy nhất có ranh giới từ Unicode-aware `(?<!\w)...(?!\w)` và phân biệt chữ hoa cho mã viết tắt ngắn (quét 23KB cẩm nang OLE tìm 112 link chỉ mất **23.70 ms**, 0 khớp nhầm).
- **Tối Ưu Kiến Trúc Zero-Lag & Click-Anywhere (`JobDetailApp.py`)**:
  * Áp dụng **Lazy Tab Rendering**: chọn Job chỉ render Tab đang mở; 5 tab còn lại render tức thì ngay khi bấm chuyển tab.
  * Thay thế ~700 CTk Canvas widgets tại Tab Phỏng vấn (và các tab Tổng quan, Kỹ năng, Lộ trình, JD Gốc, `OfflineDocViewer`) bằng **C-Engine `tk.Text`** + debounce tìm kiếm 120ms + 3 sự kiện gắn chung trên tag `term_link` (hỗ trợ kéo bôi đen copy chữ bình thường, click mở popup).
  * Tab Lộ trình giữ tương tác tích chọn checkbox `☐` ↔ `☑` trực tiếp trên C-Engine `tk.Text`.
  * Bổ sung **`TermDetailPopup`** (click chéo thuật ngữ liên quan kiểu Wikipedia, nút `⬅ Quay lại`, nút mở thẳng Cẩm nang gốc, phím `Esc`) và **`GlossaryBrowserDialog`** dùng C-Engine `tk.Listbox` lọc 60fps 110 thuật ngữ từ nút `📖 Từ Điển (110 Từ)` trên thanh Header.
- **Khắc Phục Cảnh Báo SQLite (`job_storage.py`)**:
  * Dùng `@contextmanager` đóng kết nối `conn.close()` chuẩn trong `finally`, triệt tiêu 100% `ResourceWarning: unclosed database`.
- **Cập Nhật Cẩm Nang Tổng Hợp (`CamNang_ToanDien_OE_CADIVI_MienTrung.md`)**:
  * Bổ sung **Phần IV: Từ Điển 110 Thuật Ngữ OE & CADIVI** (tổng dung lượng 409,118 ký tự, 4,749 dòng, 0 dấu `$`).

### 3. Kết Quả Benchmark Thực Tế & Kiểm Thử (Gate 2)
- **Đo tốc độ thực tế Trước vs Sau tối ưu**:
  * `_display_job_detail(1)`: **3,255.7 ms → 12.3 ms** (nhanh gấp **~264 lần**).
  * Render 100 câu phỏng vấn (+ gắn hàng trăm link thuật ngữ): **2,559.2 ms → 75.1 ms** (nhanh gấp **~34 lần**).
  * Tab Ma Trận Kỹ Năng: **133.5 ms → 6.0 ms** (nhanh gấp **~22 lần**).
  * Tab Lộ Trình Nắm Bắt: **171.9 ms → 7.7 ms** (nhanh gấp **~22 lần**).
  * Tab Ghi Chú & JD Gốc: **5.7 ms**.
  * Khởi động & tải lần đầu (`App init + first load`): **3,025.9 ms → 1,717.2 ms** (giảm **43%**).
- **Kiểm thử tự động**: `py_compile` 9/9 file `.py` (0 lỗi), **27/27 unit tests OK trong 7.214s**, 0 `ResourceWarning`, 0 trùng lặp, 0 lỗi ký tự.

---

## 2026-11-22 (Nâng cấp — Giai đoạn 3) — Bổ Sung Toàn Bộ Khoảng Trống Kiến Thức/Quy Trình OE & Hệ Thống Công Thức Hyperlink Tường Minh (`MES` Gạch Chân + Live Hover Tooltip)

### 1. Bối Cảnh & Mục Tiêu
- Rà soát sâu nội dung hiện có phát hiện các mảnh ghép kiến thức & quy trình thực tế tại nhà máy CADIVI còn thiếu: chuỗi hoạch định **S&OP → MPS → MRP → RCCP → CRP**, tồn kho (**Safety Stock / ROP / ABC-XYZ / Milk Run**), chất lượng xuyên suốt (**FPY / RTY / DPMO / 7 QC Tools / SIPOC / VOC–CTQ / Control Plan**), an toàn lao động (**EHS / LOTO 6 bước**) & bộ tứ **ISO 9001 / 14001 / 45001 / 50001**, đặc thù **cáp nhôm ACSR / cáp ABC treo trên không**, **cáp chống cháy băng Mica FR**, thử nghiệm cao áp **Partial Discharge (PD) / Water Immersion**, kế toán **Standard Cost Variance** và **Hoshin Kanri / ADKAR**.
- Người dùng đề xuất dùng cơ chế **công thức Hyperlink tường minh** cho các từ chuyên ngành nhằm triệt tiêu 100% nhận diện nhầm trên từ đa nghĩa/viết tắt ngắn (ví dụ tách bạch `[[ABC Cable|cáp ABC]]` vs `[[Cycle Counting|phân loại ABC]]`, `[[Partial Discharge|PD]]`), đồng thời chọn hiển thị **sạch đẹp dạng chữ xanh gạch chân (`MES` gạch chân, không kèm `↗` hay ngoặc `[]`)** kèm xem trước nhanh khi rê chuột.

### 2. Các Thành Phần & Cải Tiến Đã Triển Khai
- **Từ Điển & Bộ Phân Tích Công Thức Hyperlink (`term_glossary.py`)**:
  * Mở rộng từ **110 → 161 thuật ngữ độc nhất** (0 trùng lặp AST, 0 ký tự `$` / `**` / LaTeX / điều khiển; 100% `related` & `doc_key` trỏ khóa chính hợp lệ), gỡ alias trần `"ABC"` khỏi `Cycle Counting` để tránh xung đột.
  * Bổ sung 51 thuật ngữ còn thiếu: `S&OP`, `MPS`, `MRP`, `CRP`, `Safety Stock`, `ROP`, `ABC-XYZ`, `Milk Run`, `FPY`, `RTY`, `DPMO`, `SIPOC`, `VOC`, `CTQ`, `Control Plan`, `7 QC Tools`, `Histogram`, `Scatter`, `Chi-Square`, `Regression`, `Box-Cox`, `LOTO`, `EHS`, `ISO 9001`, `ISO 14001`, `ISO 45001`, `ISO 50001`, `ACSR`, `ABC Cable`, `Mica FR`, `Partial Discharge`, `Water Immersion`, `IACS`, `PCD`, `Drawing Emulsion`, `Pay-off`, `Take-up`, `Accumulator`, `Screen Pack`, `Masterbatch`, `Cooling Trough`, `Tensile`, `Aging Oven`, `VFD`, `Standard Cost`, `Hoshin Kanri`, `ADKAR`, `Visual Management`, `Downtime`, `Scrap`, `Work Combination Table`.
  * Triển khai bộ máy lai: `parse_rich_segments(text, auto_detect=True)` giải mã công thức tường minh `[[TermKey|DisplayText]]` / `[[TermKey]]` trước rồi mới chạy auto-detect cho văn bản ngoài; bổ sung `strip_term_formulas()`, `term_anchor_id()`, `convert_formulas_to_markdown_links()`.
- **Kho Cẩm Nang 100% Offline (`offline_knowledge.py`) — Mở rộng từ 19 → 20 Cẩm Nang (14 Sản xuất/Cáp điện + 6 IT)**:
  * Mở rộng `cable_mfg_machines`: bổ sung **Mục 5** về cáp ruột nhôm `ACSR` / `ABC Cable`, cáp chống cháy `Mica FR` (IEC 60331) và 2 phép thử Lab `Partial Discharge (PD)` & `Water Immersion`.
  * Thêm mới cẩm nang thứ 20: **`planning_quality_ehs_cost`** (4 tầng Basic → Expert): `S&OP → MPS → MRP → RCCP → CRP`, `Safety Stock / ROP / ABC-XYZ / Milk Run`, `FPY` vs `RTY` (ví dụ 6 công đoạn `83.27%`) & `7 QC Tools / Control Plan`, `EHS / LOTO 6 bước` & `ISO 9001 / 14001 / 45001 / 50001`, `Standard Cost Variance` và `Hoshin Kanri / ADKAR`.
- **Ngân Hàng Phỏng Vấn (`interview_bank.py`) — Mở rộng từ 100 → 112 Câu Hỏi (16 Chủ Đề)**:
  * Bổ sung **Nhóm 16: Kế Hoạch S&OP/MRP, FPY/RTY, LOTO/ISO & Giá Thành** (12 câu mới `q_plan_01`..`q_plan_12` sử dụng công thức `[[TermKey|DisplayText]]`); nâng cấp `search_questions()` khớp được cả cụm từ có chứa công thức.
- **Giao Diện, Lưu Trữ & Phân Tích (`JobDetailApp.py`, `job_storage.py`, `job_analyzer.py`)**:
  * Bổ sung **`TermHoverTooltip`** hiển thị thẻ tóm tắt nhanh khi rê chuột vào bất kỳ thuật ngữ gạch chân nào (tự ẩn khi rời chuột, cuộn trang, click hoặc mất tiêu điểm).
  * Cập nhật `insert_with_glossary()` dùng `parse_rich_segments()` hiển thị chữ xanh gạch chân (`MES` gạch chân, không ký hiệu rác); tự động làm sạch `[[...]]` khi hiển thị code/mathbox, khi Copy cẩm nang/thuật ngữ, và trong `job_storage.export_job_markdown()`.
  * Bổ sung nút cẩm nang thứ 14 `📋 Kế Hoạch, RTY & ISO` vào Tab Kho Tài Liệu, ánh xạ `_resolve_doc_key()` và thêm `planning_ehs_cost` vào `TECH_CATALOG` của `job_analyzer.py`.
- **Cơ Sở Dữ Liệu (`job_detail.db`) & Cẩm Nang Tổng Hợp (`CamNang_ToanDien_OE_CADIVI_MienTrung.md`)**:
  * Cập nhật **Job ID 1** lên **14 cẩm nang offline**, **8 tài liệu chính thống**, **112 câu hỏi phỏng vấn** và ma trận kỹ năng đầy đủ.
  * Tái xuất [CamNang_ToanDien_OE_CADIVI_MienTrung.md](file:///c:/Users/games/Desktop/Project/Python/Python%20MyWork/Project2/JobDetail/CamNang_ToanDien_OE_CADIVI_MienTrung.md): **514,425 ký tự / 5,042 dòng**, gồm **161 neo `<a id="term-..."></a>`** ở Phần IV và **1,015 liên kết nội bộ `[DisplayText](#term-slug)`** (0 liên kết gãy, 0 `[[` rò rỉ, 0 dấu `$`).

### 3. Kết Quả Kiểm Thử Thực Tế (Gate 2 — Definition of Done)
- **Kiểm tra cú pháp (`py_compile`)**: 9/9 file `.py` thành công (0 lỗi).
- **Bộ kiểm thử tự động (`unittest -v`)**: **29/29 unit tests OK trong 11.368s** (`test_job_storage.py`, `test_job_analyzer.py`, `test_qa_and_viewer.py`) — gồm kiểm thử tách nghĩa công thức `ABC Cable` vs `Cycle Counting` / `PD`, kiểm thử 100% công thức hợp lệ, kiểm thử headless 20/20 `OfflineDocViewer` không rò rỉ `[[`, kiểm thử `TermHoverTooltip` và 161 thuật ngữ AST không trùng lặp.
- **Đo tốc độ thực tế sau nâng cấp**: `_display_job_detail(1)` = **22.7 ms**, render 112 câu phỏng vấn + gắn link thuật ngữ = **219.2 ms**, mở `TermDetailPopup` lần đầu = **207.0 ms**.
- **Giới hạn chưa tự verify trực quan**: Hiển thị trực quan màu sắc/đường gạch chân `MES` và vị trí nổi của Live Hover Tooltip trên màn hình thật cần người dùng mở `Run_JobDetail.bat` để kiểm tra bằng mắt.

---

## 2026-11-22 (Nâng cấp — Giai đoạn 4: Gói A + B + C & Sửa Lỗi Gõ CV) — Đùn Cáp Chuyên Sâu, Thực Địa OE & Test Vòng 2, Render Markdown Sạch, TOC/`Ctrl+F`, Chế Độ Luyện Phỏng Vấn & Lưu Tiến Độ SQLite

### 1. Bối Cảnh & Mục Tiêu
- Kiểm toán toàn diện kho tri thức, giao diện `JobDetailApp.py`, bộ test và hồ sơ cá nhân trong `cv/` theo yêu cầu người dùng, chốt triển khai trọn gói **A + B + C** và sửa lỗi gõ `"đ cải tiến"` trong dữ liệu CV (giữ đúng phạm vi đã duyệt, không thêm Gói D).

### 2. Các Thành Phần & Cải Tiến Đã Triển Khai
- **Gói A — Hoàn Thiện Kiến Thức Chuyên Sâu Cáp Điện, OE Thực Địa & Bộ Đề Thi Thực Hành Vòng 2**:
  * **Kho Cẩm Nang (`offline_knowledge.py`) — Mở rộng `20 → 22 Cẩm Nang` (16 Sản Xuất/Cáp Điện + 6 IT)**:
    1. Thêm mới **`cable_extrusion_wire_forensics`** (4 tầng Basic → Expert): Trục vít `L/D Ratio` & tỷ số nén (`PVC` vs `XLPE` vs `LSZH`), giám sát `Melt Pressure / Melt Temperature`, công thức `DDR / DRB` chọn bộ Chày–Cối (Pressure vs Tube Tooling), ma trận 5 khuyết tật đùn (`Sharkskin`, `Bambooing`, `Die Drool`, `Voids`, `Scorch`), bài toán `CaCO3 Filler` / `Specific Gravity` (chi phí theo thể tích) & quản trị nhựa tái chế `Regrind`, phân tích mặt gãy đứt sợi đồng `Wire Break Forensics` (`Cup-and-Cone` vs `Inclusion` ASTM B49 vs `Weld Break`), cáp đặc chủng `Solar Cable H1Z2Z2-K` (`Tinned Copper`, `E-beam`), `Braiding`, `Water-Blocking` và đường biên pháp lý `QCVN 4` / `MOC / ECN`.
    2. Thêm mới **`oe_field_execution_case_test`** (4 tầng Basic → Expert): `Work Sampling` (công thức Tippett), `Headcount Planning` (3 ca 4 kíp & Luật Lao động VN) + `Learning Curve 80%`, `Loss Tree / OEE Waterfall` & `Cost Deployment` (WCM), hệ duy trì bền vững `LSW + LPA + Escalation Matrix (SLA)`, KPI Bảo trì (`PM Compliance`, `Wrench Time`, `CBM / PdM`), kèm **3 Đề Thi Thực Hành Vòng 2 OE CADIVI** (Đề 1 Excel 5 ca máy đùn OEE `74.16%` & BOM Variance; Đề 2 Case Study đơn hàng tăng +35% giải cứu xưởng Đùn 122%; Đề 3 Thuyết trình A3/ROI đầu tư Laser Gauge).
    3. Chuẩn hóa tiêu đề đủ 4 tầng (`TẦNG 1 → TẦNG 4`) cho 2 cẩm nang `oee` và `smed`.
  * **Ngân Hàng Phỏng Vấn (`interview_bank.py`) — Mở rộng `112 → 128 Câu Hỏi` (`17 Chủ Đề`)**: Thêm **Nhóm 17** gồm 16 câu chuyên sâu (`q_adv_01`..`q_adv_16`) về đùn cáp, phân tích đứt sợi, `Work Sampling`, `Cost Deployment`, `LSW/LPA`, `Wrench Time`, bài test Excel 5 ca, `MOC/ECN` & phản biện CV/lương CADIVI.
  * **Từ Điển Thuật Ngữ (`term_glossary.py`) — Mở rộng `161 → 190 Thuật Ngữ` (0 trùng lặp AST)**: Thêm 29 thuật ngữ chuyên ngành mới đầy đủ định nghĩa, công thức, áp dụng & ví dụ thực tế tại CADIVI; 100% trường dữ liệu sạch không chứa `**`, `[[`, `$`, LaTeX và 100% `related` trỏ khóa chính hợp lệ.
  * **Bộ Phân Tích (`job_analyzer.py`)**: Đăng ký `extrusion_forensics` & `oe_field_test` trong `TECH_CATALOG` & `mfg_core` để JD sản xuất/cáp điện tự động gắn đủ 16 cẩm nang và 128 câu hỏi.
- **Gói B — Sửa Lỗi Hiển Thị Markdown Thô & Nâng Cấp Trình Đọc `OfflineDocViewer` (`JobDetailApp.py`)**:
  * Nâng cấp `insert_with_glossary()` render sạch định dạng nội dòng **`**in đậm**`** (tag `bold_inline` + `term_link_bold` kết hợp gạch chân cyan) và **`` `inline_code` ``** (tag `inline_code` Consolas) → triệt tiêu hoàn toàn 466 chuỗi `**` thô trên màn hình.
  * Bổ sung **Mục lục nhảy nhanh (TOC ComboBox)** và **Tìm kiếm trong bài (`Ctrl+F` / `Enter` / `F3` / `Shift+F3`)** highlight tất cả kết quả và nhảy từng vị trí trong `OfflineDocViewer`.
- **Gói C — Lưu Tiến Độ Bền Vững Vào SQLite & Chế Độ Luyện Phỏng Vấn Chủ Động (`job_storage.py`, `JobDetailApp.py`)**:
  * Tự động migrate an toàn thêm cột `progress_json` vào bảng `jobs` trong `job_detail.db` (bảo toàn 100% dữ liệu cũ) kèm API `get_progress()` / `save_progress()`.
  * Tab Lộ Trình 90 Ngày hiển thị thanh `% hoàn thành` và tự động lưu ngay mỗi lần tích `☐ ↔ ☑` xuống SQLite.
  * Tab Phỏng Vấn tích hợp công tắc **`🎯 Chế độ Luyện Phỏng Vấn (Ẩn đáp án)`**, nút `👁️ Xem/Ẩn gợi ý trả lời` cho từng câu & toàn bộ, đánh dấu `✅ Đã thuộc` / `🔁 Cần ôn lại` lưu bền vững vào SQLite, bộ lọc theo trạng thái ôn và chỉ số `% Sẵn sàng phỏng vấn` giữ nguyên vị trí cuộn khi thao tác.
- **Sửa Lỗi Chính Tả CV (`cv/Page/CV_CADIVI_OE_Du_Lieu.json`)**: Sửa `"đ cải tiến"` → `"đã cải tiến"` và xác nhận JSON UTF-8 hợp lệ.
- **Cập Nhật CSDL (`job_detail.db`) & Cẩm Nang Tổng Hợp (`CamNang_ToanDien_OE_CADIVI_MienTrung.md`)**:
  * Cập nhật Job ID 1 đủ **16 cẩm nang offline**, **10 tài liệu chính thống**, **128 câu hỏi** và ghi chú ôn tập 5 ngày.
  * Tái xuất [CamNang_ToanDien_OE_CADIVI_MienTrung.md](file:///c:/Users/games/Desktop/Project/Python/Python%20MyWork/Project2/JobDetail/CamNang_ToanDien_OE_CADIVI_MienTrung.md): **600,922 ký tự / 5,738 dòng**, **190 neo `<a id="term-..."></a>`** và **1,375 liên kết nội bộ** (0 liên kết gãy, 0 `[[`, 0 `$`).

### 3. Kết Quả Kiểm Thử Thực Tế (Gate 2 — Definition of Done)
- **Kiểm tra cú pháp (`py_compile`)**: 9/9 file `.py` thành công (0 lỗi).
- **Bộ kiểm thử tự động (`unittest -v`)**: **30/30 unit tests OK trong 10.315s** (`test_job_storage.py` 5/5 gồm lưu & nạp lại `progress_json`, `test_job_analyzer.py` 5/5, `test_qa_and_viewer.py` 20/20 gồm 22 cẩm nang 0 `**` thô & 0 `[[`, TOC & `Ctrl+F`, chế độ Ẩn/Hiện đáp án 128 câu, 190 thuật ngữ AST 0 trùng lặp).
- **Đo tốc độ thực tế sau nâng cấp**: `_display_job_detail(1)` = **18.8 ms**, render 128 câu chế độ đầy đủ = **354.5 ms**, chế độ Luyện Phỏng Vấn (ẩn đáp án) = **127.3 ms**.
- **Giới hạn chưa tự verify trực quan**: Giao diện hiển thị thực tế của chữ in đậm + link xanh gạch chân, thanh TOC/`Ctrl+F` và chế độ Luyện Phỏng Vấn ẩn đáp án chạy kiểm thử headless nên cần người dùng mở `Run_JobDetail.bat` để trải nghiệm trực quan; đồng thời nếu dùng bản PDF CV cũ trong `cv/Page/` thì bạn nhớ mở lại CV Studio nạp file JSON đã sửa để xuất lại bản PDF mới.


---

## 2026-11-22 (Nâng cấp — Giai đoạn 5) — Sửa Triệt Để Lỗi Click Thuật Ngữ, Làm Sâu 202/202 Định Nghĩa & Xây Dựng Giáo Trình Tự Học OE A–Z (8 Học Phần / 32 Bài)

### 1. Bối Cảnh & Phản Hồi Từ Người Dùng
- Người dùng gửi ảnh chụp cửa sổ định nghĩa `Six Sigma` phản hồi 3 vấn đề trọng tâm:
  1. Nhiều từ gạch chân bên trong popup bấm vào "không thấy gì xảy ra" (ví dụ: `Six Sigma`, `Lean Six Sigma`, `Green Belt`).
  2. Nhiều định nghĩa thuật ngữ còn quá ngắn (trung vị chỉ ~200–260 ký tự), thiếu phân tích chi tiết và ví dụ cụ thể từ đời sống đến nhà máy thực tế.
  3. Cần một **Giáo trình học từ đầu (từng bài một)** đầy đủ để tự học bài bản đáp ứng vị trí Chuyên viên OE CADIVI Miền Trung.

### 2. Chẩn Đoán Nguyên Nhân Gốc & Các Thay Đổi Đã Triển Khai
- **Xóa Sổ 100% Lỗi Click Chết & Nuốt Click (`term_glossary.py`, `JobDetailApp.py`)**:
  * **Sửa 590 tự-link (self-links)**: Bổ sung tham số `exclude_key` trong `insert_with_glossary()` và truyền `exclude_key=cur_key` trong `TermDetailPopup` & `GlossaryBrowserDialog` — tên của chính thuật ngữ đang mở sẽ hiển thị chữ in đậm rõ ràng (không gạch chân tự-link về chính mình).
  * **Tách 12 khái niệm bị gộp alias thành 12 mục từ điển độc lập** (`term_glossary.py`, tăng `190 → 202` thuật ngữ, chuẩn hóa gọn về 8 nhóm danh mục): `Green Belt`, `Lean Six Sigma`, `HMI`, `MSA`, `p-value`, `Drum-Buffer-Rope`, `Bottleneck`, `Jishu Hozen`, `Red Tag`, `Pull System`, `Campaign Scheduling`, `Standard Work`. Nhờ đó bấm `Green Belt` hay `Lean Six Sigma` trong `Six Sigma` đều mở ngay trang định nghĩa riêng biệt.
  * **Chống nuốt click khi chuột rung nhẹ 1–5px**: Nâng cấp `bind_glossary_links()` gắn `<ButtonPress-1>` + widget-level `<ButtonRelease-1>`; chỉ bỏ qua khi người dùng thực sự kéo bôi đen copy (`dist > 5px` và có vùng chọn `sel`), ngược lại xóa `sel` lạc và mở thuật ngữ chính xác (kể cả rung nhẹ khỏi ký tự mép).
- **Làm Sâu Toàn Diện 202/202 Thuật Ngữ (`glossary_enrichment.py` — file mới, tự động nạp bởi `term_glossary.py`)**:
  * Mở rộng toàn bộ 202/202 thuật ngữ thành bài giảng mini chi tiết: độ dài trung vị **Định nghĩa** tăng từ `260 → 876 ký tự` (+237%), **Áp dụng CADIVI** `194 → 450 ký tự` (+132%), **Ví dụ thực tế & số liệu** `198 → 752 ký tự` (+280%, gồm ví dụ trực quan đời sống + tính toán thực chiến tại CADIVI).
  * Bổ sung **Mục 5 `⚠️ Sai lầm kinh điển cần tránh & Mẹo thực chiến OE`** và ánh xạ **`lesson_id`** cho 202/202 thuật ngữ.
  * Nâng cấp `TermDetailPopup` & `GlossaryBrowserDialog`: thêm **Thanh đường dẫn lịch sử Breadcrumb** (`Six Sigma › Green Belt`), nút **`🎓 Học Bài Lx.y`** nhảy thẳng sang bài giáo trình liên kết và hiển thị Mục 5 sai lầm cần tránh (bao gồm cả khi Copy).
- **Xây Dựng Giáo Trình Tự Học Từ Đầu A–Z (`oe_curriculum.py`, `JobDetailApp.py`, `job_storage.py`, `GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md`)**:
  * Tạo mới **`oe_curriculum.py`**: **8 Học Phần / 32 Bài Học Tuần Tự** (`L1.1 → L8.3`, tổng thời lượng tự học ~28 giờ 30 phút), mỗi bài gồm đủ 6 phần: Mục tiêu học tập, Kiến thức cốt lõi (dùng công thức `[[TermKey|Text]]` bấm tra cứu mọi nơi), Ví dụ số liệu giải chi tiết, Bài tập thực hành (Hands-on Drill), 3 câu hỏi tự kiểm tra Checkpoint (tổng 96 Checkpoint) và Từ khóa trọng tâm, liên kết trực tiếp tới Cẩm Nang sâu (`doc_key`) & Chủ đề Phỏng vấn (`interview_category`).
  * Tích hợp **Tab mới `🎓 Giáo Trình A–Z`** vào `JobDetailApp.py` (C-Engine `tk.Listbox` + `tk.Text` 60fps, lọc theo 8 Học phần, nút `☐/☑ Đánh dấu đã học xong`, `⬅ Bài trước` / `Bài tiếp ➡`, `📖 Cẩm Nang Sâu`, `❓ Luyện Câu Hỏi` tự lọc đúng chủ đề phỏng vấn) + hỗ trợ render sạch chữ nghiêng `*italic*`.
  * Cập nhật `job_storage.py` lưu thêm khóa `"curriculum"` trong `progress_json` của SQLite (tự động bảo toàn tiến độ học tập sau khi tắt/mở lại ứng dụng).
  * Tái xuất [CamNang_ToanDien_OE_CADIVI_MienTrung.md](file:///c:/Users/games/Desktop/Project/Python/Python%20MyWork/Project2/JobDetail/CamNang_ToanDien_OE_CADIVI_MienTrung.md) (**7,488 dòng / 1,251.4 KB**, 202 neo thuật ngữ, 1,436 link nội bộ, 202 link sang Giáo Trình, 0 link gãy, 0 `[[`, 0 `$`) và xuất mới [GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md](file:///c:/Users/games/Desktop/Project/Python/Python%20MyWork/Project2/JobDetail/GiaoTrinh_OE_CADIVI_Tu_A_Den_Z.md) (**1,137 dòng / 164.6 KB**, 32 neo bài học, 32 link mục lục, 688 link thuật ngữ sang Cẩm Nang, 0 link gãy, 0 `[[`, 0 `$`).

### 3. Kết Quả Kiểm Thử Thực Tế (Gate 2 — Definition of Done)
- **Kiểm tra cú pháp (`py_compile`)**: **11/11 file `.py`** thành công (0 lỗi).
- **Bộ kiểm thử tự động (`unittest -v`)**: **32/32 unit tests OK trong 13.847s** (`test_job_storage.py` 5/5 gồm lưu/nạp `"curriculum"`, `test_job_analyzer.py` 5/5, `test_qa_and_viewer.py` 22/22 gồm: 202/202 thuật ngữ AST duy nhất & đạt độ dài chuẩn + 0 token lỗi, quét **0/202 self-links**, 8 Học phần / 32 bài học 100% hợp lệ, kiểm thử headless `JobDetailApp` Tab Giáo Trình + Popup `Six Sigma` nhảy sang `Green Belt` + Breadcrumb).
- **Kiểm thử chống rung chuột (Click-Tremor vs Drag-Select)**: 3/3 kịch bản thực tế trên cửa sổ Tkinter mapped đều PASS (rung 3px có chọn 1 ký tự vẫn mở đúng `Green Belt`; kéo bôi đen 30px không bật popup nhầm; click thuần 0px mở đúng).
- **Kiểm thử render toàn bộ 32 bài & tốc độ**: Mở bài `L1.1` = **71.8 ms**, mở Popup `Six Sigma` = **140.7 ms**, nhảy thẳng từ Popup sang bài `L4.2` = **OK**, quét cả 32/32 bài có **0 rò rỉ** `[[`, `]]`, `**`, `$`; 0 câu lệnh `print()` debug thừa và không còn file tạm trong thư mục.
- **Giới hạn chưa tự verify trực quan**: Hiển thị bố cục 7 tab, màu sắc Breadcrumb/Mục 5 Sai lầm cần tránh và trải nghiệm click trực tiếp trên màn hình thực tế cần người dùng mở `Run_JobDetail.bat` để kiểm tra bằng mắt.
