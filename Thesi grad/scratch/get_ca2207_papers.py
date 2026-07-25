import subprocess
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

notebook_id = "a0372ab0-fcf7-4d29-b4f1-e005dcc141ca"

cmd = [
    "uv", "run", "--with", "mcp", 
    r"C:\Users\ADMIN\.gemini\antigravity\scratch\run_mcp_tool.py", 
    "notebook_get", 
    json.dumps({"notebook_id": "a003f073-f293-48a4-83fb-1d46752272a7"})
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
print(res.stdout)
