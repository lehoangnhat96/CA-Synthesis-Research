# BẢNG 1: ĐẶC TÍNH VẬT LIỆU THEO PHÂN LOẠI (Cấu trúc hình thái, vật lý, hóa học)



| Phân loại | Đặc tính vật liệu | Phương pháp xác định | Cơ chế kỹ thuật | Vai trò trong phân tích điện hóa | Hạng Q | Giai đoạn quyết định |
| --- | --- | --- | --- | --- | --- | --- |
| HÌNH THÁI HỌC VẬT LIỆU | Cấu trúc ống rỗng (Tubular hollow) | SEM/FE-SEM (cross-section) | Kế thừa mạch dẫn tự nhiên xơ dừa; NaOH/Thiourea bảo tồn lỗ rỗng; Tortuosity τ=1.2-1.5; Đường kính 5-50 μm | Khuếch tán glucose nhanh → Response time 2-5s (t₉₀) | Q2 | #0 Tiền xử lý + #1 Sol-gel |
| HÌNH THÁI HỌC VẬT LIỆU | Mạng lưới 3D liên kết (3D interconnected network) | SEM/TEM | Cellulose tái kết tủa tạo nút thắt liên kết; Khung carbon không bị đứt gãy sau carbonization | Dẫn electron liên tục xuyên suốt → Giảm internal resistance | Q3 | #1 Sol-gel |
| TÍNH CHẤT VẬT LÝ | Diện tích bề mặt & Phân bố lỗ xốp (SSA & Porosity) | BET (N₂ adsorption-desorption 77K) | Freeze-drying giữ cấu trúc không sụp đổ; KOH optional tạo thêm micropore. Target: SSA=1500-2500 m²/g; Mesopore 50-60%; Micropore 30-40%; Macropore 5-10%; Pore size 2-10nm | Tăng active sites → Tăng sensitivity & Hạ LOD. Mesopore KEY cho glucose access | Q2 | #2 Freeze-drying + #3 KOH (optional) |
| TÍNH CHẤT VẬT LÝ | Độ dẫn điện & Graphitization | Raman (ID/IG), XRD (002), 4-point probe | Carbonization 500-550°C loại O,H → sp² carbon; Graphitization vừa phải; N-doping tạo defect.  Target: ID/IG=0.8-1.0; Conductivity 10-50 S/cm | Fast electron transfer → Low Rct (<50Ω) → Response nhanh | Q2 | #4 Carbonization (500-550°C) |
| TÍNH CHẤT VẬT LÝ | Động học truyền ion (Charge transfer kinetics) | EIS (Nyquist plot, 0.01Hz-100kHz) | Đo trở kháng giao diện electrode/electrolyte. Semicircle → Rct; Linear 45° → Diffusion (Warburg).  Target: Rs<10Ω; Rct<50Ω | Low Rct → Fast signal conversion. Đánh giá tốc độ phản ứng bề mặt | Q2 | #6 Electrochemical testing |
| TÍNH CHẤT HÓA HỌC | Nitrogen hoạt tính (N-doping) | XPS (N 1s deconvolution) | TEPA phân hủy 200-400°C → N nhập mạng carbon. Pyridinic-N tạo dipole, tăng electron density ở C lân cận.  Target: Total N=3-6 at.%; Pyridinic-N >40%; Peaks: 398.5eV (pyridinic), 400.0eV (pyrrolic), 401.2eV (graphitic) | Tạo active sites hút glucose → Hạ LOD (phát hiện nồng độ μM). Enhance adsorption & catalysis | Q1 | #4 Carbonization (500-550°C) |
| TÍNH CHẤT HÓA HỌC | Tâm xúc tác kim loại (NiCo nanoparticles) | XPS (Ni 2p, Co 2p), TEM (size), CV (redox) | In-situ synthesis → Uniform dispersion. Ni²⁺/Ni³⁺  redox: Ni(OH)₂⇌NiOOH+H⁺+e⁻; Glucose+NiOOH→Gluconolactone+Ni(OH)₂.  Co synergy: Electron hopping.  Target: Size 5-20 nm (optimal 8-12nm); Loading 20-30%; Ni:Co=1:2; Ni²⁺/Ni³⁺ ≈1:1. XPS: Ni²⁺(855.5eV), Ni³⁺(857eV), Co²⁺(780.5eV), Co³⁺(782eV) | Direct electrocatalysis glucose → Amperometric signal. CORE của sensor | Q1 | #1 Sol-gel (in-situ) + #4 Carbonization |
| TÍNH CHẤT HÓA HỌC | Tính chọn lọc (Selectivity vs interferents) | Amperometry, CV (interference test) | Size exclusion: Mesopore (2-10nm) ưu tiên glucose.  Potential tuning: Glucose oxidize +0.5V; AA oxidize 0-0.2V (tách biệt).  N-groups repel AA⁻. Target: I_glucose/I_AA >10:1; I_glucose/I_UA >10:1; I_glucose/I_DA >5:1.  Test: PBS 0.1M pH7.4, +0.5V vs Ag/AgCl, 5mM Glc+0.1mM AA/UA/DA | Đảm bảo accuracy trong real sample (blood/saliva). Chống nhiễu AA, UA, DA | Q2 | #6 Electrochemical testing |






