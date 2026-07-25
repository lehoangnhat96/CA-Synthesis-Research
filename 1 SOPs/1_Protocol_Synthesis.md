# 1_Protocol_Synthesis.md — Quy Trình Thực Nghiệm Chế Tạo Bột Carbon Aerogel

<!-- v2.1 | Cập nhật: 2026-05-31 | Sửa T_anneal 800→750℃ + bỏ ngôn ngữ single-atom Fe-N₄ -->

> [!NOTE]
> * **Nghiên cứu cơ sở:** Fauziyah et al. 2020 (Ind. Eng. Chem. Res.) (doi:10.1021/acs.iecr.0c03771).
> * **Nghiên cứu gel hóa:** Cai & Zhang 2006 (Biomacromolecules) (doi:10.1021/bm050558m).
> * **Cơ chế hoạt hóa & tâm Fe-Nₓ:** Song et al. 2016 (doi:10.1016/j.electacta.2016.03.181).
> 
> Tài liệu này chuẩn hóa quy trình tổng hợp vật liệu **N-doped carbon aerogel (N-CA)** và **Fe/N co-doped carbon aerogel (Fe/N-CA)** từ **xơ dừa Bến Tre** làm điện cực cảm biến điện hóa. Toàn bộ các quy trình NaOH-Urea và TEPA đã được loại bỏ để tập trung vào mục tiêu tối ưu.

---

## BẢNG CÂN BẰNG KHỐI LƯỢNG TIÊU CHUẨN (MASS BALANCE - Cơ sở: 100g xơ dừa khô)

Dưới đây là bảng cân bằng vật chất thực tế từ 100g xơ dừa thô ban đầu để thu được bột Carbon Aerogel (không sử dụng hoạt hóa kiềm và không tẩy trắng mạnh để bảo toàn cấu trúc 3D phân cấp):

| Giai đoạn / Bước | Đầu vào (g) | Đầu ra (g) | Thất thoát (g) | Hiệu suất (%) | Vật liệu thu được | Nguyên nhân thất thoát / Ghi chú |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **GĐ 0** – Rửa sơ bộ | 100.0 | 100.0 | 0.0 | 100.0% | Xơ dừa khô sạch | Loại bỏ bụi cơ học, tạp cát |
| **GĐ 1** – Kiềm hóa NaOH | 100.0 | 65.0 | 35.0 | 65.0% | Bột xơ dừa DCF | Lignin mạch ngắn và hemicellulose tan trong kiềm |
| **GĐ 2** – Sol-gel NH₃-Urea | 65.0 | 61.8 | 3.2 | 95.0% | Hydrogel thô | Phần xơ thô chưa tan (>150 µm) bị lọc bỏ |
| **GĐ 3** – Đông tụ & Sấy | 61.8 | 58.7 | 3.1 | 95.0% | Cellulose Aerogel | Dung môi khuếch tán ra ngoài, co rút nhẹ |
| **GĐ 4** – Nhiệt phân (Pyrolysis) | 58.7 | 15.2 | 43.5 | 25.9% | N-CA hoặc Fe/N-CA nền | Phân hủy nhiệt cellulose, sinh VOCs, CO, CO₂ |
| **GĐ 5** – Acid leaching & Annealing | 15.2 | 13.7 | 1.5 | 90.1% | Fe/N-CA tinh sạch | Rửa trôi Fe oxide thô, Fe metallic không hoạt tính |

---

## GIAI ĐOẠN 0: TIỀN XỬ LÝ KIỀM HÓA TÁCH LIGNIN (Delignification Pretreatment)

