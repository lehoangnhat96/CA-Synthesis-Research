import os
import sys
import json
import re
import shutil
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


def extract_info_from_md(md_path):
    """
    Đọc tệp tin Markdown và trích xuất nhanh Tiêu đề, Tóm tắt (Abstract) và Kết luận (Conclusion)
    để phục vụ việc phân loại từ khóa.
    """
    try:
        with open(md_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        # 1. Trích xuất Title (dựa trên tên tệp hoặc các dòng đầu tiên)
        title = md_path.stem
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        for line in lines[:10]:
            if line.startswith("#") or len(line) > 15:
                title_candidate = line.lstrip("#* \t")
                if "page" not in title_candidate.lower() and len(title_candidate) > 10:
                    title = title_candidate
                    break
        
        # 2. Trích xuất Abstract
        abstract = ""
        abstract_match = re.search(r'(?:abstract|tóm tắt)\b', content, re.IGNORECASE)
        if abstract_match:
            start_idx = abstract_match.end()
            abstract = content[start_idx:start_idx + 1500].strip()
            
        # 3. Trích xuất Conclusion
        conclusion = ""
        conclusion_match = re.search(r'(?:conclusion|conclusions|kết luận|summary)\b', content, re.IGNORECASE)
        if conclusion_match:
            start_idx = conclusion_match.end()
            conclusion = content[start_idx:start_idx + 1500].strip()
            
        return title, abstract, conclusion
    except Exception as e:
        print(f"Lỗi khi đọc file {md_path.name}: {e}")
        return md_path.stem, "", ""


def make_long_path(path):
    """Vượt qua giới hạn MAX_PATH (260 ký tự) trên Windows khi thao tác file bằng Python."""
    abs_path = os.path.abspath(path)
    if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
        abs_path = abs_path.replace('/', '\\')
        return '\\\\?\\' + abs_path
    return abs_path


def main():
    workspace_dir = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ref_materials_dir = workspace_dir / "1 Ref materials"
    unclassified_dir = ref_materials_dir / "Chua phan loai"
    
    if not unclassified_dir.exists():
        print(f"LỖI: Không tìm thấy thư mục: {unclassified_dir}")
        return
        
    md_files = list(unclassified_dir.glob("*.md"))
    
    if not md_files:
        print(f"=== Thư mục {unclassified_dir.name} rỗng. Không có tài liệu cần phân loại. ===")
        return
        
    print(f"=== Bắt đầu phân loại tự động và di chuyển vật lý cho {len(md_files)} tài liệu ===")
    
    stats = {}
    moved_count = 0
    
    for md_path in md_files:
        pdf_name = md_path.stem + ".pdf"
        relative_path = f"Chua phan loai/{md_path.name}"
        
        # Trích xuất thông tin học thuật trực tiếp từ file Markdown
        title, abstract, conclusion = extract_info_from_md(md_path)
        
        # Phân loại tài liệu bằng hàm lọc từ khóa
        category = classify_paper(pdf_name, relative_path, title, abstract, conclusion)
        
        target_dir = ref_materials_dir / category
        os.makedirs(make_long_path(target_dir), exist_ok=True)
        
        print(f"\n📄 Tài liệu: {md_path.name}")
        print(f"   -> Nhóm phân loại: {category}")
        
        # Tiến hành di chuyển vật lý
        try:
            # 1. Di chuyển file .md
            dest_md_path = target_dir / md_path.name
            shutil.move(make_long_path(md_path), make_long_path(dest_md_path))
            
            # 2. Di chuyển file .pdf tương ứng nếu có
            pdf_path = unclassified_dir / pdf_name
            if pdf_path.exists():
                dest_pdf_path = target_dir / pdf_name
                shutil.move(make_long_path(pdf_path), make_long_path(dest_pdf_path))
                
            # 3. Di chuyển thư mục ảnh tương ứng nếu có
            images_dir_name = md_path.stem + "_images"
            images_dir = unclassified_dir / images_dir_name
            if images_dir.exists():
                dest_images_dir = target_dir / images_dir_name
                if dest_images_dir.exists():
                    shutil.rmtree(make_long_path(dest_images_dir))
                shutil.move(make_long_path(images_dir), make_long_path(dest_images_dir))
                
            print(f"   ✅ Đã di chuyển tài liệu và dữ liệu đi kèm thành công!")
            moved_count += 1
            stats[category] = stats.get(category, 0) + 1
        except Exception as e:
            print(f"   ❌ Lỗi khi di chuyển tài liệu: {e}")
            
    print(f"\n=== HOÀN THÀNH QUÁ TRÌNH PHÂN LOẠI VÀ DI CHUYỂN ===")
    print(f"Tổng số tài liệu đã di chuyển thành công: {moved_count}/{len(md_files)}")
    print("\nThống kê số lượng file được di chuyển theo từng nhóm:")
    for cat, count in sorted(stats.items()):
        print(f"  - {cat}: {count} tệp")

if __name__ == "__main__":
    main()
