import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md", 'r', encoding='utf-8') as f:
    text = f.read()

# Find GĐ 8 section
idx = text.find('GĐ 8')
if idx == -1:
    idx = text.find('Giai đoạn 8')
if idx == -1:
    idx = text.find('ĐIỆN CỰC')
if idx == -1:
    idx = text.find('Chế tạo điện cực')

print(f"Found at index: {idx}")
if idx >= 0:
    print(text[idx:idx+4000])
