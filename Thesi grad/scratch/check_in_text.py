import docx
import re
doc = docx.Document('DCLV_CA_29.06 Fe-N CA_Reordered_V2.docx')
with open('out_17_19_33.txt', 'w', encoding='utf-8') as f:
    for p in doc.paragraphs:
        if re.search(r'\[.*?(17|19|33).*?\]', p.text):
            f.write(p.text[:200] + '\n')
