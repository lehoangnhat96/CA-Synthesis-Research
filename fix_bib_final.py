import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

docx_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.docx"
doc = Document(docx_path)

start = -1
end = -1
for i, p in enumerate(doc.paragraphs):
    if 'TÀI LIỆU THAM KHẢO' in p.text.upper():
        start = i
    if 'PHỤ LỤC' in p.text.upper() and start != -1 and i > start:
        end = i
        break

print(f"Biblio range: {start} -> {end}, current entries: {end - start - 1}")

# Read correct bibliography
with open("D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DANH_MUC_MOI.txt", 'r', encoding='utf-8-sig') as f:
    bib_lines = [l.strip() for l in f if l.strip()]

print(f"New bib has {len(bib_lines)} entries. First: {bib_lines[0][:60]}")

# Remove all current bibliography paragraphs (start+1 to end-1)
to_remove = [doc.paragraphs[i]._element for i in range(start + 1, end)]
for elem in to_remove:
    elem.getparent().remove(elem)

phu_luc_elem = doc.paragraphs[start + 1]._element  # now this is PHU LUC after removal

# Insert in FORWARD order using addprevious: each new para goes before PHU LUC
# Since addprevious inserts immediately before, do in REVERSE so final order is correct
for line in reversed(bib_lines):
    new_p = OxmlElement('w:p')
    new_r = OxmlElement('w:r')
    new_t = OxmlElement('w:t')
    new_t.text = line
    new_t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    new_r.append(new_t)
    new_p.append(new_r)
    phu_luc_elem.addprevious(new_p)

doc.save(docx_path)

# Verify
doc2 = Document(docx_path)
start2 = -1
end2 = -1
for i, p in enumerate(doc2.paragraphs):
    if 'TÀI LIỆU THAM KHẢO' in p.text.upper():
        start2 = i
    if 'PHỤ LỤC' in p.text.upper() and start2 != -1 and i > start2:
        end2 = i
        break

print(f"\nAfter fix - Biblio range: {start2} -> {end2}, entries: {end2 - start2 - 1}")
print("First entry:", doc2.paragraphs[start2 + 1].text[:80])
print("Last entry:", doc2.paragraphs[end2 - 1].text[:80])
