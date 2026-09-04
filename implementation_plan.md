# 🗺️ KẾ HOẠCH TRIỂN KHAI (IMPLEMENTATION PLAN)
## Dự án: Đồng bộ origin_sub_questions & Deploy Production Vercel

### 1. Mục Tiêu
Khắc phục triệt để lỗi thiếu 38 câu hỏi con trong 16 câu tự luận (53-68) trên web app tĩnh, đồng bộ 3 file HTML, commit & push git, deploy Vercel Production và kiểm thử live E2E.

---

### 2. Phân Rã Milestones & Tiêu Chí Kiểm Thử

#### **Milestone 1: Đồng bộ dữ liệu vào `index.html`**
- **Nhiệm vụ:** Viết và chạy script Python `sync_questions_to_html.py` để nạp `questions_db.json` mới nhất vào mảng `const questions = [...]` trong `index.html`.
- **Tiêu chuẩn:** Giữ nguyên 100% cấu trúc HTML, CSS, JS runtime helper functions hiện có (`toggleSubQuestions`, renderMarkdown, filter, search, etc.).
- **Exit Criteria:** `index.html` chứa chính xác 68 câu hỏi, 16 câu tự luận có `origin_sub_questions`, tổng cộng 38 câu hỏi con.

#### **Milestone 2: Kiểm thử xác nhận trên đĩa (Disk Assertions)**
- **Nhiệm vụ:** Chạy test suite độc lập kiểm tra:
  - Câu 53 có `origin_sub_questions` với đầy đủ các trường `num`, `question`, `points`, `answer`, `source`.
  - Toàn bộ 16 câu tự luận (IDs 53 - 68) đều có trường này.
  - Tổng số câu hỏi con bằng 38.
- **Exit Criteria:** Test suite PASS 100%.

#### **Milestone 3: Đồng bộ sang 2 file đích**
- **Nhiệm vụ:** Sao chép nguyên vẹn `index.html` đè sang:
  1. `C:\Users\Admin\Desktop\học tập\on_tap_ai_ml.html`
  2. `C:\Users\Admin\Desktop\on_tap_ai_ml.html`
- **Exit Criteria:** Cả 2 file đích có hash SHA256 / byte size trùng khớp 100% với `index.html`.

#### **Milestone 4: Git Commit & Push**
- **Nhiệm vụ:**
  - Cấu hình PATH chứa gh-cli (`C:\Users\Admin\AppData\Local\gh-cli\bin`).
  - Stage `index.html`, `questions_db.json`, `GATE_STATUS.md`, `DEAD_ENDS.md`, `implementation_plan.md`.
  - Commit với thông điệp chuẩn mực: `fix(data): sync origin_sub_questions from questions_db.json to index.html and root copies`.
  - Push lên `origin/master`.
- **Exit Criteria:** Git working tree clean, push thành công lên GitHub repo `https://github.com/nep94121-lab/on-tap-ai-ml`.

#### **Milestone 5: Deploy Vercel Production**
- **Nhiệm vụ:**
  - Chạy lệnh: `vercel --prod --yes --scope tuananhs-projects-8aea56ce`.
- **Exit Criteria:** Vercel trả về mã thành công (exit code 0), URL production sẵn sàng.

#### **Milestone 6: Kiểm thử Live E2E (Curl & Payload Verification)**
- **Nhiệm vụ:**
  - Dùng curl / Python requests tải nội dung từ `https://on-tap-ai-ml.vercel.app`.
  - Kiểm tra sự xuất hiện của `origin_sub_questions`, chuỗi câu hỏi con của câu 53 và chuỗi `NGUỒN GỐC TỪ ĐỀ THI GỐC`.
- **Exit Criteria:** Payload live production chứa đầy đủ dữ liệu mới nhất.

#### **Milestone 7: Handoff & Báo Cáo**
- **Nhiệm vụ:** Lập `handoff.md`, dọn dẹp các script scratch, gửi báo cáo tổng kết chi tiết cho Agent Chính.
