"""
reclassify_ref_materials.py
============================
Di chuyen cac bo file (PDF + MD + _images) theo ket qua audit.
- Doi ten thu muc _images sang dang ngan (<=50 ky tu)
- Cap nhat duong dan anh trong file MD sau khi doi ten
- Di chuyen dong thoi: PDF + MD + thu muc anh
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

BASE = Path(r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials")
ARCHIVE = BASE.parent / "Archive_Reclassified"

CATS = {
    "01": BASE / "01_Tien_xu_ly_Nguyen_lieu",
    "02": BASE / "02_Doping_va_Gel_hoa",
    "03": BASE / "03_Say_va_Nung_Nhiet_phan",
    "04": BASE / "04_Cam_bien_Dien_hoa_Sinh_hoc",
    "05": BASE / "05_Cross_Linker_va_Tao_mang",
    "06": BASE / "06_Setup_Do_Dien_hoa",
    "07": BASE / "07_Giao_trinh_Ly_thuyet",
    "08": BASE / "08_Review_va_Tong_quan",
    "09": BASE / "09_Tai_lieu_Quy_trinh_AI",
    "archive": ARCHIVE,
}

def make_short_img_name(stem: str, max_len: int = 48) -> str:
    """
    Tao ten thu muc anh ngan gon tu stem cua file.
    Quy tac: giu toi da max_len ky tu, them hau to _img
    Loai bo ky tu dac biet, giu chu/so/gach duoi.
    """
    cleaned = re.sub(r"[^\w\s-]", "", stem)
    cleaned = re.sub(r"[\s\-]+", "_", cleaned).strip("_")
    cleaned = re.sub(r"_+", "_", cleaned)
    if len(cleaned) > max_len:
        cleaned = cleaned[:max_len].rstrip("_")
    return cleaned + "_img"

def update_md_image_refs(md_path: Path, old_img_dir: str, new_img_dir: str):
    """Cap nhat tat ca duong dan anh trong file MD."""
    if not md_path.exists() or md_path.stat().st_size < 10:
        return
    try:
        content = md_path.read_text(encoding="utf-8", errors="replace")
        updated = content.replace(old_img_dir + "/", new_img_dir + "/")
        updated = updated.replace(old_img_dir, new_img_dir)
        if updated != content:
            md_path.write_text(updated, encoding="utf-8")
            print(f"    [MD UPDATED] refs: {old_img_dir} -> {new_img_dir}")
    except Exception as e:
        print(f"    [WARNING] Could not update MD refs: {e}")

def find_actual_stem(directory: Path, search_stem: str):
    """Tim ten file thuc te trong thu muc bang partial match."""
    search_lower = search_stem.lower()
    best = None
    best_len = 0
    for f in directory.iterdir():
        if not f.is_file():
            continue
        if f.suffix not in (".pdf", ".md"):
            continue
        fl = f.stem.lower()
        # Uu tien match dai nhat
        if search_lower in fl or fl in search_lower:
            if len(f.stem) > best_len:
                best = f.stem
                best_len = len(f.stem)
    return best

def move_file_set(stem: str, src_cat: str, dst_cat: str, dry_run: bool = False):
    """
    Di chuyen bo file: {stem}.md + {stem}.pdf + {stem}_images/
    tu src_cat sang dst_cat, voi ten thu muc anh duoc rut gon.
    """
    src_dir = CATS[src_cat]
    dst_dir = CATS[dst_cat]

    actual_stem = find_actual_stem(src_dir, stem)
    if actual_stem is None:
        print(f"  [NOT FOUND] '{stem[:50]}' in cat {src_cat}")
        return False

    pdf_src = src_dir / f"{actual_stem}.pdf"
    md_src  = src_dir / f"{actual_stem}.md"
    img_src = src_dir / f"{actual_stem}_images"

    # Ten thu muc anh moi (ngan gon)
    short_img = make_short_img_name(actual_stem)
    img_dst = dst_dir / short_img

    pdf_dst = dst_dir / f"{actual_stem}.pdf"
    md_dst  = dst_dir / f"{actual_stem}.md"

    if dry_run:
        print(f"  [DRY] {src_cat}->{dst_cat}: {actual_stem[:60]}")
        print(f"        PDF={pdf_src.exists()} MD={md_src.exists()} IMG={img_src.exists()} short_img='{short_img}'")
        return True

    dst_dir.mkdir(parents=True, exist_ok=True)
    moved = []

    # Move PDF
    if pdf_src.exists():
        if not pdf_dst.exists():
            shutil.move(str(pdf_src), str(pdf_dst))
            moved.append("PDF")
        else:
            print(f"    [SKIP PDF exists] {actual_stem[:50]}.pdf")

    # Move images folder (rename to short name)
    if img_src.exists():
        if img_dst.exists():
            for item in img_src.iterdir():
                shutil.move(str(item), str(img_dst / item.name))
            try: img_src.rmdir()
            except: pass
        else:
            shutil.move(str(img_src), str(img_dst))
        moved.append(f"IMG->{short_img}")

    # Update MD refs then move
    if md_src.exists():
        old_img_name = f"{actual_stem}_images"
        update_md_image_refs(md_src, old_img_name, short_img)
        if not md_dst.exists():
            shutil.move(str(md_src), str(md_dst))
            moved.append("MD")
        else:
            print(f"    [SKIP MD exists] {actual_stem[:50]}.md")

    status = ", ".join(moved) if moved else "nothing moved"
    print(f"  [MOVED {src_cat}->{dst_cat}] {actual_stem[:55]} | {status}")
    return True

def delete_duplicate(stem: str, cat: str, dry_run: bool = False):
    """Xoa 1 file trung lap (MD + PDF + _images)."""
    d = CATS[cat]
    actual_stem = find_actual_stem(d, stem)
    if actual_stem is None:
        print(f"  [NOT FOUND for DELETE] '{stem[:50]}' in {cat}")
        return

    if dry_run:
        print(f"  [DRY DELETE] {cat}/{actual_stem[:60]}")
        return

    deleted = []
    for suffix in [".md", ".pdf"]:
        fp = d / f"{actual_stem}{suffix}"
        if fp.exists():
            fp.unlink()
            deleted.append(suffix)
    img_dir = d / f"{actual_stem}_images"
    if img_dir.exists():
        shutil.rmtree(str(img_dir))
        deleted.append("_images/")
    print(f"  [DELETED] {actual_stem[:60]} | {', '.join(deleted)}")


def main(dry_run=False):
    mode = "DRY RUN" if dry_run else "THUC THI"
    print(f"=== {mode}: Tai phan loai file 1 Ref materials ===\n")

    ARCHIVE.mkdir(parents=True, exist_ok=True)

    # ============================================================
    # BUOC 1: XOA FILE TRUNG LAP
    # ============================================================
    print("--- BUOC 1: Xoa file trung lap ---")
    delete_duplicate("Ung dung cam bien sinh hoc dien hoa SPE", "04", dry_run)
    delete_duplicate("Tong hop vat lieu cellulose aerogel tu xo dua de", "08", dry_run)
    delete_duplicate("2 Controlling NDoping Nature at Carbon Aerogels from Biomass for", "05", dry_run)

    # ============================================================
    # BUOC 2: ARCHIVE FILE LAC CHU DE
    # ============================================================
    print("\n--- BUOC 2: Archive file lac chu de ---")
    archive_list = [
        ("A RESEARCH ON FABRICATION OF RECYCLED CONCRETE USING COCONUT FIBER", "02"),
        ("Insulation performance of the coconut husk", "02"),
        ("A Sustainable Approach for the Development of Cellulose-Based Food", "05"),
        ("Preparation of Cellulose Nanocrystals Biofilm from Coconut Coir as", "05"),
    ]
    for stem, src in archive_list:
        move_file_set(stem, src, "archive", dry_run)

    # ============================================================
    # BUOC 3: DI CHUYEN SANG DANH MUC DUNG
    # ============================================================
    print("\n--- BUOC 3: Di chuyen sang danh muc dung ---")
    moves = [
        # 01 -> 02
        ("Ice-TemplatingofLigninandCelluloseNanofiber-BasedCarbon", "01", "02"),
        ("MultifunctionalCarbonAerogelswithHierarchicalAnisotropic", "01", "02"),

        # 02 -> 01
        ("Thermochemical Characterization of Coconut Husk Rice Husk", "02", "01"),
        ("Than sinh hoc tu phu pham nong nghiep Tinh chat", "02", "01"),

        # 02 -> 04
        ("Activated carbon derived from coconut coir pith as high performance", "02", "04"),
        ("Activated carbons derived from coconut", "02", "04"),
        ("A_carbonized_coconut_husk_for_supercapacitor_elect", "02", "04"),
        ("Performance and mechanisms of waste-based carbon adsorbents", "02", "04"),

        # 02 -> 08
        ("Coconut shell and husk biochar A review", "02", "08"),
        ("Bio-Based Aerogels for the Removal of Heavy Metal Ions", "02", "08"),

        # 02 -> 03
        ("TONG HOP VAT LIEU CARBON NANO SOI TREN NEN THAN", "02", "03"),

        # 04 -> 08
        ("Carbon Aerogels as Electrocatalysts for Sustainable Energy", "04", "08"),
        ("Carbon Aerogels for Environmental Clean-Up", "04", "08"),
        ("Recent Advanced Supercapacitor A Review of Storage Mechanisms", "04", "08"),
        ("Biomass-Derived Carbon Aerogels for ORR OER Bifunctional", "04", "08"),

        # 04 -> 03
        ("Lupin hull cellulose nanofiber aerogel preparation by supercritical", "04", "03"),

        # 04 -> 02
        ("Cellulose Diacetate Aerogels with Low Drying Shrinkage", "04", "02"),
        ("Heteroatom tuning in agarose derived carbon aerogel", "04", "02"),
        ("Fe-Cluster Pushing Electrons to N-Doped Graphitic Layers", "04", "02"),

        # 04 -> 01
        ("Upcycling coconut husk coir by extraction of", "04", "01"),

        # 05 -> 08
        ("Advances in Manufacturing Composite Carbon", "05", "08"),
        ("Bio-Based Aerogels in Energy Storage Systems", "05", "08"),
        ("Recent Developments in Carbon-Based Nanocomposites for Fuel Cell", "05", "08"),

        # 05 -> 02
        ("Electrochemically Controlled Synthesis of Ultrathin Nickel Hydroxid", "05", "02"),

        # 06 -> 08
        ("Carbon Aerogels Synthesis Modification and Multifunctional", "06", "08"),

        # 06 -> 04
        ("PHAN HUY p-NITROPHENOL BANG KY THUAT FENTON DIEN HOA", "06", "04"),

        # 07 -> 02
        ("TONG HOP VAT LIEU MnO2CARBON AEROGEL UNG DUNG", "07", "02"),

        # 08 -> 02
        ("1 Sustainable Hydrothermal Carbonization Synthesis of Iron-Nitrogen", "08", "02"),
        ("Dieu che nanocomposite Ag Fe3O4 Nano tinh the cellulose bang", "08", "02"),

        # 09 -> 02
        ("Carbon Aerogels and Monoliths Control of Porosity and", "09", "02"),
    ]

    for stem, src, dst in moves:
        move_file_set(stem, src, dst, dry_run)

    print(f"\n=== HOAN TAT ({mode}) ===")
    if not dry_run:
        print("Nho chay sync_ref_lib.ps1 de dong bo 1 Ref materials -> 2 Ref lib")
    print(f"Archive: {ARCHIVE}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Tai phan loai file MD/PDF/images theo ket qua audit")
    parser.add_argument("--dry-run", action="store_true", help="Kiem tra khong thay doi file")
    args = parser.parse_args()
    main(dry_run=args.dry_run)
