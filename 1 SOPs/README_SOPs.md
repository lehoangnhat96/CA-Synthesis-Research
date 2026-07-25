# README_SOPs.md — Index Hệ Thống Tài Liệu SOP
<!-- v1.0 | 2026-05-31 | Cấu trúc hợp nhất từ 17+ file → 7 file chính -->

> **Dự án:** Fe/N co-doped carbon aerogel từ xơ dừa Bến Tre · Cảm biến điện hóa Pb²⁺/Zn²⁺/Cd²⁺ và Paracetamol  
> **Đơn vị:** IUH TP.HCM · Bộ môn Hóa Phân tích  
> **Mẫu:** N-CA (700 ℃) và Fe/N-CA (800 ℃ / T_anneal 750 ℃) — chỉ 2 mẫu

---

## SƠ ĐỒ ĐIỀU HƯỚNG

```
Bắt đầu vào lab?
    │
    ├─► Tra thông số nhanh           → 0_Quick_Ref.md
    │
    ├─► Thực hiện tổng hợp           → 1_Protocol_Synthesis.md
    │
    ├─► Chế tạo điện cực & đo        → 2_Protocol_Electrochemistry.md
    │
    ├─► Lý do chọn NH₄OH / gaps      → 3_Literature_Review_and_Gap_Analysis.md
    │
    ├─► Đặc trưng vật liệu (SEM/XPS…)→ 4_Material_Characterization.md
    │
    ├─► Timeline & chiến lược bài báo → 5_Project_Timeline_and_Publication_Strategy.md
    │
    └─► Checklist pass/fail từng mẻ  → 6_Quality_Gates_Checklist.md
```

---

## MÔ TẢ FILE

| File | Nội dung | Dùng khi nào |
|:---|:---|:---|
| `0_Quick_Ref.md` | Bảng ma trận thông số GĐ0–GĐ8, công thức FeCl₃, thông số SWASV/DPV, mục tiêu XPS | Tra cứu nhanh trước/trong khi làm thí nghiệm |
| `1_Protocol_Synthesis.md` | Step-by-step tổng hợp đầy đủ + cơ chế + failure modes + DOI mapping | Khi thực hiện tổng hợp lần đầu hoặc cần biện luận |
| `2_Protocol_Electrochemistry.md` | Đánh bóng GCE, pha mực, drop-cast, CV/EIS baseline, SWASV, DPV, validation | Khi chế tạo điện cực và đo cảm biến |
| `3_Literature_Review_and_Gap_Analysis.md` | So sánh NH₄OH vs NaOH, Gap G1–G10, DOI literature | Khi viết phần Tổng quan / Thảo luận luận văn |
| `4_Material_Characterization.md` | Nhóm A–F (SEM, TEM, BET, Raman, XRD, XPS, TGA), benchmark LOD so sánh Q1/Q2 | Khi đặc trưng vật liệu và viết Chương Kết quả |
| `5_Project_Timeline_and_Publication_Strategy.md` | Gantt 12 tháng, 2 bài báo mục tiêu, ngân sách, địa điểm đo | Lập kế hoạch và họp hướng dẫn |
| `6_Quality_Gates_Checklist.md` | Checklist từng mẻ (in ra giấy), 5 Quality Gates GCE | In và dùng trực tiếp trong phòng thí nghiệm |

---

## THÔNG SỐ CHỐT THEN CHỐT (cần nhớ)

| Thông số | Giá trị | Ghi chú |
|:---|:---:|:---|
| T_pyrolysis N-CA | **700 ℃** | Giữ pyridinic-N |
| T_pyrolysis Fe/N-CA nền | **800 ℃** | Graphitization + Fe-Nₓ |
| T_anneal lần 2 | **750 ℃ / 1h** | Chốt 2026-05-31 |
| Fe khảo sát | **1% và 5%** | Không phải 5/10/15% |
| Hệ dung môi sol-gel | **NH₄OH:Urea:H₂O** | NaOH:Urea đã loại bỏ |
| Fe doping | **Post-impregnation trong EtOH** | KHÔNG thêm Fe vào sol-gel |
| Binder SWASV | **Chitosan (Gốc 1 wt% $\rightarrow$ Cuối 0.05 wt%)** | Heavy metals |
| Binder DPV | **Nafion (Gốc 5 wt% $\rightarrow$ Cuối 0.25 wt%)** | Paracetamol |

---

## LƯU TRỮ

Các file cũ (trước 2026-05-31) đã được lưu tại `_archive/` — không xóa, chỉ tham khảo nếu cần.  
Ghi chú phương pháp luận: `_notes_methodology/`
