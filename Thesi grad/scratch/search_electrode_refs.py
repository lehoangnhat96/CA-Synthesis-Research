import sys

sys.stdout.reconfigure(encoding='utf-8')

# Search all md_references files for concrete electrode parameters
ref_dir = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials\md_references"
import os

keywords_electrode = ['mg/mL', 'mg mL', 'μL', 'µL', 'uL', 'Nafion', 'nafion',
                      'chitosan', 'GCE', 'glassy carbon', 'drop cast', 'drop-cast',
                      'suspension', 'dispersion', 'sonication', 'PBS', 'buffer',
                      'scan rate', 'KCl', 'ferricyanide', 'DPV', 'CV', 'EIS',
                      '0.5%', '0.5 %', '1 mg', '2 mg', '5 mg', 'ethanol',
                      'acetate', 'pH 7', 'modified electrode']

for file in sorted(os.listdir(ref_dir)):
    if file.endswith('.md'):
        path = os.path.join(ref_dir, file)
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if any(kw.lower() in line.lower() for kw in keywords_electrode):
                # Print 2 lines of context
                context_start = max(0, i-1)
                context_end = min(len(lines), i+2)
                print(f"\n[{file} | Line {i+1}]")
                for cl in lines[context_start:context_end]:
                    print("  " + cl.rstrip())
