import re

draft_path = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\Draft_Chuong2_Academic.md"

draft_content = """# BẢN NHÁP CẬP NHẬT CHƯƠNG 2 (Cấu trúc Hàn lâm)

> Dưới đây là nội dung chi tiết được biên soạn lại từ file SOP bằng văn phong học thuật, thay thế cho các gạch đầu dòng ngắn gọn trong mục `2.2. Quy trình thực nghiệm 8 giai đoạn` của DCLV.
> Cấu trúc được nâng cấp thành các tiểu mục (2.2.1 đến 2.2.8) để phù hợp với format Luận văn. Mọi con số trích dẫn [P-xxx] đã được chuyển sang số [X] theo Bảng Mapping.

---

### 2.2.1. Giai đoạn 0: Tiền xử lý kiềm hóa tách lignin
Sợi xơ dừa Bến Tre được nghiền nhỏ và rây qua rây 100 mesh để tối ưu hóa bề mặt tiếp xúc. Quá trình kiềm hóa được thực hiện bằng dung dịch NaOH 6% (w/v) ở nhiệt độ 80 ± 2°C trong 4 giờ với tỷ lệ rắn/lỏng là 1:20. Xử lý kiềm ở điều kiện này giúp cắt đứt các liên kết ether giữa lignin và hemicellulose, làm lộ ra các vi sợi cellulose (cellulose microfibrils) thuần khiết [13]. Tuy nhiên, điểm khác biệt cốt lõi của quy trình này là sự kiểm soát để không tẩy trắng triệt để. Việc giữ lại một phần lignin đóng vai trò như các "trụ cột" (pillars) cứng nhắc tự nhiên, chống lại sự sụp đổ của khung mạng trong quá trình đông tụ và sấy thăng hoa, đồng thời cung cấp điện dung giả (pseudocapacitance) tạo vị trí hoạt tính cho cảm biến điện hóa sau này [43]. Khối lượng bã sau xử lý được theo dõi cẩn thận bằng phương pháp phân tích trọng lượng (gravimetry) sau khi sấy ở 105°C để kiểm soát tỷ lệ hao hụt.

### 2.2.2. Giai đoạn 1: Tổng hợp Sol-gel và Đánh siêu âm
Hệ dung môi phân cực được sử dụng gồm NH3 25%, Urea và H2O theo tỷ lệ tương ứng 11:4:5 (v/w/v) cho 1g cellulose thô. Hỗn hợp được phân tán bằng kỹ thuật siêu âm xung (2s on / 1s off) trong 30 phút. Quá trình siêu âm bắt buộc phải được duy trì trong bể nước đá (≤ 10°C) nhằm khống chế áp suất hơi của amoniac [5]. Việc thay thế hệ dung môi NaOH/Urea truyền thống bằng NH3/Urea đóng vai trò kép: vừa hòa tan cellulose vừa cung cấp tiền chất để tự pha tạp nitơ (in-situ N-doping) vào mạng carbon ở giai đoạn nhiệt phân [44]. Ở nhiệt độ thấp, động học tự lắp ráp (Dynamic Self-Assembly) được kích hoạt, trong đó vỏ bảo vệ urea ngăn cản cellulose tái kết tụ. Sol thu được sau đó được ủ ở -12°C trong 24 giờ để ổn định mạng lưới.

### 2.2.3. Giai đoạn 2: Đúc khuôn và Gel hóa lạnh
Sol được đúc vào các khuôn ống PP (Polypropylene) thay vì thủy tinh để tận dụng đặc tính kỵ nước của PP, giúp lấy gel dễ dàng mà không gây nứt gãy cơ học. Các bọt khí trong khuôn được khử bằng phương pháp tĩnh kết hợp chân không trong 30-60 phút ở 0-5°C nhằm cân bằng gradient nhiệt. Quá trình gel hóa chính thức được kích hoạt bằng cách cấp đông ở nhiệt độ từ -14°C đến -20°C trong 24 giờ. Cơ chế định hình bằng tinh thể đá (Ice-templating) xảy ra khi sự phát triển của băng ép các chuỗi cellulose lại với nhau [30]. Tốc độ làm lạnh chậm ở dải nhiệt độ này giúp tạo ra hệ thống lỗ xốp dạng tổ ong (honeycomb) song song định hướng, tối ưu hóa không gian cho sự khuếch tán chất phân tích [40].

### 2.2.4. Giai đoạn 3: Keo tụ và Trao đổi dung môi
Gel lạnh sau khi lấy khỏi tủ đông được rã đông tự nhiên ở nhiệt độ phòng. Quá trình keo tụ (coagulation) diễn ra bằng cách ngâm hydrogel vào ethanol 98% (tỷ lệ 15 mL cồn / 1 mL gel) ở nhiệt độ 20-25°C trong 24-48 giờ. Ethanol hoạt động như một chất phản dung môi (antisolvent), phá vỡ lớp vỏ hydrat hóa của cellulose để tái liên kết hydro nhanh chóng và tạo sự tách pha (phase separation). Nhờ khung cơ lý xơ dừa đã được tiền xử lý co ngót từ Giai đoạn 0, cấu trúc mạng 3D của gel đạt được độ cứng cơ học xuất sắc. Gel sau đó được rửa bằng nước cất nhiều lần để loại bỏ cồn tồn dư mà không làm rửa trôi các tiền chất nitơ còn bám dính, đảm bảo nồng độ N-doping lý tưởng đạt 3-6% at.

### 2.2.5. Giai đoạn 4: Sấy thăng hoa (Freeze-drying)
Gel được cấp đông sâu lại ở -50°C trong 12 giờ trước khi sấy thăng hoa dưới áp suất chân không (< 20 Pa) với nhiệt độ bẫy lạnh ≤ -30°C trong 24-48 giờ. Việc loại bỏ dung môi bằng quá trình thăng hoa (rắn sang khí) giúp triệt tiêu hoàn toàn lực mao quản tại các giao diện lỏng-khí, ngăn ngừa hiện tượng sụp đổ thành lỗ xốp thường gặp ở sấy nhiệt thông thường. Phương pháp này bảo tồn thành công các lỗ xốp vĩ mô (macropores) định hướng từ Giai đoạn 2, tạo ra các "đường cao tốc" khuếch tán lý tưởng, giúp giảm thiểu điện trở truyền khối của điện cực cảm biến [46].

### 2.2.6. Giai đoạn 5: Nhiệt phân carbon hóa lần 1
Aerogel được carbon hóa trong lò nung ống thạch anh dưới môi trường khí trơ N2 (tốc độ dòng 100 mL/min). Để kiểm soát ứng suất nhiệt sinh ra do sự giải phóng khí phân hủy đột ngột, một chiến lược nung ba chặng (3-ramp thermal strategy) được áp dụng: gia nhiệt chậm 5°C/min và giữ nhiệt lần lượt ở 150°C và 400°C trong 30 phút trước khi lên nhiệt độ mục tiêu. Mẫu Carbon Aerogel biến tính Nitơ (N-CA) được nung ở 700°C trong 2 giờ nhằm tối ưu hóa mật độ nhóm pyridinic-N xúc tác đạt mức cực đại (~54%). Đối với mẫu làm nền (Fe/N-CA), nhiệt độ mục tiêu là 800°C nhằm ưu tiên tăng cường mức độ graphit hóa bề mặt, tạo ra điện cực có độ dẫn điện xuất sắc [8].

### 2.2.7. Giai đoạn 6: Doping Fe bằng phương pháp tẩm sau (Post-impregnation)
Mẫu carbon nền Fe/N-CA được phân tán vào dung dịch ethanol chứa tiền chất FeCl3.6H2O (khảo sát nồng độ 1 wt% và 5 wt% Fe). Phương pháp tẩm sau (post-impregnation) được ưu tiên hơn so với đồng kết tủa (co-precipitation) nhằm tránh hiện tượng Fe(OH)3 tạo tủa trong môi trường kiềm ở giai đoạn Sol-gel làm hỏng mạng cellulose. Trong môi trường cồn, ion Fe3+ khuếch tán vào lõi carbon dưới sự hỗ trợ của siêu âm (30 phút đầu) và khuấy từ chậm (25 rpm, 24 giờ). Các orbital trống của sắt phối trí trực tiếp với các vị trí nitơ khuyết tật, tạo nên các liên kết xúc tác Fe-Nx vững chắc [48].

### 2.2.8. Giai đoạn 7: Xử lý acid và Nung ủ lần 2 (Acid Leaching & Annealing)
Để tinh sạch bề mặt và loại bỏ các hạt sắt oxit thô không hoạt tính, bột carbon được đun hồi lưu trong dung dịch HCl 0.5 M ở 80 ± 2°C trong 8 giờ. Bước này giúp cô lập các tâm hoạt động Fe-Nx phân tán cấp độ nguyên tử (single-atom). Mẫu sau khi rửa sạch đến pH trung tính được tiến hành nung ủ lần 2 (re-annealing) trong 1 giờ. Đề tài khảo sát hai mức nhiệt độ: 750°C nhằm bảo vệ hàm lượng nitơ, và 800°C nhằm gia tăng độ graphit hóa. Các đánh giá hóa lý và điện hóa đa chiều sẽ được sử dụng để quyết định thông số nung ủ tối ưu cuối cùng.
"""

with open(draft_path, 'w', encoding='utf-8') as f:
    f.write(draft_content)
print("Academic Draft generated.")
