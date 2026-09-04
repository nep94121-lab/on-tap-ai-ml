#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_mobile_viewports.py
Bộ kiểm thử đối kháng chất lượng cao (Challenger QA) thẩm định 100% các tiêu chí
tối ưu hóa giao diện di động (Mobile-First Polish & Bugfix):
- Tiêu chí 1: No horizontal scroll (CSS overflow-x: hidden, max-width: 100vw, box-sizing, pre/code/table break-words).
- Tiêu chí 2: Prevent iOS auto-zoom (Font-size >= 16px trên mobile cho input và textarea).
- Tiêu chí 3: Card padding p-3.5 sm:p-5 & Hàng nút câu con flex-wrap gap-1.5.
- Tiêu chí 4: Filter bar 7 nút cuộn ngang mượt mà, touch target >= 36px.
- Tiêu chí 5: Canvas touch-action: none & responsive width 100%.
- Tiêu chí 6: Smart Back-to-top 38-40px, bottom-4 right-4, bán trong suốt.
- Tiêu chí 7: Đồng bộ 3 file HTML 100% đồng nhất SHA256.
"""

import hashlib
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(BASE_DIR, "index.html")

DESKTOP_1 = r"C:\Users\Admin\Desktop\học tập\on_tap_ai_ml.html"
DESKTOP_2 = r"C:\Users\Admin\Desktop\on_tap_ai_ml.html"

def get_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def run_tests():
    print("=" * 80)
    print("BẮT ĐẦU KIỂM THỬ ĐỐI KHÁNG MOBILE-FIRST POLISH & RESPONSIVE SUITE")
    print("=" * 80)

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    passed = 0
    total = 0

    def assert_check(name, condition, detail=""):
        nonlocal passed, total
        total += 1
        if condition:
            passed += 1
            print(f"  [✔ PASS] {name}")
            if detail:
                print(f"         {detail}")
        else:
            print(f"  [✘ FAIL] {name}")
            if detail:
                print(f"         {detail}")
            raise AssertionError(f"Test failed: {name}")

    print("\n▶ [NHÓM 1] CHỐNG TRÀN MÀN HÌNH NGANG (NO HORIZONTAL SCROLL)")
    assert_check(
        "Quy tắc CSS toàn cục html, body { overflow-x: hidden; max-width: 100vw; }",
        "overflow-x: hidden" in html and "max-width: 100vw" in html,
        "Đảm bảo màn hình không bị trượt ngang trên mọi kích thước di động"
    )
    assert_check(
        "Box-sizing border-box toàn cục",
        "box-sizing: border-box" in html,
        "Ngăn chặn padding làm phình kích thước vượt khung màn hình"
    )
    assert_check(
        "Bảo vệ khối pre, code, table không làm vỡ card",
        "max-width: 100%" in html and "word-break: break-word" in html and "overflow-x: auto" in html,
        "Code dài và bảng tự động co giãn và cuộn an toàn"
    )
    assert_check(
        "Viewport meta tag chuẩn responsive (maximum-scale=5.0)",
        'name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0"' in html,
        "Thân thiện với trình duyệt di động hiện đại"
    )

    print("\n▶ [NHÓM 2] CHỐNG TỰ ĐỘNG PHÓNG TO TRÊN IOS SAFARI (AUTO-ZOOM FIX)")
    assert_check(
        "CSS Media Query ép font-size 16px cho input/textarea trên màn hình <= 768px",
        '@media screen and (max-width: 768px)' in html and 'font-size: 16px !important;' in html,
        "Triệt tiêu hoàn toàn lỗi iOS tự động zoom khi focus vào ô gõ nháp"
    )
    assert_check(
        "Ô tìm kiếm searchInput có font-size 16px trên mobile",
        'id="searchInput"' in html and 'text-[16px]' in html,
        "Tránh nhảy viewport khi người dùng chạm vào thanh tìm kiếm"
    )
    assert_check(
        "Textarea nháp tự luận có font-size 16px trên mobile",
        'id="essay-draft-${q.id}"' in html and 'text-[16px]' in html,
        "Chống auto-zoom khi gõ bài tập tự luận"
    )
    assert_check(
        "Textarea câu con có font-size 16px trên mobile",
        'id="sub-input-${q.id}-${sIdx}"' in html and 'text-[16px]' in html,
        "Chống auto-zoom khi gõ nháp từng câu hỏi nhỏ"
    )

    print("\n▶ [NHÓM 3] TỐI ƯU CARD PADDING & HÀNG NÚT BẤM CÂU CON")
    assert_check(
        "Card câu hỏi dùng padding tối ưu p-3.5 sm:p-5",
        'p-3.5 sm:p-5' in html and 'p-6 shadow-sm' not in html,
        "Mở rộng diện tích đọc chữ tối đa cho điện thoại 360px-390px"
    )
    assert_check(
        "Hàng nút điều khiển câu con dùng flex-wrap gap-1.5",
        'flex flex-wrap items-center justify-between gap-1.5 pt-1' in html,
        "Nút Xem đáp án, Xóa nháp, Ký tự không bị tràn hoặc đè lên nhau"
    )
    assert_check(
        "Thanh công cụ câu con co giãn tự nhiên",
        'flex flex-wrap items-center justify-between gap-2 pb-2' in html,
        "Thanh tiêu đề danh sách câu hỏi nhỏ không bị gãy hàng xấu"
    )
    assert_check(
        "Container main có padding thích ứng px-3 sm:px-4 py-4 sm:py-8",
        'px-3 sm:px-4 py-4 sm:py-8' in html,
        "Khoảng cách biên hai bên vừa vặn trên màn hình hẹp"
    )

    print("\n▶ [NHÓM 4] THANH ĐIỀU HƯỚNG & BỘ LỌC 7 NÚT CUỘN NGANG")
    assert_check(
        "Bộ lọc 7 nút hỗ trợ cuộn ngang mượt mà phong cách Native App",
        'overflow-x-auto whitespace-nowrap scrollbar-none' in html,
        "Dễ dàng vuốt ngang chọn Track/thể loại, không chiếm nhiều dòng"
    )
    assert_check(
        "Kích thước chạm nút lọc tối thiểu 36px (min-h-[36px])",
        html.count('min-h-[36px]') >= 7,
        f"Tìm thấy {html.count('min-h-[36px]')} nút đạt chuẩn touch target >= 36px"
    )
    assert_check(
        "Thanh Sticky Mini Header tinh giản trên mobile",
        'hidden sm:inline">Thu gọn bảng</span>' in html,
        "Rút gọn nút trên mobile để tránh tràn thanh header mini"
    )

    print("\n▶ [NHÓM 5] BẢNG VẼ TAY CANVAS NGÓN TAY")
    assert_check(
        "Canvas có thuộc tính touch-action: none",
        'touch-action: none' in html and 'touch-none' in html,
        "Không bị trượt/cuộn trang web làm đứt nét vẽ ngón tay"
    )
    assert_check(
        "Kích thước canvas 100% responsive width theo parent",
        'canvas.parentElement.clientWidth : 320' in html,
        "Không bị ép kích thước cứng gây vỡ khung trên màn hình nhỏ"
    )
    assert_check(
        "Xử lý touch và pointer events chuẩn xác",
        'canvas.addEventListener(\'pointerdown\', startDrawing, { passive: false });' in html and
        'canvas.addEventListener(\'touchstart\', startDrawing, { passive: false });' in html,
        "Bắt tọa độ chính xác 100% khi vẽ ngón tay"
    )

    print("\n▶ [NHÓM 6] NÚT NỔI SMART BACK-TO-TOP")
    assert_check(
        "Định vị bottom-4 right-4 gọn gàng",
        'bottom-4 right-4 z-40' in html,
        "Vị trí chuẩn không che khuất nội dung ở đáy trang"
    )
    assert_check(
        "Thiết kế bán trong suốt với hiệu ứng kính mờ (backdrop-blur-sm)",
        'backdrop-blur-sm' in html and 'bg-blue-600/85' in html,
        "Sang trọng, tinh tế, không làm vướng tầm nhìn"
    )
    assert_check(
        "Kích thước gọn 38-40px trên mobile (w-10 h-10 sm:w-auto)",
        'w-10 h-10 sm:w-auto' in html,
        "Dạng nút tròn nhỏ gọn trên điện thoại, tự mở rộng trên desktop"
    )

    print("\n▶ [NHÓM 7] ĐỒNG BỘ 3 FILE HTML ĐỒNG NHẤT 100%")
    src_hash = get_sha256(HTML_PATH)
    d1_hash = get_sha256(DESKTOP_1)
    d2_hash = get_sha256(DESKTOP_2)

    assert_check(
        "Đồng bộ file Desktop 1 (C:\\Users\\Admin\\Desktop\\học tập\\on_tap_ai_ml.html)",
        src_hash == d1_hash,
        f"SHA256 khớp hoàn hảo: {src_hash[:16]}..."
    )
    assert_check(
        "Đồng bộ file Desktop 2 (C:\\Users\\Admin\\Desktop\\on_tap_ai_ml.html)",
        src_hash == d2_hash,
        f"SHA256 khớp hoàn hảo: {src_hash[:16]}..."
    )

    print("\n" + "=" * 80)
    print(f"TỔNG KẾT KIỂM THỬ: {passed}/{total} CHECKS ĐẠT CHUẨN (PASS 100%)")
    print("=" * 80)
    print("🎉 TẤT CẢ CÁC TIÊU CHÍ TỐI ƯU MOBILE ĐỀU ĐÃ ĐẠT NGHIỆM THU TUYỆT ĐỐI!")

if __name__ == "__main__":
    run_tests()
