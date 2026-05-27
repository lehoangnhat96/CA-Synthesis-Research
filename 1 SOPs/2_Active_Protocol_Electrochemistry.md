# 2_Active_Protocol_Electrochemistry.md — Quy Trình Chế Tạo Điện Cực & Đo Đạc Điện Hóa Phân Tích

> [!NOTE]
> * Quy trình thực nghiệm liên hợp: [1_Active_Protocol_Synthesis.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/1_Active_Protocol_Synthesis.md)
> * Cơ sở lý thuyết bổ trợ: [3_Literature_Review_and_Gap_Analysis.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/3_Literature_Review_and_Gap_Analysis.md)
> * Cẩm nang bóc tách đỉnh phổ: [4_Material_Characterization_Guide.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/4_Material_Characterization_Guide.md)

---

## GIAI ĐOẠN 1: HOẠT HÓA BỀ MẶT ĐIỆN CỰC LÀM VIỆC (GCE Polishing & Anodizing)

*Áp dụng đối với điện cực carbon thủy tinh (Glassy Carbon Electrode - GCE) đường kính hình học Ø = 3 mm, diện tích làm việc hiệu dụng $A \approx 0.0707\text{ cm}^2$ làm điện cực nền.*

### 1. Hóa chất & Dụng cụ
* Bột mài nhôm oxit Al₂O₃ siêu mịn (dải cỡ hạt từ 1.0 µm $\rightarrow$ 0.3 µm $\rightarrow$ 0.05 µm).
* Tấm nỉ mài phẳng sạch chuyên dụng.
* Nước cất DI và cồn Ethanol tuyệt đối (HPLC grade).
* Thiết bị đo điện hóa (Potentiostat) cùng bình đo 3 điện cực.

### 2. Quy trình đánh bóng và làm sạch GCE
1. **Mài mịn bằng bột Al₂O₃:** Nhỏ vài giọt nước cất lên tấm nỉ mài phẳng, rắc một lượng nhỏ bột Al₂O₃ cỡ hạt 0.05 µm lên. Đặt đứng vuông góc điện cực GCE 90° so với mặt nỉ, di chuyển mài nhẹ nhàng vẽ theo **hình số 8** liên tục trong **2 phút**. Lặp lại thao tác 2 lần để loại bỏ hoàn toàn màng polymer cũ hoặc lớp oxit thụ động bề mặt.
2. **Siêu âm làm sạch bột mài:** Cho điện cực GCE thẳng đứng vào cốc nước cất DI, tiến hành siêu âm làm sạch trong **1 phút** để đẩy các hạt Al₂O₃ bám dính cơ học ra khỏi bề mặt. Thay nước cất DI mới, siêu âm tiếp **1 phút** (lặp lại 3 lần). Siêu âm tráng nhanh bằng cồn ethanol tuyệt đối trong **1 phút** để khử ẩm.
3. **Anodize NaOH loại bỏ cặn alumina tàn dư (Bắt buộc):** Nhúng điện cực GCE đã siêu âm vào cốc chứa dung dịch NaOH 0.1M. Áp thế điện thế phân cực dương **+1.8 V vs. Ag/AgCl trong thời gian 10 giây**. 
   * *Ý nghĩa biện luận:* Alumina ($Al_2O_3$) là oxit lưỡng tính. Việc anodize ở thế dương cực cao trong môi trường kiềm mạnh giúp hòa tan hóa học triệt để các hạt alumina siêu nhỏ còn kẹt cứng trong các khe/lỗ xốp nano của carbon thủy tinh, giải phóng hoàn toàn bề mặt hoạt tính trơn sạch của GCE. Rửa lại bằng nước cất DI.
4. **Kiểm tra độ sạch bằng phép quét thế tuần hoàn CV:**
   * Nhúng GCE sạch vào dung dịch redox probe tiêu chuẩn: **5.0 mM K₃Fe(CN)₆ trong nền 0.1M KCl**.
   * Quét thế tuần hoàn CV ở tốc độ quét **50 mV/s** (quét 3 chu kỳ).
   * ✓ **Tiêu chí đạt chuẩn (Pass):** Thế hiệu đỉnh tách biệt giữa peak oxy hóa và peak khử **$\Delta E_p < 70\text{ mV}$** và tỷ số dòng điện đỉnh đối xứng **$I_{pa}/I_{pc} \approx 0.95 - 1.05$**. Nếu chưa đạt, bắt buộc phải tiến hành đánh bóng lại bằng bột Al₂O₃ 0.05 µm.

---

## GIAI ĐOẠN 2: PHA CHẾ MỰC IN (Conductive Ink Formulation) & PHỦ ĐIỆN CỰC (Drop-casting)

