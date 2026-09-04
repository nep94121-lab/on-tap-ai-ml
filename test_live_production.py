#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_live_production.py
Kiểm thử trực tiếp trên môi trường Live Production Vercel: https://on-tap-ai-ml.vercel.app
"""

import json
import urllib.request
import ssl
import sys

URL = "https://on-tap-ai-ml.vercel.app"

def test_live():
    print(f"=== BẮT ĐẦU KIỂM THỬ LIVE PRODUCTION: {URL} ===")
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        URL,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) TestSuite/1.0"}
    )
    
    with urllib.request.urlopen(req, context=ctx, timeout=15) as response:
        status_code = response.getcode()
        print(f"✓ HTTP Status: {status_code}")
        assert status_code == 200, f"HTTP status code is {status_code}, expected 200"
        
        html_data = response.read().decode("utf-8")
        print(f"✓ Tải thành công payload HTML ({len(html_data)} bytes)")

    # 1. Assert keyword presence in HTML
    print("\n--- Kiểm tra chuỗi định danh trên Live HTML ---")
    keywords = [
        "origin_sub_questions",
        "NGUỒN GỐC TỪ ĐỀ THI GỐC",
        "toggleSubQuestions",
        "Gộp từ",
        "Dành cho Sếp học thuộc chia theo điểm"
    ]
    for kw in keywords:
        assert kw in html_data, f"❌ Thiếu chuỗi '{kw}' trên live payload!"
        print(f"✓ Tìm thấy chuỗi: '{kw}'")

    # 2. Extract and parse inline questions JSON from live payload
    prefix = "const questions = "
    start_pos = html_data.find(prefix)
    assert start_pos != -1, "Không tìm thấy 'const questions = ' trên live HTML"
    
    start_array = start_pos + len(prefix)
    end_pos = html_data.find(";\n", start_array)
    if end_pos == -1:
        end_pos = html_data.find(";\r\n", start_array)
    assert end_pos != -1, "Không tìm thấy kết thúc mảng JS trên live HTML"

    raw_json = html_data[start_array:end_pos].strip()
    questions = json.loads(raw_json)
    print(f"\n✓ Đã trích xuất và phân tích cú pháp JSON thành công: {len(questions)} câu hỏi")
    assert len(questions) == 68, f"Expected 68 questions, got {len(questions)}"

    # 3. Assert origin_sub_questions on live payload
    questions_with_sub = [q for q in questions if "origin_sub_questions" in q and q["origin_sub_questions"]]
    total_sub_q = sum(len(q["origin_sub_questions"]) for q in questions_with_sub)
    print(f"✓ Số câu có origin_sub_questions trên Live: {len(questions_with_sub)} (Kỳ vọng: 16)")
    print(f"✓ Tổng số câu con trên Live: {total_sub_q} (Kỳ vọng: 38)")
    assert len(questions_with_sub) == 16, f"Expected 16, got {len(questions_with_sub)}"
    assert total_sub_q == 38, f"Expected 38, got {total_sub_q}"

    # 4. Assert Question 53 on live payload
    q53 = next((q for q in questions if q["id"] == 53), None)
    assert q53 is not None, "Câu 53 không tồn tại trên Live!"
    assert len(q53["origin_sub_questions"]) == 3, f"Câu 53 phải có 3 câu con, có {len(q53['origin_sub_questions'])}"
    print(f"✓ Câu 53 trên Live đã có {len(q53['origin_sub_questions'])} câu con:")
    for sq in q53["origin_sub_questions"]:
        print(f"   • {sq['num']}: {sq['question'][:50]}... -> Đáp án: {sq['answer']}")

    print("\n🎉 LIVE PRODUCTION ASSERTION: PASS 100% HOÀN HẢO!")

if __name__ == "__main__":
    test_live()
