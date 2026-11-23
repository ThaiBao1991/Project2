# -*- coding: utf-8 -*-
"""
test_qa_and_viewer.py — Bộ kiểm thử tự động kiểm tra:
1. Ngân hàng câu hỏi thực chiến interview_bank (tối thiểu 50 câu, không trùng lặp, đầy đủ trường).
2. Tính năng lọc danh mục và tìm kiếm từ khóa câu hỏi.
3. Trình đọc cẩm nang OfflineDocViewer: Không phát sinh KeyError ('surface2'), render an toàn 16/16 cẩm nang.
4. Tích hợp phân tích JD Sản xuất (JobAnalyzer) và lưu trữ SQLite (JobStorage).
"""

import unittest
import ast
import os
import re
import sys
import tkinter as tk

# Đảm bảo import được module trong thư mục JobDetail
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import interview_bank
import offline_knowledge
import term_glossary
import glossary_enrichment
import oe_curriculum
from job_storage import JobStorage
from job_analyzer import JobAnalyzer
from JobDetailApp import OfflineDocViewer, TermDetailPopup, GlossaryBrowserDialog, TermHoverTooltip, insert_with_glossary, create_c_engine_text, THEME


class TestInterviewBank(unittest.TestCase):
    """Kiểm tra ngân hàng câu hỏi interview_bank."""

    def setUp(self):
        self.all_questions = interview_bank.get_all_questions()

    def test_total_count_at_least_125(self):
        """Đảm bảo số lượng câu hỏi đạt ít nhất 125 câu (thực tế 128 câu không trùng lặp)."""
        self.assertGreaterEqual(len(self.all_questions), 125, f"Yêu cầu ít nhất 125 câu, hiện có {len(self.all_questions)}")

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
        self.assertGreaterEqual(len(cats), 18)

        for cat in cats:
            filtered = interview_bank.get_questions_by_category(cat)
            if cat == "Tất cả chủ đề":
                self.assertEqual(len(filtered), len(self.all_questions))
            else:
                self.assertGreater(len(filtered), 0, f"Danh mục '{cat}' không có câu hỏi nào!")
                for q in filtered:
                    self.assertEqual(q.get("category"), cat)

    def test_search_questions(self):
        """Đảm bảo tìm kiếm từ khóa hoạt động nhanh và chính xác (cả văn bản thuần và công thức [[Key|Text]])."""
        for kw in ["OEE", "SMED", "Poka-Yoke", "LOTO", "RTY", "Standard Cost", "cáp ABC", "Work Sampling", "Sharkskin", "Cup-and-Cone"]:
            res = interview_bank.search_questions(kw)
            self.assertGreater(len(res), 0, f"Tìm kiếm '{kw}' phải có kết quả")

        res_none = interview_bank.search_questions("XYZ_NON_EXISTENT_KEYWORD_123")
        self.assertEqual(len(res_none), 0, "Từ khóa không tồn tại phải trả về 0 kết quả")


