# 1_Active_Protocol_Synthesis.md — Quy Trình Thực Nghiệm Chế Tạo Bột Carbon Aerogel Điện Hóa

> [!NOTE]
> * Luận án tham chiếu: Nguyễn Trần Xuân Phương 2024 (Tài liệu: `TOM_TAT_NTXPhuong.md` trong thư mục `08_Review_va_Tong_quan`).
> * Nghiên cứu cơ sở: Fauziyah et al. 2020 (Ind. Eng. Chem. Res.) (Tài liệu: `2 Nitrogen-Doped Carbon Aerogels Prepared by Direct Pyrolysis of.md` trong thư mục `02_Doping_va_Gel_hoa`).
> * Nghiên cứu gel hóa: Cai & Zhang 2006 (Biomacromolecules) (Tài liệu: `Unique Gelation Behavior of Cellulose in NaOH Urea Aqueous Solution.md` trong thư mục `08_Review_va_Tong_quan`).

---

## BẢNG CÂN BẰNG KHỐI LƯỢNG TỔNG THỂ (MASS BALANCE - Cơ sở: 100g xơ dừa khô)

Dưới đây là bảng cân bằng vật chất toàn diện từ 100g xơ dừa thô ban đầu để thu được ~9.5g Carbon Aerogel Fe-N (hoặc ~6.7g nếu có hoạt hóa KOH):

| Giai đoạn / Bước | Đầu vào (g) | Đầu ra (g) | Thất thoát (g) | Hiệu suất (%) | Vật liệu thu được | Nguyên nhân thất thoát / Ghi chú |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **GĐ0** – Nguyên liệu thô | 100 | 100 | 0 | 100.0% | Xơ dừa thô 100 g | Rửa sơ bộ loại bụi, cát |
| **GĐ1a** – Kiềm hóa NaOH | 100 | 75 | 25 | 75.0% | Xơ sau kiềm hóa ~75 g | Lignin mạch ngắn ~20g, tạp ~5g tan trong kiềm |
| **GĐ1b** – Tẩy trắng H₂O₂ | 75 | 62 | 13 | 82.7% | Xơ tẩy trắng ~62 g | Loại tiếp lignin còn lại ~10g, sáp ~3g |
| **GĐ1c** – Thủy phân HCl | 62 | 38 | 24 | 61.3% | Cellulose tinh khiết ~38 g | Hòa tan hemicellulose ~20g, tro ~4g |
| **-> TỔNG CỘNG GĐ1** | **100** | **38** | **62** | **38.0%** | **Cellulose tinh khiết ~38 g** | **Hiệu suất tiền xử lý tổng thể** |
| **GĐ2** – Sol-gel NaOH/Urea | 38 | 36.1 | 1.9 | 95.0% | Hydrogel khô ~36.1 g | Cellulose không tan dư ~5% (~1.9g) bị lọc bỏ |
| **GĐ3** – Doping Fe-N | 36.1 | 39.2 | -3.1 (tăng) | 108.6% | Gel sau doping ~39.2 g | Khối lượng tăng do phức Fe và N hấp thụ vào gel |
| **GĐ4** – Sấy dung môi | 39.2 | 37 | 2.2 | 94.4% | Aerogel xanh ~37.0 g | Dung môi bay hơi hoàn toàn, co ngót nhẹ |
| **GĐ5** – Carbon hóa 600°C | 37 | 9.5 | 27.5 | 25.7% | Carbon Aerogel ~9.5 g | Bay hơi khí H2O, CO2, CO, HCN, VOCs |
| **GĐ6*** – Hoạt hóa KOH (tùy chọn) | 9.5 | 6.7 | 2.8 | 70.5% | Activated CA ~6.7 g | KOH gasification ăn mòn một phần carbon (~30%) |

---

## GIAI ĐOẠN 0: TIỀN XỬ LÝ KIỀM HÓA TÁCH LIGNIN (Delignification Pretreatment)

