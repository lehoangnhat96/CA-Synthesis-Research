import json

file_path = "Master_Thesis_Full_Draft.md"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("refs_correction2.json", "r", encoding="utf-8") as f:
    results = json.load(f)

for item in results:
    if item['status'] == 'success' and item['ieee']:
        content = content.replace(item['original'], item['ieee'])

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
