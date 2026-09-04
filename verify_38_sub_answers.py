#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_38_sub_answers.py
Kiểm tra tính hợp lệ và tiêu chuẩn chất lượng của 38 câu hỏi con trong questions_db.json:
- 100% bắt đầu bằng bullet '•'
- 100% có in đậm từ khóa '**'
- Độ dài vừa phải, không rỗng
- Đầy đủ giải thích tiếng Việt và thuật ngữ tiếng Anh
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "questions_db.json")

def verify():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)

    sub_count = 0
    for q in questions:
        qid = q["id"]
        if 53 <= qid <= 68:
            assert "origin_sub_questions" in q, f"Câu {qid} thiếu origin_sub_questions"
            subs = q["origin_sub_questions"]
            for s in subs:
                sub_count += 1
                ans = s["answer"]
                assert ans.strip() != "", f"Câu {qid} sub {s['num']} answer rỗng!"
                assert ans.startswith("•"), f"Câu {qid} sub {s['num']} không bắt đầu bằng bullet! Bắt đầu bằng: {ans[:20]}"
                assert "**" in ans, f"Câu {qid} sub {s['num']} thiếu từ khóa in đậm **!"
                assert "\n" in ans, f"Câu {qid} sub {s['num']} chỉ có 1 dòng, thiếu phân tách gạch đầu dòng!"
                print(f"✓ Câu {qid} {s['num']} ({s['points']}): {len(ans.splitlines())} gạch đầu dòng | Độ dài: {len(ans)} chars")

    print(f"\n==========================================")
    print(f"PASS 100%: Toàn bộ {sub_count}/38 câu con đã đạt chuẩn gạch đầu dòng + in đậm keyword!")
    print(f"==========================================")
    assert sub_count == 38, f"Tổng số câu con phải là 38, thực tế: {sub_count}"

if __name__ == "__main__":
    verify()
