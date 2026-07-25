import zipfile
import xml.etree.ElementTree as ET
import sys

sys.stdout.reconfigure(encoding='utf-8')

def main():
    doc_path = '13.07 DCLV_HoangNhat.docx'
    
    with zipfile.ZipFile(doc_path, 'r') as zin:
        xml_content = zin.read('word/document.xml')

    # Parse XML
    root = ET.fromstring(xml_content)
    
    # Namespaces
    ns = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    }

    # We want to find if there are Zotero field codes inside TOC fields.
    # In Word XML, fields are represented by sequence of paragraphs/runs.
    # Let's iterate through all elements and track if we are inside a TOC field.
    in_toc = False
    toc_depth = 0
    
    # We will do a flat traversal of the document
    zotero_in_toc_count = 0
    current_paragraph_text = ""
    
    for el in root.iter():
        tag = el.tag.split('}')[-1]
        
        if tag == 'p':
            # Extract text of paragraph
            texts = [t.text for t in el.findall('.//w:t', ns) if t.text]
            current_paragraph_text = "".join(texts)
            
        elif tag == 'fldChar':
            char_type = el.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fldCharType')
            if char_type == 'begin':
                # We are starting a field. Let's see if it's a TOC
                pass
            elif char_type == 'end':
                if in_toc:
                    toc_depth -= 1
                    if toc_depth == 0:
                        in_toc = False
                        
        elif tag == 'instrText':
            text = el.text or ""
            if 'TOC' in text:
                in_toc = True
                toc_depth += 1
                print(f"Found TOC field code: {text.strip()}")
            elif 'ZOTERO_ITEM' in text and in_toc:
                zotero_in_toc_count += 1
                print(f"CRITICAL: Found Zotero item inside TOC! Text around: {current_paragraph_text[:100]}")
                print(f"  Zotero field code snippet: {text.strip()[:100]}")

    print(f"Total Zotero items inside TOC: {zotero_in_toc_count}")

if __name__ == '__main__':
    main()
