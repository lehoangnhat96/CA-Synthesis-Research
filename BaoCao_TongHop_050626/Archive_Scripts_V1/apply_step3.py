import re

draft_path = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\Draft_Chuong2_Academic.md"
dclv_path = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\DCLV_CA_19.06 Fe-N CA.md"

with open(draft_path, 'r', encoding='utf-8') as f:
    draft_content = f.read()

# Extract the text from the draft starting at ### 2.2.1
content_to_insert = re.search(r'(### 2\.2\.1.*)', draft_content, re.DOTALL)
if content_to_insert:
    academic_text = content_to_insert.group(1).strip()
else:
    academic_text = draft_content

# Change "đun hồi lưu" to "đun"
academic_text = academic_text.replace("đun hồi lưu", "đun")

# Read DCLV
with open(dclv_path, 'r', encoding='utf-8') as f:
    dclv = f.read()

# Find where to replace. In DCLV, section 2.2 has Bảng 2.1 then bullet points: "- *Giai đoạn 0..."
# Let's replace from the first bullet point "- *Giai đoạn 0" up to "## 2.3. Sơ đồ Flowchart"
# The text looks like: 
# - *Giai đoạn 0 (Tiền xử lý kiềm hóa tách lignin)*: ...
# ...
# 2.  **Mức 800°C (Mức đối chứng):** ...
# 
# ## 2.3. Sơ đồ Flowchart thực nghiệm

# We can use regex to replace everything between the end of Table 2.1 and "## 2.3. Sơ đồ"
# Let's find "## 2.3." first.
end_idx = dclv.find("## 2.3. Sơ đồ")
if end_idx == -1:
    end_idx = dclv.find("[2.3. Sơ đồ")

# Find the start of the bullet points. It starts with "- *Giai đoạn 0"
start_idx = dclv.find("- *Giai đoạn 0")
if start_idx == -1:
    # try another way
    start_idx = dclv.find("- *Giai đoạn 0")

if start_idx != -1 and end_idx != -1:
    new_dclv = dclv[:start_idx] + academic_text + "\n\n" + dclv[end_idx:]
    with open(dclv_path, 'w', encoding='utf-8') as f:
        f.write(new_dclv)
    print("SUCCESS: Replaced bullet points with academic text.")
else:
    print("FAILED: Could not find start or end index.")
