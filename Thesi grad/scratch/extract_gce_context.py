import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md", 'r', encoding='utf-8') as f:
    text = f.read()

paragraphs = text.split('\n\n')
for p in paragraphs:
    if 'GCE' in p or 'Nafion' in p or 'màng' in p or 'điện cực' in p:
        print('---')
        print(p.strip())
