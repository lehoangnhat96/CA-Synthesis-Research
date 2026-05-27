# Final_SOPs_CA.md — Hướng Dẫn Thực Nghiệm Rút Gọn & Tinh Giản Chế Tạo Carbon Aerogel Điện Hóa

> [!NOTE]
> * **Tài liệu tham chiếu chuẩn cốt lõi:**
>   1. Luận án Tiến sĩ Nguyễn Trần Xuân Phương 2024 (Tài liệu: `TOM_TAT_NTXPhuong.md` trong thư mục `08_Review_va_Tong_quan`).
>   2. Công trình Fauziyah et al. 2020 (Ind. Eng. Chem. Res.) (Tài liệu: `2 Nitrogen-Doped Carbon Aerogels Prepared by Direct Pyrolysis of.md` trong thư mục `02_Doping_va_Gel_hoa`).
>   3. Công trình Wu et al. 2024 (Sensors) (Tài liệu: `1 Facile Synthesis of Fe-Doped Algae Residue-Derived Carbon Aerogels for.md` trong thư mục `02_Doping_va_Gel_hoa`).

---

## PHẦN I: MA TRẬN ĐIỀU KIỆN PHẢN ỨNG VÀ THÔNG SỐ THỰC NGHIỆM TỔNG HỢP

Bảng tổng hợp toàn bộ các thông số điều kiện phản ứng cốt lõi ($T$, $t$, $C$, $Ratio$) từ GĐ0 đến GĐ6:

| Giai đoạn | Quy trình thao tác | Nhiệt độ ($T$) | Thời gian ($t$) | Nồng độ ($C$) | Tỉ lệ phản ứng / phối trộn ($Ratio$) |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **GĐ0A** | Kiềm hóa xơ dừa | $80 \pm 2^\circ\text{C}$ | $4\text{ giờ}$ | $6\text{ wt}\%\text{ }NaOH$ | $1\text{g bột} : 20\text{ mL dung dịch}$ |
| **GĐ0B** | Tẩy trắng sợi | $60^\circ\text{C}$ | $2\text{ giờ}$ | $10\text{ wt}\%\text{ }H_2O_2$ | $1\text{g bột} : 20\text{ mL dung dịch}$ ($pH \approx 11$) |
| **GĐ0C** | Thủy phân acid | $60^\circ\text{C}$ | $2\text{ giờ}$ | $2.0\text{ M }HCl$ | $1\text{g bột} : 20\text{ mL dung dịch}$ |
| **GĐ1A** | Sol $NH_4OH$-Urea (Chính) | $\le 10^\circ\text{C}$ | $30\text{ phút}$ | $25\text{ wt}\%\text{ }NH_4OH$ | $1.0\text{g BCF} : 11\text{ mL NH}_4\text{OH} : 4.0\text{g Urea} : 5\text{ mL H}_2\text{O}$ |
| **GĐ1B** | Sol $NaOH$-Urea (Đối chứng) | $-10^\circ\text{C} \text{ đến } -12^\circ\text{C}$ | $5\text{ phút}$ | $7\%/12\%/81\%$ | $7\text{ wt}\% NaOH : 12\text{ wt}\% Urea : 81\text{ wt}\% H_2O$ |
| **GĐ2A** | Gel hóa $NH_4OH$-Urea | $80^\circ\text{C}$ | $2\text{ giờ}$ | — | Đúc khuôn ống tiêm Polypropylene (PP) |
| **GĐ2B** | Gel hóa $NaOH$-Urea | $50 - 55^\circ\text{C}$ | $1.5\text{ giờ}$ | — | Đúc khuôn ống tiêm Polypropylene (PP) |
| **GĐ3A** | Keo tụ (Solvent Exchange) | $0 - 5^\circ\text{C}$ | $24\text{ giờ}$ | $98\text{ vol}\%\text{ Ethanol}$ | $15\text{ mL Ethanol} : 1\text{g cellulose}$ ban đầu |
| **GĐ3B** | Tẩm sắt ($Fe$-doping) | $0 - 5^\circ\text{C}$ | $24\text{ giờ}$ | $10\text{ wt}\%\text{ }Fe$ | $1.0\text{g gel} : 0.484\text{g FeCl}_3\cdot6\text{H}_2\text{O} : 1.0\text{g Urea} : 30\text{ mL DI}$ |
| **GĐ4** | Sấy thăng hoa chân không | $-80^\circ\text{C}$ (đông) / $\le -50^\circ\text{C}$ (bẫy) | $36 - 48\text{ giờ}$ | $P < 20\text{ Pa}$ | Thăng hoa trực tiếp tinh thể đá |
| **GĐ5A** | Nhiệt phân $N$-CA | $700^\circ\text{C}$ | $2\text{ giờ}$ | $5^\circ\text{C/phút}$ | Lưu lượng khí bảo vệ $N_2 = 100\text{ mL/phút}$ |
| **GĐ5B** | Nhiệt phân $Fe/N$-CA (nền) | $800^\circ\text{C}$ | $2\text{ giờ}$ | $5^\circ\text{C/phút}$ | Lưu lượng khí bảo vệ $N_2 = 100\text{ mL/phút}$ |
| **GĐ6A** | Acid Leaching | $80 \pm 2^\circ\text{C}$ | $8\text{ giờ}$ | $0.5\text{ M }HCl$ | $1\text{g bột} : 100\text{ mL dung dịch }HCl$ (đun hồi lưu) |
| **GĐ6B** | Annealing lần 2 | $800^\circ\text{C}$ | $1\text{ giờ}$ | $5^\circ\text{C/phút}$ | Lưu lượng khí bảo vệ $N_2 = 100\text{ mL/phút}$ |

