# Final_SOPs_CA.md — Hướng Dẫn Thực Nghiệm & Hệ Thống Đối Chứng Khoa Học Chế Tạo Carbon Aerogel Điện Hóa

> [!NOTE]
> * **Tài liệu tham chiếu chuẩn cốt lõi:**
>   1. Luận án Tiến sĩ [Nguyễn Trần Xuân Phương 2024](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20Ref%20materials/08_Review_va_Tong_quan/TOM_TAT_NTXPhuong.md) (Xác lập quy trình delignification xơ dừa Bến Tre và đối chứng hệ NaOH-Urea).
>   2. Công trình [Fauziyah et al. 2020 (Ind. Eng. Chem. Res.)](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20Ref%20materials/02_Doping_va_Gel_hoa/2%20Nitrogen-Doped%20Carbon%20Aerogels%20Prepared%20by%20Direct%20Pyrolysis%20of.md) (Xác lập hệ dung môi NH₄OH-Urea chuyển pha Cellulose III, dẫn điện 5.08 S/cm).
>   3. Công trình [Wu et al. 2024 (Sensors)](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20Ref%20materials/02_Doping_va_Gel_hoa/1%20Facile%20Synthesis%20of%20Fe-Doped%20Algae%20Residue-Derived%20Carbon%20Aerogels%20for.md) (Xác lập hệ tẩm Fe, graphit hóa nhiệt độ cao và chế tạo màng cảm biến GCE siêu nhạy đạt LOD 0.0033 µM).

---

## PHẦN I: KHUNG LÝ THUYẾT ĐỐI CHỨNG VÀ HỆ THỐNG KẾ THỪA ĐỊNH LƯỢNG

Đề tài nghiên cứu hướng tới việc tận dụng nguồn sinh khối phụ phẩm nông nghiệp có sẵn tại Việt Nam (xơ dừa Bến Tre) để tách chiết cellulose tinh khiết, sau đó chế tạo vật liệu **Carbon Aerogel** phân cấp lỗ xốp tổ ong bằng phương pháp sol-gel thân thiện môi trường. Vật liệu này được biến tính đồng thời bằng liên kết coordinated đơn nguyên tử Sắt/Nitơ (**Fe/N-CA**) nhằm định hình các tâm xúc tác hoạt tính cao ứng dụng trực tiếp biến tính điện cực làm việc carbon thủy tinh (GCE) cho hai phép phân tích điện hóa:
1. **Cảm biến sóng vuông hòa tan (SWASV) đo kim loại nặng Pb²⁺** (sử dụng keo liên kết Chitosan 1% tích điện dương).
2. **Cảm biến xung vi phân (DPV) đo dược chất Paracetamol** (sử dụng keo dẫn cation kị nước Nafion 0.25%).
3. **Phép đo xúc tác khử Oxy (ORR)** trong dung dịch kiềm 0.1M KOH được thực hiện song song làm mô hình **"Proof of Concept"** vững chắc nhằm gián tiếp xác nhận sự tồn tại của cấu trúc đơn nguyên tử $Fe-N_4$.
4. **Mẫu đối chứng Carbon NaOH-Urea** được ứng dụng đo GCD kiểm chứng đặc tính **siêu tụ điện (Supercapacitor)** trong KOH 6.0M nhờ hiệu ứng Na-etching tạo mao quản.

### Sơ đồ tư duy tiến trình thực nghiệm tổng thể:
```
[Xơ dừa Bến Tre] ──(NaOH 6% 80°C/4h)──> DCF ──(H2O2 10% 60°C/2h)──> Bleached Fiber ──(HCl 2.0M 60°C/2h)──> BCF (Cellulose I)
                                                                                                            │
                      ┌─────────────────────────────────────────────────────────────────────────────────────┘
                      ├─ HỆ CHÍNH (Sensing/ORR): [NH₄OH-Urea] + Siêu âm lạnh <10°C ──> Sol Cellulose III ──> Gel hóa nhiệt (80°C)
                      └─ HỆ ĐỐI CHỨNG (Supercap): [NaOH-Urea] + Đông sâu -10°C      ──> Sol Cellulose II  ──> Gel hóa nhiệt (55°C)
                                                                                                            │
  ┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ├─ Solvent Exchange: Ngâm Ethanol 98% lạnh (0-5°C/24h) để khóa giữ Urea (nguồn N-doping). Ngâm rửa nước cất DI 2 lần.
  ├─ Nhánh mẫu co-doped Fe: Ngâm dung dịch FeCl3·6H2O + Urea (24h) khuếch tán tĩnh tạo liên kết Fe3+ với các nhóm chức.
  ├─ Sấy thăng hoa: Cấp đông nhanh -80°C ──> Sấy chân không <20 Pa / -50°C trong 48h (Độ co ngót thể tích <12%).
  ├─ Nhiệt phân 1: Nung lò ống N2, 3 Ramp nhiệt (Gia nhiệt 5°C/min) lên 700°C (N-CA) hoặc 800°C (Fe/N-CA) giữ 2h.
  ├─ Rửa axit & Annealing 2: Đun hồi lưu HCl 0.5M ở 80°C/8h (loại sạch Fe tự do) ──> Nung re-anneal 800°C/1h trong N2.
  └─ Chế tạo Ink GCE: Trộn DMF + 5% Binder (Chitosan cho Pb2+; Nafion cho Paracetamol) ──> Drop-cast 7.0 µL ──> Khô tự nhiên.
```

---

## PHẦN II: PHÂN TÍCH ĐỐI CHỨNG VÀ KẾ THỪA CHI TIẾT THEO TỪNG BƯỚC THỰC NGHIỆM

---

### GIAI ĐOẠN 0: TIỀN XỬ LÝ TÁCH CHIẾT CELLULOSE TINH KHIẾT (Raw Material Pretreatment)

#### 1. Thao tác thực nghiệm chuẩn
*   **Kiềm hóa DCF:** Ngâm 50g bột xơ dừa khô ($<125\text{ }\mu\text{m}$) trong 1000 mL nước nóng (80°C) khuấy từ 4 giờ để rửa sơ bộ. Tiếp tục cho bã lọc vào 1000 mL dung dịch **NaOH 6 wt%**, đun ở **80 ± 2°C trong 4 giờ** liên tục (khuấy 600 rpm). Lọc qua phễu Buchner, rửa bằng nước DI nóng đến pH trung tính. Sấy bột ở 80°C trong 8 giờ.
*   **Tẩy trắng Bleached coir fiber:** Cho 30g bột kiềm hóa DCF vào 600 mL dung dịch **H₂O₂ 10 wt%** được kiềm hóa nhẹ bằng NaOH đến pH $\approx 11$. Khuấy đun cách thủy ở **60°C trong 2 giờ** (300 rpm). Lọc rửa nước cất DI đến pH trung tính.
*   **Thủy phân acid thu BCF:** Cho sợi tẩy trắng vào 600 mL dung dịch **HCl 2.0M** đun hồi lưu ở **60°C trong 2 giờ** (400 rpm) để thủy phân hemicellulose vô định hình. Lọc, rửa DI đến pH trung tính, sấy ở 80°C trong 12 giờ. Rây mịn thu bột Bleached Coir Fiber (BCF).

#### 2. Tính chất kế thừa từ tài liệu gốc
Kế thừa hoàn toàn từ **Luận án Tiến sĩ Nguyễn Trần Xuân Phương 2024 (Trang 6, Chương 2.1 & Trang 11, Chương 3.1)** về mặt xử lý kiềm hóa bằng dung dịch NaOH 6 wt% và tẩy trắng bằng dung dịch H₂O₂ 10 wt% để loại bỏ lignin, hemicellulose khỏi xơ dừa Bến Tre Việt Nam.

#### 3. Tỷ lệ kế thừa (%) & Biện luận cơ chế khoa học
*   **Kiềm hóa NaOH 6%:** Kế thừa **100% về mặt thao tác hóa học**. Cơ chế lý hóa: Các ion $OH^-$ tấn công cắt đứt liên kết alkyl-aryl ether giữa các mắt xích phenylpropane trong cấu trúc polyme lignin phức tạp vô định hình. Quá trình này hòa tan lignin thô thành dạng muối sodium-lignin màu đen dễ dàng trôi theo dung dịch rửa, giải phóng các chuỗi xenluloza tinh thể bên trong.
*   **Tẩy trắng H₂O₂ 10%:** Kế thừa **100% về mặt lý thuyết**. Cơ chế lý hóa: Trong môi trường kiềm pH 11, hydro peroxide phân ly giải phóng ion hydroperoxide cực kỳ linh động ($H_2O_2 + OH^- \rightarrow HOO^- + H_2O$). Các ion $HOO^-$ này là tác nhân nucleophile cực mạnh bẻ gãy các nhóm mang màu carbonyl và liên kết đôi nối đôi carbon-carbon không liên hợp còn sót lại của lignin vô định hình, giúp làm sạch triệt để và tẩy màu sợi từ nâu sẫm sang trắng kem.
*   **Thủy phân acid HCl 2.0M:** Kế thừa **80% cải tiến**. Cơ chế lý hóa: Dung dịch axit HCl loãng chọn lọc thủy phân liên kết glycosidic vô định hình dễ đứt gãy của hemicellulose, trong khi các chùm sợi xenluloza có độ sắp xếp chặt chẽ cao nhờ liên kết hydro liên phân tử được bảo toàn nguyên vẹn, thu được bột BCF có cấu trúc sợi ngắn phẳng mịn và độ sạch cực cao.