*Conductive Ink được thiết kế tối ưu hóa độ dày và bám dính màng mỏng, phân chia binder chuyên biệt theo bản chất của từng chất phân tích điện hóa:*

### 1. Công thức phối trộn conductive ink (Nồng độ bột carbon aerogel = 5 mg/mL)
* **Khối lượng bột Carbon Aerogel (N-CA hoặc Fe/N-CA):** 5.0 mg (cân chính xác bằng cân vi lượng phân tích $\pm 0.01\text{ mg}$).
* **Dung môi phân tán nền:** 950 µL DMF (Dimethylformamide, HPLC grade) hoặc hỗn hợp Nước DI : Ethanol (tỷ lệ 1:1 v/v).
* **Thể tích dung dịch Binder thêm vào:** 50 µL dung dịch keo liên kết chuyên biệt (Tổng thể tích Ink = 1000 µL).

### 2. Chiến lược lựa chọn Binder chuyên biệt cho từng phép đo:

| Dạng điện cực biến tính | Chất liên kết (Binder) sử dụng | Vai trò xúc tác / Phép đo áp dụng |
| :--- | :--- | :--- |
| **Fe/N-CA / Chitosan/GCE** | **Chitosan 1%** trong dung dịch acid acetic 1% v/v. | • Nhóm amino ($-NH_2$) tự do của Chitosan bị proton hóa tạo điện tích dương trong đệm acetate pH 4.5, hoạt động như phối tử chelating mạnh mẽ bắt giữ cation $Pb^{2+}$, làm giàu nồng độ chì cục bộ cực cao sát bề mặt GCE trước khi quét.<br>• Sử dụng cho phép đo **SWASV kim loại nặng**. |
| **N-CA-700 / Nafion/GCE** | **Nafion 0.25%** trong cồn ethanol. | • Nafion tạo màng trao đổi cation mỏng, kỵ nước bền vững, đẩy các anion gây nhiễu (axit uric, axit ascorbic) ra xa điện cực, đồng thời ngăn chặn hiện tượng bám dính (fouling) do sản phẩm oligomer hóa paracetamol bít các hoạt tính.<br>• Sử dụng cho phép đo **DPV Paracetamol**. |

### 3. Thực hiện phân tán siêu âm và Drop-casting
1. **Siêu âm phân tán mực:** Bọc kín bình chứa mực in. Đặt bình vào bể siêu âm nước đá lạnh (nhiệt độ bể siêu âm duy trì **< 15°C**). Tiến hành siêu âm liên tục trong **30 phút** ở chế độ siêu âm thường (không dùng đầu probe công suất cao để tránh làm đứt gãy mạch polymer Chitosan/Nafion và làm bay hơi dung môi). Mực in thu được phải đen tuyền, đồng nhất và hoàn toàn không bị lắng cặn sau 30 phút tĩnh.
2. **Drop-casting:** Dùng pipette vi lượng hút chính xác **7.0 µL** mực in. Nhỏ thật chậm, vuông góc trực tiếp lên trung tâm bề mặt điện cực GCE đã được dựng thẳng đứng trên giá đỡ.
3. **Sấy khô màng mỏng:** 
   * **Bắt buộc:** Úp ngược một cốc thủy tinh sạch che bụi lên điện cực GCE đã nhỏ mực, để màng khô tự nhiên hoàn toàn ở nhiệt độ phòng (25°C) trong **2–3 giờ** trong tủ hút khí độc.
   * **⚠️ Cảnh báo cực đoan:** Tuyệt đối không sấy gia nhiệt nhanh, không thổi khí N₂ hoặc dùng đèn sưởi hồng ngoại ở giai đoạn này. Sự bay hơi quá nhanh của DMF sẽ gây ra hiệu ứng "vành cà phê" (coffee-ring effect), làm dồn toàn bộ bột carbon ra viền mép điện cực và để rỗng tâm, phá hủy độ bền cơ học và tính tái lặp điện hóa của màng. Tuyệt đối không sấy trong tủ sấy chân không vì áp suất thấp làm dung môi sôi nổ bọt phá hỏng liên kết màng.

---

## GIAI ĐOẠN 3: SÀNG LỌC ĐIỆN CỰC NỀN TRƯỚC PHÂN TÍCH (Pre-electrode Baseline Screening)

*Màng điện cực biến tính phải vượt qua bộ 4 chỉ số baseline dưới đây để đảm bảo chất lượng truyền dẫn điện tích trước khi đo mẫu phân tích thực tế:*

