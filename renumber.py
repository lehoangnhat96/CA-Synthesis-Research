import re
import sys

file_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.md"

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Separate body and bibliography
parts = re.split(r'(?m)^# TÀI LIỆU THAM KHẢO', text)
if len(parts) < 2:
    print("Could not find bibliography section!")
    sys.exit(1)

body = parts[0]
bib_section = parts[1]

# Extract references from bibliography
ref_dict = {}
ref_matches = list(re.finditer(r'(?m)^\[(\d+)\]\s+(.*?)(?=\n\[\d+\]|\n## Phụ lục|\Z)', bib_section, re.DOTALL))
for m in ref_matches:
    num = int(m.group(1))
    content = m.group(2).strip()
    ref_dict[num] = content

print(f"Loaded {len(ref_dict)} references from bibliography.")

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
                return m.group(0) # Not a valid citation
            
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

print(f"Total unique citations mapped: {len(old_to_new)}")

# Rebuild bibliography
new_bib_lines = ["\n\n"]
for old_id, new_id in sorted(old_to_new.items(), key=lambda x: x[1]):
    if old_id in ref_dict:
        new_bib_lines.append(f"[{new_id}] {ref_dict[old_id]}\n\n")
    else:
        new_bib_lines.append(f"[{new_id}] MISSING REFERENCE FOR OLD ID {old_id}\n\n")

# Check if there's text after the bibliography (like Phụ lục)
post_bib = ""
match_post = re.search(r'(?m)^## Phụ lục.*', bib_section, re.DOTALL)
if match_post:
    post_bib = match_post.group(0)

new_text = new_body + "# TÀI LIỆU THAM KHẢO" + "".join(new_bib_lines) + post_bib

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Renumbering complete and written to file.")
print("Mapping (Old -> New):")
for old, new in list(old_to_new.items())[:5]:
    print(f"  [{old}] -> [{new}]")
if 68 in old_to_new: print(f"  [68] -> [{old_to_new[68]}]")
if 69 in old_to_new: print(f"  [69] -> [{old_to_new[69]}]")