#### 4. Chỉ số vật liệu đặc trưng đạt được (Pass/Fail Criteria)
*   **Khối lượng hao hụt DCF (Gravimetric Weight-loss %):** Phải đạt **30% – 38%** (Đạt chuẩn loại lignin). Nếu hao hụt $<30\%$, lignin vẫn còn bám dính nhiều gây cản trước sol-gel hóa; nếu $>45\%$, mạch cellulose đã bị phân hủy quá mức.
*   **Đường kính sợi (SEM):** Co rút sắc nét từ dải 80–100 µm (RCF) còn **10–20 µm (BCF)**, bề mặt sần sùi có nhiều vết rạch sọc làm tăng diện tích tiếp xúc.
*   **Độ tinh thể hóa (XRD):** Tinh thể xenluloza tự nhiên Cellulose I tăng rõ rệt từ **46.97%** (RCF ban đầu) lên **55.23%** (DCF) và cực đại đạt **57.15% (BCF)**. Xuất hiện các đỉnh nhiễu xạ sắc nhọn đặc trưng của Cellulose I tại góc góc quét $2\theta \approx 16.08^\circ$ (110) và $22.23^\circ$ (200).
*   **Độ sạch Xenluloza:** Hàm lượng cellulose trong bột BCF khô phải đạt **$\ge 92\text{ wt}\%$** (kiểm định qua phổ FT-IR không còn đỉnh este của nhóm acetyl hemicellulose tại 1735 cm⁻¹).

---

### GIAI ĐOẠN 1: TỔNG HỢP HỆ SOL CELLULOSE & ĐỐI CHỨNG DUNG MÔI ĐIỆN HÓA (Sol Preparation)

#### 1. Thao tác thực nghiệm chuẩn
*   **Hệ dung môi chính Ammonia-Urea (Chế tạo màng Cảm biến/ORR):** Định lượng chuẩn: **1.0g Cellulose BCF + 11.0 mL NH₄OH đậm đặc (25% w/w) + 4.0g Urea tinh thể rắn + 5.0 mL nước cất DI** (Tổng thể tích dung môi = 16.0 mL). Hòa tan hoàn toàn urea trong bình Teflon đậy kín miệng để nhốt hơi NH₃. Thêm 1.0g BCF. Đặt bình vào bể siêu âm đầy đá nước lạnh duy trì **≤ 10°C (tối ưu 0–5°C)**. Siêu âm xung (**2 giây ON / 1 giây OFF**) trong **30 phút** ở công suất trung bình. Thu được hệ sol màu hơi đục nhẹ, hoàn toàn đồng nhất.
*   **Hệ dung môi đối chứng NaOH-Urea (Chế tạo siêu tụ điện):** Định lượng tỷ lệ khối lượng chuẩn **7 wt% NaOH : 12 wt% Urea : 81 wt% H₂O**. Hòa tan kiềm/urea trong nước, làm lạnh dung dịch về **-10°C đến -12°C** trong tủ đông sâu đến trạng thái bán đóng băng (slushy state). Cho nhanh 1.0g BCF vào dung môi lạnh, khuấy từ tốc độ cao 3000 rpm trong **5 phút** ở nhiệt độ phòng để hòa tan nhanh. Thu được hệ sol trong suốt.

#### 2. Tính chất kế thừa từ tài liệu gốc
*   Hệ chính Ammonia-Urea kế thừa toàn diện từ nghiên cứu của **Fauziyah et al. 2020 (Trang 1, Abstract & Trang 2, Experimental Section)**.
*   Hệ đối chứng NaOH-Urea kế thừa từ luận án **Nguyễn Trần Xuân Phương 2024 (Trang 8, Chương 2.2.2)** và nghiên cứu kinh điển của **Cai & Zhang 2006 (Biomacromolecules)**.

#### 3. Tỷ lệ kế thừa (%) & Biện luận cơ chế khoa học
*   **Hệ Ammonia-Urea:** Kế thừa **100% công thức định lượng hóa học**. 
    *   *Cơ chế lý hóa chuyển pha Cellulose III:* Siêu âm lạnh ($<10^\circ$C) cưỡng bức các phân tử amoniac nhỏ gọn thâm nhập sâu vào các vùng tinh thể chặt chẽ của Cellulose I, tạo ra phức ammonia-cellulose liên kết yếu. Khi thêm cồn lạnh đông tụ, amoniac bị kéo ra ngoài giải phóng chuỗi xenluloza tự sắp xếp lại thành pha tinh thể **Cellulose III**.
    *   *Cơ chế tạo mesh xốp siêu vi tổ ong:* Khi nhiệt phân carbon hóa Cellulose III, amoniac tự do bám sâu trong mạng lưới bị giải phóng dưới dạng luồng khí áp suất cao (self-exfoliation), bóc tách các lá carbon thành cấu trúc siêu mỏng, tạo ra diện tích bề mặt riêng khổng lồ **3,733 m²/g** và độ dẫn điện cực cao **5.08 S/cm** (Fauziyah et al. 2020).
*   **Hệ NaOH-Urea:** Kế thừa **100% lý thuyết sol-gel**. 
    *   *Cơ chế lý hóa chuyển pha Cellulose II:* Nhiệt độ cực lạnh (-12°C) cho phép các ion $Na^+$ ngậm nước và phân tử urea ngập tràn bao bọc chuỗi xenluloza qua liên kết hydro tạo phức hòa tan đồng nhất. Khi đông tụ bằng cồn, phức rã ra và xenluloza tái kết tinh thành pha **Cellulose II**.
    *   *Biện luận cơ chế sập vách (NaOH collapse) đối chứng:* Trong quá trình carbon hóa Cellulose II, các cation kiềm không bay hơi $Na^+$ đóng vai trò chất ăn mòn hóa học (Na-etching) cực mạnh ở nhiệt độ cao. Tác nhân kiềm này đục khoét, phá hủy hoàn toàn vách tế bào lỗ xốp và làm **sụp đổ mạng mao quản tổ ong**, dẫn đến diện tích bề mặt co rút thảm hại chỉ còn **150 m²/g** và conductivity rơi sâu về **0.93 S/cm**. Tuy nhiên, chính cơ chế Na-etching đục khoét này lại rất thích hợp tạo các khuyết tật mao quản thô chứa chất điện ly kiềm KOH 6.0M đậm đặc trong ứng dụng **siêu tụ điện (Supercapacitor)**.

#### 4. Chỉ số vật liệu đạt được (Pass/Fail Criteria)
*   **Trạng thái Sol:** Đạt chuẩn khi dung dịch đồng nhất, không còn xơ sợi chưa tan bám ở đáy cốc.
*   **Nhiệt độ bể siêu âm hệ NH₄OH:** Phải được khống chế nghiêm ngặt **$\le 10^\circ$C** trong suốt 30 phút. Nếu nhiệt độ tăng $>15^\circ$C, NH₃ bay hơi đột ngột gây Fail vì sol bị mất hoạt tính hòa tan và không thể chuyển pha sang Cellulose III.
*   **Đỉnh tinh thể Cellulose III (XRD):** Giản đồ XRD của hydrogel sau đông tụ phải xuất hiện hai đỉnh đặc trưng rõ nét tại góc $2\theta \approx 11.6^\circ$ (110) và $20.5^\circ$ (002) đại diện cho Cellulose III sạch. Đỉnh Cellulose I gốc ($22.23^\circ$) và Cellulose II ($12.73^\circ$) phải biến mất hoàn toàn.

---

### GIAI ĐOẠN 2: ĐÚC KHUÔN PP & GIÀ HÓA NHIỆT HÌNH THÀNH HYDROGEL (Casting & Gelation)

#### 1. Thao tác thực nghiệm chuẩn
1.  **Đúc khuôn và De-gassing:** Rót từ từ dung dịch sol lạnh vào các ống tiêm Polypropylene (PP) đã cắt bỏ đầu kim để làm khuôn đúc monolith. Đặt đứng ống tiêm PP trong ngăn mát tủ lạnh ở **0–5°C trong thời gian 30–60 phút** để ổn định động học hệ sol và đuổi sạch bọt khí.
2.  **Già hóa tạo gel (Thermal Gelation):** Bọc kín hai đầu ống tiêm.
    *   *Đối với hệ NH₄OH-Urea:* Đặt tĩnh ống tiêm trong tủ sấy già hóa duy trì nhiệt độ ổn định **80°C trong 2 giờ** để sol đông đặc hoàn toàn thành hydrogel dẻo dai màu nâu nhạt.
    *   *Đối với hệ NaOH-Urea:* Đặt đứng ống tiêm vào bể nước ổn nhiệt duy trì ở **50–55°C trong 1.5 giờ** để kích hoạt gel hóa nhiệt. Dùng pít-tông nhẹ nhàng đẩy khối hydrogel ra ngoài.

