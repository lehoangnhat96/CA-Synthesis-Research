import re

file_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.md"
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(?m)^# TÀI LIỆU THAM KHẢO', text)
body = parts[0]

all_nums = []
for m in re.finditer(r'\[([0-9,\s\-]+)\]', body):
    inner = m.group(1).replace(' ', '')
    for p in inner.split(','):
        if '-' in p:
            start_s, end_s = p.split('-')
            all_nums.extend(range(int(start_s), int(end_s)+1))
        else:
            all_nums.append(int(p))

seen = set()
first_app = []
for n in all_nums:
    if n not in seen:
        seen.add(n)
        first_app.append(n)

print("First 15 from md_validator logic:")
print(first_app[:15])

# Compare with my logic
my_nums = []
for m in re.finditer(r'(\\*\[)([0-9,\s\-]+)(\\*\])', body):
    inner = m.group(2).replace(' ', '')
    for p in inner.split(','):
        if '-' in p:
            start_s, end_s = p.split('-')
            my_nums.extend(range(int(start_s), int(end_s)+1))
        else:
            my_nums.append(int(p))

my_seen = set()
my_first_app = []
for n in my_nums:
    if n not in my_seen:
        my_seen.add(n)
        my_first_app.append(n)

print("\nFirst 15 from my logic:")
print(my_first_app[:15])

for idx, (a, b) in enumerate(zip(first_app, my_first_app)):
    if a != b:
        print(f"Mismatch at position {idx+1}: md_validator got {a}, I got {b}")
        break

