# 2_Protocol_Electrochemistry.md — Quy Trình Chế Tạo Điện Cực & Đo Cảm Biến Điện Hóa

<!-- v2.0 | Chuẩn hóa: 2026-05-31 | Merge từ: 2_Active_Protocol_Electrochemistry + SYNTHESIS_PARAMETERS §12,13 + CA_characterization §7,8 -->

> [!NOTE]
> * **Tài liệu liên hợp tổng hợp:** `1_Protocol_Synthesis.md`
> * **Cơ sở lý thuyết và GAP:** `3_Literature_Review_and_Gap_Analysis.md`
> * **Đặc trưng vật lý hóa học vật liệu:** `4_Material_Characterization.md`
> * **Bảng checklist lab:** `6_Quality_Gates_Checklist.md`
>
> Tài liệu này chuẩn hóa quy trình mài bóng điện cực Carbon Thủy tinh (GCE), pha chế mực in carbon aerogel biến tính với các binder chuyên biệt, kiểm tra baseline redox probe, và thiết lập các phép đo cảm biến điện hóa phân tích kim loại nặng ($Pb^{2+}$, $Zn^{2+}$, $Cd^{2+}$) bằng kỹ thuật SWASV và Paracetamol (APAP) bằng kỹ thuật DPV. Các phần đo ORR và siêu tụ điện được chuyển thành phần mở rộng định hướng công bố bài báo (GĐ 8.6) nhằm nâng cao chất lượng khoa học, không còn nằm trong khung bắt buộc của đề cương chính.

---

## GIAI ĐOẠN 8.1: HOẠT HÓA BỀ MẶT ĐIỆN CỰC LÀM VIỆC (GCE Polishing & Anodizing)

*Áp dụng đối với điện cực carbon thủy tinh (Glassy Carbon Electrode - GCE) đường kính hình học $\emptyset = 3\text{ mm}$, diện tích hình học bề mặt $A = 0.0707\text{ cm}^2$ làm điện cực nền.*

### 1. Dụng cụ & Hóa chất bắt buộc
* Bột mài alumina ($Al_2O_3$) siêu mịn cỡ hạt $0.05\text{ }\mu\text{m}$.
* Tấm nỉ mài phẳng phẳng chuyên dụng.
* Nước cất DI và cồn Ethanol tuyệt đối (HPLC grade).
* Máy đo điện hóa (Potentiostat) cùng bình đo 3 điện cực (Điện cực làm việc GCE, điện cực đối đối chứng Pt wire, điện cực tham chiếu $Ag/AgCl$ bão hòa $KCl$).

### 2. Quy trình đánh bóng và hoạt hóa GCE
1. **Mài mịn bằng bột Al₂O₃:**
   * Nhỏ vài giọt nước cất DI và một lượng nhỏ bột $Al_2O_3$ $0.05\text{ }\mu\text{m}$ lên tấm nỉ mài.
   * Đặt đứng vuông góc điện cực GCE 90° so với mặt nỉ mài, di chuyển mài nhẹ nhàng vẽ theo **hình số 8** liên tục trong **2 phút**.
   * Lặp lại thao tác mài lần thứ hai để loại bỏ hoàn toàn các lớp polymer biến tính cũ bám dính ở mẻ trước.
2. **Siêu âm làm sạch bột mài:**
   * Cho điện cực GCE thẳng đứng vào cốc nước cất DI sạch, tiến hành siêu âm làm sạch trong **1 phút**. Thay nước cất DI mới và siêu âm lặp lại **chính xác 3 lần** để rửa sạch hoàn toàn bụi bột mài.
   * Siêu âm tráng nhanh điện cực trong cồn ethanol tuyệt đối trong **1 phút** để khử ẩm bề mặt.