#### 2. Tính chất kế thừa từ tài liệu gốc
Kế thừa sâu sắc từ nghiên cứu động học gel hóa nhiệt của **Cai & Zhang 2006 (Unique Gelation Behavior of Cellulose in NaOH Urea Aqueous Solution)** về mặt nhiệt động học rã vỏ hydrat.

#### 3. Tỷ lệ kế thừa (%) & Biện luận cơ chế khoa học
*   **Lựa chọn khuôn tiêm PP:** Kế thừa **100% kinh nghiệm thực nghiệm**. Biện luận cơ chế: Khung khuôn làm bằng nhựa Polypropylene (PP) có đặc tính kỵ nước mạnh và năng lượng bề mặt cực thấp, hoàn toàn không hình thành liên kết hydro vật lý với các nhóm hydroxyl tự do nằm ở thành ngoài của sol xenluloza. Điều này triệt tiêu hoàn toàn lực ma sát bám dính, giúp pít-tông đẩy hydrogel 3D ra khay một cách trơn tru, không gây nứt vỡ cơ học ở tâm hay mẻ đầu monolith như khuôn thủy tinh.
*   **Thời gian de-gassing ở 0-5°C:** Kế thừa **100% động học sol**. Theo Cai & Zhang, sol cellulose/urea có tính ổn định động học cực đại ở nhiệt độ lạnh 0-5°C, với thời gian gel hóa tự phát kéo dài $>191$ giờ. Khoảng thời gian để yên 30-60 phút ở vùng lạnh này là **vàng** để: (1) Toàn bộ các bóng khí nano sinh ra trong quá trình siêu âm khuấy động tự động thoát ly lên bề mặt mà không sợ hệ sol bị gel hóa sớm gây khuyết tật rỗng lỗ trong gel. (2) Đạt trạng thái cân bằng nhiệt lạnh đồng đều, chuẩn bị cho mầm tinh thể đông đá đồng trục đối xứng.
*   **Gel hóa già hóa nhiệt ở 50-80°C:** Kế thừa **100% cơ chế nhiệt động học**. Nhiệt độ cao cung cấp nhiệt lượng phá vỡ các hydration shells (vỏ bọc liên kết hydro ngậm nước dung môi) xung quanh chuỗi xenluloza. Các chuỗi bị mất vỏ bọc dung môi sẽ tự do xích lại gần nhau, hình thành các liên kết hydro liên phân tử chéo cực kỳ dày đặc và biến đổi thành mạng lưới hydrogel 3D không thể hòa tan.

#### 4. Chỉ số vật liệu đặc trưng đạt được (Pass/Fail Criteria)
*   **Hình thái Hydrogel:** Khối hydrogel monolith đẩy ra từ ống tiêm PP phải đạt hình trụ đứng nhẵn bóng, dẻo dai, có độ đàn hồi tốt (ấn nhẹ có thể trở lại hình dạng cũ), hoàn toàn không bị nứt vỡ, móp méo hay rỗng ruột bọt khí.
*   **Độ ẩm cấu trúc:** Hydrogel ẩm đều, giữ form 3D ổn định khi đặt đứng trên khay kính phẳng.

---

### GIAI ĐOẠN 3: KEO TỤ, TẨM ĐỐP Fe & KHÓA GIỮ UREA CÓ KIỂM SOÁT (Coagulation & Fe Impregnation)

#### 1. Thao tác thực nghiệm chuẩn
1.  **Keo tụ tái cấu trúc (Solvent Exchange):** Đổ cồn **Ethanol 98% lạnh duy trì ở 0–5°C** vào bình ngâm chứa các khối hydrogel ẩm (tỷ lệ thể tích tối thiểu **15 mL ethanol / 1 g cellulose** ban đầu). Đậy kín nắp và ngâm tĩnh trong tủ mát 4°C trong **24 giờ** để keo tụ. Gạn bỏ cồn cũ, rửa lại bằng cách ngâm nước cất DI sạch (gấp 5 lần thể tích gel) trong **2 giờ**, lặp lại **chính xác 2 lần** để rửa amoniac tự do dư thừa. 
    > [!IMPORTANT]
    > **⚠️ Cảnh báo cực đoan:** Tuyệt đối không rửa nước cất quá 4 lần hoặc ngâm rửa kéo dài $>12$ giờ. Việc rửa quá mức sẽ hòa tan trôi tuột hoàn toàn lượng phân tử Urea tự do bị kẹt cơ học trong mạng gel — đây chính là nguồn Nitơ (N-doping) duy nhất để tạo ra cấu trúc pyridinic-N hoạt tính khi nung!
2.  **Tẩm Sắt (Dành cho nhánh mẫu Fe/N-CA):** Hòa tan hoàn toàn **0.484g FeCl₃·6H₂O** tinh thể rắn và 1.0g Urea vào 30 mL nước cất DI lạnh (0-5°C) để chế tạo dung dịch tẩm (đạt mức tẩm sắt tối ưu 10 wt% Fe). Thả khối gel đã keo tụ vào dung dịch tẩm sắt. Đặt chậu ngâm vào bể siêu âm nước đá siêu âm nhẹ trong 30 phút, sau đó ngâm tĩnh trong tủ mát 4°C trong **24 giờ** liên tục để ion $Fe^{3+}$ khuếch tán bão hòa đều toàn lõi gel.

#### 2. Tính chất kế thừa từ tài liệu gốc
*   Keo tụ bằng cồn lạnh bảo toàn urea kế thừa từ nguyên lý thiết kế của **Fauziyah et al. 2020 (Trang 2, Experimental Section)**.
*   Tỷ lệ tẩm sắt FeCl3 kết hợp Urea kế thừa và cải tiến từ công thức đơn nguyên tử của **Wu et al. 2024 (Trang 3, Section 2.2)**.

#### 3. Tỷ lệ kế thừa (%) & Biện luận cơ chế khoa học
*   **Ngâm cồn Ethanol lạnh (0-5°C):** Kế thừa **100% động học khuếch tán**. Cơ chế lý hóa: Duy trì nhiệt độ cồn lạnh làm giảm hệ số khuếch tán tự do $D$ của các phân tử nhỏ amoniac và urea ra ngoài bể cồn khoảng 2.5 lần ($D \approx 0.8 \times 10^{-9}\text{ m}^2/\text{s}$). Điều này đóng vai trò quyết định giữ chân lượng Urea phân tử nhỏ làm tiền chất N-doping bền vững bám dính trong thành vách hydrogel, đảm bảo hàm lượng Nitơ thực tế sau nung đạt dải vàng **3.0 – 6.0 at%**.
*   **Siêu âm và ngâm tẩm Fe³⁺ kéo dài 24 giờ:** Kế thừa **100% động học chuyển khối**. Cơ chế lý hóa: Quá trình khuếch tán của các ion $Fe^{3+}$ phân cực từ dung dịch lỏng ngoài vào sâu trong lõi trung tâm của khối monolith xốp bị giới hạn bởi lực cản mao quản (Intraparticle Diffusion Limit). Siêu âm 30 phút đầu giúp mở rộng các mao quản hẹp, ngâm tĩnh kéo dài 24 giờ ở nhiệt độ phòng ổn định đảm bảo nồng độ ion đạt trạng thái bão hòa đồng nhất trên toàn bộ thể tích lõi monolith. Điều này ngăn chặn triệt để hiện tượng nghèo hoạt chất ở lõi và sự tập tụ thô của hạt sắt kim loại ngoài bề mặt khi nung.

#### 4. Chỉ số vật liệu đặc trưng đạt được (Pass/Fail Criteria)
*   **Màu sắc hydrogel sau tẩm:** Khối hydrogel N-CA ẩm có màu trắng đục nhẹ đồng đều. Khối hydrogel Fe/N-CA ẩm phải chuyển hẳn sang **màu nâu đỏ/vàng cam đồng đều** từ lớp vỏ ngoài cho đến tận tâm lõi khối gel (kiểm tra bằng cách cắt thử một mẫu nhỏ). 
*   **Trạng thái gel sau tẩm:** Không bị nứt vỡ cơ học hay bị mềm nhũn do tan rã.

---

### GIAI ĐOẠN 4: SẤY THĂNG HOA BẢO TOÀN CẤU TRÚC MAO QUẢN (Freeze Drying)

#### 1. Thao tác thực nghiệm chuẩn
1.  **Cấp đông sâu siêu tốc:** Đặt các khối gel ẩm sau tẩm vào tủ đông siêu sâu duy trì ở nhiệt độ **-80°C** (tốc độ hạ nhiệt nhanh cực đoan $-7.5\text{ K/phút}$) hoặc nhúng trực tiếp khối gel vào bình chứa Nitơ lỏng ($LN_2$, -196°C) trong **5 phút** để đóng băng toàn bộ lượng nước mao quản tự do.
2.  **Sấy thăng hoa chân không:** Khởi động máy sấy thăng hoa trước đảm bảo nhiệt độ bẫy lạnh đạt **≤ -50°C** (tối ưu -80°C) và áp suất chân không hạ sâu **< 20 Pa (0.15 Torr)**. Xếp các mẫu gel đông băng vào buồng sấy. Duy trì sấy thăng hoa liên tục trong **36–48 giờ** cho đến khi dung môi thăng hoa sạch hoàn toàn và khối lượng mẫu đạt trạng thái hằng định.
3.  **Thu hồi và đo đạc:** Thu được aerogel xốp dẻo siêu nhẹ màu trắng/vàng nhạt (N-CA) hoặc màu nâu đỏ nhạt (Fe/N-CA). Dùng thước kẹp caliper đo kích thước 3 chiều để xác định độ co ngót tuyến tính.

