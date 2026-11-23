#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
job_analyzer.py - Bộ Máy Phân Tích Hồ Sơ Công Việc Kép (Dual-Engine Job Analyzer)
Bao gồm:
  1. Offline Smart Rule-based Parser: Phân tích 100% offline không cần internet/API.
  2. Gemini AI Deep Analyzer: Phân tích chuyên sâu khi có API Key.
Tuân thủ Mô hình 5 Tầng Kiến Thức (5-Tier Job Intelligence Model) theo job_detail_analysis_rules.md.
"""

import os
import re
import sys
import json
import urllib.request
import urllib.error

try:
    import offline_knowledge
except Exception:
    offline_knowledge = None

try:
    import interview_bank
except Exception:
    interview_bank = None

# Đảm bảo UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


# =====================================================================
# BẢNG TỪ ĐIỂN TRI THỨC CÔNG NGHỆ CHUẨN (OFFLINE KNOWLEDGE BASE)
# =====================================================================
TECH_CATALOG = {
    "python": {
        "display": "Python",
        "category": "Backend",
        "doc_key": "python_core",
        "docs": {"name": "Python Official Docs", "url": "https://docs.python.org/3/", "desc": "Tài liệu ngôn ngữ chính thống, thư viện chuẩn và cú pháp"},
        "books": ["Fluent Python (Luciano Ramalho)", "Python Tricks: A Buffet of Awesome Features (Dan Bader)"],
        "keywords": ["python asyncio best practices", "python gil multithreading vs multiprocessing", "python type hinting mypy"],
        "questions": [
            {"question": "Sự khác biệt cốt lõi giữa List và Tuple trong Python là gì, và tại sao Dict lookup lại đạt O(1)?", "type": "Concept", "key_points": "Tuple là immutable, list là mutable; Dict dựa trên bảng băm (hash table), key phải hashable."},
            {"question": "Trình bày cơ chế hoạt động của GIL (Global Interpreter Lock) và cách xử lý CPU-bound vs IO-bound tasks?", "type": "Deep Dive", "key_points": "GIL chỉ cho 1 thread chạy bytecode tại 1 thời điểm. IO-bound dùng asyncio/threading; CPU-bound dùng multiprocessing."}
        ]
    },
    "fastapi": {
        "display": "FastAPI",
        "category": "Backend",
        "doc_key": "python_core",
        "docs": {"name": "FastAPI Documentation", "url": "https://fastapi.tiangolo.com/", "desc": "Framework web Python hiện đại, bất đồng bộ và tự động sinh Swagger/OpenAPI"},
        "books": ["Building Data Science Applications with FastAPI (François Voron)"],
        "keywords": ["fastapi dependency injection pattern", "fastapi async background tasks", "pydantic v2 validation"],
        "questions": [
            {"question": "Dependency Injection trong FastAPI hoạt động như thế nào qua hàm `Depends()`?", "type": "Concept", "key_points": "Tái sử dụng logic xác thực, DB session, tự động giải quyết phụ thuộc theo đồ thị (dependency graph)."}
        ]
    },
    "django": {
        "display": "Django",
        "category": "Backend",
        "doc_key": "python_core",
        "docs": {"name": "Django Project Docs", "url": "https://docs.djangoproject.com/", "desc": "Framework web đầy đủ pin (batteries-included) cho Python"},
        "books": ["Two Scoops of Django (Daniel Feldroy)"],
        "keywords": ["django orm n+1 problem select_related prefetch_related", "django custom user model migration"],
        "questions": [
            {"question": "Cách khắc phục lỗi N+1 Query trong Django ORM bằng `select_related` và `prefetch_related`?", "type": "Deep Dive", "key_points": "select_related dùng SQL JOIN (cho ForeignKey/OneToOne); prefetch_related dùng 2 query riêng biệt với IN (cho ManyToMany/reverse FK)."}
        ]
    },
    "react": {
        "display": "React",
        "category": "Frontend",
        "doc_key": "react_fe",
        "docs": {"name": "React Official Docs", "url": "https://react.dev/", "desc": "Thư viện giao diện người dùng dựa trên thành phần (Components)"},
        "books": ["Learning React (Alex Banks & Eve Porcello)", "Refactoring UI (Adam Wathan & Steve Schoger)"],
        "keywords": ["react 18 concurrent mode useTransition", "react custom hooks clean architecture", "react memo useCallback useMemo trade-offs"],
        "questions": [
            {"question": "Khi nào nên dùng `useCallback` và `useMemo`, và việc lạm dụng chúng gây hại gì?", "type": "Concept", "key_points": "Dùng khi truyền callback xuống component con bọc React.memo hoặc tính toán nặng. Lạm dụng gây tốn bộ nhớ và tăng chi phí so sánh deps."},
            {"question": "Virtual DOM hoạt động như thế nào và thuật toán Reconciliation xử lý diff ra sao?", "type": "Concept", "key_points": "Cây JS đại diện UI, so sánh bản cũ và mới để chỉ cập nhật các node DOM thật bị thay đổi (heuristics O(n) với key)."}
        ]
    },
    "javascript": {
        "display": "JavaScript (ES6+)",
        "category": "Frontend",
        "doc_key": "react_fe",
        "docs": {"name": "MDN Web Docs (JavaScript)", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript", "desc": "Bách khoa toàn thư chính thức về JS, Web APIs và runtime"},
        "books": ["You Don't Know JS Yet (Kyle Simpson)", "Eloquent JavaScript (Marijn Haverbeke)"],
        "keywords": ["javascript event loop microtask vs macrotask", "javascript closures prototype chain", "javascript promise.all vs allsettled"],
        "questions": [
            {"question": "Giải thích Event Loop trong JavaScript: Microtasks (Promise) và Macrotasks (setTimeout) ưu tiên thế nào?", "type": "Deep Dive", "key_points": "Call stack rỗng -> toàn bộ Microtask queue được xả hết trước khi chuyển sang Macrotask tiếp theo."}
        ]
    },
    "typescript": {
        "display": "TypeScript",
        "category": "Frontend",
        "doc_key": "react_fe",
        "docs": {"name": "TypeScript Handbook", "url": "https://www.typescriptlang.org/docs/", "desc": "Cẩm nang chính thức về hệ thống kiểu tĩnh của TypeScript"},
        "books": ["Programming TypeScript (Boris Cherny)", "Effective TypeScript (Dan Vanderkam)"],
        "keywords": ["typescript generics utility types Partial Record", "typescript discriminated unions type guards"],
        "questions": [
            {"question": "Khác biệt giữa `type` và `interface` trong TypeScript, khi nào ưu tiên cái nào?", "type": "Concept", "key_points": "Interface mở rộng được (declaration merging), phù hợp định nghĩa OOP/API; type mạnh hơn về union, primitives, tuples, utility types."}
        ]
    },
    "docker": {
        "display": "Docker",
        "category": "DevOps",
        "doc_key": "docker_devops",
        "docs": {"name": "Docker Documentation", "url": "https://docs.docker.com/", "desc": "Nền tảng container hóa ứng dụng độc lập môi trường"},
        "books": ["Docker Deep Dive (Nigel Poulton)"],
        "keywords": ["docker multi-stage builds optimization", "docker layer caching best practices", "docker-compose healthchecks"],
        "questions": [
            {"question": "Lợi ích của Docker Multi-stage build là gì và làm sao để giảm kích thước image từ 1GB xuống 50MB?", "type": "Scenario", "key_points": "Tách riêng môi trường build (cần compiler) và runtime (chỉ chứa binary/artifacts thuần túy, dùng alpine/distroless)."}
        ]
    },
    "kubernetes": {
        "display": "Kubernetes (K8s)",
        "category": "DevOps",
        "doc_key": "docker_devops",
        "docs": {"name": "Kubernetes Documentation", "url": "https://kubernetes.io/docs/", "desc": "Hệ thống điều phối container quy mô lớn"},
        "books": ["Kubernetes in Action (Marko Lukša)"],
        "keywords": ["k8s deployment rolling update vs blue-green", "k8s ingress controller cert-manager", "k8s horizontal pod autoscaler"],
        "questions": [
            {"question": "Khác biệt giữa Liveness Probe và Readiness Probe trong K8s Pod là gì?", "type": "Deep Dive", "key_points": "Liveness chết -> K8s restart container; Readiness chưa sẵn sàng -> K8s tạm gỡ Pod khỏi danh sách nhận traffic của Service."}
        ]
    },
    "postgresql": {
        "display": "PostgreSQL",
        "category": "Backend",
        "doc_key": "sql_db",
        "docs": {"name": "PostgreSQL Documentation", "url": "https://www.postgresql.org/docs/", "desc": "Hệ quản trị CSDL quan hệ mã nguồn mở mạnh mẽ nhất thế giới"},
        "books": ["Designing Data-Intensive Applications (Martin Kleppmann)", "The Art of PostgreSQL (Dimitri Fontaine)"],
        "keywords": ["postgresql explain analyze query plan index scan", "postgresql transaction isolation levels mvcc", "postgresql jsonb indexing gin"],
        "questions": [
            {"question": "Cơ chế MVCC (Multi-Version Concurrency Control) trong PostgreSQL hoạt động thế nào để tránh lock khi đọc?", "type": "Deep Dive", "key_points": "Mỗi row có xmin, xmax đại diện transaction ID; câu lệnh SELECT chỉ đọc snapshot dữ liệu nhìn thấy được mà không block câu lệnh WRITE."}
        ]
    },
    "sql": {
        "display": "SQL & Relational DB",
        "category": "Backend",
        "doc_key": "sql_db",
        "docs": {"name": "SQL Documentation & Standards", "url": "https://mode.com/sql-tutorial/", "desc": "Cú pháp truy vấn quan hệ, index, transaction ACID"},
        "books": ["SQL Antipatterns (Bill Karwin)"],
        "keywords": ["sql indexing b-tree composite index column order", "sql window functions over partition by"],
        "questions": [
            {"question": "Thứ tự các cột trong Composite Index (Index nhiều cột) ảnh hưởng như thế nào đến khả năng tận dụng Index?", "type": "Concept", "key_points": "Quy tắc tiền tố trái nhất (Leftmost prefix rule): Index (A, B, C) chỉ dùng được khi query có điều kiện trên A."}
        ]
    },
    "redis": {
        "display": "Redis",
        "category": "Backend",
        "doc_key": "redis_cache",
        "docs": {"name": "Redis Documentation", "url": "https://redis.io/docs/", "desc": "In-memory data structure store dùng làm cache, message broker"},
        "books": ["Redis in Action (Josiah L. Carlson)"],
        "keywords": ["redis caching strategies cache aside write through", "redis cache avalanche cache breakdown solution", "redis pub sub vs streams"],
        "questions": [
            {"question": "Xử lý hiện tượng Cache Breakdown (Hot key hết hạn đồng thời hàng triệu request ùa vào DB) như thế nào?", "type": "Scenario", "key_points": "Dùng Mutex/Distributed Lock để chỉ 1 process query DB và update cache; hoặc chủ động refresh cache nền (logical expiration)."}
        ]
    },
    "git": {
        "display": "Git",
        "category": "Tools",
        "doc_key": "git_vcs",
        "docs": {"name": "Pro Git Book", "url": "https://git-scm.com/book/en/v2", "desc": "Tài liệu chính thức toàn diện về hệ thống kiểm soát phiên bản Git"},
        "books": ["Pro Git (Scott Chacon and Ben Straub)"],
        "keywords": ["git rebase vs merge trade-offs", "git cherry-pick and bisect debugging", "git conflict resolution in detached head"],
        "questions": [
            {"question": "Khi nào nên dùng `git rebase` và khi nào nên dùng `git merge`? Quy tắc vàng của Rebase là gì?", "type": "Concept", "key_points": "Merge giữ nguyên lịch sử nhánh, an toàn cho branch dùng chung; Rebase tạo lịch sử tuyến tính sạch sẽ, TUYỆT ĐỐI không rebase các public/shared branch."}
        ]
    },
    "lean": {
        "display": "Lean Manufacturing (TPS & 7 Lãng Phí)",
        "category": "Sản Xuất (Manufacturing)",
        "doc_key": "lean_muda",
        "docs": {"name": "Lean Enterprise Institute (LEI)", "url": "https://www.lean.org/", "desc": "Tổ chức quốc tế phi lợi nhuận về triết lý sản xuất tinh gọn và chuyển đổi Lean"},
        "books": ["Toyota Production System: Beyond Large-Scale Production (Taiichi Ohno)", "Learning to See: Value Stream Mapping (Mike Rother & John Shook)"],
        "keywords": ["7 wastes muda lean manufacturing examples", "value stream mapping vsm future state", "5s visual management implementation"],
        "questions": [
            {"question": "Kể tên và phân tích 7 loại lãng phí (Muda) trong sản xuất tinh gọn. Loại lãng phí nào được coi là nguy hiểm nhất và tại sao?", "type": "Concept", "key_points": "TIMWOOD: Transportation, Inventory, Motion, Waiting, Overproduction, Overprocessing, Defects. Overproduction nguy hiểm nhất vì nó sinh ra và che giấu tất cả các loại lãng phí còn lại."},
            {"question": "Trình bày cách vẽ và phân tích Bản đồ chuỗi giá trị (Value Stream Mapping - VSM) từ Current State sang Future State?", "type": "Deep Dive", "key_points": "Theo dõi dòng vật tư và dòng thông tin từ nhà cung ứng đến khách hàng; tính toán Lead Time và Process Time; xác định các điểm dồn ứ (WIP) để thiết kế hệ thống kéo (Pull System/Kanban)."}
        ]
    },
    "oee": {
        "display": "Chỉ Số OEE & 6 Tổn Thất Lớn",
        "category": "Sản Xuất (Manufacturing)",
        "doc_key": "oee",
        "docs": {"name": "OEE Industry Standard Guide (Arno Koch)", "url": "https://www.oee.com/", "desc": "Tiêu chuẩn quốc tế và hướng dẫn chi tiết đo lường Overall Equipment Effectiveness"},
        "books": ["OEE for Operators: Overall Equipment Effectiveness (Productivity Press)"],
        "keywords": ["how to calculate OEE step by step excel template", "six big losses tpm breakdown small stops", "world class oee benchmark 85 percent"],
        "questions": [
            {"question": "Trình bày công thức tính OEE và phân tích 6 tổn thất lớn (Six Big Losses) tương ứng với 3 thành phần của OEE?", "type": "Concept", "key_points": "OEE = Availability (Breakdown, Setup) x Performance (Minor Stops, Reduced Speed) x Quality (Startup Rejects, Production Defects)."},
            {"question": "Nếu OEE của máy đạt 88% nhưng nhà máy vẫn chậm giao hàng và chi phí tăng, nguyên nhân do đâu?", "type": "Scenario", "key_points": "Bị bẫy Overproduction (sản xuất mã hàng không cần thiết để lấy OEE cao), OLE thấp do tốn quá nhiều nhân công để nuôi máy, hoặc nhịp sản xuất không khớp với Takt Time của khách hàng."}
        ]
    },
    "ole": {
        "display": "Chỉ Số OLE (Hiệu Quả Lao Động)",
        "category": "Sản Xuất (Manufacturing)",
        "doc_key": "ole",
        "docs": {"name": "Overall Labor Effectiveness (OLE) Guide", "url": "https://en.wikipedia.org/wiki/Overall_labor_effectiveness", "desc": "Phương pháp luận đo lường hiệu quả lao động toàn diện trong nhà máy"},
        "books": ["Managing Factory Maintenance (Joel Levitt)"],
        "keywords": ["overall labor effectiveness OLE calculation formula", "labor utilization vs labor efficiency", "takt time line balancing"],
        "questions": [
            {"question": "Phân biệt giữa OEE và OLE. Làm sao để nâng cao OLE mà không bắt công nhân tăng ca quá sức?", "type": "Deep Dive", "key_points": "OEE đo hiệu suất máy móc; OLE đo hiệu quả sử dụng sức lao động. Nâng OLE bằng cách cân bằng chuyền (Line Balancing), triệt tiêu thao tác thừa (Motion), chuẩn hóa thao tác (SOP), chứ không ép tăng tốc độ làm việc."}
        ]
    },
    "smed": {
        "display": "SMED (Chuyển Đổi Nhanh Dưới 10 Phút)",
        "category": "Sản Xuất (Manufacturing)",
        "doc_key": "smed",
        "docs": {"name": "SMED Quick Changeover Methodology", "url": "https://en.wikipedia.org/wiki/Single-minute_exchange_of_die", "desc": "Hệ thống Single-Minute Exchange of Die rút ngắn thời gian đổi khuôn/mã hàng"},
        "books": ["A Revolution in Manufacturing: The SMED System (Shigeo Shingo)"],
        "keywords": ["smed quick changeover implementation steps", "internal vs external setup time lean", "quick clamp 1 turn bolt smed"],
        "questions": [
            {"question": "Nêu 4 bước cụ thể của phương pháp SMED để giảm thời gian đổi khuôn từ 60 phút xuống 15 phút?", "type": "Scenario", "key_points": "(1) Quan sát quay video hiện trạng; (2) Tách thao tác Trong (Internal) và Ngoài (External); (3) Chuyển thao tác Trong thành Ngoài (chuẩn bị trước khi máy dừng); (4) Tinh gọn thao tác Trong (dùng chốt 1 chạm, tiêu chuẩn hóa ốc vít, kịch bản 2 người song song)."}
        ]
    },
    "bom": {
        "display": "Quản Lý Định Mức BOM & Hao Phí",
        "category": "Sản Xuất (Manufacturing)",
        "doc_key": "bom_cost",
        "docs": {"name": "Bill of Materials (BOM) Management Standards", "url": "https://en.wikipedia.org/wiki/Bill_of_materials", "desc": "Cấu trúc cây định mức nguyên vật liệu, phế phẩm và kiểm soát giá thành"},
        "books": ["Manufacturing Planning and Control for Supply Chain Management (Jacobs)"],
        "keywords": ["bill of materials BOM variance analysis production cost", "scrap rate vs technological loss BOM", "poka yoke scrap reduction"],
        "questions": [
            {"question": "Làm thế nào để phát hiện và kiểm soát chênh lệch giữa hao phí nguyên vật liệu thực tế so với định mức BOM?", "type": "Deep Dive", "key_points": "Kiểm soát theo Lô (Batch), phân tách hao phí công nghệ (Scrap do phôi dập) vs hao phí lỗi thao tác (Defects), vẽ Pareto xác định 20% linh kiện chiếm 80% hao hụt và áp dụng Poka-Yoke."}
        ]
    },
    "powerbi": {
        "display": "Microsoft Power BI (Dashboard Sản Xuất)",
        "category": "Tools",
        "doc_key": "powerbi_mfg",
        "docs": {"name": "Power BI Documentation", "url": "https://learn.microsoft.com/en-us/power-bi/", "desc": "Tài liệu chính thức về xây dựng báo cáo phân tích và Dashboard dữ liệu trực quan"},
        "books": ["The Definitive Guide to DAX (Alberto Ferrari & Marco Russo)"],
        "keywords": ["power bi manufacturing dashboard oee dax", "power bi scheduled refresh on-premises gateway", "power bi pareto chart dax measure"],
        "questions": [
            {"question": "Làm thế nào để thiết kế một Dashboard OEE/OLE trên Power BI tự động cập nhật từ các file log sản xuất hàng ngày?", "type": "Scenario", "key_points": "Dùng Power Query Folder Connector kết nối thư mục log, làm sạch và unpivot dữ liệu; tạo Star Schema model; viết DAX Measure tính Availability, Performance, Quality; thiết lập On-premises Gateway tự động refresh."}
        ]
    },
    "minitab": {
        "display": "Minitab (Thống Kê Chất Lượng & Six Sigma)",
        "category": "Tools",
        "doc_key": "minitab_spc",
        "docs": {"name": "Minitab Support & Documentation", "url": "https://support.minitab.com/", "desc": "Tài liệu phân tích kiểm soát quá trình thống kê SPC và năng lực quá trình Cpk"},
        "books": ["Six Sigma Quality Improvement with Minitab (G. Rex Bryce)"],
        "keywords": ["minitab process capability cpk ppk interpretation", "minitab spc xbar r chart out of control rules", "minitab anova hypothesis testing"],
        "questions": [
            {"question": "Chỉ số Cpk khác gì so với Ppk, và khi nào một quá trình sản xuất được coi là có năng lực đạt chuẩn?", "type": "Concept", "key_points": "Cpk đo lường năng lực ngắn hạn (trong nhóm - Within group), Ppk đo lường năng lực dài hạn (toàn bộ - Overall). Quá trình đạt chuẩn khi Cpk >= 1.33 (tương đương 4 Sigma, < 63 ppm lỗi)."}
        ]
    },
    "excel": {
        "display": "Microsoft Excel Nâng Cao (Power Query / VBA)",
        "category": "Tools",
        "doc_key": "excel_mfg",
        "docs": {"name": "Excel Help & Training", "url": "https://support.microsoft.com/excel", "desc": "Cẩm nang tra cứu hàm, Power Query và tự động hóa Macro VBA"},
        "books": ["Excel 2019 Power Programming with VBA (Michael Alexander)"],
        "keywords": ["excel power query combine files from folder", "excel pareto chart 80 20 rule production", "excel vba automate daily production report"],
        "questions": [
            {"question": "Ưu điểm của việc dùng Power Query so với viết công thức VLOOKUP/INDEX-MATCH truyền thống khi xử lý báo cáo sản xuất hàng triệu dòng?", "type": "Concept", "key_points": "Power Query nạp dữ liệu vào Data Model nén bộ nhớ (VertiPaq), không làm đơ file Excel, tự động hóa toàn bộ các bước làm sạch bằng 1 nút Refresh, xử lý được hàng triệu dòng vượt giới hạn 1,048,576 dòng của sheet."}
        ]
    },
    "autocad": {
        "display": "AutoCAD (Layout Nhà Xưởng & Sơ Đồ Di Chuyển)",
        "category": "Tools",
        "doc_key": "autocad_layout",
        "docs": {"name": "Autodesk AutoCAD Documentation", "url": "https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/AutoCAD-Help.html", "desc": "Phần mềm thiết kế bản vẽ kỹ thuật 2D/3D và bố trí mặt bằng nhà máy"},
        "books": ["AutoCAD 2024 for Beginners (CADFolks)"],
        "keywords": ["plant layout optimization autocad lean manufacturing", "spaghetti diagram autocad plant layout", "u-shaped cell layout design"],
        "questions": [
            {"question": "Khi thiết kế lại mặt bằng nhà xưởng (Plant Layout) bằng AutoCAD, những nguyên tắc Lean nào cần ưu tiên?", "type": "Concept", "key_points": "Bố trí chuyền chữ U (U-shaped), luồng một sản phẩm (One-piece flow), giảm tối đa khoảng cách vận chuyển (Muda of Transport), phân định rõ luồng người và luồng xe nâng để đảm bảo an toàn 5S."}
        ]
    },
    "erp_mes": {
        "display": "Hệ Thống ERP (SAP PP) & MES Sản Xuất",
        "category": "Tools",
        "doc_key": "erp_mes",
        "docs": {"name": "SAP Production Planning (PP) Overview", "url": "https://help.sap.com/", "desc": "Phân hệ quản lý kế hoạch sản xuất, lệnh sản xuất và định mức vật tư BOM"},
        "books": ["Production Planning and Control with SAP (Jawad Akhtar)"],
        "keywords": ["sap pp work order routing bom confirmation", "mes manufacturing execution system plc integration", "sap standard cost vs actual cost variance"],
        "questions": [
            {"question": "Sự kết hợp giữa hệ thống MES và hệ thống ERP trong việc quản lý năng suất nhà máy diễn ra như thế nào?", "type": "Deep Dive", "key_points": "ERP nắm kế hoạch cấp cao (Lệnh sản xuất, BOM, tồn kho); MES điều hành trực tiếp dưới xưởng (thu thập tín hiệu máy từ PLC, ghi nhận thời gian chạy/dừng, số lượng lỗi thời gian thực); MES gửi dữ liệu thực tế ngược về ERP để hạch toán chi phí."}
        ]
    },
    "cable_mfg": {
        "display": "Công Nghệ & Máy Móc Sản Xuất Dây Cáp Điện (Kéo–Ủ–Bện–Đùn–Spark Test)",
        "category": "Sản Xuất (Manufacturing)",
        "doc_key": "cable_mfg_machines",
        "aliases": ["cadivi", "dây cáp", "cáp điện", "kéo sợi", "máy bện", "đùn", "xlpe", "spark tester", "cáp lực"],
        "docs": {"name": "Tiêu Chuẩn Dây Cáp Điện IEC 60228 / IEC 60502 / TCVN 5935", "url": "https://cadivi.vn/", "desc": "Quy chuẩn ruột dẫn đồng/nhôm, cách điện PVC/XLPE/LSZH và kiểm nghiệm cáp điện"},
        "books": ["Electric Cables Handbook (BICC / G.F. Moore)", "Wire and Cable Extrusion Technology (Maillefer Technical Guide)"],
        "keywords": ["wire drawing rod breakdown copper break analysis", "cable extrusion eccentricity laser gauge oee", "xlpe silane vs ccv crosslinking process"],
        "questions": [
            {"question": "Chuỗi công nghệ kéo–ủ–bện–đùn–thử nghiệm cáp điện gồm những công đoạn và nhóm máy nào trọng yếu?", "type": "Khái Niệm Cốt Lõi", "key_points": "RBD kéo thô → Kéo trung/tinh → Ủ mềm → Bện Buncher/Strander → Đùn bọc PVC/XLPE + Spark Test → Lưu hóa → Ghép lõi & Giáp băng thép DSTA → Bọc vỏ → Lab QA/QC & Đóng cuộn."}
        ]
    },
    "six_sigma": {
        "display": "Operational Excellence (OE), Lean Six Sigma (DMAIC), TOC, TPM & PFMEA",
        "category": "Sản Xuất (Manufacturing)",
        "doc_key": "oe_six_sigma_dmaic",
        "aliases": ["oe", "operational excellence", "tối ưu quy trình", "six sigma", "dmaic", "tpm", "pfmea", "toc", "cải tiến liên tục"],
        "docs": {"name": "ASQ Six Sigma & Operational Excellence Body of Knowledge", "url": "https://asq.org/quality-resources/six-sigma", "desc": "Chuẩn mực quốc tế về DMAIC, kiểm định thống kê Before-After, TPM và PFMEA"},
        "books": ["The Goal: A Process of Ongoing Improvement (Eliyahu M. Goldratt)", "The Six Sigma Handbook (Thomas Pyzdek & Paul Keller)"],
        "keywords": ["lean six sigma dmaic manufacturing case study", "theory of constraints drum buffer rope factory", "pfmea aiag vda action priority extrusion"],
        "questions": [
            {"question": "Phân biệt OE, Lean, Six Sigma và IE; cách dùng 2-Sample t-test để chứng minh dự án cải tiến Trước–Sau có ý nghĩa thống kê?", "type": "Phân Tích Sâu", "key_points": "IE đo chuẩn, Lean tăng tốc độ dòng chảy/xóa lãng phí, Six Sigma giảm biến thiên/lỗi, OE là hệ quản trị tổng thể; dùng p-value < 0.05 để chứng minh khác biệt thật."}
        ]
    },
    "capacity_cost": {
        "display": "Hoạch Định Năng Lực (RCCP), Giá Thành & Tối Ưu Hao Phí Cáp Điện",
        "category": "Sản Xuất (Manufacturing)",
        "doc_key": "cable_cost_capacity",
        "aliases": ["năng lực", "chi phí", "hao phí công nghệ", "hao phí lao động", "điều độ", "rccp", "capacity", "cut-length"],
        "docs": {"name": "Manufacturing Capacity Planning (RCCP) & Cost Accounting Guide", "url": "https://www.apics.org/", "desc": "Hoạch định năng lực theo tấn/km, tối ưu Copper Give-away, Over-thickness và Cut-Length"},
        "books": ["Factory Physics (Wallace J. Hopp & Mark L. Spearman)", "Cost Accounting: A Managerial Emphasis (Horngren)"],
        "keywords": ["rough cut capacity planning rccp excel manufacturing", "copper giveaway cable extrusion over thickness savings", "cutting stock problem cable reel length optimization"],
        "questions": [
            {"question": "Copper Give-away và Compound Over-thickness là gì? Cách tính RCCP khi nhận đơn hàng cáp lực tăng đột biến?", "type": "Tình Huống Thực Chiến", "key_points": "Quy đổi tấn/km sang giờ máy theo OEE thực tế lịch sử từng công đoạn; thu hẹp sai số SPC để tiết kiệm hàng tỷ đồng đồng/nhựa."}
        ]
    },
    "planning_ehs_cost": {
        "display": "Kế Hoạch S&OP/MPS/MRP/CRP, Chất Lượng FPY/RTY, An Toàn LOTO/ISO & Giá Thành Định Mức",
        "category": "Sản Xuất (Manufacturing)",
        "doc_key": "planning_quality_ehs_cost",
        "aliases": ["s&op", "mps", "mrp", "crp", "rty", "fpy", "loto", "ehs", "iso 9001", "iso 14001", "iso 45001", "iso 50001", "standard cost", "hoshin kanri", "adkar", "acsr", "mica", "7 qc"],
        "docs": {"name": "ISO 9001/14001/45001/50001 & APICS S&OP / MRP / Standard Costing Standards", "url": "https://www.iso.org/standards.html", "desc": "Chuẩn hệ thống quản lý chất lượng, môi trường, an toàn LOTO, năng lượng ISO 50001 và hoạch định S&OP–MRP–CRP"},
        "books": ["Manufacturing Planning and Control for Supply Chain Management (Jacobs et al.)", "Hoshin Kanri for the Lean Enterprise (Thomas L. Jackson)"],
        "keywords": ["sop mps mrp crp manufacturing planning hierarchy", "rolled throughput yield rty vs first pass yield fpy", "loto lockout tagout 6 steps iso 50001 energy management"],
        "questions": [
            {"question": "Phân biệt FPY và RTY trong dây chuyền cáp điện 6 công đoạn, và vai trò của quy trình LOTO 6 bước khi làm SMED?", "type": "Phân Tích Sâu", "key_points": "RTY = tích các FPY từng công đoạn để phơi bày Hidden Factory; LOTO cô lập nguồn năng lượng và thử Zero Energy trước khi can thiệp khuôn/lưới lọc."}
        ]
    },
    "extrusion_forensics": {
        "display": "Công Nghệ Đùn Cáp Chuyên Sâu (L/D, DDR, Melt Pressure), Đứt Sợi Đồng & Cáp Đặc Chủng (Solar / Braiding)",
        "category": "Sản Xuất (Manufacturing)",
        "doc_key": "cable_extrusion_wire_forensics",
        "aliases": ["l/d", "ddr", "melt pressure", "sharkskin", "die drool", "regrind", "cup-and-cone", "solar", "h1z2z2", "braiding", "qcvn 4", "astm b49"],
        "docs": {"name": "Cable Extrusion Engineering, Wire Break Forensics & QCVN 4 / EN 50618", "url": "https://cadivi.vn/", "desc": "Thiết kế trục vít L/D, DDR/DRB, khuyết tật bề mặt đùn, phân tích mặt gãy đứt sợi đồng & cáp Solar/chống nhiễu"},
        "books": ["Extrusion: The Definitive Processing Guide and Handbook (Harold F. Giles)"],
        "keywords": ["cable extrusion ddr drb tooling calculation", "copper wire break forensics cup and cone inclusion", "en 50618 h1z2z2-k solar cable e-beam"],
        "questions": [
            {"question": "Cách phân biệt đứt sợi Cup-and-Cone vs Inclusion khi kéo đồng và ý nghĩa của DDR/Melt Pressure khi đùn bọc cáp?", "type": "Phân Tích Sâu", "key_points": "Cup-and-Cone là lỗi kéo/khuôn/nhũ tương nội bộ; Inclusion là tạp chất đồng Rod ASTM B49; DDR chọn đúng bộ Chày-Cối tránh nứt vỏ/dư nhựa."}
        ]
    },
    "oe_field_test": {
        "display": "Thực Địa OE (Work Sampling, Loss Tree WCM, LSW/LPA, Bảo Trì PdM) & Đề Thi Thực Hành Vòng 2",
        "category": "Sản Xuất (Manufacturing)",
        "doc_key": "oe_field_execution_case_test",
        "aliases": ["work sampling", "cost deployment", "wcm", "loss tree", "lsw", "lpa", "wrench time", "pm compliance", "cbm", "pdm", "moc", "ecn", "headcount"],
        "docs": {"name": "WCM Cost Deployment, Leader Standard Work (LSW/LPA) & OE Case Study Playbook", "url": "https://www.lean.org/", "desc": "Đo năng suất bằng Work Sampling, cây tổn thất tiền WCM, duy trì LSW/LPA, bảo trì PdM và bộ đề thi thực hành OE Vòng 2"},
        "books": ["Creating a Lean Culture (David Mann)", "Work Systems and the Methods, Measurement, and Management of Work (Mikell P. Groover)"],
        "keywords": ["work sampling tippett formula manufacturing example", "wcm cost deployment loss tree matrix", "leader standard work lsw layered process audit lpa"],
        "questions": [
            {"question": "Khi nào dùng Work Sampling thay cho Time Study, và thiết kế LSW/LPA/Escalation Matrix thế nào để duy trì cải tiến OE bền vững?", "type": "Tình Huống Thực Chiến", "key_points": "Work Sampling đo công việc chu kỳ dài (đa máy, xe nâng, bảo trì); LSW + LPA 3 cấp + Escalation SLA 5-15-30p khóa chuẩn không tái diễn."}
        ]
    }
}


class JobAnalyzer:
    """Bộ máy phân tích JD hỗ trợ cả Offline Mode và Gemini AI Mode."""

    def __init__(self, api_key=""):
        self.api_key = api_key.strip() if api_key else os.environ.get("GEMINI_API_KEY", "").strip()

    def set_api_key(self, api_key):
        self.api_key = api_key.strip()

    def analyze(self, raw_jd, force_offline=False):
        """
        Phân tích JD chính:
        - Nếu có api_key và không ép buộc offline: thử gọi Gemini AI.
        - Nếu không có key hoặc AI lỗi: chuyển sang bộ máy Offline Thông Minh.
        """
        if not raw_jd or not raw_jd.strip():
            raise ValueError("Nội dung JD không được để trống!")

        if self.api_key and not force_offline:
            try:
                result = self._analyze_with_gemini(raw_jd)
                result["analysis_engine"] = "Gemini AI"
                return result
            except Exception as e:
                # Log lỗi và fallback sang offline
                print(f"⚠️ Gọi Gemini AI gặp lỗi ({e}), chuyển sang chế độ Offline Smart Analyzer.")

        # Fallback offline
        result = self._analyze_offline(raw_jd)
        result["analysis_engine"] = "Offline Smart Rule-based Engine"
        return result

    def _analyze_offline(self, raw_jd):
        """Phân tích bằng thuật toán từ điển quy tắc (100% Offline)."""
        text = raw_jd.strip()
        lines = [line.strip() for line in text.split("\n") if line.strip()]

        # 1. Đoán Tiêu Đề (Title) & Công Ty (Company)
        title = self._detect_title(lines, text)
        company = self._detect_company(lines, text)
        level = self._detect_level(text)
        category = self._detect_category(text, title)

        # 2. Bóc tách kỹ năng xuất hiện
        detected_techs = []
        lower_text = text.lower()
        for key, info in TECH_CATALOG.items():
            matched = False
            pattern = r'\b' + re.escape(key) + r'\b'
            if re.search(pattern, lower_text):
                matched = True
            else:
                for alias in info.get("aliases", []):
                    alias_pat = r'(?<!\w)' + re.escape(alias.lower()) + r'(?!\w)'
                    if re.search(alias_pat, lower_text):
                        matched = True
                        break
            if matched:
                detected_techs.append(key)

        # Nếu không bắt được tech nào cụ thể, fallback tech mặc định dựa trên category
        if not detected_techs:
            if category == "Sản Xuất (Manufacturing)":
                detected_techs = ["lean", "oee", "ole", "smed", "bom", "six_sigma"]
            elif category == "Frontend":
                detected_techs = ["javascript", "react", "git"]
            elif category == "DevOps":
                detected_techs = ["docker", "kubernetes", "git"]
            else:
                detected_techs = ["python", "sql", "git"]

        is_mfg = any(t in ["lean", "oee", "ole", "smed", "bom", "cable_mfg", "six_sigma", "capacity_cost", "planning_ehs_cost", "extrusion_forensics", "oe_field_test"] for t in detected_techs) or any(k in category for k in ["Sản Xuất", "Manufacturing", "Lean"])

        # Bổ sung đầy đủ tri thức OE/Cáp nếu phát hiện JD sản xuất
        if is_mfg:
            for mfg_core in ["oee", "ole", "lean", "smed", "bom", "six_sigma", "capacity_cost", "planning_ehs_cost", "oe_field_test"]:
                if mfg_core not in detected_techs:
                    detected_techs.append(mfg_core)
            if any(k in lower_text for k in ["cadivi", "dây cáp", "cáp điện", "kéo sợi", "đùn", "xlpe"]):
                if "cable_mfg" not in detected_techs:
                    detected_techs.insert(0, "cable_mfg")
                if "extrusion_forensics" not in detected_techs:
                    detected_techs.insert(1, "extrusion_forensics")

        # 3. Phân bổ ma trận kỹ năng
        must_have = []
        nice_to_have = []
        if is_mfg:
            tools = [
                "Excel nâng cao (Power Query, Pivot Table, VBA Macro)",
                "Microsoft Power BI (Dashboard OEE/OLE thời gian thực)",
                "Minitab (Thống kê chất lượng SPC, Cp/Cpk, t-test, ANOVA)",
                "AutoCAD / MS Visio (Layout xưởng & Sơ đồ Spaghetti)",
                "Hệ thống ERP (SAP PP) & MES / SCADA sản xuất",
                "Python (Pandas / OpenPyXL tự động hóa báo cáo sản xuất)"
            ]
            soft_skills = [
                "Kỹ năng bám sát hiện trường (Genba Walk & Floor Communication)",
                "Quản trị thay đổi & Thuyết phục Quản đốc/Công nhân (Change Management)",
                "Tư duy phân tích gốc rễ vấn đề (5 Whys, Ishikawa, A3, 8D Report)",
                "Kỹ năng lập báo cáo định hướng sản xuất, BOM & ROI cho Ban Giám Đốc",
                "Tiếng Anh đọc hiểu tài liệu kỹ thuật & tiêu chuẩn TCVN / IEC"
            ]
        else:
            tools = ["Git", "Docker", "VS Code / IDE", "Postman", "Linux Command Line"]
            soft_skills = ["Giao tiếp & Làm việc nhóm (Teamwork)", "Tư duy giải quyết vấn đề (Problem Solving)", "Quy trình Agile/Scrum", "Đọc hiểu tài liệu tiếng Anh"]

        for idx, t in enumerate(detected_techs):
            disp = TECH_CATALOG[t]["display"]
            if idx < (5 if is_mfg else 3):
                must_have.append(disp)
            else:
                nice_to_have.append(disp)

        # 4. Tạo Lộ trình Onboarding 3 chặng dựa trên level & tech
        roadmap = self._generate_roadmap(level, detected_techs)

        # 5. Tuyển chọn tài liệu & từ khóa
        docs_list = []
        books_list = []
        keywords_list = []
        questions_list = []

        seen_docs = set()
        seen_books = set()

        for t in detected_techs:
            info = TECH_CATALOG[t]
            d = dict(info["docs"])
            d["doc_key"] = info.get("doc_key", "")
            if d["name"] not in seen_docs:
                docs_list.append(d)
                seen_docs.add(d["name"])

            for b in info.get("books", []):
                if b not in seen_books:
                    books_list.append(b)
                    seen_books.add(b)

            keywords_list.extend(info.get("keywords", []))
            questions_list.extend(info.get("questions", []))

        # Đảm bảo sách kinh điển chung phù hợp ngành
        if not is_mfg:
            if "Designing Data-Intensive Applications (Martin Kleppmann)" not in seen_books:
                books_list.append("Designing Data-Intensive Applications (Martin Kleppmann)")
            if "Clean Code: A Handbook of Agile Software Craftsmanship (Robert C. Martin)" not in seen_books:
                books_list.append("Clean Code (Robert C. Martin)")

        # Phân bổ hệ sinh thái phần mềm hỗ trợ chuyên dụng
        if is_mfg:
            softwares = [
                {"name": "Microsoft Excel Nâng Cao (Power Query, VBA)", "role": "Xử lý dữ liệu thô nhiều ca, vẽ biểu đồ Pareto 80/20, tự động hóa Macro VBA", "url": "https://support.microsoft.com/excel", "doc_key": "excel_mfg"},
                {"name": "Microsoft Power BI", "role": "Xây dựng Dashboard OEE/OLE thời gian thực, trực quan hóa xu hướng", "url": "https://powerbi.microsoft.com/", "doc_key": "powerbi_mfg"},
                {"name": "Minitab", "role": "Kiểm soát quá trình thống kê SPC (Xbar-R), phân tích năng lực quá trình Cpk & t-test", "url": "https://www.minitab.com/", "doc_key": "minitab_spc"},
                {"name": "AutoCAD / MS Visio", "role": "Thiết kế Layout xưởng, vẽ sơ đồ Spaghetti, sơ đồ chuỗi giá trị VSM", "url": "https://www.autodesk.com/", "doc_key": "autocad_layout"},
                {"name": "Hệ thống SAP ERP (PP) & MES", "role": "Quản lý định mức vật tư BOM, lệnh sản xuất và thu thập dữ liệu máy PLC/SCADA", "url": "https://help.sap.com/", "doc_key": "erp_mes"}
            ]
        else:
            softwares = [
                {"name": "Visual Studio Code / JetBrains IDE", "role": "Môi trường lập trình, gỡ lỗi và quản lý mã nguồn", "url": "https://code.visualstudio.com/", "doc_key": "python_core" if "python" in detected_techs else "react_fe"},
                {"name": "Git & GitHub / GitLab", "role": "Quản lý phiên bản mã nguồn, Pull Request và CI/CD", "url": "https://github.com/", "doc_key": "git_vcs"},
                {"name": "Docker & Docker Compose", "role": "Đóng gói container môi trường phát triển độc lập", "url": "https://www.docker.com/", "doc_key": "docker_devops"},
                {"name": "PostgreSQL / DBeaver", "role": "Quản trị cơ sở dữ liệu quan hệ và tối ưu truy vấn SQL", "url": "https://dbeaver.io/", "doc_key": "sql_db"},
                {"name": "Redis Insight", "role": "Giám sát bộ nhớ cache và tối ưu hóa hiệu năng in-memory", "url": "https://redis.io/insight/", "doc_key": "redis_cache"}
            ]

        # Tuyển chọn cẩm nang offline có sẵn tương ứng
        offline_guides = []
        seen_guides = set()
        for t in detected_techs:
            dk = TECH_CATALOG[t].get("doc_key")
            if dk and dk not in seen_guides and offline_knowledge and dk in offline_knowledge.OFFLINE_DOCS:
                seen_guides.add(dk)
                offline_guides.append({
                    "id": dk,
                    "title": offline_knowledge.OFFLINE_DOCS[dk]["title"],
                    "category": offline_knowledge.OFFLINE_DOCS[dk]["category"],
                    "summary": offline_knowledge.OFFLINE_DOCS[dk]["summary"]
                })
        for s in softwares:
            dk = s.get("doc_key")
            if dk and dk not in seen_guides and offline_knowledge and dk in offline_knowledge.OFFLINE_DOCS:
                seen_guides.add(dk)
                offline_guides.append({
                    "id": dk,
                    "title": offline_knowledge.OFFLINE_DOCS[dk]["title"],
                    "category": offline_knowledge.OFFLINE_DOCS[dk]["category"],
                    "summary": offline_knowledge.OFFLINE_DOCS[dk]["summary"]
                })

        # 6. Đóng gói kết quả theo chuẩn 5 Tầng Kiến Thức
        if is_mfg and interview_bank:
            final_interview = interview_bank.get_all_questions()
        else:
            final_interview = questions_list if questions_list else [
                {"question": "Bạn có thể chia sẻ một dự án kỹ thuật tiêu biểu mà bạn đã chủ trì hoặc tham gia?", "type": "Tình Huống Thực Chiến", "key_points": "• Nêu rõ bối cảnh (S), Nhiệm vụ (T), Hành động kỹ thuật (A), và Kết quả đo lường được (R).\n• Nhấn mạnh kỹ năng giải quyết vấn đề và làm việc nhóm."}
            ]

        overview_summary = (
            f"Vị trí {title} cấp bậc {level} thuộc lĩnh vực {category}, chuyên trách giám sát, phân tích dữ liệu năng lực/năng suất (OEE, OLE), kiểm soát định mức BOM/hao phí và triển khai các dự án cải tiến Lean / Six Sigma / SMED tại nhà máy."
            if is_mfg else
            f"Vị trí {title} cấp bậc {level} thuộc lĩnh vực {category}, tập trung vào xây dựng và phát triển hệ thống với các công nghệ chủ đạo: {', '.join([TECH_CATALOG[t]['display'] for t in detected_techs[:3]])}."
        )
        overview_mission = (
            "Tối ưu hóa quy trình sản xuất, nhận diện điểm nghẽn, triệt tiêu lãng phí, giảm hao phí vật tư/lao động và chứng minh hiệu quả cải tiến Trước–Sau bằng số liệu định lượng (ROI)."
            if is_mfg else
            "Làm chủ quy trình phát triển, bàn giao tính năng chất lượng cao đúng hạn và tối ưu hóa hệ thống ổn định."
        )

        analysis = {
            "title": title,
            "company": company,
            "level": level,
            "category": category,
            "overview": {
                "summary": overview_summary,
                "mission": overview_mission,
                "work_mode": "On-site 100% tại Nhà máy / Xưởng sản xuất (Bám sát hiện trường Genba)" if is_mfg else self._detect_work_mode(text)
            },
            "skills_matrix": {
                "must_have": must_have,
                "nice_to_have": nice_to_have,
                "tools": tools,
                "soft_skills": soft_skills
            },
            "roadmap": roadmap,
            "resources": {
                "offline_guides": offline_guides,
                "softwares": softwares,
                "official_docs": docs_list,
                "books": books_list[:8],
                "search_keywords": keywords_list[:10]
            },
            "interview_prep": final_interview,
            "tags": [level, category] + [TECH_CATALOG[t]["display"] for t in detected_techs[:4]]
        }

        return {
            "title": title,
            "company": company,
            "level": level,
            "category": category,
            "location": self._detect_location(text),
            "salary_range": self._detect_salary(text),
            "raw_jd": raw_jd,
            "analysis": analysis,
            "tags": analysis["tags"],
            "status": "New"
        }

    def _generate_roadmap(self, level, detected_techs):
        """Sinh lộ trình học tập 3 chặng tùy biến theo cấp bậc và lĩnh vực."""
        is_manufacturing = any(t in ["lean", "oee", "ole", "smed", "bom"] for t in detected_techs)
        if is_manufacturing:
            return [
                {
                    "phase": "Tuần 1 - 2: Khảo Sát Hiện Trường (Genba), Hiểu Quy Trình & Chuẩn Hóa Dữ Liệu",
                    "goals": [
                        "Đi bộ hiện trường (Genba Walk), nắm trọn dòng chảy sản xuất từ NVL đến thành phẩm.",
                        "Đọc hiểu cấu trúc bảng định mức BOM của các mã sản phẩm chủ lực và cấu trúc chi phí.",
                        "Khảo sát hiện trạng ghi chép ca, biểu mẫu đo lường dừng máy (Downtime) và phế phẩm."
                    ],
                    "action_items": [
                        "Vẽ lại sơ đồ di chuyển thực tế (Spaghetti Diagram) của công nhân và vật tư trên chuyền.",
                        "Thu thập dữ liệu ca sản xuất 1 tháng gần nhất để đánh giá độ chính xác của số liệu hiện có.",
                        "Làm quen và tạo quan hệ tin cậy với Quản đốc xưởng, Tổ trưởng và Kỹ sư bảo trì."
                    ]
                },
                {
                    "phase": "Tháng 1: Chuẩn Hóa Đo Lường OEE/OLE & Nhận Diện Điểm Nghẽn (Bottlenecks)",
                    "goals": [
                        "Xây dựng và chuẩn hóa công thức đo lường OEE/OLE hàng ngày theo chuẩn quốc tế.",
                        "Phân loại chính xác 6 tổn thất lớn (Six Big Losses) và xác định top 3 điểm nghẽn.",
                        "Phân tích chi tiết thời gian chuyển đổi dòng hàng (Changeover time)."
                    ],
                    "action_items": [
                        "Thiết lập bảng theo dõi OEE/OLE thử nghiệm trên 1 chuyền hoặc cụm máy mẫu (Pilot Line).",
                        "Quay video quy trình chuyển đổi khuôn/mẫu mã và áp dụng bước 1-2 của kỹ thuật SMED.",
                        "Tổ chức buổi họp Kaizen đầu tiên với tổ sản xuất để xử lý 1 loại lỗi dừng vặt phổ biến.",
                        "Thiết lập báo cáo phân tích chênh lệch hao phí vật tư so với định mức BOM."
                    ]
                },
                {
                    "phase": "Tháng 2 - 3: Triển Khai Cải Tiến Sâu, Cân Bằng Chuyền & Đo Lường ROI Trước - Sau",
                    "goals": [
                        "Rút ngắn thời gian chuyển đổi dòng hàng ít nhất 20-30% bằng phương pháp SMED.",
                        "Cân bằng chuyền sản xuất (Line Balancing / Takt Time) nhằm triệt tiêu thời gian chờ đợi.",
                        "Xây dựng Dashboard báo cáo tự động cho Ban Giám Đốc và chứng minh hiệu quả Before-After."
                    ],
                    "action_items": [
                        "Áp dụng cữ gá nhanh, chuẩn hóa dụng cụ chuyển đổi để đưa thời gian dừng máy về mức tối thiểu.",
                        "Cân đối Takt Time và Cycle Time trên chuyền sản xuất mẫu bằng biểu đồ Yamazumi.",
                        "Thiết kế Dashboard theo dõi OEE, OLE và hao phí BOM tự động bằng Power BI / Excel.",
                        "Tổng hợp báo cáo đánh giá hiệu quả kinh tế (ROI) của các giải pháp cải tiến đã triển khai.",
                        "Chuẩn hóa quy trình thành tài liệu SOP và tổ chức đào tạo duy trì cho công nhân."
                    ]
                }
            ]

        tech_names = ", ".join([TECH_CATALOG[t]["display"] for t in detected_techs[:3]])

        if level in ["Intern", "Fresher"]:
            return [
                {
                    "phase": "Tuần 1 - 2: Nền Tảng Cú Pháp & Setup Dự Án",
                    "goals": [
                        f"Cài đặt hoàn chỉnh môi trường phát triển (Python/Node/Git/Docker).",
                        f"Nắm vững cú pháp cơ bản và chuẩn mực viết code (PEP8/Linter) của {tech_names}.",
                        "Hiểu cấu trúc thư mục dự án và chạy thử thành công trên máy local."
                    ],
                    "action_items": [
                        "Đọc lướt qua Official Documentation phần Getting Started.",
                        "Clone repository, cài đặt dependencies và chạy thử test suite.",
                        "Tạo một pull request đầu tiên: sửa 1 typo tài liệu hoặc giải quyết 1 bug nhỏ."
                    ]
                },
                {
                    "phase": "Tháng 1: Bàn Giao Tính Năng Nghiệp Vụ Cơ Bản",
                    "goals": [
                        "Tự tin nhận và xử lý các User Story nhỏ không cần cầm tay chỉ việc.",
                        "Viết unit test cho các hàm logic chính đạt coverage > 70%.",
                        "Làm quen với quy trình Git branch, Pull Request review và CI/CD tự động."
                    ],
                    "action_items": [
                        "Thực hiện 2-3 task CRUD API hoặc component giao diện thực tế.",
                        "Tham gia buổi họp Daily Scrum và báo cáo tiến độ mạch lạc.",
                        "Ghi chú lại các lỗi hay gặp vào sổ tay kỹ thuật cá nhân."
                    ]
                },
                {
                    "phase": "Tháng 2 - 3: Làm Chủ Quy Trình & Xử Lý Tác Vụ Độc Lập",
                    "goals": [
                        "Xử lý độc lập các module phức tạp hơn, hiểu cách query CSDL tối ưu.",
                        "Hiểu luồng deploy staging và các bước kiểm tra trước khi release.",
                        "Tự tin thảo luận giải pháp kỹ thuật với đồng nghiệp."
                    ],
                    "action_items": [
                        "Tìm hiểu cách viết query không bị N+1 và tối ưu index.",
                        "Tự deploy một tính năng hoàn chỉnh lên môi trường Staging/Test.",
                        "Đọc sách Clean Code và áp dụng refactoring vào code của mình."
                    ]
                }
            ]
        elif level in ["Senior", "Lead"]:
            return [
                {
                    "phase": "Tuần 1 - 2: Thấu Suốt Kiến Trúc & Điểm Nghẽn Hệ Thống",
                    "goals": [
                        "Nắm toàn diện sơ đồ kiến trúc tổng thể (System Architecture, DB ERD, Network topology).",
                        "Xác định các rủi ro kỹ thuật, technical debt và điểm nghẽn hiệu năng hiện tại.",
                        "Xây dựng mối quan hệ tin cậy với Tech Lead và các bên liên quan (Product/QA)."
                    ],
                    "action_items": [
                        "Rà soát sơ đồ luồng dữ liệu (Data Pipeline) và các dịch vụ bên thứ ba.",
                        "Đánh giá cấu hình Production, logging, tracing (APM) và alert triggers.",
                        "Đóng góp ý kiến cải tiến coding standard hoặc tooling trong sprint đầu tiên."
                    ]
                },
                {
                    "phase": "Tháng 1: Dẫn Dắt Thiết Kế & Chuẩn Hóa Quy Trình",
                    "goals": [
                        "Thiết kế kiến trúc cho các tính năng trọng điểm (High Throughput / Low Latency).",
                        "Nâng cao chuẩn mực Code Review cho toàn team, giảm thiểu bug lọt lên Production.",
                        "Tối ưu hóa pipeline CI/CD giúp giảm thời gian build và deploy."
                    ],
                    "action_items": [
                        "Viết Technical Design Document (TDD) cho một bài toán phức tạp.",
                        "Thực hiện refactor một module nghẽn hiệu năng hoặc tối ưu query CSDL lớn.",
                        "Mentor và hỗ trợ giải quyết khó khăn kỹ thuật cho các thành viên Junior/Mid."
                    ]
                },
                {
                    "phase": "Tháng 2 - 3: Kiến Trúc Mở Rộng & Văn Hóa Kỹ Thuật",
                    "goals": [
                        "Đảm bảo hệ thống đạt độ sẵn sàng cao (High Availability, Failover, Disaster Recovery).",
                        "Xây dựng chiến lược phân vùng dữ liệu, caching đa tầng và giám sát chủ động.",
                        "Đóng vai trò trụ cột kỹ thuật, đại diện team trong các buổi họp kiến trúc lớn."
                    ],
                    "action_items": [
                        "Thiết lập bài test chịu tải (Load Testing / Stress Testing) cho hệ thống.",
                        "Xây dựng cẩm nang ứng phó sự cố (Runbook / Incident Response Guide).",
                        "Chủ trì các buổi chia sẻ kiến thức chuyên sâu (Tech Talk) định kỳ."
                    ]
                }
            ]
        else: # Mid-level default
            return [
                {
                    "phase": "Tuần 1 - 2: Làm Quen Mã Nguồn & Thiết Lập Môi Trường",
                    "goals": [
                        f"Làm chủ luồng chạy local của toàn bộ service liên quan đến {tech_names}.",
                        "Hiểu rõ luồng nghiệp vụ kinh doanh (Business Logic) và các quy ước mã nguồn.",
                        "Hoàn thành các task onboarding đầu tiên và bàn giao đúng chuẩn."
                    ],
                    "action_items": [
                        "Đọc hiểu ERD Database và tài liệu Swagger/Postman API.",
                        "Tham gia review mã nguồn của đồng nghiệp để nắm bắt phong cách của team.",
                        "Chạy kiểm thử regression test và xác nhận không có lỗi môi trường."
                    ]
                },
                {
                    "phase": "Tháng 1: Độc Lập Phát Triển Tính Năng & Tối Ưu Hóa",
                    "goals": [
                        "Chủ động nhận trách nhiệm cho các module tính năng quan trọng.",
                        "Viết unit test và integration test toàn diện cho mã mới.",
                        "Phát hiện và xử lý sớm các lỗi bảo mật hoặc query database chưa tối ưu."
                    ],
                    "action_items": [
                        "Hoàn thành xuất sắc 1 tính năng lớn từ khâu thiết kế API đến khi deploy.",
                        "Áp dụng các design pattern phù hợp (Repository, Service layer, Dependency Injection).",
                        "Tối ưu hóa các câu truy vấn chậm bằng EXPLAIN ANALYZE."
                    ]
                },
                {
                    "phase": "Tháng 2 - 3: Tự Chủ Hệ Thống & Nâng Cao Chất Lượng",
                    "goals": [
                        "Sẵn sàng tham gia trực phát hành (Release Deployment) và ứng cứu sự cố production.",
                        "Đề xuất cải tiến hiệu năng hoặc công cụ tự động hóa công việc.",
                        "Trở thành đầu mối kỹ thuật tin cậy của phân hệ mình phụ trách."
                    ],
                    "action_items": [
                        "Xây dựng dashboard giám sát metric cho các endpoint quan trọng.",
                        "Nâng cao kiến thức về Caching (Redis) và Message Queue (Kafka/RabbitMQ).",
                        "Đọc sách Designing Data-Intensive Applications để nâng cao tư duy hệ thống."
                    ]
                }
            ]

    def _detect_title(self, lines, text):
        """Phát hiện chức danh công việc."""
        for line in lines[:8]:
            m = re.search(r'(?:vị trí|job title|tuyển dụng|chức danh|role|position)[:\s-]+(.*)', line, re.IGNORECASE)
            if m and len(m.group(1).strip()) > 3:
                return m.group(1).strip()

        # Kiểm tra dòng đầu tiên nếu ngắn
        if lines and len(lines[0]) < 60:
            return lines[0].replace("#", "").strip()

        return "Kỹ Sư Phần Mềm (Software Engineer)"

    def _detect_company(self, lines, text):
        """Phát hiện tên công ty tuyển dụng."""
        for line in lines[:10]:
            m = re.search(r'(?:công ty|company|tập đoàn|doanh nghiệp)[:\s-]+(.*)', line, re.IGNORECASE)
            if m and len(m.group(1).strip()) > 2:
                return m.group(1).strip()
        return "Công ty tuyển dụng"

    def _detect_level(self, text):
        """Phát hiện cấp bậc yêu cầu."""
        lt = text.lower()
        if any(k in lt for k in ["lead", "architect", "trưởng nhóm", "chủ trì", "principal"]):
            return "Lead"
        if any(k in lt for k in ["senior", "chuyên viên cao cấp", "5 năm", "5+ năm", "4-6 năm"]):
            return "Senior"
        if any(k in lt for k in ["intern", "thực tập", "thực tập sinh"]):
            return "Intern"
        if any(k in lt for k in ["fresher", "mới tốt nghiệp", "dưới 1 năm", "chưa có kinh nghiệm"]):
            return "Fresher"
        if any(k in lt for k in ["junior", "1-2 năm", "1 năm kinh nghiệm", "2 năm"]):
            return "Junior"
        return "Mid"

    def _detect_category(self, text, title=""):
        """Phát hiện lĩnh vực chuyên môn (Ưu tiên tiêu đề trước, sau đó tính trọng số từ khóa trong JD)."""
        title_lower = title.lower()

        # 1. Kiểm tra trực tiếp trong tiêu đề
        if any(k in title_lower for k in ["sản xuất", "manufacturing", "lean", "cải tiến", "tối ưu quy trình", "oe", "ie", "industrial", "oee", "ole", "nhà máy", "bảo trì", "cadivi", "dây cáp"]):
            return "Sản Xuất (Manufacturing)"
        if any(k in title_lower for k in ["backend", "back-end", "python", "java", "golang", "c#", ".net", "php", "django", "fastapi", "spring", "nodejs"]):
            return "Backend"
        if any(k in title_lower for k in ["frontend", "front-end", "react", "vue", "angular", "ui/ux", "web"]):
            return "Frontend"
        if any(k in title_lower for k in ["fullstack", "full-stack", "full stack"]):
            return "Fullstack"
        if any(k in title_lower for k in ["devops", "cloud", "sre", "infrastructure", "sysadmin", "aws"]):
            return "DevOps"
        if any(k in title_lower for k in ["data engineer", "data science", "ai", "machine learning", "nlp", "llm"]):
            return "AI/Data"
        if any(k in title_lower for k in ["mobile", "android", "ios", "flutter", "react native"]):
            return "Mobile"
        if any(k in title_lower for k in ["tester", "qc", "qa", "automation test", "kiểm thử"]):
            return "QA"

        # 2. Tính trọng số trong toàn bộ văn bản JD
        lt = text.lower()
        scores = {
            "Sản Xuất (Manufacturing)": sum(lt.count(k) for k in ["sản xuất", "manufacturing", "lean", "oee", "ole", "nhà máy", "hao phí", "bom", "smed", "kaizen", "năng suất", "tối ưu quy trình", "cadivi", "dây cáp", "điều độ", "six sigma"]),
            "Backend": sum(lt.count(k) for k in ["backend", "back-end", "api", "database", "sql", "postgresql", "mysql", "orm", "fastapi", "django", "spring"]),
            "Frontend": sum(lt.count(k) for k in ["frontend", "front-end", "react", "vue", "angular", "css", "html", "javascript", "typescript", "ui/ux"]),
            "DevOps": sum(lt.count(k) for k in ["devops", "sre", "ci/cd", "kubernetes", "k8s", "terraform", "infrastructure", "sysadmin"]),
            "Fullstack": sum(lt.count(k) for k in ["fullstack", "full-stack", "full stack"]),
            "AI/Data": sum(lt.count(k) for k in ["machine learning", "deep learning", "nlp", "data pipeline", "etl", "spark", "llm"]),
            "Mobile": sum(lt.count(k) for k in ["mobile", "android", "ios", "flutter", "react native", "swift", "kotlin"]),
            "QA": sum(lt.count(k) for k in ["testing", "tester", "qa", "qc", "selenium", "cypress", "automation test"])
        }
        best_cat = max(scores, key=scores.get)
        if scores[best_cat] > 0:
            return best_cat
        return "Backend"

    def _detect_work_mode(self, text):
        lt = text.lower()
        if "remote" in lt or "từ xa" in lt:
            return "Remote (Làm việc từ xa)"
        if "hybrid" in lt or "linh hoạt" in lt:
            return "Hybrid (Linh hoạt kết hợp Onsite & Remote)"
        return "On-site (Văn phòng)"

    def _detect_location(self, text):
        lt = text.lower()
        if "hà nội" in lt or "ha noi" in lt:
            return "Hà Nội"
        if "hồ chí minh" in lt or "ho chi minh" in lt or "hcm" in lt or "sài gòn" in lt:
            return "TP. Hồ Chí Minh"
        if "đà nẵng" in lt or "da nang" in lt:
            return "Đà Nẵng"
        return "Việt Nam"

    def _detect_salary(self, text):
        for line in text.split("\n"):
            if any(k in line.lower() for k in ["lương", "salary", "thu nhập", "mức lương", "đãi ngộ"]):
                m = re.search(r'(?:lương|salary|mức lương|thu nhập)[:\s-]+(.*)', line, re.IGNORECASE)
                if m:
                    return m.group(1).strip()
                return line.strip()
        return "Thỏa thuận theo năng lực"

    def _analyze_with_gemini(self, raw_jd):
        """Gọi Gemini API qua REST endpoint chính thức."""
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"

        prompt = f"""
