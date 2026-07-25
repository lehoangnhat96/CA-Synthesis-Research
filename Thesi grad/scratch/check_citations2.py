import docx
import re

def get_all_paragraphs(doc):
    paragraphs = []
    # Main body paragraphs
    for p in doc.paragraphs:
        paragraphs.append(p)
    # Table paragraphs
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    paragraphs.append(p)
    return paragraphs

def parse_citations():
    doc_path = 'DCLV_CA_29.06 Fe-N CA_Reordered_V2.docx'
    doc = docx.Document(doc_path)
    
    citations_in_order = []
    seen = set()
    
    in_refs = False
    
    # We only care about order of appearance. 
    # But wait, tables might be out of order?
    # Actually, tables appear at specific locations in the document structure.
    # To get the TRUE order, we should iterate over doc.element.body and process elements sequentially.
    
    # Let's write a recursive function to iterate through block-level elements in order
    def iter_block_items(parent):
        from docx.document import Document
        from docx.oxml.text.paragraph import CT_P
        from docx.oxml.table import CT_Tbl
        from docx.table import _Cell, Table
        from docx.text.paragraph import Paragraph
        
        if isinstance(parent, Document):
            parent_elm = parent.element.body
        elif isinstance(parent, _Cell):
            parent_elm = parent._tc
        else:
            raise ValueError("Something's wrong")
            
        for child in parent_elm.iterchildren():
            if isinstance(child, CT_P):
                yield Paragraph(child, parent)
            elif isinstance(child, CT_Tbl):
                table = Table(child, parent)
                yield table

    cit_pattern = re.compile(r'\[([0-9\s,\-]+)\]')
    
    def process_text(text):
        nonlocal in_refs
        if 'TÀI LIỆU THAM KHẢO' in text:
            in_refs = True
            
        if not in_refs:
            matches = cit_pattern.findall(text)
            for match in matches:
                parts = match.split(',')
                for part in parts:
                    part = part.strip()
                    if not part: continue
                    if '-' in part:
                        try:
                            start, end = map(int, part.split('-'))
                            for i in range(start, end + 1):
                                if i not in seen:
                                    seen.add(i)
                                    citations_in_order.append(i)
                        except ValueError:
                            pass
                    else:
                        try:
                            num = int(part)
                            if num not in seen:
                                seen.add(num)
                                citations_in_order.append(num)
                        except ValueError:
                            pass

    for block in iter_block_items(doc):
        if in_refs:
            break
        if block.__class__.__name__ == 'Paragraph':
            process_text(block.text)
        elif block.__class__.__name__ == 'Table':
            for row in block.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        process_text(p.text)
                        
    # Check bibliography
    refs = []
    # bibliography is always at the end in paragraphs
    for p in doc.paragraphs:
        if 'TÀI LIỆU THAM KHẢO' in p.text:
            in_refs = True
            continue
        if in_refs:
            m = re.match(r'^\[(\d+)\]', p.text.strip())
            if m:
                refs.append(int(m.group(1)))
                
    with open('citation_check_report2.txt', 'w', encoding='utf-8') as f:
        f.write(f"Total unique citations in text: {len(seen)}\n")
        f.write(f"Order of first appearance: {citations_in_order}\n")
        f.write(f"Expected order: {list(range(1, len(seen)+1))}\n")
        
        mismatches = []
        for i, val in enumerate(citations_in_order):
            if i + 1 != val:
                mismatches.append(f"Expected {i+1}, found {val}")
                
        if mismatches:
            f.write("ORDER ISSUES IN TEXT:\n")
            for m in mismatches[:10]:
                f.write("  " + m + "\n")
            if len(mismatches) > 10:
                f.write(f"  ... and {len(mismatches)-10} more.\n")
        else:
            f.write("No order issues in text. Citations appear sequentially.\n")
            
        f.write(f"\nTotal references in bibliography: {len(refs)}\n")
        missing_in_bib = set(citations_in_order) - set(refs)
        missing_in_text = set(refs) - set(citations_in_order)
        
        if missing_in_bib:
            f.write(f"Citations in text but missing in bibliography: {sorted(list(missing_in_bib))}\n")
        if missing_in_text:
            f.write(f"Citations in bibliography but not found in text: {sorted(list(missing_in_text))}\n")

if __name__ == '__main__':
    parse_citations()
