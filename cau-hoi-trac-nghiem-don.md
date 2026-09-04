# 📌 PHẦN 1: CÂU HỎI TRẮC NGHIỆM ĐƠN (1 ĐÁP ÁN ĐÚNG)

> Tổng số câu: **47 câu** (đã lọc sạch 100% trùng lặp).
> Quy ước: Ký hiệu `[x]` thể hiện phương án đúng, đi kèm giải thích chuyên môn ngắn gọn.

---

### Câu 1: Bạn muốn build một hệ thống tự động phân loại email support thành 5 categories. Nhóm AI nào phù hợp nhất?

- [ ] **A. Agentic AI — vì cần nhiều bước phức tạp**
- [x] **B. Discriminative AI — vì đây là bài toán phân loại có output cố định**
- [ ] **C. Generative AI — vì cần sinh response tự động**
- [ ] **D. Rule-based Bot — vì email support có pattern cố định**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Phân loại email vào 5 nhóm cố định là bài toán Classification truyền thống, đầu ra là nhãn cố định (fixed categories), do đó Discriminative AI là tối ưu, tiết kiệm chi phí và chính xác nhất mà không cần sinh văn bản mới.

---

### Câu 2: Tại sao 'Garbage In, Garbage Out' quan trọng hơn khi nói về data cho AI agent?

- [ ] **A. AI models nhạy cảm hơn traditional ML với data quality**
- [x] **B. Nếu data bẩn (OCR lỗi, metadata thiếu, policy cũ), agent sẽ hallucinate và trả lời sai dù model mạnh — đổi model đắt hơn không fix được data bẩn**
- [ ] **C. AI cần nhiều data hơn traditional ML**
- [ ] **D. Data cleaning tốn kém hơn**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Với LLM/Agent, nếu dữ liệu nạp vào (retrieval context) bị sai lệch, thiếu sót hoặc lỗi thời, model dù thông minh đến đâu cũng sẽ bị hallucinate theo ngữ cảnh đó. Nâng cấp model không giải quyết được gốc rễ dữ liệu bẩn.

---

### Câu 3: Khi expose AI agent như REST API, những consideration nào quan trọng nhất?

- [ ] **A. Chỉ cần GET và POST endpoints**
- [x] **B. Authentication/authorization (ai được gọi), rate limiting (tránh abuse), streaming response (UX tốt hơn), timeout handling, và versioning (/v1/ để backward compat)**
- [ ] **C. Chỉ cần HTTPS**
- [ ] **D. Chỉ cần JSON format**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Đây là các tiêu chuẩn production API cho AI: kiểm soát bảo mật (AuthN/AuthZ), chống quá tải chi phí (Rate Limit), cải thiện thời gian phản hồi (Streaming SSE), quản lý ngắt kết nối LLM (Timeout) và duy trì tương thích (Versioning).

---

### Câu 4: Prompt injection attack hoạt động như thế nào?

- [ ] **A. Inject malicious code vào Python environment**
- [x] **B. User thêm instruction vào input để override system prompt và khiến agent làm việc nguy hiểm**
- [ ] **C. Gửi quá nhiều tokens để crash context window**
- [ ] **D. Intercept API call giữa client và server**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Prompt injection là kỹ thuật tấn công tầng ngữ nghĩa (semantic attack), kẻ tấn công lồng các câu chỉ thị vào nội dung nhập vào nhằm ghi đè các giới hạn trong system prompt ban đầu của agent.

---

### Câu 5: Track chuyên sâu của bạn là gì?

- [x] **A. AI Applications**
- [ ] **B. AI Infrastructure**
- [ ] **C. AI Product**

👉 **Đáp án đúng:** `A / B / C (Tùy chọn định hướng học viên)`
💡 **Giải thích:** Câu hỏi phân loại định hướng chuyên môn của học viên trong chương trình đào tạo.

---

### Câu 6: Trong Supervisor-worker pattern, Supervisor có trách nhiệm chính là gì?

