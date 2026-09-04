#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_index_html.py
Sinh file index.html độc lập, nhúng trực tiếp cơ sở dữ liệu 68 câu sạch từ questions_db.json.
Đảm bảo chạy offline 100% không bị CORS trên file://, đầy đủ tính năng tương tác,
bộ lọc 7 nút, chế độ Luyện thi / Học tập, tìm kiếm real-time và đếm điểm.
"""

import os
import json

TARGET_DIR = r"C:\Users\Admin\Desktop\học tập\Bo_De_AI_ML_Da_Giai"
JSON_PATH = os.path.join(TARGET_DIR, "questions_db.json")
HTML_PATH = os.path.join(TARGET_DIR, "index.html")

def generate_html():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)

    questions_json_str = json.dumps(questions, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ứng Dụng Ôn Tập AI/ML Chuẩn Hóa (68 Câu Độc Nhất)</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <style>
    /* CSS Tối Ưu Cho Cả Online & Offline */
    body {{
      font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: #f8fafc;
      color: #1e293b;
      margin: 0;
      padding: 0;
    }}
    code, pre {{
      font-family: 'JetBrains Mono', Consolas, Monaco, 'Courier New', monospace;
    }}
    .choice-btn {{
      transition: all 0.18s cubic-bezier(0.4, 0, 0.2, 1);
      cursor: pointer;
    }}
    .choice-btn:hover:not(.locked) {{
      border-color: #3b82f6;
      background-color: #eff6ff;
      transform: translateY(-1px);
    }}
    .correct-choice {{
      background-color: #ecfdf5 !important;
      border-color: #10b981 !important;
      color: #065f46 !important;
      font-weight: 600;
    }}
    .wrong-choice {{
      background-color: #fef2f2 !important;
      border-color: #ef4444 !important;
      color: #991b1b !important;
      text-decoration: line-through;
    }}
    .filter-btn.active {{
      background-color: #2563eb !important;
      color: #ffffff !important;
      border-color: #1d4ed8 !important;
      box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1);
    }}
    .explanation-box {{
      animation: fadeIn 0.25s ease-out;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(-4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    /* Fallback thuần nếu offline không nạp được Tailwind */
    .card-box {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
      margin-bottom: 24px;
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col">

  <!-- Header Sticky -->
  <header class="bg-white border-b border-slate-200 sticky top-0 z-50 shadow-sm">
    <div class="max-w-6xl mx-auto px-4 py-3 flex flex-col md:flex-row items-center justify-between gap-3">
      <div>
        <div class="flex items-center gap-2">
          <span class="bg-blue-600 text-white text-[11px] font-bold px-2.5 py-0.5 rounded-full uppercase tracking-wider">AI/ML Test Bank</span>
          <h1 class="text-base sm:text-lg font-extrabold text-slate-900 tracking-tight">Ứng Dụng Ôn Tập AI/ML Chuẩn Hóa (68 Câu Độc Nhất)</h1>
        </div>
        <p class="text-xs text-slate-500 mt-0.5">47 Trắc nghiệm đơn • 5 Nhiều đáp án • 16 Tự luận & Tình huống lớn • 100% Lời giải chuyên sâu</p>
      </div>

      <!-- Mode Selector & Stats -->
      <div class="flex flex-wrap items-center gap-2.5">
        <!-- Chuyển đổi chế độ -->
        <div class="bg-slate-100 p-1 rounded-xl flex items-center text-xs font-semibold">
          <button id="modeQuizBtn" onclick="setMode('quiz')" class="px-3 py-1.5 rounded-lg bg-white shadow-sm text-blue-600 font-bold transition">🎯 Luyện Thi (Ẩn đáp án)</button>
          <button id="modeStudyBtn" onclick="setMode('study')" class="px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 transition">📖 Học Tập (Hiện sẵn)</button>
        </div>

        <!-- Bộ đếm điểm thời gian thực -->
        <div class="bg-blue-50/80 border border-blue-200 px-3 py-1.5 rounded-xl flex items-center gap-3 text-xs">
          <div><span class="text-slate-500 font-medium">Đúng:</span> <strong id="scoreCorrect" class="text-emerald-600 font-bold text-sm">0</strong></div>
          <div><span class="text-slate-500 font-medium">Sai:</span> <strong id="scoreWrong" class="text-rose-600 font-bold text-sm">0</strong></div>
          <div><span class="text-slate-500 font-medium">Tiến độ:</span> <strong id="progressPercent" class="text-blue-600 font-bold text-sm">0%</strong></div>
        </div>
      </div>
    </div>

    <!-- Filters & Search Bar -->
    <div class="bg-slate-50 border-t border-slate-200 px-4 py-2.5">
      <div class="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-between gap-3">
        <!-- 7 Nút Bộ Lọc Chuẩn Hóa -->
        <div class="flex flex-wrap items-center gap-1.5 text-xs font-medium w-full md:w-auto">
          <button onclick="setFilter('all')" id="filter-all" class="filter-btn active px-3 py-1.5 rounded-full bg-blue-600 text-white font-semibold transition" data-filter="all">Tất cả (68)</button>
          <button onclick="setFilter('single')" id="filter-single" class="filter-btn px-3 py-1.5 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-slate-100 transition" data-filter="single">Trắc nghiệm đơn (47)</button>
          <button onclick="setFilter('multi')" id="filter-multi" class="filter-btn px-3 py-1.5 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-slate-100 transition" data-filter="multi">Nhiều đáp án (5)</button>
          <button onclick="setFilter('essay')" id="filter-essay" class="filter-btn px-3 py-1.5 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-slate-100 transition" data-filter="essay">Tự luận & Tình huống (16)</button>
          
          <span class="text-slate-300 hidden sm:inline">|</span>
          
          <!-- Chuyên đề 3 Tracks -->
          <button onclick="setFilter('track1')" id="filter-track1" class="filter-btn px-3 py-1.5 rounded-full bg-blue-50 border border-blue-300 text-blue-800 hover:bg-blue-100 font-semibold transition" data-filter="track1">🤖 Track 1: Applications (25)</button>
          <button onclick="setFilter('track2')" id="filter-track2" class="filter-btn px-3 py-1.5 rounded-full bg-amber-50 border border-amber-300 text-amber-800 hover:bg-amber-100 font-semibold transition" data-filter="track2">🛠️ Track 2: Infrastructure (34)</button>
          <button onclick="setFilter('track3')" id="filter-track3" class="filter-btn px-3 py-1.5 rounded-full bg-emerald-50 border border-emerald-300 text-emerald-800 hover:bg-emerald-100 font-semibold transition" data-filter="track3">📈 Track 3: Product (22)</button>
        </div>

        <!-- Ô Tìm Kiếm Real-time -->
        <div class="relative w-full md:w-72 flex-shrink-0">
          <input type="text" id="searchInput" oninput="handleSearch()" placeholder="Tìm kiếm (ReAct, ROI, RAGAS, P99...)" class="w-full pl-8 pr-3 py-1.5 text-xs bg-white border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition shadow-sm">
          <svg class="w-4 h-4 text-slate-400 absolute left-2.5 top-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>
      </div>
    </div>
  </header>

  <!-- Container Nội Dung Chính -->
  <main class="max-w-4xl mx-auto px-4 py-8 flex-1 w-full">
    <!-- Tiêu đề trạng thái hiển thị -->
    <div class="mb-4 flex items-center justify-between text-xs text-slate-500">
      <div id="filterStatusText">Đang hiển thị: <strong class="text-slate-800 font-semibold">Tất cả 68 câu</strong></div>
      <div id="statsSummaryText">Chưa trả lời câu nào</div>
    </div>

    <!-- Danh sách câu hỏi -->
    <div id="questionsContainer" class="space-y-6"></div>

    <!-- Trạng thái trống (Empty State) -->
    <div id="emptyState" class="hidden text-center py-16 bg-white rounded-2xl border border-slate-200 p-8 shadow-sm">
      <div class="text-4xl mb-3">🔍</div>
      <h3 class="text-base font-semibold text-slate-700">Không tìm thấy câu hỏi nào phù hợp</h3>
      <p class="text-xs text-slate-500 mt-1">Hãy thử tìm từ khóa khác hoặc xóa bộ lọc để hiển thị toàn bộ 68 câu.</p>
      <button onclick="resetAllFilters()" class="mt-4 px-4 py-2 bg-blue-600 text-white text-xs font-semibold rounded-lg hover:bg-blue-700 transition">Đặt lại bộ lọc</button>
    </div>
  </main>

  <!-- Nút Lên Đầu Trang -->
  <div class="fixed bottom-6 right-6 flex flex-col gap-2 z-40">
    <button onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }})" class="p-3 bg-white border border-slate-200 text-slate-600 rounded-full shadow-lg hover:bg-slate-50 transition" title="Lên đầu trang">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg>
    </button>
  </div>

  <!-- Footer -->
  <footer class="bg-white border-t border-slate-200 py-6 text-center text-xs text-slate-500">
    <div class="max-w-4xl mx-auto px-4">
      <p class="font-semibold text-slate-700">Bộ Đề Thi AI/ML & Agentic Systems Chuẩn Hóa 2026</p>
      <p class="mt-1 text-slate-400">Hệ thống 68 câu độc nhất vô nhị • 0 Trùng lặp • 0 Fallback • Tích hợp Offline 100%</p>
    </div>
  </footer>

  <!-- DỮ LIỆU & LOGIC JAVASCRIPT -->
  <script>
    // Nhúng trực tiếp 68 câu sạch 100% từ questions_db.json (Chạy offline không lo CORS)
    const questions = {questions_json_str};

    let currentFilter = 'all';
    let currentMode = 'quiz'; // 'quiz' (Luyện thi - ẩn đáp án) hoặc 'study' (Học tập - hiện sẵn)
    let searchQuery = '';
    
    // Lưu trữ trạng thái trả lời của người dùng: {{ [qid]: {{ selected: [...], checked: bool, isCorrect: bool }} }}
    let userAnswers = {{}};

    // Khởi tạo ứng dụng
    function init() {{
      updateStats();
      renderQuestions();
    }}

    function setMode(mode) {{
      currentMode = mode;
      const quizBtn = document.getElementById('modeQuizBtn');
      const studyBtn = document.getElementById('modeStudyBtn');

      if (mode === 'quiz') {{
        quizBtn.className = 'px-3 py-1.5 rounded-lg bg-white shadow-sm text-blue-600 font-bold transition';
        studyBtn.className = 'px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 transition';
      }} else {{
        studyBtn.className = 'px-3 py-1.5 rounded-lg bg-white shadow-sm text-blue-600 font-bold transition';
        quizBtn.className = 'px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 transition';
      }}

      renderQuestions();
    }}

    function setFilter(filter) {{
      currentFilter = filter;
      document.querySelectorAll('.filter-btn').forEach(btn => {{
        if (btn.dataset.filter === filter) {{
          btn.classList.add('active');
        }} else {{
          btn.classList.remove('active');
        }}
      }});
      
      updateFilterStatusText();
      renderQuestions();
    }}

    function updateFilterStatusText() {{
      const filterNames = {{
        'all': 'Tất cả 68 câu độc nhất',
        'single': '47 câu Trắc nghiệm đơn',
        'multi': '5 câu Trắc nghiệm nhiều đáp án',
        'essay': '16 bài Tự luận & Tình huống lớn',
        'track1': 'Track 1: AI Applications (25 câu)',
        'track2': 'Track 2: AI Infrastructure (34 câu)',
        'track3': 'Track 3: AI Product (22 câu)'
      }};
      document.getElementById('filterStatusText').innerHTML = `Đang hiển thị: <strong class="text-slate-800 font-semibold">${{filterNames[currentFilter] || currentFilter}}</strong>`;
    }}

    function handleSearch() {{
      searchQuery = document.getElementById('searchInput').value.toLowerCase().trim();
      renderQuestions();
    }}

    function resetAllFilters() {{
      document.getElementById('searchInput').value = '';
      searchQuery = '';
      setFilter('all');
    }}

    // Lọc danh sách câu hỏi theo filter và search
    function getFilteredQuestions() {{
      return questions.filter(q => {{
        if (currentFilter === 'single' && q.type !== 'single_choice') return false;
        if (currentFilter === 'multi' && q.type !== 'multi_choice') return false;
        if (currentFilter === 'essay' && q.type !== 'tu_luan') return false;
        if (currentFilter === 'track1' && !q.is_app) return false;
        if (currentFilter === 'track2' && !q.is_infra) return false;
        if (currentFilter === 'track3' && !q.is_prod) return false;

        if (searchQuery) {{
          const choicesText = q.choices ? q.choices.join(' ') : '';
          const fullText = ((q.question || '') + ' ' + (q.explanation || '') + ' ' + (q.title || '') + ' ' + choicesText).toLowerCase();
          if (!fullText.includes(searchQuery)) return false;
        }}

        return true;
      }});
    }}

    // Render danh sách câu hỏi
    function renderQuestions() {{
      const container = document.getElementById('questionsContainer');
      const emptyState = document.getElementById('emptyState');
      const filtered = getFilteredQuestions();

      if (filtered.length === 0) {{
        container.innerHTML = '';
        emptyState.classList.remove('hidden');
        return;
      }}

      emptyState.classList.add('hidden');
      container.innerHTML = filtered.map((q, index) => buildCardHtml(q, index + 1)).join('');
    }}

    // Định dạng Markdown an toàn chống XSS (§5 Frontend Standard)
    function renderMarkdown(text) {{
      if (!text) return '';
      let html = text
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');

      // Ký hiệu toán học Unicode
      html = html.replace(/\\$\\ge\\$/g, '≥').replace(/\\$\\le\\$/g, '≤');

      // Khối code pre/code
      html = html.replace(/```([a-zA-Z0-9_-]*)\\n([\\s\\S]*?)```/g, function(match, lang, code) {{
        const langLabel = lang ? `<div class="text-[10px] text-slate-400 font-mono mb-1.5 uppercase tracking-wider border-b border-slate-700 pb-1">${{lang}}</div>` : '';
        return `<pre class="bg-slate-900 text-slate-100 p-3.5 rounded-xl text-xs font-mono overflow-x-auto my-2.5 border border-slate-800 leading-relaxed shadow-inner">${{langLabel}}<code>${{code.trim()}}</code></pre>`;
      }});

      // Code inline
      html = html.replace(/`([^`]+)`/g, '<code class="px-1.5 py-0.5 rounded bg-slate-200/80 text-slate-800 font-mono text-[11px] font-semibold">$1</code>');

      // In đậm
      html = html.replace(/\\*\\*([^*]+)\\*\\*/g, '<strong class="font-bold text-slate-900">$1</strong>');

      // Dấu gạch đầu dòng bullet
      html = html.replace(/\\n\\s*[-+]\\s+(.+)/g, '<div class="flex items-start gap-2 my-1"><span class="text-blue-500 font-bold">•</span><span class="flex-1">$1</span></div>');

      // Xuống dòng
      html = html.replace(/\\n\\n/g, '<div class="h-2"></div>');
      html = html.replace(/\\n/g, '<br>');

      return html;
    }}

    // Xây dựng giao diện cho từng thẻ câu hỏi (Card)
    function buildCardHtml(q, displayIndex) {{
      const state = userAnswers[q.id] || {{ selected: [], checked: false }};
      const isAnswered = state.checked || currentMode === 'study';

      // Badges phân loại
      let typeBadge = '';
      if (q.type === 'single_choice') {{
        typeBadge = '<span class="px-2 py-0.5 rounded text-[11px] font-semibold bg-blue-100 text-blue-800">Trắc nghiệm đơn</span>';
      }} else if (q.type === 'multi_choice') {{
        typeBadge = '<span class="px-2 py-0.5 rounded text-[11px] font-semibold bg-indigo-100 text-indigo-800">Nhiều đáp án</span>';
      }} else {{
        typeBadge = '<span class="px-2 py-0.5 rounded text-[11px] font-semibold bg-purple-100 text-purple-800">Tự luận / Tình huống</span>';
      }}

      let trackBadges = '';
      if (q.is_app) trackBadges += '<span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-blue-50 text-blue-700 border border-blue-200">🤖 Track 1: App</span> ';
      if (q.is_infra) trackBadges += '<span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-amber-50 text-amber-700 border border-amber-200">🛠️ Track 2: Infra</span> ';
      if (q.is_prod) trackBadges += '<span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200">📈 Track 3: Product</span> ';

      // Render nội dung tương tác
      let choicesHtml = '';

      if (q.type === 'single_choice' && q.choices && q.choices.length > 0) {{
        // TRẮC NGHIỆM ĐƠN (1 ĐÁP ÁN ĐÚNG)
        choicesHtml = `
          <div class="space-y-2 mt-4">
            ${{q.choices.map(c => {{
              const letter = c.trim()[0];
              const isUserChoice = state.selected.includes(letter);
              
              // Xử lý đúng sai linh hoạt (Hỗ trợ Câu 5 trắc nghiệm nhận cả A, B, C)
              const isChoiceCorrect = Array.isArray(q.correct) ? q.correct.includes(letter) : (letter === q.correct);
              
              let btnClass = 'choice-btn w-full text-left p-3 rounded-xl border border-slate-200 text-sm flex items-start gap-3 bg-white ';
              let badgeHtml = `<span class="w-6 h-6 flex items-center justify-center rounded-full bg-slate-100 text-xs font-bold text-slate-600 flex-shrink-0">${{letter}}</span>`;

              if (currentMode === 'study') {{
                if (isChoiceCorrect) {{
                  btnClass += 'correct-choice';
                  badgeHtml = '<span class="w-6 h-6 flex items-center justify-center rounded-full bg-emerald-600 text-white text-xs font-bold flex-shrink-0">✓</span>';
                }}
              }} else if (state.checked) {{
                btnClass += 'locked ';
                if (isChoiceCorrect) {{
                  btnClass += 'correct-choice';
                  badgeHtml = '<span class="w-6 h-6 flex items-center justify-center rounded-full bg-emerald-600 text-white text-xs font-bold flex-shrink-0">✓</span>';
                }} else if (isUserChoice) {{
                  btnClass += 'wrong-choice';
                  badgeHtml = '<span class="w-6 h-6 flex items-center justify-center rounded-full bg-rose-600 text-white text-xs font-bold flex-shrink-0">✕</span>';
                }}
              }} else if (isUserChoice) {{
                btnClass += 'border-blue-500 bg-blue-50 text-blue-900 font-medium';
              }}

              return `
                <button onclick="selectSingleChoice(${{q.id}}, '${{letter}}')" class="${{btnClass}}" ${{state.checked || currentMode === 'study' ? 'disabled' : ''}}>
                  ${{badgeHtml}}
                  <span class="flex-1 text-xs sm:text-sm text-slate-800">${{c.substring(2).trim()}}</span>
                </button>
              `;
            }}).join('')}}
          </div>
        `;
      }} else if (q.type === 'multi_choice' && q.choices && q.choices.length > 0) {{
        // TRẮC NGHIỆM NHIỀU ĐÁP ÁN (MULTI-SELECT)
        choicesHtml = `
          <div class="space-y-2 mt-4">
            <div class="text-[11px] text-slate-500 font-medium italic">💡 Chọn tất cả các phương án đúng, sau đó bấm 'Kiểm tra đáp án'.</div>
            ${{q.choices.map(c => {{
              const letter = c.trim()[0];
              const isUserChoice = state.selected.includes(letter);
              const isOptionCorrect = Array.isArray(q.correct) ? q.correct.includes(letter) : (letter === q.correct);

              let itemClass = 'choice-btn w-full text-left p-3 rounded-xl border border-slate-200 text-sm flex items-start gap-3 bg-white ';
              if (currentMode === 'study') {{
                if (isOptionCorrect) itemClass += 'correct-choice';
              }} else if (state.checked) {{
                itemClass += 'locked ';
                if (isOptionCorrect) itemClass += 'correct-choice';
                else if (isUserChoice && !isOptionCorrect) itemClass += 'wrong-choice';
              }} else if (isUserChoice) {{
                itemClass += 'border-blue-500 bg-blue-50';
              }}

              return `
                <div onclick="toggleMultiChoice(${{q.id}}, '${{letter}}')" class="${{itemClass}} cursor-pointer">
                  <input type="checkbox" ${{isUserChoice ? 'checked' : ''}} ${{state.checked || currentMode === 'study' ? 'disabled' : ''}} class="mt-1 h-4 w-4 text-blue-600 rounded pointer-events-none">
                  <span class="flex-1 text-xs sm:text-sm text-slate-800">${{c}}</span>
                </div>
              `;
            }}).join('')}}
          </div>
          ${{currentMode === 'quiz' && !state.checked ? `
            <button onclick="checkMultiChoice(${{q.id}})" class="mt-3 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold rounded-lg transition shadow-sm">
              Kiểm tra đáp án
            </button>
          ` : ''}}
        `;
      }} else {{
        // TỰ LUẬN & BÀI TOÁN TÌNH HUỐNG LỚN
        choicesHtml = `
          <div class="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs text-slate-500 font-semibold">📝 Bài toán tự luận & tình huống thực chiến</span>
              <button onclick="toggleEssayAnswer(${{q.id}})" class="px-3.5 py-1.5 bg-slate-900 hover:bg-slate-800 text-white text-xs font-semibold rounded-lg transition shadow-sm flex items-center gap-1.5">
                ${{state.checked || currentMode === 'study' ? '🙈 Ẩn lời giải chi tiết' : '👁️ Xem lời giải chi tiết'}}
              </button>
            </div>
            ${{currentMode === 'quiz' && !state.checked ? `
              <textarea placeholder="Ghi chú câu trả lời hoặc phác thảo ý tưởng của bạn trước khi đối chiếu đáp án..." rows="2" class="w-full p-2.5 text-xs bg-white border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none transition"></textarea>
            ` : ''}}
          </div>
        `;
      }}

      // Hộp thoại giải thích chuyên sâu (Bung ra khi bấm chọn hoặc ở chế độ học tập)
      let explanationHtml = '';
      if (currentMode === 'study' || state.checked) {{
        let correctDisplay = Array.isArray(q.correct) ? q.correct.join(', ') : q.correct;
        explanationHtml = `
          <div class="explanation-box mt-4 p-4 rounded-xl border border-emerald-200 bg-emerald-50/70 text-slate-800 text-xs leading-relaxed space-y-2">
            <div class="flex flex-wrap items-center gap-2 font-bold text-emerald-900 text-sm">
              <span>🎯 Đáp án chuẩn:</span>
              <span class="bg-emerald-600 text-white px-2.5 py-0.5 rounded text-xs tracking-wide">${{correctDisplay}}</span>
            </div>
            <div class="pt-2 border-t border-emerald-200/60 text-slate-700">
              <div class="font-bold text-slate-900 mb-1 flex items-center gap-1.5 text-xs">
                <span>💡 Phân tích & Lời giải chuyên sâu:</span>
              </div>
              <div class="mt-1 leading-relaxed">${{renderMarkdown(q.explanation)}}</div>
            </div>
          </div>
        `;
      }}

      return `
        <article class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm hover:shadow-md transition">
          <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3">
            <div class="flex flex-wrap items-center gap-2">
              <span class="font-extrabold text-sm text-blue-600">Câu ${{q.id}}</span>
              ${{typeBadge}}
              ${{trackBadges}}
            </div>
            ${{q.title ? `<span class="text-xs font-bold text-slate-500">${{q.title}}</span>` : ''}}
          </div>

          <div class="mt-3.5">
            <h3 class="text-sm sm:text-base font-semibold text-slate-900 leading-snug whitespace-pre-line">${{q.question}}</h3>
          </div>

          ${{choicesHtml}}
          ${{explanationHtml}}
        </article>
      `;
    }}

    // Xử lý khi click chọn Trắc nghiệm đơn
    function selectSingleChoice(questionId, choiceLetter) {{
      if (currentMode === 'study') return;
      const state = userAnswers[questionId] || {{ selected: [], checked: false }};
      if (state.checked) return;

      const q = questions.find(item => item.id === questionId);
      
      // Kiểm tra đúng/sai (Đặc biệt: Câu 5 chấp nhận cả 'A', 'B', 'C')
      const isCorrect = Array.isArray(q.correct) ? q.correct.includes(choiceLetter) : (choiceLetter === q.correct);

      userAnswers[questionId] = {{
        selected: [choiceLetter],
        checked: true,
        isCorrect: isCorrect
      }};

      updateStats();
      renderQuestions();
    }}

    // Xử lý chọn/bỏ chọn checkbox Nhiều đáp án
    function toggleMultiChoice(questionId, choiceLetter) {{
      if (currentMode === 'study') return;
      const state = userAnswers[questionId] || {{ selected: [], checked: false }};
      if (state.checked) return;

      const idx = state.selected.indexOf(choiceLetter);
      if (idx > -1) {{
        state.selected.splice(idx, 1);
      }} else {{
        state.selected.push(choiceLetter);
      }}
      userAnswers[questionId] = state;
      renderQuestions();
    }}

    // Kiểm tra kết quả Trắc nghiệm nhiều đáp án
    function checkMultiChoice(questionId) {{
      const state = userAnswers[questionId] || {{ selected: [], checked: false }};
      const q = questions.find(item => item.id === questionId);

      const correctList = Array.isArray(q.correct) ? q.correct : [q.correct];
      const isCorrect = state.selected.length === correctList.length && state.selected.every(c => correctList.includes(c));

      userAnswers[questionId] = {{
        selected: state.selected,
        checked: true,
        isCorrect: isCorrect
      }};

      updateStats();
      renderQuestions();
    }}

    // Đóng/Mở xem lời giải Tự luận
    function toggleEssayAnswer(questionId) {{
      const state = userAnswers[questionId] || {{ selected: [], checked: false, isCorrect: true }};
      state.checked = !state.checked;
      state.isCorrect = true; // Xem tự luận được tính vào tiến độ hoàn thành
      userAnswers[questionId] = state;
      updateStats();
      renderQuestions();
    }}

    // Cập nhật bộ đếm điểm và tiến độ real-time
    function updateStats() {{
      const answeredList = Object.values(userAnswers).filter(a => a.checked);
      const correctCount = answeredList.filter(a => a.isCorrect).length;
      const wrongCount = answeredList.filter(a => a.isCorrect === false).length;
      const progress = Math.round((answeredList.length / questions.length) * 100);

      document.getElementById('scoreCorrect').innerText = correctCount;
      document.getElementById('scoreWrong').innerText = wrongCount;
      document.getElementById('progressPercent').innerText = progress + '%';
      
      const summaryElem = document.getElementById('statsSummaryText');
      if (answeredList.length === 0) {{
        summaryElem.innerText = 'Chưa trả lời câu nào';
      }} else {{
        summaryElem.innerHTML = `Đã làm: <strong class="text-slate-800 font-semibold">${{answeredList.length}}/${{questions.length}} câu</strong> (${{progress}}%)`;
      }}
    }}

    // Khởi chạy khi tài liệu tải xong
    window.onload = init;
  </script>
</body>
</html>
"""
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ XUẤT THÀNH CÔNG: {HTML_PATH} ({os.path.getsize(HTML_PATH):,} bytes).")

if __name__ == "__main__":
    generate_html()
