# 6_Quality_Gates_Checklist.md — Phiếu Kiểm Soát Chất Lượng Lab (Lab Check-sheet)

<!-- v1.1 | Cập nhật: 2026-05-31 | Sửa T_anneal 800→750℃ | Hợp nhất từ: synthesis_outline_verified Phần 1 + SYNTHESIS_PARAMETERS §16, 22 -->

> [!IMPORTANT]
> * **Quy trình tổng hợp đầy đủ:** `1_Protocol_Synthesis.md`
> * **Quy trình điện hóa đầy đủ:** `2_Protocol_Electrochemistry.md`
>
> Phiếu kiểm soát này được thiết kế để **in trực tiếp ra giấy** hoặc tích điện tử trong nhật ký phòng thí nghiệm. Từng mẻ tổng hợp (N-CA hoặc Fe/N-CA) bắt buộc phải hoàn thành đầy đủ các Quality Gates dưới đây trước khi chuyển sang bước tiếp theo.

---

## PHẦN 1. CHECKLIST TRIỂN KHAI MẺ TỔNG HỢP MỚI

*Mẻ số: __________________ | Ngày: __________________ | Người làm: __________________*

| Bước | Nội dung kiểm tra | ✓ | Thông số thực tế | Tiêu chí đạt |
|:---|:---|:---:|:---|:---|
| **GĐ 0** | Cân m₀ xơ dừa khô trước kiềm hóa | `[ ]` | m₀ = ________ g | Sấy 105 ℃ đến khối lượng không đổi |
| | Pha dung dịch kiềm NaOH | `[ ]` | V_NaOH = ________ mL | NaOH 6 wt% (pha 48 g NaOH / 752 mL nước DI, tỷ lệ 1 g : 20 mL) |
| | Cân m₁ xơ dừa khô sau kiềm hóa | `[ ]` | m₁ = ________ g | Sấy 105 ℃ đến khối lượng không đổi |
| | Tính Weight-loss % | `[ ]` | WL = ________ % | **Dải đạt: 30–38%** |
| **GĐ 1** | Cân cellulose DCF | `[ ]` | m_DCF = ________ g | 1.00 g ± 0.01 g |
| | Đong dung môi | `[ ]` | 11 mL NH₃ : 4 g Urea : 5 mL H₂O | Đúng tỷ lệ |
| | Kiểm soát nhiệt độ ice bath siêu âm | `[ ]` | T_max = ________ ℃ | **≤ 10 ℃ — bắt buộc** |
| | Siêu âm xung 30 phút (2s on/1s off) | `[ ]` | t = ________ phút | Sol đồng nhất, không còn sợi thô |
| | Bảo quản sol ngăn mát | `[ ]` | t ổn định = ________ giờ | **0–5 ℃ trong 24 giờ để ổn định** |
| **GĐ 2** | Đúc khuôn Silicone, ổn định 0–5 ℃ | `[ ]` | t de-gas = ________ phút | 15–30 phút gõ nhẹ đuổi bọt + khử bọt khí |
| | Cấp đông gel hóa | `[ ]` | T = ________ ℃ | **−14 ℃ đến −20 ℃ / 24h** |
| **GĐ 3** | Rã đông tự nhiên 25 ℃ | `[ ]` | t rã đông = ________ phút | **1 giờ** (tinh thể đá tan hết) |
| | Ngâm Ethanol 96–98% (Tỉ lệ 10:1 v/v) | `[ ]` | V_cồn = ________ mL | **Tỉ lệ 10:1 (v/v) so với dung môi gel** (~200 mL cồn cho mẻ 1g DCF) · 25 ± 2 ℃ / 24h |
| | Rửa trao đổi DI water (GĐ 3b) | `[ ]` | Số lần = ________ | **2 lần, mỗi lần 2h (chính xác)** — không rửa quá 3 lần |
| **GĐ 4** | Cấp đông sâu trước sấy | `[ ]` | T = ________ ℃ | **−20 ℃ đến −40 ℃ / ≥ 12h** |
| | Sấy thăng hoa | `[ ]` | P = ________ Pa | **< 20 Pa · bẫy lạnh ≤ −45 ℃ · 24–48h** |
| | Đo shrinkage tuyến tính | `[ ]` | Shrinkage = ________ % | **< 12%** |
| **GĐ 5** | Purge N₂ trước nung | `[ ]` | t purge = ________ phút | 150–200 mL/min / 30 phút |
| | Chương trình nhiệt 3 ramps | `[ ]` | T_target = ________ ℃ | **N-CA: 700 ℃ · Fe/N-CA nền: 800 ℃ (giữ 2h)** |
| **GĐ 6** | Cân FeCl₃·6H₂O | `[ ]` | m_Fe = ________ g | **1%: 0.0484 g · 5%: 0.242 g** (trên 1 g carbon) |
| | Ngâm tẩm Fe trong ethanol | `[ ]` | t = ________ giờ | Siêu âm nhẹ 30 phút + ngâm tĩnh 24h / 25 ℃ |
| **GĐ 7a** | Acid leaching HCl 0.5 M | `[ ]` | t = ________ giờ | **80 ± 2 ℃ / 8h liên tục** |
| | Rửa DI đến trung tính | `[ ]` | pH nước rửa = ________ | **pH 6.5–7.0** · sấy 80 ℃ / 12h |
| **GĐ 7b** | Annealing lần 2 | `[ ]` | T = ________ ℃ | **750 ℃ / 1h / N₂ — đã chốt 2026-05-31** |

