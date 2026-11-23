# PrivateVault — Ứng Dụng Bảo Mật Folder Portable (Zero-Admin)

Ứng dụng Desktop bảo vệ các thư mục dự án/tài liệu trên Windows **không cần quyền quản trị (Admin)**, có thể copy sang nhiều máy và chạy ngay.

## Tính năng chính
1. **Mặc định khóa cứng & ẩn hoàn toàn:** Khi chưa nhập mật khẩu, toàn bộ dữ liệu nằm ở dạng mã hóa **AES-256-GCM** (cả nội dung lẫn tên file), không xuất hiện thư mục thật trên máy.
2. **Nhập mật khẩu 1 lần mỗi ngày:** Xác thực 1 lần để sử dụng suốt ngày (thu nhỏ xuống System Tray), tự động khóa cứng khi qua `00:00` sang ngày mới hoặc khi thoát/tắt máy.
3. **Kiến trúc Lai (Hybrid) cho từng Folder:**
   - **Ổ đĩa ảo WebDAV (`virtual_webdav`):** Gắn thành ổ đĩa thật (VD: `Z:\`) qua `WebClient` có sẵn của Windows, giải mã trực tiếp trên RAM (`0%` file rõ chạm ổ cứng), mở/khóa `< 1 giây`. Phù hợp tài liệu & dự án có file `< 50 MB`.
   - **Vault cục bộ (`local_sync`):** Dùng cho dự án nặng (file `> 50 MB` hoặc nhiều file code). Giải mã ra vùng làm việc tốc độ ổ cứng thật khi mở khóa và tự động đồng bộ mã hóa ngược + xóa an toàn bản rõ khi khóa.
4. **3 chế độ Xóa dữ liệu không thể phục hồi (Crypto-Shredding):**
   - **Chế độ A:** Nút xóa vĩnh viễn từng folder hoặc xóa sạch toàn bộ Vault ngay lập tức.
   - **Chế độ B:** Tự động hủy toàn bộ dữ liệu nếu nhập sai mật khẩu quá `N` lần.
   - **Hẹn giờ xóa:** Đặt mốc ngày/giờ cụ thể hoặc đếm ngược tự hủy (kiểm tra liên tục khi chạy và kiểm tra ngay lúc khởi động app).

## Cách sử dụng & cài đặt trên nhiều máy
1. Copy toàn bộ thư mục này sang máy tính Windows bất kỳ có cài **Python 3.10+**.
2. Nhấp đúp **`Run_PrivateVault.bat`** — ứng dụng sẽ tự động cài các thư viện cần thiết ở chế độ `--user` (không cần Admin) trong lần chạy đầu tiên và mở giao diện.

## Lưu ý quan trọng
- **Không thể khôi phục nếu quên mật khẩu** (mã hóa thật AES-256-GCM + Scrypt).
- Mọi dữ liệu mã hóa nằm trong thư mục ẩn `vault_data/` đặt cùng chỗ với `main.py` — copy cả thư mục dự án sang USB/máy khác là mang theo được toàn bộ Vault.
