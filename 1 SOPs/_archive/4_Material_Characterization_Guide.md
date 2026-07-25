# 4_Material_Characterization_Guide.md — Cẩm Nang Phân Tích Đặc Trưng & Tiêu Chuẩn Kỹ Thuật Vật Liệu

> [!NOTE]
> * Quy trình liên hợp thực tế: `1_Active_Protocol_Synthesis.md`, `2_Active_Protocol_Electrochemistry.md`, `3_Literature_Review_and_Gap_Analysis.md`

---

## 1. TIÊU CHUẨN ĐẶC TRƯNG HÌNH THÁI VÀ CẤU TRÚC VẬT LÝ (SEM & TEM)

*   **Kính hiển vi điện tử quét (SEM):**
    *   **✓ Pass:** Màng carbon aerogel thể hiện rõ cấu trúc dạng tổ ong phân cấp liên thông (hierarchical honeycomb). Đạt đường kính macropores trung bình **10 - 100 µm**. Thành vách carbon mỏng, phẳng mịn và không bị sụp đổ.
    *   **✗ Fail:** Thành vách vỡ vụn, các sợi carbon bị co cụm đặc khít và sụp đổ cấu trúc (mẫu đối chứng NaOH-Urea do hiệu ứng Na-etching).
*   **Kính hiển vi điện tử truyền qua độ phân giải cao (TEM / HR-TEM):**
    *   **✓ Pass:** Bột Fe/N-CA sau annealing lần 2 thể hiện các lá carbon siêu mỏng dạng graphene bán tinh thể xếp chồng ngẫu nhiên ở viền rìa (graphitization). **Tuyệt đối không** xuất hiện hạt cụm sắt kim loại hoặc sắt carbide (Fe₃C) tinh thể thô (kích thước hạt > 5nm). Fe phân tán dạng đơn nguyên tử (single-atom) với các chấm sáng **< 1 nm**.
    *   **✗ Fail:** Xuất hiện các hạt/cụm đen đục kích thước lớn 10–50 nm (quá trình rửa axit đun hồi lưu chưa sạch sắt tự do thô).

---

## 2. TIÊU CHUẨN ĐẶC TRƯNG DIỆN TÍCH BỀ MẶT XỐP HẤP PHỤ (BET & BJH)

*   **Dạng đường đẳng nhiệt (Isotherm Curves):**
    *   **✓ Pass:** Đường đẳng nhiệt hấp phụ - khử hấp phụ khí Nitơ ở 77K bắt buộc thuộc **Loại IV (Type IV Isotherm)** theo phân loại IUPAC. Xuất hiện vòng lặp trễ (hysteresis loop) dạng H3 hoặc H4 rõ rệt trong vùng áp suất tương đối P/P₀ = 0.4 - 0.9 (khẳng định ưu thế của mesopores).
    *   **✗ Fail:** Không có vòng lặp trễ rõ nét, đường cong dẹt phẳng lỳ (sập cấu trúc lỗ xốp trung bình).
*   **Chỉ số định lượng tối ưu (Mẫu NH₄OH-Urea):**

| Thông số đo đạc | Ký hiệu | Giá trị tiêu chuẩn đạt chuẩn (Pass Criteria) | Trạng thái lỗi (Fail Criteria) |
| :--- | :---: | :---: | :--- |
| **Diện tích bề mặt riêng** | S_BET | **≥ 3700 m²/g** | *S*_BET < 1000m²/g (mẫu NaOH sụt giảm về 150m²/g). |
| **Thể tích lỗ xốp mao quản** | V_pore | **≥ 4.0 cm³/g** | *V*_pore < 1.0cm³/g. |
| **Đường kính lỗ xốp TB** | D_pore | **2.0 - 50.0nm** (mesopores) | Tập trung lỗ xốp thô kích thước lớn > 100nm (Fail). |

---

## 3. TIÊU CHUẨN PHA TINH THỂ VÀ THẾ MẠNG CARBON (Raman & XRD)

*   **Phổ tán xạ Raman (Defect Chemistry):**
    *   **✓ Pass:** Tỷ số cường độ hai đỉnh phổ ***I*_D / *I*_G = 0.9 - 1.2** (D-band tại ≈ 1340 cm⁻¹ đại diện cho khuyết tật mạng; G-band tại ≈ 1579 cm⁻¹ đại diện cho carbon graphit hóa phẳng dẫn điện).
    *   **✗ Fail:** Tỷ số *I*_D / *I*_G < 0.6 (quá ít khuyết tật để thế Nitơ) hoặc > 1.5 (mạng carbon bị phá hủy hoàn toàn không dẫn điện).
*   **Nhiễu xạ tia X (XRD):**
    *   **✓ Pass:** Chỉ xuất hiện hai đỉnh nhiễu xạ rộng, tù góc đặc trưng của carbon bán tinh thể tại góc quét **2θ ≈ 26.4^o** (002) và **43.5^o** (100). **Biến mất hoàn toàn** các đỉnh phổ của sắt kim loại α-Fe (2θ ≈ 44.7^o) và sắt carbide Fe₃C (2θ ≈ 43.9^o).
    *   **✗ Fail:** Xuất hiện bất kỳ đỉnh nhiễu xạ sắc nhọn nào của pha sắt thô hoặc sắt carbide (rửa axit và annealing lần 2 thất bại).

---

## 4. TIÊU CHUẨN THÀNH PHẦN HÓA HỌC BỀ MẶT (XPS)

*   **Hàm lượng nguyên tố bề mặt (XPS Survey):**
    *   **✓ Pass:** Hàm lượng Nitơ tổng (N 1s) phải nằm trong dải **3.0 - 6.0 at%**. Hàm lượng Sắt tổng (Fe 2p) nằm trong dải **0.4 - 1.5 at%**. Tỷ lệ nguyên tử **N:Fe ≥ 4:1** (đảm bảo đủ phối trí Fe-N₄).
    *   **✗ Fail:** Nitơ < 2.0 at% hoặc Sắt > 2.0 at% (hoặc tỉ lệ phối trí N:Fe < 3:1).
*   **Phân tách phổ N 1s phân giải cao (High-Resolution N 1s):**
    *   **✓ Pass:** Đỉnh phổ **Pyridinic-N** (≈ 398.2 eV) chiếm tỷ lệ diện tích ưu thế **≥ 45%** tổng phổ N 1s (đảm bảo tâm hoạt tính phối trí chelate mạnh bắt giữ kim loại Pb²⁺). Các dạng liên kết khác: Pyrrolic-N (≈ 400.1 eV), Graphitic-N (≈ 401.3 eV), Oxidized-N (≈ 403.0 eV).
    *   **✗ Fail:** Pyridinic-N chiếm < 25% diện tích tích phân peak.
*   **Phân tách phổ Fe 2p phân giải cao (High-Resolution Fe 2p):**
    *   **✓ Pass:** Phổ Fe 2p phân tách thành hai đỉnh chính: Fe 2p_3/2 (≈ 711.0 eV) và Fe 2p_1/2 (≈ 724.0 eV). Đỉnh đóng góp đặc trưng của liên kết **Fe-Nₓ** bắt buộc xuất hiện rõ nét trong dải **710.8 - 711.5 eV** (xác nhận thành công phối trí đơn nguyên tử).
    *   **✗ Fail:** Không phát hiện peak Fe-Nₓ, xuất hiện peak Fe kim loại tự do tại 707.0 eV.