#### 2. Tính chất kế thừa từ tài liệu gốc
Kế thừa hoàn toàn tiêu chuẩn sấy thăng hoa chân không của **Luận án Tiến sĩ Nguyễn Trần Xuân Phương 2024 (Trang 7, Hình 2.1 & Trang 8, Hình 2.2)** và **Fauziyah et al. 2020 (Trang 2, Experimental Section)**.

#### 3. Tỷ lệ kế thừa (%) & Biện luận cơ chế khoa học
*   **Cấp đông siêu tốc (-80°C hoặc Nitơ lỏng):** Kế thừa **100% vật lý chất rắn**. Cơ chế lý hóa: Tốc độ hạ nhiệt siêu nhanh ($>7.5\text{ K/phút}$) cưỡng bức nước tự do trong mao quản đóng băng đồng loạt tại chỗ, ngăn chặn hoàn toàn hiện tượng di trú ion $Fe^{3+}$ và sự lớn lên của các tinh thể đá thô. Kết quả là tạo ra các mầm tinh thể đá đông băng siêu nhỏ đồng đều, đóng vai trò làm chất tạo khuôn (templated) hoàn hảo cho lỗ xốp nano meso/macropore liên thông đối xứng.
*   **Sấy thăng hoa ở áp suất < 20 Pa:** Kế thừa **100% nhiệt động học chuyển pha**. Cơ chế lý hóa: Duy trì áp suất buồng sấy cực thấp dưới điểm tam trạng (Triple point) của nước ($P < 611.65\text{ Pa}$, $T < 0.01^\circ$C). Ở vùng chân không này, các tinh thể đá đông cứng thăng hoa trực tiếp từ pha rắn sang pha khí ($H_2O\text{ (solid)} \rightarrow H_2O\text{ (gas)}$) mà hoàn toàn không trải qua pha lỏng trung gian. Điều này triệt tiêu 100% lực căng bề mặt và áp suất mao dẫn lỏng-khí cực lớn (vốn lên tới vài trăm bar trong lỗ xốp nano), bảo toàn nguyên vẹn khung gel 3D tổ ong không bị co rúm hay sụp đổ cấu trúc.

#### 4. Chỉ số vật liệu đặc trưng đạt được (Pass/Fail Criteria)
*   **Độ co ngót tuyến tính (Linear Shrinkage %):** Phải đạt chỉ số **Linear Shrinkage < 12%** tính theo công thức:
    $$\text{Shrinkage \%} = \frac{D_{\text{gel}} - D_{\text{aerogel}}}{D_{\text{gel}}} \times 100\%$$
    ✓ **Pass:** Cấu trúc xốp 3D được giữ nguyên vẹn. ✗ **Fail:** Nếu co ngót $>20\%$, cấu trúc mạng mao quản đã bị sụp đổ nghiêm trọng do rò rỉ pha lỏng trong lúc sấy chân không kém hoặc cấp đông chậm.
*   **Khối lượng riêng thể tích (Bulk density):** Phải duy trì trong dải **0.03 – 0.05 g/cm³** (siêu nhẹ, có thể đứng vững trên cánh hoa).

---

### GIAI ĐOẠN 5: NHIỆT PHÂN CARBON HÓA LẦN 1 & DOPING NITƠ (First Pyrolysis & N-doping)

#### 1. Thao tác thực nghiệm chuẩn
1.  **Chuẩn bị lò ống nung:** Xếp các khối aerogel khô vào thuyền sứ sạch, đẩy vào tâm nhiệt độ của lò nung ống thạch anh.
2.  **Purge đuổi Oxy bảo vệ:** Thổi dòng khí N₂ tinh khiết (99.99%) với lưu lượng lớn **150–200 mL/min liên tục trong 30 phút** trước khi gia nhiệt để quét sạch toàn bộ khí oxy dư thừa trong ống, tránh làm cháy mẫu ở nhiệt độ cao. Duy trì dòng khí N₂ bảo vệ ổn định ở lưu lượng **100 mL/min** trong suốt tiến trình nung.
3.  **Chương trình nhiệt phân 3 Ramp (Gia nhiệt chuẩn 5°C/phút):**
    *   *Ramp 1 (Sấy ẩm sâu):* Nâng từ $25^\circ\text{C} \rightarrow 150^\circ\text{C}$, giữ nhiệt **30 phút** để giải phóng nước hấp phụ sâu.
    *   *Ramp 2 (Carbon hóa sơ bộ):* Nâng từ $150^\circ\text{C} \rightarrow 400^\circ\text{C}$, giữ nhiệt **30 phút** để cellulose giải phóng các hợp chất hữu cơ thô ổn định.
    *   *Ramp 3 (Carbon hóa sâu & Doping):* Nâng từ $400^\circ\text{C} \rightarrow \mathbf{T_{target}}$, giữ nhiệt liên tục trong **2 giờ (120 phút)**.
    *   *Target nhiệt độ ($T_{target}$):*
        *   **Nhánh mẫu N-CA:** Chọn **$T_{target} = 700^\circ$C** (Tối ưu để bảo toàn mật độ các tâm khuyết tật pyridinic-N hoạt tính).
        *   **Nhánh mẫu Fe/N-CA (nền):** Chọn **$T_{target} = 800^\circ$C** (Tăng mức độ graphit hóa tinh thể phẳng sp² carbon để dẫn điện tối đa).
    *   *Làm nguội:* Tắt gia nhiệt, để lò nguội tự nhiên dưới dòng khí N₂ thổi liên tục cho đến khi nhiệt độ đầu đo đạt **$< 50^\circ$C** mới được mở nắp ống thạch anh lấy mẫu ra ngoài.

#### 2. Tính chất kế thừa từ tài liệu gốc
Kế thừa hoàn toàn chương trình nhiệt phân 3 Ramp và nhiệt độ nung mục tiêu của **Fauziyah et al. 2020 (Trang 2, Experimental Section & Trang 5, Figure 5)**.

#### 3. Tỷ lệ kế thừa (%) & Biện luận cơ chế khoa học
*   **Chương trình nung 3 Ramp gia nhiệt 5°C/min:** Kế thừa **100% hóa học phân hủy nhiệt**. Cơ chế lý hóa: (1) Giữ ở 150°C giúp loại bỏ hơi nước liên kết sâu mà không gây nổ lỗ xốp. (2) Giữ ở 400°C là vùng Cellulose bắt đầu phân hủy mãnh liệt, phân rã các liên kết $C-O$ và giải phóng hắc ín, CO, CO₂ từ từ. Tốc độ nâng nhiệt chậm 5°C/phút khống chế sự thoát khí êm dịu, bảo toàn nguyên vẹn khung thành vách lỗ xốp mỏng 3D tổ ong không bị nứt vỡ do áp suất khí thoát đột ngột.
*   **Kiểm soát nhiệt độ mục tiêu $T_{target}$:** Kế thừa **100% hóa học khuyết tật**. 
    *   *Ở 700°C cho N-CA:* Đây là nhiệt độ vàng để các phân tử Urea phân hủy giải phóng các gốc hoạt tính chứa Nitơ ($NH_x$) phản ứng và thế vào mạng lưới carbon vô định hình, hình thành liên kết **pyridinic-N** với mật độ cao nhất. Nếu nung $>800^\circ$C, liên kết pyridinic-N kém bền nhiệt sẽ bị chuyển vị phân hủy thành graphitic-N hoặc thoát ly, làm giảm hoạt tính hấp phụ paracetamol.
    *   *Ở 800°C cho Fe/N-CA:* Nhiệt độ cao hơn là bắt buộc để kích hoạt sự graphit hóa phẳng của carbon dưới sự xúc tác của ion sắt, tạo cấu hình mạng sp² phẳng dẫn điện cực tốt, đồng thời tạo năng lượng đóng vòng để nguyên tử Fe phối trí với 4 nguyên tử N rìa khuyết tật thành tâm **$Fe-N_4$** bền vững.

#### 4. Chỉ số vật liệu đặc trưng đạt được (Pass/Fail Criteria)
*   **Trạng thái vật liệu sau nung:** Khối carbon aerogel thu được phải có **màu đen tuyền**, xốp, giữ nguyên hình monolith trụ ban đầu nhưng có sự co rút thể tích nhẹ. Khối lượng riêng tăng từ 0.04 g/cm³ lên **0.05 g/cm³ (hệ NH₃)** hoặc **0.07 g/cm³ (hệ NaOH)**.
*   **Độ bền cơ học:** Thử nghiệm ép nén đạt giá trị Young Modulus ổn định từ **6.43 kPa (N-CA)** đến **138.59 kPa (Fe/N-CA)**.

---

### GIAI ĐOẠN 6: RỬA AXIT & ANNEALING LẦN 2 TẠO TÂM Fe-N₄ SIÊU SẠCH (Acid Leaching & Re-annealing)