---

## PHẦN 2. 5 QUALITY GATES ĐIỆN CỰC (GCE Baseline)

*Tất cả 5 gates phải PASS trước khi đo cảm biến.*

```
   ┌───────────────────────────┐
   │  GATE 1 · Raman I_D/I_G  │  →  Pass: 0.9 – 1.2
   └─────────────┬─────────────┘
                 ▼
   ┌───────────────────────────┐
   │  GATE 2 · XPS N / Fe     │  →  Pass: N 3–6 at% · Fe 0.4–1.5 at% · N:Fe ≥ 4:1
   └─────────────┬─────────────┘
                 ▼
   ┌───────────────────────────┐
   │  GATE 3 · BET S_BET      │  →  Pass: > 300 m²/g
   └─────────────┬─────────────┘
                 ▼
   ┌───────────────────────────┐
   │  GATE 4 · CV ΔEp         │  →  Pass: < 120 mV
   └─────────────┬─────────────┘
                 ▼
   ┌───────────────────────────┐
   │  GATE 5 · EIS Rct        │  →  Pass: Rct(Fe/N-CA) < Rct(N-CA) < Rct(bare GCE)
   └───────────────────────────┘
```

| Gate | Kỹ thuật | Tiêu chí Pass | Kết quả | Pass/Fail | Khắc phục nếu Fail |
|:---:|:---|:---|:---|:---:|:---|
| **1** | Raman | I_D/I_G = **0.9–1.2** | ________ | | Cao → giảm T nung · Thấp → tăng T nung |
| **2** | XPS | N: **3–6 at%** · Fe: **0.4–1.5 at%** · Pyridinic-N **≥ 45%** | N=____% Fe=____% | | N thấp → ice bath chặt hơn · Fe lệch → kiểm tra cân |
| **3** | BET N₂ | S_BET **> 300 m²/g** | ________ m²/g | | BET thấp → rà soát áp suất sấy + bẫy lạnh |
| **4** | CV (K₃Fe(CN)₆) | **ΔEp < 120 mV** | ________ mV | | Màng quá dày → giảm về 5 µL, pha loãng mực |
| **5** | EIS (K₃Fe(CN)₆) | **Rct(Fe/N-CA) < Rct(N-CA) < Rct(GCE)** | ________ Ω | | Fe-Nₓ chưa phối trí → tăng cường acid leaching |

---

## PHẦN 3. PHÊ DUYỆT MẺ

*Chỉ khi cả 5 Gates PASS mới được phép tiến hành khảo sát cảm biến (SWASV / DPV).*

* **Ý kiến hướng dẫn:**
  ____________________________________________________________________________

* **Chữ ký xác nhận:** __________________________________ *Ngày: ____/____/2026*
