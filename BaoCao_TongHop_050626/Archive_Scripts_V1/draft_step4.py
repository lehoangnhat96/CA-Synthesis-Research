import re

dclv_path = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\ch3.txt"
part3_path = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\part3_master.md"
draft_path = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\BaoCao_TongHop_050626\Draft_Chuong3_4.md"

with open(part3_path, 'r', encoding='utf-8') as f:
    part3 = f.read()

draft = f"""# CHI TIẾT BẢN NHÁP CHƯƠNG 3 & KẾT LUẬN (BƯỚC 4)

> Ở bước này, tôi đã lấy các thông số kỳ vọng tuyệt đẹp (SEM, TEM, XPS, EIS, LOD) từ `Master_Thesis_Full_Draft.md` và đúc kết lại thành các đoạn văn học thuật. Các đoạn này sẽ được cấy ghép vào Chương 3 của DCLV nhằm làm nổi bật **Dự kiến kết quả**.
> Số trích dẫn cũng sẽ được quy đổi tương tự như các bước trước.

---

## 3.1. Đặc trưng Hình thái và Hóa lý (Dự kiến)

**1. Hình thái bề mặt và Cấu trúc vi mô (SEM, TEM, BET):**
Dưới kính hiển vi điện tử quét (SEM), hình ảnh dự kiến của Fe/N-CA thể hiện rõ một mạng lưới xốp tổ ong 3D (3D honeycomb-like structure) đan xen liên tục. Các lỗ xốp lớn (macropores) được hình thành từ quá trình thăng hoa tinh thể đá trong bước sấy thăng hoa. Đặc biệt, ảnh TEM độ phân giải cao kỳ vọng không xuất hiện các hạt nano sắt vón cục (agglomerations), minh chứng quá trình rửa axit bằng HCl nóng đã loại bỏ tạp chất Fe/Fe3C, chỉ để lại các cụm nano hoặc nguyên tử sắt đơn lẻ [47]. Về độ xốp, đường cong đẳng nhiệt hấp phụ-khử hấp phụ N2 dự kiến thuộc Loại IV với vòng trễ H4. Diện tích bề mặt riêng (SBET) kỳ vọng đạt trên 300 m²/g, tạo "kênh cao tốc" lý tưởng cho dung dịch điện ly và chất phân tích khuếch tán.

**2. Cấu trúc Tinh thể và Khuyết tật (XRD, Raman):**
Giản đồ XRD dự kiến xuất hiện đỉnh nhiễu xạ rộng đặc trưng của mặt phẳng (002) tại 2θ = 26°, đại diện cho carbon vô định hình, và vắng bóng các đỉnh sắc nét của Fe kim loại (44°, 65°), khẳng định sắt đã được neo vào khung carbon dưới dạng liên kết phối trí vô định hình [44]. Phổ Raman kỳ vọng hiển thị tỷ lệ cường độ ID/IG trong khoảng 0.9 - 1.2. Sự gia tăng của dải D chứng minh các nguyên tử N và Fe đã tạo ra vô số khuyết tật làm tâm xúc tác, trong khi dải G vẫn duy trì độ dẫn điện nền xuất sắc nhờ quá trình nung ủ ở 800°C [48].

**3. Phân tích Thành phần Hóa học (XPS):**
Phổ XPS toàn dải dự kiến xác nhận tỷ lệ nguyên tử N chiếm 3-6 at% và Fe chiếm 0.4-1.5 at%. Phổ phân giải cao N 1s kỳ vọng cho thấy sự ưu thế của Pyridinic-N (398.5 eV) và Pyrrolic-N (400.1 eV). Đặc biệt, phổ Fe 2p sẽ vắng bóng đỉnh Fe0, và sự dịch chuyển năng lượng liên kết của Fe2+/Fe3+ là minh chứng vững chắc cho việc hình thành cấu trúc tâm xúc tác đơn nguyên tử Fe-Nx-C [44].

---

## 3.2. Tính chất Điện hóa Cơ bản (CV, EIS)

Động học truyền điện tử được đánh giá qua kỹ thuật CV và EIS trên nền [Fe(CN)6]3-/4-. 
- **CV:** Điện cực Fe/N-CA/GCE dự kiến cho dòng đỉnh (Ip) tăng mạnh và độ phân cực (ΔEp) thu hẹp xuống < 120 mV, khẳng định các nguyên tử Fe đóng vai trò "chất dẫn tốc" trao đổi electron [49].
- **EIS:** Đường kính vòng bán nguyệt ở vùng tần số cao (Rct) dự kiến sụt giảm nghiêm trọng theo thứ tự: Bare GCE >> N-CA/GCE > Fe/N-CA/GCE. Giá trị Rct của Fe/N-CA kỳ vọng < 100 Ω nhờ hiện tượng "hiệp đồng điện tử" giữa khung graphit dẫn điện tốt và tâm Fe-Nx hạ thấp rào cản năng lượng hoạt hóa [49].

---

## 3.3. Dự kiến Thẩm định Phân tích Vết Kim loại nặng & Paracetamol

*Bảng 3.2 của DCLV sẽ được nâng cấp để bao gồm cả LOD của Paracetamol*

| Chất phân tích | Kỹ thuật | Khoảng tuyến tính | R² | Giới hạn phát hiện (LOD) | RSD |
|---|---|---|---|---|---|
| Pb²⁺ | SWASV | 0.5 – 150 ppb | ≥ 0.999 | < 0.1 ppb | < 4.5% |
| Cd²⁺ | SWASV | 1.0 – 150 ppb | ≥ 0.999 | < 0.2 ppb | < 5.0% |
| Zn²⁺ | SWASV | 2.0 – 200 ppb | ≥ 0.999 | < 0.5 ppb | < 5.0% |
| Paracetamol | DPV | 0.5 – 500 μM | ≥ 0.99 | 0.05 – 0.5 μM | < 5.0% |

**Biện luận cơ chế:**
- **Đối với Kim loại nặng (Pb/Cd/Zn):** LOD siêu nhạy (< 0.1 ppb) đạt được nhờ sự hiệp đồng kép giữa diện tích bề mặt lớn của carbon aerogel và sự phối trí đặc hiệu của tâm Fe-N4 kết hợp với màng kết dính Chitosan (đóng vai trò "nam châm" làm giàu hóa học) [45].
- **Đối với Paracetamol:** Màng composite Nafion kỵ nước hoạt động như "màng rây chọn lọc", cản trở Ascorbic Acid (AA) và Uric Acid (UA), đồng thời tâm Fe-N4 giúp tách bạch hoàn hảo các đỉnh oxy hóa của AA, UA và Paracetamol trong phép đo đồng thời [48]. Mẫu thực tế (viên nén Panadol, nước máy, nước sông) dự kiến cho độ thu hồi (Recovery) từ 95% - 105%.
"""
with open(draft_path, 'w', encoding='utf-8') as f:
    f.write(draft)
print("Draft for Chapter 3 generated.")