#### 1. Thao tác thực nghiệm chuẩn
1.  **Phản ứng Acid Leaching đun hồi lưu:** Sử dụng dung dịch **HCl 0.5M** làm tác nhân hòa tan. Cân bột Fe/N-CA nung lần 1, cho vào bình cầu chứa dung dịch HCl 0.5M với tỷ lệ định lượng **1g bột / 100 mL dung dịch**. Lắp hệ thống sinh hàn hồi lưu nước tuần hoàn và đặt trên bếp khuấy từ duy trì đun sôi nhẹ ở nhiệt độ **80 ± 2°C liên tục trong 8 giờ** (tốc độ khuấy nhẹ 200 rpm).
2.  **Lọc rửa trung hòa:** Lọc chắt bột carbon qua phễu lọc chân không Buchner dùng giấy lọc sợi thủy tinh. Rửa liên tục bằng nước cất DI nóng (60°C) cho đến khi nước rửa đạt pH trung tính hoàn toàn ($pH \approx 7.0$). Sấy khô bột ở 80°C trong 12 giờ.
3.  **Annealing tái hoạt hóa lần 2:** Đặt bột đã leaching sấy khô vào thuyền sứ trong lò nung ống thạch anh. Purge khí N₂ đuổi oxy tương tự Giai đoạn 5. Thiết lập chương trình gia nhiệt 5°C/phút lên đúng nhiệt độ mục tiêu **800°C và giữ nhiệt chính xác trong 1 giờ (60 phút)** dưới dòng khí N₂ bảo vệ (100 mL/min). Làm nguội tự nhiên về $<50^\circ$C. Thu bột đen mịn, bảo quản trong vial thủy tinh tối màu quấn Parafilm cất ở tủ mát **4°C**.

#### 2. Tính chất kế thừa từ tài liệu gốc
Kế thừa nguyên lý tinh chế tâm xúc tác đơn nguyên tử sắt từ các công trình nghiên cứu xúc tác điện hóa hàng đầu và cải tiến **100%** quy trình phù hợp với hệ phân tích cảm biến kim loại nặng Pb²⁺.

#### 3. Tỷ lệ kế thừa (%) & Biện luận cơ chế khoa học
*   **Lựa chọn Acid HCl 0.5M đun hồi lưu:** Kế thừa **100% hóa học xúc tác**.
    *   *Biện luận chống bít tắc mao quản:* Tuyệt đối không dùng axit H₂SO₄ loãng/đun nóng. Axit sunfuric là tác nhân oxy hóa và acyl hóa mạnh, có xu hướng gắn các nhóm chức acid sulfonic ($-SO_3H$) phân cực cao bám lên bề mặt carbon hydrokị, làm bít tắc nghiêm trọng cấu trúc lỗ xốp trung bình (mesopores) hoạt tính và cản trở sự chuyển tải điện thế cảm biến.
    *   *Cơ chế hòa tan pha sắt tạp:* Axit HCl trơ tuyệt đối với khung carbon graphite sp² nhưng có ái lực cực mạnh với sắt tự do. Nó hòa tan triệt để các hạt nano sắt kim loại cô lập ($\alpha-Fe$), hạt oxit sắt ($Fe_xO_y$) và sắt carbide tinh thể ($Fe_3C$) không phối trí nằm trơ trọi trên bề mặt, chuyển chúng thành dạng muối hòa tan dễ dàng rửa trôi ($Fe + 2HCl \rightarrow FeCl_2 + H_2$).
*   **Nung Annealing lần 2 ở 800°C trong 1 giờ:** Kế thừa **100% vật lý kết cấu**. Cơ chế lý hóa: Quá trình axit leaching hòa tan sắt tạp để lại các khuyết tật mạng graphite sp² bị đứt gãy, rách nát và các nguyên tử Nitơ tự do mất phối trí. Việc nung tái hoạt hóa lần 2 ở 800°C cung cấp nhiệt lượng vừa đủ để mạng lưới carbon sp² phẳng đóng vòng tự sửa chữa (self-reconstruction), bọc chặt lấy các nguyên tử sắt đơn phân tán cô lập kế cận, định hình và khóa chặt cấu hình phối trí bền vững **$Fe-N_4$ atomically dispersed** hoạt tính siêu cao và siêu bền hóa học.

#### 4. Chỉ số vật liệu đặc trưng đạt được (Pass/Fail Criteria)
*   **Kiểm tra pha tinh thể sắt (XRD):** Giản đồ XRD của bột Fe/N-CA sau annealing lần 2 phải **hoàn toàn trống sạch**, biến mất toàn bộ các đỉnh nhiễu xạ sắc nhọn đặc trưng của sắt kim loại $\alpha-Fe$ ($2\theta \approx 44.7^\circ$) và sắt carbide $Fe_3C$ ($2\theta \approx 43.9^\circ$). 
    ✓ **Pass:** Fe phân tán đơn nguyên tử tuyệt đối (single-atom), không kết tinh pha thô. ✗ **Fail:** Nếu vẫn xuất hiện đỉnh sắc nhọn tinh thể sắt $\rightarrow$ Quá trình rửa axit hồi lưu chưa đạt yêu cầu, bắt buộc phải nâng thời gian leaching hoặc nồng độ HCl.
*   **Hàm lượng nguyên tố bề mặt (XPS):** Sắt đạt **0.4 – 1.5 at%** và Nitơ đạt **3.0 – 6.0 at%** với tỷ lệ tối thiểu $N:Fe \ge 4:1$.

---

## PHẦN III: QUY TRÌNH BIẾN TÍNH ĐIỆN CỰC LÀM VIỆC & ĐO ĐẠC ĐIỆN HÓA

*Áp dụng đối với điện cực carbon thủy tinh (Glassy Carbon Electrode - GCE) đường kính hình học Ø = 3 mm, diện tích làm việc hiệu dụng $A \approx 0.0707\text{ cm}^2$ làm điện cực nền.*

### GIAI ĐOẠN 0: ĐÁNH BÓNG & ANODIZE HOẠT HÓA GCE

1.  **Mài mịn vật lý:** Nhỏ vài giọt nước cất lên tấm nỉ mài, rắc một lượng nhỏ bột Al₂O₃ cỡ hạt 0.05 µm lên. Đặt đứng điện cực GCE vuông góc 90° so với mặt nỉ, di chuyển mài nhẹ nhàng vẽ theo **hình số 8** liên tục trong **2 phút** để loại bỏ màng polymer cũ hoặc lớp oxit thụ động bề mặt.
2.  **Làm sạch bột mài siêu âm:** Nhúng GCE vào cốc nước cất DI, siêu âm làm sạch trong **1 phút** để đẩy các hạt Al₂O₃ bám cơ học ra khỏi bề mặt (lặp lại 3 lần với nước DI mới). Siêu âm tráng nhanh bằng cồn ethanol tuyệt đối trong **1 phút** để khử ẩm.
3.  **Anodize hoạt hóa kiềm (Bắt buộc):** Nhúng điện cực GCE đã siêu âm vào cốc chứa dung dịch **NaOH 0.1M**. Áp thế điện thế phân cực dương cực dương **+1.8 V vs. Ag/AgCl trong thời gian 10 giây**. 
    *   *Biện luận khoa học loại cặn Alumina:* Alumina ($Al_2O_3$) is oxit lưỡng tính. Việc anodize ở thế dương cực cao trong môi trường kiềm mạnh giúp hòa tan hóa học triệt để các hạt alumina siêu nhỏ còn kẹt cứng trong các khe/lỗ xốp nano của carbon thủy tinh ($Al_2O_3 + 2OH^- \rightarrow 2AlO_2^- + H_2O$), giải phóng hoàn toàn bề mặt hoạt tính trơn sạch của GCE. Rửa lại bằng nước cất DI.
4.  **Kiểm tra độ sạch (CV redox probe):**
    *   Nhúng GCE vào dung dịch: **5.0 mM K₃Fe(CN)₆ trong nền 0.1M KCl**.
    *   Quét thế tuần hoàn CV ở tốc độ quét **50 mV/s** (quét 3 chu kỳ).
    *   ✓ **Tiêu chí Pass:** Thế hiệu đỉnh tách biệt giữa peak oxy hóa và peak khử **$\Delta E_p < 70\text{ mV}$** và tỷ số dòng điện đỉnh đối xứng **$I_{pa}/I_{pc} \approx 0.95 - 1.05$**.

### GIAI ĐOẠN 1: PHA CHẾ MỰC IN BINDER & PHỦ ĐIỆN CỰC (Drop-casting)

#### 1. Định lượng pha chế Conductive Ink (Nồng độ bột carbon = 5 mg/mL)
*   **Bột Carbon Aerogel (N-CA hoặc Fe/N-CA):** Cân chính xác **5.0 mg** bột carbon.
*   **Dung môi phân tán nền:** **950 µL DMF** (Dimethylformamide, HPLC grade).
*   **Dung dịch Binder keo liên kết:** **50 µL** dung dịch Binder chuyên biệt (Tổng thể tích Ink = 1000 µL).

