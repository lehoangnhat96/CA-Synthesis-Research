# SYNTHESIS PARAMETERS — Fe/N Co-doped Carbon Aerogel Biosensor
# Nguồn: Xơ dừa Bến Tre | IUH TPHCM | Hóa Phân tích
# Sample set: N-CA-700 và Fe/N-CA-800
# Bản chuẩn hóa: ghép nối synthesis parameters + CA characterization biosensor

---

## 0. PHẠM VI & LOGIC CHUẨN HÓA

Tài liệu này chuẩn hóa quy trình tổng hợp và đánh giá vật liệu **N-doped carbon aerogel (N-CA)** và **Fe/N co-doped carbon aerogel (Fe/N-CA)** từ **xơ dừa Bến Tre** cho hướng **điện cực phân tích điện hóa / biosensor**.

Chuỗi nhân quả chính:

**Tiền xử lý xơ dừa → Sol-gel NH₃/Urea/H₂O → Gel/hydrogel tổ ong → Trao đổi dung môi & sấy thăng hoa → Nhiệt phân → Fe impregnation → Acid leaching & annealing → Màng điện cực GCE → CV/EIS baseline → DPV/SWASV sensing.**

Ghi chú thuật ngữ:
- Nếu hệ chưa dùng enzyme, antibody, aptamer, DNA probe hoặc thành phần nhận diện sinh học, thuật ngữ chính xác hơn là **electrochemical sensor**.
- Nếu sau này có thành phần nhận diện sinh học, có thể dùng **biosensor**.

---

## 1. TIỀN XỬ LÝ KIỀM (Alkali Pretreatment)

- Hóa chất: NaOH 5–6 wt%
- Nhiệt độ: 75–80°C
- Thời gian: 2–4h
- Khuấy: liên tục bằng máy khuấy từ + khuấy tay 20–30 phút
- Yêu cầu: xơ dừa phải được nghiền trước khi xử lý
- Không tẩy trắng: **no bleaching**
- Ràng buộc hình thái: giữ lại cấu trúc phân cấp và nhóm chức dị tố tự nhiên của xơ dừa
- Dữ liệu gốc bắt buộc: sấy 105°C và cân khối lượng trước/sau xử lý
- Output: **gravimetric weight-loss** của xơ dừa Bến Tre

Công thức ghi nhận hao hụt khối lượng:

$$
\text{Weight loss}(\%) = \frac{m_0 - m_1}{m_0} \times 100
$$

Trong đó:
- $m_0$: khối lượng xơ dừa khô trước xử lý kiềm
- $m_1$: khối lượng xơ dừa khô sau xử lý kiềm

Ý nghĩa:
- NaOH loại một phần lignin/hemicellulose, làm lộ cellulose và tăng khả năng tạo gel.
- Không tẩy trắng giúp tránh phá hủy quá mức cấu trúc sinh khối, từ đó giữ lợi thế cấu trúc phân cấp cho carbon aerogel.
- Dữ liệu hao hụt khối lượng là **Original Data Contribution**, vì hiện chưa có benchmark định lượng riêng cho xơ dừa Bến Tre.

---

## 2. TỔNG HỢP SOL-GEL & ĐÁNH SIÊU ÂM (Sol-gel Preparation & Sonication)

Quy chiếu chính: doi:10.1021/acs.iecr.0c03771

Hệ dung môi: **NH₃ 25% : Urea : H₂O**

Tuyệt đối không dùng hệ **NaOH:Urea**.

Công thức chuẩn:

| Thành phần | Lượng dùng |
|---|---:|
| Cellulose pulp | 1 g |
| NH₃ 25% | 11 mL |
| Urea | 4 g |
| H₂O | 5 mL |
| Tổng dung môi | 16 mL |
| Tỷ lệ rắn/lỏng | 1 g : 16 mL |

Thứ tự thêm:

**NH₃ 25% → Urea → H₂O → Cellulose pulp**

Điều kiện siêu âm:

| Thông số | Giá trị chuẩn |
|---|---:|
| Thời gian siêu âm | 30 phút |
| Chế độ | Pulse 2s on / 1s off |
| Kiểm soát nhiệt | Ice bath ≤10°C |
| Vùng an toàn ưu tiên | 0–5°C |
| Dấu hiệu đạt | Sol đồng nhất, không còn sợi xơ thô |

