# 3_Literature_Review_and_Gap_Analysis.md — Đối Chiếu Tài Liệu & Giải Quyết Lỗ Hổng Thực Nghiệm (Gap Analysis)

<!-- v2.0 | Chuẩn hóa: 2026-05-31 | Merge từ: 3_Literature_Review_and_Gap_Analysis gốc + synthesis_outline_verified Phần 1 -->

> [!NOTE]
> * **Nghiên cứu cơ sở:** Fauziyah et al. 2020 (doi:10.1021/acs.iecr.0c03771).
> * **Nghiên cứu GCE biến tính:** Wu et al. 2024 (doi:10.3390/s24092787).
> * **Quy trình liên kết thực tế:** [1_Protocol_Synthesis.md](file:///d:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/1_Protocol_Synthesis.md), [2_Protocol_Electrochemistry.md](file:///d:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/2_Protocol_Electrochemistry.md), [4_Material_Characterization.md](file:///d:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/4_Material_Characterization.md)

---

## 1. SO SÁNH ĐỐI CHỨNG HỆ DUNG MÔI: NH₄OH/UREA VS. NAOH/UREA

Bảng so sánh đối chứng thông số vật lý và hoạt tính điện hóa sau nung giữa hai hệ dung môi chế tạo aerogel từ cellulose xơ dừa:

| Chỉ số vật lý & điện hóa | Hệ dung môi chính NH₄OH-Urea (Chế tạo màng cảm biến) | Hệ dung môi đối chứng NaOH-Urea (Đo siêu tụ điện) |
| :--- | :--- | :--- |
| **Pha tinh thể Cellulose ẩm** | Cellulose III | Cellulose II |
| **Pha tinh thể sau nung** | Carbon bán tinh thể sp² graphitized | Carbon vô định hình bị ăn mòn kiềm mạnh |
| **Trạng thái bay hơi dung môi** | Bay hơi 100% (amoniac thoát ly hoàn toàn) | Không bay hơi (cặn ion $Na^+$ bám dính gel) |
| **Diện tích bề mặt riêng ($S_{\text{BET}}$)** | **$> 300\text{ m}^2\text{/g}$** (Mục tiêu tối ưu $\ge 370\text{ m}^2\text{/g}$, cấu trúc lá tổ ong siêu mỏng) | **$\le 150\text{ m}^2\text{/g}$** (vách lỗ xốp bị ăn mòn sụp đổ) |
| **Độ dẫn điện màng sau nung** | **5.08 S/cm** | **0.93 S/cm** |
| **Hiệu ứng ở nhiệt độ cao (800 ℃)**| Tự bóc tách các lớp carbon tạo khuyết tật mạng (N-doping) | Ăn mòn hóa học vách tế bào gây sập mao quản (Na-etching) |
| **Ứng dụng điện hóa tối ưu** | **Cảm biến màng mỏng dải vết** (truyền điện tích nhanh) | **Siêu tụ điện tích lũy lớp kép (EDLC)** trong KOH 6.0 M |

---

## 2. MA TRẬN GIẢI QUYẾT 10 LỖ HỔNG THỰC NGHIỆM (Gap Analysis G1 - G10)

Bảng tổng hợp các thông số kỹ thuật đối chứng và giải pháp tối ưu hóa nhằm khắc phục 10 lỗi thực nghiệm thường gặp trong các nghiên cứu trước:

| Lỗ hổng kỹ thuật | Mã số | Thông số lỗi thường gặp (Nghiên cứu cũ) | Thông số kỹ thuật tối ưu hóa đạt chuẩn (SOP hiện tại) |
| :--- | :---: | :--- | :--- |
| **Kiểm soát Delignification** | **G1** | Chỉ ngâm kiềm thô hoặc rửa cơ học không kiểm soát, lignin còn bám dính gây cản sol-gel hóa. | Thực hiện **NaOH 6 wt% ở 80 ± 2 ℃ trong 4 giờ, tỷ lệ 1 g : 20 mL (40.0 g xơ dừa : 800 mL NaOH 6 wt% pha từ 48 g NaOH và 752 mL nước DI)**; kiểm soát hiệu suất hao hụt khối lượng khô DCF **30% - 38%**. |
| **Khuôn đúc hydrogel** | **G2** | Dùng khuôn thủy tinh hoặc ống cứng gây bám dính cơ học, mẻ đầu monolith bị nứt vỡ khi tháo khuôn. | Sử dụng **khuôn làm bánh flan/cupcake bằng Silicone dẻo** (~60-70 mL). Bóp nhẹ viền khuôn, úp ngược để gel trượt ra nhẹ nhàng mà không chạm tay. |
| **Thời gian ổn định Sol** | **G3** | Đúc khuôn già hóa nhiệt ngay sau siêu âm gây bọt khí kẹt trong monolith tạo rỗng xốp lỗi. | Gõ nhẹ đáy khuôn đuổi bọt, đặt tĩnh sol ở **0 - 5 ℃ trong 15 - 30 phút** (de-gassing + cân bằng nhiệt đồng đều). |
| **Tỷ lệ co rút thể tích** | **G4** | Co ngót tuyến tính >20% gây sập vách, co rúm và sụp đổ cấu trúc aerogel sau sấy chân không. | Rã đông gel trong khuôn 1h ở RT, gạn bớt dung dịch lớp trên, trượt gel vào **Ethanol 96-98% ở 25 ± 2 ℃ với tỉ lệ 10:1 (v/v) so với dung môi gel (~200 mL cồn cho mẻ 1g DCF)** trong 24 giờ để keo tụ bền vững, khống chế **Linear Shrinkage < 12%**. |
| **Thời gian ngâm tẩm Sắt**| **G5** | Ngâm muối sắt $FeCl_3$ quá ngắn (<4 giờ) gây nghèo hoạt chất lõi, sắt tập tụ thô ngoài rìa. | Siêu âm nhẹ 30 phút + ngâm tĩnh **24 giờ ở 25 ± 2 ℃ (nhiệt độ phòng)** để ion $Fe^{3+}$ khuếch tán bão hòa đều lõi. |
| **Nhiệt độ ngâm tẩm Fe** | **G6** | Ngâm tẩm sắt ở nhiệt độ cao (>40 ℃) làm bay hơi dung môi, thay đổi nồng độ tẩm bất ngờ. | Duy trì ngâm tẩm tĩnh ở **25 ± 2 ℃ (nhiệt độ phòng)** liên tục trong 24 giờ. Tuyệt đối không vượt 40 ℃. |
| **Lựa chọn Acid Leaching** | **G7** | Sử dụng axit $H_2SO_4$ loãng/nóng gây sulfon hóa bề mặt carbon, bít tắc mesopores màng. | Dùng **HCl 0.5 M đun hồi lưu ở 80 ± 2 ℃ trong 8 giờ** (hòa tan sắt tự do, trơ mạng carbon sp²). |
| **Nhiệt độ Annealing 2** | **G8** | Bỏ qua bước nung lần 2 hoặc nung nhiệt độ thấp gây sập cấu trúc khuyết tật hoặc thiêu kết. | Nung re-anneal ở **750 ℃ trong 1 giờ** dưới dòng khí $N_2$ (100 mL/phút) để cố định cấu hình tâm **$Fe-N_4$** (đã chốt 2026-05-31, thấp hơn 50 ℃ so với nung lần 1 để tránh sập mao quản thêm). |
| **Chất liên kết Ink GCE** | **G9** | Sử dụng keo bám dính không phân tách, gây nhiễu dòng Faraday hoặc làm tăng điện trở màng mỏng. | Phân tách chuyên biệt: **Chitosan 1%** (cho Pb²⁺ SWASV chelate) và **Nafion 0.25%** (cho Paracetamol DPV chống bám bẩn). |
| **Sự khác biệt dung môi** | **G10** | Dùng hệ NaOH-Urea chế tạo màng cảm biến gây dòng yếu, trở kháng lớn do sập cấu trúc mao quản. | **Hệ NH₄OH-Urea** làm trục chính màng cảm biến (*S*_BET $> 300\text{ m}^2\text{/g}$). Hệ NaOH chỉ làm tụ điện. |

---

## 3. DOI MAPPING BẢN ĐỒ TÀI LIỆU KHẢO SÁT CHÍNH XÁC (9 GIAI ĐOẠN)

Dưới đây là bảng ánh xạ các bài báo tiêu biểu trong Digital Library làm cơ sở lý thuyết cho từng giai đoạn của quy trình:

| Giai đoạn | Nội dung kỹ thuật | Tài liệu tham khảo tiêu biểu | Mã số DOI / URL |
| :--- | :--- | :--- | :--- |
| **GĐ 0** | Tiền xử lý kiềm hóa tách lignin | *Cellulose Extraction from Coconut Coir with Alkaline Delignification Process* | doi:10.1088/1757-899X/980/1/012061 |
| | | *Upcycling coconut husk coir — cellulose nanofibrils CNF* | doi:10.1016/j.indcrop.2021.114400 |
| **GĐ 1** | Sol-gel NH₄OH:Urea:H₂O | *Nitrogen-Doped Carbon Aerogels Prepared by Direct Pyrolysis of... Ammonia-Urea System* | doi:10.1021/acs.iecr.0c03771 |
| | | *New Insights on the Role of Urea on Dissolution...* | doi:10.1021/acs.biomac.8b00688 |
| **GĐ 2** | Khuôn Silicone dẻo & Gel hóa lạnh | *Unique Gelation Behavior of Cellulose in NaOH-Urea...* | doi:10.1021/bm050558m |
| | | *Ice-Templating of Lignin and CNF-Based Carbon* | doi:10.1002/adma.201602448 |
| **GĐ 3** | Đông tụ cồn & Solvent exchange | *Cellulose Diacetate Aerogels with Low Drying Shrinkage...* | doi:10.1021/acs.macromol.3c00421 |
| **GĐ 4** | Sấy thăng hoa | *Kinetics of Supercritical Drying of Gels* | doi:10.1016/j.supflu.2019.104688 |
| **GĐ 5** | Nhiệt phân Carbon hóa lần 1 | *Controlling N-Doping Nature at Carbon Aerogels...* | doi:10.1016/j.carbon.2021.05.022 |
| | | *Electrochemical Properties of CA Electrodes...* | doi:10.1016/j.electacta.2023.142105 |
| **GĐ 6** | Tẩm đốp sắt (Post-impregnation) | *Facile Synthesis of Fe-Doped, Algae Residue-Derived CA...* | doi:10.3390/s24092787 |
| | | *Comparative Study of Two Types of Iron Doped Carbon Aerogels...* | doi:10.1007/s10971-020-05342-w |
| **GĐ 7** | Acid leaching & Re-annealing | *Sustainable HTC... Fe-N-Doped Carbon Nanofiber Aerogels as Electrocatalysts* | doi:10.1016/j.nanoen.2016.08.012 |
| | | *Fe-Cluster Pushing Electrons to N-Doped Graphitic Layers...* | doi:10.1021/acscatal.1c03478 |
| **GĐ 8** | Chế tạo điện cực & Đo điện hóa | *Biomass-Derived Carbon-Based Electrodes for Electrochemical Sensing* | doi:10.3390/mi14091688 |
| | | *Electrochemical sensor... N-doped carbon dots... paracetamol* | doi:10.1016/j.talanta.2021.122849 |
| | | *Zn²⁺ SWASV MWCNT Electrochemical Sensor* | doi:10.1016/j.heliyon.2023.e17346 |