> [!IMPORTANT]
> **Ràng buộc định hướng Điện hóa & Cảm biến (No Bleaching):** 
> Đối với hướng **Điện cực cảm biến điện hóa**, quy trình thực nghiệm **tuyệt đối không tẩy trắng bằng $H_2O_2/NaClO_2$ và không thủy phân bằng acid mạnh**. 
> * *Lý do 1 (Bảo toàn cấu trúc 3D):* Chất tẩy trắng và acid mạnh cắt đứt mạch cellulose làm giảm độ trùng hợp (DP), khiến vách ống tế bào xơ dừa bị mỏng yếu và dễ sụp đổ khi nhiệt phân (pore collapse).
> * *Lý do 2 (Giữ lại dị nguyên tố tự nhiên):* Giữ nguyên cấu trúc thô bán tinh thể giúp lưu giữ các nhóm chức heteroatom hữu cơ tự nhiên có sẵn trong xơ dừa, hỗ trợ đắc lực cho quá trình tự doping nitơ và phối trí kim loại sắt ($Fe$) tạo active sites.
> Bột xơ dừa sau kiềm hóa thu được có màu nâu nhạt (**DCF - Delignified Coir Fiber**) được dùng trực tiếp để làm sol-gel.

### 1. Quy trình thực hiện chi tiết
1. Chuẩn bị xơ dừa Bến Tre xay nghiền, rây lấy kích thước hạt **< 100 mesh (~150 µm)** (tối ưu nhất là 120 mesh / 125 µm) để tăng diện tích tiếp xúc kiềm, sấy khô ở 105 ℃ trong 24 giờ.
2. Ngâm 40.0 g bột xơ dừa khô trong 800 mL nước nóng (80 ± 2 ℃) trong 4 giờ dưới lực khuấy từ 600 rpm để rửa sạch bụi bẩn và sáp cơ học. Lọc qua phễu Buchner.
3. Cho bã xơ dừa vào bình tam giác chứa dung dịch **NaOH 6 wt%** (pha 48 g NaOH rắn trong 752 mL nước cất DI, tỷ lệ rắn/lỏng = 40.0 g : 800 mL w/v, đạt đúng tỷ lệ 1 g : 20 mL).
4. Duy trì nhiệt độ ở **80 ± 2 ℃** trong **4 giờ** liên tục, tốc độ khuấy 610 rpm. Bọc kín miệng bình bằng màng PP chịu nhiệt để tránh bay hơi nước.
5. Lọc bã qua phễu Buchner. Rửa bằng nước cất DI nóng (60 ℃) đến khi pH nước rửa đạt mức trung tính (**pH = 6.5–7.0**). Kiểm tra bằng cách chấm giấy chỉ thị trực tiếp lên bã ướt.
6. Sấy khô bột ở **105 ℃** trong 4 giờ (dàn đều bột tránh vón cục).
7. **Cân khối lượng (Gravimetry) bắt buộc:** Cân bột khô trước và sau kiềm hóa (sấy 105 ℃) để tính % weight-loss. 
   $$\text{Weight-loss (\%)} = \frac{m_0 - m_1}{m_0} \times 100$$
   *Trong đó: $m_0$ là khối lượng khô trước xử lý kiềm; $m_1$ là khối lượng khô sau xử lý kiềm.*

### 2. Tiêu chí đánh giá Pass/Fail
* **Hao hụt khối lượng (Weight-loss %):** Phải nằm trong dải **30%–38%** (xác nhận loại bỏ lignin thành công).
* **Trạng thái cảm quan:** Bột DCF mịn, màu nâu nhạt đồng đều, không bị vón cục thô.

---

## GIAI ĐOẠN 1: TỔNG HỢP SOL-GEL & ĐÁNH SIÊU ÂM (Sol-gel & Sonication)

### 1. Quy trình thực hiện chi tiết
1. **Hệ dung môi chuẩn (Cho 1.0 g cellulose DCF):**
   * **$NH_3$ 25%:** 11.0 mL
   * **Urea:** 4.0 g
   * **Nước cất DI:** 5.0 mL
   * *Tổng thể tích dung môi = 16.0 mL (Tỷ lệ rắn/lỏng = 1 g : 16 mL)*
