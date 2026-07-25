import zipfile
import re
import os

docx_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.docx"
temp_docx = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/temp.docx"

# First, get the mapping
md_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered_restored.md"
with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(?m)^# TÀI LIỆU THAM KHẢO', text)
body = parts[0]

old_to_new = {}
next_new_id = 1
pattern2 = r'(?:\\?\[)([0-9,\s\-]+)(?:\\?\])'

for m in re.finditer(pattern2, body):
    inner = m.group(1).replace(' ', '')
    for p in inner.split(','):
        if '-' in p:
            start_s, end_s = p.split('-')
            for num in range(int(start_s), int(end_s) + 1):
                if num not in old_to_new:
                    old_to_new[num] = next_new_id
                    next_new_id += 1
        else:
            num = int(p)
            if num not in old_to_new:
                old_to_new[num] = next_new_id
                next_new_id += 1

replacements = {}
for m in re.finditer(pattern2, body):
    full_match_clean = "[" + m.group(1) + "]"
    inner = m.group(1).replace(' ', '')
    
    new_parts = []
    for p in inner.split(','):
        if '-' in p:
            start_s, end_s = p.split('-')
            start, end = int(start_s), int(end_s)
            new_nums = []
            for num in range(start, end + 1):
                new_nums.append(old_to_new[num])
            if len(new_nums) > 2 and new_nums == list(range(new_nums[0], new_nums[-1] + 1)):
                new_parts.append(f"{new_nums[0]}-{new_nums[-1]}")
            else:
                new_parts.extend(map(str, new_nums))
        else:
            num = int(p)
            new_parts.append(str(old_to_new[num]))
            
    new_string = f"[{', '.join(new_parts)}]"
    if full_match_clean not in replacements:
        replacements[full_match_clean] = new_string

# Unzip and modify document.xml
with zipfile.ZipFile(docx_path, 'r') as zin:
    with zipfile.ZipFile(temp_docx, 'w') as zout:
        for item in zin.infolist():
            content = zin.read(item.filename)
            if item.filename == 'word/document.xml':
                xml_str = content.decode('utf-8')
                
                # Manual paragraph replacements
                xml_str = xml_str.replace(
                    "Thuyết Kén phân tử (Inclusion Complex Theory) được mô tả bởi Cai &amp; Zhang [6] cho cơ chế hòa tan cellulose trong hệ NaOH/Urea. Cơ chế này được giả định tương tự cho hệ dung môi amoniac/urea/nước được sử dụng trong đề tài [22, 23], trong đó hòa tan cellulose hòa tan cellulose theo cơ chế phối trí đa thành phần ở nhiệt độ lạnh.",
                    "Thuyết Kén phân tử (Inclusion Complex Theory) được xây dựng bởi nhóm GS. Lina Zhang: cơ chế hòa tan được mô tả qua hành vi gel hóa đặc biệt của cellulose trong hệ kiềm/urea [6], trong đó Urea đóng vai trò tạo lớp vỏ bảo vệ quanh chuỗi cellulose thông qua tương tác van der Waals và liên kết hydro — điều được xác nhận trực tiếp bằng kỹ thuật NMR bởi Xiong và cộng sự [52]. Cơ chế này được giả định tương tự cho hệ dung môi amoniac/urea/nước được sử dụng trong đề tài [17, 41], trong đó cellulose hòa tan theo cơ chế phối trí đa thành phần ở nhiệt độ lạnh."
                )
                
                xml_str = xml_str.replace(
                    "Quá trình hòa tan là phản ứng tỏa nhiệt (ΔH &lt; 0) và giảm entropy (ΔS &lt; 0), do đó sol chỉ ổn định và đồng nhất ở nhiệt độ ≤ 10°C (tối ưu 0 - 5°C).",
                    "Quá trình hòa tan là phản ứng tỏa nhiệt (ΔH &lt; 0) và giảm entropy (ΔS &lt; 0) — được Cai và Zhang xác nhận bằng phân tích nhiệt lượng quét vi sai (DSC) [53] — do đó sol chỉ ổn định và đồng nhất ở nhiệt độ ≤ 10°C (tối ưu 0 - 5°C)."
                )

                # Citation replacement using a tag-ignoring regex
                # We sort keys by length descending to avoid partial replacements (e.g. replacing [1] inside [10])
                for old_s in sorted(replacements.keys(), key=len, reverse=True):
                    new_s = replacements[old_s]
                    
                    # Build regex that allows <...> tags between ANY characters of old_s
                    # e.g. [12] -> \[(?:<[^>]*>)*1(?:<[^>]*>)*2(?:<[^>]*>)*\]
                    pattern_str = ""
                    for char in old_s:
                        if char in r"[]()\.^$*+?{}|\\":
                            pattern_str += "\\" + char
                        else:
                            pattern_str += char
                        pattern_str += r"(?:<[^>]*>)*"
                    
                    # Remove the trailing tag matcher
                    pattern_str = pattern_str[:-13]
                    
                    # The replacement logic: we want to keep the tags? 
                    # If we just replace the whole match with new_s, we LOSE inline formatting of the citation itself (e.g. if the citation was bold).
                    # But citations usually have uniform formatting. Replacing the whole block with `<w:t>new_s</w:t>` works if we wrap it in a proper run.
                    # Or we just don't use regex if it's not split.
                    
                    # Let's try simple replace first! Most citations are in a single run.
                    # A single run citation looks like <w:t>[1, 2]</w:t>
                    xml_str = xml_str.replace(old_s, new_s)
                    
                zout.writestr(item, xml_str.encode('utf-8'))
            else:
                zout.writestr(item, content)

os.replace(temp_docx, docx_path)
print("DOCX updated via XML!")
