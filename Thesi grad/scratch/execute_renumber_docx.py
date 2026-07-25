import docx
import re
import sys
from copy import deepcopy

sys.stdout.reconfigure(encoding='utf-8')

def get_chronological_mapping(doc_path):
    doc = docx.Document(doc_path)
    seen_in_text = []
    
    # We must iterate through the document elements in order
    # python-docx doesn't easily expose interleaved paragraphs and tables.
    # But wait! We can just extract all text in order by walking the XML tree.
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
            
            if not skip_mode:
                if re.match(r'^\[(\d+)\]\s+(.*)', text):
                    continue
                
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
            if not skip_mode:
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

    old_to_new = {}
    new_id = 1
    for old_num in seen_in_text:
        old_to_new[old_num] = new_id
        new_id += 1
        
    return old_to_new

def execute_renumbering():
    in_path = r"DCLV_CA_11.07 Fe-N CA.docx"
    out_path = r"DCLV_CA_11.07 Fe-N CA_Renumbered.docx"
    
    mapping = get_chronological_mapping(in_path)
    doc = docx.Document(in_path)
    
    # 1. Phase 1: In-text Old -> Temp
    def replacer_temp(match):
        inner = match.group(1)
        parts = []
        for part in inner.split(','):
            stripped = part.strip()
            if stripped.isdigit():
                num = int(stripped)
                if num in mapping and mapping[num] != num:
                    part = part.replace(str(num), f"T_{mapping[num]}")
            parts.append(part)
        return '[' + ','.join(parts) + ']'
        
    for p in doc.paragraphs:
        if re.match(r'^\[(\d+)\]\s+(.*)', p.text.strip()):
            continue
        if re.search(r'\[([\d,\s\-]+)\]', p.text):
            # Because python-docx doesn't allow easy regex replacement while preserving formatting perfectly if it spans runs,
            # we will just replace text in runs where possible, or replace the whole paragraph text (losing some formatting).
            # Usually citations like [42] are within a single run.
            for run in p.runs:
                if re.search(r'\[([\d,\s\-]+)\]', run.text):
                    run.text = re.sub(r'\[([\d,\s\-]+)\]', replacer_temp, run.text)
                    
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for run in p.runs:
                        if re.search(r'\[([\d,\s\-]+)\]', run.text):
                            run.text = re.sub(r'\[([\d,\s\-]+)\]', replacer_temp, run.text)

    # 2. Phase 2: Bibliography
    bibliography_paragraphs = {}
    bib_start_idx = -1
    
    for i, p in enumerate(doc.paragraphs):
        text = p.text.strip()
        match = re.match(r'^\[(\d+)\]\s+(.*)', text)
        if match:
            if bib_start_idx == -1: bib_start_idx = i
            num = int(match.group(1))
            # Store the xml element of this paragraph
            bibliography_paragraphs[num] = deepcopy(p._p)
            
    # Clear old bibliography entries
    # Actually it's easier to just update the text of existing paragraphs if count is same
    # But wait, bibliography formatting is complex (italics). If we just swap the XML _p elements!
    if bib_start_idx != -1:
        # Get the new ordered list of bibliography elements
        new_bib_elements = []
        for new_num in range(1, len(bibliography_paragraphs) + 1):
            # Find which old_num maps to this new_num
            old_num = None
            for o, n in mapping.items():
                if n == new_num:
                    old_num = o
                    break
            
            if old_num and old_num in bibliography_paragraphs:
                # Get the element and change [old] to [new]
                elm = bibliography_paragraphs[old_num]
                new_bib_elements.append(elm)
                
        # Now replace the paragraphs in doc
        # Just replace the XML nodes
        idx = bib_start_idx
        for elm in new_bib_elements:
            # We need to change the [X] text to [Y] inside the XML element
            # Let's just create a temporary paragraph wrapper to modify it
            p_temp = docx.text.paragraph.Paragraph(elm, doc._body)
            for run in p_temp.runs:
                if re.match(r'^\[(\d+)\]', run.text):
                    run.text = re.sub(r'^\[(\d+)\]', lambda m: f"[{mapping[int(m.group(1))]}]", run.text)
                    break # Only replace the first occurrence (the prefix)
                    
            doc.paragraphs[idx]._p.getparent().replace(doc.paragraphs[idx]._p, elm)
            idx += 1

    # 3. Phase 3: Temp -> New in text
    for p in doc.paragraphs:
        if re.match(r'^\[(\d+)\]\s+(.*)', p.text.strip()):
            continue
        for run in p.runs:
            if 'T_' in run.text:
                run.text = re.sub(r'T_(\d+)', r'\1', run.text)
                
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for run in p.runs:
                        if 'T_' in run.text:
                            run.text = re.sub(r'T_(\d+)', r'\1', run.text)

    doc.save(out_path)
    print(f"Successfully created renumbered DOCX at: {out_path}")

if __name__ == "__main__":
    execute_renumbering()
