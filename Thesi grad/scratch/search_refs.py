import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\docx_converted.md", 'r', encoding='utf-8') as f:
    text = f.read()

# Find any paragraph containing [23] or [54]
paragraphs = text.split('\n\n')
for p in paragraphs:
    if '[23]' in p or '[54]' in p:
        print("MATCH:", p)
        print("-" * 50)