---

## PHẦN II: QUY TRÌNH THAO TÁC CÁC GIAI ĐOẠN CHẾ TẠO (GĐ0 ĐẾN GĐ6)

### GIAI ĐOẠN 0: TIỀN XỬ LÝ TÁCH CHIẾT CELLULOSE TINH KHIẾT (Raw Material Pretreatment)

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
*   **Kiềm hóa DCF:**
    1. Ngâm $50\text{ g}$ bột xơ dừa khô ($<125\text{ }\mu\text{m}$) trong $1000\text{ mL}$ nước nóng ($80^\circ\text{C}$) khuấy từ $4\text{ giờ}$ để rửa sơ bộ.
    2. Cho bã lọc vào $1000\text{ mL}$ dung dịch $NaOH$ $6\text{ wt}\%$ (tỉ lệ $1:20\text{ w/v}$).
    3. Đun ở $80 \pm 2^\circ\text{C}$ trong $4\text{ giờ}$ liên tục, khuấy từ $600\text{ rpm}$.
    4. Lọc qua phễu Buchner, rửa bằng nước DI nóng đến $pH$ trung tính. Sấy bột ở $80^\circ\text{C}$ trong $8\text{ giờ}$.
*   **Tẩy trắng Bleached coir fiber:**
    1. Cho $30\text{ g}$ bột kiềm hóa DCF vào $600\text{ mL}$ dung dịch $H_2O_2$ $10\text{ wt}\%$ (tỉ lệ $1:20\text{ w/v}$).
    2. Kiềm hóa nhẹ bằng $NaOH$ đến $pH \approx 11$.
    3. Khuấy đun cách thủy ở $60^\circ\text{C}$ trong $2\text{ giờ}$, tốc độ khuấy $300\text{ rpm}$.
    4. Lọc, rửa nước cất DI đến $pH$ trung tính.
*   **Thủy phân acid thu BCF:**
    1. Cho sợi tẩy trắng vào $600\text{ mL}$ dung dịch $HCl$ $2.0\text{ M}$ (tỉ lệ $1:20\text{ w/v}$).
    2. Đun hồi lưu ở $60^\circ\text{C}$ trong $2\text{ giờ}$, tốc độ khuấy $400\text{ rpm}$.
    3. Lọc, rửa DI đến $pH$ trung tính.
    4. Sấy ở $80^\circ\text{C}$ trong $12\text{ giờ}$. Rây mịn thu bột Bleached Coir Fiber (BCF).

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Hao hụt khối lượng DCF (Gravimetric Weight-loss %):** Phải đạt **$30\% - 38\%$** (Đạt chuẩn loại lignin).
*   **Đường kính sợi (SEM):** Co rút còn **$10 - 20\text{ }\mu\text{m}$** (RCF ban đầu là $80 - 100\text{ }\mu\text{m}$).
*   **Độ tinh thể hóa (XRD):** Đạt **$\ge 55\%$** (Xuất hiện các đỉnh Cellulose I tại góc quét $2\theta \approx 16.08^\circ$ (110) và $22.23^\circ$ (200)).
*   **Độ sạch Xenluloza:** Hàm lượng cellulose trong bột BCF khô phải đạt **$\ge 92\text{ wt}\%$** (không còn đỉnh ester tại $1735\text{ cm}^{-1}$ trên phổ FT-IR).

---

### GIAI ĐOẠN 1: TỔNG HỢP HỆ SOL CELLULOSE & ĐỐI CHỨNG DUNG MÔI ĐIỆN HÓA (Sol Preparation)

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
*   **Hệ dung môi chính Ammonia-Urea ($NH_4OH$-Urea):**
    1. Cân chính xác $1.0\text{ g}$ Cellulose BCF + hòa tan $4.0\text{ g}$ Urea tinh thể vào hỗn hợp $11.0\text{ mL } NH_4OH$ đậm đặc ($25\text{ wt}\%$) và $5.0\text{ mL}$ nước cất DI trong bình Teflon đậy kín.
    2. Cho $1.0\text{ g}$ BCF vào bình dung môi.
    3. Đặt bình vào bể siêu âm đầy đá nước lạnh duy trì **$\le 10^\circ\text{C}$ (tối ưu $0 - 5^\circ\text{C}$)**.
    4. Siêu âm xung (**$2\text{ giây ON} / 1\text{ giây OFF}$**) trong **$30\text{ phút}$** ở công suất trung bình.
    5. Thu được hệ sol màu hơi đục nhẹ, hoàn toàn đồng nhất.
*   **Hệ dung môi đối chứng $NaOH$-Urea (Đo siêu tụ):**
    1. Định lượng tỷ lệ khối lượng chuẩn $7\text{ wt}\% NaOH : 12\text{ wt}\% Urea : 81\text{ wt}\% H_2O$.
    2. Làm lạnh dung dịch về **$-10^\circ\text{C}$ đến $-12^\circ\text{C}$** trong tủ đông sâu đến trạng thái bán đóng băng (slushy).
    3. Cho nhanh $1.0\text{ g}$ BCF vào dung môi lạnh, khuấy từ tốc độ cao $3000\text{ rpm}$ trong **$5\text{ phút}$** ở nhiệt độ phòng. Thu được hệ sol trong suốt.

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Trạng thái Sol:** Đồng nhất, hoàn toàn không còn xơ sợi chưa tan bám đáy.
*   **Nhiệt độ bể siêu âm hệ $NH_4OH$:** Phải khống chế **$\le 10^\circ\text{C}$** trong suốt quá trình. Nếu nhiệt độ $>15^\circ\text{C}$, $NH_3$ bay hơi đột ngột gây hỏng sol (Fail).
*   **XRD của hydrogel:** Xuất hiện các đỉnh đặc trưng của Cellulose III tại góc $2\theta \approx 11.6^\circ$ (110) và $20.5^\circ$ (002). Đỉnh Cellulose I ($22.23^\circ$) phải biến mất hoàn toàn.

