import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from docx import Document

docx_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.docx"
doc = Document(docx_path)

body_text = []
bib_text = []

in_bib = False
for p in doc.paragraphs:
    if 'TÀI LIỆU THAM KHẢO' in p.text.upper():
        in_bib = True
    elif 'PHỤ LỤC' in p.text.upper() and in_bib:
        in_bib = False
        
    if in_bib:
        bib_text.append(p.text)
    else:
        body_text.append(p.text)

body_full = '\n'.join(body_text)
bib_full = '\n'.join(bib_text)

# Extract citations from body
# We look for [1], [1, 2], [1-3]
body_nums = set()
for m in re.finditer(r'\[([0-9,\s\-]+)\]', body_full):
    inner = m.group(1).replace(' ', '')
    for part in inner.split(','):
        if '-' in part:
            try:
                start, end = map(int, part.split('-'))
                for n in range(start, end + 1):
                    body_nums.add(n)
            except ValueError:
                pass
        else:
            try:
                body_nums.add(int(part))
            except ValueError:
                pass

# Extract citations from bibliography
bib_nums = set()
for m in re.finditer(r'^\[(\d+)\]', bib_full, re.MULTILINE):
    bib_nums.add(int(m.group(1)))

orphans_in_body = body_nums - bib_nums
orphans_in_bib = bib_nums - body_nums

print(f"Total cited in body: {len(body_nums)}")
print(f"Total entries in bib: {len(bib_nums)}")
print(f"Orphans in body (cited but no bib entry): {orphans_in_body}")
print(f"Orphans in bib (has bib entry but never cited): {orphans_in_bib}")
