import re
import sys

file_path = sys.argv[1]

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split('## TÀI LIỆU THAM KHẢO')
body = parts[0] if len(parts) > 1 else text

matches = re.finditer(r'\[(.*?)\]', body)

citations = []
suspicious = []

for match in matches:
    content = match.group(1).strip()
    if re.fullmatch(r'[\d\s,\-]+', content):
        citations.append(match.group(0))
    else:
        if any(char.isdigit() for char in content):
            suspicious.append(match.group(0))

with open('suspicious_brackets.txt', 'w', encoding='utf-8') as out:
    out.write('--- VALID CITATIONS FOUND ---\n')
    for i, c in enumerate(citations[:10]):
        out.write(f"{i+1}: {c}\n")
    out.write(f"... and {len(citations) - 10} more. Total: {len(citations)}\n\n")
    
    out.write('--- SUSPICIOUS BRACKETS WITH NUMBERS ---\n')
    for s in suspicious:
        out.write(f"{s}\n")
