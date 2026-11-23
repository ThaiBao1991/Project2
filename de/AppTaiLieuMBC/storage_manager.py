import os
import sys
import json
import shutil
import ctypes
from ctypes import wintypes
from datetime import datetime

# Ensure UTF-8 output on Windows console
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')
CATALOG_PATH = os.path.join(BASE_DIR, 'tailieu_catalog.json')
GOVERNANCE_PATH = os.path.join(BASE_DIR, 'governance_catalog.json')
SETTINGS_PATH = os.path.join(BASE_DIR, 'app_settings.json')
MASTER_EXCELS_DIR = os.path.join(BASE_DIR, 'master_excels')


def get_paths(base_dir: str = None) -> dict:
    """Return all app/data paths anchored at base_dir (defaults to BASE_DIR)."""
    b = os.path.abspath(base_dir) if base_dir else BASE_DIR
    return {
        'base': b,
        'configs': os.path.join(b, 'configs'),
        'catalog': os.path.join(b, 'tailieu_catalog.json'),
        'governance': os.path.join(b, 'governance_catalog.json'),
        'settings': os.path.join(b, 'app_settings.json'),
        'master_excels': os.path.join(b, 'master_excels'),
    }


def to_long_path(p: str) -> str:
    """Handle Windows MAX_PATH limit (>260 chars)."""
    if sys.platform != 'win32' or not p:
        return p
    if p.startswith('\\\\?\\'):
        return p
    abs_p = os.path.abspath(p)
    if abs_p.startswith('\\\\?\\'):
        return abs_p
    if abs_p.startswith('\\\\'):
        return '\\\\?\\UNC\\' + abs_p[2:]
    return '\\\\?\\' + abs_p


def strip_long_prefix(p: str) -> str:
    """Strip Windows \\\\?\\ prefix for display or APIs that reject it."""
    if not p:
        return ''
    if p.startswith('\\\\?\\UNC\\'):
        return '\\\\' + p[8:]
    if p.startswith('\\\\?\\'):
        return p[4:]
    return p


def path_exists(p: str) -> bool:
    if not p:
        return False
    try:
        return os.path.exists(to_long_path(p))
    except OSError:
        return False


def is_file_exists(p: str) -> bool:
    if not p:
        return False
    try:
        return os.path.isfile(to_long_path(p))
    except OSError:
        return False


