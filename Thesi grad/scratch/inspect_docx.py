import zipfile
import re
import sqlite3
import shutil
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

TARGET_FILE = 'De_cuong_Luan_van_Thac_si_Le_Hoang_Nhat.docx.docx'

def clean_title(title):
    if not title:
        return ""
    title = title.replace('&quot;', '"').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    t = re.sub(r'^\[\d+\]\s*', '', title)
    return re.sub(r'[^a-z0-9]', '', t.strip().lower())

def main():
    print("=" * 60)
    print(f"KIỂM TRA FILE: {TARGET_FILE}")
    print("=" * 60)

    # ── PHASE 1: Zotero fields ──────────────────────────────────
    print("\n[GIAI ĐOẠN 1] Kiểm tra trích dẫn Zotero")
    with zipfile.ZipFile(TARGET_FILE, 'r') as zin:
        xml_content = zin.read('word/document.xml').decode('utf-8')

    total_zotero_fields = xml_content.count('ZOTERO_ITEM')
    print(f"  Tổng số field Zotero trong file: {total_zotero_fields}")

    # Extract all old item keys from uris
    old_keys = set(re.findall(r'/items/([A-Z0-9]+)', xml_content))
    print(f"  Tổng số item key duy nhất (unique refs): {len(old_keys)}")

    # Load Zotero DB
    db_path = 'scratch/zotero_check.sqlite'
    shutil.copy2(r'C:\Users\ADMIN\Zotero\zotero.sqlite', db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT key FROM items WHERE itemTypeID != (SELECT itemTypeID FROM itemTypes WHERE typeName='attachment')")
    db_keys = {row[0] for row in cursor.fetchall()}
    conn.close()
    os.remove(db_path)

    matched = old_keys & db_keys
    orphaned = old_keys - db_keys
    print(f"  Key khớp với Zotero hiện tại: {len(matched)}")
    print(f"  Key MỒ CÔI (gây lỗi []): {len(orphaned)}")
    if orphaned:
        print(f"  -> CẦN VÁ LIÊN KẾT! Các key mồ côi: {', '.join(sorted(orphaned)[:10])}{'...' if len(orphaned) > 10 else ''}")
    else:
        print("  -> OK: Toàn bộ liên kết Zotero đang hoạt động bình thường.")

    # ── PHASE 2: TOC fields ────────────────────────────────────
    print("\n[GIAI ĐOẠN 2] Kiểm tra Mục lục (TOC) & Trường ẩn")

    instr_texts = re.findall(r'<w:instrText[^>]*>(.*?)</w:instrText>', xml_content)
    toc_fields = [t for t in instr_texts if 'TOC' in t.upper()]
    zotero_in_toc = 0

    # Linear state machine to detect nesting
    elements = []
    for el_match in re.finditer(r'<w:fldChar[^>]*w:fldCharType="(begin|end)"[^>]*/?>|<w:instrText[^>]*>(.*?)</w:instrText>', xml_content):
        if el_match.group(1):
            elements.append(('fldChar', el_match.group(1)))
        elif el_match.group(2) is not None:
            elements.append(('instrText', el_match.group(2)))

    field_stack = []
    for etype, evalue in elements:
        if etype == 'fldChar':
            if evalue == 'begin':
                field_stack.append({'name': '', 'is_toc': False})
            elif evalue == 'end' and field_stack:
                field_stack.pop()
        elif etype == 'instrText':
            if field_stack:
                field_stack[-1]['name'] += evalue
                if 'TOC ' in field_stack[-1]['name'].upper():
                    field_stack[-1]['is_toc'] = True
                if 'ZOTERO_ITEM' in evalue:
                    if any(f['is_toc'] for f in field_stack):
                        zotero_in_toc += 1

    print(f"  Tổng số trường TOC hiện tại trong file: {len(toc_fields)}")
    if zotero_in_toc > 0:
        print(f"  -> CẢNH BÁO: {zotero_in_toc} trích dẫn Zotero nằm lồng trong TOC! (gây lỗi 'citation in index area')")
    else:
        print("  -> OK: Không có trích dẫn Zotero nào bị kẹt bên trong TOC.")

    # ── PHASE 3: Citation sequence ─────────────────────────────
    print("\n[GIAI ĐOẠN 3] Kiểm tra thứ tự trích dẫn trong văn bản")

    # Extract plainCitation values from Zotero fields  
    plain_citations = re.findall(r'"plainCitation":"(.*?)"', xml_content)
    all_numbers = []
    for cite in plain_citations:
        nums = re.findall(r'\d+', cite)
        all_numbers.extend(int(n) for n in nums)

    if all_numbers:
        print(f"  Số trích dẫn đầu tiên xuất hiện: [{all_numbers[0]}]")
        print(f"  Tổng số lượt trích dẫn: {len(all_numbers)}")
        print(f"  Dải số: [{min(all_numbers)}] đến [{max(all_numbers)}]")
        unique_cited = sorted(set(all_numbers))
        print(f"  Số tài liệu được trích dẫn duy nhất: {len(unique_cited)}")
        
        # Check if starts at 1
        if all_numbers[0] != 1:
            print(f"  -> CẢNH BÁO: Số trích dẫn đầu tiên KHÔNG phải [1] mà là [{all_numbers[0]}]!")
        else:
            print("  -> OK: Bắt đầu từ [1] đúng.")
        
        # Check for gaps
        expected = set(range(min(unique_cited), max(unique_cited)+1))
        gaps = expected - set(unique_cited)
        if gaps:
            print(f"  -> CẢNH BÁO: Có {len(gaps)} số bị bỏ trống (gaps): {sorted(gaps)}")
        else:
            print(f"  -> OK: Không có khoảng trống trong dãy số trích dẫn.")
    else:
        print("  -> Không tìm thấy trích dẫn Zotero động nào (có thể file dùng trích dẫn tĩnh).")
        
        # Check for static citations instead
        import docx
        doc = docx.Document(TARGET_FILE)
        static_cites = []
        for p in doc.paragraphs:
            nums = re.findall(r'\[(\d+)\]', p.text)
            static_cites.extend(int(n) for n in nums)
        
        if static_cites:
            unique_static = sorted(set(static_cites))
            print(f"  Phát hiện trích dẫn TĨNH. Tổng lượt: {len(static_cites)}, Duy nhất: {len(unique_static)}")
            print(f"  Dải: [{min(unique_static)}] đến [{max(unique_static)}]")
            if static_cites[0] != 1:
                print(f"  -> CẢNH BÁO: Bắt đầu từ [{static_cites[0]}] thay vì [1]!")
            expected = set(range(1, max(unique_static)+1))
            gaps = expected - set(unique_static)
            if gaps:
                print(f"  -> CẢNH BÁO: Các số bị thiếu: {sorted(gaps)}")
            else:
                print("  -> OK: Trích dẫn tĩnh liên tục không bị thiếu.")

    print("\n" + "=" * 60)
    print("KẾT THÚC KIỂM TRA")
    print("=" * 60)

if __name__ == '__main__':
    main()