class TestOfflineKnowledgeAndDocViewer(unittest.TestCase):
    """Kiểm tra kho tài liệu offline và trình hiển thị OfflineDocViewer."""

    def test_all_22_docs_exist(self):
        """Đảm bảo đầy đủ 22 cẩm nang kỹ thuật chuyên sâu (16 Sản xuất/Cáp điện + 6 IT)."""
        docs = offline_knowledge.get_all_offline_docs()
        self.assertEqual(len(docs), 22, f"Yêu cầu đủ 22 cẩm nang, hiện có {len(docs)}")
        for required_key in [
            "cable_mfg_machines", "oe_six_sigma_dmaic", "cable_cost_capacity",
            "planning_quality_ehs_cost", "cable_extrusion_wire_forensics", "oe_field_execution_case_test"
        ]:
            self.assertIn(required_key, offline_knowledge.OFFLINE_DOCS, f"Thiếu cẩm nang mới '{required_key}'")

    def test_all_explicit_formulas_resolve(self):
        """Đảm bảo 100% công thức [[TermKey|Text]] trong cẩm nang & câu hỏi đều trỏ tới khóa hợp lệ trong term_glossary."""
        pat = re.compile(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]")
        for doc_id, doc in offline_knowledge.OFFLINE_DOCS.items():
            for m in pat.finditer(doc.get("content", "")):
                key = m.group(1).strip()
                self.assertIsNotNone(term_glossary.get_term(key), f"Cẩm nang '{doc_id}' chứa khóa không tồn tại: {m.group(0)}")
        for q in interview_bank.get_all_questions():
            for fld in ("question", "key_points"):
                for m in pat.finditer(q.get(fld, "")):
                    key = m.group(1).strip()
                    self.assertIsNotNone(term_glossary.get_term(key), f"Câu hỏi '{q.get('id')}' chứa khóa không tồn tại: {m.group(0)}")

    def test_no_broken_raw_latex(self):
        """Đảm bảo không còn ký hiệu LaTeX thô hoặc ký tự escape hỏng trong toàn bộ 20 cẩm nang."""
        bad_tokens = [
            r"\frac", r"\times", r"\text", "\times", "\text", "\x0c", "\x08",
            r"\rightarrow", "ightarrow", r"\phi", "_{", r"\%", r"\ "
        ]
        for doc_id, doc in offline_knowledge.OFFLINE_DOCS.items():
            content = doc.get("content", "")
            for token in bad_tokens:
                self.assertNotIn(token, content, f"Cẩm nang '{doc_id}' còn chứa token thô '{repr(token)}'!")
            for line in content.splitlines():
                if "ENV PATH=" in line:
                    continue
                self.assertNotIn("$", line, f"Cẩm nang '{doc_id}' còn chứa ký hiệu '$': {line}")

    def test_interview_bank_no_dollars(self):
        """Đảm bảo ngân hàng 112 câu hỏi không còn dấu dollar hay token latex thô."""
        for q in interview_bank.get_all_questions():
            q_text = q.get("question", "")
            kp = q.get("key_points", "")
            self.assertNotIn("$", q_text, f"Câu hỏi {q.get('id')} còn chứa '$'")
            self.assertNotIn("$", kp, f"Câu hỏi {q.get('id')} còn chứa '$'")
            self.assertNotIn(r"\times", kp)
            self.assertNotIn("\times", kp)
            self.assertNotIn("\x0c", kp)
            self.assertNotIn(r"\text", kp)
            self.assertNotIn("_{", kp)

    def test_offline_doc_viewer_all_22_headless_no_raw_markdown_plus_toc_and_find(self):
        """Khởi tạo headless Tkinter và mở toàn bộ 22 cẩm nang: 0 rò rỉ '[[' hoặc '**bold**' thô, kiểm tra TOC & Ctrl+F."""
        root = tk.Tk()
        root.withdraw()
        try:
            for doc_id, doc in offline_knowledge.OFFLINE_DOCS.items():
                title = doc.get("title", "")
                category = doc.get("category", "")
                content = doc.get("content", "")

                viewer = OfflineDocViewer(root, title, content, category)
                rendered_text = viewer.txt_content.get("1.0", "end")
                self.assertGreater(len(rendered_text.strip()), 100, f"Cẩm nang '{doc_id}' bị rỗng nội dung!")
                self.assertNotIn("[[", rendered_text, f"Cẩm nang '{doc_id}' bị rò rỉ cú pháp thô '[[' ra giao diện!")
                self.assertNotIn("]]", rendered_text, f"Cẩm nang '{doc_id}' bị rò rỉ cú pháp thô ']]' ra giao diện!")
                self.assertNotIn("**", rendered_text, f"Cẩm nang '{doc_id}' bị rò rỉ dấu sao '**' thô ra giao diện!")
                self.assertGreater(len(viewer._toc_map), 0, f"Cẩm nang '{doc_id}' chưa dựng mục lục TOC!")
                if doc_id == "oe_field_execution_case_test":
                    cnt = viewer._find_in_doc("Work Sampling")
                    self.assertGreater(cnt, 0, "Tìm kiếm Ctrl+F trong cẩm nang phải tìm thấy 'Work Sampling'!")
                    viewer._find_next()
                    viewer._find_prev()
                viewer.destroy()
        finally:
            root.destroy()

    def test_ole_handbook_has_4_tiers_and_3_case_studies(self):
        """Đảm bảo cẩm nang OLE đạt chuẩn công nghiệp: 4 tầng kiến thức Basic->Expert, 4 case study, độ dài >15,000 ký tự."""
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
        self.assertIn("CASE STUDY 4", content)
        self.assertIn("YAMAZUMI", content.upper())
        self.assertIn("SMOOTHNESS INDEX", content.upper())
        self.assertIn("ERGONOMICS", content.upper())

    def test_manufacturing_and_cadivi_handbooks_depth(self):
        """Đảm bảo các cẩm nang OEE, SMED, BOM, SPC và 3 cẩm nang mới CADIVI/OE đều đạt độ sâu chuyên gia."""
        oee = offline_knowledge.OFFLINE_DOCS["oee"]["content"]
        self.assertIn("TEEP", oee)
        self.assertIn("CAPEX", oee)
        self.assertIn("TPM", oee)
        self.assertIn("CADIVI", oee)

        smed = offline_knowledge.OFFLINE_DOCS["smed"]["content"]
        self.assertIn("85 PHÚT", smed)
        self.assertIn("8 PHÚT 40 GIÂY", smed)
        self.assertIn("F1 PIT-STOP", smed)
        self.assertIn("Color Sequencing", smed)

        bom = offline_knowledge.OFFLINE_DOCS["bom_cost"]["content"]
        self.assertIn("10,000 SẢN PHẨM", bom)
        self.assertIn("Kitting", bom)
        self.assertIn("Two-Bin Kanban", bom)
        self.assertIn("CXV", bom)

        spc = offline_knowledge.OFFLINE_DOCS["minitab_spc"]["content"]
        self.assertIn("25.0", spc)
        self.assertIn("Nelson Rules", spc)
        self.assertIn("Gage R&R", spc)
        self.assertIn("Laser Gauge", spc)

        cable = offline_knowledge.OFFLINE_DOCS["cable_mfg_machines"]["content"]
        self.assertIn("RBD", cable)
        self.assertIn("Spark Tester", cable)
        self.assertIn("IEC 60228", cable)
        self.assertIn("NHÓM 9", cable)
        self.assertIn("ACSR", cable)
        self.assertIn("ABC Cable", cable)
        self.assertIn("Mica FR", cable)
        self.assertIn("Partial Discharge", cable)
        self.assertIn("Water Immersion", cable)

        oe_ss = offline_knowledge.OFFLINE_DOCS["oe_six_sigma_dmaic"]["content"]
        self.assertIn("DMAIC", oe_ss)
        self.assertIn("PFMEA", oe_ss)
        self.assertIn("MTBF", oe_ss)
        self.assertIn("Payback", oe_ss)

        cap = offline_knowledge.OFFLINE_DOCS["cable_cost_capacity"]["content"]
        self.assertIn("Copper Give-away", cap)
        self.assertIn("Over-thickness", cap)
        self.assertIn("RCCP", cap)
        self.assertIn("Cut-Length", cap)

        plan_ehs = offline_knowledge.OFFLINE_DOCS["planning_quality_ehs_cost"]["content"]
        for tok in ["S&OP", "MPS", "MRP", "CRP", "RTY", "83.27%", "LOTO", "ISO 50001", "Standard Cost", "Hoshin Kanri", "ADKAR"]:
            self.assertIn(tok, plan_ehs, f"Cẩm nang 'planning_quality_ehs_cost' thiếu nội dung '{tok}'")

        ext_for = offline_knowledge.OFFLINE_DOCS["cable_extrusion_wire_forensics"]["content"]
        for tok in ["L/D Ratio", "Melt Pressure", "DDR", "Sharkskin", "Die Drool", "Regrind", "Cup-and-Cone", "Solar Cable", "Braiding", "QCVN 4"]:
            self.assertIn(tok, ext_for, f"Cẩm nang 'cable_extrusion_wire_forensics' thiếu nội dung '{tok}'")

        field_test = offline_knowledge.OFFLINE_DOCS["oe_field_execution_case_test"]["content"]
        for tok in ["Work Sampling", "Cost Deployment", "LSW", "LPA", "Escalation Matrix", "Wrench Time", "ĐỀ THI 1", "ĐỀ THI 2", "ĐỀ THI 3", "74.16%"]:
            self.assertIn(tok, field_test, f"Cẩm nang 'oe_field_execution_case_test' thiếu nội dung '{tok}'")

        # Kiểm tra cả oee và smed đã chuẩn hóa đủ 4 tầng
        for dk in ("oee", "smed"):
            c = offline_knowledge.OFFLINE_DOCS[dk]["content"]
            for tier in ("TẦNG 1", "TẦNG 2", "TẦNG 3", "TẦNG 4"):
                self.assertIn(tier, c, f"Cẩm nang '{dk}' thiếu tiêu đề '{tier}'")


