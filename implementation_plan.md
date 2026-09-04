# 📋 KẾ HOẠCH TRIỂN KHAI: TỐI ƯU GIAO DIỆN DI ĐỘNG TOÀN DIỆN (MOBILE-FIRST POLISH & BUGFIX)

## 🎯 Mục Tiêu Dự Án
Đảm bảo ứng dụng Ôn Tập AI/ML (68 câu) hoạt động hoàn hảo trên mọi kích thước màn hình điện thoại (360px, 375px, 390px, 412px, 430px) và máy tính bảng:
1. 0 lỗi tràn ngang (No horizontal scroll).
2. Chống triệt để iOS Safari auto-zoom khi chạm vào ô nhập liệu / nháp.
3. Hàng nút bấm câu con, thanh công cụ bóc tách điểm co giãn tự nhiên, padding card chuẩn `p-3.5 sm:p-5`.
4. Thanh bộ lọc 7 nút cuộn ngang mượt mà phong cách native app, cảm ứng >= 36px.
5. Bảng vẽ tay ngón tay Canvas responsive 100% width, không trượt trang khi vẽ.
6. Nút "Về đầu trang" 38-40px gọn gàng, tinh tế, bán trong suốt ở góc phải dưới.
7. Đồng bộ 100% sang 2 file Desktop, Git Push và Deploy Vercel Production thành công.

---

## 📅 Danh Mục Milestones Thực Thi

### Milestone 1 (M1): CSS Reset & Chống Tràn Màn Hình Ngang
- Thêm quy tắc CSS toàn cục: `html, body { overflow-x: hidden; max-width: 100vw; }`.
- Thêm `*, *::before, *::after { box-sizing: border-box; }`.
- Cấu hình thẻ code, pre, table có `overflow-x: auto; word-break: break-word; max-width: 100%`.
- Chuẩn hóa viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">`.
- Bổ sung tiện ích CSS ẩn thanh cuộn `.scrollbar-none`.

### Milestone 2 (M2): Chống Tự Động Phóng To iOS Safari (Auto-Zoom Fix)
- Thêm media query CSS: `@media screen and (max-width: 768px) { input[type="text"], input[type="search"], textarea, select { font-size: 16px !important; } }`.
- Cập nhật ô tìm kiếm `#searchInput` với class `text-[16px] sm:text-xs`.
- Cập nhật `#essay-draft-${q.id}` với class `text-[16px] sm:text-sm`.
- Cập nhật `#sub-input-${q.id}-${sIdx}` với class `text-[16px] sm:text-xs`.

### Milestone 3 (M3): Tối Ưu Thẻ Câu Hỏi & Hàng Nút Bấm Câu Con
- Căn chỉnh padding `<main>`: `px-3 sm:px-4 py-4 sm:py-8`.
- Tinh chỉnh padding thẻ câu hỏi `<article>`: `p-3.5 sm:p-5` (thay thế `p-6`).
- Hàng nút điều khiển câu con: `flex flex-wrap items-center justify-between gap-1.5`.
- Thanh công cụ đầu khối nguồn gốc: `flex flex-wrap items-center justify-between gap-2`.
- Tối ưu khoảng cách và kích thước nút trắc nghiệm đơn / nhiều đáp án.

### Milestone 4 (M4): Tối Ưu Thanh Điều Hướng & Bộ Lọc 7 Nút
- Tinh gọn thanh Sticky Header mini trên mobile: tiêu đề co giãn, tóm tắt điểm số gọn, nút toggle bảng hiển thị biểu tượng súc tích.
- Thanh bộ lọc 7 nút: cuộn ngang mượt mà trên mobile (`overflow-x-auto whitespace-nowrap scrollbar-none pb-1.5 sm:pb-0 md:flex-wrap md:whitespace-normal flex items-center gap-1.5`).
- Kích thước chạm nút lọc tối thiểu 36px (`min-h-[36px]`).

### Milestone 5 (M5): Bảng Vẽ Tay Canvas Ngón Tay Chống Trượt
- Bổ sung CSS `canvas { touch-action: none; max-width: 100%; }`.
- Tính toán kích thước canvas responsive theo `canvas.parentElement.clientWidth` không bị tràn mép.
- Ngăn chặn triệt để hiện tượng cuộn trang khi vẽ: `touch-action: none` và `preventDefault` trên pointer/touch events.

### Milestone 6 (M6): Nút Nổi Thông Minh "Về Đầu Trang"
- Định vị `fixed bottom-4 right-4 z-40`.
- Thiết kế bán trong suốt với hiệu ứng kính mờ `bg-blue-600/85 hover:bg-blue-600 active:bg-blue-700 backdrop-blur-sm shadow-lg border border-blue-400/40`.
- Kích thước gọn gàng 38px-40px, icon mũi tên thanh lịch, không che khuất nội dung.

### Milestone 7 (M7): Đồng Bộ 3 File, Git Push & Deploy Vercel Production
- Ghi đè vào `index.html`.
- Đồng bộ sang `C:\Users\Admin\Desktop\học tập\on_tap_ai_ml.html` và `C:\Users\Admin\Desktop\on_tap_ai_ml.html`.
- Xác nhận SHA256 đồng nhất 100% trên cả 3 file.
- Commit và Push lên GitHub `origin/master`.
- Deploy Vercel Production với `--prod --yes --scope tuananhs-projects-8aea56ce`.
- Chạy script kiểm thử tự động Live Production trên các viewport di động.