# BẢNG 2.1: QUY TRÌNH TỔNG HỢP & ĐẶC TÍNH HÌNH THÀNH



| STT Giai đoạn | Hoạt động kỹ thuật cốt lõi | Đặc tính hình thành | Phương pháp minh chứng | Vai trò trong phân tích điện hóa | Hạng Q |
| --- | --- | --- | --- | --- | --- |
| #0 TIỀN XỬ LÝ (Pre-treatment) | • Delignification: NaOH 1.5M, 80°C, 90 phút • Bleaching: H₂O₂ 40%, 80°C, 2h×2 lần • Rửa sạch đến pH~7 → Sấy 60°C | • Cellulose content: 70-80% • Lignin còn lại: <5% • Màu: Trắng kem/trắng sáng • Tubular structure bảo tồn | • FTIR (C=O, C-O-C peaks) • TGA (cellulose Td ~350°C) • Visual inspection • SEM (cross-section) | Nền tảng cho cấu trúc sạch, đồng nhất. Loại bỏ tạp chất → Tăng purity | Q3: Thấy rõ các ống vi thể rỗng, sạch tạp chất |
| #1 SOL-GEL & DOPING (In-situ metal incorporation) | • Hòa tan: NaOH/Thiourea/-18°C, 60 phút • Thêm TEPA: 1.5-3.0g (N-source + chelator) • Thêm muối: NiCl₂·6H₂O + CoCl₂·6H₂O (Ni:Co = 1:2 mol ratio) • Gel hóa: 60°C, 12 giờ | • 3D network formation • NiCo uniform dispersion (không vón cục) • Particle size: 5-20 nm | • SEM (interconnected fibers) • TEM-EDX mapping (Ni, Co) • Particle size: TEM | Tạo khung dẫn electron liên tục + In-situ anchor kim loại → Tránh vón cục | Q3: 3D net Q2: Góc tiếp xúc (Contact Angle ↓) thấm ướt tốt sau nung |
| #2 FREEZE-DRYING (Cryogenic sublimation) | • Trao đổi dung môi: Ethanol → n-Hexane • Đông lạnh: -80°C • Thăng hoa: <20 Pa, -40°C, 24-48h | • SSA: 1500-2500 m²/g • Mesopore ratio: 50-60% • Pore size: 2-10 nm (dominant) • Cấu trúc xốp không sụp đổ | • BET (N₂ adsorption 77K) • BJH (pore distribution) • Isotherm Type IV (có mesopore 2-50nm) • SEM (visual check) | Maximize active sites → Tăng sensitivity. Mesopore 50-60% cho glucose tiếp cận | Q2: BET và BJH |
| #3 KOH ACTIVATION (OPTIONAL) ⚠️ nếu cần | • Tẩm KOH: 0.5:1 ratio (KOH:CA) • Nung: 750°C, N₂, 60 phút • Rửa acid loại KOH dư | • Micropore tăng nhẹ (~10%) • SSA có thể tăng thêm 200-500 m²/g ⚠️ Phá hủy Ni/Co nếu KOH quá cao | • BET (SSA comparison) • BJH (micropore %) • XPS (check metal loss) | Fine-tune pore structure (nếu cần). TEST xem có cải thiện sensitivity không | Q3 |
| #4 CARBONIZATION (Pyrolysis + Heteroatom fixing) | • Nung: 500-550°C, N₂ (200 ml/min), 120 phút • Tốc độ nung: 5°C/phút • Làm nguội tự nhiên trong lò | • Conductivity: 10-50 S/cm (bulk) • ID/IG: 0.8-1.0 (Raman) • Pyridinic-N: 3-6 at.% (>40% of N) • NiCo₂O₄ spinel structure • Ni²⁺/Ni³⁺ ≈ 1:1 (optimal) | • 4-point probe (bulk σ) • Raman spectroscopy • XPS (N 1s, Ni 2p, Co 2p) • XRD (phase identification) • TGA (metal content check) | Activate electron pathway → Low Rct. N-doping tạo active sites → Hạ LOD. NiO/Co₃O₄ formation → Catalysis | Q3:Raman ID/IG Q2: EIS, XRD/TEM Q1: XPS |
| #5 ELECTRODE FABRICATION | • Pha slurry: CA:SuperP:PVDF = 80:10:10 trong NMP • Cast lên Ni foam (1×1 cm) • Sấy 80°C/12h → Ép 10 MPa/1 phút • Ngâm PBS 0.1M/2-4h trước test | • Film uniformity (không nứt) • Adhesion (không bong) • Loading: 3-5 mg/cm² | • SEM (surface morphology) • CV repeat (3-5 cycles) • Weight measurement | Electrical contact tốt → Stable signal. Độ bền bám dính → Reproducibility | Q3: CV lặp lại, SEM bề mặt |
| #6 ELECTRO-CHEMICAL TESTING  Quyết định chất lượng sensor | • Setup: 3-electrode (WE: CA/Ni foam; RE: Ag/AgCl; CE: Pt wire) • Electrolyte: PBS 0.1M, pH 7.4 • CV: -0.2 to +0.6V, 50 mV/s • Amperometry: +0.5V vs Ag/AgCl • EIS: 0.01 Hz - 100 kHz • Stability: 100 cycles CV • Real sample: Blood/saliva (10 mẫu) | • Sensitivity: >700 μA·mM⁻¹·cm⁻² • LOD: <0.5 μM • Linear range: 0.01-15 mM • Rct: <50 Ω (từ EIS) • Response time: 2-5s (t₉₀) • Selectivity: IGlc/IAA >10:1 • Stability: >85% after 100 cycles • Recovery: 95-105% (real sample) | • CV (glucose oxidation peak) • Amperometry (+0.5V, add glucose stepwise) • EIS (Nyquist plot, Rct) • Chrono-amperometry (t₉₀) • Interference test (AA, UA, DA, Fructose) • Real sample correlation with glucometer (R²>0.99) | CORE performance metrics quyết định chất lượng sensor. Sensitivity → Độ nhạy. LOD → Phát hiện nồng độ thấp. Selectivity → Chống nhiễu. Stability → Tuổi thọ | Q1 |










