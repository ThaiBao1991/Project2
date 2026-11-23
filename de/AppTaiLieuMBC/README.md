# TÀI LIỆU INTELLIGENCE HUB — HỆ THỐNG TRA CỨU & ĐỒNG BỘ TÀI LIỆU KỸ THUẬT

Hệ thống quản lý, tải tự động, tra cứu tốc độ cao và mở nhanh liên kết các bộ tài liệu kỹ thuật chuẩn hóa từ 3 phân hệ máy chủ `\\vdm-wts08`:
1. `\\vdm-wts08\IT HOA TIEU CHUAN KIEM TRA - 品証・検査標準書IT化`
2. `\\vdm-wts08\IT HOA HIEU CHINH-DIEMKIEM点検・校正IT化`
3. `\\vdm-wts08\IT HOA YEU LINH  ー要領IT化`

---

## 🌟 CÁC TÍNH NĂNG NỔI BẬT

### 1. Cơ Chế Cập Nhật Vi Sai Độc Lập (Incremental & Selective Sync)
- **Tách biệt 8 phân hệ theo 8 file cấu hình độc lập (`configs/*.json`)**:
  - `01_qckt.json`: Quy Cách Kiểm Tra (QCKT)
  - `02_tcbh.json`: Tiêu Chuẩn Bảo Hành (TCBH)
  - `03_tckt.json`: Tiêu Chuẩn Kiểm Tra (TCKT)
  - `04_tcmt.json`: Tiêu Chuẩn Môi Trường (TCMT)
  - `05_nvbh.json`: Nghiệp Vụ Bảo Hành (NVBH)
  - `06_nvkho.json`: Nghiệp Vụ Kho (NVKHO)
  - `07_hcdk.json`: Hiệu Chỉnh - Điểm Kiểm (HCDK)
  - `08_yeulinh.json`: Loại Quy Định / Yếu Lĩnh MAB & VDM
- **Tải vi sai thông minh (Incremental Update)**: Chỉ kiểm tra và tải các file mới hoặc có sửa đổi trên máy chủ. Toàn bộ các file không đổi sẽ được **bỏ qua ngay lập tức** (< 1 giây), tiết kiệm tối đa băng thông mạng LAN.
- **Tùy chọn mục cập nhật**: Người dùng có thể tích chọn cập nhật riêng lẻ từng phân hệ hoặc cập nhật tất cả.

### 2. Chuẩn Hóa Tên File & Thư Mục
- **Loại bỏ 100% ký tự tiếng Nhật/tiếng Trung** (Kanji, Hiragana, Katakana, Hanzi) trên tên file và thư mục cục bộ.
- Chỉ giữ lại bảng chữ cái tiếng Anh/ASCII thuần chuẩn hệ thống tệp Windows (`A-Z, a-z, 0-9, _, -, .`).
- **Lọc chỉ lấy bản tiếng Việt**: Tự động loại bỏ các file tiếng Nhật (`-J.pdf`, `(J IT)`, thư mục `Ban Nhat`, `Ban J IT HOA`), chỉ tập trung tải các file tiếng Việt (`-V.pdf`, `(V IT)`, `(VJ)`, thư mục `Ban Viet`, `Ban V`).

### 3. Phục Hồi & Bổ Sung Link Cho Các File Đã Hủy
- Dò tìm tự động cả các thư mục chứa từ khóa "Hủy", "Huy", "Hủy bỏ", "HUY BO", "Haishi" trên ổ mạng.
- Tự động map và bổ sung liên kết chuẩn xác cho các mã tài liệu (ví dụ: `E-MAB-C001`, `Q-MAB-D023`, `Q-MAB-D029`, `U-MAB-D075`, `U-MAB-D082`...) mà trên file Excel tổng bị trống hoặc mất link do thư mục bị đổi tên.

