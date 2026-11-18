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

---

## 2026-11-18 — Nâng Cấp Hệ Thống JobDetail Lên 100% Tri Thức Offline Độc Lập

### 1. Bối Cảnh & Mục Tiêu
- Giải quyết triệt để yêu cầu vận hành trong môi trường Offline / Zero-Internet của người dùng.
- Thay vì phụ thuộc vào liên kết web trình duyệt, toàn bộ tài liệu, công thức, phần mềm, SOP và cẩm nang kỹ thuật được đóng gói trực tiếp vào ứng dụng `JobDetail`.

### 2. Thành Phẩm Đã Hoàn Thành
- **`offline_knowledge.py`**: Tích hợp 16 cẩm nang kỹ thuật chuyên sâu (10 cẩm nang Sản xuất / Lean / OEE / OLE / SMED / BOM / Minitab / AutoCAD / SAP-MES và 6 cẩm nang Công nghệ thông tin Python / React / Docker / SQL / Redis / Git).
- **`JobDetailApp.py`**: Tích hợp trình đọc cẩm nang `OfflineDocViewer` ngay trong giao diện, banner 10 cẩm nang truy cập nhanh phản hồi <10ms, nút `[📖 Đọc Cẩm Nang]` nổi bật cho từng mục tài liệu và phần mềm, badge `🟢 100% Offline Mode`.
- **`job_analyzer.py` & `job_detail.db`**: Tự động gán `doc_key` cho mọi tài liệu, cập nhật CSDL SQLite với đầy đủ 3 hồ sơ công việc đa dạng (Lean Engineer, Senior Python Backend, Junior React Frontend).
- **Kiểm thử**: Đạt 9/9 unit tests (100% pass), `py_compile` không lỗi cú pháp.

---

## 2026-11-18 (Nâng cấp) — Trực Quan Hóa Khung Hộp Toán Học & Sửa Lỗi Hiển Thị LaTeX

### 1. Bối Cảnh & Thành Quả
- Xử lý phản hồi của người dùng về việc các công thức toán học (OEE, OLE, BOM, Minitab SPC) bị lộ chuỗi LaTeX thô trên giao diện Desktop Tkinter.
- Chuyển đổi 100% các công thức sang định dạng **Visual Math Box (Khung Hộp Toán Học Trực Quan)** bằng font Monospace `Consolas` và ký tự Unicode (`───`, `×`, `→`, `≥`, `≤`, `σ`, `μ`).
- Nâng cấp `OfflineDocViewer` với cơ chế tô màu tiêu đề Markdown và bộ lọc tự động làm sạch LaTeX (`_sanitize_math_markup`).
- Toàn bộ 16 cẩm nang hiển thị sắc nét, chuyên nghiệp, căn lề thẳng hàng 100% không phụ thuộc internet.

---

## 2026-11-18 (Nâng cấp) — Xóa Bỏ Lỗi KeyError: 'surface2', Xây Dựng Ngân Hàng 56 Câu Hỏi Phỏng Vấn Thực Chiến & Nâng Cấp Bộ Lọc Đa Chiều

### 1. Bối Cảnh & Thành Quả
- Khắc phục triệt để lỗi KeyError: 'surface2' khi mở cẩm nang trong JobDetailApp.py, bổ sung màu an toàn vào THEME.
- Xây dựng module interview_bank.py với 56 câu hỏi phỏng vấn & tình huống thực chiến đa dạng, 100% không trùng lặp thuộc 10 chủ đề công nghiệp (OEE, OLE, Cân bằng chuyền, SMED, 7 Lãng phí, Poka-Yoke, BOM, SPC/Cpk, Layout xưởng, ERP/MES).
- Nâng cấp giao diện Tab '❓ Phỏng Vấn & Thực Chiến' với thanh tìm kiếm tức thì theo từ khóa, combobox chọn lọc 10 chủ đề, nhãn hiển thị số lượng câu hỏi và card câu hỏi phân màu sắc chuyên nghiệp.
- Cập nhật job_analyzer.py tự động nạp 56 câu hỏi cho JD Sản xuất, đồng thời cập nhật CSDL job_detail.db bản ghi Job ID 1.
- Xây dựng test suite 	est_qa_and_viewer.py và chạy vòng lặp kiểm tra: 21/21 unit tests đạt 100% (bao gồm cả kiểm tra render UI và headless 16 cẩm nang).

---

## 2026-11-18 (Nâng cấp) — Nâng Cấp Toàn Diện Tri Thức OLE & Hệ Thống Cẩm Nang Tinh Gọn Từ Basic Đến Expert (Kèm 3 Case Study Thực Chiến)

### 1. Bối Cảnh & Thành Quả
- Nâng cấp cẩm nang OLE từ 3,534 ký tự lên 20,713 ký tự với cấu trúc 4 tầng kiến thức chuẩn công nghiệp (Basic -> Intermediate -> Advanced -> Expert).
- Tích hợp 3 Case Study thực tế có số liệu thực tế tại xưởng và giải pháp Kaizen chi tiết:
  * Case Study 1: OLE cho 1 công nhân ca 8h (Availability=90.91%, Utilization=80.00%, Quality=95.00% -> OLE=69.09%).
  * Case Study 2: Line OLE cho chuyền 10 công nhân và bài toán chi phí lương thất thoát.
  * Case Study 3: Cân bằng chuyền 5 trạm, biểu đồ Yamazumi, Smoothness Index (SI), tăng LBE từ 69.05% lên 93.79%.
- Bổ sung chuyên sâu cho các cẩm nang: OEE vs TEEP & CAPEX 24/7; SMED Case study ép nhựa 85p xuống 8p40s (giảm 89.8%) với kịch bản song song 2 người F1 Pit-stop; BOM Variance cho lô 10,000 cụm van cơ khí & Kitting/Two-bin Kanban; SPC Minitab Case study tiện trục 25mm tính Cp/Cpk/Ppk & 4 quy tắc Nelson Rules.
- Chạy toàn bộ 23/23 unit tests pass 100%, render mượt mà trong chế độ Offline 100% không cần Internet.

---

## 2026-11-18 (Nâng cấp) — Triệt Tiêu 100% Ký Hiệu LaTeX Thô & Lỗi Escape Chuỗi Python (Toàn Bộ 16 Cẩm Nang & 56 Câu Hỏi)

### 1. Bối Cảnh & Thành Quả
- Xử lý dứt điểm hiện tượng chuỗi LaTeX bị escape nhầm thành ký tự Tab (\t -> 	imes, 	ext) và Carriage Return (\r -> ightarrow) cùng các dấu $ thô trên giao diện Desktop Tkinter.
- Rà soát làm sạch toàn bộ 16 cẩm nang kỹ thuật và 56 câu hỏi trong interview_bank: 100% chuyển sang ký tự Unicode chuẩn (×, →, Ø, μ, σ, ≥, ≤, ±).
- Chuẩn hóa chính xác đoạn Chi phí Lương Lãng phí: số liệu và công thức hiển thị sắc nét, thẳng hàng.
- Nâng cấp bộ lọc phòng thủ _sanitize_math_markup trong JobDetailApp.py và đồng bộ CSDL SQLite job_detail.db.
- Chạy 24/24 unit tests đạt 100% thành công trong 3.941 giây.