# BẢNG 2.2: PHÂN LOẠI PHƯƠNG PHÁP MINH CHỨNG VÀ GIÁ TRỊ PHÂN HẠNG (Q)



| Phương pháp minh chứng (Công cụ đo) | Đặc tính vật liệu được minh chứng (Kết quả thu được) | Phân loại Nhóm Đặc tính | Phân hạng Q & Ý nghĩa |
| --- | --- | --- | --- |
| 1. SEM / FE-SEM (Kính hiển vi điện tử quét) | - Cấu trúc ống dẫn tự nhiên (Tubular). - Mạng lưới 3D liên kết, độ xốp vĩ mô (Macropores). - Chất lượng bề mặt màng điện cực (độ bám, vết nứt). | CẤU TRÚC & HÌNH THÁI | [Q3] Căn bản: Bắt buộc phải có để chứng minh vật liệu là "Aerogel xơ dừa" chứ không phải than vụn. |
| 2. TEM / HR-TEM (Kính hiển vi điện tử truyền qua) | - Chi tiết mạng lưới sợi nano 3D. - Kích thước và độ phân tán của hạt xúc tác kim loại (Ni/Co) ở cấp độ nano. | CẤU TRÚC & HÌNH THÁI (Hỗ trợ Hóa học) | [Q2] Nâng cao: Chứng minh kỹ thuật doping thành công ở mức độ tinh vi, hạt nano không bị vón cục. |
| 3. BET & BJH (Đẳng nhiệt hấp phụ ) | - Diện tích bề mặt riêng tổng cộng (SSA). - Sự tồn tại và phân bố kích thước lỗ xốp trung bình (Mesopores). | VẬT LÝ & KẾT CẤU | [Q3] Căn bản: Bắt buộc đối với vật liệu xốp/aerogel để khẳng định ưu thế về diện tích tiếp xúc. |
| 4. XRD (Nhiễu xạ tia X) | - Mức độ graphit hóa của khung carbon (đỉnh 002). - Nhận diện pha tinh thể của kim loại/oxit kim loại (Ni, Co, NiO...). | CẤU TRÚC / VẬT LÝ | [Q3] Căn bản: Xác nhận thành phần pha sau khi nung. |
| 5. Raman (Phổ Raman) | - Tỷ lệ : Đánh giá độ dẫn điện (dựa trên độ graphit hóa) và mức độ khuyết tật (tâm hoạt động) của khung carbon. | VẬT LÝ & KẾT CẤU | [Q3] Căn bản: Thước đo tiêu chuẩn cho chất lượng vật liệu carbon. |
| 6. TGA (Phân tích nhiệt trọng lượng) | - Độ bền nhiệt của tiền chất. - Xác định nhiệt độ nung tối ưu để loại bỏ chất hữu cơ và hình thành carbon. | HÓA LÝ | [Q3] Căn bản: Biện luận khoa học cho quy trình nhiệt phân đã chọn. |
| 7. XPS (Quang điện tử tia X) | - Định lượng chính xác các loại nhóm chức Nitơ (đặc biệt Pyridinic-N). - Xác định trạng thái hóa trị của kim loại (  ...). | HÓA HỌC BỀ MẶT | [Q2] Quyết định: Chìa khóa để giải thích cơ chế xúc tác tại sao lại nhạy với Glucose. Thiếu cái này khó lên Q2. |
| 8. EDX / EDS (Phổ tán sắc năng lượng - đi kèm SEM) | - Bản đồ phân bố nguyên tố (Elemental Mapping): Chứng minh N, Ni, Co phân tán đều hay tụ điểm. | HÓA HỌC BỀ MẶT | [Q3] Căn bản: Kiểm tra sơ bộ định tính về sự thành công của việc doping. |
| 9. Contact Angle (Góc tiếp xúc) | - Tính thấm ướt (Hydrophilicity) của bề mặt điện cực đối với dung dịch nước. | VẬT LÝ BỀ MẶT | [Q2] Hỗ trợ: Giải thích tại sao dung dịch điện ly dễ dàng thâm nhập vào màng. |
| 10. CV (Quét thế vòng tuần hoàn) | - Sự hiện diện của cặp peak oxy hóa/khử (Redox activity). - Diện tích bề mặt điện hóa (ECSA). | ĐIỆN HÓA & ĐỘNG HỌC | [Q3] Căn bản: Chứng minh vật liệu có hoạt tính điện hóa. |
| 11. EIS (Phổ trở kháng điện hóa) | - Điện trở chuyển điện tích () tại giao diện điện cực/dung dịch. - Động học khuếch tán ion. | ĐIỆN HÓA & ĐỘNG HỌC | [Q2] Nâng cao: Cung cấp bằng chứng định lượng về tốc độ phản ứng và truyền dẫn electron nhanh. |
| 12. Amperometry (i-t) (Đo dòng theo thời gian) | - Các chỉ số hiệu năng chính: Độ nhạy (Sensitivity), Giới hạn phát hiện (LOD), Dải tuyến tính. - Thời gian phản hồi (Response time). | ĐIỆN HÓA & ĐỘNG HỌC | [Q3] Căn bản: Kết quả đầu ra bắt buộc của một bài báo về cảm biến. |
| 13. Selectivity Test (Kiểm tra tính chọn lọc - dùng i-t) | - Khả năng chống nhiễu đối với các chất như Acid Ascorbic (AA), Uric Acid (UA). | HÓA HỌC / ĐIỆN HÓA | [Q2] Quyết định: Chứng minh khả năng ứng dụng thực tế của cảm biến (quan trọng ngang XPS). |




