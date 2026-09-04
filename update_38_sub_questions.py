#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_38_sub_questions.py
Chuẩn hóa 100% (38/38) đáp án câu hỏi con trong origin_sub_questions (Câu 53 - 68).
Tuân thủ nghiêm ngặt:
1. Gạch đầu dòng rõ ràng từng ý (bullet •).
2. Súc tích, vừa phải, đúng trọng tâm "Bí kíp >70% điểm ăn chắc".
3. Làm nổi bật từ khóa chính (in đậm **keyword** quan trọng).
4. Quy tắc ngôn ngữ theo chỉ đạo của Sếp:
   - Ưu tiên giải thích, diễn đạt bằng TIẾNG VIỆT tự nhiên, dễ học thuộc.
   - Giữ TIẾNG ANH cho các thuật ngữ chuyên môn bắt buộc của đề thi kèm giải nghĩa tiếng Việt ngắn gọn, dễ hiểu bên cạnh.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "questions_db.json")

SUB_ANSWERS = {
    # ================= CÂU 53 (3 câu con) =================
    53: [
        {
            "num": "Câu con 1",
            "answer": "• **Từ khóa chuẩn:** `Thought` (hoặc `thought`).\n• **Ý nghĩa tiếng Việt:** Bước **suy nghĩ / lập luận** của Agent để định hướng mục tiêu trước khi ra quyết định hành động.\n• **Mẹo nhớ:** Chữ **T** trong chuỗi **T - A - O** (Táo: Nghĩ → Làm → Nhìn)."
        },
        {
            "num": "Câu con 2",
            "answer": "• **Từ khóa chuẩn:** `Action` (hoặc `action`).\n• **Ý nghĩa tiếng Việt:** Bước **hành động / gọi công cụ** (`Tool calling`) với tham số cụ thể dựa trên suy nghĩ vừa lập luận.\n• **Mẹo nhớ:** Chữ **A** trong chuỗi **T - A - O**."
        },
        {
            "num": "Câu con 3",
            "answer": "• **Từ khóa chuẩn:** `Observation` (hoặc `observation`).\n• **Ý nghĩa tiếng Việt:** Bước **quan sát / ghi nhận kết quả** trả về từ môi trường hoặc công cụ để nạp lại vào ngữ cảnh cho vòng lặp kế tiếp.\n• **Mẹo nhớ:** Chữ **O** trong chuỗi **T - A - O**."
        }
    ],

    # ================= CÂU 54 (3 câu con) =================
    54: [
        {
            "num": "Câu con 1",
            "answer": "• **Từ khóa chuẩn:** `temperature`.\n• **Ý nghĩa tiếng Việt:** Tham số kiểm soát **độ ngẫu nhiên và sáng tạo** của câu trả lời.\n• **Quy tắc sử dụng:** Đặt bằng `0` để có câu trả lời tất định, chuẩn xác (dùng cho trích xuất, code); đặt cao (`0.7 - 1.0`) khi cần sáng tạo nội dung phong phú."
        },
        {
            "num": "Câu con 2",
            "answer": "• **Từ khóa chuẩn:** `max_tokens` (hoặc `max_output_tokens`).\n• **Ý nghĩa tiếng Việt:** Tham số **giới hạn độ dài tối đa** của phản hồi sinh ra (tính theo token).\n• **Tác dụng:** Giúp kiểm soát chi phí gọi API và chặn hiện tượng AI trả lời lan man, quá dài."
        },
        {
            "num": "Câu con 3",
            "answer": "• **Từ khóa chuẩn:** `top_p` (hoặc `nucleus sampling`).\n• **Ý nghĩa tiếng Việt:** Tham số **lấy mẫu theo xác suất tích lũy** (`Nucleus Sampling`), chỉ chọn trong nhóm từ tiềm năng có tổng xác suất đạt ngưỡng `p`.\n• **Quy tắc sử dụng:** Thường đặt `top_p = 0.9` để loại bỏ các từ đuôi hiếm gặp; không nên điều chỉnh cùng lúc cả `temperature` và `top_p`."
        }
    ],

    # ================= CÂU 55 (3 câu con) =================
    55: [
        {
            "num": "Câu con 1",
            "answer": "• **Từ khóa chuẩn:** `Embedding` (hoặc `embedding`).\n• **Ý nghĩa tiếng Việt:** Quá trình **chuyển đổi văn bản thành vector số học** nhiều chiều mang đầy đủ ngữ nghĩa sâu xa.\n• **Mẹo nhớ:** \"Đổi chữ ra số\" để máy tính tính toán và so sánh ngữ nghĩa."
        },
        {
            "num": "Câu con 2",
            "answer": "• **Từ khóa chuẩn:** `Cosine similarity` (Độ tương đồng Cosine).\n• **Ý nghĩa tiếng Việt:** Phép đo **góc lượng giác giữa 2 vector**, không phụ thuộc vào độ dài văn bản.\n• **Đặc điểm:** Giá trị càng gần `1` tức là hai đoạn văn càng tương đồng cao về mặt ý nghĩa."
        },
        {
            "num": "Câu con 3",
            "answer": "• **Từ khóa chuẩn:** `top_k` (hoặc `k documents`).\n• **Ý nghĩa tiếng Việt:** Danh sách **k tài liệu có điểm tương đồng cao nhất** được truy xuất (`Retrieval`).\n• **Ứng dụng:** Trích xuất đúng số lượng đoạn tài liệu liên quan nhất làm ngữ cảnh đưa vào LLM."
        }
    ],

    # ================= CÂU 56 (2 câu con) =================
    56: [
        {
            "num": "Câu con 1",
            "answer": "• **A1 — B5 (Discriminative AI):** Trí tuệ nhân tạo phân biệt — Nhiệm vụ **phân loại / dự đoán nhãn** có sẵn dựa trên dữ liệu.\n• **A2 — B4 (Generative AI):** Trí tuệ nhân tạo tạo sinh — Nhiệm vụ **tạo ra dữ liệu mới** (văn bản, hình ảnh, mã nguồn).\n• **A3 — B3 (Agentic AI):** Trí tuệ nhân tạo tự chủ — Có khả năng **tự lập kế hoạch + gọi công cụ + tự điều chỉnh** hành vi theo mục tiêu.\n• **A4 — B1 (LLM):** Mô hình ngôn ngữ lớn — Được huấn luyện trên **kho văn bản khổng lồ** để hiểu và sinh ngôn ngữ tự nhiên.\n• **A5 — B2 (Transformer):** Kiến trúc mạng nơ-ron nền tảng — Hoạt động dựa trên cơ chế **Self-Attention** (tự chú ý)."
        },
        {
            "num": "Câu con 2",
            "answer": "• **Chuỗi ghép nối chuẩn xác 100%:** `A1→B5, A2→B4, A3→B3, A4→B1, A5→B2`\n• **Tóm tắt quy chiếu:**\n  - `A1→B5`: Phân loại dữ liệu có sẵn.\n  - `A2→B4`: Sinh dữ liệu mới tạo sinh.\n  - `A3→B3`: Tự chủ lập kế hoạch & gọi tool.\n  - `A4→B1`: Học từ kho văn bản khổng lồ.\n  - `A5→B2`: Cơ chế Self-Attention."
        }
    ],

    # ================= CÂU 57 (2 câu con) =================
    57: [
        {
            "num": "Câu con 1",
            "answer": "• `[B] Load`: **Nạp tài liệu thô** từ nguồn (PDF, Word, Web, Cơ sở dữ liệu).\n• `[E] Clean`: **Làm sạch văn bản**, loại bỏ ký tự thừa, định dạng HTML rác.\n• `[A] Chunk`: **Cắt đoạn văn bản** thành các khối nhỏ vừa vặn (200 - 500 tokens kèm overlap).\n• `[C] Embed`: **Mã hóa vector**, đổi từng đoạn văn thành vector số học mang ngữ nghĩa.\n• `[D] Store`: **Lưu trữ vector** cùng dữ liệu phụ trợ (metadata) vào cơ sở dữ liệu vector."
        },
        {
            "num": "Câu con 2",
            "answer": "• **Thứ tự đúng:** `B → E → A → C → D` (tương ứng: `Load → Clean → Chunk → Embed → Store`).\n• **Mẹo nhớ 5 chữ vàng:** **Nạp → Lọc → Cắt → Đổi → Lưu**.\n• **Giải thích quy trình:** Phải nạp tài liệu vào (B) → Làm sạch nội dung (E) → Cắt nhỏ đoạn văn (A) → Biến thành vector (C) → Lưu vào kho vector database (D)."
        }
    ],

    # ================= CÂU 58 (2 câu con) =================
    58: [
        {
            "num": "Câu con 1",
            "answer": "• `[B] Problem Definition`: **Xác định bài toán kinh doanh**, đối tượng sử dụng và mục tiêu ROI.\n• `[D] Data Prep`: **Chuẩn bị dữ liệu**, thu thập, làm sạch và gán nhãn dữ liệu đại diện.\n• `[E] Model Selection & Dev`: **Lựa chọn mô hình**, thiết kế prompt hoặc tinh chỉnh (fine-tune) xây bản mẫu MVP.\n• `[A] Eval`: **Đánh giá & kiểm thử**, đo lường hiệu năng bằng tập dữ liệu chuẩn trước khi phát hành.\n• `[C] Deploy & Monitor`: **Triển khai & giám sát**, vận hành thực tế, theo dõi độ trễ, chi phí và lỗi."
        },
        {
            "num": "Câu con 2",
            "answer": "• **Thứ tự đúng:** `B → D → E → A → C` (tương ứng: `Problem Definition → Data Prep → Model Selection & Dev → Eval → Deploy & Monitor`).\n• **Mẹo nhớ 5 chữ vàng:** **Định vị → Dữ liệu → Dựng mẫu → Đánh giá → Triển khai**.\n• **Nguyên tắc sống còn:** Luôn kiểm thử đánh giá (Eval) đạt chuẩn chất lượng rồi mới được triển khai (Deploy)."
        }
    ],

    # ================= CÂU 59 (2 câu con) =================
    59: [
        {
            "num": "Câu con 1",
            "answer": "• **Supervisor Agent (Quản lý):** Nhận phản hồi thô của khách hàng, phân tích ý định (`intent`), điều phối công việc cho 3 Worker và tổng hợp kết quả cuối cùng.\n• **Worker 1 (Phân tích cảm xúc):** Gán nhãn cảm xúc khách hàng (**Tích cực / Tiêu cực / Trung tính**).\n• **Worker 2 (Trích xuất chủ đề):** Bóc tách các vấn đề cụ thể khách hàng phản ánh (**Giá cả, Giao hàng, Lỗi kỹ thuật, CSKH**).\n• **Worker 3 (Sinh báo cáo):** Tổng hợp dữ liệu định lượng từ Worker 1 & 2 thành báo cáo chỉ số cho cấp quản lý."
        },
        {
            "num": "Câu con 2",
            "answer": "• **Cơ chế chuyển tiếp (Human Escalation):** Khi Worker gặp lỗi hoặc điểm tin cậy `< 80%`, hệ thống tự động chuyển tiếp cho **chuyên viên con người** thẩm định và giải quyết.\n• **Vòng lặp phản hồi (Feedback Loop):** Ý kiến sửa đổi của chuyên viên được tự động lưu vào hàng đợi dữ liệu học chủ động (`Active Learning`).\n• **Tái cải tiến hệ thống:** Dữ liệu này dùng để bổ sung vào tập dữ liệu kiểm định chuẩn (`Golden Dataset`) và fine-tune mô hình định kỳ."
        }
    ],

    # ================= CÂU 60 (2 câu con) =================
    60: [
        {
            "num": "Câu con 1",
            "answer": "• **Định nghĩa:** Là ràng buộc bắt buộc trong prompt yêu cầu mô hình AI trả về đúng **khuôn mẫu dữ liệu chuẩn xác** (thường là JSON), không kèm lời dẫn thừa.\n• **1. Khuôn mẫu (Format/Schema):** Quy định rõ cấu trúc JSON, danh sách các khóa (`keys`) bắt buộc và kiểu dữ liệu.\n• **2. Ràng buộc giá trị (Constraints):** Giới hạn độ dài, danh mục giá trị hợp lệ (`enum`) và cấm tuyệt đối văn bản giải thích thừa.\n• **3. Xử lý lỗi (Fallback/Error Handling):** Quy định rõ cấu trúc dữ liệu trả về khi gặp lỗi hoặc không tìm thấy dữ liệu (`{\"status\": \"error\", \"code\": \"NOT_FOUND\"}`)."
        },
        {
            "num": "Câu con 2",
            "answer": "• **Chống sập hệ thống Backend:** Backend dùng `json.loads()` để đọc tự động; nếu AI tự ý thêm câu chào mở đầu hay kết thúc sẽ gây lỗi cú pháp parser (`JSONDecodeError`) làm sập ứng dụng.\n• **Đảm bảo tính tất định dữ liệu:** Chuẩn hóa đầu ra giúp dữ liệu luôn nhất quán, phục vụ tích hợp an toàn vào chuỗi công cụ tự động (`Tool Chaining / Pipeline`)."
        }
    ],

    # ================= CÂU 61 (2 câu con) =================
    61: [
        {
            "num": "Câu con 1",
            "answer": "• **Chiến lược tối ưu:** Áp dụng **Semantic Chunking** (cắt đoạn theo ranh giới ngữ nghĩa của từng điều khoản chính sách).\n• **Kích thước đoạn:** Giữ khối lượng vừa phải (**200 - 400 tokens**) kèm đoạn gối đầu (**Overlap 10 - 15%**).\n• **Nguyên tắc sống còn:** Cắt trọn vẹn cả câu và điều kiện; **tuyệt đối không cắt ngang giữa câu** để bảo toàn liên kết nhân quả giữa thời hạn (30 ngày) và điều kiện hoàn tiền (còn nguyên tem mác)."
        },
        {
            "num": "Câu con 2",
            "answer": "• **1. `title` (Tên tài liệu):** Ví dụ: \"Chính sách đổi trả & hoàn tiền 2026\" - giúp nhận diện chính xác nguồn tài liệu.\n• **2. `category` (Phân loại):** Ví dụ: \"Hoàn tiền\", \"Vận chuyển\", \"Bảo hành\" - dùng để lọc trước khi tìm kiếm vector (`Metadata Filtering`).\n• **3. `version` (Phiên bản):** Ví dụ: \"v2.1\" hoặc ngày ban hành - đảm bảo chỉ truy xuất chính sách hiện hành, bỏ qua bản cũ.\n• **4. `source_url` (Đường dẫn gốc):** Link văn bản gốc để người dùng hoặc kiểm toán viên đối chiếu kiểm chứng."
        }
    ],

    # ================= CÂU 62 (2 câu con) =================
    62: [
        {
            "num": "Câu con 1",
            "answer": "• **Định nghĩa P99 Latency:** Mốc thời gian mà **99% tổng số yêu cầu được xử lý nhanh hơn**, đo lường trải nghiệm thực tế của **1% người dùng gặp độ trễ tồi tệ nhất**.\n• **Khác biệt cốt lõi:**\n  - **Mean Latency (Trung bình):** Bị kéo tụt xuống bởi các câu hỏi ngắn/dễ, tạo ra con số đẹp giả tạo và che giấu các ca nghẽn mạng.\n  - **P99 Latency:** Nhìn thẳng vào trường hợp xấu nhất lúc cao điểm để nhận diện nguy cơ treo máy."
        },
        {
            "num": "Câu con 2",
            "answer": "• **Khuếch đại độ trễ (Tail Latency Amplification):** Trong Multi-Agent, một câu hỏi kích hoạt chuỗi tuần tự nhiều Agent và gọi nhiều công cụ liên tiếp.\n• **Hệ quả dây chuyền:** Chỉ cần một Agent bước phụ bị chậm hoặc chạm mốc P99, tổng thời gian phản hồi toàn hệ thống sẽ tăng vọt theo cấp số cộng.\n• **Quyết định cam kết SLA:** Nếu P99 không được siết chặt (ví dụ: ≤ 3.0 giây), người dùng sẽ cảm thấy bị treo hệ thống, hủy giao dịch và gây sập hàng đợi lúc cao điểm."
        }
    ],

    # ================= CÂU 63 (2 câu con) =================
    63: [
        {
            "num": "Câu con 1",
            "answer": "• **Thought 1:** Cần tra cứu tỷ giá quy đổi USD sang VND hiện tại bằng cách gọi công cụ `get_exchange_rate`.\n• **Action 1:** `get_exchange_rate(from_currency=\"USD\", to_currency=\"VND\")`\n• **Observation 1:** `{\"status\": \"success\", \"rate\": 25450, \"unit\": \"VND\"}`"
        },
        {
            "num": "Câu con 2",
            "answer": "• **Thought 2:** Đã có tỷ giá 1 USD = 25.450 VND. Tiến hành tính toán: `100 * 25450 = 2,545,000` VND. Đã có đủ dữ kiện để trả lời khách hàng.\n• **Final Answer:** Tỷ giá USD/VND hiện tại là **25.450 VND/USD**, do đó **100 USD quy đổi được 2.545.000 VND**."
        }
    ],

    # ================= CÂU 64 (2 câu con) =================
    64: [
        {
            "num": "Câu con 1",
            "answer": "• **Role / Persona (Vai trò):** \"Bạn là Chuyên viên Hỗ trợ Khách hàng chuyên nghiệp của sàn E-commerce, giao tiếp bằng tiếng Việt lịch sự, thân thiện, đồng cảm và ngắn gọn.\"\n• **Knowledge Base (Căn cứ tri thức):** \"Chỉ trả lời dựa trên thông tin chính sách và dữ liệu đơn hàng được cung cấp trong ngữ cảnh; nếu không có dữ liệu, trả lời thành thật 'Tôi không có thông tin' và hướng dẫn liên hệ hotline, tuyệt đối không tự bịa đặt.\""
        },
        {
            "num": "Câu con 2",
            "answer": "• **Guardrails (Ràng buộc bảo mật & An toàn):** \"Tuyệt đối không yêu cầu, lưu trữ hay tiết lộ thông tin nhạy cảm PII (mật khẩu, mã OTP, số thẻ ngân hàng); từ chối trả lời chủ đề ngoài phạm vi dịch vụ.\"\n• **Output Format (Khuôn mẫu đầu ra):** Luôn trả lời ngắn gọn dưới 150 từ theo định dạng **JSON chuẩn**:\n  `{\"status\": \"success|need_info|error\", \"order_id\": \"...\", \"message\": \"...\", \"next_step\": \"...\"}`"
        }
    ],

    # ================= CÂU 65 (2 câu con) =================
    65: [
        {
            "num": "Câu con 1",
            "answer": "• **Nguyên nhân lỗi:** Sau khi thực thi công cụ, code không lưu kết quả `observation` vào danh sách tin nhắn hội thoại `messages`.\n• **Hậu quả:** Mô hình ở vòng lặp sau không biết kết quả công cụ đã trả về gì, dẫn đến việc liên tục lặp lại thao tác cũ (kẹt trong vòng lặp vô tận).\n• **Cách khắc phục:** Thêm dòng lưu ngữ cảnh ngay sau khi nhận kết quả:\n  `messages.append({\"role\": \"tool\", \"name\": tool_name, \"content\": observation})`"
        },
        {
            "num": "Câu con 2",
            "answer": "• **Nguyên nhân lỗi:** Vòng lặp `while True:` không có biến đếm bước lặp và thiếu điều kiện dừng khi gặp sự cố.\n• **Hậu quả:** Nếu mô hình không sinh ra `Final Answer`, vòng lặp sẽ chạy mãi mãi làm cạn kiệt ngân sách token và gây treo máy chủ.\n• **Cách khắc phục:**\n  - Khởi tạo `step = 0`, sau mỗi vòng lặp tăng `step += 1`.\n  - Đặt điều kiện dừng: nếu `step >= MAX_STEPS` (ví dụ: `5`) hoặc nhận được `Final Answer` thì lập tức gọi lệnh `break`."
        }
    ],

    # ================= CÂU 66 (3 câu con) =================
    66: [
        {
            "num": "Câu con 1",
            "answer": "• **Công thức tính:** `8 người × 8 giờ/ngày × 22 ngày/tháng × 12 tháng × 50.000 VNĐ/giờ`.\n• **Chi phí nhân sự hàng tháng:** `8 × 8 × 22 × 50.000 = 76,8 triệu VNĐ / tháng`.\n• **Tổng chi phí baseline nhân sự 1 năm:** `76,8 triệu × 12 tháng = 921,6 triệu VNĐ / năm`."
        },
        {
            "num": "Câu con 2",
            "answer": "• **Chi phí cài đặt ban đầu (Setup / Capex):** `200 triệu VNĐ` (tích hợp hệ thống, kiểm thử, triển khai).\n• **Chi phí vận hành hàng tháng (Opex):** `15 triệu VNĐ / tháng` (tiền API token LLM + server).\n• **Tổng chi phí AI năm đầu tiên:** `200 triệu + (15 triệu × 12 tháng) = 380 triệu VNĐ`."
        },
        {
            "num": "Câu con 3",
            "answer": "• **Số tiền tiết kiệm ròng sau 1 năm:** `921,6 triệu - 380 triệu = 541,6 triệu VNĐ`.\n• **Tỷ suất hoàn vốn đầu tư:** `ROI = (541,6 triệu / 380 triệu) × 100% = 142,5%`.\n• **Kết luận đánh giá:** Dự án **RẤT ĐÁNG ĐẦU TƯ** vì ROI đạt mức ấn tượng **142,5%** và thời gian hoàn vốn chỉ mất khoảng **5 tháng**."
        }
    ],

    # ================= CÂU 67 (3 câu con) =================
    67: [
        {
            "num": "Câu con 1",
            "answer": "• **Lỗi 1 (Triển khai chiều thứ Sáu):** Vi phạm nguyên tắc an toàn vận hành, triển khai vào cuối tuần khi đội ngũ kỹ thuật không túc trực để cứu trợ sự cố.\n• **Lỗi 2 (Bỏ qua kiểm thử Eval Gate):** Không chạy bộ đánh giá tự động (`Golden Eval`) để đo lường độ trễ và chi phí trước khi phát hành diện rộng.\n• **Lỗi 3 (Thiếu Output Contract & Canary):** Không kiểm soát khuôn mẫu đầu ra làm gãy backend; tung thẳng 100% lưu lượng mà không thử nghiệm Canary và thiếu cơ chế Rollback tự động."
        },
        {
            "num": "Câu con 2",
            "answer": "• **Bước 1 (Rollback tức thì):** Khôi phục ngay phiên bản mô hình ổn định trước đó (GPT-3.5) để cứu vãn hệ thống.\n• **Bước 2 (Bật fallback banner):** Kích hoạt thông báo bảo trì nhẹ để giảm áp lực cho người dùng.\n• **Bước 3 (Thu thập log lỗi):** Xuất toàn bộ log hệ thống, phân tích các điểm tăng vọt (spikes) về chi phí và độ trễ.\n• **Bước 4 (Tái hiện lỗi trong Staging):** Chạy lại các ca lỗi trong môi trường thử nghiệm riêng biệt để cô lập và xử lý nguyên nhân gốc rễ."
        },
        {
            "num": "Câu con 3",
            "answer": "• **Quy trình chuẩn 5 bước:** `Lưu mã nguồn → Kiểm thử tự động (Unit Test) → Đánh giá chất lượng (Eval Gate) → Thử nghiệm Canary (10%) → Triển khai diện rộng`.\n• **Tiêu chí Eval Gate tự động:** Chạy qua 200 câu trong bộ kiểm định (`Faithfulness ≥ 0.90`, tỷ lệ lỗi cú pháp = 0%).\n• **Tối ưu chi phí bằng Model Routing:** Định tuyến câu hỏi dễ (80%) sang model nhỏ chi phí thấp (`GPT-4o-mini`), chỉ chuyển các câu hỏi phức tạp (20%) sang model lớn (`GPT-4o`)."
        }
    ],

    # ================= CÂU 68 (3 câu con) =================
    68: [
        {
            "num": "Câu con 1",
            "answer": "• **Quy mô bộ dữ liệu:** Tối thiểu **150 - 200 câu hỏi** thực tế từ người dùng xe máy điện.\n• **Tỷ lệ phân bổ kịch bản:**\n  - **70% trường hợp chuẩn:** Tra cứu thời hạn pin, điều kiện bảo hành khung xe, địa chỉ trạm dịch vụ.\n  - **20% trường hợp biên (Edge Cases):** Xe bị ngập nước, tự ý độ chế pin, mất sổ bảo hành.\n  - **10% câu hỏi đối kháng (Prompt Injection):** Cố tình bẫy AI tiết lộ prompt nội bộ hoặc hứa hẹn bồi thường ngoài chính sách.\n• **Chuẩn hóa đáp án:** Toàn bộ câu trả lời chuẩn phải được **thẩm định và ký duyệt bởi chuyên gia CSKH**."
        },
        {
            "num": "Câu con 2",
            "answer": "• **1. `Faithfulness` (Độ trung thực - Ngưỡng ≥ 0.95):** Đo tính trung thực với tài liệu bảo hành, chống bịa đặt thông tin và ảo giác.\n• **2. `Answer Relevance` (Độ liên quan - Ngưỡng ≥ 0.90):** Đo mức độ câu trả lời đi thẳng vào trọng tâm câu hỏi của khách hàng, không trả lời vòng vo.\n• **3. `Context Precision` (Độ chính xác ngữ cảnh - Ngưỡng ≥ 0.80):** Đo tỷ lệ và thứ tự các đoạn văn liên quan được xếp ở các vị trí đầu trong danh sách truy xuất.\n• **4. `Context Recall` (Độ bao phủ ngữ cảnh - Ngưỡng ≥ 0.80):** Đo mức độ tài liệu tìm kiếm được chứa đầy đủ dữ kiện để trả lời trọn vẹn câu hỏi."
        },
        {
            "num": "Câu con 3",
            "answer": "• **Chốt chặn đầu vào (Input Guardrails):** Chặn đứng các câu hỏi tấn công tiêm nhiễm câu lệnh (`Prompt Injection`) và phá rào (`Jailbreak`).\n• **Chốt chặn đầu ra (Output Guardrails):** Che giấu thông tin cá nhân (`PII Masking`), kiểm soát tính xác thực chính sách bảo hành trước khi trả về.\n• **Sửa lỗi Retrieval (khi `Faithfulness` cao mà `Context Recall` thấp):** AI trung thực nhưng trả lời thiếu ý do tìm kiếm sót tài liệu → **Khắc phục ở Tầng Retrieval:** Tăng số lượng tài liệu lấy về (`top-k`), kết hợp tìm kiếm từ khóa và ngữ nghĩa (**Hybrid Search: BM25 + Vector**), và bổ sung bước xếp hạng lại (**Cohere Reranking**)."
        }
    ]
}