1. **Quét thế tuần hoàn CV nền:** Quét thế tuần hoàn trong dung dịch **5.0 mM K₃Fe(CN)₆ / 0.1M KCl**, tốc độ quét 50 mV/s.
   * *Chỉ số Pass:* Cường độ dòng đỉnh $I_{pa}$ phải tăng $\ge 30\%$ và thế đỉnh tách biệt $\Delta E_p < 110\text{ mV}$ chứng minh diện tích hoạt tính tăng và màng dẫn điện thông suốt.
2. **Trở kháng điện hóa EIS:** Đo phổ EIS trong dung dịch redox probe **5.0 mM K₃Fe(CN)₆ / 0.1M KCl** (tần số quét từ $100\text{ kHz} \rightarrow 0.1\text{ Hz}$, biên độ sóng hình sin $10\text{ mV}$, áp thế tĩnh $E_{dc} = 0.22\text{ V}$ vs. Ag/AgCl).
   * *Chỉ số Pass:* Đường cong Nyquist phải thể hiện điện trở truyền điện tích của Fe/N-CA nhỏ hơn N-CA và bare GCE ($R_{ct}\text{(Fe/N-CA)} < R_{ct}\text{(N-CA)} < R_{ct}\text{(bare GCE)}$). Tức bán kính cung bán tròn trở kháng của mẫu Fe/N-CA phải thu hẹp $\ge 35\%$ chứng minh sự có mặt của tâm sắt hoạt tính tăng cường chuyển tải electron cực nhanh.
3. **Diện tích điện hóa hiệu dụng (ECSA):** Quét CV trong dung dịch đệm ở nhiều tốc độ quét tăng dần ($25 \rightarrow 200\text{ mV/s}$) trong khoảng thế không có phản ứng Faraday ($0.0 \rightarrow 0.1\text{ V}$) để thu được dòng điện dung lớp kép ($C_{dl}$), tính toán diện tích ECSA phục vụ biện luận cơ chế.

---

## GIAI ĐOẠN 4: THIẾT LẬP CHƯƠNG TRÌNH PHÂN TÍCH CẢM BIẾN ĐIỆN HÓA

### 1. Phép đo cảm biến Pb²⁺ bằng kỹ thuật sóng vuông hòa tan (SWASV)
* **WE sử dụng:** Điện cực Fe/N-CA / Chitosan/GCE (mẫu nung 800°C đã acid leaching và annealing lần 2).
* **Dung dịch điện ly nền:** Đệm Acetate pH 4.5 (Pha từ hỗn hợp dung dịch axit axetic 0.1M và natri axetat 0.1M).
* **Các bước lập trình thiết bị (SWASV Program):**
  1. **Làm giàu điện hóa (Pre-concentration):** Áp thế điện thế khử âm **$E_{dep} = -1.1\text{ V}$** vs. Ag/AgCl trong thời gian **$t_{dep} = 120\text{ s}$** dưới lực khuấy từ ổn định 400 rpm để khử các ion $Pb^{2+}$ thành kim loại chì $Pb^0$ bám dính tích lũy trên màng điện cực.
  2. **Thời gian cân bằng (Quiet time):** Tắt khuấy từ bể đo, để hệ điện cực đứng yên tĩnh lặng trong **10 giây** để ổn định dòng nền dung dịch.
  3. **Hòa tan sóng vuông (Anodic Stripping):** Quét thế phân cực anode bằng sóng vuông (SWV) ngược từ **-1.4 V đến -0.2 V** vs. Ag/AgCl để oxy hóa hòa tan chì tích lũy trở lại dung dịch ($Pb^0 \rightarrow Pb^{2+} + 2e^-$). Tín hiệu peak cực đại của chì xuất hiện ở khoảng thế $\approx -0.5\text{ V}$.
     * *Thông số sóng vuông:* SW frequency = **25 Hz** | SW amplitude = **25 mV** | Step potential = **5 mV**.
  4. **Làm sạch điện cực (Cleaning):** Áp thế dương **+0.2 V trong 30 giây** kết hợp khuấy từ tốc độ cao 600 rpm để giải phóng hoàn toàn lượng kim loại nặng còn sót lại khỏi màng điện cực trước khi thực hiện chu kỳ quét tiếp theo, tránh hiện tượng nhiễm chéo mẫu.

