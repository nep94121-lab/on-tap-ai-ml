#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_html_subquestions.py
Bộ kiểm thử đối kháng (Challenger QA) kiểm tra chi tiết cấu trúc index.html.
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(BASE_DIR, "index.html")

def verify_all():
    print("=== BẮT ĐẦU KIỂM THỬ XÁC NHẬN INDEX.HTML ===")
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Parse JS questions array
    prefix = "const questions = "
    start = content.find(prefix) + len(prefix)
    end = content.find(";\n", start)
    if end == -1:
        end = content.find(";\r\n", start)
    
    questions = json.loads(content[start:end].strip())
    print(f"✓ Nạp thành công {len(questions)} câu hỏi từ index.html")
    assert len(questions) == 68, "Số lượng câu hỏi phải đúng 68"

    # 2. Check 16 essay questions (ID 53 to 68)
    essay_ids = list(range(53, 69))
    total_sub_questions = 0
    print("\n--- Chi tiết 16 câu tự luận (53-68) ---")
    for qid in essay_ids:
        q = next((item for item in questions if item["id"] == qid), None)
        assert q is not None, f"Không tìm thấy câu {qid}"
        assert q["type"] == "tu_luan", f"Câu {qid} phải là tu_luan"
        assert "origin_sub_questions" in q, f"Câu {qid} thiếu origin_sub_questions"
        subs = q["origin_sub_questions"]
        assert isinstance(subs, list) and len(subs) > 0, f"Câu {qid} có origin_sub_questions rỗng hoặc sai kiểu"
        
        total_sub_questions += len(subs)
        print(f"  [ID {qid:02d}] {q.get('title', 'Tự luận')} -> {len(subs)} câu hỏi con")
        
        for idx, sub in enumerate(subs):
            for field in ["num", "question", "points", "answer", "source"]:
                assert field in sub, f"Câu {qid} - sub-q #{idx+1} thiếu field '{field}'"
                assert sub[field] != "", f"Câu {qid} - sub-q #{idx+1} field '{field}' bị rỗng"

    print(f"\n✓ Tổng số câu hỏi con trong 16 câu tự luận: {total_sub_questions} câu")
    assert total_sub_questions == 38, f"Tổng số câu con phải là 38, thực tế: {total_sub_questions}"

    # 3. Check question 53 specifically
    q53 = next(q for q in questions if q["id"] == 53)
    print("\n--- Chi tiết Câu 53 (Test Case Đặc Biệt) ---")
    print(f"Tiêu đề: {q53.get('title')}")
    print(f"Số câu con: {len(q53['origin_sub_questions'])}")
    for sq in q53["origin_sub_questions"]:
        print(f"  • {sq['num']} ({sq['points']}): {sq['question'][:60]}... -> Đáp án: {sq['answer'][:40]}")

    # 4. Check UI rendering code exists in index.html
    assert "q.origin_sub_questions && q.origin_sub_questions.length > 0" in content, "Thiếu điều kiện kiểm tra origin_sub_questions trong render logic"
    assert "NGUỒN GỐC TỪ ĐỀ THI GỐC" in content, "Thiếu nhãn NGUỒN GỐC TỪ ĐỀ THI GỐC"
    assert "toggleSubQuestions" in content, "Thiếu function toggleSubQuestions"
    print("\n✓ Đã kiểm tra UI rendering code và hàm toggleSubQuestions: TẤT CẢ TỒN TẠI")

    print("\n🎉 TẤT CẢ 100% KIỂM THỬ XÁC NHẬN ĐÃ PASS HOÀN HẢO!")

if __name__ == "__main__":
    verify_all()