### 4. Phân Tầng Hồ Sơ Nguồn (Master Root) vs Hồ Sơ Triển Khai
- **👑 Hồ Sơ Nguồn (Master / Root Standards)**: Các quy định khung, chuẩn mực cơ sở quy định chung cho toàn bộ tập đoàn/nhà máy:
  - Sổ tay chất lượng (`Q-MAB-Z001`), Sổ tay môi trường (`E-MAB-Z001`).
  - Quy định khung quản lý cấp A/B/C (`G-MAB-A*`, `G-MAB-B*`, `Q-MAB-B*`, `E-MAB-C*`, `U-MAB-C*`, `G-VDM-B*`, `Q-VDM-B*`).
  - Tiêu chuẩn bảo hành toàn bộ (`QA-A`, `QA-B`), Tiêu chuẩn kho vận gốc (`ZA-A-04`).
  - Tiêu chuẩn điểm kiểm gốc (`000-0-V`, `000-00(VDM-312-DK-156)`).
- **📄 Hồ Sơ Triển Khai / Chi Tiết (Execution Detail Documents)**: Các văn bản triển khai thực thi (quy trình thao tác chi tiết `*-D*`, quy cách kiểm tra từng mã linh kiện QCKT, biểu điểm kiểm từng máy đo VDM-312-DK-xxx...).
- **Đường dẫn liên kết quản trị (`parent_ref`)**: Mọi văn bản chi tiết đều hiển thị rõ "Căn cứ theo quy định nguồn nào" để đối chiếu nhanh.
- **Lọc & Sắp Xếp Ưu Tiên**: 1-Click lọc tức thì chỉ xem Hồ Sơ Nguồn hoặc bật chế độ sắp xếp `👑 Ưu Tiên Nguồn` đưa tài liệu chuẩn lên đầu.

### 5. Tiêu Đề Tiếng Việt, Tóm Tắt Nghiệp Vụ & Tìm Kiếm Đa Chiều Không Dấu
- **100% tài liệu được làm giàu Metadata từ 8 Master Excel**:
  - Bóc tách tự động tên 363 máy đo trong file Hiệu Chỉnh Điểm Kiểm (`IT HOA HIEU CHINH DIEM KIEM.xls`), tên linh kiện trong Quy Cách Kiểm Tra (`IT HOA QUY CACH KIEM TRA.xls`), tên quy định trong Yếu Lĩnh (`TIM KIEM LOAI QUI DINH.xlsm`), tên nghiệp vụ bảo hành...
  - Mỗi tài liệu đều có **Tiêu đề tiếng Việt** rõ ràng và **Tóm tắt nội dung nghiệp vụ** (1-2 câu súc tích mô tả mục đích kiểm soát, rủi ro ngăn ngừa, đơn vị sở hữu).
- **Tìm kiếm đa từ & không dấu (Accent-free Multi-word AND Search)**:
  - Cho phép gõ tìm kiếm bằng tiếng Việt có dấu hoặc không dấu (ví dụ: `san pham bat hop cach`, `vo nho`, `dong ho do`, `mui han`, `kiem tra chat luong`...).
  - Tìm kiếm đồng thời trên: Mã tài liệu, Tên file, Tiêu đề, Tóm tắt công việc, Tên linh kiện/thiết bị đo, Đơn vị sở hữu và Phân hệ quản lý.
- **Bộ Lọc Lĩnh Vực Quản Trị (Pillar Filter)**: 1-click lọc nhanh theo 8 lĩnh vực ngay tại Tab 1 (Tất Cả, Đảm Bảo Chất Lượng, Kỹ Thuật Sản Xuất, Quy Cách Kiểm Tra, Đo Lường Hiệu Chỉnh, Môi Trường, Quản Lý Kho, Quản Trị Chung).
- **Hiển Thị Bảng (Table View) Trực Quan**: Cột thứ 3 hiển thị chi tiết `Tiêu Đề & Tóm Tắt Nghiệp Vụ (Mô Tả Công Việc)` rộng 490px, kèm theo cột `Lĩnh Vực Quản Trị` và `Đơn Vị Sở Hữu`, loại bỏ hoàn toàn việc lặp lại tên file PDF vô nghĩa.

