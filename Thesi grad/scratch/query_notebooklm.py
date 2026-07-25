import subprocess
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def run_query(notebook_id, query):
    cmd = [
        "uv", "run", "--with", "mcp", 
        r"C:\Users\ADMIN\.gemini\antigravity\scratch\run_mcp_tool.py", 
        "notebook_query", 
        json.dumps({"notebook_id": notebook_id, "query": query})
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

notebook_id = "77de0828-7583-4042-baae-8b1210d09d9c" # CA 4 5 6 7

queries = [
    "Dựa vào các bài báo, hãy cho biết chính xác tỉ lệ pha trộn thể tích giữa dung dịch Chitosan và dung dịch Nafion để tạo thành Composite Binder là bao nhiêu (ví dụ: 1:1, 2:1)? Và nồng độ của dung dịch Chitosan ban đầu là bao nhiêu % (ví dụ 1 wt% hay 0.5 wt%)?",
    "Trong quy trình chế tạo điện cực (drop-casting), sau khi nhỏ hỗn hợp mực in (ink) lên GCE và sấy khô, có bước nung nhẹ (annealing) nào ở nhiệt độ 60-80°C hay không? Nhiệt độ và thời gian sấy màng chính xác là bao nhiêu?",
    "Thể tích cell đo điện hóa (electrochemical cell volume) thường được sử dụng trong các phép đo CV, DPV, SWASV là bao nhiêu mL (ví dụ 10 mL, 25 mL, 50 mL)?",
    "Trong các bài báo, ngoài Pb và Cd, tác giả có đề cập đến việc đo/phát hiện các kim loại Đồng (Cu), Kẽm (Zn), Niken (Ni) bằng kỹ thuật SWASV hay không? Nếu có, hãy liệt kê thông số LOD và độ ưu tiên của chúng."
]

for i, q in enumerate(queries):
    print(f"--- QUERY {i+1} ---")
    print(f"Q: {q}")
    ans = run_query(notebook_id, q)
    print(f"A: {ans}")
    print("\n")
