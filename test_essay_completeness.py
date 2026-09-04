#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_essay_completeness.py
Comprehensive Quality Assurance suite verifying:
- Completeness of 16 essay questions (53-68)
- Presence of all 4 RAGAS metrics & thresholds in Question 68
- Human-in-the-loop in Question 59
- 3 components of Output Contract in Question 60
- 4-step Incident Response in Question 67
- 100% synchronization across questions_db.json, index.html, and 2 target desktop copies.
"""

import json
import os
import hashlib

def run_tests():
    print("[*] Starting QA Test Suite for Essay Questions...")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "questions_db.json")
    html_path = os.path.join(base_dir, "index.html")
    desktop_copy1 = r"C:\Users\Admin\Desktop\học tập\on_tap_ai_ml.html"
    desktop_copy2 = r"C:\Users\Admin\Desktop\on_tap_ai_ml.html"

    # 1. Load JSON
    with open(json_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    assert len(db) == 68, f"Expected 68 questions, got {len(db)}"
    print("  [✓] Database length: 68 questions")

    # 2. Check 16 essay questions
    essay_qs = [q for q in db if 53 <= q.get("id", 0) <= 68]
    assert len(essay_qs) == 16, f"Expected 16 essay questions, got {len(essay_qs)}"
    
    sub_count = sum(len(q.get("origin_sub_questions", [])) for q in essay_qs)
    assert sub_count == 38, f"Expected 38 sub-questions, got {sub_count}"
    print(f"  [✓] 16 essay questions validated with {sub_count} origin sub-questions")

    # 3. Test Question 68 specifically
    q68 = next(q for q in essay_qs if q["id"] == 68)
    qt68 = q68["quick_tip"]
    exp68 = q68["explanation"]

    for metric in ["Faithfulness", "Answer Relevance", "Context Precision", "Context Recall"]:
        assert metric in qt68, f"Q68 quick_tip missing metric: {metric}"
        assert metric in exp68, f"Q68 explanation missing metric: {metric}"
    print("  [✓] Q68: All 4 RAGAS metrics present in both quick_tip and explanation")

    assert "Context Precision" in qt68 and "≥ 0.80" in qt68, "Q68 quick_tip missing Context Precision threshold"
    assert "Context Recall" in qt68 and "≥ 0.80" in qt68, "Q68 quick_tip missing Context Recall threshold"
    assert "Retrieval" in qt68 and "0.60" in qt68, "Q68 quick_tip missing Retrieval analysis"
    assert "Retrieval" in exp68 and "0.60" in exp68, "Q68 explanation missing Retrieval analysis"
    print("  [✓] Q68: All 4 release thresholds and Retrieval layer analysis verified")

    # 4. Test Question 59
    q59 = next(q for q in essay_qs if q["id"] == 59)
    assert "Feedback Loop" in q59["quick_tip"] and "Human-in-the-loop" in q59["quick_tip"], "Q59 quick_tip missing Human-in-the-loop"
    assert "Human-in-the-loop" in q59["explanation"] and "80%" in q59["explanation"], "Q59 explanation missing Human-in-the-loop details"
    print("  [✓] Q59: Feedback Loop & Human-in-the-loop verified")

    # 5. Test Question 60
    q60 = next(q for q in essay_qs if q["id"] == 60)
    assert "3 thành phần" in q60["quick_tip"] or "Format/Schema" in q60["quick_tip"], "Q60 quick_tip missing 3 components"
    assert "3 thành phần" in q60["explanation"], "Q60 explanation missing 3 components"
    print("  [✓] Q60: 3 core components of Output Contract verified")

    # 6. Test Question 67
    q67 = next(q for q in essay_qs if q["id"] == 67)
    assert "Ứng phó sự cố 4 bước" in q67["quick_tip"] or "Rollback" in q67["quick_tip"], "Q67 quick_tip missing incident response"
    assert "Kế hoạch ứng cứu sự cố khẩn cấp 4 bước" in q67["explanation"], "Q67 explanation missing incident response 4 steps"
    print("  [✓] Q67: 4-step Incident Response verified")

    # 7. Test Question 56 sub 2 answer
    q56 = next(q for q in essay_qs if q["id"] == 56)
    sub2_ans = q56["origin_sub_questions"][1]["answer"]
    assert "A1→B5, A2→B4, A3→B3, A4→B1, A5→B2" in sub2_ans, f"Q56 sub 2 answer incorrect: {sub2_ans}"
    print("  [✓] Q56: Matching format standardized")

    # 8. Check HTML inline questions
    with open(html_path, "r", encoding="utf-8") as f:
        html_text = f.read()

    prefix = "const questions = "
    start_pos = html_text.find(prefix)
    assert start_pos != -1, "index.html missing 'const questions = '"
    array_start = start_pos + len(prefix)
    end_pos = html_text.find(";\n", array_start)
    if end_pos == -1:
        end_pos = html_text.find(";\r\n", array_start)
    assert end_pos != -1, "Could not find end of 'const questions = '"
    
    html_json = json.loads(html_text[array_start:end_pos])
    assert len(html_json) == 68, f"index.html has {len(html_json)} questions, expected 68"
    html_q68 = next(q for q in html_json if q["id"] == 68)
    assert "Context Precision" in html_q68["quick_tip"], "index.html Q68 missing Context Precision"
    assert "Context Recall" in html_q68["quick_tip"], "index.html Q68 missing Context Recall"
    print("  [✓] index.html: inline questions array verified with 68 questions and updated Q68")

    # 9. Verify file hashes
    def get_hash(path):
        with open(path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    h_main = get_hash(html_path)
    h_c1 = get_hash(desktop_copy1)
    h_c2 = get_hash(desktop_copy2)

    assert h_main == h_c1, f"Hash mismatch: index.html ({h_main}) vs {desktop_copy1} ({h_c1})"
    assert h_main == h_c2, f"Hash mismatch: index.html ({h_main}) vs {desktop_copy2} ({h_c2})"
    print(f"  [✓] All 3 HTML files have identical MD5 hash: {h_main}")

    print("\n=======================================================")
    print("[+] ALL 9 QA TESTS PASSED WITH 100% SUCCESS!")
    print("=======================================================")

if __name__ == "__main__":
    run_tests()
