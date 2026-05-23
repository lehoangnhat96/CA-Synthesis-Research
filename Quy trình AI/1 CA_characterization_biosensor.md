# ĐẶC TÍNH VẬT LIỆU CARBON AEROGEL — HƯỚNG ỨNG DỤNG BIOSENSOR
# Phân tích tương đồng đa hướng ứng dụng + Xác thực DOI
# Mục tiêu: N-CA và Fe/N-CA từ xơ dừa Bến Tre — phân tích điện hóa

---

## PHẦN 1. OUTLINE ĐẶC TÍNH CARBON AEROGEL CHO BIOSENSOR

### 1.1 Nhóm A — Hình thái & Cấu trúc vật lý

| Kỹ thuật | Thông số đo | Giá trị mục tiêu (biosensor) |
|----------|------------|-------------------------------|
| SEM | Hình thái bề mặt, kích thước lỗ xốp, cấu trúc tổ ong | Macropore liên thông, hierarchical |
| TEM | Cấu trúc lớp graphene, phân bố hạt Fe | Lớp carbon mỏng, Fe phân tán đều |
| BET (N₂, 77K) | S_BET (m²/g) | > 300 m²/g (mục tiêu điện hóa) |
| BJH | V_meso (cm³/g), D_pore (nm) | Mesopore 2–50 nm, V_meso > 0.3 cm³/g |
| TGA | Độ bền nhiệt, % tro (ash) | Tro < 5% |

Nguồn DOI: doi:10.3390/mi14091688 (Onfray 2023); doi:10.3390/s24092787 (Wu 2024)

---

### 1.2 Nhóm B — Thành phần hóa học bề mặt

| Kỹ thuật | Thông số đo | Giá trị mục tiêu |
|----------|------------|------------------|
| XPS toàn phổ | C at%, N at%, O at%, Fe at% | N: 3–6 at%; Fe: 1–3 at%; N:Fe ≥ 4:1 |
| XPS N 1s | Pyridinic-N (~398.5 eV), Pyrrolic-N (~400.1 eV), Graphitic-N (~401.2 eV) | Pyridinic-N chiếm tỷ lệ cao nhất |
| XPS Fe 2p | Fe²⁺/Fe³⁺ ratio, Fe–Nₓ coordination | Fe–Nₓ sites xác nhận bằng peak ~707 eV |
| XPS C 1s | sp² C (284.6 eV), C–N, C–O | sp² C > 60% |
| FTIR | Nhóm chức bề mặt: –OH, C=N, C–N | Xác nhận N-doping và nhóm chức hoạt động |

Nguồn DOI: doi:10.1021/acs.iecr.0c03771 (Fauziyah 2020); doi:10.1021/acsomega.3c09297 (2024)

---

### 1.3 Nhóm C — Cấu trúc carbon & Mức độ graphite hóa

| Kỹ thuật | Thông số đo | Giá trị mục tiêu |
|----------|------------|------------------|
| Raman | D-band (1340 cm⁻¹), G-band (1579 cm⁻¹) | Xác nhận cấu trúc carbon |
| Raman | Tỷ lệ I_D/I_G | 0.9–1.2 (defect cao = active sites nhiều) |
| Raman | 2D-band (~2700 cm⁻¹) | Đánh giá mức độ graphene hóa |
| XRD | Peak (002) ~26°, (100) ~43° | Bán tinh thể, không cần graphite hóa hoàn toàn |

Nguồn DOI: doi:10.3390/nano13050817 (Nanomaterials 2023)

---

### 1.4 Nhóm D — Tính chất điện

| Kỹ thuật | Thông số đo | Giá trị mục tiêu |
|----------|------------|------------------|
| Đo 4 mũi dò hoặc pellet | Độ dẫn điện σ (S/cm) = L/(R×A) | σ > 1 S/cm (đủ cho điện cực) |
| Góc tiếp xúc (Contact angle) | Độ ưa nước bề mặt (°) | < 90° (ưa nước → tiếp xúc tốt với dung dịch) |
| Dispersibility | Khả năng phân tán trong ethanol/nước | Phân tán đồng đều, không vón sau 30 phút |

