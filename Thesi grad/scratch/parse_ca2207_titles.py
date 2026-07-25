import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

log_path = r"C:\Users\ADMIN\.gemini\antigravity\brain\a0372ab0-fcf7-4d29-b4f1-e005dcc141ca\.system_generated\tasks\task-1610.log"

with open(log_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract filenames ending in .pdf
filenames = re.findall(r'"([^"]+\.pdf)"', content)

print("=== PAPERS IN CA 22.07 ===")
for i, name in enumerate(sorted(set(filenames))):
    print(f"{i+1}. {name}")
