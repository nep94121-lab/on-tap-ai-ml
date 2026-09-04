#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_essay_enhancements.py
Cập nhật đầy đủ nội dung rà soát cho 16 câu tự luận trong questions_db.json:
- Câu 68: Bổ sung 4 chỉ số RAGAS (Faithfulness, Answer Relevance, Context Precision, Context Recall),
          ngưỡng an toàn release cho cả 4 chỉ số, phân tích tầng Retrieval.
- Câu 59: Bổ sung Feedback Loop & Human-in-the-loop khi Worker gặp lỗi / confidence < 80%.
- Câu 60: Bổ sung 3 thành phần cốt lõi của Output Contract.
- Câu 67: Bổ sung Kế hoạch Incident Response 4 bước cứu vãn hệ thống trong đêm thứ Sáu.
- Câu 56: Chuẩn hóa chuỗi đáp án ghép nối trong origin_sub_questions sub 2.
"""

import json
import os

JSON_PATH = "questions_db.json"

def apply_enhancements():
    print(f"[*] Loading {JSON_PATH}...")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    q_map = {q["id"]: q for q in data}

    # =========================================================================
    # 1. CẬP NHẬT CÂU 68 (TRỌNG TÂM CỦA SẾP)
    # =========================================================================
    q68 = q_map[68]
    q68["quick_tip"] = (
        "• **Ý 1 (Bộ dữ liệu kiểm định):** Chọn 150 - 200 câu hỏi thực tế đại diện cho mọi trường hợp "
        "(câu hỏi chuẩn 70%, ngoài chính sách/ca biên 20%, câu hỏi bẫy đối kháng 10%), có **đáp án chuẩn từ chuyên gia CSKH**.\n"
        "• **Ý 2 (Khung đo lường 4 chỉ số RAGAS):**\n"
        "  - `Faithfulness`: Đo tính trung thực với tài liệu bảo hành (chống ảo giác, không tự bịa thời hạn/chính sách).\n"
        "  - `Answer Relevance`: Đo mức độ trả lời đúng trọng tâm câu hỏi của khách hàng.\n"
        "  - `Context Precision`: Đo độ chính xác ngữ cảnh — tỷ lệ và thứ hạng chunks liên quan được xếp ở vị trí đầu.\n"
        "  - `Context Recall`: Đo độ bao phủ ngữ cảnh — mức độ tài liệu truy xuất chứa đầy đủ thông tin để trả lời.\n"
        "• **Ý 3 (Điều kiện đạt chuẩn Release & Sửa lỗi Retrieval):**\n"
        "  - Ngưỡng Release: `Faithfulness` ≥ 0.95 (hoặc ≥ 0.85), `Answer Relevance` ≥ 0.90 (hoặc ≥ 0.85), "
        "`Context Precision` ≥ 0.80, `Context Recall` ≥ 0.80.\n"
        "  - Tỷ lệ vi phạm an toàn / lọt prompt injection = 0%; Độ trễ P99 ≤ 3.0 giây.\n"
        "  - Nếu `Faithfulness` = 0.95 mà `Context Recall` = 0.60: Agent trung thực nhưng thiếu thông tin do tìm kiếm sót -> "
        "Cần sửa ở **Tầng Retrieval** (tăng top-k, Hybrid Search, Reranking)."
    )

    q68["explanation"] = (
        "- **Ý 1: Thiết kế bộ dữ liệu kiểm thử (Evaluation Dataset).**\n"
        "  👉 **Trả lời:** Từ 500 câu hỏi thực tế, lọc chọn ra 150 - 200 câu hỏi đa dạng đại diện cho các nhóm:\n"
        "  1. Câu hỏi chuẩn có trong tài liệu chính sách bảo hành (Happy path / In-domain) ~ 70%.\n"
        "  2. Câu hỏi ngoài phạm vi chính sách, mơ hồ, ca biên (Edge cases / Out-of-domain) ~ 20%.\n"
        "  3. Câu hỏi cố tình công kích, bẫy hoặc tiêm nhiễm mã độc (Adversarial / Prompt Injection) ~ 10%.\n"
        "  Mỗi dòng dữ liệu (row) bắt buộc có: Question (Câu hỏi khách), Ground Truth (Đáp án chuẩn phê duyệt bởi chuyên gia CSKH bảo hành), Reference Context (Đoạn tài liệu gốc tương ứng).\n\n"
        "- **Ý 2: Nêu 4 RAGAS metrics và giải thích ý nghĩa trong bối cảnh bảo hành.**\n"
        "  👉 **Trả lời:** Khung đánh giá chất lượng RAGAS gồm 4 chỉ số cốt lõi kết hợp LLM-as-a-Judge:\n"
        "  1. **Faithfulness (Độ trung thực):** Đo lường xem câu trả lời của agent có hoàn toàn dựa trên ngữ cảnh bảo hành được cung cấp hay không. Chống việc AI tự bịa đặt chính sách (ví dụ: bịa tăng thời gian bảo hành pin từ 3 năm lên 5 năm).\n"
        "  2. **Answer Relevance (Độ liên quan câu trả lời):** Đo lường mức độ câu trả lời giải quyết đúng và trúng thắc mắc của khách hàng, không trả lời lan man hoặc bỏ qua câu hỏi chính.\n"
        "  3. **Context Precision (Độ chính xác ngữ cảnh truy xuất):** Đo tỷ lệ các đoạn văn bản (chunks) thực sự chứa câu trả lời nằm ở các vị trí xếp hạng cao trong top-k. Đảm bảo thông tin quan trọng nhất nằm ngay đầu ngữ cảnh đưa vào LLM.\n"
        "  4. **Context Recall (Độ bao phủ ngữ cảnh truy xuất):** Đo lường xem các tài liệu được truy xuất có chứa đầy đủ mọi thông tin cần thiết để trả lời câu hỏi hay không (đối chiếu với Ground Truth).\n\n"
        "- **Ý 3: Phân tích ca biên và Tiêu chuẩn Pass/Fail đạt chuẩn Production.**\n"
        "  👉 **Trả lời:**\n"
        "  * **Phân tích ca bệnh (Faithfulness = 0.95, Context Recall = 0.60):**\n"
        "    - *Ý nghĩa:* Agent trả lời rất trung thực với dữ liệu nhận được (chống ảo giác tốt, đạt 0.95), nhưng câu trả lời bị thiếu sót thông tin quan trọng của khách hàng do hệ thống chỉ truy xuất được 60% dữ liệu cần thiết.\n"
        "    - *Tầng cần khắc phục:* **Tầng Retrieval (Truy xuất dữ liệu)**, không phải tầng Generation!\n"
        "    - *Giải pháp:* Tăng số lượng `top_k` chunks (ví dụ từ 3 lên 5-7), cải thiện kỹ thuật Chunking có overlap (15-20%), kết hợp Hybrid Search (Dense vector + BM25 keyword search), hoặc bổ sung Reranker (Cohere/BGE-Reranker).\n"
        "  * **Điều kiện tối thiểu phê duyệt Release:**\n"
        "    - Faithfulness ≥ 0.85 (khuyến nghị ≥ 0.95 đối với chính sách bảo hành).\n"
        "    - Answer Relevance ≥ 0.85 (khuyến nghị ≥ 0.90).\n"
        "    - Context Precision ≥ 0.80.\n"
        "    - Context Recall ≥ 0.80.\n"
        "    - Guardrails: Tỷ lệ vi phạm an toàn / lọt prompt injection = 0%; Che giấu PII (số điện thoại, biển số xe) = 100%.\n"
        "    - Hiệu năng: Độ trễ P99 ≤ 3.0 giây."
    )

    # =========================================================================
    # 2. CẬP NHẬT CÂU 59 (BỔ SUNG FEEDBACK LOOP & HUMAN-IN-THE-LOOP)
    # =========================================================================
    q59 = q_map[59]
    q59["quick_tip"] = (
        "• **Mô hình kiến trúc:** 1 Quản lý (Supervisor) + 3 Công nhân (Worker):\n"
        "  1. **Quản lý (Supervisor Agent):** Nhận phản hồi thô, phân việc cho 3 worker và gom kết quả viết báo cáo.\n"
        "  2. **Worker 1 (Phân tích cảm xúc):** Gán nhãn Tích cực / Tiêu cực / Trung tính.\n"
        "  3. **Worker 2 (Trích xuất chủ đề):** Bóc tách vấn đề (Giá cả, Vận chuyển, Lỗi phần mềm, CSKH).\n"
        "  4. **Worker 3 (Sinh báo cáo):** Tổng hợp số liệu và viết báo cáo tóm tắt cho ban giám đốc.\n"
        "• **Vòng lặp phản hồi (Feedback Loop & Human-in-the-loop):**\n"
        "  - Khi Worker gặp lỗi hoặc điểm tin cậy < 80%: Chuyển tiếp (Escalate) cho chuyên viên con người thẩm định thủ công.\n"
        "  - Dữ liệu con người sửa được lưu vào hàng đợi Active Learning để đánh giá và fine-tune mô hình định kỳ."
    )

    q59["explanation"] = (
        "**Bản thiết kế kiến trúc Supervisor-Worker:**\n"
        "1. **Supervisor Agent (Điều phối trung tâm):**\n"
        "   - Nhận batch phản hồi khách hàng thô.\n"
        "   - Phân chia công việc thành 3 tác vụ độc lập và định tuyến dữ liệu cho các Worker chuyên trách.\n"
        "   - Tổng hợp kết quả đầu ra từ các Worker và xuất báo cáo hoàn chỉnh.\n"
        "2. **Sentiment Analysis Worker:**\n"
        "   - Đầu vào: Nội dung phản hồi.\n"
        "   - Nhiệm vụ: Phân loại nhãn cảm xúc (Positive, Neutral, Negative) kèm điểm số tin cậy (confidence score).\n"
        "3. **Topic Extraction Worker:**\n"
        "   - Đầu vào: Nội dung phản hồi.\n"
        "   - Nhiệm vụ: Trích xuất các chủ đề/khía cạnh chính (UI/UX, Giá cả, CSKH, Tốc độ giao hàng, Lỗi hệ thống).\n"
        "4. **Report Generator Worker:**\n"
        "   - Đầu vào: Ma trận Sentiment + Topic từ 2 worker trên.\n"
        "   - Nhiệm vụ: Phân tích xu hướng, tổng hợp thống kê và sinh văn bản báo cáo tóm tắt (Executive Summary) cho ban quản trị.\n\n"
        "**Cơ chế Feedback Loop & Human-in-the-loop (Yêu cầu đề thi gốc):**\n"
        "- **Ngưỡng kích hoạt (Escalation Trigger):** Khi bất kỳ Worker nào trả về lỗi hoặc có Điểm tin cậy (Confidence Score) < 80%, tác vụ sẽ tự động kích hoạt cơ chế Fallback và định tuyến sang hàng đợi của chuyên viên con người (Human-in-the-loop).\n"
        "- **Vòng lặp phản hồi (Feedback Loop):** Chuyên viên kiểm duyệt và chỉnh sửa nhãn chuẩn. Các ca biên khó này được lưu trữ thành tập dữ liệu phản hồi (Feedback Dataset / Active Learning Queue) dùng để kiểm thử hồi quy (Regression Test) và tinh chỉnh prompt/fine-tune model cho các phiên bản tiếp theo."
    )

    # =========================================================================
    # 3. CẬP NHẬT CÂU 60 (BỔ SUNG 3 THÀNH PHẦN CỐT LÕI OUTPUT CONTRACT)
    # =========================================================================
    q60 = q_map[60]
    q60["quick_tip"] = (
        "• **Khái niệm:** Quy định bắt buộc trong prompt yêu cầu AI trả về đúng khuôn mẫu (thường là **JSON chuẩn**).\n"
        "• **3 thành phần cốt lõi bắt buộc phải có:**\n"
        "  1. **Format/Schema:** Định dạng chuẩn (JSON Schema, danh sách trường key bắt buộc, kiểu dữ liệu).\n"
        "  2. **Constraints:** Ràng buộc giá trị (độ dài tối đa, enum giá trị hợp lệ, cấm thêm văn bản giải thích ngoài JSON).\n"
        "  3. **Fallback/Error Handling:** Quy tắc trả về khi thiếu dữ liệu hoặc gặp lỗi (ví dụ: `{\"status\": \"error\", \"code\": \"...\"}`).\n"
        "• **2 lý do sống còn trong Production API:**\n"
        "  1. Giúp code backend đọc được tự động (`json.loads()`), **không bị lỗi sập app** do AI viết lời chào dẫn thừa ('Đây là kết quả...').\n"
        "  2. Đảm bảo tính tất định dữ liệu và tích hợp mượt mà trong chuỗi công cụ (Tool Chaining/Pipeline)."
    )

    q60["explanation"] = (
        "**Trả lời:**\n"
        "- **Định nghĩa Output Contract:** Output contract (Giao ước đầu ra) là tập hợp các quy định bắt buộc được định nghĩa tường minh trong system prompt, yêu cầu LLM phải trả về kết quả tuân thủ nghiêm ngặt một định dạng xác định mà máy móc có thể đọc được (machine-readable).\n\n"
        "- **3 thành phần cốt lõi bắt buộc phải có:**\n"
        "  1. **Định dạng chuẩn (Output Format & Schema):** Chỉ định rõ cấu trúc dữ liệu (JSON Schema, XML, regex), danh sách khóa (keys) bắt buộc và kiểu dữ liệu từng trường (string, integer, boolean, list).\n"
        "  2. **Ràng buộc giá trị & quy tắc sinh (Field Constraints):** Quy định tập giá trị cho phép (enum values), độ dài ký tự tối đa, và chỉ thị cấm tuyệt đối việc tự ý chèn văn bản mở đầu/kết thúc ngoài cấu trúc JSON (`no conversational preamble`).\n"
        "  3. **Quy tắc xử lý ngoại lệ (Error Handling & Fallback):** Cấu trúc chuẩn mực để agent phản hồi khi thông tin đầu vào không đủ, không hợp lệ hoặc gặp lỗi (ví dụ trả về `{\"status\": \"failed\", \"reason\": \"insufficient_data\"}`).\n\n"
        "- **Tầm quan trọng sống còn trong Production:**\n"
        "  1. **Tính tương thích hệ thống (Machine-readable & Anti-crash):** Giúp code backend phân tích cú pháp an toàn bằng `json.loads()` mà không bị lỗi crash parser do LLM sinh lời chào dẫn thừa ('Here is your response...').\n"
        "  2. **Tích hợp Tool Chaining:** Cho phép output của agent này làm input tin cậy cho agent hoặc API tiếp theo trong pipeline nghiệp vụ.\n"
        "  3. **Kiểm thử tự động & Đảm bảo SLA:** Cho phép viết các bài unit test tự động xác minh tính toàn vẹn của dữ liệu đầu ra trước khi gửi cho client."
    )

    # =========================================================================
    # 4. CẬP NHẬT CÂU 67 (BỔ SUNG INCIDENT RESPONSE 4 BƯỚC ĐÊM THỨ SÁU)
    # =========================================================================
    q67 = q_map[67]
    q67["quick_tip"] = (
        "• **Ý 1 (3 sai lầm lớn):**\n"
        "  1. Vi phạm quy tắc: Cấm triển khai vào chiều thứ Sáu (không có người trực cuối tuần).\n"
        "  2. Không chạy kiểm thử hồi quy (không đo độ trễ và chi phí trước khi phát hành).\n"
        "  3. Thiếu kiểm thực khuôn mẫu dữ liệu (output contract) làm gãy hệ thống phía sau.\n"
        "• **Ý 2 (Kế hoạch ứng cứu khẩn cấp 4 bước trong đêm thứ Sáu & Tối ưu chi phí):**\n"
        "  - *Ứng phó sự cố 4 bước:* Bước 1: Rollback ngay về GPT-3.5; Bước 2: Bật fallback banner bảo trì; "
        "Bước 3: Thu thập log lỗi & spikes; Bước 4: Tái hiện sự cố trong staging.\n"
        "  - *Tối ưu chi phí:* Áp dụng **Phân luồng mô hình (Model Routing)**: Dùng model nhỏ rẻ (GPT-4o-mini) cho 80% câu dễ, chỉ route câu phức tạp sang GPT-4o.\n"
        "• **Ý 3 (Quy trình CI/CD chuẩn 5 bước):**\n"
        "  Lưu mã nguồn → Kiểm thử tự động → Đánh giá chất lượng (Eval Gate) → Chạy thử nghiệm Canary 10% → Triển khai toàn bộ."
    )

    q67["explanation"] = (
        "- **Ý 1: Phân tích các sai lầm trong quá trình triển khai.**\n"
        "  👉 **Trả lời:**\n"
        "  1. Vi phạm nguyên tắc 'Never deploy on Friday evening': Triển khai vào chiều thứ Sáu khiến team không kịp ứng cứu sự cố trong kỳ nghỉ cuối tuần.\n"
        "  2. Không chạy kiểm thử hồi quy (Regression test) và Eval gate: Không đo lường benchmark độ trễ và chi phí trước khi release chính thức.\n"
        "  3. Thiếu schema validation / output contract: Model mới sinh format khác làm crash parser backend của downstream services.\n\n"
        "- **Ý 2: Kế hoạch ứng cứu khẩn cấp (Incident Response 4 bước) & Giải pháp chi phí.**\n"
        "  👉 **Trả lời:**\n"
        "  * **Kế hoạch ứng cứu sự cố khẩn cấp 4 bước (Incident Response):**\n"
        "    - *Bước 1 (Rollback tức thì):* Trong vòng 5-10 phút đầu, kích hoạt cờ rollback đưa hệ thống ngay lập tức trở lại model ổn định GPT-3.5 để khôi phục dịch vụ cho người dùng.\n"
        "    - *Bước 2 (Fallback & Thông báo sự cố):* Bật cơ chế chuyển mạch dự phòng (Circuit Breaker / Fallback response) hoặc hiển thị banner bảo trì nhẹ đối với các chức năng đang bị nghẽn parser.\n"
        "    - *Bước 3 (Thu thập dữ liệu & Log):* Trích xuất toàn bộ system logs, latency metrics, token consumption, và các payloads làm crash parser để phục vụ phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA).\n"
        "    - *Bước 4 (Tái hiện & Khắc phục trên Staging):* Cô lập môi trường Staging, tái hiện chính xác luồng lỗi và chạy lại bộ test kiểm định trước khi xem xét nâng cấp lại vào đầu tuần.\n"
        "  * **Giải pháp chi phí token tăng 6x:**\n"
        "    - Chỉ chấp nhận nếu Task Completion Rate tăng rõ rệt bù đắp được chi phí.\n"
        "    - *Giải pháp tối ưu:* Áp dụng **Phân luồng mô hình (Model Routing)** — định tuyến 80% câu hỏi thông thường/chào hỏi sang model nhỏ giá rẻ (GPT-4o-mini), chỉ 20% yêu cầu suy luận phức tạp hoặc khiếu nại mới chuyển sang GPT-4o. Kết hợp Prompt Caching và tinh gọn System Prompt.\n\n"
        "- **Ý 3: Thiết kế CI/CD pipeline chuẩn cho AI kèm Eval Gate.**\n"
        "  👉 **Trả lời:** Pipeline chuẩn 6 bước: (1) Code/Prompt Commit → (2) Unit Tests & Output Schema Validation → "
        "(3) Offline Evaluation trên tập Golden Dataset đo Faithfulness/Accuracy → "
        "(4) Cost & Latency Benchmark Gate (chặn deploy nếu P99 > 1.5s hoặc cost vượt ngân sách) → "
        "(5) Canary Release (10% traffic thực tế) có giám sát Real-time Metrics → "
        "(6) Full Rollout & Auto-Rollback trigger nếu tỷ lệ lỗi tăng > 1%."
    )

    # =========================================================================
    # 5. CHUẨN HÓA CÂU 56 (origin_sub_questions sub 2 đáp án chuỗi nối)
    # =========================================================================
    q56 = q_map[56]
    for sub in q56.get("origin_sub_questions", []):
        if "A1→" in sub.get("answer", ""):
            sub["answer"] = "A1→B5, A2→B4, A3→B3, A4→B1, A5→B2"

    print(f"[*] Saving updated data back to {JSON_PATH}...")
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("[+] Successfully updated questions_db.json with all enhancements!")

if __name__ == "__main__":
    apply_enhancements()