---

### 1.5 Nhóm E — Điện hóa nền (Baseline electrochemistry)

| Kỹ thuật | Thông số đo | Mục tiêu |
|----------|------------|----------|
| CV (K₃Fe(CN)₆/KCl) | ΔEp (mV) | < 120 mV |
| CV đa tốc độ quét | D (cm²/s) — Randles-Ševčík | Tính hệ số khuếch tán |
| EIS | R_ct (Ω), R_s (Ω), Warburg | R_ct Fe/N-CA << R_ct N-CA |
| CV (K₃Fe(CN)₆) | EASA (cm²) = I_p / (2.69×10⁵ × n^1.5 × D^0.5 × ν^0.5) | So sánh N-CA vs Fe/N-CA |

---

### 1.6 Nhóm F — Thông số phân tích điện hóa (RIÊNG cho Biosensor)

| Thông số | Công thức / Phương pháp | Mục tiêu |
|----------|------------------------|----------|
| LOD | 3σ/slope | Pb²⁺ < 0.1 µg/L; Paracetamol < 0.1 µM |
| LOQ | 10σ/slope | — |
| Sensitivity | µA / (µM·cm²) | So sánh với literature |
| Linear range | µM hoặc µg/L | Phủ nồng độ thực tế |
| Selectivity | Interference test: ion cạnh tranh (Cu²⁺, Cd²⁺, AA, UA) | Recovery 95–105% |
| Repeatability | RSD% (n=5, cùng điện cực) | RSD < 5% |
| Reproducibility | RSD% (n=5, điện cực khác nhau) | RSD < 8% |
| Stability | % giữ tín hiệu sau 7–30 ngày | > 90% sau 14 ngày |
| Real sample | Recovery% trong mẫu thực | 95–105% |

---

## PHẦN 2. BẢNG TƯƠNG THÍCH (%) GIỮA BIOSENSOR VÀ CÁC HƯỚNG KHÁC

Cơ sở đánh giá: so sánh số lượng thông số đặc trưng dùng chung / tổng thông số mỗi hướng.
Nguồn xác thực: doi:10.3390/mi14091688; doi:10.1021/acs.iecr.2c03058; doi:10.3390/nano13050817

| Hướng ứng dụng | Tương đồng với Biosensor (%) | Cơ sở |
|----------------|------------------------------|-------|
| **Supercapacitor** | **~75–80%** | Cùng dùng: BET, XPS, Raman, SEM/TEM, CV, EIS, XRD, FTIR, conductivity |
| ORR / Fuel cell | ~55–60% | Cùng dùng: XPS N-type, Fe–Nₓ sites, electron transfer kinetics, EIS |
| Adsorption / Xử lý nước | ~35–40% | Cùng dùng: BET, SEM, FTIR, XRD — phần điện hóa không dùng |
| Battery | ~40–45% | Cùng dùng: XRD, Raman, XPS, CV — GCD và rate capability không dùng |
| EMI Shielding | ~20–25% | Chỉ dùng chung: SEM, conductivity, Raman |

KẾT LUẬN: Supercapacitor có độ tương đồng cao nhất với Biosensor (~75–80%).

---

## PHẦN 3. CHI TIẾT PHÂN TÍCH SUPERCAPACITOR ↔ BIOSENSOR

### 3.1 Thông số DÙNG CHUNG (tương đồng cao — kế thừa trực tiếp)

