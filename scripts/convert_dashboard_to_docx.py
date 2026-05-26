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

def add_hyperlink(paragraph, url, text, color="003399", underline=True):
    """
    Thêm liên kết (hyperlink) có thể click trực tiếp trong Word (.docx).
    Sử dụng chèn XML cấp thấp của python-docx.
    """
    part = paragraph.part
    # Tạo mối quan hệ liên kết bên ngoài (External Relationship)
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

    # Tạo thẻ w:hyperlink
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('r:id'), r_id)

    # Tạo thẻ w:r (run)
    new_run = OxmlElement('w:r')

    # Định dạng run (màu sắc, gạch chân)
    rPr = OxmlElement('w:rPr')
    if color:
        c = OxmlElement('w:color')
        c.set(qn('w:val'), color)
        rPr.append(c)
    if underline:
        u = OxmlElement('w:u')
        u.set(qn('w:val'), 'single')
        rPr.append(u)
    
    # Định dạng font Times New Roman và cỡ chữ 10pt cho bảng
    f = OxmlElement('w:rFonts')
    f.set(qn('w:ascii'), 'Times New Roman')
    f.set(qn('w:hAnsi'), 'Times New Roman')
    rPr.append(f)
    
    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), '20') # 10pt = 20 half-points
    rPr.append(sz)

    new_run.append(rPr)
    
    # Gán text hiển thị
    text_node = OxmlElement('w:t')
    text_node.text = text
    new_run.append(text_node)
    
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)
    return hyperlink

def parse_markdown_link(cell_text):
    """Phân tách chuỗi Markdown link [Hiển thị](Đường dẫn) thành tuple (Text, Link)."""
    match = re.search(r'\[([^\]]+)\]\(([^)]+)\)', cell_text)
    if match:
        return match.group(1), match.group(2)
    return cell_text, None

