import docx
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def validate_chronological_order(doc_path):
    doc = docx.Document(doc_path)
    
    seen_in_text = []
    bibliography = {}
    
    def iter_block_items(parent):
        from docx.document import Document
        from docx.oxml.table import CT_Tbl
        from docx.oxml.text.paragraph import CT_P
        from docx.table import _Cell, Table
        from docx.text.paragraph import Paragraph

        if isinstance(parent, Document):
            parent_elm = parent.element.body
        elif isinstance(parent, _Cell):
            parent_elm = parent._tc
        else:
            raise ValueError("Something's not right")

        for child in parent_elm.iterchildren():
            if isinstance(child, CT_P):
                yield Paragraph(child, parent)
            elif isinstance(child, CT_Tbl):
                yield Table(child, parent)

    skip_mode = False
    
    for block in iter_block_items(doc):
        if isinstance(block, docx.text.paragraph.Paragraph):
            text = block.text.strip()
            text_upper = text.upper()
            if text_upper == 'MỤC LỤC': skip_mode = True
            if text_upper == 'MỞ ĐẦU': skip_mode = False
            
            if skip_mode: continue
            
            # Check if this is a bibliography definition
            bib_match = re.match(r'^\[(\d+)\]\s+(.*)', text)
            if bib_match:
                num = int(bib_match.group(1))
                bibliography[num] = bib_match.group(2).strip()
                continue
            
            # Match in-text citations
            matches = re.finditer(r'\[([\d,\s\-]+)\]', text)
            for m in matches:
                parts = m.group(1).split(',')
                for part in parts:
                    part = part.strip()
                    if '-' in part:
                        try:
                            start, end = map(int, part.split('-'))
                            for num in range(start, end + 1):
                                if num not in seen_in_text: seen_in_text.append(num)
                        except ValueError: pass
                    elif part.isdigit():
                        num = int(part)
                        if num not in seen_in_text: seen_in_text.append(num)
                        
        elif isinstance(block, docx.table.Table):
            if skip_mode: continue
            for row in block.rows:
                for cell in row.cells:
                    text = cell.text.strip()
                    matches = re.finditer(r'\[([\d,\s\-]+)\]', text)
                    for m in matches:
                        parts = m.group(1).split(',')
                        for part in parts:
                            part = part.strip()
                            if '-' in part:
                                try:
                                    start, end = map(int, part.split('-'))
                                    for num in range(start, end + 1):
                                        if num not in seen_in_text: seen_in_text.append(num)
                                except ValueError: pass
                            elif part.isdigit():
                                num = int(part)
                                if num not in seen_in_text: seen_in_text.append(num)
                                
    # Analysis
    print("=== FINAL VALIDATION RESULTS ===")
    print(f"File checked: {doc_path}")
    print(f"Total unique citations found in text: {len(seen_in_text)}")
    print(f"Total entries in bibliography: {len(bibliography)}\n")
    
    out_of_order = []
    missing_in_bib = []
    
    expected_next = 1
    for num in seen_in_text:
        if num != expected_next:
            if num > expected_next:
                out_of_order.append((num, expected_next))
        expected_next = max(expected_next, num) + 1
        
        if num not in bibliography:
            missing_in_bib.append(num)
            
    if out_of_order:
        print("❌ CẢNH BÁO: Phát hiện trích dẫn sai thứ tự logic:")
        for actual, expected in out_of_order:
            print(f"  -> Thấy [{actual}] xuất hiện, nhưng theo đúng trình tự đáng ra phải là [{expected}]")
    else:
        print("✅ PASSED: TOÀN BỘ trích dẫn trong văn bản đã xuất hiện theo ĐÚNG THỨ TỰ LOGIC TỪ 1 ĐẾN Cuối.")
        
    if missing_in_bib:
        print("❌ CẢNH BÁO: Có trích dẫn trong bài nhưng thiếu thông tin ở danh mục:")
        print(missing_in_bib)
    else:
        print("✅ PASSED: 100% trích dẫn đều có thông tin tương ứng trong danh mục.")
        
    unused = set(bibliography.keys()) - set(seen_in_text)
    if unused:
        print("❌ CẢNH BÁO: Dư thừa tài liệu trong danh mục (không được trích dẫn trong bài):")
        print(unused)
    else:
        print("✅ PASSED: Không có tài liệu thừa trong danh mục.")

if __name__ == "__main__":
    validate_chronological_order(r"DCLV_CA_02.07 Fe-N CA_Renumbered.docx")
