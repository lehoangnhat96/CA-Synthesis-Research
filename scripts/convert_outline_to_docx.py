# -*- coding: utf-8 -*-
import os
import sys
import re
from pathlib import Path

# Thử import thư viện docx
try:
    import docx
    from docx import Document
    from docx.shared import Inches, Pt, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml.ns import qn, nsdecls
    from docx.oxml import parse_xml, OxmlElement
except ImportError:
    print("LỖI: Chưa cài đặt 'python-docx'. Vui lòng chạy 'pip install python-docx'")
    sys.exit(1)

# Thiết lập UTF-8 cho console để tránh lỗi mã hóa trên Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def make_long_path(path):
    """Bỏ qua giới hạn MAX_PATH (260 ký tự) trên Windows."""
    abs_path = os.path.abspath(path)
    if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
        abs_path = abs_path.replace('/', '\\')
        return '\\\\?\\' + abs_path
    return abs_path

def normalize_for_relpath(path_val):
    """Bỏ tiền tố \\\\?\\ để xử lý tệp tin chính xác trên Windows."""
    path_str = str(path_val)
    if path_str.startswith('\\\\?\\'):
        return path_str[4:]
    return path_str

def parse_bold_text(paragraph, text, is_italic=False, font_size_pt=11, font_color_rgb=None):
    """
    Hàm phân tích cú pháp **in đậm** trong Markdown và thêm các Run tương ứng vào Paragraph.
    Giúp hiển thị chữ in đậm chính xác trong Word.
    """
    parts = text.split('**')
    for idx, part in enumerate(parts):
        if not part:
            continue
        run = paragraph.add_run(part)
        run.font.name = "Times New Roman"
        run.font.size = Pt(font_size_pt)
        if idx % 2 != 0:
            run.bold = True
        if is_italic:
            run.font.italic = True
        if font_color_rgb:
            run.font.color.rgb = font_color_rgb

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Đặt khoảng đệm (padding/margins) cho ô trong bảng để bảng thoáng và dễ đọc hơn."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def main():
    workspace_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent
    md_file = workspace_dir / "Quy trình AI" / "new" / "synthesis_outline_verified.md"
    docx_file = workspace_dir / "Quy trình AI" / "new" / "synthesis_outline_verified.docx"
    
    if not os.path.exists(make_long_path(md_file)):
        print(f"LỖI: Không tìm thấy tệp {md_file.name}")
        sys.exit(1)
        
    print(f"=== Bắt đầu chuyển đổi {md_file.name} sang file Word ===")
    
    with open(make_long_path(md_file), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    doc = Document()
    
    # Cấu hình Margins khổ A4 chuẩn học thuật (2.0 cm)
    for section in doc.sections:
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.0)
        section.right_margin = Cm(2.0)
        
    # Kiểu chữ mặc định
    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)
    style.paragraph_format.space_after = Pt(6)
    style.paragraph_format.line_spacing = 1.15
    
    # Kiểu chữ Heading 1, 2, 3
    for level in range(1, 4):
        hs = doc.styles[f"Heading {level}"]
        hs.font.name = "Times New Roman"
        hs.font.bold = True
        hs.font.color.rgb = RGBColor(0, 51, 102)
        if level == 1:
            hs.font.size = Pt(16)
        elif level == 2:
            hs.font.size = Pt(13)
        else:
            hs.font.size = Pt(12)
            
    in_table = False
    table_headers = []
    table_rows = []
    
    for line in lines:
        stripped = line.strip()
        
        # Bỏ qua các đường kẻ phân cách bảng của Markdown
        if stripped.startswith('|') and ('---' in stripped or ':---' in stripped):
            continue
            
        # 1. Phát hiện và xử lý Bảng
        if stripped.startswith('|') and stripped.endswith('|'):
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if not in_table:
                table_headers = cells
                in_table = True
            else:
                table_rows.append(cells)
            continue
        else:
            # Ghi bảng đã tích lũy trước khi xử lý phần văn bản khác
            if in_table:
                cols_count = len(table_headers)
                print(f"Đang tạo bảng Word có {cols_count} cột, {len(table_rows)} dòng...")
                table = doc.add_table(rows=1 + len(table_rows), cols=cols_count)
                table.style = "Table Grid"
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                
                # Tính toán độ rộng cột tự động dựa trên số cột
                # Khổ rộng in khả dụng là khoảng 17cm (21cm A4 - 4cm margins)
                if cols_count == 3:
                    col_widths = [3.5, 6.0, 7.5]
                elif cols_count == 4:
                    col_widths = [2.5, 4.5, 4.5, 5.5]
                elif cols_count == 5:
                    col_widths = [1.2, 5.5, 4.5, 2.9, 2.9]
                else:
                    col_widths = [17.0 / cols_count] * cols_count
                    
                # Ghi tiêu đề bảng (Deep Blue, White Text, Bold)
                for col_idx, h_text in enumerate(table_headers):
                    cell = table.rows[0].cells[col_idx]
                    cell.text = ""
                    p = cell.paragraphs[0]
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p.paragraph_format.space_before = Pt(4)
                    p.paragraph_format.space_after = Pt(4)
                    
                    run = p.add_run(h_text)
                    run.bold = True
                    run.font.name = "Times New Roman"
                    run.font.size = Pt(10)
                    run.font.color.rgb = RGBColor(255, 255, 255)
                    
                    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="003366"/>')
                    cell._tc.get_or_add_tcPr().append(shading)
                    set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
                    
                # Ghi dữ liệu bảng
                for r_idx, row_data in enumerate(table_rows):
                    row = table.rows[r_idx + 1]
                    for c_idx, cell_data in enumerate(row_data):
                        # Đề phòng trường hợp dòng thiếu cột
                        if c_idx >= cols_count:
                            break
                        cell = row.cells[c_idx]
                        cell.text = ""
                        p = cell.paragraphs[0]
                        p.paragraph_format.space_before = Pt(3)
                        p.paragraph_format.space_after = Pt(3)
                        
                        # Căn lề
                        if c_idx == 0 and len(cell_data) < 5:
                            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        elif cols_count >= 4 and c_idx in [cols_count-2, cols_count-1] and len(cell_data) < 8:
                            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        else:
                            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                            
                        # Parse in đậm bên trong ô của bảng
                        parse_bold_text(p, cell_data, font_size_pt=9.5)
                        
                        # Màu nền xen kẽ (Zebra Striping)
                        if r_idx % 2 == 0:
                            shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F4F8FE"/>')
                            cell._tc.get_or_add_tcPr().append(shading)
                            
                        set_cell_margins(cell, top=80, bottom=80, left=150, right=150)
                        
                # Cập nhật độ rộng các cột
                for r in table.rows:
                    for c_idx, w in enumerate(col_widths):
                        if c_idx < len(r.cells):
                            r.cells[c_idx].width = Cm(w)
                            
                doc.add_paragraph() # Ngăn cách sau bảng
                
                # Reset trạng thái bảng
                in_table = False
                table_headers = []
                table_rows = []
                
        # 2. Xử lý các văn bản Markdown thông thường
        if stripped.startswith('# '):
            h_text = stripped[2:].strip()
            doc.add_heading(h_text, level=1)
        elif stripped.startswith('## '):
            h_text = stripped[3:].strip()
            doc.add_heading(h_text, level=2)
        elif stripped.startswith('### '):
            h_text = stripped[4:].strip()
            doc.add_heading(h_text, level=3)
        elif stripped.startswith('>'):
            # Xử lý các Callout blocks như > [!NOTE], > [!WARNING]...
            clean_line = stripped.replace('> [!NOTE]', '').replace('> [!IMPORTANT]', '').replace('> [!WARNING]', '').replace('> [!TIP]', '').replace('> [!CAUTION]', '').replace('>', '').strip()
            if clean_line:
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Cm(1.27) # Thụt lề blockquote
                
                # Đặt màu chữ cam đất/đỏ cho các cảnh báo quan trọng, hoặc màu xanh đậm cho note
                is_warning = ('[!IMPORTANT]' in stripped) or ('[!WARNING]' in stripped) or ('[!CAUTION]' in stripped)
                is_tip = '[!TIP]' in stripped
                
                color = RGBColor(160, 50, 0) if is_warning else (RGBColor(0, 100, 50) if is_tip else RGBColor(80, 80, 80))
                
                # Tiền tố nhãn
                if '[!IMPORTANT]' in stripped or '[!WARNING]' in stripped or '[!CAUTION]' in stripped:
                    run_pref = p.add_run("[!] CHÚ Ý: ")
                    run_pref.bold = True
                    run_pref.font.name = "Times New Roman"
                    run_pref.font.size = Pt(10.5)
                    run_pref.font.color.rgb = color
                elif '[!TIP]' in stripped:
                    run_pref = p.add_run("[*] GỢI Ý/MẸO: ")
                    run_pref.bold = True
                    run_pref.font.name = "Times New Roman"
                    run_pref.font.size = Pt(10.5)
                    run_pref.font.color.rgb = color
                elif '[!NOTE]' in stripped:
                    run_pref = p.add_run("[i] LƯU Ý: ")
                    run_pref.bold = True
                    run_pref.font.name = "Times New Roman"
                    run_pref.font.size = Pt(10.5)
                    run_pref.font.color.rgb = color
                    
                parse_bold_text(p, clean_line, is_italic=True, font_size_pt=10.5, font_color_rgb=color)
        elif stripped.startswith('- ') or stripped.startswith('* '):
            # Điểm danh sách tròn (Bullet List)
            clean_line = stripped[2:].strip()
            p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.left_indent = Cm(1.0)
            parse_bold_text(p, clean_line, font_size_pt=11)
        elif stripped == '---':
            # Ngắt trang hoặc phân cách (Ở đây dùng ngắt trang cho các phần lớn)
            # Nếu gặp phân cách giữa các Giai đoạn, thực hiện ngắt trang để in ấn đẹp mắt
            pass
        elif stripped:
            # Đoạn văn bản thông thường
            p = doc.add_paragraph()
            parse_bold_text(p, stripped, font_size_pt=11.5)
            
    # Ghi file Word kết quả
    long_output = make_long_path(docx_file)
    doc.save(long_output)
    print(f"=== ĐÃ TẠO FILE WORD THÀNH CÔNG TẠI: {docx_file.name} ===")

if __name__ == "__main__":
    main()
