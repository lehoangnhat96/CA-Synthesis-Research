import sys, io, re, json
import urllib.request
import urllib.parse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def get_doi(ref_text):
    # Clean up the reference text for better search
    query = re.sub(r'^\[\d+\]\s*', '', ref_text)
    url = "https://api.crossref.org/works?query.bibliographic=" + urllib.parse.quote(query) + "&rows=1&select=DOI,score,title"
    
    req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            items = data.get('message', {}).get('items', [])
            if items and items[0].get('score', 0) > 40: # threshold for matching
                return items[0].get('DOI')
    except Exception as e:
        pass
    return None

test_ref = '[43] H. Li, R. Zhao, P. Li, et al., "Ultra-lightweight, robust and flexible porous carbon monoliths from biomass aerogels," J. Mater. Chem. A, vol. 8, pp. 22292-22301, 2020.'
print("Testing DOI search...")
doi = get_doi(test_ref)
print("Found DOI:", doi)