> [!IMPORTANT]
> **⚠️ Ràng buộc định hướng Điện hóa & Cảm biến (No Bleaching):** 
> Trái với hướng hấp phụ chất màu/dầu của hệ xenluloza tinh khiết (cần tẩy trắng để thu sợi trắng BCF), đối với hướng **Điện cực cảm biến điện hóa (carbon aerogel)**, quy trình thực nghiệm **tuyệt đối không tẩy trắng bằng H₂O₂/NaClO₂ và không thủy phân acid mạnh bằng HCl**. 
> *   *Lý do 1 (Bảo toàn cấu trúc 3D):* Chất tẩy trắng và acid mạnh cắt đứt mạch xenluloza làm giảm độ trùng hợp (DP), khiến vách ống tế bào xơ dừa bị mỏng yếu và dễ sụp đổ khi nhiệt phân cao tần (pore collapse).
> *   *Lý do 2 (Giữ lại dị nguyên tố tự nhiên):* Giữ nguyên cấu trúc thô bán tinh thể giúp lưu giữ các dị tố hữu cơ tự nhiên có sẵn trong xơ dừa, hỗ trợ đắc lực cho quá trình tự doping nitơ và phối trí kim loại sắt (Fe) tạo active sites.
> Do đó, xơ dừa sau kiềm hóa thu được bột **DCF (Delignified Coir Fiber)** có màu nâu nhạt sẽ được dùng trực tiếp để làm sol-gel.

### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1. Chuẩn bị xơ dừa xay nghiền, rây lấy kích thước hạt < 100 mesh (~150 µm) để tăng diện tích tiếp xúc kiềm (tham chiếu: Cellulose Extraction from Coconut Coir with Alkaline Delignification Process, thư mục 01_Tien_xu_ly_Nguyen_lieu, hướng trích ly cellulose bằng kiềm), sấy khô ở 80 °C trong 24 giờ.
2. Ngâm 50 g bột xơ dừa khô trong 1000 mL nước nóng (80 °C) trong 4 giờ dưới lực khuấy từ 600 rpm để rửa sạch bụi bẩn và sáp cơ học. Lọc qua phễu Buchner.
3. Cho bã xơ dừa vào bình tam giác 1000 mL chứa dung dịch **NaOH 6 wt%** (pha 60 g NaOH rắn trong 1000 mL nước cất DI, tỷ lệ rắn/lỏng = 1:20 w/v).
4. Duy trì nhiệt độ ở **80 ± 2 °C** trong **4 giờ** liên tục, tốc độ khuấy 600 rpm (tham chiếu: Cellulose Extraction from Coconut Coir with Alkaline Delignification Process, thư mục 01_Tien_xu_ly_Nguyen_lieu, hướng trích ly cellulose bằng kiềm). Bọc kín miệng bình bằng màng PP chịu nhiệt.
5. Lọc bã qua phễu Buchner. Rửa bằng nước cất DI nóng (60 °C) đến khi pH trung tính (pH = 6.5–7.0).
6. Sấy khô bột ở 80 °C trong 12 giờ thu được bột xơ dừa kiềm hóa **DCF**. Cân xác định hiệu suất hao hụt khối lượng (**Gravimetric Weight-loss %**).

### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Hiệu suất hao hụt khối lượng DCF:** Phải nằm trong dải **30%–38%** (xác nhận loại bỏ lignin thành công).
*   **Đường kính sợi (SEM):** Đạt kích thước **20–50 µm** (lộ cấu trúc cellulose hình ống sần sùi).
*   **Độ tinh thể hóa (XRD):** Đạt **≥ 55%** (Xuất hiện các đỉnh đặc trưng của Cellulose I tại góc quét 2θ ≈ 16.08° (110) và 22.23° (200)).
*   **Hàm lượng cellulose bề mặt:** Đạt **≥ 69.8 wt%** (FT-IR giảm >90% đỉnh ester tại 1735 cm⁻¹, xuất hiện peak dao động kéo giãn C-O-C ở 1050 cm⁻¹).

---

## GIAI ĐOẠN 1: TỔNG HỢP SOL & PHỐI TRỘN DUNG MÔI (Sol Preparation)

### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
*   **Công thức A: Hệ Ammonia-Urea (Hệ chính chế tạo màng Cảm biến & ORR)**
    1. Công thức định lượng: **1.0 g Cellulose DCF + 11.0 mL NH₄OH (25 wt%) + 4.0 g Urea tinh thể + 5.0 mL nước cất DI** (Tổng thể tích dung môi = 16.0 mL).
    2. Hòa tan hoàn toàn 4.0 g Urea vào hỗn hợp NH₄OH và nước cất DI trong bình phản ứng Teflon đậy kín miệng.
    3. Thêm từ từ 1.0 g bột DCF vào bình dung môi, khuấy nhẹ cho ngấm đều.
    4. Đặt bình vào bể siêu âm. **Bắt buộc:** Đổ đầy đá và nước để duy trì nhiệt độ bể **≤ 10 °C (tối ưu 0 - 5 °C)**.
    5. Thiết lập siêu âm xung (**2 giây ON / 1 giây OFF**) liên tục trong **30 phút** ở công suất trung bình.
    6. Thu được hệ sol (huyền phù keo) màu hơi đục nhẹ, phân tán đều.
*   **Công thức B: Hệ Sodium-Urea (Hệ đối chứng dùng cho Siêu tụ điện)**
    1. Công thức định lượng: **1.0 g bột DCF + 16.0 g dung dịch kiềm** (7 wt% NaOH : 12 wt% Urea : 81 wt% H₂O).
    2. Hòa tan NaOH và Urea vào nước cất. Làm lạnh dung dịch kiềm về **-10 °C đến -12 °C** trong tủ đông sâu đến trạng thái bán đông băng (slushy).
    3. Cho nhanh 1.0 g bột DCF vào dung môi lạnh, khuấy từ tốc độ cao 3000 rpm trong **5 phút** ở nhiệt độ phòng. Thu được hệ sol trong suốt.

### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Trạng thái Sol:** Hệ huyền phù keo phân tán đồng đều, không bị lắng cặn hay vón cục sợi lớn.
*   **Nhiệt độ bể siêu âm hệ NH₄OH:** Khống chế nghiêm ngặt **≤ 10 °C**. Nếu nhiệt độ bể >15 °C gây hỏng sol (Fail).
*   **XRD của hydrogel sau đông tụ:** Giản đồ XRD xuất hiện hai đỉnh đặc trưng của Cellulose III tại góc 2θ ≈ 11.6° (110) và 20.5° (002).

### 3. Cơ chế phân tán và vai trò của Urea (Dispersion Mechanism & Urea Role)
*   **Amoniac (NH₄OH):** Đóng vai trò là tác nhân trương nở mạnh. Các ion NH₄⁺ và OH⁻ thâm nhập vào các vùng vô định hình và bán tinh thể của cellulose, cắt đứt các liên kết hydro liên phân tử và nội phân tử bền vững của cellulose nguyên bản.
*   **Urea:** Đóng vai trò là "lá chắn sơ thủy" (hydrophobic shield) và chất ổn định mạng lưới. Khi xơ dừa bị trương nở dưới tác động của kiềm, các mặt kỵ nước của mạch cellulose lộ ra ngoài. Urea tự lắp ghép xung quanh các bề mặt kỵ nước này thông qua tương tác van der Waals, ngăn không cho các mạch cellulose tái tổ hợp và kết tụ lại với nhau. Đồng thời, urea tạo liên kết hydro mới với các nhóm hydroxyl của cellulose, duy trì trạng thái phân tán bền vững trong hệ sol (huyền phù keo).

---

## GIAI ĐOẠN 2: ĐÚC KHUÔN PP & GIÀ HÓA NHIỆT HÌNH THÀNH HYDROGEL (Casting & Gelation)

### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Đúc khuôn:** Rót từ từ sol đã hòa tan vào ống tiêm Polypropylene (PP) đã cắt bỏ đầu kim để làm khuôn đúc monolith.
2.  **Khử bọt khí (De-gassing):** Đặt đứng ống tiêm chứa sol ở nhiệt độ ngăn mát tủ lạnh ở **0 - 5 °C trong thời gian 30 - 60 phút** để bọt khí thoát ly hoàn toàn ra ngoài và ổn định hệ sol.
3.  **Đông lạnh tạo gel (Frozen Gelation / Cryo-concentration):** Bọc kín hai đầu ống tiêm đúc khuôn.
    *   *Đối với hệ NH₄OH-Urea (Chính):* Đặt tĩnh ống tiêm đúc khuôn trong ngăn đông tủ lạnh ở **-5 °C trong 24 giờ** để xảy ra quá trình đông lạnh tạo gel (frozen gelation). Sau đó, lấy khối gel ra ngoài và để rã đông tự nhiên ở nhiệt độ phòng (25 - 30 °C).
    *   *Đối với hệ đối chứng NaOH-Urea:* Lấy sol từ tủ đông sâu ra rã đông ở nhiệt độ phòng. Rót sol vào khuôn, sau đó thả khuôn chứa sol vào bình chứa cồn **Ethanol 96% đun nóng ở 70 °C duy trì trong 1.5 - 2 giờ** để kích hoạt phản ứng đông tụ gel hóa nhanh (`EtOH 96°, 70 °C Gel hoá`).
4.  Dùng pít-tông nhẹ nhàng đẩy khối hydrogel đã định hình ra ngoài.

### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Hình thái Hydrogel:** Khối hydrogel monolith trụ nhẵn bóng, dẻo dai, đàn hồi tốt, hoàn toàn không bị nứt vỡ cơ học, móp méo hay rỗng ruột bọt khí.
*   **Tính ổn định:** Đứng vững trên mặt phẳng phẳng, ẩm đồng đều.

### 3. Cơ chế đông lạnh tạo gel (Frozen Gelation Mechanism)
*   **Hiệu ứng tích tụ đông băng (Cryo-concentration):** Khi hạ nhiệt độ xuống −5 °C, nước trong hệ sol bắt đầu kết tinh thành các tinh thể đá tinh khiết. Sự phát triển của tinh thể đá đẩy cellulose, amoniac và urea vào các kênh chất lỏng hẹp chưa đông băng giữa các tinh thể đá.
*   **Tái sắp xếp mạch cellulose:** Dưới áp lực nén ép vật lý của tinh thể đá và nồng độ cellulose tăng cao trong các kênh lỏng, các mạch cellulose bị ép lại gần nhau. Urea tiếp tục che chở các bề mặt kỵ nước, trong khi amoniac bay hơi một phần hoặc khuếch tán ra ngoài làm giảm khả năng hòa tan cục bộ. Khi rã đông ở nhiệt độ phòng, các mạch cellulose tiếp xúc gần sẽ tự phát liên kết lại với nhau thông qua mạng lưới liên kết hydro chằng chịt, tạo nên cấu trúc gel 3D vật lý dẻo dai và ổn định, giam giữ nước bên trong các mao quản rộng.

---

## GIAI ĐOẠN 3: KEO TỤ & TẨM ĐỐP Fe TÂM HOẠT TÍNH (Coagulation & Fe Impregnation)

### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Keo tụ & Trao đổi dung môi (Coagulation & Solvent Exchange):**
    *   *Đối với hệ NH₄OH-Urea (Chính):*
        *   **Keo tụ (Coagulation):** Thả khối hydrogel đã rã đông vào bình chứa cồn **Ethanol 98% ở nhiệt độ phòng (25 - 30 °C)** với tỷ lệ tối thiểu **15 mL ethanol / 1 g cellulose** ban đầu. Đậy kín nắp và ngâm tĩnh ở nhiệt độ phòng trong **24 giờ** để đông tụ và cố định cấu trúc mạng lưới cellulose III.
        *   **Trao đổi dung môi ngược (Solvent Exchange):** Gạn bỏ cồn cũ, ngâm rửa gel bằng nước cất DI sạch (gấp 5 lần thể tích gel) ở nhiệt độ phòng trong **2 giờ**, lặp lại **chính xác 2 lần** để rửa sạch cồn và amoniac tự do, thay thế hoàn toàn cồn bằng nước DI trong mạng mao quản.
        > [IMPORTANT]
        > **⚠️ Cảnh báo sấy & rửa ngược:** Bắt buộc phải trao đổi ngược từ cồn sang nước DI trước khi sấy thăng hoa vì Ethanol có điểm đông đặc cực thấp (-114 °C) không thể đông băng ở nhiệt độ tủ sấy (-20 °C hay -80 °C), dẫn đến hiện tượng sôi dung môi làm sập cấu trúc gel (collapse) dưới áp suất chân không. Tuy nhiên, tuyệt đối không rửa nước DI quá 4 lần hoặc ngâm kéo dài >12 giờ để tránh làm trôi bộ Urea tự do bám trong gel (nguồn N-doping duy nhất).
    *   *Đối với hệ đối chứng NaOH-Urea:*
        *   **Rửa trung hòa:** Ngâm rửa khối gel trong bể nước cất DI lớn ở nhiệt độ phòng, thay nước sạch sau mỗi 2 - 4 giờ **cho đến khi nước rửa đạt pH trung tính hoàn toàn (pH ≈ 7)** để loại bỏ toàn bộ NaOH và urea tự do dư thừa bám dính.
        > [WARNING]
        > **⚠️ Cấm cặn kiềm:** Bắt buộc phải rửa trung hòa đến pH ≈ 7 để loại bỏ hoàn toàn các ion Na⁺. Nếu còn cặn kiềm NaOH trong mạng gel, khi nhiệt phân ở 800 °C sẽ xảy ra phản ứng ăn mòn hóa học kiềm cực mạnh (Alkaline/Na-etching), phá hủy hoàn toàn vách tế bào carbon và làm sập cấu trúc mao quản, dẫn đến diện tích bề mặt sụt giảm nghiêm trọng (*S*_BET ≤ 150 m²/g).
        *   **Tạo liên kết TEPA (Đối với mẫu NUTA):** Ngâm khối gel đã rửa trung hòa vào dung dịch **TEPA : EtOH : H₂O (tỷ lệ 2:5:3 v/v)** ở nhiệt độ phòng trong **24 giờ** để tạo liên kết ngang hóa học cố định cấu hình chứa N.