3. **Anodize kiềm hoạt hóa:**
   * Nhúng đầu điện cực GCE đã làm sạch vào cốc chứa dung dịch **NaOH 0.1 M**.
   * Áp thế điện thế phân cực dương cực mạnh **+1.8 V vs. Ag/AgCl trong thời gian 10 giây**. 
   * *Ý nghĩa:* Giúp oxy hóa hòa tan triệt để các hạt alumina siêu nhỏ bám dính vật lý sâu trong các vi kẽ carbon, tạo các nhóm chức chứa oxy hoạt tính phân cực bề mặt.
   * Rửa lại điện cực bằng nước cất DI.
4. **Kiểm tra độ sạch bằng phép quét thế tuần hoàn CV (Baseline Gate):**
   * Nhúng GCE sạch vào dung dịch redox probe tiêu chuẩn: **5.0 mM $K_3Fe(CN)_6$ trong nền 0.1 M KCl**.
   * Quét thế tuần hoàn CV ở tốc độ quét **50 mV/s** (quét 5 chu kỳ ổn định).
   * **Tiêu chí đạt chuẩn (Pass):** Thế hiệu đỉnh tách biệt giữa peak oxy hóa và peak khử $\Delta E_p < 70\text{ mV}$ và tỷ số dòng điện đỉnh đối xứng $I_{pa}/I_{pc} = 0.95 - 1.05$.
   * *Nếu $\Delta E_p \ge 70\text{ mV}$:* Bắt buộc phải thực hiện đánh bóng lại từ bước 1.

---

## GIAI ĐOẠN 8.2: PHA CHẾ MỰC IN (Conductive Ink) & PHỦ ĐIỆN CỰC (Drop-casting)

### 1. Công thức phối trộn conductive ink (Nồng độ 5 mg/mL) và phân vai Binder
Để tối ưu hóa độ nhạy và tính chọn lọc của cảm biến, hệ binder kết dính được phân chia chuyên biệt theo hướng phân tích:

* **Mực Fe/N-CA (Đo kim loại nặng Pb²⁺, Zn²⁺, Cd²⁺ bằng SWASV):**
  * Bột Carbon Aerogel ($Fe/N-CA$): **5.0 mg** (đã nghiền mịn, rây lấy kích thước hạt $<75\text{ }\mu\text{m}$).
  * Dung môi DMF tinh khiết (HPLC grade): **950 µL**.
  * Dung dịch **Chitosan 1 wt%** (pha sẵn trong acid acetic 1%): **50 µL** (Cho nồng độ Chitosan cuối trong mực đạt **0.05 wt%**).
  * *Biện luận khoa học:* Chitosan chứa lượng lớn nhóm chức amino ($-NH_2$) và hydroxyl ($-OH$) hoạt động phối trí chelate hóa cực mạnh với các cation kim loại nặng ($Pb^{2+}$, $Zn^{2+}$, $Cd^{2+}$), tăng hiệu quả làm giàu tích lũy kim loại bề mặt khi lắng khử.
* **Mực N-CA (Đo Paracetamol bằng DPV):**
  * Bột Carbon Aerogel ($N-CA-700$): **5.0 mg**.
  * Dung môi DMF tinh khiết: **950 µL**.
  * Dung dịch **Nafion 5 wt% thương mại**: **50 µL** (Cho nồng độ Nafion cuối trong mực đạt **0.25 wt%**).
  * *Biện luận khoa học:* Nafion hoạt động như màng trao đổi cation chọn lọc, bền nhiệt, dẫn tốt, chống bám bẩn (anti-fouling) bởi các tạp chất hữu cơ phân tử lớn khi phân tích Paracetamol.

