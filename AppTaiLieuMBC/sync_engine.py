import os
import sys
import re
import json
import time
import shutil
import unicodedata
from datetime import datetime

# Windows Console UTF-8
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')
CATALOG_PATH = os.path.join(BASE_DIR, 'tailieu_catalog.json')

from storage_manager import (
    get_storage_root,
    get_module_storage_root,
    resolve_local_path,
    resolve_master_excel_path,
    to_storage_rel_or_abs,
    is_file_exists,
    atomic_write_json,
)

def to_long_path(p: str) -> str:
    """Handle Windows MAX_PATH limit (>260 chars)"""
    if sys.platform != 'win32' or not p:
        return p
    abs_p = os.path.abspath(p)
    if abs_p.startswith('\\\\?\\'):
        return abs_p
    if abs_p.startswith('\\\\'):
        return '\\\\?\\UNC\\' + abs_p[2:]
    return '\\\\?\\' + abs_p

# Regex for Japanese / Chinese characters (Hiragana, Katakana, Kanji, Hanzi, CJK Symbols)
CJK_REGEX = re.compile(r'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uffef\u4e00-\u9faf\u3400-\u4dbf\uf900-\ufaff]')

def sanitize_ascii_name(name: str) -> str:
    """
    Remove Japanese and Chinese characters, and normalize name to clean English/ASCII letters,
    digits, spaces, hyphens, underscores, dots, parentheses.
    """
    if not name:
        return ""
    
    # Remove CJK characters
    cleaned = CJK_REGEX.sub('', name)
    
    # Replace common Asian punctuation with standard ASCII
    replacements = {
        '・': '-',
        'ー': '-',
        '【': '[',
        '】': ']',
        '（': '(',
        '）': ')',
        '、': ',',
        '。': '.',
        '〜': '-',
        '～': '-',
        '：': ':',
        '　': ' '  # Full-width space
    }
    for k, v in replacements.items():
        cleaned = cleaned.replace(k, v)
        
    # Remove accents for purely English character requirement
    # Normalize unicode to decomposed form and strip diacritics
    nfkd_form = unicodedata.normalize('NFKD', cleaned)
    ascii_only = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    
    # Replace invalid Windows filename characters <>:"/\|?*
    ascii_only = re.sub(r'[<>:"/\\|?*]', '_', ascii_only)
    
    # Replace multiple underscores or spaces
    ascii_only = re.sub(r' +', ' ', ascii_only)
    ascii_only = re.sub(r'_+', '_', ascii_only)
    ascii_only = re.sub(r'-+', '-', ascii_only)
    
    # Strip leading/trailing spaces, dots, dashes
    ascii_only = ascii_only.strip(' .-_')
    
    return ascii_only

def is_japanese_path_or_file(filename: str, full_path: str) -> bool:
    """Detect if file or path belongs to Japanese version"""
    fl = filename.lower()
    pl = full_path.lower()
    
    # Japanese folder indicators
    if 'ban nhat' in pl or 'ban j' in pl or '\\j\\' in pl or '/j/' in pl:
        return True
        
    # Japanese file indicators
    if fl.endswith('-j.pdf') or fl.endswith('_j.pdf') or fl.endswith(' j.pdf'):
        return True
    if ' (j ' in fl or '(j it)' in fl or ' (j).pdf' in fl or '(j).pdf' in fl:
        return True
    if '-j ' in fl or '-j huy' in fl or ' j huy' in fl:
        return True
    if fl.endswith('-j.xls') or fl.endswith('-j.xlsx'):
        return True
        
    return False

def is_vietnamese_pdf(filename: str, full_path: str) -> bool:
    """Detect if file is a Vietnamese PDF or relevant bilingual file"""
    if not filename.lower().endswith('.pdf'):
        return False
        
    if is_japanese_path_or_file(filename, full_path):
        return False
        
    fl = filename.lower()
    pl = full_path.lower()
    
    # Vietnamese indicators
    if 'ban viet' in pl or 'ban v' in pl or 'vdm' in pl:
        return True
    if '-v.pdf' in fl or '_v.pdf' in fl or '(v)' in fl or '(v it)' in fl or '-v ' in fl:
        return True
    if '(vj)' in fl or '-vj' in fl or '_vj' in fl:
        return True
    if 'chu y' in fl or 'huong dan' in fl:
        return True
        
    # General non-Japanese PDF fallback in English/Vietnamese folders
    return True

