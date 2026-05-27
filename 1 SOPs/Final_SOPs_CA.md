# Final_SOPs_CA.md — Hướng Dẫn Thực Nghiệm Rút Gọn & Tinh Giản Chế Tạo Carbon Aerogel Điện Hóa

> [!NOTE]
> * **Tài liệu tham chiếu chuẩn cốt lõi:**
>   1. Luận án Tiến sĩ Nguyễn Trần Xuân Phương 2024 (Tài liệu: `TOM_TAT_NTXPhuong.md` trong thư mục `08_Review_va_Tong_quan`).
>   2. Công trình Fauziyah et al. 2020 (Ind. Eng. Chem. Res.) (Tài liệu: `2 Nitrogen-Doped Carbon Aerogels Prepared by Direct Pyrolysis of.md` trong thư mục `02_Doping_va_Gel_hoa`).
>   3. Công trình Wu et al. 2024 (Sensors) (Tài liệu: `1 Facile Synthesis of Fe-Doped Algae Residue-Derived Carbon Aerogels for.md` trong thư mục `02_Doping_va_Gel_hoa`).

---

## PHẦN I: MA TRẬN ĐIỀU KIỆN PHẢN ỨNG VÀ THÔNG SỐ THỰC NGHIỆM TỔNG HỢP

Bảng tổng hợp toàn bộ các thông số điều kiện phản ứng cốt lõi (*T*, *t*, *C*, *Ratio*) từ GĐ0 đến GĐ6:

| Giai đoạn | Quy trình thao tác | Nhiệt độ (*T*) | Thời gian (*t*) | Nồng độ (*C*) | Tỉ lệ phản ứng / phối trộn (*Ratio*) |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **GĐ0** | Tiền xử lý kiềm hóa (tách lignin) | 80 ± 2 °C | 4 giờ | 6 wt% NaOH | 1 g bột : 20 mL dung dịch |
| **GĐ1A** | Sol NH₄OH-Urea (Chính) | ≤ 10 °C | 30 phút | 25 wt% NH₄OH | 1.0 g DCF : 11 mL NH₄OH : 4.0 g Urea : 5 mL H₂O |
| **GĐ1B** | Sol NaOH-Urea (Đối chứng) | -10 °C đến -12 °C | 5 phút | 7%/12%/81% | 7 wt% NaOH : 12 wt% Urea : 81 wt% H₂O |
| **GĐ2A** | Gel hóa NH₄OH-Urea (Đông đông) | -5 °C | 24 giờ | — | Đúc khuôn PP, đông gel → Rã đông tự nhiên |
| **GĐ2B** | Gel hóa NaOH-Urea (Đông tụ) | 70 °C | 1.5 - 2 giờ | 96 vol% Ethanol | Rã đông sol → Đông tụ trong cồn 96% nóng |
| **GĐ3A** | Keo tụ & Solvent Exchange (NH₄OH) | 0 - 5 °C | 24 giờ (cồn) + 4 giờ (nước) | 98 vol% EtOH / Nước DI | Ngâm cồn 98% lạnh (24 giờ) → Rửa ngược nước DI (2 lần x 2 giờ) |
| **GĐ3B** | Rửa trung hòa & Tẩm sắt (NaOH) | 25 - 30 °C (rửa) / 0 - 5 °C (tẩm) | Đến pH ≈ 7 + 24 giờ | Nước DI / 10 wt% Fe | Rửa nước cất đến pH ≈ 7 → Tẩm Fe³⁺ (24 giờ, Fe/N-CA) |
| **GĐ4** | Sấy thăng hoa chân không | 80 °C (đông) / ≤ 50 °C (bẫy) | 36 - 48 giờ | P < 20 Pa | Thăng hoa trực tiếp tinh thể đá |
| **GĐ5A** | Nhiệt phân N-CA | 700 °C | 2 giờ | 5 °C/phút | Lưu lượng khí bảo vệ N₂ = 100 mL/phút |
| **GĐ5B** | Nhiệt phân Fe/N-CA (nền) | 800 °C | 2 giờ | 5 °C/phút | Lưu lượng khí bảo vệ N₂ = 100 mL/phút |
| **GĐ6A** | Acid Leaching | 80 ± 2 °C | 8 giờ | 0.5 M HCl | 1 g bột : 100 mL dung dịch HCl (đun hồi lưu) |
| **GĐ6B** | Annealing lần 2 | 800 °C | 1 giờ | 5 °C/phút | Lưu lượng khí bảo vệ N₂ = 100 mL/phút |

---

## PHẦN II: QUY TRÌNH THAO TÁC CÁC GIAI ĐOẠN CHẾ TẠO (GĐ0 ĐẾN GĐ6)

### GIAI ĐOẠN 0: TIỀN XỬ LÝ KIỀM HÓA TÁCH LIGNIN (Delignification Pretreatment)

