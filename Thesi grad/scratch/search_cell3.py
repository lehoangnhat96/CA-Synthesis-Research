import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\docx_converted.md", 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'(.{0,80}Cellulose III.{0,80})', text, re.IGNORECASE)
for i, m in enumerate(matches):
    print(f"MATCH {i}:", m.group(1).replace('\n', ' '))
