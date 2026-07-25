import sys, io, re, json, time
import urllib.request
import urllib.parse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from docx import Document
from docx.oxml import OxmlElement

def get_doi(ref_text):
    # Strip the leading [1] 
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

docx_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.docx"
doc = Document(docx_path)

# Find biblio range
start = -1
end = -1
for i, p in enumerate(doc.paragraphs):
    if 'TÀI LIỆU THAM KHẢO' in p.text.upper():
        start = i
    if 'PHỤ LỤC' in p.text.upper() and start != -1 and i > start:
        end = i
        break

print(f"Biblio range: {start} -> {end}")

# Read current entries
bib_lines = []
for i in range(start + 1, end):
    bib_lines.append(doc.paragraphs[i].text)

print(f"Extracting DOIs for {len(bib_lines)} entries...")
updated_lines = []
added_count = 0

for line in bib_lines:
    if not line.strip():
        continue
    # Check if DOI already exists
    if 'doi:' in line.lower() or 'doi.org' in line.lower():
        updated_lines.append(line)
        continue
        
    print(f"Searching DOI for: {line[:50]}...")
    doi = get_doi(line)
    if doi:
        # Avoid double DOI
        new_line = line.strip()
        if not new_line.endswith('.'):
            new_line += '.'
        new_line += f' doi: {doi}.'
        updated_lines.append(new_line)
        added_count += 1
        print(f" -> Found: {doi}")
    else:
        updated_lines.append(line)
        print(" -> Not found.")
    time.sleep(0.2)  # rate limit

print(f"\nAdded DOIs to {added_count} references. Updating DOCX...")

# Update DOCX (using the forward addnext method)
to_remove = [doc.paragraphs[i]._element for i in range(start + 1, end)]
for elem in to_remove:
    elem.getparent().remove(elem)

heading_elem = doc.paragraphs[start]._element
for line in updated_lines:
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
print("DOCX updated with DOIs successfully!")
