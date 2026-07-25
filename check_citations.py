import re

file_path = 'D:/1 Master''s Ana Chem/1 Master''s thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.md'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

body, bib = text.split('## TÀI LIỆU THAM KHẢO')

# Find all citations like [1], [2, 3], [1-3]
cites = re.findall(r'\[(\d+(?:,\s*\d+|-\d+)*)\]', body)

seen = []
for cite in cites:
    parts = []
    if '-' in cite:
        start, end = map(int, cite.split('-'))
        parts.extend(range(start, end+1))
    else:
        parts.extend([int(x.strip()) for x in cite.split(',')])
    
    for num in parts:
        if num not in seen:
            seen.append(num)

print('First 15 appearance order:', seen[:15])
print('Total unique citations in text:', len(seen))

expected = list(range(1, len(seen)+1))
mismatches = [(i+1, seen[i]) for i in range(len(seen)) if seen[i] != expected[i]]
print('Mismatches (Expected vs Actual):', mismatches[:10])