2. **Thứ tự hòa tan:** Cho 11.0 mL $NH_3$ 25% vào bình Teflon phản ứng $\rightarrow$ thêm từ từ 4.0 g Urea tinh thể, khuấy nhẹ cho tan hoàn toàn $\rightarrow$ thêm 5.0 mL nước cất DI $\rightarrow$ cho 1.0 g bột cellulose DCF vào sau cùng. Bọc kín miệng bình bằng màng thực phẩm để tránh thất thoát dung môi.
3. **Đánh siêu âm (Sonication):** Đặt bình phản ứng vào bể siêu âm. 
   * **Bắt buộc:** Đổ đầy đá và nước để duy trì nhiệt độ bể **$\le 10$ ℃ (tối ưu 0–5 ℃)**.
   * **Thiết lập:** Siêu âm chế độ xung (**Pulse 2s on / 1s off**) liên tục trong **30 phút**.
4. **Bảo quản sol:** Thu được hệ sol màu hơi đục nhẹ, phân tán đều. Đặt tĩnh trong ngăn mát tủ lạnh ở **0–5 ℃ trong 24 giờ** để ổn định mạng lưới trước gel hóa.

### 2. Tiêu chí đánh giá Pass/Fail
* **Trạng thái Sol:** Hệ huyền phù keo phân tán đồng đều, không bị lắng cặn hay vón cục sợi thô.
* **Nhiệt độ bể siêu âm:** Phải luôn khống chế nghiêm ngặt $\le 10$ ℃. Nếu nhiệt độ vượt quá 15 ℃ gây bay hơi amoniac dữ dội, làm hỏng sol (Fail).

### 3. Cơ chế phân tán và vai trò của Urea
* **Amoniac ($NH_4OH$):** Đóng vai trò là tác nhân trương nở mạnh. Các ion $NH_4^+$ và $OH^-$ thâm nhập vào các vùng vô định hình và bán tinh thể của cellulose, cắt đứt các liên kết hydro liên phân tử và nội phân tử bền vững của cellulose nguyên bản.
* **Urea:** Đóng vai trò là "lá chắn sơ thủy" (hydrophobic shield). Khi xơ dừa bị trương nở dưới tác động của kiềm, các mặt kỵ nước của mạch cellulose lộ ra ngoài. Urea tự lắp ghép xung quanh các bề mặt kỵ nước này thông qua lực tương tác van der Waals, ngăn không cho các mạch cellulose tái tổ hợp và kết tụ lại với nhau. Đồng thời, urea tạo liên kết hydro mới với các nhóm hydroxyl của cellulose, duy trì trạng thái phân tán bền vững trong hệ sol.

---

## GIAI ĐOẠN 2: ĐÚC KHUÔN & GEL HÓA LẠNH (Casting & Gelation)

### 1. Quy trình thực hiện chi tiết
1. **Đúc khuôn:** Khuyến nghị cao nhất: dùng muỗng/phới dẹt silicone miết nhẹ để chuyển hệ sol sền sệt vào **Khuôn làm bánh flan/cupcake bằng Silicone dẻo (thể tích ~60-70 mL)**. KHÔNG dùng khuôn thủy tinh vì gel bị dính chặt vào vách. Hạn chế dùng ống cứng (như Falcon) vì khó tháo khuôn và dễ làm rách gel.
2. **Khử bọt khí (De-gassing) & Ổn định:** Gõ nhẹ đáy khuôn silicone xuống mặt bàn vài nhịp. Đặt khuôn chứa sol vào ngăn mát tủ lạnh ở **0–5 ℃ trong 15–30 phút** để bọt khí tự động nổi lên và vỡ bớt (Tuyệt đối không dùng sóng siêu âm để khử bọt vì sinh nhiệt và làm bay hơi $NH_3$).
3. **Gel hóa lạnh (Cryo-concentration):** Bọc kín hoàn toàn miệng khuôn bằng nhiều lớp màng bọc thực phẩm (chống bay hơi $NH_3$). Đặt tĩnh khuôn trong ngăn đông tủ lạnh ở **−14 ℃ đến −20 ℃ trong 24 giờ** để xảy ra quá trình đông lạnh tạo gel (frozen gelation).
4. **Rã đông:** Lấy khuôn gel đông băng ra ngoài. **Giữ nguyên lớp màng bọc miệng khuôn**, để rã đông tự nhiên ở nhiệt độ phòng (25 ℃) trong đúng **1 giờ** cho đến khi tinh thể đá tan hoàn toàn thành nước lỏng. (Tuyệt đối không tháo khuôn khi gel còn đang đông đá).
5. **Tháo khuôn:** Mở màng bọc, bóp nhẹ các viền bên ngoài khuôn silicone để không khí lọt vào đáy tách gel ra. Không dùng tay cầm hay muỗng nạy gel.

