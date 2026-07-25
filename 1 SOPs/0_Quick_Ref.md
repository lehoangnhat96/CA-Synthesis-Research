# 0_Quick_Ref.md — Bảng Thông Số Tham Chiếu Nhanh
<!-- v1.0 | Chuẩn hóa: 2026-05-31 | Merge từ: SYNTHESIS_PARAMETERS §23 + Final_SOPs_CA Phần I -->

> Tài liệu này chỉ chứa **thông số chốt**. Chi tiết bước thực hiện và cơ chế → xem `1_Protocol_Synthesis.md`.

---

## BẢNG THÔNG SỐ TỔNG HỢP — GĐ 0 ĐẾN GĐ 7

| Giai đoạn | Quy trình | Nhiệt độ | Thời gian | Nồng độ / Tỷ lệ | Lưu ý bắt buộc |
|:---|:---|:---:|:---:|:---|:---|
| **GĐ 0** | Tiền xử lý kiềm hóa | 80 ± 2 ℃ | 4 giờ | NaOH 6 wt% | Tỷ lệ 1 g : 20 mL (40.0 g xơ dừa : 800 mL NaOH 6 wt% pha từ 48 g NaOH và 752 mL nước DI) · Không tẩy trắng · Nghiền < 150 µm trước |
| **GĐ 1** | Sol-gel NH₃/Urea/H₂O | ≤ 10 ℃ (ice bath) | 30 phút siêu âm | 1 g DCF : 11 mL NH₃ 25% : 4 g Urea : 5 mL H₂O | Pulse 2s on / 1s off · Bọc kín tránh NH₃ bay hơi |
| **GĐ 2** | Đúc khuôn & gel hóa | −14 ℃ đến −20 ℃ | 24 giờ | — | Ưu tiên khuôn Silicone dẻo (như khuôn flan) · Gõ nhẹ đuổi bọt, bọc kín màng bọc, để tĩnh 15-30p ở 0-5℃ rồi cấp đông |
| **GĐ 3a** | Đông tụ (coagulation) | Nhiệt độ phòng | 24 giờ | Ethanol 96-98% · **Tỉ lệ 10:1 (v/v) so với dung môi trong gel** (~200 mL cồn cho mẻ 1g DCF chứa ~20 mL dung môi) | ĐỂ NGUYÊN KHUÔN rã đông 1h $\rightarrow$ Nghiêng nhẹ gạn bỏ dung dịch thừa $\rightarrow$ Úp ngược trượt gel vào khay chứa sẵn 200 mL cồn ở nhiệt độ phòng |
| **GĐ 3b** | Rửa solvent exchange | Nhiệt độ phòng | 2 h × 2 lần (chính xác) | Nước DI | Không rửa quá 3 lần → tránh rửa trôi Urea/NH₃ (nguồn N) |
| **GĐ 4** | Sấy thăng hoa | Cấp đông −20 ℃ ≥ 12 h | 24–48 giờ | P < 20 Pa · Bẫy lạnh ≤ −45 ℃ | Tuyệt đối không sấy nhiệt |
| **GĐ 5a** | Nhiệt phân N-CA | **700 ℃** | Giữ 2 giờ | 5 ℃/min · N₂ 100 mL/min | Purge N₂ 150–200 mL/min trong 30 phút trước nung |
| **GĐ 5b** | Nhiệt phân nền Fe/N-CA | **800 ℃** | Giữ 2 giờ | 5 ℃/min · N₂ 100 mL/min | Chương trình 3 ramp: 25→150 (30'), 150→400 (30'), 400→T_target (2h) |
| **GĐ 6** | Doping Fe (chỉ Fe/N-CA) | Nhiệt độ phòng | 24 giờ | **1% hoặc 5% Fe/m_mẫu** · Ethanol | 30 phút đầu siêu âm nhẹ · Sấy 60 ℃ sau tẩm |
| **GĐ 7a** | Acid leaching | 80 ± 2 ℃ | 8 giờ | HCl 0.5 M · 1 g/100 mL | Đun hồi lưu · Rửa DI đến pH 6.5–7.0 · Sấy **80 ℃**/12 h |
| **GĐ 7b** | Annealing lần 2 | **750 ℃** | Giữ 1 giờ | 5 ℃/min · N₂ 100 mL/min | Kiểm tra Raman I_D/I_G ngay sau khi hoàn thành |

---

## TÍNH LƯỢNG FeCl₃·6H₂O (MW = 270.3 g/mol)

```
m_FeCl₃·6H₂O = m_mẫu × w_Fe × (270.3 / 55.845)
```

| Mức Fe mục tiêu | Với 1.000 g mẫu |
|---:|---:|
| **1 wt%** | **0.0484 g** FeCl₃·6H₂O |
| **5 wt%** | **0.242 g** FeCl₃·6H₂O |

---

## CÔNG THỨC GRAVIMETRY (GĐ 0 — Original Data Contribution)

```
Weight-loss (%) = [(m₀ − m₁) / m₀] × 100
```
- m₀: khối lượng xơ dừa khô trước xử lý (sấy 105 ℃)
- m₁: khối lượng xơ dừa khô sau xử lý (sấy 105 ℃)
- Dải đạt: **30–38%**

---

## GIAI ĐOẠN 8: CHẾ TẠO ĐIỆN CỰC — THÔNG SỐ CHỐT