Cơ chế kiểm soát:
- NH₃ là nguồn môi trường kiềm và liên quan đến N-doping.
- Khi siêu âm, nhiệt sinh ra có thể làm NH₃ bay hơi.
- Nếu NH₃ bay hơi, nồng độ hệ thay đổi, làm giảm khả năng N-doping và làm sai lệch tính tái lặp.
- Vì vậy, bể đá là điều kiện bắt buộc, không phải tùy chọn.

---

## 3. ĐÚC KHUÔN & GEL HÓA (Casting & Gelation)

- Khuôn: silicone hoặc ống PP
- Không dùng: khuôn thủy tinh
- Nhiệt độ khuôn: 0–5°C trước khi rót sol
- Sau khi rót: để yên 30–60 phút để ổn định hình dạng ban đầu
- Gel hóa chính: giữ ở −5°C trong 24h
- Output: hydrogel dạng mạng tổ ong

Ý nghĩa:
- Gel hóa lạnh làm chậm động học kết tụ, giúp mạng cellulose–urea hình thành đều hơn.
- Cấu trúc hydrogel là tiền đề để tạo macropore/mesopore sau sấy thăng hoa và nhiệt phân.

---

## 4. TRAO ĐỔI DUNG MÔI & SẤY THĂNG HOA (Solvent Exchange & Freeze Drying)

Bước này bắt buộc để tránh sụp đổ mạng lưới 3D.

### 4.1 Đông tụ / Coagulation

| Thông số | Giá trị chuẩn |
|---|---:|
| Môi trường | Ethanol 98% |
| Tỷ lệ | 15 mL ethanol / 1 mL gel |
| Nhiệt độ ethanol | 0–5°C |
| Thời gian chuẩn | 24h |
| Backup an toàn | 36–48h nếu gel yếu hoặc còn co rút |
| Thay ethanol | Có thể thay sau 24h nếu kéo dài 36–48h |

### 4.2 Rửa trôi / Washing

- Gạn bỏ ethanol dư
- Thay bằng nước DI
- Ngâm 24h
- Thay nước 1–2 lần
- Không rửa quá nhiều lần để tránh rửa trôi quá mức phần urea còn liên quan đến N-doping

### 4.3 Sấy thăng hoa / Freeze Drying

- Cấp đông mẫu: −20°C, tối thiểu 12h
- Sau đó đưa vào thiết bị freeze dryer
- Không dùng sấy nhiệt
- Thông số áp suất/thời gian phụ thuộc thiết bị lab, nhưng phải ghi lại trong notebook thí nghiệm

Cơ chế:
- Sấy nhiệt làm dung môi bay hơi qua pha lỏng–khí, sinh lực mao quản lớn và kéo sập mạng gel.
- Freeze drying loại dung môi qua thăng hoa, giảm lực mao quản và bảo toàn cấu trúc 3D.

---

## 5. NHIỆT PHÂN (Pyrolysis)

Môi trường: N₂

| Giai đoạn khí | Thông số |
|---|---:|
| Purge trước nung | 150–200 mL/min trong 30 phút |
| Lưu lượng khi nung/làm mát | 100 mL/min |
| Làm mát | Tự nhiên trong lò, duy trì N₂ |

Chương trình nhiệt:

| Ramp | Chương trình | Tốc độ | Giữ nhiệt |
|---|---|---:|---:|
| Ramp 1 | 25 → 150°C | 5°C/min | 30 phút |
| Ramp 2 | 150 → 400°C | 5°C/min | 30 phút |
| Ramp 3 | 400°C → $T_{target}$ | 5°C/min | 2h |

$T_{target}$:

| Mẫu | Nhiệt độ nhiệt phân |
|---|---:|
| N-CA | 700°C |
| Fe/N-CA nền | 800°C |

Ý nghĩa:
- 700°C giữ được nhiều nhóm N và defect hơn, phù hợp với nhánh paracetamol.
- 800°C tăng độ dẫn và độ ổn định carbon, phù hợp làm nền cho Fe/N active sites.

---

## 6. DOPING Fe — CHỈ ÁP DỤNG CHO Fe/N-CA

Phương pháp: **Post-impregnation** trong ethanol sau khi đã có aerogel.

Tuyệt đối không thêm Fe trực tiếp vào hệ NH₃/Urea/H₂O vì có nguy cơ tạo Fe(OH)₃ và phá hỏng hệ sol-gel.

| Thông số | Giá trị chuẩn |
|---|---:|
| Tiền chất | FeCl₃·6H₂O |
| Khối lượng phân tử | 270.3 g/mol |
| Dung môi | Ethanol |
| Nồng độ khảo sát | 1% và 5% Fe theo khối lượng mẫu |
| Thời gian ngâm | 24h |
| 30 phút đầu | Siêu âm nhẹ |
| Thời gian còn lại | Khuấy từ chậm |
| Sấy sau tẩm | 60°C |