| Thông số | Supercapacitor | Biosensor | Ghi chú |
|----------|---------------|-----------|---------|
| S_BET (m²/g) | > 500 m²/g (năng lượng cao) | > 300 m²/g (đủ cho sensing) | Biosensor không cần cực đại, cần phân bố đều |
| V_meso (cm³/g) | Mesopore tối ưu cho ion khuếch tán | Cùng mục tiêu | Dùng chung hoàn toàn |
| I_D/I_G (Raman) | 0.9–1.2 (defect = pseudo-capacitance) | 0.9–1.2 (defect = active sites) | Cùng target, cùng lý do vật lý |
| XPS N at% | Tăng capacitance qua pseudo-cap | Tăng electrocatalysis | Giá trị khác nhau nhưng kỹ thuật đo giống nhau |
| XPS N-type | Pyridinic, Pyrrolic, Graphitic | Pyridinic ưu tiên cao hơn | Phân tích giống, ý nghĩa khác |
| EIS — R_ct | Đánh giá ion transport | Đánh giá electron transfer | Cùng kỹ thuật, diễn giải khác |
| CV | Tính capacitance, redox | Tính EASA, D, ΔEp | Cùng kỹ thuật, thông số tính khác |
| SEM/TEM | Pore morphology | Pore morphology | Dùng chung 100% |
| XRD | Graphitization | Graphitization | Dùng chung 100% |
| Conductivity (σ) | S/cm — ảnh hưởng ESR | S/cm — ảnh hưởng background current | Dùng chung 100% |
| FTIR | Nhóm chức | Nhóm chức liên quan đến analyte | Dùng chung 100% |

---

### 3.2 Thông số SUPERCAPACITOR không dùng trong Biosensor

| Thông số | Lý do không dùng |
|----------|-----------------|
| Specific capacitance (F/g) | Không liên quan đến LOD/sensitivity |
| Energy density (Wh/kg) | Thông số năng lượng, không phân tích |
| Power density (W/kg) | Thông số năng lượng, không phân tích |
| GCD (galvanostatic charge-discharge) | Kỹ thuật đặc thù supercap |
| Cycle stability (1000–10000 cycles) | Biosensor chỉ cần 7–30 ngày |
| Rate capability | Không liên quan sensing |
| Coulombic efficiency | Không liên quan sensing |

---

### 3.3 Thông số BIOSENSOR phải tự nghiên cứu — không có trong Supercapacitor

Đây là phần cần tìm riêng, không thể kế thừa từ supercapacitor literature:

| Thông số | Phân loại | Kỹ thuật / Phương pháp | DOI tham chiếu |
|----------|-----------|------------------------|----------------|
| LOD / LOQ | Phân tích định lượng | 3σ/slope và 10σ/slope từ đường chuẩn | doi:10.3390/s24092787 |
| Sensitivity (µA/µM·cm²) | Hiệu năng sensor | Slope đường chuẩn / EASA | doi:10.3390/mi14091688 |
| Linear dynamic range | Phân tích định lượng | Khảo sát nồng độ I_p vs C | doi:10.3390/s24092787 |
| Selectivity | Đặc trưng sensor | Interference test — coexisting species | doi:10.1021/acs.iecr.2c03058 |
| Anti-fouling | Bền bề mặt điện cực | Kiểm tra tín hiệu trước/sau matrix phức tạp | doi:10.3390/bios14010009 |
| Repeatability (RSD%) | Độ lặp lại | n=5, cùng điện cực | — |
| Reproducibility (RSD%) | Độ tái lặp | n=5, điện cực độc lập | — |
| Stability (% signal retention) | Bền theo thời gian | Đo lại sau 7, 14, 30 ngày | — |
| Real sample recovery (%) | Xác thực thực tế | Spike-and-recovery trong mẫu thực | — |
| Electron transfer coefficient α | Cơ chế điện hóa | Tafel plot hoặc Butler-Volmer | — |
| Diffusion coefficient D | Cơ chế khuếch tán | Randles-Ševčík: I_p = 2.69×10⁵ n^1.5 A D^0.5 C ν^0.5 | — |
| Deposition potential/time (SWASV) | Tối ưu hóa | Khảo sát E_dep và t_dep cho Pb²⁺/Zn²⁺ | — |
| pH tối ưu | Điều kiện phân tích | Khảo sát pH dung dịch nền | — |
| Accumulation time | Điều kiện SWASV | Khảo sát thời gian làm giàu | — |

---

## PHẦN 4. ỨNG DỤNG THÔNG SỐ ORR VÀO BIOSENSOR (hướng tương đồng thứ 2)

Hướng ORR tương đồng ~55–60% — khai thác phần Fe–Nₓ sites:

### Phần dùng chung ORR ↔ Biosensor

