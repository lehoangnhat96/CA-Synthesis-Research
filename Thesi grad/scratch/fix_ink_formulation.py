import sys

sys.stdout.reconfigure(encoding='utf-8')

draft_path = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\0 Master_Thesis_Full_Draft.md"

with open(draft_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Correct the Ink formulation section in Stage 8
old_ink_sec = """| **Bột Fe/N-CA** (đã qua rây < 75 µm) | — | **5.0 mg ± 0.01 mg** cho 1 mL ink | Cân trực tiếp |
| **DMF** (N,N-Dimethylformamide, HPLC grade) | Nguyên chất | **950 µL** (làm dung môi chính) | Đong bằng micropipette chính xác |
| **Nafion 0.5 wt%** (pha từ Nafion 5% thương mại) | 0.5 wt% | **50 µL** trộn vào ink | Pha loãng 1:9 (Nafion 5% : DMF) trước |
| **Chitosan 2 wt% (2.0 g/100 mL acetic acid 0.17 M)** (pha trong acetic acid 1%) | 1 wt% | Kết hợp cùng Nafion trong 50 µL binder | Pha riêng, sau đó trộn với Nafion 0.5% theo tỉ lệ 1:1 thể tích |

> [!NOTE]
> **Tỉ lệ tổng Ink (1 mL):** 5 mg Fe/N-CA + 950 µL DMF + 50 µL Composite Binder (Chitosan 2% + Nafion 0.5%).
> Nồng độ ink = **5 mg/mL**. Mỗi lần drop-cast 5 µL → nạp ~25 µg vật liệu/điện cực."""

new_ink_sec = """| Hóa chất | Nồng độ | Thể tích cho 1 mL Ink | Cách chuẩn bị chuẩn y văn (CA 4 & CA 8) |
|---|---|---|---|
| **Bột Fe/N-CA** (rây < 75 µm) | — | **2.0 mg ± 0.01 mg** | Cân trực tiếp |
| **Ethanol tuyệt đối / Nước DI** | Tỉ lệ 4:1 v/v | **800 µL Ethanol + 150 µL Nước DI** | Thay thế hoàn toàn DMF để tránh làm kết tủa Chitosan và tránh tồn dư dung môi sôi cao |
| **Dung dịch Chitosan 0.5 wt%** | 0.5 wt% trong acetic acid 0.17 M | **50 µL** | Hòa tan Chitosan trong acid acetic 0.17 M (pH 5.0), khuấy tan hoàn toàn |
| **Nafion 0.5 wt%** | 0.5 wt% trong Isopropanol/Water | **10–20 µL** (tùy chỉnh) | Pha loãng từ Nafion 5% thương mại bằng Ethanol |

> [!IMPORTANT]
> **Hiệu chỉnh Công thức Ink Chuẩn Y Văn (1 mL):** 
> 2.0 mg Fe/N-CA + 800 µL Ethanol + 150 µL Nước DI + 50 µL dung dịch Chitosan 0.5% (hoặc 10–20 µL Nafion 0.5%).
> Nồng độ ink chuẩn = **2.0 mg/mL**. Thể tích drop-cast **3.0–5.0 µL** $\rightarrow$ Tải lượng nạp tối ưu **6.0–10.0 µg** vật liệu/điện cực (giúp màng mỏng mịn, khô nhanh trong 30–45 phút ở 25°C và không bị tróc màng)."""

if old_ink_sec in text:
    text = text.replace(old_ink_sec, new_ink_sec)
    with open(draft_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Corrected Ink Formulation SOP in draft!")
else:
    print("Old ink section not found via exact match, running substring fix...")
    # let's search for DMF in Section 2a
    idx = text.find("### 2a. Danh sách hóa chất cần chuẩn bị để pha Ink")
    idx_2b = text.find("### 2b. Quy trình pha Ink step-by-step")
    if idx != -1 and idx_2b != -1:
        text = text[:idx] + "### 2a. Danh sách hóa chất cần chuẩn bị để pha Ink\n\n" + new_ink_sec + "\n\n" + text[idx_2b:]
        with open(draft_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print("Updated section 2a via range replacement!")
