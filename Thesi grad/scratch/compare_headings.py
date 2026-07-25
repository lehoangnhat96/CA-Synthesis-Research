import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_headings(filepath):
    headings = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if re.match(r'^#{1,6}\s', line):
                headings.append(line.strip())
    return headings

def main():
    docx_md = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\docx_converted.md"
    orig_md = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md"
    
    docx_headings = get_headings(docx_md)
    orig_headings = get_headings(orig_md)
    
    with open(r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\headings_output_utf8.txt", 'w', encoding='utf-8') as out:
        out.write("--- HEADINGS IN DOCX (New) ---\n")
        for h in docx_headings:
            out.write(h + '\n')
            
        out.write("\n--- HEADINGS IN MD (Original) ---\n")
        for h in orig_headings:
            out.write(h + '\n')

if __name__ == "__main__":
    main()
