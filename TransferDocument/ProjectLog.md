# ProjectLog — TransferDocument

## 2026-11-27 — Khởi tạo & Hoàn thiện phiên bản đầu tiên (v1.0)

### Mục tiêu
Xây dựng ứng dụng desktop Python cho phép chọn tài liệu Office mới (`.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`), dịch sang **Tiếng Việt — Font Arial**, giữ nguyên 100% định dạng, màu sắc, bảng biểu, hình ảnh, TextBox/Shape, công thức Excel và không bị lỗi ô chữ (tofu `□`, vỡ khung, cắt chữ, dính Furigana Nhật).

### Các module đã xây dựng
- `settings_reader.py`: Đọc & giải mã (`ENC:`) Gemini API Keys từ `AskCpl/settings.json` (có fallback cục bộ).
- `gemini_safe.py`: Kế thừa từ `MBC/DeThi`, bổ sung phân loại lỗi `free tier is not available` / `set up billing` -> `INVALID_KEY` để xoay vòng tài khoản tức thì không bỏ sót batch.
- `office_converter.py`: Chuyển đổi `.doc/.xls/.ppt` -> `.docx/.xlsx/.pptx` và xuất PDF qua MS Office COM (`win32com.client`), kèm hàm `verify_office_file_opens`.
- `translator_engine.py`: Dịch batch JSON (35 đoạn/lô), bộ lọc thông minh giữ nguyên mã tài liệu/ký hiệu kỹ thuật, chuẩn hóa khoảng trắng giữa chữ CJK (`\u3000` và space), tích hợp Glossary QA/QC Nhật–Việt và `translation_cache.json`.
- `docx_translator.py`: Xử lý trực tiếp OOXML (`lxml`) trên `document.xml`, `header*.xml`, `footer*.xml`, `footnotes.xml`, `endnotes.xml`, `styles.xml`, `numbering.xml`, `theme*.xml`. Hỗ trợ cả TextBox DrawingML/VML và run hỗn hợp chứa `<w:tab/>`/`<w:br/>`/`<w:lastRenderedPageBreak/>`. Ép Arial toàn diện (`ascii/hAnsi/eastAsia/cs`, gỡ theme font) và chống cắt chữ (`trHeight exact -> atLeast`, `normAutofit`).
- `xlsx_translator.py`: Xử lý OOXML trên `sharedStrings.xml`, `worksheets/sheet*.xml`, `drawings/drawing*.xml`, `styles.xml`, `theme*.xml`. Tự động xóa thẻ Furigana Nhật (`<rPh>`, `<phoneticPr>`), giữ công thức/màu/ảnh, ép Arial (xóa `charset/scheme`), bật `wrapText` và tự nới chiều cao dòng.
- `pptx_translator.py`: Hỗ trợ dịch PowerPoint `.pptx` ở mức XML, ép Arial và bật `normAutofit`.
- `document_processor.py`: Bộ điều phối chung cho toàn bộ định dạng Office.
- `app_gui.py`: Giao diện CustomTkinter dark-mode (chọn nhiều file / chọn thư mục / nạp `SourceDocument`, tùy chọn chống cắt chữ / Glossary / Cache / xuất PDF, thanh tiến trình, log thời gian thực, auto-install thư viện thiếu).
- `Chay_Ung_Dung.bat`: File khởi chạy Windows (CRLF, thoát sạch CMD).

### Kết quả kiểm thử thực tế trên 3 file mẫu (`SourceDocument/` -> `OutputDocument/`)
1. `BA-A1-08A-B.doc` -> `BA-A1-08A-B_VI.docx`:
   - Word COM mở hợp lệ (`pages=3, tables=2, shapes=1`), `non_arial=0`, `jp_left=0`.
2. `ZZ-A1-06-1H-Attachment.xlsx` -> `ZZ-A1-06-1H-Attachment_VI.xlsx`:
   - Excel COM mở hợp lệ (`sheets=1`), `fonts={'Arial'}`, `rPh (Furigana)=0`, `jp_left=0`.
3. `ZZ-A1-06-1H.docx` -> `ZZ-A1-06-1H_VI.docx`:
   - Word COM mở hợp lệ (`pages=16, tables=5, shapes=26, inline_images=2`), bảo toàn 7/7 file ảnh (`word/media/`), `non_arial=0`, đã dịch 251/251 đoạn (chỉ còn 1 từ `合否` trong 1 câu do AI giữ nguyên).