- [ ] **A. Thực hiện tất cả tasks**
- [x] **B. Nhận task, route đúng worker, và tổng hợp kết quả**
- [ ] **C. Monitor system health**
- [ ] **D. Handle errors và retry**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Mô hình Supervisor đóng vai trò điều phối trung tâm: phân tích nhiệm vụ tổng thể, định tuyến đến worker chuyên trách phù hợp và thu thập, tổng hợp kết quả cuối cùng.

---

### Câu 7: Khi agent trả lời đúng fact nhưng là fact cũ (stale), symptom này chỉ ra lỗi ở tầng nào?

- [ ] **A. Model quality**
- [ ] **B. Prompt engineering**
- [x] **C. Freshness — publish pipeline hoặc cache vector bị stale**
- [ ] **D. Retrieval ranking**

👉 **Đáp án đúng:** `C`
💡 **Giải thích:** Dữ liệu trả lời đúng logic nhưng chứa thông tin lỗi thời phản ánh vấn đề độ tươi mới của dữ liệu (Data Freshness), do pipeline cập nhật vector store bị trễ hoặc cache chưa được invalidate.

---

### Câu 8: Prompt grounding trong Generation stage nghĩa là gì?

- [ ] **A. Viết prompt ngắn gọn**
- [x] **B. Hướng dẫn model chỉ trả lời từ retrieved context, citation rõ nguồn, và nói 'không biết' khi thiếu chứng cứ**
- [ ] **C. Dùng system prompt để set role**
- [ ] **D. Grounding là quá trình training model với domain data**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Grounding là ràng buộc câu trả lời của model gắn chặt với tài liệu được truy xuất (retrieved context), bắt buộc trích dẫn nguồn và từ chối suy đoán khi dữ liệu không hỗ trợ.

---

### Câu 9: AI-specific metrics quan trọng nhất cần monitor cho LLM agent là gì?

- [ ] **A. CPU usage và memory**
- [x] **B. TTFT (Time to First Token), Quality score, Cost per request, Drift (model/data)**
- [ ] **C. HTTP response codes và uptime**
- [ ] **D. Database query time**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Các chỉ số đặc thù của LLM gồm: Tốc độ phản hồi token đầu tiên (TTFT), điểm chất lượng câu trả lời (Quality/Eval), chi phí token trên mỗi request (Cost per request) và hiện tượng trôi dạt ngữ nghĩa/phân phối dữ liệu (Drift).

---

### Câu 10: Theo AI Readiness Checklist, bài toán nào phù hợp nhất để dùng AI (Go decision)?

- [ ] **A. Tính toán lương nhân viên theo công thức cố định**
- [x] **B. Phân tích sentiment của 10,000 feedback khách hàng mỗi ngày**
- [ ] **C. Kiểm tra xem form có đủ trường bắt buộc không**
- [ ] **D. Hiển thị danh sách sản phẩm theo category**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Phân tích sắc thái của lượng lớn văn bản phi cấu trúc là bài toán phức tạp mà thuật toán truyền thống khó giải quyết hiệu quả, đây là bài toán lý tưởng (Go decision) cho AI.

---

### Câu 11: Semantic caching là cost optimization strategy như thế nào?

- [ ] **A. Cache LLM responses cho exact same queries**
- [x] **B. Cache LLM responses cho semantically similar queries — 'hủy đơn hàng' và 'cancel order' nhận cùng response**
- [ ] **C. Compress prompt để giảm tokens**
- [ ] **D. Dùng cheaper model cho tất cả queries**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Semantic caching dùng vector similarity để nhận diện các câu hỏi tương đồng về mặt ý nghĩa (dù từ ngữ khác nhau) và trả về kết quả đã cache sẵn, giúp tiết kiệm chi phí gọi LLM.

---

### Câu 12: Khi đánh giá ROI 3 kịch bản cho AI investment, kịch bản nào thường cho ROI cao nhất nhanh nhất?

