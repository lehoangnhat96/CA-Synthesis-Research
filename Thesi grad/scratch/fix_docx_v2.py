import docx
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def main():
    doc_path = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\De_cuong_Luan_van_Thac_si_Le_Hoang_Nhat.docx.docx"
    doc = docx.Document(doc_path)
    
    # Target string in 2.4.2.2
    target_phrase = "lộ trình phức hợp amoniac-cellulose"
    
    # New paragraph text (removing 'giả thuyết', removing [54], adding the hedge)
    new_para_text = "Dưới lực ép cơ học của tinh thể đá đang phát triển và cự ly tiếp xúc phân tử cực ngắn (< 0.3 nm), lớp kén bảo vệ của urea bị phá vỡ. Các nhóm hydroxyl tự do trên các chuỗi cellulose lân cận tự kết nối chéo vật lý trực tiếp với nhau, hình thành Cellulose III thông qua lộ trình phức hợp amoniac-cellulose (ammonia-cellulose complex pathway) [23]. Tuy nhiên, cơ chế kết tinh này cần được xác nhận lại bằng XRD trên chính mẫu của đề tài, do tỉ lệ tiền chất, nồng độ NH4OH và nguồn xơ dừa khác với nghiên cứu của Fauziyah [23]. Khung gel 3D tổ ong được định hình, giam giữ các tinh thể đá làm khuôn lỗ xốp lớn (macropores)."

    for p in doc.paragraphs:
        if target_phrase in p.text:
            p.text = new_para_text
            break

    out_path = r"d:\1 Master's Ana Chem\1 Master's thesis\Carbon Aerogel\Thesi grad\De_cuong_Luan_van_Thac_si_Le_Hoang_Nhat_Fixed_Cellulose_v2.docx"
    doc.save(out_path)
    print("Fixed document v2 saved to:", out_path)

if __name__ == '__main__':
    main()
