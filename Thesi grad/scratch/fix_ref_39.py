import docx

def update_ref_39():
    doc_path = 'DCLV_CA_29.06 Fe-N CA_Reordered_V2.docx'
    doc = docx.Document(doc_path)
    
    new_text = '[39] Y. El Hamdouni et al., "Biomass valorization of walnut shell into biochar as a resource for electrochemical simultaneous detection of heavy metal ions in water and soil samples: Preparation, characterization, and applications," Arabian Journal of Chemistry, vol. 15, no. 11, p. 104252, Nov. 2022, doi: 10.1016/j.arabjc.2022.104252.'
    
    in_refs = False
    found = False
    
    for p in doc.paragraphs:
        if 'TÀI LIỆU THAM KHẢO' in p.text:
            in_refs = True
            
        if in_refs:
            if p.text.startswith('[39]'):
                p.text = new_text
                found = True
                break
                
    if found:
        doc.save(doc_path)
        print("Updated reference [39] successfully.")
    else:
        print("Could not find reference [39] to update.")

if __name__ == '__main__':
    update_ref_39()