- [ ] **A. Kịch bản worst case — để manage risk**
- [ ] **B. Kịch bản best case để thuyết phục stakeholder**
- [x] **C. Kịch bản realistic/base case với rõ assumptions và timeline cụ thể**
- [ ] **D. Không cần ROI — AI là strategic investment**

👉 **Đáp án đúng:** `C`
💡 **Giải thích:** Trong thẩm định tài chính đầu tư AI, kịch bản Realistic (Base case) với giả định minh bạch và mốc thời gian rõ ràng là cơ sở vững chắc nhất để đo lường tỷ suất hoàn vốn đáng tin cậy.

---

### Câu 13: Prompt kém: 'Viết email cho tôi'. Prompt tốt theo framework RTCF là gì?

- [ ] **A. Viết một email rất hay và professional**
- [x] **B. Viết email xin lỗi khách hàng về giao hàng trễ 2 ngày, tone lịch sự, dưới 120 từ, có CTA rõ ràng**
- [ ] **C. Bạn là email writer. Viết email.**
- [ ] **D. Hãy là một professional email writer và viết email tốt nhất có thể**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Khung RTCF bao gồm Role (Vai trò), Task (Nhiệm vụ), Context (Ngữ cảnh: trễ 2 ngày), Constraints (Ràng buộc: dưới 120 từ, lịch sự), Format (CTA rõ ràng).

---

### Câu 14: ML (Machine Learning) là một tập con của Deep Learning.

- [ ] **A. True**
- [x] **B. False**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Deep Learning là tập con của Machine Learning (ML bao gồm cả hồi quy, SVM, random forest, cây quyết định và Deep Learning).

---

### Câu 15: LLM-as-a-Judge có thể thay thế hoàn toàn human evaluation trong mọi trường hợp.

- [ ] **A. True**
- [x] **B. False**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** LLM-as-a-Judge không thể thay thế con người hoàn toàn, đặc biệt trong các kịch bản rủi ro cao (y tế, pháp lý), các trường hợp đánh giá thẩm mỹ chủ quan và để hiệu chuẩn (calibrate) chính ban giám khảo LLM.

---

### Câu 16: Prompt injection và jailbreaking là cùng một loại attack.

- [ ] **A. True**
- [x] **B. False**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Đây là hai loại tấn công khác nhau: Prompt Injection nhằm phá vỡ logic/nhiệm vụ của ứng dụng (ghi đè prompt của hệ thống), còn Jailbreaking nhằm phá bỏ các rào cản an toàn đạo đức cốt lõi của nhà phát triển mô hình.

---

### Câu 17: Trong RAG system, nếu agent trả lời sai, bước đầu tiên nên làm là upgrade lên model mạnh hơn (ví dụ: từ GPT-4o sang GPT-4o-mini sang Claude).

- [ ] **A. True**
- [x] **B. False**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Bước đầu tiên phải là kiểm tra và debug pipeline RAG: xem tài liệu truy xuất có chính xác không (retrieval quality), chunking có bị cắt cụt không, trước khi đổi model đắt tiền hơn.

---

### Câu 18: Tình huống ReAct: Tool schema chỉ có name và description, LLM gọi tool với empty args và fail, tăng temp từ 0 lên 0.8 không giải quyết được. Root cause khả năng cao nhất là gì?

- [ ] **A. ReAct loop implementation sai — cần parser mạnh hơn để extract action từ LLM output**
- [x] **B. Tool schema thiếu 'parameters' field — LLM không biết phải truyền argument nào; temperature không liên quan đến vấn đề này**
- [ ] **C. LLM cần được fine-tune với domain data sản phẩm mới hiểu cách dùng tool**
- [ ] **D. Agent cần thêm few-shot examples trong system prompt để học cách gọi tool**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Khi Tool schema không định nghĩa rõ trường parameters (các tham số và kiểu dữ liệu), LLM không thể suy luận chính xác cấu trúc tham số để truyền vào, dẫn đến gọi hàm rỗng.

---

### Câu 19: Tình huống: BLEU = 0.74 (tốt), nhưng user satisfaction chỉ 3.1/10. Root cause khả năng cao nhất là gì?