Công thức tính lượng FeCl₃·6H₂O:

$$
m_{\mathrm{FeCl_3\cdot 6H_2O}}
=
m_{\mathrm{sample}}
\times w_{\mathrm{Fe}}
\times
\frac{270.3}{55.845}
$$

Ví dụ với 1.000 g mẫu:

| Mức Fe mục tiêu | Khối lượng Fe nguyên tố | FeCl₃·6H₂O cần cân |
|---:|---:|---:|
| 1 wt% Fe | 0.0100 g | 0.0484 g |
| 5 wt% Fe | 0.0500 g | 0.242 g |

Ghi chú thiết kế mẫu:
- Nếu báo cáo đúng nghĩa “2 vật liệu”, Fe 1% và Fe 5% nên là khảo sát tối ưu nội bộ, sau đó chọn mẫu tốt nhất làm Fe/N-CA chính.
- Nếu báo cáo toàn bộ dữ liệu, bộ mẫu thực tế sẽ là: N-CA-700, Fe/N-CA-1%, Fe/N-CA-5%.

---

## 7. HẬU XỬ LÝ — CHỈ ÁP DỤNG CHO Fe/N-CA

### 7.1 Acid Leaching

| Thông số | Giá trị chuẩn |
|---|---:|
| Acid | HCl 0.5M |
| Nhiệt độ | 80°C |
| Thời gian | 8h |
| Sau xử lý | Lọc → rửa DI water → sấy 60°C/12h |
| Mục đích | Rửa trôi Fe tự do, Fe oxide hoặc Fe₃C không hoạt tính |

### 7.2 Annealing lần 2

| Thông số | Giá trị chuẩn |
|---|---:|
| Khí | N₂ |
| Tốc độ gia nhiệt | 5°C/min |
| $T_{anneal}$ | 750°C |
| Thời gian giữ | 1h |
| Làm mát | Tự nhiên trong N₂ |
| Kiểm chứng bắt buộc | Raman $I_D/I_G$ ngay sau annealing |

Cơ chế:
- Acid leaching loại Fe không phối trí, giúp giảm nhiễu và giảm nguy cơ peak giả.
- Annealing lần 2 cung cấp đủ năng lượng để ổn định tâm Fe–Nₓ và phục hồi một phần mạng sp² carbon.
- 750°C thấp hơn nhiệt phân nền 800°C, nhờ đó hạn chế phá vỡ cấu trúc xốp đã hình thành.

---

## 8. CÔNG THỨC MỰC IN & CHẾ TẠO ĐIỆN CỰC (Electrode Fabrication)

Nội suy từ hệ tương đương: doi:10.3390/s24092787

| Thông số | Giá trị chuẩn |
|---|---:|
| Nền điện cực | Glassy Carbon Electrode, GCE |
| Đường kính GCE | 3 mm |
| Diện tích hình học | 0.0707 cm² |
| Nồng độ mực | 5 mg vật liệu / 1 mL dung môi |
| Dung môi phân tán | Nước:cồn hoặc DMF |
| Siêu âm mực | Ít nhất 1h |
| Binder 1 | Chitosan 1% trong acid acetic 1% |
| Binder 2 | Nafion 117 |
| Tỷ lệ Nafion | Ink:Nafion = 40:1 v/v |
| Drop-casting | 5–8 µL |
| Sấy màng | Tự nhiên hoặc dưới đèn hồng ngoại |

Loading ước tính:

| Thể tích drop | Khối lượng vật liệu CA | Loading trên GCE |
|---:|---:|---:|
| 5 µL | 25 µg | 0.354 mg/cm² |
| 8 µL | 40 µg | 0.566 mg/cm² |

Cơ chế tối ưu:
- Loading quá thấp làm tín hiệu yếu vì số active sites ít.
- Loading quá cao làm màng dày, tăng điện trở khuếch tán và background current.
- Vì vậy 5–8 µL là vùng khởi đầu hợp lý trước khi tối ưu.

---

## 9. PRE-ELECTRODE SCREENING

Trước khi chế tạo điện cực chính thức, cần sàng lọc vật liệu để tránh tốn thời gian đo sensor trên mẫu không đạt.

