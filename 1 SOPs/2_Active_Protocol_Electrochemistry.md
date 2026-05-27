# 2_Active_Protocol_Electrochemistry.md — Quy Trình Chế Tạo Điện Cực & Đo Đạc Điện Hóa Phân Tích

> [!NOTE]
> * Quy trình thực nghiệm liên hợp: [1_Active_Protocol_Synthesis.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/1_Active_Protocol_Synthesis.md)
> * Cơ sở lý thuyết bổ trợ: [3_Literature_Review_and_Gap_Analysis.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/3_Literature_Review_and_Gap_Analysis.md)
> * Cẩm nang bóc tách đỉnh phổ: [4_Material_Characterization_Guide.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/4_Material_Characterization_Guide.md)

---

## GIAI ĐOẠN 1: HOẠT HÓA BỀ MẶT ĐIỆN CỰC LÀM VIỆC (GCE Polishing & Anodizing)

*Áp dụng đối với điện cực carbon thủy tinh (Glassy Carbon Electrode - GCE) đường kính hình học $\varnothing = 3\text{ mm}$, diện tích làm việc hiệu dụng $A \approx 0.0707\text{ cm}^2$ làm điện cực nền.*

### 1. Dụng cụ & Hóa chất
* Bột mài nhôm oxit $Al_2O_3$ cỡ hạt $0.05\text{ }\mu\text{m}$.
* Tấm nỉ mài phẳng phẳng chuyên dụng.
* Nước cất DI và cồn Ethanol tuyệt đối (HPLC grade).
* Thiết bị đo điện hóa (Potentiostat) cùng bình đo 3 điện cực.

### 2. Quy trình đánh bóng và hoạt hóa GCE
1. **Mài mịn bằng bột $Al_2O_3$:**
    * Nhỏ vài giọt nước cất và bột $Al_2O_3$ $0.05\text{ }\mu\text{m}$ lên tấm nỉ mài phẳng.
    * Đặt đứng vuông góc điện cực GCE 90° so với mặt nỉ, di chuyển mài nhẹ nhàng vẽ theo **hình số 8** liên tục trong **$2\text{ phút}$**.
    * Lặp lại thao tác 2 lần để loại bỏ màng polymer cũ.
2. **Siêu âm làm sạch bột mài:**
    * Cho điện cực GCE thẳng đứng vào cốc nước cất DI, tiến hành siêu âm làm sạch trong **$1\text{ phút}$** (thay nước cất DI, siêu âm lặp lại 3 lần).
    * Siêu âm tráng nhanh bằng cồn ethanol tuyệt đối trong **$1\text{ phút}$** để khử ẩm.
3. **Anodize kiềm hoạt hóa (Bắt buộc):**
    * Nhúng điện cực GCE đã siêu âm vào cốc chứa dung dịch **$NaOH$ $0.1\text{ M}$**.
    * Áp thế điện thế phân cực dương **$+1.8\text{ V}$ vs. $Ag/AgCl$ trong thời gian $10\text{ giây}$** để hòa tan triệt để các hạt alumina siêu nhỏ bám dính vật lý trong các lỗ xốp nano.
    * Rửa lại bằng nước cất DI.
4. **Kiểm tra độ sạch bằng phép quét thế tuần hoàn CV:**
    * Nhúng GCE sạch vào dung dịch redox probe: **$5.0\text{ mM } K_3Fe(CN)_6$ trong nền $0.1\text{ M } KCl$**.
    * Quét thế tuần hoàn CV ở tốc độ quét **$50\text{ mV/s}$** (quét 3 chu kỳ).
    * ✓ **Tiêu chí đạt chuẩn (Pass):** Thế hiệu đỉnh tách biệt giữa peak oxy hóa và peak khử **$\Delta E_p < 70\text{ mV}$** và tỷ số dòng điện đỉnh đối xứng **$I_{pa}/I_{pc} \approx 0.95 - 1.05$**. Nếu chưa đạt, bắt buộc phải đánh bóng lại.

---

## GIAI ĐOẠN 2: PHA CHẾ MỰC IN (Conductive Ink Formulation) & PHỦ ĐIỆN CỰC (Drop-casting)

### 1. Công thức phối trộn conductive ink (Nồng độ $5\text{ mg/mL}$)
* **Bột Carbon Aerogel ($N$-CA hoặc $Fe/N$-CA):** $5.0\text{ mg}$ (cân chính xác bằng cân phân tích).
* **Dung môi phân tán nền:** $950\text{ }\mu\text{L}$ DMF (Dimethylformamide).
* **Dung dịch Binder chuyên biệt:** $50\text{ }\mu\text{L}$ (Tổng thể tích Ink = $1000\text{ }\mu\text{L}$).

### 2. Quy hoạch Binder chuyên biệt theo chất phân tích:

| Dạng điện cực biến tính | Chất liên kết (Binder) sử dụng | Phép đo áp dụng |
| :--- | :--- | :--- |
| **Fe/N-CA / Chitosan/GCE** | **Chitosan $1\%$** trong dung dịch acid acetic $1\text{ vol}\%$. | Đo **SWASV kim loại nặng** trong đệm acetate $pH = 4.5$. |
| **N-CA-700 / Nafion/GCE** | **Nafion $0.25\%$** trong cồn ethanol. | Đo **DPV Paracetamol** trong đệm PBS $pH = 7.0 - 7.4$. |

### 3. Thực hiện phân tán siêu âm và Drop-casting
1. **Siêu âm phân tán mực:** Bọc kín bình chứa mực in. Đặt bình vào bể siêu âm nước đá lạnh (nhiệt độ duy trì **$< 15^\circ\text{C}$**). Tiến hành siêu âm liên tục trong **$30\text{ phút}$** ở chế độ siêu âm thường. Mực in thu được phải đen tuyền, đồng nhất.
2. **Drop-casting:** Dùng pipette vi lượng hút chính xác **$7.0\text{ }\mu\text{L}$** mực in. Nhỏ thật chậm, vuông góc trực tiếp lên trung tâm bề mặt điện cực GCE đã được dựng thẳng đứng trên giá đỡ.
3. **Sấy khô màng mỏng (Bắt buộc):**
    * Úp ngược một cốc thủy tinh sạch che bụi lên điện cực GCE, để màng khô tự nhiên hoàn toàn ở nhiệt độ phòng ($25^\circ\text{C}$) trong **$2 - 3\text{ giờ}$** trong tủ hút.
    * **⚠️ Cảnh báo cực đoan:** Tuyệt đối không sấy gia nhiệt nhanh, không thổi khí $N_2$ hoặc dùng đèn sưởi hồng ngoại, không sấy chân không để tránh hiệu ứng "vành cà phê" (coffee-ring) làm dồn toàn bộ bột carbon ra viền mép điện cực.

---

## GIAI ĐOẠN 3: SÀNG LỌC ĐIỆN CỰC NỀN TRƯỚC PHÂN TÍCH (Pre-electrode Baseline Screening)

Màng điện cực biến tính phải vượt qua các chỉ số baseline dưới đây trước khi đo mẫu thực tế:

1. **Quét thế tuần hoàn CV nền:** Quét thế tuần hoàn trong dung dịch **$5.0\text{ mM } K_3Fe(CN)_6 / 0.1\text{ M } KCl$**, tốc độ quét $50\text{ mV/s}$.
    * *Chỉ số Pass:* Cường độ dòng đỉnh $I_{pa}$ phải tăng **$\ge 30\%$** và thế đỉnh tách biệt **$\Delta E_p < 110\text{ mV}$** so với điện cực bare GCE.
2. **Trở kháng điện hóa EIS:** Đo phổ EIS trong dung dịch redox probe **$5.0\text{ mM } K_3Fe(CN)_6 / 0.1\text{ M } KCl$** (tần số quét từ $100\text{ kHz} \rightarrow 0.1\text{ Hz}$, biên độ sóng $10\text{ mV}$, áp thế tĩnh $E_{dc} = 0.22\text{ V}$ vs. $Ag/AgCl$).
    * *Chỉ số Pass:* Bán kính cung bán tròn trở kháng của mẫu $Fe/N$-CA phải thu hẹp **$\ge 35\%$** so với bare GCE ($R_{ct}\text{(Fe/N-CA)} < R_{ct}\text{(N-CA)} < R_{ct}\text{(bare GCE)}$).
3. **Diện tích điện hóa hiệu dụng (ECSA):** Quét CV trong dung dịch đệm ở nhiều tốc độ quét tăng dần ($25 \rightarrow 200\text{ mV/s}$) trong khoảng thế không Faraday ($0.0 \rightarrow 0.1\text{ V}$) để thu được dòng điện dung lớp kép ($C_{dl}$).

---

## GIAI ĐOẠN 4: THIẾT LẬP CHƯƠNG TRÌNH PHÂN TÍCH CẢM BIẾN ĐIỆN HÓA

