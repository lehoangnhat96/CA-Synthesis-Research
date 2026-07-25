import re
text = r"Some text \[1\] and [2\] and [3] and \[4] and [5, 6\]"
for m in re.finditer(r'\\?\[([0-9,\s\-]+)\\?\]', text):
    print(m.group(1))
