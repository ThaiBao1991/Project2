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
