# 3_Literature_Review_and_Gap_Analysis.md — So Sánh Đối Chứng Kỹ Thuật & Giải Quyết Lỗ Hổng Thực Nghiệm (Gap Analysis)

> [!NOTE]
> * Luận án tham chiếu: [Nguyễn Trần Xuân Phương 2024](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20Ref%20materials/08_Review_va_Tong_quan/TOM_TAT_NTXPhuong.md) (Đối chứng hệ $NaOH$ và TEPA).
> * Nghiên cứu cơ sở: [Fauziyah et al. 2020 (Ind. Eng. Chem. Res.)](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20Ref%20materials/02_Doping_va_Gel_hoa/2%20Nitrogen-Doped%20Carbon%20Aerogels%20Prepared%20by%20Direct%20Pyrolysis%20of.md) (Mô hình $NH_4OH$-Urea chuyển pha Cellulose III).
> * Quy trình liên kết thực tế:
>   * [1_Active_Protocol_Synthesis.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/1_Active_Protocol_Synthesis.md)  
>   * [2_Active_Protocol_Electrochemistry.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/2_Active_Protocol_Electrochemistry.md)  
>   * [4_Material_Characterization_Guide.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/4_Material_Characterization_Guide.md)

---

## 1. SO SÁNH ĐỐI CHỨNG HỆ DUNG MÔI: NH₄OH/UREA VS. NAOH/UREA

Bảng so sánh đối chứng thông số vật lý và điện hóa sau nung giữa hai hệ dung môi chế tạo aerogel:

| Chỉ số vật lý & điện hóa | Hệ dung môi chính $NH_4OH$-Urea (Tạo màng cảm biến) | Hệ dung môi đối chứng $NaOH$-Urea (Đo siêu tụ điện) |
| :--- | :--- | :--- |
| **Pha tinh thể Cellulose ẩm** | Cellulose III | Cellulose II |
| **Pha tinh thể sau nung** | Carbon bán tinh thể sp² graphitized | Carbon vô định hình bị ăn mòn kiềm |
| **Trạng thái bay hơi dung môi** | Bay hơi $100\%$ ($NH_3$ thoát ly hoàn toàn) | Không bay hơi (Cặn ion $Na^+$ bám dính gel) |
| **Diện tích bề mặt riêng ($S_{\text{BET}}$)** | **$\ge 3700\text{ m}^2/\text{g}$** (cấu trúc lá tổ ong siêu mỏng) | **$\le 150\text{ m}^2/\text{g}$** (vách lỗ xốp bị ăn mòn sụp đổ) |
| **Độ dẫn điện màng sau nung** | **$5.08 S/cm$** | **$0.93 S/cm$** |
| **Hiệu ứng ở nhiệt độ cao ($800^\circ\text{C}$)**| Tự bóc tách các lớp carbon tạo khuyết tật mạng ($N$-doping) | Ăn mòn hóa học vách tế bào gây sập mao quản ($Na$-etching) |
| **Ứng dụng điện hóa tối ưu** | **Cảm biến màng mỏng dải vết & ORR** (truyền điện tích nhanh) | **Siêu tụ điện tích lũy lớp kép (EDLC)** trong $KOH$ $6.0\text{ M}$ |

---

## 2. MA TRẬN GIẢI QUYẾT 10 LỖ HỔNG THỰC NGHIỆM (Gap Analysis G1 - G10)

Bảng tổng hợp các thông số kỹ thuật đối chứng và giải pháp tối ưu hóa nhằm khắc phục 10 lỗi thực nghiệm thường gặp trong các nghiên cứu cũ:

| Lỗ hổng kỹ thuật | Mã số | Thông số lỗi thường gặp (Ref Materials) | Thông số kỹ thuật tối ưu hóa đạt chuẩn (Active SOPs) |
| :--- | :---: | :--- | :--- |
| **Kiểm soát Delignification** | **G1** | Chỉ ngâm kiềm thô hoặc rửa cơ học không kiểm soát, lignin còn bám dính gây cản sol-gel hóa. | Thực hiện **NaOH 6 wt% ở $80 \pm 2^\circ\text{C}$ trong $4\text{ giờ}$**; kiểm soát hiệu suất hao hụt khối lượng khô DCF **$30\% - 38\%$**. |
| **Khuôn đúc hydrogel** | **G2** | Dùng khuôn thủy tinh gây bám dính cơ học, mẻ đầu monolith hoặc nứt vỡ khi đẩy gel. | Sử dụng **ống tiêm Polypropylene (PP) cắt đầu** (kháng dính hydrogel tuyệt đối, đẩy pít-tông trơn tru). |
| **Thời gian ổn định Sol** | **G3** | Đúc khuôn già hóa nhiệt ngay sau siêu âm gây bọt khí kẹt trong monolith tạo rỗng xốp lỗi. | Đặt tĩnh sol đông tụ ở **$0 - 5^\circ\text{C}$ trong $30 - 60\text{ phút}$** (de-gassing hoàn toàn + mầm tinh thể đá đồng đều). |
| **Tỷ lệ co rút thể tích** | **G4** | Co ngót tuyến tính $>20\%$ gây sập vách, co rúm và sụp đổ cấu trúc aerogel sau sấy chân không. | Ngâm cồn **Ethanol 98% lạnh ở $0 - 5^\circ\text{C}$ trong $24\text{ giờ}$** (keo tụ), khống chế **Linear Shrinkage $< 12\%$**. |
| **Thời gian ngâm tẩm Sắt**| **G5** | Ngâm muối sắt FeCl3 quá ngắn ($<4\text{ giờ}$) gây nghèo hoạt chất lõi, sắt tập tụ thô ngoài rìa. | Siêu âm nhẹ $30\text{ phút}$ nước đá + ngâm tĩnh **$24\text{ giờ}$ ở $4^\circ\text{C}$** để ion $Fe^{3+}$ khuếch tán bão hòa đều lõi. |
| **Nhiệt độ ngâm tẩm Fe** | **G6** | Ngâm tẩm sắt ở nhiệt độ cao ($>40^\circ\text{C}$) làm bay hơi dung môi, thay đổi nồng độ tẩm bất ngờ. | Duy trì ngâm tẩm tĩnh ở **$0 - 5^\circ\text{C}$ (hoặc tủ mát $4^\circ\text{C}$)** liên tục trong $24\text{ giờ}$. |
| **Lựa chọn Acid Leaching** | **G7** | Sử dụng axit $H_2SO_4$ loãng/nóng gây sulfon hóa bề mặt carbon, bít tắc mesopores màng. | Dùng **$HCl$ $0.5\text{ M}$ đun hồi lưu ở $80 \pm 2^\circ\text{C}$ trong $8\text{ giờ}$** (hòa tan sắt tự do, trơ mạng carbon sp²). |
| **Nhiệt độ Annealing 2** | **G8** | Bỏ qua bước nung lần 2 hoặc nung nhiệt độ thấp gây sập cấu trúc khuyết tật hoặc thiêu kết. | Nung re-anneal ở **$800^\circ\text{C}$ trong $1\text{ giờ}$** dưới dòng khí $N_2$ ($100\text{ mL/phút}$) để cố định cấu hình tâm **$Fe-N_4$**. |
| **Chất liên kết Ink GCE** | **G9** | Sử dụng keo bám dính không phân tách, gây nhiễu dòng Faraday hoặc làm tăng điện trở màng mỏng. | Phân tách chuyên biệt: **Chitosan 1%** (cho Pb2+ SWASV chelate) và **Nafion 0.25%** (cho Paracetamol DPV chống bám bẩn). |
| **Sự khác biệt dung môi** | **G10** | Dùng hệ NaOH-Urea chế tạo màng cảm biến gây dòng yếu, trở kháng lớn do sập cấu trúc mao quản. | **Hệ $NH_4OH$-Urea** làm trục chính màng cảm biến cảm biến ($S_{BET} \ge 3700\text{ m}^2/\text{g}$). Hệ NaOH chỉ làm tụ điện. |
