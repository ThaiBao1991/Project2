import os
import sys
import re
import json
import glob
import unicodedata
import win32com.client

# Windows Console UTF-8
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GOVERNANCE_PATH = os.path.join(BASE_DIR, 'governance_catalog.json')
CATALOG_PATH = os.path.join(BASE_DIR, 'tailieu_catalog.json')

from storage_manager import (
    get_storage_root,
    resolve_master_excel_path,
    MASTER_EXCELS_DIR,
    is_file_exists,
    atomic_write_json,
)

def remove_accents(input_str):
    if not input_str:
        return ""
    nfkd = unicodedata.normalize('NFKD', str(input_str))
    return "".join([c for c in nfkd if not unicodedata.combining(c)]).lower()

GOVERNANCE_RULES = {
    'U': {
        'pillar': 'Kỹ Thuật & Thiết Bị Sản Xuất',
        'icon': '🔧',
        'default_dept': 'Ban Kỹ thuật sản xuất (生産技術部)',
        'kiem_soat': 'Bản vẽ máy móc, thông số thiết bị, điều kiện ép nhựa thành hình, đóng gói chống rỉ sét, trình tự chuyển giao công nghệ thiết bị.',
        'ho_so': 'Bản vẽ kỹ thuật, Biểu điều kiện thành hình, Nhật ký bảo trì máy, Biên bản nghiệm thu thiết bị.',
        'rui_ro': 'Hỏng hóc máy móc dừng chuyền, rỉ sét linh kiện thiết bị, sai lệch thông số thành hình gây phế phẩm hàng loạt, trễ tiến độ lắp đặt.',
        'ket_qua': 'Hiệu chỉnh nhiệt độ/áp suất/tốc độ máy ép, bảo dưỡng định kỳ, cô lập thiết bị lỗi, dừng chuyền xử lý sự cố.',
        'luu_tru': 'Lưu trữ điện tử trên hệ thống máy chủ KTSX & lưu hồ sơ bảo dưỡng tại xưởng.'
    },
    'Q': {
        'pillar': 'Đảm Bảo & Kiểm Soát Chất Lượng',
        'icon': '🛡️',
        'default_dept': 'Ban Bảo hành chất lượng (品質保証部)',
        'kiem_soat': 'Kích thước dung sai linh kiện, tiêu chuẩn ngoại quan, trị dị thường, tỷ lệ phế phẩm công đoạn, đánh giá khiếu nại khách hàng.',
        'ho_so': 'Biên bản Chất Lượng (BBCL), Form nhập BHC, Báo cáo dị thường công đoạn, Báo cáo đánh giá chất lượng motor.',
        'rui_ro': 'Xuất lọt phế phẩm sang khách hàng, dị thường hàng loạt phát sinh chi phí đền bù, vi phạm tiêu chuẩn ISO 9001 / IATF 16949.',
        'ket_qua': 'Lập phiếu BHC, cô lập tức thì lô hàng nghi ngờ, truy tìm nguyên nhân gốc rễ (5 Why, 4M), ban hành đối sách phòng ngừa tái phát.',
        'luu_tru': 'Lưu trữ hồ sơ chất lượng tối thiểu 5 - 10 năm theo quy chuẩn quốc tế ngành ô tô.'
    },
    'E': {
        'pillar': 'Quản Lý Môi Trường & Hóa Chất',
        'icon': '🌿',
        'default_dept': 'Ban Quản lý Môi trường & An toàn (環境管理部)',
        'kiem_soat': 'Hàm lượng chất độc hại RoHS/REACH (Pb, Cd, Hg, Cr6+), xử lý hóa chất độc hại, phân loại rác thải nguy hại, môi trường phòng sạch.',
        'ho_so': 'Chứng chỉ RoHS linh kiện, Bảng chỉ dẫn an toàn hóa chất (SDS), Báo cáo kiểm định môi trường định kỳ.',
        'rui_ro': 'Bị phạt chế tài pháp luật, đình chỉ xuất khẩu hàng vào thị trường Châu Âu/Mỹ do vi phạm chất cấm, sự cố tràn đổ hóa chất.',
        'ket_qua': 'Từ chối nhập kho linh kiện không đạt tiêu chuẩn xanh, thu hồi sản phẩm vi phạm, kích hoạt quy trình ứng phó sự cố môi trường.',
        'luu_tru': 'Lưu trữ hồ sơ kiểm định môi trường theo quy định pháp luật môi trường hiện hành.'
    },
    'G': {
        'pillar': 'Quản Trị Chung & An Ninh Dữ Liệu',
        'icon': '🏢',
        'default_dept': 'Ban Hành chính & Ban Hệ thống thông tin (総務・情報システム部)',
        'kiem_soat': 'Công bố thông tin ra bên ngoài, quy trình thanh lý hủy bỏ linh kiện - tài sản, phân quyền an ninh mạng và bảo mật dữ liệu.',
        'ho_so': 'Quyết định ban hành nội quy, Biên bản hủy bỏ linh kiện, Cam kết bảo mật thông tin, Nhật ký truy cập hệ thống.',
        'rui_ro': 'Lộ lọt bí mật công nghệ, thất thoát tài sản phế phẩm, rò rỉ dữ liệu khách hàng, mất mát tài liệu khi sập server.',
        'ket_qua': 'Thu hồi quyền truy cập, thanh tra kỷ luật nội bộ, báo cáo Ban Giám Đốc, sao lưu phục hồi dữ liệu dự phòng.',
        'luu_tru': 'Lưu trữ điện tử bảo mật nhiều lớp trên hệ thống mạng nội bộ công ty.'
    },
    'HCDK': {
        'pillar': 'Đo Lường & Hiệu Chỉnh Thiết Bị',
        'icon': '📏',
        'default_dept': 'Tổ Quản lý Thiết bị đo lường / Phòng Kiểm tra',
        'kiem_soat': 'Sai số dụng cụ đo (Thước kẹp, Panme, Kính hiển vi, OGP, LM-X), chu kỳ kiểm định, hạn dán tem hiệu chuẩn thiết bị.',
        'ho_so': 'Form điểm kiểm máy đo hàng ngày/tháng (VDM-312-DK-xxx), Giấy chứng nhận hiệu chuẩn, Tem kiểm định trên máy.',
        'rui_ro': 'Dụng cụ đo trôi dạt sai số dẫn đến kết luận nhầm hàng hỏng thành đạt hoặc ngược lại, làm sai lệch toàn bộ dữ liệu đo.',
        'ket_qua': 'Dán tem ngưng sử dụng màu đỏ, cô lập dụng cụ đo sai lệch, hiệu chỉnh lại hoặc gửi trung tâm kiểm định bên ngoài.',
        'luu_tru': 'Form điểm kiểm lưu tại chuyền + số hóa lưu trữ trên máy chủ IT hóa định kỳ.'
    },
    'QCKT': {
        'pillar': 'Quy Cách Kiểm Tra Linh Kiện',
        'icon': '🔍',
        'default_dept': 'Bộ phận Tiêu chuẩn kiểm tra (Phòng QC)',
        'kiem_soat': 'Bản vẽ ngoại quan, kích thước danh định, dung sai cho phép từng linh kiện (Trục, Nam châm, Vỏ, Chổi than), mẫu khuyết tật giới hạn.',
        'ho_so': 'Bản quy cách kiểm tra linh kiện (Rev. hiện hành), Bảng giới hạn mẫu ngoại quan (BBS), Báo cáo kết quả đo thực tế.',
        'rui_ro': 'Công nhân kiểm tra sai phương pháp, bỏ sót lỗi nứt/bavia/rỉ sét, dùng nhầm phiên bản bản vẽ đã hết hiệu lực.',
        'ket_qua': 'Cập nhật bản Rev mới nhất, thu hồi bản cũ, đào tạo lại công nhân kiểm tra theo mẫu giới hạn chuẩn.',
        'luu_tru': 'Số hóa và lưu trữ tập trung trên máy chủ IT hóa kiểm tra.'
    },
    'NVKHO': {
        'pillar': 'Quản Lý Kho Vận & Vật Tư',
        'icon': '📦',
        'default_dept': 'Bộ phận Kho vận & Logistics',
        'kiem_soat': 'Điều kiện bảo quản linh kiện trong kho (Nhiệt độ, Độ ẩm), hạn sử dụng vật tư, thủ tục nhập - xuất - tồn, quy trình kế hoạch dự phòng.',
        'ho_so': 'Thẻ kho, Phiếu kiểm tra nhiệt độ độ ẩm, Sổ theo dõi xuất nhập vật tư (ZA/ZB Series), Manual phòng chống rủi ro kho.',
        'rui_ro': 'Vật tư bị ẩm mốc rỉ sét trong kho, xuất nhầm chủng loại linh kiện cho chuyền sản xuất, cạn kiệt tồn kho an toàn.',
        'ket_qua': 'Điều chỉnh điều hòa máy hút ẩm, thanh lý vật tư quá hạn, kích hoạt kế hoạch dự phòng khẩn cấp Contingency Planning.',
        'luu_tru': 'Hồ sơ kho lưu trữ theo năm tài chính.'
    }
}

