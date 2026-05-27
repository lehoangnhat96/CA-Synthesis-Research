"""
Convert: "View of Investigate coir fibers' properties...NaOH solution.pdf"
to proper Markdown with image extraction.
"""
import os
import sys
import shutil
import hashlib
import multiprocessing
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

try:
    import fitz
except ImportError:
    print("ERROR: pymupdf not installed. Run: pip install pymupdf")
    sys.exit(1)

try:
    import pymupdf4llm
except ImportError:
    print("WARNING: pymupdf4llm not found, using basic fallback")
    pymupdf4llm = None


def make_long_path(path):
    abs_path = os.path.abspath(str(path))
    if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
        abs_path = abs_path.replace('/', '\\')
        return '\\\\?\\' + abs_path
    return abs_path


def convert_basic(pdf_path, md_path, images_dir):
    """Basic PyMuPDF conversion with full image extraction."""
    long_pdf = make_long_path(pdf_path)
    long_md  = make_long_path(md_path)
    long_img = make_long_path(images_dir)

    doc = fitz.open(long_pdf)
    os.makedirs(long_img, exist_ok=True)
    blocks = []
    img_count = 0
    img_dir_name = os.path.basename(str(images_dir))

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks.append(f"\n## Page {page_num + 1}\n")
        blocks.append(page.get_text("text"))

        try:
            for img_idx, img_info in enumerate(page.get_images(full=True)):
                xref = img_info[0]
                base_image = doc.extract_image(xref)
                ext  = base_image["ext"]
                name = f"page-{page_num+1:03d}-img-{img_idx+1:02d}.{ext}"
                img_path = os.path.join(long_img, name)
                with open(img_path, "wb") as f:
                    f.write(base_image["image"])
                blocks.append(f"\n![Image {img_count+1}]({img_dir_name}/{name})\n")
                img_count += 1
        except Exception as ex:
            print(f"  Warning page {page_num+1} image: {ex}")

    content = "\n".join(blocks)
    with open(long_md, "w", encoding="utf-8") as f:
        f.write(content)

    total_lines = content.count("\n")
    print(f"  Basic conversion done: {img_count} images, ~{total_lines} lines")
    return True


def convert_with_pymupdf4llm(pdf_path, md_path, images_dir, workspace_dir):
    """High-quality conversion using pymupdf4llm (temp-copy workaround)."""
    h = hashlib.md5(str(pdf_path).encode()).hexdigest()[:8]
    temp_pdf = workspace_dir / f"_temp_{h}_conv_.pdf"
    temp_md  = workspace_dir / f"_temp_{h}_conv_.md"
    temp_img = workspace_dir / f"_temp_{h}_conv__images"

    try:
        shutil.copy2(make_long_path(pdf_path), make_long_path(temp_pdf))
        os.makedirs(make_long_path(temp_img), exist_ok=True)

        md_content = pymupdf4llm.to_markdown(
            doc=str(temp_pdf),
            write_images=True,
            image_path=str(temp_img),
            image_format="png"
        )

        # Fix image references to point to actual images_dir name
        img_dir_name = os.path.basename(str(images_dir))
        md_content = md_content.replace(temp_img.name + "/", img_dir_name + "/")
        md_content = md_content.replace(temp_img.name, img_dir_name)

        with open(make_long_path(temp_md), "w", encoding="utf-8") as f:
            f.write(md_content)

        shutil.move(make_long_path(temp_md), make_long_path(md_path))

        long_t_img = make_long_path(temp_img)
        long_d_img = make_long_path(images_dir)
        if os.path.exists(long_t_img) and os.listdir(long_t_img):
            if os.path.exists(long_d_img):
                shutil.rmtree(long_d_img)
            shutil.move(long_t_img, long_d_img)
        elif os.path.exists(long_t_img):
            shutil.rmtree(long_t_img)

        print("  pymupdf4llm conversion done (high quality).")
        return True

    except Exception as e:
        print(f"  pymupdf4llm error: {e}")
        return False

    finally:
        for p in [temp_pdf, temp_md]:
            lp = make_long_path(p)
            if os.path.exists(lp):
                try: os.remove(lp)
                except: pass
        lt = make_long_path(temp_img)
        if os.path.exists(lt):
            try: shutil.rmtree(lt)
            except: pass


def main():
    workspace_dir = Path(__file__).parent.parent
    cat_dir = workspace_dir / "1 Ref materials" / "01_Tien_xu_ly_Nguyen_lieu"

    # Find the actual file using os.listdir (avoids apostrophe path issues)
    pdf_path = None
    md_path  = None
    img_dir  = None

    for fname in os.listdir(str(cat_dir)):
        if "nvestigate" in fname and fname.endswith(".pdf"):
            pdf_path = cat_dir / fname
            stem = fname[:-4]  # remove .pdf
            md_path  = cat_dir / (stem + ".md")
            img_dir  = cat_dir / (stem + "_images")
            break

    if pdf_path is None:
        print("ERROR: Could not find 'Investigate coir fibers' PDF in 01_Tien_xu_ly_Nguyen_lieu")
        sys.exit(1)

    print(f"PDF  : {pdf_path.name}")
    print(f"MD   : {md_path.name}")
    print(f"IMGS : {img_dir.name}")
    print(f"Size : {os.path.getsize(make_long_path(pdf_path)):,} bytes")
    print()

    # Remove empty MD if exists
    lmd = make_long_path(md_path)
    if os.path.exists(lmd):
        size = os.path.getsize(lmd)
        if size < 100:
            os.remove(lmd)
            print(f"  Removed empty MD ({size} bytes).")
        else:
            print(f"  MD already exists ({size} bytes) — will overwrite.")
            os.remove(lmd)

    # Try pymupdf4llm first, then fallback
    success = False
    if pymupdf4llm is not None:
        print("Trying pymupdf4llm (high quality)...")
        success = convert_with_pymupdf4llm(pdf_path, md_path, img_dir, workspace_dir)

    if not success:
        print("Using basic PyMuPDF...")
        success = convert_basic(pdf_path, md_path, img_dir)

    if success:
        print()
        print("=== Preview (first 30 lines of MD) ===")
        with open(make_long_path(md_path), "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines[:30]:
            print(line.rstrip())
        print(f"\n... Total: {len(lines)} lines, {os.path.getsize(make_long_path(md_path)):,} bytes")

        # Show image count
        lid = make_long_path(img_dir)
        if os.path.exists(lid):
            img_files = [x for x in os.listdir(lid) if not x.startswith('.')]
            print(f"Images extracted: {len(img_files)}")
    else:
        print("CONVERSION FAILED")
        sys.exit(1)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
