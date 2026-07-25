import sys

sys.stdout.reconfigure(encoding='utf-8')

draft_path = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md"

with open(draft_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Update Chitosan concentration to 2 wt% (2g / 100 mL acetic 0.17M)
text = text.replace("Chitosan 1 wt%", "Chitosan 2 wt% (2.0 g/100 mL acetic acid 0.17 M)")
text = text.replace("Chitosan 1%", "Chitosan 2%")

with open(draft_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated draft with verified Chitosan parameters.")
