import os
import difflib

root = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626"
folder = os.path.join(root, "Archive_Old_Versions")

def safe_print(text):
    print(text.encode('ascii', 'replace').decode('ascii'))

def compare_files(f1_name, f2_name):
    p1 = os.path.join(folder, f1_name)
    p2 = os.path.join(folder, f2_name)
    
    if not os.path.exists(p2):
        p2 = os.path.join(root, f2_name)
        
    with open(p1, 'r', encoding='utf-8') as f:
        t1 = f.read()
    with open(p2, 'r', encoding='utf-8') as f:
        t2 = f.read()
        
    safe_print(f"=== SO SANH: {f1_name} VS {f2_name} ===")
    safe_print(f"Size: {len(t1)} vs {len(t2)} chars")
    
    l1 = t1.split('\n')
    l2 = t2.split('\n')
    safe_print(f"Lines: {len(l1)} vs {len(l2)}")
    
    diff = list(difflib.unified_diff(l1, l2, fromfile=f1_name, tofile=f2_name, n=0))
    safe_print(f"Diff lines count: {len(diff)}")
    
    safe_print("Diff details:")
    count = 0
    for line in diff:
        if line.startswith(('+', '-')) and not line.startswith(('+++', '---')):
            safe_print(f"  {line[:120]}")
            count += 1
            if count >= 15:
                break
    safe_print("\n")

compare_files("01_Viet_TongQuan_va_DoiChieu_DacTrung_VatLieu.md", "Phan1_TongQuan_Va_DacTrung_VatLieu.md")
compare_files("03_LuanAn_KeThua_ThaoTac_va_CoChe_ChiTiet.md", "Phan3_KetQua_ThaoLuan_ChiTiet.md")
