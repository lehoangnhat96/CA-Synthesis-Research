# 2_Active_Protocol_Electrochemistry.md — Quy Trình Chế Tạo Điện Cực & Đo Đạc Điện Hóa Phân Tích

> [!NOTE]
> * Quy trình thực nghiệm liên hợp: `1_Active_Protocol_Synthesis.md`
> * Cơ sở lý thuyết bổ trợ: `3_Literature_Review_and_Gap_Analysis.md`
> * Cẩm nang bóc tách đỉnh phổ: `4_Material_Characterization_Guide.md`

---

## GIAI ĐOẠN 1: HOẠT HÓA BỀ MẶT ĐIỆN CỰC LÀM VIỆC (GCE Polishing & Anodizing)

*Áp dụng đối với điện cực carbon thủy tinh (Glassy Carbon Electrode - GCE) đường kính hình học Ø = 3 mm, diện tích làm việc hiệu dụng A ≈ 0.0707 cm² làm điện cực nền.*

### 1. Dụng cụ & Hóa chất
* Bột mài nhôm oxit Al₂O₃ cỡ hạt 0.05 µm.
* Tấm nỉ mài phẳng phẳng chuyên dụng.
* Nước cất DI và cồn Ethanol tuyệt đối (HPLC grade).
* Thiết bị đo điện hóa (Potentiostat) cùng bình đo 3 điện cực.

### 2. Quy trình đánh bóng và hoạt hóa GCE
1. **Mài mịn bằng bột Al₂O₃:**
    * Nhỏ vài giọt nước cất và bột Al₂O₃ 0.05 µm lên tấm nỉ mài phẳng.
    * Đặt đứng vuông góc điện cực GCE 90° so với mặt nỉ, di chuyển mài nhẹ nhàng vẽ theo **hình số 8** liên tục trong **2 phút**.
    * Lặp lại thao tác 2 lần để loại bỏ màng polymer cũ.
2. **Siêu âm làm sạch bột mài:**
    * Cho điện cực GCE thẳng đứng vào cốc nước cất DI, tiến hành siêu âm làm sạch trong **1 phút** (thay nước cất DI, siêu âm lặp lại 3 lần).
    * Siêu âm tráng nhanh bằng cồn ethanol tuyệt đối trong **1 phút** để khử ẩm.
3. **Anodize kiềm hoạt hóa (Bắt buộc):**
    * Nhúng điện cực GCE đã siêu âm vào cốc chứa dung dịch **NaOH 0.1 M**.
    * Áp thế điện thế phân cực dương **+1.8 V vs. Ag/AgCl trong thời gian 10 giây** để hòa tan triệt để các hạt alumina siêu nhỏ bám dính vật lý trong các lỗ xốp nano.
    * Rửa lại bằng nước cất DI.
