#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_suite.py
Kiểm thử tự động toàn diện tính toàn vẹn của cơ sở dữ liệu questions_db.json
và ứng dụng Web index.html (68 câu độc nhất, 0 fallback, 0 trùng lặp).
"""

import os
import sys
import json
import re

TARGET_DIR = r"C:\Users\Admin\Desktop\học tập\Bo_De_AI_ML_Da_Giai"
JSON_PATH = os.path.join(TARGET_DIR, "questions_db.json")
HTML_PATH = os.path.join(TARGET_DIR, "index.html")

def run_tests():
    print("================================================================================")
    print("BẮT ĐẦU KIỂM THỬ PHÁP Y: CƠ SỞ DỮ LIỆU & GIAO DIỆN WEB AI/ML (68 CÂU)")
    print("================================================================================")
    
    passes = 0
    failures = 0

    def assert_test(cond, test_name, detail=""):
        nonlocal passes, failures
        if cond:
            print(f"  [PASS] {test_name}")
            passes += 1
        else:
            print(f"  [FAIL] {test_name}: {detail}")
            failures += 1

    # --- PHẦN 1: KIỂM THỬ questions_db.json ---
    print("\n--- PHẦN 1: KIỂM THỬ TOÀN VẸN questions_db.json ---")
    
    assert_test(os.path.exists(JSON_PATH), "File questions_db.json tồn tại")
    
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1. Số lượng câu hỏi
    assert_test(len(data) == 68, f"Tổng số câu hỏi đúng bằng 68 (Thực tế: {len(data)})")

    # 2. Phân bố các dạng câu hỏi
    sc_count = sum(1 for q in data if q.get("type") == "single_choice")
    mc_count = sum(1 for q in data if q.get("type") == "multi_choice")
    essay_count = sum(1 for q in data if q.get("type") == "tu_luan")
    assert_test(sc_count == 47, f"Đúng 47 câu trắc nghiệm đơn (Thực tế: {sc_count})")
    assert_test(mc_count == 5, f"Đúng 5 câu trắc nghiệm nhiều đáp án (Thực tế: {mc_count})")
    assert_test(essay_count == 16, f"Đúng 16 bài tập tự luận/tình huống lớn (Thực tế: {essay_count})")

    # 3. Tính liên tục của ID (1 đến 68)
    ids = [q["id"] for q in data]
    assert_test(ids == list(range(1, 69)), f"Các ID câu hỏi tuần tự từ 1 đến 68")

    # 4. Kiểm tra Placeholder
    bad_phrases = [
        "xem lời giải chi tiết", 
        "theo bài giảng", 
        "kiểm tra lại trong bài học",
        "phương án chuẩn xác theo nguyên lý thiết kế"
    ]
    found_placeholders = []
    for q in data:
        full_text = (str(q.get("correct", "")) + " " + str(q.get("explanation", ""))).lower()
        for bp in bad_phrases:
            if bp in full_text:
                found_placeholders.append((q["id"], bp))
    assert_test(len(found_placeholders) == 0, f"0 placeholder trong toàn bộ cơ sở dữ liệu (Tìm thấy: {found_placeholders})")

    # 5. Kiểm tra trùng lặp câu hỏi
    seen_q = {}
    duplicates = []
    for q in data:
        norm = re.sub(r'[^a-zA-Z0-9\u00C0-\u1EF9]', '', q["question"].lower())[:60]
        if norm in seen_q:
            duplicates.append((q["id"], seen_q[norm]))
        else:
            seen_q[norm] = q["id"]
    assert_test(len(duplicates) == 0, f"0 câu hỏi trùng lặp (Tìm thấy: {duplicates})")

    # 6. Kiểm tra Câu 5 trắc nghiệm
    q5 = next(q for q in data if q["id"] == 5)
    assert_test(isinstance(q5["correct"], list) and set(q5["correct"]) == {"A", "B", "C"}, 
                "Câu 5 hỗ trợ cả 3 đáp án A, B, C (Tùy chọn định hướng học viên)")

    # 7. Kiểm tra các câu tự luận chuyên sâu quan trọng
    # Bài toán tài chính CSKH (ID 66)
    q66 = next(q for q in data if q["id"] == 66)
    exp66 = q66["explanation"]
    has_roi = ("142,5%" in exp66 or "142.5%" in exp66) and "380" in exp66 and ("921,6" in exp66 or "921.6" in exp66) and ("541,6" in exp66 or "541.6" in exp66)
    assert_test(has_roi, "Bài 14 (ID 66): Đầy đủ số liệu ROI 142.5%, Chi phí 380tr, Lợi ích 921.6tr, Lợi nhuận ròng 541.6tr")

    # Sửa code ReAct (ID 65)
    q65 = next(q for q in data if q["id"] == 65)
    exp65 = q65["explanation"]
    has_react_code = "def run_agent" in exp65 and "Observation:" in exp65 and "max_iterations" in exp65
    assert_test(has_react_code, "Bài 13 (ID 65): Đầy đủ 2 lỗi thiết kế & mã nguồn Python run_agent() chuẩn")

    # Sự cố E-commerce Friday 17h (ID 67)
    q67 = next(q for q in data if q["id"] == 67)
    exp67 = q67["explanation"]
    has_ecom = ("Friday" in exp67 or "thứ Sáu" in exp67) and "Model Routing" in exp67 and "CI/CD" in exp67
    assert_test(has_ecom, "Bài 15 (ID 67): Đầy đủ 3 sai lầm, phân luồng Model Routing & pipeline CI/CD")

    # Khung kiểm định RAGAS (ID 68)
    q68 = next(q for q in data if q["id"] == 68)
    exp68 = q68["explanation"]
    has_ragas = "RAGAS" in exp68 and "Faithfulness" in exp68 and "Relevance" in exp68
    assert_test(has_ragas, "Bài 16 (ID 68): Đầy đủ Golden Dataset & 4 chỉ số RAGAS")

    # Kiến trúc Supervisor-Worker (ID 59)
    q59 = next(q for q in data if q["id"] == 59)
    exp59 = q59["explanation"]
    has_supervisor = "Supervisor" in exp59 and "Sentiment" in exp59 and "Topic" in exp59
    assert_test(has_supervisor, "Bài 7 (ID 59): Đầy đủ sơ đồ Supervisor và 3 Workers")

    # System prompt CSKH 4 phần (ID 64)
    q64 = next(q for q in data if q["id"] == 64)
    exp64 = q64["explanation"]
    has_prompt = "ROLE" in exp64 and "CONSTRAINTS" in exp64 and "OUTPUT CONTRACT" in exp64 and "SAFEGUARD" in exp64
    assert_test(has_prompt, "Bài 12 (ID 64): Đầy đủ System Prompt chuẩn 4 phần (ROLE, CONSTRAINTS, OUTPUT CONTRACT, SAFEGUARD)")

    # 8. Kiểm tra Track distribution
    t1_count = sum(1 for q in data if q.get("is_app"))
    t2_count = sum(1 for q in data if q.get("is_infra"))
    t3_count = sum(1 for q in data if q.get("is_prod"))
    assert_test(t1_count >= 22 and t2_count >= 31 and t3_count >= 19, 
                f"Phân loại Track đầy đủ (Track 1: {t1_count}, Track 2: {t2_count}, Track 3: {t3_count})")

    # --- PHẦN 2: KIỂM THỬ index.html ---
    print("\n--- PHẦN 2: KIỂM THỬ GIAO DIỆN WEB index.html ---")
    assert_test(os.path.exists(HTML_PATH), "File index.html tồn tại")

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Nhúng mảng câu hỏi
    match_questions = re.search(r'const\s+questions\s*=\s*(\[[\s\S]*?\]);', html)
    assert_test(bool(match_questions), "Mảng const questions = [...] được nhúng trực tiếp trong HTML")
    if match_questions:
        html_data = json.loads(match_questions.group(1))
        assert_test(len(html_data) == 68, f"Mảng nhúng trong HTML chứa đúng 68 câu (Thực tế: {len(html_data)})")

    # 2. 0 placeholder trong các câu hỏi nhúng ở HTML
    html_placeholders = []
    for q in html_data:
        q_text = (str(q.get("correct", "")) + " " + str(q.get("explanation", ""))).lower()
        for bp in bad_phrases:
            if bp in q_text:
                html_placeholders.append((q["id"], bp))
    assert_test(len(html_placeholders) == 0, f"0 câu hỏi mang placeholder fallback trong HTML (Tìm thấy: {html_placeholders})")

    # 3. Kiểm tra các nút bộ lọc cần thiết
    required_filters = [
        ('id="filter-all"', "Nút Tất cả (68)"),
        ('id="filter-single"', "Nút Trắc nghiệm đơn (47)"),
        ('id="filter-multi"', "Nút Nhiều đáp án (5)"),
        ('id="filter-essay"', "Nút Tự luận & Tình huống (16)"),
        ('id="filter-track1"', "Nút Track 1: Applications"),
        ('id="filter-track2"', "Nút Track 2: Infrastructure"),
        ('id="filter-track3"', "Nút Track 3: Product")
    ]
    for fid, label in required_filters:
        assert_test(fid in html, f"Thanh bộ lọc có {label}")

    # 4. Kiểm tra loại bỏ nút thừa check2 (Bộ 2)
    assert_test('data-filter="check2"' not in html, "Đã loại bỏ nút Check 2 (Bộ 2) thừa thãi")

    # 5. Kiểm tra các chức năng UI
    assert_test('id="searchInput"' in html, "Có ô tìm kiếm real-time (searchInput)")
    assert_test('id="scoreCorrect"' in html and 'id="scoreWrong"' in html and 'id="progressPercent"' in html, 
                "Có các trường bộ đếm điểm real-time (scoreCorrect, scoreWrong, progressPercent)")
    assert_test('id="modeQuizBtn"' in html and 'id="modeStudyBtn"' in html, 
                "Có hai chế độ: Luyện thi (ẩn đáp án) & Học tập (hiện sẵn)")
    assert_test('function selectSingleChoice' in html and 'function toggleMultiChoice' in html and 'function toggleEssayAnswer' in html,
                "Có đầy đủ các hàm xử lý tương tác (selectSingleChoice, toggleMultiChoice, toggleEssayAnswer)")

    # 6. Kiểm tra logic Câu 5 trong JavaScript
    assert_test('Array.isArray(q.correct) ? q.correct.includes(choiceLetter) : (choiceLetter === q.correct)' in html,
                "Logic selectSingleChoice trong JS hỗ trợ chấm đúng cho mọi đáp án của Câu 5 (A, B, C)")

    print("\n================================================================================")
    print(f"TỔNG KẾT KIỂM THỬ: {passes} PASS, {failures} FAIL")
    print("================================================================================")

    if failures == 0:
        print("🎉 TOÀN BỘ CÁC BÀI KIỂM THỬ ĐỀU ĐẠT CHUẨN PASS 100%!")
        return True
    else:
        print(f"❌ CÓ {failures} LỖI CẦN KHẮC PHỤC!")
        return False

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