2.  **Tẩm sắt Fe Impregnation (Dành cho nhánh mẫu Fe/N-CA):**
    *   **Công thức định lượng & Tính toán (Molar & Weight Calculations):**
        *   Lượng tiền chất FeCl₃·6H₂O được tính toán chính xác để đạt hàm lượng Fe mục tiêu là 10 wt% so với khối lượng cellulose DCF khô ban đầu (1.0 g):
            m_FeCl₃·6H₂O = m_cellulose × 10% × (M_FeCl₃·6H₂O / M_Fe)
                         = 1.0 g × 0.10 × (270.3 g/mol / 55.845 g/mol)
                         ≈ 0.484 g
        *   Hòa tan hoàn toàn 0.484 g FeCl₃·6H₂O và 1.0 g Urea vào 30 mL nước cất DI lạnh (0 - 5 °C) trong bình Teflon tối màu quấn Parafilm. 
        *   *(Vai trò của 1.0 g Urea thêm vào dung dịch tẩm: Hoạt động như một phối tử nitrogen tự do hỗ trợ chelate hóa tạm thời ion Fe³⁺, ngăn ngừa sự thủy phân sớm tạo kết tủa Fe(OH)₃ hoặc Fe₂O₃ thô khi tiếp xúc với lượng amoniac tàn dư trong gel, đảm bảo Fe phân tán ở cấp độ phân tử).*
        *   **Bảng ma trận ngâm tẩm khảo sát hàm lượng Doping (Thể tích dung dịch ngâm chuẩn: 2040 mL):**
            
            | Tên Mẫu | Tỷ lệ Fe mục tiêu | Khối lượng Fe cần ngấm | Muối FeCl3.6H2O cần cân | Urea (nguồn N) cần cân | Nồng độ FeCl3 trong bể ngâm | Vai trò thực nghiệm |
            | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
            | **Fe5N-CA** | 5 wt.% | 1.8 g | **10.5 g** *(đã dư 20%)* | 7.2 g | 4.3 g/L (~0.016 M) | Mẫu nồng độ thấp (đối chứng) |
            | **Fe10N-CA** | **10 wt.%** | **3.6 g** | **20.9 g** *(đã dư 20%)* | **7.2 g** | **8.5 g/L (~0.031 M)** | **Mẫu tối ưu (Sweet spot)** |
            | **Fe15N-CA** | 15 wt.% | 5.4 g | **31.4 g** *(đã dư 20%)* | 7.2 g | 12.7 g/L (~0.047 M) | Mẫu nồng độ cao (dễ bị vón hạt) |
    *   **Quy trình thao tác chi tiết:**
        *   Thả nhẹ nhàng khối hydrogel NH₄OH-Urea đã keo tụ và rửa ngược (đã ráo nước bề mặt) vào dung dịch tẩm sắt.
        *   Đặt bình chứa vào bể siêu âm nước đá, duy trì nhiệt độ < 10 °C và tiến hành siêu âm nhẹ ở công suất thấp (hoặc chế độ rung rửa) trong 30 phút để kích hoạt động học trao đổi chất, mở rộng các lỗ mao quản cho ion Fe³⁺ thâm nhập nhanh.
        *   Chuyển bình chứa vào tủ mát ở nhiệt độ ổn định 4 °C (0 - 5 °C) và ngâm tĩnh liên tục trong 24 giờ để ion Fe³⁺ khuếch tán bão hòa tuyệt đối và đồng đều từ lớp vỏ ngoài đi sâu vào tận tâm lõi của khối hydrogel monolith xốp.
    *   **Cơ chế liên kết neo giữ ligand (Ligand-anchoring Mechanism):**
        *   Các ion sắt Fe³⁺ phân tán trong lòng gel sẽ tương tác mạnh với các nhóm chức giàu điện tử tự do (-OH của cellulose và -NH₂ của urea/amonia liên kết vật lý bám trong vách gel) đóng vai trò như các phối tử (ligands).
        *   Sự phối trí này hình thành các liên kết chelating phức chất nội cấu trúc bền vững. Liên kết giữ ion Fe³⁺ này cực kỳ quan trọng, giữ cho các nguyên tử sắt bị "khóa cứng" biệt lập trên các chuỗi cellulose và không bị tụ tập lại với nhau trong quá trình nung. Khi carbon hóa ở 800 °C, các nguyên tử sắt đơn lẻ này sẽ phối trí trực tiếp với các nguyên tử nitrogen sinh ra từ sự phân hủy urea để hình thành các tâm hoạt tính đơn nguyên tử **Fe-N₄ (single-atom sites)** siêu bền và hoạt động cao.
    *   **Chỉ tiêu kiểm soát (Pass/Fail):** Khối hydrogel sau 24h tẩm phải chuyển hẳn sang **màu nâu đỏ/vàng cam đồng đều** hoàn toàn từ vỏ vào lõi, không có vệt loang màu trắng đục tàn dư. Khối gel giữ nguyên hình dáng, không bị nứt vỡ hay nhão cơ học.

---

### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Màu sắc hydrogel sau tẩm:** Khối hydrogel N-CA ẩm có màu trắng đục nhẹ đồng đều. Khối hydrogel Fe/N-CA ẩm phải chuyển sang **màu nâu đỏ/vàng cam đồng đều** hoàn toàn từ vỏ ngoài vào tận lõi gel (không bị loang lổ).

---

## GIAI ĐOẠN 4: SẤY THĂNG HOA BẢO TOÀN CẤU TRÚC MAO QUẢN (Freeze Drying)

### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Cấp đông sâu siêu tốc:** Đặt các khối gel ẩm sau tẩm vào tủ đông siêu sâu duy trì ở nhiệt độ **80 °C** hoặc nhúng trực tiếp khối gel vào bình chứa Nitơ lỏng (LN₂, 196 °C) trong **5 phút**.
2.  **Sấy thăng hoa chân không:**
    *   Khởi động máy sấy thăng hoa đảm bảo bẫy lạnh đạt **≤ 50 °C** (tối ưu 80 °C) và áp suất chân không **< 20Pa (0.15 Torr)**.
    *   Xếp các mẫu gel đông băng vào buồng sấy. Duy trì sấy thăng hoa liên tục trong **36 - 48 giờ** đến khối lượng mẫu không đổi.
