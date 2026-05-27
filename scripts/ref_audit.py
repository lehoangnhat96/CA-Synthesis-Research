"""
Đọc các file MD trong từng thư mục con của 1 Ref materials
và tổng hợp tiêu đề/nội dung để nhận xét phân loại.
"""
import os
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

BASE = Path(r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials")
OUT  = Path(r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\scripts\ref_audit_report.md")

CATEGORIES = [
    "01_Tien_xu_ly_Nguyen_lieu",
    "02_Doping_va_Gel_hoa",
    "03_Say_va_Nung_Nhiet_phan",
    "04_Cam_bien_Dien_hoa_Sinh_hoc",
    "05_Cross_Linker_va_Tao_mang",
    "06_Setup_Do_Dien_hoa",
    "07_Giao_trinh_Ly_thuyet",
    "08_Review_va_Tong_quan",
    "09_Tai_lieu_Quy_trinh_AI",
]

CAT_LABELS = {
    "01_Tien_xu_ly_Nguyen_lieu":     "Tiền xử lý nguyên liệu (NaOH, bleach, xơ dừa thô → cellulose)",
    "02_Doping_va_Gel_hoa":          "Doping & Gel hóa (N-doped, Fe-doped, sol-gel, NaOH:urea, freeze-gelation)",
    "03_Say_va_Nung_Nhiet_phan":     "Sấy & Nung nhiệt phân (freeze-drying, pyrolysis, carbonization)",
    "04_Cam_bien_Dien_hoa_Sinh_hoc": "Cảm biến điện hóa sinh học (electrochemical sensor, biosensor, SPE, detection)",
    "05_Cross_Linker_va_Tao_mang":   "Cross-linker & Tạo màng (binder, chitosan, PVDF, electrode fabrication)",
    "06_Setup_Do_Dien_hoa":          "Setup đo điện hóa (CV, EIS, GCD, electrochemical methods, thiết bị đo)",
    "07_Giao_trinh_Ly_thuyet":       "Giáo trình lý thuyết (textbook, principles, analytical electrochemistry)",
    "08_Review_va_Tong_quan":        "Review & Tổng quan (review papers, synthesis workflow, overview)",
    "09_Tai_lieu_Quy_trinh_AI":      "Tài liệu quy trình AI (AI-generated research plans, process notes)",
}

def extract_md_summary(md_path, max_lines=25):
    """Lấy tiêu đề và abstract từ đầu file MD."""
    try:
        with open(md_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
        # Lọc bỏ dòng trống và dòng hình ảnh
        clean = []
        for line in lines[:80]:
            stripped = line.strip()
            if stripped and not stripped.startswith("![") and not stripped.startswith("![]") and "-----" not in stripped:
                clean.append(stripped)
            if len(clean) >= max_lines:
                break
        return clean
    except Exception as e:
        return [f"[ERROR reading: {e}]"]

def get_first_heading(summary_lines):
    """Lấy heading đầu tiên có nội dung thực."""
    for line in summary_lines:
        if line.startswith("#"):
            cleaned = line.lstrip("#").strip()
            if len(cleaned) > 5:
                return cleaned
    # Fallback: dòng đầu không rỗng
    for line in summary_lines:
        if len(line) > 5:
            return line[:150]
    return "(no title)"

lines_out = []
lines_out.append("# Báo cáo Rà soát Phân loại File MD — 1 Ref materials\n")
lines_out.append("*Tự động tạo bởi ref_audit.py*\n\n")
lines_out.append("---\n")

for cat in CATEGORIES:
    cat_path = BASE / cat
    label = CAT_LABELS.get(cat, cat)
    
    lines_out.append(f"\n## 📁 {cat}\n")
    lines_out.append(f"**Mục đích danh mục:** {label}\n\n")
    
    if not cat_path.exists():
        lines_out.append("⚠️ **KHÔNG TÌM THẤY THƯ MỤC**\n\n")
        continue
    
    md_files = sorted([f for f in cat_path.iterdir() if f.is_file() and f.suffix == ".md"])
    
    if not md_files:
        lines_out.append("*(Không có file MD nào)*\n\n")
        continue
    
    lines_out.append(f"**Số file MD:** {len(md_files)}\n\n")
    lines_out.append("| # | Tên file | Dòng tiêu đề / Nội dung đầu | Kích thước |\n")
    lines_out.append("|---|----------|------------------------------|------------|\n")
    
    for i, md_file in enumerate(md_files, 1):
        size = md_file.stat().st_size
        if size < 50:
            title = "⚠️ **FILE RỖNG**"
        else:
            summary = extract_md_summary(md_file)
            title = get_first_heading(summary)
            # Truncate for table
            if len(title) > 120:
                title = title[:120] + "..."
        
        # Escape pipes for markdown table
        title_escaped = title.replace("|", "\\|")
        name_short = md_file.name if len(md_file.name) <= 70 else md_file.name[:67] + "..."
        
        lines_out.append(f"| {i} | `{name_short}` | {title_escaped} | {size:,} B |\n")
    
    lines_out.append("\n")

# Write output
with open(OUT, "w", encoding="utf-8") as f:
    f.writelines(lines_out)

print(f"Report written to: {OUT}")
print(f"Total lines: {len(lines_out)}")