def is_master_root_document(code: str, title: str, module: str) -> tuple:
    """
    Classify whether a document is a MASTER / ROOT REGULATION (Level 1) or EXECUTION DETAIL (Level 2).
    Returns (is_master: bool, tier_label: str, parent_code: str)
    """
    code_u = code.upper().strip()
    title_l = title.lower().strip()
    
    # 1. Level 1 - Corporate Manuals (Sổ tay chất lượng, Sổ tay môi trường)
    if any(k in code_u for k in ['-Z001', '-Z002', '-Z003']) or 'sổ tay' in title_l or 'manual' in title_l:
        return True, "👑 HỒ SƠ NGUỒN (Sổ Tay Cốt Lõi)", "TOÀN TẬP ĐOÀN"
        
    # 2. Level 1 - Corporate Fundamental Regulations (*-A, *-B, *-C Series in Yeu Linh)
    m_level1 = re.search(r'([A-Z]+-[A-Z]+-[ABC]\d+)', code_u)
    if m_level1:
        return True, "👑 HỒ SƠ NGUỒN (Quy Định Quản Lý Khung)", code_u.split('-')[0] + "-MAB"
        
    # 3. Level 1 - Fundamental Quality Standards (QA-A, QA-B)
    if code_u.startswith('QA-A') or code_u.startswith('QA-B'):
        return True, "👑 HỒ SƠ NGUỒN (Tiêu Chuẩn Bảo Hành Cơ Bản)", "QA-ROOT"
        
    # 4. Level 1 - Fundamental Warehouse Operations (ZA-A)
    if code_u.startswith('ZA-A'):
        return True, "👑 HỒ SƠ NGUỒN (Chính Sách Kho Vận Khung)", "KHO-ROOT"
        
    # 5. Level 1 - Fundamental Inspection Calibration Framework
    if code_u in ['000-0-V', '000-00(VDM-312-DK-156)', 'INF-A', 'Z00-0-V'] or 'quy định chung' in title_l:
        return True, "👑 HỒ SƠ NGUỒN (Tiêu Chuẩn Điểm Kiểm Khung)", "HCDK-ROOT"
        
    # 6. Title keywords explicitly denoting Master Policies / Umbrella Regulations
    master_keywords = [
        'quy định quản lý', 'chính sách chất lượng', 'quy định giám định',
        'quy định quyền hạn', 'nội quy chung', 'tiêu chuẩn cơ sở',
        'biểu liệt kê biên bản chất lượng vdm'
    ]
    if any(k in title_l for k in master_keywords) and not code_u.startswith('VDM-312-DK-'):
        return True, "👑 HỒ SƠ NGUỒN (Quy Định Khung)", "ROOT"
        
    # Infer parent master code for child execution documents
    parent_ref = "Hồ sơ nguồn tương ứng"
    if '-D' in code_u:
        parent_prefix = code_u.split('-D')[0]
        parent_ref = f"{parent_prefix}-B (Quy định quản lý)"
    elif 'VDM-312-DK-' in code_u:
        parent_ref = "000-00(VDM-312-DK-156) Tiêu chuẩn điểm kiểm gốc"
    elif module == 'qckt':
        parent_ref = "IT HOA QUY CACH KIEM TRA (Bản Quy Cách Chuẩn)"
    elif code_u.startswith('QA-D'):
        parent_ref = "QA-A (Tiêu Chuẩn Bảo Hành Toàn Bộ)"
    elif code_u.startswith('ZB-'):
        parent_ref = "ZA-A-04 (Logistics Operation Manual)"
        
    return False, "📄 HỒ SƠ TRIỂN KHAI (Chi Tiết)", parent_ref