3.  Thu hồi aerogel xốp dẻo siêu nhẹ. Đo kích thước để tính độ co ngót.

### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Độ co ngót tuyến tính (Linear Shrinkage %):** Phải đạt chỉ số **Linear Shrinkage < 12%** tính theo công thức:
    *   **Công thức tính:** Shrinkage % = (D_gel - D_aerogel) / D_gel × 100%
    *   ✓ **Pass:** Shrinkage < 12%.
    *   ✗ **Fail:** Shrinkage ≥ 20% (cấu trúc mạng mao quản bị sụp đổ).
*   **Khối lượng riêng thể tích (Bulk density):** Phải duy trì trong dải **0.03 - 0.05 g/cm³**.

---

## GIAI ĐOẠN 5: NHIỆT PHÂN CARBON HÓA LẦN 1 & DOPING NITƠ (First Pyrolysis & N-doping)

### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Chuẩn bị:** Xếp các khối aerogel khô vào thuyền sứ sạch, đẩy vào trung tâm lò nung ống thạch anh.
2.  **Purge đuổi Oxy bảo vệ:** Thổi dòng khí N₂ tinh khiết (99.99%) với lưu lượng **150 - 200 mL/phút trong 30 phút** trước khi gia nhiệt. Duy trì dòng khí N₂ bảo vệ ổn định ở lưu lượng **100 mL/phút** suốt quá trình nung.
3.  **Chương trình nhiệt phân 3 Ramp (Gia nhiệt 5 °C/phút):**
    *   *Ramp 1 (Sấy ẩm sâu):* Nâng từ 25 °C → 150 °C, giữ nhiệt **30 phút**.
    *   *Ramp 2 (Phân hủy hữu cơ thô):* Nâng từ 150 °C → 400 °C, giữ nhiệt **30 phút**.
    *   *Ramp 3 (Carbon hóa sâu & Doping):* Nâng từ 400 °C → T_target, giữ nhiệt liên tục trong **2 giờ (120 phút)**.
    *   *Nhiệt độ mục tiêu (T_target):*
        *   **Nhánh mẫu N-CA:** Chọn **T_target = 700 °C**.
        *   **Nhánh mẫu Fe/N-CA (nền):** Chọn **T_target = 800 °C**.
4.  **Làm nguội:** Tắt gia nhiệt, để lò nguội tự nhiên dưới dòng khí N₂ bảo vệ. Lấy mẫu ra ngoài khi nhiệt độ đầu đo đạt **< 50 °C**.

### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Trạng thái vật liệu:** Khối carbon aerogel thu được phải có **màu đen tuyền**, xốp, giữ nguyên hình monolith trụ ban đầu. Bulk density đạt **0.05 g/cm³ (NH₃-Urea)** hoặc **0.07 g/cm³ (NaOH-Urea)**.
*   **Độ bền cơ học:** Ép nén đạt Young Modulus ổn định từ **6.43kPa (N-CA)** đến **138.59kPa (Fe/N-CA)**.

---

## GIAI ĐOẠN 6: RỬA AXIT & ANNEALING LẦN 2 TẠO TÂM Fe-N₄ SIÊU SẠCH (Acid Leaching & Re-annealing)

### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Phản ứng Acid Leaching đun hồi lưu:**
    *   Sử dụng dung dịch **HCl 0.5 M** làm tác nhân hòa tan.
    *   Cho bột Fe/N-CA nung lần 1 vào bình cầu chứa HCl 0.5 M với tỷ lệ **1 g bột / 100 mL dung dịch**.
    *   Lắp hệ thống sinh hàn hồi lưu và đặt trên bếp khuấy từ đun sôi nhẹ ở nhiệt độ **80 ± 2 °C liên tục trong 8 giờ** (khuấy nhẹ 200 rpm).