### 2. Tiêu chí đánh giá Pass/Fail
* Khối hydrogel monolith trụ nhẵn bóng, dẻo dai, đàn hồi tốt, hoàn toàn không bị nứt vỡ cơ học hay rỗng ruột bọt khí.

### 3. Cơ chế đông lạnh tạo gel (Frozen Gelation)
* **Hiệu ứng tích tụ đông băng (Cryo-concentration):** Khi hạ nhiệt độ xuống dưới 0 ℃, nước trong hệ sol kết tinh thành các tinh thể đá tinh khiết. Sự phát triển của tinh thể đá đẩy cellulose, amoniac và urea vào các kênh chất lỏng cực hẹp chưa đông băng giữa các biên tinh thể đá.
* **Tái sắp xếp mạch cellulose:** Dưới áp lực nén ép vật lý của tinh thể đá và nồng độ cellulose tăng vọt trong các kênh lỏng, các mạch cellulose bị ép lại gần nhau. Khi rã đông ở nhiệt độ phòng, các mạch cellulose tiếp xúc gần sẽ tự phát liên kết lại với nhau thông qua mạng lưới liên kết hydro chằng chịt, tạo nên cấu trúc gel 3D vật lý dẻo dai, giam giữ nước bên trong các mao quản rộng.

---

## GIAI ĐOẠN 3: KEO TỤ & TRAO ĐỔI DUNG MÔI (GĐ 3a: Coagulation & GĐ 3b: Solvent Exchange)

### 1. Quy trình thực hiện chi tiết
1. **GĐ 3a — Keo tụ & Đông tụ gel (Coagulation):**
   * **Bắt buộc rã đông an toàn:** ĐỂ NGUYÊN KHUÔN gel lấy ra khỏi tủ đông sinh hàn (không bóc màng bọc miệng), rã đông tự nhiên ở nhiệt độ phòng (25 ℃) trong đúng **1 giờ** cho tới khi đá tan hoàn toàn. (Tuyệt đối không thả gel đông đá vào cồn lạnh vì chênh lệch ứng suất sẽ xé rách khối gel thành từng mảng).
   * **Ngâm cồn đông tụ (Kỹ thuật trượt - Slide):** Chuẩn bị sẵn khay hoặc bình chứa **tối thiểu 200 mL cồn Ethanol tuyệt đối (96-98% ở nhiệt độ phòng)**. Tỉ lệ thể tích cồn/dung môi trong gel phải lớn gấp 10 lần (**tỉ lệ 10:1 v/v**, tương ứng ~200 mL cồn cho mẻ gel chứa ~20 mL dung môi của 1g DCF). **Nghiêng khuôn nhẹ nhàng gạn bớt dung dịch lỏng ở lớp trên của khuôn gel**. Úp ngược khuôn silicone sát mặt cồn (cách < 1 cm), ấn nhẹ đáy khuôn để khối hydrogel dẻo tự trượt nhẹ nhàng vào bể cồn. Không chạm tay hay dùng muỗng nạy gel.
   * **Thời gian đông tụ:** Đậy kín nắp bình chứa, ngâm tĩnh ở **nhiệt độ phòng (25 ± 2 ℃) trong 24 giờ** (hoặc 36–48 giờ cho monolith lớn, thay cồn mới sau 24 giờ đầu để đảm bảo nước được trao đổi hoàn toàn).
   * *Ý nghĩa:* Cồn tuyệt đối đóng vai trò là tác nhân đông tụ và khử nước mạnh, phá vỡ lớp vỏ hydrat hóa của cellulose để tái tạo gel ổn định dạng cấu trúc Cellulose III. Việc ngâm ở nhiệt độ thường giúp quá trình trao đổi diễn ra nhanh chóng và trơn tru, phù hợp với quy trình chuẩn đã được công bố và kiểm chứng của Fauziyah et al. 2020. **Lưu ý đặc biệt về tỷ lệ 10:1 (v/v):** Việc sử dụng lượng cồn áp đảo tối thiểu gấp 10 lần dung môi trong gel là bắt buộc nhằm: (1) *Chống pha loãng (Duy trì >90%):* Khi khối gel 20 mL của bạn tiết nước ra, nó sẽ làm loãng bể cồn. Với 200 mL cồn ban đầu, nồng độ lúc cân bằng vẫn đạt mức $\approx 91\%$. Ở mức nồng độ áp đảo này, cấu trúc xenlulozo mới bị khóa cứng (tủa trắng) vĩnh viễn. Nếu dùng quá ít cồn, cồn bị loãng dưới 50% làm sập vách, mất tác dụng tủa và khối gel bị nhão; (2) *Động lực vắt kiệt Urea:* Lượng cồn khổng lồ đóng vai trò như một "bể hút" (infinite sink), tạo ra sự chênh lệch nồng độ cực lớn để hút sạch sành sanh muối Urea và Amoniac từ tít sâu trong lõi mao quản của gel ra ngoài.
