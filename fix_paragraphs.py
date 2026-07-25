from docx import Document

docx_path = "D:/1 Master's Ana Chem/1 Master's thesis/Carbon Aerogel/Thesi grad/DCLV_CA_02.07 Fe-N CA_Renumbered.docx"
doc = Document(docx_path)

p1_found = False
p2_found = False

for p in doc.paragraphs:
    if "Thuyết Kén phân tử (Inclusion Complex Theory) được mô tả bởi Cai" in p.text or "Thuyết Kén phân tử" in p.text:
        p.text = "Thuyết Kén phân tử (Inclusion Complex Theory) được xây dựng bởi nhóm GS. Lina Zhang: cơ chế hòa tan được mô tả qua hành vi gel hóa đặc biệt của cellulose trong hệ kiềm/urea [6], trong đó Urea đóng vai trò tạo lớp vỏ bảo vệ quanh chuỗi cellulose thông qua tương tác van der Waals và liên kết hydro — điều được xác nhận trực tiếp bằng kỹ thuật NMR bởi Xiong và cộng sự [52]. Cơ chế này được giả định tương tự cho hệ dung môi amoniac/urea/nước được sử dụng trong đề tài [17, 41], trong đó cellulose hòa tan theo cơ chế phối trí đa thành phần ở nhiệt độ lạnh."
        p1_found = True
        
    if "Quá trình hòa tan là phản ứng tỏa nhiệt (ΔH < 0)" in p.text or "phản ứng tỏa nhiệt" in p.text:
        p.text = "Quá trình hòa tan là phản ứng tỏa nhiệt (ΔH < 0) và giảm entropy (ΔS < 0) — được Cai và Zhang xác nhận bằng phân tích nhiệt lượng quét vi sai (DSC) [53] — do đó sol chỉ ổn định và đồng nhất ở nhiệt độ ≤ 10°C (tối ưu 0 - 5°C)."
        p2_found = True

doc.save(docx_path)
print(f"P1 found: {p1_found}, P2 found: {p2_found}")
