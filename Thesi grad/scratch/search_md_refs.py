import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

terms = ["hornification", "phthalocyanine"]

search_dir = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials\md_references"

for file in os.listdir(search_dir):
    if file.endswith('.md'):
        path = os.path.join(search_dir, file)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                for term in terms:
                    if term in content:
                        print(f"FOUND '{term}' in {file}")
                        # Extract context
                        lines = content.split('\n')
                        for i, line in enumerate(lines):
                            if term in line:
                                print(f"  Line {i+1}: {line.strip()}")
        except Exception as e:
            pass