2.  **Lọc rửa trung hòa:** Lọc chắt bột qua phễu lọc chân không Buchner dùng giấy lọc sợi thủy tinh. Rửa liên tục bằng nước cất DI nóng (60 °C) cho đến khi nước rửa đạt pH ≈ 7.0 hoàn toàn. Sấy khô bột ở 80 °C trong 12 giờ.
3.  **Annealing tái hoạt hóa lần 2:**
    *   Đặt bột sấy khô vào lò nung ống thạch anh. Purge khí N₂ tương tự Giai đoạn 5.
    *   Thiết lập chương trình gia nhiệt 5 °C/phút lên đúng nhiệt độ mục tiêu **800 °C và giữ nhiệt chính xác trong 1 giờ (60 phút)** dưới dòng khí N₂ bảo vệ (100 mL/phút).
    *   Để lò nguội tự nhiên về < 50 °C dưới dòng khí bảo vệ. Bảo quản bột trong vial thủy tinh tối màu quấn Parafilm cất ở tủ mát **4 °C**.

### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **XRD kiểm tra pha tinh thể sắt:** Giản đồ XRD của bột Fe/N-CA sau annealing lần 2 phải **hoàn toàn sạch**, biến mất toàn bộ các đỉnh nhiễu xạ của sắt kim loại α-Fe (2θ ≈ 44.7°) và sắt carbide Fe₃C (2θ ≈ 43.9°).
    *   ✓ **Pass:** Fe phân tán đơn nguyên tử tuyệt đối (single-atom).
    *   ✗ **Fail:** Vẫn xuất hiện đỉnh sắt tinh thể thô (quá trình leaching chưa triệt để).
*   **Hàm lượng nguyên tố bề mặt (XPS):** Sắt đạt **0.4 - 1.5 at%** và Nitơ đạt **3.0 - 6.0 at%** với tỷ lệ tối thiểu N:Fe ≥ 4:1.

---

## PHẦN BỔ SUNG LÝ THUYẾT: CƠ CHẾ DOPING, HOẠT HÓA & THIẾT KẾ LỖ XỐP PHÂN CẤP

### 1. Cơ chế pha tạp dị nguyên tử Nitơ (N-doping configuration)
Việc pha tạp Nitơ (N) vào mạng carbon tạo ra các cấu hình dị nguyên tử có hoạt tính điện hóa đặc trưng:
*   **Pyridinic-N (N-6):** Nguyên tử N nằm ở các khuyết tật mép vòng, phối trí với 2 nguyên tử C lân cận. Bản chất Lewis base của cặp electron tự do trên Pyridinic-N đóng vai trò là **tâm hoạt tính (active sites)** tối ưu để chelate hóa cation kim loại Pb²⁺, Cd²⁺, Zn²⁺ trong quá trình làm giàu stripping, đồng thời giảm thế quá phân cực.
*   **Pyrrolic-N (N-5):** Nằm trong vòng 5 cạnh nhạy cảm, đóng góp 2 electron liên hợp tạo ra điện dung giả Faradaic, nâng cao độ bền của màng sửa đổi.
*   **Graphitic-N (Quaternary-N):** Thay thế trực tiếp nguyên tử C ở trung tâm mạng lưới phẳng sp², giải phóng electron tự do vào dải dẫn giúp **tăng vọt độ dẫn điện** của điện cực.

### 2. Kỹ thuật thiết kế lỗ xốp phân cấp (Hierarchical Porosity Design)
*   **Cơ chế đúc băng (Ice-Templating):** Quá trình cấp đông định hướng ở −20°C hình thành các tinh thể đá rỗng dọc theo chiều hướng nhiệt. Khi sấy thăng hoa chân không ở áp suất < 20 Pa, các tinh thể đá thăng hoa trực tiếp để lại hệ thống **lỗ xốp lớn (macropores > 50 nm)** liên thông nhau, đóng vai trò là các "bể chứa ion" dung dịch (electrolyte reservoirs).
*   **Cơ chế sinh khí tự hoạt hóa (Gas Evolution):** Quá trình nhiệt phân cellulose tạo khí CO, CO₂ làm nứt vỡ vách tế bào polymer đang carbon hóa, tạo thêm các **lỗ xốp trung bình (mesopores 2 - 50 nm)** đóng vai trò như các "đường cao tốc" hỗ trợ khuếch tán nhanh ion đến bề mặt làm việc mà không gặp trở lực cơ học.