2. **GĐ 3b — Rửa trao đổi dung môi ngược (Solvent Exchange):** Gạn bỏ cồn dư. Thay thế bằng nước DI sạch (thể tích gấp 5 lần thể tích gel). Ngâm trong **2 giờ**, lặp lại **chính xác 2 lần** để nước thay thế hoàn toàn cồn trong mao quản gel.
   * > [!IMPORTANT]
   * > **Cấm sấy trực tiếp từ cồn:** Ethanol có điểm đông đặc cực thấp (−114 ℃) không thể đông băng ở tủ đông thông thường, dẫn đến hiện tượng sôi dung môi làm sập cấu trúc gel (collapse) dưới áp suất chân không sấy thăng hoa.
   * > **Không rửa quá nhiều lần:** Tuyệt đối không rửa quá 3 lần hoặc ngâm rửa cồn/nước kéo dài quá lâu để tránh rửa trôi hoàn toàn urea liên kết vật lý trong mạng gel (nguồn N-doping).

---

## GIAI ĐOẠN 4: SẤY THĂNG HOA (Freeze Drying)

### 1. Quy trình thực hiện chi tiết
1. **Cấp đông trước sấy (Pre-freezing):** Cấp đông khối gel ẩm ở **−20 ℃ đến −40 ℃ trong tối thiểu 12–24 giờ** để đóng băng hoàn toàn nước trong mao quản.
2. **Sấy thăng hoa (Freeze Drying):**
   * Thiết lập thiết bị sấy chân không đạt bẫy lạnh **$\le -45$ ℃** và áp suất buồng sấy **< 20 Pa (~0.15 Torr)**.
   * Xếp các mẫu gel đã đông băng vào buồng sấy. Tiến hành sấy thăng hoa liên tục trong **24–48 giờ** đến khi khối lượng không đổi.
   * Thu được khối Cellulose Aerogel xốp dẻo siêu nhẹ, màu nâu nhạt.

### 2. Tiêu chí đánh giá Pass/Fail
* **Độ co ngót tuyến tính (Linear Shrinkage %):** Đạt chỉ số **Linear Shrinkage < 12%** tính theo công thức:
  $$\text{Shrinkage (\%)} = \frac{D_{\text{gel}} - D_{\text{aerogel}}}{D_{\text{gel}}} \times 100$$
  *✓ Pass: Shrinkage < 12%. ✗ Fail: Shrinkage $\ge 20\%$ (mao quản bị sập do lực mao dẫn).*
* **Khối lượng riêng thể tích (Bulk density):** Duy trì trong dải **0.03–0.05 g/cm³**.

---

## GIAI ĐOẠN 5: NHIỆT PHÂN CARBON HÓA LẦN 1 (First Pyrolysis & N-doping)

