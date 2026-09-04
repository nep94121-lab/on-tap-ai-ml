# 📖 SỔ TAY THUẬT NGỮ CHUYÊN NGÀNH & BAREM ĂN TRỌN ĐIỂM TỰ LUẬN AI/ML

> Tài liệu hướng dẫn độc quyền dành cho kỳ thi AI Applications, AI Infrastructure & AI Product.
> Hướng dẫn chi tiết: **Từ nào bắt buộc viết tiếng Anh**, **Từ nào được dịch tiếng Việt vẫn được chấm đúng**, và **Barem từ khóa ăn trọn 100% điểm của từng bài tự luận**.

---

## 🎯 PHẦN 1: NGUYÊN TẮC VÀNG VỀ NGÔN NGỮ KHI LÀM BÀI TỰ LUẬN

### 🔴 NHÓM 1: BẮT BUỘC GIỮ NGUYÊN TIẾNG ANH (Tuyệt đối không dịch)
*Nếu dịch sang tiếng Việt, giám khảo hoặc AI chấm tự động sẽ coi là sai thuật ngữ chuẩn:*

1. **`ReAct` pattern**: Viết đúng `ReAct` (Reasoning + Acting). Không dịch thành "phản ứng".
2. **`Thought` $\rightarrow$ `Action` $\rightarrow$ `Observation`**: 3 bước chu trình ReAct bắt buộc viết đúng 3 từ này trong trace.
3. **`temperature`**, **`max_tokens`**, **`top_p`**: Tên 3 tham số API (viết tiếng Việt là sai cú pháp kỹ thuật).
4. **`RAG`** (Retrieval-Augmented Generation): Viết tắt chuẩn quốc tế.
5. **`Prompt Injection` & `Jailbreak`**: Hai loại tấn công bảo mật khác nhau, viết nguyên văn tiếng Anh.
6. **`System Prompt`** & **`Output Contract`**: Thuật ngữ kỹ nghệ prompt.
7. **`P99 Latency`** & **`TTFT`** (Time to First Token): Các metrics hạ tầng serving.
8. **`VRAM`**, **`KV Cache`**, **`LoRA`**, **`Quantization` (INT8/INT4)**.
9. **`HyDE`** (Hypothetical Document Embeddings), **`PreRAG`**, **`Grounding`**.
10. **4 chỉ số RAGAS**: `Faithfulness`, `Answer Relevance`, `Context Precision`, `Context Recall`.
11. **5 mẫu Anthropic**: `Prompt Chaining`, `Routing`, `Parallelization`, `Orchestrator-subagents`, `Evaluator-optimizer`.

---

### 🟢 NHÓM 2: ĐƯỢC DỊCH SANG TIẾNG VIỆT (Vẫn được tính trọn điểm)
*Các từ này Sếp dùng tiếng Việt thoải mái mà không sợ bị trừ điểm:*

| Thuật ngữ tiếng Anh | Cách viết tiếng Việt ĐƯỢC CHẤM TRỌN ĐIỂM | Ghi chú & Ngữ cảnh sử dụng |
| :--- | :--- | :--- |
| **`Hidden costs / risks`** | **Chi phí ẩn / Rủi ro tiềm ẩn** | Chi phí đào tạo, chi phí hallucination, chi phí sửa lỗi |
| **`Cost saving`** | **Tiết kiệm chi phí / Chi phí cắt giảm được** | Số tiền quỹ lương tiết kiệm được hàng tháng |
| **`Gross benefit`** | **Tổng lợi ích thu về / Giá trị kinh tế tạo ra** | Tổng giá trị thời gian/tiền tiết kiệm được trong 1 năm |
| **`Net profit`** | **Lợi nhuận ròng** | Lợi ích trừ đi tổng chi phí đầu tư và vận hành |
| **`Workload`** | **Khối lượng công việc / Khối lượng ticket** | % thời gian xử lý công việc của nhân sự |
| **`Hallucination`** | **Ảo giác AI / Bịa đặt thông tin** | Hiện tượng AI tự nghĩ ra câu trả lời không có căn cứ |
| **`Rate limiting`** | **Giới hạn tần suất gọi / Chặn spam request** | Ngăn chặn người dùng gọi API quá nhiều lần/phút |
| **`Input / Output validation`**| **Kiểm thực dữ liệu đầu vào / đầu ra** | Quét prompt injection ở input, quét PII ở output |
| **`Human-in-the-loop`** | **Phê duyệt bởi con người / Giám sát con người** | Bắt buộc người duyệt trước khi gửi email/xóa data |
| **`Regression testing`** | **Kiểm thử hồi quy** | Kiểm tra đảm bảo bản cập nhật mới không làm hỏng tính năng cũ |
| **`Model routing`** | **Phân luồng mô hình** | Dùng model nhỏ rẻ cho 80% câu dễ, model lớn cho câu khó |
| **`Semantic chunking`** | **Phân đoạn ngữ nghĩa** | Cắt văn bản theo trọn vẹn ngữ nghĩa, không cắt ngang câu |
| **`Selection bias`** | **Thiên lệch chọn mẫu** | Web form/email chỉ thu thập toàn phàn nàn tiêu cực |
| **`Eval gates`** | **Cổng đánh giá chất lượng tự động** | Chốt chặn trong CI/CD ngăn release bản kém chất lượng |

---

## 🏆 PHẦN 2: BAREM TỪ KHÓA ĂN TRỌN 100% ĐIỂM CÁC BÀI TỰ LUẬN LỚN

