import re

files_to_check = [
    "Phan2_QuyTrinh_8Buoc_SOP_ChiTiet.md",
    "03_LuanAn_KeThua_ThaoTac_va_CoChe_ChiTiet.md",
    "DCLV_CA_19.06 Fe-N CA.md",
    "Master_Thesis_Full_Draft.md"
]

report = ""

def extract_citations(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # We want to find patterns like [1], [1, 2], [1-4], [P-019_Fe_Doped_Algae_CAs], etc.
        # But avoid things like Markdown links [text](url) or alerts [!WARNING]
        
        # Remove code blocks
        content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        
        # Find all brackets
        raw_matches = re.findall(r'\[([^\]]+)\]', content)
        
        citations = []
        for match in raw_matches:
            if match.startswith('!'): continue # alert
            if match.startswith('^'): continue # footnote
            
            # If it's a number, a range, or starts with P-, it's likely a citation
            if re.match(r'^[\d\s,\-]+$', match) or match.startswith('P-') or match.startswith('Sách_'):
                citations.append(match.strip())
                
        return citations
    except Exception as e:
        return [f"ERROR: {e}"]

report += "==== CITATIONS FOUND IN FILES ====\n\n"

for fp in files_to_check:
    cites = extract_citations(fp)
    unique_cites = sorted(list(set(cites)))
    report += f"--- {fp} ---\n"
    if unique_cites:
        for c in unique_cites:
            report += f"- [{c}]\n"
    else:
        report += "No citations found.\n"
    report += "\n"

# Extract the 25 references from Master_Thesis_Full_Draft
try:
    with open("Master_Thesis_Full_Draft.md", "r", encoding="utf-8") as f:
        master_content = f.read()
        ref_section = master_content.split("# TÀI LIỆU THAM KHẢO")[1]
        
        report += "--- GOLDEN REFERENCES IN MASTER THESIS ---\n"
        for line in ref_section.strip().split('\n'):
            line = line.strip()
            if line.startswith('[') and ']' in line:
                report += f"{line}\n"
except Exception as e:
    report += f"Error reading golden references: {e}\n"

with open("refs_comparison_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("Comparison report generated.")
