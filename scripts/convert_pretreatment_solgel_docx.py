# -*- coding: utf-8 -*-
"""
Generate a highly-formatted Word (.docx) document for Phase 0 (Pretreatment)
and Phase 1 (Sol-Gel & Doping) based on the standardized Markdown document.
Uses elegant styling matching create_docx.py.
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
    "PHAN_TICH_CHI_TIET_TIEN_XU_LY_VA_SOL_GEL.docx",
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
    "PHAN TICH CHI TIET GIAI DOAN #0 & #1\nTIEN XU LY VA SOL-GEL"
)
run_t.bold = True
run_t.font.size = Pt(20)
run_t.font.color.rgb = RGBColor(0, 51, 102)

doc.add_paragraph()
p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_s = p_sub.add_run(
    "Trich xuat va Bien soan tu Tai lieu Huong dan Quy trinh Carbon Aerogel"
)
run_s.font.size = Pt(13)
run_s.font.color.rgb = RGBColor(80, 80, 80)

doc.add_paragraph()
p_info = doc.add_paragraph()
p_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_i = p_info.add_run(
    "Hệ vật liệu: Fe/N Co-doped Carbon Aerogel\n"
    "Nguồn nguyên liệu: Xơ dừa Bến Tre (Kiềm hóa Delignification - Không tẩy trắng)"
)
run_i.font.size = Pt(11)
run_i.font.italic = True

doc.add_page_break()


# ===== GIAI DOAN #0: TIEN XU LY =====
doc.add_heading("GIAI DOAN #0: TIEN XU LY (Pre-treatment - Delignification)", level=1)

doc.add_heading("🎯 MUC TIEU TONG THE", level=2)
p = doc.add_paragraph()
run = p.add_run(
    "Loai bo lignin, hemicellulose va tap chat tu xo dua tho nham thu duoc "
    "Cellulose tinh khiet (65-75%) dong thoi bao ton nguyen ven cau truc ong rong tu nhien. "
    "Giai doan nay quyet dinh chat luong nen tang - neu con lignin du nhieu se lam carbon hoa "
    "khong dong nhat va lam giam do dan dien."
)
run.font.size = Pt(11)

doc.add_heading("🧪 HOA CHAT & THIET BI", level=2)
add_table(
    doc,
    ["Hoa chat/Thiet bi", "Thong so ky thuat", "Vai tro", "Dieu kien hoat dong"],
    [
        ["Xo dua tho", "Tu vo trai dua, cat ngan 2-3 cm", "Nguyen lieu goc", "Rua sach bui dat, phoi kho so bo"],
        ["NaOH pellets", "AR grade, >=96%", "Pha vo lignin (delignification)", "[!] An mon manh - Deo gang tay cao su day"],
        ["DI water", "Conductivity < 1 uS/cm", "Rua sach kiem", "Can ~10-15 lit/batch 100g xo dua"],
        ["Bep dun khuay tu", "T_max 120C, 200-400 rpm", "Gia nhiet deu, tranh chay day", "Dung binh borosilicate 2-5 lit"],
        ["Binh phan ung", "2-5 lit, borosilicate, co nap", "Chua dung dich phan ung kiem", "Chiu kiem tot, co phan hoi luu"],
        ["Nhiet ke", "0-150C, sai so +/- 1C", "Theo doi nhiet do chinh xac", "Nhung sat vao hon hop phan ung"],
        ["pH meter", "Dai 0-14, +/- 0.1 pH", "Kiem tra pH sau rua", "Hieu chuan buffer pH 4, 7, 10"],
        ["Luoi loc inox", "Mesh 200 (75 um)", "Loc tach xo sau phan ung", "Rua sach bang nuoc sau moi lan dung"],
        ["Tu say doi luu", "60C, +/- 2C", "Say kho xo sau kiem hoa", "Thong gio tot de thoat am"],
        ["Can ky thuat", "+/- 0.01g, max 500g", "Can khoi luong truoc/sau", "Tinh toan yield cellulose"],
    ],
    col_widths=[3.5, 4.5, 4, 4.5]
)

doc.add_heading("📋 PHAN TICH TUNG THAO TAC", level=2)

doc.add_heading("Buoc 0A: Delignification (Loai Lignin)", level=3)
add_table(
    doc,
    ["STT", "Thao tac", "Dieu kien cu the", "Muc dich", "Co che hoa hoc", "Target dat"],
    [
        ["0A.1", "Chuan bi xo dua", "Cat ngan 2-3 cm, rua nuoc may 3 lan, vat kho", "Loai bui, tap chat co hoc be mat", "Rua troi vat ly", "Xo sach, khong con mui am moc"],
        ["0A.2", "Pha kiem NaOH", "NaOH 1.5M (~6% w/v), ty le 20 mL/g xo kho", "Hoa tan kiem deu", "NaOH -> Na+ + OH-", "Dung dich trong suot, khong ket tua"],
        ["0A.3", "Nau kiem lan 1", "80C, 90 phut, khuay 200 rpm, ty le 1:20 (w/v)", "Pha vo lien ket lignin-cellulose", "Lignin + OH- -> Phenolate (tan); Hemicellulose -> Xylan fragments", "Dung dich chuyen nau sam (lignin hoa tan)"],
        ["0A.4", "Loc & rua 1", "Loc qua luoi inox, rua nuoc am 60C tu 5-7 lan", "Loai bo phan lignin da hoa tan va kiem du", "Rua troi phenolate va Na+", "pH nuoc rua giam xuong 9-10"],
        ["0A.5", "Nau kiem lan 2", "NaOH 1.5M moi, 80C, 90 phut, khuay 200 rpm", "Loai bo lignin tanden sau ben trong", "Tuong tu lan 1 nhung hieu qua hon do cau truc da long", "Dung dich chuyen vang nhat (it lignin hon)"],
        ["0A.6", "Loc & rua 2", "Rửa bang DI water den khi pH ve 7-8", "Loai sach hoan toan kiem du", "Rua sach den khi [OH-] < 0.01M", "pH nuoc rua dat 7.0 +/- 0.5"],
    ],
    col_widths=[1, 2.5, 3.5, 3, 3.5, 3]
)

add_note(doc, "Neu sau 2 lan nau xo van con vang sam, co the nau lan 3 o 80C trong 60 phut. Tuyet doi khong nau qua 3 lan vi se lam cellulose bi phan huy, giam do ben co hoc.", "LUU Y QUAN TRONG")

doc.add_heading("Buoc 0B: Say Kho", level=3)
add_table(
    doc,
    ["STT", "Thao tac", "Dieu kien cu the", "Muc dich", "Co che vat ly", "Target dat"],
    [
        ["0B.1", "Vat nuoc", "Dung tay vat nhe hoac ly tam 2000 rpm trong 5 phut", "Loai bo nuoc tu do", "Luc co hoc day nuoc ra khoi xo", "Do am giam con ~60-70%"],
        ["0B.2", "Say doi luu", "Say o 60C trong 12-16 gio, trai mong tren khay", "Bay hoi hoan toan nuoc lien ket", "Nhiet do say thap giup tranh phan huy nhiet cellulose", "Do am xo dat < 5%"],
        ["0B.3", "Can khoi luong", "Can khoi luong kho chinh xac bang can ky thuat", "Tinh toan yield cellulose thu hoi", "-", "Yield dat 40-50% so voi ban dau"],
    ],
    col_widths=[1, 2.5, 3.5, 3, 3.5, 3]
)

p_calc = doc.add_paragraph()
run_c1 = p_calc.add_run("Cong thuc tinh:\n")
run_c1.bold = True
p_calc.add_run(
    "Cellulose content (%) = (Khoi luong kho sau xu ly / Khoi luong xo tho ban dau) x 100%\n"
    "Target thuong dat: 40-50% (trong do ham luong cellulose tinh dat ~70-80%, phan con lai hao hut chu yeu la do lignin va hemicellulose da bi loai bo)."
)

doc.add_heading("🔬 KY THUAT PHAN TICH (Rut gon)", level=2)
add_table(
    doc,
    ["Ky thuat", "Thong so do", "Target", "Y nghia", "Hang Q"],
    [
        ["FTIR", "Peaks lignin (1730 cm-1), cellulose (1050 cm-1)", "Peak lignin giam > 80%, peak cellulose manh", "Chung minh delignification thanh cong", "Q3"],
        ["TGA", "Nhiet do phan huy T_decomposition", "Cellulose Td ~350C, lignin Td rai rac tu 250-450C", "Xac nhan thu duoc cellulose tinh khiet", "Q3"],
        ["Visual", "Mau sac xo", "Mau vang rom / vang nhat (no bleaching)", "Danh gia nhanh cam quan", "Q3"],
        ["SEM (cross-section)", "Cau truc ong rong tu nhien", "Duong kinh ong 5-50 um, nguyen ven khong sap", "Xac nhan bao ton tubular structure", "Q2"],
    ],
    col_widths=[3.5, 4.5, 4, 3, 1.5]
)

doc.add_heading("🔗 KET QUA MAU CHOT", level=2)
add_table(
    doc,
    ["Dieu kien xu ly", "Cellulose content (%)", "Lignin con lai (%)", "Mau sac", "Cau truc ong rong", "Danh gia"],
    [
        ["Chua xu ly", "~40%", "~30%", "Nau sam", "Nguyen ven", "Khong dung lam sensor duoc"],
        ["Nau kiem 1 lan", "~55%", "~15%", "Vang kem / nau nhat", "Nguyen ven", "Chua du sach"],
        ["Nau kiem 2 lan (CHOT)", "65-75%", "< 8%", "Vang rom / vang nhat", "Nguyen ven", "Optimal (Ben Tre Coir Benchmark)"],
        ["Nau kiem 3 lan", "~70%", "< 6%", "Vang nhat", "Mot so ong bi nut, be", "Over-treatment (cellulose bi ton thuong)"],
    ],
    col_widths=[4, 3, 3, 3, 3, 2.5]
)

doc.add_heading("💡 GHI CHU QUAN TRỌNG", level=2)
p_q1 = doc.add_paragraph()
run_q1 = p_q1.add_run("1. Tai sao phai loai bo lignin?\n")
run_q1.bold = True
p_q1.add_run(
    "- Lignin la cac khoi polyphenol khong deu, neu nung truc tiep se carbon hoa khong dong nhat.\n"
    "- Lignin chua nhieu heteroatom O, S de gay nhiễu va lam giam do dan dien (conductivity) cua carbon.\n"
    "- Lignin co cau truc vo dinh hinh, khong tao ra vung graphitic carbon dan dien tot."
)

p_q2 = doc.add_paragraph()
run_q2 = p_q2.add_run("2. Tai sao dung NaOH thay vi acid?\n")
run_q2.bold = True
p_q2.add_run(
    "- Axit manh (nhu H2SO4) phan huy ca cellulose lam yield thap va mat cau truc ong.\n"
    "- NaOH co tinh chon loc cao, tan cong vao lien ket ester va phenolic OH cua lignin, giu lai bo khung tinh the cellulose nguyen ven."
)

doc.add_page_break()


# ===== GIAI DOAN #1: SOL-GEL & IN-SITU DOPING =====
doc.add_heading("GIAI DOAN #1: SOL-GEL & IN-SITU METAL DOPING", level=1)

doc.add_heading("🎯 MUC TIEU TONG THE", level=2)
p = doc.add_paragraph()
run = p.add_run(
    "Hoa tan hoan toan cellulose xo dua trong he dung moi kiem-urea lanh de phuc hoi (tai ket tua) "
    "thanh mang luoi hydrogel 3D, dong thoi dua cac ion Ni2+, Co2+ phoi tri phan tan nano-level "
    "de doping dong thoi (in-situ synthesis). Giai doan nay la then chot nhat, quyet dinh 60% "
    "hieu nang truyen electron va mat do active sites cua sensor sau nay."
)
run.font.size = Pt(11)

doc.add_heading("🧪 HOA CHAT & THIET BI", level=2)
add_table(
    doc,
    ["Hoa chat/Thiet bi", "Thong so ky thuat", "Vai tro", "Dieu kien hoat dong"],
    [
        ["Cellulose tu #0", "Do am < 5%, cat nho < 1 cm", "Nguon carbon chinh", "Can chinh xac (vi du: 5.0 g)"],
        ["NaOH pellets", "AR grade, >=96%", "Pha vo lien ket H cua cellulose", "Dung NaOH tuoi, tranh de hut am tu khi quyen"],
        ["Thiourea (hoac Urea)", "AR grade, >=99%", "Uc che tai ket tua som + nguon N", "[!] Thiourea doc, deo gang tay khi thao tac"],
        ["TEPA", "95% active content, liquid", "Chelator kim loai + N-source", "An da, kich ung - dung pipette thuy tinh trong tu hut"],
        ["NiCl2.6H2O", "AR grade, >=98%", "Nguon kim loai niken", "Hoa tan rat tot trong nuoc DI lanh"],
        ["CoCl2.6H2O", "AR grade, >=98%", "Nguon kim loai coban", "Hoa tan rat tot trong nuoc DI lanh"],
        ["DI water", "Conductivity < 1 uS/cm", "Dung moi hoa tan", "Khu khi (boiling 10') va lam lanh trong khi trơ N2"],
        ["Tu lanh sau", "-18C den -25C", "Lam lanh dung dich NaOH/Thiourea", "Nhiet do lanh sau on dinh +/- 2C"],
        ["Magnetic stirrer lanh", "T: -20C den 100C, 500 rpm", "Khuay deu o nhiet do am", "Dung chau lam lanh chuyen dung voi glycol"],
        ["Binh tam giac", "250-500 mL, borosilicate", "Chua dung dich sol-gel", "Chiu nhiet va chịu co hoc tot"],
        ["Tu am", "60C, +/- 1C", "Gia nhiet cham de gel hoa", "Khong khi tinh, khong rung dong co hoc"],
        ["Khuon nhua PE", "Duong kinh 5 cm, sau 2 cm", "Dinh hinh monolith gel", "Rua sach bang nuoc cat va cồn, de kho"],
        ["Nhiet ke dien tu", "Dai -50 den 150C, +/- 0.5C", "Theo doi nhiet do chat long", "Dau do kim loai phu Teflon chong an mon"],
    ],
    col_widths=[3.5, 4.5, 4, 4.5]
)

doc.add_heading("📋 PHAN TICH TUNG THAO TAC", level=2)

doc.add_heading("Buoc 1A: Hoa Tan Cellulose (Dissolution)", level=3)
add_table(
    doc,
    ["STT", "Thao tac", "Dieu kien cu the", "Muc dich", "Co che hoa hoc", "Target dat"],
    [
        ["1A.1", "Lam lanh dung dich", "NaOH 7% (w/v) + Thiourea 12% (w/v), lam lanh o -18C trong 4h", "Tiên lam lanh he truoc khi cho cellulose", "Nhiet do thap lam giam entropy, giam do nhot he va tang kha nang hydrat hoa", "Dung dich dong bang nhe, co the khuay tan nhanh"],
        ["1A.2", "Them cellulose xo dua", "Cho 5g cellulose/100 mL dung dich, giu nhiet do -12C den -15C, khuấy 500 rpm", "Ngan ngua cellulose tai ket tua som truoc khi tan hoan toan", "OH- tan cong vao lien ket hydro, Na+ va thiourea tao cum hydrat bao quanh chuoi cellulose", "Cellulose bat dau truong no, dun dich dac lai nhu keo"],
        ["1A.3", "Khuay hoa tan", "Khuay deu o -12C trong 60 phut, binh phai dat trong chau da/glycol lanh", "Hoàn tan hoan toan chuoi cellulose thanh sol dong nhat", "Cellulose chain duoc rieng re hoa, dung dich tro nen trong suot hon", "Dung dich trong suot hoac duc nhe, khong con soi xo tho"],
    ],
    col_widths=[1, 2.5, 3.5, 3, 3.5, 3]
)

add_note(doc, "Neu nhiet do he vuot qua -10°C, cellulose se lap tuc tai ket tua va dong vón khong the tan lai. Nguoc lai neu lanh qua -20°C dung dich se dong bang cung, khong the khuay duoc.", "LUU Y QUAN TRONG")

doc.add_heading("Buoc 1B: In-Situ Metal Doping", level=3)
add_table(
    doc,
    ["STT", "Thao tac", "Dieu kien cu the", "Muc dich", "Co che hoa hoc", "Target dat"],
    [
        ["1B.1", "Pha dung dich muoi", "NiCl2 0.5M + CoCl2 1.0M (ty le mol Ni:Co = 1:2), pha trong DI water lanh", "Chuan bi nguon kim loai phan tan", "Muoi dien ly hoan toan tao ra cac aquo complex [Ni(H2O)6]2+ va [Co(H2O)6]2+", "Dung dich trong, xanh lam dac trung cua cobalt co nuoc"],
        ["1B.2", "Chelate bang TEPA", "Them tu tu TEPA 2.5g vao dung dich muoi, khuay o 25C trong 10 phut", "Che lat ion kim loai ngan chan ket tua hydroxide trong kiem", "TEPA phoi tri lam cap ca 5 nitơ phoi tri tao phuc co vong chelate ben vung voi Ni2+ va Co2+", "Dung dich chuyen sang mau xanh thong xam dam, tuyet doi khong bi ket tua"],
        ["1B.3", "Tron vao cellulose sol", "Nho tu tu dung dich phuc [Metal-TEPA] vao cellulose sol o -12C, khuay 300 rpm, 30'", "Phan tan deu cac tam kim loai vao khoi sol-gel o cap do phan tu", "Phuc chelate 'boi' giua cac chuoi cellulose ma khong gay ket tua keo tu", "Sol dong nhat mau xanh da troi, tron lang min"],
    ],
    col_widths=[1, 2.5, 3.5, 3, 3.5, 3]
)

doc.add_heading("Buoc 1C: Gelation (Tao Gel)", level=3)
add_table(
    doc,
    ["STT", "Thao tac", "Dieu kien cu the", "Muc dich", "Co che vat ly", "Target dat"],
    [
        ["1C.1", "Do khuon", "Do cham dung dich sol mau xanh vao cac khuon PE day 1-2 cm, loc bot bot", "Dinh hinh gel truoc khi gia nhiet", "Loai bo bot khi va xep cac chuoi deu", "Sol phan bo deu tren mat khuon, mat gel lang"],
        ["1C.2", "Gia nhiet gel hoa", "Giu o 60C trong tu am suot 12 gio, giu kien kiet khong rung lac", "Cellulose tai ket tua lai de lien ket cheo tao hydrogel 3D vung chac", "Nhiet do tang lam cac cum hydrat kiem-thiourea roi ra, cellulose chain lai gan nhau va tai tao lien ket hydro", "Gel ran chac, dan hoi nhu thach, giữ duoc hinh dang monolith"],
        ["1C.3", "Tach gel", "Nhe nhang lay gel ra khoi khuôn PE", "Kiem tra chat luong co ly", "Tach khoi khuon ma khong ton thuong cau truc", "Gel monolith nguyen ven, khong nut, khong bi chay nhe ra"],
    ],
    col_widths=[1, 2.5, 3.5, 3, 3.5, 3]
)

p_mech = doc.add_paragraph()
run_m1 = p_mech.add_run("Co che tao mang 3D:\n")
run_m1.bold = True
p_mech.add_run(
    "Cellulose chains (linear) --[cooling at -12C]--> Dissolved chains (mobile)\n"
    "   ↓ [heating at 60C]\n"
    "Physical crosslinking (H-bonds) -> 3D network hydrogel + [Metal-TEPA] trapped inside"
)

doc.add_heading("🔬 KY THUẬT PHÂN TÍCH (Rút gọn)", level=2)
add_table(
    doc,
    ["Ky thuat", "Thong so do", "Target", "Y nghia", "Hang Q"],
    [
        ["SEM (freeze-dried gel)", "Mang luoi 3D lien ket chéo", "Cac soi xenlulo nano dan xen chat, khong lam nut/sap", "Chung minh cau truc hydrogel 3D tuong thich", "Q3"],
        ["TEM + EDX mapping", "Su phan bo cua Ni, Co", "Cac dom phuc kim loai size < 5nm phan bo deu khong vón", "Xac nhan doping in-situ thanh cong cap do nguyen tu", "Q2"],
        ["ICP-MS", "Ham luong Ni, Co (wt%)", "Ni: 3-5%; Co: 6-10% trong khoi", "Kiem chung dinh luong ham luong kim loai thuc te", "Q3"],
        ["Particle size (TEM)", "Kich thuoc truoc carbonization", "Cac dom phuc [Metal-TEPA] dat size < 2nm", "Tien doan kích thuoc hat oxide sau carbonization", "Q3"],
    ],
    col_widths=[3.5, 4.5, 4, 3, 1.5]
)

doc.add_heading("🔗 KET QUA MAU CHOT", level=2)
add_table(
    doc,
    ["Dieu kien", "Cellulose tan (%)", "Phan tan NiCo", "Gel strength", "Cau truc 3D", "Danh gia"],
    [
        ["Thiourea 8%, -10C", "70%", "Von cuc nhe", "Yeu, mem", "Khong deu", "Chua dat, yield thap"],
        ["Thiourea 12%, -15C (CHOT)", "> 95%", "Dong nhat", "Tot, dan hoi", "Lien ket chat", "Optimal (Direct Pyrolysis Precursor)"],
        ["Urea 12%, -15C", "85%", "Dong nhat", "Tot", "Lien ket", "Kha, nhung kha nang hoa tan cellulose kem thiourea"],
        ["Khong dung TEPA", "> 95%", "Ket tua Ni(OH)2, Co(OH)2", "Tot", "Tot, nhung mat kim loai", "That bai (kim loai bi ket tua tho ra ngoai gel)"],
    ],
    col_widths=[3.5, 3, 3, 2.5, 2.5, 3]
)

doc.add_heading("💡 GHI CHU QUAN TRONG", level=2)
p_s1 = doc.add_paragraph()
run_s1 = p_s1.add_run("1. Tai sao phai duy tri -12C den -15C khi hoa tan?\n")
run_s1.bold = True
p_s1.add_run(
    "- O nhiet do am sau, kha nang hydrat hoa cua NaOH tang manh, tao ra luc day tinh dien manh hon giua cac chuoi cellulose.\n"
    "- Neu nhiet do len >-10°C, dong nang cac chuoi tang lam lien ket hydro tu tai tao nhanh chong gay ket tua ngay lập tuc."
)

p_s2 = doc.add_paragraph()
run_s2 = p_s2.add_run("2. Tai sao ty le mol Ni:Co duoc chon la 1:2?\n")
run_s2.bold = True
p_s2.add_run(
    "- Tỷ le 1:2 la ty le thich hop nhat de khi carbon hoa se tao ra pha tinh the spinel NiCo2O4 tinh khiet.\n"
    "- Coban trong spinel co trang thai hoa tri mixed valence (Co3+/Co4+) mang lai hoat tinh dien hoa cuc cao cho sensor, trong khi Niken giup on dinh mang tinh the."
)

p_s3 = doc.add_paragraph()
run_s3 = p_s3.add_run("3. Tai sao thiet lap nhiet do gel hoa o 60°C?\n")
run_s3.bold = True
p_s3.add_run(
    "- O 60°C, van toc lam de-hydrate hoa cua kiem-thiourea la toi uu de tai tao lien ket hydro tu tu giup gel tao mang deu.\n"
    "- Neu <50°C, qua trinh gel hoa rat cham (>24h). Neu >70°C, sol de mat nuoc cuc bo lam nut nut gel, va co the phan huy cellulose."
)

# -- SAVE --
doc.save(OUTPUT)
print("[OK] Done:", OUTPUT.encode("ascii", errors="replace").decode())
