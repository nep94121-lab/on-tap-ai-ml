# 🚫 DEAD ENDS LOG

Ghi nhận các hướng tiếp cận thất bại hoặc không khả thi để tránh lặp lại sai lầm.

| STT | Thời Điểm | Hướng Tiếp Cận | Lý Do Thất Bại / Rủi Ro | Hướng Thay Thế Khả Thi |
|:---:|---|---|---|---|
| 1 | 2026-09-04 | Dùng regex đơn giản để parse và replace mảng JS lớn | Rủi ro cú pháp JSON / JS escaping, có thể làm gãy HTML | Dùng script Python đọc `index.html`, định vị chính xác dòng `const questions = ` và thay thế bằng `json.dumps(..., ensure_ascii=False)` chuẩn xác |
| 2 | 2026-09-04 | Chạy trực tiếp `update_index_html.py` | `update_index_html.py` là template cũ, thiếu logic audioMap, speed_70 mode, và khối `origin_sub_questions`. Chạy file này sẽ làm mất các tính năng mới của `index.html` | Viết script đồng bộ chỉ cập nhật đúng mảng `const questions = [...]` tại dòng 199 trong `index.html`, giữ nguyên 100% template HTML/JS hiện có |