### 2. Thực hiện phân tán siêu âm và Drop-casting tạo màng
1. **Siêu âm phân tán mực:** Bọc kín bình chứa mực in bằng Parafilm. Đặt bình vào bể siêu âm nước đá lạnh (duy trì nhiệt độ **< 15 ℃** để ngăn nóng cục bộ gây bay hơi DMF hoặc đông tụ binder). Tiến hành siêu âm liên tục trong **30–60 phút**. Mực in thu được phải đen tuyền, phân tán tuyệt đối, không có cặn lắng ở đáy bình.
2. **Drop-casting:** Dùng pipette vi lượng hút chính xác **5.0 µL** mực in nhỏ chậm lên trung tâm bề mặt điện cực GCE đã được dựng thẳng đứng trên giá đỡ. 
3. **Sấy khô màng mỏng tự nhiên:**
   * Úp ngược một cốc thủy tinh sạch che bụi lên điện cực GCE, để màng khô tự nhiên hoàn toàn ở nhiệt độ phòng (25 ℃) trong **2–3 giờ** trong tủ hút khí độc.
   * > [!CAUTION]
   * > **CẤM SẤY NHIỆT NHANH:** Tuyệt đối không thổi khí $N_2$ hoặc dùng đèn sưởi hồng ngoại, không sấy chân không đối với màng ướt để tránh hiệu ứng "vành cà phê" (coffee-ring) làm dồn toàn bộ bột carbon ra viền mép điện cực, gây bong tróc màng khi quay đo điện cực.

---

## GIAI ĐOẠN 8.3: SÀNG LỌC ĐIỆN CỰC NỀN TRƯỚC PHÂN TÍCH (Baseline Screening)

Màng điện cực biến tính ($N-CA/GCE$ và $Fe/N-CA/GCE$) bắt buộc phải vượt qua các chỉ số sàng lọc điện hóa nền dưới đây:

1. **Quét thế tuần hoàn CV nền:** Quét thế tuần hoàn trong dung dịch **5.0 mM $K_3Fe(CN)_6$ / 0.1 M KCl**, tốc độ quét 50 mV/s (quét 5 chu kỳ).
   * **Chỉ số Pass:** Cường độ dòng đỉnh $I_{pa}$ phải tăng **$\ge 30\%$** và thế hiệu đỉnh tách biệt $\Delta E_p < 120\text{ mV}$ so với điện cực bare GCE.
2. **Trở kháng điện hóa EIS:** Đo phổ EIS trong dung dịch redox probe **5.0 mM $K_3Fe(CN)_6$ / 0.1 M KCl** (tần số quét từ 100 kHz $\rightarrow$ 0.1 Hz, biên độ sóng 10 mV, áp thế tĩnh $E_{dc} = 0.22\text{ V}$ vs. Ag/AgCl).
   * **Chỉ số Pass:** Bán kính cung bán tròn trở kháng của mẫu Fe/N-CA phải thu hẹp **$\ge 35\%$** so với bare GCE ($R_{ct}(Fe/N-CA) < R_{ct}(N-CA) < R_{ct}(\text{bare GCE})$).
3. **Diện tích bề mặt hoạt tính điện hóa (EASA):**
   * Quét CV trong dung dịch redox probe ở nhiều tốc độ quét tăng dần ($v = 10, 20, 50, 100, 150, 200\text{ mV/s}$).
   * Sử dụng phương trình Randles-Ševčík để tính toán diện tích hoạt tính điện hóa ($A_{\text{eff}}$):
     $$I_p = (2.69 \times 10^5) n^{3/2} A_{\text{eff}} D^{1/2} C v^{1/2}$$
     *Trong đó: $n=1$, $D \approx 7.6 \times 10^{-6}\text{ cm}^2\text{/s}$ của $[Fe(CN)_6]^{3-}$, $C = 5.0 \times 10^{-6}\text{ mol/cm}^3$.*
   * **Chỉ số Pass:** $A_{\text{eff}} \ge 0.12\text{ cm}^2$ (Tăng gấp đôi so với diện tích hình học GCE $0.0707\text{ cm}^2$).

---

## GIAI ĐOẠN 8.4: THIẾT LẬP CHƯƠNG TRÌNH PHÂN TÍCH CẢM BIẾN