---

### GIAI ĐOẠN 2: ĐÚC KHUÔN PP & GIÀ HÓA NHIỆT HÌNH THÀNH HYDROGEL (Casting & Gelation)

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Đúc khuôn và De-gassing:** Rót từ từ dung dịch sol lạnh vào các ống tiêm Polypropylene (PP) đã cắt bỏ đầu kim. Đặt đứng ống tiêm trong ngăn mát tủ lạnh ở **$0 - 5^\circ\text{C}$ trong thời gian $30 - 60\text{ phút}$** để khử hoàn toàn bọt khí.
2.  **Già hóa tạo gel (Thermal Gelation):** Bọc kín hai đầu ống tiêm.
    *   *Đối với hệ $NH_4OH$-Urea:* Đặt tĩnh ống tiêm già hóa ở nhiệt độ ổn định **$80^\circ\text{C}$ trong $2\text{ giờ}$** để tạo hydrogel dẻo dai màu nâu nhạt.
    *   *Đối với hệ đối chứng $NaOH$-Urea:* Đặt đứng ống tiêm vào bể nước ổn nhiệt duy trì ở **$50 - 55^\circ\text{C}$ trong $1.5\text{ giờ}$**.
3.  Dùng pít-tông nhẹ nhàng đẩy khối hydrogel ra ngoài.

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Hình thái Hydrogel:** Khối hydrogel monolith trụ nhẵn bóng, dẻo dai, đàn hồi tốt, hoàn toàn không bị nứt vỡ, móp méo hay rỗng ruột bọt khí.
*   **Tính ổn định:** Hydrogel giữ form 3D ổn định khi đặt đứng trên khay kính phẳng.

---

### GIAI ĐOẠN 3: KEO TỤ, TẨM ĐỐP Fe & KHÓA GIỮ UREA CÓ KIỂM SOÁT (Coagulation & Fe Impregnation)

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Keo tụ tái cấu trúc (Solvent Exchange):**
    *   Ngâm các khối hydrogel ẩm trong cồn **Ethanol $98\%$ lạnh duy trì ở $0 - 5^\circ\text{C}$** (tỷ lệ thể tích tối thiểu **$15\text{ mL ethanol} / 1\text{ g cellulose}$** ban đầu).
    *   Đậy kín nắp và ngâm tĩnh trong tủ mát $4^\circ\text{C}$ trong **$24\text{ giờ}$**.
    *   Gạn bỏ cồn cũ, ngâm rửa bằng nước cất DI sạch (gấp 5 lần thể tích gel) trong **$2\text{ giờ}$**, lặp lại **chính xác 2 lần** để loại bỏ amoniac tự do dư thừa.
    > [!IMPORTANT]
    > **⚠️ Cấm ngâm rửa quá mức:** Tuyệt đối không rửa nước cất quá 4 lần hoặc ngâm rửa kéo dài $>12\text{ giờ}$ để tránh làm trôi toàn bộ lượng phân tử Urea tự do trong mạng gel (nguồn $N$-doping duy nhất).
2.  **Tẩm Sắt (Dành cho nhánh mẫu $Fe/N$-CA):**
    *   Hòa tan hoàn toàn **$0.484\text{ g } FeCl_3\cdot6H_2O$** và $1.0\text{ g}$ Urea vào $30\text{ mL}$ nước cất DI lạnh ($0 - 5^\circ\text{C}$).
    *   Thả khối gel đã keo tụ vào dung dịch tẩm sắt.
    *   Siêu âm nhẹ trong $30\text{ phút}$ ở bể nước đá, sau đó ngâm tĩnh trong tủ mát $4^\circ\text{C}$ trong **$24\text{ giờ}$** liên tục để ion $Fe^{3+}$ khuếch tán bão hòa đều toàn lõi gel.

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Màu sắc hydrogel sau tẩm:** Khối hydrogel $N$-CA có màu trắng đục nhẹ đồng đều. Khối hydrogel $Fe/N$-CA ẩm phải chuyển hẳn sang **màu nâu đỏ/vàng cam đồng đều** từ lớp vỏ ngoài cho đến tận tâm lõi khối gel.
*   **Trạng thái gel:** Khối gel giữ nguyên cấu trúc trụ tròn, không bị mềm nhũn hay nứt vỡ.

---

### GIAI ĐOẠN 4: SẤY THĂNG HOA BẢO TOÀN CẤU TRÚC MAO QUẢN (Freeze Drying)

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Cấp đông sâu siêu tốc:** Đặt các khối gel ẩm sau tẩm vào tủ đông siêu sâu duy trì ở nhiệt độ **$-80^\circ\text{C}$** hoặc nhúng trực tiếp khối gel vào bình chứa Nitơ lỏng ($LN_2$, $-196^\circ\text{C}$) trong **$5\text{ phút}$**.
2.  **Sấy thăng hoa chân không:**
    *   Đảm bảo nhiệt độ bẫy lạnh đạt **$\le -50^\circ\text{C}$** (tối ưu $-80^\circ\text{C}$) và áp suất chân không **$< 20\text{ Pa}$ ($0.15\text{ Torr}$)**.
    *   Duy trì sấy thăng hoa liên tục trong **$36 - 48\text{ giờ}$**.
