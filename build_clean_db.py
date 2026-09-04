#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_clean_db.py
Tái cấu trúc cơ sở dữ liệu câu hỏi AI/ML (~68 câu độc nhất, sạch 100% trùng lặp và 0 fallback).
Sinh file questions_db.json chuẩn hóa phục vụ Web HTML và hệ thống kiểm định pháp y.
"""

import os
import sys
import json
import re

# Thêm đường dẫn tới tin-mat-ocr để nạp dữ liệu gốc
OCR_DIR = r"C:\Users\Admin\Desktop\học tập\tin-mat-ocr"
TARGET_DIR = r"C:\Users\Admin\Desktop\học tập\Bo_De_AI_ML_Da_Giai"
if OCR_DIR not in sys.path:
    sys.path.append(OCR_DIR)

from generate_all_solutions import SINGLE_CHOICE_QUESTIONS, MULTI_CHOICE_QUESTIONS

# Ánh xạ Tracks cho 47 câu trắc nghiệm đơn (ID 1 -> 47)
SINGLE_CHOICE_TRACKS = {
    1: ["track1"],
    2: ["track1"],
    3: ["track2"],
    4: ["track1"],
    5: ["track1", "track2", "track3"], # Chung cho cả 3 track
    6: ["track1"],
    7: ["track2"],
    8: ["track1"],
    9: ["track2"],
    10: ["track3"],
    11: ["track2"],
    12: ["track3"],
    13: ["track1"],
    14: ["track1"],
    15: ["track1"],
    16: ["track2"],
    17: ["track1", "track2", "track3"], # Chung RAG vs Model Upgrade
    18: ["track1"],
    19: ["track3"],
    20: ["track3"],
    21: ["track3"],
    22: ["track3"],
    23: ["track3"],
    24: ["track3"],
    25: ["track3"],
    26: ["track3"],
    27: ["track3"],
    28: ["track3"],
    29: ["track2"],
    30: ["track2"],
    31: ["track2"],
    32: ["track2"],
    33: ["track2"],
    34: ["track2"],
    35: ["track2"],
    36: ["track2"],
    37: ["track2"],
    38: ["track1"],
    39: ["track2"],
    40: ["track1", "track2", "track3"], # Chung RAGAS Faithfulness
    41: ["track1"],
    42: ["track2"],
    43: ["track2"],
    44: ["track2"],
    45: ["track1"],
    46: ["track2"],
    47: ["track2"]
}

# Ánh xạ Tracks cho 5 câu trắc nghiệm nhiều đáp án (ID 48 -> 52)
MULTI_CHOICE_TRACKS = {
    48: ["track1", "track3"], # RAG vs Fine-tuning
    49: ["track2", "track3"], # Guardrails cho AI agent
    50: ["track1", "track2"], # Multi-agent architecture
    51: ["track1"],           # Best practice System Prompt
    52: ["track2", "track3"]  # Metrics monitor production
}

# Ánh xạ Tracks cho 16 bài tập tự luận / tình huống lớn (ID 53 -> 68)
ESSAY_TRACKS = {
    53: ["track1"],           # Điền từ ReAct (Thought, Action, Observation)
    54: ["track2"],           # Điền tham số API (temperature, max_tokens, top_p)
    55: ["track2"],           # Điền từ Semantic Search (Embedding, Cosine, Retrieval)
    56: ["track1"],           # Ghép nối định nghĩa AI (A1-B5, A2-B4, ...)
    57: ["track2"],           # Sắp xếp quy trình RAG Indexing (B->E->A->C->D)
    58: ["track3"],           # Sắp xếp AI Product Lifecycle (C->B->D->E->A)
    59: ["track1"],           # Thiết kế kiến trúc Supervisor-Worker
    60: ["track1", "track2"], # Khái niệm Output Contract trong System Prompt
    61: ["track2"],           # Chunking chính sách hoàn tiền & Metadata
    62: ["track2"],           # P99 Latency vs Average Latency
    63: ["track1"],           # Trace Thought-Action-Observation USD/VND
    64: ["track1"],           # Viết System Prompt CSKH Chuẩn Production
    65: ["track1", "track2"], # Sửa 2 lỗi thiết kế code ReAct Python
    66: ["track3"],           # Bài toán tài chính ROI CSKH Logistics (ROI 142.5%)
    67: ["track2", "track3"], # Sự cố E-commerce Upgrade chiều thứ Sáu
    68: ["track3"]            # Khung kiểm định trước Production (RAGAS)
}

# Tóm tắt đáp án chuẩn cho 16 bài tự luận (để hiển thị gọn gàng trên UI trước khi mở rộng)
ESSAY_CORRECT_SUMMARIES = {
    53: "[1] = Thought | [2] = Action | [3] = Observation",
    54: "[1] = temperature | [2] = max_tokens | [3] = top_p",
    55: "[1] = Embedding | [2] = Cosine similarity | [3] = Retrieval",
    56: "A1—B5 | A2—B4 | A3—B3 | A4—B1 | A5—B2",
    57: "B → E → A → C → D",
    58: "C → B → D → E → A",
    59: "Supervisor-Worker (1 Supervisor điều phối + 3 Worker chuyên trách)",
    60: "Output Contract: Giao ước định dạng bắt buộc (JSON Schema) cho Machine-readable & Tool Chaining",
    61: "Semantic Chunking nguyên đoạn + Metadata chuẩn (doc_id, version, category, source_url)",
    62: "P99 Latency: Đo lường trải nghiệm 1% worst-case, SLA và rủi ro nghẽn hệ thống",
    63: "Thought → Action: get_exchange_rate('USD', 'VND') → Observation: 25.450 → Final Answer",
    64: "System Prompt 4 phần: ROLE & PERSONA, CONSTRAINTS, OUTPUT CONTRACT, SAFEGUARD (PII)",
    65: "Fix 2 lỗi cốt tử: Mất context trong loop & Thiếu điều kiện dừng + Code run_agent() Python chuẩn",
    66: "Cost 380tr | Benefit 921.6tr | Lợi nhuận ròng 541.6tr | ROI 142.5%",
    67: "3 sai lầm Friday deploy | Phân luồng Model Routing GPT-4o-mini | Pipeline CI/CD Eval Gate 6 bước",
    68: "Golden Dataset 150-200 câu | 4 RAGAS metrics | Pass/Fail: Faithfulness >= 0.95, Relevance >= 0.90"
}

def parse_essay_markdown(filepath):
    """
    Phân tích file cau-hoi-tu-luan.md để trích xuất 16 bài tự luận chuẩn hóa.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Tách theo ### Câu X (...)
    items = re.split(r'(?m)^###\s+(?:Câu|Bài)\s+(\d+)\s*(?:\(([^)]+)\))?:', text)
    essays = []
    for i in range(1, len(items), 3):
        num = int(items[i])
        sub_type = items[i+1].strip() if items[i+1] else "Tự luận"
        body = items[i+2].strip()

        # Tách phần đề bài và phần giải pháp
        parts = re.split(r'(?m)^\*\*(?:Chi tiết từng ý và câu trả lời|Lời giải / Câu trả lời chuẩn xác):\*\*', body)
        q_text = parts[0].replace('**Nội dung:**', '').strip()
        # Loại bỏ gạch phân cách cuối bài nếu có
        sol_text = parts[1].strip() if len(parts) > 1 else ""
        sol_text = re.sub(r'(?m)^---+\s*$', '', sol_text).strip()

        essays.append({
            "essay_index": num,
            "sub_type": sub_type,
            "question": q_text,
            "explanation": sol_text
        })
    return essays

