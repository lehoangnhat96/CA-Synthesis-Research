import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md", 'r', encoding='utf-8') as f:
    text = f.read()

# Search for sections related to electrode preparation and measurement setup
paragraphs = text.split('\n\n')
keywords = ['GCE', 'Nafion', 'Chitosan', 'binder', 'kết dính', 'mg/mL', 'µL', 'μL',
            'PBS', 'đệm', 'buffer', 'siêu âm', 'sonication', 'CV', 'DPV', 'EIS',
            'quét thế', 'phủ', 'drop', 'cast', 'mực', 'suspension', 'phân tán',
            'bảo quản', 'tủ lạnh', 'KCl', 'Ferricyanide', 'điện cực làm việc', '3.1', '3.2', '3.3']

for p in paragraphs:
    if any(kw.lower() in p.lower() for kw in keywords):
        if len(p.strip()) > 30:
            print('---')
            print(p.strip()[:600])