3.  Thu hồi aerogel xốp dẻo siêu nhẹ. Dùng thước kẹp đo kích thước để xác định độ co ngót.

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Độ co ngót tuyến tính (Linear Shrinkage %):** Phải đạt chỉ số **Linear Shrinkage $< 12\%$** tính theo công thức:
    $$\text{Shrinkage \%} = \frac{D_{\text{gel}} - D_{\text{aerogel}}}{D_{\text{gel}}} \times 100\%$$
    *   ✓ **Pass:** Shrinkage $< 12\%$.
    *   *   ✗ **Fail:** Shrinkage $\ge 20\%$ (cấu trúc mạng mao quản bị sụp đổ).
*   **Khối lượng riêng thể tích (Bulk density):** Duy trì trong dải **$0.03 - 0.05\text{ g/cm}^3$** (siêu nhẹ).

---

### GIAI ĐOẠN 5: NHIỆT PHÂN CARBON HÓA LẦN 1 & DOPING NITƠ (First Pyrolysis & N-doping)

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Chuẩn bị:** Xếp các khối aerogel khô vào thuyền sứ sạch, đẩy vào tâm nhiệt độ của lò nung ống thạch anh.
2.  **Purge đuổi Oxy bảo vệ:** Thổi dòng khí $N_2$ tinh khiết ($99.99\%$) với lưu lượng **$150 - 200\text{ mL/phút}$ liên tục trong $30\text{ phút}$** trước khi gia nhiệt. Duy trì dòng khí $N_2$ bảo vệ ổn định ở lưu lượng **$100\text{ mL/phút}$** trong suốt tiến trình nung.
3.  **Chương trình nhiệt phân 3 Ramp (Gia nhiệt $5^\circ\text{C/phút}$):**
    *   *Ramp 1 (Sấy ẩm sâu):* Nâng từ $25^\circ\text{C} \rightarrow 150^\circ\text{C}$, giữ nhiệt **$30\text{ phút}$**.
    *   *Ramp 2 (Carbon hóa sơ bộ):* Nâng từ $150^\circ\text{C} \rightarrow 400^\circ\text{C}$, giữ nhiệt **$30\text{ phút}$**.
    *   *Ramp 3 (Carbon hóa sâu & Doping):* Nâng từ $400^\circ\text{C} \rightarrow T_{\text{target}}$, giữ nhiệt liên tục trong **$2\text{ giờ}$ ($120\text{ phút}$)**.
    *   *Nhiệt độ mục tiêu ($T_{\text{target}}$):*
        *   **Nhánh mẫu $N$-CA:** Chọn **$T_{\text{target}} = 700^\circ\text{C}$**.
        *   **Nhánh mẫu $Fe/N$-CA (nền):** Chọn **$T_{\text{target}} = 800^\circ\text{C}$**.
4.  **Làm nguội:** Tắt gia nhiệt, để lò nguội tự nhiên dưới dòng khí $N_2$ thổi liên tục. Mở lò lấy mẫu khi nhiệt độ đầu đo đạt **$< 50^\circ\text{C}$**.

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **Trạng thái vật liệu sau nung:** Khối carbon aerogel thu được phải có **màu đen tuyền**, xốp, giữ nguyên hình monolith trụ ban đầu nhưng có sự co rút thể tích nhẹ. Bulk density đạt **$0.05\text{ g/cm}^3$ ($NH_3$-Urea)** hoặc **$0.07\text{ g/cm}^3$ ($NaOH$-Urea)**.
*   **Độ bền cơ học:** Thử nghiệm ép nén đạt Young Modulus ổn định từ **$6.43\text{ kPa}$ ($N$-CA)** đến **$138.59\text{ kPa}$ ($Fe/N$-CA)**.

---

### GIAI ĐOẠN 6: RỬA AXIT & ANNEALING LẦN 2 TẠO TÂM Fe-N₄ SIÊU SẠCH (Acid Leaching & Re-annealing)

#### 1. Quy trình thực nghiệm chuẩn (Step-by-Step Parameters)
1.  **Phản ứng Acid Leaching đun hồi lưu:**
    *   Sử dụng dung dịch **$HCl$ $0.5\text{ M}$** làm tác nhân hòa tan.
    *   Cho bột $Fe/N$-CA nung lần 1 vào bình cầu chứa dung dịch $HCl$ $0.5\text{ M}$ với tỷ lệ **$1\text{ g bột} / 100\text{ mL dung dịch}$**.
    *   Lắp hệ thống sinh hàn hồi lưu nước và đặt trên bếp khuấy từ đun sôi nhẹ ở nhiệt độ **$80 \pm 2^\circ\text{C}$ liên tục trong $8\text{ giờ}$** (tốc độ khuấy $200\text{ rpm}$).
