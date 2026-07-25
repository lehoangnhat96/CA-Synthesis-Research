import os

f1 = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\Phan2_QuyTrinh_8Buoc_SOP_ChiTiet.md"
f2 = r"C:\Users\ADMIN\.gemini\antigravity\brain\0726e7c6-fe20-4423-a0eb-a1f928b783bf\SOP_Final_Snapshot.md"

with open(f1, 'r', encoding='utf-8') as f:
    lines1 = f.readlines()
with open(f2, 'r', encoding='utf-8') as f:
    lines2 = f.readlines()

print('Lines in Phan2 (Current):', len(lines1))
print('Lines in Snapshot (Backup):', len(lines2))

# Check headings
h1 = [l.strip() for l in lines1 if l.startswith('#')]
h2 = [l.strip() for l in lines2 if l.startswith('#')]

missing = [h for h in h2 if h not in h1]
if missing:
    print('Missing headings in Current compared to Snapshot:')
    for h in missing: 
        print("  " + h.encode('ascii', 'replace').decode('ascii'))
else:
    print('No headings lost!')

import difflib
diff = list(difflib.unified_diff(lines2, lines1, fromfile='Snapshot', tofile='Current', n=0))
add = sum(1 for l in diff if l.startswith('+') and not l.startswith('+++'))
rem = sum(1 for l in diff if l.startswith('-') and not l.startswith('---'))

print(f"Added lines: {add}")
print(f"Removed lines: {rem}")
