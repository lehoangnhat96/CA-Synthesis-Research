# -*- coding: utf-8 -*-
"""
Generate OUTLINE THONG SO TONG HOP CARBON AEROGEL (N-CA va Fe/N-CA)
as a .docx file with formatted tables.
Updated: 2026-05-25 — includes gap analysis resolution results.
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
import os

OUTPUT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "1 SOPs",
    "new",
    "OUTLINE_THONG_SO_TONG_HOP_CA.docx",
)

doc = Document()

# -- Global styles --
style = doc.styles["Normal"]
style.font.name = "Times New Roman"
style.font.size = Pt(12)
style.paragraph_format.space_after = Pt(4)
style.paragraph_format.line_spacing = 1.15

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


# -- Helper functions --
def add_table(doc, headers, rows, col_widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="003366"/>')
        cell._tc.get_or_add_tcPr().append(shading)
    for r_idx, row_data in enumerate(rows):
        for c_idx, val in enumerate(row_data):
            cell = table.rows[r_idx + 1].cells[c_idx]
            cell.text = ""
            p = cell.paragraphs[0]
            run = p.add_run(str(val))
            run.font.size = Pt(10)
            if r_idx % 2 == 0:
                shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="E8F0FE"/>')
                cell._tc.get_or_add_tcPr().append(shading)
    if col_widths:
        for i, w in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = Cm(w)
    doc.add_paragraph()
    return table


def add_note(doc, text, prefix="LUU Y"):
    p = doc.add_paragraph()
    run = p.add_run(f"[!] {prefix}: ")
    run.bold = True
    run.font.color.rgb = RGBColor(180, 60, 0)
    run.font.size = Pt(10)
    run2 = p.add_run(text)
    run2.font.size = Pt(10)
    run2.font.italic = True


def add_bullet(doc, text, level=0):
    p = doc.add_paragraph(text, style="List Bullet")
    p.paragraph_format.left_indent = Cm(1.27 + level * 0.63)
    for run in p.runs:
        run.font.size = Pt(11)


def add_result(doc, text, color_rgb=RGBColor(0, 100, 0)):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    run.font.color.rgb = color_rgb
    run.font.size = Pt(11)


# ===== TITLE PAGE =====
for _ in range(4):
    doc.add_paragraph()

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_t = p_title.add_run(
    "OUTLINE THONG SO TONG HOP\nCARBON AEROGEL (N-CA VA Fe/N-CA)"
)
run_t.bold = True
run_t.font.size = Pt(22)
run_t.font.color.rgb = RGBColor(0, 51, 102)

doc.add_paragraph()
p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_s = p_sub.add_run(
    "Doi chieu - Xac thuc ke thua - Danh gia tu Thu vien Tai lieu\nGap Analysis & Resolution (Updated 2026-05-25)"
)
run_s.font.size = Pt(14)
run_s.font.color.rgb = RGBColor(80, 80, 80)

doc.add_paragraph()
p_info = doc.add_paragraph()
p_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_i = p_info.add_run(
    "Nguon: Xo dua Ben Tre | IUH TPHCM | Hoa Phan tich\nSample set: N-CA (700C) va Fe/N-CA (800C)"
)
run_i.font.size = Pt(12)
run_i.font.italic = True

doc.add_page_break()

# ===== PHAN 1: DOI CHIEU TAI LIEU =====
doc.add_heading(
    "PHAN 1. DOI CHIEU TAI LIEU VOI 8 GIAI DOAN TONG HOP", level=1
)

p = doc.add_paragraph()
run = p.add_run(
    "Thu muc '1 Ref materials' chua ~90 bai bao (PDF + MD). "
    "Duoi day la ket qua ra soat, anh xa vao tung giai doan va danh gia % ke thua."
)
run.font.size = Pt(11)
run.font.italic = True

doc.add_heading("Tong hop danh gia ke thua toan quy trinh", level=2)

add_table(
    doc,
    ["Giai doan", "% Ke thua", "So bai ho tro", "Thieu sot chinh"],
    [
        ["1. Tien xu ly kiem", "~90%", "17", "Gravimetry xo dua Ben Tre (original)"],
        ["2. Sol-gel & sieu am", "~95%", "7", "(Gan hoan chinh)"],
        ["3. Duc khuon & gel hoa", "~90%", "4", "Toi uu hoa khuon PP va bien luan thoi gian de-gas 30-60 min"],
        ["4. Trao doi DM & say thang hoa", "~85%", "7", "Ap suat buong say, ty le co rut"],
        ["5. Nhiet phan", "~95%", "9", "(Gan hoan chinh)"],
        ["6. Doping Fe", "~95%", "7", "Bien luan thoi gian tam 24h cho monolith, chot RT"],
        ["7. Hau xu ly", "~95%", "4", "Thong nhat chon HCl 0.5M, nang T_anneal len 800C/1h"],
        ["8. Che tao dien cuc & do", "~95%", "22", "Toi uu loading, chot rieng binder Chitosan 1% va Nafion 0.25%"],
        ["TRUNG BINH", "~93%", "~77 bai", ""],
    ],
    col_widths=[5, 2.5, 2.5, 7],
)

# ===== PHAN 2: GAP ANALYSIS RESOLUTION =====
doc.add_page_break()
doc.add_heading("PHAN 2. KET QUA GIAI QUYET LO HONG (GAP ANALYSIS)", level=1)

p = doc.add_paragraph()
run = p.add_run(
    "Sau khi ra soat literature (24.05.2026), 10/10 lo hong da duoc giai quyet triet de va thong nhat. "
    "Moc T_anneal duoc nang len 800C de khop literature benchmark."
)
run.font.size = Pt(11)
run.font.italic = True

doc.add_heading("Bang tong ket trang thai 10 lo hong", level=2)

add_table(
    doc,
    ["#", "Lo hong", "Giai doan", "Trang thai", "Ket luan / Hanh dong"],
    [
        ["G1", "Gravimetry xo dua Ben Tre", "GD 1", "DA GIAI QUYET", "Original Contribution - tu do va bao cao"],
        ["G2", "Loai khuon duc", "GD 3", "DA GIAI QUYET", "Chot dung ong tiem PP cat dau de de tach gel"],
        ["G3", "Thoi gian on dinh gel 30-60 min", "GD 3", "DA GIAI QUYET", "De yen 30-60 min de de-gas va can bang nhiet (Cai & Zhang 2006)"],
        ["G4", "Shrinkage % sau say thang hoa", "GD 4", "DA GIAI QUYET", "Do bang caliper, khong che shrinkage < 15% (Q2)"],
        ["G5", "Thoi gian ngam Fe 24h vs 12h", "GD 6", "DA GIAI QUYET", "Chot 24h - intraparticle diffusion cho monolith"],
        ["G6", "Nhiet do ngam Fe", "GD 6", "DA GIAI QUYET", "Chot RT (25 +/- 2C)"],
        ["G7", "HCl vs H2SO4 acid leaching", "GD 7", "DA GIAI QUYET", "Chot HCl 0.5M - tranh sulfonation be mat"],
        ["G8", "T_anneal = 750C vs 800C", "GD 7", "DA GIAI QUYET", "Chot 800C/1h theo literature benchmark (Song et al. 2016)"],
        ["G9", "Chitosan vs Nafion binder", "GD 8", "DA GIAI QUYET", "Chitosan cho SWASV Pb/Cd, Nafion cho paracetamol DPV"],
        ["G10", "Chat lien ket ECH vs Citric", "GD 2", "DA GIAI QUYET", "Khao san song song: NH3/Urea vat ly vs 10% Citric Acid"],
    ],
    col_widths=[1, 5, 2, 3, 6],
)

# -- G5 Detail --
doc.add_heading("G5 - Thoi gian ngam Fe: 24h (DA CHOT)", level=2)
doc.add_paragraph(
    "Literature xac nhan: 24h la gia tri 'an toan' tieu chuan cho vat lieu xop phuc tap. "
    "Khuech tan noi hat (intraparticle diffusion) la buoc gioi han toc do."
)
add_note(
    doc,
    '"A 24-hour impregnation period was selected to ensure complete Fe3+ diffusion '
    'into the interior of the monolithic aerogel structure, as intraparticle diffusion '
    'is the rate-limiting step for porous carbon materials."',
    "BIEN LUAN MAU",
)

# -- G7 Detail --
doc.add_heading("G7 - HCl vs H2SO4: CHOT HCl 0.5M", level=2)
doc.add_paragraph(
    "Trong linh vuc Fe-N-C catalyst, ca HCl va H2SO4 deu duoc dung. "
    "HCl pho bien hon trong cac bai ORR Fe-N-C (ACS Catalysis, JACS). "
    "H2SO4 co the gay sulfonation be mat carbon (them nhom -SO3H)."
)
add_note(
    doc,
    '"HCl was preferred to avoid potential sulfonation of the carbon surface, '
    'which could alter the electrochemical behavior of Fe-Nx active sites."',
    "BIEN LUAN MAU",
)

# -- G8 Detail --
doc.add_heading("G8 - T_anneal: CHOT 800C / 1H (DA GIAI QUYET)", level=2)
doc.add_paragraph(
    "Nhiet do nung lan 2 da duoc nang len 800C (bang nhiet do carbon hoa lan 1) de phu hop hoan hao voi literature benchmark (Song et al. 2016). "
    "Moc nhiet do nay dam bao dong bo hoa nhiet dong hoc de sap xep cac tam Fe-N4 single-atom ben vung, trong khi do rut ngan thoi gian giu nhiet (1h) "
    "giup bao toan cau truc mesopore khong bi collapse."
)
add_table(
    doc,
    ["Phuong an", "T_anneal", "Giu nhiet", "Uu diem", "Trang thai"],
    [
        ["A (cu)", "750C", "1h", "An toan cho cau truc xop", "Da loai bo (nhiet do qua thap)"],
        ["B (CHOT)", "800C", "1h", "Khop voi literature benchmark; Fe-N4 hoan chinh", "Dang ap dung cho quy trinh"],
        ["C (khao sat)", "Khao sat 700, 750, 800C", "1h", "Co du lieu so sanh cho bai bao", "Tuy chon neu muon viet sau hon"],
    ],
    col_widths=[3, 2.5, 2, 5, 4.5],
)

# -- G9 Detail --
doc.add_heading("G9 - Chitosan vs Nafion: PHAN CHIA THEO UNG DUNG", level=2)
add_table(
    doc,
    ["Tieu chi", "Chitosan", "Nafion"],
    [
        ["Co che", "Chelation qua -NH2 va -OH -> hap phu chu dong KLN", "Ion-exchange qua -SO3- -> cation-selective"],
        ["Uu diem", "Tang preconcentration Pb2+/Cd2+ truc tiep; green chemistry", "Ben hoa hoc, chong fouling, on dinh"],
        ["Nhuoc diem", "Dan dien thap", "Co the bit lo xop active site"],
        ["Ung dung ly tuong", "Heavy metal SWASV", "Bao ve be mat trong mau phuc tap / DPV"],
    ],
    col_widths=[3, 7, 7],
)
add_result(doc, "-> Bai Pb2+/Cd2+/Zn2+ (SWASV): Chitosan 1% trong acetic acid 1%")
add_result(doc, "-> Bai Paracetamol (DPV): Nafion 0.25%")

doc.add_page_break()

# ===== PHAN 3: OUTLINE HOAN CHINH =====
doc.add_heading("PHAN 3. OUTLINE THONG SO TONG HOP HOAN CHINH", level=1)

p_note = doc.add_paragraph()
run_note = p_note.add_run(
    "Tap trung trinh bay: Thong so / Dieu kien <-> Muc dich & Luu y"
)
run_note.bold = True
run_note.font.size = Pt(12)
run_note.font.color.rgb = RGBColor(0, 51, 102)

# -- GD 1 --
doc.add_heading("GD 1 - Tien xu ly kiem (Alkali Pretreatment)", level=2)
doc.add_paragraph(
    "Muc dich: Loai lignin/hemicellulose, lo cellulose, giu cau truc phan cap tu nhien."
)
add_table(
    doc,
    ["Thong so", "Dieu kien", "Muc dich & Luu y"],
    [
        ["Nguyen lieu", "40g xo dua Ben Tre (da xay nhuyen)", "Xay truoc de tang be mat tiep xuc kiem"],
        ["Rua so bo", "800 mL nuoc voi, 80 +/- 2C, khuay 610 rpm, 4h", "Loai bui ban, tap co hoc"],
        ["Kiem hoa NaOH", "6% w/v (30g NaOH / 500 mL), 80 +/- 2C, 4h, 610 rpm", "Pha vo lien ket lignin-cellulose"],
        ["Loc & rua", "Giay loc, rua nuoc may den pH 6-7", "Kiem tra pH bang giay chi thi"],
        ["Say kho", "80C / 4h", "Dan deu tranh von. Neu von -> say lai + nghien"],
        ["Can khoi luong", "Say 105C, can truoc/sau kiem hoa", "Du lieu goc: tinh % weight-loss"],
    ],
    col_widths=[3.5, 7, 6.5],
)

# -- GD 2 --
doc.add_heading("GD 2 - Tong hop Sol-gel & danh sieu am", level=2)
doc.add_paragraph(
    "Muc dich: Hoa tan cellulose tao Sol dong nhat, dua N (tu NH3 + Urea) vao mang luoi gel."
)
doc.add_heading("Cong thuc he dung moi (cho 1g cellulose)", level=3)
add_table(
    doc,
    ["Thanh phan", "Luong", "Vai tro"],
    [
        ["NH3 25%", "11 mL", "Tao kiem hoa tan cellulose + nguon N-doping"],
        ["Urea", "4 g", "Pha cau truc hydrat hoa cellulose + nguon N-doping"],
        ["H2O DI", "5 mL", "Dung moi pha loang"],
        ["Cellulose pulp", "1 g", "-"],
        ["Tong dung moi", "16 mL", "Ty le ran/long = 1:16"],
    ],
    col_widths=[3.5, 3, 10.5],
)
doc.add_heading("Quy trinh thuc hien", level=3)
add_table(
    doc,
    ["Buoc", "Dieu kien", "Muc dich & Luu y"],
    [
        ["Pha dung moi", "NH3 -> Urea (khuay tan) -> H2O", "TUYET DOI KHONG dung NaOH thay NH3"],
        ["Cho cellulose", "Cho vao sau cung, boc kin mang thuc pham", "Tranh NH3 bay hoi"],
        ["Danh sieu am", "30 phut, pulse 2s on / 1s off", "Phan tan dong nhat cellulose"],
        ["Kiem soat nhiet", "Ice bath <= 10C (uu tien 0-5C)", "BAT BUOC - NH3 bay hoi neu > 10C"],
        ["Dau hieu dat", "Sol dong nhat, khong con soi xo tho", "Neu chua dat -> tang thoi gian sieu am"],
        ["Bao quan sol", "-12C / 24h trong tu lanh", "On dinh mang luoi truoc gel hoa"],
    ],
    col_widths=[3.5, 6, 7.5],
)
add_note(doc, "Neu NH3 bay hoi khi sieu am -> nong do N-doping giam -> XPS N at% < 3% -> tin hieu dien hoa yeu.", "CANH BAO")

# -- GD 3 --
doc.add_heading("GD 3 - Duc khuon & gel hoa (Casting & Gelation)", level=2)
doc.add_paragraph("Muc dich: Chuyen Sol thanh cau truc Hydrogel 3D on dinh.")
add_table(
    doc,
    ["Buoc", "Dieu kien", "Muc dich & Luu y"],
    [
        ["Do khuon", "Khuon silicone hoac ong PP (KHONG dung thuy tinh)", "Thuy tinh dinh gel, kho tach"],
        ["Nhiet do khuon", "0-5C", "Giu lanh tranh gel hoa bat thuong"],
        ["On dinh", "De yen 30-60 phut o 0-5C", "Khu thu bong bong khi (de-gassing) va can bang nhiet (Cai & Zhang 2006)"],
        ["Cap dong gel hoa", "-14C den -20C / 24h", "Tao mang hydrogel to ong"],
        ["Ra dong", "Tu nhien 10-20 phut", "Loai bo nuoc du be mat"],
    ],
    col_widths=[3.5, 7, 6.5],
)

# -- GD 4 --
doc.add_heading("GD 4 - Keo tu, trao doi dung moi & say thang hoa", level=2)
doc.add_paragraph("Muc dich: Thay nuoc trong gel bang dung moi de thang hoa, sau do say loai dung moi ma khong pha vo mang 3D.")
doc.add_heading("4a. Keo tu / Coagulation (chia 2 mau song song)", level=3)
add_table(
    doc,
    ["Mau", "Dieu kien ngam", "Muc dich"],
    [
        ["N-CA", "Ethanol 98% lanh (0-5C), 15 mL/mL gel, 24-48h", "Thay the nuoc bang ethanol"],
        ["Fe/N-CA", "Ethanol + FeCl3.6H2O (0-5C), 24-48h\n1% Fe -> 0.048g; 5% Fe -> 0.242g", "Keo tu + tam Fe vao cau truc gel"],
    ],
    col_widths=[3, 9, 5],
)
doc.add_heading("4b. Rua / Solvent Exchange", level=3)
add_table(
    doc,
    ["Buoc", "Dieu kien", "Luu y"],
    [
        ["Rua ethanol", "DI water >= 5x the tich gel, ngam 2-3h, lap 2-3 lan", "Den khi het mui con + pH trung tinh"],
        ["Gradient TBA (optional)", "15% TBA 6-8h -> 30% TBA 12-24h", "Tinh the hoa tot hon khi cap dong"],
    ],
    col_widths=[4, 8, 5],
)
doc.add_heading("4c. Say thang hoa / Freeze Drying", level=3)
add_table(
    doc,
    ["Thong so", "Dieu kien", "Muc dich"],
    [
        ["Cap dong", "-20C den -40C, >= 12-24h", "Dong bang hoan toan dung moi"],
        ["Bay lanh (Cold trap)", "<= -30C", "Gom hoi dung moi, bao ve bom chan khong"],
        ["Ap suat", "< 20 Pa (~0.15 Torr)", "Thang hoa: ran -> khi, khong qua long"],
        ["Thoi gian", "24-48h (den khi KL khong doi)", "-"],
    ],
    col_widths=[4, 6, 7],
)
add_note(doc, "Do shrinkage %: Volume Shrinkage = (V_gel - V_aerogel) / V_gel x 100. Benchmark freeze drying tot: < 15% linear shrinkage.", "DO SHRINKAGE")

# -- GD 5 --
doc.add_heading("GD 5 - Nhiet phan (Pyrolysis)", level=2)
doc.add_paragraph("Muc dich: Carbon hoa cellulose aerogel, hinh thanh cau truc carbon ban tinh the voi N-doping.")
doc.add_heading("Thiet lap khi bao ve", level=3)
add_table(
    doc,
    ["Buoc", "Thong so", "Muc dich"],
    [
        ["Purge truoc nung", "N2, 150-200 mL/min, 15-30 phut", "Day het O2 ra khoi lo"],
        ["Duy tri khi nung", "N2, 100 mL/min", "Bao ve suot qua trinh"],
        ["Duy tri khi cooling", "N2, 100 mL/min", "Tranh oxy hoa khi carbon con nong"],
    ],
    col_widths=[4, 6, 7],
)
doc.add_heading("Chuong trinh nhiet", level=3)
add_table(
    doc,
    ["Giai doan", "Khoang nhiet", "Toc do", "Giu nhiet", "Muc dich"],
    [
        ["Ramp 1", "25 -> 150C", "5C/min", "30 phut", "Loai hoan toan am"],
        ["Ramp 2", "150 -> 400C", "5C/min", "30 phut", "Carbon hoa so bo"],
        ["Ramp 3", "400C -> T_target", "5C/min", "2h", "Carbon hoa + N-doping"],
        ["Cooling", "T_target -> < 50C", "Tu nhien", "-", "Giu N2 lien tuc"],
    ],
    col_widths=[2.5, 3.5, 2.5, 2, 6.5],
)
doc.add_heading("Nhiet do muc tieu", level=3)
add_table(
    doc,
    ["Mau", "T_target", "Ly do"],
    [
        ["N-CA", "700C", "Giu nhieu pyridinic-N. Du cho DPV paracetamol."],
        ["Fe/N-CA (nen)", "800C", "Tang graphitization -> tang do dan -> nen tot cho Fe-Nx."],
    ],
    col_widths=[3, 2.5, 11.5],
)

# -- GD 6 --
doc.add_heading("GD 6 - Doping Fe (Post-impregnation) - CHI CHO Fe/N-CA", level=2)
doc.add_paragraph("Muc dich: Dua Fe3+ vao mao quan carbon aerogel, tao tien chat cho tam xuc tac Fe-Nx.")
add_table(
    doc,
    ["Thong so", "Dieu kien", "Muc dich & Luu y"],
    [
        ["Tien chat", "FeCl3.6H2O (MW = 270.3)", "Tan tot trong ethanol"],
        ["Dung moi", "Ethanol", "KHONG dung nuoc (Fe(OH)3 ket tua trong kiem)"],
        ["Nong do Fe", "1% (0.048g) va 5% (0.242g) / g mau", "Khao sat toi uu -> chon mau tot nhat"],
        ["30 phut dau", "Sieu am nhe", "Day Fe3+ vao mao quan ban dau"],
        ["Thoi gian con lai", "Khuay tu cham, tong 24h", "CHOT 24h: intraparticle diffusion la rate-limiting step"],
        ["Nhiet do ngam", "25 +/- 2C (nhiet do phong)", "RT - da xac nhan tu literature"],
        ["Say sau tam", "60C", "Loai ethanol nhe nhang, giu Fe phan tan"],
    ],
    col_widths=[3.5, 6, 7.5],
)
add_note(doc, "TUYET DOI KHONG them Fe vao he NH3/Urea/H2O -> gay ket tua Fe(OH)3 -> pha hong sol-gel.", "CANH BAO")

# -- GD 7 --
doc.add_heading("GD 7 - Hau xu ly (Acid Leaching + Annealing) - CHI CHO Fe/N-CA", level=2)
doc.add_paragraph("Muc dich: Loai bo Fe tu do/Fe oxide khong hoat tinh, on dinh tam xuc tac Fe-Nx.")
doc.add_heading("7a. Acid Leaching - CHOT HCl 0.5M", level=3)
add_table(
    doc,
    ["Thong so", "Dieu kien", "Muc dich"],
    [
        ["Acid", "HCl 0.5M (CHOT - tranh sulfonation tu H2SO4)", "Hoa tan Fe metallic, Fe3C, Fe oxide"],
        ["Nhiet do", "80C", "Tang toc phan ung hoa tan"],
        ["Thoi gian", "8h", "Du de loai het Fe khong phoi tri"],
        ["Sau xu ly", "Loc -> rua DI water -> say 60C/12h", "Dua ve trang thai kho sach"],
    ],
    col_widths=[3.5, 6, 7.5],
)
doc.add_heading("7b. Annealing lan 2", level=3)
add_table(
    doc,
    ["Thong so", "Dieu kien", "Muc dich"],
    [
        ["Khi", "N2", "Bao ve carbon"],
        ["Toc do gia nhiet", "5C/min", "-"],
        ["T_anneal", "800C", "Chot 800C/1h - bang T_pyrolysis 1 de tai tao va on dinh tam Fe-N4 (Song et al. 2016)"],
        ["Giu nhiet", "1h", "-"],
        ["Cooling", "Tu nhien trong N2", "-"],
        ["Kiem chung ngay sau", "Raman I_D/I_G", "Xac nhan cau truc carbon khong bi hỏng"],
    ],
    col_widths=[3.5, 5, 8.5],
)

# -- GD 8 --
doc.add_heading("GD 8 - Che tao dien cuc & dac trung dien hoa", level=2)
doc.add_paragraph("Muc dich: Chuyen vat lieu bot CA thanh dien cuc lam viec, danh gia hieu nang phan tich.")
doc.add_heading("8a. Nghien, ray & luu tru", level=3)
add_bullet(doc, "Nghien trong coi ma nao den bot min dong deu")
add_bullet(doc, "Ray qua luoi 75 um (lay phan < 75 um)")
add_bullet(doc, "Bao quan: Vial thuy tinh nau, nap kin, 4C, hut chan khong nhe hoac bom N2")
add_bullet(doc, "Ghi nhan day du: Mau / Batch / Ngay / BET / Sigma")

doc.add_heading("8b. Hoat hoa GCE", level=3)
add_table(
    doc,
    ["Buoc", "Dieu kien", "Muc dich"],
    [
        ["Mai", "Al2O3 0.05 um, hinh so 8, 2 min x 2 lan", "Lam sach + tao be mat moi"],
        ["Sieu am", "DI water 1 min x 3 + Ethanol 1 min x 1", "Loai bui Al2O3"],
        ["Loai Al2O3 du", "NaOH 0.1M + anodize +1.8V/10s", "-"],
        ["Kiem tra", "CV 3 chu ky, 5 mM K3Fe(CN)6/0.1M KCl, 50 mV/s", "dEp < 70 mV; Ipa/Ipc = 0.95-1.05"],
    ],
    col_widths=[3, 8, 6],
)

doc.add_heading("8c. Pha Ink & Drop-casting", level=3)
add_table(
    doc,
    ["Thong so", "Dieu kien", "Luu y"],
    [
        ["Can carbon", "5.0 mg +/- 0.01 mg", "-"],
        ["Dung moi", "950 uL DMF (HPLC grade)", "Hoac Nuoc:Ethanol"],
        ["Binder SWASV", "Chitosan 1% trong acetic acid 1%", "Tang preconcentration Pb2+/Cd2+ qua chelation -NH2"],
        ["Binder DPV", "Nafion 0.25% trong ethanol", "Chong bam ban (anti-fouling) cho paracetamol DPV"],
        ["Sieu am", "Bath, nuoc da (< 20C), 30 phut", "KHONG probe > 30% amplitude"],
        ["Kiem tra ink", "Den dong deu, lang cham", "DLS D50 < 500 nm = tot"],
        ["Drop-cast", "7 uL nho cham tung uL len GCE", "Loading ly thuyet = 35 ug/dien cuc"],
        ["Say mang", "Tu nhien, 25C, tu hut sach, 2-3h", "KHONG thoi N2, KHONG say nong"],
    ],
    col_widths=[3, 7, 7],
)

doc.add_heading("8d. Screening 4 vat lieu", level=3)
add_table(
    doc,
    ["Phep do", "Dung dich", "Thong so", "Tieu chi Pass"],
    [
        ["CV", "5 mM K3Fe(CN)6 / 0.1M KCl", "50 mV/s, 5 chu ky", "Ip tang >= 30%, dEp giam"],
        ["EIS", "5 mM K3Fe(CN)6 / 0.1M KCl", "100 kHz -> 0.1 Hz, 10 mV", "Rct giam >= 30%"],
        ["ECSA", "0.1M H2SO4", "25-200 mV/s", "Tinh C_dl -> ECSA"],
        ["SWASV so bo", "Pb2++Cd2+ 100 ppb, acetate pH 4.5", "E_dep=-1.1V, t_dep=120s", "Tach peak >= 100 mV"],
    ],
    col_widths=[3, 5, 4.5, 4.5],
)

doc.add_heading("8e. Phan tich Pb2+/Cd2+/Zn2+ (SWASV) - Bai Q1/Q2", level=3)
add_table(
    doc,
    ["Thong so", "Khoang khao sat", "Gia tri khoi dau"],
    [
        ["pH dung dich nen", "3.5 - 6.0 (acetate buffer)", "4.5"],
        ["E_dep", "-0.8 den -1.4 V vs Ag/AgCl", "-1.1 V"],
        ["t_dep", "60 - 240 s (khuay 400 rpm)", "120 s"],
        ["SW frequency", "10 - 100 Hz", "25 Hz"],
        ["SW amplitude", "10 - 50 mV", "25 mV"],
        ["Step potential", "2 - 10 mV", "4-5 mV"],
    ],
    col_widths=[4, 7, 6],
)
add_bullet(doc, "LOD muc tieu: Pb2+ < 0.1 ug/L; Zn2+ < 10 nM")
add_bullet(doc, "Duong chuan: 0.5, 1, 2, 5, 10, 20, 50, 100, 200 ppb (n=3/diem)")
add_bullet(doc, "Ion gay nhieu: Cu2+ (!), Hg2+, Fe3+, Mn2+, Ca2+, Mg2+, Na+, K+, NO3-")
add_bullet(doc, "Real sample: Nuoc song/may -> loc 0.45 um -> vo co hoa uot -> Standard Addition 3 diem")

doc.add_heading("8f. Phan tich Paracetamol (DPV) - Bai Q3/Q4", level=3)
add_table(
    doc,
    ["Thong so", "Khoang khao sat", "Gia tri khoi dau"],
    [
        ["pH dung dich nen", "5.0 - 8.0 (PBS)", "7.0-7.4"],
        ["Pulse amplitude", "10 - 75 mV", "50 mV"],
        ["Pulse width", "10 - 100 ms", "50 ms"],
        ["Step potential", "2 - 10 mV", "5 mV"],
    ],
    col_widths=[4, 7, 6],
)
add_bullet(doc, "LOD muc tieu: < 0.05 uM")
add_bullet(doc, "Chat gay nhieu: AA, UA, DA, glucose, diclofenac, nimesulide, amoxicillin")
add_bullet(doc, "Real sample: Thuoc vien paracetamol thuong mai -> Recovery 95-105%")

doc.add_heading("8g. Repeatability, Reproducibility, Stability", level=3)
add_table(
    doc,
    ["Chi tieu", "Phuong phap", "Tieu chi"],
    [
        ["Repeatability", "1 dien cuc x 10 lan lien tiep", "RSD < 5%"],
        ["Reproducibility", "5 dien cuc doc lap, cung dieu kien", "RSD < 8%"],
        ["Stability", "Do lai sau 0, 7, 14, 30 ngay (bao quan 4C)", "> 90% Ip sau 14 ngay"],
    ],
    col_widths=[3.5, 7, 6.5],
)

# -- QUALITY GATE --
doc.add_page_break()
doc.add_heading("QUALITY GATE - CHECKLIST SAU MOI GIAI DOAN", level=2)
add_table(
    doc,
    ["Giai doan", "Du lieu bat buoc", "Tieu chi PASS", "Neu FAIL"],
    [
        ["GD 1", "% weight-loss (say 105C)", "Co du lieu truoc/sau", "Thieu Original Contribution"],
        ["GD 2", "Nhiet do ice bath suot sieu am", "Sol dong nhat, T <= 10C", "Tang sieu am, them da"],
        ["GD 3", "Anh gel sau cap dong", "Khong nut, khong sup", "Toi uu ethanol exchange"],
        ["GD 4", "Hinh dang aerogel + shrinkage %", "Mang 3D, shrinkage < 15%", "Kiem tra cap dong"],
        ["GD 5", "Yield %, mau, do gion", "Den, gion, khong chay", "Kiem tra purge N2"],
        ["GD 6", "Luong FeCl3, thoi gian ngam", "24h, RT", "-"],
        ["GD 7", "Raman I_D/I_G sau annealing (800C/1h)", "0.9-1.2", "Defect qua muc / thieu sites"],
        ["GD 8 Raman", "I_D/I_G", "0.9-1.2", "Dieu chinh T nung"],
        ["GD 8 XPS", "N at%, Fe at%", "N 3-6%, Fe 0.4-1.5%, N:Fe >= 4:1", "Dieu chinh Fe / annealing"],
        ["GD 8 BET", "S_BET", "> 300 m2/g", "KOH activation neu can"],
        ["GD 8 CV", "dEp", "< 120 mV", "Toi uu loading, binder"],
        ["GD 8 EIS", "Rct", "Fe/N-CA < N-CA < GCE", "Kiem tra Fe-Nx, mang"],
    ],
    col_widths=[2.5, 4.5, 4.5, 5.5],
)

add_result(
    doc,
    "\n-> Neu ca 5 chi so tren deu PASS -> vat lieu du nen de chuyen sang toi uu DPV/SWASV va xay dung phan Analytical Performance cho bai bao.",
)

# -- SAVE --
doc.save(OUTPUT)
print("[OK] Done:", OUTPUT.encode("ascii", errors="replace").decode())
