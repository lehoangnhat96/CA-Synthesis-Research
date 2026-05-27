# 4_Material_Characterization_Guide.md — Cẩm Nang Phân Tích Đặc Trưng Vật Liệu Carbon Aerogel

> [!NOTE]
> * Quy trình liên kết thực tế:
>   * [1_Active_Protocol_Synthesis.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/1_Active_Protocol_Synthesis.md)  
>   * [2_Active_Protocol_Electrochemistry.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/2_Active_Protocol_Electrochemistry.md)  
>   * [3_Literature_Review_and_Gap_Analysis.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/3_Literature_Review_and_Gap_Analysis.md)
> * Chiến lược công bố: [5_Project_Timeline_and_Publication_Strategy.md](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/5_Project_Timeline_and_Publication_Strategy.md)

---

## 1. PHÂN TÍCH HÌNH THÁI VÀ CẤU TRÚC VẬT LÝ NỀN (SEM & TEM)

### 1.1 Kính hiển vi điện tử quét (SEM)
*   **Mục tiêu ghi nhận:** Quan sát cấu trúc không gian 3D xốp và sự biến đổi vách tế bào của aerogel.
*   **Tiêu chuẩn đạt chuẩn đối với màng cảm biến (Pass Criteria):**
    *   Ảnh SEM phải thể hiện rõ cấu trúc **dạng tổ ong phân cấp** (hierarchical honeycomb/alveolar structure) liên thông với các macropore lớn đường kính **10–100 µm** kế thừa từ vách xơ dừa tự nhiên.
    *   Thành vách carbon phải mỏng, phẳng mịn và không bị sụt đổ, chứng minh hệ amoniac và quá trình sấy thăng hoa đã bảo toàn được khung gel.
*   **Mẫu đối chứng NaOH:** Ảnh SEM sẽ xuất hiện tình trạng thành vách vỡ vụn, sợi co cụm đặc khít do hiện tượng sập cấu trúc bị ăn mòn bởi ion $Na^+$ ở nhiệt độ cao (Na-etching). Điều này giải thích trực quan diện tích bề mặt thấp và độ truyền tải ion kém của mẫu NaOH.

### 1.2 Kính hiển vi điện tử truyền qua độ phân giải cao (TEM / HR-TEM)
*   **Mục tiêu ghi nhận:** Xác định cấu trúc mạng graphite sp² và mức độ phân tán của hạt sắt (Fe).
*   **Tiêu chuẩn đạt chuẩn (Pass Criteria):**
    *   Ảnh TEM của Fe/N-CA phải thể hiện các lá carbon mỏng dạng graphene bán tinh thể xếp chồng lên nhau ở viền rìa (graphitization).
    *   **Độ phân tán của Fe:** Đối với mẫu single-atom tối ưu, trên ảnh TEM **không được xuất hiện** bất kỳ hạt cụm sắt kim loại hoặc hạt sắt carbide tinh thể lớn dạng chấm đen thô (kích thước $> 5\text{ nm}$). Fe phải tồn tại dưới dạng các chấm sáng đơn phân tán cực kỳ nhỏ ($< 1\text{ nm}$) liên kết với mạng nitơ (quan sát rõ nhất qua ảnh HAADF-STEM).
    *   *Lỗi thường gặp:* Xuất hiện các hạt nano Fe/Fe₃C tinh thể lớn đục ngầu $\rightarrow$ Chứng tỏ quá trình tẩm sắt bị tập tụ hạt hoặc quá trình acid leaching bằng HCl 0.5M đun nóng chưa rửa trôi sạch các pha kim loại tự do.

---

## 2. PHÂN TÍCH DIỆN TÍCH BỀ MẶT XỐP (BET & BJH)

*Kỹ thuật hấp phụ - khử hấp phụ khí Nitơ ở nhiệt độ 77 K.*

### 2.1 Các chỉ số mục tiêu bắt buộc đối với Điện hóa cảm biến

| Chỉ số đặc trưng | Ký hiệu | Giá trị tiêu chuẩn (Hệ NH₃) | Vai trò trong ứng dụng cảm biến điện hóa |
| :--- | :---: | :---: | :--- |
| **Diện tích bề mặt cụ thể** | $S_{BET}$ | **$> 3000\text{ m}^2/\text{g}$** | Cung cấp diện tích tiếp xúc khổng lồ để neo giữ mật độ cực cao các active sites $Fe-N_x$ đơn nguyên tử, tránh thiêu kết vón cục. |
| **Thể tích lỗ xốp mesopore** | $V_{pore}$ | **$> 3.0\text{ cm}^3/\text{g}$** | Tạo đường truyền dẫn ion kiềm và đệm cực kỳ thông thoáng, tăng tốc độ phản ứng điện cực. |
| **Đường kính lỗ xốp trung bình** | $D_{pore}$ | **2.0 – 50.0 nm** | Phù hợp đường kính solvat hóa của ion kim loại nặng ($Pb^{2+}$) và dược chất (Paracetamol), giảm thiểu trở lực mao quản. |

### 2.2 Dạng đường cong đẳng nhiệt (Isotherm Curves)
*   Đường cong hấp phụ phải thuộc **Loại IV (Type IV)** theo phân loại IUPAC, xuất hiện vòng lặp trễ (hysteresis loop) dạng H3 hoặc H4 trong khoảng áp suất tương đối $P/P_0 = 0.4 - 0.9$. Điều này xác nhận sự tồn tại ưu thế của cấu trúc lỗ xốp trung bình (mesopores) liên thông.

---