def update_db():
    print(f"[*] Đang nạp cơ sở dữ liệu: {JSON_PATH}")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)

    updated_subs = 0
    updated_questions = 0

    for q in questions:
        qid = q["id"]
        if qid in SUB_ANSWERS:
            expected_subs = SUB_ANSWERS[qid]
            current_subs = q.get("origin_sub_questions", [])
            assert len(current_subs) == len(expected_subs), f"Câu {qid}: Số câu con lệch! Hiện có {len(current_subs)}, cấu hình {len(expected_subs)}"
            
            for i, exp in enumerate(expected_subs):
                assert current_subs[i]["num"] == exp["num"], f"Câu {qid} sub {i}: num không khớp ({current_subs[i]['num']} vs {exp['num']})"
                # Cập nhật đáp án mới
                current_subs[i]["answer"] = exp["answer"]
                updated_subs += 1
            
            updated_questions += 1

    assert updated_questions == 16, f"Kỳ vọng cập nhật 16 câu tự luận, thực tế: {updated_questions}"
    assert updated_subs == 38, f"Kỳ vọng cập nhật 38 câu con, thực tế: {updated_subs}"

    print(f"[+] Đã cập nhật thành công {updated_subs} câu con trên {updated_questions} câu tự luận.")
    
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"[+] Đã lưu vào {JSON_PATH} thành công.")

if __name__ == "__main__":
    update_db()