### 1. Quy trình thực hiện chi tiết
1. **Chuẩn bị:** Xếp khối aerogel khô vào thuyền sứ sạch, đẩy vào vùng gia nhiệt trung tâm của lò nung ống thạch anh.
2. **Purge khí bảo vệ:** Thổi dòng khí $N_2$ tinh khiết (99.99%) với lưu lượng **150–200 mL/phút trong 30 phút** trước khi gia nhiệt để đuổi hết $O_2$ khỏi lò. Duy trì dòng khí $N_2$ bảo vệ ở lưu lượng **100 mL/phút** trong suốt quá trình nung và làm nguội.
3. **Chương trình nhiệt phân 3 Ramp (Tốc độ gia nhiệt 5 ℃/phút):**
   * **Ramp 1 (Sấy ẩm sâu):** Gia nhiệt từ 25 ℃ $\rightarrow$ 150 ℃, giữ nhiệt **30 phút**.
   * **Ramp 2 (Phân hủy hữu cơ thô):** Gia nhiệt từ 150 ℃ $\rightarrow$ 400 ℃, giữ nhiệt **30 phút**.
   * **Ramp 3 (Carbon hóa & N-doping):** Gia nhiệt từ 400 ℃ $\rightarrow$ **$T_{\text{target}}$**, giữ nhiệt liên tục trong **2 giờ (120 phút)**.
   * **Cooling:** Tắt gia nhiệt, để lò nguội tự nhiên dưới dòng khí $N_2$ bảo vệ. Lấy mẫu ra ngoài khi nhiệt độ đầu đo đạt **< 50 ℃**.
4. **Nhiệt độ mục tiêu ($T_{\text{target}}$) phân nhánh:**
   * **Mẫu N-CA (Cho nhánh Paracetamol):** Chọn **$T_{\text{target}} = 700$ ℃** để bảo toàn tối đa các nhóm nitơ hoạt tính Pyridinic-N (bị phân hủy mạnh ở nhiệt độ > 800 ℃).
   * **Mẫu Fe/N-CA nền (Cho nhánh Kim loại nặng):** Chọn **$T_{\text{target}} = 800$ ℃** để tăng mức độ graphit hóa bề mặt, nâng cao độ dẫn điện của khung carbon nền.

### 2. Tiêu chí đánh giá Pass/Fail
* Khối carbon aerogel thu được màu đen tuyền, cực nhẹ, giữ nguyên hình dạng trụ ban đầu, không bị cháy tro hóa (nếu bị xám tro tức là bị rò rỉ khí oxy vào lò). Bulk density đạt **0.04–0.05 g/cm³**.

---

## GIAI ĐOẠN 6: DOPING Fe (Post-impregnation) — CHỈ CHO Fe/N-CA

> [!IMPORTANT]
> **TUYỆT ĐỐI KHÔNG** thêm muối sắt trực tiếp vào hệ sol-gel kiềm ban đầu vì pH kiềm cao sẽ lập tức làm kết tủa Fe³⁺ dưới dạng $Fe(OH)_3$ thô dạng keo, phá vỡ hoàn toàn cấu trúc sol-gel của cellulose. Phương pháp chuẩn là **tẩm Fe sau nung (Post-impregnation)** trong môi trường ethanol tuyệt đối.

### 1. Quy trình thực hiện chi tiết
1. **Chuẩn bị muối sắt tiền chất:** Sử dụng muối sắt tinh khiết $FeCl_3\cdot6H_2O$ (MW = 270.3 g/mol).
2. **Khảo sát nồng độ Fe chốt:** Khảo sát 2 mức nồng độ Fe nguyên tố theo khối lượng mẫu carbon aerogel nền: **1 wt% Fe** và **5 wt% Fe**.
   * *Công thức tính lượng muối sắt cần cân (Cho 1.000 g bột carbon aerogel):*
     $$m_{FeCl_3\cdot6H_2O} = m_{\text{sample}} \times w_{Fe} \times \frac{270.3}{55.845}$$
   * *Bảng định lượng muối sắt cho 1.000 g mẫu:*
     * **Mức 1 wt% Fe:** Cân **0.0484 g** $FeCl_3\cdot6H_2O$ hòa tan vào 20 mL Ethanol tuyệt đối.
     * **Mức 5 wt% Fe:** Cân **0.242 g** $FeCl_3\cdot6H_2O$ hòa tan vào 20 mL Ethanol tuyệt đối.