## 3. PHÂN TÍCH CẤU TRÚC CARBON (Raman & XRD)

### 3.1 Phổ tán xạ Raman (Raman Spectroscopy)
*   **D-band** ($\approx 1340\text{ cm}^{-1}$): Đại diện cho các khuyết tật mạng carbon, carbon vô định hình hoặc liên kết carbon lai hóa sp³ ($C-N$ hoặc $C-O$).
*   **G-band** ($\approx 1579\text{ cm}^{-1}$): Đại diện cho dao động kéo giãn của liên kết sp² carbon dạng vòng graphite tinh thể phẳng dẫn điện.
*   **Tỷ lệ cường độ đỉnh phổ ($I_D/I_G$):**
    *   **Giá trị mục tiêu:** **$0.9 - 1.2$**.
    *   *Ý nghĩa biện luận:* Tỷ lệ $I_D/I_G$ nằm trong dải vàng này chứng minh vật liệu có cấu trúc carbon sp² dẫn điện tốt (từ G-band) nhưng đồng thời sở hữu lượng **khuyết tật mạng vừa đủ (từ D-band)**. Các điểm khuyết tật mạng chính là vị trí các nguyên tử nitơ thế vào khung carbon tạo active sites $Fe-N_x$. Tỷ lệ này giảm nhẹ sau khi annealing lần 2 do mạng graphite sp² được phục hồi một phần độ tinh thể.

### 3.2 Nhiễu xạ tia X (XRD)
*   **Đỉnh phổ carbon:** Xuất hiện hai đỉnh phổ nhiễu xạ góc tù, rộng tại **$2\theta \approx 26^\circ$** (tương ứng mặt mạng (002)) và **$43^\circ$** (tương ứng mặt mạng (100) của carbon vô định hình/bán tinh thể).
*   **Đỉnh phổ pha sắt:** **Tuyệt đối không** được xuất hiện các đỉnh nhiễu xạ sắc nhọn của sắt kim loại $\alpha-Fe$ ($2\theta \approx 44.7^\circ$) hoặc sắt carbide $Fe_3C$ ($2\theta \approx 43.9^\circ$). Sự biến mất của các đỉnh phổ này chứng minh sắt tồn tại dạng đơn nguyên tử phối trí (single-atom) phân tán hoàn toàn, không kết tinh thành pha tinh thể thô.

---

## 4. PHÂN TÍCH THÀNH PHẦN HÓA HỌC BỀ MẶT (XPS)

*Đây là kỹ thuật định lượng và định danh hóa học quan trọng nhất để chứng minh sự hình thành liên kết phối trí Fe-Nx.*

### 4.1 Hàm lượng nguyên tố bề mặt (XPS Survey)
*   **Nitơ tổng số (N at%):** **3.0 – 6.0 at%** (Dưới 3.0% độ nhạy cảm biến sẽ yếu; trên 6.0% mạng carbon bị phá hủy cấu trúc dẫn điện).
*   **Sắt tổng số (Fe at%):** **0.4 – 1.5 at%** (Hàm lượng tối ưu cho xúc tác đơn nguyên tử).
*   **Tỷ lệ nguyên tố N : Fe:** **$\ge 4 : 1$** (Đảm bảo đủ nitơ để phối trí bọc quanh 1 nguyên tử sắt tạo cấu trúc $Fe-N_4$ ổn định).

### 4.2 Phân tích phổ N 1s phân giải cao (High-Resolution N 1s Deconvolution)
Tiến hành tách peak phổ N 1s thành 4 dạng liên kết nitơ đặc trưng:
1.  **Pyridinic-N ($\approx 398.2\text{ eV}$):**
    *   *Ý nghĩa biện luận:* **Đây là dạng nitơ quan trọng nhất đối với cảm biến**. Cặp electron tự do của Pyridinic-N có ái lực cực mạnh, tạo liên kết phối trí hiến-nhận bền vững với ion sắt $Fe^{3+}/Fe^{2+}$ để tạo thành tâm hoạt tính **$Fe-N_4$**. Bạn cần viết biện luận chứng minh diện tích peak Pyridinic-N chiếm tỷ lệ ưu thế trong phổ phân tích.
2.  **Pyrrolic-N ($\approx 400.1\text{ eV}$):** Nguyên tử N nằm trong vòng năm cạnh carbon, cũng có thể phối trí một phần với sắt tạo cấu trúc $Fe-N_x$.
3.  **Graphitic-N ($\approx 401.3\text{ eV}$):** Nguyên tử N thế vị trí của nguyên tử carbon bên trong mạng sp² phẳng phẳng. Giúp tăng mật độ hạt mang điện và độ dẫn điện tổng thể cho màng carbon.
4.  **Oxidized-N ($\approx 403.0\text{ eV}$):** Các liên kết nitơ bị oxy hóa ($N-O_x$), ít hoạt tính xúc tác.

### 4.3 Phân tích phổ Fe 2p phân giải cao (High-Resolution Fe 2p)
*   Phổ Fe 2p phân tách thành hai đỉnh spin-orbit chính: **Fe 2p₃/₂** ($\approx 711.0\text{ eV}$) và **Fe 2p₁/₂** ($\approx 724.0\text{ eV}$).
*   **Liên kết $Fe-N_x$:** Xuất hiện đỉnh phổ đóng góp đặc trưng ở **$710.8\text{ eV} - 711.5\text{ eV}$** chứng minh nguyên tử sắt đã liên kết thành công với Nitơ, khác biệt hoàn toàn với peak của Fe kim loại ($707.0\text{ eV}$) hay Fe oxit tự do.
