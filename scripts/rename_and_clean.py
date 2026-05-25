import os
import re
import sys
import unicodedata
from pathlib import Path

# Thiết lập UTF-8 cho console
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def remove_accents(input_str):
    """Chuyển tiếng Việt có dấu thành không dấu và loại bỏ các ký tự lạ lỗi font."""
    s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
    s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
    s = ''
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    
    # Chuẩn hóa unicode và loại bỏ các dấu kết hợp (combining characters) còn sót
    s = unicodedata.normalize('NFKD', s).encode('ASCII', 'ignore').decode('utf-8')
    return s

def clean_and_shorten_filename(filename, max_words=10, max_length=80):
    """
    Rút gọn và làm sạch tên file.
    - Chuyển thành không dấu.
    - Giữ lại các ký tự chữ, số, khoảng trắng và gạch ngang/dưới.
    - Cắt bớt số từ/độ dài để tên file không quá dài.
    """
    # Xử lý tiếng Việt và ký tự lạ
    clean_name = remove_accents(filename)
    
    # Chỉ giữ lại chữ cái, số, khoảng trắng
    clean_name = re.sub(r'[^\w\s-]', '', clean_name)
    
    # Thay thế nhiều khoảng trắng thành 1 khoảng trắng
    clean_name = re.sub(r'\s+', ' ', clean_name).strip()
    
    # Cắt số từ
    words = clean_name.split()
    if len(words) > max_words:
        clean_name = " ".join(words[:max_words])
        
    # Cắt độ dài tuyệt đối nếu vẫn còn quá dài
    if len(clean_name) > max_length:
        clean_name = clean_name[:max_length].strip()
        
    # Thay khoảng trắng thành dấu gạch dưới (tùy chọn, để tên file lập trình dễ đọc hơn)
    # clean_name = clean_name.replace(' ', '_')
    
    return clean_name

def make_long_path(path):
    abs_path = os.path.abspath(path)
    if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
        abs_path = abs_path.replace('/', '\\')
        return '\\\\?\\' + abs_path
    return abs_path

def main():
    workspace_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent
    target_dir = workspace_dir / "1 Ref materials"
    
    if not target_dir.exists():
        print(f"LỖI: Không tìm thấy thư mục {target_dir}")
        sys.exit(1)
        
    print(f"=== Bắt đầu quét và làm sạch tên file tại: {target_dir.name} ===")
    
    pdf_files = []
    for root, dirs, files in os.walk(target_dir):
        if ".git" in root or "Duplicates_Backup" in root or ".vscode" in root or "_temp_" in root:
            continue
        for file in files:
            if file.lower().endswith(".pdf") and not file.startswith("_temp_"):
                pdf_files.append(Path(root) / file)
                
    print(f"Tìm thấy {len(pdf_files)} file PDF cần kiểm tra.\n")
    
    # Theo dõi các tên file mới để xử lý trùng lặp
    used_names_in_dir = {}
    rename_count = 0
    
    for pdf_path in pdf_files:
        old_stem = pdf_path.stem
        pdf_dir = pdf_path.parent
        
        # 1. Tạo tên mới
        new_stem = clean_and_shorten_filename(old_stem)
        
        # Bỏ qua nếu tên không đổi hoặc tên mới rỗng
        if not new_stem or new_stem == old_stem:
            continue
            
        # 2. Xử lý trùng lặp tên trong cùng thư mục
        dir_str = str(pdf_dir)
        if dir_str not in used_names_in_dir:
            used_names_in_dir[dir_str] = set()
            
        final_new_stem = new_stem
        counter = 1
        while final_new_stem.lower() in [n.lower() for n in used_names_in_dir[dir_str]] or os.path.exists(make_long_path(pdf_dir / f"{final_new_stem}.pdf")):
            # Tránh trường hợp nó tự trùng với chính tên cũ của nó
            if final_new_stem.lower() == old_stem.lower():
                break
            final_new_stem = f"{new_stem}_{counter}"
            counter += 1
            
        used_names_in_dir[dir_str].add(final_new_stem)
        
        if final_new_stem == old_stem:
            continue
            
        print(f"Đang xử lý: {old_stem[:30]}...")
        print(f"  -> Đổi thành: {final_new_stem}")
        
        # Đường dẫn cũ
        old_pdf = pdf_dir / f"{old_stem}.pdf"
        old_md = pdf_dir / f"{old_stem}.md"
        old_img_dir = pdf_dir / f"{old_stem}_images"
        
        # Đường dẫn mới
        new_pdf = pdf_dir / f"{final_new_stem}.pdf"
        new_md = pdf_dir / f"{final_new_stem}.md"
        new_img_dir = pdf_dir / f"{final_new_stem}_images"
        
        # 3. Đổi tên file vật lý
        try:
            long_old_pdf = make_long_path(old_pdf)
            long_new_pdf = make_long_path(new_pdf)
            long_old_md = make_long_path(old_md)
            long_new_md = make_long_path(new_md)
            long_old_img_dir = make_long_path(old_img_dir)
            long_new_img_dir = make_long_path(new_img_dir)

            if os.path.exists(long_old_pdf):
                os.rename(long_old_pdf, long_new_pdf)
            
            md_exists = os.path.exists(long_old_md)
            if md_exists:
                os.rename(long_old_md, long_new_md)
                
            img_dir_exists = os.path.exists(long_old_img_dir)
            if img_dir_exists:
                os.rename(long_old_img_dir, long_new_img_dir)
                
            # 4. Cập nhật đường link bên trong file Markdown
            if md_exists:
                long_new_md = make_long_path(new_md)
                with open(long_new_md, 'r', encoding='utf-8') as f:
                    md_content = f.read()
                    
                # Replace the exact image folder reference in markdown links
                old_link_ref = f"{old_stem}_images/"
                new_link_ref = f"{final_new_stem}_images/"
                
                # Cần chú ý escape các ký tự đặc biệt trong old_link_ref (nếu có)
                # Tuy nhiên lệnh replace chuỗi thông thường là đủ vì nó thay thế chính xác nguyên văn
                if old_link_ref in md_content:
                    md_content = md_content.replace(old_link_ref, new_link_ref)
                    with open(long_new_md, 'w', encoding='utf-8') as f:
                        f.write(md_content)
                    print(f"  -> Đã cập nhật internal links trong file MD.")
                    
            rename_count += 1
            
        except Exception as e:
            print(f"  -> LỖI khi đổi tên: {e}")
            
    print(f"\n=== HOÀN TẤT ===")
    print(f"Đã đổi tên thành công {rename_count} bộ tài liệu.")

if __name__ == "__main__":
    main()
