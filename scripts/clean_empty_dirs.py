import os
import sys
import shutil
from pathlib import Path

# Thiết lập UTF-8 cho console để tránh lỗi UnicodeEncodeError trên Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

def make_long_path(path):
    """Vượt qua giới hạn MAX_PATH (260 ký tự) trên Windows."""
    abs_path = os.path.abspath(path)
    if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
        abs_path = abs_path.replace('/', '\\')
        return '\\\\?\\' + abs_path
    return abs_path

def is_dir_empty_recursive(dir_path):
    """Kiểm tra xem thư mục có thực sự rỗng (không chứa bất kỳ tệp tin nào) không."""
    long_path = make_long_path(dir_path)
    for root, dirs, files in os.walk(long_path):
        if files:
            return False
    return True

def delete_empty_dirs_recursive(dir_path, exclude_prefixes):
    """Quét và xóa các thư mục rỗng đệ quy, từ sâu nhất trở ra ngoài."""
    long_path = make_long_path(dir_path)
    
    # Bước 1: Quét tất cả các thư mục con
    subdirs = []
    for root, dirs, files in os.walk(long_path):
        for d in dirs:
            full_d_path = Path(os.path.join(root, d))
            # Bỏ qua các thư mục đặc biệt
            should_exclude = False
            for prefix in exclude_prefixes:
                if d.startswith(prefix) or prefix in str(full_d_path):
                    should_exclude = True
                    break
            if not should_exclude:
                subdirs.append(full_d_path)
                
    # Sắp xếp theo chiều dài giảm dần (các thư mục sâu nhất xếp trước)
    subdirs.sort(key=lambda p: len(str(p)), reverse=True)
    
    deleted_count = 0
    # Bước 2: Xóa các thư mục rỗng từ sâu ra nông
    for d_path in subdirs:
        long_d = make_long_path(d_path)
        if os.path.exists(long_d):
            # Nếu rỗng tuyệt đối
            if is_dir_empty_recursive(d_path):
                try:
                    # Xóa thư mục rỗng
                    os.rmdir(long_d)
                    print(f"Đã xóa thư mục rỗng: {d_path.name}")
                    deleted_count += 1
                except Exception as e:
                    print(f"Không thể xóa {d_path.name}: {e}")
                    
    return deleted_count

def main():
    workspace_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent
    print(f"=== Bắt đầu dọn dẹp các thư mục rỗng cũ trong: {workspace_dir} ===")
    
    # Danh sách các tiền tố/thư mục không được xóa
    exclude_prefixes = [
        ".git", ".vscode", "Duplicates_Backup",
        "01_", "02_", "03_", "04_", "05_", "06_", "07_", "08_", "09_"
    ]
    
    # Thực hiện dọn dẹp tệp tạm
    print("Đang quét dọn dẹp các tệp tạm _temp_...")
    for root, dirs, files in os.walk(make_long_path(workspace_dir)):
        for file in files:
            if file.startswith("_temp_"):
                try:
                    os.remove(make_long_path(os.path.join(root, file)))
                except Exception:
                    pass
        for d in dirs:
            if d.startswith("_temp_"):
                try:
                    shutil.rmtree(make_long_path(os.path.join(root, d)))
                except Exception:
                    pass
                    
    # Thực hiện xóa thư mục rỗng
    deleted = delete_empty_dirs_recursive(workspace_dir, exclude_prefixes)
    
    print(f"\n=== HOÀN THÀNH DỌN DẸP ===")
    print(f"Tổng số thư mục rỗng cũ đã xóa: {deleted}")

if __name__ == "__main__":
    main()
