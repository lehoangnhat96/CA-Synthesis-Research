import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

terms = ["hornification", "1.5", "phthalocyanine"]

search_dir = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel"
count = 0

for root, _, files in os.walk(search_dir):
    if '.git' in root or '.venv' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.md') or file.endswith('.txt') or file.endswith('.json'):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        for term in terms:
                            if term.lower() in line.lower():
                                print(f"FOUND '{term}' in {path} (Line {i+1}):")
                                print(line.strip())
                                print("-" * 50)
                                count += 1
                                if count > 50:
                                    break
            except Exception as e:
                pass
