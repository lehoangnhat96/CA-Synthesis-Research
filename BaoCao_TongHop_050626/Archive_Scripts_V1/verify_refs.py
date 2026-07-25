import re
import urllib.request
import json
import time
import os

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

def get_openalex_data(doi):
    doi_clean = doi.replace('doi:', '').replace('DOI:', '').strip()
    if doi_clean.startswith('10.'):
        url = f"https://api.openalex.org/works/https://doi.org/{doi_clean}"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                return data
        except Exception as e:
            return None
    return None

def format_ieee(work):
    authors = work.get('authorships', [])
    author_strs = []
    for a in authors:
        name = a['author']['display_name']
        parts = name.split()
        if len(parts) > 1:
            initials = " ".join([p[0] + "." for p in parts[:-1]])
            author_strs.append(f"{initials} {parts[-1]}")
        else:
            author_strs.append(name)
    
    if len(author_strs) > 6:
        author_text = ", ".join(author_strs[:3]) + ", et al."
    elif len(author_strs) > 1:
        author_text = ", ".join(author_strs[:-1]) + ", and " + author_strs[-1]
    elif len(author_strs) == 1:
        author_text = author_strs[0]
    else:
        author_text = "Unknown"

    title = work.get('title', '')
    journal = work.get('primary_location', {}).get('source', {}).get('display_name', '')
    year = work.get('publication_year', '')
    vol = work.get('volume', '')
    issue = work.get('issue', '')
    
    # Try to get pages
    pages = ""
    biblio = work.get('biblio', {})
    if biblio.get('first_page') and biblio.get('last_page'):
        pages = f"pp. {biblio.get('first_page')}-{biblio.get('last_page')}"
    elif biblio.get('first_page'):
        pages = f"p. {biblio.get('first_page')}"
        
    doi = work.get('doi', '').replace('https://doi.org/', '')

    citation = f"{author_text}, \"{title},\" *{journal}*"
    if vol:
        citation += f", vol. {vol}"
    if issue:
        citation += f", no. {issue}"
    if pages:
        citation += f", {pages}"
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
        doi = doi_match.group(0)
        work = get_openalex_data(doi)
        if work:
            ieee_cite = f"[{idx}] {format_ieee(work)}"
            results.append({"idx": idx, "original": ref, "ieee": ieee_cite, "status": "success"})
        else:
            results.append({"idx": idx, "original": ref, "ieee": "", "status": "not_found"})
    else:
        results.append({"idx": idx, "original": ref, "ieee": "", "status": "no_doi"})
    time.sleep(0.1)

with open("refs_correction.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Done")
