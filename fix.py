import re
import sys

file_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered_restored.md"

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Make the manual replacements using replace instead of regex to avoid escaping issues
r1_target = "Thuyết Kén phân tử (Inclusion Complex Theory) được mô tả bởi Cai & Zhang \[6\] cho cơ chế hòa tan cellulose trong hệ NaOH/Urea. Cơ chế này được giả định tương tự cho hệ dung môi amoniac/urea/nước được sử dụng trong đề tài \[22, 23\], trong đó hòa tan cellulose hòa tan cellulose theo cơ chế phối trí đa thành phần ở nhiệt độ lạnh."
r1_repl = "Thuyết Kén phân tử (Inclusion Complex Theory) được xây dựng bởi nhóm GS. Lina Zhang: cơ chế hòa tan được mô tả qua hành vi gel hóa đặc biệt của cellulose trong hệ kiềm/urea \[6\], trong đó Urea đóng vai trò tạo lớp vỏ bảo vệ quanh chuỗi cellulose thông qua tương tác van der Waals và liên kết hydro — điều được xác nhận trực tiếp bằng kỹ thuật NMR bởi Xiong và cộng sự \[68\]. Cơ chế này được giả định tương tự cho hệ dung môi amoniac/urea/nước được sử dụng trong đề tài \[17, 41\], trong đó cellulose hòa tan theo cơ chế phối trí đa thành phần ở nhiệt độ lạnh."
if r1_target in text:
    text = text.replace(r1_target, r1_repl)
else:
    print("WARNING: Target 1 not found!")

r2_target = "Quá trình hòa tan là phản ứng tỏa nhiệt (ΔH \\< 0) và giảm entropy (ΔS \\< 0), do đó sol chỉ ổn định và đồng nhất ở nhiệt độ ≤ 10°C (tối ưu 0 - 5°C)."
r2_repl = "Quá trình hòa tan là phản ứng tỏa nhiệt (ΔH \\< 0) và giảm entropy (ΔS \\< 0) — được Cai và Zhang xác nhận bằng phân tích nhiệt lượng quét vi sai (DSC) \[69\] — do đó sol chỉ ổn định và đồng nhất ở nhiệt độ ≤ 10°C (tối ưu 0 - 5°C)."
if r2_target in text:
    text = text.replace(r2_target, r2_repl)
else:
    print("WARNING: Target 2 not found!")

parts = re.split(r'(?m)^# TÀI LIỆU THAM KHẢO', text)
body = parts[0]
bib_section = parts[1] if len(parts) > 1 else ""

with open('bib_raw.txt', 'r', encoding='utf-8') as fb:
    bib_raw = fb.read()

ref_dict = {}
for m in re.finditer(r'(?m)^\[(\d+)\]\s+(.*?)(?=\n\[\d+\]|\n## Phụ lục|\Z)', bib_raw, re.DOTALL):
    ref_dict[int(m.group(1))] = m.group(2).strip()

old_to_new = {}
next_new_id = 1
pattern2 = r'(\\*\[)([0-9,\s\-]+)(\\*\])'

def replacer(m):
    global next_new_id
    prefix = m.group(1)
    inner = m.group(2).replace(' ', '')
    suffix = m.group(3)
    
    new_parts = []
    for p in inner.split(','):
        if '-' in p:
            start_s, end_s = p.split('-')
            try:
                start, end = int(start_s), int(end_s)
            except ValueError:
                return m.group(0)
            
            new_nums = []
            for num in range(start, end + 1):
                if num not in old_to_new:
                    old_to_new[num] = next_new_id
                    next_new_id += 1
                new_nums.append(old_to_new[num])
            
            if len(new_nums) > 2 and new_nums == list(range(new_nums[0], new_nums[-1] + 1)):
                new_parts.append(f"{new_nums[0]}-{new_nums[-1]}")
            else:
                new_parts.extend(map(str, new_nums))
        else:
            try:
                num = int(p)
            except ValueError:
                return m.group(0)
            if num not in old_to_new:
                old_to_new[num] = next_new_id
                next_new_id += 1
            new_parts.append(str(old_to_new[num]))
    return f"{prefix}{', '.join(new_parts)}{suffix}"

new_body = re.sub(pattern2, replacer, body)
new_bib_lines = ["\n\n"]
for old_id, new_id in sorted(old_to_new.items(), key=lambda x: x[1]):
    if old_id in ref_dict:
        new_bib_lines.append(f"[{new_id}] {ref_dict[old_id]}\n\n")
    else:
        new_bib_lines.append(f"[{new_id}] MISSING REFERENCE FOR OLD ID {old_id}\n\n")

post_bib = ""
match_post = re.search(r'(?m)^## Phụ lục.*', text, re.DOTALL)
if match_post:
    post_bib = match_post.group(0)

new_text = new_body + "# TÀI LIỆU THAM KHẢO" + "".join(new_bib_lines) + post_bib

out_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.md"
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print(f"Renumbering complete! Total unique mapped: {len(old_to_new)}")
if 68 in old_to_new:
    print(f"Replaced [68] -> [{old_to_new[68]}]")
if 69 in old_to_new:
    print(f"Replaced [69] -> [{old_to_new[69]}]")
