# Quy định định dạng Đề cương Luận văn Carbon Aerogel (N-CA & Fe/N-CA)

Tài liệu này lưu trữ các quy tắc định dạng được thiết lập và chuẩn hóa cho đề cương luận văn thạc sĩ ngành Hóa phân tích của học viên **Lê Hoàng Nhật**. Các mô hình AI và công cụ chuyển đổi sau này cần tuân thủ nghiêm ngặt các quy tắc này để đảm bảo tính nhất quán giữa file Word (`De_cuong_Luan_van_CA.docx`) và các file Markdown (`De_cuong_Luan_van_CA.md` / `_integrated.md`).

---

## 1. Quy tắc viết Chỉ số dưới (Subscript) và Chỉ số trên (Superscript)

Để đảm bảo tương thích tuyệt đối khi xuất từ Markdown sang MS Word để trình lên hội đồng, **tuyệt đối KHÔNG sử dụng định dạng LaTeX** (như `^{...}` hay `_{...}`) và **KHÔNG dùng các thẻ HTML** (như `<sub>`, `<sup>`).

Thay vào đó:
*   **Chỉ số dưới (Subscript) cho công thức hóa học:** Sử dụng các ký tự Unicode chỉ số dưới trực tiếp.
    *   *Ví dụ:* `H₂O`, `CO₂`, `Fe-N₄`, `Fe-Nₓ`
*   **Chỉ số dưới (Subscript) cho biến số:** Sử dụng cú pháp subscript của Pandoc Markdown (`~...~`) kết hợp in nghiêng biến chính. Tuyệt đối không để dấu gạch chân `_` trần.
    *   *Ví dụ:* `*I*~p~`, `*S*~BET~`, `*R*~ct~`
*   **Chỉ số trên (Superscript):** Sử dụng các ký tự Unicode chỉ số trên (² , ⁺, ⁻...).
    *   *Ví dụ:* `Pb²⁺`, `Cd²⁺`, `sp²`, `e⁻`
*   **Biến toán học:** Viết in nghiêng bằng dấu `*...*`.
    *   *Ví dụ:* `*R*² ≥ 0.999`

---

## 2. Quy tắc định dạng Biến số Toán học và Điện hóa

*   Các biến số toán học, điện hóa và vật lý phải được **in nghiêng biến chính** (dùng `*...*`), còn phần chỉ số dưới/chỉ số trên giữ nguyên chữ đứng thông qua cú pháp Pandoc `~...~`.
    *   *Ví dụ:* `*I*~p~`, `*R*~ct~`, `*S*~BET~`, `*A*~eff~`

*   **Phương trình Randles–Ševčík chuẩn hóa:**
    `*I*~p~ = (2.69 × 10⁵) · *n*³ᐟ² · *A*~eff~ · *D*¹ᐟ² · *C*~0~* · *v*¹ᐟ²`
    *(Trong đó thế các biến số được biểu diễn đồng bộ và đẹp mắt bằng cú pháp Pandoc).*

---

## 3. Loại bỏ ký tự LaTeX phức tạp (Thay bằng Unicode sạch)

Tránh sử dụng ký hiệu toán học dạng LaTeX phức tạp nằm trong dấu `$` đối với các ký hiệu phổ thông. Hãy sử dụng Unicode sạch trực tiếp để hiển thị tốt trên MS Word và Markdown:
*   Thay `$\beta$` bằng **β** (như trong β-D-glucopyranose)
*   Thay `$\gamma$` bằng **γ**
*   Thay `$\theta$` bằng **θ** (như trong góc tiếp xúc θ)
*   Thay `$\omega$` bằng **ω** (trở kháng)
*   Thay `$\alpha$` bằng **α**
*   Thay `$\le$`, `$\ge$` bằng **≤**, **≥**
*   Thay `$\approx$` bằng **≈**
*   Thay `$\rightleftharpoons$` bằng **⇌** (phản ứng thuận nghịch)
*   Thay `$\pm$` bằng **±**

---

## 4. Ràng buộc về nội dung Khoa học & Thực nghiệm

*   **Quy trình GĐ0 (Tiền xử lý kiềm hóa tách lignin từ xơ dừa):**
    Bột xơ dừa sau khi ngâm kiềm (NaOH 6 wt% ở 80 °C) **chỉ được rửa bằng nước cất DI ấm** đến pH trung tính. **Tuyệt đối không rửa bằng axit HCl** hay bất kỳ axit nào khác để tránh gây thủy phân sớm xenlulozo, làm hỏng cấu trúc khung polymer.
