import json
import sys
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

args1 = {
    "notebook_id": "8ae055dd-590e-4430-8afb-afcb31320320",
    "query": "Dựa trên tài liệu, phân tích claim sau: \"Fe[3+] in (Ni,Fe)OOH has an unusually short Fe-O bond distance and constitutes the highly active site for Oxygen Evolution Reaction, not Ni.\". Trả lời theo đúng định dạng 3 dòng:\n- Cơ chế: ...\n- Ứng dụng vs SOP: ...\n- Bằng chứng hội tụ: ..."
}
args2 = {
    "notebook_id": "c2f074f1-396a-4df0-a32e-938c2433e3e4",
    "query": "Dựa trên tài liệu, phân tích claim sau: \"Phytic acid/graphene oxide nanocomposites modified electrode for electrochemical sensing of dopamine with LOD 16 nM in the presence of AA and UA.\". Trả lời theo đúng định dạng 3 dòng:\n- Cơ chế: ...\n- Ứng dụng vs SOP: ...\n- Bằng chứng hội tụ: ..."
}
args3 = {
    "notebook_id": "c2f074f1-396a-4df0-a32e-938c2433e3e4",
    "query": "Dựa trên tài liệu, phân tích claim sau: \"Sensitive and Selective Electrochemical Detection of Lead(II) Based on Waste-Biomass-Derived Carbon Quantum Dots@Zeolitic Imidazolate Framework-8 with LOD 0.04 nM.\". Trả lời theo đúng định dạng 3 dòng:\n- Cơ chế: ...\n- Ứng dụng vs SOP: ...\n- Bằng chứng hội tụ: ..."
}

def run_query(args, num):
    print(f"--- QUERY {num} ---")
    cmd = ["uv", "run", "--with", "mcp", r"C:\Users\ADMIN\.gemini\antigravity\scratch\run_mcp_tool.py", "notebook_query", json.dumps(args)]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print("ERR:", res.stderr)
    print("-------------------\n")

run_query(args1, 1)
run_query(args2, 2)
run_query(args3, 3)
