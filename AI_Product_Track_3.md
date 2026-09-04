# 📈 CHUYÊN ĐỀ ÔN TẬP: AI PRODUCT TRACK (TRACK 3) (ĐẦY ĐỦ 3 DẠNG CÂU HỎI & ĐÁP ÁN)

> Tài liệu chuyên sâu tập hợp toàn bộ các câu hỏi thuộc **Track 3: AI Product (Quản trị Sản phẩm AI, Tính toán ROI, Thẩm định thị trường, Khung pháp lý & Vòng đời sản phẩm)**.
> Bao gồm đầy đủ cả 3 loại câu hỏi: **Trắc nghiệm đơn**, **Trắc nghiệm nhiều đáp án**, và **Tự luận / Bài toán tài chính ROI**, tất cả đều đã có đáp án đúng chuẩn xác và lời giải phân tích số liệu chi tiết.

## 📑 MỤC LỤC NỘI DUNG:
1. [Phần 1: Trắc nghiệm đơn AI Product (12 câu)](#phan-1-trac-nghiem-don-ai-product)
2. [Phần 2: Trắc nghiệm nhiều đáp án AI Product (3 câu)](#phan-2-trac-nghiem-nhieu-dap-an-ai-product)
3. [Phần 3: Tự luận, Bài toán Tài chính ROI, Sự cố Vận hành & Khung Đánh giá Khoa học (4 bài)](#phan-3-tu-luan-ai-product)

---

<a id='phan-1-trac-nghiem-don-ai-product'></a>
## 1. PHẦN 1: TRẮC NGHIỆM ĐƠN (1 ĐÁP ÁN ĐÚNG) - 12 CÂU

### Câu 1: Theo AI Readiness Checklist, bài toán nào phù hợp nhất để dùng AI (Go decision)?

- [ ] **A. Tính toán lương nhân viên theo công thức cố định**
- [x] **B. Phân tích sentiment của 10,000 feedback khách hàng mỗi ngày**
- [ ] **C. Kiểm tra xem form có đủ trường bắt buộc không**
- [ ] **D. Hiển thị danh sách sản phẩm theo category**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Phân tích sắc thái của lượng lớn văn bản phi cấu trúc là bài toán phức tạp mà thuật toán truyền thống khó giải quyết hiệu quả, đây là bài toán lý tưởng (Go decision) cho AI.

---

### Câu 2: Khi đánh giá ROI 3 kịch bản cho AI investment, kịch bản nào thường cho ROI cao nhất nhanh nhất?

- [ ] **A. Kịch bản worst case — để manage risk**
- [ ] **B. Kịch bản best case để thuyết phục stakeholder**
- [x] **C. Kịch bản realistic/base case với rõ assumptions và timeline cụ thể**
- [ ] **D. Không cần ROI — AI là strategic investment**

👉 **Đáp án đúng:** `C`
💡 **Giải thích chuyên môn:** Trong thẩm định tài chính đầu tư AI, kịch bản Realistic (Base case) với giả định minh bạch và mốc thời gian rõ ràng là cơ sở vững chắc nhất để đo lường tỷ suất hoàn vốn đáng tin cậy.

---

### Câu 3: Tình huống: BLEU = 0.74 (tốt), nhưng user satisfaction chỉ 3.1/10. Root cause khả năng cao nhất là gì?

- [ ] **A. Implementation lỗi — BLEU bị tính sai, cần audit lại evaluation script**
- [x] **B. BLEU đo lexical overlap với reference answers, không đo khả năng solve problem thực tế; metric không align với North Star Metric (task completion / customer satisfaction)**
- [ ] **C. Model sinh ra câu trả lời quá ngắn**
- [ ] **D. Người dùng đánh giá quá khắt khe**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** BLEU là chỉ số đo độ trùng lặp từ vựng (n-gram overlap) trong dịch máy, không phản ánh được tính chính xác về logic hay mức độ giải quyết được vấn đề thực tế của khách hàng.

---

### Câu 4: Luật TTNT VN 2025 (Luật Trí tuệ Nhân tạo Việt Nam) yêu cầu gì đối với high-risk AI systems?

- [ ] **A. Chỉ cần đăng ký với Bộ TTTT**
- [x] **B. Yêu cầu đánh giá rủi ro trước khi deploy, logging và audit trail, transparency với người dùng (phải biết đây là AI), và human oversight mechanism cho quyết định quan trọng**
- [ ] **C. Không có yêu cầu cụ thể cho high-risk AI**
- [ ] **D. Chỉ cần comply với EU AI Act là đủ**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Các hệ thống AI rủi ro cao bắt buộc phải tuân thủ đánh giá an toàn trước triển khai, lưu vết kiểm toán, minh bạch thông tin và có sự giám sát của con người (human oversight).

---

### Câu 5: Khi present AI project cho C-suite, frame nào hiệu quả nhất?

- [ ] **A. Explain kỹ technical architecture**
- [x] **B. Frame theo business outcomes: cost savings, revenue impact, risk reduction — với specific numbers và timeline**
- [ ] **C. Benchmark so với competitor AI capabilities**
- [ ] **D. Demo technical features**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Lãnh đạo cấp cao (C-suite) quan tâm trực tiếp tới tác động kinh doanh: tiết kiệm chi phí, thúc đẩy doanh thu, giảm thiểu rủi ro kèm số liệu định lượng và mốc thời gian cụ thể.

---

### Câu 6: Hidden assumptions trong first product definition nguy hiểm vì sao?

- [ ] **A. Assumptions không cần validate nếu có experience**
- [x] **B. Assumptions ngầm không được test → build product cho thị trường không tồn tại hoặc sai target segment**
- [ ] **C. Assumptions chỉ xuất hiện ở startup, không phải enterprise**
- [ ] **D. Assumptions có thể fix sau khi launch**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Các giả định ngầm không được kiểm chứng sẽ dẫn đến việc xây dựng sản phẩm dựa trên nhu cầu ảo, gây lãng phí toàn bộ chi phí kỹ thuật cho phân khúc khách hàng không phù hợp.

---

### Câu 7: Tại sao AI adoption trong enterprise thường chậm hơn so với expectation?

- [ ] **A. Technology chưa đủ mature**
- [x] **B. Change management: người dùng lo ngại mất việc, thiếu training, workflow integration phức tạp, và trust building cần thời gian**
- [ ] **C. Budget không đủ**
- [ ] **D. IT security quá strict**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Rào cản lớn nhất trong doanh nghiệp là quản trị thay đổi (change management), bao gồm văn hóa tiếp nhận, đào tạo nhân sự, tích hợp quy trình làm việc và xây dựng niềm tin vào công nghệ mới.

---

### Câu 8: Market analysis cho AI product cần tập trung vào điều gì ngoài market size?

- [ ] **A. Chỉ cần biết TAM/SAM/SOM**
- [x] **B. Timing (thị trường đã ready chưa?), competition moats, customer adoption barriers, và regulatory landscape**
- [ ] **C. Geography và demographics**
- [ ] **D. Số lượng competitors**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Thị trường AI đòi hỏi đánh giá toàn diện về tính thời điểm (Timing), hào lũy cạnh tranh (Moats), rào cản ứng dụng của khách hàng và khung khổ pháp lý.

---

### Câu 9: Khi build financial model cho AI investment, baseline quan trọng nhất cần establish là gì?

- [ ] **A. Total cost của AI project**
- [x] **B. Current cost/time của process sẽ bị AI replace — để tính delta (savings/improvements)**
- [ ] **C. Market size của opportunity**
- [ ] **D. Competitor AI spending**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Phải có đường cơ sở (baseline) là chi phí và thời gian hiện tại của quy trình thủ công thì mới đo lường được giá trị chênh lệch (delta) mà AI đem lại.

---

### Câu 10: EU AI Act phân loại AI systems thành mấy risk levels?

- [ ] **A. 2 — Safe và Unsafe**
- [ ] **B. 3 — Low, Medium, High**
- [x] **C. 4 — Minimal/No risk, Limited risk, High risk, Unacceptable risk**
- [ ] **D. 5 levels**

👉 **Đáp án đúng:** `C`
💡 **Giải thích chuyên môn:** Đạo luật EU AI Act phân cấp thành 4 cấp độ rủi ro: Rủi ro không thể chấp nhận (bị cấm), Rủi ro cao, Rủi ro hạn chế (yêu cầu minh bạch), và Rủi ro tối thiểu.

---

### Câu 11: AI Roadmap execution khác software roadmap ở điểm nào quan trọng nhất?

- [ ] **A. AI roadmap dài hơn**
- [x] **B. AI roadmap phải tích hợp eval gates (quality thresholds) và data milestones — không chỉ feature delivery**
- [ ] **C. AI roadmap không cần stakeholder buy-in**
- [ ] **D. AI roadmap phải include research phase**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Lộ trình phát triển AI phụ thuộc vào tính bất định của mô hình, do đó bắt buộc phải có các cổng đánh giá chất lượng (eval gates) và các cột mốc làm sạch/bổ sung dữ liệu trước khi bàn giao tính năng.

---

### Câu 12: Tình huống: Data thu thập từ Web form và Email chỉ phản ánh phàn nàn. Đây là loại data quality issue nào và cách fix phù hợp?

- [ ] **A. Data completeness issue — thiếu data từ kênh call center; cần thêm call center transcripts vào pipeline**
- [x] **B. Selection bias — web form và email chỉ capture negative feedback (triggered by problems); kết quả không đại diện cho toàn bộ khách hàng**
- [ ] **C. Data consistency issue — format và ngôn ngữ không nhất quán giữa 3 nguồn, cần chuẩn hóa**
- [ ] **D. Model bias — sentiment model được train trên data tiếng Anh, không**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Đây là hiện tượng thiên lệch chọn mẫu (Selection Bias): chỉ những khách hàng gặp sự cố mới chủ động điền form/gửi email, dẫn đến tập dữ liệu bị nghiêng nặng về tiêu cực.

---

<a id='phan-2-trac-nghiem-nhieu-dap-an-ai-product'></a>
## 2. PHẦN 2: TRẮC NGHIỆM NHIỀU ĐÁP ÁN ĐÚNG - 3 CÂU

### Câu 1: Những tình huống nào dưới đây phù hợp với RAG hơn so với Fine-tuning? (Chọn tất cả đáp án đúng)

- [x] **A. Agent cần trả lời từ tài liệu nội bộ công ty được cập nhật hàng tuần**
- [ ] **B. Cần model học phong cách viết thương hiệu đặc thù và nhất quán**
- [x] **C. Agent cần truy xuất chính xác từ knowledge base pháp lý hơn 50.000 trang**
- [ ] **D. Cần model hiểu sâu thuật ngữ y tế chuyên biệt (ICD codes, clinical notes)**
- [x] **E. Agent cần biết giá sản phẩm real-time từ catalog cập nhật liên tục**

👉 **Đáp án đúng:** `A, C, E`
💡 **Giải thích chuyên môn:** RAG vượt trội khi: dữ liệu cập nhật liên tục (A, E), và cần truy xuất chính xác kèm trích dẫn trên kho tri thức khổng lồ (C). Trong khi đó, Fine-tuning phù hợp hơn để định hình văn phong (B) hoặc học ngữ pháp/thuật ngữ miền sâu (D).

---

### Câu 2: Những kỹ thuật nào dưới đây là guardrail hợp lệ cho AI agent trong production? (Chọn tất cả đáp án đúng)

- [x] **A. Input validation: detect và block prompt injection patterns trước khi đưa vào LLM**
- [x] **B. Output validation: scan response có PII (tên, số điện thoại, CCCD) trước khi trả về user**
- [ ] **C. Tăng temperature lên 1.8 để model 'suy nghĩ đa dạng hơn' và tránh bị jailbreak**
- [x] **D. Human-in-the-loop: yêu cầu human approve khi action có tác động cao (gửi email hàng loạt, xóa data)**
- [x] **E. Rate limiting: giới hạn số lượng requests/phút từ một user để tránh abuse và kiểm soát chi phí**

👉 **Đáp án đúng:** `A, B, D, E`
💡 **Giải thích chuyên môn:** Các chốt chặn bảo vệ chuẩn production bao gồm lọc dữ liệu đầu vào (A), ẩn danh hóa thông tin nhạy cảm đầu ra (B), phê duyệt của con người cho tác vụ nguy hiểm (D) và giới hạn tần suất truy cập (E). Phương án C sai hoàn toàn vì tăng nhiệt độ lên 1.8 sẽ gây ảo giác nặng và mất kiểm soát.

---

### Câu 3: Những metrics nào cần monitor cho AI agent trong production? (Chọn tất cả đáp án đúng)

- [x] **A. Latency P50 và P99 (percentile) của mỗi request**
- [x] **B. Token cost per request (input tokens + output tokens × đơn giá model)**
- [ ] **C. Số lần model weights được updated trong ngày**
- [x] **D. Error rate: tool call failures, JSON parsing errors, timeouts**
- [x] **E. Task completion rate: % requests đạt được Final Answer thành công**

👉 **Đáp án đúng:** `A, B, D, E`
💡 **Giải thích chuyên môn:** Giám sát AI production cần theo dõi độ trễ (A), chi phí token (B), tỷ lệ lỗi gọi công cụ/phân tích cú pháp (D) và tỷ lệ hoàn thành tác vụ thành công (E). Trọng số mô hình nền tảng qua API không được cập nhật từng ngày (C sai).

---

<a id='phan-3-tu-luan-ai-product'></a>
## 3. PHẦN 3: TỰ LUẬN, BÀI TOÁN TÀI CHÍNH ROI, SỰ CỐ VẬN HÀNH & KHUNG ĐÁNH GIÁ - 4 BÀI

### Bài 1 (Sắp xếp quy trình):
**Nội dung câu hỏi:**
Sắp xếp các giai đoạn trong AI Product Lifecycle theo đúng thứ tự phát triển sản phẩm:
[A] Monitor — theo dõi performance, cost, errors trong production
[B] Build & Prototype — xây dựng MVP agent, lab thực hành
[C] Problem Scoping — xác định bài toán kinh doanh, stakeholders, ROI target
[D] Test & Evaluate — chạy eval pipeline, đo metrics, tìm failure cases
[E] Deploy — containerize, CI/CD, release lên production

**Lời giải / Đáp án kỹ thuật chi tiết:**
**Thứ tự sắp xếp đúng:**
**C → B → D → E → A**
1. [C] Problem Scoping (Xác định bài toán, ROI)
2. [B] Build & Prototype (Xây dựng MVP)
3. [D] Test & Evaluate (Đánh giá và kiểm thử chất lượng)
4. [E] Deploy (Đóng gói và triển khai)
5. [A] Monitor (Giám sát vận hành trong thực tế)

---

### Bài 2 (Bài toán tình huống ROI CSKH):
**Nội dung câu hỏi:**
Bạn là AI Product Manager tại công ty logistics 500 nhân viên. CSKH hiện có 8 người xử lý 1.200 ticket/ngày, mỗi ticket trung bình 6 phút, lương trung bình 12 triệu/tháng. Đề xuất deploy AI Agent: xử lý tự động 60% ticket đơn giản, 40% còn lại hỗ trợ giảm thời gian từ 6 phút xuống 3 phút. Chi phí build: 200 triệu (một lần). Chi phí vận hành AI: 15 triệu/tháng.

**Chi tiết từng câu hỏi con & Lời giải chuẩn:**
- **Ý 1: Nêu 2 hidden cost/risk quan trọng mà financial model trên CHƯA tính đến.**
  👉 **Trả lời:** 1. Chi phí xử lý sự cố và đền bù khách hàng khi AI đưa ra thông tin sai (Hallucination risk / Error cost).
2. Chi phí bảo trì dữ liệu, cập nhật knowledge base định kỳ và đào tạo lại nhân viên làm quen với công cụ mới (Change management & continuous data curation cost).

- **Ý 2: Tính cost saving hàng tháng từ việc giảm workload nhân viên CSKH (giả sử quy đổi theo giờ công lao động).**
  👉 **Trả lời:** **Lời giải chi tiết:**
- Tổng thời gian ban đầu: 1.200 ticket × 6 phút = 7.200 phút/ngày = 120 giờ/ngày (Mỗi người làm 15 giờ/ngày -> tương đương quy mô đang quá tải).
- Thời gian sau khi có AI:
  + 60% ticket giải quyết tự động = 0 phút.
  + 40% ticket còn lại (480 ticket) × 3 phút = 1.440 phút/ngày = 24 giờ/ngày.
- Tỷ lệ thời gian tiết kiệm: (120 - 24) / 120 = 80% workload được giải phóng.
- Tổng quỹ lương hiện tại: 8 người × 12 triệu = 96 triệu/tháng.
- Giá trị thời gian tiết kiệm được quy đổi: 96 triệu × 80% = **76,8 triệu đồng/tháng** (hoặc nếu giảm biên chế tương ứng).

- **Ý 3: Tính ROI tháng 12 (sau 1 năm vận hành). Dự án có đáng đầu tư không?**
  👉 **Trả lời:** **Lời giải chi tiết:**
- Tổng chi phí đầu tư sau 1 năm (Cost):
  + Vốn đầu tư ban đầu: 200 triệu
  + Chi phí vận hành 12 tháng: 15 triệu × 12 = 180 triệu
  => Tổng chi phí (Total Cost) = 200 + 180 = **380 triệu đồng**.
- Tổng giá trị tiết kiệm sau 1 năm (Gross Benefit):
  + 76,8 triệu × 12 tháng = **921,6 triệu đồng**.
- Lợi nhuận ròng (Net Profit) = 921,6 - 380 = **541,6 triệu đồng**.
- Tỷ suất hoàn vốn: **ROI = (541,6 / 380) × 100% ≈ 142,5%**.
- **Kết luận:** Dự án **RẤT ĐÁNG ĐẦU TƯ** vì ROI đạt trên 140% và thời gian hòa vốn chỉ khoảng 5 - 6 tháng.

---

### Bài 3 (Bài toán sự cố triển khai E-commerce):
**Nội dung câu hỏi:**
Tình huống: Team AI của e-commerce platform nâng cấp chatbot từ GPT-3.5 lên GPT-4o vào 17h thứ Sáu. Sau triển khai: (1) Latency tăng từ 800ms lên 2.4s, (2) Token cost tăng 6x, (3) Output format thay đổi làm gãy parser một số dịch vụ downstream.

**Chi tiết từng câu hỏi con & Lời giải chuẩn:**
- **Ý 1: Phân tích các sai lầm trong quá trình triển khai.**
  👉 **Trả lời:** 1. Vi phạm nguyên tắc 'Never deploy on Friday evening': Triển khai vào chiều thứ Sáu khiến team không kịp ứng cứu sự cố cuối tuần.
2. Không chạy kiểm thử hồi quy (Regression test) và Eval gate: Không đo lường benchmark độ trễ và chi phí trước khi release.
3. Thiếu schema validation / output contract: Model mới sinh format khác làm crash backend của downstream services.

- **Ý 2: Cost tăng 6x có thể chấp nhận được không? Đề xuất cách quyết định.**
  👉 **Trả lời:** Chi phí tăng 6x chỉ được chấp nhận nếu tỷ lệ hoàn thành tác vụ (Task Completion Rate) tăng đáng kể và giảm tỷ lệ phàn nàn, bù đắp được chi phí. Đề xuất: Phân luồng câu hỏi (Model Routing) — dùng model nhỏ giá rẻ (GPT-4o-mini) cho 80% câu hỏi dễ và chỉ route câu hỏi khó sang GPT-4o.

- **Ý 3: Thiết kế CI/CD pipeline đúng cho lần upgrade model tiếp theo.**
  👉 **Trả lời:** Pipeline chuẩn: (1) Code/Prompt Commit → (2) Unit Tests & Schema Check → (3) Offline Evaluation trên tập Golden Dataset đo Faithfulness/Accuracy → (4) Cost & Latency Benchmark Gate → (5) Canary Release (10% traffic) có giám sát Real-time Metrics → (6) Full Rollout.

---

### Bài 4 (Bài toán kiểm định trước Production):
**Nội dung câu hỏi:**
Tình huống: Sau 2 tuần demo agent CSKH bảo hành, Tech Lead yêu cầu bằng chứng khoa học cụ thể trước khi đưa vào Production. Team có 500 câu hỏi thực tế từ 3 tháng qua, tài liệu đầy đủ và ngân sách kiểm thử.

**Chi tiết từng câu hỏi con & Lời giải chuẩn:**
- **Ý 1: Thiết kế bộ dữ liệu kiểm thử (Evaluation Dataset).**
  👉 **Trả lời:** Từ 500 câu hỏi thực tế, lọc chọn ra 150 - 200 câu hỏi đa dạng đại diện cho các nhóm: câu hỏi chuẩn có trong tài liệu (happy path), câu hỏi ngoài phạm vi chính sách (out-of-domain), câu hỏi mơ hồ và các câu hỏi cố tình công kích (adversarial / prompt injection). Gán nhãn Ground Truth chuẩn bởi chuyên viên CSKH cấp cao.

- **Ý 2: Chọn khung đánh giá và các chỉ số đo lường.**
  👉 **Trả lời:** Áp dụng khung RAGAS kết hợp LLM-as-a-Judge:
- **Faithfulness:** Kiểm tra câu trả lời có trung thực với tài liệu bảo hành không (chống bịa đặt).
- **Answer Relevance:** Đo mức độ trả lời đúng trọng tâm câu hỏi của khách.
- **Context Precision & Recall:** Đo lường độ chính xác của tầng truy xuất dữ liệu.

- **Ý 3: Tiêu chuẩn Pass/Fail để đủ điều kiện Production.**
  👉 **Trả lời:** - Faithfulness score $\ge$ 0.95 (tuyệt đối hạn chế ảo giác chính sách).
- Answer Relevance $\ge$ 0.90.
- Tỷ lệ vi phạm an toàn / lọt prompt injection = 0%.
- Latency P99 $\le$ 3.0s.

---

