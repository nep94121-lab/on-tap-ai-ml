#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
E2E VERIFICATION SUITE — BỘ ĐỀ THI & ỨNG DỤNG ÔN TẬP AI/ML (WEB QUIZ)
================================================================================
File: C:\\Users\\Admin\\Desktop\\học tập\\Bo_De_AI_ML_Da_Giai\\verify_quiz_suite.py
Vai trò tác giả: Test Writer Agent (Phase 2 - E2E Verification Track)
Mục tiêu: Kiểm thử độc lập 100% tiêu chí nghiệm thu từ ORIGINAL_REQUEST.md & DISPATCH.md
================================================================================
Các tiêu chí kiểm định (8 Test Suites):
1. SUITE 1: Kiểm định quy mô dữ liệu & phân loại định dạng (68 câu = 47 đơn + 5 nhiều + 16 tự luận)
2. SUITE 2: Quét sạch 100% chuỗi fallback placeholder ("Xem lời giải", "theo bài giảng", ...)
3. SUITE 3: Kiểm định trùng lặp nội dung câu hỏi (0 nhóm trùng lặp)
4. SUITE 4: Tính toàn vẹn của câu trắc nghiệm (100% có đáp án đúng & giải thích chuyên môn sâu)
5. SUITE 5: Kiểm định pháp y nội dung câu tự luận (ROI 142.5%, ReAct code, deploy e-commerce, system prompt, RAGAS)
6. SUITE 6: Kiểm tra logic chấm điểm Câu 5 trắc nghiệm (chấp nhận A/B/C)
7. SUITE 7: Kiểm định tương thích Offline & Zero-CORS (không fetch ngoài trên file://)
8. SUITE 8: Kiểm định giao diện Web HTML, bộ lọc 3 Tracks và các tính năng tương tác
================================================================================
"""

import sys
import os
import json
import re
import unicodedata
import argparse
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

# Cấu hình màu sắc Terminal (ANSI)
COLOR_RESET = "\033[0m"
COLOR_BOLD = "\033[1m"
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_MAGENTA = "\033[95m"
COLOR_CYAN = "\033[96m"

# Danh sách từ khóa fallback bị cấm tuyệt đối theo Acceptance Criteria
FORBIDDEN_FALLBACK_PATTERNS = [
    r"xem\s+lời\s+giải",
    r"theo\s+bài\s+giảng",
    r"phương\s+án\s+chuẩn\s+xác\s+theo\s+nguyên\s+lý\s+thiết\s+kế",
    r"kiểm\s+tra\s+lại\s+trong\s+bài\s+học",
    r"bài\s+giảng\s+kỹ\s+thuật",
]


class TestResult:
    def __init__(self, suite_id: str, suite_name: str, check_name: str, passed: bool, message: str, details: Optional[List[str]] = None):
        self.suite_id = suite_id
        self.suite_name = suite_name
        self.check_name = check_name
        self.passed = passed
        self.message = message
        self.details = details or []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "suite_id": self.suite_id,
            "suite_name": self.suite_name,
            "check_name": self.check_name,
            "passed": self.passed,
            "message": self.message,
            "details": self.details,
        }


def normalize_text(text: str) -> str:
    """Chuẩn hóa chuỗi văn bản: unicode NFD/NFC, chữ thường, bỏ dấu câu và khoảng trắng thừa."""
    if not text:
        return ""
    text = unicodedata.normalize("NFC", text.lower())
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


class QuizVerificationSuite:
    def __init__(self, db_path: Path, html_path: Path, verbose: bool = False):
        self.db_path = db_path
        self.html_path = html_path
        self.verbose = verbose
        self.results: List[TestResult] = []

        self.db_questions: List[Dict[str, Any]] = []
        self.html_questions: List[Dict[str, Any]] = []
        self.html_content: str = ""

        self._load_files()

    def _load_files(self):
        """Đọc và nạp dữ liệu từ questions_db.json và index.html."""
        # 1. Đọc JSON DB
        if self.db_path.exists():
            try:
                with open(self.db_path, "r", encoding="utf-8") as f:
                    self.db_questions = json.load(f)
            except Exception as e:
                self.results.append(
                    TestResult(
                        "SETUP",
                        "File Loading",
                        "Load questions_db.json",
                        False,
                        f"Lỗi cú pháp JSON khi đọc {self.db_path}: {e}",
                    )
                )
        else:
            self.results.append(
                TestResult(
                    "SETUP",
                    "File Loading",
                    "Load questions_db.json",
                    False,
                    f"Không tìm thấy file: {self.db_path}",
                )
            )

        # 2. Đọc HTML Content & bóc tách mảng questions
        if self.html_path.exists():
            try:
                with open(self.html_path, "r", encoding="utf-8") as f:
                    self.html_content = f.read()

                # Bóc tách biến const questions = [...] trong script
                match = re.search(r"const\s+questions\s*=\s*(\[\s*\{.*?\}\s*\]);", self.html_content, re.DOTALL)
                if not match:
                    # Thử dạng regex linh hoạt hơn
                    match = re.search(r"(?:const|var|let)\s+questions\s*=\s*(\[.*?\]);", self.html_content, re.DOTALL)

                if match:
                    try:
                        self.html_questions = json.loads(match.group(1))
                    except Exception as e:
                        self.results.append(
                            TestResult(
                                "SETUP",
                                "File Loading",
                                "Parse questions array in index.html",
                                False,
                                f"Lỗi parse JSON mảng questions trong index.html: {e}",
                            )
                        )
                else:
                    self.results.append(
                        TestResult(
                            "SETUP",
                            "File Loading",
                            "Extract questions array in index.html",
                            False,
                            "Không tìm thấy định nghĩa mảng `const questions = [...]` trong index.html",
                        )
                    )
            except Exception as e:
                self.results.append(
                    TestResult(
                        "SETUP",
                        "File Loading",
                        "Read index.html",
                        False,
                        f"Lỗi đọc file {self.html_path}: {e}",
                    )
                )
        else:
            self.results.append(
                TestResult(
                    "SETUP",
                    "File Loading",
                    "Read index.html",
                    False,
                    f"Không tìm thấy file: {self.html_path}",
                )
            )

    # --------------------------------------------------------------------------
    # SUITE 1: ĐẾM SỐ CÂU HỎI VÀ PHÂN LOẠI ĐỊNH DẠNG (ĐÚNG 68 CÂU ĐỘC NHẤT)
    # --------------------------------------------------------------------------
    def run_suite_1_size_and_distribution(self):
        suite_id = "SUITE_1"
        suite_name = "Quy mô Dữ liệu & Phân bố Định dạng"

        # Kiểm định trên questions_db.json
        if self.db_questions:
            total_db = len(self.db_questions)
            sc_db = sum(1 for q in self.db_questions if q.get("type") in ("single_choice", "single"))
            mc_db = sum(1 for q in self.db_questions if q.get("type") in ("multi_choice", "multi"))
            essay_db = sum(1 for q in self.db_questions if q.get("type") in ("tu_luan", "essay", "dien_tu"))

            # Check 1.1: Tổng số câu questions_db.json == 68
            p1 = (total_db == 68)
            msg1 = f"Tổng số câu trong questions_db.json: {total_db}/68 câu"
            det1 = [f"Phân loại hiện tại: {sc_db} trắc nghiệm đơn, {mc_db} nhiều đáp án, {essay_db} tự luận/tình huống"]
            self.results.append(TestResult(suite_id, suite_name, "DB Total Questions == 68", p1, msg1, det1))

            # Check 1.2: Phân bố 47 đơn, 5 nhiều, 16 tự luận trong DB
            p2 = (sc_db == 47 and mc_db == 5 and essay_db == 16)
            msg2 = f"Phân bố dạng câu hỏi trong questions_db.json: Single={sc_db}/47, Multi={mc_db}/5, Essay={essay_db}/16"
            self.results.append(TestResult(suite_id, suite_name, "DB Category Distribution (47-5-16)", p2, msg2))

        # Kiểm định trên index.html
        if self.html_questions:
            total_html = len(self.html_questions)
            sc_html = sum(1 for q in self.html_questions if q.get("type") in ("single_choice", "single"))
            mc_html = sum(1 for q in self.html_questions if q.get("type") in ("multi_choice", "multi"))
            essay_html = sum(1 for q in self.html_questions if q.get("type") in ("tu_luan", "essay", "dien_tu"))

            # Check 1.3: Tổng số câu embedded index.html == 68
            p3 = (total_html == 68)
            msg3 = f"Tổng số câu embedded trong index.html: {total_html}/68 câu"
            det3 = [f"Phân loại hiện tại: {sc_html} trắc nghiệm đơn, {mc_html} nhiều đáp án, {essay_html} tự luận/tình huống"]
            self.results.append(TestResult(suite_id, suite_name, "HTML Embedded Total == 68", p3, msg3, det3))

            # Check 1.4: Phân bố trong index.html
            p4 = (sc_html == 47 and mc_html == 5 and essay_html == 16)
            msg4 = f"Phân bố dạng câu hỏi trong index.html: Single={sc_html}/47, Multi={mc_html}/5, Essay={essay_html}/16"
            self.results.append(TestResult(suite_id, suite_name, "HTML Category Distribution (47-5-16)", p4, msg4))

    # --------------------------------------------------------------------------
    # SUITE 2: QUÉT SẠCH 100% CHUỖI FALLBACK PLACEHOLDER
    # --------------------------------------------------------------------------
    def run_suite_2_fallback_elimination(self):
        suite_id = "SUITE_2"
        suite_name = "Quét Sạch Chuỗi Fallback Placeholder"

        def scan_fallbacks(questions: List[Dict[str, Any]], source_name: str) -> Tuple[int, List[str]]:
            violations = []
            for q in questions:
                qid = q.get("id", "Unknown")
                text_corpus = " ".join([
                    str(q.get("question", "")),
                    str(q.get("correct", "")),
                    str(q.get("explanation", "")),
                    str(q.get("full_body", "")),
                    " ".join(q.get("choices", [])) if isinstance(q.get("choices"), list) else str(q.get("choices", ""))
                ])

                matched_patterns = []
                for pat in FORBIDDEN_FALLBACK_PATTERNS:
                    if re.search(pat, text_corpus, re.IGNORECASE):
                        matched_patterns.append(pat)

                if matched_patterns:
                    violations.append(
                        f"[{source_name}] Câu ID {qid}: chứa fallback {matched_patterns} (Trích dẫn: '{q.get('explanation', '')[:60]}...')"
                    )
            return len(violations), violations

        # Check 2.1: Fallback trong questions_db.json
        if self.db_questions:
            count_db, details_db = scan_fallbacks(self.db_questions, "DB")
            p_db = (count_db == 0)
            msg_db = f"Số câu hỏi dính fallback trong questions_db.json: {count_db} câu (Kỳ vọng: 0)"
            self.results.append(TestResult(suite_id, suite_name, "Zero Fallback in questions_db.json", p_db, msg_db, details_db))

        # Check 2.2: Fallback trong index.html
        if self.html_questions:
            count_html, details_html = scan_fallbacks(self.html_questions, "HTML")
            p_html = (count_html == 0)
            msg_html = f"Số câu hỏi dính fallback trong index.html: {count_html} câu (Kỳ vọng: 0)"
            self.results.append(TestResult(suite_id, suite_name, "Zero Fallback in index.html", p_html, msg_html, details_html))

    # --------------------------------------------------------------------------
    # SUITE 3: KIỂM ĐỊNH TRÙNG LẶP NỘI DUNG (0 NHÓM TRÙNG LẶP)
    # --------------------------------------------------------------------------
    def run_suite_3_deduplication(self):
        suite_id = "SUITE_3"
        suite_name = "Kiểm Định Trùng Lặp Nội Dung (Deduplication)"

        def find_duplicate_groups(questions: List[Dict[str, Any]], source_name: str) -> Tuple[int, List[str]]:
            seen: Dict[str, List[int]] = {}
            for q in questions:
                raw_q = q.get("question", "")
                norm = normalize_text(raw_q)
                # Lấy 60 ký tự đầu của câu hỏi chuẩn hóa để nhận diện trùng lặp đề bài
                key = norm[:80] if len(norm) >= 80 else norm
                if not key:
                    continue
                seen.setdefault(key, []).append(q.get("id", -1))

            duplicate_groups = {k: v for k, v in seen.items() if len(v) > 1}
            details = []
            for k, v in duplicate_groups.items():
                details.append(f"[{source_name}] Nhóm trùng lặp IDs {v}: '{k[:50]}...'")

            return len(duplicate_groups), details

        # Check 3.1: Trùng lặp trong questions_db.json
        if self.db_questions:
            count_db, details_db = find_duplicate_groups(self.db_questions, "DB")
            p_db = (count_db == 0)
            msg_db = f"Số nhóm câu hỏi trùng lặp trong questions_db.json: {count_db} nhóm (Kỳ vọng: 0)"
            self.results.append(TestResult(suite_id, suite_name, "Zero Duplicates in questions_db.json", p_db, msg_db, details_db))

        # Check 3.2: Trùng lặp trong index.html
        if self.html_questions:
            count_html, details_html = find_duplicate_groups(self.html_questions, "HTML")
            p_html = (count_html == 0)
            msg_html = f"Số nhóm câu hỏi trùng lặp trong index.html: {count_html} nhóm (Kỳ vọng: 0)"
            self.results.append(TestResult(suite_id, suite_name, "Zero Duplicates in index.html", p_html, msg_html, details_html))

        # Check 3.3: Tính duy nhất của ID (1 đến 68)
        if self.db_questions:
            ids = [q.get("id") for q in self.db_questions]
            unique_ids = set(ids)
            p_ids = (len(ids) == len(unique_ids))
            msg_ids = f"Tính độc nhất của trường ID trong DB: {len(unique_ids)}/{len(ids)} unique IDs"
            self.results.append(TestResult(suite_id, suite_name, "Unique IDs in questions_db.json", p_ids, msg_ids))

    # --------------------------------------------------------------------------
    # SUITE 4: TÍNH TOÀN VẸN CÂU TRẮC NGHIỆM (100% CÓ ĐÁP ÁN & GIẢI THÍCH SÂU)
    # --------------------------------------------------------------------------
    def run_suite_4_objective_questions_integrity(self):
        suite_id = "SUITE_4"
        suite_name = "Tính Toàn Vẹn Câu Trắc Nghiệm (Single & Multi)"

        # Kiểm định câu trắc nghiệm đơn (Single Choice)
        single_questions = [q for q in self.db_questions if q.get("type") in ("single_choice", "single")]
        sc_errors = []
        for q in single_questions:
            qid = q.get("id")
            choices = q.get("choices", [])
            correct = q.get("correct")
            explanation = str(q.get("explanation", "")).strip()

            if not choices or len(choices) < 2:
                sc_errors.append(f"Câu ID {qid}: danh sách choices rỗng hoặc < 2 lựa chọn")

            if not correct:
                sc_errors.append(f"Câu ID {qid}: trường correct bị rỗng")

            # Giải thích phải sâu (> 25 ký tự và không rỗng)
            if len(explanation) < 25:
                sc_errors.append(f"Câu ID {qid}: explanation quá ngắn hoặc rỗng ({len(explanation)} chars)")

        p_sc = (len(sc_errors) == 0)
        msg_sc = f"Kiểm tra 47 câu trắc nghiệm đơn: {len(single_questions) - len(sc_errors)}/{len(single_questions)} câu đạt chuẩn"
        self.results.append(TestResult(suite_id, suite_name, "Single Choice Integrity (Choices, Correct, Explanation)", p_sc, msg_sc, sc_errors))

        # Kiểm định câu trắc nghiệm nhiều đáp án (Multi Choice)
        multi_questions = [q for q in self.db_questions if q.get("type") in ("multi_choice", "multi")]
        mc_errors = []
        for q in multi_questions:
            qid = q.get("id")
            choices = q.get("choices", [])
            correct = q.get("correct")
            explanation = str(q.get("explanation", "")).strip()

            if not choices or len(choices) < 2:
                mc_errors.append(f"Câu ID {qid}: danh sách choices rỗng hoặc < 2")

            # Đáp án đúng của multi choice phải là danh sách có ít nhất 2 phương án (hoặc chuỗi nhiều ký tự)
            if isinstance(correct, list):
                if len(correct) < 2:
                    mc_errors.append(f"Câu ID {qid}: correct là mảng nhưng có < 2 đáp án: {correct}")
            elif isinstance(correct, str):
                if len(re.findall(r"[A-E]", correct)) < 2:
                    mc_errors.append(f"Câu ID {qid}: correct dạng chuỗi nhưng có < 2 đáp án: '{correct}'")
            else:
                mc_errors.append(f"Câu ID {qid}: định dạng trường correct không hợp lệ: {type(correct)}")

            if len(explanation) < 25:
                mc_errors.append(f"Câu ID {qid}: explanation quá ngắn hoặc rỗng ({len(explanation)} chars)")

        p_mc = (len(mc_errors) == 0)
        msg_mc = f"Kiểm tra 5 câu trắc nghiệm nhiều đáp án: {len(multi_questions) - len(mc_errors)}/{len(multi_questions)} câu đạt chuẩn"
        self.results.append(TestResult(suite_id, suite_name, "Multi Choice Integrity (Choices >= 2, Correct List, Explanation)", p_mc, msg_mc, mc_errors))

    # --------------------------------------------------------------------------
    # SUITE 5: KIỂM ĐỊNH PHÁP Y NỘI DUNG CÂU TỰ LUẬN & TÌNH HUỐNG
    # --------------------------------------------------------------------------
    def run_suite_5_essay_forensic_accuracy(self):
        suite_id = "SUITE_5"
        suite_name = "Kiểm Định Pháp Y Nội Dung Câu Tự Luận & Tình Huống"

        essay_questions = [q for q in self.db_questions if q.get("type") in ("tu_luan", "essay", "dien_tu")]
        
        # Check 5.1: 100% câu tự luận có explanation chi tiết (> 80 ký tự)
        shallow_essays = []
        for q in essay_questions:
            qid = q.get("id")
            explanation = str(q.get("explanation", "")).strip()
            full_body = str(q.get("full_body", "")).strip()
            # Nội dung giải thích kết hợp
            combined_sol = explanation + " " + full_body
            if len(combined_sol) < 80:
                shallow_essays.append(f"Câu ID {qid}: lời giải quá sơ sài ({len(combined_sol)} ký tự)")

        p_len = (len(shallow_essays) == 0 and len(essay_questions) > 0)
        msg_len = f"Độ sâu lời giải 16 câu tự luận: {len(essay_questions) - len(shallow_essays)}/{len(essay_questions)} câu có lời giải chi tiết"
        self.results.append(TestResult(suite_id, suite_name, "Essay Detailed Solution Length (>80 chars)", p_len, msg_len, shallow_essays))

        # Tổng hợp toàn bộ văn bản của các câu tự luận để kiểm tra forensic các thành phần bắt buộc
        essay_corpus = " ".join([
            str(q.get("question", "")) + " " + str(q.get("explanation", "")) + " " + str(q.get("correct", "")) + " " + str(q.get("full_body", ""))
            for q in essay_questions
        ])

        # Check 5.2: Bài toán tài chính CSKH Logistics (Quỹ lương 8 người, 380tr, 921.6tr, 541.6tr, ROI 142.5%)
        roi_checks = [
            ("Quỹ lương / Headcount", bool(re.search(r"(quỹ\s+lương|8\s+người|12\s+triệu|96\s+triệu)", essay_corpus, re.I))),
            ("Tổng chi phí 380tr", bool(re.search(r"380\s*(triệu|tr)", essay_corpus, re.I))),
            ("Lợi ích 921.6tr", bool(re.search(r"921[\.,]6\s*(triệu|tr)", essay_corpus, re.I))),
            ("ROI 142.5%", bool(re.search(r"142[\.,]5\s*%", essay_corpus, re.I))),
        ]
        failed_roi = [name for name, passed in roi_checks if not passed]
        p_roi = (len(failed_roi) == 0)
        msg_roi = f"Kiểm tra số liệu tài chính CSKH Logistics: {4 - len(failed_roi)}/4 chỉ số xuất hiện"
        self.results.append(TestResult(suite_id, suite_name, "Financial ROI Case Study Forensic Data", p_roi, msg_roi, [f"Thiếu chỉ số: {failed_roi}"] if failed_roi else []))

        # Check 5.3: Mã nguồn sửa lỗi ReAct pattern (def run_agent() & 2 lỗi thiết kế)
        react_has_func = bool(re.search(r"def\s+run_agent|run_agent\(", essay_corpus))
        react_has_flaws = bool(re.search(r"(2\s+lỗi|mất\s+context|lặp\s+vô\s+hạn|infinite\s+loop|observation)", essay_corpus, re.I))
        p_react = (react_has_func and react_has_flaws)
        msg_react = f"Kiểm tra code ReAct: Có hàm run_agent(): {react_has_func}, Phân tích lỗi thiết kế: {react_has_flaws}"
        self.results.append(TestResult(suite_id, suite_name, "ReAct Pattern Code & Flaws Analysis", p_react, msg_react))

        # Check 5.4: Sự cố deploy e-commerce Friday 5pm (3 sai lầm, Model Routing, CI/CD)
        ecom_has_mistakes = bool(re.search(r"(thứ\s+sáu|friday|regression|hồi\s+quy|schema|output\s+contract)", essay_corpus, re.I))
        ecom_has_routing = bool(re.search(r"(model\s+routing|phân\s+luồng|gpt-4o-mini)", essay_corpus, re.I))
        ecom_has_cicd = bool(re.search(r"(ci/cd|canary|golden\s+dataset|benchmark)", essay_corpus, re.I))
        p_ecom = (ecom_has_mistakes and ecom_has_routing and ecom_has_cicd)
        msg_ecom = f"Kiểm tra sự cố Deploy E-commerce: 3 Sai lầm={ecom_has_mistakes}, Model Routing={ecom_has_routing}, CI/CD={ecom_has_cicd}"
        self.results.append(TestResult(suite_id, suite_name, "E-commerce Friday Deploy Case Study", p_ecom, msg_ecom))

        # Check 5.5: System prompt CSKH đầy đủ 4 phần (Role, Constraints, Output Contract, Safeguard/PII)
        prompt_has_role = bool(re.search(r"(#\s*role|vai\s*trò|persona)", essay_corpus, re.I))
        prompt_has_constraints = bool(re.search(r"(#\s*constraints|ràng\s*buộc)", essay_corpus, re.I))
        prompt_has_contract = bool(re.search(r"(#\s*output\s*contract|giao\s*ước\s*đầu\s*ra|định\s*dạng\s*đầu\s*ra)", essay_corpus, re.I))
        prompt_has_safeguard = bool(re.search(r"(#\s*safeguard|bảo\s*vệ|pii|mật\s*khẩu|otp)", essay_corpus, re.I))
        p_prompt = (prompt_has_role and prompt_has_constraints and prompt_has_contract and prompt_has_safeguard)
        msg_prompt = f"Kiểm tra System Prompt 4 phần: Role={prompt_has_role}, Constraints={prompt_has_constraints}, Contract={prompt_has_contract}, Safeguard={prompt_has_safeguard}"
        self.results.append(TestResult(suite_id, suite_name, "Production System Prompt 4 Sections", p_prompt, msg_prompt))

        # Check 5.6: Khung đánh giá RAGAS (Faithfulness, Answer Relevance, Context Precision/Recall, P99)
        ragas_has_faith = bool(re.search(r"faithfulness", essay_corpus, re.I))
        ragas_has_relevance = bool(re.search(r"answer\s*relevance", essay_corpus, re.I))
        ragas_has_context = bool(re.search(r"context\s*(precision|recall)", essay_corpus, re.I))
        ragas_has_p99 = bool(re.search(r"(p99|0[\.,]95|0[\.,]90)", essay_corpus, re.I))
        p_ragas = (ragas_has_faith and ragas_has_relevance and ragas_has_context and ragas_has_p99)
        msg_ragas = f"Kiểm tra khung RAGAS: Faithfulness={ragas_has_faith}, Answer Relevance={ragas_has_relevance}, Context Precision/Recall={ragas_has_context}, Thresholds={ragas_has_p99}"
        self.results.append(TestResult(suite_id, suite_name, "RAGAS Evaluation Framework Metrics", p_ragas, msg_ragas))

    # --------------------------------------------------------------------------
    # SUITE 6: LOGIC CHẤM ĐIỂM CÂU 5 TRẮC NGHIỆM (CHẤP NHẬN A/B/C)
    # --------------------------------------------------------------------------
    def run_suite_6_question_5_evaluation_logic(self):
        suite_id = "SUITE_6"
        suite_name = "Kiểm Tra Logic Câu 5 Trắc Nghiệm (A / B / C)"

        q5_db = next((q for q in self.db_questions if q.get("id") == 5), None)
        if not q5_db:
            self.results.append(TestResult(suite_id, suite_name, "Find Question 5 in DB", False, "Không tìm thấy câu có ID = 5 trong questions_db.json"))
            return

        # Check 6.1: Dữ liệu Câu 5 là câu hỏi chọn Track và các lựa chọn là A, B, C
        choices = q5_db.get("choices", [])
        has_3_tracks = len(choices) >= 3 and any("AI Applications" in c for c in choices) and any("AI Infrastructure" in c for c in choices) and any("AI Product" in c for c in choices)
        p_data = has_3_tracks
        msg_data = f"Dữ liệu Câu 5: '{q5_db.get('question', '')}' kèm 3 lựa chọn Tracks: {has_3_tracks}"
        self.results.append(TestResult(suite_id, suite_name, "Question 5 Track Choices Integrity", p_data, msg_data))

        # Check 6.2: Trường correct trong DB phải hỗ trợ A, B, C (dạng mảng ['A', 'B', 'C'] hoặc chuỗi linh hoạt)
        correct_val = q5_db.get("correct")
        db_accepts_all = False
        if isinstance(correct_val, list):
            db_accepts_all = set(["A", "B", "C"]).issubset(set(correct_val))
        elif isinstance(correct_val, str):
            # Nếu là string thì không được là chuỗi cứng gây lỗi so sánh 'A' === 'A / B / C...'
            # Chấp nhận nếu có cơ chế xử lý riêng
            db_accepts_all = "A" in correct_val and "B" in correct_val and "C" in correct_val
        
        msg_db = f"Trường correct của Câu 5 trong DB ({correct_val}): Chấp nhận cả 3 tracks = {db_accepts_all}"
        self.results.append(TestResult(suite_id, suite_name, "Question 5 Correct Answer Definition in DB", db_accepts_all, msg_db))

        # Check 6.3: Logic đánh giá trong JavaScript của index.html
        # Cần xác nhận khi click A, B, hoặc C thì isCorrect đều trả về TRUE
        js_accepts_all = False
        js_details = []

        if self.html_content:
            # Chạy thử nghiệm qua Node.js VM môi trường thực tế
            node_script = """
const vm = require('vm');
const fs = require('fs');

try {
    const htmlFile = process.argv[1];
    const html = fs.readFileSync(htmlFile, 'utf8');

    const scripts = html.match(/<script>([\\s\\S]*?)<\\/script>/gi) || [];
    let targetScript = '';
    for (const s of scripts) {
        if (s.includes('selectSingleChoice')) {
            targetScript = s.replace(/<\\/?script>/gi, '');
            break;
        }
    }

    if (!targetScript) {
        console.log(JSON.stringify({ success: false, error: 'Cannot find selectSingleChoice script' }));
        process.exit(0);
    }

    const context = {
        console: console,
        document: {
            getElementById: () => ({ innerText: '', value: '', classList: { add: () => {}, remove: () => {} } }),
            querySelectorAll: () => []
        },
        window: {}
    };
    vm.createContext(context);
    vm.runInContext(targetScript, context);

    // Test click 'A'
    vm.runInContext("setMode('quiz'); selectSingleChoice(5, 'A');", context);
    const ansA = vm.runInContext("userAnswers[5] ? userAnswers[5].isCorrect : null;", context);

    // Test click 'B'
    vm.runInContext("userAnswers = {}; selectSingleChoice(5, 'B');", context);
    const ansB = vm.runInContext("userAnswers[5] ? userAnswers[5].isCorrect : null;", context);

    // Test click 'C'
    vm.runInContext("userAnswers = {}; selectSingleChoice(5, 'C');", context);
    const ansC = vm.runInContext("userAnswers[5] ? userAnswers[5].isCorrect : null;", context);

    // Test click 'D'
    vm.runInContext("userAnswers = {}; selectSingleChoice(5, 'D');", context);
    const ansD = vm.runInContext("userAnswers[5] ? userAnswers[5].isCorrect : null;", context);

    console.log(JSON.stringify({ success: true, ansA, ansB, ansC, ansD }));
} catch (e) {
    console.log(JSON.stringify({ success: false, error: e.message }));
}
"""
            try:
                proc = subprocess.run(
                    ["node", "-e", node_script, str(self.html_path)],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if proc.returncode == 0 and proc.stdout.strip():
                    res = json.loads(proc.stdout.strip())
                    if res.get("success"):
                        eval_a = res.get("ansA")
                        eval_b = res.get("ansB")
                        eval_c = res.get("ansC")
                        eval_d = res.get("ansD")

                        if eval_a is True and eval_b is True and eval_c is True and eval_d is not True:
                            js_accepts_all = True
                            js_details.append(f"Node.js Virtual Evaluation: Click A={eval_a}, Click B={eval_b}, Click C={eval_c}, Click D={eval_d} (PASS: Chấp nhận cả A, B, C)")
                        else:
                            js_details.append(f"Node.js Virtual Evaluation: Click A={eval_a}, Click B={eval_b}, Click C={eval_c}, Click D={eval_d} (FAIL: Hiện tại chỉ trả về Đúng khi trùng chuỗi gốc)")
                    else:
                        js_details.append(f"Lỗi script Node: {res.get('error')}")
                else:
                    js_details.append(f"Lỗi chạy Node process: {proc.stderr.strip()}")
            except Exception as e:
                js_details.append(f"Node execution exception: {e}")

            # Phân tích tĩnh (Static analysis) fallback
            if not js_accepts_all and not any("Node.js Virtual Evaluation" in d for d in js_details):
                has_array_check = bool(re.search(r"Array\.isArray\(q\.correct\)\s*\?\s*q\.correct\.includes\(choiceLetter\)", self.html_content))
                has_q5_special = bool(re.search(r"q\.id\s*===\s*5|choiceLetter\s*===\s*q\.correct\s*\|\|", self.html_content))
                js_accepts_all = has_array_check or has_q5_special

        p_js = js_accepts_all
        msg_js = f"Kiểm tra tương tác click Câu 5 trong index.html: Chấp nhận A/B/C = {p_js}"
        self.results.append(TestResult(suite_id, suite_name, "Question 5 Interactive Click Evaluation (A/B/C)", p_js, msg_js, js_details))

    # --------------------------------------------------------------------------
    # SUITE 7: TÍNH TƯƠNG THÍCH OFFLINE & ZERO-CORS (GIAO THỨC FILE://)
    # --------------------------------------------------------------------------
    def run_suite_7_offline_compatibility(self):
        suite_id = "SUITE_7"
        suite_name = "Tính Tương Thích Offline & Zero-CORS (file://)"

        if not self.html_content:
            self.results.append(TestResult(suite_id, suite_name, "HTML Content Exists", False, "Không có nội dung index.html để kiểm tra"))
            return

        # Check 7.1: Không có lệnh fetch() đến tài nguyên cục bộ hoặc ngoài gây lỗi CORS khi mở bằng file://
        # Tìm các lệnh fetch('questions_db.json') hoặc fetch(url)
        fetch_calls = re.findall(r"fetch\s*\(\s*['\"`].*?['\"`]\s*\)", self.html_content)
        xhr_calls = re.findall(r"new\s+XMLHttpRequest", self.html_content)
        
        has_cors_risks = (len(fetch_calls) > 0 or len(xhr_calls) > 0)
        p_cors = not has_cors_risks
        msg_cors = f"Quét rủi ro CORS trên giao thức file://: Tìm thấy {len(fetch_calls)} fetch calls, {len(xhr_calls)} XMLHttpRequest"
        det_cors = [f"Phát hiện call: {c}" for c in fetch_calls + xhr_calls]
        self.results.append(TestResult(suite_id, suite_name, "Zero External Fetch / XHR Calls", p_cors, msg_cors, det_cors))

        # Check 7.2: Dữ liệu được nhúng trực tiếp (Inline Data Embedding)
        has_embedded_data = bool(self.html_questions and len(self.html_questions) > 0)
        msg_embed = f"Dữ liệu câu hỏi được nhúng trực tiếp (inline) trong index.html: {len(self.html_questions)} câu"
        self.results.append(TestResult(suite_id, suite_name, "Inline Data Embedding for Offline Use", has_embedded_data, msg_embed))

        # Check 7.3: Cấu trúc HTML5 chuẩn mực
        has_doctype = bool(re.search(r"<!DOCTYPE\s+html>", self.html_content, re.I))
        has_utf8 = bool(re.search(r"<meta\s+charset=[\"']?utf-8[\"']?", self.html_content, re.I))
        has_viewport = bool(re.search(r"<meta\s+name=[\"']viewport[\"']", self.html_content, re.I))
        p_structure = has_doctype and has_utf8 and has_viewport
        msg_structure = f"Chuẩn cấu trúc HTML5: DOCTYPE={has_doctype}, UTF-8={has_utf8}, Viewport={has_viewport}"
        self.results.append(TestResult(suite_id, suite_name, "HTML5 Offline Document Structure", p_structure, msg_structure))

    # --------------------------------------------------------------------------
    # SUITE 8: GIAO DIỆN WEB HTML & BỘ LỌC ĐẦY ĐỦ
    # --------------------------------------------------------------------------
    def run_suite_8_html_ui_and_filters(self):
        suite_id = "SUITE_8"
        suite_name = "Giao Diện Web HTML & Bộ Lọc Đầy Đủ"

        if not self.html_content:
            self.results.append(TestResult(suite_id, suite_name, "HTML UI Elements", False, "Không có nội dung index.html"))
            return

        # Check 8.1: Header/Title không còn chứa chuỗi cũ "124 Câu"
        has_old_124_title = bool(re.search(r"124\s*câu", self.html_content, re.I))
        p_title = not has_old_124_title
        msg_title = f"Tiêu đề và Header không còn chứa chuỗi lỗi '124 Câu': {'ĐẠT (Không còn)' if p_title else 'VI PHẠM (Vẫn còn 124 câu)'}"
        self.results.append(TestResult(suite_id, suite_name, "Clean Title & Header (No 124 count)", p_title, msg_title))

        # Check 8.2: Các nút lọc định dạng & chuyên đề
        filters_to_check = [
            ("Tất cả (All)", r"setFilter\s*\(\s*['\"]all['\"]\s*\)"),
            ("Trắc nghiệm đơn (Single)", r"setFilter\s*\(\s*['\"]single['\"]\s*\)"),
            ("Nhiều đáp án (Multi)", r"setFilter\s*\(\s*['\"]multi['\"]\s*\)"),
            ("Tự luận (Essay)", r"setFilter\s*\(\s*['\"]essay['\"]\s*\)"),
            ("Track 1 (AI Applications)", r"setFilter\s*\(\s*['\"]track1['\"]\s*\)"),
            ("Track 2 (AI Infrastructure)", r"setFilter\s*\(\s*['\"]track2['\"]\s*\)"),
            ("Track 3 (AI Product)", r"setFilter\s*\(\s*['\"]track3['\"]\s*\)"),
        ]
        missing_filters = []
        for label, pattern in filters_to_check:
            if not re.search(pattern, self.html_content):
                missing_filters.append(label)

        # Kiểm tra loại bỏ nút thừa "Check 2 (Bộ 2)"
        has_obsolete_check2 = bool(re.search(r"setFilter\s*\(\s*['\"]check2['\"]\s*\)", self.html_content))
        if has_obsolete_check2:
            missing_filters.append("Nút cũ 'Check 2' chưa được loại bỏ")

        p_filters = (len(missing_filters) == 0)
        msg_filters = f"Kiểm tra hệ thống nút lọc (All, Single, Multi, Essay, 3 Tracks): {7 - len([f for f in missing_filters if not 'Check 2' in f])}/7 nút hợp lệ"
        self.results.append(TestResult(suite_id, suite_name, "Comprehensive Filter Buttons Integrity", p_filters, msg_filters, missing_filters))

        # Check 8.3: Chế độ Luyện thi (Quiz) & Học tập (Study)
        has_mode_quiz = bool(re.search(r"setMode\s*\(\s*['\"]quiz['\"]\s*\)", self.html_content))
        has_mode_study = bool(re.search(r"setMode\s*\(\s*['\"]study['\"]\s*\)", self.html_content))
        p_mode = has_mode_quiz and has_mode_study
        msg_mode = f"Chế độ học tập: Quiz Mode (Ẩn đáp án)={has_mode_quiz}, Study Mode (Hiện sẵn)={has_mode_study}"
        self.results.append(TestResult(suite_id, suite_name, "Dual Mode Switch (Quiz / Study)", p_mode, msg_mode))

        # Check 8.4: Ô tìm kiếm từ khóa và bộ đếm điểm real-time
        has_search = bool(re.search(r"id=[\"']searchInput[\"']", self.html_content) and re.search(r"handleSearch", self.html_content))
        has_score_correct = bool(re.search(r"id=[\"']scoreCorrect[\"']", self.html_content))
        has_score_wrong = bool(re.search(r"id=[\"']scoreWrong[\"']", self.html_content))
        has_progress = bool(re.search(r"id=[\"']progressPercent[\"']", self.html_content))
        p_widgets = has_search and has_score_correct and has_score_wrong and has_progress
        msg_widgets = f"Tiện ích tương tác: Search Box={has_search}, Score Correct={has_score_correct}, Score Wrong={has_score_wrong}, Progress%={has_progress}"
        self.results.append(TestResult(suite_id, suite_name, "Search Bar & Real-time Score Counters", p_widgets, msg_widgets))

    # --------------------------------------------------------------------------
    # BỘ ĐIỀU PHỐI CHẠY TOÀN BỘ TEST SUITES
    # --------------------------------------------------------------------------
    def run_all(self):
        self.run_suite_1_size_and_distribution()
        self.run_suite_2_fallback_elimination()
        self.run_suite_3_deduplication()
        self.run_suite_4_objective_questions_integrity()
        self.run_suite_5_essay_forensic_accuracy()
        self.run_suite_6_question_5_evaluation_logic()
        self.run_suite_7_offline_compatibility()
        self.run_suite_8_html_ui_and_filters()

    def print_summary(self) -> int:
        """In bảng tổng kết kết quả kiểm thử ra console."""
        total_tests = len(self.results)
        passed_tests = sum(1 for r in self.results if r.passed)
        failed_tests = total_tests - passed_tests

        print("\n" + "=" * 80)
        print(f"{COLOR_BOLD}{COLOR_CYAN}BÁO CÁO KẾT QUẢ KIỂM THỬ TỰ ĐỘNG E2E VERIFICATION SUITE{COLOR_RESET}")
        print("=" * 80)
        print(f"Cơ sở dữ liệu: {self.db_path.resolve()}")
        print(f"File Web HTML : {self.html_path.resolve()}")
        print("-" * 80)

        current_suite = ""
        for r in self.results:
            if r.suite_id != current_suite:
                current_suite = r.suite_id
                print(f"\n{COLOR_BOLD}{COLOR_BLUE}▶ [{r.suite_id}] {r.suite_name}{COLOR_RESET}")

            status_icon = f"{COLOR_GREEN}✔ PASS{COLOR_RESET}" if r.passed else f"{COLOR_RED}✖ FAIL{COLOR_RESET}"
            print(f"  [{status_icon}] {r.check_name}")
            print(f"         {r.message}")

            if not r.passed and r.details:
                for d in r.details[:5]:
                    print(f"         {COLOR_YELLOW}↳ {d}{COLOR_RESET}")
                if len(r.details) > 5:
                    print(f"         {COLOR_YELLOW}↳ ... và {len(r.details) - 5} vi phạm khác{COLOR_RESET}")

        print("\n" + "=" * 80)
        rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        if failed_tests == 0:
            print(f"{COLOR_BOLD}{COLOR_GREEN}KẾT LUẬN TOÀN DIỆN: 100% PASS! HỆ THỐNG ĐẠT CHUẨN NGHIỆM THU TUYỆT ĐỐI.{COLOR_RESET}")
        else:
            print(f"{COLOR_BOLD}{COLOR_RED}KẾT LUẬN TOÀN DIỆN: PHÁT HIỆN {failed_tests} HẠNG MỤC CHƯA ĐẠT (Tỷ lệ: {rate:.1f}% PASS).{COLOR_RESET}")
            print(f"{COLOR_YELLOW}Cần chuyển giao danh sách lỗi cho Worker để khắc phục triệt để.{COLOR_RESET}")

        print(f"Tổng số checks: {total_tests} | Đạt: {passed_tests} | Lỗi: {failed_tests}")
        print("=" * 80 + "\n")

        return 0 if failed_tests == 0 else 1


def main():
    parser = argparse.ArgumentParser(description="Chạy bộ kiểm thử tự động E2E cho Web Quiz AI/ML")
    parser.add_argument(
        "--db",
        type=str,
        default="questions_db.json",
        help="Đường dẫn file questions_db.json",
    )
    parser.add_argument(
        "--html",
        type=str,
        default="index.html",
        help="Đường dẫn file index.html",
    )
    parser.add_argument(
        "--json-output",
        type=str,
        default=None,
        help="Xuất kết quả kiểm thử ra file JSON",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Hiển thị chi tiết toàn bộ vi phạm",
    )

    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent
    db_file = Path(args.db) if Path(args.db).is_absolute() else base_dir / args.db
    html_file = Path(args.html) if Path(args.html).is_absolute() else base_dir / args.html

    suite = QuizVerificationSuite(db_file, html_file, verbose=args.verbose)
    suite.run_all()

    if args.json_output:
        out_path = Path(args.json_output) if Path(args.json_output).is_absolute() else base_dir / args.json_output
        report_data = {
            "total_checks": len(suite.results),
            "passed": sum(1 for r in suite.results if r.passed),
            "failed": sum(1 for r in suite.results if not r.passed),
            "results": [r.to_dict() for r in suite.results],
        }
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(report_data, f, ensure_ascii=False, indent=2)
        print(f"Đã xuất báo cáo JSON ra: {out_path}")

    exit_code = suite.print_summary()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