def main():
    workspace_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent
    md_file = workspace_dir / "REF_MATERIALS_DASHBOARD.md"
    docx_file = workspace_dir / "REF_MATERIALS_DASHBOARD.docx"
    
    if not os.path.exists(make_long_path(md_file)):
        print(f"LỖI: Không tìm thấy tệp {md_file.name}. Hãy tạo file MD trước!")
        sys.exit(1)
        
    print(f"=== Bắt đầu chuyển đổi {md_file.name} sang {docx_file.name} ===")
    
    # Đọc nội dung Markdown
    with open(make_long_path(md_file), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    doc = Document()
    
    # Thiết lập định dạng trang (Page Margins)
    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.0)
        section.right_margin = Cm(2.0)
        
    # Thiết lập styles mặc định (Times New Roman, 12pt)
    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)
    style.paragraph_format.space_after = Pt(6)
    style.paragraph_format.line_spacing = 1.15
    
    # Thiết lập style tiêu đề Heading 1 & Heading 2
    for level in range(1, 3):
        hs = doc.styles[f"Heading {level}"]
        hs.font.name = "Times New Roman"
        hs.font.bold = True
        hs.font.color.rgb = RGBColor(0, 51, 102)
        if level == 1:
            hs.font.size = Pt(18)
        else:
            hs.font.size = Pt(14)
            
    # Bắt đầu đọc và xây dựng nội dung Word
    in_table = False
    table_headers = []
    table_rows = []
    
    for line in lines:
        stripped = line.strip()
        
        # Bỏ qua dòng trống phân cách bảng hoặc định nghĩa định dạng bảng Markdown (ví dụ: |---|---|)
        if stripped.startswith('|') and ('---' in stripped or ':---' in stripped):
            continue
            
        # Kiểm tra nếu là dòng bảng
        if stripped.startswith('|') and stripped.endswith('|'):
            # Phân tách các ô trong dòng
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            
            if not in_table:
                # Dòng đầu tiên là tiêu đề bảng
                table_headers = cells
                in_table = True
            else:
                table_rows.append(cells)
            continue
        else:
            # Nếu dòng không phải là bảng nhưng trước đó đang trong bảng -> Ghi bảng trước
            if in_table:
                # Xử lý và ghi bảng vào docx
                print(f"Đang tạo bảng Word với {len(table_rows)} tài liệu...")
                table = doc.add_table(rows=1 + len(table_rows), cols=5)
                table.style = "Table Grid"
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                
                # Chiều rộng các cột
                col_widths = [1.2, 8.5, 4.0, 2.3, 2.3] # Tổng cộng ~18.3 cm khít khổ giấy A4
                
                # 1. Ghi tiêu đề bảng (Deep Blue Header)
                for col_idx, h_text in enumerate(table_headers):
                    cell = table.rows[0].cells[col_idx]
                    cell.text = ""
                    p = cell.paragraphs[0]
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    run = p.add_run(h_text)
                    run.bold = True
                    run.font.size = Pt(10.5)
                    run.font.color.rgb = RGBColor(255, 255, 255)
                    
                    # Tô màu nền tiêu đề bảng
                    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="003366"/>')
                    cell._tc.get_or_add_tcPr().append(shading)
                    
                # 2. Ghi dữ liệu bảng
                for r_idx, row_data in enumerate(table_rows):
                    row = table.rows[r_idx + 1]
                    
                    for c_idx, cell_data in enumerate(row_data):
                        cell = row.cells[c_idx]
                        cell.text = ""
                        p = cell.paragraphs[0]
                        p.paragraph_format.space_after = Pt(2)
                        p.paragraph_format.space_before = Pt(2)
                        
                        # Căn lề
                        if c_idx == 0:
                            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        elif c_idx in [3, 4]:
                            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        else:
                            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                            
                        # Phân tích xem ô có chứa link Markdown hay không
                        text, link = parse_markdown_link(cell_data)
                        
                        if link:
                            # Nếu có link, chèn hyperlink
                            # Loại bỏ định dạng inline code `...` nếu có
                            clean_text = text.replace('`', '')
                            # Mã hóa liên kết phù hợp
                            encoded_link = link.replace(' ', '%20')
                            # Tạo đường dẫn tuyệt đối hoặc tương đối phù hợp (Word hỗ trợ link tương đối tốt)
                            add_hyperlink(p, encoded_link, clean_text)
                        else:
                            # Ô văn bản thường
                            clean_text = cell_data.replace('`', '')
                            run = p.add_run(clean_text)
                            run.font.size = Pt(9.5)
                            
                        # Tô màu xen kẽ cho các dòng (Zebra Striping)
                        if r_idx % 2 == 0:
                            shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F4F8FE"/>')
                            cell._tc.get_or_add_tcPr().append(shading)
                            
                # Thiết lập độ rộng cột
                for row in table.rows:
                    for idx, w in enumerate(col_widths):
                        row.cells[idx].width = Cm(w)
                        
                # Thêm paragraph trống ngăn cách sau bảng
                doc.add_paragraph()
                
                in_table = False
                table_headers = []
                table_rows = []
                
        # Xử lý các văn bản thông thường
        if stripped.startswith('# '):
            h_text = stripped[2:].strip()
            doc.add_heading(h_text, level=1)
        elif stripped.startswith('## '):
            h_text = stripped[3:].strip()
            doc.add_heading(h_text, level=2)
        elif stripped.startswith('>') or stripped.startswith('*'):
            # Điểm danh sách hoặc note
            clean_line = stripped.replace('> [!NOTE]', '').replace('>', '').strip()
            if clean_line:
                if clean_line.startswith('*'):
                    p = doc.add_paragraph(style="List Bullet")
                    p.paragraph_format.left_indent = Cm(1.0)
                    # Định dạng in đậm các cụm từ quan trọng trong danh sách
                    parts = clean_line[1:].strip().split('**')
                    for p_idx, part in enumerate(parts):
                        run = p.add_run(part)
                        run.font.size = Pt(11)
                        if p_idx % 2 != 0:
                            run.bold = True
                else:
                    p = doc.add_paragraph()
                    # Định dạng in nghiêng khối trích dẫn
                    parts = clean_line.split('**')
                    for p_idx, part in enumerate(parts):
                        run = p.add_run(part)
                        run.font.size = Pt(11)
                        run.font.italic = True
                        if p_idx % 2 != 0:
                            run.bold = True
                            
    # Ghi file Word hoàn thành
    long_output = make_long_path(docx_file)
    doc.save(long_output)
    print(f"=== ĐÃ CHUYỂN ĐỔI THÀNH CÔNG SANG FILE WORD: {docx_file.name} ===")

if __name__ == "__main__":
    main()
