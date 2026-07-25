# Quy tắc làm việc chung (Workspace Agent Rules)

Các quy tắc dưới đây được thiết lập để bắt buộc mọi Agent (bao gồm Antigravity, Subagents, và IDE Assistants) phải tuân thủ trong suốt quá trình xử lý dự án Carbon Aerogel, nhằm khắc phục triệt để các hạn chế về ngữ cảnh (Context Window) và tránh bỏ sót dữ liệu.

## 1. Nguyên tắc Không Tự ý Lược bỏ (No Silent Truncation)
- Khi thực hiện các tác vụ gộp file (merge/integration), nếu phát hiện nội dung dư thừa hoặc không phù hợp với văn phong hiện tại (VD: ghi chú cá nhân, dàn ý thô), Agent **tuyệt đối không được âm thầm xóa bỏ**.
- Agent phải tổng hợp các nội dung bị lược bỏ vào một danh sách (hoặc Artifact `dropped_content_log.md`) và báo cáo ngay cho người dùng để xin ý kiến (Request User Approval).

## 2. Nguyên tắc Xử lý Trích dẫn (Strict Citation Resolution)
- Mọi mã trích dẫn nội bộ (như `[P-012]`, `[P-088]`) sinh ra từ các báo cáo RAG/NotebookLM không được phép mang thẳng vào văn bản cuối cùng.
- Agent có trách nhiệm quét toàn bộ danh mục **Tài liệu tham khảo (Bibliography)** hiện có. Nếu phát hiện bài báo có nội dung trùng khớp, ưu tiên **tái sử dụng số thứ tự hiện tại**.
- Nếu không có bài nào khớp, Agent phải xin phép người dùng để tìm kiếm web (Web Search) bài báo chuẩn Q1/Q2 bù đắp, tuyệt đối không bịa số trích dẫn (hallucination).
- **Cấm cắm trích dẫn theo mức độ phù hợp thấp ("tangentially related"):** Agent chỉ được cắm trích dẫn khi mức độ liên quan là **"trực tiếp hỗ trợ claim"** (bài báo đó chứa dữ liệu hoặc lập luận cụ thể cho đúng luận điểm đang nói). Tuyệt đối không cắm chỉ vì "tác giả cùng lĩnh vực" hay "đề tài nói chung chung về chủ đề". 

## 3. Nguyên tắc Chuyển giao Bối cảnh (Context Handover Protocol)
- Khi người dùng muốn bàn giao tác vụ cho một Agent khác hoặc IDE, Agent hiện tại không chỉ viết prompt đơn thuần mà phải cung cấp **Bối cảnh Hiện trạng** chi tiết.
- Việc chia nhỏ tác vụ để tránh tràn ngữ cảnh (Context Overflow) phải được lập kế hoạch rõ ràng và thông báo trước cho người dùng.

## 4. Tôn trọng Định dạng Học thuật
- Mọi bảng biểu phải luôn dùng chuẩn Markdown Pipe Tables (`|---|---|`).
- Tuyệt đối giữ đúng định dạng ký hiệu hóa học và toán học ($Pb^{2+}, S_{BET}$, 1249 cm⁻¹). 
- Bất kỳ Agent nào phá vỡ định dạng này đều bị coi là vi phạm nghiêm trọng quy trình làm việc.

## 5. Nguyên tắc Định lượng và Can thiệp bằng Code (Chống Silent Truncation triệt để)
Để giải quyết dứt điểm rủi ro AI tự động lược bỏ (Silent Truncation) và giảm tải cho Context Window khi chỉnh sửa tài liệu lớn, mọi Agent phải tuân thủ nghiêm ngặt quy trình sau:
- **Cắm cọc tiêu & Định lượng (Outline Anchoring & Quantification):** Trước khi chỉnh sửa, Agent bắt buộc phải đếm và liệt kê các thành phần cốt lõi (ví dụ: có bao nhiêu Giai đoạn, bao nhiêu Mục) để làm hệ quy chiếu (Anchor). 
- **Can thiệp bằng Script (Script-based Editing):** Đối với các tệp tin có cấu trúc phức tạp như tài liệu Word (`.docx`), trang tính, hoặc tệp nhị phân, CẤM tự ý sinh ra (generate) văn bản mới để thay thế toàn bộ văn bản cũ. Agent BẮT BUỘC phải viết mã Python (dùng `python-docx` hoặc thư viện tương đương) để tìm đúng dòng cần sửa và thay thế (replace) chính xác tại vị trí đó. Đối với mã nguồn hoặc văn bản phẳng (`.md`, `.json`, `.txt`), ưu tiên dùng công cụ chỉnh sửa tệp tin chuyên biệt (như `replace_file_content` hoặc `multi_replace_file_content`) để tránh ghi đè toàn bộ tệp.
- **Rà soát chéo (Cross-verification):** Sau khi chạy Script hoặc thực hiện chỉnh sửa, Agent phải chủ động đếm ngược lại các "cọc tiêu" để đảm bảo 100% nội dung không bị mất mát hay nhảy cóc.

