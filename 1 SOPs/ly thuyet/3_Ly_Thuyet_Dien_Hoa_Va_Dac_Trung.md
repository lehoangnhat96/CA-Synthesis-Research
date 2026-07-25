# 3_Ly_Thuyet_Dien_Hoa_Va_Dac_Trung.md — Lý Thuyết Điện Hóa Phân Tích & Phân Tích Đặc Trưng Vật Liệu
<!-- v1.0 | Thiết lập: 2026-06-03 -->

Tài liệu này tổng hợp lý thuyết cơ sở điện hóa phân tích phân tích vết và các phép đặc trưng cấu trúc vật lý của màng cảm biến biến tính bằng Carbon Aerogel.

---

## I. LÝ THUYẾT CV & PHÉP ĐO BASLINE PROBE

Quét thế tuần hoàn (Cyclic Voltammetry - CV) trong dung dịch chỉ thị oxi hóa-khử $K_3Fe(CN)_6$ bão hòa $KCl$ là công cụ cốt lõi để đánh giá tính chất điện hóa của điện cực làm việc.

### 1. Phản ứng chỉ thị điện hóa thuận nghịch
Cặp chỉ thị $Fe(CN)_6^{3-/4-}$ là hệ thuận nghịch điện hóa điển hình với phản ứng:
$$Fe(CN)_6^{3-} + e^- \rightleftharpoons Fe(CN)_6^{4-}$$
Động học phản ứng tuân theo phương trình dòng đỉnh Randles-Sevcik cho quá trình khuếch tán kiểm soát ở $25\text{ }^\circ\text{C}$:
$$I_p = (2.69 \times 10^5) \cdot n^{3/2} \cdot A \cdot D^{1/2} \cdot C_0^* \cdot v^{1/2}$$
Trong đó:
*   $I_p$: Dòng điện đỉnh (anode $I_{pa}$ hoặc cathode $I_{pc}$, A).
*   $n$: Số electron trao đổi ($n = 1$).
*   $A$: Diện tích hoạt tính điện hóa hiệu dụng ($EASA$, $\text{cm}^2$).
*   $D$: Hệ số khuếch tán ($D \approx 7.6 \times 10^{-6}\text{ cm}^2\text{/s}$ của ferricyanide trong $0.1\text{ M KCl}$).
*   $C_0^*$: Nồng độ chỉ thị trong dung dịch nền ($\text{mol/cm}^3$).
*   $v$: Tốc độ quét thế ($\text{V/s}$).

### 2. Tiêu chí đánh giá chất lượng màng qua thế tách đỉnh ($\Delta E_p$)
Khoảng cách giữa hai đỉnh thế hiệu dòng:
$$\Delta E_p = E_{pa} - E_{pc}$$
*   **Với điện cực trần lý tưởng (bare GCE):** $\Delta E_p \approx 59\text{ mV}/n \approx 59\text{ mV}$ ở tốc độ quét chậm. Trong thực tế lab, GCE sạch đạt $\Delta E_p \le 80\text{ mV}$.
*   **Khi phủ màng Carbon Aerogel biến tính:** Độ dẫn điện tốt và diện tích bề mặt lớn làm tăng dòng đỉnh $I_{pa}$ vượt trội. Tiêu chí đạt chất lượng màng là **$\Delta E_p < 120\text{ mV}$** ở tốc độ quét $50\text{ mV/s}$.
*   *Nếu $\Delta E_p > 150\text{ mV}$:* Chứng tỏ màng carbon có độ dẫn điện kém, trở kháng nội điện cực lớn hoặc lớp phủ quá dày cản trở sự chuyển khối (Fail).

---

## II. PHỔ TRỞ KHÁNG ĐIỆN HÓA (EIS) & MẠCH TƯƠNG ĐƯƠNG RANDLES

EIS đo lường trở kháng phức $Z(\omega) = Z' - jZ''$ bằng cách áp dao động xoay chiều tần số nhỏ. Giản đồ Nyquist ($Z'$ vs. $-Z''$) của hệ được phân tích thông qua mạch tương đương Randles sửa đổi:

```
                  ┌───────[ Rct ]───────[ Zw ]───────┐
                  │                                  │
    ───[ Rs ]─────┴───────────────[ CPE ]────────────┴───
```

### 1. Ý nghĩa vật lý của các linh kiện trong mạch
1.  **$R_s$ (Solution Resistance):** Điện trở của dung dịch đệm điện ly và dây dẫn. Biểu diễn bằng giao điểm của đường cong Nyquist với trục hoành $Z'$ ở vùng tần số cực cao.
2.  **$R_{ct}$ (Charge Transfer Resistance):** Điện trở chuyển điện tích của phản ứng redox tại bề mặt phân giới điện cực/dung dịch. Biểu diễn bằng đường kính của vòng bán nguyệt ở vùng tần số cao và trung bình.
3.  **$CPE$ (Constant Phase Element):** Thay thế cho tụ điện lớp kép ($C_{dl}$) để hiệu chỉnh sự gồ ghề và không đồng nhất về mặt hình học của bề mặt Carbon Aerogel xốp. Trở kháng $Z_{CPE} = \frac{1}{Y_0(j\omega)^n}$ (với $n$ từ $0.8 - 0.95$).
4.  **$Z_W$ (Warburg Impedance):** Trở kháng khuếch tán của chất phản ứng từ lòng dung dịch đến bề mặt điện cực. Biểu diễn bằng đường thẳng nghiêng góc $\approx 45^\circ$ ở vùng tần số thấp.

### 2. Tiêu chí Gate 5 điện hóa
*   Lớp biến tính Carbon Aerogel có độ dẫn điện cao và nhiều khuyết tật hoạt tính giúp tăng tốc độ chuyển điện tích, làm bán kính vòng bán nguyệt co nhỏ lại.
*   **Tiêu chí bắt buộc:**
    $$R_{ct}\text{(Fe/N-CA)} < R_{ct}\text{(N-CA)} < R_{ct}\text{(bare GCE)}$$
    Chứng minh tâm hoạt tính sắt Fe-N₄ thúc đẩy động học chuyển electron nhanh hơn hẳn nền carbon thường.

---

## III. LÝ THUYẾT CỰC PHỔ HÒA TAN SÓNG VUÔNG (SWASV) ĐO KIM LOẠI NẶNG

SWASV là phương pháp phân tích vết kim loại cực kỳ nhạy nhờ tích hợp 2 giai đoạn:

### 1. Giai đoạn lắng khử (Accumulation/Deposition Step)
Áp một thế âm cực mạnh (**$-1.1\text{ V}$ vs. Ag/AgCl**) dưới lực khuấy từ mạnh 400 rpm:
*   Các cation kim loại nặng ($Pb^{2+}, Cd^{2+}, Zn^{2+}$) khuếch tán đối lưu nhanh đến bề mặt điện cực và bị khử điện hóa thành kim loại tự do bám trên vách carbon:
    $$\text{M}^{2+} + 2e^- \rightarrow \text{M}^0\text{ (bám dính trên CA)}$$
*   Động học lắng phụ thuộc vào tốc độ khuấy (convective mass transfer) và mật độ các nhóm Pyridinic-N/tâm Fe-N₄ bắt giữ ion trên màng.

### 2. Giai đoạn hòa tan (Stripping Step)
Ngừng khuấy từ, để tĩnh dung dịch trong 15 giây. Quét thế phân cực anode sóng vuông tần số cao:
*   Các kim loại bị oxy hóa và hòa tan trở lại dung dịch tại thế đặc trưng của từng kim loại:
    $$\text{M}^0\text{ (bám trên CA)} \rightarrow \text{M}^{2+} + 2e^-$$
*   **Cơ chế sóng vuông (Square Wave):** Tần số xung cao cho phép đo dòng điện tại hai thời điểm cuối xung dương và xung âm. Hiệu dòng thu được loại bỏ hoàn toàn dòng điện dung phóng nạp không Faraday ($I_c$), chỉ thu nhận dòng Faraday ($I_f$), giúp hạ giới hạn phát hiện ($LOD$) xuống mức dải vết cực thấp (< 0.1 ppb).

