import re
import urllib.request
import json
import difflib

# 1. Read DCLV References
with open('DCLV_CA_19.06 Fe-N CA.md', 'r', encoding='utf-8') as f:
    dclv_content = f.read()
dclv_ref_section = re.split(r'# TÀI LIỆU THAM KHẢO|TÀI LIỆU THAM KHẢO', dclv_content)[-1]
dclv_refs = []
for line in dclv_ref_section.strip().split('\n'):
    line = line.strip()
    match = re.search(r'\\?\[(\d+)\\?\]\s*(.*)', line)
    if match:
        idx = int(match.group(1))
        text = match.group(2).replace('\\', '')
        doi_match = re.search(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', text, re.I)
        doi = doi_match.group(0).rstrip('.') if doi_match else None
        dclv_refs.append({'idx': idx, 'text': text, 'doi': doi})

# 2. Read Master Draft References
with open('Master_Thesis_Full_Draft.md', 'r', encoding='utf-8') as f:
    master_content = f.read()
master_ref_section = master_content.split("# TÀI LIỆU THAM KHẢO")[1]
master_refs = []
for line in master_ref_section.strip().split('\n'):
    line = line.strip()
    match = re.search(r'\\?\[(\d+)\\?\]\s*(.*)', line)
    if match:
        idx = int(match.group(1))
        text = match.group(2).replace('\\', '')
        doi_match = re.search(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', text, re.I)
        doi = doi_match.group(0).rstrip('.') if doi_match else None
        master_refs.append({'idx': idx, 'text': text, 'doi': doi, 'original_idx': idx})

# 3. Compare and Map
mapping = []
new_refs = []
next_dclv_idx = max([r['idx'] for r in dclv_refs]) + 1 if dclv_refs else 1

for m_ref in master_refs:
    found_in_dclv = None
    
    # Check by DOI
    if m_ref['doi']:
        for d_ref in dclv_refs:
            if d_ref['doi'] and d_ref['doi'].lower() == m_ref['doi'].lower():
                found_in_dclv = d_ref
                break
                
    # Fallback: Fuzzy match title if no DOI match
    if not found_in_dclv:
        m_title_match = re.search(r'"([^"]+)"', m_ref['text'])
        m_title = m_title_match.group(1) if m_title_match else m_ref['text']
        
        best_ratio = 0
        best_match = None
        for d_ref in dclv_refs:
            d_title_match = re.search(r'"([^"]+)"', d_ref['text'])
            d_title = d_title_match.group(1) if d_title_match else d_ref['text']
            ratio = difflib.SequenceMatcher(None, m_title.lower(), d_title.lower()).ratio()
            if ratio > 0.85 and ratio > best_ratio:
                best_ratio = ratio
                best_match = d_ref
        
        if best_match:
            found_in_dclv = best_match

    if found_in_dclv:
        mapping.append({
            'master_idx': m_ref['idx'],
            'mapped_to_dclv': found_in_dclv['idx'],
            'status': 'TRÙNG',
            'dclv_text': found_in_dclv['text']
        })
    else:
        mapping.append({
            'master_idx': m_ref['idx'],
            'mapped_to_dclv': next_dclv_idx,
            'status': 'CHƯA CÓ (Sẽ bổ sung)',
            'master_text': m_ref['text']
        })
        new_refs.append(m_ref)
        next_dclv_idx += 1

# Process SOP tags
p_tags_mapping = {}
raw_matches = re.findall(r'\[(P-[^\]]+)\]', master_content)
for rm in raw_matches:
    parts = rm.split(',')
    if len(parts) >= 2:
        tag = parts[0].strip()
        num_str = parts[-1].strip()
        if num_str.isdigit():
            m_idx = int(num_str)
            try:
                mapped_dclv_idx = next(item['mapped_to_dclv'] for item in mapping if item['master_idx'] == m_idx)
                p_tags_mapping[tag] = mapped_dclv_idx
            except StopIteration:
                pass

report_md = """# Bảng Đối chiếu và Cập nhật Tài liệu Tham khảo

**Tình trạng ban đầu:**
- File DCLV hiện có **{}** tài liệu tham khảo.
- File Master Draft có **{}** tài liệu (chuẩn IEEE).

Dưới đây là kết quả rà soát: Các tài liệu nào ở Master Draft đã có mặt trong DCLV sẽ được tái sử dụng số cũ của DCLV để tránh trùng. Các tài liệu nào chưa có sẽ được nối tiếp bắt đầu từ số [{}].

## 1. Bảng đối chiếu chéo (Master Draft -> DCLV)

| Số trong Master | Trạng thái | Số sẽ dùng trong DCLV |
| :--- | :--- | :--- |
""".format(len(dclv_refs), len(master_refs), max([r['idx'] for r in dclv_refs]) + 1 if dclv_refs else 1)

for m in mapping:
    note = "Đã có sẵn" if m['status'] == 'TRÙNG' else "Sẽ thêm mới"
    report_md += f"| Bài [{m['master_idx']}] | {m['status']} | **[{m['mapped_to_dclv']}]** |\n"

report_md += """
## 2. Bảng quy đổi Thẻ bài báo (Tags) sang Số chuẩn trong DCLV
Các thẻ nhớ bài báo (ví dụ `[P-019...]`) dùng trong các file SOP sẽ được phần mềm tự động quy đổi thành số theo bảng sau:

| Thẻ bài báo (SOP) | Sẽ được quy đổi thành số trong DCLV |
| :--- | :--- |
"""
for tag, dclv_idx in p_tags_mapping.items():
    report_md += f"| [{tag}] | **[{dclv_idx}]** |\n"

report_md += "\n> **KẾT LUẬN**: Sau khi hợp nhất, danh mục tài liệu tham khảo của DCLV sẽ dài lên thành **{}** tài liệu (gồm {} bài gốc + {} bài mới đắp vào). Mọi chỉ mục `[X]` trong bài sẽ được đánh tự động theo bảng số liệu này, tuyệt đối không bị lộn xộn hay trùng lặp.\n".format(
    next_dclv_idx - 1, len(dclv_refs), len(new_refs)
)

with open('C:\\Users\\ADMIN\\.gemini\\antigravity\\brain\\0726e7c6-fe20-4423-a0eb-a1f928b783bf\\Reference_Mapping_Table.md', 'w', encoding='utf-8') as f:
    f.write(report_md)
print("Mapping complete.")