## 6. Nguyên tắc Quản trị Ngữ cảnh (Context Window Management)
Để tuyệt đối tránh việc cạn kiệt bộ nhớ dẫn đến "quên" quy tắc hoặc cắt xén câu trả lời, mọi Agent phải tuân thủ nghiêm ngặt 3 chiến lược:
- **Chừa khoảng trống trừ hao (Context Buffering):** Cấm nạp toàn bộ file kích thước lớn vào một lần. Phải dùng code (slicing) để trích xuất và chỉ nạp đúng phần (chunk) cần xử lý nhằm giữ bộ nhớ luôn ở mức an toàn.
- **Ngoại cảnh hóa bộ nhớ (Externalized Memory):** Không in dữ liệu lớn ra lịch sử chat. Phải kết xuất dữ liệu thô (raw data) ra các tệp tin tạm (scratch files hoặc .json) và dùng code để xử lý chéo.
- **Chốt trạng thái (State Checkpointing):** Mọi phát hiện, dàn ý, và thay đổi lớn phải được ghi nhận liên tục vào các tệp Artifact (như `walkthrough.md` hoặc `implementation_plan.md`) để làm "điểm neo" khôi phục ngữ cảnh khi cần thiết.

## 7. Nguyên tắc Hậu kiểm Bắt buộc (Mandatory Post-Verification Protocol)
Mọi thao tác chỉnh sửa — kể cả "sửa nhỏ" hay "chỉ thêm một trích dẫn" — đều phải có một vòng kiểm tra ngược độc lập sau khi hoàn thành. Agent nghiêm cấm tự nhận "đã sửa xong" mà không có bằng chứng hậu kiểm cụ thể:
- **Đếm trước/sau (Count Before & After):** Ghi lại số lượng trích dẫn, số đoạn văn, số ký hiệu hóa học trước khi sửa. Sau khi sửa, chạy script đếm lại và so sánh. Nếu lệch → báo cáo ngay, không tự ý giải thích.
- **Đọc lại dòng đã sửa (Re-read the Modified Line):** Sau khi sửa đổi (bằng script hoặc công cụ chỉnh sửa), dùng mã lệnh hoặc công cụ đọc tệp trích xuất lại đúng dòng/đoạn đó để in ra màn hình, xác nhận bằng đầu ra thực tế — không chỉ tin vào nhật ký thực thi "success".
- **Báo cáo công khai kết quả hậu kiểm:** Mọi báo cáo "đã hoàn thành" đều phải đính kèm output hậu kiểm rõ ràng. Câu "đã sửa thành công" mà không có bằng chứng là vi phạm quy trình.
- **Tiêu chí nguồn độc lập:** Đối với các thông số kỹ thuật hoặc phát biểu định lượng quan trọng, kết quả chỉ được coi là "đã kiểm chứng đầy đủ" khi có ít nhất $\ge 2$ nguồn độc lập hỗ trợ. Nếu chỉ có 1 nguồn duy nhất, phải gắn nhãn `[Cần xác nhận thêm]`.

