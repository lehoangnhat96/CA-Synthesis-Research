import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_11.07 Fe-N CA_Renumbered.md", 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(?m)^# TÀI LIỆU THAM KHẢO', text)
body = parts[0]
bib = parts[1] if len(parts) > 1 else ''

# Extract bib details
for line in bib.split('\n'):
    if line.startswith('[2]') or line.startswith('[20]'):
        print(f"BIBLIO:\n{line.strip()}\n")

# Extract citations in body
lines = body.split('\n')
for i, line in enumerate(lines):
    # Regex to find [2] or within [1, 2] or [2, 3] or [1-3]
    if re.search(r'\[2\]|\[\d+,\s*2\]|\[2,\s*\d+\]|\[1-\d+\]', line):
        print(f"CITED [2] at Line {i+1}:")
        print(line.strip())
        print()
    if re.search(r'\[20\]|\[\d+,\s*20\]|\[20,\s*\d+\]|\[(?:1[0-9]|20)-\d+\]', line):
        print(f"CITED [20] at Line {i+1}:")
        print(line.strip())
        print()
