# 📌 PHẦN 2: CÂU HỎI TRẮC NGHIỆM NHIỀU ĐÁP ÁN ĐÚNG

> Tổng số câu: **5 câu** (đã lọc sạch 100% trùng lặp).
> Quy ước: Chọn tất cả các phương án đúng `[x]`, đi kèm giải thích chuyên môn chi tiết.

---

### Câu 1: Những tình huống nào dưới đây phù hợp với RAG hơn so với Fine-tuning? (Chọn tất cả đáp án đúng)

- [x] **A. Agent cần trả lời từ tài liệu nội bộ công ty được cập nhật hàng tuần**
- [ ] **B. Cần model học phong cách viết thương hiệu đặc thù và nhất quán**
- [x] **C. Agent cần truy xuất chính xác từ knowledge base pháp lý hơn 50.000 trang**
- [ ] **D. Cần model hiểu sâu thuật ngữ y tế chuyên biệt (ICD codes, clinical notes)**
- [x] **E. Agent cần biết giá sản phẩm real-time từ catalog cập nhật liên tục**

👉 **Đáp án đúng:** `A, C, E`
💡 **Giải thích:** RAG vượt trội khi: dữ liệu cập nhật liên tục (A, E), và cần truy xuất chính xác kèm trích dẫn trên kho tri thức khổng lồ (C). Trong khi đó, Fine-tuning phù hợp hơn để định hình văn phong (B) hoặc học ngữ pháp/thuật ngữ miền sâu (D).

---

### Câu 2: Những kỹ thuật nào dưới đây là guardrail hợp lệ cho AI agent trong production? (Chọn tất cả đáp án đúng)

- [x] **A. Input validation: detect và block prompt injection patterns trước khi đưa vào LLM**
- [x] **B. Output validation: scan response có PII (tên, số điện thoại, CCCD) trước khi trả về user**
- [ ] **C. Tăng temperature lên 1.8 để model 'suy nghĩ đa dạng hơn' và tránh bị jailbreak**
- [x] **D. Human-in-the-loop: yêu cầu human approve khi action có tác động cao (gửi email hàng loạt, xóa data)**
- [x] **E. Rate limiting: giới hạn số lượng requests/phút từ một user để tránh abuse và kiểm soát chi phí**

👉 **Đáp án đúng:** `A, B, D, E`
💡 **Giải thích:** Các chốt chặn bảo vệ chuẩn production bao gồm lọc dữ liệu đầu vào (A), ẩn danh hóa thông tin nhạy cảm đầu ra (B), phê duyệt của con người cho tác vụ nguy hiểm (D) và giới hạn tần suất truy cập (E). Phương án C sai hoàn toàn vì tăng nhiệt độ lên 1.8 sẽ gây ảo giác nặng và mất kiểm soát.

---

### Câu 3: Khi nào nên chuyển từ single agent sang multi-agent architecture? (Chọn tất cả đáp án đúng)

- [x] **A. Task cần parallel processing — ví dụ: crawl và summarize 100 URLs đồng thời**
- [x] **B. Context window của agent đang chạm giới hạn (>80% capacity) thường xuyên**
- [ ] **C. Model GPT-4 quá đắt, muốn thay bằng GPT-3.5 cho tốc độ nhanh hơn**
- [x] **D. Task gồm nhiều sub-tasks hoàn toàn độc lập có thể chạy song song**
- [x] **E. Task đòi hỏi vai trò chuyên biệt: Researcher → Writer → Critic (specialized agents)**

👉 **Đáp án đúng:** `A, B, D, E`
💡 **Giải thích:** Kiến trúc Multi-agent cần thiết khi xử lý song song khối lượng lớn (A, D), giảm tải áp lực ngữ cảnh (B) và phân chia vai trò chuyên môn hóa theo quy trình phản biện/tạo tác (E). Phương án C chỉ là bài toán lựa chọn mô hình (Model Selection/Routing).

---

### Câu 4: Những yếu tố nào là best practice khi thiết kế system prompt cho AI agent? (Chọn tất cả đáp án đúng)

- [x] **A. Mô tả rõ role, persona và nhiệm vụ chính của agent**
- [ ] **B. Viết CAPS LOCK để nhấn mạnh các instruction quan trọng**
- [x] **C. Định nghĩa output format mong muốn (JSON schema, bullet list, markdown, etc.)**
- [x] **D. Liệt kê explicit những gì agent KHÔNG được làm (negative constraints)**
- [x] **E. Cung cấp few-shot examples cho task phức tạp hoặc format đặc biệt**

👉 **Đáp án đúng:** `A, C, D, E`
💡 **Giải thích:** Thiết kế system prompt chuẩn cần có vai trò (A), định dạng đầu ra rõ ràng (C), các giới hạn cấm làm (D) và ví dụ mẫu few-shot (E). Viết in hoa toàn bộ (B) là thói quen xấu, không đảm bảo tính ổn định trong kỹ nghệ prompt.

---

### Câu 5: Những metrics nào cần monitor cho AI agent trong production? (Chọn tất cả đáp án đúng)

- [x] **A. Latency P50 và P99 (percentile) của mỗi request**
- [x] **B. Token cost per request (input tokens + output tokens × đơn giá model)**
- [ ] **C. Số lần model weights được updated trong ngày**
- [x] **D. Error rate: tool call failures, JSON parsing errors, timeouts**
- [x] **E. Task completion rate: % requests đạt được Final Answer thành công**

👉 **Đáp án đúng:** `A, B, D, E`
💡 **Giải thích:** Giám sát AI production cần theo dõi độ trễ (A), chi phí token (B), tỷ lệ lỗi gọi công cụ/phân tích cú pháp (D) và tỷ lệ hoàn thành tác vụ thành công (E). Trọng số mô hình nền tảng qua API không được cập nhật từng ngày (C sai).

---