| Kỹ thuật | Thông số | Tiêu chí mục tiêu |
|---|---|---|
| Raman | $I_D/I_G$ | 0.9–1.2 |
| Độ dẫn điện pellet | $\sigma = L/(R \times A)$ | > 1 S/cm |
| Contact angle | Độ thấm ướt | < 90° |
| Dispersibility | Phân tán trong ethanol/nước | Không vón rõ sau 30 phút |

Ý nghĩa:
- Raman loại mẫu có defect quá cao hoặc graphite hóa quá mức.
- Độ dẫn điện loại mẫu carbon hóa kém.
- Contact angle và dispersibility dự đoán khả năng tạo màng điện cực ổn định.

---

## 10. ĐẶC TRƯNG VẬT LIỆU CARBON AEROGEL

### 10.1 Nhóm A — Hình thái & Cấu trúc vật lý

| Kỹ thuật | Thông số đo | Giá trị mục tiêu |
|---|---|---|
| SEM | Hình thái bề mặt, kích thước lỗ xốp, cấu trúc tổ ong | Macropore liên thông, hierarchical |
| TEM | Cấu trúc lớp carbon, phân bố Fe | Lớp carbon mỏng, Fe phân tán đều |
| BET, N₂ 77K | $S_{BET}$ | > 300 m²/g; cạnh tranh > 400 m²/g |
| BJH | $V_{meso}$, $D_{pore}$ | Mesopore 2–50 nm; $V_{meso} > 0.3$ cm³/g |
| TGA | Độ bền nhiệt, % tro | Tro < 5% |

Nguồn DOI: doi:10.3390/mi14091688; doi:10.3390/s24092787

### 10.2 Nhóm B — Thành phần hóa học bề mặt

| Kỹ thuật | Thông số đo | Giá trị mục tiêu |
|---|---|---|
| XPS survey | C at%, N at%, O at%, Fe at% | N 3–6 at%; Fe 1–3 at%; N:Fe ≥ 4:1 |
| XPS N 1s | Pyridinic-N, pyrrolic-N, graphitic-N | Pyridinic-N chiếm tỷ lệ cao nhất |
| XPS Fe 2p | Fe²⁺/Fe³⁺, Fe–Nₓ | Có tín hiệu Fe–Nₓ |
| XPS C 1s | sp² C, C–N, C–O | sp² C > 60% |
| FTIR | –OH, C=N, C–N, C–O | Xác nhận N-doping và nhóm chức hoạt động |

Nguồn DOI: doi:10.1021/acs.iecr.0c03771; doi:10.1021/acsomega.3c09297

### 10.3 Nhóm C — Cấu trúc carbon & mức độ graphite hóa

| Kỹ thuật | Thông số đo | Giá trị mục tiêu |
|---|---|---|
| Raman | D-band ~1340 cm⁻¹, G-band ~1579 cm⁻¹ | Xác nhận cấu trúc carbon |
| Raman | $I_D/I_G$ | 0.9–1.2 |
| Raman | 2D-band ~2700 cm⁻¹ | Đánh giá mức độ graphene hóa |
| XRD | Peak (002) ~26°, (100) ~43° | Bán tinh thể, không cần graphite hóa hoàn toàn |

Nguồn DOI: doi:10.3390/nano13050817

### 10.4 Nhóm D — Tính chất điện & bề mặt

| Kỹ thuật | Thông số đo | Giá trị mục tiêu |
|---|---|---|
| 4-point probe hoặc pellet | Độ dẫn điện $\sigma$ | > 1 S/cm |
| Contact angle | Độ ưa nước | < 90° |
| Dispersibility | Khả năng phân tán trong ethanol/nước | Phân tán đều, không vón sau 30 phút |

---

## 11. ĐẶC TRƯNG ĐIỆN HÓA NỀN (Baseline Electrochemistry)

| Hạng mục | Thông số chuẩn |
|---|---|
| Redox probe | 5–10 mM K₃Fe(CN)₆ |
| Điện ly nền | 0.1M KCl |
| CV | Khảo sát đa tốc độ quét |
| EIS | So sánh $R_{ct}$ giữa GCE, N-CA, Fe/N-CA |
| Tiêu chí CV | $\Delta E_p < 120$ mV |
| Tiêu chí EIS | $R_{ct}$(Fe/N-CA) < $R_{ct}$(N-CA) < $R_{ct}$(bare GCE) |

Công thức Randles–Ševčík:

$$
I_p = 2.69 \times 10^5 n^{3/2} A D^{1/2} C \nu^{1/2}
$$

Từ đó có thể tính:
- EASA
- Hệ số khuếch tán biểu kiến
- Mức cải thiện electron transfer sau khi biến tính Fe/N

