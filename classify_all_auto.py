import os
import sys
import json
from pathlib import Path

# Thiết lập UTF-8 cho console để tránh lỗi UnicodeEncodeError trên Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

def classify_paper(pdf_name, relative_path, title, abstract, conclusion):
    """
    Phân loại bài viết kết hợp Thư mục gốc ban đầu (Độ chính xác cao nhất) và Từ khóa học thuật.
    """
    path_lower = relative_path.lower()
    text_lower = f"{pdf_name} {title} {abstract} {conclusion}".lower()
    
    # 1. Nhóm 09: Tài liệu Quy trình AI
    if "quy trình ai" in path_lower or "claude" in path_lower or "chatgpt" in path_lower or "kế thừa gpt" in path_lower:
        return "09_Tai_lieu_Quy_trinh_AI"
    if any(kw in text_lower for kw in ["chatgpt", "kế thừa gpt", "plan_v2", "research_plan"]):
        return "09_Tai_lieu_Quy_trinh_AI"

    # 2. Nhóm 07: Giáo trình & Lý thuyết Điện hóa
    if "lý thuyết" in path_lower or "giao trinh" in path_lower or "sách" in path_lower:
        return "07_Giao_trinh_Ly_thuyet"
    if any(kw in text_lower for kw in ["analytical_electrochemistry", "electrochemical methods", "phương pháp phân tích", "giáo trình"]):
        return "07_Giao_trinh_Ly_thuyet"

    # 3. Nhóm 06: Setup đo điện hóa
    if "setup" in path_lower or "fenton" in path_lower or "điện hấp phụ" in path_lower:
        return "06_Setup_Do_Dien_hoa"
    if "fenton điện hóa" in text_lower or "hấp phụ amoni" in text_lower or "electrosorption" in text_lower:
        return "06_Setup_Do_Dien_hoa"

    # 4. Nhóm 05: Chất liên kết chéo & Tạo màng composite
    if "cross linker" in path_lower or "tạo màng" in path_lower or "binder" in path_lower:
        return "05_Cross_Linker_va_Tao_mang"
    # Kiểm tra từ khóa đặc thù cho màng/binder
    if any(kw in text_lower for kw in ["binder", "cross-link", "crosslinked", "pvdf", "nafion", "polybenzoxazine"]):
        return "05_Cross_Linker_va_Tao_mang"

    # 5. Nhóm 01: Tiền xử lý nguyên liệu (Kiềm hóa, tẩy trắng, delignification)
    if "kiềm hóa" in path_lower or "tẩy trắng" in path_lower or "0 kiềm hóa, 1 tẩy trắng" in path_lower:
        return "01_Tien_xu_ly_Nguyen_lieu"

    # 6. Nhóm 02: Doping & Gel hóa
    if "doping" in path_lower or "gel hóa" in path_lower or "2 doping, gel hóa" in path_lower:
        return "02_Doping_va_Gel_hoa"

    # 7. Nhóm 03: Sấy & Nung
    if "sấy" in path_lower or "nung" in path_lower or "3 sấy, 4 nung" in path_lower:
        return "03_Say_va_Nung_Nhiet_phan"

    # 8. Nhóm 04: Cảm biến điện hóa & Sinh học
    if "cảm biến" in path_lower or "sensor" in path_lower or "sensing" in path_lower or "spe" in path_lower:
        return "04_Cam_bien_Dien_hoa_Sinh_hoc"
    if any(kw in text_lower for kw in ["sensor", "sensing", "biosensor", "electroanalytical", "detection of", "cảm biến", " glass carbon", "spe", "dopamine", "paracetamol", "nitrophenol"]):
        return "04_Cam_bien_Dien_hoa_Sinh_hoc"

    # 9. Nhóm 08: Review & Tổng quan (Tài liệu tổng hợp hoặc chứa từ khóa review)
    if "tài liệu tổng hợp" in path_lower or "review" in text_lower or "advances" in text_lower or "progress" in text_lower or "overview" in text_lower:
        return "08_Review_va_Tong_quan"

    # Nhóm dự phòng mặc định
    return "08_Review_va_Tong_quan"


def main():
    brain_dir = Path(r"C:\Users\ADMIN\.gemini\antigravity\brain\365f84a4-e609-4dee-9c3d-858faeaa18e0")
    json_path = brain_dir / "extracted_summaries.json"
    
    if not json_path.exists():
        print(f"LỖI: Không tìm thấy file {json_path}")
        return
        
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    print(f"=== Bắt đầu phân loại chính xác kết hợp Thư mục cho {len(data)} tài liệu ===")
    
    classification_map = {}
    stats = {}
    
    for pdf_name, item in data.items():
        title = item.get("title", "")
        abstract = item.get("abstract", "")
        conclusion = item.get("conclusion", "")
        relative_path = item.get("relative_path", "")
        
        category = classify_paper(pdf_name, relative_path, title, abstract, conclusion)
        classification_map[pdf_name] = category
        
        stats[category] = stats.get(category, 0) + 1
        
    # Ghi kết quả vào file classification_map.json trong thư mục brain
    output_path = brain_dir / "classification_map.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(classification_map, f, ensure_ascii=False, indent=2)
        
    print(f"\n=== HOÀN THÀNH PHÂN LOẠI CHÍNH XÁC ===")
    print(f"Kết quả phân loại đã được lưu tại: {output_path}")
    print("\nThống kê số lượng file theo từng nhóm mới:")
    for cat, count in sorted(stats.items()):
        print(f"  - {cat}: {count} tệp")

if __name__ == "__main__":
    main()