2.  **Lọc rửa trung hòa:** Lọc chắt bột carbon qua phễu lọc chân không Buchner dùng giấy lọc sợi thủy tinh. Rửa liên tục bằng nước cất DI nóng ($60^\circ\text{C}$) cho đến khi nước rửa đạt $pH \approx 7.0$. Sấy khô bột ở $80^\circ\text{C}$ trong $12\text{ giờ}$.
3.  **Annealing tái hoạt hóa lần 2:**
    *   Đặt bột sấy khô vào lò nung ống thạch anh. Purge khí $N_2$ tương tự Giai đoạn 5.
    *   Thiết lập chương trình gia nhiệt $5^\circ\text{C/phút}$ lên đúng nhiệt độ mục tiêu **$800^\circ\text{C}$ và giữ nhiệt chính xác trong $1\text{ giờ}$ ($60\text{ phút}$)** dưới dòng khí $N_2$ bảo vệ ($100\text{ mL/phút}$).
    *   Để lò nguội tự nhiên về $<50^\circ\text{C}$ dưới dòng khí bảo vệ. Bảo quản bột trong vial thủy tinh tối màu quấn Parafilm cất ở tủ mát **$4^\circ\text{C}$**.

#### 2. Chỉ tiêu kiểm soát chất lượng (Pass/Fail Specification)
*   **XRD kiểm tra pha tinh thể sắt:** Giản đồ XRD của bột $Fe/N$-CA sau annealing lần 2 phải **hoàn toàn sạch**, biến mất toàn bộ các đỉnh nhiễu xạ sắc nhọn của sắt kim loại $\alpha-Fe$ ($2\theta \approx 44.7^\circ$) và sắt carbide $Fe_3C$ ($2\theta \approx 43.9^\circ$).
    *   ✓ **Pass:** $Fe$ phân tán đơn nguyên tử tuyệt đối (single-atom), không kết tinh pha thô.
    *   ✗ **Fail:** Vẫn xuất hiện đỉnh sắt tinh thể thô (quá trình rửa axit chưa đạt yêu cầu).
*   **Hàm lượng nguyên tố bề mặt (XPS):** Sắt đạt **$0.4 - 1.5\text{ at}\%$** và Nitơ đạt **$3.0 - 6.0\text{ at}\%$** với tỷ lệ tối thiểu $N:Fe \ge 4:1$.

---

## PHẦN III: QUY TRÌNH BIẾN TÍNH ĐIỆN CỰC LÀM VIỆC & ĐO ĐẠC ĐIỆN HÓA

### GIAI ĐOẠN 0: ĐÁNH BÓNG & ANODIZE HOẠT HÓA GCE

1.  **Mài mịn vật lý:** Nhỏ vài giọt nước cất và bột $Al_2O_3$ cỡ hạt $0.05\text{ }\mu\text{m}$ lên tấm nỉ mài. Đặt đứng điện cực GCE vuông góc 90° so với mặt nỉ, di chuyển mài nhẹ nhàng vẽ theo **hình số 8** liên tục trong **$2\text{ phút}$**.
2.  **Làm sạch siêu âm:** Nhúng GCE vào cốc nước cất DI, siêu âm làm sạch trong **$1\text{ phút}$** (lặp lại 3 lần với nước DI mới). Siêu âm tráng nhanh bằng cồn ethanol tuyệt đối trong **$1\text{ phút}$** để khử ẩm.
3.  **Anodize hoạt hóa kiềm:** Nhúng điện cực GCE vào dung dịch **$NaOH$ $0.1\text{ M}$**. Áp thế điện thế phân cực dương **$+1.8\text{ V}$ vs. $Ag/AgCl$ trong thời gian $10\text{ giây}$**. Rửa lại bằng nước cất DI.
4.  **Kiểm tra độ sạch (CV redox probe):**
    *   Dung dịch đo: **$5.0\text{ mM } K_3Fe(CN)_6$ trong nền $0.1\text{ M } KCl$**.
    *   Quét thế tuần hoàn CV ở tốc độ quét **$50\text{ mV/s}$** (quét 3 chu kỳ).
    *   ✓ **Tiêu chí Pass:** Thế hiệu đỉnh tách biệt **$\Delta E_p < 70\text{ mV}$** và tỷ số dòng điện đỉnh đối xứng **$I_{pa}/I_{pc} \approx 0.95 - 1.05$**.

### GIAI ĐOẠN 1: PHA CHẾ MỰC IN BINDER & PHỦ ĐIỆN CỰC (Drop-casting)

1.  **Định lượng pha chế Conductive Ink (Nồng độ $5\text{ mg/mL}$):**
    *   Bột Carbon Aerogel ($N$-CA hoặc $Fe/N$-CA): **$5.0\text{ mg}$**.
    *   Dung môi phân tán: **$950\text{ }\mu\text{L}$ DMF** (Dimethylformamide).
    *   Keo liên kết Binder chuyên biệt: **$50\text{ }\mu\text{L}$** (Tổng thể tích Ink = $1000\text{ }\mu\text{L}$).
2.  **Quy hoạch Binder chuyên biệt theo chất phân tích:**
    *   **Nhánh mẫu Cảm biến kim loại nặng $Pb^{2+}$ (SWASV):** Sử dụng Binder **Chitosan $1\%$** trong dung dịch acid acetic $1\text{ vol}\%$.
    *   **Nhánh mẫu Cảm biến dược chất Paracetamol (DPV):** Sử dụng Binder **Nafion $0.25\%$** trong cồn ethanol.