---

## 12. PHÂN TÍCH Pb²⁺, Zn²⁺, Cd²⁺ — SWASV

| Thông số | Giá trị chuẩn / khoảng khảo sát |
|---|---|
| Vật liệu ưu tiên | Fe/N-CA |
| Kỹ thuật | SWASV |
| Nền điện ly | Acetate buffer pH 4.5 |
| Khoảng pH khảo sát | 3.5–6.0 |
| Điện thế làm giàu $E_{dep}$ | −0.8 đến −1.4 V vs Ag/AgCl |
| Giá trị khởi đầu Pb²⁺ | khoảng −1.0 V |
| Giá trị khởi đầu Zn²⁺ | khoảng −1.3 V |
| Thời gian làm giàu $t_{dep}$ | 60–240 s |
| Giá trị khởi đầu $t_{dep}$ | 120 s |
| Tốc độ khuấy | 200–600 rpm |
| SW amplitude | 10–50 mV; khởi đầu 25 mV |
| SW frequency | 10–100 Hz; khởi đầu 25 Hz |
| Step potential | 2–10 mV; khởi đầu 5 mV |

Mục tiêu hiệu năng:

| Chất phân tích | Mục tiêu |
|---|---|
| Pb²⁺ | LOD < 0.1 µg/L |
| Zn²⁺ | LOD < 10 nM |
| Cd²⁺ | Cần benchmark riêng trước khi chốt |
| Recovery mẫu thực | 95–105% |

Ion gây nhiễu cần khảo sát:

Cu²⁺, Cd²⁺, Hg²⁺, Fe³⁺, Mn²⁺, Ca²⁺, Mg²⁺, Na⁺, K⁺

Tiêu chí chấp nhận:

- Tín hiệu thay đổi < 10%
- Recovery 95–105%

---

## 13. PHÂN TÍCH PARACETAMOL — DPV/CV

| Thông số | Giá trị chuẩn / khoảng khảo sát |
|---|---|
| Vật liệu ưu tiên | N-CA |
| Kỹ thuật | DPV/CV |
| Dung dịch nền | PBS pH 7.0–7.4 |
| Khoảng pH khảo sát | 5.0–8.0 |
| Pulse amplitude | 10–75 mV; khởi đầu 50 mV |
| Pulse width | 10–100 ms; khởi đầu 50 ms |
| Step potential | 2–10 mV; khởi đầu 5 mV |
| Tốc độ quét CV | 5–100 mV/s |
| Mục tiêu LOD | < 0.05–0.1 µM |
| Linear range mục tiêu | 0.1–100 µM |
| Real sample | Thuốc viên paracetamol |
| Recovery | 95–105% |

Chất gây nhiễu cần khảo sát:

Ascorbic acid (AA), uric acid (UA), dopamine (DA), glucose, diclofenac, nimesulide, amoxicillin, hydroquinone, catechol.

---

## 14. THÔNG SỐ PHÂN TÍCH ĐIỆN HÓA CẦN BÁO CÁO

| Thông số | Công thức / phương pháp | Mục tiêu |
|---|---|---|
| LOD | $3\sigma/slope$ | Pb²⁺ < 0.1 µg/L; paracetamol < 0.1 µM |
| LOQ | $10\sigma/slope$ | Báo cáo theo đường chuẩn |
| Sensitivity | Slope / EASA | So sánh literature |
| Linear range | $I_p$ hoặc current response theo nồng độ | Phủ vùng nồng độ thực tế |
| Selectivity | Interference test | Tín hiệu thay đổi < 10% |
| Repeatability | RSD%, n=5 cùng điện cực | RSD < 5% |
| Reproducibility | RSD%, n=5 điện cực khác nhau | RSD < 8% |
| Stability | % giữ tín hiệu sau 7–30 ngày | > 90% sau 14 ngày |
| Real sample | Spike-and-recovery | 95–105% |

---

## 15. BẢNG TƯƠNG THÍCH (%) GIỮA BIOSENSOR VÀ CÁC HƯỚNG KHÁC

Cơ sở đánh giá: số lượng thông số đặc trưng dùng chung / tổng thông số quan trọng của từng hướng.

