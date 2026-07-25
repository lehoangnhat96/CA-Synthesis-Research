# Kế Hoạch Tái Cấu Trúc Hệ Thống SOPs - Carbon Aerogel (CA)

Kế hoạch này chi tiết hóa việc hợp nhất, dọn dẹp và đồng bộ hóa hệ thống tài liệu SOP (Quy trình thao tác chuẩn) cho đề tài Luận văn Thạc sĩ từ 17+ file phân mảnh xuống còn **7 file cốt lõi** duy nhất, giải quyết triệt để các xung đột thông số kỹ thuật và tối ưu hóa quy trình làm việc trong phòng thí nghiệm.

---

## User Review Required

Các quyết định khoa học và kỹ thuật quan trọng cần bạn (Nhật) xác nhận trước khi tôi tiến hành tự động thực thi chỉnh sửa file:

> [!IMPORTANT]
> ### 1. Nhiệt độ nung lần 2 ($T_{anneal}$) cho Fe/N-CA
> * **Xung đột:** `SYNTHESIS_PARAMETERS` đề xuất **$750^\circ\text{C}$** để bảo toàn cấu trúc xốp. `synthesis_outline_verified` đề xuất **$800^\circ\text{C}$** (bằng nhiệt độ nung nền) để đảm bảo năng lượng tối thiểu tái tổ chức mạng carbon sp² và ổn định tâm hoạt động $Fe-N_4$ (theo Song et al. 2016).
> * **Giải pháp đề xuất:** Chọn **$800^\circ\text{C}$** làm thông số chuẩn chính thức để tối ưu tính ổn định xúc tác $Fe-N_4$. Ghi chú **$750^\circ\text{C}$** là thông số đối chứng/khảo sát bổ trợ nếu thực nghiệm phát hiện sập cấu trúc xốp.
> * **Xác nhận từ bạn:** Bạn đồng ý với phương án này chứ?

> [!NOTE]
> ### 2. Trạng thái xác thực của Cadmium ($Cd^{2+}$)
> * **Xung đột:** $Pb^{2+}$ và $Zn^{2+}$ đã được confirm chính thức. $Cd^{2+}$ xuất hiện trong một số bản nháp mới nhưng chưa được confirm chính thức trong memory context.
> * **Giải pháp đề xuất:** Giữ nguyên phần quy trình đo đồng thời cả 3 ion ($Pb^{2+}$, $Zn^{2+}$, $Cd^{2+}$) bằng kỹ thuật SWASV trong tài liệu điện hóa, nhưng đánh dấu $Cd^{2+}$ là *"Thông số đang tối ưu hóa thực nghiệm"* để giữ tính linh hoạt.
> * **Xác nhận từ bạn:** Phương án này có phù hợp với tiến độ chạy máy thực tế của bạn không?

> [!WARNING]
> ### 3. Chất liên kết (Binder) cho Paracetamol (APAP)
> * **Xung đột:** File cũ dùng Nafion 0.25 wt% cho APAP. Bản nháp mới đề xuất Chitosan cross-linked citric acid như một upgrade nâng cao.
> * **Giải pháp đề xuất:** Thống nhất **Chitosan 1 wt%** làm binder chính cho nhánh kim loại nặng ($Pb/Zn/Cd$ - SWASV) nhờ nhóm amino tự do chelate hóa kim loại cực tốt. Đối với APAP (DPV), vẫn giữ **Nafion 0.25 wt%** làm binder chính vì màng Nafion có tính chọn lọc cation tốt, chống bám bẩn điện cực bởi các tạp chất hữu cơ. Chitosan sẽ được ghi nhận là phương án nâng cao (Option B) cho APAP.

---

## Proposed Changes