class TestJobStorageAndAnalyzerIntegration(unittest.TestCase):
    """Kiểm tra tích hợp CSDL SQLite và bộ phân tích JobAnalyzer."""

    def test_job_id_1_loaded_with_cadivi_oe_full_data(self):
        """Đảm bảo hồ sơ công việc ID 1 trong CSDL chuẩn CADIVI Miền Trung OE và có đủ 128 câu hỏi + 16 cẩm nang."""
        db_path = os.path.join(current_dir, "job_detail.db")
        if os.path.exists(db_path):
            storage = JobStorage(db_path)
            job = storage.get_job(1)
            self.assertIsNotNone(job, "Hồ sơ Job ID 1 phải tồn tại trong CSDL")
            self.assertIn("CADIVI", job.get("company", "").upper())
            self.assertIn("OE", job.get("title", "").upper())
            analysis = job.get("analysis", {})
            interview = analysis.get("interview_prep", [])
            self.assertGreaterEqual(len(interview), 125, f"Job ID 1 phải có ít nhất 125 câu hỏi, hiện có {len(interview)}")
            guides = analysis.get("resources", {}).get("offline_guides", [])
            self.assertGreaterEqual(len(guides), 16, f"Job ID 1 phải gắn đủ 16 cẩm nang offline, hiện có {len(guides)}")
            guide_ids = [g.get("id") for g in guides]
            for req in ("planning_quality_ehs_cost", "cable_extrusion_wire_forensics", "oe_field_execution_case_test"):
                self.assertIn(req, guide_ids)

            exported_md = storage.export_job_markdown(1)
            self.assertNotIn("[[", exported_md, "export_job_markdown bị rò rỉ cú pháp thô '[['!")
            self.assertNotIn("]]", exported_md, "export_job_markdown bị rò rỉ cú pháp thô ']]'!")

    def test_mfg_analyzer_generates_128_questions(self):
        """Đảm bảo JobAnalyzer tự động nạp 128 câu hỏi và đủ 16 cẩm nang khi phân tích JD OE / Dây Cáp Điện."""
        analyzer = JobAnalyzer()
        mfg_jd = """
        Tuyển Chuyên Viên Tối Ưu Quy Trình (OE) — Nhà máy CADIVI Miền Trung
        - Phân tích năng suất, chỉ số OEE, OLE trên chuyền kéo sợi, bện, đùn bọc cáp XLPE/PVC
        - Triển khai SMED rút ngắn thời gian chuyển đổi màu nhựa và tiết diện
        - Kiểm soát định mức hao hụt vật tư BOM đồng/nhựa, cân bằng chuyền
        - Áp dụng Lean Manufacturing, Six Sigma DMAIC, 5S, Kaizen và Poka-Yoke tại Genba
        """
        result = analyzer.analyze(mfg_jd, force_offline=True)
        self.assertIsNotNone(result)
        self.assertEqual(result["category"], "Sản Xuất (Manufacturing)")
        analysis = result.get("analysis", {})
        interview = analysis.get("interview_prep", [])
        self.assertGreaterEqual(len(interview), 125, f"JD sản xuất phải tự động sinh ít nhất 125 câu hỏi, thực tế: {len(interview)}")
        guide_ids = [g.get("id") for g in analysis.get("resources", {}).get("offline_guides", [])]
        for req in ("planning_quality_ehs_cost", "cable_extrusion_wire_forensics", "oe_field_execution_case_test"):
            self.assertIn(req, guide_ids)

    def test_job_detail_app_interview_ui_filter_and_search(self):
        """Đảm bảo giao diện C-Engine JobDetailApp render 128 câu hỏi siêu tốc, Chế độ Luyện Phỏng Vấn ẩn đáp án & lưu tiến độ."""
        import time
        from JobDetailApp import JobDetailApp
        app = JobDetailApp()
        app.withdraw()
        orig_progress = app.storage.get_progress(1)
        try:
            t0 = time.perf_counter()
            app._display_job_detail(1)
            dt_display = (time.perf_counter() - t0) * 1000
            self.assertLess(dt_display, 400, f"_display_job_detail quá chậm: {dt_display:.1f} ms")

            # Chuyển sang tab Phỏng vấn để kích hoạt Lazy Render C-Engine 128 câu
            t1 = time.perf_counter()
            app.tabview.set("❓ Phỏng Vấn & Thực Chiến")
            app._on_tab_change()
            dt_interview = (time.perf_counter() - t1) * 1000
            self.assertLess(dt_interview, 650, f"Render 128 câu phỏng vấn quá chậm: {dt_interview:.1f} ms")

            total_q = len(interview_bank.get_all_questions())
            self.assertEqual(len(app._current_interview_raw), total_q)
            self.assertEqual(len(app._filtered_interview_items), total_q)

            # Kiểm tra không rò rỉ '[[' hoặc '**' trong giao diện tab Phỏng vấn và đã gắn thẻ thuật ngữ
            rendered_iv = app.txt_interview.get("1.0", "end")
            self.assertNotIn("[[", rendered_iv, "Tab Phỏng vấn bị rò rỉ cú pháp thô '[['!")
            self.assertNotIn("**", rendered_iv, "Tab Phỏng vấn bị rò rỉ dấu sao '**' thô!")
            all_tags = app.txt_interview.tag_names()
            self.assertIn("term_link", all_tags)
            self.assertIn("term::OEE", all_tags)
            self.assertIn("term::MES", all_tags)
            self.assertIn("term::Minitab", all_tags)
            self.assertIn("term::LOTO", all_tags)
            self.assertIn("term::RTY", all_tags)
            self.assertIn("term::Work Sampling", all_tags)

            # Kiểm tra Chế độ Luyện Phỏng Vấn (Ẩn đáp án -> Mở đáp án -> Đánh dấu Đã thuộc)
            app.var_quiz_mode.set(True)
            app._toggle_quiz_mode()
            hidden_text = app.txt_interview.get("1.0", "end")
            self.assertNotIn("Gợi ý trả lời & Điểm mấu chốt", hidden_text, "Chế độ luyện thi phải ẩn đáp án ban đầu!")
            self.assertIn("Xem gợi ý trả lời", hidden_text)

            app._revealed_qids.add("q_oee_01")
            app._update_interview_display(preserve_scroll=True)
            self.assertIn("Gợi ý trả lời & Điểm mấu chốt", app.txt_interview.get("1.0", "end"))

            # Tắt chế độ ẩn đáp án và kiểm tra lọc Chủ đề 17 (16 câu)
            app.var_quiz_mode.set(False)
            app._toggle_quiz_mode()
            app.cbo_interview_cat.set("Đùn Cáp Chuyên Sâu, Đứt Sợi, Thực Địa LSW/WCM & Test Thực Hành Vòng 2")
            app._update_interview_display()
            self.assertEqual(len(app._filtered_interview_items), 16)

            # Tìm kiếm từ khóa Spark và cụm có công thức 'cáp ABC'
            app.cbo_interview_cat.set("Tất cả chủ đề")
            app.ent_interview_search.delete(0, "end")
            app.ent_interview_search.insert(0, "Spark")
            app._update_interview_display()
            self.assertGreater(len(app._filtered_interview_items), 0)

            app.ent_interview_search.delete(0, "end")
            app.ent_interview_search.insert(0, "cáp ABC")
            app._update_interview_display()
            self.assertGreater(len(app._filtered_interview_items), 0)

            # Kiểm tra các tab Lazy còn lại + Tab Giáo Trình A–Z
            for tab_name in ["🎓 Giáo Trình A–Z", "🛠️ Ma Trận Kỹ Năng", "🧭 Lộ Trình Nắm Bắt", "📚 Kho Tài Liệu", "📝 Ghi Chú & JD Gốc"]:
                app.tabview.set(tab_name)
                app._on_tab_change()
            self.assertIn("term::OEE", app.txt_raw_jd.tag_names())

            # Kiểm tra Tab Giáo Trình A–Z: 32 bài, mở bài L4.2 (Six Sigma), không rò rỉ '[[' / '**', lưu SQLite
            app.open_curriculum_lesson("L4.2")
            self.assertEqual(app.tabview.get(), "🎓 Giáo Trình A–Z")
            self.assertEqual(app._current_lesson_id, "L4.2")
            self.assertEqual(app.lb_curriculum.size(), 32)
            curr_txt = app.txt_curriculum.get("1.0", "end")
            self.assertIn("Six Sigma", curr_txt)
            self.assertNotIn("[[", curr_txt, "Tab Giáo Trình bị rò rỉ cú pháp thô '[['!")
            self.assertNotIn("]]", curr_txt, "Tab Giáo Trình bị rò rỉ cú pháp thô ']]'!")
            self.assertNotIn("**", curr_txt, "Tab Giáo Trình bị rò rỉ dấu sao '**' thô!")
            self.assertIn("term::Six Sigma", app.txt_curriculum.tag_names())

            # Kiểm tra đánh dấu hoàn thành bài học lưu xuống SQLite
            was_done = bool(app._curriculum_done.get("L4.2", False))
            app._toggle_current_lesson_done()
            reloaded_prog = app.storage.get_progress(1)
            self.assertEqual(bool(reloaded_prog.get("curriculum", {}).get("L4.2", False)), not was_done)

            # Kiểm tra Live Hover Tooltip headless
            tip = TermHoverTooltip(app.txt_overview)
            tip._show("MES", 120, 120)
            self.assertIsNotNone(tip.tip_win)
            tip.hide()
            self.assertIsNone(tip.tip_win)

            # Mở thử Popup định nghĩa 'Six Sigma': xác nhận 0 self-link, có Green Belt/Lean Six Sigma riêng & common_mistakes!
            popup = app.open_term_popup("Six Sigma")
            self.assertIsNotNone(popup)
            ss_body = popup.tb.get("1.0", "end")
            self.assertIn("CADIVI", ss_body)
            self.assertIn("SAI LẦM KINH ĐIỂN", ss_body)
            self.assertNotIn("term::Six Sigma", popup.tb.tag_names(), "Popup Six Sigma KHÔNG được chứa tự-link (self-link)!")
            self.assertIn("term::Green Belt", popup.tb.tag_names(), "Popup Six Sigma phải mở được trang riêng của Green Belt!")
            self.assertIn("term::Lean Six Sigma", popup.tb.tag_names(), "Popup Six Sigma phải mở được trang riêng của Lean Six Sigma!")
            popup.show_term("Green Belt", push_history=True)
            self.assertEqual(popup.current_info["term"], "Green Belt")
            self.assertEqual(len(popup.history), 1)
            self.assertIn("Six Sigma › Green Belt", popup.lbl_breadcrumb.cget("text"))
            popup._go_back()
            self.assertEqual(popup.current_info["term"], "Six Sigma")
            popup.destroy()

            browser = app._open_glossary_browser()
            self.assertEqual(browser.lb.size(), 202)
            browser.destroy()
        finally:
            app.storage.save_progress(1, orig_progress)
            app.destroy()


