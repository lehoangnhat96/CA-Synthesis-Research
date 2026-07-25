import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def check_parameters(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    results = []
    
    # Check LOD
    results.append("LOD Pb: " + str(bool(re.search(r'0\.1\s*(ppb|µg/L)', content))))
    results.append("LOD Cd: " + str(bool(re.search(r'0\.2\s*(ppb|µg/L)', content))))
    results.append("LOD Zn: " + str(bool(re.search(r'0\.5\s*(ppb|µg/L)', content))))
    
    # Check pH
    results.append("pH 4.5: " + str(bool(re.search(r'pH.*4\.5', content))))
    
    # Check calcination temperature (750 vs 800)
    results.append("Nung 750C: " + str(bool(re.search(r'750\s*°C', content))))
    results.append("Nung 800C: " + str(bool(re.search(r'800\s*°C', content))))
    
    return results

print("--- DOCX ---")
print("\n".join(check_parameters(r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\docx_converted.md")))

print("\n--- ORIG MD ---")
print("\n".join(check_parameters(r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md")))
