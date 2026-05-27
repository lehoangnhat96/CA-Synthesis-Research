import os
import shutil
import sys

# Set standard output encoding to utf-8 if possible
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

# Define paths
base_dir = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel"
archive_dir = os.path.join(base_dir, "2 Ref lib", "Archive_Drafts")

# Ensure archive directory exists
os.makedirs(archive_dir, exist_ok=True)

# Subfolders to archive
folders_to_archive = {
    "Quy trình AI": os.path.join(archive_dir, "Quy_trinh_AI"),
    "1 C.A_ syn workflow": os.path.join(archive_dir, "1_CA_syn_workflow")
}

for src_rel_path, dest_path in folders_to_archive.items():
    src_path = os.path.join(base_dir, src_rel_path)
    if os.path.exists(src_path):
        os.makedirs(dest_path, exist_ok=True)
        # Move all contents
        items = os.listdir(src_path)
        print(f"Archiving {len(items)} items from '{src_rel_path}'...")
        for item in items:
            item_src = os.path.join(src_path, item)
            item_dest = os.path.join(dest_path, item)
            
            # Avoid self-archiving if they overlap or if it's already there
            if os.path.exists(item_dest):
                try:
                    if os.path.isdir(item_dest):
                        shutil.rmtree(item_dest)
                    else:
                        os.remove(item_dest)
                except Exception as e:
                    print(f"Error removing existing target: {e}")
                    
            try:
                shutil.move(item_src, item_dest)
            except Exception as e:
                # Safe print or ignore
                print(f"Error moving an item: {type(e).__name__}")
        print(f"Successfully archived contents of '{src_rel_path}'")
    else:
        print(f"Source path does not exist: {src_path.encode('ascii', 'replace').decode('ascii')}")

print("Archiving complete!")