*   **Độ nhạy Paracetamol (Bảng 3.3):**
    Thế đỉnh pic oxy hóa của Paracetamol trên điện cực biến tính N-CA được thiết lập chính xác từ **`≈ +0.43 V đến +0.47 V vs. Ag/AgCl`** (thay vì mức +0.34 V của điện cực bare GCE).
*   **Đánh giá sai số (Mục 2.7):**
    Phép kiểm định so sánh kết quả đo cảm biến với phương pháp đối chứng (ICP-MS và HPLC-UV) bắt buộc phải sử dụng hai phép kiểm định thống kê: **<i>F</i>-test** (so sánh phương sai/độ chụm) và **<i>t</i>-test** (so sánh giá trị trung bình/độ đúng) ở độ tin cậy 95% (α = 0.05).

---

## 5. Cấu trúc Tiêu đề và Liên kết Hình ảnh

*   **Logic đánh số tiêu đề:**
    Toàn bộ tiêu đề trong Chương 2, Chương 3 và Chương 4 bắt buộc phải đánh số dạng phân cấp thập phân (ví dụ: `2.2.1`, `2.2.1.1` thay vì dạng La Mã `I.`, `1.`).
*   **Chèn hình ảnh:**
    Giữ nguyên các liên kết hình ảnh cục bộ dạng `![Mô tả hình ảnh](file:///D:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/1%20thesis%20CA/C.A/ref/...)` ngay dưới các tiêu đề hoặc đoạn văn mô tả tương ứng để đảm bảo trình đọc Markdown hiển thị chính xác.

---

## 6. Định dạng Cấu trúc (Heading), Ngắt trang và Đánh số trang

Để quá trình xuất từ Markdown sang MS Word diễn ra hoàn hảo và giảm thiểu thao tác chỉnh sửa thủ công, cần tuân thủ:

*   **Định dạng Tiêu đề (Headings):** Bắt buộc tuân thủ số lượng dấu `#` tương ứng chính xác với các cấp độ Heading trong Word.
    *   `#` (Heading 1): Dành riêng cho Tên Chương (VD: CHƯƠNG 1, CHƯƠNG 2).
    *   `##` (Heading 2): Dành cho Mục lớn (VD: 1.1, 2.1).
    *   `###` (Heading 3) và `####` (Heading 4): Dành cho Tiểu mục chi tiết (VD: 1.1.1, 1.1.1.1).
*   **Sang trang mới (Page Break) & Ngắt khu vực (Section Break):** 
    *   Để ép ngắt trang khi sang Chương mới, chèn thẻ HTML: `<div style="page-break-before: always;"></div>`
    *   **Section Break:** Thường dùng khi cần đổi định dạng số trang (từ La Mã sang Arab) hoặc **xoay ngang trang giấy (Landscape)** cho các bảng siêu rộng. Việc chèn Section Break phức tạp thường không được Markdown hỗ trợ hoàn hảo; do đó phải xử lý bằng cách cấu hình Template Word hoặc chèn Section break thủ công trên Word.
*   **Định dạng Bảng biểu (Tables) & Màu nền:** 
    *   Sử dụng cú pháp Markdown chuẩn (cột ngăn cách bằng `|`). 
    *   Đặc biệt quan trọng: Các bảng biểu khi xuất sang Word phải đảm bảo định dạng chuyên chuẩn hàn lâm với **màu nền trắng hoàn toàn (không tô màu nền xen kẽ các hàng hay màu sắc sặc sỡ)**. Template Word cần được set mặc định kiểu bảng là *Plain Table* hoặc *Grid Table* (có viền đen đơn giản).
    *   Không làm bảng quá nhiều cột để tránh bị tràn khổ giấy A4 theo chiều dọc.
*   **Tiêu đề Hình ảnh & Bảng biểu (Captions):** 
    *   **Tên Hình** đặt ở **DƯỚI** hình ảnh (Ví dụ: *Hình 1.1. Sơ đồ...*).
    *   **Tên Bảng** đặt ở **TRÊN** bảng biểu (Ví dụ: *Bảng 2.1. Cân bằng khối lượng...*).
    *   Tuân thủ định dạng chữ đậm ở cụm "Hình/Bảng" và chữ thường/in nghiêng ở phần mô tả (theo đúng quy chuẩn của Bộ Giáo dục / trường Đại học).
