import sys

sys.stdout.reconfigure(encoding='utf-8')

draft_path = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md"

with open(draft_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Add literature benchmark from CA 22.07 to Section 3.1.1 BET discussion
old_bet_text = "Diện tích bề mặt riêng ($S_{BET}$) kỳ vọng đạt trên $300 \\text{ m}^2\\text{/g}$, lớn hơn đáng kể so với sợi nguyên liệu thô."
new_bet_text = """Diện tích bề mặt riêng ($S_{BET}$) kỳ vọng đạt trên $300 \\text{ m}^2\\text{/g}$, lớn hơn đáng kể so với sợi nguyên liệu thô.

> **[Đối chứng y văn mới — Notebook CA 22.07]:** Dữ liệu đối chiếu từ các nghiên cứu carbon aerogel tiền chất sinh học (cellulose/lignin aerogels) cho thấy bước cacbon hóa và nhiệt phân kích hoạt có thể đẩy diện tích bề mặt riêng $S_{BET}$ tăng từ hàng trăm lần: từ $121 \\text{ m}^2\\text{/g}$ (carbon aerogel từ *kraft lignin*) đến $1873 - 2825 \\text{ m}^2\\text{/g}$ (khi kích hoạt bằng $\\text{CO}_2$ từ khuôn nanofibril cellulose). Đối với vật liệu Fe/N-CA trong đề tài, việc không sử dụng chất kích hoạt hóa học mạnh ($\\text{KOH}$ hoặc $\\text{CO}_2$ nhiệt độ cao) nhằm mục đích **tránh thiêu kết hoặc làm tổn thất các cụm tâm xúc tác $Fe-N_4$ phân tán cao**. Do đó, mức $S_{BET} > 300 \\text{ m}^2\\text{/g}$ là điểm cân bằng tối ưu giữa việc duy trì độ xốp phân cấp để khuếch tán ion và bảo toàn tối đa mật độ tâm hoạt tính điện hóa.
"""

if old_bet_text in text:
    text = text.replace(old_bet_text, new_bet_text)
    with open(draft_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully added CA 22.07 literature benchmark to Master Draft!")
else:
    print("Target BET text not found.")
