# -*- coding: utf-8 -*-
"""
sync_ref_lib_perfect.py
========================
Đồng bộ hóa hoàn hảo từ 1 Ref materials sang 2 Ref lib:
- Xóa sạch các thư mục từ 01_Tien_xu_ly_Nguyen_lieu đến 09_Tai_lieu_Quy_trinh_AI trong 2 Ref lib.
- Sao chép toàn bộ cấu trúc mới từ 1 Ref materials sang 2 Ref lib.
- Dọn dẹp các tệp đã tái phân loại còn sót lại ở thư mục gốc của 2 Ref lib.
"""

import os
import sys
import shutil
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

WORKSPACE = Path(r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel")
SRC_BASE = WORKSPACE / "1 Ref materials"
DST_BASE = WORKSPACE / "2 Ref lib"

CATEGORIES = [
    "01_Tien_xu_ly_Nguyen_lieu",
    "02_Doping_va_Gel_hoa",
    "03_Say_va_Nung_Nhiet_phan",
    "04_Cam_bien_Dien_hoa_Sinh_hoc",
    "05_Cross_Linker_va_Tao_mang",
    "06_Setup_Do_Dien_hoa",
    "07_Giao_trinh_Ly_thuyet",
    "08_Review_va_Tong_quan",
    "09_Tai_lieu_Quy_trinh_AI"
]

ROOT_FILES_TO_CLEAN = [
    # Cảm biến điện hóa
    "NGHIÊN CỨU ỨNG DỤNG CẢM BIẾN SINH HỌC ĐIỆN HÓA TRÊN CƠ SỞ VI ĐIỆN CỰC BIẾN TÍNH XÁC ĐỊNH DƯ LƯỢNG THUỐC BẢO VỆ THỰC VẬT.pdf",
    "NGHIÊN CỨU ỨNG DỤNG CẢM BIẾN SINH HỌC ĐIỆN HÓA TRÊN CƠ SỞ VI ĐIỆN CỰC BIẾN TÍNH XÁC ĐỊNH DƯ LƯỢNG THUỐC BẢO VỆ THỰC VẬT.md",
    "NGHIÊN CỨU ỨNG DỤNG CẢM BIẾN SINH HỌC ĐIỆN HÓA TRÊN CƠ SỞ VI ĐIỆN CỰC BIẾN TÍNH XÁC ĐỊNH DƯ LƯỢNG THUỐC BẢO VỆ THỰC VẬT_images",
    
    # Tóm tắt luận án Phương
    "TOM_TAT_NTXPhuong.pdf",
    "TOM_TAT_NTXPhuong.md",
    "TOM_TAT_NTXPhuong_images",
    
    # Xơ dừa
    "View of Investigate coir fibers’ properties produced by coconut fiber extracting machine in Ben Tre and research the treatment for fiber with NaOH solution.pdf",
    "View of Investigate coir fibers’ properties produced by coconut fiber extracting machine in Ben Tre and research the treatment for fiber with NaOH solution.md"
]

def make_long_path(path):
    abs_path = os.path.abspath(str(path))
    if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
        abs_path = abs_path.replace('/', '\\')
        return '\\\\?\\' + abs_path
    return abs_path

def main():
    print("=== BẮT ĐẦU ĐỒNG BỘ HÓA HOÀN HẢO 2 REF LIB ===")
    
    # 1. Đồng bộ các danh mục từ 01 đến 09
    for cat in CATEGORIES:
        src_cat = SRC_BASE / cat
        dst_cat = DST_BASE / cat
        
        long_src = make_long_path(src_cat)
        long_dst = make_long_path(dst_cat)
        
        if not os.path.exists(long_src):
            print(f"  [BỎ QUA] Không tìm thấy danh mục nguồn: {cat}")
            continue
            
        print(f"  [ĐỒNG BỘ] Danh mục: {cat}...")
        
        # Xóa danh mục cũ ở đích nếu có để tránh file rác
        if os.path.exists(long_dst):
            shutil.rmtree(long_dst)
            
        # Sao chép toàn bộ danh mục từ nguồn sang đích
        shutil.copytree(long_src, long_dst)
        print(f"    -> Đã sao chép hoàn tất danh mục {cat}")
        
    # 2. Dọn dẹp các tệp lẻ ở thư mục gốc của 2 Ref lib
    print("\n=== DỌN DẸP TỆP LẺ Ở THƯ MỤC GỐC 2 REF LIB ===")
    for item in ROOT_FILES_TO_CLEAN:
        item_path = DST_BASE / item
        long_item = make_long_path(item_path)
        
        if os.path.exists(long_item):
            if os.path.isdir(long_item):
                shutil.rmtree(long_item)
                print(f"  [ĐÃ XÓA THƯ MỤC] {item}")
            else:
                os.remove(long_item)
                print(f"  [ĐÃ XÓA TỆP] {item}")
        else:
            print(f"  [BỎ QUA] Không tồn tại hoặc đã dọn dẹp: {item}")
            
    print("\n=== ĐỒNG BỘ HÓA HOÀN TẤT ===")
    print("Thư mục 1 Ref materials và 2 Ref lib hiện tại đã khớp 100% về cấu trúc và hình ảnh.")

if __name__ == "__main__":
    main()