### 1. Phép đo cảm biến Pb²⁺ bằng kỹ thuật sóng vuông hòa tan (SWASV)
* **WE sử dụng:** Điện cực $Fe/N$-CA / Chitosan/GCE.
* **Dung dịch điện ly nền:** Đệm Acetate $0.1\text{ M}$, $pH = 4.5$.
* **Các bước lập trình thiết bị (SWASV Program):**
  1. **Làm giàu khử (Pre-concentration):** Áp thế điện thế khử âm **$E_{\text{dep}} = -1.1\text{ V}$ vs. $Ag/AgCl$** trong thời gian **$t_{\text{dep}} = 120\text{ giây}$** dưới lực khuấy từ ổn định $400\text{ rpm}$ để khử các ion $Pb^{2+}$ thành $Pb^0$ tích lũy trên màng.
  2. **Thời gian cân bằng (Quiet time):** Tắt khuấy từ, để hệ điện cực đứng yên tĩnh lặng trong **$10\text{ giây}$** để ổn định dòng nền.
  3. **Hòa tan sóng vuông (Anodic Stripping):** Quét thế phân cực anode bằng sóng vuông ngược từ **$-1.4\text{ V}$ đến $-0.2\text{ V}$ vs. $Ag/AgCl$** để oxy hóa hòa tan chì tích lũy trở lại dung dịch ($Pb^0 \rightarrow Pb^{2+} + 2e^-$). Peak hòa tan xuất hiện ở khoảng thế $\approx -0.5\text{ V}$.
      * *Thông số sóng vuông:* SW frequency = **$25\text{ Hz}$** | SW amplitude = **$25\text{ mV}$** | Step potential = **$5\text{ mV}$**.
  4. **Làm sạch điện cực (Cleaning):** Áp thế dương **$+0.2\text{ V}$ trong $30\text{ giây}$** kết hợp khuấy từ tốc độ cao $600\text{ rpm}$ để giải phóng lượng kim loại còn sót lại, tránh hiện tượng nhiễm chéo mẫu.

### 2. Phép đo cảm biến Paracetamol bằng kỹ thuật xung vi phân (DPV)
* **WE sử dụng:** Điện cực $N$-CA-700 / Nafion/GCE.
* **Dung dịch điện ly nền:** Phosphate Buffered Saline (PBS) $0.1\text{ M}$, $pH = 7.0 - 7.4$.
* **Các bước lập trình thiết bị (DPV Program):**
  * Khoảng thế quét: Quét phân cực dương từ **$0.0\text{ V}$ đến $+0.8\text{ V}$ vs. $Ag/AgCl$**.
  * Tốc độ quét thế: $20\text{ mV/s}$.
  * *Thông số xung vi phân:* **Pulse amplitude = $50\text{ mV}$** | **Pulse width = $50\text{ ms}$** | **Step potential = $5\text{ mV}$**.
  * Phép đo được tiến hành quét trực tiếp, không áp thế làm giàu điện hóa ($E_{\text{dep}}$). Peak oxy hóa Paracetamol xuất hiện rõ nét ở $\approx +0.34\text{ V}$ vs. $Ag/AgCl$.

---

## GIAI ĐOẠN 5: THIẾT LẬP MODULE ĐO ĐẶC TÍNH ĐIỆN HÓA BỔ TRỢ ĐỒNG DẠNG (ORR & Siêu Tụ Điện)

### 1. Phép đo Xúc tác khử Oxy (ORR) làm "Proof of Concept" chứng minh tâm Fe-N₄
* **WE sử dụng:** Điện cực $Fe/N$-CA / Chitosan/GCE.
* **Điện ly nền:** Dung dịch **$KOH$ $0.1\text{ M}$**.
* **Quy trình đo đạc:**
  1. Thổi khí $N_2$ sục liên tục vào bình điện giải $KOH$ $0.1\text{ M}$ trong $30\text{ phút}$ để đuổi sạch oxy. Tiến hành chạy quét thế CV từ **$-1.0\text{ V}$ đến $+0.2\text{ V}$ vs. $Ag/AgCl$** ở tốc độ quét $50\text{ mV/s}$. CV thu được là đường nền phẳng, đại diện dòng dung.
  2. Chuyển sang sục liên tục khí $O_2$ trong $30\text{ phút}$ để bão hòa oxy. Chạy quét thế CV tương tự. Đường phổ CV bắt buộc phải xuất hiện một peak khử oxy cực kỳ sắc nét ở thế dương hơn **$-0.2\text{ V}$ vs. $Ag/AgCl$** với cường độ dòng đỉnh khử đạt **$I_c \ge 1.0\text{ mA/cm}^2$**.
  3. Đo linear sweep voltammetry (LSV) trên điện cực quay RDE ở các tốc độ quay từ $400\text{ rpm}$ đến $3600\text{ rpm}$ để tính toán số electron chuyển tải ($n \approx 3.14 - 3.69$ tiệm cận cơ chế 4 electron).

### 2. Phép đo Siêu tụ điện hóa (Supercapacitor) của mẫu đối chứng NaOH-Urea
* **WE sử dụng:** Mẫu carbon $NaOH$-Urea ép viên drop-cast.
* **Điện ly nền:** Dung dịch **$KOH$ $6.0\text{ M}$** siêu đậm đặc.
* **Quy trình đo đạc:**
  1. Chạy CV trong $KOH$ $6.0\text{ M}$ ở các tốc độ quét từ $5 - 100\text{ mV/s}$ trong khoảng thế tĩnh từ $-1.0\text{ V} \rightarrow 0.0\text{ V}$ vs. $Ag/AgCl$. Đường CV thu được dạng hình hộp chữ nhật đối xứng.
  2. Đo phóng nạp dòng hằng GCD ở các mật độ dòng từ $0.5 - 10\text{ A/g}$. Đường phóng nạp GCD phải có dạng tam giác cân đối xứng, xác định điện dung riêng cụ thể ($C_s\text{ F/g}$).
