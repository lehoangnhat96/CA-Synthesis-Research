# Quy tắc dự án: Carbon Aerogel Master's Thesis

## Quy tắc an toàn khi làm việc với file Word (.docx)

> [!CAUTION]
> **TUYỆT ĐỐI KHÔNG dùng Pandoc để ghi đè (overwrite) lên một file `.docx` đã tồn tại.**
> Pandoc khi chuyển đổi từ `.md` sang `.docx` sẽ tạo ra một file Word mới hoàn toàn, xóa sạch toàn bộ định dạng, hình ảnh, bảng biểu, header/footer và kiểu chữ của file gốc. Đây là thao tác **phá hủy không thể khôi phục** nếu không có bản sao lưu.

### Phương pháp đúng khi cập nhật nội dung vào file Word gốc:

1. **Thay đổi nội dung văn bản (text) chỉ:**
   - Dùng kỹ thuật unzip-edit-zip: giải nén file `.docx` (thực chất là ZIP), sửa file `word/document.xml` bằng Python, rồi đóng gói lại.
   - Đây là phương pháp an toàn nhất để chỉ thay số trích dẫn hoặc sửa đoạn văn nhỏ mà không ảnh hưởng tới định dạng.

2. **Thêm nội dung lớn (tài liệu tham khảo, danh mục):**
   - Xuất nội dung mới ra file `.txt` riêng biệt.
   - Hướng dẫn người dùng copy-paste thủ công vào vị trí cần trong file Word.

3. **Khi người dùng yêu cầu "cập nhật file Word":**
   - LUÔN tạo bản sao lưu `*_backup_YYYY-MM-DD.docx` TRƯỚC KHI thực hiện bất kỳ thao tác nào.
   - Chỉ sửa đúng những gì được yêu cầu. Không thay đổi format, style, hoặc cấu trúc document ngoài yêu cầu.

## Quy tắc quản lý trích dẫn

- **KHÔNG dùng Pandoc** để ghi đè file `.docx` hiện có khi mục đích chỉ là cập nhật nội dung.
- Khi đánh số lại (renumber) trích dẫn: làm trên file `.md` trước → validate bằng `md-citation-validator` → áp dụng vào `.docx` bằng kỹ thuật XML an toàn.
- Script `md-citation-validator` phải dùng regex hỗ trợ cả dạng thoát ký tự `\[1\]` (do Pandoc sinh ra trong tiêu đề mục lục), tránh báo sai số.

## Quy tắc trích dẫn học thuật

- KHÔNG được tự bịa đặt Volume, Issue, Số trang, hoặc DOI.
- LUÔN dùng `search_web` hoặc đọc file thực tế để lấy metadata chính xác trước khi viết citation.

## Phạm vi dự án

- File luận văn chính: `DCLV_CA_02.07 Fe-N CA_Renumbered.docx`
- File Markdown chuẩn: `DCLV_CA_02.07 Fe-N CA_Renumbered.md`
- File bản sao bibliography gốc: `bib_raw.txt`


## Quy tắc xác nhận file trước khi thao tác

Trước BẤT KỲ thao tác đọc/ghi/sửa nào trên file, BẮT BUỘC phải:

1. **Xác nhận đúng file đích** — Nêu rõ tên đầy đủ (absolute path) của file sẽ được thao tác.
2. **Không tự mở file "gốc" khi người dùng chỉ định file "đã xử lý"** — Ví dụ: nếu người dùng nói làm trên `_Renumbered.docx`, thì không được mở `Fe-N CA.docx`.
3. **Không SaveAs sang file khác** — Chỉ ghi đè đúng file người dùng chỉ định (dùng `.save()` thay vì `.SaveAs()`).
4. **Không tạo file mới hoặc bản sao trung gian** nếu người dùng không yêu cầu.

Nếu không chắc file nào là đúng → **hỏi người dùng trước**, đừng tự đoán.

---

## Quy tắc hiệu quả thực thi (Anti-Inefficiency Rules)

> [!IMPORTANT]
> Các quy tắc này được đúc rút từ session thực tế. Vi phạm gây tốn token, mất thời gian người dùng và phải approve nhiều lần không cần thiết.

### Quy tắc 1 — Nguồn sự thật duy nhất (Single Source of Truth)
- **File Markdown `_Renumbered.md` luôn là nguồn sự thật duy nhất** cho nội dung, số trích dẫn và danh mục tài liệu.
- KHÔNG ĐỌC `bib_raw.txt`, không dùng file backup hay file phụ để xây dựng danh mục — chỉ đọc thẳng từ `.md`.
- Quy tắc này cũng áp dụng cho DOI: nếu trong `.md` đã có `doi:`, đó là DOI chính xác, không được ghi đè.

### Quy tắc 2 — Gộp thành 1 Script Duy nhất (Batch Execution)
- Toàn bộ quy trình của 1 tác vụ (đọc → xử lý → validate → ghi) phải được gộp thành **đúng 1 script Python duy nhất**.
- Tuyệt đối không viết nhiều script nhỏ lẻ kiểu test-từng-bước trong production. Mỗi script nhỏ = 1 lần Approve = tốn thời gian người dùng.
- Ngoại lệ duy nhất được phép: 1 script nhỏ để đọc cấu trúc file trước khi xử lý, nếu cần thiết.

### Quy tắc 3 — Kiểm tra trước khi ghi (Pre-flight Check)
Trước khi ghi vào DOCX, script phải tự kiểm tra bằng assert bên trong:
```python
assert len(final_lines) == 69, f"Expected 69 entries, got {len(final_lines)}"
assert all(f"[{i+1}]" in final_lines[i] for i in range(len(final_lines))), "Numbering mismatch!"
```
Nếu assert thất bại → script tự dừng, báo lỗi, KHÔNG ghi vào DOCX.

### Quy tắc 4 — Bảo toàn DOI gốc (Preserve Existing DOI)
- Khi search thêm DOI, luôn kiểm tra `'doi:' in line.lower()` trước.
- Nếu đã có DOI → bỏ qua, không search lại, không ghi đè.
- DOI được search từ Crossref API với ngưỡng score > 40 để chống bịa.

### Quy tắc 5 — Đánh số vùng Biblio (Range Detection)
- Khi tìm phạm vi danh mục, `start` là index của dòng heading (`TÀI LIỆU THAM KHẢO`).
- Các entry thực sự bắt đầu từ `start + 1`, không phải từ `start`.
- Luôn in ra số lượng entry thực tế để verify: `end - start - 1` phải bằng đúng 69 (hoặc số tài liệu hiện tại).

### Quy tắc 6 — Kiểm tra đầu ra bằng chính script (Self-Validate)
Sau khi ghi xong, script phải tự đọc lại và in ra kiểm tra:
```python
# Verify sau khi save
doc2 = Document(docx_path)
first = doc2.paragraphs[start2 + 1].text
last = doc2.paragraphs[end2 - 1].text
assert first.startswith('[1]'), f"First entry wrong: {first}"
assert last.startswith('[69]'), f"Last entry wrong: {last}"
print("✅ Verified OK")
```