| Hướng ứng dụng | Tương đồng với biosensor (%) | Phần kế thừa được | Phần không dùng trực tiếp |
|---|---:|---|---|
| Supercapacitor | 75–80% | BET, BJH, SEM/TEM, Raman, XPS, conductivity, CV, EIS, electrode stability | Specific capacitance, energy density, power density, GCD, Coulombic efficiency |
| ORR / Fuel cell | 55–60% | Pyridinic-N, Fe–Nₓ, defect, electron transfer, XPS Fe/N, EIS | Half-wave potential, RRDE, Koutecky–Levich, H₂O₂ yield |
| Electrochemical sensor | Rất cao ở phần đo | CV, DPV, SWASV, LOD, LOQ, sensitivity, selectivity, recovery | Không thay thế được hóa học vật liệu CA |
| Biosensor vật liệu carbon khác | Cao nếu có bioreceptor | Immobilization, anti-fouling, storage stability, matrix effect | Không thay thế được thông số CA từ xơ dừa |
| Adsorption / xử lý nước | 35–40% | BET, FTIR, surface functional groups, tương tác ion kim loại | Không có tín hiệu điện hóa định lượng |
| Battery | 40–45% | XRD, Raman, XPS, CV, conductivity | GCD, rate capability, capacity retention |
| EMI shielding | 20–25% | SEM, conductivity, Raman | Shielding efficiency không liên quan sensing |

Kết luận:
- Supercapacitor kế thừa mạnh nhất cho phần cấu trúc xốp, độ dẫn và electrode architecture.
- ORR kế thừa mạnh cho phần Fe–Nₓ, pyridinic-N và active sites.
- Electrochemical sensor kế thừa mạnh cho phần phương pháp đo, LOD/LOQ, selectivity và recovery.

---

## 16. QUALITY GATE THEO GIAI ĐOẠN

| Giai đoạn | Dữ liệu bắt buộc | Tiêu chí đạt | Nếu không đạt |
|---|---|---|---|
| Alkali pretreatment | % weight-loss | Có số liệu trước/sau 105°C | Không có dữ liệu gốc để báo cáo |
| Sol-gel | Quan sát sol | Đồng nhất, không còn sợi thô | Tăng thời gian siêu âm nhưng giữ ≤10°C |
| Gelation | Hình dạng gel | Không nứt/sụp rõ | Kéo dài gel hóa hoặc tối ưu ethanol exchange |
| Freeze drying | Hình dạng aerogel | Giữ mạng 3D, co rút thấp | Không dùng sấy nhiệt; kiểm tra trao đổi dung môi |
| Pyrolysis | Yield, màu, độ giòn | Carbon đen, không cháy oxy hóa | Kiểm tra purge N₂ |
| Raman | $I_D/I_G$ | 0.9–1.2 | Quá cao: defect quá mức; quá thấp: thiếu active sites |
| XPS | N, Fe at% | N 3–6%; Fe 1–3%; N:Fe ≥ 4:1 | Điều chỉnh Fe loading/annealing |
| BET/BJH | $S_{BET}$, $V_{meso}$ | >300 m²/g; mesopore 2–50 nm | Tối ưu freeze drying/activation |
| CV baseline | $\Delta E_p$ | <120 mV | Màng quá dày, dẫn kém hoặc binder che phủ |
| EIS | $R_{ct}$ | Fe/N-CA < N-CA | Fe sites chưa hiệu quả hoặc tiếp xúc màng kém |
| Sensor | LOD, linear range | Đạt benchmark mục tiêu | Tối ưu pH, loading, deposition time |
| Real sample | Recovery | 95–105% | Matrix effect hoặc interference chưa kiểm soát |

---

## 17. CLOSED PARAMETERS — ĐÃ CHỐT SAU RÀ SOÁT

| Thông số | Trạng thái cũ | Giá trị chốt | Lý do |
|---|---|---|---|
| Lượng cellulose pulp | 1g nhưng từng có nghi vấn 2g | 1g | Giữ tỷ lệ 1:16 để sol không quá nhớt |
| Thời gian siêu âm | 15–20 phút | 30 phút | Tăng đồng nhất hóa, có ice bath để kiểm soát NH₃ |
| Nhiệt độ siêu âm | 0–5°C | ≤10°C, ưu tiên 0–5°C | Tránh NH₃ bay hơi |
| Gel hóa | Chưa tách rõ | −5°C/24h | Tạo mạng hydrogel ổn định |
| Ethanol coagulation | 36–48h | 24h chuẩn; 36–48h backup | 24h đủ làm thông số chuẩn, kéo dài khi gel yếu |
| Fe impregnation | 12–24h | 24h | Đảm bảo Fe³⁺ khuếch tán vào mao quản |
| $T_{anneal}$ | Chưa chốt | 750°C/1h | Ổn định Fe–Nₓ và phục hồi carbon backbone |
| Ink concentration | Thiếu | 5 mg/mL | Cần để tính loading, EASA, sensitivity |
| Drop-casting | Thiếu | 5–8 µL | Cần để đảm bảo repeatability |
| Nafion ratio | Chưa định lượng | Ink:Nafion = 40:1 v/v | Giảm nguy cơ binder che phủ active sites |

