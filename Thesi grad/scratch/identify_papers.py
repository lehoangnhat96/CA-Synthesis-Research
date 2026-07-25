import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ref_dir = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials\md_references"

phrases = {
    'chitosan_2g': '2.0 g',
    'acetic_017': '0.17',
    'chit_cnt_nafion': 'Chit-CNT',
    'priority_hg_cu': 'Hg', # will check manually
    'cu_lod_383': '3.83',
    'zn_ni_peak': '1.059',
    'zn_ni_peak2': '0.897'
}

for file in os.listdir(ref_dir):
    if not file.endswith('.md'): continue
    path = os.path.join(ref_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for k, phrase in phrases.items():
        if phrase in content:
            # find the line
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if phrase in line:
                    print(f"[{file}] {k}: {line.strip()[:150]}")