| Thông số | Giá trị |
|:---|:---|
| Nền điện cực | GCE Ø 3 mm (A = 0.0707 cm²) |
| Đánh bóng | Al₂O₃ 0.05 µm, hình số 8, 2 phút × 2 lần |
| Nồng độ mực | 5 mg CA / 1 mL dung môi (DMF) |
| Siêu âm mực | 30–60 phút, ice bath < 15 ℃ |
| Drop-cast | **5.0 µL** |
| Sấy màng | Tự nhiên 25 ℃, 2–3 giờ — **cấm sấy nóng / thổi khí** |
| Binder — kim loại nặng (SWASV) | Chitosan 1 wt% trong acetic acid 1% · nồng độ cuối 0.05 wt% |
| Binder — paracetamol (DPV) | Nafion 5 wt% thương mại · tỷ lệ Ink:Nafion = 40:1 v/v (nồng độ cuối 0.25 wt%) |
| Redox probe (baseline) | 5–10 mM K₃Fe(CN)₆ / 0.1 M KCl |
| Tiêu chí CV baseline | ΔE_p < 120 mV |
| Tiêu chí EIS baseline | R_ct(Fe/N-CA) < R_ct(N-CA) < R_ct(bare GCE) |

---

## GIAI ĐOẠN 8: ĐIỀU KIỆN ĐO CẢM BIẾN — THÔNG SỐ KHỞI ĐẦU

### SWASV — Pb²⁺ / Cd²⁺ / Zn²⁺

| Thông số | Khởi đầu | Khoảng khảo sát |
|:---|:---:|:---|
| Nền điện ly | Acetate buffer 0.1 M, pH 4.5 | pH 3.5–6.0 |
| E_dep (thế lắng khử) | −1.1 V vs. Ag/AgCl | −0.8 V đến −1.4 V |
| t_dep (thời gian lắng khử) | 120 s (khuấy 400 rpm) | 60–240 s |
| SW frequency | 25 Hz | 10–100 Hz |
| SW amplitude | 25 mV | 10–50 mV |
| Step potential | 5 mV | 2–10 mV |

### DPV — Paracetamol

| Thông số | Khởi đầu | Khoảng khảo sát |
|:---|:---:|:---|
| Nền điện ly | PBS 0.1 M, pH 7.0–7.4 | pH 5.0–8.0 |
| Pulse amplitude | 50 mV | 10–75 mV |
| Pulse width | 50 ms | 10–100 ms |
| Step potential | 5 mV | 2–10 mV |

---

## MỤC TIÊU XPS SAU NUNG

| Thông số | Mục tiêu | Fail nếu |
|:---|:---:|:---|
| N at% (tổng) | 3–6 at% | < 2 at% |
| Fe at% (tổng) | 0.4–1.5 at% | > 2.0 at% |
| Tỷ lệ N:Fe | ≥ 4:1 | < 3:1 |
| Pyridinic-N / tổng N 1s | ≥ 45% diện tích | < 25% |
| Peak Fe–Nₓ (Fe 2p₃/₂) | 710.8–711.5 eV | Không xuất hiện |

---

---

## ĐIỆN CỰC SO SÁNH & ĐỊNH HƯỚNG MỞ RỘNG PHI NƯỚC

### 1. Khuyến nghị & Chuẩn bị điện cực so sánh (RE Prep & Maintenance)
*   **Hiệu chuẩn OCP:** Đo thế mạch hở giữa điện cực nước mới và điện cực chuẩn lab trong dung dịch $KCl$ 3 M. **Tiêu chí đạt: $\Delta E_{OCP} \le 10\text{ mV}$** (tránh trôi thế nền).
*   **"Hack" điện cực nước dự phòng:** 
    *   *Chuẩn bị:* Đánh bóng dây bạc ($Ag$) $\rightarrow$ nhúng vào $HCl$ 0.1 M $\rightarrow$ áp thế dương $+0.8\text{ V}$ trong $2\text{ phút}$ (phủ lớp $AgCl$ xám tro).
    *   *Nạp:* Bơm đầy dung dịch $KCl$ 3 M (hoặc bão hòa) vào thân điện cực phi nước rỗng $\rightarrow$ lắp dây bạc đã phủ $AgCl$.

### 2. Phương hướng mở rộng phi nước chiến lược (Non-aqueous Directions)
*   **Định hướng 1: Siêu tụ điện hữu cơ thế cao (Organic Supercapacitor) - KHUYÊN DÙNG ĐỂ VIẾT BÁO MỚI**
    *   *Vật liệu & Hệ đo:* Carbon Aerogel ($N-CA$ hoặc $Fe/N-CA$) phủ lên Nickel foam (WE) + Pt wire (CE) + Non-aqueous Silver Ion RE.
    *   *Chất điện ly hữu cơ:* $1.0\text{ M } TEABF_4$ hoặc $1.0\text{ M } LiClO_4$ trong Acetonitrile.
    *   *Kỹ thuật:* Quét CV thế cao ($0\text{ V} \rightarrow 3.0\text{ V}$), phóng nạp GCD ($0.5 - 10\text{ A/g}$), trở kháng EIS hữu cơ.
*   **Định hướng 2: Cảm biến hữu cơ kỵ nước trong dung môi hỗn hợp (Mixed-Solvent Sensor)**
    *   *Đối tượng đo:* Thuốc trừ sâu (Carbaryl, Chlorpyrifos) hoặc Bisphenol A.
    *   *Môi trường & Hệ đo:* Acetonitrile/Nước (tỷ lệ 50/50) + Non-aqueous Silver Ion RE + DPV/SWV quét thế phân cực anode.

---

*→ Quy trình đầy đủ: `1_Protocol_Synthesis.md` | Điện hóa: `2_Protocol_Electrochemistry.md` | Đặc trưng vật liệu: `4_Material_Characterization.md` | Checklist: `6_Quality_Gates_Checklist.md`*