| Thông số | Vai trò trong ORR | Vai trò trong Biosensor |
|----------|------------------|------------------------|
| XPS pyridinic-N at% | Active site cho O₂ reduction | Active site cho electrocatalysis analyte |
| XPS Fe–Nₓ coordination (~707 eV) | Catalytic center | Catalytic center cho Pb²⁺, paracetamol |
| EIS — electron transfer rate | Đánh giá kinetics ORR | Đánh giá kinetics sensing |
| CV — onset potential | Hoạt tính xúc tác | Overpotential cho oxidation/reduction analyte |
| Raman D/G ratio | Defect density | Defect density = active sites |

### Phần ORR KHÔNG dùng trong Biosensor

| Thông số ORR | Lý do loại bỏ |
|-------------|---------------|
| Half-wave potential (E₁/₂) | Đặc thù ORR |
| Tafel slope (mV/dec) | Đặc thù ORR kinetics |
| RRDE (rotating ring disk) | Thiết bị đặc thù |
| H₂O₂ yield % | Không liên quan |
| Koutecky-Levich plot | Đặc thù ORR |
| n (electron transfer number ORR) | Đặc thù ORR |

---

## PHẦN 5. TRÌNH TỰ ĐẶC TRƯNG VẬT LIỆU — ĐỀ XUẤT CHO N-CA & Fe/N-CA

### Giai đoạn Pre-screening (trước chế tạo điện cực)
1. Raman → I_D/I_G: loại mẫu không đạt
2. σ (pellet): loại mẫu dẫn kém
3. Dispersibility: kiểm tra khả năng coating
4. Contact angle: xác nhận tính ưa nước

### Giai đoạn Characterization chính
5. SEM/TEM: hình thái, pore structure
6. BET/BJH: S_BET, V_meso, D_pore
7. XRD: graphitization, peak Fe (nếu có)
8. FTIR: nhóm chức
9. XPS toàn phổ + deconvolution N 1s, Fe 2p, C 1s
10. TGA: độ bền nhiệt

### Giai đoạn Electrochemical baseline
11. CV (K₃Fe(CN)₆) đa tốc độ → ΔEp, D, EASA
12. EIS → R_ct N-CA vs Fe/N-CA

### Giai đoạn Sensing (riêng cho Biosensor)
13. Tối ưu hóa điều kiện đo (pH, E_dep, t_dep)
14. Đường chuẩn → LOD, LOQ, Sensitivity, Linear range
15. Interference test → Selectivity
16. Repeatability + Reproducibility + Stability
17. Real sample validation → Recovery%

---

## PHẦN 6. THÔNG SỐ MỤC TIÊU TỐI THIỂU ĐỂ CÔNG BỐ Q1/Q2

| Thông số | Ngưỡng tối thiểu Q2 | Ngưỡng cạnh tranh Q1 | Nguồn benchmark |
|----------|--------------------|-----------------------|----------------|
| S_BET | > 200 m²/g | > 400 m²/g | doi:10.3390/mi14091688 |
| I_D/I_G | 0.9–1.2 | — | doi:10.3390/nano13050817 |
| N at% (XPS) | 3–6% | > 5% pyridinic | doi:10.1021/acsomega.3c09297 |
| R_ct giảm so với GCE | > 50% | > 70% | doi:10.3390/s24092787 |
| LOD Pb²⁺ | < 1 µg/L | < 0.1 µg/L | WHO guideline: 10 µg/L |
| LOD Paracetamol | < 0.1 µM | < 0.05 µM | doi:10.3390/s24092787 |
| Sensitivity | cạnh tranh top 50% | top 20% literature | — |
| Real sample recovery | 95–105% | 98–102% | — |
| Stability | > 85% sau 7 ngày | > 90% sau 14 ngày | — |

---

## TÀI LIỆU DOI XÁC THỰC

