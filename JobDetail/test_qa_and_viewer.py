# -*- coding: utf-8 -*-
"""
test_qa_and_viewer.py — Bộ kiểm thử tự động kiểm tra:
1. Ngân hàng câu hỏi thực chiến interview_bank (tối thiểu 50 câu, không trùng lặp, đầy đủ trường).
2. Tính năng lọc danh mục và tìm kiếm từ khóa câu hỏi.
3. Trình đọc cẩm nang OfflineDocViewer: Không phát sinh KeyError ('surface2'), render an toàn 16/16 cẩm nang.
4. Tích hợp phân tích JD Sản xuất (JobAnalyzer) và lưu trữ SQLite (JobStorage).
"""

import unittest
import os
import sys
import tkinter as tk

# Đảm bảo import được module trong thư mục JobDetail
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import interview_bank
import offline_knowledge
from job_storage import JobStorage
from job_analyzer import JobAnalyzer
from JobDetailApp import OfflineDocViewer, THEME


class TestInterviewBank(unittest.TestCase):
    """Kiểm tra ngân hàng câu hỏi interview_bank."""

    def setUp(self):
        self.all_questions = interview_bank.get_all_questions()

    def test_total_count_at_least_50(self):
        """Đảm bảo số lượng câu hỏi đạt ít nhất 50 câu (thực tế 56 câu)."""
        self.assertGreaterEqual(len(self.all_questions), 50, f"Yêu cầu ít nhất 50 câu, hiện có {len(self.all_questions)}")

    def test_all_questions_unique_ids(self):
        """Đảm bảo 100% ID câu hỏi là duy nhất, không trùng lặp."""
        ids = [q.get("id") for q in self.all_questions]
        unique_ids = set(ids)
        self.assertEqual(len(ids), len(unique_ids), f"Phát hiện ID trùng lặp trong interview_bank!")

    def test_all_questions_unique_text(self):
        """Đảm bảo nội dung các câu hỏi không bị trùng lặp lẫn nhau."""
        q_texts = [q.get("question", "").strip().lower() for q in self.all_questions]
        unique_texts = set(q_texts)
        self.assertEqual(len(q_texts), len(unique_texts), f"Phát hiện câu hỏi có nội dung trùng lặp!")

    def test_required_fields_non_empty(self):
        """Đảm bảo mỗi câu hỏi đều có đầy đủ id, category, type, question, key_points."""
        for idx, q in enumerate(self.all_questions, 1):
            self.assertTrue(q.get("id"), f"Câu #{idx} bị thiếu ID")
            self.assertTrue(q.get("category"), f"Câu #{idx} bị thiếu category")
            self.assertTrue(q.get("type"), f"Câu #{idx} bị thiếu type")
            self.assertTrue(q.get("question"), f"Câu #{idx} bị thiếu question text")
            self.assertTrue(q.get("key_points"), f"Câu #{idx} bị thiếu key_points")
            # Kiểm tra độ dài nội dung có chiều sâu thực chiến
            self.assertGreater(len(q.get("key_points", "")), 50, f"Gợi ý trả lời câu #{idx} quá ngắn, thiếu chi tiết!")

    def test_category_filtering(self):
        """Đảm bảo bộ lọc theo từng chủ đề hoạt động chuẩn xác."""
        cats = interview_bank.get_categories()
        self.assertIn("Tất cả chủ đề", cats)
        self.assertGreaterEqual(len(cats), 10)

        for cat in cats:
            filtered = interview_bank.get_questions_by_category(cat)
            if cat == "Tất cả chủ đề":
                self.assertEqual(len(filtered), len(self.all_questions))
            else:
                self.assertGreater(len(filtered), 0, f"Danh mục '{cat}' không có câu hỏi nào!")
                for q in filtered:
                    self.assertEqual(q.get("category"), cat)

    def test_search_questions(self):
        """Đảm bảo tìm kiếm từ khóa hoạt động nhanh và chính xác."""
        res_oee = interview_bank.search_questions("OEE")
        self.assertGreater(len(res_oee), 0, "Tìm kiếm 'OEE' phải có kết quả")

        res_smed = interview_bank.search_questions("SMED")
        self.assertGreater(len(res_smed), 0, "Tìm kiếm 'SMED' phải có kết quả")

        res_poka = interview_bank.search_questions("Poka-Yoke")
        self.assertGreater(len(res_poka), 0, "Tìm kiếm 'Poka-Yoke' phải có kết quả")

        res_none = interview_bank.search_questions("XYZ_NON_EXISTENT_KEYWORD_123")
        self.assertEqual(len(res_none), 0, "Từ khóa không tồn tại phải trả về 0 kết quả")


