# 📋 IMPLEMENTATION PLAN: CHUẨN HÓA GẠCH ĐẦU DÒNG 38 ĐÁP ÁN CÂU CON (>70% ĐIỂM) & NÂNG CẤP UI RENDER BULLET

## 1. Mục tiêu Sprint
- **Chuẩn hóa nội dung 38 câu con (Q53 - Q68):**
  + 100% đáp án câu con phải có gạch đầu dòng (`•`), mỗi ý rõ ràng trên từng dòng.
  + Súc tích, vừa phải, đúng trọng tâm "Bí kíp >70% điểm ăn chắc", làm nổi bật từ khóa chính (in đậm `**keyword**` quan trọng).
  + Quy tắc ngôn ngữ theo chỉ đạo của Sếp: Ưu tiên tiếng Việt giải thích dễ học thuộc; CHỈ giữ tiếng Anh đối với thuật ngữ chuyên môn bắt buộc và luôn kèm giải nghĩa tiếng Việt súc tích bên cạnh.
  + Cập nhật trực tiếp vào `questions_db.json`.
- **Nâng cấp giao diện hiển thị trong `index.html`:**
  + Tạo hàm chuyên dụng `renderSubAnswer(rawAnswer)` an toàn XSS.
  + Chuyển đổi các dòng bullet `•` thành danh sách các ý có thụt lề, bullet badge màu nổi bật, khoảng cách dòng `space-y-2` thoáng mắt.
  + Hỗ trợ định dạng `**in đậm**` và `` `code/thuật ngữ` `` giúp mắt người đọc quét nhanh từ khóa chính.
  + Đảm bảo giao diện responsive hoàn hảo trên cả điện thoại di động và máy tính để bàn.
- **Đồng bộ toàn hệ thống & Deploy:**
  + Đồng bộ dữ liệu `questions_db.json` vào `index.html`.
  + Đồng bộ 100% sang 2 file Desktop:
    * `C:\Users\Admin\Desktop\học tập\on_tap_ai_ml.html`
    * `C:\Users\Admin\Desktop\on_tap_ai_ml.html`
  + Git commit & push lên repo GitHub `https://github.com/nep94121-lab/on-tap-ai-ml`.
  + Deploy Vercel Production (`vercel --prod --yes --scope tuananhs-projects-8aea56ce`).
  + Chạy kiểm thử tự động Live E2E payload và nghiệm thu.

## 2. Kế hoạch Milestones (M1 - M7)
- **M1: Thiết kế & Chuẩn hóa toàn bộ 38 đáp án câu con (Data Layer)**
  - Soạn thảo và chuẩn hóa đáp án cho từng câu con từ Q53 đến Q68 theo tiêu chí:
    * Có gạch đầu dòng `•`.
    * In đậm `**từ khóa**`.
    * Dưới 4 bullet mỗi câu, súc tích, ăn chắc >70% điểm.
    * Giải thích tiếng Việt + thuật ngữ tiếng Anh chuẩn.
  - Cập nhật vào `questions_db.json`.
- **M2: Nâng cấp Logic Render UI trong `index.html` (Presentation Layer)**
  - Viết hàm `renderSubAnswer(text)` trong `index.html`.
  - Thay thế render `${sq.answer}` bằng `${renderSubAnswer(sq.answer)}`.
  - Thiết kế CSS / Tailwind styling cho từng bullet item cực kỳ đẹp mắt, thoáng mắt.
- **M3: Đồng bộ dữ liệu vào `index.html`**
  - Chạy script `sync_questions_to_html.py` để cập nhật `const questions = [...]`.
- **M4: Đồng bộ sang 2 file Desktop**
  - Sao chép đè sang 2 file đích trên Desktop và kiểm tra SHA256.
- **M5: Kiểm thử tự động (QA Challenger & Tech Lead 10-Tier Pre-Flight)**
  - Kiểm tra 38 câu con: 100% có bullet, 100% có bold keyword, không rỗng.
  - Kiểm tra hàm `renderSubAnswer`: escape XSS, parse bold, code, bullet.
  - Kiểm tra SHA256 3 file HTML trùng khớp 100%.
- **M6: Git Commit & Push Remote**
  - Git commit & push `origin master`.
- **M7: Deploy Vercel Production & Live E2E Verification**
  - Deploy Vercel Production và kiểm tra live URL.
  - Lập `handoff.md` và báo cáo hoàn tất cho Agent Chính.
