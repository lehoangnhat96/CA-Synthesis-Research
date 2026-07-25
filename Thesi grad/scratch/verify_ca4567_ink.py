import subprocess
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

notebook_id = "77de0828-7583-4042-baae-8b1210d09d9c" # CA 4 5 6 7

query = """
Vui lòng trích xuất NGUYÊN VĂN quy trình pha mực in (ink formulation) và dung dịch chất kết dính (binder) từ các bài báo trong notebook này (đặc biệt là bài báo dùng Chitosan).
Cụ thể:
1. Vật liệu carbon (Fe-CA, N-CA, RGO, CNT, hay carbon aerogel) được cân bao nhiêu mg?
2. Dung môi phân tán chính là gì (Ethanol, Nước, Acetic acid, DMF, hay hỗn hợp)? Thể tích bao nhiêu mL/µL?
3. Binder được pha như thế nào? Nồng độ Chitosan là bao nhiêu %? Có pha chung với Nafion không? Tỉ lệ pha Binder chính xác là bao nhiêu?
"""

cmd = [
    "uv", "run", "--with", "mcp", 
    r"C:\Users\ADMIN\.gemini\antigravity\scratch\run_mcp_tool.py", 
    "notebook_query", 
    json.dumps({"notebook_id": notebook_id, "query": query})
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
print(res.stdout)