### 2. Phép đo cảm biến Paracetamol bằng kỹ thuật xung vi phân (DPV)
* **WE sử dụng:** Điện cực N-CA-700 / Nafion/GCE (mẫu carbon hóa 700°C).
* **Dung dịch điện ly nền:** Phosphate Buffered Saline (PBS) pH 7.0–7.4 (Pha từ dung dịch đệm muối phosphat $Na_2HPO_4 / NaH_2PO_4$ 0.1M).
* **Các bước lập trình thiết bị (DPV Program):**
  * Khoảng thế quét: Quét phân cực dương từ **0.0 V đến +0.8 V** vs. Ag/AgCl.
  * Tốc độ gia nhiệt quét thế: 20 mV/s.
  * *Thông số xung vi phân:* **Pulse amplitude = 50 mV** | **Pulse width = 50 ms** | **Step potential = 5 mV**.
  * Phép đo được tiến hành quét trực tiếp, hoàn toàn không cần bước áp thế làm giàu điện hóa ($E_{dep}$). Peak oxy hóa Paracetamol xuất hiện rõ nét ở $\approx +0.34\text{ V}$ vs Ag/AgCl.

---

## GIAI ĐOẠN 5: THIẾT LẬP MODULE ĐO ĐẶC TÍNH ĐIỆN HÓA BỔ TRỢ ĐỒNG DẠNG (ORR & Siêu Tụ Điện)

*Để hoàn thiện luận văn điện hóa có chiều sâu học thuật cao nhất, tiến hành chạy hai module đo đạc đặc tính đối chứng đồng dạng dưới đây:*

### 1. Phép đo Xúc tác khử Oxy (ORR) làm "Proof of Concept" chứng minh tâm Fe-N₄
* **Ý nghĩa:** ORR là phản ứng điện hóa chị em có cấu trúc hoạt tính $Fe-N_4$ tương đồng tuyệt đối với cảm biến Pb²⁺ và Paracetamol. Việc chứng minh vật liệu có hoạt tính ORR xuất sắc là bằng chứng thép khẳng định sự tồn tại của các tâm xúc tác đơn nguyên tử hoạt tính cao.
* **WE sử dụng:** Bột Fe/N-CA trộn PVDF làm binder drop-cast lên GCE (hoặc có thể dùng trực tiếp điện cực Chitosan để đo kiểm tra).
* **Điện ly nền:** Dung dịch **KOH 0.1 M** (pha loãng từ KOH rắn chuẩn tinh khiết).
* **Quy trình đo đạc:**
  1. Thổi khí khí Nitơ ($N_2$) sục liên tục vào bình điện giải KOH 0.1M trong 30 phút để đuổi sạch oxy. Tiến hành chạy quét thế CV từ **-1.0 V đến +0.2 V** vs. Ag/AgCl ở tốc độ quét 50 mV/s. CV nền thu được phải là một đường dung dung phẳng phẳng, hoàn toàn không có peak Faraday.
  2. Chuyển sang sục liên tục khí Oxy ($O_2$) trong 30 phút để bão hòa oxy. Chạy quét thế CV tương tự. Đường phổ CV bắt buộc phải xuất hiện một peak khử oxy cực kỳ sắc nét ở thế dương hơn **-0.2 V vs Ag/AgCl** với cường độ dòng đỉnh $I_c \ge 1.0\text{ mA/cm}^2$.
  3. Đo linear sweep voltammetry (LSV) trên điện cực quay RDE ở các tốc độ quay từ 400 rpm đến 3600 rpm để tính toán số electron chuyển tải ($n \approx 3.14 - 3.69$ tiến gần cơ chế 4 electron sạch).

### 2. Phép đo Siêu tụ điện hóa (Supercapacitor) của mẫu đối chứng NaOH-Urea
* **Ý nghĩa:** Kiểm chứng đặc tính lưu trữ dung lượng lớp kép điện dịch (EDLC) của mẫu nung NaOH-Urea vốn bị Na-etching ăn mòn vách tạo lỗ xốp lớn tơi xốp, thích hợp làm tụ điện hóa.
* **WE sử dụng:** Mẫu carbon NaOH-Urea ép viên conductive carbon hoặc drop-cast.
* **Điện ly nền:** Dung dịch **KOH 6.0 M** siêu đậm đặc.
* **Quy trình đo đạc:**
  1. Chạy CV trong KOH 6.0M ở các tốc độ quét từ $5 \rightarrow 100\text{ mV/s}$ trong khoảng thế tĩnh từ $-1.0\text{ V} \rightarrow 0.0\text{ V}$ vs. Ag/AgCl. Đường CV thu được phải có dạng **hình hộp chữ nhật đối xứng chuẩn** đại diện cho điện dung lớp kép lý tưởng.
  2. Đo phóng nạp dòng hằng GCD ở các mật độ dòng từ $0.5 \rightarrow 10\text{ A/g}$. Đường phóng nạp GCD phải có dạng tam giác cân đối xứng, xác định điện dung riêng cụ thể ($C_s\text{ F/g}$) để viết phần biện luận đối chứng cho luận văn.