Tôi sẽ tiến hành dọn dẹp thư mục [1 SOPs](file:///d:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs) và cấu trúc lại hệ thống tệp tin theo sơ đồ dưới đây:

```
1 SOPs/
├── 0_Quick_Ref.md                             [NEW]
├── 1_Protocol_Synthesis.md                    [MODIFY / CONSOLIDATE]
├── 2_Protocol_Electrochemistry.md              [MODIFY / CONSOLIDATE]
├── 3_Literature_Review_and_Gap_Analysis.md    [MODIFY - Append DOI-mapping]
├── 4_Material_Characterization.md             [NEW - Replace old guide with biosensor version]
├── 5_Project_Timeline_and_Publication_Strategy.md [KEEP]
├── 6_Quality_Gates_Checklist.md               [NEW]
├── _notes_methodology/                        [RENAME from '1 good question']
│   └── (Giữ nguyên các file ghi chú học thuật)
└── _archive/                                  [NEW / MOVE]
    ├── Final_SOPs_CA.md & .docx
    ├── keo tu.txt
    └── (Toàn bộ thư mục 'new/' cũ để backup an toàn)
```

### Chi tiết các bước thực hiện:

---

### [Component 1] Kiến Trúc SOP Mới (Thư mục chính)

#### [NEW] [0_Quick_Ref.md](file:///d:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/0_Quick_Ref.md)
* **Nội dung:** Tổng hợp bảng ma trận thông số 8 giai đoạn (GĐ0–GĐ7) rút gọn từ `Final_SOPs_CA` và Bảng kết luận thông số chuẩn hóa (§23) của `SYNTHESIS_PARAMETERS`.
* **Vai trò thực tế:** Tra cứu cực nhanh trong 1 trang giấy khi đang đứng trong phòng lab.

#### [NEW] [1_Protocol_Synthesis.md](file:///d:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/1_Protocol_Synthesis.md)
* **Nội dung:** Thay thế và nâng cấp hoàn toàn file `1_Active_Protocol_Synthesis.md` cũ.
  * **Khung quy trình:** Lấy từ `synthesis_outline_verified` Phần 2 (quy trình step-by-step mới nhất, có DOI minh chứng).
  * **Cơ chế khoa học:** Giữ lại lý luận chi tiết từ file gốc (cơ chế đông tụ, cryo-concentration, ligand-anchoring).
  * **Failure modes:** Tích hợp mục thất bại mẫu (§18) từ `SYNTHESIS_PARAMETERS`.
  * **Lọc bỏ:** Cắt bỏ hoàn toàn hệ NaOH-Urea, TEPA, hàm lượng Fe 10/15%, mục tiêu single-atom thuần túy không thực tế, và các đo đạc ORR/supercap không thuộc phạm vi.

#### [MODIFY] [2_Protocol_Electrochemistry.md](file:///d:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/2_Protocol_Electrochemistry.md)
* **Nội dung:** Hợp nhất `2_Active_Protocol_Electrochemistry.md` với các mảnh thông số từ bản nháp mới:
  * **Chế tạo điện cực & Ink:** Cập nhật tỷ lệ binder rõ ràng cho từng nhánh (Chitosan cho SWASV, Nafion cho DPV APAP).
  * **Đo SWASV:** Đồng bộ thông số thế lắng khử ($-1.1\text{ V}$ đến $-1.4\text{ V}$), thời gian lắng ($120\text{ s}$), pH dung dịch đệm acetate ($4.5$).
  * **Đo DPV (APAP):** Sửa đỉnh peak thế APAP từ $+0.34\text{ V}$ thành $+0.43 - +0.47\text{ V}$ vs. Ag/AgCl.
  * **Bổ sung:** Bảng so sánh LOD đối thủ (benchmark) từ `CA_characterization` (§7.1–7.3) và danh sách ion gây nhiễu (§8).
  * **Lọc bỏ:** Phần đo ORR trong KOH 0.1M và đo siêu tụ điện.

#### [MODIFY] [3_Literature_Review_and_Gap_Analysis.md](file:///d:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/3_Literature_Review_and_Gap_Analysis.md)
* **Nội dung:** Giữ nguyên bảng so sánh hệ kiềm và phân tích Gap G1-G10.
* **Hành động thêm:** Trích lục bảng ánh xạ DOI (~90 bài báo tương ứng với 8 giai đoạn tổng hợp) từ `synthesis_outline_verified` Phần 1 dưới dạng rút gọn để làm cơ sở biện luận học thuật vững chắc cho Luận văn.

#### [NEW] [4_Material_Characterization.md](file:///d:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/4_Material_Characterization.md)
* **Nội dung:** Thay thế hoàn toàn file `4_Material_Characterization_Guide.md` cũ bằng nội dung của `CA_characterization_biosensor.md`.
* **Lý do:** Bản mới đầy đủ hơn gấp nhiều lần, phân chia rõ ràng 6 nhóm đặc trưng vật lý - hóa học (Nhóm A-F), bao gồm các thông số cốt lõi mới như: Contact angle (độ ưa nước), ECSA/EASA (diện tích bề mặt hoạt tính điện hóa), TGA (độ bền nhiệt), và cấu trúc khung bài báo (Phần 9).

#### [NEW] [6_Quality_Gates_Checklist.md](file:///d:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/6_Quality_Gates_Checklist.md)
* **Nội dung:** Tạo mới hoàn toàn bằng cách tích hợp:
  * Bảng tổng hợp Quality Gates GĐ1–GĐ8 ở cuối Phần 1 của `synthesis_outline_verified`.
  * Các tiêu chí kiểm tra mẻ đầu tiên (§22) và Quality Gate theo giai đoạn (§16) từ `SYNTHESIS_PARAMETERS`.
* **Vai trò thực tế:** Check-sheet in ra để tích hợp vào nhật ký thí nghiệm (lab notebook).

---

### [Component 2] Dọn Dẹp và Tổ Chức Thư Mục

1. **Đổi tên thư mục:** [1 good question](file:///d:/1%20Master's%20Ana%20Chem/1%20Master's%20thesis/Carbon%20Aerogel/1%20SOPs/1%20good%20question) thành `_notes_methodology/` để phản ánh đúng vai trò lưu trữ ghi chú phương pháp luận.
2. **Tạo thư mục lưu trữ:** `_archive/` ở trong `1 SOPs`.
3. **Di chuyển các file sau vào `_archive/`:**
   * `Final_SOPs_CA.md` và `Final_SOPs_CA.docx` (Trùng lặp, dư thừa).
   * `keo tu.txt` (Ghi chú thô, rác).
   * **Toàn bộ thư mục `new/`** (10 file nháp sau khi đã merge thành công).
   * Các tệp tin trung gian cũ (`1_Active_Protocol_Synthesis.md` bản gốc).

---

## Verification Plan

Tôi sẽ kiểm tra tính toàn vẹn và chất lượng của hệ thống tài liệu sau khi hoàn thành thông qua các bước:

1. **Kiểm tra liên kết chéo:** Đảm bảo tất cả các file liên kết với nhau bằng đường dẫn Markdown tuyệt đối/tương đối chính xác để bạn dễ dàng click mở trực tiếp trong VS Code/Obsidian.
2. **Kiểm tra thông số kỹ thuật:** Chạy script rà soát tự động (hoặc tự rà soát thủ công) để đảm bảo không còn bất kỳ dòng nào nhắc đến các thông số cũ (như Fe 10%, thế APAP $+0.34\text{ V}$, hay hệ NaOH-Urea) trong các tài liệu chính.
3. **Xác nhận cấu trúc:** Đảm bảo thư mục hoạt động sạch sẽ, gọn gàng đúng 7 file chính + 2 thư mục phụ (`_archive`, `_notes_methodology`).