3.  **Thao tác thực hiện:**
    *   **Siêu âm phân tán mực:** Bình chứa mực được đậy kín nắp, đặt vào bể siêu âm nước đá lạnh (nhiệt độ duy trì **$< 15^\circ\text{C}$**). Siêu âm liên tục trong **$30\text{ phút}$** ở chế độ thường.
    *   **Drop-casting:** Dùng pipette vi lượng hút chính xác **$7.0\text{ }\mu\text{L}$** mực in. Nhỏ thật chậm, vuông góc trực tiếp lên trung tâm bề mặt điện cực GCE đã được dựng thẳng đứng trên giá đỡ.
    *   **Sấy khô màng mỏng (Bắt buộc):** Úp ngược một cốc thủy tinh sạch che bụi lên điện cực GCE, để màng khô tự nhiên hoàn toàn ở nhiệt độ phòng ($25^\circ\text{C}$) trong **$2 - 3\text{ giờ}$** trong tủ hút.
    > [!IMPORTANT]
    > **⚠️ Cấm sấy gia nhiệt nhanh:** Tuyệt đối không sấy gia nhiệt nhanh, không thổi khí $N_2$, không sấy chân không để tránh hiệu ứng "vành cà phê" (coffee-ring) phá hỏng cấu trúc bề mặt màng.

### GIAI ĐOẠN 2: THIẾT LẬP THÔNG SỐ CHƯƠNG TRÌNH PHÂN TÍCH ĐIỆN HÓA CẢM BIẾN

#### 1. Phép đo cảm biến Pb²⁺ bằng kỹ thuật sóng vuông hòa tan (SWASV)
*   **Điện cực làm việc (WE):** Điện cực $Fe/N$-CA / Chitosan/GCE.
*   **Dung dịch điện ly nền:** Đệm Acetate $0.1\text{ M}$, $pH = 4.5$.
*   **Bảng thông số cài đặt thiết bị đo (SWASV Parameters):**

| Thông số thiết lập | Giá trị cài đặt tiêu chuẩn |
| :--- | :---: |
| **Thế làm giàu khử ($E_{\text{dep}}$)** | **$-1.1\text{ V}$** vs. $Ag/AgCl$ |
| **Thời gian làm giàu ($t_{\text{dep}}$)** | **$120\text{ giây}$** (khuấy từ $400\text{ rpm}$) |
| **Thời gian yên lặng (Quiet time)** | **$10\text{ giây}$** (không khuấy từ) |
| **Khoảng quét thế hòa tan** | **$-1.4\text{ V}$ đến $-0.2\text{ V}$** vs. $Ag/AgCl$ |
| **Tần số sóng vuông (SW Frequency)** | **$25\text{ Hz}$** |
| **Biên độ sóng vuông (SW Amplitude)** | **$25\text{ mV}$** |
| **Bước thế (Step potential)** | **$5\text{ mV}$** |
| **Thế điện cực làm sạch (Cleaning potential)**| **$+0.2\text{ V}$** vs. $Ag/AgCl$ trong $30\text{ giây}$ ($600\text{ rpm}$) |

*   **Đỉnh hòa tan cực đại của Chì ($Pb^0 \rightarrow Pb^{2+} + 2e^-$):** Xuất hiện tại **$\approx -0.5\text{ V}$**.

#### 2. Mở rộng đo đồng thời đa ion kim loại nặng (Zn²⁺, Cd²⁺, Pb²⁺, Cu²⁺) bằng kỹ thuật SWASV
*   **Dung dịch điện ly nền:** Đệm Acetate $0.1\text{ M}$, $pH = 4.5$.
*   **Quy trình đo đồng thời (Simultaneous SWASV):**
    *   Đặt thế làm giàu khử âm sâu: **$E_{\text{dep}} = -1.30\text{ V}$ vs. $Ag/AgCl$** trong thời gian **$t_{\text{dep}} = 120 - 180\text{ giây}$** dưới lực khuấy từ $400\text{ rpm}$.
    *   Quiet time: $10\text{ giây}$.
    *   Quét sóng vuông hòa tan anode xuôi từ **$-1.40\text{ V}$ đến $+0.40\text{ V}$** vs. $Ag/AgCl$.
*   **Thế hiệu đỉnh hòa tan (Stripping Potentials) đặc trưng:**

| Ion kim loại nặng | Stripping Peak Potential (vs. $Ag/AgCl$) |
| :--- | :---: |
| **Kẽm ($Zn^{2+}$)** | **$\approx -1.10\text{ V}$** |
| **Cadmium ($Cd^{2+}$)** | **$\approx -0.80\text{ V}$** |
| **Chì ($Pb^{2+}$)** | **$\approx -0.50\text{ V}$** |
| **Đồng ($Cu^{2+}$)** | **$\approx +0.05\text{ V}$** |

#### 3. Thiết lập quy trình đo riêng lẻ Thủy ngân (Hg²⁺)
*   **Dung dịch điện ly nền:** Đệm Acetate $0.1\text{ M}$, $pH = 4.5$.
*   **Quy trình đo đơn $Hg^{2+}$:**
    *   Áp thế làm giàu khử chọn lọc: **$E_{\text{dep}} = -0.20\text{ V}$ vs. $Ag/AgCl$** trong thời gian **$120\text{ giây}$** (tránh phản ứng phụ giải phóng hydro $HER$ phá hỏng màng).
    *   Quiet time: $10\text{ giây}$.
    *   Quét thế hòa tan sóng vuông từ **$0.0\text{ V}$ đến $+0.6\text{ V}$** vs. $Ag/AgCl$. Peak hòa tan xuất hiện tại **$\approx +0.25\text{ V}$**.

