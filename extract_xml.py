import zipfile
import re

docx_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA.docx"
with zipfile.ZipFile(docx_path, 'r') as z:
    xml = z.read('word/document.xml').decode('utf-8')

# Find the paragraph XML block containing "Thuyết Kén phân tử"
matches = re.findall(r'<w:p[ >].*?Thuyết.*?Kén.*?phân.*?tử.*?</w:p>', xml)
if matches:
    print("Found Paragraph 1!")
    with open('p1.xml', 'w', encoding='utf-8') as f:
        f.write(matches[0])
else:
    print("Not found P1")

matches2 = re.findall(r'<w:p[ >].*?Quá.*?trình.*?hòa.*?tan.*?là.*?phản.*?ứng.*?tỏa.*?nhiệt.*?</w:p>', xml)
if matches2:
    print("Found Paragraph 2!")
    with open('p2.xml', 'w', encoding='utf-8') as f:
        f.write(matches2[0])
else:
    print("Not found P2")