## 8. Nguyên tắc Kiểm chứng Nội dung trước khi Cắm Trích dẫn (Claim-Verification-First)
Được đúc rút từ lỗi thực chiến tại Đoạn 164 Chương 1. Agent tuyệt đối không được cắm trích dẫn chỉ dựa trên tiêu đề hoặc tên tác giả:
- **Bắt buộc đọc tóm tắt (Abstract-level Verification):** Trước khi cắm, Agent phải xác định bài báo đó có chứa **dữ liệu đo thực nghiệm hoặc lập luận cơ chế cụ thể** hỗ trợ đúng luận điểm đang đề cập.
- **Phân cấp mức độ phù hợp (Domain Classification):** Phân loại nguồn thành 4 mức rõ ràng để xử lý:
  1. *Direct (Trực tiếp):* Cùng vật liệu/hệ phản ứng/kỹ thuật và cùng mục tiêu ứng dụng → Được ưu tiên trích dẫn trực tiếp để bảo vệ luận điểm.
  2. *Analogical (Gián tiếp):* Cùng vật liệu/cơ chế nhưng khác ứng dụng (ví dụ: dùng cho ORR, siêu tụ thay vì cảm biến) → Cần ghi chú rõ ràng về sự khác biệt ứng dụng khi sử dụng.
  3. *Mechanistic (Cơ chế nền):* Khác vật liệu nhưng giải thích chung một quy luật vật lý/hóa học cơ sở → Chỉ dùng để củng cố lập luận lý thuyết chung.
  4. *OUT_OF_SCOPE (Không liên quan):* Không cùng hệ vật liệu hoặc cơ chế liên quan → Tuyệt đối không cắm trích dẫn.
- **Gắn nhãn "tentative" nếu không chắc:** Nếu không đọc được nội dung đầy đủ hoặc không chắc chắn về mức độ liên quan, Agent phải ghi chú rõ `[Cần user xác nhận]` thay vì âm thầm chọn bài gần đúng nhất.

## 9. Nguyên tắc Bộ nhớ Tích lũy trong Tác vụ Dài (Incremental Memory Protocol)
Để xử lý các tác vụ có tính lặp lại (batch processing) hoặc kéo dài qua nhiều phiên làm việc mà không làm tràn ngữ cảnh:
- **Duy trì nhật ký trạng thái:** Agent phải thiết lập và duy trì một tệp trạng thái hoặc nhật ký tiến trình (ví dụ: `.json` hoặc tệp tạm) để lưu trữ danh sách các phần việc/tệp tin đã xử lý thành công kèm trạng thái `"processed": true`.
- **Tránh xử lý trùng lặp:** Agent tuyệt đối không được đọc lại hoặc thực thi lại các phần việc đã hoàn thành trong nhật ký, trừ khi có yêu cầu cấu hình lại hoặc yêu cầu trực tiếp từ người dùng.

## 10. Nguyên tắc Giới hạn Quyền quyết định (Boundary of Authority)
- Agent tuyệt đối không được tự ý sửa lỗi hoặc thay đổi dữ liệu (kể cả khi phát hiện người dùng tính toán sai hoặc lệch số thứ tự trích dẫn) nếu chưa xin phép.
- Khi phát hiện sự bất hợp lý hoặc sai lệch giữa yêu cầu của người dùng và thực tế logic của bài, Agent PHẢI:
  1. Dừng lại ngay lập tức, không được viết mã thực thi.
  2. Lập bảng đối chiếu hiện trạng, báo cáo nguyên nhân sai lệch và đề xuất giải pháp.
  3. Đặt câu hỏi xác nhận và CHỈ ĐƯỢC PHÉP thực thi khi người dùng trả lời "Đồng ý". Mọi hành động "cầm đèn chạy trước ô tô" (tự động sửa lỗi hộ) đều bị cấm.

## 11. Nguyên tắc An toàn Script Python (Python Script Safety Protocol)
Mọi script Python tạo ra để xử lý file dữ liệu phải tuân thủ:
- **Bắt buộc dùng `encoding='utf-8'` khi mở file** và `newline='\n'` khi ghi (không phụ thuộc platform).
- **Bắt buộc dùng `.encode('ascii','replace').decode('ascii')`** trước mọi lệnh `print()` có chuỗi tiếng Việt hoặc ký hiệu đặc biệt (khi in ra console để tránh UnicodeEncodeError trên Windows).
- **Bắt buộc chạy thử trên file nháp** (hoặc đoạn text nhỏ) trước khi áp dụng lên file SOP gốc.
- **CẤM dùng `text.replace('\r\n', '\n')` rồi lại `replace('\n', '\r\n')`** theo vòng lặp vì sẽ nhân đôi dòng trắng. Chỉ được phép chuẩn hóa 1 chiều duy nhất.