class TestOfflineKnowledgeAndDocViewer(unittest.TestCase):
    """Kiểm tra kho tài liệu offline và trình hiển thị OfflineDocViewer."""

    def test_all_16_docs_exist(self):
        """Đảm bảo đầy đủ 16 cẩm nang kỹ thuật chuyên sâu."""
        docs = offline_knowledge.get_all_offline_docs()
        self.assertEqual(len(docs), 16, f"Yêu cầu đủ 16 cẩm nang, hiện có {len(docs)}")

    def test_no_broken_raw_latex(self):
        """Đảm bảo không còn ký hiệu LaTeX thô hoặc escape hỏng trong 16 cẩm nang."""
        bad_tokens = [r"\frac", r"\times", r"\text", "	imes", "	ext", r"\rightarrow", "ightarrow", r"\phi"]
        for doc_id, doc in offline_knowledge.OFFLINE_DOCS.items():
            content = doc.get("content", "")
            for token in bad_tokens:
                self.assertNotIn(token, content, f"Cẩm nang '{doc_id}' còn chứa token thô '{token}'!")
            for line in content.splitlines():
                if "ENV PATH=" in line:
                    continue
                self.assertNotIn("$", line, f"Cẩm nang '{doc_id}' còn chứa ký hiệu '$': {line}")

    def test_interview_bank_no_dollars(self):
        """Đảm bảo ngân hàng 56 câu hỏi không còn dấu dollar hay token latex thô."""
        for q in self.all_questions if hasattr(self, 'all_questions') else interview_bank.get_all_questions():
            q_text = q.get("question", "")
            kp = q.get("key_points", "")
            self.assertNotIn("$", q_text, f"Câu hỏi {q.get('id')} còn chứa '$'")
            self.assertNotIn("$", kp, f"Câu hỏi {q.get('id')} còn chứa '$'")
            self.assertNotIn(r"\times", kp)
            self.assertNotIn("	imes", kp)
            self.assertNotIn(r"\text", kp)

    def test_offline_doc_viewer_all_16_headless(self):
        """Khởi tạo headless Tkinter và mở toàn bộ 16 cẩm nang, xác nhận 0 lỗi KeyError ('surface2') hay crash."""
        root = tk.Tk()
        root.withdraw()  # Chạy ngầm, không mở cửa sổ đồ họa
        try:
            for doc_id, doc in offline_knowledge.OFFLINE_DOCS.items():
                title = doc.get("title", "")
                category = doc.get("category", "")
                content = doc.get("content", "")

                viewer = OfflineDocViewer(root, title, content, category)
                # Kiểm tra nội dung text widget đã được nạp
                rendered_text = viewer.txt_content.get("1.0", "end")
                self.assertGreater(len(rendered_text.strip()), 100, f"Cẩm nang '{doc_id}' bị rỗng nội dung!")
                viewer.destroy()
        finally:
            root.destroy()

    def test_ole_handbook_has_4_tiers_and_3_case_studies(self):
        """Đảm bảo cẩm nang OLE đạt chuẩn công nghiệp: 4 tầng kiến thức Basic->Expert, 3 case study, độ dài >15,000 ký tự."""
        ole = offline_knowledge.OFFLINE_DOCS.get("ole", {})
        content = ole.get("content", "")
        self.assertGreaterEqual(len(content), 15000, "Cẩm nang OLE phải sâu sắc trên 15,000 ký tự")
        self.assertIn("TẦNG 1: CƠ BẢN", content)
        self.assertIn("TẦNG 2: TRUNG CẤP", content)
        self.assertIn("TẦNG 3: NÂNG CAO", content)
        self.assertIn("TẦNG 4: CHUYÊN GIA", content)
        self.assertIn("CASE STUDY 1", content)
        self.assertIn("CASE STUDY 2", content)
        self.assertIn("CASE STUDY 3", content)
        self.assertIn("YAMAZUMI", content.upper())
        self.assertIn("SMOOTHNESS INDEX", content.upper())
        self.assertIn("ERGONOMICS", content.upper())

    def test_manufacturing_handbooks_depth(self):
        """Đảm bảo các cẩm nang OEE, SMED, BOM, SPC đều có Case Study thực tế và chi tiết chuyên gia."""
        oee = offline_knowledge.OFFLINE_DOCS["oee"]["content"]
        self.assertIn("TEEP", oee)
        self.assertIn("CAPEX", oee)
        self.assertIn("TPM", oee)

        smed = offline_knowledge.OFFLINE_DOCS["smed"]["content"]
        self.assertIn("85 PHÚT", smed)
        self.assertIn("8 PHÚT 40 GIÂY", smed)
        self.assertIn("F1 PIT-STOP", smed)

        bom = offline_knowledge.OFFLINE_DOCS["bom_cost"]["content"]
        self.assertIn("10,000 SẢN PHẨM", bom)
        self.assertIn("Kitting", bom)
        self.assertIn("Two-Bin Kanban", bom)

        spc = offline_knowledge.OFFLINE_DOCS["minitab_spc"]["content"]
        self.assertIn("25.0", spc)
        self.assertIn("Nelson Rules", spc)
        self.assertIn("Gage R&R", spc)


