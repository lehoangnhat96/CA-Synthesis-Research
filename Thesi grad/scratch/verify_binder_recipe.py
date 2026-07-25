import subprocess
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def query_nb(notebook_id, query):
    cmd = [
        "uv", "run", "--with", "mcp", 
        r"C:\Users\ADMIN\.gemini\antigravity\scratch\run_mcp_tool.py", 
        "notebook_query", 
        json.dumps({"notebook_id": notebook_id, "query": query})
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    return res.stdout

query = """
Vui lòng trích xuất NGUYÊN VĂN quy trình pha mực in (ink formulation) và dung dịch chất kết dính (binder) từ các bài báo trong notebook này.
Cụ thể:
1. Vật liệu carbon (Fe-CA, N-CA, hay carbon aerogel) được cân bao nhiêu mg?
2. Dung môi phân tán chính là gì (DMF, Ethanol, Nước, hay hỗn hợp)? Thể tích bao nhiêu mL/µL?
3. Loại binder được dùng là gì (Nafion riêng lẻ, Chitosan riêng lẻ, hay Composite Chitosan + Nafion)?
4. Nồng độ % chính xác và thể tích (µL) của Nafion và Chitosan là bao nhiêu? Binder được pha loãng trong dung môi nào trước khi cho vào ink?
"""

print("=== CHECKING NOTEBOOK CA 8 ===")
print(query_nb("27c1da2f-329a-4410-9547-5e92efaeb83b", query))

print("\n=== CHECKING NOTEBOOK CA 4 5 6 7 ===")
print(query_nb("77de0828-7583-4042-baae-8b1210d09d9c", query))