## 12. Nguyên tắc Thẩm định Suy luận Bắc cầu (Bridging Inference Protocol)
Mọi luận điểm (claim) dựa trên suy luận bắc cầu từ hệ dung môi khác (VD: NaOH/Urea → NH₃/Urea) hoặc ứng dụng khác (VD: ORR → GCE Sensing) đều **BẮT BUỘC** phải trải qua "Ma trận thẩm định 5 tiêu chí" trước khi được đưa vào SOP:
1. **Cơ sở Nguồn (Source Foundation):** Xác định rõ bài báo gốc đo đạc thực tế trong điều kiện nào. Tuyệt đối phân biệt giữa số liệu thực nghiệm và suy diễn từ Abstract.
2. **Phân tích Tương đồng (Mechanism Similarity):** Đánh giá % tương đồng về bản chất vật lý/hóa học giữa hệ tham chiếu và hệ mục tiêu. Nếu chỉ giống cơ chế vỏ bọc urea nhưng khác cation kiềm, phải ghi rõ giới hạn bắc cầu.
3. **Đếm Hội tụ (Convergent Evidence Count):** Bắt buộc đếm số lượng bài báo độc lập xác nhận luận điểm. Nếu $n \ge 2$: đủ hội tụ. Nếu $n = 1$: bắt buộc gắn nhãn `[Cần xác nhận thêm]`.
4. **Kiểm tra Phù hợp Ứng dụng Đích (Target Relevance Test):** Luận điểm phải có cầu nối logic trực tiếp đến hiệu năng của hệ đích (Ví dụ: diện tích bề mặt lớn → tăng pre-concentration → giảm LOD cho GCE). Nếu không có liên kết rõ ràng → loại bỏ (OUT_OF_SCOPE).
5. **Loại suy (Elimination Test):** Chủ động tìm kiếm bằng chứng phản bác (counter-evidence). Bất kỳ mâu thuẫn thực nghiệm nào (VD: nhiệt độ đông tụ sol lỏng) từ hệ thống cốt lõi sẽ lập tức phủ quyết suy luận bắc cầu.

**Quy định xử lý kết quả bắc cầu:**
- **Bắt buộc ghi chú rõ "Áp dụng tương đồng từ hệ [X]"** hoặc "Ứng dụng từ [Y] sang Sensing" trong phần biện luận. Tuyệt đối không viết như thể dữ liệu được đo trực tiếp trên hệ mục tiêu.
- Các giá trị định lượng từ hệ bắc cầu (như $E_{a,s} = -101\text{ kJ/mol}$) chỉ được dùng để củng cố **định tính** (phản ứng tỏa nhiệt), CẤM dùng như thông số định lượng tuyệt đối cho hệ mới nếu không có bằng chứng độc lập.

## 13. Nguyên tắc Đồng bộ Tài liệu Một chiều (Document Sync Directionality)
Đúc rút từ lỗi thực chiến: AI đã sửa trực tiếp file lớn (`Master_Thesis_Full_Draft.md`) trong khi hệ thống dự án vận hành theo kiến trúc compile từ các file nhỏ. Điều này gây mâu thuẫn nội dung khi chạy lại script gộp.

**Kiến trúc tệp tin của dự án:**
- **File nguồn thành phần (Source):** `Phan2_QuyTrinh_8Buoc_SOP_ChiTiet.md` và các file Phần 1, Phần 3 — đây là nơi duy nhất được phép chỉnh sửa nội dung.
- **File gộp (Compiled Output):** `Master_Thesis_Full_Draft.md` — đây là kết quả của script compile (`update_master_draft.py`), KHÔNG được chỉnh sửa trực tiếp.

**Quy tắc bắt buộc:**
- Agent **CẤM** chỉnh sửa trực tiếp vào file lớn `Master_Thesis_Full_Draft.md`. Mọi thay đổi phải thực hiện trên file nguồn nhỏ tương ứng.
- Sau khi sửa file nhỏ, Agent phải gợi ý người dùng chạy script compile (`python update_master_draft.py`) để đồng bộ sang file lớn.
- **Ngoại lệ khẩn cấp:** Nếu (vì bất kỳ lý do nào) Agent đã lỡ chỉnh sửa trực tiếp file lớn, Agent PHẢI ngay lập tức chạy script trích xuất ngược (`extract_p2_from_master.py` hoặc tương đương) để đồng bộ các thay đổi về lại file nguồn nhỏ — TRƯỚC KHI báo cáo hoàn thành. Không được để file lớn và file nhỏ bất đồng bộ.
- **Không tạo file trung gian thừa:** Cấm tạo các file snapshot hoặc bản sao tạm của file SOP trong thư mục hệ thống AI (ổ C) nếu không có mục đích so sánh rõ ràng. Nếu tạo, phải xóa ngay sau khi sử dụng xong.