- [ ] **A. Implementation lỗi — BLEU bị tính sai, cần audit lại evaluation script**
- [x] **B. BLEU đo lexical overlap với reference answers, không đo khả năng solve problem thực tế; metric không align với North Star Metric (task completion / customer satisfaction)**
- [ ] **C. Model sinh ra câu trả lời quá ngắn**
- [ ] **D. Người dùng đánh giá quá khắt khe**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** BLEU là chỉ số đo độ trùng lặp từ vựng (n-gram overlap) trong dịch máy, không phản ánh được tính chính xác về logic hay mức độ giải quyết được vấn đề thực tế của khách hàng.

---

### Câu 20: Luật TTNT VN 2025 (Luật Trí tuệ Nhân tạo Việt Nam) yêu cầu gì đối với high-risk AI systems?

- [ ] **A. Chỉ cần đăng ký với Bộ TTTT**
- [x] **B. Yêu cầu đánh giá rủi ro trước khi deploy, logging và audit trail, transparency với người dùng (phải biết đây là AI), và human oversight mechanism cho quyết định quan trọng**
- [ ] **C. Không có yêu cầu cụ thể cho high-risk AI**
- [ ] **D. Chỉ cần comply với EU AI Act là đủ**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Các hệ thống AI rủi ro cao bắt buộc phải tuân thủ đánh giá an toàn trước triển khai, lưu vết kiểm toán, minh bạch thông tin và có sự giám sát của con người (human oversight).

---

### Câu 21: Khi present AI project cho C-suite, frame nào hiệu quả nhất?

- [ ] **A. Explain kỹ technical architecture**
- [x] **B. Frame theo business outcomes: cost savings, revenue impact, risk reduction — với specific numbers và timeline**
- [ ] **C. Benchmark so với competitor AI capabilities**
- [ ] **D. Demo technical features**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Lãnh đạo cấp cao (C-suite) quan tâm trực tiếp tới tác động kinh doanh: tiết kiệm chi phí, thúc đẩy doanh thu, giảm thiểu rủi ro kèm số liệu định lượng và mốc thời gian cụ thể.

---

### Câu 22: Hidden assumptions trong first product definition nguy hiểm vì sao?

- [ ] **A. Assumptions không cần validate nếu có experience**
- [x] **B. Assumptions ngầm không được test → build product cho thị trường không tồn tại hoặc sai target segment**
- [ ] **C. Assumptions chỉ xuất hiện ở startup, không phải enterprise**
- [ ] **D. Assumptions có thể fix sau khi launch**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Các giả định ngầm không được kiểm chứng sẽ dẫn đến việc xây dựng sản phẩm dựa trên nhu cầu ảo, gây lãng phí toàn bộ chi phí kỹ thuật cho phân khúc khách hàng không phù hợp.

---

### Câu 23: Tại sao AI adoption trong enterprise thường chậm hơn so với expectation?

- [ ] **A. Technology chưa đủ mature**
- [x] **B. Change management: người dùng lo ngại mất việc, thiếu training, workflow integration phức tạp, và trust building cần thời gian**
- [ ] **C. Budget không đủ**
- [ ] **D. IT security quá strict**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Rào cản lớn nhất trong doanh nghiệp là quản trị thay đổi (change management), bao gồm văn hóa tiếp nhận, đào tạo nhân sự, tích hợp quy trình làm việc và xây dựng niềm tin vào công nghệ mới.

---

### Câu 24: Market analysis cho AI product cần tập trung vào điều gì ngoài market size?

- [ ] **A. Chỉ cần biết TAM/SAM/SOM**
- [x] **B. Timing (thị trường đã ready chưa?), competition moats, customer adoption barriers, và regulatory landscape**
- [ ] **C. Geography và demographics**
- [ ] **D. Số lượng competitors**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Thị trường AI đòi hỏi đánh giá toàn diện về tính thời điểm (Timing), hào lũy cạnh tranh (Moats), rào cản ứng dụng của khách hàng và khung khổ pháp lý.

