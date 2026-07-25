import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

draft_path = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md"
plan_path = r"C:\Users\ADMIN\.gemini\antigravity\brain\a0372ab0-fcf7-4d29-b4f1-e005dcc141ca\implementation_plan.md"

with open(draft_path, 'r', encoding='utf-8') as f:
    draft = f.read()
    
with open(plan_path, 'r', encoding='utf-8') as f:
    plan = f.read()

# Extract the core of the plan (from Phần 1 to end of Phần 5)
start_plan = plan.find('## Phần 1 — Hoạt hóa')
end_plan = plan.find('## Phần 6 — Câu hỏi cần xác minh')

if start_plan == -1 or end_plan == -1:
    print("Could not extract plan content.")
    sys.exit(1)

plan_content = plan[start_plan:end_plan].strip()

# Now find where to put it in the draft
start_draft = draft.find('### 8a. Nghiền, rây & lưu trữ')
end_draft = draft.find('### 8g. Đánh giá Repeatability, Reproducibility, Stability')

if start_draft == -1 or end_draft == -1:
    # Try finding GĐ 8 start
    start_draft = draft.find('GĐ 8 — CHẾ TẠO ĐIỆN CỰC')
    end_draft = draft.find('## TỔNG KẾT: QUALITY GATE')

if start_draft == -1 or end_draft == -1:
    print("Could not find insertion points in draft.")
    sys.exit(1)

# Replace the block
new_draft = draft[:start_draft] + "### THÔNG SỐ VÀ QUY TRÌNH (SOP) CẬP NHẬT\n\n" + plan_content + "\n\n" + draft[end_draft:]

with open(draft_path, 'w', encoding='utf-8') as f:
    f.write(new_draft)
    
print("Successfully updated GĐ 8 in Master Thesis Draft.")
