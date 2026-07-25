import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
filepath = 'DCLV_CA_01.07 Fe-N CA.md'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

table_row = '''<tr>
<td>Nafion/TiO2-graphene/GCE</td>
<td>Paracetamol</td>
<td>Nafion</td>
<td>0.21 µM</td>
<td>1 – 100 µM</td>
<td style="text-align: center;">[65]</td>
</tr>
'''

if '<td>Fe/N-CA</td>' in text:
    text = text.replace('<tr>\n<td>Fe/N-CA</td>', table_row + '<tr>\n<td>Fe/N-CA</td>')
    print('Row 65 added to Table 1.5')

# The text from file is:
# "ph?m có dòng oxi hóa phân h?y ph?c t?p nhu Paracetamol \[55, 61, 65\]."
# Wait, because of Markdown parsing, the \[ might be literally \[ or [ in the text.
# Let's use regex to replace it safely.
pattern = r'ph?m có dòng oxi hóa phân h?y ph?c t?p nhu Paracetamol \\?\[55, 61, 65\\?\].'
new_text = 'ph?m có dòng oxi hóa phân h?y ph?c t?p nhu Paracetamol \[55, 61\]. Hon n?a, vi?c s? d?ng các di?n c?c bi?n tính b?ng màng Nafion-composite (c? th? là Nafion/TiO2-graphene) dã thi?t l?p m?t h? quy chi?u hi?u nang quan tr?ng cho phép phân tích Paracetamol v?i d? nh?y cao và LOD d?t m?c v?t (0.21 µM) \[65\], t?o co s? tr?c ti?p d? so sánh và d?nh chu?n (benchmark) hi?u nang c?m bi?n DPV trong d? tài này.'

if re.search(pattern, text):
    text = re.sub(pattern, new_text, text)
    print('Benchmark sentence for [65] added.')
else:
    print('Failed to find exact text for benchmark sentence.')
    # Fallback to a simpler replace
    if 'Paracetamol \[55, 61, 65\]' in text:
        text = text.replace('Paracetamol \[55, 61, 65\]', 'Paracetamol \[55, 61\]. Hon n?a, vi?c s? d?ng các di?n c?c bi?n tính b?ng màng Nafion-composite (c? th? là Nafion/TiO2-graphene) dã thi?t l?p m?t h? quy chi?u hi?u nang quan tr?ng cho phép phân tích Paracetamol v?i d? nh?y cao và LOD d?t m?c v?t (0.21 µM) \[65\], t?o co s? tr?c ti?p d? so sánh và d?nh chu?n (benchmark) hi?u nang c?m bi?n DPV trong d? tài này')
        print('Fallback replacement successful.')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)
