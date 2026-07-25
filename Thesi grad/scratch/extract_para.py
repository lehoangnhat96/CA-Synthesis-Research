import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\docx_converted.md", 'r', encoding='utf-8') as f:
    text = f.read()

paragraphs = text.split('\n\n')
for i, p in enumerate(paragraphs):
    if 'lộ trình phức hợp amoniac-cellulose' in p:
        print(f"PARAGRAPH {i}:")
        print(p)
        print("-" * 50)
