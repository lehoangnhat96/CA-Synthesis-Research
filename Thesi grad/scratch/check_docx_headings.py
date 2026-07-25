import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document(r"DCLV_CA_02.07 Fe-N CA.docx")
for i, p in enumerate(doc.paragraphs):
    text = p.text.strip().upper()
    if text in ['MỤC LỤC', 'MỞ ĐẦU', 'TÓM TẮT', 'ABSTRACT', 'TÀI LIỆU THAM KHẢO']:
        print(f"Para {i}: {text}")
