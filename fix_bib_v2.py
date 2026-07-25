import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from docx import Document
from docx.oxml.ns import qn
from lxml import etree
import re

docx_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.docx"
doc = Document(docx_path)

# Tìm vị trí đầu và cuối vùng tài liệu tham khảo
start = -1
end = -1
for i, p in enumerate(doc.paragraphs):
    if 'TÀI LIỆU THAM KHẢO' in p.text.upper():
        start = i
    if 'PHỤ LỤC' in p.text.upper() and start != -1 and i > start:
        end = i
        break

print(f"Biblio range: {start} -> {end}")

# Đọc file DANH_MUC mới
with open("D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DANH_MUC_MOI.txt", 'r', encoding='utf-8-sig') as f:
    bib_lines = [l.strip() for l in f.readlines() if l.strip()]

print(f"New bibliography has {len(bib_lines)} entries")

# Lấy style của paragraph đầu tiên trong vùng biblio (phần tử ngay sau heading)
# Để tái dùng cho các entry mới
# Tìm một entry cũ (nếu còn) để lấy style name -- đã bị xóa hết rồi nên dùng 'List Paragraph' hoặc 'Normal'
bib_style_name = doc.paragraphs[start + 1].style.name  # thường là 'Normal'
print(f"Using style: {bib_style_name}")

# Xóa tất cả các paragraph rỗng trong vùng biblio (từ start+1 đến end-1)
# Để làm điều này an toàn: lấy element cha (body), rồi xóa các w:p elements trong range đó
body = doc.element.body
all_paras = body.findall(qn('w:p'))
print(f"Total w:p in body: {len(all_paras)}")

# Xác định các elements cần xóa
to_remove = []
for i in range(start + 1, end):
    p_elem = doc.paragraphs[i]._element
    to_remove.append(p_elem)

print(f"Removing {len(to_remove)} old empty paragraphs")

# Lưu reference đến paragraph PHỤ LỤC để chèn trước nó
phu_luc_elem = doc.paragraphs[end]._element

# Xóa các paragraphs cũ
for elem in to_remove:
    elem.getparent().remove(elem)

# Chèn các entry mới vào trước phần PHỤ LỤC
# Cần làm ngược từ cuối để thứ tự đúng với insert_before
from docx.oxml import OxmlElement
from copy import deepcopy

# Lấy namespace
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

for line in reversed(bib_lines):
    # Tạo paragraph mới
    new_p = OxmlElement('w:p')
    new_r = OxmlElement('w:r')
    new_t = OxmlElement('w:t')
    new_t.text = line
    new_t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    new_r.append(new_t)
    new_p.append(new_r)
    
    # Chèn trước phần PHỤ LỤC
    phu_luc_elem.addprevious(new_p)

doc.save(docx_path)
print("Bibliography re-inserted successfully!")