1. doi:10.3390/mi14091688 — Onfray 2023 — Biomass carbon sensing review (tổng hợp thông số)
2. doi:10.3390/s24092787 — Wu 2024 — Fe-CA dopamine biosensor (analogy system)
3. doi:10.1021/acs.iecr.0c03771 — Fauziyah 2020 — N-CA coir NH₄OH:Urea
4. doi:10.1021/acsomega.3c09297 — N-CA coir+EFB pyridinic-N 2024
5. doi:10.3390/nano13050817 — CA supercapacitor BET/Raman/XPS 2023
6. doi:10.1021/acs.iecr.2c03058 — Biomass carbon electrochemical sensing review
7. doi:10.3390/bios14010009 — Heavy metal ion sensing review 2023

---

## PHẦN 7. BENCHMARK THÔNG SỐ PHÂN TÍCH — DỮ LIỆU ĐỂ SO SÁNH KHI VIẾT BÀI

### 7.1 Pb²⁺ — SWASV (Literature benchmark)

| Vật liệu điện cực | LOD | Sensitivity (µA/µM·cm²) | Linear range | DOI |
|-------------------|-----|--------------------------|--------------|-----|
| B,N,S,P-doped carbon aerogel | < 0.1 µg/L | — | 0.001–60 µM | doi:10.1016/j.microc.2023.109382 |
| Biochar + nanodiamonds + chitosan/GCE | 0.056 µmol/L | 5.3 µA/µmol·cm² | 0.25–6.0 µM | doi:10.1016/j.microc.2020.105085 |
| Fe doped carbon xerogel / chitosan/GCE | 97 fM | 9.2×10⁵ µA/µM | — | PMC10670808 |
| Fe₃O₄/MWCNT/GCE | — | 125.91 µA/mM·cm² | — | doi:10.20944/preprints202307.0064 |
| **Mục tiêu N-CA / Fe/N-CA** | **< 0.1 µg/L** | **cạnh tranh top 20%** | — | — |

---

### 7.2 Zn²⁺ — SWASV (Literature benchmark)

| Vật liệu điện cực | LOD | Linear range | Điều kiện | DOI |
|-------------------|-----|--------------|-----------|-----|
| HDPBA-MWCNTs/CPE | 2.48 nM | 0.02–10 µM | BR buffer pH 6, E_dep = −1.30V, t = 120s | doi:10.1016/j.heliyon.2023.e17346 |
| Bi-film/GCE | 0.1 µg/L | 1–200 µg/L | Acetate buffer pH 4.5 | — |
| Cu-based disposable | 100 nM | 100 nM–40 µM | Acetate buffer pH 6 | doi:10.1021/ac500277j |
| **Mục tiêu** | **< 10 nM** | **0.01–50 µM** | Acetate pH 4.5 | — |

---

### 7.3 Paracetamol — DPV (Literature benchmark)

| Vật liệu điện cực | LOD | Sensitivity | Linear range | Real sample | DOI |
|-------------------|-----|------------|--------------|-------------|-----|
| Fe–NC–800/GCE (Fe-N carbon) | 0.026 µM | — | 0–100 µM | Tablet ✓ | doi:10.3390/molecules28073006 |
| N-CMOS/GCE (N-doped carbon) | 0.030 µM | 1.97 µA/µM·cm² | 0.1–80 µM | — | doi:10.1039/d1an00966d |
| rGO/PPy NTs/SPE | 0.04 µM | — | 0.1–390 µM | Tablet ✓ | — |
| Y-CDs/Cu₂O/GCE (biomass) | 90 nM | — | 0.5–100 µM | Tablet ✓ | doi:10.1080/00032719.2024.2343365 |
| N-doped biochar/β-CD-MOF | < 50 nM | — | — | ✓ | PMC10054116 |
| **Mục tiêu N-CA** | **< 0.05 µM** | **> 1.5 µA/µM·cm²** | **0.1–100 µM** | Thuốc viên ✓ | — |

---

### 7.4 Thông số điều kiện tối ưu SWASV cần khảo sát (Pb²⁺/Zn²⁺)