#### 4. Phép đo cảm biến Paracetamol bằng kỹ thuật xung vi phân (DPV)
*   **Điện cực làm việc (WE):** Điện cực $N$-CA-700 / Nafion/GCE.
*   **Dung dịch điện ly nền:** Phosphate Buffered Saline (PBS) $0.1\text{ M}$, $pH = 7.0 - 7.4$.
*   **Bảng thông số cài đặt thiết bị đo (DPV Parameters):**

| Thông số thiết lập | Giá trị cài đặt tiêu chuẩn |
| :--- | :---: |
| **Thế làm giàu khử ($E_{\text{dep}}$)** | **Không áp dụng (Không cần làm giàu)** |
| **Khoảng thế quét** | **$0.0\text{ V}$ đến $+0.8\text{ V}$** vs. $Ag/AgCl$ |
| **Tốc độ quét thế (Scan rate)** | **$20\text{ mV/s}$** |
| **Biên độ xung (Pulse Amplitude)** | **$50\text{ mV}$** |
| **Độ rộng xung (Pulse Width)** | **$50\text{ ms}$** |
| **Bước thế (Step potential)** | **$5\text{ mV}$** |

*   **Peak oxy hóa Paracetamol:** Xuất hiện rõ nét tại **$\approx +0.34\text{ V}$** vs. $Ag/AgCl$.

---

### GIAI ĐOẠN 3: ĐO ĐẠC ĐẶC TÍNH ĐỐI CHỨNG ĐỒNG DẠNG NÂNG CAO (ORR & Siêu Tụ Điện)

#### 1. Phép đo Xúc tác khử Oxy (ORR) làm "Proof of Concept" chứng minh tâm Fe-N₄
*   **WE sử dụng:** Điện cực $Fe/N$-CA / Chitosan/GCE.
*   **Điện ly nền:** Dung dịch **$KOH$ $0.1\text{ M}$**.
*   **Quy trình đo đạc:**
  1.  Sục khí Nitơ ($N_2$) tinh khiết liên tục trong $30\text{ phút}$ vào bình điện giải. Quét CV từ **$-1.0\text{ V}$ đến $+0.2\text{ V}$ vs. $Ag/AgCl$** ở tốc độ quét $50\text{ mV/s}$ để thu được dòng điện dung nền.
  2.  Chuyển sang sục liên tục khí Oxy ($O_2$) trong $30\text{ phút}$ để bão hòa. Chạy quét thế CV tương tự. Đường phổ CV bắt buộc phải xuất hiện một peak khử oxy cực kỳ sắc nét ở thế dương hơn **$-0.2\text{ V}$ vs. $Ag/AgCl$** với cường độ dòng đỉnh khử đạt **$I_c \ge 1.0\text{ mA/cm}^2$**.
  3.  Đo linear sweep voltammetry (LSV) trên điện cực quay RDE ở các tốc độ quay từ $400\text{ rpm}$ đến $3600\text{ rpm}$ để tính toán số electron chuyển tải ($n \approx 3.14 - 3.69$ tiệm cận cơ chế 4 electron).

#### 2. Phép đo Siêu tụ điện hóa (Supercapacitor) của mẫu đối chứng NaOH-Urea
*   **WE sử dụng:** Mẫu carbon $NaOH$-Urea ép viên drop-cast.
*   **Điện ly nền:** Dung dịch **$KOH$ $6.0\text{ M}$** siêu đậm đặc.
*   **Quy trình đo đạc:**
  1.  Chạy CV trong $KOH$ $6.0\text{ M}$ ở các tốc độ quét từ $5 - 100\text{ mV/s}$ trong khoảng thế tĩnh từ $-1.0\text{ V} \rightarrow 0.0\text{ V}$ vs. $Ag/AgCl$. Đường CV phải có dạng **hình hộp chữ nhật đối xứng chuẩn** đại diện cho điện dung lớp kép lý tưởng.
  2.  Đo phóng nạp dòng hằng GCD ở các mật độ dòng từ $0.5 - 10\text{ A/g}$. Đường phóng nạp GCD phải có dạng tam giác cân đối xứng, xác định điện dung riêng cụ thể ($C_s\text{ F/g}$) để viết phần biện luận đối chứng cho luận văn.

---

## PHẦN IV: THÔNG SỐ ĐẶC TRƯNG KỸ THUẬT VẬT LIỆU ĐẠT CHUẨN (Material Spec Sheet)

Toàn bộ các chỉ số vật lý, hóa học, tinh thể đạt chuẩn (Pass Criteria) đối với bột Carbon Aerogel sau khi chế tạo được quy hoạch trực quan trong bảng dưới đây:

