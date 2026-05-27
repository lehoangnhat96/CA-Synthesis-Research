import os
import json
from pathlib import Path

# Root path to the Ref materials folder
def get_root_path():
    return Path(r"D:\\1 Master's Ana Chem\\1 Master's thesis\\Carbon Aerogel\\1 Ref materials")

def is_image(file_path: Path):
    return file_path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"}

def discover_files():
    root = get_root_path()
    data = {"markdown": [], "pdf": [], "images": []}
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            p = Path(dirpath) / name
            if p.suffix.lower() == ".md":
                data["markdown"].append(str(p))
            elif p.suffix.lower() == ".pdf":
                data["pdf"].append(str(p))
            elif is_image(p):
                data["images"].append(str(p))
    # Save JSON list for later steps
    out_path = root.parent / "ref_materials_file_list.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Discovered {len(data['markdown'])} markdown, {len(data['pdf'])} pdf, {len(data['images'])} images.")
    print(f"File list saved to {out_path}")

if __name__ == "__main__":
    discover_files()
