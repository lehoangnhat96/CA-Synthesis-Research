import re

md_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.md"
with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(?m)^# TÀI LIỆU THAM KHẢO', text)
if len(parts) > 1:
    bib = parts[1]
    # Remove any ## Phụ lục if present
    bib = re.split(r'(?m)^## Phụ lục', bib)[0].strip()
    with open("D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DANH_MUC_MOI.txt", 'w', encoding='utf-8-sig') as out:
        out.write(bib)
    print("Created DANH_MUC_MOI.txt")
