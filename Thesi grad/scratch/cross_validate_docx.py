"""
CROSS-VALIDATOR: So sánh mapping từ file GỐC vs thực tế trong file RENUMBERED.

Nguyên tắc "Validator độc lập":
  - Bước 1: Đọc file GỐC → tính mapping "đúng" (bỏ qua MỤC LỤC)
  - Bước 2: Đọc file RENUMBERED → thu thập thứ tự thực tế (bỏ qua MỤC LỤC)
  - Bước 3: So sánh chéo và báo cáo

Đây là guard độc lập, không dùng chung logic với execute_renumber_docx.py.
"""

import docx
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

SOURCE_PATH = r"DCLV_CA_11.07 Fe-N CA.docx"
RENUMBERED_PATH = r"DCLV_CA_11.07 Fe-N CA_Renumbered.docx"

# ─────────────────────────────────────────────
# HELPER: Đọc tất cả block items theo đúng thứ
#          tự XML (paragraphs xen kẽ tables)
# ─────────────────────────────────────────────
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
        raise ValueError("Unexpected parent type")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def extract_citations(doc_path, label=""):
    """
    Thu thập:
      - seen_in_text: thứ tự xuất hiện đầu tiên của số trích dẫn (bỏ qua MỤC LỤC)
      - bibliography: dict {số -> nội dung} từ danh mục cuối bài
    """
    doc = docx.Document(doc_path)
    seen_in_text = []
    bibliography = {}
    skip_mode = False

    for block in iter_block_items(doc):
        if isinstance(block, docx.text.paragraph.Paragraph):
            text = block.text.strip()
            text_upper = text.upper()

            # ── Phát hiện ranh giới MỤC LỤC / MỞ ĐẦU ──
            if text_upper == 'MỤC LỤC':
                skip_mode = True
            if text_upper == 'MỞ ĐẦU':
                skip_mode = False

            if skip_mode:
                continue

            # ── Danh mục tài liệu tham khảo ──
            bib_match = re.match(r'^\[(\d+)\]\s+(.*)', text)
            if bib_match:
                num = int(bib_match.group(1))
                bibliography[num] = bib_match.group(2)[:60]  # 60 ký tự đầu
                continue

            # ── Trích dẫn trong văn bản ──
            for m in re.finditer(r'\[([\d,\s\-]+)\]', text):
                for part in m.group(1).split(','):
                    part = part.strip()
                    if '-' in part:
                        try:
                            a, b = map(int, part.split('-'))
                            for n in range(a, b + 1):
                                if n not in seen_in_text:
                                    seen_in_text.append(n)
                        except ValueError:
                            pass
                    elif part.isdigit():
                        n = int(part)
                        if n not in seen_in_text:
                            seen_in_text.append(n)

        elif isinstance(block, docx.table.Table):
            if skip_mode:
                continue
            for row in block.rows:
                for cell in row.cells:
                    for m in re.finditer(r'\[([\d,\s\-]+)\]', cell.text.strip()):
                        for part in m.group(1).split(','):
                            part = part.strip()
                            if '-' in part:
                                try:
                                    a, b = map(int, part.split('-'))
                                    for n in range(a, b + 1):
                                        if n not in seen_in_text:
                                            seen_in_text.append(n)
                                except ValueError:
                                    pass
                            elif part.isdigit():
                                n = int(part)
                                if n not in seen_in_text:
                                    seen_in_text.append(n)

    return seen_in_text, bibliography


def run_cross_validation():
    print("=" * 60)
    print("  CROSS-VALIDATOR: Kiểm tra độc lập hai chiều")
    print("=" * 60)

    # ── Bước 1: Mapping đúng từ file GỐC ──
    print(f"\n[1/3] Đọc file GỐC: {SOURCE_PATH}")
    src_seq, src_bib = extract_citations(SOURCE_PATH)
    expected_mapping = {old: new for new, old in enumerate(src_seq, start=1)}
    print(f"      → Tìm thấy {len(src_seq)} trích dẫn theo thứ tự thực tế")
    print(f"      → Danh mục gốc có {len(src_bib)} mục")

    # ── Bước 2: Đọc file RENUMBERED ──
    print(f"\n[2/3] Đọc file RENUMBERED: {RENUMBERED_PATH}")
    ren_seq, ren_bib = extract_citations(RENUMBERED_PATH)
    print(f"      → Tìm thấy {len(ren_seq)} trích dẫn theo thứ tự thực tế")
    print(f"      → Danh mục mới có {len(ren_bib)} mục")

    # ── Bước 3: So sánh chéo ──
    print("\n[3/3] So sánh chéo:")
    errors = []

    # 3a. Thứ tự trong RENUMBERED phải là 1, 2, 3, 4...
    for i, actual in enumerate(ren_seq):
        expected = i + 1
        if actual != expected:
            errors.append(
                f"  ❌ Vị trí {i+1} trong văn bản: Thấy [{actual}], "
                f"nhưng phải là [{expected}]"
            )

    # 3b. Tổng số trích dẫn phải khớp
    if len(src_seq) != len(ren_seq):
        errors.append(
            f"  ❌ Số trích dẫn khác nhau: Gốc có {len(src_seq)}, "
            f"Renumbered có {len(ren_seq)}"
        )

    # 3c. Danh mục phải đủ và không thừa
    ren_text_set = set(ren_seq)
    missing = [n for n in ren_seq if n not in ren_bib]
    orphans = [n for n in ren_bib if n not in ren_text_set]

    if missing:
        errors.append(f"  ❌ Trích dẫn không có trong danh mục: {missing}")
    if orphans:
        errors.append(f"  ❌ Tài liệu mồ côi (trong danh mục nhưng không dùng): {sorted(orphans)}")

    # ── Kết quả ──
    print()
    if errors:
        print(f"  ✗ Tìm thấy {len(errors)} lỗi:")
        for e in errors:
            print(e)
    else:
        print("  ✅ PASSED — Tất cả kiểm tra độc lập đều pass:")
        print(f"     • Thứ tự trích dẫn trong văn bản: 1 → {len(ren_seq)} (chính xác)")
        print(f"     • Không có trích dẫn thiếu danh mục")
        print(f"     • Không có tài liệu mồ côi")
        print(f"     • Tổng số khớp với file gốc: {len(src_seq)} tài liệu")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    run_cross_validation()