> [!IMPORTANT]
> **⚠️ Ràng buộc định hướng Điện hóa & Cảm biến (No Bleaching):** 
> Trái với hướng hấp phụ chất màu/dầu của hệ xenluloza tinh khiết (cần tẩy trắng để thu sợi trắng BCF), đối với hướng **Điện cực cảm biến điện hóa (carbon aerogel)**, quy trình thực nghiệm **tuyệt đối không tẩy trắng bằng H₂O₂/NaClO₂ và không thủy phân acid mạnh bằng HCl**. 
> *   *Lý do 1 (Bảo toàn cấu trúc 3D):* Chất tẩy trắng và acid mạnh cắt đứt mạch xenluloza làm giảm độ trùng hợp (DP), khiến vách ống tế bào xơ dừa bị mỏng yếu và dễ sụp đổ khi nhiệt phân cao tần (pore collapse).
> *   *Lý do 2 (Giữ lại dị nguyên tố tự nhiên):* Giữ nguyên cấu trúc thô bán tinh thể giúp lưu giữ các dị tố hữu cơ tự nhiên có sẵn trong xơ dừa, hỗ trợ đắc lực cho quá trình tự doping nitơ và phối trí kim loại sắt (Fe) tạo active sites.
> Do đó, xơ dừa sau kiềm hóa thu được bột **DCF (Delignified Coir Fiber)** có màu nâu nhạt sẽ được dùng trực tiếp để làm sol-gel.

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1. Chuẩn bị xơ dừa xay nghiền, rây lấy kích thước hạt < 125 µm, sấy khô ở 80 °C trong 24 giờ.
2. Ngâm 50 g bột xơ dừa khô trong 1000 mL nước nóng (80 °C) trong 4 giờ dưới lực khuấy từ 600 rpm để rửa sạch bụi bẩn và sáp cơ học. Lọc qua phễu Buchner.
3. Cho bã lọc vào bình phản ứng 1000 mL chứa dung dịch **NaOH 6 wt%** (pha 60 g NaOH rắn trong 1000 mL nước cất DI, tỉ lệ rắn/lỏng = 1:20 w/v).
4. Đun ở **80 ± 2 °C** trong **4 giờ** liên tục, tốc độ khuấy duy trì 600 rpm. Bọc kín miệng bình tam giác bằng màng chịu nhiệt.
5. Lọc lấy bã qua phễu Buchner, rửa liên tục bằng nước cất DI nóng (60 °C) cho đến khi nước rửa đạt pH trung tính hoàn toàn (pH = 6.5 - 7.0).
6. Sấy bột ẩm ở **80 °C trong 12 giờ**, rây lại thu bột xơ dừa kiềm hóa **DCF**. Cân chính xác khối lượng bột khô để tính hiệu suất hao hụt (**Weight-loss %**).

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Hao hụt khối lượng khô (Gravimetric Weight-loss %):** Phải đạt trong dải **30% - 38%** (xác nhận loại bỏ thành công phần lớn lignin vô định hình và hemicellulose dễ tan).
*   **Đường kính sợi (SEM):** Sợi co rút từ 80 - 100 µm xuống còn **20 - 50 µm** (vách ngoài sần sùi lộ cellulose cấu trúc hình ống).
*   **Độ tinh thể hóa (XRD):** Đạt **≥ 55%** (Xuất hiện các đỉnh đặc trưng của Cellulose I tại góc quét 2θ ≈ 16.08^o (110) và 22.23^o (200)).
*   **Hàm lượng cellulose bề mặt:** Đạt **≥ 69.8 wt%** (phổ FT-IR xuất hiện peak dao động C-O-C tại 1050 cm⁻¹ sắc nét, các liên kết este của lignin tại 1735 cm⁻¹ giảm >90%).

---

### GIAI ĐOẠN 1: TỔNG HỢP HỆ SOL CELLULOSE & ĐỐI CHỨNG DUNG MÔI ĐIỆN HÓA (Sol Preparation)

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
*   **Hệ dung môi chính Ammonia-Urea (NH₄OH-Urea):**
    1. Cân chính xác 1.0 g Cellulose DCF + hòa tan 4.0 g Urea tinh thể vào hỗn hợp 11.0 mL NH₄OH đậm đặc (25 wt%) và 5.0 mL nước cất DI trong bình Teflon đậy kín.
    2. Cho 1.0 g DCF vào bình dung môi.
    3. Đặt bình vào bể siêu âm đầy đá nước lạnh duy trì **≤ 10 °C (tối ưu 0 - 5 °C)**.
    4. Siêu âm xung (**2 giây ON / 1 giây OFF**) trong **30 phút** ở công suất trung bình.
    5. Thu được hệ sol màu hơi đục nhẹ, hoàn toàn đồng nhất.
*   **Hệ dung môi đối chứng NaOH-Urea (Đo siêu tụ):**
    1. Định lượng tỷ lệ khối lượng chuẩn 7 wt% NaOH : 12 wt% Urea : 81 wt% H₂O.
    2. Làm lạnh dung dịch về **10 °C đến 12 °C** trong tủ đông sâu đến trạng thái bán đóng băng (slushy).
    3. Cho nhanh 1.0 g DCF vào dung môi lạnh, khuấy từ tốc độ cao 3000 rpm trong **5 phút** ở nhiệt độ phòng. Thu được hệ sol trong suốt.

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Trạng thái Sol:** Đồng nhất, hoàn toàn không còn xơ sợi chưa tan bám đáy.
*   **Nhiệt độ bể siêu âm hệ NH₄OH:** Phải khống chế **≤ 10 °C** trong suốt quá trình. Nếu nhiệt độ >15 °C, NH₃ bay hơi đột ngột gây hỏng sol (Fail).
*   **XRD của hydrogel:** Xuất hiện các đỉnh đặc trưng của Cellulose III tại góc 2θ ≈ 11.6^o (110) và 20.5^o (002). Đỉnh Cellulose I (22.23^o) phải biến mất hoàn toàn.

---

