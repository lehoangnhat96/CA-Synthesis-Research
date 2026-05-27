import os
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, color_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="444444"/>\n'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E0E0E0"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def add_callout_box(doc, text, title="GHI CHÚ / THÔNG TIN QUAN TRỌNG", color_hex="1B365D", bg_hex="F0F4F8"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.0)
    set_cell_background(cell, bg_hex)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    # Left border only (accent border)
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:left w:val="single" w:sz="36" w:space="0" w:color="{color_hex}"/>\n'
        f'  <w:top w:val="none"/>\n'
        f'  <w:bottom w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    run_title = p.add_run(f"★ {title}\n")
    run_title.font.name = 'Arial'
    run_title.font.bold = True
    run_title.font.size = Pt(10.5)
    run_title.font.color.rgb = RGBColor.from_string(color_hex)
    
    run_text = p.add_run(text.strip())
    run_text.font.name = 'Arial'
    run_text.font.italic = True
    run_text.font.size = Pt(9.5)
    run_text.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

def add_styled_heading(doc, text, level):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    
    if level == 1:
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(8)
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.bold = True
        run.font.size = Pt(18)
        run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D) # Deep Navy
        
        # Add a bottom border line to Heading 1
        pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="12" w:space="4" w:color="1B365D"/></w:pBdr>')
        p._p.get_or_add_pPr().append(pBdr)
        
    elif level == 2:
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.bold = True
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(0x4A, 0x77, 0x7A) # Muted Teal/Steel Blue
        
    elif level == 3:
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.bold = True
        run.font.size = Pt(12)
        run.font.color.rgb = RGBColor(0x33, 0x33, 0x33) # Dark Charcoal
        
    else:
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        run.font.name = 'Arial'
        run.font.bold = True
        run.font.italic = True
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

def format_rich_text(p, text):
    # Regex to extract bold (**), inline code (`), and regular text
    tokens = re.split(r'(\*\*.*?\*\*|`.*?`)', text)
    for token in tokens:
        if token.startswith('**') and token.endswith('**'):
            t_text = token[2:-2]
            run = p.add_run(t_text)
            run.font.bold = True
            run.font.name = 'Arial'
        elif token.startswith('`') and token.endswith('`'):
            t_text = token[1:-1]
            run = p.add_run(t_text)
            run.font.name = 'Courier New'
            run.font.size = Pt(9.5)
            run.font.color.rgb = RGBColor(0xA3, 0x15, 0x15) # Crimson code
        else:
            run = p.add_run(token)
            run.font.name = 'Arial'
    
    # Set spacing
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15

