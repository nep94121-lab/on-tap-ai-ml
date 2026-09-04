#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_questions_to_html.py
Đồng bộ mảng inline `const questions = [...]` trong index.html từ questions_db.json.
Đảm bảo giữ nguyên 100% logic rendering HTML/JS (bao gồm audioMap, toggleSubQuestions, speed_70 mode).
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "questions_db.json")
HTML_PATH = os.path.join(BASE_DIR, "index.html")

def sync_data():
    print(f"[*] Reading questions database: {JSON_PATH}")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)

    print(f"    - Total questions in DB: {len(db)}")
    sub_count = 0
    questions_with_sub = 0
    for q in db:
        subs = q.get("origin_sub_questions", [])
        if subs:
            questions_with_sub += 1
            sub_count += len(subs)

    print(f"    - Questions with origin_sub_questions: {questions_with_sub}")
    print(f"    - Total sub-questions: {sub_count}")

    assert len(db) == 68, f"Expected 68 questions, got {len(db)}"
    assert questions_with_sub == 16, f"Expected 16 questions with sub-questions, got {questions_with_sub}"
    assert sub_count == 38, f"Expected 38 sub-questions, got {sub_count}"

    print(f"[*] Reading HTML file: {HTML_PATH}")
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html_content = f.read()

    prefix = "const questions = "
    start_pos = html_content.find(prefix)
    if start_pos == -1:
        raise ValueError("Could not find 'const questions = ' in index.html")

    # Find the end of this JS statement (semicolon followed by newline or next var)
    array_start = start_pos + len(prefix)
    if html_content[array_start] != '[':
        raise ValueError(f"Expected '[' after 'const questions = ', found '{html_content[array_start]}'")

    # Find the semicolon ending the statement
    end_pos = html_content.find(";\n", array_start)
    if end_pos == -1:
        end_pos = html_content.find(";\r\n", array_start)
    if end_pos == -1:
        raise ValueError("Could not find ending semicolon for 'const questions = ' statement")

    json_str = json.dumps(db, ensure_ascii=False)
    new_html = html_content[:start_pos + len(prefix)] + json_str + html_content[end_pos:]

    print(f"[*] Writing updated content to: {HTML_PATH}")
    with open(HTML_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_html)

    print("[*] Performing verification assertions on updated index.html...")
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        updated_content = f.read()

    verify_start = updated_content.find(prefix)
    verify_array_start = verify_start + len(prefix)
    verify_end = updated_content.find(";\n", verify_array_start)
    if verify_end == -1:
        verify_end = updated_content.find(";\r\n", verify_array_start)
    
    extracted_json = updated_content[verify_array_start:verify_end].strip()
    parsed = json.loads(extracted_json)

    assert len(parsed) == 68, f"Verification failed: expected 68 questions, got {len(parsed)}"
    
    verified_with_sub = [q for q in parsed if "origin_sub_questions" in q and q["origin_sub_questions"]]
    verified_sub_count = sum(len(q["origin_sub_questions"]) for q in verified_with_sub)

    assert len(verified_with_sub) == 16, f"Verification failed: expected 16 questions with sub, got {len(verified_with_sub)}"
    assert verified_sub_count == 38, f"Verification failed: expected 38 sub-questions, got {verified_sub_count}"

    # Verify Question 53 specifically
    q53 = next((q for q in parsed if q["id"] == 53), None)
    assert q53 is not None, "Question 53 not found!"
    assert "origin_sub_questions" in q53, "Question 53 missing origin_sub_questions!"
    assert len(q53["origin_sub_questions"]) > 0, "Question 53 origin_sub_questions is empty!"
    
    first_sub = q53["origin_sub_questions"][0]
    for key in ["num", "question", "points", "answer", "source"]:
        assert key in first_sub, f"Question 53 first sub-question missing key: {key}"

    print("[+] SUCCESS! index.html updated and verified with 100% accuracy.")
    print(f"    - 68 total questions")
    print(f"    - 16 essay questions with origin_sub_questions")
    print(f"    - 38 total sub-questions")
    print(f"    - Question 53 validated: {len(q53['origin_sub_questions'])} sub-questions")

if __name__ == "__main__":
    sync_data()