---

### Câu 25: Khi build financial model cho AI investment, baseline quan trọng nhất cần establish là gì?

- [ ] **A. Total cost của AI project**
- [x] **B. Current cost/time của process sẽ bị AI replace — để tính delta (savings/improvements)**
- [ ] **C. Market size của opportunity**
- [ ] **D. Competitor AI spending**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Phải có đường cơ sở (baseline) là chi phí và thời gian hiện tại của quy trình thủ công thì mới đo lường được giá trị chênh lệch (delta) mà AI đem lại.

---

### Câu 26: EU AI Act phân loại AI systems thành mấy risk levels?

- [ ] **A. 2 — Safe và Unsafe**
- [ ] **B. 3 — Low, Medium, High**
- [x] **C. 4 — Minimal/No risk, Limited risk, High risk, Unacceptable risk**
- [ ] **D. 5 levels**

👉 **Đáp án đúng:** `C`
💡 **Giải thích:** Đạo luật EU AI Act phân cấp thành 4 cấp độ rủi ro: Rủi ro không thể chấp nhận (bị cấm), Rủi ro cao, Rủi ro hạn chế (yêu cầu minh bạch), và Rủi ro tối thiểu.

---

### Câu 27: AI Roadmap execution khác software roadmap ở điểm nào quan trọng nhất?

- [ ] **A. AI roadmap dài hơn**
- [x] **B. AI roadmap phải tích hợp eval gates (quality thresholds) và data milestones — không chỉ feature delivery**
- [ ] **C. AI roadmap không cần stakeholder buy-in**
- [ ] **D. AI roadmap phải include research phase**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Lộ trình phát triển AI phụ thuộc vào tính bất định của mô hình, do đó bắt buộc phải có các cổng đánh giá chất lượng (eval gates) và các cột mốc làm sạch/bổ sung dữ liệu trước khi bàn giao tính năng.

---

### Câu 28: Tình huống: Data thu thập từ Web form và Email chỉ phản ánh phàn nàn. Đây là loại data quality issue nào và cách fix phù hợp?

- [ ] **A. Data completeness issue — thiếu data từ kênh call center; cần thêm call center transcripts vào pipeline**
- [x] **B. Selection bias — web form và email chỉ capture negative feedback (triggered by problems); kết quả không đại diện cho toàn bộ khách hàng**
- [ ] **C. Data consistency issue — format và ngôn ngữ không nhất quán giữa 3 nguồn, cần chuẩn hóa**
- [ ] **D. Model bias — sentiment model được train trên data tiếng Anh, không**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Đây là hiện tượng thiên lệch chọn mẫu (Selection Bias): chỉ những khách hàng gặp sự cố mới chủ động điền form/gửi email, dẫn đến tập dữ liệu bị nghiêng nặng về tiêu cực.

---

### Câu 29: Yếu tố nào là bottleneck chính khi scale LLM serving?

- [ ] **A. Số lượng CPU cores**
- [x] **B. VRAM (GPU memory) — phải đủ chứa model weights + KV cache cho concurrent requests**
- [ ] **C. Network bandwidth của instance**
- [ ] **D. SSD storage capacity**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Dung lượng bộ nhớ GPU (VRAM) là nút thắt cổ chai lớn nhất vì vừa phải tải trọng lượng mô hình (weights), vừa phải cấp phát bộ nhớ KV Cache cho các luồng yêu cầu đồng thời.

---

### Câu 30: Các threat vectors đặc thù cho AI infrastructure (không có trong traditional app security) là gì?

- [ ] **A. SQL injection và XSS**
- [x] **B. Model extraction (reverse engineer model qua API), training data poisoning, adversarial examples, và supply chain attacks (compromised model weights)**
- [ ] **C. DDoS và brute force**
- [ ] **D. Chỉ API key theft**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Các nguy cơ đặc thù gồm trích xuất mô hình, đầu độc dữ liệu huấn luyện, mẫu dữ liệu đối kháng và tấn công chuỗi cung ứng mô hình pre-trained.