| Thông số | Khoảng khảo sát | Tham chiếu |
|----------|----------------|------------|
| pH dung dịch nền | 3.5–6.0 | Acetate buffer — tối ưu thường 4.5 |
| Điện thế làm giàu E_dep | −0.8 đến −1.4 V vs Ag/AgCl | Pb²⁺: −1.0V; Zn²⁺: −1.3V thường gặp |
| Thời gian làm giàu t_dep | 60–240 s | 120s là phổ biến |
| Tốc độ khuấy | 200–600 rpm | Trong quá trình deposition |
| Biên độ SW (amplitude) | 10–50 mV | Thường 25 mV |
| Tần số SW (frequency) | 10–100 Hz | Thường 25 Hz |
| Bước thế (step potential) | 2–10 mV | Thường 5 mV |

---

### 7.5 Thông số điều kiện tối ưu DPV cần khảo sát (Paracetamol)

| Thông số | Khoảng khảo sát | Tham chiếu |
|----------|----------------|------------|
| pH dung dịch nền | 5.0–8.0 | PBS — tối ưu thường 7.0–7.4 |
| Biên độ xung (pulse amplitude) | 10–75 mV | Thường 50 mV |
| Thời gian xung (pulse width) | 10–100 ms | Thường 50 ms |
| Bước thế (step potential) | 2–10 mV | Thường 5 mV |
| Tốc độ quét | 5–100 mV/s | — |
| Thể tích drop cast | 3–10 µL | Tối ưu tín hiệu vs background |

---

## PHẦN 8. INTERFERENCE TEST — DANH SÁCH CHẤT CẦN KHẢO SÁT

### Cho Pb²⁺/Zn²⁺ (SWASV)
Ion cạnh tranh cần test: Cu²⁺, Cd²⁺, Hg²⁺, Fe³⁺, Mn²⁺, Ca²⁺, Mg²⁺, Na⁺, K⁺
Nồng độ thường dùng: 5–50× nồng độ analyte mục tiêu
Tiêu chí chấp nhận: tín hiệu thay đổi < 10%

### Cho Paracetamol (DPV)
Chất cần test: ascorbic acid (AA), uric acid (UA), dopamine (DA), glucose,
              diclofenac, nimesulide, amoxicillin, hydroquinone, catechol
Nguồn: doi:10.3390/molecules28073006

---

## PHẦN 9. CẤU TRÚC PHẦN KẾT QUẢ — GỢI Ý CHO BÀI BÁO

### Bài 1 (N-CA — Paracetamol — Q3/Q4)
3.1 Characterization: SEM, BET, Raman, XPS (N at%, N-type), FTIR
3.2 Electrochemical baseline: CV/EIS N-CA vs GCE
3.3 Optimization DPV: pH, pulse parameters
3.4 Analytical performance: LOD, LOQ, linear range, sensitivity
3.5 Selectivity: interference test
3.6 Real sample: thuốc viên paracetamol — recovery%

### Bài 2 (Fe/N-CA — Pb²⁺/Zn²⁺ — Q1/Q2)
3.1 Characterization: SEM, TEM, BET, Raman, XPS (N at%, Fe at%, Fe–Nₓ), XRD
3.2 Electrochemical baseline: CV/EIS N-CA vs Fe/N-CA vs GCE — chứng minh Fe–Nₓ synergy
3.3 Optimization SWASV: pH, E_dep, t_dep, SW parameters
3.4 Analytical performance Pb²⁺: LOD, LOQ, linear range, sensitivity
3.5 Analytical performance Zn²⁺: LOD, LOQ, linear range, sensitivity
3.6 Simultaneous detection: tách peak Pb²⁺ và Zn²⁺
3.7 Selectivity: interference ions
3.8 Real sample: nước máy, nước sông — spike and recovery

---

## NGUỒN DOI BỔ SUNG (Phần 7–9)

- doi:10.3390/molecules28073006 — Fe–NC/GCE paracetamol DPV 2023
- doi:10.1039/d1an00966d — N-CMOS paracetamol 2021
- doi:10.1080/00032719.2024.2343365 — biomass carbon dot paracetamol 2024
- doi:10.1016/j.heliyon.2023.e17346 — Zn²⁺ SWASV MWCNT 2023
- doi:10.1021/ac500277j — Zn²⁺ disposable ASV
- doi:10.20944/preprints202307.0064 — heavy metal SWASV review 2023