### GIAI ĐOẠN 2: ĐÚC KHUÔN PP & GIÀ HÓA NHIỆT HÌNH THÀNH HYDROGEL (Casting & Gelation)

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Đúc khuôn và De-gassing:** Rót từ từ dung dịch sol lạnh vào các ống tiêm Polypropylene (PP) đã cắt bỏ đầu kim. Đặt đứng ống tiêm trong ngăn mát tủ lạnh ở **0 - 5 °C trong thời gian 30 - 60 phút** để khử hoàn toàn bọt khí và ổn định hệ sol.
2.  **Già hóa tạo gel (Gelation & Coagulation):** Bọc kín hai đầu ống tiêm đúc khuôn.
    *   *Đối với hệ NH₄OH-Urea (Chính):* Đặt tĩnh ống tiêm đúc khuôn trong ngăn đông tủ lạnh ở **-5 °C trong 24 giờ** để hình thành gel lạnh (frozen gelation). Sau đó, lấy khối gel ra ngoài và để rã đông tự nhiên ở nhiệt độ phòng (25 - 30 °C).
    *   *Đối với hệ đối chứng NaOH-Urea:* Lấy sol từ tủ đông sâu ra rã đông ở nhiệt độ phòng. Rót sol vào khuôn, sau đó thả khuôn chứa sol vào bình chứa cồn **Ethanol 96% đun nóng ở 70 °C duy trì trong 1.5 - 2 giờ** để kích hoạt phản ứng đông tụ gel hóa nhanh (`EtOH 96°, 70 °C Gel hoá`).
3.  Dùng pít-tông nhẹ nhàng đẩy khối hydrogel đã định hình ra ngoài.

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Hình thái Hydrogel:** Khối hydrogel monolith trụ nhẵn bóng, dẻo dai, đàn hồi tốt, hoàn toàn không bị nứt vỡ, móp méo hay rỗng ruột bọt khí.
*   **Tính ổn định:** Hydrogel giữ form 3D ổn định khi đặt đứng trên khay kính phẳng.

---

### GIAI ĐOẠN 3: KEO TỤ, TẨM ĐỐP Fe & KHÓA GIỮ UREA CÓ KIỂM SOÁT (Coagulation & Fe Impregnation)

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Keo tụ & Trao đổi dung môi (Coagulation & Solvent Exchange):**
    *   *Đối với hệ NH₄OH-Urea (Chính):*
        *   **Keo tụ (Coagulation):** Thả khối hydrogel đã rã đông vào bình chứa cồn **Ethanol 98% lạnh (0 - 5 °C)** với tỷ lệ tối thiểu **15 mL ethanol / 1 g cellulose** ban đầu. Đậy kín nắp và ngâm tĩnh trong tủ lạnh ở **4 °C (0 - 5 °C) trong 24 giờ** để đông tụ chậm và cố định mạng lưới cellulose III.
        *   **Trao đổi dung môi ngược (Solvent Exchange):** Gạn bỏ cồn cũ, ngâm rửa gel bằng nước cất DI sạch (gấp 5 lần thể tích gel) ở nhiệt độ phòng trong **2 giờ**, lặp lại **chính xác 2 lần** để rửa sạch cồn và amoniac tự do, thay thế hoàn toàn cồn bằng nước DI trong mạng mao quản.
        > [IMPORTANT]
        > **⚠️ Cảnh báo sấy & rửa ngược:** Bắt buộc phải trao đổi ngược từ cồn sang nước DI trước khi sấy thăng hoa vì Ethanol có điểm đông đặc cực thấp (-114 °C) không thể đông băng ở nhiệt độ tủ sấy (-20 °C hay -80 °C), dẫn đến hiện tượng sôi dung môi làm sập cấu trúc gel (collapse) dưới áp suất chân không. Tuy nhiên, tuyệt đối không rửa nước DI quá 4 lần hoặc ngâm kéo dài >12 giờ để tránh làm trôi toàn bộ Urea tự do bám trong gel (nguồn N-doping duy nhất).
    *   *Đối với hệ đối chứng NaOH-Urea:*
        *   **Rửa trung hòa:** Ngâm rửa khối gel trong bể nước cất DI lớn ở nhiệt độ phòng, thay nước sạch sau mỗi 2 - 4 giờ **cho đến khi nước rửa đạt pH trung tính hoàn toàn (pH ≈ 7)** để loại bỏ toàn bộ NaOH và urea tự do dư thừa bám dính.
        > [WARNING]
        > **⚠️ Cấm cặn kiềm:** Bắt buộc phải rửa trung hòa đến pH ≈ 7 để loại bỏ hoàn toàn các ion Na⁺. Nếu còn cặn kiềm NaOH trong mạng gel, khi nhiệt phân ở 800 °C sẽ xảy ra phản ứng ăn mòn hóa học kiềm cực mạnh (Alkaline/Na-etching), phá hủy hoàn toàn vách tế bào carbon và làm sập cấu trúc mao quản, dẫn đến diện tích bề mặt sụt giảm nghiêm trọng (*S*_BET ≤ 150 m²/g).
        *   **Tạo liên kết TEPA (Đối với mẫu NUTA):** Ngâm khối gel đã rửa trung hòa vào dung dịch **TEPA : EtOH : H₂O (tỷ lệ 2:5:3 v/v)** ở nhiệt độ phòng trong **24 giờ** để tạo liên kết ngang hóa học cố định cấu hình chứa N.
