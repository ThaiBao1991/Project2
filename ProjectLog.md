# Nhật Ký Dự Án Trung Tâm (Master ProjectLog) — Project 2

Tài liệu nhật ký trung tâm theo dõi kiến trúc, kho kỹ năng/quy tắc và các phân hệ dự án trong `Project 2`.

---

## 2026-11-17 — Khởi Tạo Không Gian Làm Việc `Project 2` & Đồng Bộ Skills / Rules

### 1. Bối Cảnh & Mục Tiêu
- Tiếp nhận và thiết lập không gian làm việc `Project 2` kế thừa toàn bộ 27 Skills và 11 Rules từ kho trung tâm `GravityCode`.
- Thiết lập kho dự phòng cục bộ `Project 2\SettingAILocal` và runtime `.agents`.
- Chuẩn bị nền tảng để phát triển dự án mới `JobDetail` chuyên về phân tích, lập lộ trình và tra cứu JD.

### 2. Các Thành Phần Đã Triển Khai
- **Đồng Bộ Runtime `.agents`**:
  * Sao chép toàn bộ 27 Skills và 11 Rules vào `.agents/skills` và `.agents/rules`.
  * Đồng bộ các file chỉ thị cốt lõi: `AGENTS.md`, `GEMINI.md`, `mcp_config.json`, `plugins.json`, `skills.json`.
- **Kho Trung Tâm Cục Bộ `SettingAILocal`**:
  * Trang bị công cụ `sync_skills_rules.py` tự động thích ứng với đường dẫn máy tính `12953 Bao`.
  * Trang bị giao diện desktop `SkillRuleApp.py` và launcher `Run_SkillRuleHub.bat`.
- **Quy Chuẩn & Kỹ Năng Mới**:
  * Đã bổ sung Rule: `job_detail_analysis_rules.md` (Mô hình 5 Tầng Kiến Thức cho JD).
  * Đã bổ sung Skill: `job_detail_analyzer` (Quy trình bóc tách JD và hướng dẫn prompt AI).
- **Trạng thái đồng bộ**: Đạt 100% nhất quán giữa Project 1 (`GravityCode`), Project 2 (`SettingAILocal`), Global (`~/.gemini/config`) và các runtime `.agents`.

---

## 2026-11-17 (Hoàn thành) — Triển Khai Hoàn Tất Dự Án `JobDetail Intelligence Hub`

### 1. Bối Cảnh & Thành Quả
- Đã hoàn thành 100% ứng dụng `JobDetail` theo đúng yêu cầu:
  * Cho phép nhập JD (văn bản thô hoặc file) và phân tích từ đơn giản đến chi tiết.
  * Phân rã theo Mô hình 5 Tầng Kiến Thức: Tổng quan, Ma trận kỹ năng, Lộ trình Onboarding 3 chặng, Danh mục tài liệu & từ khóa tra cứu, Bộ câu hỏi phỏng vấn sát sườn.
  * Hỗ trợ lưu trữ CSDL SQLite bền vững và tra cứu đa chiều (tìm kiếm tức thì, lọc Level, Ngành nghề, Trạng thái).
  * Giao diện Desktop CustomTkinter 60fps zero-lag (Catppuccin Mocha Dark Mode).
  * Đầy đủ bộ unit tests (`test_job_storage.py`, `test_job_analyzer.py`), launcher `Run_JobDetail.bat` và `README.md`.
- Trạng thái: Sẵn sàng đưa vào sử dụng thực tế.

---

## 2026-11-17 — Xây Dựng CV Khớp JD Điều Độ / Quản Lý Sản Xuất & Đo Lường

### 1. Bối Cảnh & Mục Tiêu
- Tạo bản CV chuyên nghiệp chuẩn HTML/CSS theo mẫu `JobDetail\cv\Page\ApplyMaBuChi.html`, tối ưu hóa trực tiếp cho JD vị trí Quản lý / Điều độ sản xuất & Cải tiến.
- Tiếp nhận và phản ánh trung thực 100% dữ liệu thực tế từ ứng viên (không bịa đặt số liệu KPI hay kỹ năng chưa từng làm):
  * Làm việc tại Công ty TNHH Mabuchi Motor Đà Nẵng từ 2022 đến nay.
  * Thăng tiến lên Nhóm trưởng Phòng Kiểm tra từ tháng 07/2025.
  * Khả năng lập trình Python, VBA (ứng dụng Microsoft Access, Excel) phục vụ quản lý dữ liệu kiểm tra và nâng cao hiệu suất công việc.
  * Tự động hóa đo lường trên các máy đo kiểm: Keyence LM-X Series, OGP SmartScope, INEX.
  * Đào tạo tiêu chuẩn ISO/IEC 17025; thực hiện Kaizen, 5S và cải thiện tiết giảm số công lao động.

### 2. Thành Phẩm & Kiểm Thử
- **File tạo mới**: `JobDetail\cv\Page\ApplyLeanProductionLeader.html`
- **Kết quả xác minh (Gate 2)**:
  * Cú pháp HTML: 0 thẻ mở/đóng lỗi, tương thích hoàn toàn chuẩn UTF-8 tiếng Việt.
  * Đường dẫn tài nguyên: Liên kết chính xác CSS (`style.css`), Font Awesome, Bootstrap và Avatar cá nhân (`assets/img/avatar.jpg`).
  * Bố cục 2 cột: Tối ưu hiển thị màn hình và chuẩn in ấn khổ A4 / xuất PDF.
- **Trạng thái**: Hoàn thành, sẵn sàng nộp hồ sơ hoặc mở trên trình duyệt.
