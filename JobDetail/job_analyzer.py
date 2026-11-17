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
        "docs": {"name": "Pro Git Book", "url": "https://git-scm.com/book/en/v2", "desc": "Tài liệu chính thức toàn diện về hệ thống kiểm soát phiên bản Git"},
        "books": ["Pro Git (Scott Chacon and Ben Straub)"],
        "keywords": ["git rebase vs merge trade-offs", "git cherry-pick and bisect debugging", "git conflict resolution in detached head"],
        "questions": [
            {"question": "Khi nào nên dùng `git rebase` và khi nào nên dùng `git merge`? Quy tắc vàng của Rebase là gì?", "type": "Concept", "key_points": "Merge giữ nguyên lịch sử nhánh, an toàn cho branch dùng chung; Rebase tạo lịch sử tuyến tính sạch sẽ, TUYỆT ĐỐI không rebase các public/shared branch."}
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
            pattern = r'\b' + re.escape(key) + r'\b'
            if re.search(pattern, lower_text):
                detected_techs.append(key)

        # Nếu không bắt được tech nào cụ thể, fallback tech mặc định dựa trên category
        if not detected_techs:
            if category == "Frontend":
                detected_techs = ["javascript", "react", "git"]
            elif category == "DevOps":
                detected_techs = ["docker", "kubernetes", "git"]
            else:
                detected_techs = ["python", "sql", "git"]

        # 3. Phân bổ ma trận kỹ năng
        must_have = []
        nice_to_have = []
        tools = ["Git", "Docker", "VS Code / IDE", "Postman", "Linux Command Line"]
        soft_skills = ["Giao tiếp & Làm việc nhóm (Teamwork)", "Tư duy giải quyết vấn đề (Problem Solving)", "Quy trình Agile/Scrum", "Đọc hiểu tài liệu tiếng Anh"]

        for idx, t in enumerate(detected_techs):
            disp = TECH_CATALOG[t]["display"]
            if idx < 3:
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
            d = info["docs"]
            if d["name"] not in seen_docs:
                docs_list.append(d)
                seen_docs.add(d["name"])

            for b in info.get("books", []):
                if b not in seen_books:
                    books_list.append(b)
                    seen_books.add(b)

            keywords_list.extend(info.get("keywords", []))
            questions_list.extend(info.get("questions", []))

        # Đảm bảo sách kinh điển chung
        if "Designing Data-Intensive Applications (Martin Kleppmann)" not in seen_books:
            books_list.append("Designing Data-Intensive Applications (Martin Kleppmann)")
        if "Clean Code: A Handbook of Agile Software Craftsmanship (Robert C. Martin)" not in seen_books:
            books_list.append("Clean Code (Robert C. Martin)")

        # 6. Đóng gói kết quả theo chuẩn 5 Tầng Kiến Thức
        analysis = {
            "title": title,
            "company": company,
            "level": level,
            "category": category,
            "overview": {
                "summary": f"Vị trí {title} cấp bậc {level} thuộc lĩnh vực {category}, tập trung vào xây dựng và phát triển hệ thống với các công nghệ chủ đạo: {', '.join([TECH_CATALOG[t]['display'] for t in detected_techs[:3]])}.",
                "mission": f"Làm chủ quy trình phát triển, bàn giao tính năng chất lượng cao đúng hạn và tối ưu hóa hệ thống ổn định.",
                "work_mode": self._detect_work_mode(text)
            },
            "skills_matrix": {
                "must_have": must_have,
                "nice_to_have": nice_to_have,
                "tools": tools,
                "soft_skills": soft_skills
            },
            "roadmap": roadmap,
            "resources": {
                "official_docs": docs_list,
                "books": books_list[:5],
                "search_keywords": keywords_list[:8]
            },
            "interview_prep": questions_list[:6],
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
        """Sinh lộ trình học tập 3 chặng tùy biến theo cấp bậc."""
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
