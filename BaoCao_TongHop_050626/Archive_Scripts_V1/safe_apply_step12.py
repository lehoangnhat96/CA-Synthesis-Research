import re

ref_path = r"C:\Users\ADMIN\.gemini\antigravity\brain\0726e7c6-fe20-4423-a0eb-a1f928b783bf\Reference_Mapping_Table.md"
draft_path = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\Draft_MoDau_Chuong1_Full.md"
master_path = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\Master_Thesis_Full_Draft.md"
dclv_path = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\DCLV_CA_19.06 Fe-N CA.md"

with open(ref_path, 'r', encoding='utf-8') as f:
    table_content = f.read()

mapping_tag_to_num = {}
for line in table_content.split('\n'):
    match = re.search(r'\|\s*\[(P-[^\]]+)\]\s*\|\s*\*\*\[(\d+)\]\*\*', line)
    if match:
        mapping_tag_to_num[match.group(1)] = match.group(2)

mapping_num_to_num = {}
for line in table_content.split('\n'):
    match = re.search(r'\|\s*\[(\d+)\]\s*\|\s*(.*?)\s*\|\s*\*\*\[(\d+)\]\*\*', line)
    if match:
        mapping_num_to_num[match.group(1)] = match.group(3)

with open(draft_path, 'r', encoding='utf-8') as f:
    draft = f.read()

intro_match = re.search(r'## 1\. PHẦN MỞ ĐẦU.*?\n(.*?)(?=\n---)', draft, re.DOTALL)
intro_text = intro_match.group(1).strip() if intro_match else ""

coche1_match = re.search(r'\*\*1\.1\.1\. Lập luận thiết kế và Biện luận cơ chế.*?\n(Việc lựa chọn hệ dung môi.*?)(?=\n### Sẽ chèn)', draft, re.DOTALL)
coche_part1 = coche1_match.group(1).strip() if coche1_match else ""

coche2_match = re.search(r'\*\*1\.2\.2\. Cơ sở khoa học của quá trình Nhiệt phân.*?\n(Quá trình nhiệt phân Fe-doped.*)', draft, re.DOTALL)
coche_part2 = coche2_match.group(1).strip() if coche2_match else ""

def repl_tags(match):
    tag = match.group(1)
    if tag in mapping_tag_to_num:
        return f"[{mapping_tag_to_num[tag]}]"
    return match.group(0)

coche_part1 = re.sub(r'\[(P-[^\]]+)\]', repl_tags, coche_part1)
coche_part2 = re.sub(r'\[(P-[^\]]+)\]', repl_tags, coche_part2)

def repl_intro_refs(match):
    inner = match.group(1)
    nums = re.findall(r'\d+', inner)
    mapped_nums = [mapping_num_to_num.get(n, n) for n in nums]
    return "[" + ", ".join(mapped_nums) + "]"

intro_text = re.sub(r'\[([\d\s,\-]+)\]', repl_intro_refs, intro_text)

with open(dclv_path, 'r', encoding='utf-8') as f:
    dclv_content = f.read()

start_idx = dclv_content.find("[MỞ ĐẦU")
end_idx = dclv_content.find("[CHƯƠNG 1")
if start_idx != -1 and end_idx != -1:
    dclv_content = dclv_content[:start_idx] + intro_text + "\n\n" + dclv_content[end_idx:]

c1_formatted = "\n\n**1.1.5. Lập luận thiết kế và Biện luận cơ chế (Bổ sung)**\n\n" + coche_part1 + "\n\n"
dclv_content = re.sub(r'(?i)(\n\[1\.2\. Carbon Aerogel)', c1_formatted + r'\1', dclv_content)

c2_formatted = "\n\n**1.2.2. Cơ sở khoa học của quá trình Nhiệt phân và Pha tạp (Bổ sung)**\n\n" + coche_part2 + "\n\n"
dclv_content = re.sub(r'(?i)(\n\[1\.3\. Cơ chế lớp kép)', c2_formatted + r'\1', dclv_content)

with open(master_path, 'r', encoding='utf-8') as f:
    master_ref_section = f.read().split("# TÀI LIỆU THAM KHẢO")[1]

m_refs_dict = {}
for line in master_ref_section.strip().split('\n'):
    match = re.search(r'\\?\[(\d+)\\?\]\s*(.*)', line.strip())
    if match:
        m_refs_dict[match.group(1)] = match.group(2).replace('\\', '')

new_refs_to_append = []
for line in table_content.split('\n'):
    match = re.search(r'\|\s*\[(\d+)\]\s*\|\s*CHƯA CÓ.*?\s*\|\s*\*\*\[(\d+)\]\*\*', line, re.I)
    if match:
        m_id = match.group(1)
        d_id = match.group(2)
        if m_id in m_refs_dict:
            new_refs_to_append.append(f"[{d_id}] {m_refs_dict[m_id]}")

if new_refs_to_append:
    dclv_content += "\n\n" + "\n\n".join(new_refs_to_append) + "\n"

with open(dclv_path, 'w', encoding='utf-8') as f:
    f.write(dclv_content)

print("SUCCESS: DCLV updated with mapped numbers!")
