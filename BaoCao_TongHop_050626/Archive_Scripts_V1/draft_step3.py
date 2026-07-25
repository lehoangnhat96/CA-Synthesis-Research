import re

ref_path = r"C:\Users\ADMIN\.gemini\antigravity\brain\0726e7c6-fe20-4423-a0eb-a1f928b783bf\Reference_Mapping_Table.md"
sop_path = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\Phan2_QuyTrinh_8Buoc_SOP_ChiTiet.md"
draft_output_path = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\Draft_Chuong2_SOP.md"

# 1. Parse Mapping
with open(ref_path, 'r', encoding='utf-8') as f:
    table_content = f.read()

mapping_tag_to_num = {}
for line in table_content.split('\n'):
    match = re.search(r'\|\s*\[(P-[^\]]+)\]\s*\|\s*\*\*\[(\d+)\]\*\*', line)
    if match:
        mapping_tag_to_num[match.group(1)] = match.group(2)

# 2. Extract SOP content
with open(sop_path, 'r', encoding='utf-8') as f:
    sop_content = f.read()

# Lấy từ "## Giai đoạn 1:" đến hết quy trình 8 bước
sop_match = re.search(r'(## Giai đoạn 1:.*?)(?=\n## 4\. )', sop_content, re.DOTALL)
sop_text = sop_match.group(1).strip() if sop_match else sop_content

# We should translate tags in the draft so the user sees the final result
def repl_tags(match):
    tag = match.group(1)
    if tag in mapping_tag_to_num:
        return f"[{mapping_tag_to_num[tag]}]"
    return match.group(0)

sop_text_translated = re.sub(r'\[(P-[^\]]+)\]', repl_tags, sop_text)

# 3. Create Draft
draft = f"""# CHI TIẾT NỘI DUNG SẼ ĐƯỢC CHÈN VÀO DCLV (BƯỚC 3: CHƯƠNG 2)

> Dưới đây là nội dung Quy trình 8 bước chi tiết từ file SOP sẽ được ghi đè vào Mục `2.2. Quy trình thực nghiệm 8 giai đoạn tổng hợp Carbon Aerogel` trong file DCLV gốc. 
> Toàn bộ các thẻ [P-xxx] đã được tôi **tự động chuyển đổi thành các con số trích dẫn chuẩn** dựa trên bảng Mapping (ví dụ `[P-019...]` -> `[X]`). 

---

{sop_text_translated}
"""

with open(draft_output_path, 'w', encoding='utf-8') as f:
    f.write(draft)
