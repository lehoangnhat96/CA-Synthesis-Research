import re

# 1. Trích xuất Phần Mở Đầu từ Master_Thesis_Full_Draft.md
with open('Master_Thesis_Full_Draft.md', 'r', encoding='utf-8') as f:
    master = f.read()

intro_match = re.search(r'(# MỞ ĐẦU\n.*?)(?=# CHƯƠNG 1\. TỔNG QUAN)', master, re.DOTALL)
intro_text = intro_match.group(1).strip() if intro_match else "Không tìm thấy phần Mở Đầu."

# 2. Trích xuất cơ chế từ 03_LuanAn_KeThua_ThaoTac_va_CoChe_ChiTiet.md
with open('03_LuanAn_KeThua_ThaoTac_va_CoChe_ChiTiet.md', 'r', encoding='utf-8') as f:
    coche = f.read()

# Lấy các cơ chế
co_che_match = re.search(r'(## 1\. Cơ sở khoa học của quy trình\n.*?)(?=\n## 2\. Hoàn thiện thông số)', coche, re.DOTALL)
coche_text = co_che_match.group(1).strip() if co_che_match else "Không tìm thấy cơ chế."

# Tạo bản nháp Full
draft_full = f"""# CHI TIẾT NỘI DUNG SẼ ĐƯỢC CHÈN VÀO DCLV (BƯỚC 1 & 2)

> Dưới đây là từng chữ, từng câu chính xác nhất sẽ được thay thế/chèn vào file DCLV gốc để bạn đọc và duyệt. 

---

## 1. PHẦN MỞ ĐẦU (Sẽ GHI ĐÈ thay thế hoàn toàn phần Mở đầu cũ của DCLV)

{intro_text}

---

## 2. CHƯƠNG 1: TỔNG QUAN (Sẽ CHÈN THÊM vào cuối các mục tương ứng trong DCLV)

> Các đoạn dưới đây được lấy từ file Cơ chế. Khi đắp vào DCLV, các [P-xxx] sẽ được đổi thành số [X].

### Sẽ chèn đoạn này vào cuối Mục `1.1. Sinh khối xơ dừa và tách chiết Cellulose` trong DCLV:

**1.1.1. Lập luận thiết kế và Biện luận cơ chế (Bổ sung)**

Việc lựa chọn hệ dung môi NH4OH/Urea/H2O (8:12:80) dựa trên cơ sở hóa học xanh và khả năng hòa tan chọn lọc. Phức chất NH3 tạo liên kết hydrogen mạnh với các nhóm hydroxyl (-OH) của cellulose, đồng thời urea đóng vai trò như một "chất phá vỡ" (breaker) mạng lưới liên kết hydrogen nội phân tử và gian phân tử [P-011_Insights into sustainable]. Quá trình làm lạnh sâu (-12°C) là yếu tố nhiệt lực học then chốt, làm giảm entropy của hệ, thúc đẩy sự hình thành phức chất bao vây (inclusion complex) ổn định giữa cellulose, urea và các cụm nước (water clusters) [P-024_3D hierarchical porous].

Bên cạnh đó, việc giữ lại một phần lignin (delignification bán phần) không phải là sự hạn chế của quy trình mà là một chủ ý thiết kế vật liệu. Lignin với cấu trúc polymer thơm phức tạp đóng vai trò như các "trụ cột" (pillars) cứng nhắc tự nhiên, chống lại sự sụp đổ của khung mạng cellulose trong quá trình đông tụ và sấy thăng hoa [P-016_Upcycling coconut husk]. Hơn thế nữa, sự tương tác dị thể giữa các vùng ưa nước (cellulose) và kỵ nước (lignin) tạo ra hiện tượng tự lắp ráp động học (Dynamic Self-Assembly), hình thành nên cấu trúc lỗ xốp đa cấp (hierarchical porosity) có đường đi khúc khuỷu (tortuous path) cao [P-032_Dynamic Self-Assembly]. Cấu trúc tortuous path này mang lại lợi thế kép: (1) tăng bề mặt riêng (SBET) tiếp xúc hiệu dụng và (2) tạo hiệu ứng giam giữ không gian (spatial confinement) giúp khuếch tán chọn lọc các ion kim loại nặng trong quá trình đo điện hóa.

### Sẽ chèn đoạn này vào cuối Mục `1.2. Carbon Aerogel biến tính Nitơ và Sắt` trong DCLV:

**1.2.2. Cơ sở khoa học của quá trình Nhiệt phân và Pha tạp (Bổ sung)**

Quá trình nhiệt phân Fe-doped cellulose aerogel trải qua các giai đoạn biến đổi hóa lý phức tạp. Ở giai đoạn đầu, sự phân hủy urea giải phóng các khí chứa nitơ (NH3, HNCO), tạo môi trường tự doping nitơ (in-situ N-doping) vào khung carbon đang hình thành. Lignin dư thừa, do bản chất giàu vòng thơm và có độ bền nhiệt cao hơn cellulose, hoạt động như các lõi carbon hóa định hướng (nucleation sites), thúc đẩy quá trình graphit hóa [P-039_Cellulose_Lignin_Interactions_Pyrolysis].

Sự kết hợp đồng thời của Fe(III) (từ tiền chất FeCl3) và Nitơ (từ urea) dưới điều kiện nhiệt phân sinh ra các tâm hoạt tính xúc tác điện hóa Fe-Nx (đặc biệt là Fe-N4 pyridinic) phân tán ở cấp độ nguyên tử (single-atom) [P-061_Fe_N_C_H2O2], [P-036_Fe-Cluster_Pushing_Electrons]. Cấu hình Fe-Nx này làm thay đổi cấu trúc điện tử cục bộ của mạng lưới carbon, tạo ra sự phân cực mật độ điện tích, qua đó tăng cường động học truyền electron (electron transfer kinetics) và ái lực xúc tác (electrocatalytic affinity) đối với quá trình oxy hóa khử của các ion kim loại nặng [P-035_Fe_N_Co-Doped_Carbon]. Việc sử dụng hỗn hợp chitosan (CS) và Nafion làm màng kết dính (binder) không chỉ đảm bảo độ bền cơ học trên bề mặt điện cực GCE mà còn tạo ra cơ chế "mỏ neo kép" (dual-anchoring): CS với các nhóm amine (-NH2) có khả năng chelate hóa các cation kim loại, trong khi mạng lưới perfluorinated của Nafion hỗ trợ trao đổi cation và loại trừ các anion gây nhiễu [P-045_Chitosan_Nafion].
"""

with open('Draft_MoDau_Chuong1_Full.md', 'w', encoding='utf-8') as f:
    f.write(draft_full)

print("Full Draft Generated.")
