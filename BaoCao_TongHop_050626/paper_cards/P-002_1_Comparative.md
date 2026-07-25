## [P-002] 1 Comparative
- **File gốc:** 1 Comparative Study of Two Types of Iron Doped Carbon.md
- **Domain:** Analogical
- **Stage coverage:** GĐ2, GĐ4, GĐ5, GĐ8
- **Processed:** true

### Claims
| Stage | Thông số | Giá trị | Đơn vị | Điều kiện | SOP? | Evidence |
|-------|----------|---------|--------|-----------|------|----------|
| GĐ2   | Doping Fe | Fe(II), Fe(III) | - | ion-exchange | ⚠️ | Analogical |
| GĐ4   | Drying | Supercritical CO2 | - | - | ⚠️ | Analogical |
| GĐ5   | T_pyrolysis | 750 | °C | Ar | ✅ | Analogical |
| GĐ8   | Target | H2O2 | - | - | 🔲 | Analogical |

### Conflict (nếu có)
- [conflict_id: C-001] Stage GĐ4: Drying bằng Supercritical CO2 khác với Freeze-drying trong SOP.
- [conflict_id: C-002] Stage GĐ2: Doping bằng ion-exchange với muối K+ thay vì post-impregnation.

### RAG Oracle (NotebookLM — V2.0)
- **Triggered:** YES | **Điều kiện kích hoạt:** 2: Domain=Analogical
- **Notebook queried:** C.A - 7 8 (ID: c2f074f1-396a-4df0-a32e-938c2433e3e4)
- **Kết quả:**
  - Cơ chế: Pyrolysis tại 750°C tạo ra mạng lưới dẫn điện tốt và hình thành các tâm Fe linh hoạt cho xúc tác điện hóa.
  - Ứng dụng vs SOP: Tương thích cho GĐ5 (nhiệt phân 700-800°C), Cần điều chỉnh ở GĐ2 (phương pháp doping).
  - Bằng chứng hội tụ: Có — phù hợp với hướng tối ưu nhiệt độ của hệ Fe-N-C.