def parse_markdown_to_docx(doc, md_filepath):
    with open(md_filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    in_code_block = False
    code_content = []
    
    in_table = False
    table_headers = []
    table_rows = []
    
    in_callout = False
    callout_type = "NOTE"
    callout_lines = []
    
    in_list = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # 1. Code Blocks
        if stripped.startswith('```'):
            if in_code_block:
                # End of code block
                in_code_block = False
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.4)
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(8)
                
                # Shaded background for code block
                pPr = p._p.get_or_add_pPr()
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F5F5F5"/>')
                pPr.append(shd)
                
                borders = parse_xml(f'<w:pBdr {nsdecls("w")}><w:left w:val="single" w:sz="12" w:space="8" w:color="CCCCCC"/></w:pBdr>')
                pPr.append(borders)
                
                code_text = "".join(code_content)
                run = p.add_run(code_text.strip())
                run.font.name = 'Courier New'
                run.font.size = Pt(8.5)
                run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
                code_content = []
            else:
                in_code_block = True
            i += 1
            continue
            
        if in_code_block:
            code_content.append(line)
            i += 1
            continue
            
        # 2. Callouts (Obsidian style > [!NOTE], > [!IMPORTANT])
        if stripped.startswith('>'):
            match = re.match(r'^>\s*\[!(NOTE|IMPORTANT|WARNING|CAUTION|TIP)\](.*)', stripped, re.IGNORECASE)
            if match:
                in_callout = True
                callout_type = match.group(1).upper()
                extra_text = match.group(2)
                if extra_text.strip():
                    callout_lines.append(extra_text)
            else:
                if in_callout:
                    # Append callout line
                    val = stripped[1:].strip()
                    callout_lines.append(val)
                else:
                    # Regular quote block
                    val = stripped[1:].strip()
                    p = doc.add_paragraph()
                    p.paragraph_format.left_indent = Inches(0.4)
                    pPr = p._p.get_or_add_pPr()
                    borders = parse_xml(f'<w:pBdr {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="8" w:color="CCCCCC"/></w:pBdr>')
                    pPr.append(borders)
                    run = p.add_run(val)
                    run.font.italic = True
                    run.font.name = 'Arial'
                    run.font.size = Pt(10)
            i += 1
            continue
        else:
            if in_callout:
                # End of callout block
                in_callout = False
                c_text = " ".join(callout_lines)
                
                # Title color and style mapping
                color_map = {
                    "IMPORTANT": ("8B0000", "LƯU Ý QUAN TRỌNG (CRITICAL REQUIREMENTS)", "FDF2F2"),
                    "WARNING": ("B25900", "CẢNH BÁO (WARNING / HAZARDS)", "FFF9F2"),
                    "CAUTION": ("B25900", "THẬN TRỌNG (CAUTION / MARGINS)", "FFF9F2"),
                    "TIP": ("006400", "MẸO THỰC THI (EXPERT TIP)", "F2FDF2"),
                    "NOTE": ("1B365D", "GHI CHÚ THAM CHIẾU (NOTE / REFERENCE)", "F0F4F8")
                }
                color_hex, title_str, bg_hex = color_map.get(callout_type, ("1B365D", "GHI CHÚ / THÔNG TIN", "F0F4F8"))
                
                add_callout_box(doc, c_text, title=title_str, color_hex=color_hex, bg_hex=bg_hex)
                callout_lines = []
                
        # 3. Headings
        if stripped.startswith('#'):
            heading_match = re.match(r'^(#+)\s*(.*)', stripped)
            if heading_match:
                level = len(heading_match.group(1))
                h_text = heading_match.group(2).strip()
                # Skip title if it matches file header or format cleanly
                if level == 1 and h_text.endswith('.md'):
                    h_text = h_text.split('—')[1].strip() if '—' in h_text else h_text
                add_styled_heading(doc, h_text, level)
            i += 1
            continue
            
        # 4. Tables
        if stripped.startswith('|'):
            in_table = True
            row_cells = [c.strip() for c in stripped.split('|')[1:-1]]
            # If it's a separator row (e.g. | :--- | :---: |), skip it
            if all(re.match(r'^[-:\s]+$', c) for c in row_cells):
                i += 1
                continue
            
            # Check if this is the first row of table (header) or regular row
            if len(table_headers) == 0:
                table_headers = row_cells
            else:
                table_rows.append(row_cells)
            i += 1
            continue
        else:
            if in_table:
                # End of table block, write to docx
                in_table = False
                
                # Check column count
                col_count = len(table_headers)
                if col_count > 0:
                    tbl = doc.add_table(rows=len(table_rows) + 1, cols=col_count)
                    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
                    tbl.autofit = True
                    set_table_borders(tbl)
                    
                    # Style Header
                    hdr_row = tbl.rows[0]
                    # Set header row height & repeating header XML tag
                    trPr = hdr_row._tr.get_or_add_trPr()
                    trPr.append(OxmlElement('w:tblHeader'))
                    trPr.append(OxmlElement('w:cantSplit'))
                    
                    for col_idx, text in enumerate(table_headers):
                        cell = hdr_row.cells[col_idx]
                        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                        set_cell_background(cell, "1B365D") # Deep Navy Header
                        set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
                        
                        p = cell.paragraphs[0]
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                        p.paragraph_format.space_after = Pt(0)
                        p.paragraph_format.space_before = Pt(0)
                        run = p.add_run(text)
                        run.font.bold = True
                        run.font.name = 'Arial'
                        run.font.size = Pt(9.5)
                        run.font.color.rgb = RGBColor(255, 255, 255) # White text
                        
                    # Style Body Rows
                    for row_idx, row_data in enumerate(table_rows):
                        row = tbl.rows[row_idx + 1]
                        # Keep row together
                        trPr = row._tr.get_or_add_trPr()
                        trPr.append(OxmlElement('w:cantSplit'))
                        
                        # Alternating background colors
                        bg_color = "F9FBFD" if row_idx % 2 == 1 else "FFFFFF"
                        
                        for col_idx, text in enumerate(row_data):
                            if col_idx < len(row.cells):
                                cell = row.cells[col_idx]
                                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                                set_cell_background(cell, bg_color)
                                set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
                                
                                p = cell.paragraphs[0]
                                p.paragraph_format.space_after = Pt(0)
                                p.paragraph_format.space_before = Pt(0)
                                format_rich_text(p, text)
                                p.runs[0].font.size = Pt(9)
                                
                table_headers = []
                table_rows = []
                
        # 5. Lists (Bullet & Numbered)
        bullet_match = re.match(r'^([\*\-\+])\s+(.*)', stripped)
        num_match = re.match(r'^(\d+)\.\s+(.*)', stripped)
        
        if bullet_match:
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.15
            content = bullet_match.group(2).strip()
            format_rich_text(p, content)
            i += 1
            continue
            
        elif num_match:
            p = doc.add_paragraph(style='List Number')
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.15
            content = num_match.group(2).strip()
            format_rich_text(p, content)
            i += 1
            continue
            
        # 6. Regular paragraphs
        if stripped:
            p = doc.add_paragraph()
            format_rich_text(p, stripped)
            
        i += 1

