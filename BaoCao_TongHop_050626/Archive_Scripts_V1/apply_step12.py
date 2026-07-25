import re
import difflib

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
        master_refs.append({'idx': idx, 'text': text, 'doi': doi})

mapping_num_to_num = {}
next_dclv_idx = max([r['idx'] for r in dclv_refs]) + 1 if dclv_refs else 1
new_added_refs = []

for m_ref in master_refs:
    found_in_dclv = None
    if m_ref['doi']:
        for d_ref in dclv_refs:
            if d_ref['doi'] and d_ref['doi'].lower() == m_ref['doi'].lower():
                found_in_dclv = d_ref
                break
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
        mapping_num_to_num[str(m_ref['idx'])] = str(found_in_dclv['idx'])
    else:
        mapping_num_to_num[str(m_ref['idx'])] = str(next_dclv_idx)
        new_added_refs.append(f"[{next_dclv_idx}] {m_ref['text']}")
        next_dclv_idx += 1

mapping_tag_to_num = {}
raw_matches = re.findall(r'\[(P-[^\]]+)\]', master_content)
for rm in raw_matches:
    parts = rm.split(',')
    if len(parts) >= 2:
        tag = parts[0].strip()
        num_str = parts[-1].strip()
        if num_str.isdigit():
            if num_str in mapping_num_to_num:
                mapping_tag_to_num[tag] = mapping_num_to_num[num_str]

intro_match = re.search(r'(# MỞ ĐẦU\n.*?)(?=# CHƯƠNG 1\. TỔNG QUAN)', master_content, re.DOTALL)
intro_text = intro_match.group(1).strip() if intro_match else ""

def repl_intro_refs(match):
    inner = match.group(1)
    nums = re.findall(r'\d+', inner)
    mapped_nums = []
    for n in nums:
        mapped_nums.append(mapping_num_to_num.get(n, n))
    return "[" + ", ".join(mapped_nums) + "]"

intro_text = re.sub(r'\[([\d\s,\-]+)\]', repl_intro_refs, intro_text)

with open('03_LuanAn_KeThua_ThaoTac_va_CoChe_ChiTiet.md', 'r', encoding='utf-8') as f:
    coche = f.read()

co_che_match = re.search(r'(## 1\. Cơ sở khoa học của quy trình\n.*?)(?=\n## 2\. Hoàn thiện thông số)', coche, re.DOTALL)
coche_text = co_che_match.group(1).strip() if co_che_match else ""
coche_part1 = "Việc lựa chọn hệ dung môi" + coche_text.split("Việc lựa chọn hệ dung môi")[1].split("1.2.2.")[0].strip()
coche_part2 = "Quá trình nhiệt phân Fe-doped" + coche_text.split("Quá trình nhiệt phân Fe-doped")[1].strip()

def repl_tags(match):
    tag = match.group(1)
    return "[" + mapping_tag_to_num.get(tag, tag) + "]"

coche_part1 = "\n\n**1.1.5. Lập luận thiết kế và Biện luận cơ chế (Bổ sung)**\n\n" + re.sub(r'\[(P-[^\]]+)\]', repl_tags, coche_part1) + "\n\n"
coche_part2 = "\n\n**1.2.2. Cơ sở khoa học của quá trình Nhiệt phân và Pha tạp (Bổ sung)**\n\n" + re.sub(r'\[(P-[^\]]+)\]', repl_tags, coche_part2) + "\n\n"

dclv_content = re.sub(r'(?is)\[MỞ ĐẦU.*?# MỞ ĐẦU.*?(?=\[CHƯƠNG 1)', intro_text + "\n\n", dclv_content)

# In case the regex above fails to match the DCLV link structure:
if "# MỞ ĐẦU" not in dclv_content:
    # Manual string replacement for safety
    start_idx = dclv_content.find("[MỞ ĐẦU")
    end_idx = dclv_content.find("[CHƯƠNG 1")
    if start_idx != -1 and end_idx != -1:
        dclv_content = dclv_content[:start_idx] + intro_text + "\n\n" + dclv_content[end_idx:]

dclv_content = re.sub(r'(?i)(\n\[1\.2\. Carbon Aerogel)', coche_part1 + r'\1', dclv_content)
dclv_content = re.sub(r'(?i)(\n\[1\.3\. Cơ chế lớp kép)', coche_part2 + r'\1', dclv_content)

if new_added_refs:
    # Append the new refs
    dclv_content += "\n\n" + "\n\n".join(new_added_refs) + "\n"

with open('DCLV_CA_19.06 Fe-N CA.md', 'w', encoding='utf-8') as f:
    f.write(dclv_content)

print("Applied Step 1 & 2 successfully.")
