# update_sop.py
import os
import shutil

sop_path = r"d:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/BaoCao_TongHop_050626/Phan2_QuyTrinh_8Buoc_SOP_ChiTiet.md"
master_summary = r"d:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/1 Ref materials/All_folders_combined_summary.md"

# Create a backup if it does not exist
backup_path = sop_path + ".backup"
if not os.path.exists(backup_path):
    shutil.copyfile(sop_path, backup_path)
    print(f"Backup created at {backup_path}")
else:
    print(f"Backup already exists at {backup_path}")

# Append the master summary under a new heading
with open(sop_path, "a", encoding="utf-8") as sop_file:
    sop_file.write("\n\n## Tổng hợp các tóm tắt từ các thư mục\n\n")
    with open(master_summary, "r", encoding="utf-8") as ms:
        sop_file.write(ms.read())
        sop_file.write("\n")
print("SOP updated with master summary.")
