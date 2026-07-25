import docx
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_mapping():
    doc = docx.Document(r"DCLV_CA_02.07 Fe-N CA.docx")
    seen_in_text = []
    
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

    for block in iter_block_items(doc):
        if isinstance(block, docx.text.paragraph.Paragraph):
            text = block.text.strip()
            if re.match(r'^\[(\d+)\]\s+(.*)', text):
                continue
            matches = re.finditer(r'\[([\d,\s\-]+)\]', text)
            for m in matches:
                for part in m.group(1).split(','):
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
            for row in block.rows:
                for cell in row.cells:
                    text = cell.text.strip()
                    matches = re.finditer(r'\[([\d,\s\-]+)\]', text)
                    for m in matches:
                        for part in m.group(1).split(','):
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
                                
    print("First 20 seen_in_text:", seen_in_text[:20])

if __name__ == "__main__":
    get_mapping()
