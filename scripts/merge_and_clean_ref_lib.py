# -*- coding: utf-8 -*-
"""
Automation script to restructure D:\\1 Master's Ana Chem\\1 Master's thesis\\Carbon Aerogel\\2 Ref lib.
Consolidates scattered knowledge into 4 core handbooks (SOPs), moves legacy files to Archive,
removes absolute duplicates, and cleans up raw intermediate markdown files.
"""

import os
import sys
import shutil
from pathlib import Path

# Set console encoding to UTF-8 on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def make_long_path(path):
    abs_path = os.path.abspath(path)
    if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
        abs_path = abs_path.replace('/', '\\')
        return '\\\\?\\' + abs_path
    return abs_path

# Define paths
base_dir = Path("d:\\1 Master's Ana Chem\\1 Master's thesis\\Carbon Aerogel\\2 Ref lib")
archive_dir = base_dir / "Archive"
org_dir = archive_dir / "Originals"
mgmt_dir = archive_dir / "Management"
lit_dir = archive_dir / "Literature_Reviews"

def create_directories():
    print("Creating Archive directories...")
    for d in [org_dir, mgmt_dir, lit_dir]:
        os.makedirs(make_long_path(d), exist_ok=True)
    print("  -> Archive directories created successfully.")

def delete_redundant_files():
    print("Deleting redundant / absolute duplicate files...")
    # List of files to delete
    files_to_delete = [
        base_dir / "old/R&D_QA/5.1 Chất liên kết.md",
        base_dir / "old/R&D_QA/5.1 Chất liên kết.docx",
        base_dir / "old/R&D_QA/5.2 Chất liên kết.md",
        base_dir / "old/R&D_QA/5.2 Chất liên kết.docx",
        base_dir / "Raw_Markdown/Standardized_Drafts/CA_characterization_biosensor.md"
    ]
    for f in files_to_delete:
        long_f = make_long_path(f)
        if os.path.exists(long_f):
            os.remove(long_f)
            print(f"  -> Deleted: {f.name}")
    print("  -> Deletion of duplicates completed.")

def move_files_to_archive():
    print("Moving files to their respective Archive categories...")
    
    # 1. Move all administrative and planning files to Management
    mgmt_stems = [
        "career growth",
        "Chi phí và tuyển dụng",
        "Chia bài báo để nghiên cứu",
        "Chi phí và hướng đi nghiên cứu"
    ]
    
    # 2. Move review papers to Literature_Reviews
    lit_stems = [
        "Coconut_Aerogels_Environmental_Solutions",
        "Xơ_Dừa_Đến_Siêu_Vật_Liệu"
    ]
    
    # Walk through the directory and classify files
    for root, dirs, files in os.walk(make_long_path(base_dir)):
        # Skip directories already inside Archive
        if "Archive" in root:
            continue
            
        norm_root = Path(root[4:] if root.startswith('\\\\?\\') else root)
        
        for file in files:
            file_path = norm_root / file
            stem = file_path.stem
            ext = file_path.suffix.lower()
            
            # Check if it should go to Management
            is_mgmt = False
            for ms in mgmt_stems:
                if stem.lower() == ms.lower() or stem.lower().startswith(ms.lower() + "_"):
                    is_mgmt = True
                    break
            
            # Check if it should go to Literature Reviews
            is_lit = False
            for ls in lit_stems:
                if stem.lower() == ls.lower() or stem.lower().startswith(ls.lower() + "_"):
                    is_lit = True
                    break
                    
            if is_mgmt:
                dest = mgmt_dir / file
                print(f"  -> Moving to Management: {file_path.name}")
                shutil.move(make_long_path(file_path), make_long_path(dest))
            elif is_lit:
                dest = lit_dir / file
                print(f"  -> Moving to Literature Reviews: {file_path.name}")
                shutil.move(make_long_path(file_path), make_long_path(dest))
            elif ext in [".docx", ".pdf", ".png"]:
                # Move other original documents to Originals
                dest = org_dir / file
                # If destination already exists, generate a unique name
                counter = 1
                while os.path.exists(make_long_path(dest)):
                    dest = org_dir / f"{file_path.stem}_{counter}{file_path.suffix}"
                    counter += 1
                print(f"  -> Moving Original: {file_path.name} -> Archive/Originals/")
                shutil.move(make_long_path(file_path), make_long_path(dest))