def extract_all_master_excel_metadata():
    """
    Extracts rich titles, Japanese titles, departments, component names, and device names
    from all 8 local Master Excel files using fast matrix memory parsing.
    Searches across storage_root, BASE_DIR/master_excels, and BASE_DIR (deduplicated).
    Returns: (excel_meta, device_map)
    """
    storage_root = get_storage_root()
    raw_candidates = []
    if os.path.exists(MASTER_EXCELS_DIR):
        raw_candidates.extend(glob.glob(os.path.join(MASTER_EXCELS_DIR, '*.xls*')))
    if os.path.exists(storage_root):
        raw_candidates.extend(glob.glob(os.path.join(storage_root, '*', '**', '*.xls*'), recursive=True))
        raw_candidates.extend(glob.glob(os.path.join(storage_root, '*.xls*')))
    if os.path.normcase(os.path.abspath(storage_root)) != os.path.normcase(os.path.abspath(BASE_DIR)):
        raw_candidates.extend(glob.glob(os.path.join(BASE_DIR, '*', '**', '*.xls*'), recursive=True))

    excel_files = []
    seen_names = set()
    for ef in raw_candidates:
        bn = os.path.basename(ef)
        if bn.startswith('~$') or not bn.lower().endswith(('.xls', '.xlsx', '.xlsm')):
            continue
        key = bn.lower()
        if key not in seen_names:
            seen_names.add(key)
            excel_files.append(ef)

    if not excel_files:
        return {}, {}

    excel = None
    excel_meta = {}
    device_map = {}
    
    def add_meta(code_raw, title_v, title_j=None, dept=None, part_no=None):
        if not code_raw:
            return
        c = str(code_raw).strip()
        if not c or c.lower() in ['none', 'maso', 'mã số', 'mã số 番号', '番号']:
            return
        clean_v = str(title_v).replace('\n', ' ').strip() if title_v and str(title_v).lower() != 'none' else ''
        clean_j = str(title_j).replace('\n', ' ').strip() if title_j and str(title_j).lower() != 'none' else ''
        clean_d = str(dept).replace('\n', ' ').strip() if dept and str(dept).lower() != 'none' else ''
        clean_p = str(part_no).replace('\n', ' ').strip() if part_no and str(part_no).lower() != 'none' else ''
        
        t_full = clean_v
        if clean_j and clean_j != clean_v:
            t_full = f"{clean_v} ({clean_j})" if clean_v else clean_j
            
        c_upper = c.upper()
        entry = {
            'title': t_full,
            'title_v': clean_v,
            'title_j': clean_j,
            'dept': clean_d,
            'part': clean_p
        }
        excel_meta[c_upper] = entry
        base_c = re.sub(r'-[VESJ]$', '', c_upper)
        if base_c not in excel_meta:
            excel_meta[base_c] = entry
            
        m_dev = re.match(r'^(\d{3}(-\d+)?)$', base_c)
        if m_dev:
            device_map[m_dev.group(1)] = clean_v or clean_j
            prefix3 = m_dev.group(1).split('-')[0]
            if prefix3 not in device_map:
                device_map[prefix3] = clean_v or clean_j

    try:
        excel = win32com.client.Dispatch('Excel.Application')
        excel.Visible = False
        excel.DisplayAlerts = False
        for ef in excel_files:
            full_p = os.path.abspath(ef)
            wb = excel.Workbooks.Open(full_p, ReadOnly=True)
            fname = os.path.basename(ef)
            
            for s in wb.Sheets:
                raw = s.UsedRange.Value
                if not raw or len(raw) < 2:
                    continue
                rows = [list(r) for r in raw]
                sname = s.Name
                
                if 'QUY CACH KIEM TRA' in fname:
                    if 'quy cach kiem tra' in sname.lower():
                        for r in rows[7:]:
                            if len(r) > 4:
                                add_meta(r[1], r[4], r[3], part_no=r[2])
                    elif 'do luong' in sname.lower():
                        for r in rows[7:]:
                            if len(r) > 3:
                                add_meta(r[1], r[3], r[2])
                elif 'BAO HANH(MMK)' in fname:
                    for r in rows[7:]:
                        if len(r) > 3:
                            add_meta(r[1], r[3], r[2])
                elif 'TIEU CHUAN KIEM TRA.xls' in fname:
                    for r in rows[9:]:
                        if len(r) > 3:
                            add_meta(r[1], r[3], r[2])
                elif 'TIEU CHUAN MOI TRUONG' in fname:
                    for r in rows[9:]:
                        if len(r) > 3:
                            add_meta(r[1], r[3], r[2])
                elif 'BIEU LIET KE' in fname:
                    for r in rows[2:]:
                        if len(r) > 2:
                            add_meta(r[1], r[2])
                elif 'NGHIEP VU KHO' in fname:
                    for r in rows[9:]:
                        if len(r) > 3:
                            add_meta(r[1], r[3], r[2])
                elif 'HIEU CHINH DIEM KIEM' in fname:
                    if 'HC - DK' in sname:
                        for r in rows[7:]:
                            if len(r) > 3:
                                add_meta(r[1], r[3], r[2])
                    elif 'TU CHU' in sname:
                        for r in rows[5:]:
                            if len(r) > 2:
                                add_meta(r[1], r[2])
                elif 'TIM KIEM LOAI QUI DINH' in fname:
                    if 'TONG' in sname:
                        for r in rows[6:]:
                            if len(r) > 7:
                                add_meta(r[1], r[2], dept=r[7])
            wb.Close(False)
    except Exception as e:
        print(f"Lỗi trích xuất metadata Excel: {e}")
    finally:
        if excel is not None:
            try:
                excel.Quit()
            except Exception:
                pass
        
    return excel_meta, device_map

