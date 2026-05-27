# -*- coding: utf-8 -*-
"""
restructure_images.py
======================
Tái cấu trúc thư mục hình ảnh theo Phương án B (Tập trung theo danh mục):
- Quét qua 9 danh mục con trong 1 Ref materials.
- Tạo thư mục con "_images" trong mỗi danh mục con.
- Di chuyển tất cả thư mục ảnh (*_images, *_img) vào bên trong "_images".
- Quét toàn bộ tệp .md trong danh mục và cập nhật đường dẫn ảnh (thêm tiền tố "_images/").
"""

import os
import sys
import shutil
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

BASE_DIR = Path(r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials")

def make_long_path(path):
    abs_path = os.path.abspath(str(path))
    if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
        abs_path = abs_path.replace('/', '\\')
        return '\\\\?\\' + abs_path
    return abs_path

def process_category(cat_path: Path, dry_run: bool = False):
    print(f"\nProcessing category: {cat_path.name}")
    long_cat = make_long_path(cat_path)
    
    # Create the central '_images' directory inside this category
    images_root = cat_path / "_images"
    long_images_root = make_long_path(images_root)
    
    # 1. Identify all image folders inside this category
    img_folders = []
    for item in os.listdir(long_cat):
        item_path = cat_path / item
        long_item = make_long_path(item_path)
        
        # Check if it is a directory and ends with _images or _img, and is not '_images' itself or '.obsidian'
        if os.path.isdir(long_item) and item != "_images" and item != ".obsidian":
            if item.endswith("_images") or item.endswith("_img"):
                img_folders.append(item)
                
    if not img_folders:
        print("  No paper-specific image folders found in this category.")
        return
        
    print(f"  Found image folders to move: {img_folders}")
    
    if not dry_run:
        os.makedirs(long_images_root, exist_ok=True)
        
    moved_folders = []
    
    # 2. Move image folders inside '_images'
    for folder in img_folders:
        src = cat_path / folder
        dst = images_root / folder
        
        long_src = make_long_path(src)
        long_dst = make_long_path(dst)
        
        print(f"  -> Moving: {folder} -> _images/{folder}")
        if not dry_run:
            if os.path.exists(long_dst):
                # If target already exists, merge contents
                print(f"     Target already exists, merging files...")
                for file_item in os.listdir(long_src):
                    shutil.move(os.path.join(long_src, file_item), os.path.join(long_dst, file_item))
                try: shutil.rmtree(long_src)
                except Exception as e: print(f"     Warning: Could not remove empty source folder: {e}")
            else:
                shutil.move(long_src, long_dst)
            moved_folders.append(folder)
            
    # 3. Update all markdown file image references
    md_files = [f for f in os.listdir(long_cat) if f.lower().endswith(".md")]
    print(f"  Updating references in {len(md_files)} markdown files...")
    
    for md_name in md_files:
        md_path = cat_path / md_name
        long_md = make_long_path(md_path)
        
        try:
            with open(long_md, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
                
            updated_content = content
            replacements_made = 0
            
            for folder in img_folders:
                # We need to replace any reference to this folder with _images/folder
                # Common patterns in Markdown:
                # 1. folder/image.png
                # 2. folder\image.png
                # 3. folder\\image.png
                
                # Check if the folder is in the content before doing heavy regex
                if folder in content:
                    # Let's perform careful replacements
                    # Avoid double-prepending: only prepend '_images/' if it's not already prepended with '_images/'
                    
                    # Pattern matching "folder/" not preceded by "_images/"
                    # We can use negative lookbehind: (?<!_images/)folder/
                    # Note: in Python re, lookbehinds must be fixed width, which (?<!_images/) is (7 chars).
                    
                    # Replace forward slash
                    pattern_fs = re.compile(rf'(?<!_images/)(?<!_images\\){re.escape(folder)}/')
                    updated_content, count_fs = pattern_fs.subn(f"_images/{folder}/", updated_content)
                    replacements_made += count_fs
                    
                    # Replace backward slashes (single or double)
                    pattern_bs = re.compile(rf'(?<!_images/)(?<!_images\\){re.escape(folder)}\\')
                    updated_content, count_bs = pattern_bs.subn(f"_images/{folder}/", updated_content)
                    replacements_made += count_bs
                    
            if updated_content != content:
                if not dry_run:
                    with open(long_md, "w", encoding="utf-8") as f:
                        f.write(updated_content)
                print(f"    [UPDATED] {md_name} ({replacements_made} references updated)")
            else:
                print(f"    [NO CHANGE] {md_name}")
                
        except Exception as e:
            print(f"    [ERROR] Failed to process {md_name}: {e}")

def main(dry_run=False):
    mode = "DRY RUN" if dry_run else "THỰC THI CHÍNH THỨC"
    print(f"=== KHỞI CHẠY TÁI CẤU TRÚC HÌNH ẢNH ({mode}) ===")
    
    # Process categories 01 through 09
    for i in range(1, 10):
        # Find folder starting with two digits
        cat_folder = None
        for item in os.listdir(make_long_path(BASE_DIR)):
            if item.startswith(f"{i:02d}"):
                cat_folder = BASE_DIR / item
                break
                
        if cat_folder and os.path.isdir(make_long_path(cat_folder)):
            process_category(cat_folder, dry_run=dry_run)
            
    print(f"\n=== HOÀN TẤT TÁI CẤU TRÚC HÌNH ẢNH ({mode}) ===")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Tái cấu trúc thư mục hình ảnh theo Phương án B")
    parser.add_argument("--dry-run", action="store_true", help="Chạy thử nghiệm không thay đổi tệp")
    args = parser.parse_args()
    
    # We will first run with dry-run then real run in terminal commands
    main(dry_run=args.dry_run)