---

## 18. FAILURE MODE QUAN TRỌNG

### 18.1 NH₃ bay hơi khi siêu âm

Nếu nhiệt độ siêu âm vượt 10°C, NH₃ bay hơi làm giảm nguồn N. Hệ quả là XPS N at% thấp, pyridinic-N không đạt và tín hiệu điện hóa giảm. Kiểm soát bằng ice bath và chế độ pulse.

### 18.2 Gel sụp khi trao đổi dung môi

Nếu ethanol exchange hoặc freeze drying không đủ, mạng 3D bị sụp. Hệ quả là BET thấp, mesopore giảm và khuếch tán chất phân tích kém. Kiểm soát bằng ethanol lạnh 0–5°C và freeze drying đúng quy trình.

### 18.3 Fe loading cao nhưng không tạo Fe–Nₓ

Nếu Fe chỉ tạo Fe oxide/Fe carbide, XPS Fe có thể cao nhưng $R_{ct}$ không giảm. Kiểm chứng bằng XPS Fe 2p, N 1s, Raman và EIS.

### 18.4 Màng điện cực quá dày

Nếu drop-cast vượt vùng 5–8 µL ở mực 5 mg/mL, peak có thể tăng ban đầu nhưng diffusion resistance và background current cũng tăng. Kiểm soát bằng CV/EIS và RSD repeatability.

---

## 19. CHIẾN LƯỢC CÔNG BỐ

### Bài 1 — N-CA + Paracetamol, DPV/CV

- Mức mục tiêu: Q3/Q4
- Vật liệu: N-CA-700
- Chất phân tích: Paracetamol
- Kỹ thuật: DPV/CV
- Mẫu thật: thuốc viên paracetamol
- Cấu trúc kết quả đề xuất:
  1. Characterization: SEM, BET, Raman, XPS N at%, FTIR
  2. Electrochemical baseline: CV/EIS N-CA vs GCE
  3. Optimization DPV: pH, pulse amplitude, pulse width, step potential
  4. Analytical performance: LOD, LOQ, linear range, sensitivity
  5. Selectivity: interference test
  6. Real sample: tablet recovery

### Bài 2 — Fe/N-CA + Pb²⁺/Zn²⁺, SWASV

- Mức mục tiêu: Q1/Q2
- Vật liệu: Fe/N-CA-800/750
- Chất phân tích: Pb²⁺/Zn²⁺, có thể mở rộng Cd²⁺ nếu dữ liệu tốt
- Kỹ thuật: SWASV
- Mẫu thật: nước máy, nước sông
- Cấu trúc kết quả đề xuất:
  1. Characterization: SEM, TEM, BET, Raman, XPS Fe/N, XRD
  2. Electrochemical baseline: CV/EIS GCE vs N-CA vs Fe/N-CA
  3. Optimization SWASV: pH, $E_{dep}$, $t_{dep}$, SW parameters
  4. Analytical performance Pb²⁺
  5. Analytical performance Zn²⁺
  6. Simultaneous detection: peak separation Pb²⁺/Zn²⁺
  7. Selectivity: ion interference
  8. Real sample: spike-and-recovery

Lưu ý chiến lược:
- Nếu dữ liệu Fe/N-CA đủ mạnh, ưu tiên submit Bài 2 trước để tránh mất tính mới.
- Bài 1 có thể đóng vai trò nền phương pháp và đối chứng N-CA.

---

## 20. ĐÓNG GÓP DỮ LIỆU GỐC (Original Contributions)

1. Gravimetry hao hụt khối lượng xơ dừa Bến Tre sau tiền xử lý NaOH, dựa trên sấy 105°C trước/sau xử lý.
2. Tổ hợp vật liệu mới: xơ dừa Bến Tre → N-CA / Fe/N-CA → điện cực phân tích điện hóa.
3. Hệ vật liệu so sánh N-CA-700 và Fe/N-CA-800/750 để chứng minh vai trò Fe–Nₓ.
4. Nền điện hóa kép: paracetamol bằng DPV/CV và kim loại nặng bằng SWASV.
5. Kết nối kế thừa liên ngành: supercapacitor cho cấu trúc xốp/độ dẫn, ORR cho Fe–Nₓ, electrochemical sensor cho hiệu năng phân tích.