## 14. Nguyên tắc Phân biệt Thông tin Mới/Cũ khi Cập nhật (Content Freshness Protocol)
Đúc rút từ câu hỏi thực chiến: "Làm sao Agent biết thông tin mình đưa vào là mới và đúng, không phải cũ và sai?" Agent phải dựa vào **3 trụ cột thẩm định** sau để đưa ra quyết định chấp nhận hoặc lọc bỏ thông tin:

**Trụ cột 1 — Hội tụ Thẻ bài báo (Paper Card Convergence):**
- Chạy script quét toàn bộ thư mục `paper_cards/` để đếm số bài báo độc lập ($n$) xác nhận một thông số/cơ chế.
- $n \ge 2$: Thông tin đủ hội tụ, được phép đưa vào. $n = 1$: Gắn nhãn `[Cần xác nhận thêm]`. $n = 0$: Nghi ngờ là hallucination, BẮT BUỘC phải truy vấn RAG Oracle trước khi đưa vào.

**Trụ cột 2 — RAG Oracle (NotebookLM):**
- Gửi truy vấn trực tiếp vào Notebook chứa PDF nguồn của dự án.
- Nếu Oracle xác nhận và cung cấp tên bài báo cụ thể: Thông tin được coi là **đúng thực tế học thuật** (nhận vào).
- Nếu Oracle phát hiện sai số định lượng (ví dụ: XPS lệch 0.2 eV): Thông tin cũ trong SOP được coi là **lệch** → hiệu chỉnh về mốc mới mà Oracle xác nhận.
- Nếu Oracle không tìm thấy bằng chứng nào và thông số đó phi logic: Thông tin được coi là **bịa (hallucination)** → loại bỏ hoàn toàn, không đưa vào.

**Trụ cột 3 — Ma trận 5 Tiêu chí Thẩm định Suy luận Bắc cầu (xem Rule 12):**
- Áp dụng để lọc các lập luận gián tiếp (Analogical/Mechanistic), không để hallucination hoặc thông tin ngoài phạm vi lọt vào SOP.

**Quy tắc phán quyết tổng hợp:**
- **PASS (Nhận vào):** Được xác nhận bởi ít nhất 2 trong 3 trụ cột.
- **REVISE (Hiệu chỉnh):** Trụ cột 2 (RAG Oracle) phát hiện sai số cụ thể → sửa về mốc đúng của Oracle, có ghi chú rõ nguồn.
- Agent phải ghi kết quả phán quyết vào báo cáo thẩm định (ví dụ: `evaluation_report_phase*.md`) trước khi thực thi bất kỳ thay đổi nào lên file SOP.

## 15. Nguyên tắc Khởi tạo và Phối hợp Kỹ năng (Skill Orchestration Protocol - SOP-SOP)
Đúc rút từ thực chiến chuẩn bị rà soát tài liệu đề cương: Để các công cụ chuyên biệt (như `md-citation-validator`, `notebooklm-mcp`, và các script Python hỗ trợ) không chạy đơn lẻ hoặc chồng chéo, mọi tác vụ rà soát hoặc cập nhật tài liệu lớn bắt buộc phải tuân theo luồng khởi tạo và phối hợp sau:
- **Bước Khởi tạo (Phase 0 - Pre-flight check):** Trước khi can thiệp bất kỳ dòng code hoặc text nào, Agent phải chạy các công cụ thống kê (ví dụ: `md-citation-validator count`) để chụp lại trạng thái nguyên bản (baseline snapshot) và ghi nhận vào một file cấu hình tiến trình (ví dụ: `de_cuong_progress.json` hoặc `task_state.json`).
- **Kết nối thông tin một chiều:** Dữ liệu đầu ra của công cụ này (như file snapshot) phải làm tham số đầu vào cho các công cụ khác (như so sánh `diff` hoặc kiểm chứng chéo).
- **Cập nhật trạng thái liên tục:** Sau mỗi Phase nhỏ được hoàn thành, Agent phải cập nhật trạng thái `"status": "done"` vào file tiến trình để làm điểm neo khôi phục ngữ cảnh (Checkpoint) phòng trường hợp token bị ngắt quãng hoặc đổi model.

