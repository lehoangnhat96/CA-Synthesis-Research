import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ref_dir = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials\md_references"

keywords = {
    'chitosan_nafion_ratio': ['chitosan', 'nafion', 'ratio', 'binder', 'composite', 'volume', 'mix'],
    'chitosan_conc': ['chitosan', 'wt%', 'wt %', 'mg/mL', 'acetic', 'dissolved in'],
    'annealing_temp': ['anneal', 'dry', 'dried', 'room temperature', 'oven', 'drop-cast', 'drop cast', 'cast'],
    'cell_volume': ['cell', 'volume', 'mL', 'beaker', 'electrolyte', 'solution']
}

results = {k: [] for k in keywords}

for file in sorted(os.listdir(ref_dir)):
    if file.endswith('.md'):
        path = os.path.join(ref_dir, file)
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for i, line in enumerate(lines):
            line_lower = line.lower()
            if 'ca' not in file.lower() and 'ref' not in file.lower():
                continue # limit to main refs
                
            # Check chitosan & nafion ratio
            if ('chitosan' in line_lower and 'nafion' in line_lower) or ('binder' in line_lower):
                results['chitosan_nafion_ratio'].append(f"[{file}:{i+1}] {line.strip()}")
                
            # Check chitosan concentration
            if 'chitosan' in line_lower and ('%' in line_lower or 'mg/ml' in line_lower or 'mg ml' in line_lower or 'acetic' in line_lower):
                results['chitosan_conc'].append(f"[{file}:{i+1}] {line.strip()}")
                
            # Check annealing temp
            if ('drop-cast' in line_lower or 'drop cast' in line_lower or 'modified electrode' in line_lower) and ('dry' in line_lower or 'dried' in line_lower or 'anneal' in line_lower):
                results['annealing_temp'].append(f"[{file}:{i+1}] {line.strip()}")
                
            # Check cell volume
            if ('cell' in line_lower or 'electrolyte' in line_lower) and 'ml' in line_lower:
                results['cell_volume'].append(f"[{file}:{i+1}] {line.strip()}")

for k, v in results.items():
    print(f"=== {k.upper()} ===")
    for item in v[:20]: # show first 20
        print(item)
    print("\n")
