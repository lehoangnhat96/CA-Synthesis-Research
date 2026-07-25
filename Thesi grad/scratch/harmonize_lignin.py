import sys

sys.stdout.reconfigure(encoding='utf-8')

draft_path = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md"

with open(draft_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's write a harmonious section 8g that values Lignin's role in Stages 1-4 while explaining Stage 8 binder transition
harmonious_text = """### 8g. Cơ Sở Khoa Học & Phân Tích Vai Trò Lignin (GĐ 1–4 vs. GĐ 8)

Các thông số thực nghiệm (Chitosan 2.0%, Cell 30 mL, không nung màng GCE) và ma trận đo SWASV được xây dựng dựa trên sự kế thừa khoa học và làm rõ hai vai trò khác nhau của Lignin qua các giai đoạn:

1. **Vai trò của Lignin trong Giai đoạn 1–4 (Tạo Gel & Khung Aerogel Sinh khối):**
   - Lignin tự nhiên trong xơ dừa đóng vai trò là "chất keo sinh học" (natural crosslinker). Mật độ cao của các nhóm chức aromatic và hydroxyl (-OH) trong Lignin kết hợp với sợi Nanocellulose giúp mạng hydrogel đạt độ bền cơ học cao, chống rã trong môi trường nước (như minh chứng từ các bài báo trong Notebook CA 22.07 về aerogel Lignocellulose).

2. **Sự Chuyển Hóa của Lignin trong Giai đoạn 5–7 (Nhiệt phân 800°C):**
   - Khi trải qua quá trình nung nhiệt phân ở 800°C dưới dòng khí N₂, Lignin không còn ở dạng polyme dẻo mà bị cacbon hóa hoàn toàn thành **vách carbon graphit sp² giàu vi mao quản (micropores)**. Quá trình này góp phần quyết định tạo nên diện tích bề mặt riêng BET > 300 m²/g của bột Fe/N-CA.

3. **Vai trò của Chitosan/Nafion Binder trong Giai đoạn 8 (Drop-casting trên GCE):**
   - Vì Lignin đã chuyển hóa hoàn toàn thành khung carbon cứng ở GĐ 5, bột Fe/N-CA thu được không thể tự dính vào bề mặt điện cực than kính (GCE). Lúc này, **Composite Binder (Chitosan 2.0% + Nafion 0.5%)** sẽ tiếp quản vai trò "chất dán thế tấp": Chitosan tạo tương tác tĩnh điện/chelate dán chặt bột carbon lên GCE, còn Nafion đóng vai trò là màng kỵ nước bảo vệ màng không bị rã khi làm việc trong cell điện hóa 30 mL."""

idx_8g = text.find("### 8g. Cơ Sở Khoa Học")
idx_8h = text.find("### 8h. Ma Trận Tín Hiệu")

if idx_8g != -1 and idx_8h != -1:
    text = text[:idx_8g] + harmonious_text + "\n\n" + text[idx_8h:]
    with open(draft_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Harmonized Lignin role across stages in draft successfully!")
