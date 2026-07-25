import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document(r"DCLV_CA_02.07 Fe-N CA.docx")
for i, p in enumerate(doc.paragraphs):
    if 'Fauziyah' in p.text:
        print(f"Para {i}: {p.text[:50]}")
    if 'Theo QCVN' in p.text:
        print(f"Para {i} (QCVN): {p.text[:50]}")
