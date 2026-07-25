import os
import glob

# Paths
root = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626"
file_new = os.path.join(root, "Phan2_QuyTrinh_8Buoc_SOP_ChiTiet.md")

old_files = glob.glob(os.path.join(root, "Archive_Old_Versions", "*.md"))

def analyze_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Đếm số Giai đoạn (GĐ)
    gd_count = content.count("## GĐ")
    
    # Lấy các heading
    lines = content.split('\n')
    headings = [l.strip() for l in lines if l.startswith('## ')]
    
    # Word count
    words = len(content.split())
    
    return gd_count, headings, words

print("--- PHÂN TÍCH SO SÁNH SOP CŨ & MỚI ---")
gd_new, head_new, wc_new = analyze_file(file_new)
print(f"[NEW] Phan2_QuyTrinh_8Buoc_SOP_ChiTiet.md - {wc_new} words, {gd_new} Giai đoạn")

for old_file in old_files:
    gd_old, head_old, wc_old = analyze_file(old_file)
    print(f"[OLD] {os.path.basename(old_file)} - {wc_old} words, {gd_old} Giai đoạn")
    
    # So sánh với DeCuong_QuyTrinh_CheTao_DaXacThuc.md vì đây là file chuẩn nhất
    if "06_DeCuong_QuyTrinh_CheTao_DaXacThuc.md" in old_file:
        missing = [h for h in head_old if h not in head_new]
        print(f"   -> Chênh lệch số từ: {wc_new - wc_old} words")
        if missing:
            print(f"   -> [CẢNH BÁO] Các mục có trong OLD nhưng không có trong NEW: {missing}")
        else:
            print("   -> [OK] Không mất mục nào từ bản DeCuong cũ.")

