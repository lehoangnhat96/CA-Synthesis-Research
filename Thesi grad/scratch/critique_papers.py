import subprocess
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

notebook_id = "a003f073-f293-48a4-83fb-1d46752272a7"

query = """
Hãy phân tích chính xác thành phần hóa chất, tiền chất và cơ chế được sử dụng trong 3 bài báo:
1. Enhanced Mechanical Stability and Hydrophobicity of Cellulose Aerogels via Quantitative Doping of Nano-Lignin
2. Preparation of High-Strength Sustainable Lignocellulose Gels and Their Applications for Antiultraviolet Weathering and Dye Removal
3. Promoted hydrogel formation of lignin-containing arabinoxylan aerogel using cellulose nanofibers as a functional biomaterial

Vui lòng làm rõ:
- Các hóa chất/tiền chất cụ thể được sử dụng trong các bài báo này là gì?
- Sự khác biệt về mặt bản chất hóa học giữa các hệ vật liệu này (aerogel polysaccharide/lignin chưa nung) với vật liệu Carbon Aerogel đã qua nung nhiệt phân (Fe/N-CA) phối trộn binder Chitosan/Nafion trên điện cực GCE trong đề tài của tôi là gì?
- Liệu việc kế thừa hay so sánh cơ chế độ bền màng/liên kết chéo từ 3 bài báo này vào đề tài Fe/N-CA có điểm nào bị lệch bản chất hóa học hoặc không tương thích hay không?
"""

cmd = [
    "uv", "run", "--with", "mcp", 
    r"C:\Users\ADMIN\.gemini\antigravity\scratch\run_mcp_tool.py", 
    "notebook_query", 
    json.dumps({"notebook_id": notebook_id, "query": query})
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
print(res.stdout)