2.  **Tẩm Sắt (Fe Impregnation - Dành cho nhánh mẫu Fe/N-CA):**
    *   Hòa tan hoàn toàn **0.484 g FeCl₃·6H₂O** và 1.0 g Urea vào 30 mL nước cất DI lạnh (0 - 5 °C).
    *   Thả khối gel NH₄OH-Urea đã keo tụ và rửa sạch vào dung dịch tẩm sắt.
    *   Siêu âm nhẹ trong 30 phút ở bể nước đá, sau đó ngâm tĩnh trong tủ mát 4 °C trong **24 giờ** liên tục để ion Fe³⁺ khuếch tán bão hòa đều từ vỏ vào tận tâm lõi gel.

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Màu sắc hydrogel sau tẩm:** Khối hydrogel N-CA có màu trắng đục nhẹ đồng đều. Khối hydrogel Fe/N-CA ẩm phải chuyển hẳn sang **màu nâu đỏ/vàng cam đồng đều** từ lớp vỏ ngoài cho đến tận tâm lõi khối gel.
*   **Trạng thái gel:** Khối gel giữ nguyên cấu trúc trụ tròn, không bị mềm nhũn hay nứt vỡ.

---

### GIAI ĐOẠN 4: SẤY THĂNG HOA BẢO TOÀN CẤU TRÚC MAO QUẢN (Freeze Drying)

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Cấp đông sâu siêu tốc:** Đặt các khối gel ẩm sau tẩm vào tủ đông siêu sâu duy trì ở nhiệt độ **80 °C** hoặc nhúng trực tiếp khối gel vào bình chứa Nitơ lỏng (LN₂, 196 °C) trong **5 phút**.
2.  **Sấy thăng hoa chân không:**
    *   Đảm bảo nhiệt độ bẫy lạnh đạt **≤ 50 °C** (tối ưu 80 °C) và áp suất chân không **< 20Pa (0.15 Torr)**.
    *   Duy trì sấy thăng hoa liên tục trong **36 - 48 giờ**.
3.  Thu hồi aerogel xốp dẻo siêu nhẹ. Dùng thước kẹp đo kích thước để xác định độ co ngót.

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Độ co ngót tuyến tính (Linear Shrinkage %):** Phải đạt chỉ số **Linear Shrinkage < 12%** tính theo công thức:
    *   **Công thức tính:** Shrinkage % = (D_gel - D_aerogel) / D_gel × 100%
    *   ✓ **Pass:** Shrinkage < 12%.
    *   *   ✗ **Fail:** Shrinkage ≥ 20% (cấu trúc mạng mao quản bị sụp đổ).
*   **Khối lượng riêng thể tích (Bulk density):** Duy trì trong dải **0.03 - 0.05 g/cm³** (siêu nhẹ).

---

### GIAI ĐOẠN 5: NHIỆT PHÂN CARBON HÓA LẦN 1 & DOPING NITƠ (First Pyrolysis & N-doping)

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Chuẩn bị:** Xếp các khối aerogel khô vào thuyền sứ sạch, đẩy vào tâm nhiệt độ của lò nung ống thạch anh.
2.  **Purge đuổi Oxy bảo vệ:** Thổi dòng khí N₂ tinh khiết (99.99%) với lưu lượng **150 - 200 mL/phút liên tục trong 30 phút** trước khi gia nhiệt. Duy trì dòng khí N₂ bảo vệ ổn định ở lưu lượng **100 mL/phút** trong suốt tiến trình nung.
3.  **Chương trình nhiệt phân 3 Ramp (Gia nhiệt 5 °C/phút):**
    *   *Ramp 1 (Sấy ẩm sâu):* Nâng từ 25 °C &rarr; 150 °C, giữ nhiệt **30 phút**.
    *   *Ramp 2 (Carbon hóa sơ bộ):* Nâng từ 150 °C &rarr; 400 °C, giữ nhiệt **30 phút**.
    *   *Ramp 3 (Carbon hóa sâu & Doping):* Nâng từ 400 °C &rarr; T_target, giữ nhiệt liên tục trong **2 giờ (120 phút)**.
    *   *Nhiệt độ mục tiêu (T_target):*
        *   **Nhánh mẫu N-CA:** Chọn **T_target = 700 °C**.
        *   **Nhánh mẫu Fe/N-CA (nền):** Chọn **T_target = 800 °C**.
4.  **Làm nguội:** Tắt gia nhiệt, để lò nguội tự nhiên dưới dòng khí N₂ thổi liên tục. Mở lò lấy mẫu khi nhiệt độ đầu đo đạt **< 50 °C**.

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Trạng thái vật liệu sau nung:** Khối carbon aerogel thu được phải có **màu đen tuyền**, xốp, giữ nguyên hình monolith trụ ban đầu nhưng có sự co rút thể tích nhẹ. Bulk density đạt **0.05 g/cm³ (NH₃-Urea)** hoặc **0.07 g/cm³ (NaOH-Urea)**.
*   **Độ bền cơ học:** Thử nghiệm ép nén đạt Young Modulus ổn định từ **6.43kPa (N-CA)** đến **138.59kPa (Fe/N-CA)**.

---

### GIAI ĐOẠN 6: RỬA AXIT & ANNEALING LẦN 2 TẠO TÂM Fe-N₄ SIÊU SẠCH (Acid Leaching & Re-annealing)

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Phản ứng Acid Leaching đun hồi lưu:**
    *   Sử dụng dung dịch **HCl 0.5 M** làm tác nhân hòa tan.
    *   Cho bột Fe/N-CA nung lần 1 vào bình cầu chứa dung dịch HCl 0.5 M với tỷ lệ **1 g bột / 100 mL dung dịch**.
    *   Lắp hệ thống sinh hàn hồi lưu nước và đặt trên bếp khuấy từ đun sôi nhẹ ở nhiệt độ **80 ± 2 °C liên tục trong 8 giờ** (tốc độ khuấy 200 rpm).