Bạn là Chuyên Gia Tuyển Dụng Kỹ Thuật và Kỹ Sư Trưởng Hệ Thống.
Hãy phân tích Bản mô tả công việc (JD) sau đây và trả về DUY NHẤT một chuỗi JSON hợp lệ (không kèm markdown ```json bọc ngoài, chỉ JSON thuần) theo đúng Mô Hình 5 Tầng Kiến Thức:

BẢN MÔ TẢ CÔNG VIỆC:
\"\"\"
{raw_jd}
\"\"\"

SCHEMA BẮT BUỘC:
{{
  "title": "Tiêu đề vị trí",
  "company": "Tên công ty",
  "level": "Intern | Fresher | Junior | Mid | Senior | Lead",
  "category": "Backend | Frontend | Fullstack | DevOps | AI/Data | Mobile | QA | Other",
  "location": "Địa điểm",
  "salary_range": "Mức lương",
  "overview": {{
    "summary": "Tóm tắt ngắn gọn vai trò",
    "mission": "Mục tiêu trọng tâm",
    "work_mode": "Onsite | Hybrid | Remote"
  }},
  "skills_matrix": {{
    "must_have": ["kỹ năng cốt lõi 1", "kỹ năng 2"],
    "nice_to_have": ["điểm cộng 1", "điểm cộng 2"],
    "tools": ["công cụ 1", "công cụ 2"],
    "soft_skills": ["kỹ năng mềm 1", "kỹ năng mềm 2"]
  }},
  "roadmap": [
    {{
      "phase": "Tuần 1 - 2: Nền Tảng & Setup",
      "goals": ["mục tiêu 1", "mục tiêu 2"],
      "action_items": ["việc 1", "việc 2"]
    }},
    {{
      "phase": "Tháng 1: Bàn Giao Tính Năng Nghiệp Vụ Cốt Lõi",
      "goals": ["mục tiêu 1"],
      "action_items": ["việc 1", "việc 2"]
    }},
    {{
      "phase": "Tháng 2 - 3: Chuyên Sâu & Tối Ưu Hóa",
      "goals": ["mục tiêu 1"],
      "action_items": ["việc 1", "việc 2"]
    }}
  ],
  "resources": {{
    "official_docs": [
      {{"name": "Tên tài liệu", "url": "URL", "desc": "Mô tả"}}
    ],
    "books": ["Sách 1", "Sách 2"],
    "search_keywords": ["keyword 1", "keyword 2"]
  }},
  "interview_prep": [
    {{
      "question": "Câu hỏi phỏng vấn?",
      "type": "Concept | Scenario | Deep Dive",
      "key_points": "Gợi ý trả lời"
    }}
  ],
  "tags": ["tag1", "tag2"]
}}
"""
        req_data = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": 0.2,
                "response_mime_type": "application/json"
            }
        }

        req = urllib.request.Request(
            url,
            data=json.dumps(req_data).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        with urllib.request.urlopen(req, timeout=30) as response:
            res_body = response.read().decode("utf-8")
            res_json = json.loads(res_body)
            candidate_text = res_json["candidates"][0]["content"]["parts"][0]["text"].strip()
            # Khử markdown fences nếu có
            if candidate_text.startswith("```"):
                candidate_text = re.sub(r"^```(?:json)?\s*", "", candidate_text)
                candidate_text = re.sub(r"\s*```$", "", candidate_text)

            parsed = json.loads(candidate_text)
            return {
                "title": parsed.get("title", "Kỹ sư phần mềm"),
                "company": parsed.get("company", "Công ty tuyển dụng"),
                "level": parsed.get("level", "Junior"),
                "category": parsed.get("category", "Backend"),
                "location": parsed.get("location", "Việt Nam"),
                "salary_range": parsed.get("salary_range", "Thỏa thuận"),
                "raw_jd": raw_jd,
                "analysis": parsed,
                "tags": parsed.get("tags", [parsed.get("level", "Junior"), parsed.get("category", "Backend")]),
                "status": "New"
            }
