import re

path = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\Phan2_QuyTrinh_8Buoc_SOP_ChiTiet.md"

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

def decode_unicode(match):
    try:
        # Xử lý surrogate pairs (VD: \ud83d\udcd5 -> 📕)
        # Bằng cách decode json thay vì unicode_escape để an toàn hơn với Python 3
        import json
        return json.loads(f'"{match.group(0)}"')
    except:
        return match.group(0).encode('utf-8').decode('unicode_escape')

# Fix unicode escapes (gồm cả surrogate pairs như \ud83d\udcd5)
text = re.sub(r'(\\u[0-9a-fA-F]{4})+', decode_unicode, text)

# Fix double backslashes trong LaTeX block
text = text.replace('\\\\circ', '\\circ')
text = text.replace('\\\\text', '\\text')
text = text.replace('\\\\le', '\\le')
text = text.replace('\\\\ge', '\\ge')

with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(text)

print("Đã sửa lỗi Unicode và LaTeX thành công.")
