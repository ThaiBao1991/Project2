#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
test_job_storage.py - Kiểm thử CSDL SQLite, CRUD, Tìm kiếm và Xuất Markdown cho JobDetail.
"""

import os
import sys
import tempfile
import unittest

# Đảm bảo UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from job_storage import JobStorage


class TestJobStorage(unittest.TestCase):
    def setUp(self):
        # Dùng file tạm thời để kiểm thử cô lập
        self.temp_db = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.temp_db.close()
        self.storage = JobStorage(self.temp_db.name)

    def tearDown(self):
        # Dọn dẹp file test
        if os.path.exists(self.temp_db.name):
            try:
                os.remove(self.temp_db.name)
            except Exception:
                pass

    def test_add_and_get_job(self):
        sample_analysis = {
            "overview": {"summary": "Lập trình viên Python backend"},
            "skills_matrix": {"must_have": ["Python", "Django"]},
            "roadmap": [{"phase": "Tuần 1", "goals": ["Setup"]}]
        }
        job_id = self.storage.add_job(
            title="Senior Python Engineer",
            company="Công ty Công Nghệ Á Châu",
            level="Senior",
            category="Backend",
            raw_jd="Cần tuyển Senior Python 5 năm kinh nghiệm, thành thạo Django/PostgreSQL.",
            analysis=sample_analysis,
            location="Hà Nội",
            salary_range="30 - 45 Triệu",
            tags=["Python", "Senior", "Backend"]
        )
        self.assertGreater(job_id, 0)

        job = self.storage.get_job(job_id)
        self.assertIsNotNone(job)
        self.assertEqual(job["title"], "Senior Python Engineer")
        self.assertEqual(job["company"], "Công ty Công Nghệ Á Châu")
        self.assertEqual(job["level"], "Senior")
        self.assertEqual(job["analysis"]["overview"]["summary"], "Lập trình viên Python backend")
        self.assertIn("Python", job["tags"])

    def test_search_and_filter(self):
        self.storage.add_job(
            title="Frontend React Developer",
            company="FPT Software",
            level="Junior",
            category="Frontend",
            raw_jd="ReactJS, Redux, TailwindCSS",
            analysis={"overview": {"summary": "Frontend react"}},
            tags=["React", "Junior"]
        )
        self.storage.add_job(
            title="DevOps Engineer",
            company="Viettel Group",
            level="Senior",
            category="DevOps",
            raw_jd="Docker, Kubernetes, AWS, Terraform",
            analysis={"overview": {"summary": "DevOps k8s"}},
            tags=["DevOps", "Senior"]
        )

        # Lọc theo keyword
        results = self.storage.list_jobs(keyword="React")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Frontend React Developer")

        # Lọc theo Level
        seniors = self.storage.list_jobs(level="Senior")
        self.assertEqual(len(seniors), 1)
        self.assertEqual(seniors[0]["title"], "DevOps Engineer")

        # Lọc theo Category
        frontends = self.storage.list_jobs(category="Frontend")
        self.assertEqual(len(frontends), 1)

    def test_update_and_delete(self):
        job_id = self.storage.add_job(
            title="QA Engineer",
            company="Shopee",
            level="Mid",
            category="QA",
            raw_jd="Selenium, Appium, Python",
            analysis={}
        )
        # Update notes & status
        self.storage.update_notes(job_id, "Đã ôn tập kỹ phần Selenium")
        self.storage.update_status(job_id, "Ready")

        job = self.storage.get_job(job_id)
        self.assertEqual(job["user_notes"], "Đã ôn tập kỹ phần Selenium")
        self.assertEqual(job["status"], "Ready")

        # Delete
        success = self.storage.delete_job(job_id)
        self.assertTrue(success)
        self.assertIsNone(self.storage.get_job(job_id))

    def test_export_markdown(self):
        job_id = self.storage.add_job(
            title="Backend Golang Engineer",
            company="VNG",
            level="Mid",
            category="Backend",
            raw_jd="Go, Microservices, Kafka",
            analysis={
                "overview": {"summary": "Xây dựng hệ thống chat hiệu năng cao", "mission": "Đạt 1 triệu CCU", "work_mode": "Hybrid"},
                "skills_matrix": {
                    "must_have": ["Golang", "Kafka"],
                    "nice_to_have": ["Redis"],
                    "tools": ["Docker"],
                    "soft_skills": ["Agile"]
                },
                "roadmap": [{"phase": "Tuần 1", "goals": ["Chạy local"]}],
                "resources": {"official_docs": [{"name": "Go Docs", "url": "https://go.dev", "desc": "Official"}]},
                "interview_prep": [{"question": "Goroutine là gì?", "type": "Concept", "key_points": "Lightweight thread"}]
            }
        )
        md = self.storage.export_job_markdown(job_id)
        self.assertIn("# 📋 Hồ Sơ Phân Tích Công Việc: Backend Golang Engineer", md)
        self.assertIn("Goroutine là gì?", md)
        self.assertIn("Golang", md)


if __name__ == "__main__":
    unittest.main()