#### 2. Quy hoạch Binder chuyên biệt theo chất phân tích:
1.  **Nhánh mẫu Cảm biến kim loại nặng Pb²⁺ (SWASV):**
    *   *Sử dụng Binder:* **Chitosan 1%** trong dung dịch acid acetic 1% v/v.
    *   *Biện luận cơ chế hấp phụ chelate:* Trong môi trường đệm acetate pH 4.5 của phép đo SWASV, các nhóm amino tự do ($-NH_2$) trên mạch polyme Chitosan bị proton hóa mạnh mẽ thành dạng mang điện tích dương ($-NH_3^+$). Các nhóm chức phân cực này đóng vai trò là các phối tử chelating cực mạnh, chủ động bắt giữ cation kim loại nặng $Pb^{2+}$ từ dung dịch loãng thông qua lực hút tĩnh điện và liên kết phối trí. Quá trình này **làm giàu nồng độ chì cực cao (pre-concentration)** sát bề mặt điện cực trước khi quét thế hòa tan, hạ thấp giới hạn phát hiện LOD vượt bậc đạt **0.0033 µM** (Wu et al. 2024).
2.  **Nhánh mẫu Cảm biến dược chất Paracetamol (DPV):**
    *   *Sử dụng Binder:* **Nafion 0.25%** trong cồn ethanol.
    *   *Biện luận cơ chế Anti-fouling:* Nafion là màng ionomer kỵ nước chứa các nhóm sulfonate ($-SO_3^-$) phân cực. Nó hoạt động như một rào cản chọn lọc điện tích: (1) Đẩy ngược tĩnh điện các anion gây nhiễu phân cực trong dịch sinh học như axit uric, axit ascorbic ra xa bề mặt điện cực. (2) Ngăn chặn triệt để hiện tượng bám dính bẩn màng (anti-fouling effect) gây ra bởi các sản phẩm phụ oligome hóa/trùng hợp của paracetamol sau phản ứng oxy hóa bít kín các lỗ xốp carbon hoạt tính.

#### 3. Thực hiện Drop-casting màng mỏng
1.  **Siêu âm phân tán mực:** Bình chứa mực được đậy kín nắp, đặt vào bể siêu âm nước đá lạnh (nhiệt độ duy trì **< 15°C**). Siêu âm liên tục trong **30 phút** ở chế độ siêu âm thường để màng mỏng polymer của binder không bị đứt gãy mạch. Mực in thu được phải đen tuyền, đồng nhất.
2.  **Drop-casting:** Dùng pipette vi lượng hút chính xác **7.0 µL** mực in. Nhỏ thật chậm, vuông góc trực tiếp lên trung tâm bề mặt điện cực GCE đã được dựng thẳng đứng trên giá đỡ.
3.  **Sấy khô màng mỏng:** 
    *   **Bắt buộc:** Úp ngược một cốc thủy tinh sạch che bụi lên điện cực GCE đã nhỏ mực, để màng khô tự nhiên hoàn toàn ở nhiệt độ phòng (25°C) trong **2–3 giờ** trong tủ hút khí độc.
    *   **⚠️ Cảnh báo cực đoan:** Tuyệt đối không sấy gia nhiệt nhanh, không thổi khí N₂ hoặc dùng đèn sưởi hồng ngoại ở giai đoạn này. Sự bay hơi quá nhanh của DMF sẽ gây ra hiệu ứng "vành cà phê" (coffee-ring effect), làm dồn toàn bộ bột carbon ra viền mép điện cực và để rỗng tâm, phá hủy độ bền cơ học và tính tái lặp điện hóa của màng. Tuyệt đối không sấy trong tủ sấy chân không vì áp suất thấp làm dung môi sôi nổ bọt phá hỏng liên kết màng.

### GIAI ĐOẠN 2: CHƯƠNG TRÌNH PHÂN TÍCH ĐIỆN HÓA CẢM BIẾN

#### 1. Phép đo cảm biến Pb²⁺ bằng kỹ thuật sóng vuông hòa tan (SWASV)
*   **WE sử dụng:** Điện cực Fe/N-CA / Chitosan/GCE (mẫu nung 800°C đã acid leaching và annealing lần 2).
*   **Dung dịch điện ly nền:** Đệm Acetate pH 4.5 (Pha từ hỗn hợp dung dịch axit axetic 0.1M và natri axetat 0.1M).
*   **Các bước lập trình thiết bị (SWASV Program):**
  1.  **Làm giàu điện hóa (Pre-concentration):** Áp thế điện thế khử âm **$E_{dep} = -1.1\text{ V}$ vs. Ag/AgCl** trong thời gian **$t_{dep} = 120\text{ s}$** dưới lực khuấy từ ổn định 400 rpm để khử các ion $Pb^{2+}$ thành kim loại chì $Pb^0$ bám dính tích lũy trên màng điện cực.
  2.  **Thời gian cân bằng (Quiet time):** Tắt khuấy từ bể đo, để hệ điện cực đứng yên tĩnh lặng trong **10 giây** để ổn định dòng nền dung dịch.
  3.  **Hòa tan sóng vuông (Anodic Stripping):** Quét thế phân cực anode bằng sóng vuông (SWV) ngược từ **-1.4 V đến -0.2 V vs. Ag/AgCl** để oxy hóa hòa tan chì tích lũy trở lại dung dịch ($Pb^0 \rightarrow Pb^{2+} + 2e^-$). Tín hiệu peak cực đại của chì xuất hiện ở khoảng thế $\approx -0.5\text{ V}$.
      * *Thông số sóng vuông:* SW frequency = **25 Hz** | SW amplitude = **25 mV** | Step potential = **5 mV**.
  4.  **Làm sạch điện cực (Cleaning):** Áp thế dương **+0.2 V trong 30 giây** kết hợp khuấy từ tốc độ cao 600 rpm để giải phóng hoàn toàn lượng kim loại nặng còn sót lại khỏi màng điện cực trước khi thực hiện chu kỳ quét tiếp theo, tránh hiện tượng nhiễm chéo mẫu.

#### 2. Mở rộng phân tích đồng thời đa ion kim loại nặng (Cd²⁺, Cu²⁺, Hg²⁺, Zn²⁺) bằng kỹ thuật SWASV
*   **Ý nghĩa thực tiễn & Học thuật nâng cao:** Bên cạnh cation chì ($Pb^{2+}$), điện cực biến tính **Fe/N-CA / Chitosan/GCE** có khả năng phân tích đồng thời (simultaneous determination) hoặc riêng lẻ các cation kim loại nặng độc hại khác nhờ sự khác biệt rõ rệt về thế khử hòa tan (stripping potential) trên nền carbon dẫn điện.
*   **Cơ chế bắt giữ hiệp đồng (Synergistic Capture Mechanism):**
    *   *Vai trò của coordinated Fe-N₄ active centers:* Các tâm đơn nguyên tử phối trí sắt cung cấp mật độ điện tử cục bộ cao, hoạt động như các "active micro-cavities" giúp xúc tác phản ứng trao đổi electron xảy ra siêu tốc.
    *   *Vai trò của Chitosan 1% Binder:* Các nhóm amino ($-NH_2$) tự do phân bố đều trên polyme Chitosan đóng vai trò là tác nhân càng hóa (chelating ligand) mạnh mẽ bắt cặp với các cation kim loại nặng hóa trị II thông qua cặp electron tự do của nguyên tử Nitơ.
*   **Các thông số thế hiệu đỉnh hòa tan (Stripping Potentials) đặc trưng:**
    Khi thực hiện đo trong đệm **Acetate pH 4.5**, thế hòa tan cực đại xuất hiện riêng biệt, hoàn toàn không bị chồng lấp đỉnh:
    1.  **Kẽm ($Zn^{2+}$):** Stripping peak xuất hiện sắc nét tại **$\approx -1.10\text{ V}$** vs. Ag/AgCl.
    2.  **Cadmium ($Cd^{2+}$):** Stripping peak xuất hiện sắc nét tại **$\approx -0.80\text{ V}$** vs. Ag/AgCl.
    3.  **Chì ($Pb^{2+}$):** Stripping peak xuất hiện sắc nét tại **$\approx -0.50\text{ V}$** vs. Ag/AgCl.
    4.  **Đồng ($Cu^{2+}$):** Stripping peak xuất hiện sắc nét tại **$\approx +0.05\text{ V}$** vs. Ag/AgCl.
    5.  **Thủy ngân ($Hg^{2+}$):** Stripping peak xuất hiện sắc nét tại **$\approx +0.25\text{ V}$** vs. Ag/AgCl.

*   **Thiết lập quy trình đo đồng thời (Simultaneous SWASV):**
    *   *Dung dịch nền:* Đệm axetate 0.1M, pH 4.5.
    *   *Thế làm giàu khử âm sâu:* Đặt điện thế làm giàu **$E_{dep} = -1.30\text{ V}$ vs. Ag/AgCl** (thế này đủ âm hơn thế khử của tất cả các ion gồm cả kẽm và cadmi) trong thời gian **$t_{dep} = 120 - 180\text{ s}$** dưới lực khuấy từ 400 rpm để điện phân khử đồng loạt các cation thành dạng kim loại bám dính màng ($M^{2+} + 2e^- \rightarrow M^0$).
    *   *Thời gian yên lặng:* 10 giây tắt khuấy từ.
    *   *Quét sóng vuông hòa tan anode:* Quét thế xuôi từ **-1.40 V đến +0.40 V vs. Ag/AgCl**. Thu được phổ stripping 4 đỉnh sắc nét phân tách hoàn toàn của Zn, Cd, Pb và Cu.
    *   *Xử lý nhiễu tương tác kim loại (Intermetallic compounds):* Khi đo đồng thời nồng độ cao Cu²⁺ và Zn²⁺/Pb²⁺, có khả năng hình thành hợp chất liên kim loại $Cu-Zn$ hoặc $Cu-Pb$ gây méo đỉnh hoặc giảm dòng stripping. Nhờ sự phân tán đơn nguyên tử cô lập của tâm Fe-N₄ trên vách carbon aerogel xốp diện tích BET lớn ($3733\text{ m}^2/\text{g}$), các nguyên tử kim loại khử $M^0$ được định vị cô lập phân tán xa nhau, hạn chế tối đa sự tụ tập hạt thô liên kim loại, đảm bảo tính tái lặp dòng stripping tuyệt vời.

