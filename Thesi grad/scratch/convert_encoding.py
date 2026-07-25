import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\1 Master\'s Ana Chem\1 Master\'s thesis\Carbon Aerogel\Thesi grad\scratch\headings_output.txt', 'r', encoding='utf-16le') as f:
    text = f.read()

with open(r'd:\1 Master\'s Ana Chem\1 Master\'s thesis\Carbon Aerogel\Thesi grad\scratch\headings_output_utf8.txt', 'w', encoding='utf-8') as f:
    f.write(text)