def write_core_handbooks():
    print("Writing 4 Core Standardized Handbooks (SOPs)...")
    
    # Handbook 1: coconut_coir_carbon_aerogel_synthesis_sop.md
    h1_content = """# CẨM NĂNG 1: QUY TRÌNH TIÊU CHUẨN TỔNG HỢP CARBON AEROGEL TỪ XƠ DỪA (COCONUT COIR CARBON AEROGEL SYNTHESIS SOP)

Cẩm nang này hướng dẫn chi tiết quy trình thực nghiệm chuẩn hóa gồm 5 giai đoạn chính để chế tạo thành công Carbon Aerogel (CA) từ nguồn sinh khối xơ dừa tự nhiên, tích hợp và tối ưu hóa các thông số kỹ thuật cốt lõi.

---

## 1. BẢNG TỔNG HỢP QUY TRÌNH 5 GIAI ĐOẠN

| Giai đoạn | Các phương án thực nghiệm | Điều kiện - Thông số tối ưu | Hiệu suất & Chỉ tiêu đạt được | Cảnh báo & Rủi ro (⚠️ Risk) |
| :--- | :--- | :--- | :--- | :--- |
| **#0 – Tiền xử lý**<br>*(Xơ dừa $\rightarrow$ Cellulose)* | 1. NaOH kiềm hóa<br>2. **NaOH + H₂O₂ (Khuyến nghị)** ⭐<br>3. NaClO₂ tẩy trắng | • Xử lý kiềm: NaOH 1.5M, 80°C, 2 lần.<br>• Tẩy trắng: H₂O₂ 10%, 80°C, 2 lần × 2h. | • Hiệu suất: 40–50% so với xơ thô.<br>• Hàm lượng Lignin còn lại: <5%.<br>• Hàm lượng Cellulose: 70–80%. | ⚠️ NaClO₂ tạo khí clo độc hại và dioxin gây ô nhiễm, tránh sử dụng quy mô lớn.<br>⚠️ Không loại bỏ 100% lignin vì lignin là nguồn carbon cố định cao giúp giữ khung aerogel. |
| **#1 – Sol-Gel & Doping**<br>*(Cellulose $\rightarrow$ Hydrogel)* | 1. Control (không doping)<br>2. N-doping (Urea)<br>3. **Ni/Co co-doping (Khuyến nghị)** ⭐<br>4. N,S,Ni/Co ternary | • Hệ dung môi: 5 mL nước : 4 g Urê : 11 mL $NH_4OH$ 25% ở -12°C.<br>• Tỷ lệ kim loại: $NiCl_2:CoCl_2$ = 1:2 (mol).<br>• Chất tạo liên kết: TEPA 1.5 - 3.0g. | • Độ phân tán kim loại: Cấp độ phân tử nhờ phức chelate TEPA.<br>• Trực quan: Gel đông tụ hoàn toàn, màu xanh đậm đặc trưng. | ⚠️ Muối Sắt (Fe) dễ kết tủa thành $Fe(OH)_3$ trong môi trường kiềm cực mạnh của NaOH trước khi kịp tạo phức. Cần kiểm soát chặt pH hoặc dùng $Ni/Co$ tạo phức bền hơn. |
| **#2 – Freeze-Drying**<br>*(Hydrogel $\rightarrow$ Aerogel)* | 1. **Sấy đông khô (FD)** ⭐<br>2. Sấy siêu tới hạn ($SCD-CO_2$)<br>3. Sấy áp suất thường (APD) | • Trao đổi dung môi: Nước $\rightarrow$ Ethanol $\rightarrow$ n-Hexane (hoặc t-butanol).<br>• Làm đông: Đông sâu ở −80°C.<br>• Thăng hoa: Áp suất <20 Pa, −40°C, 24–48h. | • Giữ nguyên cấu trúc 3D không co ngót.<br>• Tỷ lệ Mesopore: 50–60%.<br>• Diện tích bề mặt riêng (SSA): 1500–2500 m²/g (sau hoạt hóa). | ⚠️ Không sấy chân không nóng trực tiếp vì sức căng bề mặt của nước bay hơi sẽ làm sập hoàn toàn cấu trúc lỗ xốp (pore collapse). |
| **#3 – Hoạt hóa (Optional)**<br>*(Aerogel $\rightarrow$ Activated CA)* | 1. KOH:CA = 0.5:1<br>2. KOH:CA = 1:1<br>3. **Bỏ qua (Khuyến nghị cho Ni/Co)** ⭐ | • Tỷ lệ hoạt hóa nhẹ: KOH:CA = 0.5:1.<br>• Nung hoạt hóa: 750°C trong 60 phút.<br>• Rửa axit: Rửa bằng HCl loãng để loại bỏ tro và kali dư. | • Tăng SSA thêm +300–500 m²/g.<br>• Tăng tỷ lệ vi lỗ (micropore) tích điện tích. | ⚠️ Hoạt hóa KOH quá mạnh (tỷ lệ 1:1) ở nhiệt độ cao sẽ khử và ăn mòn hạt nano kim loại hoạt tính $Ni/Co$, làm giảm 10–20% độ nhạy cảm biến. |
| **#4 – Carbon hóa**<br>*(Aerogel $\rightarrow$ Carbon Aerogel)* | 1. Carbon hóa ở 500°C<br>2. **550–600°C (Khuyến nghị)** ⭐<br>3. Nung ở 700°C<br>4. Nung ở 800–900°C | • Tốc độ gia nhiệt: 5°C/phút.<br>• Nhiệt độ giữ: 550°C - 600°C trong 2 giờ.<br>• Khí quyển bảo vệ: Khí trơ $N_2$ hoặc Argon tinh khiết. | • Hàm lượng Nitơ giữ lại: 4–6 wt.%.<br>• Cấu hình hoạt tính: Ưu tiên vòng Pyrrolic-N và Pyridinic-N.<br>• Độ dẫn điện: 20–50 S/cm. | ⚠️ Nung >800°C làm bay hơi hết Nitơ hoạt tính (<1 wt.%) và gây sập các lỗ xốp nhỏ, làm giảm mạnh độ nhạy cảm biến sinh học dù độ dẫn điện tăng. |

---

## 2. QUY TRÌNH THỰC NGHIỆM CHI TIẾT TỪNG BƯỚC

### Bước 0: Tiền xử lý sinh khối xơ dừa
1.  **Rửa sạch & Nghiền nhỏ:** Xơ dừa thô được rửa bằng nước DI nhiều lần để loại bỏ bụi bẩn, phơi khô ở 80°C trong 24 giờ, sau đó nghiền thành bột mịn và rây qua cỡ hạt 100 mesh.
2.  **Kiềm hóa loại bỏ bán cellulose (Hemicellulose) và Lignin:**
    *   Trộn bột xơ dừa với dung dịch NaOH 1.5 M theo tỷ lệ lỏng/rắn là 20:1.
    *   Khuấy đều và gia nhiệt ở 80°C trong 2 giờ. Lọc lấy phần bã rắn.
    *   Lặp lại quy trình kiềm hóa lần thứ 2 để hòa tan tối đa hemicellulose. Rửa sạch bã bằng nước DI đến pH trung tính.
3.  **Tẩy trắng chọn lọc (Bleaching & Delignification):**
    *   Hòa tan bã rắn vào dung dịch chứa $NaOH$ 1.5 M và $H_2O_2$ 10% (tỷ lệ 1:1).
    *   Gia nhiệt ở 80°C trong 2 giờ dưới sự khuấy trộn nhẹ liên tục. Phản ứng này oxy hóa mạnh và hòa tan lignin mạch ngắn.
    *   Lọc, rửa sạch bằng nước DI nhiều lần và sấy khô ở 60°C. Ta thu được bột cellulose tinh chế màu trắng ngà (hàm lượng cellulose >75%, lignin <5%).

### Bước 1: Hòa tan và Tạo Gel Lưỡng Kim (Sol-Gel & Ni/Co Co-Doping)
1.  **Hòa tan Cellulose trong Hệ dung môi NaOH/Urea lạnh:**
    *   Chuẩn bị hệ dung môi gồm: $NaOH$ 7 wt.%, Urea 12 wt.% và nước DI.
    *   Làm lạnh hệ dung môi này xuống nhiệt độ cực lạnh **-12°C** (sử dụng bể đá muối hoặc tủ đông sâu).
    *   Thêm bột cellulose tinh chế (tỷ lệ 3-5 wt.%) vào hệ dung môi lạnh, khuấy cơ học tốc độ cao trong 30 phút. Nhiệt độ cực lạnh giúp NaOH phá vỡ các liên kết hydro của cellulose, tạo ra dung dịch sol trong suốt và đồng nhất.
2.  **Phối trộn chất tạo liên kết và kim loại chuyển tiếp:**
    *   Hòa tan muối $NiCl_2.6H_2O$ và $CoCl_2.6H_2O$ theo tỷ lệ mol **1:2** vào dung dịch sol (tổng hàm lượng kim loại mục tiêu chiếm 25 wt.% khối lượng cellulose).
    *   Thêm chất liên kết ngang **TEPA** (Tetraethylenepentamine) với hàm lượng 2.5g. Khuấy đều trong 15 phút. Nhóm amine dồi dào trên TEPA sẽ lập tức phối trí mạnh mẽ với các cation $Ni^{2+}$ và $Co^{2+}$ tạo thành phức chelate tan đồng nhất, ngăn chặn tuyệt đối sự kết tủa vô định hình của kim loại.
3.  **Hóa Gel (Gelation):**
    *   Đổ dung dịch hỗn hợp vào các khuôn teflon định hình.
    *   Đặt khuôn vào tủ sấy ở **60°C** trong 12 giờ. Nhiệt độ kích hoạt sự liên kết ngang của các chuỗi cellulose với sự hỗ trợ của TEPA, chuyển dịch hệ sol thành hydrogel rắn dẻo dai màu xanh thẫm.

### Bước 2: Đông Khô Bảo Tồn Cấu Trúc (Freeze-Drying Protocol)
1.  **Trao đổi dung môi loại bỏ muối và kiềm dư:**
    *   Ngâm hydrogel trong hỗn hợp Nước:Ethanol (tỷ lệ 1:1) trong 12 giờ.
    *   Chuyển sang ngâm trong Ethanol nguyên chất (99.5%) 2 lần, mỗi lần 12 giờ để loại bỏ hoàn toàn phân tử nước bên trong mạng lưới gel (tránh sự co rút do lực mao dẫn của nước khi sấy).
    *   (Tùy chọn) Trao đổi dung môi cuối cùng sang n-Hexane hoặc tert-butanol để hạ thấp tối đa nhiệt độ đông kết và sức căng bề mặt.
2.  **Đông sâu định hướng (Ice-Templating/Freeze-Casting):**
    *   Đặt các khối gel đã trao đổi dung môi vào khay kim loại tiếp xúc trực tiếp với tấm lạnh của thiết bị hạ nhiệt.
    *   Hạ nhiệt độ chậm với tốc độ **-7.5 K/phút** xuống mức **-80°C** để định hướng sự phát triển của các tinh thể đá rỗng theo chiều dọc.
3.  **Sấy thăng hoa:**
    *   Chuyển nhanh mẫu đã đông cứng vào buồng sấy đông khô.
    *   Thiết lập áp suất chân không cực thấp **<20 Pa** và nhiệt độ thăng hoa **-40°C**. Duy trì liên tục trong 36 giờ để toàn bộ tinh thể đá thăng hoa trực tiếp từ thể rắn sang thể khí, tạo ra sản phẩm Aerogel siêu xốp và nhẹ.

### Bước 3: Carbon hóa cấu trúc xốp và Định hình tâm hoạt động
1.  **Thiết lập thiết bị nung:** Đặt các mẫu Aerogel vào đĩa sứ, đưa vào lò nung ống carbolite.
2.  **Khử khí và bảo vệ:** Sục dòng khí trơ $N_2$ tinh khiết (tốc độ lưu lượng 100 mL/phút) trong 30 phút trước khi gia nhiệt để đuổi sạch oxy trong lò.
3.  **Nung Carbon hóa tối ưu:**
    *   Gia nhiệt từ nhiệt độ phòng lên **600°C** với tốc độ gia nhiệt chậm **5°C/phút** để tránh làm rạn nứt khung aerogel do sự thoát khí đột ngột của chất bay hơi.
    *   Duy trì nhiệt độ ổn định ở **600°C** trong **2 giờ** dưới dòng khí trơ liên tục.
    *   *Ý nghĩa khoa học:* Đây là nhiệt độ "vàng" (sweet spot) giúp carbon hóa hoàn toàn khung hữu cơ nhưng vẫn giữ lại tỷ lệ Nitơ hoạt tính tối ưu (4-6 wt.%), đồng thời nhiệt phân phức kim loại-TEPA thành các hạt nano lưỡng kim $Ni/Co$ phân tán cực mịn trên mạng lưới carbon xốp.
4.  **Làm nguội:** Tắt nguồn gia nhiệt, để lò nguội tự nhiên dưới dòng khí trơ bảo vệ cho đến khi nhiệt độ lò giảm xuống <80°C mới tiến hành mở lò lấy sản phẩm Carbon Aerogel.
"""

    # Handbook 2: pore_engineering_and_doping_handbook.md
    h2_content = """# CẨM NĂNG 2: LÝ THUYẾT DOPING, HOẠT HÓA & THIẾT KẾ LỖ XỐP (PORE ENGINEERING & DOPING HANDBOOK)

Cẩm nang này cung cấp cơ sở lý thuyết hóa học phân tích, cơ chế phản ứng và các lập luận khoa học cốt lõi để bảo vệ luận văn liên quan đến việc biến tính pha tạp dị nguyên tử ($N, S$), pha tạp lưỡng kim ($Ni/Co$) và kỹ thuật kiểm soát lỗ xốp trên nền Carbon Aerogel (CA) từ xơ dừa.

---

## 1. CƠ CHẾ PHA TẠP DỊ NGUYÊN TỬ (HETEROATOM DOPING CHEMISTRY)

Việc đưa các nguyên tử phi kim có độ âm điện khác biệt như Nitơ ($N$, độ âm điện 3.04) và Lưu huỳnh ($S$, độ âm điện 2.58) thay thế cho các nguyên tử Carbon ($C$, độ âm điện 2.55) trong mạng lưới graphene là chiến lược then chốt để chuyển đổi cấu trúc điện tử của khung carbon trơ thành các vị trí hoạt động xúc tác mạnh mẽ.

```
       Graphitic-N (Tăng dẫn điện)
             \ 
              C — C — C — C
             /     \     / \
            C — C — N — C   C
           /     \     /     \
          C — C — C — C — N — H  Pyrrolic-N (Điện dung giả)
               /       \
              N          S — Doping Lưu huỳnh (Lệch mật độ spin)
            /   \
           C     C
           \     /
              C  <--- Pyridinic-N (Lewis Base - Tâm hoạt động chính cho ORR & Glucose oxidation)
```

### Các dạng cấu hình Nitơ trong mạng lưới carbon:
1.  **Pyridinic-N (N-6):**
    *   *Bản chất:* Nguyên tử Nitơ nằm ở mép của các lớp graphene rỗng, liên kết phối trí với 2 nguyên tử Carbon lân cận và đóng góp 1 electron vào hệ liên hợp $\pi$.
    *   *Vai trò trong Cảm biến:* Pyridinic-N sở hữu cặp electron tự do (Lewis base) không tham gia liên hợp, tạo ra một vùng có mật độ điện tích âm cao phân cực mạnh. Đây chính là **tâm hoạt động xúc tác (catalytic active sites)** tối ưu nhất để hấp phụ phân tử glucose và các tác nhân oxy hóa khử trong dung dịch. Nó giúp đẩy nhanh tốc độ truyền electron và giảm thế phân cực quá mức của cảm biến.
2.  **Pyrrolic-N (N-5):**
    *   *Bản chất:* Nguyên tử Nitơ đóng góp 2 electron vào hệ $\pi$ liên hợp và nằm trong vòng dị vòng 5 cạnh (tương tự vòng pyrrole).
    *   *Vai trò:* Tham gia mạnh vào các phản ứng oxy hóa khử Faradaic thuận nghịch trên bề mặt (tạo điện dung giả - Pseudocapacitance), cực kỳ có lợi cho các ứng dụng siêu tụ điện.
3.  **Graphitic-N (Quaternary-N):**
    *   *Bản chất:* Nguyên tử Nitơ thay thế trực tiếp nguyên tử Carbon bên trong các lá graphene planar.
    *   *Vai trò:* Do có nhiều hơn C một electron hóa trị, nó hiến electron vào dải dẫn, làm tăng vọt mật độ hạt mang điện và nâng cao **độ dẫn điện** tổng thể của vật liệu điện cực.

---

## 2. HIỆU ỨNG HIỆP ĐỒNG LƯỠNG KIM Ni/Co & VAI TRÒ CỦA TEPA

Khi bị Hội đồng chấm Luận văn chất vấn: *"Tại sao em chọn hệ lưỡng kim Ni/Co và sử dụng phụ gia TEPA trong quá trình sol-gel?"*, hãy sử dụng các lập luận đanh thép sau:

### A. Sự bù trừ hoàn hảo giữa Ni và Co (Synergistic Effect)
*   **Nikken (Ni):** Sở hữu khả năng lưu trữ năng lượng và hoạt tính oxy hóa khử cực cao nhờ các phản ứng chuyển đổi hóa trị thuận nghịch ($Ni^{2+} \leftrightarrow Ni^{3+}$). Tuy nhiên, nhược điểm chí tử của các hợp chất niken là độ dẫn điện tự nhiên cực kỳ kém (bản chất là chất bán dẫn hoặc cách điện).
*   **Coban (Co):** Có độ dẫn điện vượt trội hơn rất nhiều và tốc độ phản ứng điện hóa nhanh (Kinetics cao), giúp hệ thống sạc xả ở mật độ dòng lớn không bị nghẽn electron. Tuy nhiên, dung lượng riêng và độ bền hóa học của Co đơn độc lại thấp hơn Ni và chi phí đắt đỏ.
*   **Hệ lưỡng kim Ni-Co:** Sự kết hợp đồng thời tạo ra cấu trúc spinel hỗn hợp ($NiCo_2O_4$ hoặc $Ni_xCo_{1-x}$ alloy). Trong cấu trúc này, các cation Ni và Co phân bố xen kẽ trong các hốc bát diện và tứ diện của mạng tinh thể, tạo ra đường truyền electron và ion thông suốt, đồng thời tăng cường độ ổn định cấu trúc. Hiệu suất thu được lớn hơn nhiều so với tổng hiệu suất của hai kim loại đơn lẻ cộng lại.

### B. Vai trò "Neo giữ" phân tử của TEPA (Chelation Chemistry)
*   Trong các quy trình tổng hợp thông thường, khi đưa các muối kim loại $Ni^{2+}$ và $Co^{2+}$ vào dung dịch sol của cellulose xơ dừa, dưới tác động của môi trường kiềm (NaOH), các cation này lập tức phản ứng tạo thành kết tủa hydroxide vô định hình cỡ lớn ($Ni(OH)_2, Co(OH)_2$). Các hạt kết tủa này sẽ bị vón cục (aggregation), làm giảm nghiêm trọng diện tích tiếp xúc hoạt tính và làm sụp đổ lỗ xốp của aerogel.
*   **Giải pháp TEPA:** TEPA (Tetraethylenepentamine) là một amine đa chức dồi dào nhóm $-NH_2$ và $-NH-$. Amine hoạt động như một phối tử đa răng (multidentate ligand) cực kỳ mạnh mẽ. Nó tạo phức chelate vòng càng năm cạnh siêu bền với $Ni^{2+}$ và $Co^{2+}$ ở cấp độ phân tử. Phức chất này tan hoàn toàn và phân tán đều đặn dọc theo các mạch polymer của cellulose. Khi nung nhiệt phân, phức chất bị phân hủy đều đặn tại chỗ, tạo ra các hạt nano hợp kim $NiCo$ phân tán cực mịn (kích thước <10 nm) bám chặt trên vách carbon aerogel mà không bị vón cục.

---

## 3. KỸ THUẬT THIẾT KẾ LỖ XỐP PHÂN CẤP (HIERARCHICAL POROSITY DESIGN)

Một vật liệu điện cực hoàn hảo không chỉ cần diện tích bề mặt lớn (vi lỗ) mà cần một kiến trúc không gian thông minh để ion dung dịch có thể tiếp cận nhanh chóng:

```
        Dung dịch điện ly
               │
               ▼
      [ LỖ XỐP LỚN - Macropores (>50nm) ]  <--- Bể chứa ion (Electrolyte Reservoir)
               │
               ▼  (Khuếch tán cực nhanh)
      [ LỖ XỐP TRUNG BÌNH - Mesopores (2-50nm) ] <--- "Đường cao tốc" (Ion Highways)
               │
               ▼  (Hấp phụ tạo dòng điện)
      [ VI LỖ XỐP - Micropores (<2nm) ]    <--- "Bãi đỗ xe" lưu trữ điện lượng cực lớn
```

1.  **Cơ chế đúc băng (Ice-Templating):**
    *   Khi đông lạnh dung dịch cellulose xơ dừa ở -80°C, các tinh thể đá rỗng phát triển theo định hướng trục nhiệt độ, đẩy các chuỗi cellulose dồn lại sát nhau.
    *   Khi sấy thăng hoa, các tinh thể băng biến mất để lại hệ thống **lỗ xốp lớn (macropores)** thẳng tắp, liên thông nhau. Hệ lỗ này đóng vai trò như các "bể chứa" (electrolyte reservoirs) chứa sẵn dung dịch điện ly trong lòng điện cực.
2.  **Cơ chế sinh khí hoạt hóa (Gas Evolution):**
    *   Sự nhiệt phân cellulose và lignin xơ dừa (chứa nhiều nhóm oxy) giải phóng các dòng khí $CO, CO_2, H_2$ tự nhiên ở nhiệt độ cao. Dòng khí này thổi mạnh vào vách ngăn polymer đang bị carbon hóa, tạo thêm các **lỗ xốp trung bình (mesopores)** hoạt động như những "đường cao tốc" giúp các ion khuếch tán không gặp trở lực vật lý.
3.  **Khả năng đệm giãn nở thể tích (Buffering Swelling/Expansion):**
    *   Trong các phản ứng điện hóa, sự xâm nhập và thoát ra liên tục của các ion ngậm nước kích thước lớn thường tạo ra ứng suất cơ học khổng lồ lên mạng lưới carbon, gây ra sự nứt vỡ, bong tróc lớp phủ điện cực (pore collapse/delamination).
    *   Cấu trúc rỗng xốp đa cấp độ hoạt động như một hệ thống lò xo giảm chấn cơ học, tự do co giãn thể tích để hấp thụ toàn bộ lực căng cơ học đó, giúp điện cực đạt độ bền chu kỳ cực cao (>95% dung lượng sau 5000 chu kỳ).
"""

    # Handbook 3: electrode_fabrication_and_electrochemistry_sop.md
    h3_content = """# CẨM NĂNG 3: KỸ THUẬT CHẾ TẠO ĐIỆN CỰC & ĐO ĐẠC ĐIỆN HÓA (ELECTRODE FABRICATION & ELECTROCHEMISTRY SOP)

Cẩm nang này hướng dẫn chi tiết các thao tác chuẩn trong phòng thí nghiệm để chế tạo màng điện cực làm việc từ Carbon Aerogel xơ dừa, đồng thời thiết lập hệ đo điện hóa phân tích độ nhạy cao cho cảm biến glucose phi enzym và tụ điện hóa.

---

## 1. CÔNG THỨC VÀNG PHA CHẾ MỰC ĐIỆN CỰC (INK FORMULATION STRATEGY)

Pha chế mực là khâu quyết định sự phân tán đều đặn của vật liệu hoạt tính trên bề mặt điện cực và kiểm soát nội trở dòng.

### Bảng thông số pha chế tiêu chuẩn:

| Thành phần | Thông số Kỹ thuật (Specs) | Ý nghĩa chiến lược & Cảnh báo (Rationale & ⚠️ Risk) |
| :--- | :--- | :--- |
| **Vật liệu chính** | NiCo/N-doped Carbon Aerogel<br>*(Đã nghiền siêu mịn)* | Nghiền bằng cối mã não $\rightarrow$ hạt kích thước sub-micron giúp màng sau khi phủ phẳng mịn tối đa, tăng diện tích tiếp xúc hiệu dụng và giảm dòng nền nhiễu (background noise). |
| **Chất kết dính (Binder)** | Nafion 5% solution<br>*(Tỷ lệ rắn tối ưu: 2 - 5 wt.%)* | • **Tại sao chọn Nafion:** Nafion vừa làm keo dính siêu bền, vừa dẫn cation tốt ($Na^+, K^+$), đồng thời là màng ngăn loại trừ điện tích âm giúp ngăn chặn các chất gây nhiễu phổ biến như Axit Ascorbic (AA) và Axit Uric (UA).<br>• ⚠️ **Rủi ro:** Tuyệt đối không dùng Nafion >10 wt.%. Hàm lượng keo quá cao sẽ tạo ra lớp màng polymer cách điện bọc kín toàn bộ hạt hoạt tính, ngăn cản sự tiếp xúc giữa glucose và tâm xúc tác NiCo, làm tăng nội trở và gây "chết" độ nhạy của cảm biến. |
| **Dung môi (Solvent)** | Hỗn hợp Ethanol : Nước DI<br>*(Tỷ lệ thể tích 1:1)* | Tạo độ nhớt vừa phải giúp mực dễ lan đều trên bề mặt nhỏ hẹp của điện cực carbon thủy tinh (GCE), tốc độ bay hơi vừa phải ở nhiệt độ phòng. |
| **Nồng độ mực** | 2.0 - 5.0 mg/mL | Nồng độ chuẩn để đảm bảo việc định lượng khối lượng phủ (mass loading) chính xác bằng micropipette. |
| **Phân tán siêu âm** | Bể siêu âm (Ultrasonication)<br>Thời gian: >30 phút trong bể đá lạnh. | • Bắt buộc phải đặt cốc mực trong chậu đá lạnh trong quá trình siêu âm.<br>• ⚠️ **Lý do:** Quá trình siêu âm sinh nhiệt lớn có thể làm bay hơi dung môi ethanol làm thay đổi nồng độ mực, hoặc gây đông tụ/hỏng cấu trúc chuỗi của polymer Nafion. |

---

## 2. QUY TRÌNH PHỦ MÀNG LÊN ĐIỆN CỰC CARBON THỦY TINH (DROP-CASTING PROTOCOL)

*Mục tiêu: Chế tạo lớp màng mỏng, đồng nhất, bám dính siêu bền, không bị rạn nứt hay nổ bọt trên bề mặt điện cực làm việc GCE.*

### Các bước thực hiện:
1.  **Đánh bóng bề mặt GCE (WE):**
    *   Nhỏ vài giọt huyền phù Alumina bột mịn ($Al_2O_3$ cỡ hạt 0.05 $\mu$m) lên tấm nỉ đánh bóng chuyên dụng.
    *   Đặt thẳng đứng điện cực GCE và chà nhẹ theo hình số 8 liên tục trong 5-10 phút để loại bỏ hoàn toàn các tạp chất hữu cơ hoặc lớp màng oxit cũ bám trên mặt điện cực.
    *   Rửa sạch bằng nước DI và siêu âm trong nước DI khoảng 2 phút để loại bỏ các hạt alumina bám dính.
2.  **Kiểm tra chất lượng đánh bóng (Quality Control Gate):**
    *   Đo đường quét thế tuần hoàn (CV) của GCE trong dung dịch phân tích chuẩn $5 mM K_3[Fe(CN)_6] + 0.1 M KCl$.
    *   ✓ **Tiêu chuẩn đạt:** Khoảng cách giữa thế đỉnh oxy hóa và thế đỉnh khử ($\Delta E_p$) phải **nhỏ hơn 100 mV** (tốt nhất là <80 mV). Nếu $\Delta E_p > 100 mV$, chứng tỏ bề mặt cực còn bẩn hoặc rạn nứt, bắt buộc phải tiến hành đánh bóng lại.
3.  **Phủ mực điện cực (Drop-casting):**
    *   Hút chính xác **5 - 10 $\mu$L** mực điện cực đã siêu âm phân tán đều bằng Micropipette.
    *   Đặt đầu tip micropipette sát tâm mặt điện cực GCE (không chạm trực tiếp vào bề mặt), từ từ bơm mực ra để tạo thành một giọt lồi tròn cân đối bao phủ toàn bộ mặt GCE ($\phi$ = 3mm).
4.  **Làm khô màng:**
    *   Đặt điện cực nằm ngang dưới một cốc thủy tinh úp ngược để làm khô chậm tự nhiên ở nhiệt độ phòng, hoặc sấy nhẹ dưới đèn hồng ngoại (IR Lamp) ở nhiệt độ ấm nhẹ 40°C.
    *   *Tránh hiệu ứng Coffee-Ring:* Không sấy ở nhiệt độ quá cao vì dung môi bay hơi quá nhanh sẽ đẩy toàn bộ hạt vật liệu dồn ra mép ngoài của vòng tròn điện cực, tạo ra màng không đồng đều (rỗng ở tâm và dày ở viền mép).
    *   ⚠️ **Tuyệt đối không sấy trong tủ sấy chân không (Vacuum drying):** Áp suất thấp sẽ làm dung môi sôi lên tạo thành các bong bóng khí nổ vỡ trên màng điện cực, phá hủy hoàn toàn độ bám dính.

---

## 3. THIẾT LẬP HỆ ĐO ĐIỆN HÓA TIÊU CHUẨN (ELECTROCHEMICAL SETUP)

### Cấu hình hệ đo 3 điện cực:
*   **Điện cực làm việc (WE):** Điện cực GCE đã phủ Carbon Aerogel xơ dừa.
*   **Điện cực đối (CE):** Dây Platinum (Pt) dạng vòng hoặc thanh carbon graphite có độ tinh khiết cao. Diện tích bề mặt của CE phải lớn hơn ít nhất 10 lần WE để đảm bảo dòng điện phản ứng không bị giới hạn bởi điện cực đối.
*   **Điện cực so sánh (RE):** Điện cực $Ag/AgCl$ trong dung dịch $KCl$ bão hòa hoặc $3M KCl$. Đặt đầu RE càng gần WE càng tốt để giảm thiểu tối đa sai số sụt thế Ohm ($iR$ drop) trong dung dịch.

```
                  ┌──────────────────────┐
                  │    MÁY ĐO ĐIỆN HÓA   │
                  │   (Potentiostat)     │
                  └──────┬────┬────┬─────┘
                         │    │    │
            ┌────────────┘    │    └────────────┐
            ▼                 ▼                 ▼
     [So sánh - RE]    [Làm việc - WE]    [Cực đối - CE]
      (Ag/AgCl)           (GCE + CA)         (Dây Pt)
            │                 │                 │
            └─────────┐       │       ┌─────────┘
                      ▼       ▼       ▼
                     ┌─────────────────┐
                     │ Dung dịch kiềm  │
                     │  (0.1M NaOH)    │
                     └─────────────────┘
```

---

## 4. BẢN CHẤT HỆ ĐIỆN LY: SỰ KHÁC BIỆT CỐT LÕI GIỮA ĐO SIÊU TỤ & CẢM BIẾN

Việc lựa chọn chất điện ly có vai trò sống còn đối với hiệu suất hoạt động của vật liệu Carbon Aerogel lưỡng kim NiCo:

### A. Đối với Cảm biến Glucose phi enzym (Non-Enzymatic Glucose Sensor)
*   **Chất điện ly bắt buộc:** Dung dịch **$NaOH$ 0.1 M hoặc $KOH$ 0.1 M (pH $\approx$ 13)**.
*   **Cơ chế hoạt động:** Phản ứng oxy hóa glucose không thể xảy ra trực tiếp trên bề mặt carbon trơ mà cần sự kích hoạt của các cặp oxy hóa khử kim loại ($Ni^{2+}/Ni^{3+}$ và $Co^{2+}/Co^{3+}$). Trong môi trường kiềm cực mạnh, các hạt nano hợp kim trên vách CA biến đổi thành dạng oxy-hydroxide hoạt tính cao:
    $$NiCo_{alloy} + OH^- \rightarrow NiOOH + CoOOH + H_2O + e^-$$
    Chính dạng oxy-hydroxide hóa trị cao này ($NiOOH$) hấp phụ và oxy hóa trực tiếp phân tử glucose thành glucolactone:
    $$NiOOH + Glucose \rightarrow Ni(OH)_2 + Glucolactone$$
*   ⚠️ **Lưu ý quan trọng:** Tuyệt đối không dùng dung dịch đệm sinh lý PBS (pH 7.4) để đo cảm biến glucose phi enzym sử dụng hệ xúc tác kim loại chuyển tiếp này. Ở pH trung tính, cặp redox hoạt tính $NiOOH$ không thể hình thành, cảm biến sẽ hoàn toàn **không có tín hiệu dòng** hoặc tín hiệu cực thấp.

### B. Đối với ứng dụng Siêu tụ điện (Supercapacitor)
*   **Chất điện ly ưu tiên:** Dung dịch **$KOH$ 6.0 M**.
*   **Lý do:** Siêu tụ điện cần tối đa hóa mật độ năng lượng và công suất. Dung dịch $KOH$ 6M có độ dẫn điện ion cao nhất trong tất cả các chất điện ly lỏng dùng cho tụ điện hóa, giúp giảm tối đa điện trở nối tiếp tương đương (ESR). Đồng thời, kích thước ion hydrat hóa của $K^+$ nhỏ giúp khuếch tán cực nhanh vào các vi lỗ xốp của carbon aerogel, tận dụng tối đa điện dung lớp kép điện (EDLC) cùng với điện dung giả (pseudocapacitance) của cấu hình Pyrrolic-N và các tâm kim loại $NiCo$ trong môi trường kiềm.
"""

    # Handbook 4: material_characterization_and_instrumentation_guide.md
    h4_content = """# CẨM NĂNG 4: ĐẶC TRƯNG VẬT LIỆU & HƯỚNG DẪN VẬN HÀNH THIẾT BỊ (MATERIAL CHARACTERIZATION & INSTRUMENTATION GUIDE)

Cẩm nang này tổng hợp các kỹ thuật đo đạc vật lý, hóa học bề mặt và hướng dẫn vận hành chi tiết các thiết bị phân tích hiện đại dùng để đánh giá chất lượng sản phẩm Carbon Aerogel xơ dừa.

---

## 1. CÁC PHƯƠNG PHÁP ĐẶC TRƯNG VẬT LIỆU CỐT LÕI (KEY CHARACTERIZATION METHODS)

### A. Kính hiển vi điện tử quét (SEM) & Kính hiển vi điện tử truyền qua (TEM)
*   **SEM (Scanning Electron Microscopy):**
    *   *Mục tiêu:* Đánh giá hình thái cấu trúc vĩ mô 3D.
    *   *Đặc trưng CA xơ dừa:* SEM sẽ chỉ ra cấu trúc tổ ong (honeycomb-like structure) với các vách ngăn mỏng dẻo dai từ cellulose đan xen liên tục, minh chứng cho việc sấy thăng hoa thành công không làm sập khung gel.
*   **TEM (Transmission Electron Microscopy):**
    *   *Mục tiêu:* Quan sát cấu trúc siêu mịn ở cấp độ nano.
    *   *Đặc trưng:* TEM/HRTEM sẽ chỉ ra sự phân bố của các hạt nano hợp kim $NiCo$ (kích thước thường <10 nm) bám đều đặn trên vách carbon. Nó cũng cho thấy các vân tinh thể graphit hóa bao bọc xung quanh hạt kim loại (cấu trúc lõi-vỏ), bảo vệ kim loại khỏi bị ăn mòn trong kiềm.

### B. Phép đo hấp phụ-khử hấp phụ Nitơ (Đo BET)
*   **Mục tiêu:** Xác định diện tích bề mặt riêng (SSA) và phân bố kích thước lỗ xốp.
*   **Thông số quan trọng:**
    *   *Đường cong đẳng nhiệt (Isotherm):* CA xơ dừa tối ưu thường cho đường cong hỗn hợp loại I và loại IV (theo IUPAC), chứng tỏ vật liệu sở hữu cấu trúc **lỗ xốp phân cấp (hierarchical porosity)** chứa cả vi lỗ (micropore) và lỗ trung bình (mesopore).
    *   *Chỉ số diện tích bề mặt (SSA):* Phải đạt từ **1200 đến 3500 m²/g** để đạt hiệu suất điện hóa cao nhất.
    *   *Phân bố kích thước lỗ xốp (PSD):* Tính toán qua mô hình DFT hoặc BJH để xác định đường kính mesopores tối ưu trong khoảng **3 - 5 nm**.

### C. Nhiễu xạ tia X (XRD) & Phổ Raman (Raman Spectroscopy)
*   **XRD (X-ray Diffraction):**
    *   *Mục tiêu:* Xác định cấu trúc tinh thể và các pha kim loại.
    *   *Đặc trưng:* XRD sẽ chỉ ra hai pic rộng của cấu trúc carbon vô định hình hoặc carbon bán tinh thể ở góc $2\theta \approx 24^\circ$ và $44^\circ$. Đồng thời, các đỉnh nhiễu xạ sắc nhọn ở góc $2\theta \approx 44.5^\circ, 51.8^\circ$ và $76.3^\circ$ tương ứng với các mặt mạng (111), (200), (220) của pha tinh thể hợp kim lưỡng kim $NiCo$ hệ lập phương tâm mặt (fcc).
*   **Phổ Raman:**
    *   *Mục tiêu:* Đánh giá mức độ khuyết tật và mức độ than hóa (graphitization) của carbon.
    *   *Chỉ số cốt lõi:* Tỷ lệ cường độ giữa pic D (khoảng $1350 cm^{-1}$, đại diện cho cấu trúc khuyết tật, sai hỏng) và pic G (khoảng $1580 cm^{-1}$, đại diện cho carbon mạng lưới tinh thể $sp^2$) $\rightarrow$ **Tỷ lệ $I_D/I_G$**.
    *   *Ý nghĩa:* Tỷ lệ $I_D/I_G$ tối ưu cho cảm biến điện hóa là từ **0.9 đến 1.2**. Tỷ lệ này cân bằng hoàn hảo giữa mật độ khuyết tật (tạo vị trí hoạt tính cho cảm biến) và mức độ graphit hóa (tăng khả năng dẫn điện).

---

## 2. HƯỚNG DẪN VẬN HÀNH THIẾT BỊ ĐO ĐIỆN HÓA CHI TIẾT (ELECTROCHEMICAL STATION GUIDE)

### Thiết bị: Máy đo điện hóa Autolab / PGSTAT / CHI660E
*   **Quy trình chuẩn bị hệ thống:**
    1.  Cắm cáp kết nối điện cực từ máy đo vào các đầu điện cực tương ứng: Cáp màu xanh lá cây vào **WE** (GCE+CA), cáp màu đỏ vào **CE** (Dây Pt), cáp màu trắng vào **RE** (Ag/AgCl).
    2.  Rót dung dịch điện ly kiềm ($0.1M NaOH$) vào cốc đo teflon sạch (khoảng 15-20 mL). Đảm bảo cả 3 đầu điện cực đều ngâm ngập trong dung dịch ít nhất 1.5 cm.
3.  **Kỹ thuật đo Quét thế tuần hoàn (Cyclic Voltammetry - CV) ổn định màng:**
    *   *Thiết lập thông số:* Khoảng quét thế từ **0.0 V đến +0.6 V vs Ag/AgCl**; tốc độ quét thế **50 mV/s**.
    *   *Thao tác:* Chạy liên tục **50 chu kỳ** quét CV đầu tiên trong dung dịch $NaOH$ trắng.
    *   *Ý nghĩa:* Việc quét CV liên tục giúp dung dịch kiềm thấm sâu vào các vi lỗ của carbon aerogel, đồng thời oxy hóa bề mặt kim loại $NiCo$ tạo thành lớp oxy-hydroxide hoạt tính ($NiOOH, CoOOH$), giúp dòng nền đạt trạng thái ổn định tuyệt đối trước khi tiến hành đo glucose.
4.  **Kỹ thuật đo Dòng - Thời gian nhạy cao (Amperometry - i-t):**
    *   *Thiết lập thông số:* Thế phân cực không đổi (E_applied) = **+0.5 V vs Ag/AgCl** (thế tối ưu để xảy ra phản ứng oxy hóa glucose mà ít bị ảnh hưởng bởi nhiễu nền); thời gian đo: 400 giây; thời gian lấy mẫu: 0.1 giây.
    *   *Thao tác thực hiện:*
        *   Bật thanh khuấy từ hoạt động ở tốc độ không đổi ổn định (khoảng 300 rpm) để đảm bảo sự phân tán chất phân tích nhanh và đồng đều trong cốc đo.
        *   Nhấn Start bắt đầu đo. Đợi khoảng 100 giây cho dòng nền giảm xuống ổn định và phẳng hoàn toàn (dòng nền giảm dần và tiệm cận mức hằng số).
        *   Tại giây thứ 120, tiến hành tiêm (inject) chính xác một thể tích nhỏ dung dịch glucose chuẩn vào cốc đo bằng micropipette siêu nhạy.
        *   *Hiện tượng quan sát:* Dòng điện sẽ lập tức tăng vọt lên tạo thành một bước nhảy dòng sắc nét dạng bậc thang trong vòng chưa đầy **3 giây** (thời gian đáp ứng cực nhanh nhờ cấu trúc lỗ xốp phân cấp).
        *   Tiếp tục tiêm các nồng độ glucose tăng dần ở các khoảng thời gian đều đặn tiếp theo (giây thứ 160, 200, 240,...) để dựng đường chuẩn tuyến tính ($I_p$ vs Concentration).
"""

    # Dictionary of handbooks and contents
    handbooks = {
        base_dir / "1_coconut_coir_carbon_aerogel_synthesis_sop.md": h1_content,
        base_dir / "2_pore_engineering_and_doping_handbook.md": h2_content,
        base_dir / "3_electrode_fabrication_and_electrochemistry_sop.md": h3_content,
        base_dir / "4_material_characterization_and_instrumentation_guide.md": h4_content
    }

    # Write each handbook
    for path, content in handbooks.items():
        long_p = make_long_path(path)
        with open(long_p, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"  -> Successfully generated core handbook: {path.name}")
    print("  -> All 4 Core Handbooks generated successfully.")

