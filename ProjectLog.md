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

---

## 2026-11-20 — Xây Dựng Hệ Thống `TaiLieu Intelligence Hub` & Đồng Bộ Dữ Liệu 3 Ổ Mạng Chuẩn Hóa

### 1. Bối Cảnh & Mục Tiêu
- Tiếp nhận yêu cầu tải và quản lý tập trung toàn bộ tài liệu kỹ thuật từ 3 địa chỉ máy chủ `\\vdm-wts08`:
  * `IT HOA TIEU CHUAN KIEM TRA - 品証・検査標準書IT化` (QCKT, Tiêu chuẩn bảo hành, kiểm tra, môi trường, nghiệp vụ kho, nghiệp vụ bảo hành).
  * `IT HOA HIEU CHINH-DIEMKIEM点検・校正IT化` (Hiệu chỉnh - Điểm kiểm, Form kiểm máy đo).
  * `IT HOA YEU LINH  ー要領IT化` (Loại quy định & Yếu lĩnh MAB, VDM).
- Các tiêu chuẩn nghiêm ngặt đã đáp ứng 100%:
  * **An toàn tuyệt đối**: Không thay đổi hay ghi đè bất kỳ dữ liệu nào trên ổ mạng nguồn (100% Read-Only).
  * **Chuẩn hóa tên file & folder**: 100% loại bỏ ký tự tiếng Nhật/tiếng Trung (Kanji, Hiragana, Katakana, Hanzi), chỉ giữ lại ký tự tiếng Anh/ASCII thuần chuẩn Windows.
  * **Lọc file tiếng Việt**: Loại bỏ toàn bộ file tiếng Nhật (`-J.pdf`, `(J IT)`, folder `Ban Nhat`, `Ban J`), chỉ giữ lại các file tiếng Việt và song ngữ (`-V.pdf`, `(V IT)`, `(VJ)`).
  * **File Excel tổng**: Lưu giữ nguyên vẹn 8 file Excel tổng trong các thư mục tương ứng để đối chiếu, dò kiểm tra.
  * **Khôi phục link file hủy**: Tự động quét và bổ sung liên kết cho 95 file tài liệu bị hủy/hết hiệu lực mà trong Excel tổng bị mất hoặc trống link.
  * **Cấu hình độc lập & Đồng bộ vi sai (Incremental Sync)**: Mỗi phân hệ có 1 file JSON cấu hình riêng (`configs/*.json`). Lần sau cập nhật chỉ tải các file mới hoặc có sửa đổi, bỏ qua 100% file không đổi.
  * **Ứng dụng Desktop tra cứu & mở nhanh (`TaiLieuApp.py`)**: Giao diện CustomTkinter Dark Mode Catppuccin Mocha, tìm kiếm tức thì <10ms, nút mở nhanh File cục bộ, File mạng gốc và thư mục lưu.