### 6. Ma Trận Quản Trị & Điều Hành 7 Yếu Tố
- **Tab chuyên biệt "🏛️ Ma Trận Quản Trị & Điều Hành"**:
  - Mô hình hóa chuẩn hóa: *Quy định gì ➔ Ai sở hữu ➔ Dữ liệu kiểm soát gì ➔ Hồ sơ/Form ở đâu ➔ Rủi ro tiềm ẩn ➔ Kết quả/Xử lý ➔ Phương thức & Thời hạn lưu trữ*.
  - Phân loại theo 6 Trụ cột quản trị cốt lõi:
    - 🔧 Kỹ Thuật Sản Xuất (U)
    - 🛡️ Đảm Bảo Chất Lượng (Q)
    - 🔍 Quy Cách Kiểm Tra Linh Kiện (QCKT)
    - 📏 Đo Lường Hiệu Chỉnh Thiết Bị (HCDK)
    - 🌿 Môi Trường & An Toàn Hóa Chất (E)
    - 🏢 Quản Trị Chung & An Ninh Dữ Liệu (G)
    - 📦 Quản Lý Kho Vận & Vật Tư (NVKHO)

### 7. Hiệu Năng Vượt Trội Zero-Lag (CustomTkinter Performance Rules)
- **Nạp dần (Lazy Loading / Infinite Scroll)**: Phân trang theo khối 25 tài liệu/lần kết hợp Debounce tìm kiếm 150ms, loại bỏ hoàn toàn hiện tượng nghẽn UI khi duyệt 3.450 tài liệu.
- **Chế độ Dual-View**: Chuyển đổi linh hoạt giữa Dạng Thẻ (Card View) trực quan và Dạng Bảng (Table View Treeview) cực nhanh.
- **2 Chế độ Cập nhật rõ ràng**:
  - `⚡ Cập Nhật Nhanh (Chỉ File Mới/Thay Đổi)`: Bỏ qua 100% file không đổi, chỉ tải bổ sung file mới trong vài giây.
  - `🔄 Đồng Bộ Toàn Bộ (Full Deep Sync)`: Quét sâu toàn diện toàn bộ ổ mạng.

### 8. Quản Lý Kho Lưu Trữ Tách Biệt, Di Chuyển, Đổi Link & Xóa Tài Liệu (Tab 4)
- **Tách riêng dữ liệu PDF nặng khỏi thư mục App Python + Data**:
  - Thư mục App chỉ giữ lại mã nguồn Python (`.py`, `.bat`) và dữ liệu nhẹ (`configs/*.json`, `tailieu_catalog.json`, `governance_catalog.json`, `app_settings.json`, tùy chọn `master_excels/`).
  - Toàn bộ kho PDF (~2,16 GB) có thể di chuyển sang bất kỳ ổ đĩa hoặc thư mục nào khác (ví dụ `D:\KhoTaiLieuMBC`); mọi lần mở file và đồng bộ sau đó đều tự động dùng kho mới.