3. **Quy trình tẩm sắt:**
   * Cho bột carbon aerogel nền vào dung dịch tẩm muối sắt.
   * Siêu âm nhẹ nhàng trong **30 phút đầu** ở nhiệt độ phòng để đẩy dung dịch muối sắt thâm nhập vào các mao quản sâu.
   * Khuấy từ chậm bằng máy khuấy ở tốc độ 150 rpm liên tục trong **24 giờ** ở nhiệt độ phòng ($25 \pm 2$ ℃) để ion $Fe^{3+}$ khuếch tán đồng đều vào sâu trong cấu trúc.
   * Sấy mẫu sau tẩm ở **60 ℃** trong 12 giờ để loại bỏ hoàn toàn ethanol nhẹ nhàng, thu được bột carbon tẩm Fe khô.

### 2. Tiêu chí đánh giá Pass/Fail
* Bột sau tẩm khô hoàn toàn, màu đen xám đồng đều, không bị vón cục sắt vàng cam bám dính thô ở bề mặt ngoài.

---

## GIAI ĐOẠN 7: HẬU XỬ LÝ — RỬA AXIT & ANNEALING LẦN 2 (GĐ 7a: Leaching & GĐ 7b: Annealing lần 2) — CHỈ CHO Fe/N-CA

### 1. Quy trình thực hiện chi tiết
1. **GĐ 7a — Phản ứng Acid Leaching đun hồi lưu:**
   * Hòa tan bột carbon đã tẩm Fe khô vào dung dịch **HCl 0.5 M** với tỷ lệ **1.0 g bột / 100 mL dung dịch**. 
   * *Lý do chọn HCl:* HCl hòa tan hiệu quả các hạt sắt kim loại tự do và oxide sắt thô dạng hạt mà không gây sulfonation bề mặt carbon như $H_2SO_4$, bảo toàn độ nhạy tối đa cho cảm biến.
   * Đun hồi lưu hỗn hợp trên bếp khuấy từ ở **80 ± 2 ℃ trong 8 giờ** (tốc độ khuấy nhẹ 200 rpm).
2. **Lọc rửa trung hòa:** Lọc bột qua phễu lọc chân không Buchner dùng giấy lọc sợi thủy tinh. Rửa liên tục bằng nước cất DI nóng (60 ℃) cho đến khi nước rửa đạt pH trung tính hoàn toàn (**pH ≈ 7.0**). Sấy khô bột ở 80 ℃ trong 12 giờ.
3. **GĐ 7b — Annealing tái hoạt hóa lần 2:**
   * Đặt bột khô sạch vào thuyền sứ trong lò ống. Purge khí $N_2$ bảo vệ tương tự Giai đoạn 5.
   * Thiết lập chương trình gia nhiệt 5 ℃/phút lên **$T_{\text{anneal}} = $ 750 ℃ và giữ nhiệt chính xác trong 1 giờ (60 phút)** dưới dòng khí $N_2$ bảo vệ (100 mL/phút).
   * *Biện luận khoa học:* Nung ở 750 ℃ (thấp hơn 50 ℃ so với nhiệt phân lần 1) cung cấp đủ năng lượng nhiệt để tái cấu trúc mạng carbon sp² bị lỗi do quá trình rửa axit, đồng thời thúc đẩy phối trí Fe với nitơ vách carbon để tạo tâm hoạt tính **Fe-Nₓ** phân tán đồng đều. Chọn 750 ℃ (thay vì 800 ℃) nhằm giảm nguy cơ tiếp tục làm sập cấu trúc xốp đã hình thành ở bước trước. Thời gian khống chế 1h để tránh phá hủy cấu trúc xốp.
   * Để lò nguội tự nhiên về < 50 ℃ dưới khí bảo vệ. Bảo quản bột trong lọ thủy tinh tối màu quấn Parafilm cất ở tủ mát **4 ℃**.