### 1. Phép đo đồng thời Chì ($Pb^{2+}$), Kẽm ($Zn^{2+}$) và Cadmium ($Cd^{2+}$) bằng SWASV
* **WE sử dụng:** Điện cực Fe/N-CA / Chitosan/GCE.
* **Dung dịch điện ly nền:** Đệm Acetate 0.1 M, pH = 4.5.
* **Các bước lập trình thiết bị (SWASV Program):**
  1. **Lắng khử (Deposition):** Áp thế điện thế khử âm **$E_{\text{dep}} = -1.1\text{ V vs. Ag/AgCl}$** (Hoặc $-1.3\text{ V}$ khi đo thêm Kẽm) trong thời gian **$t_{\text{dep}} = 120\text{ giây}$** dưới lực khuấy từ ổn định 400 rpm để khử các cation kim loại ($M^{2+} \rightarrow m^0$) tích lũy trên màng.
  2. **Thời gian cân bằng (Quiet time):** Tắt khuấy từ, để hệ điện cực đứng yên tĩnh lặng trong **10 giây** để ổn định dòng nền.
  3. **Hòa tan sóng vuông (Anodic Stripping):** Quét thế phân cực anode bằng sóng vuông ngược từ **$-1.4\text{ V}$ đến $-0.2\text{ V}$ vs. Ag/AgCl** để oxy hóa hòa tan kim loại tích lũy trở lại dung dịch.
     * *Thông số sóng vuông chốt:* SW frequency = **25 Hz** | SW amplitude = **25 mV** | Step potential = **5 mV**.
  4. **Thế hiệu đỉnh hòa tan (Stripping Potentials) đặc trưng:**
     * **Kẽm ($Zn^{2+}$):** $\approx -1.10\text{ V}$ vs. Ag/AgCl.
     * **Cadmium ($Cd^{2+}$):** $\approx -0.80\text{ V}$ vs. Ag/AgCl *(Đang tối ưu thực nghiệm)*.
     * **Chì ($Pb^{2+}$):** $\approx -0.50\text{ V}$ vs. Ag/AgCl.
  5. **Làm sạch điện cực (Cleaning):** Áp thế dương **$+0.2\text{ V}$ trong $30\text{ giây}$** kết hợp khuấy từ tốc độ cao 600 rpm để giải phóng hoàn toàn lượng kim loại còn sót lại, tránh hiện tượng nhiễm chéo mẫu cho lượt đo sau.

* **Khoảng khảo sát tối ưu:**
  * Khảo sát thế lắng khử ($E_{\text{dep}}$) từ $-0.8\text{ V}$ đến $-1.4\text{ V}$.
  * Khảo sát thời gian lắng khử ($t_{\text{dep}}$) từ $60\text{ s}$ đến $240\text{ s}$.
  * Khảo sát pH dung dịch đệm acetate từ $3.5$ đến $6.0$.
* **Mục tiêu hiệu năng (Benchmark LOD):**
  * **$Pb^{2+}$:** LOD < $0.1\text{ }\mu\text{g/L}$ ($0.1\text{ ppb}$).
  * **$Zn^{2+}$:** LOD < $10\text{ nM}$.
* **Danh sách ion gây nhiễu cần khảo sát (Interference test):**
  * $Cu^{2+}$ (gây nhiễu mạnh nhất do tạo hợp kim bismuth/sắt cạnh tranh), $Hg^{2+}$, $Fe^{3+}$, $Mn^{2+}$, $Ca^{2+}$, $Mg^{2+}$, $Na^+$, $K^+$, $NO_3^-$.
  * *Tiêu chí chấp nhận:* Tín hiệu dòng peak thay đổi $< 10\%$ khi có mặt chất gây nhiễu nồng độ gấp 10-100 lần.

