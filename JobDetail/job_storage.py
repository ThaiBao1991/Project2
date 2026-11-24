#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
job_storage.py - Module Lưu Trữ & Quản Lý Cơ Sở Dữ Liệu Hồ Sơ Công Việc (JobDetail)
Sử dụng SQLite local database với đầy đủ tính năng CRUD, tìm kiếm đa chiều,
thống kê và trích xuất báo cáo Markdown / JSON chuẩn UTF-8.
"""

import os
import sys
import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime

try:
    import term_glossary
except Exception:
    term_glossary = None

# Đảm bảo UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

DB_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB_PATH = os.path.join(DB_DIR, "job_detail.db")


class JobStorage:
    def __init__(self, db_path=None):
        self.db_path = db_path or DEFAULT_DB_PATH
        self.init_db()

    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def init_db(self):
        """Khởi tạo bảng cơ sở dữ liệu nếu chưa tồn tại."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    company TEXT,
                    level TEXT DEFAULT 'Junior',
                    category TEXT DEFAULT 'Backend',
                    location TEXT DEFAULT '',
                    salary_range TEXT DEFAULT '',
                    raw_jd TEXT NOT NULL,
                    analysis_json TEXT NOT NULL,
                    user_notes TEXT DEFAULT '',
                    tags TEXT DEFAULT '[]',
                    status TEXT DEFAULT 'New',
                    progress_json TEXT DEFAULT '{}',
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
            """)
            # Tự động bổ sung cột progress_json cho CSDL cũ một cách an toàn (không mất dữ liệu)
            cursor.execute("PRAGMA table_info(jobs)")
            existing_cols = {row[1] for row in cursor.fetchall()}
            if "progress_json" not in existing_cols:
                cursor.execute("ALTER TABLE jobs ADD COLUMN progress_json TEXT DEFAULT '{}'")
            # Index cho việc tìm kiếm và lọc nhanh
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_jobs_level ON jobs(level)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_jobs_category ON jobs(category)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_jobs_status ON jobs(status)")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_jobs_title ON jobs(title)")
            conn.commit()

    def add_job(self, title, company, level, category, raw_jd, analysis,
                location="", salary_range="", user_notes="", tags=None, status="New"):
        """Thêm mới một công việc đã phân tích vào CSDL."""
        now = datetime.now().isoformat()
        tags_json = json.dumps(tags if tags is not None else [], ensure_ascii=False)
        analysis_str = json.dumps(analysis, ensure_ascii=False) if isinstance(analysis, dict) else str(analysis)

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO jobs (
                    title, company, level, category, location, salary_range,
                    raw_jd, analysis_json, user_notes, tags, status, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                title.strip(),
                company.strip() if company else "Không xác định",
                level.strip() if level else "Junior",
                category.strip() if category else "Backend",
                location.strip() if location else "",
                salary_range.strip() if salary_range else "Thỏa thuận",
                raw_jd.strip(),
                analysis_str,
                user_notes.strip() if user_notes else "",
                tags_json,
                status.strip() if status else "New",
                now,
                now
            ))
            conn.commit()
            return cursor.lastrowid

    def update_job(self, job_id, title=None, company=None, level=None, category=None,
                   raw_jd=None, analysis=None, location=None, salary_range=None,
                   user_notes=None, tags=None, status=None):
        """Cập nhật thông tin công việc."""
        existing = self.get_job(job_id)
        if not existing:
            return False

        now = datetime.now().isoformat()
        u_title = title if title is not None else existing["title"]
        u_company = company if company is not None else existing["company"]
        u_level = level if level is not None else existing["level"]
        u_category = category if category is not None else existing["category"]
        u_location = location if location is not None else existing["location"]
        u_salary = salary_range if salary_range is not None else existing["salary_range"]
        u_raw_jd = raw_jd if raw_jd is not None else existing["raw_jd"]
        
        if analysis is not None:
            u_analysis = json.dumps(analysis, ensure_ascii=False) if isinstance(analysis, dict) else str(analysis)
        else:
            u_analysis = json.dumps(existing["analysis"], ensure_ascii=False)
            
        u_notes = user_notes if user_notes is not None else existing["user_notes"]
        u_tags = json.dumps(tags, ensure_ascii=False) if tags is not None else json.dumps(existing["tags"], ensure_ascii=False)
        u_status = status if status is not None else existing["status"]

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE jobs SET
                    title = ?, company = ?, level = ?, category = ?,
                    location = ?, salary_range = ?, raw_jd = ?, analysis_json = ?,
                    user_notes = ?, tags = ?, status = ?, updated_at = ?
                WHERE id = ?
            """, (
                u_title, u_company, u_level, u_category, u_location, u_salary,
                u_raw_jd, u_analysis, u_notes, u_tags, u_status, now, job_id
            ))
            conn.commit()
            return cursor.rowcount > 0

    def update_notes(self, job_id, user_notes):
        """Cập nhật ghi chú cá nhân của người dùng cho công việc."""
        now = datetime.now().isoformat()
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE jobs SET user_notes = ?, updated_at = ? WHERE id = ?", (user_notes, now, job_id))
            conn.commit()
            return cursor.rowcount > 0

    def update_status(self, job_id, status):
        """Cập nhật trạng thái công việc (New, Learning, Ready, Applied)."""
        now = datetime.now().isoformat()
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE jobs SET status = ?, updated_at = ? WHERE id = ?", (status, now, job_id))
            conn.commit()
            return cursor.rowcount > 0

    def get_progress(self, job_id):
        """Đọc tiến độ học tập bền vững (checkbox lộ trình, ôn phỏng vấn, giáo trình & dòng chảy nhà máy)."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT progress_json FROM jobs WHERE id = ?", (job_id,))
            row = cursor.fetchone()
            if not row:
                return {"roadmap": {}, "interview": {}, "curriculum": {}, "factory_flow": {}}
            try:
                data = json.loads(row[0] or "{}")
                if not isinstance(data, dict):
                    data = {}
            except Exception:
                data = {}
            data.setdefault("roadmap", {})
            data.setdefault("interview", {})
            data.setdefault("curriculum", {})
            data.setdefault("factory_flow", {})
            return data

    def save_progress(self, job_id, progress_dict):
        """Lưu tiến độ học tập bền vững vào SQLite."""
        now = datetime.now().isoformat()
        payload = json.dumps(progress_dict if isinstance(progress_dict, dict) else {}, ensure_ascii=False)
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE jobs SET progress_json = ?, updated_at = ? WHERE id = ?", (payload, now, job_id))
            conn.commit()
            return cursor.rowcount > 0

    def delete_job(self, job_id):
        """Xóa một công việc theo ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
            conn.commit()
            return cursor.rowcount > 0

    def get_job(self, job_id):
        """Lấy chi tiết một công việc theo ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM jobs WHERE id = ?", (job_id,))
            row = cursor.fetchone()
            if not row:
                return None
            return self._row_to_dict(row)

    def list_jobs(self, keyword="", level="", category="", status=""):
        """Tra cứu danh sách công việc theo bộ lọc đa chiều."""
        query = "SELECT * FROM jobs WHERE 1=1"
        params = []

        if keyword:
            kw = f"%{keyword.strip().lower()}%"
            query += " AND (LOWER(title) LIKE ? OR LOWER(company) LIKE ? OR LOWER(raw_jd) LIKE ? OR LOWER(tags) LIKE ?)"
            params.extend([kw, kw, kw, kw])

        if level and level != "Tất cả":
            query += " AND level = ?"
            params.append(level)

        if category and category != "Tất cả":
            query += " AND category = ?"
            params.append(category)

        if status and status != "Tất cả":
            query += " AND status = ?"
            params.append(status)

        query += " ORDER BY id DESC"

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [self._row_to_dict(r) for r in rows]

    def get_statistics(self):
        """Lấy số liệu thống kê tổng quan."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM jobs")
            total = cursor.fetchone()[0]

            cursor.execute("SELECT level, COUNT(*) FROM jobs GROUP BY level")
            by_level = {row[0]: row[1] for row in cursor.fetchall()}

            cursor.execute("SELECT category, COUNT(*) FROM jobs GROUP BY category")
            by_category = {row[0]: row[1] for row in cursor.fetchall()}

            cursor.execute("SELECT status, COUNT(*) FROM jobs GROUP BY status")
            by_status = {row[0]: row[1] for row in cursor.fetchall()}

            return {
                "total": total,
                "by_level": by_level,
                "by_category": by_category,
                "by_status": by_status
            }

    def _row_to_dict(self, row):
        """Chuyển đổi sqlite3.Row thành dict với JSON đã parse."""
        d = dict(row)
        try:
            d["analysis"] = json.loads(d["analysis_json"])
        except Exception:
            d["analysis"] = {}

        try:
            d["tags"] = json.loads(d["tags"])
        except Exception:
            d["tags"] = []

        try:
            prog = json.loads(d.get("progress_json") or "{}")
            if not isinstance(prog, dict):
                prog = {}
        except Exception:
            prog = {}
        prog.setdefault("roadmap", {})
        prog.setdefault("interview", {})
        prog.setdefault("curriculum", {})
        prog.setdefault("factory_flow", {})
        d["progress"] = prog
        return d

    def export_job_markdown(self, job_id):
        """Xuất hồ sơ chi tiết của một công việc sang định dạng Markdown chuẩn đẹp."""
        job = self.get_job(job_id)
        if not job:
            return ""

        analysis = job.get("analysis", {})
        overview = analysis.get("overview", {})
        skills = analysis.get("skills_matrix", {})
        roadmap = analysis.get("roadmap", [])
        resources = analysis.get("resources", {})
        interview = analysis.get("interview_prep", [])

        md = []
        md.append(f"# 📋 Hồ Sơ Phân Tích Công Việc: {job['title']}")
        md.append(f"**Công ty:** {job['company']} | **Cấp bậc:** {job['level']} | **Lĩnh vực:** {job['category']}")
        md.append(f"**Địa điểm:** {job.get('location', 'N/A')} | **Mức lương:** {job.get('salary_range', 'Thỏa thuận')}")
        md.append(f"**Trạng thái:** {job.get('status', 'New')} | **Ngày lưu:** {job.get('created_at', '')[:10]}")
        md.append("\n---\n")

        # Tầng 1: Tổng quan
        md.append("## 1. 📌 Tổng Quan Vị Trí (Role Overview)")
        md.append(f"- **Tóm tắt vai trò:** {overview.get('summary', 'Chưa có thông tin')}")
        md.append(f"- **Mục tiêu cốt lõi:** {overview.get('mission', 'Chưa có thông tin')}")
        md.append(f"- **Hình thức làm việc:** {overview.get('work_mode', 'N/A')}")
        md.append("")

        # Tầng 2: Ma trận kỹ năng
        md.append("## 2. 🛠️ Ma Trận Kỹ Năng & Công Nghệ (Skills Matrix)")
        md.append("### Kỹ Năng Bắt Buộc (Must-Have / Core):")
        for item in skills.get("must_have", []):
            md.append(f"- 🔴 **{item}**")
        md.append("\n### Kỹ Năng Ưu Tiên / Điểm Cộng (Nice-To-Have):")
        for item in skills.get("nice_to_have", []):
            md.append(f"- 🟢 {item}")
        md.append("\n### Công Cụ & Hệ Sinh Thái (Tools & Platforms):")
        for item in skills.get("tools", []):
            md.append(f"- ⚙️ {item}")
        md.append("\n### Kỹ Năng Mềm & Phương Pháp Luận:")
        for item in skills.get("soft_skills", []):
            md.append(f"- 💡 {item}")
        md.append("")

        # Tầng 3: Lộ trình Onboarding
        md.append("## 3. 🧭 Lộ Trình Nắm Bắt Công Việc (Learning & Onboarding Roadmap)")
        for idx, phase in enumerate(roadmap, 1):
            md.append(f"### Giai Đoạn {idx}: {phase.get('phase', f'Chặng {idx}')}")
            goals = phase.get("goals", [])
            if goals:
                md.append("**Mục tiêu cần đạt:**")
                for g in goals:
                    md.append(f"  * {g}")
            actions = phase.get("action_items", [])
            if actions:
                md.append("**Hành động cụ thể:**")
                for a in actions:
                    md.append(f"  - [ ] {a}")
            md.append("")

        # Tầng 4: Kho tài liệu
        md.append("## 4. 📚 Danh Mục Tài Liệu & Nguồn Học Chuẩn (Curated Resources)")
        docs = resources.get("official_docs", [])
        if docs:
            md.append("### Tài Liệu Chính Thống (Official Documentation):")
            for d in docs:
                url = d.get('url', '#')
                name = d.get('name', 'Tài liệu')
                desc = d.get('desc', '')
                md.append(f"- [{name}]({url}) — *{desc}*")
        books = resources.get("books", [])
        if books:
            md.append("\n### Sách & Giáo Trình Kinh Điển:")
            for b in books:
                md.append(f"- 📖 **{b}**")
        keywords = resources.get("search_keywords", [])
        if keywords:
            md.append("\n### Từ Khóa Vàng Tra Cứu (Search Queries):")
            md.append("`" + "` | `".join(keywords) + "`")
        md.append("")

        # Tầng 5: Câu hỏi phỏng vấn
        md.append("## 5. ❓ Bộ Câu Hỏi Phỏng Vấn & Thực Chiến (Interview Prep)")
        for idx, q in enumerate(interview, 1):
            q_text = q.get("question", "")
            q_type = q.get("type", "General")
            q_key = q.get("key_points", "")
            md.append(f"**Câu {idx} [{q_type}]:** {q_text}")
            md.append(f"> 💡 *Gợi ý trả lời:* {q_key}\n")

        # Ghi chú cá nhân
        if job.get("user_notes"):
            md.append("## 📝 Ghi Chú Cá Nhân (My Notes)")
            md.append(job["user_notes"])
            md.append("")

        result_md = "\n".join(md)
        if term_glossary:
            result_md = term_glossary.strip_term_formulas(result_md)
        return result_md