def synthesize_metadata(doc, excel_meta, device_map):
    """
    Synthesize complete doc_title, summary, dept, pillar, and search_text for a document.
    """
    code = doc.get('doc_code', '').strip()
    fname = doc.get('filename', '')
    mod = doc.get('module_id', '')
    code_u = code.upper()
    base_c = re.sub(r'-[VESJ]$', '', code_u)
    
    meta_entry = excel_meta.get(code_u, excel_meta.get(base_c, {}))
    raw_title = meta_entry.get('title', '')
    raw_dept = meta_entry.get('dept', '')
    
    # 1. Determine Title
    title = raw_title
    if not title:
        if mod == 'qckt':
            # Clean component title from filename
            clean = re.sub(r'\.(pdf|xls[xm]?)$', '', fname, flags=re.I)
            clean = re.sub(r'\s*\((V\s*IT|VJ|V|J\s*IT|J)\)\s*', '', clean, flags=re.I).strip()
            title = f"Bản quy cách kiểm tra: {clean}"
        elif mod == 'hcdk':
            # Check for form or standard
            m_form = re.search(r'\(?(VDM-312-DK-\d+)\)?', fname)
            m_code = re.match(r'^(\d{3}(-\d+)?)', code)
            dev_key = m_code.group(1) if m_code else ''
            dev_name = device_map.get(dev_key, device_map.get(dev_key.split('-')[0] if '-' in dev_key else '', 'Thiết bị đo lường'))
            
            if m_form:
                form_no = m_form.group(1)
                title = f"Biểu mẫu điểm kiểm: {dev_name} (Form: {form_no})"
            else:
                title = f"Tiêu chuẩn điểm kiểm: {dev_name} ({code})"
        else:
            clean = re.sub(r'\.(pdf|xls[xm]?)$', '', fname, flags=re.I)
            clean = re.sub(r'\s*\((V\s*IT|VJ|V|J\s*IT|J)\)\s*', '', clean, flags=re.I).strip()
            title = f"Tài liệu tiêu chuẩn {clean}"

    # 2. Determine Department & Pillar
    rule_key = 'QCKT' if mod == 'qckt' else \
               'HCDK' if mod == 'hcdk' else \
               'E' if mod == 'tcmt' or code_u.startswith('E-') or 'MT' in code_u else \
               'U' if code_u.startswith('U-') else \
               'G' if code_u.startswith('G-') else \
               'NVKHO' if mod == 'nvkho' or code_u.startswith('Z') else 'Q'
               
    rule = GOVERNANCE_RULES.get(rule_key, GOVERNANCE_RULES['Q'])
    pillar = rule['pillar']
    icon = rule['icon']
    dept = raw_dept if raw_dept else rule['default_dept']
    
    # 3. Determine Master Root & Parent Ref
    is_master, tier_label, parent_ref = is_master_root_document(code, title, mod)
    
    # 4. Synthesize Summary (Mô tả công việc & Mục đích của file)
    summary = ""
    if is_master:
        summary = f"👑 Quy định nguồn chuẩn mực cốt lõi ({tier_label}) thuộc trụ cột {pillar}, do {dept} ban hành. Thiết lập nguyên tắc chung, thẩm quyền phê duyệt và quy trình khung bắt buộc cho toàn bộ nhà máy tuân thủ."
    elif mod == 'qckt':
        summary = f"Quy cách kiểm tra linh kiện motor: Kiểm soát kích thước danh định, dung sai lắp ghép, tiêu chuẩn ngoại quan (không nứt, bavia, biến dạng) và mẫu giới hạn lỗi (BBS)."
    elif mod == 'hcdk':
        if 'Biểu mẫu' in title or 'Form:' in title or 'VDM-312-DK' in title:
            summary = f"Biểu mẫu điểm kiểm định kỳ hàng ngày/tháng: Ghi chép dữ liệu đo đạc thực tế, xác nhận độ chính xác máy đo và trạng thái an toàn trước khi vào chuyền."
        else:
            summary = f"Bản tiêu chuẩn kỹ thuật điểm kiểm thiết bị: Quy định trình tự thao tác, chu kỳ hiệu chuẩn, giới hạn sai số cho phép và phán định đạt/không đạt."
    elif mod in ['tcbh', 'tckt']:
        summary = f"Tiêu chuẩn bảo hành & kiểm tra chất lượng: Hướng dẫn kiểm tra xác suất xuất xưởng, phán định thông số điện/cơ, kiểm soát nhãn in và xử lý phế phẩm."
    elif mod == 'nvbh':
        summary = f"Nghiệp vụ phòng bảo hành chất lượng: Quy định quy trình giải quyết sự cố, phân tích phế phẩm motor, giám tra nội bộ và đào tạo Keyman."
    elif mod == 'nvkho':
        summary = f"Nghiệp vụ kho vận & vật tư: Quy định quy trình xuất - nhập - tồn linh kiện, kiểm soát nhiệt độ độ ẩm kho và kế hoạch dự phòng Contingency."
    elif mod == 'tcmt':
        summary = f"Tiêu chuẩn quản lý môi trường: Kiểm soát chất độc hại cấm sử dụng (RoHS/REACH), phân loại rác thải nguy hại và an toàn hóa chất."
    else:
        summary = f"Quy trình tác nghiệp chi tiết ({pillar}): Quy định cụ thể các bước thực hiện, phân công trách nhiệm và biểu mẫu đối chiếu theo {parent_ref}."

    # 5. Search Text (Accent-free and Accented for Ultra-Fast Search)
    search_text = (
        f"{code} {title} {summary} {dept} {pillar} {parent_ref} {fname} "
        f"{remove_accents(code)} {remove_accents(title)} {remove_accents(summary)} "
        f"{remove_accents(dept)} {remove_accents(pillar)}"
    )

    return {
        'doc_title': title,
        'summary': summary,
        'so_huu': dept,
        'pillar': pillar,
        'icon': icon,
        'is_master_root': is_master,
        'doc_tier': tier_label,
        'parent_ref': parent_ref,
        'search_text': search_text
    }

