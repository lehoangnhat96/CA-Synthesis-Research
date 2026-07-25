import re
import urllib.request
import json
import time

file_path = "Master_Thesis_Full_Draft.md"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

ref_section = content.split("# TÀI LIỆU THAM KHẢO")[1]
lines = ref_section.strip().split('\n')

refs = []
for line in lines:
    line = line.strip()
    if line.startswith('[') and ']' in line:
        refs.append(line)

def get_crossref_data(doi):
    doi_clean = doi.strip().rstrip('.')
    url = f"https://api.crossref.org/works/{doi_clean}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data['message']
    except Exception as e:
        return None

def format_ieee_crossref(work):
    authors = work.get('author', [])
    author_strs = []
    for a in authors:
        given = a.get('given', '')
        family = a.get('family', '')
        initials = " ".join([p[0].upper() + "." for p in given.split() if p])
        if family and initials:
            author_strs.append(f"{initials} {family}")
        elif family:
            author_strs.append(family)
        elif given:
            author_strs.append(given)
            
    if len(author_strs) > 6:
        author_text = ", ".join(author_strs[:3]) + ", et al."
    elif len(author_strs) > 1:
        author_text = ", ".join(author_strs[:-1]) + ", and " + author_strs[-1]
    elif len(author_strs) == 1:
        author_text = author_strs[0]
    else:
        author_text = "Unknown"

    title = work.get('title', [''])[0]
    
    container_title = work.get('container-title', [])
    journal = container_title[0] if container_title else ''
    
    published = work.get('published', {}).get('date-parts', [[None]])
    year = published[0][0] if published[0][0] else ''
    
    vol = work.get('volume', '')
    issue = work.get('issue', '')
    pages = work.get('page', '')
    doi = work.get('DOI', '')

    citation = f"{author_text}, \"{title},\" *{journal}*"
    if vol:
        citation += f", vol. {vol}"
    if issue:
        citation += f", no. {issue}"
    if pages:
        citation += f", pp. {pages}"
    if year:
        citation += f", {year}"
    if doi:
        citation += f", doi: {doi}."
    else:
        citation += "."
        
    return citation

results = []
for ref in refs:
    match = re.search(r'\[(\d+)\]', ref)
    idx = match.group(1) if match else "?"
    
    doi_match = re.search(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', ref, re.I)
    if doi_match:
        doi = doi_match.group(0).rstrip('.')
        work = get_crossref_data(doi)
        if work:
            ieee_cite = f"[{idx}] {format_ieee_crossref(work)}"
            results.append({"idx": idx, "original": ref, "ieee": ieee_cite, "status": "success"})
        else:
            results.append({"idx": idx, "original": ref, "ieee": "", "status": "not_found"})
    else:
        results.append({"idx": idx, "original": ref, "ieee": "", "status": "no_doi"})
    time.sleep(0.1)

with open("refs_correction2.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Done generating refs_correction2.json")