class TestTermGlossaryEngine(unittest.TestCase):
    """Kiểm tra kho từ điển thuật ngữ OE/CADIVI, làm giàu nội dung 202/202, chống self-link & Giáo trình 32 bài."""

    def test_glossary_completeness_ast_unique_and_cleanliness(self):
        """Đảm bảo đủ 202 thuật ngữ, 0 khóa trùng lặp AST, 202/202 đã làm giàu chi tiết, 0 ký tự lỗi, 100% liên kết hợp lệ."""
        glossary_path = os.path.join(current_dir, "term_glossary.py")
        with open(glossary_path, "r", encoding="utf-8") as fh:
            tree = ast.parse(fh.read())
        ast_keys = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name) and t.id == "GLOSSARY":
                        for k in node.value.keys:
                            if isinstance(k, ast.Constant):
                                ast_keys.append(k.value)
        self.assertEqual(len(ast_keys), len(set(ast_keys)), "Phát hiện khóa trùng lặp trong GLOSSARY!")
        self.assertEqual(len(ast_keys), 202, f"Yêu cầu đúng 202 thuật ngữ, hiện có {len(ast_keys)}")

        terms = term_glossary.get_all_terms()
        self.assertEqual(len(terms), 202)
        self.assertEqual(set(glossary_enrichment.ENRICHMENTS.keys()), set(term_glossary.GLOSSARY.keys()), "100% 202 thuật ngữ phải có enrichment!")

        valid_lesson_ids = {l["id"] for l in oe_curriculum.get_all_lessons()}
        for core in [
            "MES", "Minitab", "OEE", "OLE", "SMED", "BOM", "ERP", "XLPE", "Spark Tester",
            "Laser Gauge", "Copper Give-away", "Over-thickness", "RBD", "DMAIC", "RCCP",
            "S&OP", "MPS", "MRP", "CRP", "RTY", "FPY", "LOTO", "ISO 50001", "ACSR",
            "ABC Cable", "Mica FR", "Partial Discharge", "Water Immersion", "Standard Cost",
            "Hoshin Kanri", "ADKAR", "L/D Ratio", "Melt Pressure", "DDR", "Sharkskin",
            "Wire Break Forensics", "Cup-and-Cone", "Solar Cable", "Braiding", "QCVN 4",
            "Work Sampling", "Cost Deployment", "LSW", "LPA", "Escalation Matrix", "Wrench Time",
            "Six Sigma", "Green Belt", "Lean Six Sigma", "HMI", "MSA", "p-value",
            "Drum-Buffer-Rope", "Bottleneck", "Jishu Hozen", "Red Tag", "Pull System",
            "Campaign Scheduling", "Standard Work"
        ]:
            info = term_glossary.get_term(core)
            self.assertIsNotNone(info, f"Thiếu thuật ngữ bắt buộc '{core}'")
            self.assertEqual(info["term"], core, f"Thuật ngữ '{core}' phải là khóa độc lập, không bị gộp alias!")
            self.assertIn("CADIVI", (info.get("cadivi_application", "") + info.get("cadivi_example", "")).upper(), f"'{core}' thiếu nội dung gắn thực tế CADIVI")

        bad_tokens = ["\x0c", "\x08", r"\frac", r"\times", r"\text", "_{", "$", "**", "[[", "]]"]
        for info in terms:
            for field in ["term", "full_name", "category", "short_desc", "definition", "formula_or_spec", "cadivi_application", "cadivi_example", "common_mistakes"]:
                val = info.get(field, "")
                if field != "formula_or_spec":
                    self.assertTrue(val and len(val) > 1, f"Thuật ngữ '{info.get('term')}' bị thiếu trường '{field}'")
                for tok in bad_tokens:
                    self.assertNotIn(tok, val, f"Thuật ngữ '{info.get('term')}' trường '{field}' còn token lỗi {repr(tok)}")
            self.assertGreaterEqual(len(info["definition"]), 350, f"Định nghĩa '{info['term']}' quá ngắn (<350 ký tự)")
            self.assertGreaterEqual(len(info["cadivi_example"]), 280, f"Ví dụ '{info['term']}' quá ngắn (<280 ký tự)")
            self.assertIn(info.get("lesson_id"), valid_lesson_ids, f"Thuật ngữ '{info['term']}' trỏ lesson_id không hợp lệ: {info.get('lesson_id')}")
            for rel in info.get("related", []):
                self.assertIn(rel, term_glossary.GLOSSARY, f"Thuật ngữ '{info.get('term')}' trỏ related không phải khóa chính: '{rel}'")
            dk = info.get("doc_key", "")
            if dk:
                self.assertIn(dk, offline_knowledge.OFFLINE_DOCS, f"Thuật ngữ '{info.get('term')}' trỏ doc_key không tồn tại: '{dk}'")

    def test_zero_self_links_across_all_202_terms(self):
        """Quét toàn bộ 202 thuật ngữ với exclude_key=term: đảm bảo 0/202 thuật ngữ tự gắn link về chính nó."""
        root = tk.Tk()
        root.withdraw()
        try:
            _, tb = create_c_engine_text(root)
            for key, info in term_glossary.GLOSSARY.items():
                tb.delete("1.0", "end")
                for t in list(tb.tag_names()):
                    if t.startswith("term::"):
                        tb.tag_delete(t)
                combined = "\n".join([
                    info.get("short_desc", ""),
                    info.get("definition", ""),
                    info.get("cadivi_application", ""),
                    info.get("cadivi_example", ""),
                    info.get("common_mistakes", ""),
                ])
                insert_with_glossary(tb, combined, "normal", exclude_key=key)
                self.assertNotIn(
                    f"term::{key}",
                    tb.tag_names(),
                    f"Thuật ngữ '{key}' vẫn bị tự-link (self-link) khi truyền exclude_key!"
                )
        finally:
            root.destroy()

    def test_curriculum_8_modules_32_lessons_integrity(self):
        """Đảm bảo Giáo Trình A–Z có đủ 8 Học phần, 32 bài học không trùng ID, 100% công thức & liên kết hợp lệ."""
        mods = oe_curriculum.get_all_modules()
        lessons = oe_curriculum.get_all_lessons()
        self.assertEqual(len(mods), 8)
        self.assertEqual(len(lessons), 32)
        mod_ids = {m["id"] for m in mods}
        les_ids = [l["id"] for l in lessons]
        self.assertEqual(len(les_ids), len(set(les_ids)), "Phát hiện mã bài học trùng lặp trong oe_curriculum!")

        pat = re.compile(r"\[\[([^|\]]+)(?:\|([^\]]+))?\]\]")
        iv_cats = set(interview_bank.get_categories())
        for les in lessons:
            lid = les["id"]
            self.assertIn(les["module_id"], mod_ids)
            self.assertGreaterEqual(len(les.get("objectives", [])), 2, f"{lid} cần ít nhất 2 mục tiêu")
            self.assertGreaterEqual(len(les.get("checkpoints", [])), 3, f"{lid} cần ít nhất 3 câu hỏi tự kiểm tra")
            self.assertGreater(len(les.get("core_theory", "")), 200, f"{lid} lý thuyết quá ngắn")
            self.assertGreater(len(les.get("worked_example", "")), 100, f"{lid} ví dụ quá ngắn")
            self.assertIn(les.get("doc_key"), offline_knowledge.OFFLINE_DOCS, f"{lid} doc_key không hợp lệ")
            self.assertIn(les.get("interview_category"), iv_cats, f"{lid} interview_category không hợp lệ")
            for kt in les.get("key_terms", []):
                self.assertIsNotNone(term_glossary.get_term(kt), f"{lid} key_term không tồn tại: {kt}")
            for fld in ("title", "core_theory", "worked_example", "hands_on_drill"):
                txt = les.get(fld, "")
                self.assertNotIn("$", txt, f"{lid}.{fld} còn ký tự '$'")
                for m in pat.finditer(txt):
                    self.assertIsNotNone(term_glossary.get_term(m.group(1).strip()), f"{lid}.{fld} khóa lỗi: {m.group(0)}")

    def test_explicit_formula_disambiguation_and_markdown_links(self):
        """Kiểm tra công thức [[TermKey|DisplayText]] tách nghĩa chính xác ABC Cable vs Cycle Counting, PD và sinh link Markdown."""
        sample = "So sánh [[ABC Cable|ABC]] với [[Cycle Counting|ABC]] và [[Partial Discharge|PD]] cùng [[MES]]."
        segs = term_glossary.parse_rich_segments(sample, auto_detect=True)
        linked = [(txt, key) for txt, key in segs if key is not None]
        self.assertEqual(linked, [
            ("ABC", "ABC Cable"),
            ("ABC", "Cycle Counting"),
            ("PD", "Partial Discharge"),
            ("MES", "MES"),
        ])
        # Đảm bảo chữ hiển thị sạch, không có ký hiệu ↗ hay ngoặc [[
        joined = "".join(txt for txt, _ in segs)
        self.assertEqual(joined, "So sánh ABC với ABC và PD cùng MES.")
        self.assertNotIn("↗", joined)
        self.assertNotIn("[[", joined)

        # Kiểm tra strip_term_formulas và fallback khóa không tồn tại
        self.assertEqual(
            term_glossary.strip_term_formulas("Thử [[NonExistentKey|văn bản thường]] và [[MES]]."),
            "Thử văn bản thường và MES."
        )
        fallback_segs = term_glossary.parse_rich_segments("Thử [[NonExistentKey|văn bản thường]].", auto_detect=False)
        self.assertEqual("".join(t for t, _ in fallback_segs), "Thử văn bản thường.")
        self.assertTrue(all(k is None for _, k in fallback_segs))

        # Kiểm tra chuyển đổi sang Markdown internal anchor link
        md_linked = term_glossary.convert_formulas_to_markdown_links(sample)
        self.assertIn("[ABC](#term-abc-cable)", md_linked)
        self.assertIn("[ABC](#term-cycle-counting)", md_linked)
        self.assertIn("[PD](#term-partial-discharge)", md_linked)
        self.assertIn("[MES](#term-mes)", md_linked)
        self.assertNotIn("[[", md_linked)

    def test_glossary_matcher_precision_no_false_positives(self):
        """Đảm bảo nhận diện đúng MES, Minitab, OEE, Spark Tester và KHÔNG khớp nhầm vào giữa từ khác (times, shoes, poem)."""
        sample = "Sử dụng MES, Minitab và OEE trên máy đùn XLPE có Spark Tester để giảm Copper Give-away."
        spans = term_glossary.find_term_spans(sample)
        keys = [s[3] for s in spans]
        for expected in ["MES", "Minitab", "OEE", "Extruder", "XLPE", "Spark Tester", "Copper Give-away"]:
            self.assertIn(expected, keys, f"Không khớp được thuật ngữ '{expected}' trong: {keys}")

        # Kiểm tra không khớp nhầm từ viết tắt ngắn vào từ tiếng Anh/Việt thường
        false_sample = "Many times the shoes and poem choe mes oe bom are not acronyms."
        false_spans = term_glossary.find_term_spans(false_sample)
        self.assertEqual(false_spans, [], f"Phát hiện khớp nhầm thuật ngữ: {false_spans}")

    def test_term_popup_and_browser_headless(self):
        """Khởi tạo headless TermDetailPopup cho MES, Minitab, OEE, LOTO, RTY và GlossaryBrowserDialog xác nhận 0 lỗi."""
        root = tk.Tk()
        root.withdraw()
        try:
            for key in ["MES", "Minitab", "OEE", "Spark Tester", "Copper Give-away", "LOTO", "RTY", "ABC Cable", "Standard Cost"]:
                pop = TermDetailPopup(root, key)
                title_txt = pop.lbl_title.cget("text")
                body_txt = pop.tb.get("1.0", "end")
                self.assertIn(key, title_txt)
                self.assertIn("CADIVI", body_txt)
                self.assertNotIn("[[", body_txt)
                pop.destroy()

            dlg = GlossaryBrowserDialog(root)
            dlg.ent_search.insert(0, "MES")
            dlg._refresh_list()
            self.assertGreaterEqual(len(dlg.filtered_terms), 1)
            dlg.destroy()
        finally:
            root.destroy()


if __name__ == "__main__":
    unittest.main()
