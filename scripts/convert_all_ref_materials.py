# -*- coding: utf-8 -*-
"""
High-fidelity converter for 1 Ref materials directory.
Recursively converts all unconverted .pdf files to .md and extracts images to {pdf_stem}_images folders
within the D:\\1 Master's Ana Chem\\1 Master's thesis\\Carbon Aerogel\\1 Ref materials directory.
"""

import os
import sys
import shutil
import hashlib
from pathlib import Path

# Set console encoding to UTF-8 on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# Import PyMuPDF
try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: 'pymupdf' is not installed.")
    sys.exit(1)

try:
    import pymupdf4llm
except ImportError:
    pymupdf4llm = None


def make_long_path(path):
    abs_path = os.path.abspath(path)
    if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
        abs_path = abs_path.replace('/', '\\')
        return '\\\\?\\' + abs_path
    return abs_path


def convert_pdf_to_md_basic(pdf_path, output_md_path, images_dir):
    long_pdf = make_long_path(pdf_path)
    long_md = make_long_path(output_md_path)
    long_images = make_long_path(images_dir)
    
    try:
        doc = fitz.open(long_pdf)
    except Exception as e:
        return False, f"Failed to open PDF: {e}"
        
    text_blocks = []
    image_count = 0
    os.makedirs(long_images, exist_ok=True)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text_blocks.append(f"## Page {page_num + 1}\n")
        text_blocks.append(page.get_text("text"))
        
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
            pass
            
    md_content = "\n".join(text_blocks)
    with open(long_md, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    if os.path.exists(long_images) and not os.listdir(long_images):
        os.rmdir(long_images)
        
    return True, f"Success (fitz basic, {image_count} images extracted)"


def convert_pdf_to_md(pdf_path, output_md_path, images_dir, workspace_dir):
    if pymupdf4llm is None:
        return convert_pdf_to_md_basic(pdf_path, output_md_path, images_dir)

    temp_pdf_name = f"_temp_{hashlib.md5(str(pdf_path).encode('utf-8')).hexdigest()[:8]}_convert_.pdf"
    temp_md_name = temp_pdf_name.replace(".pdf", ".md")
    temp_images_name = temp_pdf_name.replace(".pdf", "_images")
    
    temp_pdf_path = workspace_dir / temp_pdf_name
    temp_md_path = workspace_dir / temp_md_name
    temp_images_dir = workspace_dir / temp_images_name
    
    try:
        # Clean old temp files
        for path in [temp_pdf_path, temp_md_path]:
            long_p = make_long_path(path)
            if os.path.exists(long_p):
                os.remove(long_p)
        long_t_img = make_long_path(temp_images_dir)
        if os.path.exists(long_t_img):
            shutil.rmtree(long_t_img)
            
        shutil.copy2(make_long_path(pdf_path), make_long_path(temp_pdf_path))
        
        os.makedirs(make_long_path(temp_images_dir), exist_ok=True)
        md_content = pymupdf4llm.to_markdown(
            doc=str(temp_pdf_path),
            write_images=True,
            image_path=str(temp_images_dir),
            image_format="png"
        )
        
        with open(make_long_path(temp_md_path), "w", encoding="utf-8") as f:
            f.write(md_content)
            
        shutil.move(make_long_path(temp_md_path), make_long_path(output_md_path))
        
        long_dest_images = make_long_path(images_dir)
        if os.path.exists(long_t_img) and os.listdir(long_t_img):
            if os.path.exists(long_dest_images):
                shutil.rmtree(long_dest_images)
            shutil.move(long_t_img, long_dest_images)
        elif os.path.exists(long_t_img):
            shutil.rmtree(long_t_img)
            
        return True, "Success (pymupdf4llm via temp copy)"
    except Exception as e:
        print(f"  -> pymupdf4llm failed: {e}. Falling back to basic fitz...")
        return convert_pdf_to_md_basic(pdf_path, output_md_path, images_dir)
    finally:
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


def main():
    workspace_dir = Path("d:\\1 Master's Ana Chem\\1 Master's thesis\\Carbon Aerogel")
    target_dir = workspace_dir / "1 Ref materials"
    
    print(f"=== Scanning 1 Ref materials for unconverted PDFs ===")
    
    pdf_files = []
    for root, dirs, files in os.walk(make_long_path(target_dir)):
        # Skip git or temporary folders
        if ".git" in root or "_temp_" in root:
            continue
        norm_root = Path(root[4:] if root.startswith('\\\\?\\') else root)
        for file in files:
            if file.lower().endswith(".pdf") and not file.startswith("_temp_"):
                pdf_files.append(norm_root / file)
                
    print(f"Found total: {len(pdf_files)} PDF files.")
    
    converted_count = 0
    skipped_count = 0
    
    for idx, pdf_path in enumerate(pdf_files, 1):
        md_path = pdf_path.with_suffix(".md")
        images_dir = pdf_path.parent / f"{pdf_path.stem}_images"
        
        long_md = make_long_path(md_path)
        long_images = make_long_path(images_dir)
        
        has_md = os.path.exists(long_md) and os.path.getsize(long_md) > 100
        has_images = os.path.exists(long_images) and len(os.listdir(long_images)) > 0 if os.path.exists(long_images) else False
        
        if has_md and has_images:
            print(f"[{idx}/{len(pdf_files)}] PDF already converted: {pdf_path.name} -> skipping")
            skipped_count += 1
            continue
            
        print(f"[{idx}/{len(pdf_files)}] Converting: {pdf_path.name}...")
        success, msg = convert_pdf_to_md(pdf_path, md_path, images_dir, workspace_dir)
        print(f"  -> {msg}")
        converted_count += 1
        
    print(f"\n=== REF MATERIALS PDF CONVERSION COMPLETED ===")
    print(f"Successfully converted: {converted_count}")
    print(f"Skipped (already converted): {skipped_count}")


if __name__ == "__main__":
    main()
