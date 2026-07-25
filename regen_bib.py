import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Read bib_raw to get all entries
with open("D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/bib_raw.txt", 'r', encoding='utf-8') as f:
    bib_raw = f.read()

# Parse all entries from bib_raw
old_bib = {}
for m in re.finditer(r'\[(\d+)\]\s+(.+?)(?=\n\[\d+\]|\Z)', bib_raw, re.DOTALL):
    old_bib[int(m.group(1))] = m.group(2).strip().replace('\n', ' ')

print(f"Parsed {len(old_bib)} entries from bib_raw")
print("Sample [1]:", repr(old_bib.get(1, 'NOT FOUND')[:100]))

# Read renumbered MD to build old->new mapping
with open("D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.md", 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(?m)^# TÀI LIỆU THAM KHẢO', text)
bib_section = parts[1] if len(parts) > 1 else ''

# Parse the new bibliography to get new_id -> text
new_bib = {}
for m in re.finditer(r'\[(\d+)\]\s+(.+?)(?=\n\[\d+\]|\n#|\Z)', bib_section, re.DOTALL):
    new_bib[int(m.group(1))] = m.group(2).strip().replace('\n', ' ')

print(f"Parsed {len(new_bib)} entries from Renumbered MD bibliography")
print("Sample new[1]:", repr(new_bib.get(1, 'NOT FOUND')[:100]))

# Check if [1] in new bib contains MISSING
for k, v in sorted(new_bib.items()):
    if 'MISSING' in v:
        print(f"MISSING found at new [{k}]: {repr(v)}")

# Actually build the correct bibliography from scratch
# using the BODY of the renumbered MD to get old->new mapping, then pull text from bib_raw
body = parts[0]

old_to_new = {}
next_new_id = 1
pattern2 = r'(?:\\?\[)([0-9,\s\-]+)(?:\\?\])'
for m in re.finditer(pattern2, body):
    inner = m.group(1).replace(' ', '')
    for p in inner.split(','):
        if '-' in p:
            a, b = p.split('-')
            for num in range(int(a), int(b) + 1):
                if num not in old_to_new:
                    old_to_new[num] = next_new_id
                    next_new_id += 1
        else:
            num = int(p)
            if num not in old_to_new:
                old_to_new[num] = next_new_id
                next_new_id += 1

new_to_old = {v: k for k, v in old_to_new.items()}
print(f"\nMapping: {len(old_to_new)} entries built")
print("Old->New [1]:", old_to_new.get(1, 'NOT IN MAPPING'))
print("new[1] comes from old:", new_to_old.get(1, 'N/A'))

# Build the final bibliography in order new[1]...new[69]
max_new = max(new_to_old.keys())
final_lines = []
missing_ids = []
for new_id in range(1, max_new + 1):
    old_id = new_to_old.get(new_id)
    if old_id and old_id in old_bib:
        final_lines.append(f"[{new_id}] {old_bib[old_id]}")
    elif old_id:
        final_lines.append(f"[{new_id}] [OLD_ID {old_id} NOT IN BIB_RAW]")
        missing_ids.append(new_id)
    else:
        final_lines.append(f"[{new_id}] [NEW_ID {new_id} HAS NO OLD MAPPING]")
        missing_ids.append(new_id)

print(f"\nFinal bib has {len(final_lines)} entries. Missing: {missing_ids}")
print("First 3:", final_lines[:3])

# Also add the new entries that don't exist in old bib (52=Xiong, 53=Cai DSC)
# These need to be inserted from the Renumbered MD bibliography
for new_id in missing_ids:
    if new_id in new_bib and 'MISSING' not in new_bib[new_id]:
        final_lines[new_id - 1] = f"[{new_id}] {new_bib[new_id]}"
        print(f"Recovered new[{new_id}] from Renumbered MD bib")
    else:
        # Check if it's in the bib_section directly  
        print(f"Still missing: [{new_id}] old_id={new_to_old.get(new_id)}")

with open("D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DANH_MUC_MOI.txt", 'w', encoding='utf-8-sig') as f:
    f.write('\n'.join(final_lines))

print("\nDANH_MUC_MOI.txt regenerated correctly!")