- **Di chuyển toàn bộ / theo phân hệ / theo tài liệu đã chọn (Tự động đổi link)**:
  - Hỗ trợ kiểm tra dung lượng đĩa trống, copy-verify-delete an toàn (chỉ xóa nguồn sau khi khớp kích thước đích), hỗ trợ đường dẫn dài Windows (`\\?\`) và dừng an toàn giữa chừng.
  - Trên **Tab 1**: bấm nút `⋯` trên từng Thẻ hoặc giữ `Ctrl`/`Shift` chọn nhiều dòng trong **Dạng Bảng** để Di chuyển, Đổi link hoặc Xóa hàng loạt.
- **Cập nhật địa chỉ kho / Đổi link không cần di chuyển file (Relink)**:
  - Khi người dùng tự Cut/Copy thư mục PDF bằng Windows Explorer sang chỗ khác, chỉ cần trỏ thư mục mới → ứng dụng tự động cập nhật liên kết và hỗ trợ **Dò tìm thông minh theo tên file** nếu cấu trúc thư mục con đã thay đổi.
  - Hỗ trợ sửa riêng đường dẫn cục bộ & đường dẫn ổ mạng cho từng tài liệu.
- **Xóa tài liệu an toàn với 3 chế độ + Thùng Rác Windows**:
  1. *Chỉ xóa file PDF trên ổ cứng* (giải phóng dung lượng, giữ danh mục tra cứu & link ổ mạng để tải lại sau).
  2. *Xóa file PDF trên ổ cứng VÀ xóa khỏi danh mục ứng dụng*.
  3. *Chỉ xóa khỏi danh mục ứng dụng* (giữ nguyên file vật lý).
  - Mặc định đưa file vào **Thùng Rác Windows** để có thể khôi phục khi cần; tích hợp nút dọn nhanh toàn bộ PDF Đã Hủy trên ổ cứng.

---

## 🚀 HƯỚNG DẪN KHỞI CHẠY

### Cách 1: Khởi động giao diện 1-Click (Tự động cài thư viện & tự đóng CMD)
Nhấp đúp chuột vào file:
```cmd
Run_TaiLieuApp.bat
```
- Lần đầu chạy trên máy mới, ứng dụng sẽ **tự động kiểm tra và cài đặt thư viện còn thiếu** (`customtkinter`, `pywin32`), có hộp thoại sao chép lệnh cài thủ công dự phòng nếu máy bị chặn mạng/proxy (hoặc chạy `python -m pip install -r requirements.txt`).
- Khi đóng cửa sổ ứng dụng, cả tiến trình Python lẫn cửa sổ CMD đều tự động thoát sạch hoàn toàn.

### Cách 2: Chạy trực tiếp từ dòng lệnh
```bash
python TaiLieuApp.py
```

### Cách 3: Chạy đồng bộ từ terminal (CLI)
```bash
python sync_engine.py
```

---

## 📁 CẤU TRÚC THƯ MỤC CỤC BỘ

```text
TaiLieu/
├── 01_TIEU_CHUAN_KIEM_TRA/
│   ├── IT HOA BAN QCKT/                   (Kèm Excel tổng: IT HOA QUY CACH KIEM TRA.xls)
│   ├── IT HOA TIEU CHUAN BAO HANH/        (Kèm Excel tổng: IT HOA TIEU CHUAN BAO HANH(MMK).xls)
│   ├── IT HOA TIEU CHUAN KIEM TRA/        (Kèm Excel tổng: IT HOA TIEU CHUAN KIEM TRA.xls)
│   ├── IT HOA TIEU CHUAN MOI TRUONG/      (Kèm Excel tổng: IT HOA TIEU CHUAN MOI TRUONG.xls)
│   ├── IT HOA TIEU CHUAN NGHIEP VU BAO HANH/ (Kèm Excel tổng: (IT) BIEU LIET KE.xls)
│   └── IT HOA TIEU CHUAN NGHIEP VU KHO/   (Kèm Excel tổng: IT HOA TIEU CHUAN NGHIEP VU KHO.xls)
├── 02_HIEU_CHINH_DIEM_KIEM/
│   ├── IT HOA HIEU CHINH DIEM KIEM.xls    (File Excel tổng)
│   └── Ban V (Hieu Chinh Diem Kiem)/      (Toàn bộ PDF tiếng Việt)
├── 03_YEU_LINH_QUI_DINH/
│   ├── TIM KIEM LOAI QUI DINH.xlsm        (File Excel tổng)
│   ├── Loai quy dinh MAB/                 (Toàn bộ PDF tiếng Việt -V kể cả mục Hủy)
│   └── Loai quy dinh VDM/                 (Toàn bộ PDF tiếng Việt/Song ngữ VJ)
├── configs/                               (8 file cấu hình JSON độc lập từng phân hệ)
├── master_excels/                         (Tùy chọn: 8 file Excel tổng được giữ gọn tại App khi dời PDF)
├── app_settings.json                      (Cấu hình địa chỉ kho PDF tách biệt & lịch sử dời kho)
├── storage_manager.py                     (Module quản lý kho, di chuyển, đổi link & xóa an toàn)
├── sync_engine.py                         (Engine đồng bộ vi sai & phục hồi link)
├── governance_matrix.py                   (Engine ma trận quản trị 7 yếu tố & làm giàu metadata)
├── tailieu_catalog.json                   (Chỉ mục dữ liệu tra cứu tốc độ cao)
├── governance_catalog.json                (Chỉ mục ma trận quản trị 7 yếu tố)
├── TaiLieuApp.py                          (Ứng dụng Desktop tra cứu, quản trị & quản lý kho)
├── requirements.txt                       (Danh sách thư viện phụ thuộc dự phòng)
├── Run_TaiLieuApp.bat                     (Khởi động 1-click chuẩn CRLF, tự đóng CMD khi thoát)
└── README.md                              (Tài liệu hướng dẫn)
```
