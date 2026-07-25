import subprocess
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

notebook_id = "77de0828-7583-4042-baae-8b1210d09d9c"

query = """
Vui lòng liệt kê tên đầy đủ (Title) của tất cả các bài báo/tài liệu tham khảo mà bạn đã sử dụng để trả lời các câu hỏi về thông số điện hóa (ví dụ: bài báo nói về Chitosan 2.0g pha trong 100mL acetic acid, bài báo nói về LOD của Cu là 3.83 nM, và bài báo phân tích Cu, Zn, Ni bằng SWASV).
Với mỗi bài báo, hãy trình bày ngắn gọn:
1. Tên bài báo (Title)
2. Bối cảnh nghiên cứu, đối tượng nghiên cứu của bài báo đó.
3. Hướng ứng dụng và lý do tại sao vật liệu/phương pháp trong bài đó lại quan trọng để luận văn của tôi (về Fe/N-CA) cần kế thừa.
"""

cmd = [
    "uv", "run", "--with", "mcp", 
    r"C:\Users\ADMIN\.gemini\antigravity\scratch\run_mcp_tool.py", 
    "notebook_query", 
    json.dumps({"notebook_id": notebook_id, "query": query})
]
try:
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error: {e.stderr}")