# BẢNG 3: PHÂN CẤP ƯU TIÊN CHARACTERIZATION (THEO NGÂN SÁCH)



| Kỹ thuật phân tích | Thông tin thu được | Chi phí (VNĐ) | Thời gian nhận kết quả | Thời gian nhận kết quả | Hạng | Hạng | Ghi chú | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LEVEL 1: BẮT BUỘC (Không thể thiếu cho biosensor) _ Q3 | LEVEL 1: BẮT BUỘC (Không thể thiếu cho biosensor) _ Q3 | LEVEL 1: BẮT BUỘC (Không thể thiếu cho biosensor) _ Q3 | LEVEL 1: BẮT BUỘC (Không thể thiếu cho biosensor) _ Q3 | LEVEL 1: BẮT BUỘC (Không thể thiếu cho biosensor) _ Q3 | LEVEL 1: BẮT BUỘC (Không thể thiếu cho biosensor) _ Q3 | LEVEL 1: BẮT BUỘC (Không thể thiếu cho biosensor) _ Q3 | LEVEL 1: BẮT BUỘC (Không thể thiếu cho biosensor) _ Q3 | LEVEL 1: BẮT BUỘC (Không thể thiếu cho biosensor) _ Q3 |
| SEM + EDX | Morphology + Metal distribution | 500k-800k | 3-5 ngày | 3-5 ngày | Q2 | Q2 | Check vón cục, phân tán NiCo | Check vón cục, phân tán NiCo |
| BET | SSA + Pore distribution (BJH) | 1-1.5 triệu | 5-7 ngày | 5-7 ngày | Q2 | Q2 | PHẢI có BJH, không chỉ số SSA | PHẢI có BJH, không chỉ số SSA |
| CV | Glucose oxidation peak | - | Ngay (nếu có máy) | Ngay (nếu có máy) | Q1 | Q1 | Quick screen mẫu tốt/dở | Quick screen mẫu tốt/dở |
| Amperometry | Sensitivity, LOD, Linear range | - | 1-2 ngày/mẫu | 1-2 ngày/mẫu | Q1 | Q1 | CORE test | CORE test |
| EIS | Rct (charge transfer) | - | 30 phút/mẫu | 30 phút/mẫu | Q2 | Q2 | Giải thích tại sao nhanh/chậm | Giải thích tại sao nhanh/chậm |
| Subtotal Level 1 | Subtotal Level 1 | ~2-2.5 triệu | ~2-2.5 triệu | 2 tuần | 2 tuần | - | - | Đủ cho conference/Q3-Q4 journal |
| LEVEL 2: NÊN CÓ (Tăng chất lượng lên Q1-Q2) | LEVEL 2: NÊN CÓ (Tăng chất lượng lên Q1-Q2) | LEVEL 2: NÊN CÓ (Tăng chất lượng lên Q1-Q2) | LEVEL 2: NÊN CÓ (Tăng chất lượng lên Q1-Q2) | LEVEL 2: NÊN CÓ (Tăng chất lượng lên Q1-Q2) | LEVEL 2: NÊN CÓ (Tăng chất lượng lên Q1-Q2) | LEVEL 2: NÊN CÓ (Tăng chất lượng lên Q1-Q2) | LEVEL 2: NÊN CÓ (Tăng chất lượng lên Q1-Q2) | LEVEL 2: NÊN CÓ (Tăng chất lượng lên Q1-Q2) |
| XPS | N, S, Ni, Co bonding states | 2.5-4 triệu | 2-3 tuần | 2-3 tuần | Q1 | Q1 | QUAN TRỌNG NHẤT cho cơ chế | QUAN TRỌNG NHẤT cho cơ chế |
| XRD | Phase: NiCo₂O₄, NiO, Co₃O₄ | 500k-1 triệu | 3-5 ngày | 3-5 ngày | Q2 | Q2 | Chứng minh pha kim loại | Chứng minh pha kim loại |
| Raman | ID/IG ratio (graphitization) | 300k-600k | 2-3 ngày | 2-3 ngày | Q2 | Q2 | Chứng minh N-doping → defect | Chứng minh N-doping → defect |
| TGA | Metal content (ash %) | 400k-800k | 3-5 ngày | 3-5 ngày | Q3 | Q3 | Validate loading thực tế | Validate loading thực tế |
| Subtotal Level 2 | Subtotal Level 2 | ~4-7 triệu | ~4-7 triệu | 3-4 tuần | 3-4 tuần | - | - | Total với L1: 6-9 triệu → Q1-Q2 |
| LEVEL 3: TỐT NẾU CÓ (Top-tier, không bắt buộc) | LEVEL 3: TỐT NẾU CÓ (Top-tier, không bắt buộc) | LEVEL 3: TỐT NẾU CÓ (Top-tier, không bắt buộc) | LEVEL 3: TỐT NẾU CÓ (Top-tier, không bắt buộc) | LEVEL 3: TỐT NẾU CÓ (Top-tier, không bắt buộc) | LEVEL 3: TỐT NẾU CÓ (Top-tier, không bắt buộc) | LEVEL 3: TỐT NẾU CÓ (Top-tier, không bắt buộc) | LEVEL 3: TỐT NẾU CÓ (Top-tier, không bắt buộc) | LEVEL 3: TỐT NẾU CÓ (Top-tier, không bắt buộc) |
| TEM (HR-TEM) | Particle size chính xác (<1nm) | 1.5-3 triệu | 1-2 tuần | 1-2 tuần | Q2 | Q2 | Chỉ khi SEM không đủ rõ | Chỉ khi SEM không đủ rõ |
| FTIR | Functional groups (-OH, C=O) | 200k-400k | 1-2 ngày | 1-2 ngày | Q3 | Q3 | XPS tốt hơn, FTIR hỗ trợ | XPS tốt hơn, FTIR hỗ trợ |
| Contact Angle | Hydrophilicity (wettability) | 300k-500k | 1 ngày | 1 ngày | Q3 | Q3 | Giải thích glucose adsorption | Giải thích glucose adsorption |
| 4-point probe | Bulk conductivity (S/cm) | 300k-500k | 1 ngày | 1 ngày | Q3 | Q3 | EIS đã cho Rct, ít cần thiết hơn | EIS đã cho Rct, ít cần thiết hơn |
| Subtotal Level 3 | Subtotal Level 3 | ~2-5 triệu | ~2-5 triệu | 2-3 tuần | 2-3 tuần | - | - | Total all: 10-14 triệu → Top-tier |






