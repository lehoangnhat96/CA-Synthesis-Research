import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

folder = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 Ref materials\01_Tien_xu_ly_Nguyen_lieu"

print("All files containing 'Investigate' or 'coir fiber':")
for f in os.listdir(folder):
    if "nvestigate" in f or "Ben Tre" in f or "coir fiber" in f.lower():
        full = os.path.join(folder, f)
        size = os.path.getsize(full) if os.path.isfile(full) else -1
        print(f"  NAME : {repr(f)}")
        print(f"  SIZE : {size} bytes")
        print()
