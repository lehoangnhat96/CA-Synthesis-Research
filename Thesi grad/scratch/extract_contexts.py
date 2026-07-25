import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_contexts(filepath, keywords, window=3):
    with open(filepath, 'r', encoding='utf-8') as f:
        paragraphs = f.read().split('\n\n')
        
    results = {}
    for kw in keywords:
        results[kw] = []
        for idx, p in enumerate(paragraphs):
            if re.search(r'(?i)' + re.escape(kw), p):
                # Get a window of paragraphs
                start = max(0, idx - 1)
                end = min(len(paragraphs), idx + 2)
                context = "\n\n".join(paragraphs[start:end])
                results[kw].append((idx, context))
    return results

def main():
    docx_md = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\docx_converted.md"
    keywords = ["FTIR", "Cellulose III", "Fe-N", "sấy thăng hoa", "gel hóa"]
    
    contexts = extract_contexts(docx_md, keywords)
    
    with open(r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\extracted_contexts.txt", 'w', encoding='utf-8') as out:
        for kw, matches in contexts.items():
            out.write(f"=========================================\n")
            out.write(f"KEYWORD: {kw} (Found {len(matches)} times)\n")
            out.write(f"=========================================\n")
            # Write first 3 occurrences to keep it concise
            for idx, ctx in matches[:3]:
                out.write(f"[Paragraph index {idx}]:\n{ctx}\n\n")

if __name__ == '__main__':
    main()