---

## 21. TÀI LIỆU THAM CHIẾU CHÍNH

- Fauziyah 2020 — N-CA từ coir, NH₄OH:Urea, ORR: doi:10.1021/acs.iecr.0c03771
- N-CA coir+EFB, pyridinic-N, 2024: doi:10.1021/acsomega.3c09297
- Wu 2024 — Fe-doped algae CA, dopamine sensor: doi:10.3390/s24092787
- Onfray 2023 — biomass carbon sensing review: doi:10.3390/mi14091688
- Carbon aerogel / supercapacitor benchmark: doi:10.3390/nano13050817
- Biomass carbon electrochemical sensing review: doi:10.1021/acs.iecr.2c03058
- Heavy metal ion sensing review: doi:10.3390/bios14010009
- Paracetamol Fe–NC/GCE DPV: doi:10.3390/molecules28073006
- N-CMOS paracetamol: doi:10.1039/d1an00966d
- Zn²⁺ SWASV MWCNT: doi:10.1016/j.heliyon.2023.e17346
- Zn²⁺ disposable ASV: doi:10.1021/ac500277j

---

## 22. CHECKLIST TRIỂN KHAI MẺ ĐẦU TIÊN

| Nhóm việc | Checklist |
|---|---|
| Trước tổng hợp | Nghiền xơ dừa; chuẩn bị NaOH; cân mẫu khô trước xử lý |
| Sau tiền xử lý | Sấy 105°C; cân mẫu khô; tính weight-loss |
| Sol-gel | Duy trì ice bath; ghi nhiệt độ trong suốt siêu âm |
| Gelation | Chụp ảnh gel sau −5°C/24h |
| Solvent exchange | Ghi tỷ lệ ethanol/gel; ghi thời gian và nhiệt độ |
| Freeze drying | Ghi thời gian cấp đông và thông số máy nếu có |
| Pyrolysis | Ghi chương trình nhiệt, lưu lượng N₂, yield |
| Fe impregnation | Cân FeCl₃·6H₂O theo 1% và 5%; ghi thời gian ngâm |
| Post-treatment | Ghi acid leaching, rửa, sấy, annealing |
| Screening | Raman, conductivity, contact angle, dispersibility |
| Characterization | SEM/TEM, BET/BJH, XPS, XRD, FTIR, TGA |
| Electrochemistry | CV/EIS trong K₃Fe(CN)₆/KCl |
| Sensing | DPV paracetamol; SWASV Pb²⁺/Zn²⁺/Cd²⁺ |

---

## 23. KẾT LUẬN CHUẨN HÓA

Cấu hình chuẩn để triển khai là:

| Hạng mục | Giá trị chốt |
|---|---|
| Cellulose pulp | 1 g |
| Dung môi sol-gel | 11 mL NH₃ 25% + 4 g urea + 5 mL H₂O |
| Sonication | 30 phút, pulse 2s on / 1s off, ice bath ≤10°C |
| Gelation | −5°C/24h |
| Ethanol coagulation | Ethanol 98%, 15 mL/mL gel, 0–5°C, 24h |
| Washing | DI water 24h, thay 1–2 lần |
| Freeze dry pre-freeze | −20°C, ≥12h |
| Pyrolysis N-CA | 700°C, N₂, giữ 2h |
| Pyrolysis nền Fe/N-CA | 800°C, N₂, giữ 2h |
| Fe impregnation | 1% và 5% Fe, ethanol, 24h |
| Acid leaching | HCl 0.5M, 80°C, 8h |
| Annealing lần 2 | 750°C, N₂, 1h |
| Ink | 5 mg/mL |
| Drop-cast | 5–8 µL trên GCE 3 mm |
| Binder | Chitosan 1% hoặc Nafion 117, ink:Nafion = 40:1 |
| Baseline | 5–10 mM K₃Fe(CN)₆ / 0.1M KCl |
| Kim loại nặng | SWASV, acetate buffer pH 4.5 |
| Paracetamol | DPV/CV, PBS pH 7.0–7.4 |

Điểm kiểm chứng quan trọng sau mẻ đầu tiên:

**Raman $I_D/I_G$ → XPS N/Fe → BET/BJH → CV $\Delta E_p$ → EIS $R_{ct}$**

Nếu 5 chỉ số này đạt, vật liệu đủ nền để chuyển sang tối ưu DPV/SWASV và xây dựng phần analytical performance.
