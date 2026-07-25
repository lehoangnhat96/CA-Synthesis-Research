import re
with open('DCLV_CA_19.06 Fe-N CA.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where references start
parts = re.split(r'# TÀI LIỆU THAM KHẢO|TÀI LIỆU THAM KHẢO', content)
if len(parts) > 1:
    refs = parts[-1].strip()
    with open('dclv_refs_out.txt', 'w', encoding='utf-8') as out:
        out.write(refs)
else:
    with open('dclv_refs_out.txt', 'w', encoding='utf-8') as out:
        out.write("NOT FOUND")
