import os
import sys
import re
from pathlib import Path

# Thiết lập UTF-8 cho console để tránh lỗi mã hóa trên Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def make_long_path(path):
    """Bỏ qua giới hạn MAX_PATH (260 ký tự) trên Windows."""
    abs_path = os.path.abspath(path)
    if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
        abs_path = abs_path.replace('/', '\\')
        return '\\\\?\\' + abs_path
    return abs_path

def url_encode_path(path_str):
    """Mã hóa ký tự đặc biệt và khoảng trắng để tương thích tốt nhất với liên kết Markdown tiêu chuẩn."""
    # Thay thế khoảng trắng thành %20 và dấu gạch chéo ngược thành gạch chéo xuôi
    return path_str.replace('\\', '/').replace(' ', '%20')

def normalize_for_relpath(path_val):
    """Bỏ tiền tố \\\\?\\ để thực hiện tính toán relative path chính xác trên Windows."""
    path_str = str(path_val)
    if path_str.startswith('\\\\?\\'):
        return path_str[4:]
    return path_str

def main():
    workspace_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent
    target_dir = workspace_dir / "1 Ref materials"
    output_file = workspace_dir / "REF_MATERIALS_DASHBOARD.md"
    
    if not os.path.exists(make_long_path(target_dir)):
        print(f"LỖI: Không tìm thấy thư mục {target_dir}")
        sys.exit(1)
        
    print(f"=== Bắt đầu rà quét tài liệu để tạo Dashboard tại: {target_dir} ===")
    
    # 1. Thu thập dữ liệu tài liệu
    documents = []
    topic_counts = {}
    
    for root, dirs, files in os.walk(make_long_path(target_dir)):
        if ".git" in root or "Duplicates_Backup" in root or ".vscode" in root or "_temp_" in root:
            continue
            
        # Lấy tên thư mục chuyên đề (relative từ target_dir)
        rel_root = os.path.relpath(normalize_for_relpath(root), normalize_for_relpath(target_dir))
        if rel_root == ".":
            topic = "Chưa phân loại"
        else:
            topic = rel_root.split(os.sep)[0]
            
        for file in files:
            if file.lower().endswith(".md") and not file.startswith("_temp_") and not file.lower().endswith("metadata.json"):
                md_path = Path(root) / file
                stem = md_path.stem
                
                # Xác định các file liên quan
                pdf_name = f"{stem}.pdf"
                pdf_path = Path(root) / pdf_name
                images_dir_name = f"{stem}_images"
                images_dir_path = Path(root) / images_dir_name
                
                has_pdf = os.path.exists(make_long_path(pdf_path))
                has_images = os.path.exists(make_long_path(images_dir_path))
                
                # Tính toán số lượng hình ảnh trích xuất
                image_count = 0
                if has_images:
                    try:
                        image_count = len([f for f in os.listdir(make_long_path(images_dir_path)) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))])
                    except:
                        pass
                
                # Tính đường dẫn tương đối từ gốc workspace
                rel_md = os.path.relpath(normalize_for_relpath(md_path), normalize_for_relpath(workspace_dir))
                rel_pdf = os.path.relpath(normalize_for_relpath(pdf_path), normalize_for_relpath(workspace_dir)) if has_pdf else None
                rel_images = os.path.relpath(normalize_for_relpath(images_dir_path), normalize_for_relpath(workspace_dir)) if has_images else None
                
                documents.append({
                    "stem": stem,
                    "topic": topic,
                    "rel_md": rel_md,
                    "rel_pdf": rel_pdf,
                    "rel_images": rel_images,
                    "image_count": image_count
                })
                
                # Thống kê số lượng theo chuyên đề
                topic_counts[topic] = topic_counts.get(topic, 0) + 1

    # Sắp xếp tài liệu theo Chuyên đề rồi tới tên tệp
    documents.sort(key=lambda x: (x["topic"], x["stem"].lower()))
    total_docs = len(documents)
    print(f"Rà quét hoàn tất. Tìm thấy {total_docs} tài liệu Markdown chuyên ngành.")
    
    # 2. Xây dựng nội dung Dashboard bằng Markdown
    content = []
    
    content.append("# 📑 MỤC LỤC TỔNG HỢP TÀI LIỆU NGHIÊN CỨU (CARBON AEROGEL)")
    content.append("\n> [!NOTE]\n> *Dashboard này được tự động hóa tạo ra bởi Python để quản lý toàn bộ tài liệu nghiên cứu chuyên ngành Carbon Aerogel phục vụ viết luận văn Thạc sĩ.*")
    content.append("> *Tất cả các liên kết dưới đây đều có thể click trực tiếp trong **Obsidian** hoặc trình đọc Markdown để mở tệp Markdown, file PDF gốc hoặc thư mục ảnh trích xuất tương ứng.*")
    
    # Thống kê tổng quan
    content.append("\n## 📊 Báo cáo thống kê tài liệu")
    content.append(f"\n* **Tổng số lượng tài liệu đã số hóa:** `{total_docs}` bộ tài liệu.")
    content.append("* **Phân bổ theo chuyên đề nghiên cứu:**")
    
    for t_name, count in sorted(topic_counts.items()):
        percentage = (count / total_docs) * 100
        content.append(f"  * 📁 **`{t_name}`**: `{count}` tài liệu (`{percentage:.1f}%`)")
        
    # Tạo bảng danh mục chính
    content.append("\n## 🗂️ Danh mục tài liệu chi tiết")
    content.append("\n| STT | Tài liệu nghiên cứu (Xem Markdown) | Chuyên đề nghiên cứu | File gốc (PDF) | Ảnh trích xuất |")
    content.append("| :---: | :--- | :--- | :---: | :---: |")
    
    for idx, doc in enumerate(documents, 1):
        # Tạo link Markdown
        md_link = f"[{doc['stem']}]({url_encode_path(doc['rel_md'])})"
        
        pdf_link = "❌"
        if doc['rel_pdf']:
            pdf_link = f"[📄 Mở PDF]({url_encode_path(doc['rel_pdf'])})"
            
        images_link = "❌"
        if doc['rel_images'] and doc['image_count'] > 0:
            images_link = f"[🖼️ {doc['image_count']} ảnh]({url_encode_path(doc['rel_images'])})"
            
        # Rút gọn tên chuyên đề để hiển thị đẹp hơn trong bảng
        topic_display = doc['topic'].replace('_', ' ')
        
        content.append(f"| {idx} | {md_link} | `{topic_display}` | {pdf_link} | {images_link} |")
        
    content.append(f"\n---\n*Cập nhật lần cuối vào lúc: {Path(output_file).stat().st_mtime if output_file.exists() else 'Vừa mới tạo'}*")
    
    # 3. Ghi file Dashboard
    long_output = make_long_path(output_file)
    with open(long_output, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
        
    print(f"=== ĐÃ TẠO THÀNH CÔNG FILE DASHBOARD: {output_file.name} ===")

if __name__ == "__main__":
    main()