### Ghi chú / Chưa tự verify
- Chưa tự verify hiển thị trực quan bằng mắt trên màn hình GUI `app_gui.py` và bố cục trực quan từng trang Word/Excel trong MS Office — cần người dùng mở kiểm tra thực tế.

## 2026-11-27 — Bản nâng cấp bố cục & khắc phục 4 lỗi hiển thị trực quan (v1.1)

### Các lỗi đã khắc phục
1. **Word — Mất dấu cách khi đổi màu chữ (Hình 2)**: Bổ sung `_fix_inter_segment_spacing_and_punct` tự động chèn dấu cách tại ranh giới giữa hai run liền kề khác màu/định dạng và chuẩn hóa dấu câu full-width Nhật (`。` -> `.`, `、` -> `,`, `「」` -> `“”`).
2. **Word — Xuống dòng giữa câu vô lý (Hình 1)**: Bổ sung `_merge_broken_paragraphs` gộp các đoạn văn thuần chữ bị tác giả Nhật bấm Enter + chèn dòng trống đệm giữa câu trước khi dịch (kèm checkbox **"Gộp câu ngắt dòng"** trong `app_gui.py`). Thực tế gộp sạch 39 dòng ngắt giữa câu trên `ZZ-A1-06-1H.docx` và 5 dòng trên `BA-A1-08A-B.doc`.
3. **Word — Ô nhãn quá hẹp gãy chữ & chữ bị kéo dãn ngang (Hình 3)**: Gỡ `<w:w>`, `<w:fitText>`, `<w:spacing>` giãn rộng trong `<w:rPr>` (`Tiêu chuẩn kiểm tra` hết bị bẹt); bổ sung `_optimize_narrow_table_cells` thu gọn lề trong `tcMar=20 dxa`, tự mượn nhẹ độ rộng từ cột rộng theo đúng lưới `tblGrid` (bảo toàn 100% merge & tổng chiều rộng bảng) và co nhẹ cỡ chữ để `Mã số`, `Ký hiệu`, `Trang` hiển thị gọn đẹp trên 1 dòng.
4. **Excel — Giữ nguyên kết cấu merge/tiêu đề nổi & chống cắt tiêu đề xoay dọc**: Không tự ép `wrapText` lên các ô tiêu đề không viền (`borderId=0`), đổi `textRotation="255"` -> `"90"`, tự tính và nới chiều cao hàng hợp lý cho các hàng xoay dọc 90° và các ô `wrapText` có viền không nằm trong merge dọc.
5. **Chống lỗi `PermissionError`**: Bổ sung `_resolve_writable_output_path` trong `document_processor.py` tự động xuất sang `_v2`, `_v3`... nếu file đích đang được mở trong Word/Excel.

