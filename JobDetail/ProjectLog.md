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
- Unit Tests: `test_job_storage.py` (4/4 passed), `test_job_analyzer.py` (3/3 passed).
- Data Persistence: SQLite hoạt động ổn định, dữ liệu lưu trữ bền vững.
- Đồng bộ Rules & Skills: Đã đồng bộ 27 Skills và 11 Rules sang kho trung tâm và toàn cục máy tính qua `sync_skills_rules.py --push-all`.