def clean_up_intermediate_markdowns():
    print("Cleaning up intermediate/raw markdown files to leave workspace pristine...")
    
    # We want to delete the raw unconsolidated markdown files in 2 Ref lib
    # but KEEP the newly generated handbooks, directories, and anything inside Archive.
    # Also keep standard directories, but remove raw md files inside 2 Ref lib/old (which were converted from docx).
    
    # List of specific raw intermediate md files to clean up in 2 Ref lib/old subdirectories
    for root, dirs, files in os.walk(make_long_path(base_dir)):
        # Skip Archive directory and main handbooks
        if "Archive" in root:
            continue
            
        norm_root = Path(root[4:] if root.startswith('\\\\?\\') else root)
        
        for file in files:
            file_path = norm_root / file
            # If it's a markdown file that is NOT one of the 4 handbooks
            if file.lower().endswith(".md") and not file.startswith(("1_", "2_", "3_", "4_", "ref_lib_")):
                long_p = make_long_path(file_path)
                if os.path.exists(long_p):
                    os.remove(long_p)
                    print(f"  -> Cleaned intermediate MD: {file_path.name}")
                    
    # Also clean up empty subfolders in 'old' to keep it tidy, or move old/ to Archive/Originals/
    old_dir = base_dir / "old"
    if os.path.exists(make_long_path(old_dir)):
        print("Moving old/ folder contents to Archive...")
        # Since we already moved docx, pdf, png to Archive/Originals/ and deleted intermediate MDs,
        # let's clean up any empty folders inside 'old/' and delete 'old/' if empty.
        for root, dirs, files in os.walk(make_long_path(old_dir), topdown=False):
            long_r = make_long_path(root)
            if not os.listdir(long_r):
                os.rmdir(long_r)
        if os.path.exists(make_long_path(old_dir)) and not os.listdir(make_long_path(old_dir)):
            os.rmdir(make_long_path(old_dir))
            print("  -> Cleaned empty 'old' directory.")

    # Also clean up 'Raw_Markdown' folder
    raw_md_dir = base_dir / "Raw_Markdown"
    if os.path.exists(make_long_path(raw_md_dir)):
        print("Cleaning up intermediate Raw_Markdown folder...")
        for root, dirs, files in os.walk(make_long_path(raw_md_dir), topdown=False):
            long_r = make_long_path(root)
            for file in files:
                os.remove(os.path.join(long_r, file))
            if not os.listdir(long_r):
                os.rmdir(long_r)
        if os.path.exists(make_long_path(raw_md_dir)) and not os.listdir(make_long_path(raw_md_dir)):
            os.rmdir(make_long_path(raw_md_dir))
            print("  -> Cleaned empty 'Raw_Markdown' directory.")

def main():
    print("=== STARTING REFERENCE LIBRARY RESTRICTION & CONSOLIDATION ===\n")
    create_directories()
    delete_redundant_files()
    move_files_to_archive()
    write_core_handbooks()
    clean_up_intermediate_markdowns()
    print("\n=== SUCCESS: REFERENCE LIBRARY COMPACT & CLEAN ===")

if __name__ == "__main__":
    main()