class TestJobStorageAndAnalyzerIntegration(unittest.TestCase):
    """Kiểm tra tích hợp CSDL SQLite và bộ phân tích JobAnalyzer."""

    def test_job_id_1_loaded_with_50_plus_questions(self):
        """Đảm bảo hồ sơ công việc ID 1 lưu trong CSDL đã có đủ 56 câu hỏi."""
        db_path = os.path.join(current_dir, "job_detail.db")
        if os.path.exists(db_path):
            storage = JobStorage(db_path)
            job = storage.get_job(1)
            self.assertIsNotNone(job, "Hồ sơ Job ID 1 phải tồn tại trong CSDL")
            analysis = job.get("analysis", {})
            interview = analysis.get("interview_prep", [])
            self.assertGreaterEqual(len(interview), 50, f"Job ID 1 phải có ít nhất 50 câu hỏi, hiện có {len(interview)}")

    def test_mfg_analyzer_generates_56_questions(self):
        """Đảm bảo JobAnalyzer tự động nạp 56 câu hỏi khi phân tích JD Sản xuất / Lean."""
        analyzer = JobAnalyzer()
        mfg_jd = """
        Tuyển Kỹ Sư Cải Tiến Sản Xuất (Lean / IE Engineer)
        - Phân tích năng suất, chỉ số OEE, OLE trên chuyền sản xuất
        - Triển khai SMED rút ngắn thời gian chuyển đổi khuôn
        - Kiểm soát định mức hao hụt vật tư BOM, cân bằng chuyền
        - Áp dụng 7 lãng phí, 5S, Kaizen và Poka-Yoke tại Genba
        """
        result = analyzer.analyze(mfg_jd, force_offline=True)
        self.assertIsNotNone(result)
        analysis = result.get("analysis", {})
        interview = analysis.get("interview_prep", [])
        self.assertGreaterEqual(len(interview), 50, f"JD sản xuất phải tự động sinh ít nhất 50 câu hỏi, thực tế: {len(interview)}")

    def test_job_detail_app_interview_ui_filter_and_search(self):
        """Đảm bảo giao diện JobDetailApp render 56 thẻ câu hỏi, lọc theo chủ đề và tìm kiếm từ khóa không lỗi."""
        from JobDetailApp import JobDetailApp
        app = JobDetailApp()
        app.withdraw()
        try:
            app._display_job_detail(1)
            self.assertEqual(len(app._current_interview_raw), 56)
            self.assertEqual(len(app.scroll_interview.winfo_children()), 56)

            # Lọc theo danh mục OEE
            app.cbo_interview_cat.set("OEE & 6 Tổn Thất Lớn")
            app._update_interview_display()
            self.assertEqual(len(app.scroll_interview.winfo_children()), 6)

            # Tìm kiếm từ khóa SMED
            app.cbo_interview_cat.set("Tất cả chủ đề")
            app.ent_interview_search.delete(0, "end")
            app.ent_interview_search.insert(0, "SMED")
            app._update_interview_display()
            self.assertGreater(len(app.scroll_interview.winfo_children()), 0)
        finally:
            app.destroy()


if __name__ == "__main__":
    unittest.main()