def main():
    doc = Document()
    
    # Document Margins (Standard 1 inch all around)
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
        
    # --- Title Page (Trang Bìa) ---
    # Top spacing
    p_top = doc.add_paragraph()
    p_top.paragraph_format.space_before = Pt(72)
    p_top.paragraph_format.space_after = Pt(12)
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run("QUY TRÌNH TIÊU CHUẨN (SOP)\n& HỆ THỐNG CƠ SỞ KHOA HỌC CHẾ TẠO CARBON AEROGEL TRONG ĐIỆN HÓA")
    run_title.font.name = 'Arial'
    run_title.font.bold = True
    run_title.font.size = Pt(22)
    run_title.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D) # Deep Navy
    p_title.paragraph_format.space_after = Pt(18)
    
    p_subtitle = doc.add_paragraph()
    p_subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = p_subtitle.add_run("Cẩm nang Toàn diện Tách chiết Cellulose, Tổng hợp Sol-gel, Doping Sắt/Nitơ,\nBiến tính Điện cực Carbon Thủy tinh (GCE), Phép đo Điện hóa (Sensing/ORR/Supercap)\nvà Lộ trình Công bố Bài báo Khoa học.")
    run_sub.font.name = 'Arial'
    run_sub.font.italic = True
    run_sub.font.size = Pt(12)
    run_sub.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    p_subtitle.paragraph_format.space_after = Pt(120)
    
    p_info = doc.add_paragraph()
    p_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_info = p_info.add_run(
        "LUẬN VĂN THẠC SĨ HÓA PHÂN TÍCH\n"
        "Học viên Thực hiện: LÊ HOÀNG NHẬT\n"
        "Đơn vị Nghiên cứu: Phòng Thí nghiệm Hóa Phân tích nâng cao\n"
        "Địa điểm: Thành phố Hồ Chí Minh, Việt Nam"
    )
    run_info.font.name = 'Arial'
    run_info.font.bold = True
    run_info.font.size = Pt(11)
    run_info.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    
    # Page Break after Title page
    doc.add_page_break()
    
    # --- Read and compile the 5 Master SOP files ---
    sop_dir = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\1 SOPs"
    sop_files = [
        "1_Active_Protocol_Synthesis.md",
        "2_Active_Protocol_Electrochemistry.md",
        "3_Literature_Review_and_Gap_Analysis.md",
        "4_Material_Characterization_Guide.md",
        "5_Project_Timeline_and_Publication_Strategy.md"
    ]
    
    for filename in sop_files:
        filepath = os.path.join(sop_dir, filename)
        if os.path.exists(filepath):
            print(f"Parsing {filename}...")
            
            # Add a big page header/separator for each SOP
            p_sep = doc.add_paragraph()
            p_sep.paragraph_format.space_before = Pt(24)
            p_sep.paragraph_format.space_after = Pt(12)
            p_sep.paragraph_format.keep_with_next = True
            
            run_sep = p_sep.add_run(f"★ PHẦN {filename.split('_')[0]}: {filename.replace('_', ' ').replace('.md', '').upper()}")
            run_sep.font.name = 'Arial'
            run_sep.font.bold = True
            run_sep.font.size = Pt(14)
            run_sep.font.color.rgb = RGBColor(0x4A, 0x77, 0x7A)
            
            # Bottom border line
            pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="4" w:color="4A777A"/></w:pBdr>')
            p_sep._p.get_or_add_pPr().append(pBdr)
            
            parse_markdown_to_docx(doc, filepath)
            
            # Page break between parts
            if filename != sop_files[-1]:
                doc.add_page_break()
                
    # Save the consolidated document to both places for convenience
    dest_path1 = os.path.join(sop_dir, "Quy_Trinh_Tieu_Chuan_SOP_Carbon_Aerogel.docx")
    dest_path2 = r"D:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Quy_Trinh_Tieu_Chuan_SOP_Carbon_Aerogel.docx"
    
    doc.save(dest_path1)
    doc.save(dest_path2)
    print(f"Successfully compiled and saved document to:\n1. {dest_path1}\n2. {dest_path2}")

if __name__ == "__main__":
    main()
