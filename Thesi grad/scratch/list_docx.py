import os
import time

folder = "d:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad"
files = []
for f in os.listdir(folder):
    if f.endswith('.docx') and not f.startswith('~'):
        path = os.path.join(folder, f)
        mtime = os.path.getmtime(path)
        files.append((f, mtime, os.path.getsize(path)))

files.sort(key=lambda x: x[1], reverse=True)
for f, mtime, size in files:
    print(f"{f}: last modified {time.ctime(mtime)}, size={size} bytes")