2.  **Lọc rửa trung hòa:** Lọc chắt bột carbon qua phễu lọc chân không Buchner dùng giấy lọc sợi thủy tinh. Rửa liên tục bằng nước cất DI nóng (60 °C) cho đến khi nước rửa đạt pH ≈ 7.0. Sấy khô bột ở 80 °C trong 12 giờ.
3.  **Annealing tái hoạt hóa lần 2:**
    *   Đặt bột sấy khô vào lò nung ống thạch anh. Purge khí N₂ tương tự Giai đoạn 5.
    *   Thiết lập chương trình gia nhiệt 5 °C/phút lên đúng nhiệt độ mục tiêu **800 °C và giữ nhiệt chính xác trong 1 giờ (60 phút)** dưới dòng khí N₂ bảo vệ (100 mL/phút).
    *   Để lò nguội tự nhiên về < 50 °C dưới dòng khí bảo vệ. Bảo quản bột trong vial thủy tinh tối màu quấn Parafilm cất ở tủ mát **4 °C**.

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **XRD kiểm tra pha tinh thể sắt:** Giản đồ XRD của bột Fe/N-CA sau annealing lần 2 phải **hoàn toàn sạch**, biến mất toàn bộ các đỉnh nhiễu xạ sắc nhọn của sắt kim loại α-Fe (2θ ≈ 44.7^o) và sắt carbide Fe₃C (2θ ≈ 43.9^o).
    *   ✓ **Pass:** Fe phân tán đơn nguyên tử tuyệt đối (single-atom), không kết tinh pha thô.
    *   ✗ **Fail:** Vẫn xuất hiện đỉnh sắt tinh thể thô (quá trình rửa axit chưa đạt yêu cầu).
*   **Hàm lượng nguyên tố bề mặt (XPS):** Sắt đạt **0.4 - 1.5 at%** và Nitơ đạt **3.0 - 6.0 at%** với tỷ lệ tối thiểu N:Fe ≥ 4:1.

---

## PHẦN III: QUY TRÌNH BIẾN TÍNH ĐIỆN CỰC LÀM VIỆC & ĐO ĐẠC ĐIỆN HÓA

### GIAI ĐOẠN 0: ĐÁNH BÓNG & ANODIZE HOẠT HÓA GCE