def atomic_write_json(path: str, data):
    """Write JSON atomically via a temporary file to prevent corruption."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(to_long_path(parent), exist_ok=True)
    tmp_path = path + '.tmp'
    with open(to_long_path(tmp_path), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.flush()
        try:
            os.fsync(f.fileno())
        except OSError:
            pass
    os.replace(to_long_path(tmp_path), to_long_path(path))


def _load_json(path: str, default):
    if not is_file_exists(path):
        return default
    try:
        with open(to_long_path(path), 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return default


# =========================================================================
# APP SETTINGS & STORAGE ROOT RESOLUTION
# =========================================================================

def load_app_settings(base_dir: str = None) -> dict:
    paths = get_paths(base_dir)
    data = _load_json(paths['settings'], {})
    if not isinstance(data, dict):
        data = {}
    data.setdefault('storage_root', '')
    data.setdefault('keep_excel_in_app', True)
    data.setdefault('last_updated', '')
    data.setdefault('history', [])
    return data


def save_app_settings(settings: dict, base_dir: str = None):
    paths = get_paths(base_dir)
    settings['last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    atomic_write_json(paths['settings'], settings)


def get_storage_root(base_dir: str = None) -> str:
    """Return active root folder where PDFs are stored (defaults to BASE_DIR)."""
    paths = get_paths(base_dir)
    settings = load_app_settings(base_dir)
    raw = (settings.get('storage_root') or '').strip()
    if raw:
        return os.path.normpath(os.path.abspath(raw))
    return os.path.normpath(paths['base'])


def is_custom_storage_root(base_dir: str = None) -> bool:
    paths = get_paths(base_dir)
    root = get_storage_root(base_dir)
    return os.path.normcase(os.path.abspath(root)) != os.path.normcase(os.path.abspath(paths['base']))


def set_storage_root(new_root: str, note: str = '', keep_excel_in_app: bool = None, base_dir: str = None) -> dict:
    """Persist new storage_root in app_settings.json."""
    paths = get_paths(base_dir)
    settings = load_app_settings(base_dir)
    old_root = get_storage_root(base_dir)
    norm_new = os.path.normpath(os.path.abspath(new_root)) if new_root else paths['base']

    if os.path.normcase(norm_new) == os.path.normcase(paths['base']):
        settings['storage_root'] = ''
    else:
        settings['storage_root'] = norm_new

    if keep_excel_in_app is not None:
        settings['keep_excel_in_app'] = bool(keep_excel_in_app)

    hist = settings.get('history', [])
    if not isinstance(hist, list):
        hist = []
    hist.append({
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'from': old_root,
        'to': norm_new,
        'note': note
    })
    settings['history'] = hist[-20:]
    save_app_settings(settings, base_dir)
    return settings


def _is_subpath(child: str, parent: str) -> bool:
    """Return True if child equals parent or is located inside parent."""
    try:
        c = os.path.normcase(os.path.abspath(strip_long_prefix(child)))
        p = os.path.normcase(os.path.abspath(strip_long_prefix(parent)))
        return os.path.commonpath([c, p]) == p
    except ValueError:
        return False


def resolve_local_path(local_path: str, storage_root: str = None, base_dir: str = None) -> str:
    """
    Resolve a document's local_path (relative or absolute) to a normalized absolute path.
    - If local_path is absolute: returned normalized directly.
    - If local_path is relative: joined against storage_root (or get_storage_root()).
    """
    if not local_path:
        return ''
    cleaned = str(local_path).strip()
    if not cleaned:
        return ''
    if os.path.isabs(cleaned):
        return os.path.normpath(cleaned)
    root = os.path.abspath(storage_root) if storage_root else get_storage_root(base_dir)
    return os.path.normpath(os.path.join(root, cleaned))


def to_storage_rel_or_abs(abs_path: str, storage_root: str = None, base_dir: str = None) -> str:
    """
    Store path relative to storage_root if inside it (keeps catalog portable),
    otherwise store normalized absolute path.
    """
    if not abs_path:
        return ''
    norm_abs = os.path.normpath(os.path.abspath(strip_long_prefix(abs_path)))
    root = os.path.normpath(os.path.abspath(storage_root)) if storage_root else get_storage_root(base_dir)
    if _is_subpath(norm_abs, root):
        rel = os.path.relpath(norm_abs, root)
        if rel != '.':
            return rel
    return norm_abs


def resolve_master_excel_path(local_subfolder: str, excel_local_name: str,
                              storage_root: str = None, base_dir: str = None) -> str:
    """
    Locate a module's Master Excel file seamlessly across:
      1. storage_root / local_subfolder / excel_local_name
      2. BASE_DIR / master_excels / excel_local_name
      3. BASE_DIR / local_subfolder / excel_local_name
    Returns the first existing path, or the preferred default path if none exists.
    """
    if not excel_local_name:
        return ''
    paths = get_paths(base_dir)
    root = os.path.normpath(os.path.abspath(storage_root)) if storage_root else get_storage_root(base_dir)
    sub = local_subfolder or ''

    candidates = [
        os.path.normpath(os.path.join(root, sub, excel_local_name)),
        os.path.normpath(os.path.join(paths['master_excels'], excel_local_name)),
        os.path.normpath(os.path.join(paths['base'], sub, excel_local_name)),
    ]
    seen = set()
    unique_cands = []
    for c in candidates:
        nc = os.path.normcase(c)
        if nc not in seen:
            seen.add(nc)
            unique_cands.append(c)

    for c in unique_cands:
        if is_file_exists(c):
            return c

    settings = load_app_settings(base_dir)
    if settings.get('keep_excel_in_app', True) and is_custom_storage_root(base_dir):
        return os.path.normpath(os.path.join(paths['master_excels'], excel_local_name))
    return unique_cands[0]


def get_module_storage_root(cfg: dict, base_dir: str = None) -> str:
    """Return effective root directory for a specific module config."""
    custom = (cfg.get('custom_storage_root') or '').strip()
    if custom:
        return os.path.normpath(os.path.abspath(custom))
    return get_storage_root(base_dir)


# =========================================================================
# CONFIG & CATALOG HELPERS
# =========================================================================

def _load_all_configs(base_dir: str = None) -> list:
    """Return list of (cfg_path, cfg_dict) sorted by filename."""
    paths = get_paths(base_dir)
    res = []
    if not path_exists(paths['configs']):
        return res
    for fname in sorted(os.listdir(to_long_path(paths['configs']))):
        if fname.endswith('.json'):
            p = os.path.join(paths['configs'], fname)
            cfg = _load_json(p, None)
            if isinstance(cfg, dict):
                res.append((p, cfg))
    return res


def get_storage_summary(base_dir: str = None) -> dict:
    """Compute storage statistics (file count, existing count, size per module)."""
    paths = get_paths(base_dir)
    storage_root = get_storage_root(base_dir)
    catalog = _load_json(paths['catalog'], [])

    total_docs = len(catalog)
    existing_docs = 0
    missing_docs = 0
    total_bytes = 0
    custom_path_docs = 0
    per_module = {}

    for doc in catalog:
        mod_id = doc.get('module_id', 'unknown')
        mod_name = doc.get('module_name', mod_id)
        if mod_id not in per_module:
            per_module[mod_id] = {
                'id': mod_id,
                'name': mod_name,
                'total': 0,
                'existing': 0,
                'missing': 0,
                'canceled': 0,
                'canceled_existing': 0,
                'bytes': 0,
            }
        m = per_module[mod_id]
        m['total'] += 1
        lp = doc.get('local_path', '')
        if lp and os.path.isabs(lp):
            custom_path_docs += 1
        full_p = resolve_local_path(lp, storage_root, base_dir)
        exists = is_file_exists(full_p)
        if exists:
            existing_docs += 1
            m['existing'] += 1
            try:
                sz = os.path.getsize(to_long_path(full_p))
            except OSError:
                sz = doc.get('size', 0) or 0
            total_bytes += sz
            m['bytes'] += sz
            if doc.get('is_canceled'):
                m['canceled_existing'] += 1
        else:
            missing_docs += 1
            m['missing'] += 1
        if doc.get('is_canceled'):
            m['canceled'] += 1

    # Count master excels
    excel_count = 0
    excel_bytes = 0
    for _, cfg in _load_all_configs(base_dir):
        ep = resolve_master_excel_path(cfg.get('local_subfolder', ''), cfg.get('excel_local_name', ''),
                                       storage_root, base_dir)
        if is_file_exists(ep):
            excel_count += 1
            try:
                excel_bytes += os.path.getsize(to_long_path(ep))
            except OSError:
                pass

    return {
        'app_dir': paths['base'],
        'storage_root': storage_root,
        'is_separated': is_custom_storage_root(base_dir),
        'total_docs': total_docs,
        'existing_docs': existing_docs,
        'missing_docs': missing_docs,
        'custom_path_docs': custom_path_docs,
        'total_bytes': total_bytes,
        'excel_count': excel_count,
        'excel_bytes': excel_bytes,
        'modules': list(per_module.values()),
    }


# =========================================================================
# SAFE FILE MOVE / COPY / DELETE / RECYCLE BIN
# =========================================================================

def _safe_move_file(src_abs: str, dst_abs: str, copy_only: bool = False) -> tuple:
    """
    Safely move or copy a single file with Windows long-path support and size verification.
    Never deletes source unless destination is verified on disk.
    Returns (ok: bool, status: str)
    """
    src_norm = os.path.normpath(os.path.abspath(strip_long_prefix(src_abs)))
    dst_norm = os.path.normpath(os.path.abspath(strip_long_prefix(dst_abs)))

    if os.path.normcase(src_norm) == os.path.normcase(dst_norm):
        return True, 'same_path'

    long_src = to_long_path(src_norm)
    long_dst = to_long_path(dst_norm)

    if not os.path.isfile(long_src):
        return False, f'Không tìm thấy file nguồn: {src_norm}'

    dst_parent = os.path.dirname(dst_norm)
    if dst_parent:
        os.makedirs(to_long_path(dst_parent), exist_ok=True)

    src_size = os.path.getsize(long_src)

    # Fast path: atomic rename on same filesystem when moving
    if not copy_only:
        try:
            if not os.path.exists(long_dst):
                os.replace(long_src, long_dst)
                if os.path.isfile(long_dst) and os.path.getsize(long_dst) == src_size:
                    return True, 'moved'
        except OSError:
            # Cross-device move (EXDEV) or locked destination -> fall back to copy-verify-delete
            pass

    tmp_dst = to_long_path(dst_norm + '.moving_tmp')
    try:
        shutil.copy2(long_src, tmp_dst)
        if not os.path.isfile(tmp_dst) or os.path.getsize(tmp_dst) != src_size:
            raise IOError('Kích thước file sau khi sao chép không khớp với file gốc')
        os.replace(tmp_dst, long_dst)

        if not os.path.isfile(long_dst) or os.path.getsize(long_dst) != src_size:
            raise IOError('Xác minh file tại thư mục đích thất bại')

        if not copy_only:
            os.remove(long_src)
            return True, 'moved'
        return True, 'copied'
    except Exception as e:
        try:
            if os.path.exists(tmp_dst):
                os.remove(tmp_dst)
        except OSError:
            pass
        return False, str(e)


def _send_to_recycle_bin_win32(abs_path: str) -> tuple:
    """Send a file to Windows Recycle Bin using pywin32 or ctypes SHFileOperationW."""
    norm = os.path.normpath(os.path.abspath(strip_long_prefix(abs_path)))
    if len(norm) >= 255:
        return False, 'path_too_long_for_recycle_bin'

    # Prefer pywin32 shell if installed (handles 32/64-bit struct packing natively)
    try:
        from win32com.shell import shell, shellcon
        flags = shellcon.FOF_ALLOWUNDO | shellcon.FOF_NOCONFIRMATION | shellcon.FOF_SILENT | shellcon.FOF_NOERRORUI
        ret, aborted = shell.SHFileOperation((0, shellcon.FO_DELETE, norm, None, flags, None, None))
        if ret == 0 and not aborted and not path_exists(norm):
            return True, 'recycled'
        return False, f'SHFileOperation code={ret}, aborted={aborted}'
    except ImportError:
        pass
    except Exception as e:
        return False, str(e)

    # Fallback: ctypes SHFileOperationW
    try:
        FO_DELETE = 0x0003
        FOF_SILENT = 0x0004
        FOF_NOCONFIRMATION = 0x0010
        FOF_ALLOWUNDO = 0x0040
        FOF_NOERRORUI = 0x0400

        class SHFILEOPSTRUCTW(ctypes.Structure):
            if ctypes.sizeof(ctypes.c_void_p) == 4:
                _pack_ = 1
            _fields_ = [
                ('hwnd', wintypes.HWND),
                ('wFunc', wintypes.UINT),
                ('pFrom', wintypes.LPCWSTR),
                ('pTo', wintypes.LPCWSTR),
                ('fFlags', wintypes.WORD),
                ('fAnyOperationsAborted', wintypes.BOOL),
                ('hNameMappings', wintypes.LPVOID),
                ('lpszProgressTitle', wintypes.LPCWSTR),
            ]

        buf = ctypes.create_unicode_buffer(norm + '\0')
        op = SHFILEOPSTRUCTW()
        op.hwnd = None
        op.wFunc = FO_DELETE
        op.pFrom = ctypes.cast(buf, wintypes.LPCWSTR)
        op.pTo = None
        op.fFlags = FOF_ALLOWUNDO | FOF_NOCONFIRMATION | FOF_SILENT | FOF_NOERRORUI
        op.fAnyOperationsAborted = False
        op.hNameMappings = None
        op.lpszProgressTitle = None

        ret = ctypes.windll.shell32.SHFileOperationW(ctypes.byref(op))
        if ret == 0 and not op.fAnyOperationsAborted and not path_exists(norm):
            return True, 'recycled'
        return False, f'SHFileOperationW code={ret}'
    except Exception as e:
        return False, str(e)


def delete_file_safe(abs_path: str, use_recycle_bin: bool = True, allow_long_fallback: bool = True) -> tuple:
    """
    Safely delete a file. Uses Windows Recycle Bin when use_recycle_bin=True.
    Returns (ok: bool, method: str, detail: str).
    """
    if not abs_path:
        return False, 'invalid', 'Đường dẫn rỗng'
    norm = os.path.normpath(os.path.abspath(strip_long_prefix(abs_path)))
    long_p = to_long_path(norm)
    if not os.path.exists(long_p):
        return True, 'not_found', 'File không tồn tại trên ổ cứng'

    if use_recycle_bin and sys.platform == 'win32':
        ok, info = _send_to_recycle_bin_win32(norm)
        if ok:
            return True, 'recycled', ''
        if info == 'path_too_long_for_recycle_bin' and allow_long_fallback:
            try:
                os.remove(long_p)
                return True, 'deleted_permanent_longpath', 'Đường dẫn > 255 ký tự, đã xóa trực tiếp'
            except Exception as e:
                return False, 'error', str(e)
        return False, 'recycle_failed', info

    try:
        os.remove(long_p)
        return True, 'deleted_permanent', ''
    except Exception as e:
        return False, 'error', str(e)


def cleanup_empty_dirs(target_dirs: list, protected_dirs: list = None) -> int:
    """Remove completely empty subdirectories bottom-up and prune empty parents up to protected_dirs."""
    protected = set()
    for pd in (protected_dirs or []):
        if pd:
            protected.add(os.path.normcase(os.path.abspath(strip_long_prefix(pd))))

    removed = 0
    ancestor_candidates = set()
    for d in target_dirs:
        if not d:
            continue
        norm_d = os.path.normpath(os.path.abspath(strip_long_prefix(d)))
        if not path_exists(norm_d):
            continue
        for root, dirs, files in os.walk(to_long_path(norm_d), topdown=False):
            clean_root = strip_long_prefix(root)
            if os.path.normcase(os.path.abspath(clean_root)) in protected:
                continue
            try:
                if not os.listdir(root):
                    os.rmdir(root)
                    removed += 1
                    ancestor_candidates.add(os.path.dirname(clean_root))
            except OSError:
                pass

    # Walk upward from removed leaf dirs to prune empty parent chains safely
    for anc in ancestor_candidates:
        cur = anc
        while cur:
            norm_cur = os.path.normcase(os.path.abspath(cur))
            if norm_cur in protected:
                break
            parent = os.path.dirname(cur)
            if not parent or os.path.normcase(parent) == norm_cur:
                break
            try:
                if path_exists(cur) and not os.listdir(to_long_path(cur)):
                    os.rmdir(to_long_path(cur))
                    removed += 1
                    cur = parent
                else:
                    break
            except OSError:
                break
    return removed


def _make_unique_path(dst_abs: str) -> str:
    """If dst_abs already exists, append _1, _2, ... before extension."""
    if not path_exists(dst_abs):
        return dst_abs
    base, ext = os.path.splitext(dst_abs)
    i = 1
    while True:
        cand = f'{base}_{i}{ext}'
        if not path_exists(cand):
            return cand
        i += 1


def _doc_key(doc: dict) -> tuple:
    return (doc.get('module_id', ''), doc.get('remote_path', ''))


# =========================================================================
# FEATURE 1: MOVE ALL / SELECTED MODULES STORAGE & AUTO-RELINK
# =========================================================================

def move_all_documents(
    dest_root: str,
    module_ids: list = None,
    include_excels: bool = False,
    keep_excel_in_app: bool = True,
    copy_only: bool = False,
    cleanup_empty: bool = True,
    progress_callback=None,
    cancel_event=None,
    base_dir: str = None,
) -> dict:
    """
    Move (or copy) all documents or selected modules' documents to dest_root,
    automatically updating app_settings.json, configs/*.json, tailieu_catalog.json,
    and governance_catalog.json while preserving 100% of enriched metadata.
    """
    def log(msg, pct=None):
        if progress_callback:
            progress_callback(msg, pct)

    paths = get_paths(base_dir)
    old_root = get_storage_root(base_dir)
    dest_root_norm = os.path.normpath(os.path.abspath(dest_root))

    configs = _load_all_configs(base_dir)
    all_mod_ids = [cfg.get('id') for _, cfg in configs]
    if module_ids is None or len(module_ids) == 0:
        selected_mod_ids = set(all_mod_ids)
    else:
        selected_mod_ids = set(module_ids)
    is_full_move = (selected_mod_ids == set(all_mod_ids))

    stats = {
        'ok': False,
        'cancelled': False,
        'is_full_move': is_full_move,
        'old_root': old_root,
        'dest_root': dest_root_norm,
        'total_docs': 0,
        'moved': 0,
        'skipped_same': 0,
        'missing_src': 0,
        'excels_moved': 0,
        'errors': 0,
        'error_details': [],
        'bytes_moved': 0,
        'empty_dirs_removed': 0,
    }

    # --- Pre-flight validation ---
    if not dest_root or not dest_root.strip():
        stats['error_details'].append('Chưa chọn thư mục đích.')
        return stats

    if is_full_move and os.path.normcase(dest_root_norm) == os.path.normcase(old_root):
        stats['error_details'].append('Thư mục đích trùng với kho lưu trữ hiện tại.')
        return stats

    # Prevent moving into one of the source document subfolders
    for _, cfg in configs:
        if cfg.get('id') not in selected_mod_ids:
            continue
        sub = cfg.get('local_subfolder', '')
        if sub:
            src_sub = os.path.normpath(os.path.join(old_root, sub))
            if _is_subpath(dest_root_norm, src_sub):
                stats['error_details'].append(
                    f'Thư mục đích không được nằm bên trong thư mục tài liệu nguồn ({src_sub}).'
                )
                return stats

    # Create destination directory & test write permission
    try:
        os.makedirs(to_long_path(dest_root_norm), exist_ok=True)
        test_file = os.path.join(dest_root_norm, '.tailieu_write_test.tmp')
        with open(to_long_path(test_file), 'w', encoding='utf-8') as tf:
            tf.write('ok')
        os.remove(to_long_path(test_file))
    except Exception as e:
        stats['error_details'].append(f'Không thể ghi vào thư mục đích ({dest_root_norm}): {e}')
        return stats

    catalog = _load_json(paths['catalog'], [])
    governance = _load_json(paths['governance'], [])
    cfg_by_mod = {cfg.get('id'): (cp, cfg) for cp, cfg in configs}

    # Identify unique physical source files and compute required space
    target_docs = [d for d in catalog if d.get('module_id') in selected_mod_ids]
    stats['total_docs'] = len(target_docs)

    # Plan physical file moves: normcase(src_abs) -> (src_abs, dst_abs, target_rel, docs_list)
    move_plan = {}
    missing_keys = set()
    needed_bytes = 0
    same_drive = (
        os.path.splitdrive(os.path.abspath(old_root))[0].lower()
        == os.path.splitdrive(os.path.abspath(dest_root_norm))[0].lower()
    )

    for doc in target_docs:
        mod_id = doc.get('module_id', '')
        lp = doc.get('local_path', '')
        if not lp:
            missing_keys.add(_doc_key(doc))
            continue

        src_abs = resolve_local_path(lp, old_root, base_dir)
        if not is_file_exists(src_abs):
            missing_keys.add(_doc_key(doc))
            continue

        # Determine target relative path inside dest_root
        if not os.path.isabs(lp):
            rel_in_dest = os.path.normpath(lp)
        elif _is_subpath(src_abs, old_root):
            rel_in_dest = os.path.relpath(src_abs, old_root)
        else:
            mod_sub = cfg_by_mod.get(mod_id, (None, {}))[1].get('local_subfolder', mod_id)
            rel_in_dest = os.path.normpath(os.path.join(mod_sub, os.path.basename(src_abs)))

        dst_abs = os.path.normpath(os.path.join(dest_root_norm, rel_in_dest))
        src_key = os.path.normcase(os.path.abspath(src_abs))

        if src_key not in move_plan:
            try:
                sz = os.path.getsize(to_long_path(src_abs))
            except OSError:
                sz = 0
            needed_bytes += sz
            move_plan[src_key] = {
                'src_abs': src_abs,
                'dst_abs': dst_abs,
                'rel_in_dest': rel_in_dest,
                'size': sz,
                'docs': [doc],
            }
        else:
            move_plan[src_key]['docs'].append(doc)

    stats['missing_src'] = len(missing_keys)

    # Check free disk space when copying or moving across different drives
    if copy_only or not same_drive:
        try:
            free_bytes = shutil.disk_usage(dest_root_norm).free
            # Keep a small 50 MB safety buffer
            if free_bytes < needed_bytes + 50 * 1024 * 1024:
                stats['error_details'].append(
                    f'Ổ đĩa đích không đủ dung lượng trống! Cần {needed_bytes / (1024**2):.1f} MB, '
                    f'chỉ còn {free_bytes / (1024**2):.1f} MB.'
                )
                return stats
        except OSError:
            pass

    action_label = 'Sao chép' if copy_only else 'Di chuyển'
    log(
        f'🚚 Bắt đầu {action_label.lower()} {len(move_plan):,} file PDF '
        f'({needed_bytes / (1024**2):.1f} MB) → {dest_root_norm}',
        0.02,
    )

    # --- Execute file transfers ---
    moved_map = {}  # (module_id, remote_path) -> new_abs
    failed_map = {}  # (module_id, remote_path) -> old_abs
    total_files = max(len(move_plan), 1)
    source_top_dirs = set()

    for idx, entry in enumerate(move_plan.values(), 1):
        if cancel_event and cancel_event.is_set():
            stats['cancelled'] = True
            log('⏹ Đã nhận yêu cầu dừng an toàn. Đang lưu cập nhật link cho các file đã xử lý...', None)
            break

        src_abs = entry['src_abs']
        dst_abs = entry['dst_abs']
        ok, status = _safe_move_file(src_abs, dst_abs, copy_only=copy_only)

        if ok:
            if status == 'same_path':
                stats['skipped_same'] += 1
            else:
                stats['moved'] += 1
                stats['bytes_moved'] += entry['size']
            for d in entry['docs']:
                moved_map[_doc_key(d)] = dst_abs
            # Track source folder for empty cleanup
            if _is_subpath(src_abs, old_root):
                rel_p = os.path.relpath(src_abs, old_root)
                top = rel_p.split(os.sep)[0]
                if top and top != '.':
                    source_top_dirs.add(os.path.join(old_root, top))
        else:
            stats['errors'] += 1
            err_msg = f'{os.path.basename(src_abs)}: {status}'
            if len(stats['error_details']) < 50:
                stats['error_details'].append(err_msg)
            log(f'⚠️ Lỗi {action_label.lower()}: {err_msg}', None)
            for d in entry['docs']:
                failed_map[_doc_key(d)] = src_abs

        if idx % 50 == 0 or idx == len(move_plan) or idx <= 3:
            pct = 0.05 + 0.80 * (idx / total_files)
            log(f'[{idx:,}/{len(move_plan):,}] {action_label}: {os.path.basename(dst_abs)}', pct)

    # --- Handle 8 Master Excel files (only if not cancelled) ---
    if not stats['cancelled']:
        for mod_id in selected_mod_ids:
            pair = cfg_by_mod.get(mod_id)
            if not pair:
                continue
            _, cfg = pair
            excel_name = cfg.get('excel_local_name', '')
            sub = cfg.get('local_subfolder', '')
            if not excel_name:
                continue
            src_excel = resolve_master_excel_path(sub, excel_name, old_root, base_dir)
            if not is_file_exists(src_excel):
                continue

            if include_excels:
                dst_excel = os.path.normpath(os.path.join(dest_root_norm, sub, excel_name))
                ok_ex, st_ex = _safe_move_file(src_excel, dst_excel, copy_only=copy_only)
                if ok_ex and st_ex != 'same_path':
                    stats['excels_moved'] += 1
                    log(f'📊 Đã {action_label.lower()} Excel tổng: {excel_name}', None)
                if _is_subpath(src_excel, old_root):
                    top = os.path.relpath(src_excel, old_root).split(os.sep)[0]
                    if top and top != '.':
                        source_top_dirs.add(os.path.join(old_root, top))
            elif keep_excel_in_app and not copy_only and is_full_move:
                # Consolidate Master Excels cleanly into BASE_DIR/master_excels/
                # so the 3 PDF folders in BASE_DIR can be completely cleaned up!
                dst_excel = os.path.normpath(os.path.join(paths['master_excels'], excel_name))
                if os.path.normcase(src_excel) != os.path.normcase(dst_excel):
                    ok_ex, st_ex = _safe_move_file(src_excel, dst_excel, copy_only=False)
                    if ok_ex:
                        log(f'📊 Đã gom gọn Excel tổng về App/master_excels/: {excel_name}', None)
                    if _is_subpath(src_excel, old_root):
                        top = os.path.relpath(src_excel, old_root).split(os.sep)[0]
                        if top and top != '.':
                            source_top_dirs.add(os.path.join(old_root, top))

    # --- Determine new global storage_root and update ALL JSON links ---
    log('🔗 Đang cập nhật liên kết trong cấu hình, Catalog và Ma Trận Quản Trị...', 0.90)

    # Only switch global storage_root if this was a full move and NOT cancelled partway
    switched_global_root = is_full_move and not stats['cancelled']
    effective_root = dest_root_norm if switched_global_root else old_root

    if switched_global_root:
        set_storage_root(
            dest_root_norm,
            note=f'{action_label} toàn bộ kho ({stats["moved"]} PDF)',
            keep_excel_in_app=(not include_excels and keep_excel_in_app),
            base_dir=base_dir,
        )

    # Track remote_path -> new_stored_local_path for governance update
    remote_to_new_lp = {}
    old_lp_to_new_lp = {}

    # Update configs/*.json
    for cfg_path, cfg in configs:
        mod_id = cfg.get('id')
        changed_cfg = False
        if switched_global_root and cfg.get('custom_storage_root'):
            cfg['custom_storage_root'] = ''
            changed_cfg = True
        elif not is_full_move and not stats['cancelled'] and mod_id in selected_mod_ids:
            cfg['custom_storage_root'] = dest_root_norm
            changed_cfg = True

        sync_state = cfg.get('sync_state', {})
        for remote_p, info in sync_state.items():
            key = (mod_id, remote_p)
            old_lp = info.get('local_path', '')
            if key in moved_map:
                new_lp = to_storage_rel_or_abs(moved_map[key], effective_root, base_dir)
                if new_lp != old_lp:
                    info['local_path'] = new_lp
                    changed_cfg = True
                remote_to_new_lp[remote_p] = new_lp
                if old_lp:
                    old_lp_to_new_lp[(mod_id, old_lp)] = new_lp
            elif key in failed_map:
                # Keep failed file pointing to its actual surviving location
                new_lp = to_storage_rel_or_abs(failed_map[key], effective_root, base_dir)
                if new_lp != old_lp:
                    info['local_path'] = new_lp
                    changed_cfg = True
                remote_to_new_lp[remote_p] = new_lp
            elif switched_global_root and old_lp and os.path.isabs(old_lp) and _is_subpath(old_lp, dest_root_norm):
                new_lp = to_storage_rel_or_abs(old_lp, effective_root, base_dir)
                info['local_path'] = new_lp
                changed_cfg = True
                remote_to_new_lp[remote_p] = new_lp

        if changed_cfg:
            atomic_write_json(cfg_path, cfg)

    # Update tailieu_catalog.json (preserving 100% rich metadata)
    for doc in catalog:
        key = _doc_key(doc)
        if key in moved_map:
            new_lp = to_storage_rel_or_abs(moved_map[key], effective_root, base_dir)
            doc['local_path'] = new_lp
            doc['file_exists'] = is_file_exists(moved_map[key])
        elif key in failed_map:
            new_lp = to_storage_rel_or_abs(failed_map[key], effective_root, base_dir)
            doc['local_path'] = new_lp
            doc['file_exists'] = is_file_exists(failed_map[key])
        else:
            resolved = resolve_local_path(doc.get('local_path', ''), effective_root, base_dir)
            doc['file_exists'] = is_file_exists(resolved)
    atomic_write_json(paths['catalog'], catalog)

    # Update governance_catalog.json
    if governance:
        gov_changed = False
        for item in governance:
            rp = item.get('remote_path', '')
            sm = item.get('source_module', '')
            lp = item.get('local_path', '')
            if rp and rp in remote_to_new_lp:
                if item.get('local_path') != remote_to_new_lp[rp]:
                    item['local_path'] = remote_to_new_lp[rp]
                    gov_changed = True
            elif lp and (sm, lp) in old_lp_to_new_lp:
                if item.get('local_path') != old_lp_to_new_lp[(sm, lp)]:
                    item['local_path'] = old_lp_to_new_lp[(sm, lp)]
                    gov_changed = True
        if gov_changed:
            atomic_write_json(paths['governance'], governance)

    # --- Clean up empty directories at old location ---
    if cleanup_empty and not copy_only and source_top_dirs:
        protected = [
            paths['base'],
            paths['configs'],
            paths['master_excels'],
            old_root,
            dest_root_norm,
        ]
        stats['empty_dirs_removed'] = cleanup_empty_dirs(list(source_top_dirs), protected_dirs=protected)
        if stats['empty_dirs_removed']:
            log(f'🧹 Đã dọn sạch {stats["empty_dirs_removed"]:,} thư mục con rỗng ở vị trí cũ.', 0.98)

    stats['ok'] = (stats['errors'] == 0 and not stats['cancelled'])
    log(
        f'✅ Hoàn tất: {action_label} {stats["moved"]:,} PDF '
        f'({stats["bytes_moved"] / (1024**2):.1f} MB), '
        f'bỏ qua {stats["skipped_same"]:,}, thiếu nguồn {stats["missing_src"]:,}, lỗi {stats["errors"]:,}.',
        1.0,
    )
    return stats


# =========================================================================
# FEATURE 2: RELINK STORAGE ROOT / VERIFY LINKS (WITHOUT MOVING FILES)
# =========================================================================

def relink_storage_root(
    new_root: str,
    smart_scan: bool = False,
    clear_module_overrides: bool = True,
    progress_callback=None,
    base_dir: str = None,
) -> dict:
    """
    Point the app to an existing document storage directory WITHOUT moving files.
    Verifies all 3,450+ document links and optionally smart-matches by filename
    if subfolder structure was altered.
    """
    def log(msg, pct=None):
        if progress_callback:
            progress_callback(msg, pct)

    paths = get_paths(base_dir)
    old_root = get_storage_root(base_dir)
    new_root_norm = os.path.normpath(os.path.abspath(new_root))

    stats = {
        'ok': False,
        'old_root': old_root,
        'new_root': new_root_norm,
        'total': 0,
        'found': 0,
        'smart_matched': 0,
        'missing': 0,
        'error': '',
    }

    if not new_root or not path_exists(new_root_norm):
        stats['error'] = f'Thư mục không tồn tại: {new_root}'
        return stats

    # Optional smart scan index: filename.lower() -> list of relative paths
    filename_index = {}
    if smart_scan:
        log(f'🔎 Đang quét toàn bộ file PDF tại {new_root_norm} để dò link thông minh...', 0.10)
        for root, _, files in os.walk(to_long_path(new_root_norm)):
            clean_r = strip_long_prefix(root)
            for fn in files:
                if fn.lower().endswith('.pdf'):
                    full = os.path.join(clean_r, fn)
                    rel = os.path.relpath(full, new_root_norm)
                    filename_index.setdefault(fn.lower(), []).append(rel)
        log(f'🔎 Đã lập chỉ mục {sum(len(v) for v in filename_index.values()):,} file PDF tại địa chỉ mới.', 0.35)

    def _pick_best_smart_match(old_lp: str, fname: str) -> str:
        cands = filename_index.get((fname or '').lower(), [])
        if not cands:
            return ''
        if len(cands) == 1:
            return cands[0]
        # Score by shared parent folder names
        old_parts = set(p.lower() for p in os.path.normpath(old_lp).split(os.sep)[:-1] if p)
        best = cands[0]
        best_score = -1
        for c in cands:
            c_parts = set(p.lower() for p in os.path.normpath(c).split(os.sep)[:-1] if p)
            score = len(old_parts & c_parts)
            if score > best_score:
                best_score = score
                best = c
        return best

    set_storage_root(new_root_norm, note='Cập nhật địa chỉ kho (Relink)', base_dir=base_dir)

    configs = _load_all_configs(base_dir)
    catalog = _load_json(paths['catalog'], [])
    governance = _load_json(paths['governance'], [])

    log('🔗 Đang đối chiếu và nối lại đường dẫn cho toàn bộ tài liệu...', 0.50)

    remote_to_lp = {}
    old_lp_to_new_lp = {}

    for cfg_path, cfg in configs:
        mod_id = cfg.get('id')
        if clear_module_overrides and cfg.get('custom_storage_root'):
            cfg['custom_storage_root'] = ''
        sync_state = cfg.get('sync_state', {})
        for remote_p, info in sync_state.items():
            old_lp = info.get('local_path', '')
            fname = info.get('clean_filename') or os.path.basename(old_lp)
            new_lp = old_lp

            # 1. If old_lp was absolute inside old_root, remap to relative in new_root
            if old_lp and os.path.isabs(old_lp):
                if _is_subpath(old_lp, old_root):
                    rel = os.path.relpath(old_lp, old_root)
                    if is_file_exists(os.path.join(new_root_norm, rel)):
                        new_lp = rel
                elif _is_subpath(old_lp, new_root_norm):
                    new_lp = os.path.relpath(old_lp, new_root_norm)

            # 2. Check resolved path directly
            cand_abs = resolve_local_path(new_lp, new_root_norm, base_dir)
            if not is_file_exists(cand_abs) and smart_scan:
                matched_rel = _pick_best_smart_match(old_lp, fname)
                if matched_rel:
                    new_lp = matched_rel
                    cand_abs = os.path.join(new_root_norm, matched_rel)
                    stats['smart_matched'] += 1

            info['local_path'] = new_lp
            if is_file_exists(cand_abs):
                try:
                    info['size'] = os.path.getsize(to_long_path(cand_abs))
                    info['mtime'] = os.path.getmtime(to_long_path(cand_abs))
                except OSError:
                    pass
            remote_to_lp[remote_p] = new_lp
            if old_lp:
                old_lp_to_new_lp[(mod_id, old_lp)] = new_lp

        atomic_write_json(cfg_path, cfg)

    # Update tailieu_catalog.json
    stats['total'] = len(catalog)
    for doc in catalog:
        rp = doc.get('remote_path', '')
        old_lp = doc.get('local_path', '')
        new_lp = remote_to_lp.get(rp, old_lp)

        # Handle catalog entries not in sync_state (edge case)
        cand_abs = resolve_local_path(new_lp, new_root_norm, base_dir)
        if not is_file_exists(cand_abs) and smart_scan:
            matched_rel = _pick_best_smart_match(old_lp, doc.get('filename') or os.path.basename(old_lp))
            if matched_rel:
                new_lp = matched_rel
                cand_abs = os.path.join(new_root_norm, matched_rel)
                stats['smart_matched'] += 1

        doc['local_path'] = new_lp
        exists = is_file_exists(cand_abs)
        doc['file_exists'] = exists
        if exists:
            stats['found'] += 1
            try:
                doc['size'] = os.path.getsize(to_long_path(cand_abs))
                doc['mtime'] = os.path.getmtime(to_long_path(cand_abs))
            except OSError:
                pass
        else:
            stats['missing'] += 1

    atomic_write_json(paths['catalog'], catalog)

    # Update governance_catalog.json
    if governance:
        for item in governance:
            rp = item.get('remote_path', '')
            sm = item.get('source_module', '')
            lp = item.get('local_path', '')
            if rp and rp in remote_to_lp:
                item['local_path'] = remote_to_lp[rp]
            elif lp and (sm, lp) in old_lp_to_new_lp:
                item['local_path'] = old_lp_to_new_lp[(sm, lp)]
        atomic_write_json(paths['governance'], governance)

    stats['ok'] = True
    log(
        f'✅ Đã cập nhật địa chỉ kho mới: {new_root_norm}\n'
        f'   • Khớp tìm thấy: {stats["found"]:,} / {stats["total"]:,} tài liệu '
        f'(Dò thông minh: {stats["smart_matched"]:,}, Chưa có file: {stats["missing"]:,})',
        1.0,
    )
    return stats


def verify_all_links(progress_callback=None, base_dir: str = None) -> dict:
    """Re-verify file_exists for all catalog entries against current storage_root."""
    def log(msg, pct=None):
        if progress_callback:
            progress_callback(msg, pct)

    paths = get_paths(base_dir)
    root = get_storage_root(base_dir)
    catalog = _load_json(paths['catalog'], [])
    found = 0
    missing = 0

    log(f'🔄 Đang kiểm tra lại {len(catalog):,} liên kết tài liệu tại {root}...', 0.2)
    for doc in catalog:
        full_p = resolve_local_path(doc.get('local_path', ''), root, base_dir)
        exists = is_file_exists(full_p)
        doc['file_exists'] = exists
        if exists:
            found += 1
            try:
                doc['size'] = os.path.getsize(to_long_path(full_p))
            except OSError:
                pass
        else:
            missing += 1

    atomic_write_json(paths['catalog'], catalog)
    log(f'✅ Kiểm tra xong: {found:,} sẵn sàng cục bộ, {missing:,} chưa có file.', 1.0)
    return {'total': len(catalog), 'found': found, 'missing': missing, 'storage_root': root}


# =========================================================================
# FEATURE 3: MOVE SELECTED DOCUMENTS & UPDATE SINGLE DOCUMENT ADDRESS
# =========================================================================

def move_selected_documents(
    docs: list,
    dest_dir: str,
    preserve_structure: bool = False,
    copy_only: bool = False,
    progress_callback=None,
    base_dir: str = None,
) -> dict:
    """
    Move (or copy) one or more selected documents to dest_dir and update their links
    across configs/*.json, tailieu_catalog.json, and governance_catalog.json.
    """
    def log(msg, pct=None):
        if progress_callback:
            progress_callback(msg, pct)

    paths = get_paths(base_dir)
    storage_root = get_storage_root(base_dir)
    dest_norm = os.path.normpath(os.path.abspath(dest_dir))

    stats = {
        'ok': False,
        'requested': len(docs),
        'moved': 0,
        'skipped_same': 0,
        'missing': 0,
        'errors': 0,
        'error_details': [],
        'updated_records': 0,
    }

    if not dest_dir or not docs:
        stats['error_details'].append('Thiếu danh sách tài liệu hoặc thư mục đích.')
        return stats

    try:
        os.makedirs(to_long_path(dest_norm), exist_ok=True)
    except Exception as e:
        stats['error_details'].append(f'Không thể tạo thư mục đích: {e}')
        return stats

    catalog = _load_json(paths['catalog'], [])
    governance = _load_json(paths['governance'], [])
    configs = _load_all_configs(base_dir)

    selected_keys = set(_doc_key(d) for d in docs)
    selected_norm_srcs = {}  # normcase(src_abs) -> src_abs

    for doc in catalog:
        if _doc_key(doc) in selected_keys:
            lp = doc.get('local_path', '')
            if lp:
                src_abs = resolve_local_path(lp, storage_root, base_dir)
                selected_norm_srcs[os.path.normcase(os.path.abspath(src_abs))] = (src_abs, lp)

    # Also find ALL catalog entries sharing the same physical source file (prevent broken links on duplicates)
    src_to_affected_keys = {}
    for doc in catalog:
        lp = doc.get('local_path', '')
        if not lp:
            continue
        src_abs = resolve_local_path(lp, storage_root, base_dir)
        nc = os.path.normcase(os.path.abspath(src_abs))
        if nc in selected_norm_srcs:
            # If copying, only update the explicitly selected records;
            # if moving, update ALL records sharing the physical file so none break!
            if not copy_only or _doc_key(doc) in selected_keys:
                src_to_affected_keys.setdefault(nc, []).append(_doc_key(doc))

    moved_key_to_new_abs = {}
    total_ops = max(len(selected_norm_srcs), 1)

    for idx, (nc_src, (src_abs, sample_lp)) in enumerate(selected_norm_srcs.items(), 1):
        if not is_file_exists(src_abs):
            stats['missing'] += 1
            continue

        if preserve_structure and sample_lp and not os.path.isabs(sample_lp):
            dst_abs = os.path.normpath(os.path.join(dest_norm, sample_lp))
        else:
            dst_abs = os.path.normpath(os.path.join(dest_norm, os.path.basename(src_abs)))

        # Avoid clobbering an unrelated file with the same filename
        if os.path.normcase(dst_abs) != nc_src and path_exists(dst_abs):
            dst_abs = _make_unique_path(dst_abs)

        ok, status = _safe_move_file(src_abs, dst_abs, copy_only=copy_only)
        if ok:
            if status == 'same_path':
                stats['skipped_same'] += 1
            else:
                stats['moved'] += 1
            for k in src_to_affected_keys.get(nc_src, []):
                moved_key_to_new_abs[k] = dst_abs
        else:
            stats['errors'] += 1
            stats['error_details'].append(f'{os.path.basename(src_abs)}: {status}')

        log(f'[{idx}/{total_ops}] {os.path.basename(dst_abs)}', idx / total_ops)

    # Persist link updates across configs, catalog, governance
    remote_to_new_lp = {}
    for cfg_path, cfg in configs:
        mod_id = cfg.get('id')
        changed = False
        for rp, info in cfg.get('sync_state', {}).items():
            k = (mod_id, rp)
            if k in moved_key_to_new_abs:
                new_abs = moved_key_to_new_abs[k]
                new_lp = to_storage_rel_or_abs(new_abs, storage_root, base_dir)
                info['local_path'] = new_lp
                info['clean_filename'] = os.path.basename(new_abs)
                remote_to_new_lp[rp] = new_lp
                changed = True
        if changed:
            atomic_write_json(cfg_path, cfg)

    for doc in catalog:
        k = _doc_key(doc)
        if k in moved_key_to_new_abs:
            new_abs = moved_key_to_new_abs[k]
            new_lp = to_storage_rel_or_abs(new_abs, storage_root, base_dir)
            doc['local_path'] = new_lp
            doc['filename'] = os.path.basename(new_abs)
            doc['file_exists'] = is_file_exists(new_abs)
            stats['updated_records'] += 1
    atomic_write_json(paths['catalog'], catalog)

    if governance and remote_to_new_lp:
        gov_changed = False
        for item in governance:
            rp = item.get('remote_path', '')
            if rp and rp in remote_to_new_lp:
                item['local_path'] = remote_to_new_lp[rp]
                gov_changed = True
        if gov_changed:
            atomic_write_json(paths['governance'], governance)

    stats['ok'] = stats['errors'] == 0
    return stats


def update_document_paths(
    module_id: str,
    remote_path: str,
    new_local_path: str = None,
    new_remote_path: str = None,
    base_dir: str = None,
) -> dict:
    """
    Update local_path and/or remote_path for a single document across
    configs/*.json, tailieu_catalog.json, and governance_catalog.json.
    """
    paths = get_paths(base_dir)
    storage_root = get_storage_root(base_dir)
    catalog = _load_json(paths['catalog'], [])
    governance = _load_json(paths['governance'], [])
    configs = _load_all_configs(base_dir)

    target_doc = None
    for d in catalog:
        if d.get('module_id') == module_id and d.get('remote_path', '') == (remote_path or ''):
            target_doc = d
            break

    if target_doc is None:
        return {'ok': False, 'error': 'Không tìm thấy tài liệu trong danh mục.'}

    old_remote = target_doc.get('remote_path', '')
    old_local = target_doc.get('local_path', '')

    final_remote = old_remote
    if new_remote_path is not None:
        cleaned_r = new_remote_path.strip()
        if cleaned_r != old_remote:
            # Ensure new remote_path doesn't collide with another doc in same module
            for d in catalog:
                if d is not target_doc and d.get('module_id') == module_id and d.get('remote_path') == cleaned_r:
                    return {'ok': False, 'error': 'Đường dẫn ổ mạng mới bị trùng với một tài liệu khác trong cùng phân hệ.'}
            final_remote = cleaned_r

    final_local = old_local
    final_abs = resolve_local_path(old_local, storage_root, base_dir)
    if new_local_path is not None:
        cleaned_l = new_local_path.strip()
        if cleaned_l:
            if os.path.isabs(cleaned_l):
                final_abs = os.path.normpath(os.path.abspath(cleaned_l))
                final_local = to_storage_rel_or_abs(final_abs, storage_root, base_dir)
            else:
                final_local = os.path.normpath(cleaned_l)
                final_abs = resolve_local_path(final_local, storage_root, base_dir)
        else:
            final_local = ''
            final_abs = ''

    exists = is_file_exists(final_abs)
    new_size = target_doc.get('size', 0)
    new_mtime = target_doc.get('mtime', 0)
    new_fname = target_doc.get('filename', '')
    if exists:
        try:
            new_size = os.path.getsize(to_long_path(final_abs))
            new_mtime = os.path.getmtime(to_long_path(final_abs))
        except OSError:
            pass
    if final_local:
        new_fname = os.path.basename(final_local)

    # 1. Update configs/<module>.json
    for cfg_path, cfg in configs:
        if cfg.get('id') != module_id:
            continue
        sync_state = cfg.get('sync_state', {})
        entry = sync_state.pop(old_remote, None)
        if entry is None:
            entry = {
                'doc_code': target_doc.get('doc_code', ''),
                'is_canceled': target_doc.get('is_canceled', False),
            }
        entry['local_path'] = final_local
        entry['clean_filename'] = new_fname
        entry['size'] = new_size
        entry['mtime'] = new_mtime
        entry['last_updated'] = datetime.now().isoformat()
        sync_state[final_remote] = entry
        cfg['sync_state'] = sync_state
        atomic_write_json(cfg_path, cfg)
        break

    # 2. Update tailieu_catalog.json
    target_doc['local_path'] = final_local
    target_doc['remote_path'] = final_remote
    target_doc['filename'] = new_fname
    target_doc['file_exists'] = exists
    target_doc['size'] = new_size
    target_doc['mtime'] = new_mtime
    atomic_write_json(paths['catalog'], catalog)

    # 3. Update governance_catalog.json
    if governance:
        gov_changed = False
        for item in governance:
            matched = False
            if old_remote and item.get('remote_path') == old_remote:
                matched = True
            elif not old_remote and old_local and item.get('source_module') == module_id and item.get('local_path') == old_local:
                matched = True
            if matched:
                item['local_path'] = final_local
                item['remote_path'] = final_remote
                gov_changed = True
        if gov_changed:
            atomic_write_json(paths['governance'], governance)

    return {
        'ok': True,
        'local_path': final_local,
        'resolved_local_path': final_abs,
        'remote_path': final_remote,
        'file_exists': exists,
    }


# =========================================================================
# FEATURE 4: DELETE DOCUMENTS (3 SAFE MODES + WINDOWS RECYCLE BIN)
# =========================================================================

def delete_documents(
    docs: list,
    mode: str = 'disk_only',
    use_recycle_bin: bool = True,
    cleanup_empty: bool = True,
    progress_callback=None,
    base_dir: str = None,
) -> dict:
    """
    Delete one or more documents safely.
    mode:
      - 'disk_only': Delete PDF file on disk to free space; keep catalog/config entries (file_exists=False).
      - 'disk_and_catalog': Delete PDF file on disk AND remove from configs, catalog, governance.
      - 'catalog_only': Remove from configs, catalog, governance; leave file untouched on disk.
    """
    def log(msg, pct=None):
        if progress_callback:
            progress_callback(msg, pct)

    if mode not in ('disk_only', 'disk_and_catalog', 'catalog_only'):
        return {'ok': False, 'error': f'Chế độ xóa không hợp lệ: {mode}'}

    paths = get_paths(base_dir)
    storage_root = get_storage_root(base_dir)
    catalog = _load_json(paths['catalog'], [])
    governance = _load_json(paths['governance'], [])
    configs = _load_all_configs(base_dir)

    selected_keys = set(_doc_key(d) for d in docs)
    matched_docs = [d for d in catalog if _doc_key(d) in selected_keys]

    stats = {
        'ok': False,
        'mode': mode,
        'requested': len(docs),
        'matched': len(matched_docs),
        'files_deleted': 0,
        'files_recycled': 0,
        'files_not_found': 0,
        'records_removed': 0,
        'gov_removed': 0,
        'bytes_freed': 0,
        'errors': 0,
        'error_details': [],
    }

    deleted_norm_paths = set()
    parent_dirs_touched = set()

    # 1. Delete physical files on disk if requested
    if mode in ('disk_only', 'disk_and_catalog'):
        unique_files = {}  # normcase(abs_path) -> abs_path
        for d in matched_docs:
            lp = d.get('local_path', '')
            if not lp:
                continue
            full_p = resolve_local_path(lp, storage_root, base_dir)
            unique_files[os.path.normcase(os.path.abspath(full_p))] = full_p

        total_f = max(len(unique_files), 1)
        for idx, (nc_p, full_p) in enumerate(unique_files.items(), 1):
            if not is_file_exists(full_p):
                stats['files_not_found'] += 1
                deleted_norm_paths.add(nc_p)
                continue

            try:
                sz = os.path.getsize(to_long_path(full_p))
            except OSError:
                sz = 0

            ok, method, detail = delete_file_safe(full_p, use_recycle_bin=use_recycle_bin)
            if ok:
                stats['files_deleted'] += 1
                stats['bytes_freed'] += sz
                if method == 'recycled':
                    stats['files_recycled'] += 1
                deleted_norm_paths.add(nc_p)
                parent_dirs_touched.add(os.path.dirname(full_p))
            else:
                stats['errors'] += 1
                stats['error_details'].append(f'{os.path.basename(full_p)}: {detail}')
                log(f'⚠️ Không thể xóa {os.path.basename(full_p)}: {detail}', None)

            if idx % 25 == 0 or idx == len(unique_files):
                log(f'🗑️ Đang xóa file [{idx:,}/{len(unique_files):,}]...', 0.1 + 0.7 * (idx / total_f))

        if cleanup_empty and parent_dirs_touched:
            protected = [paths['base'], paths['configs'], paths['master_excels'], storage_root]
            cleanup_empty_dirs(list(parent_dirs_touched), protected_dirs=protected)

    # 2. Update catalog, configs, governance
    removed_remotes = set()
    removed_mod_lp = set()

    if mode == 'disk_only':
        # Update file_exists for all docs whose physical file was deleted (including shared duplicates!)
        for d in catalog:
            lp = d.get('local_path', '')
            if not lp:
                continue
            full_p = resolve_local_path(lp, storage_root, base_dir)
            nc = os.path.normcase(os.path.abspath(full_p))
            if nc in deleted_norm_paths:
                d['file_exists'] = is_file_exists(full_p)
        atomic_write_json(paths['catalog'], catalog)
    else:
        # Remove selected records from catalog
        new_catalog = []
        for d in catalog:
            k = _doc_key(d)
            if k in selected_keys:
                stats['records_removed'] += 1
                rp = d.get('remote_path', '')
                lp = d.get('local_path', '')
                if rp:
                    removed_remotes.add(rp)
                if lp:
                    removed_mod_lp.add((d.get('module_id', ''), lp))
                continue
            # Also sync file_exists if another surviving record shared a deleted physical file
            if deleted_norm_paths and d.get('local_path'):
                full_p = resolve_local_path(d['local_path'], storage_root, base_dir)
                if os.path.normcase(os.path.abspath(full_p)) in deleted_norm_paths:
                    d['file_exists'] = is_file_exists(full_p)
            new_catalog.append(d)
        atomic_write_json(paths['catalog'], new_catalog)

        # Remove from configs/*.json
        for cfg_path, cfg in configs:
            mod_id = cfg.get('id')
            sync_state = cfg.get('sync_state', {})
            to_del = [rp for rp in sync_state if (mod_id, rp) in selected_keys]
            if to_del:
                for rp in to_del:
                    sync_state.pop(rp, None)
                cfg['sync_state'] = sync_state
                atomic_write_json(cfg_path, cfg)

        # Remove matching items from governance_catalog.json
        if governance:
            new_gov = []
            for item in governance:
                rp = item.get('remote_path', '')
                sm = item.get('source_module', '')
                lp = item.get('local_path', '')
                should_remove = False
                if rp and rp in removed_remotes:
                    should_remove = True
                elif not rp and lp and (sm, lp) in removed_mod_lp:
                    should_remove = True
                if should_remove:
                    stats['gov_removed'] += 1
                    continue
                new_gov.append(item)
            if stats['gov_removed'] > 0:
                atomic_write_json(paths['governance'], new_gov)

    stats['ok'] = stats['errors'] == 0
    log(
        f'✅ Xóa xong ({mode}): xóa {stats["files_deleted"]:,} file trên ổ cứng '
        f'({stats["bytes_freed"] / (1024**2):.2f} MB), xóa {stats["records_removed"]:,} bản ghi danh mục, '
        f'lỗi {stats["errors"]:,}.',
        1.0,
    )
    return stats