---

### Câu 31: Data Observability khác với Application Observability ở điểm gì?

- [ ] **A. Data Observability theo dõi database performance**
- [x] **B. Data Observability monitor health của data pipelines và data quality (freshness, completeness, schema changes) — không chỉ infra**
- [ ] **C. Data Observability chỉ dùng cho batch jobs**
- [ ] **D. Data Observability không cần cho AI**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Data Observability tập trung vào chất lượng nội dung và dòng chảy dữ liệu (độ tươi, tính toàn vẹn, phân phối và sự biến đổi schema), khác với App Observability chỉ đo CPU, RAM và HTTP latency.

---

### Câu 32: GPU FinOps cho AI workloads: kỹ thuật nào giúp giảm cost nhiều nhất với trade-off thấp nhất?

- [ ] **A. Dùng spot/preemptible instances cho tất cả workloads kể cả production**
- [x] **B. Spot instances cho batch/training (fault-tolerant), reserved instances cho production inference (consistent load), và auto-scaling để không idle**
- [ ] **C. Tắt hết instances vào ban đêm**
- [ ] **D. Chỉ dùng CPU instances để tránh GPU cost**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Kết hợp tối ưu: dùng Spot giá rẻ cho tác vụ huấn luyện có khả năng chịu lỗi, dùng Reserved cho tải suy luận nền cố định của production và kích hoạt Auto-scaling theo nhu cầu thực.

---

### Câu 33: Quantization (INT8/INT4) trong model serving đánh đổi gì?

- [ ] **A. Không có trade-off — INT4 tốt hơn FP16 mọi mặt**
- [x] **B. Giảm memory footprint và tăng throughput, đổi lấy nhỏ quality degradation — acceptable với nhiều production tasks**
- [ ] **C. Tăng accuracy nhưng chậm hơn**
- [ ] **D. Chỉ dùng được với model nhỏ hơn 7B**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Lượng tử hóa (Quantization) nén trọng số từ 16-bit xuống 8-bit hoặc 4-bit giúp giảm mạnh bộ nhớ VRAM và tăng tốc độ xử lý, chỉ đánh đổi một phần rất nhỏ độ chính xác.

---

### Câu 34: Data Lakehouse kết hợp ưu điểm của Data Lake và Data Warehouse như thế nào?

- [ ] **A. Lakehouse chỉ lưu structured data**
- [x] **B. Lakehouse = Data Lake storage (raw, flexible, cheap) + Data Warehouse analytics (ACID transactions, schema enforcement, query performance)**
- [ ] **C. Lakehouse replace cả hai**
- [ ] **D. Lakehouse dùng cho real-time streaming only**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Kiến trúc Lakehouse mang lại khả năng lưu trữ linh hoạt, giá rẻ của Data Lake kết hợp cùng khả năng quản trị giao dịch ACID, kiểm soát schema và hiệu năng cao của Data Warehouse.

---

### Câu 35: Trong CI/CD pipeline cho AI, 'eval gate' hoạt động như thế nào?

- [ ] **A. Eval gate là bước manual review trước khi deploy**
- [x] **B. Eval gate chạy automated evaluation sau mỗi code/prompt/model change — chỉ allow deploy nếu eval scores vượt thresholds (faithfulness, accuracy, safety)**
- [ ] **C. Eval gate chỉ check syntax của prompt**
- [ ] **D. Eval gate là load testing tool**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Cổng đánh giá (Eval Gate) là chốt chặn tự động trong pipeline CI/CD: tự động kiểm thử và ngăn chặn việc triển khai nếu các chỉ số chất lượng/an toàn không vượt qua ngưỡng cam kết.

---

### Câu 36: Model serving optimization strategies nào giúp giảm latency nhất?

