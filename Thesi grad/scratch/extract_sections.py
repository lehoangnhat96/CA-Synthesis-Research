import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_section(filepath, start_keyword, end_keyword):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex search between two headings or keywords
    pattern = re.compile(re.escape(start_keyword) + r'(.*?)' + re.escape(end_keyword), re.DOTALL | re.IGNORECASE)
    match = pattern.search(content)
    if match:
        return match.group(1).strip()
    return "Not found"

def main():
    docx_md = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\docx_converted.md"
    
    print("--- SECTION 2.4.4: Vật lý sấy thăng hoa ---")
    sec_244 = extract_section(docx_md, "### 2.4.4. Vật lý sấy thăng hoa", "### 2.4.5. Cơ sở khoa học")
    print(sec_244[:1500])
    
    print("\n--- SECTION 2.5.4: Hóa học phối trí ---")
    sec_254 = extract_section(docx_md, "### 2.5.4. Hóa học phối trí tâm hoạt tính", "## 2.6. Quy trình tổng hợp màng mỏng")
    print(sec_254[:1500])

if __name__ == '__main__':
    main()