1.  **Mài mịn vật lý:** Nhỏ vài giọt nước cất và bột Al₂O₃ cỡ hạt 0.05 µm lên tấm nỉ mài. Đặt đứng điện cực GCE vuông góc 90° so với mặt nỉ, di chuyển mài nhẹ nhàng vẽ theo **hình số 8** liên tục trong **2 phút**.
2.  **Làm sạch siêu âm:** Nhúng GCE vào cốc nước cất DI, siêu âm làm sạch trong **1 phút** (lặp lại 3 lần với nước DI mới). Siêu âm tráng nhanh bằng cồn ethanol tuyệt đối trong **1 phút** để khử ẩm.
3.  **Anodize hoạt hóa kiềm:** Nhúng điện cực GCE vào dung dịch **NaOH 0.1 M**. Áp thế điện thế phân cực dương **+1.8 V vs. Ag/AgCl trong thời gian 10 giây**. Rửa lại bằng nước cất DI.
4.  **Kiểm tra độ sạch (CV redox probe):**
    *   Dung dịch đo: **5.0mM K₃Fe(CN)₆ trong nền 0.1M KCl**.
    *   Quét thế tuần hoàn CV ở tốc độ quét **50 mV/s** (quét 3 chu kỳ).
    *   ✓ **Tiêu chí Pass:** Thế hiệu đỉnh tách biệt **ΔE_p < 70 mV** và tỷ số dòng điện đỉnh đối xứng ***I*_pa/*I*_pc ≈ 0.95 - 1.05**.

### GIAI ĐOẠN 1: PHA CHẾ MỰC IN BINDER & PHỦ ĐIỆN CỰC (Drop-casting)

1.  **Định lượng pha chế Conductive Ink (Nồng độ 5 mg/mL) và quy hoạch Binder:**
    Tùy thuộc vào phương pháp phủ màng và chất phân tích, nồng độ pha chế của chất kết dính (binder) được tính toán nghiêm ngặt để cân bằng giữa độ bền liên kết và độ dẫn điện bề mặt:

    *   **🧪 Phương pháp A: Mực Hợp Phần Đồng Nhất (Single-pot Composite Ink - Khuyên dùng):**
        *   **Điện cực Fe/N-CA / Chitosan/GCE (Đo kim loại nặng SWASV):** Bột Carbon Aerogel (Fe/N-CA): **5.0 mg** + dung môi DMF tinh khiết: **950 µL** + dung dịch **Chitosan 1 wt%** (trong acid acetic 1%): **50 µL** (Cho nồng độ Chitosan cuối trong mực là **0.05 wt%**, đây là "Sweet Spot" chelate Pb²⁺ tối ưu mà không cản trở dòng điện).
        *   **Điện cực N-CA-700 / Nafion/GCE (Đo Paracetamol DPV):** Bột Carbon Aerogel (N-CA-700): **5.0 mg** + dung môi DMF tinh khiết: **950 µL** + dung dịch **Nafion 5 wt% thương mại**: **50 µL** (Cho nồng độ Nafion cuối trong mực đạt đúng **0.25 wt%** hoạt tính cao).
    *   **🧪 Phương pháp B: Phủ Màng Từng Lớp (Layer-by-Layer Coating - Tùy chọn):**
        *   *Lớp carbon nền:* Nhỏ **5.0 µL** mực carbon thuần (5.0 mg N-CA-700 trong 1000 µL DMF tinh khiết, không chứa binder). Sấy khô nhẹ ở 40 °C trong 15 phút.
        *   *Lớp màng bảo vệ:* Nhỏ phủ tiếp **2.0 µL** dung dịch **Nafion 0.25 wt%** (pha loãng bằng cách trộn 10 µL Nafion 5 wt% thương mại + 190 µL Ethanol tuyệt đối) lên trên lớp carbon đã khô, để khô tự nhiên.

2.  **Thao tác thực hiện:**
    *   **Siêu âm phân tán mực:** Bình chứa mực được đậy kín nắp, đặt vào bể siêu âm nước đá lạnh (nhiệt độ duy trì **< 15 °C** để ngăn bay hơi và keo tụ binder). Siêu âm liên tục trong **30 - 60 phút** ở chế độ thường.
    *   **Drop-casting:** Dùng pipette vi lượng hút chính xác **5.0 µL** mực in (đối với cả Phương pháp A và lớp nền Phương pháp B) nhỏ lên trung tâm bề mặt điện cực GCE đã được dựng thẳng đứng trên giá đỡ.
    *   **Sấy khô màng mỏng (Bắt buộc):** Úp ngược một cốc thủy tinh sạch che bụi lên điện cực GCE, để màng khô tự nhiên hoàn toàn ở nhiệt độ phòng (25 °C) trong **2 - 3 giờ** trong tủ hút.
    > [!IMPORTANT]
    > **⚠️ Cấm sấy gia nhiệt nhanh:** Tuyệt đối không sấy gia nhiệt nhanh, không thổi khí N₂, không sấy chân không đối với màng ướt để tránh hiệu ứng "vành cà phê" (coffee-ring) phá hỏng cấu trúc bề mặt màng.

### GIAI ĐOẠN 2: THIẾT LẬP THÔNG SỐ CHƯƠNG TRÌNH PHÂN TÍCH ĐIỆN HÓA CẢM BIẾN

#### 1. Phép đo cảm biến Pb²⁺ bằng kỹ thuật sóng vuông hòa tan (SWASV)
*   **Điện cực làm việc (WE):** Điện cực Fe/N-CA / Chitosan/GCE.
*   **Dung dịch điện ly nền:** Đệm Acetate 0.1 M, pH = 4.5.
*   **Bảng thông số cài đặt thiết bị đo (SWASV Parameters):**

| Thông số thiết lập | Giá trị cài đặt tiêu chuẩn |
| :--- | :---: |
| **Thế làm giàu khử (E_dep)** | **-1.1V** vs. Ag/AgCl |
| **Thời gian làm giàu (t_dep)** | **120 giây** (khuấy từ 400 rpm) |
| **Thời gian yên lặng (Quiet time)** | **10 giây** (không khuấy từ) |
| **Khoảng quét thế hòa tan** | **-1.4V đến -0.2V** vs. Ag/AgCl |
| **Tần số sóng vuông (SW Frequency)** | **25 Hz** |
| **Biên độ sóng vuông (SW Amplitude)** | **25 mV** |
| **Bước thế (Step potential)** | **5 mV** |
| **Thế điện cực làm sạch (Cleaning potential)**| **+0.2V** vs. Ag/AgCl trong 30 giây (600 rpm) |

*   **Đỉnh hòa tan cực đại của Chì (Pb⁰ → Pb²⁺ + 2e⁻):** Xuất hiện tại **≈ -0.5V**.

#### 2. Mở rộng đo đồng thời đa ion kim loại nặng (Zn²⁺, Cd²⁺, Pb²⁺, Cu²⁺) bằng kỹ thuật SWASV
*   **Dung dịch điện ly nền:** Đệm Acetate 0.1 M, pH = 4.5.
*   **Quy trình đo đồng thời (Simultaneous SWASV):**
    *   Đặt thế làm giàu khử âm sâu: **E_dep = -1.30V vs. Ag/AgCl** trong thời gian **t_dep = 120 - 180 giây** dưới lực khuấy từ 400 rpm.
    *   Quiet time: 10 giây.
    *   Quét sóng vuông hòa tan anode xuôi từ **-1.40V đến +0.40V** vs. Ag/AgCl.
*   **Thế hiệu đỉnh hòa tan (Stripping Potentials) đặc trưng:**

| Ion kim loại nặng | Stripping Peak Potential (vs. Ag/AgCl) |
| :--- | :---: |
| **Kẽm (Zn²⁺)** | **≈ -1.10V** |
| **Cadmium (Cd²⁺)** | **≈ -0.80V** |
| **Chì (Pb²⁺)** | **≈ -0.50V** |
| **Đồng (Cu²⁺)** | **≈ +0.05V** |

#### 3. Thiết lập quy trình đo riêng lẻ Thủy ngân (Hg²⁺) và Thạch tín (As³⁺)
*   **Dung dịch điện ly nền:** Đệm Acetate 0.1 M, pH = 4.5 (cho Hg²⁺) hoặc đệm H₂SO₄ loãng (cho As³⁺).
*   **Quy trình đo đơn Hg²⁺ / As³⁺:**
    *   Áp thế làm giàu khử chọn lọc: **E_dep = -0.20V đến -0.40V vs. Ag/AgCl** trong thời gian **120 - 180 giây** (tránh phản ứng phụ giải phóng hydro HER phá hỏng màng).
    *   Quiet time: 10 giây.
    *   Quét thế hòa tan sóng vuông từ **0.0V đến +0.6V** vs. Ag/AgCl.
*   **Thế hiệu đỉnh hòa tan đặc trưng:**
    *   **Thạch tín (As³⁺):** Xuất hiện tại **≈ +0.15V đến +0.20V**.
    *   **Thủy ngân (Hg²⁺):** Xuất hiện tại **≈ +0.25V đến +0.30V**.

#### 4. Phép đo cảm biến Paracetamol bằng kỹ thuật xung vi phân (DPV)
*   **Điện cực làm việc (WE):** Điện cực N-CA-700 / Nafion/GCE.
*   **Dung dịch điện ly nền:** Phosphate Buffered Saline (PBS) 0.1 M, pH = 7.0 - 7.4.
*   **Bảng thông số cài đặt thiết bị đo (DPV Parameters):**

| Thông số thiết lập | Giá trị cài đặt tiêu chuẩn |
| :--- | :---: |
| **Thế làm giàu khử (E_dep)** | **Không áp dụng (Không cần làm giàu)** |
| **Khoảng thế quét** | **0.0V đến +0.8V** vs. Ag/AgCl |
| **Tốc độ quét thế (Scan rate)** | **20 mV/s** |
| **Biên độ xung (Pulse Amplitude)** | **50 mV** |
| **Độ rộng xung (Pulse Width)** | **50 ms** |
| **Bước thế (Step potential)** | **5 mV** |

*   **Peak oxy hóa Paracetamol:** Xuất hiện rõ nét tại **≈ +0.34V** vs. Ag/AgCl.

---

### GIAI ĐOẠN 3: ĐO ĐẠC ĐẶC TÍNH ĐỐI CHỨNG ĐỒNG DẠNG NÂNG CAO (ORR & Siêu Tụ Điện)

#### 1. Phép đo Xúc tác khử Oxy (ORR) làm "Proof of Concept" chứng minh tâm Fe-N₄
*   **WE sử dụng:** Điện cực Fe/N-CA / Chitosan/GCE.
*   **Điện ly nền:** Dung dịch **KOH 0.1 M**.
*   **Quy trình đo đạc:**
  1.  Sục khí Nitơ (N₂) tinh khiết liên tục trong 30 phút vào bình điện giải. Quét CV từ **-1.0V đến +0.2V vs. Ag/AgCl** ở tốc độ quét 50 mV/s để thu được dòng điện dung nền.
  2.  Chuyển sang sục liên tục khí Oxy (O₂) trong 30 phút để bão hòa. Chạy quét thế CV tương tự. Đường phổ CV bắt buộc phải xuất hiện một peak khử oxy cực kỳ sắc nét ở thế dương hơn **-0.2V vs. Ag/AgCl** với cường độ dòng đỉnh khử đạt ***I*_c ≥ 1.0mA/cm²**.
  3.  Đo linear sweep voltammetry (LSV) trên điện cực quay RDE ở các tốc độ quay từ 400 rpm đến 3600 rpm để tính toán số electron chuyển tải (n ≈ 3.14 - 3.69 tiệm cận cơ chế 4 electron).

#### 2. Phép đo Siêu tụ điện hóa (Supercapacitor) của mẫu đối chứng NaOH-Urea
*   **WE sử dụng:** Mẫu carbon NaOH-Urea ép viên drop-cast.
*   **Điện ly nền:** Dung dịch **KOH 6.0 M** siêu đậm đặc.
*   **Quy trình đo đạc:**
  1.  Chạy CV trong KOH 6.0 M ở các tốc độ quét từ 5 - 100 mV/s trong khoảng thế tĩnh từ -1.0V → 0.0V vs. Ag/AgCl. Đường CV phải có dạng **hình hộp chữ nhật đối xứng chuẩn** đại diện cho điện dung lớp kép lý tưởng.
  2.  Đo phóng nạp dòng hằng GCD ở các mật độ dòng từ 0.5 - 10A/g. Đường phóng nạp GCD phải có dạng tam giác cân đối xứng, xác định điện dung riêng cụ thể (*C*_sF/g) để viết phần biện luận đối chứng cho luận văn.

---

## PHẦN IV: THÔNG SỐ ĐẶC TRƯNG KỸ THUẬT VẬT LIỆU ĐẠT CHUẨN (Material Spec Sheet)

Toàn bộ các chỉ số vật lý, hóa học, tinh thể đạt chuẩn (Pass Criteria) đối với bột Carbon Aerogel sau khi chế tạo được quy hoạch trực quan trong bảng dưới đây:

| Kỹ thuật phân tích | Chỉ số đặc trưng | Giá trị tiêu chuẩn đạt chuẩn (Pass Criteria) | Trạng thái (Fail Criteria) |
| :--- | :--- | :--- | :--- |
| **SEM** | Cấu trúc hình thái không gian | Mạng lưới tổ ong 3D phân cấp liên thông, đường kính macropores **10 - 100 µm**, thành vách phẳng mỏng mịn. | Thành vách vỡ vụn, sợi co cụm đặc khít, sập cấu trúc mao quản (mẫu đối chứng NaOH). |
| **TEM / HR-TEM** | Phân tán pha Sắt (Fe) | **Tuyệt đối không** xuất hiện hạt cụm sắt kim loại hoặc sắt carbide (Fe₃C) tinh thể lớn (kích thước > 5nm). Fe tồn tại dưới dạng các chấm sáng đơn phân tán cực nhỏ **< 1 nm**. | Xuất hiện các chấm đen đục kích thước lớn 10–50 nm (quá trình rửa axit chưa sạch sắt tạp). |
| **BET** | Dạng đẳng nhiệt hấp phụ | **Loại IV (Type IV Isotherm)** theo IUPAC, xuất hiện vòng lặp trễ (hysteresis loop) dạng H3 hoặc H4 ở P/P₀ = 0.4 - 0.9. | Không xuất hiện vòng lặp trễ, đường hấp phụ dạng dẹt (sụp đổ mesopores). |
| **BET** | Diện tích bề mặt riêng | ***S*_BET ≥ 3700m²/g** | S_BET < 1000 m²/g (tụt sâu về 150m²/g đối với mẫu đối chứng NaOH). |
| **BET** | Thể tích lỗ xốp | ***V*_pore ≥ 4.0cm³/g** | *V*_pore < 1.0cm³/g. |
| **BET** | Đường kính lỗ xốp TB | Phân bố tập trung trong dải **2.0 - 50.0nm** (mesopores). | Đường kính thô > 100nm (sụp đổ hệ xốp nhỏ). |
| **Raman** | Tỷ số defect carbon | Tỷ lệ cường độ đỉnh ***I*_D / *I*_G = 0.9 - 1.2** | *I*_D / *I*_G < 0.6 hoặc > 1.5. |
| **XRD** | Tinh thể carbon | Hai đỉnh nhiễu xạ góc tù, rộng tại **2θ ≈ 26.4^o** (002) và **43.5^o** (100) đại diện carbon bán tinh thể. | Xuất hiện các đỉnh nhiễu xạ sắc nhọn của α-Fe (44.7^o) hoặc Fe₃C (43.9^o) (Rửa axit thất bại). |
| **XPS Survey** | Hàm lượng nguyên tố bề mặt | Nitơ tổng đạt **3.0 - 6.0 at%**<br>Sắt tổng đạt **0.4 - 1.5 at%** | Nitơ < 2.0 at% (thiếu active sites) hoặc Sắt > 2.0 at% (thiếu phối trí). |
| **XPS Survey** | Tỉ lệ nguyên tố phối trí | Tỷ lệ nguyên tử **N:Fe ≥ 4:1** | Tỷ lệ N:Fe < 3:1. |
| **XPS N 1s** | Liên kết Nitơ phân giải cao | Đỉnh **Pyridinic-N** tại thế liên kết **≈ 398.2 eV** chiếm tỷ lệ diện tích ưu thế tối thiểu **≥ 45%** tổng phổ N 1s. | Pyridinic-N chiếm < 25% diện tích tách phổ. |
| **XPS Fe 2p** | Liên kết Sắt phân giải cao | Đỉnh đặc trưng liên kết **Fe-Nₓ** xuất hiện rõ nét trong khoảng thế liên kết **710.8 - 711.5 eV**. | Không có peak Fe-Nₓ, xuất hiện peak Fe kim loại tự do (707.0 eV). |

---

## PHẦN V: KIẾN NGHỊ VÀ DANH MỤC THAM CHIẾU HỆ THỐNG

### 1. Kiến nghị Cải tiến Hóa học Thực nghiệm
*   **Chuyển đổi trục dung môi:** Kiến nghị chuyển hẳn sang hệ NH₄OH-Urea làm trục chính chế tạo màng cảm biến điện hóa. Hệ dung môi kiềm cũ NaOH-Urea chỉ được duy trì làm mẫu đối chứng đo siêu tụ điện.
*   **Bắt buộc Acid Leaching đun hồi lưu:** Đối với điện cực phân tích nhạy dải vết (Pb²⁺), bắt buộc phải thực hiện bước leaching đun hồi lưu bằng HCl 0.5 M ở 80 °C trong 8 giờ và nung annealing lần 2 ở 800 °C trong 1 giờ để triệt tiêu hoàn toàn pha sắt tự do và oxit sắt thô, đảm bảo cấu trúc đơn nguyên tử Fe-N₄ tinh khiết.
*   **Hoạt hóa điện cực nền GCE:** Bắt buộc áp dụng bước anodize hóa học trong dung dịch NaOH 0.1 M ở thế +1.8 V vs. Ag/AgCl trong 10 giây để hòa tan sạch cặn alumina lưỡng tính bám dính cơ học, giải phóng hoàn toàn các khe nano hoạt tính của GCE.

### 2. Danh mục File Tham chiếu Hệ thống
*   Tài liệu `TOM_TAT_NTXPhuong.md` trong thư mục `08_Review_va_Tong_quan`.
*   Tài liệu `2 Nitrogen-Doped Carbon Aerogels Prepared by Direct Pyrolysis of.md` trong thư mục `02_Doping_va_Gel_hoa`.
*   Tài liệu `1 Facile Synthesis of Fe-Doped Algae Residue-Derived Carbon Aerogels for.md` trong thư mục `02_Doping_va_Gel_hoa`.
