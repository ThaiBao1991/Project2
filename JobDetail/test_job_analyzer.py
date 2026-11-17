#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
test_job_analyzer.py - Kiểm thử Bộ Máy Phân Tích JD (Offline Mode & 5-Tier Intelligence Model).
"""

import sys
import unittest

# Đảm bảo UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from job_analyzer import JobAnalyzer


class TestJobAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = JobAnalyzer()

    def test_offline_analysis_python_backend(self):
        raw_jd = """
        Vị trí: Senior Backend Developer (Python)
        Công ty: Cty Công Nghệ Quốc Tế VinaTech
        Địa điểm: Hà Nội
        Mức lương: 35.000.000 - 50.000.000 VNĐ
        
        Mô tả công việc:
        - Xây dựng hệ thống REST API hiệu năng cao với Python, FastAPI và PostgreSQL.
        - Thiết kế kiến trúc Microservices, sử dụng Redis cache và Docker / Kubernetes để deploy.
        - Quản lý mã nguồn với Git, làm việc theo quy trình Agile/Scrum.
        
        Yêu cầu:
        - Tối thiểu 5 năm kinh nghiệm lập trình backend.
        - Thành thạo Python, hiểu sâu về Asyncio và ORM.
        - Có kinh nghiệm tối ưu hóa câu truy vấn CSDL PostgreSQL.
        """
        result = self.analyzer.analyze(raw_jd, force_offline=True)

        self.assertIsNotNone(result)
        self.assertIn("Python", result["title"])
        self.assertEqual(result["level"], "Senior")
        self.assertEqual(result["category"], "Backend")
        self.assertEqual(result["location"], "Hà Nội")

        analysis = result["analysis"]
        # Kiểm tra 5 tầng kiến thức:
        # Tầng 1: Overview
        self.assertIn("overview", analysis)
        self.assertTrue(len(analysis["overview"]["summary"]) > 0)

        # Tầng 2: Skills Matrix
        skills = analysis["skills_matrix"]
        self.assertIn("Python", skills["must_have"] + skills["nice_to_have"])
        self.assertTrue(len(skills["must_have"]) > 0)
        self.assertTrue(len(skills["tools"]) > 0)

        # Tầng 3: Roadmap (3 chặng)
        roadmap = analysis["roadmap"]
        self.assertEqual(len(roadmap), 3)
        self.assertIn("Tuần 1 - 2", roadmap[0]["phase"])
        self.assertIn("Tháng 1", roadmap[1]["phase"])
        self.assertIn("Tháng 2 - 3", roadmap[2]["phase"])

        # Tầng 4: Resources
        resources = analysis["resources"]
        self.assertTrue(len(resources["official_docs"]) > 0)
        self.assertTrue(len(resources["books"]) > 0)
        self.assertTrue(len(resources["search_keywords"]) > 0)

        # Tầng 5: Interview Prep
        interview = analysis["interview_prep"]
        self.assertTrue(len(interview) > 0)
        self.assertIn("question", interview[0])
        self.assertIn("key_points", interview[0])

    def test_offline_analysis_frontend_react(self):
        raw_jd = """
        Tuyển dụng: Junior Frontend React Developer
        Công ty: TechStartup
        Hình thức: Remote
        
        Yêu cầu:
        - 1-2 năm kinh nghiệm làm việc với JavaScript, React và TypeScript.
        - Hiểu biết về Responsive design, HTML/CSS.
        - Biết sử dụng Git cơ bản.
        """
        result = self.analyzer.analyze(raw_jd, force_offline=True)
        self.assertEqual(result["level"], "Junior")
        self.assertEqual(result["category"], "Frontend")
        self.assertIn("Remote", result["analysis"]["overview"]["work_mode"])

    def test_empty_jd_raises_error(self):
        with self.assertRaises(ValueError):
            self.analyzer.analyze("")


if __name__ == "__main__":
    unittest.main()
