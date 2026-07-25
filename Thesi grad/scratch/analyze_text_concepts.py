import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def find_terms(filepath, terms):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    found = {}
    for term in terms:
        matches = list(re.finditer(r'(?i)' + re.escape(term), content))
        if matches:
            found[term] = len(matches)
    return found

def main():
    docx_md = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\docx_converted.md"
    terms = [
        "Cellulose III", "Cellulose I", "hornification", "sụp vách", "vách xốp", 
        "hydrophobic", "stacking", "vòng glucopyranoside", "DLVO", "lực đẩy lớp kép",
        "1730", "1737", "lignin", "hemicellulose", "acid leaching", "Fe-N",
        "1.5 Å", "phthalocyanine", "chelate", "solvat hóa"
    ]
    
    found_terms = find_terms(docx_md, terms)
    print("--- CÁC THUẬT NGỮ KHOA HỌC TRONG FILE WORD ---")
    for term in terms:
        count = found_terms.get(term, 0)
        print(f"Thuật ngữ '{term}': {count} lần xuất hiện.")

if __name__ == '__main__':
    main()
