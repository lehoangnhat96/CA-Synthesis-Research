import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def clean_toc_and_preamble(content):
    # Split the document at the first heading 'MỞ ĐẦU' or 'CHƯƠNG 1' to avoid counting TOC and lists of figures
    parts = re.split(r'#\s+(?:MỞ ĐẦU|CHƯƠNG 1)', content, maxsplit=1)
    if len(parts) > 1:
        return parts[1]
    return content

def check_sequence(content, pattern_prefix, label):
    content = clean_toc_and_preamble(content)
    # Find patterns like "Hình 1.1", "Bảng 2.1"
    # Ensure they are at the beginning of a line or part of a caption
    matches = re.findall(pattern_prefix + r'\s*(\d+)\.(\d+)', content)
    if not matches:
        return []
    
    # Track the exact matches found
    print(f"\n[Dữ liệu thô {label} sau khi lọc TOC]: {[f'{m[0]}.{m[1]}' for m in matches]}")
    
    issues = []
    by_chapter = {}
    for ch, num in matches:
        ch, num = int(ch), int(num)
        by_chapter.setdefault(ch, []).append(num)
        
    for ch, nums in by_chapter.items():
        # Check for duplication or out-of-order sequence
        seen = set()
        expected = 1
        for n in nums:
            if n in seen:
                issues.append(f"Lỗi trùng lặp: {label} {ch}.{n} xuất hiện nhiều hơn 1 lần trong văn bản.")
            seen.add(n)
            
        # Check sequence of unique numbers
        unique_nums = sorted(list(set(nums)))
        for i, n in enumerate(unique_nums):
            expected = i + 1
            if n != expected:
                issues.append(f"Lỗi nhảy số: {label} Chương {ch} mong đợi số {expected} nhưng nhận được {n}.")
                
    return issues

def main():
    docx_md_path = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\scratch\docx_converted.md"
    
    with open(docx_md_path, 'r', encoding='utf-8') as f:
        docx_content = f.read()
        
    print("--- KIỂM TRA SỐ THỨ TỰ BẢNG VÀ HÌNH CHƯƠNG MỤC ---")
    fig_issues = check_sequence(docx_content, r'Hình', 'Hình')
    tbl_issues = check_sequence(docx_content, r'Bảng', 'Bảng')
    
    print("\n--- KẾT QUẢ KIỂM TRA ---")
    for issue in fig_issues + tbl_issues:
        print(issue)
    if not fig_issues and not tbl_issues:
        print("Không phát hiện lỗi nhảy số Hình/Bảng.")

if __name__ == '__main__':
    main()