4. **Kiểm tra độ sạch bằng phép quét thế tuần hoàn CV:**
    * Nhúng GCE sạch vào dung dịch redox probe: **5.0mM K₃Fe(CN)₆ trong nền 0.1M KCl**.
    * Quét thế tuần hoàn CV ở tốc độ quét **50 mV/s** (quét 3 chu kỳ).
    * ✓ **Tiêu chí đạt chuẩn (Pass):** Thế hiệu đỉnh tách biệt giữa peak oxy hóa và peak khử **ΔE_p < 70 mV** và tỷ số dòng điện đỉnh đối xứng ***I*_pa/*I*_pc ≈ 0.95 - 1.05**. Nếu chưa đạt, bắt buộc phải đánh bóng lại.

---

## GIAI ĐOẠN 2: PHA CHẾ MỰC IN (Conductive Ink Formulation) & PHỦ ĐIỆN CỰC (Drop-casting)

### 1. Công thức phối trộn conductive ink (Nồng độ 5 mg/mL) và quy hoạch Binder tối ưu
Tùy thuộc vào phương pháp phủ màng và chất phân tích, nồng độ pha chế của chất kết dính (binder) được tính toán nghiêm ngặt để cân bằng giữa độ bền liên kết và độ dẫn điện bề mặt:

#### 🧪 Phương pháp A: Mực Hợp Phần Đồng Nhất (Single-pot Composite Ink - Khuyên dùng)
*Phương pháp này tích hợp hoàn toàn binder vào mạng lưới carbon, đảm bảo màng đồng nhất và truyền điện tích nhanh.*
*   **Điện cực Fe/N-CA / Chitosan/GCE (Đo kim loại nặng SWASV):**
    *   Bột Carbon Aerogel (Fe/N-CA): **5.0 mg**.
    *   Dung môi DMF tinh khiết: **950 µL**.
    *   Dung dịch **Chitosan 1 wt%** (pha trong acid acetic 1%): **50 µL** (Cho nồng độ Chitosan cuối trong mực là **0.05 wt%**, đây là "Sweet Spot" tối ưu chelate Pb²⁺ mà không cản dòng điện).
*   **Điện cực N-CA-700 / Nafion/GCE (Đo Paracetamol DPV):**
    *   Bột Carbon Aerogel (N-CA-700): **5.0 mg**.
    *   Dung môi DMF tinh khiết: **950 µL**.
    *   Dung dịch **Nafion 5 wt% thương mại**: **50 µL** (Cho nồng độ Nafion cuối trong mực đạt đúng **0.25 wt%** hoạt tính cao).

#### 🧪 Phương pháp B: Phủ Màng Từng Lớp (Layer-by-Layer Coating - Tùy chọn)
*Phương pháp này tạo màng Nafion mỏng phủ ngoài, hoạt động như một lớp màng ngăn cản chất bẩn (anti-fouling) rất nhạy.*
*   *Lớp carbon nền:* Nhỏ **5.0 µL** mực carbon thuần (5.0 mg N-CA-700 trong 1000 µL DMF tinh khiết, không chứa binder). Sấy khô nhẹ ở 40 °C trong 15 phút.
*   *Lớp màng bảo vệ:* Nhỏ phủ tiếp **2.0 µL** dung dịch **Nafion 0.25 wt%** (pha loãng bằng cách trộn 10 µL Nafion 5 wt% thương mại + 190 µL Ethanol tuyệt đối) lên trên lớp carbon đã khô, để khô tự nhiên.

### 2. Thực hiện phân tán siêu âm và Drop-casting
1. **Siêu âm phân tán mực:** Bọc kín bình chứa mực in. Đặt bình vào bể siêu âm nước đá lạnh (nhiệt độ duy trì **< 15 °C** để ngăn bay hơi dung môi và kết tụ binder). Tiến hành siêu âm liên tục trong **30 - 60 phút** ở chế độ thường. Mực in thu được phải đen tuyền, phân tán tuyệt đối.
2. **Drop-casting:** Dùng pipette vi lượng hút chính xác **5.0 µL** mực in (đối với cả Phương pháp A và lớp nền Phương pháp B) lên trung tâm bề mặt điện cực GCE đã được dựng thẳng đứng trên giá đỡ. 
3. **Sấy khô màng mỏng (Bắt buộc):**
    * Úp ngược một cốc thủy tinh sạch che bụi lên điện cực GCE, để màng khô tự nhiên hoàn toàn ở nhiệt độ phòng (25 °C) trong **2 - 3 giờ** trong tủ hút.
    * **⚠️ Cảnh báo cực đoan:** Tuyệt đối không sấy gia nhiệt nhanh, không thổi khí N₂ hoặc dùng đèn sưởi hồng ngoại, không sấy chân không đối với màng ướt để tránh hiệu ứng "vành cà phê" (coffee-ring) làm dồn toàn bộ bột carbon ra viền mép điện cực.

---

## GIAI ĐOẠN 3: SÀNG LỌC ĐIỆN CỰC NỀN TRƯỚC PHÂN TÍCH (Pre-electrode Baseline Screening)

Màng điện cực biến tính phải vượt qua các chỉ số baseline dưới đây trước khi đo mẫu thực tế:

1. **Quét thế tuần hoàn CV nền:** Quét thế tuần hoàn trong dung dịch **5.0mM K₃Fe(CN)₆ / 0.1M KCl**, tốc độ quét 50 mV/s.
    * *Chỉ số Pass:* Cường độ dòng đỉnh I_pa phải tăng **≥ 30%** và thế đỉnh tách biệt **ΔE_p < 110 mV** so với điện cực bare GCE.
2. **Trở kháng điện hóa EIS:** Đo phổ EIS trong dung dịch redox probe **5.0mM K₃Fe(CN)₆ / 0.1M KCl** (tần số quét từ 100kHz → 0.1 Hz, biên độ sóng 10 mV, áp thế tĩnh E_dc = 0.22 V vs. Ag/AgCl).
    * *Chỉ số Pass:* Bán kính cung bán tròn trở kháng của mẫu Fe/N-CA phải thu hẹp **≥ 35%** so với bare GCE (R_ct(Fe/N-CA) < R_ct(N-CA) < R_ct(bare GCE)).
3. **Diện tích điện hóa hiệu dụng (ECSA):** Quét CV trong dung dịch đệm ở nhiều tốc độ quét tăng dần (25 → 200 mV/s) trong khoảng thế không Faraday (0.0 → 0.1V) để thu được dòng điện dung lớp kép (C_dl).

---

## GIAI ĐOẠN 4: THIẾT LẬP CHƯƠNG TRÌNH PHÂN TÍCH CẢM BIẾN ĐIỆN HÓA

### 1. Phép đo cảm biến Pb²⁺ bằng kỹ thuật sóng vuông hòa tan (SWASV)
* **WE sử dụng:** Điện cực Fe/N-CA / Chitosan/GCE.
* **Dung dịch điện ly nền:** Đệm Acetate 0.1 M, pH = 4.5.
* **Các bước lập trình thiết bị (SWASV Program):**
  1. **Làm giàu khử (Pre-concentration):** Áp thế điện thế khử âm **E_dep = -1.1V vs. Ag/AgCl** trong thời gian **t_dep = 120 giây** dưới lực khuấy từ ổn định 400 rpm để khử các ion Pb²⁺ thành Pb⁰ tích lũy trên màng.
  2. **Thời gian cân bằng (Quiet time):** Tắt khuấy từ, để hệ điện cực đứng yên tĩnh lặng trong **10 giây** để ổn định dòng nền.
  3. **Hòa tan sóng vuông (Anodic Stripping):** Quét thế phân cực anode bằng sóng vuông ngược từ **-1.4V đến -0.2V vs. Ag/AgCl** để oxy hóa hòa tan chì tích lũy trở lại dung dịch (Pb⁰ → Pb²⁺ + 2e⁻). Peak hòa tan xuất hiện ở khoảng thế ≈ -0.5V.
      * *Thông số sóng vuông:* SW frequency = **25 Hz** | SW amplitude = **25 mV** | Step potential = **5 mV**.
  4. **Làm sạch điện cực (Cleaning):** Áp thế dương **+0.2V trong 30 giây** kết hợp khuấy từ tốc độ cao 600 rpm để giải phóng lượng kim loại còn sót lại, tránh hiện tượng nhiễm chéo mẫu.

### 2. Mở rộng đo đồng thời đa ion kim loại nặng (Zn²⁺, Cd²⁺, Pb²⁺, Cu²⁺) bằng kỹ thuật SWASV
* **Dung dịch điện ly nền:** Đệm Acetate 0.1 M, pH = 4.5.
* **Các bước lập trình thiết bị:**
  1. **Làm giàu khử:** Áp thế E_dep = **-1.30V vs. Ag/AgCl** trong **120 - 180 giây** (khuấy 400 rpm).
  2. **Thời gian cân bằng:** 10 giây.
  3. **Hòa tan sóng vuông:** Quét thế từ **-1.40V đến +0.40V** vs. Ag/AgCl.
* **Thế hiệu đỉnh hòa tan (Stripping Potentials) đặc trưng:**
  * **Kẽm (Zn²⁺):** ≈ -1.10V
  * **Cadmium (Cd²⁺):** ≈ -0.80V
  * **Chì (Pb²⁺):** ≈ -0.50V
  * **Đồng (Cu²⁺):** ≈ +0.05V

### 3. Thiết lập quy trình đo riêng lẻ Thủy ngân (Hg²⁺) và Thạch tín (As³⁺)
* **Dung dịch điện ly nền:** Đệm Acetate 0.1 M, pH = 4.5 (cho Hg²⁺) hoặc đệm H₂SO₄ loãng (cho As³⁺).
* **Các bước lập trình thiết bị:**
  1. **Làm giàu khử:** Áp thế chọn lọc E_dep = **-0.20V đến -0.40V vs. Ag/AgCl** trong **120 - 180 giây** (tránh sinh bọt khí H₂).
  2. **Thời gian cân bằng:** 10 giây.
  3. **Hòa tan sóng vuông:** Quét thế từ **0.0V đến +0.6V** vs. Ag/AgCl.
* **Thế hiệu đỉnh hòa tan đặc trưng:**
  * **Thạch tín (As³⁺):** ≈ +0.15V đến +0.20V
  * **Thủy ngân (Hg²⁺):** ≈ +0.25V đến +0.30V

### 4. Phép đo cảm biến Paracetamol bằng kỹ thuật xung vi phân (DPV)
* **WE sử dụng:** Điện cực N-CA-700 / Nafion/GCE.
* **Dung dịch điện ly nền:** Phosphate Buffered Saline (PBS) 0.1 M, pH = 7.0 - 7.4.
* **Các bước lập trình thiết bị (DPV Program):**
  * Khoảng thế quét: Quét phân cực dương từ **0.0V đến +0.8V vs. Ag/AgCl**.
  * Tốc độ quét thế: 20 mV/s.
  * *Thông số xung vi phân:* **Pulse amplitude = 50 mV** | **Pulse width = 50 ms** | **Step potential = 5 mV**.
  * Phép đo được tiến hành quét trực tiếp, không áp thế làm giàu điện hóa (E_dep). Peak oxy hóa Paracetamol xuất hiện rõ nét ở ≈ +0.34V vs. Ag/AgCl.

---

## GIAI ĐOẠN 5: THIẾT LẬP MODULE ĐO ĐẶC TÍNH ĐIỆN HÓA BỔ TRỢ ĐỒNG DẠNG (ORR & Siêu Tụ Điện)

### 1. Phép đo Xúc tác khử Oxy (ORR) làm "Proof of Concept" chứng minh tâm Fe-N₄
* **WE sử dụng:** Điện cực Fe/N-CA / Chitosan/GCE.
* **Điện ly nền:** Dung dịch **KOH 0.1 M**.
* **Quy trình đo đạc:**
  1. Thổi khí N₂ sục liên tục vào bình điện giải KOH 0.1 M trong 30 phút để đuổi sạch oxy. Tiến hành chạy quét thế CV từ **-1.0V đến +0.2V vs. Ag/AgCl** ở tốc độ quét 50 mV/s. CV thu được là đường nền phẳng, đại diện dòng dung.
  2. Chuyển sang sục liên tục khí O₂ trong 30 phút để bão hòa oxy. Chạy quét thế CV tương tự. Đường phổ CV bắt buộc phải xuất hiện một peak khử oxy cực kỳ sắc nét ở thế dương hơn **-0.2V vs. Ag/AgCl** với cường độ dòng đỉnh khử đạt ***I*_c ≥ 1.0mA/cm²**.
  3. Đo linear sweep voltammetry (LSV) trên điện cực quay RDE ở các tốc độ quay từ 400 rpm đến 3600 rpm để tính toán số electron chuyển tải (n ≈ 3.14 - 3.69 tiệm cận cơ chế 4 electron).

### 2. Phép đo Siêu tụ điện hóa (Supercapacitor) của mẫu đối chứng NaOH-Urea
* **WE sử dụng:** Mẫu carbon NaOH-Urea ép viên drop-cast.
* **Điện ly nền:** Dung dịch **KOH 6.0 M** siêu đậm đặc.
* **Quy trình đo đạc:**
  1. Chạy CV trong KOH 6.0 M ở các tốc độ quét từ 5 - 100 mV/s trong khoảng thế tĩnh từ -1.0V → 0.0V vs. Ag/AgCl. Đường CV thu được dạng hình hộp chữ nhật đối xứng.
  2. Đo phóng nạp dòng hằng GCD ở các mật độ dòng từ 0.5 - 10A/g. Đường phóng nạp GCD phải có dạng tam giác cân đối xứng, xác định điện dung riêng cụ thể (*C*_sF/g).