*   **Căn lề (Alignment), Giãn dòng & Đánh số thứ tự trang:** 
    Ngôn ngữ Markdown không can thiệp cứng vào layout giấy. Do đó, toàn bộ việc căn lề văn bản (Justify - canh đều 2 bên), giãn dòng (Line spacing 1.3 - 1.5), lề giấy (Trái 3cm, Phải/Trên/Dưới 2cm) và đánh số trang tự động sẽ được **kế thừa 100% từ file MS Word Template (Reference docx)** khi xuất qua Pandoc. Tuyệt đối không cố gắng hardcode (code cứng) Header/Footer hay dùng HTML ép lề trong file Markdown.

---

## 7. Mục lục tự động (Table of Contents)

*   **Nguyên tắc:** Mục lục **KHÔNG được viết tay** (hardcode) vào file Markdown. Thay vào đó, đặt một placeholder hướng dẫn tại vị trí `# MỤC LỤC` trong file MD.
*   **Cơ chế hoạt động:** Khi xuất MD sang Word, toàn bộ các heading `#` (Heading 1), `##` (Heading 2), `###` (Heading 3), `####` (Heading 4) sẽ được Word nhận diện tự động. Sau đó trên Word:
    1.  Đặt con trỏ vào vị trí Mục lục.
    2.  Vào tab **References** → **Table of Contents** → chọn kiểu hiển thị.
    3.  Word sẽ tự động quét toàn bộ Heading và sinh ra Mục lục có số trang chính xác.
    4.  Sau mỗi lần chỉnh sửa nội dung, nhấn **Ctrl + A** rồi **F9** để cập nhật lại số trang trong Mục lục.
*   **Lưu ý:** Tương tự, **Danh mục Bảng biểu** và **Danh mục Hình ảnh** cũng nên được tạo tự động trên Word bằng tính năng **Insert > Table of Figures** (yêu cầu các Caption Hình/Bảng đã được chèn đúng bằng Insert Caption trong Word).

---

## 8. Quy tắc Xử lý và Biên dịch Tự động (Hậu xử lý python-docx)

Khi biên dịch từ file Markdown (`.md`) sang Word (`.docx`) qua Pandoc, cần áp dụng script Python hậu xử lý để tự động hóa định dạng mà không ảnh hưởng tới nội dung:

*   **Sao chép nguyên bản Trang bìa (Cover Page):** 
    Để bảo toàn 100% định dạng, vị trí tab thông tin học viên, font chữ tiêu đề lớn và hình ảnh logo trường, script Python phải tự động cắt bỏ phần trang bìa được sinh ra từ Markdown (mọi dòng trước `LỜI CAM ĐOAN`) và chép đè nguyên mẫu toàn bộ các Paragraphs (kèm Runs, font, align, size) từ trang bìa của file gốc `De_cuong_Luan_van_CA.docx`.
*   **Phân biệt Tiêu đề và Văn bản tham chiếu:** 
    Để tránh căn lề giữa nhầm các câu tham chiếu (như *"Hình 2.5 minh họa..."*), chỉ được nhận dạng tiêu đề thực tế bằng biểu thức chính quy (Regex):
    `re.match(r'^(Hình|Bảng)\s+\d+\.\d+(\s*[\.\:—\-–]|\s*$)', text)`
    *   **Tiêu đề Hình ảnh** (Hình X.Y.): Đặt ở dưới hình, căn lề giữa (**CENTER**).
    *   **Tiêu đề Bảng biểu** (Bảng X.Y.): Đặt ở trên bảng, căn lề trái (**LEFT**).
    *   **Danh mục Hình ảnh/Bảng biểu** (ở front-matter): Căn lề trái (**LEFT**).
*   **Cỡ chữ trong Bảng biểu:** 
    Để đáp ứng quy chuẩn trình bày, toàn bộ chữ bên trong tất cả các ô của bảng biểu phải được đặt đồng bộ ở kích thước **13pt** và font **Times New Roman**.
*   **Định dạng thụt đầu dòng (Indents) và giãn cách dòng:** 
    Các đoạn văn bình thường trong thân bài được căn đều 2 bên (**JUSTIFY**), giãn dòng **1.5 line** và khoảng cách sau đoạn **6pt** (space after). Các tiêu đề hình/bảng (Captions) được giữ nguyên khoảng cách dòng mặc định để tránh mất thẩm mỹ.


