# 4_Material_Characterization.md — Hướng Dẫn Đặc Trưng Vật Liệu Carbon Aerogel

<!-- v2.0 | Chuẩn hóa: 2026-05-31 | Thay thế hoàn toàn bằng: CA_characterization_biosensor.md -->

> [!NOTE]
> * **Quy trình tổng hợp liên hợp:** [1_Protocol_Synthesis.md](file:///d:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/1_Protocol_Synthesis.md)
> * **Quy trình điện hóa liên hợp:** [2_Protocol_Electrochemistry.md](file:///d:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/2_Protocol_Electrochemistry.md)
>
> Tài liệu này chuẩn hóa khung đánh giá các đặc trưng cấu trúc vật lý, thành phần hóa học bề mặt, cấu trúc graphite hóa của vật liệu $N-CA$ và $Fe/N-CA$, đồng thời phân tích tính tương đồng liên ngành (Supercapacitor vs. Biosensor) để làm cơ sở biện luận học thuật vững chắc cho Luận văn Thạc sĩ.

---

## PHẦN 1. SÁU NHÓM ĐẶC TRƯNG TIÊU CHUẨN (Nhóm A - Nhóm F)

### 1.1 Nhóm A — Hình thái & Cấu trúc vật lý
*Mục đích: Xác nhận cấu trúc xốp 3D tổ ong phân cấp.*

| Kỹ thuật | Thông số đo | Giá trị mục tiêu cho Cảm biến | Ý nghĩa vật lý / Vai trò điện hóa |
| :--- | :--- | :--- | :--- |
| **SEM** | Hình thái bề mặt, kích thước lỗ xốp, vách tổ ong. | Macropore liên thông phân cấp (hierarchical). | Đảm bảo hệ lỗ xốp dẫn lớn đóng vai trò bể chứa chất điện ly, giảm trở lực khuếch tán. |
| **TEM** | Cấu trúc lớp carbon phẳng, độ phân tán Fe. | Lớp carbon mỏng dạng lá, Fe phân tán cực mịn. | Xác nhận nguyên tử sắt không bị tụ tụ thành hạt thô, bám đều trên vách graphite sp². |
| **BET** *(N₂, 77K)* | Diện tích bề mặt riêng ($S_{\text{BET}}$). | **$> 300\text{ m}^2\text{/g}$** (Mục tiêu tối ưu $\ge 370\text{ m}^2\text{/g}$, cạnh tranh **$> 400\text{ m}^2\text{/g}$**). | Cung cấp lượng lớn diện tích tiếp xúc hữu hiệu để gắn kết active sites và làm giàu ion. |
| **BJH** | Thể tích mesopore ($V_{\text{meso}}$), đường kính ($D_{\text{pore}}$). | $V_{\text{meso}} > 0.3\text{ cm}^3\text{/g}$ | Mesopores ($2 - 50\text{ nm}$) đóng vai trò đường dẫn cao tốc vận chuyển nhanh chất phân tích. |
| **TGA** | Độ bền nhiệt, % lượng tro ($ash\%$). | Hàm lượng tro $< 5\%$ | Xác nhận loại bỏ hoàn toàn tạp chất vô cơ và delignification triệt để. |

*Nguồn tham chiếu: doi:10.3390/mi14091688 (Onfray 2023); doi:10.3390/s24092787 (Wu 2024)*

---

### 1.2 Nhóm B — Thành phần hóa học bề mặt
*Mục đích: Xác nhận pha tạp N thành công và sự phối trí của tâm hoạt tính $Fe-N_x$.*

| Kỹ thuật | Thông số đo | Giá trị mục tiêu đạt chuẩn | Vai trò trong Phản ứng xúc tác cảm biến |
| :--- | :--- | :--- | :--- |
| **XPS toàn phổ** | Hàm lượng $C, N, O, Fe$ ở bề mặt (at%). | **$N$: 3–6 at%** \| **$Fe$: 0.4–1.5 at%** \| $N:Fe \ge 4:1$. | Tỷ lệ tối ưu đảm bảo mật độ tâm hoạt tính hoạt động cao và phân tán đồng đều. |
| **XPS N 1s** | Phân deconvolution các dạng N: Pyridinic-N, Pyrrolic-N, Graphitic-N. | **Pyridinic-N chiếm tỷ lệ cao nhất ($\ge 45\%$)** | Pyridinic-N là các Lewis base có cặp e tự do chelate hóa cực mạnh với cation $Pb^{2+}, Zn^{2+}, Cd^{2+}$. |
| **XPS Fe 2p** | Trạng thái oxi hóa $Fe^{2+}/Fe^{3+}$, peak liên kết $Fe-N_x$. | peak $Fe-N_x$ xuất hiện ở khoảng thế **$710.8 - 711.5\text{ eV}$**. | Xác nhận trực tiếp sự hình thành các tâm hoạt tính đơn nguyên tử $Fe-N_4$ xúc tác điện hóa. |
| **XPS C 1s** | Tỷ lệ sp² carbon phẳng (284.6 eV), C-N, C-O. | Tỷ lệ carbon $sp^2 > 60\%$ | Đảm bảo liên kết carbon dẫn điện bền vững và cấu trúc graphite hóa. |
| **FTIR** | Nhóm chức hoạt tính bề mặt: $-OH, C=N, C-N$. | Peak $C=N/C-N$ ở $1630\text{ cm}^{-1}$ và $1380\text{ cm}^{-1}$. | Xác nhận sự bám dính hóa học của Urea/Amoniac làm nguồn N-doping. |

*Nguồn tham chiếu: doi:10.1021/acs.iecr.0c03771 (Fauziyah 2020); doi:10.1021/acsomega.3c09297 (2024)*

---

### 1.3 Nhóm C — Cấu trúc mạng carbon & Mức độ graphite hóa
*Mục đích: Đánh giá độ khuyết tật mạng carbon (tạo active sites) và độ dẫn điện.*

| Kỹ thuật | Thông số đo | Giá trị mục tiêu | Diễn giải khoa học |
| :--- | :--- | :--- | :--- |
| **Raman** | D-band (~1340 cm⁻¹), G-band (~1579 cm⁻¹). | peak dao động đặc trưng của carbon. | D-band đại diện khuyết tật mạng; G-band đại diện sp² carbon graphite hóa. |
| **Raman** | Tỷ lệ cường độ đỉnh **$I_D/I_G$**. | **$0.9 - 1.2$** | defect cao đồng nghĩa có nhiều biên khuyết tật để gắn các nhóm chức nitơ và kim loại làm active sites. |
| **Raman** | 2D-band (~2700 cm⁻¹). | peak 2D đối xứng rộng. | Xác định cấu trúc lớp graphene mỏng chồng lợp bán tuần hoàn. |
| **XRD** | Mặt phẳng (002) ~26° và (100) ~43°. | Peak rộng bán vô định hình, không có peak nhọn của Fe. | Xác nhận carbon cấu trúc bán tinh thể xốp. Không có peak Fe chứng tỏ sắt đã được hòa tan hoặc phân tán nguyên tử sạch. |

---

### 1.4 Nhóm D — Tính chất điện & độ thấm ướt bề mặt
*Mục đích: Đảm bảo độ bền cơ học màng và khả năng truyền electron với dung dịch.*

| Kỹ thuật | Thông số đo | Giá trị mục tiêu | Ý nghĩa thực nghiệm |
| :--- | :--- | :--- | :--- |
| **Bốn mũi dò** | Độ dẫn điện màng ($\sigma$, S/cm). | **$\sigma > 1\text{ S/cm}$** | Giảm thiểu điện trở trong của điện cực, hạn chế dòng nền nhiễu. |
| **Góc tiếp xúc** | Contact angle nước ($\theta$, °). | **$\theta < 90^\circ$ (Ưa nước)** | Đảm bảo màng thấm ướt tốt với dung dịch đệm, tăng tốc độ trao đổi ion. |
| **Dispersibility** | Khả năng phân tán trong DMF/Ethanol. | Phân tán đều, không lắng vón sau 30 phút. | Đảm bảo khả năng drop-cast màng phẳng đồng đều, không nứt nẻ. |

---

### 1.5 Nhóm E — Điện hóa nền (Baseline Electrochemistry)
*Mục đích: Sàng lọc điện cực hoạt động tốt trước khi phân tích cảm biến.*

* **CV** (trong 5.0 mM $K_3Fe(CN)_6$ / 0.1 M KCl, quét 50 mV/s): ΔEp < 120 mV.
* **EIS** (trong K₃Fe(CN)₆/KCl, tần số 100 kHz $\rightarrow$ 0.1 Hz): $R_{ct}$ của $Fe/N-CA$ co-doped phải nhỏ hơn rõ rệt so với $N-CA$ và bare GCE ($R_{ct}(\text{Fe/N-CA}) < R_{ct}(\text{N-CA}) < R_{ct}(\text{bare GCE})$), chứng minh $Fe-N_x$ đóng vai trò xúc tác tăng tốc độ truyền e.

---

### 1.6 Nhóm F — Thông số phân tích điện hóa (Chỉ tiêu cho Biosensor)
* **LOD / LOQ:** LOD tính theo $3\sigma/slope$. Mục tiêu: $Pb^{2+} < 0.1\text{ }\mu\text{g/L}$; Paracetamol $< 0.1\text{ }\mu\text{M}$.
* **Selectivity:** Tín hiệu dòng peak thay đổi $< 10\%$ khi có mặt nồng độ cao các tác nhân gây nhiễu ($Cu^{2+}, Cd^{2+}, AA, UA, DA$).
* **Repeatability:** RSD < 5% (n=10 lần đo cùng 1 điện cực).
* **Reproducibility:** RSD < 8% (n=5 điện cực chế tạo độc lập).
* **Stability:** Tín hiệu giữ vững $\ge 90\%$ sau 14 ngày bảo quản ở 4 ℃.

---

## PHẦN 2. BIỆN LUẬN LIÊN NGÀNH: SUPERCAPACITOR VS. BIOSENSOR

Trong Luận văn, việc liên hệ cấu trúc xốp của Carbon Aerogel giữa hai hướng ứng dụng **Supercapacitor** (Siêu tụ điện) và **Biosensor** (Cảm biến) có ý nghĩa học thuật rất lớn, thể hiện độ bao quát tri thức rộng:

> [!TIP]
> ### Phân tích tương đồng liên ngành (Độ tương hợp đạt 75 - 80%):
> * **Cơ sở cấu trúc xốp chung:** Cả hai hướng đều đòi hỏi một diện tích bề mặt riêng ($S_{\text{BET}}$) lớn và hệ lỗ xốp mesopore-macropore phân cấp liên thông. Trong siêu tụ điện, hệ lỗ xốp này giúp hấp phụ tĩnh điện ion tối đa tạo điện dung lớp kép ($EDLC$); trong cảm biến, nó đóng vai trò bể chứa ion và kênh vận chuyển để tăng tốc độ khuếch tán chất phân tích đến bề mặt điện cực.
> * **Độ khuyết tật carbon ($I_D/I_G$):** Trong siêu tụ điện, các lỗi khuyết tật carbon sp² tạo ra điện dung giả Faradaic ($pseudo-capacitance$); trong cảm biến điện hóa, các khuyết tật này chính là nơi tích hợp các nhóm chức tạp heteroatom ($N, Fe$) để tạo nên các tâm xúc tác hoạt động nhạy.
> * **Khác biệt cốt lõi:** Siêu tụ điện tìm cách cực đại hóa dòng tích lũy điện lượng (dòng sạc $I_c$, dòng nền không Faraday lớn); ngược lại, cảm biến điện hóa cần dòng nền không Faraday **càng nhỏ càng tốt** để làm nổi bật dòng peak Faraday của chất phân tích dải vết (tăng tỷ số Signal-to-Noise). Vì vậy, cảm biến ưu tiên độ dày màng mỏng hơn (drop-cast 5 µL nồng độ 5 mg/mL) và độ dẫn điện cực cao để tăng vận tốc electron.

---

## PHẦN 3. BẢNG BENCHMARK DỮ LIỆU ĐỐI CHIẾU KHI VIẾT LUẬN VĂN

Sử dụng các bảng số liệu benchmark dưới đây để so sánh và biện luận kết quả thực nghiệm trong Chương Kết quả & Thảo luận:

### 3.1 Pb²⁺ — Stripping bằng SWASV (Literature benchmark)

| Vật liệu điện cực biến tính | LOD (Giới hạn phát hiện) | Khoảng tuyến tính (Linear range) | Nguồn DOI tham chiếu |
| :--- | :--- | :--- | :--- |
| B,N,S,P-doped carbon aerogel | < 0.1 µg/L (0.1 ppb) | 0.001–60 µM | doi:10.1016/j.microc.2023.109382 |
| Biochar + nanodiamonds + chitosan/GCE | 0.056 µmol/L (~11.6 µg/L) | 0.25–6.0 µM | doi:10.1016/j.microc.2020.105085 |
| Fe doped carbon xerogel / chitosan/GCE | 97 fM (siêu vết) | — | PMC10670808 (Song et al.) |
| Fe₃O₄/MWCNT/GCE | — | 0.1 - 20 µM | doi:10.20944/preprints202307.0064 |
| **Mục tiêu của Fe/N-CA từ xơ dừa** | **< 0.1 µg/L (0.1 ppb)** | **0.5 - 200 µg/L** | *Đề tài hiện tại* |

---

### 3.2 Zn²⁺ — Stripping bằng SWASV (Literature benchmark)

| Vật liệu điện cực biến tính | LOD | Khoảng tuyến tính | Điều kiện phân tích | Nguồn DOI |
| :--- | :--- | :--- | :--- | :--- |
| HDPBA-MWCNTs/CPE | 2.48 nM | 0.02–10 µM | Đệm BR pH 6, $E_{\text{dep}} = -1.30\text{V}$ | doi:10.1016/j.heliyon.2023.e17346 |
| Bi-film/GCE (Màng Bismuth) | 0.1 µg/L (~1.5 nM) | 1–200 µg/L | Đệm Acetate pH 4.5 | Standard EPA Method |
| Cu-based disposable electrode | 100 nM | 100 nM–40 µM | Đệm Acetate pH 6.0 | doi:10.1021/ac500277j |
| **Mục tiêu của Fe/N-CA** | **< 10 nM** | **0.01 - 50 µM** | **Đệm Acetate pH 4.5** | *Đề tài hiện tại* |

---

### 3.3 Paracetamol (APAP) — Đo bằng DPV (Literature benchmark)

| Vật liệu điện cực biến tính | LOD (Giới hạn phát hiện) | Độ nhạy (Sensitivity) | Khoảng tuyến tính | Nguồn DOI |
| :--- | :--- | :--- | :--- | :--- |
| Fe–NC–800/GCE (Fe-N carbon) | 0.026 µM | — | 0–100 µM | doi:10.3390/molecules28073006 |
| N-CMOS/GCE (N-doped carbon) | 0.030 µM | 1.97 µA/µM·cm² | 0.1–80 µM | doi:10.1039/d1an00966d |
| Y-CDs/Cu₂O/GCE (sinh khối) | 90 nM | — | 0.5–100 µM | doi:10.1080/00032719.2024.2343365 |
| **Mục tiêu của N-CA-700** | **< 0.05 µM** | **> 1.5 µA/µM·cm²** | **0.1–100 µM** | *Đề tài hiện tại* |