*   **Thiết lập quy trình đo riêng lẻ Thủy ngân ($Hg^{2+}$):**
    *   *Lý do tách riêng:* Thế khử của thủy ngân rất dương ($+0.25\text{ V}$). Nếu đặt thế khử âm sâu -1.30 V sẽ gây ra phản ứng phụ giải phóng hydro ($HER$) cực mạnh phá hỏng cấu trúc màng Chitosan và gây nhiễu dòng.
    *   *Thông số đo đơn $Hg^{2+}$:* Áp thế điện thế khử làm giàu **$E_{dep} = -0.20\text{ V}$ vs. Ag/AgCl trong thời gian 120 giây** (thế này chỉ khử chọn lọc $Hg^{2+} \rightarrow Hg^0$ mà không khử các ion khác). Quét thế hòa tan sóng vuông từ **0.0 V đến +0.6 V vs. Ag/AgCl**. Peak hòa tan cực đại của thủy ngân xuất hiện tại **$\approx +0.25\text{ V}$**.

#### 3. Phép đo cảm biến Paracetamol bằng kỹ thuật xung vi phân (DPV)
*   **WE sử dụng:** Điện cực N-CA-700 / Nafion/GCE (mẫu carbon hóa 700°C).
*   **Dung dịch điện ly nền:** Phosphate Buffered Saline (PBS) pH 7.0–7.4 (Pha từ dung dịch đệm muối phosphat $Na_2HPO_4 / NaH_2PO_4$ 0.1M).
*   **Các bước lập trình thiết bị (DPV Program):**
  * Khoảng thế quét: Quét phân cực dương từ **0.0 V đến +0.8 V vs. Ag/AgCl**.
  * Tốc độ gia nhiệt quét thế: 20 mV/s.
  * *Thông số xung vi phân:* **Pulse amplitude = 50 mV** | **Pulse width = 50 ms** | **Step potential = 5 mV**.
  * Phép đo được tiến hành quét trực tiếp, hoàn toàn không cần bước áp thế làm giàu điện hóa ($E_{dep}$). Peak oxy hóa Paracetamol xuất hiện rõ nét ở $\approx +0.34\text{ V}$ vs Ag/AgCl.

---

### GIAI ĐOẠN 3: ĐO ĐẠC ĐẶC TÍNH ĐỐI CHỨNG ĐỒNG DẠNG NÂNG CAO (ORR & Siêu Tụ Điện)

#### 1. Phép đo Xúc tác khử Oxy (ORR) làm "Proof of Concept" chứng minh tâm Fe-N₄
*   **Ý nghĩa biện luận khoa học:** Phản ứng ORR nhạy cảm bậc nhất với cấu hình phối trí **$Fe-N_4$ đơn nguyên tử**. Việc chứng minh Fe/N-CA có hoạt tính ORR vượt trội là bằng chứng thực nghiệm vững chắc nhất khẳng định sự hình thành của tâm xúc tác $Fe-N_4$, trực tiếp hỗ trợ biện luận cho cơ chế cảm biến Pb²⁺/Paracetamol.
*   **WE sử dụng:** Điện cực Fe/N-CA / Chitosan/GCE.
*   **Điện ly nền:** Dung dịch **KOH 0.1 M**.
*   **Quy trình đo đạc:**
  1.  Sục khí Nitơ ($N_2$) tinh khiết liên tục vào bình điện giải KOH 0.1M trong 30 phút để đuổi sạch oxy. Tiến hành chạy quét thế CV từ **-1.0 V đến +0.2 V vs. Ag/AgCl** ở tốc độ quét 50 mV/s. CV nền thu được phải là một đường phẳng lỳ đại diện cho dòng dung thuần túy.
  2.  Chuyển sang sục liên tục khí Oxy ($O_2$) trong 30 phút để bão hòa oxy. Chạy quét thế CV tương tự. Đường phổ CV bắt buộc phải xuất hiện một peak khử oxy cực kỳ sắc nét ở thế dương hơn **-0.2 V vs Ag/AgCl** với cường độ dòng đỉnh khử đạt **$I_c \ge 1.0\text{ mA/cm}^2$** (Fauziyah et al. 2020).
  3.  Đo linear sweep voltammetry (LSV) trên điện cực quay RDE ở các tốc độ quay từ 400 rpm đến 3600 rpm để tính toán số electron chuyển tải ($n \approx 3.14 - 3.69$ tiệm cận cơ chế 4 electron).

#### 2. Phép đo Siêu tụ điện hóa (Supercapacitor) của mẫu đối chứng NaOH-Urea
*   **Ý nghĩa:** Kiểm chứng dung lượng tích trữ điện tích lớp kép (EDLC) của mẫu carbon NaOH-Urea bị Na-etching ăn mòn vách tạo mao quản.
*   **WE sử dụng:** Mẫu carbon NaOH-Urea ép viên drop-cast.
*   **Điện ly nền:** Dung dịch **KOH 6.0 M** siêu đậm đặc.
*   **Quy trình đo đạc:**
  1.  Chạy CV trong KOH 6.0M ở các tốc độ quét từ $5 \rightarrow 100\text{ mV/s}$ trong khoảng thế tĩnh từ $-1.0\text{ V} \rightarrow 0.0\text{ V}$ vs. Ag/AgCl. Đường CV thu được phải có dạng **hình hộp chữ nhật đối xứng chuẩn** đại diện cho điện dung lớp kép lý tưởng.
  2.  Đo phóng nạp dòng hằng GCD ở các mật độ dòng từ $0.5 \rightarrow 10\text{ A/g}$. Đường phóng nạp GCD phải có dạng tam giác cân đối xứng, xác định điện dung riêng cụ thể ($C_s\text{ F/g}$) để viết phần biện luận đối chứng cho luận văn.

---

## PHẦN IV: CẨM NĂNG PHÂN TÍCH ĐẶC TRƯNG VẬT LIỆU CHUYÊN SÂU (Characterization Interpretation)

---

### 1. KÍNH HIỂN VI ĐIỆN TỬ QUÉT (SEM) & TRUYỀN QUA (TEM / HR-TEM)

#### SEM (Scanning Electron Microscopy)
*   **Mẫu NH₄OH-Urea (N-CA & Fe/N-CA):** Phải thể hiện rõ nét cấu trúc **tổ ong phân cấp (hierarchical honeycomb)** đồng nhất. Các thành vách carbon mỏng dính, phẳng mịn liên kết với nhau tạo mạng lưới không gian 3D thông suốt với các macropore lớn đường kính **10–100 µm** kế thừa nguyên vẹn từ cấu trúc vách xơ dừa tự nhiên.
*   **Mẫu đối chứng NaOH-Urea:** Ảnh SEM sẽ xuất hiện tình trạng thành vách vỡ vụn, các sợi carbon bị co cụm đặc khít và sụp đổ cấu trúc hoàn toàn. Điều này minh chứng cho sự phá hủy vách mao quản do hiện tượng Na-etching ăn mòn cực mạnh của ion Na+ ở nhiệt độ nung cao.

#### TEM / HR-TEM (High-Resolution Transmission Electron Microscopy)
*   **Đặc trưng tinh thể:** Ảnh HR-TEM phải quan sát thấy các lá carbon siêu mỏng dạng graphene bán tinh thể xếp chồng ngẫu nhiên ở viền rìa (mức độ graphit hóa tinh thể phẳng sp² carbon dẫn điện tốt).
*   **Độ phân tán của pha Sắt (Fe):** Đối với bột Fe/N-CA tối ưu sau rửa axit và annealing lần 2, trên ảnh TEM **tuyệt đối không được xuất hiện** bất kỳ hạt cụm sắt kim loại hoặc hạt sắt carbide tinh thể lớn dạng chấm đen thô (kích thước $> 5\text{ nm}$). Fe phải tồn tại dưới dạng các **chấm sáng đơn phân tán cực kỳ nhỏ ($< 1\text{ nm}$)** đại diện cho các nguyên tử sắt đơn lẻ phối trí (Single-atom dispersion).
*   *Lỗi chẩn đoán Fail:* Nếu xuất hiện các chấm đen đục kích thước lớn 10–50 nm $\rightarrow$ Chứng tỏ quá trình rửa axit hồi lưu bằng HCl chưa sạch sắt tạp, hạt sắt bị thiêu kết vón cục, bắt buộc phải lọc rửa axit lại.

---