def extract_doc_code(filename: str) -> str:
    """Extract standard document code like U-MAB-D001, QA-A001, VDM-312-DK-001, ZB-A-03, etc."""
    base = os.path.splitext(filename)[0]
    # Patterns like U-MAB-D001, Q-MAB-C014, QA-A001, VDM-312-DK-001
    m = re.search(r'([A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)?)', base)
    if m:
        return m.group(1).upper()
    m2 = re.search(r'([A-Za-z0-9]+-[A-Za-z0-9]+)', base)
    if m2:
        return m2.group(1).upper()
    return base.strip()

def is_canceled_item(name: str, path: str) -> bool:
    """Detect if folder or filename indicates canceled / abolished document"""
    check_str = (name + " " + path).lower()
    for kw in ['hủy', 'huy', 'hủy bỏ', 'huy bo', 'haishi', 'bỏ', 'bo']:
        if kw in check_str:
            return True
    return False

def load_module_config(cfg_path: str) -> dict:
    with open(cfg_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_module_config(cfg_path: str, data: dict):
    atomic_write_json(cfg_path, data)

def sync_single_module(cfg_path: str, mode: str = 'fast', progress_callback=None) -> dict:
    """
    Perform sync for a single module:
    mode='fast': Only scan and download new or modified files. Skip unchanged existing files.
    mode='full': Deep scan, verify all files and re-index everything.
    """
    cfg = load_module_config(cfg_path)
    module_id = cfg['id']
    module_name = cfg['name']
    local_subfolder_rel = cfg['local_subfolder']
    global_storage_root = get_storage_root()
    module_storage_root = get_module_storage_root(cfg)
    local_subfolder_abs = os.path.join(module_storage_root, local_subfolder_rel)
    os.makedirs(to_long_path(local_subfolder_abs), exist_ok=True)
    
    excel_remote = cfg.get('excel_remote')
    excel_local_name = cfg.get('excel_local_name')
    remote_scan_roots = cfg.get('remote_scan_roots', [])
    sync_state = cfg.get('sync_state', {})
    
    stats = {
        'module_id': module_id,
        'module_name': module_name,
        'mode': mode,
        'total_scanned': 0,
        'downloaded': 0,
        'skipped': 0,
        'errors': 0,
        'restored_links': 0,
        'master_excel_updated': False
    }
    
    def log(msg):
        if progress_callback:
            progress_callback(msg)
        else:
            print(f"[{module_id.upper()}] {msg}")
            
    mode_text = "⚡ NHANH (Chỉ File Mới/Thay Đổi)" if mode == 'fast' else "🔄 TOÀN BỘ (Quét & Kiểm Tra Sâu)"
    log(f"=== Bắt đầu đồng bộ phân hệ: {module_name} [{mode_text}] ===")
    
    # 1. Sync Master Excel File
    if excel_remote and os.path.exists(excel_remote):
        try:
            remote_mtime = os.path.getmtime(excel_remote)
            remote_size = os.path.getsize(excel_remote)
            local_excel_path = resolve_master_excel_path(local_subfolder_rel, excel_local_name, module_storage_root)
            os.makedirs(to_long_path(os.path.dirname(local_excel_path)), exist_ok=True)
            
            need_download = True
            if is_file_exists(local_excel_path):
                local_size = os.path.getsize(to_long_path(local_excel_path))
                local_mtime = os.path.getmtime(to_long_path(local_excel_path))
                if local_size == remote_size and abs(local_mtime - remote_mtime) < 2:
                    need_download = False
                    
            if need_download:
                log(f"Đang tải file Excel tổng: {excel_local_name}")
                shutil.copy2(to_long_path(excel_remote), to_long_path(local_excel_path))
                stats['master_excel_updated'] = True
            else:
                log(f"File Excel tổng không đổi: {excel_local_name} (Bỏ qua)")
        except Exception as e:
            log(f"Lỗi khi copy Excel tổng: {e}")
            stats['errors'] += 1
            
    # 2. Scan remote directories for Vietnamese PDFs
    log("Đang quét danh mục file trên máy chủ...")
    remote_pdf_candidates = []
    remote_code_map = {} # doc_code -> list of remote_paths
    
    for root_scan in remote_scan_roots:
        if not os.path.exists(root_scan):
            log(f"Cảnh báo: Thư mục nguồn không truy cập được: {root_scan}")
            continue
            
        for root, dirs, files in os.walk(root_scan):
            for f in files:
                if not f.lower().endswith('.pdf'):
                    continue
                full_p = os.path.join(root, f)
                
                # Filter out Japanese
                if is_japanese_path_or_file(f, full_p):
                    continue
                    
                if is_vietnamese_pdf(f, full_p):
                    remote_pdf_candidates.append((full_p, root_scan, root, f))
                    code = extract_doc_code(f)
                    if code not in remote_code_map:
                        remote_code_map[code] = []
                    remote_code_map[code].append(full_p)
                    
    stats['total_scanned'] = len(remote_pdf_candidates)
    log(f"Tìm thấy {len(remote_pdf_candidates)} file PDF tiếng Việt/hợp lệ.")
    
    # 3. Incremental Download & Link Restoration
    idx = 0
    for full_remote_path, root_scan, root, filename in remote_pdf_candidates:
        idx += 1
        try:
            r_mtime = os.path.getmtime(full_remote_path)
            r_size = os.path.getsize(full_remote_path)
            
            # Determine sanitized relative destination folder
            rel_dir = os.path.relpath(root, root_scan)
            if rel_dir == '.':
                target_dir_rel = ""
            else:
                # Sanitize folder path parts
                parts = rel_dir.split(os.sep)
                clean_parts = [sanitize_ascii_name(p) for p in parts]
                # Filter empty parts
                clean_parts = [p for p in clean_parts if p]
                target_dir_rel = os.path.join(*clean_parts) if clean_parts else ""
                
            clean_filename = sanitize_ascii_name(filename)
            # Ensure extension .pdf
            if not clean_filename.lower().endswith('.pdf'):
                clean_filename += ".pdf"
                
            dest_dir = os.path.join(local_subfolder_abs, target_dir_rel)
            long_dest_dir = to_long_path(dest_dir)
            os.makedirs(long_dest_dir, exist_ok=True)
            local_file_path = os.path.join(dest_dir, clean_filename)
            long_local_path = to_long_path(local_file_path)
            long_remote_path = to_long_path(full_remote_path)
            
            # Check if canceled
            canceled = is_canceled_item(filename, full_remote_path)
            doc_code = extract_doc_code(filename)
            
            # Check incremental state
            cached_info = sync_state.get(full_remote_path)
            need_copy = True
            
            if cached_info and os.path.exists(long_local_path):
                c_size = cached_info.get('size')
                c_mtime = cached_info.get('mtime')
                local_act_size = os.path.getsize(long_local_path)
                if local_act_size == r_size and abs(c_mtime - r_mtime) < 2:
                    need_copy = False
                    stats['skipped'] += 1
            elif os.path.exists(long_local_path):
                # File exists locally with exact same size and close mtime
                local_act_size = os.path.getsize(long_local_path)
                local_act_mtime = os.path.getmtime(long_local_path)
                if local_act_size == r_size and abs(local_act_mtime - r_mtime) < 2:
                    need_copy = False
                    stats['skipped'] += 1
                    
            if need_copy:
                shutil.copy2(long_remote_path, long_local_path)
                stats['downloaded'] += 1
                if canceled:
                    stats['restored_links'] += 1
                if stats['downloaded'] % 50 == 0 or stats['downloaded'] <= 5:
                    log(f"[{idx}/{len(remote_pdf_candidates)}] Tải mới: {clean_filename} ({r_size/1024:.0f} KB)")
                    
            # Record in sync_state (relative to global storage_root if inside it, else absolute)
            sync_state[full_remote_path] = {
                'local_path': to_storage_rel_or_abs(local_file_path, global_storage_root),
                'clean_filename': clean_filename,
                'doc_code': doc_code,
                'mtime': r_mtime,
                'size': r_size,
                'is_canceled': canceled,
                'last_updated': datetime.now().isoformat()
            }
        except Exception as e:
            stats['errors'] += 1
            log(f"Lỗi khi xử lý file {filename}: {e}")
            
    # Update config
    cfg['last_sync_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cfg['sync_state'] = sync_state
    save_module_config(cfg_path, cfg)
    
    log(f"Hoàn thành {module_name}: Quét {stats['total_scanned']}, Tải mới {stats['downloaded']}, Bỏ qua {stats['skipped']}, Lỗi {stats['errors']}.")
    return stats

def rebuild_consolidated_catalog() -> list:
    """
    Read all configs and build tailieu_catalog.json for instant search in UI.
    Preserves previously enriched metadata (doc_title, summary, pillar, etc.) if present.
    """
    storage_root = get_storage_root()
    prev_meta = {}
    if os.path.exists(CATALOG_PATH):
        try:
            with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
                for old_item in json.load(f):
                    key = (old_item.get('module_id', ''), old_item.get('remote_path', ''))
                    prev_meta[key] = old_item
        except Exception:
            pass

    enrich_fields = (
        'doc_title', 'summary', 'so_huu', 'pillar', 'icon',
        'is_master_root', 'doc_tier', 'parent_ref', 'search_text'
    )

    catalog = []
    cfg_files = sorted([f for f in os.listdir(CONFIGS_DIR) if f.endswith('.json')])
    
    for fname in cfg_files:
        cfg_path = os.path.join(CONFIGS_DIR, fname)
        try:
            cfg = load_module_config(cfg_path)
            module_id = cfg.get('id')
            module_name = cfg.get('name')
            sync_state = cfg.get('sync_state', {})
            excel_local_name = cfg.get('excel_local_name')
            local_subfolder = cfg.get('local_subfolder')
            
            excel_rel_path = os.path.join(local_subfolder, excel_local_name) if excel_local_name else ""
            excel_remote_path = cfg.get('excel_remote', '')
            
            for remote_p, info in sync_state.items():
                local_p = info.get('local_path', '')
                full_local = resolve_local_path(local_p, storage_root)
                file_exists = is_file_exists(full_local)
                
                doc_entry = {
                    'module_id': module_id,
                    'module_name': module_name,
                    'doc_code': info.get('doc_code', ''),
                    'filename': info.get('clean_filename', os.path.basename(local_p)),
                    'local_path': local_p,
                    'remote_path': remote_p,
                    'is_canceled': info.get('is_canceled', False),
                    'status': 'Đã Hủy Bỏ (Đã Bổ Sung Link)' if info.get('is_canceled') else 'Đang Hiệu Lực',
                    'size': info.get('size', 0),
                    'mtime': info.get('mtime', 0),
                    'file_exists': file_exists,
                    'master_excel_local': excel_rel_path,
                    'master_excel_remote': excel_remote_path
                }
                old_rec = prev_meta.get((module_id, remote_p))
                if old_rec:
                    for fld in enrich_fields:
                        if fld in old_rec:
                            doc_entry[fld] = old_rec[fld]
                catalog.append(doc_entry)
        except Exception as e:
            print(f"Error loading {fname}: {e}")
            
    atomic_write_json(CATALOG_PATH, catalog)
    return catalog

def sync_all_modules(selected_ids=None, mode='fast', progress_callback=None) -> dict:
    """
    Sync all or selected modules.
    mode='fast': Fast incremental.
    mode='full': Full re-check.
    """
    cfg_files = sorted([f for f in os.listdir(CONFIGS_DIR) if f.endswith('.json')])
    overall_stats = {}
    
    for fname in cfg_files:
        cfg_path = os.path.join(CONFIGS_DIR, fname)
        cfg = load_module_config(cfg_path)
        mod_id = cfg.get('id')
        
        if selected_ids and mod_id not in selected_ids:
            continue
            
        stats = sync_single_module(cfg_path, mode=mode, progress_callback=progress_callback)
        overall_stats[mod_id] = stats
        
    rebuild_consolidated_catalog()
    try:
        from governance_matrix import build_governance_matrix
        build_governance_matrix()
    except Exception as e:
        print(f"Notice: governance matrix rebuild: {e}")
    return overall_stats

if __name__ == '__main__':
    print("Testing sync_engine directly...")
    # Test with module 06_nvkho first (small, 34 files)
    test_cfg = os.path.join(CONFIGS_DIR, '06_nvkho.json')
    if os.path.exists(test_cfg):
        st = sync_single_module(test_cfg)
        print("Test Result:", st)
        cat = rebuild_consolidated_catalog()
        print(f"Catalog contains {len(cat)} items.")
