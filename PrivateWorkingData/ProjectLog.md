# ProjectLog - PrivateVault (Ứng dụng Bảo Mật Folder Portable)

## 1. Mục tiêu dự án
Xây dựng ứng dụng Desktop Windows **PrivateVault** chạy hoàn toàn Portable (không cần quyền Admin, copy sang nhiều máy chạy ngay):
- Quản lý và thêm/bớt các folder dự án/tài liệu cần bảo vệ.
- Mặc định khóa cứng: không có mật khẩu thì không thấy folder và không truy cập được.
- Xác thực mật khẩu **1 lần mỗi ngày** (giữ phiên trong RAM qua System Tray, tự động khóa cứng khi qua `00:00` sang ngày mới hoặc khi thoát/tắt máy).
- **Kiến trúc Lai (Hybrid)**:
  - `virtual_webdav`: Ổ đĩa ảo mã hóa AES-256-GCM giải mã on-the-fly trong RAM qua Windows `WebClient` (Zero-Admin, mở/khóa `< 1s`, giới hạn `< 50MB/file`).
  - `local_sync`: Vault cục bộ cho folder nặng / có file `> 50MB` (giải mã ra vùng làm việc khi mở khóa, tự động đồng bộ mã hóa ngược & xóa an toàn bản rõ khi khóa).
- **3 chế độ Xóa không thể phục hồi (Crypto-Shredding + Secure Wipe)**:
  - Chế độ A: Nút xóa vĩnh viễn thủ công (từng folder hoặc toàn bộ Vault).
  - Chế độ B: Tự động hủy dữ liệu nếu nhập sai mật khẩu quá `N` lần.
  - Chế độ Hẹn giờ xóa: Hẹn ngày/giờ cụ thể hoặc đếm ngược tự hủy (kiểm tra nền liên tục và kiểm tra ngay lúc khởi động app).

## 2. Môi trường thực tế đã kiểm tra
- OS: Windows (tài khoản domain `VDM\12953 Bao`, `InAdminGroup: False` — không có quyền Admin).
- Python: `3.10.10`.
- Windows `WebClient`: `Running` (`FileSizeLimitInBytes = 50000000`).

## 3. Nhật ký thay đổi
- **2026-11-23**:
  - Hoàn thành toàn bộ mã nguồn ứng dụng **PrivateVault** gồm: `bootstrap.py`, `crypto_engine.py`, `policy_manager.py`, `webdav_mount.py`, `main.py`, `Run_PrivateVault.bat`, `README.md`.
  - Đã chạy kiểm tra cú pháp (`py_compile`), tự động cài đặt thành công `WsgiDAV`, `cheroot`, `pystray` bằng `--user` không cần quyền Admin.
  - Đã chạy bộ kiểm thử E2E thực tế trên máy không có Admin (`VDM\12953 Bao`):
    - `[PASS]` Khởi tạo Vault, Scrypt + AES-256-GCM, từ chối mật khẩu sai, đổi mật khẩu.
    - `[PASS]` Gắn ổ đĩa ảo bảo mật thực tế tại `Z:\` không cần Admin, đọc/ghi tệp đa chunk tiếng Việt Unicode trực tiếp trên `Z:\`, ngắt ổ & biến mất hoàn toàn khi khóa.
    - `[PASS]` Chuyển chế độ Lai `virtual_webdav` ↔ `local_sync`, đồng bộ chỉnh sửa và xóa sạch bản rõ `work/` khi khóa.
    - `[PASS]` Phiên 1 lần/ngày (tự hết hạn khi sang `00:00` ngày mới), Chế độ B (đếm sai mật khẩu chạm ngưỡng `N`), và Chế độ Hẹn giờ xóa.
    - `[PASS]` Chế độ A: Xóa vĩnh viễn từng folder và Crypto-Shredding toàn bộ Vault.
  - Trạng thái: Sẵn sàng sử dụng (chưa tự kiểm thử tương tác chuột trực tiếp trên cửa sổ GUI & System Tray — cần người dùng mở `Run_PrivateVault.bat` kiểm tra giao diện thực tế).
- **2026-11-23 (Cập nhật UX & Tự động khóa theo giờ)**:
  - Sửa `export_and_remove_folder()` trong `crypto_engine.py` và hộp thoại **Gỡ & Xuất** trong `main.py`: giải mã & chuyển trực tiếp tệp/thư mục con vào đúng thư mục đích người dùng chọn (hết tình trạng tạo lồng `A\A`), đồng thời gợi ý mở sẵn thư mục gốc ban đầu.
  - Bổ sung chế độ **Tự động khóa theo khoảng giờ (`1h`, `2h`, `4h`, `8h` hoặc nhập tùy ý như `0.5h`)** song song với chế độ `1 lần/ngày (00:00)` trong `policy_manager.py` và tab `Thiết lập Xóa & Bảo mật` của `main.py`, kèm đồng hồ đếm ngược phiên trên Header.
  - Đã kiểm thử tự động: `[PASS]` xuất trực tiếp vào `A` không lồng `A\A`, `[PASS]` tự khóa theo giờ (`2h`, `0.5h`, lưu bền vững ra disk) và chế độ `daily`.