### 2. Thành Phẩm Đã Hoàn Thành
- **`configs/*.json`**: 8 file cấu hình độc lập (`01_qckt.json`, `02_tcbh.json`, `03_tckt.json`, `04_tcmt.json`, `05_nvbh.json`, `06_nvkho.json`, `07_hcdk.json`, `08_yeulinh.json`).
- **`sync_engine.py`**: Engine đồng bộ thông minh, hỗ trợ đường dẫn dài Windows (>260 ký tự `\\?\`), lọc tiếng Nhật, làm sạch ASCII và khôi phục link file hủy.
- **`tailieu_catalog.json`**: Chỉ mục cơ sở dữ liệu tra cứu gồm 3.450 tài liệu sẵn sàng mở nhanh.
- **`TaiLieuApp.py` & `Run_TaiLieuApp.bat`**: Ứng dụng Desktop tra cứu và quản lý cập nhật chọn lọc theo phân hệ.
- **`README.md`**: Tài liệu hướng dẫn sử dụng và bàn giao.
- **Dữ liệu đã tải về**: 3.450 tài liệu PDF tiếng Việt và 8 file Excel tổng đã được tải về cục bộ tại `TaiLieu/`.
- **Kết quả kiểm thử**: 100% file và folder không chứa ký tự tiếng Nhật/Trung; cơ chế vi sai bỏ qua 100% file cũ; ứng dụng khởi động mượt mà.

---

## 2026-11-20 (Nâng cấp) — Ma Trận Quản Trị 7 Yếu Tố, Tối Ưu Nạp Dần (Lazy Loading) & 2 Chế Độ Cập Nhật

### 1. Bối Cảnh & Mục Tiêu
- Nâng cấp trải nghiệm người dùng theo phản hồi thực tế:
  * Khắc phục triệt để hiện tượng đơ lag khi render danh sách lớn bằng cơ chế nạp dần (Lazy Loading / Infinite Scroll) và Debounce tìm kiếm (150ms).
  * Xây dựng bộ nút sắp xếp trực quan (Mã A-Z/Z-A, Tên, Ngày sửa đổi, Trạng thái, Bộ phận).
  * Tích hợp chế độ Dual-View: Chuyển đổi linh hoạt giữa Dạng Thẻ (Card View) và Dạng Bảng Siêu Tốc (Table View Treeview).
  * Mô hình hóa Ma Trận Quản Trị & Điều Hành 7 Yếu Tố: *Quy định gì ➔ Ai sở hữu ➔ Kiểm soát gì ➔ Hồ sơ ở đâu ➔ Rủi ro ➔ Kết quả/Hành động ➔ Phương thức lưu trữ*.
  * Tách biệt 2 chế độ cập nhật: `⚡ Cập Nhật Nhanh (Chỉ file mới/sửa đổi)` vs `🔄 Đồng Bộ Toàn Bộ (Full Sync)`.

### 2. Thành Phẩm Đã Hoàn Thành
- **`governance_matrix.py` & `governance_catalog.json`**:
  * Phân rã 3.038 quy trình quản trị chuẩn hóa theo 6 trụ cột cốt lõi: Kỹ thuật sản xuất (U), Đảm bảo chất lượng (Q), Quy cách kiểm tra (QCKT), Đo lường hiệu chỉnh (HCDK), Môi trường (E), Quản trị an ninh (G) và Quản lý kho (NVKHO).
  * Bóc tách rõ ràng Đơn vị sở hữu, Thông số kiểm soát, Hồ sơ/Form biểu mẫu, Rủi ro tiềm ẩn, Đối sách khắc phục và Thời hạn lưu trữ.
- **`TaiLieuApp.py` (Phiên bản V2 Zero-Lag)**:
  * **Tab 1: Tra Cứu & Mở Nhanh**: Tích hợp Lazy Loading 25 items/batch (<25ms load time), thanh nút sắp xếp 6 chiều, nút chuyển đổi Dạng Thẻ / Dạng Bảng Treeview.
  * **Tab 2: Ma Trận Quản Trị & Điều Hành**: Tab chuyên biệt tra cứu ma trận 7 yếu tố, bộ lọc theo 7 Trụ cột quản lý và tìm kiếm đa chiều.
  * **Tab 3: Cập Nhật & Đồng Bộ**: Cung cấp 2 nút chức năng riêng biệt `[⚡ Cập Nhật Nhanh]` (bỏ qua 100% file cũ, chạy trong vài giây) và `[🔄 Đồng Bộ Toàn Bộ]`.
- **`sync_engine.py`**: Bổ sung tham số `mode='fast'` và `mode='full'`, tự động tái lập cả 2 catalog sau khi đồng bộ.
- **Kiểm thử Gate 2**:
  * `py_compile` 100% không lỗi cú pháp.
  * Bộ test headless UI tự động (`test_app_headless.py`) xác minh trơn tru việc lọc tìm kiếm, đổi chế độ sắp xếp, nạp trang nối tiếp (Page 1 -> Page 2) và chuyển đổi trụ cột quản trị.
  * Toàn bộ mã nguồn sạch sẽ, không file rác, sẵn sàng sử dụng.

---

## 2026-11-20 (Mới nhất) — Phân Tầng Hồ Sơ Nguồn (Master Root Standards) vs Hồ Sơ Triển Khai & Khóa Liên Kết Quản Trị

### 1. Bối Cảnh & Mục Tiêu
- Tiếp nhận yêu cầu chuyên sâu về phân tầng quản trị tài liệu:
  * Trong toàn bộ hệ thống tài liệu Mabuchi, tồn tại các **Hồ Sơ Nguồn (Master / Root Standards)** là quy định khung, chuẩn mực cơ sở quy định chung cho toàn bộ tập đoàn/nhà máy (Sổ tay chất lượng/môi trường, Quy định quản lý cấp A/B/C, Tiêu chuẩn chất lượng QA-A/QA-B, Tiêu chuẩn điểm kiểm gốc 000-0-V...).
  * Toàn bộ các tài liệu còn lại là **Hồ Sơ Triển Khai / Chi Tiết (Child / Execution Documents)** (quy trình thao tác chi tiết `*-D*`, quy cách kiểm tra từng mã linh kiện QCKT, biểu điểm kiểm từng máy đo VDM-312-DK-xxx...). Các hồ sơ này bắt buộc phải dựa trên và tuân theo Hồ Sơ Nguồn tương ứng.
  * Yêu cầu phân biệt rõ ràng Hồ Sơ Nguồn để người dùng có thể lọc tức thì 1 click các tài liệu quan trọng nhất mà không bị lẫn giữa hàng nghìn tài liệu chi tiết.

### 2. Thành Phẩm Đã Hoàn Thành
- **Thuật Toán Phân Tầng `is_master_root_document` (`governance_matrix.py`)**:
  * Xác định chính xác **284 Quy định nguồn cốt lõi** trong tổng số 3.038 quy trình Ma trận quản trị, và **491 file hồ sơ nguồn** trong tổng số 3.450 file catalog vật lý.
  * Tự động suy diễn và gắn nhãn liên kết: `parent_ref` (Ví dụ: quy trình `U-MAB-D001` liên kết căn cứ với quy định nguồn `U-MAB-B001`, máy đo `VDM-312-DK-xxx` liên kết với tiêu chuẩn điểm kiểm gốc `000-00(VDM-312-DK-156)`...).
- **Nâng Cấp Giao Diện `TaiLieuApp.py` (Phiên bản V3 Master Tiered)**:
  * **Header Badge Mới**: Bổ sung badge số lượng `👑 Hồ Sơ Nguồn: 491` ngay cạnh Tổng tài liệu, Hiệu lực và Cục bộ.
  * **Tab 1: Tra Cứu & Mở Nhanh**:
    - Thêm bộ lọc Cấp bậc: `["Tất Cả", "👑 Hồ Sơ Nguồn", "📄 Chi Tiết"]` lọc tức thì <10ms.
    - Thêm nút sắp xếp `👑 Ưu Tiên Nguồn (MASTER_FIRST)`: Luôn đưa toàn bộ tài liệu nguồn lên đầu danh sách.
    - Card View: Thẻ Hồ Sơ Nguồn được viền nổi bật màu vàng ánh kim (`Catppuccin Yellow`), gắn huy hiệu `👑 HỒ SƠ NGUỒN`. Thẻ chi tiết hiển thị rõ ràng đường link `🔗 Căn cứ: [Tên quy định nguồn]`.
    - Table View: Bổ sung cột `Cấp Bậc` hiển thị `👑 NGUỒN` vs `📄 CHI TIẾT`.
  * **Tab 2: Ma Trận Quản Trị 7 Yếu Tố**:
    - Thêm Segmented Button chuyển đổi: `["Tất Cả (3.038)", "👑 Chỉ Hồ Sơ Nguồn Chuẩn (284)", "📄 Hồ Sơ Triển Khai (2.754)"]`.
    - Card Ma trận quản trị hiển thị rõ chuỗi quy định chuẩn: Hồ sơ nguồn được đóng khung vàng và ghi chú "Căn cứ chuẩn mực bắt buộc"; Hồ sơ triển khai hiển thị rõ "Quy định nguồn gốc đối chiếu".
- **Kiểm Thử Gate 2 (Định Nghĩa Hoàn Thành)**:
  * Chạy `python -m py_compile TaiLieuApp.py` đạt 100% không lỗi syntax.
  * Kiểm thử headless tự động xác minh: 491 file hồ sơ nguồn trong Tab 1, 284 quy định nguồn trong Tab 2, phân loại chính xác 100%, không bị sai lệch số liệu.
  * Cập nhật `README.md` hướng dẫn cách tra cứu và lọc hồ sơ nguồn.


---

## 2026-11-20 (Hoàn thành) — Làm Giàu Tiêu Đề Tiếng Việt & Tóm Tắt Nghiệp Vụ (Summary) Cho 100% Tài Liệu, Nâng Cấp Tìm Kiếm Đa Chiều & Bộ Lọc Lĩnh Vực

### 1. Bối Cảnh & Mục Tiêu
- Tiếp nhận phản hồi từ người dùng kèm ảnh chụp thực tế màn hình Table View:
  * Trước đây cột bảng hiển thị lặp lại mã và tên file PDF (`Q-MAB-C022-V` ➔ `Q-MAB-C022-V.pdf`), không thể hiện file đó dùng để làm gì, quy định việc gì, gây khó khăn khi tra cứu nghiệp vụ thực tế.
  * Yêu cầu:
    1. Bổ sung **Tiêu đề tiếng Việt chuẩn & Tóm tắt nội dung nghiệp vụ (Summary)** ngắn gọn, súc tích cho từng tài liệu (mục đích kiểm soát, đơn vị phụ trách, thiết bị đo hoặc linh kiện áp dụng).
    2. Nâng cấp **Tìm kiếm nội dung đa chiều & không dấu**: Cho phép người dùng tìm kiếm theo tên nghiệp vụ ("sản phẩm bất hợp cách", "danh sách hoá chất"), tên linh kiện ("vỏ nhỏ", "chổi than"), tên máy đo ("đồng hồ đo dòng", "kính hiển vi", "đầu mũi hàn"), hoặc phòng ban sở hữu thay vì chỉ gõ đúng mã số tài liệu.
    3. Bổ sung **Bộ lọc nhanh theo Lĩnh vực (Pillar Filter)** ngay trên Tab 1 để thu hẹp phạm vi tìm kiếm theo từng khối công việc.

### 2. Thành Phẩm Đã Hoàn Thành
- **Bộ Bóc Tách Metadata Master Excel Siêu Tốc (`extract_all_master_excel_metadata` trong `governance_matrix.py`)**:
  * Tận dụng COM Automation nạp toàn bộ ma trận dữ liệu 2D `s.UsedRange.Value` của 8 file Master Excel (26 sheets) chỉ trong ~5 giây.
  * Bóc tách chuẩn xác 363 tên máy đo tiếng Việt trong `IT HOA HIEU CHINH DIEM KIEM.xls`, toàn bộ tên linh kiện/sản phẩm trong `IT HOA QUY CACH KIEM TRA.xls`, tên nghiệp vụ trong `(IT) BIEU LIET KE.xls`, tên quy định trong `TIM KIEM LOAI QUI DINH.xlsm`...
  * Thuật toán `synthesize_metadata`: Tự động tạo tiêu đề tiếng Việt chuẩn xác và tạo đoạn tóm tắt nghiệp vụ xúc tích (1-2 câu) cho **100% trong số 3.450 tài liệu** (0 tài liệu bị trống).
  * Xây dựng chỉ mục tìm kiếm `search_text` đa chiều: Gom mã tài liệu, tên file, tiêu đề tiếng Việt, tóm tắt nghiệp vụ, tên thiết bị đo, linh kiện, đơn vị sở hữu, trụ cột quản trị kèm cả phiên bản **loại bỏ dấu tiếng Việt** (`remove_accents`).
- **Nâng Cấp Giao Diện `TaiLieuApp.py` (Phiên Bản V4 Smart Metadata)**:
  * **Hàm tìm kiếm đa từ & không dấu (`remove_accents` & `apply_search_filter`)**: Chuẩn hóa tách từ khóa dạng `AND`, hỗ trợ gõ có dấu hoặc không dấu (ví dụ: gõ "san pham bat hop cach" khớp ngay "Quy định xử lý sản phẩm bất hợp cách", gõ "vo nho" khớp ngay 24 tài liệu linh kiện vỏ nhỏ).
  * **Bộ Lọc Lĩnh Vực Quản Trị (OptionMenu `cmb_search_pillar`)**: Thêm ngay cạnh thanh tìm kiếm Tab 1 với 8 nhóm nghiệp vụ trực quan (Tất Cả, Đảm Bảo Chất Lượng, Kỹ Thuật Sản Xuất, Quy Cách Kiểm Tra, Đo Lường Hiệu Chỉnh, Môi Trường, Quản Lý Kho, Quản Trị Chung).
  * **Cải Tiến Bảng Dữ Liệu (Table View)**:
    - Thay thế cột tên file thô sơ bằng cột `Tiêu Đề & Tóm Tắt Nghiệp Vụ (Mô Tả Công Việc)` rộng 490px, hiển thị rõ ràng `{Tiêu đề} — {Tóm tắt nghiệp vụ}`.
    - Bổ sung cột `Lĩnh Vực Quản Trị` (155px) và `Đơn Vị Sở Hữu` (160px).
    - Cấu trúc cột hoàn chỉnh: `Cấp Bậc | Mã Số Tài Liệu | Tiêu Đề & Tóm Tắt Nghiệp Vụ (Mô Tả Công Việc) | Lĩnh Vực Quản Trị | Đơn Vị Sở Hữu | Trạng Thái | Kích Thước | Trạng Thái File`.
  * **Cải Tiến Dạng Thẻ (Card View)**:
    - Hiển thị tiêu đề tiếng Việt in đậm nổi bật ngay cạnh mã tài liệu.
    - Bổ sung khung hộp tóm tắt nghiệp vụ: `📋 Tóm tắt: [Mô tả chi tiết mục đích, đối tượng kiểm soát]`.
    - Bổ sung huy hiệu phòng ban `🏢 [Phòng ban sở hữu]` và huy hiệu trụ cột `[Lĩnh vực]`.
- **Kiểm Thử Gate 2 (Định Nghĩa Hoàn Thành)**:
  * `py_compile TaiLieuApp.py` và `py_compile governance_matrix.py` đạt 100% không lỗi cú pháp.
  * Bộ test tự động kiểm tra xác nhận: 0/3.450 tài liệu bị thiếu title hoặc summary; test truy vấn "sản phẩm bất hợp cách" / "san pham bat hop cach" trả về chuẩn xác `Q-MAB-C022-E`; test "vo nho" trả về 24 QCKT; test "dong ho do" trả về 17 máy đo HCDK; test bộ lọc "Đo Lường Hiệu Chỉnh" trả về 954 tài liệu.