### 2. Phép đo cảm biến Paracetamol (APAP) bằng kỹ thuật xung vi phân (DPV)
* **WE sử dụng:** Điện cực N-CA / Nafion/GCE.
* **Dung dịch điện ly nền:** Đệm Phosphate Buffered Saline (PBS) 0.1 M, pH = 7.0–7.4 (Khảo sát pH từ $5.0$ đến $8.0$).
* **Các bước lập trình thiết bị (DPV Program):**
  1. **Quét thế phân cực dương trực tiếp:** Quét phân cực anode từ **$0.0\text{ V}$ đến $+0.8\text{ V}$ vs. Ag/AgCl**.
     * *Tuyệt đối không áp thế lắng khử điện hóa ($E_{\text{dep}}$) để tránh sụp đổ dòng.*
  2. **Thông số xung vi phân chốt:**
     * Pulse amplitude = **50 mV**
     * Pulse width = **50 ms**
     * Step potential = **5 mV**
     * Tốc độ quét thế hiệu dụng = **20 mV/s**
  3. **Thế hiệu đỉnh oxy hóa đặc trưng:**
     * Peak oxy hóa Paracetamol xuất hiện rõ nét ở thế hiệu: **$\approx +0.43\text{ V}$ đến $+0.47\text{ V}$ vs. Ag/AgCl**.
     * *(Lưu ý: Màng biến tính carbon dời đỉnh peak từ $+0.34\text{ V}$ của điện cực bare GCE về phía thế dương hơn một chút do ảnh hưởng của lực khuếch tán bề mặt và độ dày màng, đây là hiện tượng bình thường và đại diện cho tính chất xúc tác màng).*
* **Mục tiêu hiệu năng (Benchmark LOD):**
  * Paracetamol: LOD < $0.05\text{ }\mu\text{M}$ (linear range mục tiêu từ $0.1$ đến $100\text{ }\mu\text{M}$).
* **Danh sách chất gây nhiễu cần khảo sát:**
  * Ascorbic acid (AA), uric acid (UA), dopamine (DA), glucose, diclofenac, nimesulide, amoxicillin.

---

## GIAI ĐOẠN 8.5: ĐÁNH GIÁ ĐỘ LẶP LẠI, ĐỘ TÁI LẶP & ĐỘ ỔN ĐỊNH (Analytical Validation)

Để số liệu đủ điều kiện công bố quốc tế (Q1/Q2), bắt buộc phải thực hiện các phép đo sau:

| Chỉ tiêu | Phương pháp đo | Tiêu chí chấp nhận |
| :--- | :--- | :--- |
| **Độ lặp lại (Repeatability)** | Chạy $10$ lần phép đo liên tiếp trên **cùng 1 điện cực** biến tính trong dung dịch chứa analyte cố định. | $RSD < 5\%$ |
| **Độ tái lặp (Reproducibility)** | Chế tạo độc lập **$5$ điện cực khác nhau** cùng công thức, tiến hành đo trong cùng điều kiện. | $RSD < 8\%$ |
| **Độ ổn định bảo quản (Stability)** | Lưu trữ điện cực trong tủ mát ở 4 ℃ (bọc kín). Đo lại sau **$7, 14, 30$ ngày**. | Giữ được **$\ge 90\%$** cường độ dòng điện đỉnh ban đầu sau $14$ ngày. |
| **Mẫu thực (Real sample)** | Sử dụng phương pháp thêm chuẩn (**Standard Addition**) 3 điểm trên mẫu nước sông/nước máy (nhánh kim loại) hoặc thuốc viên paracetamol thương mại. | Hiệu suất thu hồi (**Recovery**) đạt **$95\% - 105\%$**. |

---

## GIAI ĐOẠN 8.6: QUẢN LÝ ĐIỆN CỰC SO SÁNH & QUY TRÌNH MỞ RỘNG PHI NƯỚC (Reference Electrode Calibration & Non-Aqueous Extensions)

Nhằm tối ưu hóa thiết bị, kiểm soát sai số hệ thống và mở rộng phạm vi nghiên cứu để nâng cao chất lượng công bố quốc tế, quy trình bổ sung các hướng dẫn kỹ thuật liên quan đến điện cực so sánh nước (Ceramic Ag/AgCl) và điện cực so sánh phi nước (Non-aqueous Ag/Ag⁺):