| Kỹ thuật phân tích | Chỉ số đặc trưng | Giá trị tiêu chuẩn đạt chuẩn (Pass Criteria) | Trạng thái (Fail Criteria) |
| :--- | :--- | :--- | :--- |
| **SEM** | Cấu trúc hình thái không gian | Mạng lưới tổ ong 3D phân cấp liên thông, đường kính macropores **$10 - 100\text{ }\mu\text{m}$**, thành vách phẳng mỏng mịn. | Thành vách vỡ vụn, sợi co cụm đặc khít, sập cấu trúc mao quản (mẫu đối chứng $NaOH$). |
| **TEM / HR-TEM** | Phân tán pha Sắt ($Fe$) | **Tuyệt đối không** xuất hiện hạt cụm sắt kim loại hoặc sắt carbide ($Fe_3C$) tinh thể lớn (kích thước $> 5\text{ nm}$). $Fe$ tồn tại dưới dạng các chấm sáng đơn phân tán cực nhỏ **$< 1\text{ nm}$**. | Xuất hiện các chấm đen đục kích thước lớn 10–50 nm (quá trình rửa axit chưa sạch sắt tạp). |
| **BET** | Dạng đẳng nhiệt hấp phụ | **Loại IV (Type IV Isotherm)** theo IUPAC, xuất hiện vòng lặp trễ (hysteresis loop) dạng H3 hoặc H4 ở $P/P_0 = 0.4 - 0.9$. | Không xuất hiện vòng lặp trễ, đường hấp phụ dạng dẹt (sụp đổ mesopores). |
| **BET** | Diện tích bề mặt riêng | **$S_{BET} \ge 3700\text{ m}^2/\text{g}$** | $S_{BET} < 1000\text{ m}^2/\text{g}$ (tụt sâu về $150\text{ m}^2/\text{g}$ đối với mẫu đối chứng $NaOH$). |
| **BET** | Thể tích lỗ xốp | **$V_{pore} \ge 4.0\text{ cm}^3/\text{g}$** | $V_{pore} < 1.0\text{ cm}^3/\text{g}$. |
| **BET** | Đường kính lỗ xốp TB | Phân bố tập trung trong dải **$2.0 - 50.0\text{ nm}$** (mesopores). | Đường kính thô $> 100\text{ nm}$ (sụp đổ hệ xốp nhỏ). |
| **Raman** | Tỷ số defect carbon | Tỷ lệ cường độ đỉnh **$I_D / I_G = 0.9 - 1.2$** | $I_D / I_G < 0.6$ hoặc $> 1.5$. |
| **XRD** | Tinh thể carbon | Hai đỉnh nhiễu xạ góc tù, rộng tại **$2\theta \approx 26.4^\circ$** (002) và **$43.5^\circ$** (100) đại diện carbon bán tinh thể. | Xuất hiện các đỉnh nhiễu xạ sắc nhọn của $\alpha-Fe$ ($44.7^\circ$) hoặc $Fe_3C$ ($43.9^\circ$) (Rửa axit thất bại). |
| **XPS Survey** | Hàm lượng nguyên tố bề mặt | Nitơ tổng đạt **$3.0 - 6.0\text{ at}\%$**<br>Sắt tổng đạt **$0.4 - 1.5\text{ at}\%$** | Nitơ $< 2.0\text{ at}\%$ (thiếu active sites) hoặc Sắt $> 2.0\text{ at}\%$ (thiếu phối trí). |
| **XPS Survey** | Tỉ lệ nguyên tố phối trí | Tỷ lệ nguyên tử **$N : Fe \ge 4 : 1$** | Tỷ lệ $N : Fe < 3 : 1$. |
| **XPS N 1s** | Liên kết Nitơ phân giải cao | Đỉnh **Pyridinic-N** tại thế liên kết **$\approx 398.2\text{ eV}$** chiếm tỷ lệ diện tích ưu thế tối thiểu **$\ge 45\%$** tổng phổ N 1s. | Pyridinic-N chiếm $< 25\%$ diện tích tách phổ. |
| **XPS Fe 2p** | Liên kết Sắt phân giải cao | Đỉnh đặc trưng liên kết **$Fe-N_x$** xuất hiện rõ nét trong khoảng thế liên kết **$710.8\text{ eV} - 711.5\text{ eV}$**. | Không có peak $Fe-N_x$, xuất hiện peak $Fe$ kim loại tự do ($707.0\text{ eV}$). |

---

## PHẦN V: KIẾN NGHỊ VÀ DANH MỤC THAM CHIẾU HỆ THỐNG

### 1. Kiến nghị Cải tiến Hóa học Thực nghiệm
*   **Chuyển đổi trục dung môi:** Kiến nghị chuyển hẳn sang hệ $NH_4OH$-Urea làm trục chính chế tạo màng cảm biến điện hóa. Hệ dung môi kiềm cũ $NaOH$-Urea chỉ được duy trì làm mẫu đối chứng đo siêu tụ điện.
*   **Bắt buộc Acid Leaching đun hồi lưu:** Đối với điện cực phân tích nhạy dải vết ($Pb^{2+}$), bắt buộc phải thực hiện bước leaching đun hồi lưu bằng $HCl$ $0.5\text{ M}$ ở $80^\circ\text{C}$ trong $8\text{ giờ}$ và nung annealing lần 2 ở $800^\circ\text{C}$ trong $1\text{ giờ}$ để triệt tiêu hoàn toàn pha sắt tự do và oxit sắt thô, đảm bảo cấu trúc đơn nguyên tử $Fe-N_4$ tinh khiết.
*   **Hoạt hóa điện cực nền GCE:** Bắt buộc áp dụng bước anodize hóa học trong dung dịch $NaOH$ $0.1\text{ M}$ ở thế $+1.8\text{ V}$ vs. $Ag/AgCl$ trong $10\text{ giây}$ để hòa tan sạch cặn alumina lưỡng tính bám dính cơ học, giải phóng hoàn toàn các khe nano hoạt tính của GCE.

### 2. Danh mục File Tham chiếu Hệ thống
*   Tài liệu `TOM_TAT_NTXPhuong.md` trong thư mục `08_Review_va_Tong_quan`.
*   Tài liệu `2 Nitrogen-Doped Carbon Aerogels Prepared by Direct Pyrolysis of.md` trong thư mục `02_Doping_va_Gel_hoa`.
*   Tài liệu `1 Facile Synthesis of Fe-Doped Algae Residue-Derived Carbon Aerogels for.md` trong thư mục `02_Doping_va_Gel_hoa`.
