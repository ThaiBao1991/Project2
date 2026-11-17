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