### 1. Quy trình hiệu chuẩn và kiểm tra điện cực so sánh nước (Aqueous RE Calibration)
Trước mỗi đợt đo cảm biến quan trọng (SWASV kim loại nặng hoặc DPV paracetamol), bắt buộc phải kiểm tra độ ổn định của điện cực so sánh nhằm tránh hiện tượng trôi thế nền:
*   **Phép đo OCP so sánh trực tiếp (Nhanh & Hiệu quả):**
    *   Nhúng điện cực cần kiểm tra và một điện cực so sánh chuẩn (đang hoạt động tốt hoặc điện cực mới nguyên hộp) vào cùng một cốc dung dịch **$KCl$ 3 M** hoặc **$KCl$ bão hòa**.
    *   Sử dụng một Volt kế điện tử (Multimeter) có trở kháng cao hoặc chạy chương trình đo thế mạch hở (OCP) trên máy Potentiostat trong **$60\text{ giây}$**.
    *   *Tiêu chí chấp nhận:* Hiệu điện thế chênh lệch $\Delta E_{OCP} \le 10\text{ mV}$ (lý tưởng nhất là $\le 3\text{ mV}$). Nếu hiệu thế lệch $> 10\text{ mV}$, điện cực cần phải được bảo dưỡng (thay dung dịch $KCl$ bên trong, ngâm thông màng xốp ceramic).
*   **Phép đo CV kiểm tra hệ Redox chuẩn:**
    *   Quét CV dung dịch redox probe chuẩn **$5.0\text{ mM } K_3Fe(CN)_6$ trong $0.1\text{ M } KCl$**, tốc độ quét $50\text{ mV/s}$.
    *   *Tiêu chí chấp nhận:* Thế hiệu formal $E_{1/2} = (E_{pa} + E_{pc})/2$ của cặp $[Fe(CN)_6]^{3-/4-}$ phải duy trì ổn định trong khoảng **$+0.22\text{ V}$ đến $+0.25\text{ V}$ vs. Ag/AgCl (sat. KCl)**.

### 2. Quy trình "Hô biến" điện cực phi nước (Non-aqueous RE) thành điện cực Ag/AgCl nước dự phòng
Nếu điện cực Ceramic của bạn bị hỏng hoặc nghẽn màng ngăn, bạn hoàn toàn có thể tận dụng cấu tạo ống của điện cực phi nước (Non-aqueous Silver Ion Electrode) để tự chế một điện cực so sánh hệ nước dự phòng hiệu năng cao:
1.  **Tháo rời và làm sạch:** Rút sợi dây bạc ($Ag$ wire) bên trong thân ống điện cực phi nước ra, dùng cồn và nước cất DI rửa sạch hoàn toàn tàn dư dung môi hữu cơ bên trong thân ống. Dùng giấy nhám mịn đánh bóng nhẹ sợi dây bạc để loại bỏ các lớp oxit.
2.  **Clorua hóa sợi dây bạc (Chloridization):**
    *   Nhúng sợi dây bạc sạch vào dung dịch **$HCl$ 0.1 M** (hoặc $KCl$ 1 M).
    *   Nối sợi dây bạc vào cực làm việc (WE), dùng một điện cực đối Pt hoặc kim loại khác làm đối cực (CE).
    *   Áp một thế phân cực dương nhẹ **$+0.8\text{ V}$** (hoặc áp dòng điện dương ổn định $0.5 - 1.0\text{ mA/cm}^2$) trong thời gian **$2\text{ phút}$**.
    *   *Kết quả đạt:* Sợi dây bạc chuyển từ màu sáng kim loại sang màu xám tro hoặc xám nâu sẫm, xác nhận lớp $AgCl$ đã bám chắc đều bề mặt.
3.  **Nạp dung dịch nước:** Dùng xi-lanh bơm đầy dung dịch **$KCl$ 3 M hoặc $KCl$ bão hòa** vào trong thân ống điện cực rỗng.
4.  **Lắp ráp:** Luồn sợi dây bạc đã clorua hóa trở lại thân ống. Bạn đã có ngay một chiếc điện cực so sánh $Ag/AgCl$ hệ nước dự phòng chất lượng tốt.

