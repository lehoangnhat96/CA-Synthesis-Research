import docx
doc = docx.Document('DCLV_CA_29.06 Fe-N CA_Reordered_V2.docx')
in_refs = False
with open('out_biblio.txt', 'w', encoding='utf-8') as f:
    for p in doc.paragraphs:
        if 'TÀI LIỆU THAM KHẢO' in p.text:
            in_refs = True
            continue
        if in_refs:
            f.write(p.text[:100] + '\n')