### 2. PHÂN TÍCH DIỆN TÍCH BỀ MẶT XỐP HẤP PHỤ (BET)
*   **Dạng đường đẳng nhiệt (Isotherm Curves):** Đường đẳng nhiệt hấp phụ - khử hấp phụ khí Nitơ ở 77K bắt buộc phải thuộc **Loại IV (Type IV Isotherm)** theo phân loại chuẩn của IUPAC. Xuất hiện vòng lặp trễ rõ rệt (hysteresis loop) dạng H3 hoặc H4 trong vùng áp suất tương đối cao $P/P_0 = 0.4 - 0.9$. Đây là bằng chứng thép khẳng định sự tồn tại ưu thế tuyệt đối của hệ thống lỗ xốp trung bình (mesopores) liên thông.
*   **Chỉ số cụ thể tối ưu (Mẫu NH₄OH-Urea 11N):**
    *   Diện tích bề mặt riêng cực đại: **$S_{BET} \ge 3700\text{ m}^2/\text{g}$**.
    *   Tổng thể tích lỗ xốp mao quản: **$V_{pore} \ge 4.0\text{ cm}^3/\text{g}$**.
    *   Đường kính lỗ xốp trung bình (BJH desorption): Tập trung sắc nét trong khoảng **2.0 – 50.0 nm** (mesopores).

---

### 3. PHỔ TẠO MẠNG RAMAN & NHIỄU XẠ TIA X (XRD)

#### Phổ tán xạ Raman (Defect Chemistry)
*   **D-band** ($\approx 1340\text{ cm}^{-1}$): Đại diện cho các khuyết tật mạng graphite, carbon vô định hình sp³ ($C-N$ hoặc $C-O$).
*   **G-band** ($\approx 1579\text{ cm}^{-1}$): Đại diện cho dao động kéo giãn của liên kết sp² carbon tinh thể phẳng dẫn điện tốt.
*   **Tỷ số cường độ đỉnh ($I_D/I_G$):**
    *   **Giá trị vàng đạt chuẩn (Pass):** **$0.9 - 1.2$**.
    *   *Biện luận khoa học:* Tỷ số $I_D/I_G$ nằm trong khoảng này chứng minh cấu trúc carbon sp² dẫn điện tốt (G-band rõ rệt) nhưng đồng thời sở hữu lượng **khuyết tật mạng vừa đủ (D-band)**. Các điểm khuyết tật mạng chính là vị trí các nguyên tử nitơ thế vào khung carbon tạo active sites $Fe-N_x$. Tỷ lệ này giảm nhẹ sau khi annealing lần 2 do mạng graphite sp² được phục hồi một phần độ tinh thể.

#### Nhiễu xạ tia X (XRD - Cấu trúc pha)
*   **Đỉnh phổ carbon:** Chỉ được phép xuất hiện hai đỉnh nhiễu xạ góc tù rộng đặc trưng của carbon bán tinh thể/vô định hình tại góc góc quét **$2\theta \approx 26.4^\circ$** (mặt mạng (002) của graphite) và **$43.5^\circ$** (mặt mạng (100)).
*   **Pha sắt tinh thể:** **Tuyệt đối không** được xuất hiện các đỉnh nhiễu xạ sắc nhọn đại diện cho pha tinh thể thô của sắt kim loại $\alpha-Fe$ ($2\theta \approx 44.7^\circ$) và sắt carbide $Fe_3C$ ($2\theta \approx 43.9^\circ$). Sự biến mất của các đỉnh phổ này chứng minh sắt tồn tại dạng đơn nguyên tử phối trí (single-atom) phân tán hoàn toàn, không kết tinh thành pha tinh thể thô.

---

### 4. PHỔ QUANG ĐIỆN TỬ TIA X (XPS - Thành phần hóa học bề mặt)

#### Hàm lượng nguyên tố bề mặt (XPS Survey)
*   Hàm lượng nguyên tố Nitơ (N 1s) phải đạt từ **3.0 đến 6.0 at%**.
*   Hàm lượng nguyên tố Sắt (Fe 2p) đạt từ **0.4 đến 1.5 at%**.
*   Tỷ lệ nguyên tố $N:Fe \ge 4:1$ đảm bảo đủ liên kết phối trí.

#### Tách phổ phân giải cao N 1s (High-Resolution N 1s Deconvolution)
Phổ N 1s được phân tách chính xác thành 4 peak liên kết N đặc trưng:
1.  **Pyridinic-N ($\approx 398.2\text{ eV}$):** Đây là dạng nitơ quan trọng nhất đối với cảm biến. Cặp electron tự do của Pyridinic-N có ái lực cực mạnh, tạo liên kết phối trí hiến-nhận bền vững với ion sắt $Fe^{3+}/Fe^{2+}$ để tạo thành tâm hoạt tính **$Fe-N_4$**. Bạn cần viết biện luận chứng minh diện tích peak Pyridinic-N chiếm tỷ lệ ưu thế trong phổ phân tích.
2.  **Pyrrolic-N ($\approx 400.1\text{ eV}$):** Nguyên tử N nằm trong vòng năm cạnh carbon, cũng có thể phối trí một phần với sắt tạo cấu trúc $Fe-N_x$.
3.  **Graphitic-N ($\approx 401.3\text{ eV}$):** Nguyên tử N thế vị trí của nguyên tử carbon bên trong mạng sp² phẳng phẳng. Giúp tăng mật độ hạt mang điện và độ dẫn điện tổng thể cho màng carbon.
4.  **Oxidized-N ($\approx 403.0\text{ eV}$):** Các liên kết nitơ bị oxy hóa ($N-O_x$), ít hoạt tính xúc tác.

#### Tách phổ phân giải cao Fe 2p (High-Resolution Fe 2p)
*   Phổ Fe 2p phân tách thành hai đỉnh spin-orbit chính: **Fe 2p₃/₂** ($\approx 711.0\text{ eV}$) và **Fe 2p₁/₂** ($\approx 724.0\text{ eV}$).
*   **Liên kết $Fe-N_x$:** Đóng góp cực đại đặc trưng tại thế liên kết **$710.8\text{ eV} - 711.5\text{ eV}$** là bằng chứng trực tiếp khẳng định sắt phối trí thành công với Nitơ, khác biệt hoàn toàn với peak của Fe kim loại ($707.0\text{ eV}$) hay Fe oxit tự do.

---

## PHẦN V: KIẾN NGHỊ THAY ĐỔI & FILE THAM CHIẾU HỆ THỐNG

### 1. Đề xuất Kiến nghị Điều chỉnh so với Nghiên cứu Cũ (Ref materials)
*   **Khắc phục lỗi sập mao quản hệ NaOH:** So với quy trình tổng hợp cellulose aerogel bằng hệ dung môi NaOH-Urea trong các tài liệu cũ (như luận án NTX Phương 2024 hoặc các tài liệu khảo sát cũ tại Bến Tre), **kiến nghị chuyển hẳn sang hệ Ammonia-Urea làm trục chính chế tạo màng cảm biến điện hóa**. Hệ NaOH-Urea chỉ được duy trì làm mẫu đối chứng đo siêu tụ điện.
*   **Bắt buộc Acid Leaching đun hồi lưu:** Hầu hết các tài liệu cũ chỉ nung carbon 1 lần và bỏ qua giai đoạn làm sạch axit. Đối với điện cực phân tích nhạy dải vết (SWASV Pb²⁺), **bắt buộc phải thực hiện bước leaching đun hồi lưu bằng HCl 0.5M ở 80°C trong 8 giờ và nung annealing lần 2 ở 800°C trong 1 giờ**. Bước này giải quyết triệt để vấn đề nhiễu dòng Faraday do cặn sắt tự do và oxit sắt thô gây ra, đảm bảo Pass chỉ số XRD tinh khiết của xúc tác đơn nguyên tử $Fe-N_4$.
*   **Chiến lược hoạt hóa GCE bằng Anodize kiềm:** Hướng dẫn thực nghiệm cũ chỉ dừng lại ở đánh bóng vật lý bằng bột Al₂O₃. Kiến nghị **áp dụng bắt buộc bước anodize hóa học trong NaOH 0.1M ở thế +1.8 V trong 10 giây** để hòa tan sạch cặn alumina lưỡng tính bám dính cơ học, giải phóng hoàn toàn các khe nano của điện cực carbon thủy tinh.

### 2. Danh mục File Tham chiếu Hệ thống
*   **Tách chiết delignification:** [TOM_TAT_NTXPhuong.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20Ref%20materials/08_Review_va_Tong_quan/TOM_TAT_NTXPhuong.md)
*   **Nguyên lý Ammonia-Urea:** [2 Nitrogen-Doped Carbon Aerogels Prepared by Direct Pyrolysis of.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20Ref%20materials/02_Doping_va_Gel_hoa/2%20Nitrogen-Doped%20Carbon%20Aerogels%20Prepared%20by%20Direct%20Pyrolysis%20of.md)
*   **Nguyên lý Doping Sắt cảm biến:** [1 Facile Synthesis of Fe-Doped Algae Residue-Derived Carbon Aerogels for.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20Ref%20materials/02_Doping_va_Gel_hoa/1%20Facile%20Synthesis%20of%20Fe-Doped%20Algae%20Residue-Derived%20Carbon%20Aerogels%20for.md)
