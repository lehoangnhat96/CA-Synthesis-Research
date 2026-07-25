import sys

sys.stdout.reconfigure(encoding='utf-8')

draft_path = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md"

with open(draft_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Update cell volume to 30 mL
text = text.replace("Pha từng lần, 25 mL", "Pha từng lần, 30 mL (thể tích cell tiêu chuẩn 30 mL, tính dư để đảm bảo điện cực ngập hoàn toàn)")

# Add core references section at the end of the SOP part, right before Phase 8g or end of Phase 8
core_refs = """

### 8g. Cơ Sở Khoa Học và Tài Liệu Kế Thừa Cốt Lõi (GĐ 8)

Các thông số thực nghiệm (Chitosan 2.0%, Cell 30 mL, không nung màng GCE) và ma trận đo SWASV được xây dựng và đối chiếu từ các công bố quốc tế cốt lõi sau:

1. **A screen-printed carbon electrode modified with a chitosan-based film for in situ heavy metal ions measurement**
   - *Bối cảnh & Ứng dụng:* Chế tạo cảm biến đo tại chỗ các kim loại (Zn, Ni, Cu, Pb, Hg, As, Fe) trong nước thải bằng kỹ thuật SWASV.
   - *Lý do kế thừa:* Cung cấp công thức chuẩn pha Chitosan (2.0g trong 100mL acid acetic 0.17M). Bài báo chứng minh cơ chế bẫy ion (chelation) mạnh mẽ của màng Chitosan với các kim loại nặng nhờ mật độ cao nhóm amine (-NH₂) và hydroxyl (-OH), là tiền đề quan trọng để cố định màng Fe/N-CA.

2. **Simultaneous determination of trace Cd(II), Pb(II) and Cu(II) by differential pulse anodic stripping voltammetry using a reduced graphene oxide-chitosan/ poly-L-lysine nanocomposite modified glassy carbon electrode**
   - *Bối cảnh & Ứng dụng:* Chế tạo điện cực GCE phủ nanocomposite (Graphene oxide khử, Chitosan, Poly-L-lysine) để đo đồng thời Cd, Pb, Cu.
   - *Lý do kế thừa:* Minh chứng sự tương tác tĩnh điện giữa Chitosan (mang điện dương) và vật liệu carbon (mang điện âm), giúp phân tán đồng đều vật liệu và ngăn chặn hiện tượng xếp chồng (restacking) của các lớp carbon aerogel. Hỗ trợ giải thích độ bám dính chắc chắn của Fe/N-CA trên GCE. Đồng thời khẳng định việc sấy khô màng tự nhiên ở nhiệt độ phòng.

3. **Recent progress of electrochemical sensors for accurate detection of heavy metal ions in water: A comprehensive review**
   - *Bối cảnh & Ứng dụng:* Tổng quan về tiến bộ của cảm biến điện hóa phát hiện kim loại nặng trong nước.
   - *Lý do kế thừa:* Cung cấp cơ sở lý thuyết khẳng định động học truyền electron vượt trội của vật liệu carbon và điểm hoạt tính xúc tác (active sites) từ kim loại. Đặc biệt, xác nhận độ nhạy cực kỳ cao của ion Đồng (Cu) trong SWASV (LOD có thể đạt 3.83 nM), là cơ sở để đẩy Cu lên độ ưu tiên cao nhất trong ma trận phân tích.

### 8h. Ma Trận Tín Hiệu & Ưu Tiên Các Kim Loại Phân Tích (SWASV)

Dựa trên cơ chế tương tác và giới hạn phát hiện:
- **Đồng (Cu²⁺): Ưu tiên 1**. Tín hiệu cực nhạy (LOD 3.83 nM), peak sắc nét ở ~ +0.11V. Bắt buộc đo.
- **Chì (Pb²⁺): Ưu tiên 2**. Mục tiêu cốt lõi của đề tài, peak rõ ở ~ -0.50V. Bắt buộc đo.
- **Cadimi (Cd²⁺): Ưu tiên 3**. Mục tiêu cốt lõi, peak tách biệt rõ nét với Pb ở ~ -0.70V. Bắt buộc đo.
- **Kẽm (Zn²⁺): Ưu tiên 4**. Đỉnh doãng rộng ở -1.17V đến -1.24V, tính lặp lại kém do nhiễu thoát khí hydro. Đo bổ sung nếu có thời gian.
- **Niken (Ni²⁺): Bỏ qua**. Không tách đỉnh độc lập, bị chập peak gộp với Kẽm ở thế ~ -0.897V đến -1.059V. Không phù hợp đo bằng cấu hình SWASV hiện tại.

"""

# Insert core_refs right before "### 8g. Đánh giá Repeatability, Reproducibility, Stability" which was originally in the draft, but wait, the update replaced 8a to 8g.
# Let's just append it to the end of the SOP update section.
target = "## Phần 5 — Điều kiện Bảo quản Hóa chất & Điện cực"
if target in text:
    text = text.replace(target, core_refs + "\n" + target)
else:
    # Just append it before TỔNG KẾT: QUALITY GATE
    target2 = "## TỔNG KẾT: QUALITY GATE"
    if target2 in text:
        text = text.replace(target2, core_refs + "\n" + target2)
    else:
        text += core_refs

with open(draft_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Added core references and heavy metal priorities to the draft.")