### 📝 BÀI 1: TÍNH ROI DỰ ÁN CSKH LOGISTICS (8 NHÂN SỰ)
**Đề bài:** 8 người xử lý 1.200 ticket/ngày, 6 phút/ticket, lương 12tr/tháng. AI giải quyết tự động 60%, 40% còn lại giảm từ 6 phút xuống 3 phút. Chi phí build 200tr, vận hành 15tr/tháng.

#### 👉 Cách làm để ăn trọn 100% điểm:
1. **Ý 1 (Hidden costs/risks):** Phải nêu đủ 2 từ khóa:
   - *Chi phí đào tạo (Training / Change management cost)* cho nhân viên làm quen hệ thống.
   - *Chi phí rủi ro ảo giác (Hallucination risk / Error compensation)*: Chi phí bồi thường khi AI trả lời sai chính sách giao hàng.
2. **Ý 2 (Cost saving hàng tháng):**
   - Nêu tỷ lệ Workload giảm: $60\% + 40\% \times 50\% = 80\%$ thời gian được giải phóng.
   - Quỹ lương hiện tại: $8 \times 12 = 96$ triệu/tháng.
   - **Cost saving hàng tháng:** $96 \times 80\% =$ **`76.8 triệu đồng/tháng`**.
3. **Ý 3 (Tính ROI sau 1 năm & Kết luận):**
   - **Tổng chi phí (Total Cost):** $200 + 15 \times 12 =$ **`380 triệu đồng`**.
   - **Tổng lợi ích (Gross Benefit):** $76.8 \times 12 =$ **`921.6 triệu đồng`**.
   - **Lợi nhuận ròng (Net Profit):** $921.6 - 380 =$ **`541.6 triệu đồng`**.
   - **Công thức ROI:** $\text{ROI} = \frac{541.6}{380} \times 100\% \approx$ **`142.5%`**.
   - **BẮT BUỘC CÓ DÒNG KẾT LUẬN:** *"Dự án **RẤT ĐÁNG ĐẦU TƯ** vì ROI đạt 142.5% (> 100%) và thời gian hoàn vốn (Payback period) chỉ khoảng 5 tháng."*

---

### 📝 BÀI 2: SỰ CỐ DEPLOY E-COMMERCE 17H THỨ SÁU (GPT-3.5 LÊN GPT-4o)
**Đề bài:** Latency tăng 800ms -> 2.4s, Token cost tăng 6x, Output format làm gãy parser downstream services.

#### 👉 Cách làm để ăn trọn 100% điểm:
1. **Ý 1 (Phân tích sai lầm):**
   - Vi phạm quy tắc vàng: *"Never deploy on Friday evening"* (Deploy chiều thứ Sáu không kịp ứng cứu sự cố).
   - Thiếu *Eval Gate / Regression Testing* trước khi release (không đo lường độ trễ và chi phí).
   - Thiếu *Output Contract / Schema validation* khiến format mới làm crash hệ thống hạ tầng phía sau.
2. **Ý 2 (Cost tăng 6x có chấp nhận được không?):**
   - Chỉ chấp nhận nếu *Task Completion Rate* hoặc doanh thu tăng tương ứng.
   - Đề xuất giải pháp bắt buộc: **`Model Routing`** (Phân luồng: Dùng GPT-4o-mini giá rẻ cho 80% câu hỏi dễ, chỉ route câu hỏi khiếu nại/phức tạp sang GPT-4o).
3. **Ý 3 (Thiết kế CI/CD pipeline chuẩn):**
   - Bước 1: Commit code & prompt $\rightarrow$ Unit test.
   - Bước 2: Chạy kiểm thử tự động trên tập *Golden Dataset* (đo Faithfulness, Latency, Cost).
   - Bước 3: *Eval Gate* (nếu vượt ngưỡng mới cho qua).
   - Bước 4: *Canary Deployment* (chạy thử nghiệm trên 5-10% người dùng thực tế).
   - Bước 5: Full Rollout có giám sát realtime cảnh báo (Alerting).

---

### 📝 BÀI 3: TRACE THOUGHT - ACTION - OBSERVATION
**Đề bài:** Query "Tỷ giá USD/VND hiện tại là bao nhiêu?", tool `get_exchange_rate()`.

#### 👉 Bắt buộc viết đúng cấu trúc tiếng Anh:
```text
Question: Tỷ giá USD/VND hiện tại là bao nhiêu?

Thought: Người dùng muốn biết tỷ giá USD/VND mới nhất. Tôi cần gọi tool get_exchange_rate với tham số tương ứng.

Action: get_exchange_rate(from_currency="USD", to_currency="VND")

Observation: {"status": "success", "rate": 25450, "currency": "VND"}

Thought: Đã nhận được kết quả tỷ giá 25.450 VND từ tool. Tôi có đủ dữ liệu để trả lời người dùng.

Final Answer: Tỷ giá USD/VND hiện tại là 25.450 VND đổi 1 USD.
```

---

### 📝 BÀI 4: SỬA 2 LỖI CODE REACT PYTHON
**Đề bài:** Đoạn code implement ReAct agent có 2 lỗi thiết kế.

#### 👉 Từ khóa chỉ ra 2 lỗi:
1. **Lỗi 1:** *Mất Context quan sát (Missing Observation in context)*: Kết quả tool trả về không được đưa ngược vào mảng `messages`, khiến model không thấy kết quả và lặp lại hành động cũ.
2. **Lỗi 2:** *Thiếu điều kiện dừng / Vòng lặp vô hạn (Infinite Loop)*: Không có tham số `max_iterations` và không có điều kiện thoát khi gặp `Final Answer`.