### Kiểm thử trực quan (PDF -> PNG qua PyMuPDF)
- Đã tự kiểm tra ảnh render trực tiếp của [ZZ-A1-06-1H_VI_v2.docx](file:///c:/Users/12953%20Bao/Desktop/desktop/work/Project/Python/BasicLearnPython/W3schools/Project%202/TransferDocument/OutputDocument/ZZ-A1-06-1H_VI_v2.docx) và [ZZ-A1-06-1H-Attachment_VI_v2.xlsx](file:///c:/Users/12953%20Bao/Desktop/desktop/work/Project/Python/BasicLearnPython/W3schools/Project%202/TransferDocument/OutputDocument/ZZ-A1-06-1H-Attachment_VI_v2.xlsx):
  - Header Word (`Tiêu chuẩn kiểm tra | Mã số | ZZ-A1-06-1 | Ký hiệu | H | Trang | 2/14`) hiển thị gọn 1 dòng, không gãy/mất chữ.
  - Đoạn văn đỏ & đoạn đen–đỏ liền mạch, có dấu cách đầy đủ giữa các màu.
  - Excel giữ nguyên 100% merge, đường chéo, tiêu đề nổi 1 dòng (`[Bảng phụ 1]...`, `(1) Đo đường kính...`), toàn bộ tiêu đề xoay dọc 90° và hàng 2 dòng (`Máy đo kích thước 3D...`) hiển thị đầy đủ không cắt chữ.

## 2026-11-27 — Hỗ trợ PDF, nâng cấp PowerPoint & Đa ngôn ngữ Nguồn ↔ Đích + Chọn Font (v1.2)

### Tính năng mới
- **`language_config.py`**: Quản lý cấu hình đa ngôn ngữ Nguồn (`auto`, `vi`, `ja`, `en`, `zh`, `ko`) ↔ Đích (`vi`, `ja`, `en`, `zh`, `ko`), ánh xạ Font hệ thống Windows (`.ttf`/`.ttc`), Locale XML và hậu tố file (`_VI`, `_JA`, `_EN`, `_ZH`, `_KO`).
- **`pdf_translator.py`**: Engine dịch PDF bằng PyMuPDF (`pymupdf`) dùng kỹ thuật Redact chọn lọc lớp chữ (`PDF_REDACT_IMAGE_NONE`, `PDF_REDACT_LINE_ART_NONE`) + lấy mẫu màu nền thực tế + `insert_htmlbox` nhúng font Unicode (`scale_low=0.0` tự co vừa khít mọi ô nhỏ) + tự cảnh báo trang PDF scan không có lớp text.
- **`pptx_translator.py` (nâng cấp)**: Hỗ trợ đầy đủ Slide, Notes, Table, GroupShape, SmartArt (`diagrams/data*.xml`), Chart (`charts/chart*.xml`), gộp run cùng định dạng màu/đậm/nghiêng, tự chèn dấu cách ranh giới màu khi dịch sang ngôn ngữ có dấu cách, ép `target_font` + `normAutofit`.
- **`translator_engine.py`, `docx_translator.py`, `xlsx_translator.py`, `office_converter.py`, `document_processor.py`, `app_gui.py`**: Đồng bộ toàn bộ pipeline đa ngôn ngữ 2 chiều (bao gồm dịch từ Tiếng Việt sang Nhật/Anh/Trung/Hàn với Glossary tự đảo chiều Việt–Nhật, Cache tách theo cặp `source->target`, và dropdown chọn **Nguồn → Đích + Font đích** tự động gợi ý font trên GUI).

### Kết quả kiểm thử (v1.2)
- `python -m py_compile` đạt 11/11 module.
- **PDF**: Test thực tế `ja -> vi` (Arial, 23/23 blocks) và `vi -> ja` (Yu Gothic, 18/18 blocks), kiểm tra trực quan PNG xác nhận không lỗi ô vuông, giữ màu chữ đen–đỏ và khung bảng; đã chỉnh `scale_low=0.0` để các ô header cực nhỏ không bị ẩn chữ.
- **PowerPoint**: Test thực tế `vi -> ja` (Yu Gothic, 12/12 segments, XML font 100% `Yu Gothic`) và `vi -> en` (Calibri, 12/12 segments, XML font 100% `Calibri`), kiểm tra PowerPoint COM OK và verify ảnh PNG giữ nguyên màu chữ đỏ–đen, bảng biểu và khoảng trắng.
- Đã dọn sạch toàn bộ thư mục test tạm (`scratch/test_v12`).

## 2026-11-27 — Viết lại Engine PDF theo Spatial Cell-Aware (v1.3)

### Cải tiến cốt lõi trong `pdf_translator.py`
- Chuyển từ trích xuất theo `block` thô sang mức ký tự (`rawdict`) + đọc toàn bộ đường kẻ bảng ngang/dọc từ vector graphics (`page.get_drawings()`).
- Tự động loại khoảng trắng thừa kéo giãn `bbox`, tách chính xác từng cột bảng theo khoảng hở ngang và đường kẻ dọc (không còn trộn 4 cột bảng hay dồn mục `1./2./3.`).
- Chuyển `add_redact_annot(..., fill=False)` kết hợp `PDF_REDACT_IMAGE_NONE` + `PDF_REDACT_LINE_ART_NONE` -> xóa phẫu thuật đúng lớp chữ gốc mà không vẽ mảng màu đè, bảo toàn 100% đường kẻ bảng, highlight vàng, con dấu đỏ và hình ảnh.
- Nới thông minh khung `insert_htmlbox` tới sát đường kẻ/khối kế bên và chuẩn hóa ký tự bullet (`・`/`\uf0b7` -> `•`) hết sạch ô vuông `□`.

### Kết quả kiểm thử thực tế trên 2 file PDF thật
1. `SourceDocument\000-0-J.pdf` -> `OutputDocument\000-0-J_VI.pdf` (3 trang, 107/107 ô/khối, giữ 4/4 ảnh):
   - Đã kiểm tra ảnh PNG trang 1–2: toàn bộ đường kẻ bảng (kể cả bảng 4 cột dầu chống gỉ), highlight vàng, con dấu đỏ `THU NHẬN / QA Section`, vị trí 3 mục `1./2./3.` và dấu chấm `•` giữ nguyên chuẩn xác, không chồng chữ hay ô vuông.
2. `SourceDocument\000-0-E.pdf` -> `OutputDocument\000-0-E_VI.pdf` (3 trang, 117/117 ô/khối):
   - Đã kiểm tra ảnh PNG trang 1–2: hết sạch mảng xám loang và chữ chồng ở bảng dưới, toàn bộ đường kẻ & cột bảng giữ nguyên sắc nét.
- Đã dọn sạch các thư mục ảnh chẩn đoán tạm (`scratch/pdf_diag`, `scratch/pdf_diag2`).

## 2026-11-27 — Nâng cấp PDF Highlight-Aware, Tránh Con Dấu & Chuẩn Hóa Metadata (v1.4)

### 5 cải tiến đã hoàn thiện trong `pdf_translator.py` & `translator_engine.py`
1. **Bảo vệ mã phiên bản & ngày gọn**: Giữ nguyên mã phiên bản (`000-0 g`, `RE_VERSION_CODE`), tự chuyển ngày đơn lẻ (`1994年 6月 20日` / `Jul 1, 2022`) sang dạng gọn `DD/MM/YYYY`, và không gộp các hàng bảng key-value song song không viền (`Ban hành | 20/06/1994`, `Sửa đổi | 01/07/2022`, `Đo lường | 000-0 g`).
2. **Highlight-Aware 2-Pass Redaction & CSS Redraw**: Xóa đúng hình chữ nhật highlight cũ của các cụm đã dịch bằng `PDF_REDACT_LINE_ART_REMOVE_IF_COVERED` (giữ nguyên highlight trên mã không dịch như chữ `g` trong `000-0 g` và không đụng đường kẻ bảng) rồi tô lại highlight bằng CSS `<span style="background-color:#ffff00">` khớp 100% độ dài chữ tiếng Việt mới.
3. **Gộp tiêu đề giãn chữ CJK (`_merge_spaced_cjk_and_cell_tokens`)**: Tự động gộp các tiêu đề giãn chữ như `点  検  ・  処  置  方  法` -> `Phương pháp kiểm tra / xử lý` và `内   容` -> `Nội dung`, căn giữa đều trong ô bảng.
4. **Tránh vật cản Con dấu & Hình ảnh (`_extract_obstacles`)**: Tự động dừng khung chữ trước mép trái của Annotation Stamp (`THU NHẬN / QA Section`) và hình ảnh chèn (4 con dấu trang 3) tối thiểu `4pt`, không bị con dấu che mất chữ.
5. **Gộp mảnh cùng ô bảng hẹp**: Xử lý các mảnh tách lẻ trong cùng ô bảng `< 150pt`.

### Kết quả kiểm chứng trực quan (PNG cả 3 trang)
- `OutputDocument\000-0-J_VI_v2.pdf` (3 trang, 109/109 ô/khối, giữ 4/4 ảnh):
  - Trang 1: `Ban hành 20/06/1994`, `Sửa đổi 01/07/2022`, `Đo lường 000-0 g` (highlight vàng khớp từng pixel trên chữ `g`), con dấu đỏ không che chữ, highlight vàng khớp chữ tiếng Việt, tiêu đề `Phương pháp kiểm tra / xử lý` căn giữa sắc nét.
  - Trang 2 & Trang 3: Toàn bộ bảng lịch sử sửa đổi 6 cột, 4 con dấu đỏ (`冨永`, `石井`, `清水`, `熊倉`), highlight vàng mục `(6)` & dòng `g | 2022.07.01` hiển thị chuẩn xác.
- `OutputDocument\000-0-E_VI.pdf` (3 trang, 127/127 ô/khối): Hết lỗi chồng chữ `000-0 g` lên ngày sửa đổi, giữ nguyên toàn bộ bảng biểu.
- Đã dọn sạch thư mục ảnh tạm `scratch/pdf_v14`.
