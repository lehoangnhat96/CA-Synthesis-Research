import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\docx_converted.md", 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'(.{0,100}lộ trình phức hợp.{0,100})', text, re.IGNORECASE)
for m in matches:
    print("DOCX MATCH:", m.group(1))
    
matches2 = re.finditer(r'(.{0,100}amoniac-cellulose.{0,100})', text, re.IGNORECASE)
for m in matches2:
    print("DOCX MATCH 2:", m.group(1))

with open(r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md", 'r', encoding='utf-8') as f2:
    text2 = f2.read()

matches3 = re.finditer(r'(.{0,100}amoniac-cellulose.{0,100})', text2, re.IGNORECASE)
for m in matches3:
    print("DRAFT MATCH:", m.group(1))

