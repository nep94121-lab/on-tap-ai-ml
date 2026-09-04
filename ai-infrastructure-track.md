# 🛠️ CHUYÊN ĐỀ ÔN TẬP: AI INFRASTRUCTURE TRACK (ĐẦY ĐỦ 3 DẠNG CÂU HỎI & ĐÁP ÁN)

> Tài liệu chuyên sâu tập hợp toàn bộ các câu hỏi thuộc phân hệ **AI Infrastructure (Hạ tầng AI, MLOps, LLMOps, GPU FinOps & Serving)**.
> Bao gồm đầy đủ cả 3 loại câu hỏi: **Trắc nghiệm đơn**, **Trắc nghiệm nhiều đáp án**, và **Tự luận / Tình huống hạ tầng**, tất cả đều đã có đáp án đúng chuẩn xác và giải thích kỹ thuật chi tiết.

## 📑 MỤC LỤC NỘI DUNG:
1. [Phần 1: Trắc nghiệm đơn AI Infrastructure (20 câu)](#phan-1-trac-nghiem-don-ai-infrastructure)
2. [Phần 2: Trắc nghiệm nhiều đáp án AI Infrastructure (3 câu)](#phan-2-trac-nghiem-nhieu-dap-an-ai-infrastructure)
3. [Phần 3: Tự luận, Điền khuyết, Sửa lỗi Code & Bài toán Sự cố Hạ tầng (8 bài)](#phan-3-tu-luan-va-tinh-huong-ha-tang)

---

<a id='phan-1-trac-nghiem-don-ai-infrastructure'></a>
## 1. PHẦN 1: TRẮC NGHIỆM ĐƠN (1 ĐÁP ÁN ĐÚNG) - 20 CÂU

### Câu 1: Khi expose AI agent như REST API, những consideration nào quan trọng nhất?

- [ ] **A. Chỉ cần GET và POST endpoints**
- [x] **B. Authentication/authorization (ai được gọi), rate limiting (tránh abuse), streaming response (UX tốt hơn), timeout handling, và versioning (/v1/ để backward compat)**
- [ ] **C. Chỉ cần HTTPS**
- [ ] **D. Chỉ cần JSON format**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Đây là các tiêu chuẩn production API cho AI: kiểm soát bảo mật (AuthN/AuthZ), chống quá tải chi phí (Rate Limit), cải thiện thời gian phản hồi (Streaming SSE), quản lý ngắt kết nối LLM (Timeout) và duy trì tương thích (Versioning).

---

### Câu 2: Khi agent trả lời đúng fact nhưng là fact cũ (stale), symptom này chỉ ra lỗi ở tầng nào?

- [ ] **A. Model quality**
- [ ] **B. Prompt engineering**
- [x] **C. Freshness — publish pipeline hoặc cache vector bị stale**
- [ ] **D. Retrieval ranking**

👉 **Đáp án đúng:** `C`
💡 **Giải thích chuyên môn:** Dữ liệu trả lời đúng logic nhưng chứa thông tin lỗi thời phản ánh vấn đề độ tươi mới của dữ liệu (Data Freshness), do pipeline cập nhật vector store bị trễ hoặc cache chưa được invalidate.

---

### Câu 3: AI-specific metrics quan trọng nhất cần monitor cho LLM agent là gì?

- [ ] **A. CPU usage và memory**
- [x] **B. TTFT (Time to First Token), Quality score, Cost per request, Drift (model/data)**
- [ ] **C. HTTP response codes và uptime**
- [ ] **D. Database query time**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Các chỉ số đặc thù của LLM gồm: Tốc độ phản hồi token đầu tiên (TTFT), điểm chất lượng câu trả lời (Quality/Eval), chi phí token trên mỗi request (Cost per request) và hiện tượng trôi dạt ngữ nghĩa/phân phối dữ liệu (Drift).

---

### Câu 4: Semantic caching là cost optimization strategy như thế nào?

- [ ] **A. Cache LLM responses cho exact same queries**
- [x] **B. Cache LLM responses cho semantically similar queries — 'hủy đơn hàng' và 'cancel order' nhận cùng response**
- [ ] **C. Compress prompt để giảm tokens**
- [ ] **D. Dùng cheaper model cho tất cả queries**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Semantic caching dùng vector similarity để nhận diện các câu hỏi tương đồng về mặt ý nghĩa (dù từ ngữ khác nhau) và trả về kết quả đã cache sẵn, giúp tiết kiệm chi phí gọi LLM.

---

### Câu 5: Prompt injection và jailbreaking là cùng một loại attack.

- [ ] **A. True**
- [x] **B. False**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Đây là hai loại tấn công khác nhau: Prompt Injection nhằm phá vỡ logic/nhiệm vụ của ứng dụng (ghi đè prompt của hệ thống), còn Jailbreaking nhằm phá bỏ các rào cản an toàn đạo đức cốt lõi của nhà phát triển mô hình.

---

### Câu 6: Yếu tố nào là bottleneck chính khi scale LLM serving?

- [ ] **A. Số lượng CPU cores**
- [x] **B. VRAM (GPU memory) — phải đủ chứa model weights + KV cache cho concurrent requests**
- [ ] **C. Network bandwidth của instance**
- [ ] **D. SSD storage capacity**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Dung lượng bộ nhớ GPU (VRAM) là nút thắt cổ chai lớn nhất vì vừa phải tải trọng lượng mô hình (weights), vừa phải cấp phát bộ nhớ KV Cache cho các luồng yêu cầu đồng thời.

---

### Câu 7: Các threat vectors đặc thù cho AI infrastructure (không có trong traditional app security) là gì?

- [ ] **A. SQL injection và XSS**
- [x] **B. Model extraction (reverse engineer model qua API), training data poisoning, adversarial examples, và supply chain attacks (compromised model weights)**
- [ ] **C. DDoS và brute force**
- [ ] **D. Chỉ API key theft**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Các nguy cơ đặc thù gồm trích xuất mô hình, đầu độc dữ liệu huấn luyện, mẫu dữ liệu đối kháng và tấn công chuỗi cung ứng mô hình pre-trained.

---

### Câu 8: Data Observability khác với Application Observability ở điểm gì?

- [ ] **A. Data Observability theo dõi database performance**
- [x] **B. Data Observability monitor health của data pipelines và data quality (freshness, completeness, schema changes) — không chỉ infra**
- [ ] **C. Data Observability chỉ dùng cho batch jobs**
- [ ] **D. Data Observability không cần cho AI**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Data Observability tập trung vào chất lượng nội dung và dòng chảy dữ liệu (độ tươi, tính toàn vẹn, phân phối và sự biến đổi schema), khác với App Observability chỉ đo CPU, RAM và HTTP latency.

---

### Câu 9: GPU FinOps cho AI workloads: kỹ thuật nào giúp giảm cost nhiều nhất với trade-off thấp nhất?

- [ ] **A. Dùng spot/preemptible instances cho tất cả workloads kể cả production**
- [x] **B. Spot instances cho batch/training (fault-tolerant), reserved instances cho production inference (consistent load), và auto-scaling để không idle**
- [ ] **C. Tắt hết instances vào ban đêm**
- [ ] **D. Chỉ dùng CPU instances để tránh GPU cost**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Kết hợp tối ưu: dùng Spot giá rẻ cho tác vụ huấn luyện có khả năng chịu lỗi, dùng Reserved cho tải suy luận nền cố định của production và kích hoạt Auto-scaling theo nhu cầu thực.

---

### Câu 10: Quantization (INT8/INT4) trong model serving đánh đổi gì?

- [ ] **A. Không có trade-off — INT4 tốt hơn FP16 mọi mặt**
- [x] **B. Giảm memory footprint và tăng throughput, đổi lấy nhỏ quality degradation — acceptable với nhiều production tasks**
- [ ] **C. Tăng accuracy nhưng chậm hơn**
- [ ] **D. Chỉ dùng được với model nhỏ hơn 7B**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Lượng tử hóa (Quantization) nén trọng số từ 16-bit xuống 8-bit hoặc 4-bit giúp giảm mạnh bộ nhớ VRAM và tăng tốc độ xử lý, chỉ đánh đổi một phần rất nhỏ độ chính xác.

---

### Câu 11: Data Lakehouse kết hợp ưu điểm của Data Lake và Data Warehouse như thế nào?

- [ ] **A. Lakehouse chỉ lưu structured data**
- [x] **B. Lakehouse = Data Lake storage (raw, flexible, cheap) + Data Warehouse analytics (ACID transactions, schema enforcement, query performance)**
- [ ] **C. Lakehouse replace cả hai**
- [ ] **D. Lakehouse dùng cho real-time streaming only**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Kiến trúc Lakehouse mang lại khả năng lưu trữ linh hoạt, giá rẻ của Data Lake kết hợp cùng khả năng quản trị giao dịch ACID, kiểm soát schema và hiệu năng cao của Data Warehouse.

---

### Câu 12: Trong CI/CD pipeline cho AI, 'eval gate' hoạt động như thế nào?

- [ ] **A. Eval gate là bước manual review trước khi deploy**
- [x] **B. Eval gate chạy automated evaluation sau mỗi code/prompt/model change — chỉ allow deploy nếu eval scores vượt thresholds (faithfulness, accuracy, safety)**
- [ ] **C. Eval gate chỉ check syntax của prompt**
- [ ] **D. Eval gate là load testing tool**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Cổng đánh giá (Eval Gate) là chốt chặn tự động trong pipeline CI/CD: tự động kiểm thử và ngăn chặn việc triển khai nếu các chỉ số chất lượng/an toàn không vượt qua ngưỡng cam kết.

---

### Câu 13: Model serving optimization strategies nào giúp giảm latency nhất?

- [ ] **A. Dùng model nhỏ hơn**
- [x] **B. Batching requests, KV cache, speculative decoding, và quantization — kết hợp để reduce TTFT và throughput cost**
- [ ] **C. Tăng GPU memory**
- [ ] **D. Reduce context window**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Sự kết hợp giữa Continuous Batching, lưu trữ KV Cache, giải mã phỏng đoán (Speculative Decoding) và lượng tử hóa mang lại hiệu quả tối ưu độ trễ toàn diện nhất.

---

### Câu 14: Tình huống: HR Chatbot không tìm thấy thông tin 'leave advance'. Root cause khả năng cao nhất là gì?

- [ ] **A. Embedding model không hỗ trợ tiếng Việt, cần đổi sang multilingual model**
- [x] **B. Chunk size quá lớn — 1 chunk chứa nhiều sections, semantic signal của 'leave advance' bị dilute, retrieval score thấp**
- [ ] **C. Vector database bị corrupt, cần rebuild index từ đầu**
- [ ] **D. Temperature quá cao trong generation step khiến model hallucinate 'không biết'**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Khi chunk quá lớn, vector embedding đại diện cho ý nghĩa chung của toàn bộ khối văn bản khiến tín hiệu ngữ nghĩa của chi tiết nhỏ bị phân tán (diluted) và trượt khỏi top kết quả truy xuất.

---

### Câu 15: LoRA (Low-Rank Adaptation) cơ chế hoạt động như thế nào?

- [ ] **A. Train lại toàn bộ model weights**
- [x] **B. Freeze pre-trained weights, thêm low-rank adapter matrices nhỏ vào attention layers — chỉ train adapters**
- [ ] **C. Distill model lớn thành model nhỏ**
- [ ] **D. Quantize model để chạy trên hardware yếu hơn**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** LoRA đóng băng toàn bộ trọng số gốc của mô hình pre-trained và chèn thêm các ma trận biến đổi hạng thấp vào các tầng chú ý, chỉ huấn luyện các ma trận phụ này để tiết kiệm tài nguyên.

---

### Câu 16: Tại sao Basic RAG thất bại trong production khi demo chạy tốt?

- [ ] **A. Production có nhiều users hơn**
- [x] **B. Production data phức tạp hơn, có noise, inconsistency, và edge cases mà demo data không có**
- [ ] **C. Model quá yếu**
- [ ] **D. Infrastructure không đủ**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Dữ liệu demo thường sạch và đơn giản; trong môi trường thực tế, dữ liệu có tính phân tán, định dạng phức tạp, tài liệu mâu thuẫn và các câu hỏi mơ hồ làm sụp đổ pipeline RAG cơ bản.

---

### Câu 17: PreRAG (Fix ONLINE — trước khi retrieve) bao gồm những kỹ thuật nào?

- [ ] **A. Chỉ clean user query**
- [x] **B. Query expansion, query rewriting, HyDE (Hypothetical Document Embeddings), và query routing theo intent**
- [ ] **C. Translate query sang tiếng Anh**
- [ ] **D. Cache query results**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** PreRAG xử lý câu hỏi trực tuyến trước khi truy vấn: mở rộng từ khóa, viết lại câu truy vấn rõ nghĩa hơn, tạo tài liệu giả định (HyDE) và phân luồng câu hỏi theo ý định người dùng.

---

### Câu 18: Context Engineering Framework giải quyết vấn đề gì trong memory management?

- [ ] **A. Tăng context window size của model**
- [x] **B. Quyết định cái gì đưa vào context window có hạn: prioritize, compress, retrieve đúng memories theo relevance**
- [ ] **C. Compress toàn bộ conversation history**
- [ ] **D. Cache context để reuse**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Context Engineering tối ưu hóa việc sử dụng cửa sổ ngữ cảnh: chọn lọc thông tin ưu tiên, cô đọng lịch sử và truy xuất các mẩu ký ức phù hợp nhất để đưa vào prompt.

---

### Câu 19: Hệ thống RAG cho Fintech: Trong vector store vẫn còn chunk từ file cũ (sla-p1-2024.pdf) do thiếu metadata effective_date. Root cause thuộc tầng nào?

- [ ] **A. Retrieval**
- [x] **B. Indexing**
- [ ] **C. Generation**
- [ ] **D. Evaluation**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Lỗi nằm ở tầng Indexing: quá trình nạp và đánh chỉ mục tài liệu không thiết kế trường metadata thời gian hiệu lực (effective_date) và không có cơ chế xóa/ghi đè tài liệu hết hiệu lực.

---

### Câu 20: Ngoài lỗi Indexing, hãy đề xuất thêm 1 kiểm tra ở tầng Generation để tránh trả lời fact cũ?

- [ ] **A. Tăng temperature**
- [x] **B. Yêu cầu LLM kiểm tra citation ngày hiệu lực trong context và cảnh báo nếu có mâu thuẫn phiên bản**
- [ ] **C. Giảm max_tokens**
- [ ] **D. Đổi prompt sang tiếng Anh**

👉 **Đáp án đúng:** `B`
💡 **Giải thích chuyên môn:** Ở tầng sinh văn bản (Generation), cấu hình system prompt yêu cầu LLM trích dẫn ngày hiệu lực và phát hiện cảnh báo xung đột nếu có hai văn bản đưa ra số liệu khác nhau.

---

<a id='phan-2-trac-nghiem-nhieu-dap-an-ai-infrastructure'></a>
## 2. PHẦN 2: TRẮC NGHIỆM NHIỀU ĐÁP ÁN ĐÚNG - 3 CÂU

### Câu 1: Những kỹ thuật nào dưới đây là guardrail hợp lệ cho AI agent trong production? (Chọn tất cả đáp án đúng)

- [x] **A. Input validation: detect và block prompt injection patterns trước khi đưa vào LLM**
- [x] **B. Output validation: scan response có PII (tên, số điện thoại, CCCD) trước khi trả về user**
- [ ] **C. Tăng temperature lên 1.8 để model 'suy nghĩ đa dạng hơn' và tránh bị jailbreak**
- [x] **D. Human-in-the-loop: yêu cầu human approve khi action có tác động cao (gửi email hàng loạt, xóa data)**
- [x] **E. Rate limiting: giới hạn số lượng requests/phút từ một user để tránh abuse và kiểm soát chi phí**

👉 **Đáp án đúng:** `A, B, D, E`
💡 **Giải thích chuyên môn:** Các chốt chặn bảo vệ chuẩn production bao gồm lọc dữ liệu đầu vào (A), ẩn danh hóa thông tin nhạy cảm đầu ra (B), phê duyệt của con người cho tác vụ nguy hiểm (D) và giới hạn tần suất truy cập (E). Phương án C sai hoàn toàn vì tăng nhiệt độ lên 1.8 sẽ gây ảo giác nặng và mất kiểm soát.

---

### Câu 2: Khi nào nên chuyển từ single agent sang multi-agent architecture? (Chọn tất cả đáp án đúng)

- [x] **A. Task cần parallel processing — ví dụ: crawl và summarize 100 URLs đồng thời**
- [x] **B. Context window của agent đang chạm giới hạn (>80% capacity) thường xuyên**
- [ ] **C. Model GPT-4 quá đắt, muốn thay bằng GPT-3.5 cho tốc độ nhanh hơn**
- [x] **D. Task gồm nhiều sub-tasks hoàn toàn độc lập có thể chạy song song**
- [x] **E. Task đòi hỏi vai trò chuyên biệt: Researcher → Writer → Critic (specialized agents)**

👉 **Đáp án đúng:** `A, B, D, E`
💡 **Giải thích chuyên môn:** Kiến trúc Multi-agent cần thiết khi xử lý song song khối lượng lớn (A, D), giảm tải áp lực ngữ cảnh (B) và phân chia vai trò chuyên môn hóa theo quy trình phản biện/tạo tác (E). Phương án C chỉ là bài toán lựa chọn mô hình (Model Selection/Routing).

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

<a id='phan-3-tu-luan-va-tinh-huong-ha-tang'></a>
## 3. PHẦN 3: TỰ LUẬN, ĐIỀN KHUYẾT, SỬA LỖI CODE & SỰ CỐ HẠ TẦNG - 8 BÀI

### Bài 1 (Điền tham số API):
**Nội dung câu hỏi:**
Điền tên tham số API LLM phù hợp vào chỗ trống:
Trong API LLM (OpenAI, Anthropic):
- Tham số [1] kiểm soát mức độ ngẫu nhiên của output (0 = deterministic, giá trị cao = creative/random).
- Tham số [2] giới hạn độ dài tối đa của response tính bằng tokens.
- Tham số [3] kiểm soát xác suất tích lũy của token pool được sample (nucleus sampling).

**Chi tiết từng câu hỏi con & Lời giải chuẩn:**
- **Tham số [1] là gì?**
  👉 **Trả lời:** temperature

- **Tham số [2] là gì?**
  👉 **Trả lời:** max_tokens (hoặc max_completion_tokens)

- **Tham số [3] là gì?**
  👉 **Trả lời:** top_p

---

### Bài 2 (Điền từ vào chỗ trống):
**Nội dung câu hỏi:**
Điền vào chỗ trống để mô tả đúng quy trình tìm kiếm ngữ nghĩa:
Quá trình chuyển đổi text thành vector số học gọi là [1]. Trong vector database, việc đo khoảng cách giữa 2 vectors thường dùng độ đo [2] (cosine similarity hoặc dot product). Kết quả trả về là top-k chunks có độ tương đồng ngữ nghĩa cao nhất với query vector, được gọi là quá trình [3].

**Chi tiết từng câu hỏi con & Lời giải chuẩn:**
- **[1] = ?**
  👉 **Trả lời:** Embedding (hoặc Vectorization)

- **[2] = ?**
  👉 **Trả lời:** Cosine similarity (hoặc Vector distance metric)

- **[3] = ?**
  👉 **Trả lời:** Retrieval (Truy xuất / Vector search / Semantic retrieval)

---

### Bài 3 (Sắp xếp quy trình):
**Nội dung câu hỏi:**
Sắp xếp các bước trong RAG Indexing pipeline theo đúng thứ tự từ đầu đến cuối:
[A] Chunk document thành các đoạn nhỏ (100–512 tokens mỗi chunk).
[B] Load raw documents từ nguồn (PDF, web page, database, API).
[C] Embed mỗi chunk thành dense vector dùng embedding model.
[D] Lưu vectors vào vector database (Pinecone, ChromaDB, pgvector).
[E] Clean và tiền xử lý text (loại bỏ noise, normalize format, bỏ duplicate).

**Lời giải / Đáp án kỹ thuật chi tiết:**
**Thứ tự sắp xếp đúng:**
**B → E → A → C → D**
1. [B] Load raw documents từ nguồn
2. [E] Clean và tiền xử lý text
3. [A] Chunk document thành các đoạn nhỏ
4. [C] Embed mỗi chunk thành dense vector
5. [D] Lưu vectors vào vector database

---

### Bài 4 (Tự luận khái niệm):
**Nội dung câu hỏi:**
Giải thích 'output contract' trong system prompt là gì và tại sao quan trọng trong production agent.

**Lời giải / Đáp án kỹ thuật chi tiết:**
**Trả lời:**
- **Định nghĩa:** Output contract (Giao ước đầu ra) là tập hợp các quy định bắt buộc được định nghĩa tường minh trong system prompt, yêu cầu LLM phải trả về kết quả tuân thủ nghiêm ngặt một định dạng xác định (ví dụ: JSON Schema chuẩn, regex format, danh sách trường bắt buộc, không kèm văn bản giải thích thừa).
- **Tầm quan trọng trong production:**
  1. **Tính tương thích hệ thống (Machine-readable):** Giúp code backend phân tích (parse) cú pháp an toàn bằng `json.loads()` mà không bị lỗi crash hệ thống do LLM sinh lời mở đầu ('Here is your result...').
  2. **Tích hợp Tool Chaining:** Cho phép output của agent này làm input tin cậy cho agent tiếp theo trong pipeline.
  3. **Độ ổn định & Kiểm thử tự động:** Cho phép viết các bài unit test tự động xác minh tính toàn vẹn của dữ liệu đầu ra.

---

### Bài 5 (Tự luận RAG):
**Nội dung câu hỏi:**
Cho document sau: 'Chính sách hoàn tiền được áp dụng trong vòng 30 ngày kể từ ngày mua. Điều kiện: sản phẩm chưa qua sử dụng và còn nguyên tem.' Hãy mô tả cách chunk đúng với metadata đầy đủ.

**Lời giải / Đáp án kỹ thuật chi tiết:**
**Mô tả phương pháp Chunking & Metadata chuẩn:**
1. **Chiến lược Chunking:**
   - Áp dụng **Semantic Chunking** hoặc Chunk theo đoạn hoàn chỉnh (giữ trọn vẹn cả thời hạn và điều kiện trong cùng 1 chunk để bảo toàn ngữ nghĩa, không cắt ngang giữa câu).
2. **Nội dung Chunk:**
   ```text
   Chính sách hoàn tiền được áp dụng trong vòng 30 ngày kể từ ngày mua. Điều kiện: sản phẩm chưa qua sử dụng và còn nguyên tem.
   ```
3. **Cấu trúc Metadata đi kèm:**
   ```json
   {
     "doc_id": "policy_refund_v1",
     "title": "Chính sách hoàn tiền",
     "category": "customer_policy",
     "effective_date": "2026-01-01",
     "expiry_date": null,
     "version": "1.0",
     "section": "refund_conditions",
     "chunk_id": "refund_001",
     "source_url": "https://company.vn/policies/refund.pdf"
   }
   ```

---

### Bài 6 (Tự luận giám sát):
**Nội dung câu hỏi:**
Mô tả ngắn gọn (2-3 câu) tại sao P99 latency quan trọng hơn average latency khi monitor AI agent performance.

**Lời giải / Đáp án kỹ thuật chi tiết:**
**Trả lời:**
- Average latency thường che giấu các trường hợp bất thường vì các request đơn giản sẽ kéo điểm trung bình xuống thấp.
- P99 latency phản ánh độ trễ thực tế của 1% người dùng gặp trải nghiệm tồi tệ nhất (như agent bị kẹt vòng lặp tool call, context quá dài hoặc API bị nghẽn).
- Trong môi trường sản xuất, P99 là chỉ số đo lường trực tiếp SLA và tính ổn định tối đa của hệ thống đối với các tác vụ khó.

---

### Bài 7 (Tự luận Sửa code ReAct):
**Nội dung câu hỏi:**
Đoạn code dưới đây implement một ReAct agent nhưng có 2 lỗi thiết kế khiến agent không hoạt động đúng theo pattern Thought→Action→Observation. Nhiệm vụ: Xác định 2 lỗi thiết kế và viết lại hàm run_agent() đúng theo ReAct pattern (pseudocode chấp nhận được).

**Lời giải / Đáp án kỹ thuật chi tiết:**
**Phân tích 2 lỗi thiết kế cốt tử:**
1. **Lỗi 1 (Mất Context trong vòng lặp):** Lịch sử hội thoại không tích lũy Observation trả về từ tool, khiến LLM không nhìn thấy kết quả hành động trước đó và lặp lại câu lệnh cũ vô tận.
2. **Lỗi 2 (Thiếu điều kiện dừng / Infinite Loop):** Không có cơ chế kiểm tra Final Answer hoặc giới hạn số lần lặp tối đa (`max_iterations`), dẫn đến agent chạy vô hạn và phát sinh chi phí lớn.

**Mã nguồn viết lại chuẩn ReAct Pattern:**
```python
def run_agent(query, max_iterations=5):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": query}
    ]
    
    for step in range(max_iterations):
        # LLM sinh Thought và Action
        response = call_llm(messages)
        messages.append({"role": "assistant", "content": response})
        
        # Phân tích cú pháp xem có Final Answer chưa
        if "Final Answer:" in response:
            return extract_final_answer(response)
            
        # Bóc tách tool và tham số
        action_name, action_args = parse_action(response)
        
        # Thực thi tool lấy kết quả (Observation)
        try:
            observation = execute_tool(action_name, action_args)
        except Exception as e:
            observation = f"Tool error: {str(e)}"
            
        # Đưa Observation trở lại context
        messages.append({"role": "user", "content": f"Observation: {observation}"})
        
    return "Agent không hoàn thành tác vụ trong số bước tối đa cho phép."
```

---

### Bài 8 (Bài toán sự cố triển khai E-commerce):
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