---

## IV. LÝ THUYẾT QUÉT THẾ XUNG VI PHÂN (DPV) ĐO PARACETAMOL

DPV áp dụng các xung thế chồng lên thế quét tuyến tính chậm, đo dòng trước khi áp xung và cuối xung để loại dòng điện dung.

### 1. Cơ chế phản ứng oxi hóa Paracetamol (APAP)
Oxi hóa Paracetamol trên điện cực biến tính carbon aerogel là quá trình chuyển đổi thuận nghịch giả 2 electron và 2 proton ($2e^-, 2H^+$):

$$\text{APAP (Paracetamol)} \rightleftharpoons \text{NAPQI (N-acetyl-p-benzoquinone imine)} + 2H^+ + 2e^-$$

*   Sự hiện diện của các nhóm chức ưa nước và mạng lưới mao quản xốp của N-CA giúp bắt giữ paracetamol qua tương tác liên phân tử liên kết hydro và tương tác $\pi-\pi$ stacking thơm, tăng mật độ tích lũy chất phân tích sát bề mặt.

---

## V. LÝ THUYẾT CÁC PHÉP ĐẶC TRƯNG VẬT LIỆU

### 1. Raman Spectroscopy (Cấu trúc khuyết tật mạng)
*   **$D$-band ($\approx 1350\text{ cm}^{-1}$):** Dao động của cấu trúc lai hóa $sp^3$ của nguyên tử carbon khuyết tật, mép phiến graphit hoặc nối với dị tố (N, O).
*   **$G$-band ($\approx 1580\text{ cm}^{-1}$):** Dao động kéo giãn $C-C$ trong mặt phẳng lai hóa $sp^2$ của vòng thơm graphit tinh thể.
*   **Tỷ số $I_D/I_G$:** Đánh giá mật độ khuyết tật.
    *   Với carbon aerogel làm cảm biến, tỷ lệ **$I_D/I_G = 0.9 - 1.2$** là tối ưu. Tỷ lệ này cân bằng giữa: (1) Mật độ khuyết tật đủ lớn để cung cấp các active sites bắt giữ ion; (2) Mạng lưới graphite sp² đủ nguyên vẹn để dẫn điện tốt.

### 2. XPS Spectroscopy (Hóa học bề mặt và liên kết phối trí)
*   **Phân tích N 1s:** Giải phổ (deconvolution) xác định tỉ lệ Pyridinic-N (398.5 eV), Pyrrolic-N (400.1 eV), và Graphitic-N (401.2 eV). Để làm cảm biến Pb²⁺ tốt, Pyridinic-N phải đạt **$\ge 45\%$** diện tích đỉnh.
*   **Phân tích Fe 2p:** Đỉnh $Fe 2p_{3/2}$ ở **$710.8 - 711.5\text{ eV}$** là bằng chứng xác thực cho sự phối trí của sắt đơn nguyên tử với nitơ ($Fe-N_x$), phân biệt rõ với sắt metallic $Fe^0$ ($707\text{ eV}$) và sắt oxit tự do ($712\text{ eV}$ trở lên).

### 3. BET Surface Area Analysis (Phân bố kích thước lỗ xốp)
*   Isotherm hấp phụ-khử hấp phụ $N_2$ của Carbon Aerogel từ xơ dừa thuộc **Isotherm Loại IV (Type IV Isotherm)** với vòng lặp trễ hysteresis loop đặc trưng cho vật liệu mesopores ($2 - 50\text{ nm}$).
*   Diện tích bề mặt riêng **$S_{\text{BET}} > 300\text{ m}^2\text{/g}$** cùng phân bố thể tích lỗ xốp BJH tập trung ở dải mesopores bảo đảm dung dịch điện ly khuếch tán nhanh nhất, tránh hiện tượng bít tắc lỗ xốp khi biến tính mực in điện cực.
