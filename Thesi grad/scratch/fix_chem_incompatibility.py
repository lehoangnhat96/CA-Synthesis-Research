import sys

sys.stdout.reconfigure(encoding='utf-8')

draft_path = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md"

with open(draft_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the misleading references in Section 8g with a accurate conceptual distinction
old_refs_text = """### 8g. Cơ Sở Khoa Học và Tài Liệu Kế Thừa Cốt Lõi (GĐ 8)

Các thông số thực nghiệm (Chitosan 2.0%, Cell 30 mL, không nung màng GCE) và ma trận đo SWASV được xây dựng và đối chiếu từ các công bố quốc tế cốt lõi sau:

1. **A screen-printed carbon electrode modified with a chitosan-based film for in situ heavy metal ions measurement**
   - *Bối cảnh & Ứng dụng:* Chế tạo cảm biến đo tại chỗ các kim loại (Zn, Ni, Cu, Pb, Hg, As, Fe) trong nước thải bằng kỹ thuật SWASV.
   - *Lý do kế thừa:* Cung cấp công thức chuẩn pha Chitosan (2.0g trong 100mL acid acetic 0.17M). Bài báo chứng minh cơ chế bẫy ion (chelation) mạnh mẽ của màng Chitosan với các kim loại nặng nhờ mật độ cao nhóm amine (-NH₂) và hydroxyl (-OH), là tiền đề quan trọng để cố định màng Fe/N-CA.

2. **Simultaneous determination of trace Cd(II), Pb(II) and Cu(II) by differential pulse anodic stripping voltammetry using a reduced graphene oxide-chitosan/ poly-L-lysine nanocomposite modified glassy carbon electrode**
   - *Bối cảnh & Ứng dụng:* Chế tạo điện cực GCE phủ nanocomposite (Graphene oxide khử, Chitosan, Poly-L-lysine) để đo đồng thời Cd, Pb, Cu.
   - *Lý do kế thừa:* Minh chứng sự tương tác tĩnh điện giữa Chitosan (mang điện dương) và vật liệu carbon (mang điện âm), giúp phân tán đồng đều vật liệu và ngăn chặn hiện tượng xếp chồng (restacking) của các lớp carbon aerogel. Hỗ trợ giải thích độ bám dính chắc chắn của Fe/N-CA trên GCE. Đồng thời khẳng định việc sấy khô màng tự nhiên ở nhiệt độ phòng.

3. **Recent progress of electrochemical sensors for accurate detection of heavy metal ions in water: A comprehensive review**
   - *Bối cảnh & Ứng dụng:* Tổng quan về tiến bộ của cảm biến điện hóa phát hiện kim loại nặng trong nước.
   - *Lý do kế thừa:* Cung cấp cơ sở lý thuyết khẳng định động học truyền electron vượt trội của vật liệu carbon và điểm hoạt tính xúc tác (active sites) từ kim loại. Đặc biệt, xác nhận độ nhạy cực kỳ cao của ion Đồng (Cu) trong SWASV (LOD có thể đạt 3.83 nM), là cơ sở để đẩy Cu lên độ ưu tiên cao nhất trong ma trận phân tích."""

new_refs_text = """### 8g. Cơ Sở Khoa Học và Tài Liệu Kế Thừa Cốt Lõi (GĐ 8)

Các thông số thực nghiệm (Chitosan 2.0%, Cell 30 mL, không nung màng GCE) và ma trận đo SWASV được xây dựng và đối chiếu từ các công bố điện hóa chuẩn xác sau:

1. **A screen-printed carbon electrode modified with a chitosan-based film for in situ heavy metal ions measurement**
   - *Bối cảnh & Ứng dụng:* Chế tạo cảm biến đo tại chỗ các kim loại (Zn, Ni, Cu, Pb, Hg, As, Fe) trong nước thải bằng kỹ thuật SWASV.
   - *Lý do kế thừa:* Cung cấp công thức chuẩn pha dung dịch Chitosan 2.0% (2.0 g trong 100 mL acid acetic 0.17 M). Bài báo chứng minh cơ chế bẫy ion (chelation) mạnh mẽ của màng Chitosan với các ion kim loại nặng nhờ mật độ cao nhóm amine (-NH₂) và hydroxyl (-OH), là tiền đề quan trọng để phối trộn với bột Fe/N-CA.

2. **Simultaneous determination of trace Cd(II), Pb(II) and Cu(II) by differential pulse anodic stripping voltammetry using a reduced graphene oxide-chitosan/ poly-L-lysine nanocomposite modified glassy carbon electrode**
   - *Bối cảnh & Ứng dụng:* Chế tạo điện cực GCE phủ nanocomposite (Graphene oxide khử, Chitosan, Poly-L-lysine) để đo đồng thời Cd, Pb, Cu.
   - *Lý do kế thừa:* Minh chứng sự tương tác tĩnh điện giữa polyme Chitosan (mang điện dương) và vật liệu carbon (mang điện âm), giúp phân tán đồng đều bột carbon aerogel và ngăn chặn hiện tượng xếp chồng (restacking). Đồng thời khẳng định quy trình sấy màng tự nhiên ở nhiệt độ phòng (không nung nhiệt gốm/không dùng nhiệt cao làm nứt màng polyme).

3. **Recent progress of electrochemical sensors for accurate detection of heavy metal ions in water: A comprehensive review**
   - *Bối cảnh & Ứng dụng:* Tổng quan về tiến bộ của cảm biến điện hóa phát hiện kim loại nặng trong nước.
   - *Lý do kế thừa:* Cung cấp cơ sở lý thuyết khẳng định động học truyền electron vượt trội của vật liệu carbon và điểm hoạt tính xúc tác (active sites) từ kim loại. Đặc biệt, xác nhận độ nhạy cực kỳ cao của ion Đồng (Cu) trong SWASV (LOD có thể đạt 3.83 nM), là cơ sở để đẩy Cu lên độ ưu tiên cao nhất trong ma trận phân tích.

> **[Cảnh báo Nguyên lý Hóa học — Phân biệt Hệ Polyme Sinh học và Hệ Carbon Vô cơ Fe/N-CA]:**
> Tuyệt đối **không khiên cưỡng áp dụng cơ chế liên kết chóa (ester hóa bằng citric acid, ngưng tụ silane APTES hay keo nhiệt dẻo lignin ở 160°C)** từ các bài báo chế tạo aerogel polyme sinh học chưa nung (như các nghiên cứu hydrogel/aerogel nanocellulose-lignin) cho khung vật liệu Fe/N-CA. 
> Quá trình nhiệt phân (> 700°C) đã biến đổi hoàn toàn tiền chất sinh khối thành cấu trúc carbon vô cơ sp² graphit, triệt tiêu hầu hết nhóm aliphatic -OH/-COOH. Độ bền và khả năng chống rửa trôi của màng Fe/N-CA trên điện cực GCE **phụ thuộc 100% vào mạng polyme ngoại lai Composite Binder (Chitosan + Nafion)**, trong đó Nafion đóng vai trò là pha kỵ nước chống rã màng và Chitosan tạo liên kết tĩnh điện/chelate dán chặt bột Fe/N-CA lên bề mặt GCE."""

if old_refs_text in text:
    text = text.replace(old_refs_text, new_refs_text)
    with open(draft_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Corrected references section in draft to fix chemical incompatibility!")
else:
    print("Old refs text not found, updating via regex/substring search...")
    # let's find section 8g and replace it
    idx_8g = text.find("### 8g. Cơ Sở Khoa Học và Tài Liệu Kế Thừa Cốt Lõi (GĐ 8)")
    idx_8h = text.find("### 8h. Ma Trận Tín Hiệu & Ưu Tiên Các Kim Loại Phân Tích (SWASV)")
    if idx_8g != -1 and idx_8h != -1:
        text = text[:idx_8g] + new_refs_text + "\n\n" + text[idx_8h:]
        with open(draft_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print("Updated section 8g via range replacement!")
