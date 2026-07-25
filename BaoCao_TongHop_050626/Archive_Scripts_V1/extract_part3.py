import re

with open('Master_Thesis_Full_Draft.md', 'r', encoding='utf-8') as f:
    content = f.read()

part3 = re.search(r'(# PHẦN 3: KẾT QUẢ VÀ THẢO LUẬN.*?)(?=# PHẦN 4: KẾT LUẬN CHUNG)', content, re.DOTALL)
if part3:
    with open('part3_master.md', 'w', encoding='utf-8') as f:
        f.write(part3.group(1))
    print("Extracted Part 3")
else:
    print("Could not find Part 3")
