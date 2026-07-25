import subprocess
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

notebook_id = "a003f073-f293-48a4-83fb-1d46752272a7"

def run_mcp(tool_name, args=None):
    cmd = [
        "uv", "run", "--with", "mcp", 
        r"C:\Users\ADMIN\.gemini\antigravity\scratch\run_mcp_tool.py", 
        tool_name
    ]
    if args:
        cmd.append(json.dumps(args))
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', check=True)
        return res.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

print("=== SOURCES IN CA 22.07 ===")
print(run_mcp("notebook_get", {"notebook_id": notebook_id}))

print("\n=== SUMMARY OF CA 22.07 ===")
print(run_mcp("notebook_describe", {"notebook_id": notebook_id}))

query = "Tóm tắt các phát hiện chính, cơ chế nổi bật, số liệu thực nghiệm hoặc kết luận quan trọng trong notebook này có liên quan đến việc tổng hợp, đặc trưng (SEM, XRD, XPS, Raman, BET) và ứng dụng điện hóa (CV, EIS, DPV, SWASV) của Carbon Aerogel (CA, Fe/N-CA) để có thể cập nhật vào file master luận văn."
print("\n=== DETAILED QUERY OF CA 22.07 ===")
print(run_mcp("notebook_query", {"notebook_id": notebook_id, "query": query}))
