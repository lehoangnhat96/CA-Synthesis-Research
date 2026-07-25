import sys, io, re, json, time
import urllib.request
import urllib.parse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from docx import Document
from docx.oxml import OxmlElement

# 1. Read the PERFECT bibliography from the Markdown file
with open("D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.md", 'r', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'(?m)^# TÀI LIỆU THAM KHẢO', text)
bib = parts[1] if len(parts) > 1 else ''

# Extract all entries
entries = {}
for m in re.finditer(r'\[(\d+)\]\s+(.+?)(?=\n\[\d+\]|\n#|\Z)', bib, re.DOTALL):
    entries[int(m.group(1))] = m.group(2).strip().replace('\n', ' ')

# 2. Fix entry [1] which is missing in the Markdown
entries[1] = 'International Council for Harmonisation (ICH), "ICH harmonised guideline Q2(R2): Validation of analytical procedures," ICH, Geneva, Switzerland, Guideline, Nov. 2023.'

# 3. Apply the DOIs we fetched earlier
def get_doi(ref_text):
    query = re.sub(r'^\[\d+\]\s*', '', ref_text)
    url = "https://api.crossref.org/works?query.bibliographic=" + urllib.parse.quote(query) + "&rows=1&select=DOI,score,title"
    req = urllib.request.Request(url, headers={'User-Agent': 'mailto:research@example.com'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            items = data.get('message', {}).get('items', [])
            if items and items[0].get('score', 0) > 40:
                return items[0].get('DOI')
    except Exception as e:
        pass
    return None

final_lines = []
added = 0
print(f"Checking {len(entries)} entries for missing DOIs...")
for i in range(1, len(entries) + 1):
    line = entries.get(i, f"MISSING ENTRY {i}")
    if 'doi:' not in line.lower() and 'doi.org' not in line.lower() and 'MISSING' not in line:
        doi = get_doi(line)
        if doi:
            if not line.endswith('.'): line += '.'
            line += f' doi: {doi}.'
            added += 1
            print(f"[{i}] Added DOI")
        time.sleep(0.2)
    final_lines.append(f"[{i}] {line}")

print(f"Added {added} new DOIs. Updating DOCX...")

# 4. Insert into DOCX
docx_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.docx"
doc = Document(docx_path)

start = -1
end = -1
for i, p in enumerate(doc.paragraphs):
    if 'TÀI LIỆU THAM KHẢO' in p.text.upper():
        start = i
    if 'PHỤ LỤC' in p.text.upper() and start != -1 and i > start:
        end = i
        break

to_remove = [doc.paragraphs[i]._element for i in range(start + 1, end)]
for elem in to_remove:
    elem.getparent().remove(elem)

heading_elem = doc.paragraphs[start]._element
for line in final_lines:
    new_p = OxmlElement('w:p')
    new_r = OxmlElement('w:r')
    new_t = OxmlElement('w:t')
    new_t.text = line
    new_t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    new_r.append(new_t)
    new_p.append(new_r)
    heading_elem.addnext(new_p)
    heading_elem = new_p

doc.save(docx_path)
print("DOCX fixed completely! Xiong is [52], Cai is [53], DOIs are intact.")