### 3. Hướng mở rộng 1: Siêu tụ điện thế cao trong môi trường hữu cơ (Organic Supercapacitor)
*Ý nghĩa:* Tận dụng cấu trúc carbon aerogel 3D siêu xốp và các dị tố $N, Fe$ để làm điện cực tích trữ năng lượng thế hiệu cao trong dung môi hữu cơ, mở ra hướng viết **Bài báo khoa học thứ 3** cực kỳ triển vọng với chi phí phát sinh rất thấp.
*   **Tính khả thi & Cơ sở thực hiện:** Điện cực so sánh phi nước ($Ag/Ag^+$), dung môi hữu cơ Acetonitrile chất lượng cao, các muối hữu cơ ($TEABF_4$, $LiClO_4$) và bọt Niken ($Nickel\text{ }foam$) làm đế dẫn đều có sẵn tại phòng thí nghiệm trung tâm IUH. Cấu trúc carbon aerogel dẻo dai từ xơ dừa có tính ổn định cơ lý cao, hạn chế bong tróc khi sạc xả liên tục ở mật độ dòng lớn ($0.5 - 10\text{ A/g}$).
*   **Thiết lập hệ đo 3 điện cực:**
    *   **WE (Làm việc):** Carbon Aerogel biến tính tráng lên bọt niken (Nickel foam) làm điện cực làm việc.
    *   **CE (Đối cực):** Dây Pt hoặc tấm carbon phẳng diện tích lớn.
    *   **RE (So sánh):** Điện cực phi nước **Non-aqueous Silver Ion Reference Electrode** (đã nạp dung dịch $0.01\text{ M } AgNO_3$ + $0.1\text{ M } TBAP$ trong Acetonitrile).
*   **Chất điện ly hữu cơ:** Muối nền hữu cơ **$1.0\text{ M } TEABF_4$** hoặc **$1.0\text{ M } LiClO_4$** hòa tan trong dung môi hữu cơ Acetonitrile (AN) hoặc Propylene Carbonate (PC).
*   **Chương trình thực nghiệm phân tích:**
    *   **Quét CV thế cao:** Quét CV ở các tốc độ quét từ $5 - 200\text{ mV/s}$ trong khoảng thế rộng từ **$0.0\text{ V}$ đến $+2.5\text{ V}$ hoặc $+3.0\text{ V}$** để tính toán điện dung riêng ($F/g$) và đánh giá đóng góp pseudocapacitance của các tâm $N$ và $Fe-N_x$.
    *   **Phóng nạp hằng dòng (GCD):** Chạy GCD ở các mật độ dòng điện từ $0.5 - 10\text{ A/g}$ để đánh giá hiệu suất Coulombic và độ bền chu kỳ phóng nạp (khảo sát $5000 - 10000$ chu kỳ liên tục).
    *   **Trở kháng EIS hữu cơ:** Đo EIS ở thế tĩnh $1.25\text{ V}$ để đánh giá điện trở chuyển điện tích hữu cơ ($R_{ct}$) và điện trở khuếch tán ion.

### 4. Hướng mở rộng 2: Cảm biến chất hữu cơ kỵ nước trong dung môi hỗn hợp (Mixed-Solvent Sensor)
*Ý nghĩa:* Phát triển cảm biến carbon aerogel đo trực tiếp các tác nhân ô nhiễm hữu cơ khó tan trong nước (như thuốc trừ sâu Carbaryl, Chlorpyrifos, hoặc Bisphenol A).
*   **Môi trường đo:** Sử dụng hệ dung môi hỗn hợp **Acetonitrile/Nước (tỷ lệ thể tích 50/50)** hoặc **DMF/Nước** chứa chất chuẩn phân tích kỵ nước.
*   **Thiết lập RE:** Sử dụng điện cực so sánh phi nước **Non-aqueous Silver Ion Electrode** để tránh hiện tượng dung môi hữu cơ thẩm thấu phá hủy màng gốm ceramic của điện cực nước, đồng thời ngăn sự rò rỉ nước từ điện cực làm ảnh hưởng đến độ tan của chất phân tích.
*   **Kỹ thuật đo:** Quét thế phân cực anode bằng xung vi phân (DPV) hoặc sóng vuông (SWV) để ghi nhận peak oxy hóa đặc trưng của chất phân tích kỵ nước trên nền màng composite $Fe/N-CA$ hoặc $N-CA$.

