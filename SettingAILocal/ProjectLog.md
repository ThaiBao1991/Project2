# Nhật Ký Dự Án (ProjectLog) — SettingAILocal (Project 2)

Tài liệu nhật ký theo dõi kiến trúc, kho kỹ năng, quy tắc dùng chung và lịch sử đồng bộ giữa Project 1 và Project 2.

---

## 2026-11-05 — Khởi Tạo Hub Dự Án 2 & Thiết Lập Đồng Bộ 2 Chiều Project 1 $\Leftrightarrow$ Project 2

### 1. Bối Cảnh & Mục Tiêu
- Người dùng chỉ thị: Thiết lập kho lưu trữ kỹ năng (skills) và quy tắc (rules) từ Project 1 (`.../Project1`) sang Project 2 (`.../Project2/SettingAILocal`).
- Bổ sung điều luật và cơ chế kỹ thuật để mọi skill/rule mới trong Project 1 sẽ tự động đồng bộ sang Project 2, và ngược lại mọi skill/rule mới trong tương lai tại Project 2 sẽ tự động đồng bộ ngược về Project 1 và đẩy lên Toàn Cục (`~/.gemini/config/`).

### 2. Các Thành Phần Đã Triển Khai
1. **Kho Lưu Trữ Hub 2**:
   - Sao chép và chuẩn hóa đầy đủ 25 Skills và 10 Rules sang `Project2/SettingAILocal/`.
   - Tạo thư mục runtime `.agents/` chuẩn hóa cho Project 2 để Antigravity IDE tự động kích hoạt.
2. **Cơ Chế Đồng Bộ 2 Chiều (`sync_skills_rules.py`)**:
   - Nâng cấp thuật toán đồng bộ 2 chiều (`sync_directory_bidirectional`) giữa Hub 1 (Project 1) và Hub 2 (Project 2).
   - Cơ chế so sánh thời gian sửa đổi (`mtime`), phiên bản mới hơn sẽ tự động cập nhật phiên bản cũ hơn.
   - Tự động đẩy ra Global (`~/.gemini/config`) và các Workspace runtime `.agents`.
   - Hỗ trợ các cờ lệnh: `--sync-all` (`--push-all`), `--check`, `--harvest`.
3. **Bộ Quy Chuẩn & Luật Đồng Bộ Mới**:
   - Bổ sung **Điều 2: Luật Đồng Bộ 2 Chiều Bắt Buộc (Cross-Project Bidirectional Sync Rule)** vào `skill_rule_sync_protocol.md` và `workflow_rules.md`.
   - Cập nhật Gate 2 Checklist mục 8 trong `workflow_rules.md`: Agent bắt buộc tự động chạy `python sync_skills_rules.py --sync-all` trước khi kết thúc task.
   - Cập nhật quy tắc toàn cục `~/.gemini/config/AGENTS.md`.
4. **Giao Diện Quản Trị Desktop**:
   - Triển khai `SkillRuleApp.py` và `Run_SkillRuleHub.bat` tại `SettingAILocal` để tra cứu Markdown và kích hoạt đồng bộ 1 chạm.

