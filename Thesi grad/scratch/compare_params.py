import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_parameters(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex extractions
    lods = re.findall(r'(?i)LOD.*?([\d\.]+)\s*(?:ppb|µg/L|nM|uM|M)', content)
    ph = re.findall(r'(?i)pH\s*[:=\s]*([\d\.]+)', content)
    temps = re.findall(r'(?i)(?:nhiệt độ|nhiệt phân|calcination).*?([\d\.]+)\s*(?:°C|C)', content)
    
    return {
        'LODs': lods,
        'pH': set(ph),
        'Temps': set(temps)
    }

def main():
    docx_md = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\docx_converted.md"
    orig_md = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md"
    
    docx_params = extract_parameters(docx_md)
    orig_params = extract_parameters(orig_md)
    
    with open(r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\params_comparison.txt", 'w', encoding='utf-8') as out:
        out.write("--- PARAMETERS IN DOCX (New) ---\n")
        out.write(f"pH: {docx_params['pH']}\n")
        out.write(f"Temperatures: {docx_params['Temps']}\n")
        
        out.write("\n--- PARAMETERS IN MD (Original) ---\n")
        out.write(f"pH: {orig_params['pH']}\n")
        out.write(f"Temperatures: {orig_params['Temps']}\n")

if __name__ == "__main__":
    main()