### 2. Tiêu chí đánh giá Pass/Fail
* **XRD kiểm tra pha tinh thể sắt:** Giản đồ XRD của bột Fe/N-CA sau annealing phải biến mất toàn bộ các đỉnh nhiễu xạ của sắt kim loại $\alpha$-Fe ($2\theta \approx 44.7^\circ$) và sắt carbide $Fe_3C$ ($2\theta \approx 43.9^\circ$).
  * *✓ Pass: Sắt phân tán dạng cluster siêu nhỏ hoặc Fe-Nₓ vô định hình. ✗ Fail: Vẫn xuất hiện các đỉnh sắt tinh thể thô (quá trình rửa acid leaching chưa triệt để).*

---

## TỔNG HỢP CÁC FAILURE MODES (CHẾ ĐỘ THẤT BẠI CẦN TRÁNH TRONG LAB)

### 1. Thất thoát khí $NH_3$ trong quá trình siêu âm sol-gel
* **Hiện tượng:** Nhiệt độ bể siêu âm tăng vượt mức 10 ℃, làm khí amoniac ($NH_3$) bay hơi mạnh ra khỏi hệ sol.
* **Hậu quả:** Giảm nghiêm trọng nồng độ tác nhân kiềm trương nở và nguồn N-doping. Vật liệu sau nung có hàm lượng XPS N < 3 at%, mất đi các nhóm pyridinic-N hoạt tính, điện cực cảm biến đo tín hiệu cực kỳ yếu.
* **Biện pháp kiểm soát:** Bắt buộc duy trì bể nước đá ổn định $\le 10$ ℃ (ưu tiên 0–5 ℃) và bọc thật kín miệng bình phản ứng.

### 2. Sụp đổ mạng lưới xốp 3D (Gel Collapse) khi trao đổi dung môi
* **Hiện tượng:** Rửa nước DI quá nhiều lần làm trôi hết Urea liên kết vật lý trong gel, hoặc sấy thăng hoa khi nước chưa đông băng hoàn toàn hoặc còn tàn dư cồn trong mao quản.
* **Hậu quả:** Lực mao dẫn trong pha lỏng-khí kéo sập vách cellulose, làm aerogel sau sấy bị co rút mạnh (Shrinkage > 20%), khối lượng riêng tăng vọt, diện tích bề mặt $S_{\text{BET}}$ sụt giảm nghiêm trọng (< 150 m²/g), cản trở sự khuếch tán ion khi làm cảm biến.
* **Biện pháp kiểm soát:** Khống chế chính xác tỷ lệ cồn 98% ở nhiệt độ phòng, rửa ngược nước DI chính xác 2 lần và cấp đông sâu $\ge 12\text{ h}$ trước khi sấy.

### 3. Tụ tập hạt sắt thô (Iron Aggregation) không tạo tâm hoạt tính Fe-Nₓ
* **Hiện tượng:** Hàm lượng sắt tẩm quá cao (10–15 wt%) hoặc quá trình acid leaching hồi lưu đun rửa không đủ thời gian/nhiệt độ, hoặc annealing lần 2 ở nhiệt độ quá thấp (< 700 ℃) hay quá cao (> 900 ℃).
* **Hậu quả:** Sắt tồn tại dưới dạng hạt nano oxide sắt ($Fe_2O_3$, $Fe_3O_4$) hoặc hạt sắt kim loại thô. Bột có XPS Fe rất cao nhưng điện trở chuyển điện tích $R_{ct}$ trên EIS không giảm, peak stripping của kim loại nặng bị nhòe và xuất hiện peak giả của sắt.
* **Biện pháp kiểm soát:** Duy trì nồng độ Fe khảo sát thấp (1% và 5%), đun hồi lưu HCl 0.5M đủ 8 giờ và annealing lần 2 chính xác ở **750 ℃** trong 1 giờ.
