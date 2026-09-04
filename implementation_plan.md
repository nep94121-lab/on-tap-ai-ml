# 📋 IMPLEMENTATION PLAN: RÀ SOÁT & ĐỒNG BỘ NỘI DUNG 16 CÂU TỰ LUẬN (53-68)

## 1. Mục tiêu
- Sửa triệt để Câu 68: Bổ sung đủ 4 chỉ số RAGAS (Faithfulness, Answer Relevance, Context Precision, Context Recall) kèm định nghĩa, ngưỡng chuẩn Release cho cả 4 chỉ số, và phân tích tầng Retrieval khi Context Recall thấp.
- Bổ sung các câu tự luận khác có câu hỏi con chưa được phản ánh đủ trong quick_tip/explanation:
  + Câu 59: Bổ sung Cơ chế Vòng lặp phản hồi (Feedback Loop) & Human-in-the-loop khi Worker gặp lỗi / confidence < 80%.
  + Câu 60: Bổ sung 3 thành phần cốt lõi của Output Contract (Định dạng Schema, Ràng buộc giá trị, Quy tắc xử lý ngoại lệ/Fallback).
  + Câu 67: Bổ sung Kế hoạch ứng phó sự cố khẩn cấp (Incident Response) 4 bước trong đêm thứ Sáu.
  + Câu 56: Chuẩn hóa chuỗi đáp án ghép nối trong origin_sub_questions.
- Đồng bộ toàn bộ dữ liệu sang `index.html` và 2 file đích trên máy người dùng.
- Kiểm thử tự động, Git push và Deploy Vercel Production.

## 2. Kế hoạch Milestones chi tiết
- **M1: Cập nhật `questions_db.json`**
  - Viết script Python `apply_essay_enhancements.py` để cập nhật chính xác và an toàn các trường `quick_tip`, `explanation`, `origin_sub_questions`.
  - Kiểm tra tính hợp lệ JSON (valid syntax, không thoát ký tự lỗi).
- **M2: Đồng bộ sang `index.html`**
  - Dùng `sync_questions_to_html.py` để nhúng `const questions = [...]` trực tiếp vào `index.html`.
  - Đảm bảo giữ nguyên các tính năng UI, thẻ tag, và hiển thị `origin_sub_questions`.
- **M3: Đồng bộ đè sang 2 file đích**
  - Sao chép đè file `index.html` sang:
    1. `C:\Users\Admin\Desktop\học tập\on_tap_ai_ml.html`
    2. `C:\Users\Admin\Desktop\on_tap_ai_ml.html`
- **M4: Kiểm thử tự động (Quality Assurance)**
  - Viết script `test_essay_completeness.py` kiểm tra assertions:
    + Câu 68: có đủ 4 chỉ số RAGAS, có đủ 4 ngưỡng release, có phân tích Retrieval.
    + Câu 59: có Feedback Loop & Human-in-the-loop.
    + Câu 60: có 3 thành phần Output Contract.
    + Câu 67: có 4 bước Incident Response.
    + Toàn bộ 16 câu tự luận có đủ origin_sub_questions và nội dung đầy đủ.
    + Kiểm tra cả 3 file HTML đồng bộ 100%.
- **M5: Git Commit & Push**
  - Commit với thông điệp chuẩn hóa rõ ràng.
  - Push lên remote repo `origin/master`.
- **M6: Deploy Vercel Production**
  - Chạy `vercel --prod --yes --scope tuananhs-projects-8aea56ce`.
- **M7: Live Production Payload Verification**
  - Curl trực tiếp URL Vercel production kiểm tra payload Câu 68 có đủ 4 chỉ số RAGAS và các câu khác.