- [ ] **A. Dùng model nhỏ hơn**
- [x] **B. Batching requests, KV cache, speculative decoding, và quantization — kết hợp để reduce TTFT và throughput cost**
- [ ] **C. Tăng GPU memory**
- [ ] **D. Reduce context window**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Sự kết hợp giữa Continuous Batching, lưu trữ KV Cache, giải mã phỏng đoán (Speculative Decoding) và lượng tử hóa mang lại hiệu quả tối ưu độ trễ toàn diện nhất.

---

### Câu 37: Tình huống: HR Chatbot không tìm thấy thông tin 'leave advance'. Root cause khả năng cao nhất là gì?

- [ ] **A. Embedding model không hỗ trợ tiếng Việt, cần đổi sang multilingual model**
- [x] **B. Chunk size quá lớn — 1 chunk chứa nhiều sections, semantic signal của 'leave advance' bị dilute, retrieval score thấp**
- [ ] **C. Vector database bị corrupt, cần rebuild index từ đầu**
- [ ] **D. Temperature quá cao trong generation step khiến model hallucinate 'không biết'**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Khi chunk quá lớn, vector embedding đại diện cho ý nghĩa chung của toàn bộ khối văn bản khiến tín hiệu ngữ nghĩa của chi tiết nhỏ bị phân tán (diluted) và trượt khỏi top kết quả truy xuất.

---

### Câu 38: Khi nào single-agent architecture thất bại và cần nâng lên advanced patterns?

- [ ] **A. Khi cần latency thấp**
- [x] **B. Khi task cần nhiều iterative refinement, complex planning với backtracking, hoặc exploration của nhiều solution paths**
- [ ] **C. Khi cần thêm nhiều tools**
- [ ] **D. Khi context window đầy**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Một agent đơn lẻ sẽ bộc lộ hạn chế khi đối mặt với quy trình phức tạp đòi hỏi lập kế hoạch nhiều tầng, quay lui sửa sai (backtracking) hoặc phối hợp nhiều góc nhìn chuyên biệt.

---

### Câu 39: LoRA (Low-Rank Adaptation) cơ chế hoạt động như thế nào?

- [ ] **A. Train lại toàn bộ model weights**
- [x] **B. Freeze pre-trained weights, thêm low-rank adapter matrices nhỏ vào attention layers — chỉ train adapters**
- [ ] **C. Distill model lớn thành model nhỏ**
- [ ] **D. Quantize model để chạy trên hardware yếu hơn**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** LoRA đóng băng toàn bộ trọng số gốc của mô hình pre-trained và chèn thêm các ma trận biến đổi hạng thấp vào các tầng chú ý, chỉ huấn luyện các ma trận phụ này để tiết kiệm tài nguyên.

---

### Câu 40: Faithfulness metric trong RAGAS đo lường điều gì chính xác?

- [ ] **A. Accuracy của answer so với ground truth**
- [x] **B. Tỷ lệ claims trong generated answer có được support bởi retrieved context — không được suy diễn ngoài context**
- [ ] **C. Similarity giữa question và answer**
- [ ] **D. Completeness của answer**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Chỉ số Faithfulness (độ trung thực) kiểm tra tỷ lệ các nhận định trong câu trả lời có bằng chứng trực tiếp từ ngữ cảnh truy xuất hay không, nhằm phát hiện hiện tượng ảo giác (hallucination).

---

### Câu 41: 5 Agentic Workflow Patterns của Anthropic là gì?

- [ ] **A. Plan, Execute, Review, Revise, Publish**
- [x] **B. Prompt Chaining, Routing, Parallelization, Orchestrator-subagents, Evaluator-optimizer**
- [ ] **C. Input, Process, Output, Feedback, Improve**
- [ ] **D. Retrieve, Augment, Generate, Evaluate, Deploy**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** 5 mô hình chuẩn của Anthropic bao gồm: Chuỗi câu lệnh (Chaining), Định tuyến (Routing), Song song hóa (Parallelization), Bộ điều phối - cấp dưới (Orchestrator-subagents) và Đánh giá - Tối ưu hóa (Evaluator-optimizer).