def build_database():
    questions = []

    print("[1/4] Xử lý 47 câu trắc nghiệm đơn...")
    for idx, q in enumerate(SINGLE_CHOICE_QUESTIONS):
        qid = idx + 1
        tracks = SINGLE_CHOICE_TRACKS.get(qid, ["track1"])
        
        # Xử lý đặc biệt Câu 5: hỗ trợ A, B, C đều đúng
        if qid == 5:
            correct_val = ["A", "B", "C"]
            explanation_val = (
                "Cả 3 phương án A, B, C đều chính xác tùy theo định hướng chuyên môn của học viên:\n"
                "- Track 1 (AI Applications): Phát triển ứng dụng AI, Agentic Workflows, ReAct, Prompt Engineering & Multi-Agent Systems.\n"
                "- Track 2 (AI Infrastructure): Hạ tầng kỹ thuật AI, MLOps, LLMOps, GPU FinOps, Vector Database & Model Serving Optimization.\n"
                "- Track 3 (AI Product): Quản trị sản phẩm AI, tính toán tài chính ROI, phân tích thị trường, khung pháp lý (EU AI Act, Luật TTNT VN 2025) & vòng đời sản phẩm."
            )
        else:
            correct_val = q["correct"]
            explanation_val = q["explanation"]

        questions.append({
            "id": qid,
            "type": "single_choice",
            "question": q["question"].strip(),
            "choices": [c.strip() for c in q["choices"]],
            "correct": correct_val,
            "explanation": explanation_val.strip(),
            "tracks": tracks,
            "is_app": "track1" in tracks,
            "is_infra": "track2" in tracks,
            "is_prod": "track3" in tracks,
            "category": "Trắc nghiệm đơn",
            "tags": [f"Track {t[-1]}" for t in tracks]
        })

    print(f" -> Đã nạp thành công {len(questions)} câu trắc nghiệm đơn.")

    print("[2/4] Xử lý 5 câu trắc nghiệm nhiều đáp án...")
    for idx, q in enumerate(MULTI_CHOICE_QUESTIONS):
        qid = 47 + idx + 1 # 48 -> 52
        tracks = MULTI_CHOICE_TRACKS.get(qid, ["track1"])

        questions.append({
            "id": qid,
            "type": "multi_choice",
            "question": q["question"].strip(),
            "choices": [c.strip() for c in q["choices"]],
            "correct": q["correct"],
            "explanation": q["explanation"].strip(),
            "tracks": tracks,
            "is_app": "track1" in tracks,
            "is_infra": "track2" in tracks,
            "is_prod": "track3" in tracks,
            "category": "Trắc nghiệm nhiều đáp án",
            "tags": [f"Track {t[-1]}" for t in tracks]
        })

    print(f" -> Đã nạp thành công 5 câu nhiều đáp án. Tổng hiện tại: {len(questions)} câu.")

    print("[3/4] Phân tích và nạp 16 bài tập tự luận/tình huống lớn từ cau-hoi-tu-luan.md...")
    essay_md_path = os.path.join(TARGET_DIR, "cau-hoi-tu-luan.md")
    parsed_essays = parse_essay_markdown(essay_md_path)
    assert len(parsed_essays) == 16, f"Kỳ vọng 16 bài tự luận, thực tế tìm thấy {len(parsed_essays)}"

    for idx, e in enumerate(parsed_essays):
        qid = 52 + idx + 1 # 53 -> 68
        tracks = ESSAY_TRACKS.get(qid, ["track1"])
        correct_summary = ESSAY_CORRECT_SUMMARIES.get(qid, "Xem lời giải chi tiết bên dưới.")

        questions.append({
            "id": qid,
            "type": "tu_luan",
            "title": f"Bài {e['essay_index']}: {e['sub_type']}",
            "question": e["question"].strip(),
            "choices": [],
            "correct": correct_summary,
            "explanation": e["explanation"].strip(),
            "tracks": tracks,
            "is_app": "track1" in tracks,
            "is_infra": "track2" in tracks,
            "is_prod": "track3" in tracks,
            "category": f"Tự luận / {e['sub_type']}",
            "tags": [f"Track {t[-1]}" for t in tracks] + [e['sub_type']]
        })

    print(f" -> Đã nạp thành công 16 bài tự luận. Tổng cộng: {len(questions)} câu.")

    # [4/4] Kiểm tra toàn vẹn dữ liệu
    print("[4/4] Kiểm tra tính toàn vẹn và độ sạch của cơ sở dữ liệu...")
    assert len(questions) == 68, f"LỖI: Tổng số câu không phải 68 mà là {len(questions)}"

    # Kiểm tra placeholder
    bad_patterns = ["Xem lời giải chi tiết bên dưới", "bài giảng kỹ thuật", "kiểm tra lại trong bài học", "theo bài giảng"]
    found_placeholders = 0
    for q in questions:
        # Kiểm tra explanation không được chứa fallback text chung chung
        if "phương án chuẩn xác theo nguyên lý thiết kế" in q["explanation"].lower():
            print(f" [!] Cảnh báo placeholder tại câu {q['id']}")
            found_placeholders += 1
        if "theo bài giảng" in q["explanation"].lower():
            print(f" [!] Cảnh báo 'theo bài giảng' tại câu {q['id']}")
            found_placeholders += 1

    assert found_placeholders == 0, f"LỖI: Phát hiện {found_placeholders} câu có placeholder!"

    # Kiểm tra trùng lặp nội dung câu hỏi
    seen_questions = set()
    for q in questions:
        norm = re.sub(r'\s+', ' ', q["question"]).strip().lower()[:80]
        if norm in seen_questions:
            raise AssertionError(f"LỖI: Phát hiện câu hỏi trùng lặp tại ID {q['id']}: {norm}")
        seen_questions.add(norm)

    # Kiểm tra Câu 5
    q5 = next(item for item in questions if item["id"] == 5)
    assert set(q5["correct"]) == {"A", "B", "C"}, "LỖI: Câu 5 không chấp nhận cả A, B, C"

    # Ghi ra questions_db.json
    output_path = os.path.join(TARGET_DIR, "questions_db.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    file_size = os.path.getsize(output_path)
    print(f"✅ XUẤT THÀNH CÔNG: {output_path} ({file_size:,} bytes, đúng {len(questions)} câu sạch 100%).")

    # [5/5] Cập nhật đồng bộ index.html (§16 Bundle Drift Prevention)
    print("[5/5] Tự động cập nhật đồng bộ file index.html...")
    try:
        import update_index_html
        update_index_html.generate_html()
    except Exception as e:
        print(f"Lỗi khi cập nhật index.html: {e}")

    return questions

if __name__ == "__main__":
    build_database()