def build_governance_matrix():
    """
    Parse master Excels and catalog to build the complete 7-element Governance Matrix
    and enrich all documents with rich titles, summaries, and search indexes.
    """
    print("=== Đang xây dựng Ma Trận Quản Trị & Làm Giàu Tiêu Đề / Tóm Tắt Dữ Liệu ===")
    
    # 1. Load catalog
    catalog = []
    if os.path.exists(CATALOG_PATH):
        with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
            catalog = json.load(f)
            
    doc_lookup = {}
    for item in catalog:
        code = item.get('doc_code', '').upper()
        if code and code not in doc_lookup:
            doc_lookup[code] = item

    # 2. Extract Master Excel Metadata
    print("-> Đang trích xuất tiêu đề và thông tin nghiệp vụ từ 8 file Excel tổng...")
    excel_meta, device_map = extract_all_master_excel_metadata()
    print(f"-> Đã trích xuất {len(excel_meta)} mã quy định và {len(device_map)} thiết bị đo lường.")
    
    # 3. Parse TIM KIEM LOAI QUI DINH
    yeulinh_records = []
    f3_candidates = [
        resolve_master_excel_path('03_YEU_LINH_QUI_DINH', 'TIM KIEM LOAI QUI DINH.xlsm'),
        os.path.join(MASTER_EXCELS_DIR, 'TIM KIEM LOAI QUI DINH.xlsm'),
        os.path.join(BASE_DIR, '03_YEU_LINH_QUI_DINH', 'TIM KIEM LOAI QUI DINH.xlsm'),
        r'\\vdm-wts08\IT HOA YEU LINH  ー要領IT化\TIM KIEM LOAI QUI DINH 【規程類一覧】.xlsm'
    ]
    f3 = next((f for f in f3_candidates if f and is_file_exists(f)), None)
    
    if f3:
        try:
            excel = win32com.client.Dispatch('Excel.Application')
            excel.Visible = False
            excel.DisplayAlerts = False
            wb = excel.Workbooks.Open(os.path.abspath(f3), ReadOnly=True)
            ws = wb.Sheets('TONG・合計')
            raw = ws.UsedRange.Value
            for r in raw[6:]:
                if r and len(r) > 7 and r[1] is not None:
                    code_str = str(r[1]).strip().upper()
                    name_str = str(r[2]).strip().replace('\n', ' ') if r[2] else ""
                    dept_str = str(r[7]).strip().replace('\n', ' ') if r[7] else ""
                    rev_str = str(r[3]).strip() if r[3] else ""
                    date_str = str(r[8]).strip() if len(r) > 8 and r[8] else ""
                    
                    yeulinh_records.append({
                        'code': code_str,
                        'name': name_str,
                        'dept': dept_str,
                        'rev': rev_str,
                        'date': date_str
                    })
            wb.Close(False)
            excel.Quit()
        except Exception as e:
            print(f"Lỗi đọc Excel Yeu Linh: {e}")

    # 4. Build Governance Items
    gov_items = []
    master_count = 0
    detail_count = 0
    
    # Process Yeu Linh records
    for rec in yeulinh_records:
        code = rec['code']
        cat_match = doc_lookup.get(code)
        local_path = cat_match.get('local_path', '') if cat_match else ''
        remote_path = cat_match.get('remote_path', '') if cat_match else ''
        is_canceled = cat_match.get('is_canceled', False) if cat_match else False
        status = cat_match.get('status', 'Đang Hiệu Lực') if cat_match else 'Đang Hiệu Lực'
        
        doc_dummy = {'doc_code': code, 'filename': f"{code}.pdf", 'module_id': 'yeulinh'}
        synth = synthesize_metadata(doc_dummy, excel_meta, device_map)
        
        if synth['is_master_root']:
            master_count += 1
        else:
            detail_count += 1
            
        rule = GOVERNANCE_RULES.get('Q', GOVERNANCE_RULES['Q'])
        for k in GOVERNANCE_RULES:
            if GOVERNANCE_RULES[k]['pillar'] == synth['pillar']:
                rule = GOVERNANCE_RULES[k]
                break
                
        gov_item = {
            'doc_code': code,
            'title': rec['name'] if rec['name'] else synth['doc_title'],
            'doc_title': rec['name'] if rec['name'] else synth['doc_title'],
            'summary': synth['summary'],
            'rev': rec['rev'],
            'date': rec['date'],
            'pillar': synth['pillar'],
            'icon': synth['icon'],
            'so_huu': rec['dept'] if rec['dept'] else synth['so_huu'],
            'kiem_soat': rule['kiem_soat'],
            'ho_so': rule['ho_so'],
            'rui_ro': rule['rui_ro'],
            'ket_qua': rule['ket_qua'],
            'luu_tru': rule['luu_tru'],
            'status': status,
            'is_canceled': is_canceled,
            'is_master_root': synth['is_master_root'],
            'doc_tier': synth['doc_tier'],
            'parent_ref': synth['parent_ref'],
            'local_path': local_path,
            'remote_path': remote_path,
            'source_module': 'yeulinh',
            'search_text': synth['search_text']
        }
        gov_items.append(gov_item)
        
    # Process other catalog modules
    for doc in catalog:
        mod = doc.get('module_id')
        if mod == 'yeulinh':
            continue
            
        code = doc.get('doc_code', '')
        if not code:
            continue
            
        synth = synthesize_metadata(doc, excel_meta, device_map)
        if synth['is_master_root']:
            master_count += 1
        else:
            detail_count += 1
            
        rule = GOVERNANCE_RULES.get('Q', GOVERNANCE_RULES['Q'])
        for k in GOVERNANCE_RULES:
            if GOVERNANCE_RULES[k]['pillar'] == synth['pillar']:
                rule = GOVERNANCE_RULES[k]
                break
                
        gov_item = {
            'doc_code': code,
            'title': synth['doc_title'],
            'doc_title': synth['doc_title'],
            'summary': synth['summary'],
            'rev': 'Current',
            'date': '',
            'pillar': synth['pillar'],
            'icon': synth['icon'],
            'so_huu': synth['so_huu'],
            'kiem_soat': rule['kiem_soat'],
            'ho_so': rule['ho_so'],
            'rui_ro': rule['rui_ro'],
            'ket_qua': rule['ket_qua'],
            'luu_tru': rule['luu_tru'],
            'status': doc.get('status', 'Đang Hiệu Lực'),
            'is_canceled': doc.get('is_canceled', False),
            'is_master_root': synth['is_master_root'],
            'doc_tier': synth['doc_tier'],
            'parent_ref': synth['parent_ref'],
            'local_path': doc.get('local_path', ''),
            'remote_path': doc.get('remote_path', ''),
            'source_module': mod,
            'search_text': synth['search_text']
        }
        gov_items.append(gov_item)

    # Save governance catalog
    atomic_write_json(GOVERNANCE_PATH, gov_items)
        
    # 5. Enrich 100% of documents in tailieu_catalog.json
    print("-> Đang làm giàu 100% tiêu đề, tóm tắt và chỉ mục tìm kiếm vào tailieu_catalog.json...")
    for doc in catalog:
        synth = synthesize_metadata(doc, excel_meta, device_map)
        doc['doc_title'] = synth['doc_title']
        doc['summary'] = synth['summary']
        doc['so_huu'] = synth['so_huu']
        doc['pillar'] = synth['pillar']
        doc['icon'] = synth['icon']
        doc['is_master_root'] = synth['is_master_root']
        doc['doc_tier'] = synth['doc_tier']
        doc['parent_ref'] = synth['parent_ref']
        doc['search_text'] = synth['search_text']
        
    atomic_write_json(CATALOG_PATH, catalog)
        
    print(f"✅ Hoàn tất Ma Trận Quản Trị & Làm Giàu Dữ Liệu:")
    print(f"   👑 HỒ SƠ NGUỒN (Master Root): {master_count} quy định gốc cốt lõi")
    print(f"   📄 HỒ SƠ TRIỂN KHAI (Execution Detail): {detail_count} tài liệu chi tiết")
    print(f"   📚 100% tài liệu ({len(catalog):,} file) đã được cấp Tiêu Đề tiếng Việt và Tóm Tắt Nghiệp Vụ!")
    return gov_items

def load_governance_matrix():
    if os.path.exists(GOVERNANCE_PATH):
        try:
            with open(GOVERNANCE_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return build_governance_matrix()
    return build_governance_matrix()

if __name__ == '__main__':
    build_governance_matrix()