---

### Câu 42: Tại sao Basic RAG thất bại trong production khi demo chạy tốt?

- [ ] **A. Production có nhiều users hơn**
- [x] **B. Production data phức tạp hơn, có noise, inconsistency, và edge cases mà demo data không có**
- [ ] **C. Model quá yếu**
- [ ] **D. Infrastructure không đủ**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Dữ liệu demo thường sạch và đơn giản; trong môi trường thực tế, dữ liệu có tính phân tán, định dạng phức tạp, tài liệu mâu thuẫn và các câu hỏi mơ hồ làm sụp đổ pipeline RAG cơ bản.

---

### Câu 43: PreRAG (Fix ONLINE — trước khi retrieve) bao gồm những kỹ thuật nào?

- [ ] **A. Chỉ clean user query**
- [x] **B. Query expansion, query rewriting, HyDE (Hypothetical Document Embeddings), và query routing theo intent**
- [ ] **C. Translate query sang tiếng Anh**
- [ ] **D. Cache query results**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** PreRAG xử lý câu hỏi trực tuyến trước khi truy vấn: mở rộng từ khóa, viết lại câu truy vấn rõ nghĩa hơn, tạo tài liệu giả định (HyDE) và phân luồng câu hỏi theo ý định người dùng.

---

### Câu 44: Context Engineering Framework giải quyết vấn đề gì trong memory management?

- [ ] **A. Tăng context window size của model**
- [x] **B. Quyết định cái gì đưa vào context window có hạn: prioritize, compress, retrieve đúng memories theo relevance**
- [ ] **C. Compress toàn bộ conversation history**
- [ ] **D. Cache context để reuse**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Context Engineering tối ưu hóa việc sử dụng cửa sổ ngữ cảnh: chọn lọc thông tin ưu tiên, cô đọng lịch sử và truy xuất các mẩu ký ức phù hợp nhất để đưa vào prompt.

---

### Câu 45: Reflexion agent giải quyết được bài toán nào mà ReAct không làm được?

- [ ] **A. Gọi nhiều tools song song**
- [x] **B. Tự đánh giá output của mình và sửa lỗi trong vòng lặp tiếp theo — thêm self-evaluation layer**
- [ ] **C. Handle multi-modal input**
- [ ] **D. Reduce latency**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Kiến trúc Reflexion mở rộng ReAct bằng cách bổ sung khả năng tự phản tư (self-reflection): agent tự phân tích kết quả quan sát, ghi nhớ lỗi sai vào bộ nhớ tạm để điều chỉnh hành vi ở vòng lặp sau.

---

### Câu 46: Hệ thống RAG cho Fintech: Trong vector store vẫn còn chunk từ file cũ (sla-p1-2024.pdf) do thiếu metadata effective_date. Root cause thuộc tầng nào?

- [ ] **A. Retrieval**
- [x] **B. Indexing**
- [ ] **C. Generation**
- [ ] **D. Evaluation**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Lỗi nằm ở tầng Indexing: quá trình nạp và đánh chỉ mục tài liệu không thiết kế trường metadata thời gian hiệu lực (effective_date) và không có cơ chế xóa/ghi đè tài liệu hết hiệu lực.

---

### Câu 47: Ngoài lỗi Indexing, hãy đề xuất thêm 1 kiểm tra ở tầng Generation để tránh trả lời fact cũ?

- [ ] **A. Tăng temperature**
- [x] **B. Yêu cầu LLM kiểm tra citation ngày hiệu lực trong context và cảnh báo nếu có mâu thuẫn phiên bản**
- [ ] **C. Giảm max_tokens**
- [ ] **D. Đổi prompt sang tiếng Anh**

👉 **Đáp án đúng:** `B`
💡 **Giải thích:** Ở tầng sinh văn bản (Generation), cấu hình system prompt yêu cầu LLM trích dẫn ngày hiệu lực và phát hiện cảnh báo xung đột nếu có hai văn bản đưa ra số liệu khác nhau.

---