# GIẢI THÍCH TRÌNH TỰ PHÂN HẠNG Q


**1. Nhóm Q3 (Định tính & Khẳng định):**

- Tập trung vào việc chứng minh bạn đã làm ra vật liệu (SEM, XRD) và nó có hoạt tính (CV, Amperometry).

- Lập luận dừng lại ở mức: "Tôi có lỗ xốp lớn nên diện tích tiếp xúc cao, dẫn đến dòng điện cao".

**2. Nhóm Q2 (Định lượng & Cơ chế chuyên sâu):**

- Bắt buộc phải có XPS để biện luận về bản chất hóa học (Tại sao doping Nitơ lại tốt? Tại sao tỷ lệ Ni/Co này là tối ưu?).

- Phải có EIS để chứng minh động học (Kinetics).

- Phải có Real Sample Analysis (Đo mẫu thực). Reviewer Q2 sẽ không tin nếu chỉ đo trong dung dịch chuẩn phòng thí nghiệm.

**Ngưỡng Q2: Bạn phải tính toán các thông số động học như:**

- Diện tích bề mặt điện hóa (ECSA): Đo CV ở nhiều tốc độ quét khác nhau (v).

- Hệ số khuếch tán (D): Dựa trên phương trình Randles–Sevcik.

- Trở kháng (Rct): Đo EIS để chứng minh phản ứng Redox diễn ra thuận lợi (vòng Nyquist nhỏ).

**3. Nhóm Q1 (Đột phá & Mô hình hóa):**

- Thường yêu cầu thêm tính toán lý thuyết (DFT) để mô phỏng cách phân tử Glucose bám vào vị trí Pyridinic-N.

- Yêu cầu độ bền cực cao (Stability test > 30 ngày).