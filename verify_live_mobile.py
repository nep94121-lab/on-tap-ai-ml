#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_live_mobile.py
Kiểm thử tự động Live Production trên Vercel:
URL: https://on-tap-ai-ml.vercel.app
"""

import hashlib
import os
import urllib.request

LIVE_URL = "https://on-tap-ai-ml.vercel.app"
LOCAL_PATH = r"C:\Users\Admin\Desktop\học tập\Bo_De_AI_ML_Da_Giai\index.html"

def test_live():
    print("=" * 80)
    print(f"BẮT ĐẦU KIỂM THỬ LIVE PRODUCTION TRÊN VERCEL: {LIVE_URL}")
    print("=" * 80)

    req = urllib.request.Request(
        LIVE_URL,
        headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148"}
    )
    with urllib.request.urlopen(req) as resp:
        assert resp.status == 200, f"HTTP status {resp.status}"
        live_content = resp.read().decode("utf-8")

    print(f"[+] Nạp thành công HTML từ Live Vercel ({len(live_content)} bytes)")

    # 1. Check Anti-Horizontal Scroll
    assert "overflow-x: hidden" in live_content, "Thiếu overflow-x: hidden trên Live"
    assert "max-width: 100vw" in live_content, "Thiếu max-width: 100vw trên Live"
    print("  [✔ PASS] Live CSS Anti-Horizontal Scroll: overflow-x: hidden, max-width: 100vw")

    # 2. Check Anti-iOS Auto-zoom
    assert "@media screen and (max-width: 768px)" in live_content, "Thiếu media query font-size 16px trên Live"
    assert "font-size: 16px !important;" in live_content, "Thiếu font-size: 16px !important trên Live"
    assert 'id="searchInput"' in live_content and 'text-[16px]' in live_content, "Thiếu text-[16px] trên searchInput Live"
    assert 'text-[16px] sm:text-sm' in live_content, "Thiếu text-[16px] trên essay-draft Live"
    assert 'text-[16px] sm:text-xs' in live_content, "Thiếu text-[16px] trên sub-input Live"
    print("  [✔ PASS] Live iOS Auto-Zoom Prevention: font-size 16px trên mobile")

    # 3. Check Card Padding & Sub-question Buttons
    assert "p-3.5 sm:p-5" in live_content, "Thiếu card padding p-3.5 sm:p-5 trên Live"
    assert "p-6 shadow-sm" not in live_content, "Vẫn còn padding p-6 cũ trên Live"
    assert "flex flex-wrap items-center justify-between gap-1.5 pt-1" in live_content, "Thiếu flex-wrap gap-1.5 cho nút câu con trên Live"
    print("  [✔ PASS] Live Card Padding & Controls: p-3.5 sm:p-5, flex-wrap gap-1.5")

    # 4. Check Filter Bar Scroll
    assert "overflow-x-auto whitespace-nowrap scrollbar-none" in live_content, "Thiếu cuộn ngang 7 nút filter trên Live"
    assert live_content.count("min-h-[36px]") >= 7, "Nút lọc thiếu min-h-[36px] trên Live"
    print("  [✔ PASS] Live Filter Bar: cuộn ngang mượt mà, touch target >= 36px")

    # 5. Check Touch Canvas
    assert "touch-action: none" in live_content, "Thiếu touch-action: none cho canvas trên Live"
    assert "canvas.parentElement.clientWidth : 320" in live_content, "Thiếu responsive canvas calculation trên Live"
    print("  [✔ PASS] Live Touch Canvas: touch-action: none, 100% responsive")

    # 6. Check Smart Back-to-Top
    assert "bottom-4 right-4 z-40" in live_content, "Thiếu bottom-4 right-4 trên Live"
    assert "w-10 h-10 sm:w-auto" in live_content, "Thiếu w-10 h-10 trên Live"
    assert "backdrop-blur-sm" in live_content, "Thiếu backdrop-blur-sm trên Live"
    print("  [✔ PASS] Live Smart Back-to-Top: bottom-4 right-4, bán trong suốt")

    # 7. Check SHA256 match with local index.html
    local_hash = hashlib.sha256(open(LOCAL_PATH, "rb").read()).hexdigest()
    live_hash = hashlib.sha256(live_content.encode("utf-8")).hexdigest()
    print(f"\n[+] Local SHA256: {local_hash}")
    print(f"[+] Live  SHA256: {live_hash}")
    assert local_hash == live_hash, f"SHA256 Live không khớp Local! Local: {local_hash}, Live: {live_hash}"
    print("  [✔ PASS] SHA256 giữa Live Vercel và Local hoàn toàn trùng khớp 100%!")

    print("\n" + "=" * 80)
    print("🎉 TẤT CẢ 100% KIỂM THỬ LIVE PRODUCTION TRÊN VERCEL ĐÃ PASS TUYỆT ĐỐI!")
    print("=" * 80)

if __name__ == "__main__":
    test_live()
