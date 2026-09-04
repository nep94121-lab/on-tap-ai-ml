# 📋 IMPLEMENTATION PLAN: NÂNG CẤP GIAO DIỆN CÂU CON TƯƠNG TÁC & ĐỒNG BỘ ĐÁP ÁN VỚI QUICK_TIP

## 1. Mục tiêu
- **Đồng bộ nội dung:** Rà soát toàn bộ 38 câu hỏi con trong 16 câu tự luận (53 - 68) trong `questions_db.json`. Nội dung trường `answer` của từng câu con phải đồng bộ 100% với nội dung chuẩn, súc tích, dễ nhớ trong `quick_tip`. Đặc biệt tại Câu 68: Câu con 2 phải ghi rõ cả định nghĩa súc tích của 4 chỉ số RAGAS (Faithfulness, Answer Relevance, Context Precision, Context Recall) và ngưỡng release.
- **Nâng cấp giao diện tương tác (Interactive Sub-questions UI):**
  + Thu gọn sẵn phần đáp án `👉 Đáp án câu này:` ở mỗi câu con, có nút bấm `[👁️ Xem đáp án ▼]` <-> `[Thu gọn đáp án ▲]`.
  + Bổ sung khu vực Textarea ghi câu trả lời riêng cho từng câu con, tự động lưu vào `localStorage` key `sub_ans_{qid}_{idx}`, có hiển thị số ký tự và nút xóa nháp.
  + Thêm nút tiện ích "Mở tất cả đáp án" / "Thu gọn tất cả đáp án" ở đầu khối Nguồn gốc.
- **Đồng bộ toàn hệ thống & Deploy:**
  + Cập nhật `index.html` và sao chép 100% sang 2 file đích Desktop.
  + Git commit & push lên repo GitHub.
  + Deploy Vercel Production và kiểm thử Live payload.

## 2. Kế hoạch Milestones chi tiết
- **M1: Rà soát & Cập nhật `questions_db.json`**
  - Viết script Python chuẩn hóa `origin_sub_questions[].answer` cho cả 38 câu con ăn khớp với `quick_tip`.
  - Cập nhật Câu 68 câu con 2 đầy đủ 4 định nghĩa RAGAS + ngưỡng.
- **M2: Nâng cấp Template UI và JS trong `index.html`**
  - Cập nhật khối render `origin_sub_questions` (ẩn đáp án, nút toggle từng câu con, textarea luyện gõ câu trả lời, badge lưu localStorage, nút xóa nháp).
  - Thêm nút "Mở tất cả đáp án" / "Thu gọn tất cả đáp án" tại header câu con.
  - Viết các hàm JS: `toggleSubAnswer(qid, idx)`, `toggleAllSubAnswers(qid, showAll)`, `saveSubAnswer(qid, idx, val)`, `clearSubAnswer(qid, idx)`.
- **M3: Đồng bộ dữ liệu vào `index.html`**
  - Chạy đồng bộ `const questions = [...]` từ `questions_db.json` sang `index.html`.
- **M4: Sao chép đè sang 2 file đích Desktop**
  - `C:\Users\Admin\Desktop\học tập\on_tap_ai_ml.html`
  - `C:\Users\Admin\Desktop\on_tap_ai_ml.html`
- **M5: Kiểm thử tự động (Quality Assurance & Challenger QA)**
  - Viết và chạy test suite kiểm tra:
    + 68 câu, 16 câu tự luận, 38 câu con.
    + Câu 68 sub 2 có 4 chỉ số RAGAS + định nghĩa + ngưỡng.
    + Các hàm JS và thành phần UI trong cả 3 file HTML.
    + SHA256 checksum 3 file đồng nhất 100%.
- **M6: Git Commit & Push Remote**
  - `git commit` với thông điệp chuẩn hóa.
  - `git push origin master`.
- **M7: Deploy Vercel Production & Live Verification**
  - `vercel --prod --yes --scope tuananhs-projects-8aea56ce`.
  - Curl live production URL kiểm tra payload và giao diện.
