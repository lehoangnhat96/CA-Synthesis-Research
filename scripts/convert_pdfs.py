import os
import sys
import hashlib
import shutil
import multiprocessing
from pathlib import Path

# Thiết lập UTF-8 cho console để tránh lỗi UnicodeEncodeError trên Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# Thử import thư viện chuyên dụng
try:
    import fitz  # PyMuPDF
except ImportError:
    print("LỖI: Chưa cài đặt thư viện 'pymupdf'. Vui lòng chạy 'pip install pymupdf'")
    sys.exit(1)

try:
    import pymupdf4llm
except ImportError:
    print("CẢNH BÁO: Chưa cài đặt thư viện 'pymupdf4llm'. Sẽ dùng giải pháp PyMuPDF cơ bản làm mặc định.")
    pymupdf4llm = None


def make_long_path(path):
    """Vượt qua giới hạn MAX_PATH (260 ký tự) trên Windows khi thao tác file bằng Python."""
    abs_path = os.path.abspath(path)
    if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
        abs_path = abs_path.replace('/', '\\')
        return '\\\\?\\' + abs_path
    return abs_path


def calculate_md5(file_path):
    """Tính mã băm MD5 của một file để xác định trùng lặp tuyệt đối."""
    long_path = make_long_path(file_path)
    hash_md5 = hashlib.md5()
    with open(long_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def convert_pdf_to_md_basic(pdf_path, output_md_path, images_dir):
    """Giải pháp PyMuPDF (fitz) cơ bản - Cực kỳ nhanh, không bao giờ bị treo."""
    long_pdf = make_long_path(pdf_path)
    long_md = make_long_path(output_md_path)
    long_images = make_long_path(images_dir)
    
    doc = fitz.open(long_pdf)
    text_blocks = []
    image_count = 0
    os.makedirs(long_images, exist_ok=True)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text_blocks.append(f"## Page {page_num + 1}\n")
        text_blocks.append(page.get_text("text"))
        
        # Trích xuất ảnh cơ bản
        try:
            image_list = page.get_images(full=True)
            for img_idx, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_name = f"page-{page_num+1}-img-{img_idx+1}.{image_ext}"
                image_path = os.path.join(long_images, image_name)
                
                with open(image_path, "wb") as f_img:
                    f_img.write(image_bytes)
                
                img_dir_name = os.path.basename(images_dir)
                text_blocks.append(f"\n![Ảnh {image_count+1}]({img_dir_name}/{image_name})\n")
                image_count += 1
        except Exception:
            pass  # Bỏ qua nếu lỗi trích xuất ảnh trên trang
            
    # Ghi file MD
    md_content = "\n".join(text_blocks)
    with open(long_md, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    if os.path.exists(long_images) and not os.listdir(long_images):
        os.rmdir(long_images)
        
    return True, f"Thành công (fallback PyMuPDF cơ bản, trích xuất {image_count} ảnh)"


def convert_pdf_to_md(pdf_path, output_md_path, images_dir, workspace_dir):
    """
    Chuyển đổi một file PDF sang Markdown và trích xuất hình ảnh.
    Sử dụng giải pháp Sao chép tạm thời (Temporary Copy Workaround) để tránh 
    tất cả các lỗi tương thích đường dẫn dài / ký tự đặc biệt của thư viện C-level.
    """
    temp_pdf_name = f"_temp_{hashlib.md5(str(pdf_path).encode('utf-8')).hexdigest()[:8]}_convert_.pdf"
    temp_md_name = temp_pdf_name.replace(".pdf", ".md")
    temp_images_name = temp_pdf_name.replace(".pdf", "_images")
    
    temp_pdf_path = workspace_dir / temp_pdf_name
    temp_md_path = workspace_dir / temp_md_name
    temp_images_dir = workspace_dir / temp_images_name
    
    try:
        # Đảm bảo dọn dẹp các tệp tạm cũ nếu có
        for path in [temp_pdf_path, temp_md_path]:
            long_p = make_long_path(path)
            if os.path.exists(long_p):
                os.remove(long_p)
        long_t_img = make_long_path(temp_images_dir)
        if os.path.exists(long_t_img):
            shutil.rmtree(long_t_img)
            
        # Sao chép file PDF cần chuyển đổi ra thư mục gốc với tên tạm ngắn gọn
        shutil.copy2(make_long_path(pdf_path), make_long_path(temp_pdf_path))
        
        if pymupdf4llm is not None:
            # Tạo thư mục ảnh tạm
            os.makedirs(make_long_path(temp_images_dir), exist_ok=True)
            
            # Chuyển đổi file tạm (đường dẫn cực ngắn, không bao giờ lỗi MAX_PATH hay slash)
            md_content = pymupdf4llm.to_markdown(
                doc=str(temp_pdf_path),
                write_images=True,
                image_path=str(temp_images_dir),
                image_format="png"
            )
            
            # Ghi nội dung Markdown tạm
            with open(make_long_path(temp_md_path), "w", encoding="utf-8") as f:
                f.write(md_content)
                
            # Di chuyển kết quả về đích thực tế
            shutil.move(make_long_path(temp_md_path), make_long_path(output_md_path))
            
            long_dest_images = make_long_path(images_dir)
            if os.path.exists(long_t_img) and os.listdir(long_t_img):
                if os.path.exists(long_dest_images):
                    shutil.rmtree(long_dest_images)
                shutil.move(long_t_img, long_dest_images)
            elif os.path.exists(long_t_img):
                shutil.rmtree(long_t_img)
                
            return True, "Thành công (pymupdf4llm qua cơ chế temp copy)"
            
        else:
            return convert_pdf_to_md_basic(pdf_path, output_md_path, images_dir)
            
    except Exception as e:
        return False, f"LỖI: {str(e)}"
        
    finally:
        # Dọn dẹp tệp tạm ở mọi tình huống để giữ workspace sạch sẽ
        try:
            long_temp_pdf = make_long_path(temp_pdf_path)
            if os.path.exists(long_temp_pdf):
                os.remove(long_temp_pdf)
            long_temp_md = make_long_path(temp_md_path)
            if os.path.exists(long_temp_md):
                os.remove(long_temp_md)
            long_t_img = make_long_path(temp_images_dir)
            if os.path.exists(long_t_img):
                shutil.rmtree(long_t_img)
        except Exception:
            pass


def _multiprocess_worker(pdf_path, output_md_path, images_dir, workspace_dir, queue):
    """Hàm worker chạy trong tiến trình riêng biệt để thực hiện chuyển đổi."""
    try:
        success, msg = convert_pdf_to_md(pdf_path, output_md_path, images_dir, workspace_dir)
        queue.put((success, msg))
    except Exception as e:
        queue.put((False, f"LỖI Worker: {str(e)}"))


def convert_pdf_with_timeout(pdf_path, output_md_path, images_dir, workspace_dir, timeout=45):
    """
    Chạy hàm chuyển đổi PDF trong một Tiến trình riêng biệt với giới hạn thời gian (Timeout).
    Nếu quá thời gian cho phép (mặc định 45s), tiến trình sẽ bị kết thúc cưỡng bức để tránh treo script.
    """
    # Khởi tạo Queue giao tiếp giữa các tiến trình
    ctx = multiprocessing.get_context("spawn")
    queue = ctx.Queue()
    
    # Khởi tạo tiến trình con
    p = ctx.Process(
        target=_multiprocess_worker, 
        args=(pdf_path, output_md_path, images_dir, workspace_dir, queue)
    )
    
    p.start()
    p.join(timeout)
    
    if p.is_alive():
        p.terminate()
        p.join()
        # Nếu bị timeout ở thư viện pymupdf4llm phức tạp, thực hiện fallback về PyMuPDF cơ bản ngay lập tức
        print(f"  -> Bị treo (Quá {timeout}s), tự động kích hoạt fallback PyMuPDF cơ bản...")
        try:
            success, msg = convert_pdf_to_md_basic(pdf_path, output_md_path, images_dir)
            return success, f"{msg} (sau khi kích hoạt fallback do timeout)"
        except Exception as ex:
            return False, f"TIMEOUT và Fallback thất bại: {str(ex)}"
        
    if not queue.empty():
        return queue.get()
        
    return False, "LỖI: Tiến trình con kết thúc không để lại kết quả."


def main():
    workspace_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent
    print(f"=== Bắt đầu quét và chuyển đổi PDF trong thư mục: {workspace_dir} ===")
    
    # 1. Quét tìm tất cả các file PDF trong workspace (bỏ qua thư mục .git, backup và tệp tạm)
    pdf_files = []
    for root, dirs, files in os.walk(workspace_dir):
        if ".git" in root or "Duplicates_Backup" in root or ".vscode" in root or "_temp_" in root:
            continue
        for file in files:
            if file.lower().endswith(".pdf") and not file.startswith("_temp_"):
                pdf_files.append(Path(os.path.join(root, file)))
                
    total_pdfs = len(pdf_files)
    print(f"Tìm thấy tổng cộng: {total_pdfs} file PDF.")
    
    # 2. Phát hiện trùng lặp tuyệt đối bằng MD5
    md5_map = {}
    duplicates = []
    unique_pdfs = []
    
    for pdf_path in pdf_files:
        try:
            md5_val = calculate_md5(pdf_path)
            if md5_val in md5_map:
                duplicates.append((pdf_path, md5_map[md5_val]))
            else:
                md5_map[md5_val] = pdf_path
                unique_pdfs.append(pdf_path)
        except Exception as e:
            print(f"Không thể tính MD5 cho {pdf_path.name}: {e}")
            unique_pdfs.append(pdf_path)
            
    print(f"Số lượng file trùng lặp phát hiện: {len(duplicates)} file.")
    
    # Tạo thư mục Duplicates_Backup nếu có trùng lặp
    if duplicates:
        backup_dir = workspace_dir / "Duplicates_Backup"
        os.makedirs(make_long_path(backup_dir), exist_ok=True)
        print(f"Sẽ di chuyển các file trùng lặp vào thư mục backup: {backup_dir}")
        for dup_file, _ in duplicates:
            try:
                dest_path = backup_dir / dup_file.name
                counter = 1
                while dest_path.exists():
                    dest_path = backup_dir / f"{dup_file.stem}_{counter}{dup_file.suffix}"
                    counter += 1
                
                long_src = make_long_path(dup_file)
                long_dst = make_long_path(dest_path)
                shutil.move(long_src, long_dst)
                print(f"  -> Đã di chuyển file trùng: {dup_file.name} -> Duplicates_Backup")
            except Exception as e:
                print(f"  -> LỖI khi di chuyển file trùng {dup_file.name}: {e}")

    # Cập nhật danh sách các file duy nhất cần xử lý chuyển đổi
    print(f"\nSố lượng file PDF duy nhất cần chuyển đổi: {len(unique_pdfs)}")
    
    # 3. Tiến hành chuyển đổi từng file duy nhất
    success_count = 0
    fail_count = 0
    
    for idx, pdf_path in enumerate(unique_pdfs, 1):
        pdf_dir = pdf_path.parent
        pdf_stem = pdf_path.stem
        
        output_md_path = pdf_dir / f"{pdf_stem}.md"
        images_dir = pdf_dir / f"{pdf_stem}_images"
        
        print(f"[{idx}/{len(unique_pdfs)}] Đang chuyển đổi: {pdf_path.name}...")
        
        # Kiểm tra xem file MD đã tồn tại chưa và dung lượng lớn hơn 100 bytes
        long_md_check = make_long_path(output_md_path)
        if os.path.exists(long_md_check) and os.path.getsize(long_md_check) > 100:
            print(f"  -> Bỏ qua (Đã tồn tại file Markdown của bài viết này)")
            success_count += 1
            continue
            
        # Gọi hàm chuyển đổi có gắn timeout (mặc định 45 giây)
        success, msg = convert_pdf_with_timeout(pdf_path, output_md_path, images_dir, workspace_dir, timeout=45)
        if success:
            print(f"  -> {msg}")
            success_count += 1
        else:
            print(f"  -> {msg}")
            fail_count += 1
            
    print(f"\n=== HOÀN THÀNH QUÁ TRÌNH CHUYỂN ĐỔI ===")
    print(f"Thành công: {success_count}/{len(unique_pdfs)}")
    if fail_count > 0:
        print(f"Thất bại: {fail_count}/{len(unique_pdfs)}")


if __name__ == "__main__":
    # Bắt buộc trên Windows để dùng multiprocessing
    multiprocessing.freeze_support()
    main()
