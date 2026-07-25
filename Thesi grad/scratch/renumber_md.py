import docx
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def generate_mapping():
    md_path = r"DCLV_CA_01.07 Fe-N CA.md"
    
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    seen_in_text = []
    
    def process_text_for_cites(text):
        matches = re.finditer(r'\\?\[([\d,\s\-]+)\\?\](?!\()', text)
        for m in matches:
            inner = m.group(1)
            parts = inner.split(',')
            for part in parts:
                part = part.strip()
                if '-' in part:
                    try:
                        start, end = map(int, part.split('-'))
                        for num in range(start, end + 1):
                            if num not in seen_in_text:
                                seen_in_text.append(num)
                    except ValueError:
                        pass
                else:
                    if part.isdigit():
                        num = int(part)
                        if num not in seen_in_text:
                            seen_in_text.append(num)

    for text in lines:
        text = text.strip()
        if re.match(r'^\\\[(\d+)\\\]\s+(.*)', text):
            continue 
        process_text_for_cites(text)
                
    old_to_new = {}
    current_new_id = 1
    for old_num in seen_in_text:
        old_to_new[old_num] = current_new_id
        current_new_id += 1
        
    return old_to_new

def renumber_markdown(mapping):
    md_in_path = r"DCLV_CA_01.07 Fe-N CA.md"
    md_out_path = r"DCLV_CA_02.07 Fe-N CA_Renumbered.md"
    
    with open(md_in_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Phase 1: Old -> Temp
    # Replace bibliography definitions first: \[XX\]
    for old_num, new_num in mapping.items():
        if old_num == new_num: continue
        # Target escaped brackets like \[66\] in markdown
        content = re.sub(fr'\\\[{old_num}\\\]', f'\\[T_{new_num}\\]', content)
        
    # Replace in-text citations. 
    # To handle things like [17, 66] or \[66\], we'll use a regex replacement function
    # We must NOT match markdown links like [42](#heading). We can use negative lookahead (?!\()
    def replacer_temp(match):
        inner = match.group(1)
        # Split by comma, preserving spaces
        parts = []
        for part in inner.split(','):
            stripped = part.strip()
            if stripped.isdigit():
                num = int(stripped)
                if num in mapping and mapping[num] != num:
                    # Convert to Temp
                    part = part.replace(str(num), f"T_{mapping[num]}")
            parts.append(part)
        return '[' + ','.join(parts) + ']'
        
    content = re.sub(r'\[([\d,\s]+)\](?!\()', replacer_temp, content)
    
    # Also handle table cells that might just be [45] (in HTML) if not caught above
    content = re.sub(r'\[(\d+)\](?!\()', replacer_temp, content)
    
    # Phase 2: Temp -> New
    # Re-escape the bibliography definitions
    content = re.sub(r'\\\[T_(\d+)\\\]', r'\\[\1\\]', content)
    # Remove T_ from in text citations
    content = re.sub(r'T_(\d+)', r'\1', content)
    
    # Also sort the bibliography paragraphs logically.
    # The bibliography is at the end of the file.
    # We will extract all paragraphs starting with \[N\] and sort them.
    lines = content.split('\n')
    bib_entries = {}
    other_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        bib_match = re.match(r'^\\\[(\d+)\\\]\s+(.*)', line)
        if bib_match:
            num = int(bib_match.group(1))
            # Collect full entry which might span multiple lines
            entry_lines = [line]
            i += 1
            while i < len(lines) and lines[i].strip() != '' and not re.match(r'^\\\[\d+\\\]', lines[i]) and not lines[i].startswith('##'):
                entry_lines.append(lines[i])
                i += 1
            bib_entries[num] = '\n'.join(entry_lines)
            continue
        else:
            other_lines.append(line)
        i += 1
        
    if bib_entries:
        print(f"Sorting {len(bib_entries)} bibliography entries...")
        sorted_bib_text = []
        for num in sorted(bib_entries.keys()):
            sorted_bib_text.append(bib_entries[num])
            sorted_bib_text.append('') # empty line between entries
            
        # Re-insert bibliography where it was (likely before the Phụ lục)
        # Find where "## Phụ lục" starts
        insert_idx = len(other_lines)
        for idx, l in enumerate(other_lines):
            if "## Phụ lục" in l:
                insert_idx = idx
                break
                
        final_lines = other_lines[:insert_idx] + sorted_bib_text + other_lines[insert_idx:]
        content = '\n'.join(final_lines)

    with open(md_out_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Renumbered markdown saved to {md_out_path}")

if __name__ == "__main__":
    mapping = generate_mapping()
    renumber_markdown(mapping)
