#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_mobile_polish.py
Thực thi tối ưu hóa toàn diện giao diện di động cho index.html:
1. CSS Reset & Chống tràn ngang: html, body overflow-x: hidden, max-width: 100vw, box-sizing.
2. Chống iOS Safari Auto-Zoom: media query font-size 16px, searchInput + textarea font-size 16px.
3. Card padding: p-3.5 sm:p-5; nút câu con: flex-wrap gap-1.5; toolbar mở/thu gọn responsive.
4. Filter bar 7 nút: overflow-x-auto, whitespace-nowrap, min-h-[36px] touch target.
5. Canvas vẽ tay: responsive 100% width, touch-action: none.
6. Smart back-to-top: bottom-4 right-4, 38-40px, semi-transparent backdrop blur.
"""

import os
import re

INDEX_PATH = r"C:\Users\Admin\Desktop\học tập\Bo_De_AI_ML_Da_Giai\index.html"

def polish_index_html():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    orig_len = len(content)
    print(f"Đọc index.html: {orig_len} ký tự, {content.count(chr(10))} dòng")

    # 1. VIEWPORT META TAG
    # Đảm bảo viewport không bị lock scale cứng ngắc và thân thiện với mobile
    old_viewport = re.search(r'<meta\s+name="viewport"\s+content="[^"]+">', content)
    if old_viewport:
        content = content.replace(
            old_viewport.group(0),
            '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">'
        )
        print("✓ Cập nhật Viewport Meta Tag (maximum-scale=5.0)")

    # 2. GLOBAL CSS IN <style>
    # Thêm quy tắc CSS chống tràn ngang, chống iOS zoom, break-word cho code/table
    target_style = """  <style>
    /* CSS Tối Ưu Toàn Diện Cho Điện Thoại & Desktop (Mobile-First Polish) */
    *, *::before, *::after {
      box-sizing: border-box;
    }
    html, body {
      overflow-x: hidden;
      max-width: 100vw;
      width: 100%;
    }
    /* Chống iOS Safari tự động phóng to màn hình khi chạm vào ô nhập dữ liệu / nháp */
    @media screen and (max-width: 768px) {
      input[type="text"],
      input[type="search"],
      textarea,
      select {
        font-size: 16px !important;
      }
    }
    /* Đảm bảo bảng, khối code và công thức toán không làm vỡ khung card */
    pre, code, table {
      max-width: 100%;
      word-break: break-word;
    }
    pre {
      overflow-x: auto;
      white-space: pre-wrap;
      word-wrap: break-word;
    }
    canvas {
      touch-action: none;
      max-width: 100%;
    }
    /* Tiện ích ẩn thanh cuộn nhưng vẫn cuộn ngang mượt mà */
    .scrollbar-none {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }
    .scrollbar-none::-webkit-scrollbar {
      display: none;
    }
    body {"""
    
    content = re.sub(
        r'<style>\s*/\*\s*CSS Tối Ưu Cho Cả Online & Offline\s*\*/\s*body\s*\{',
        target_style,
        content
    )
    print("✓ Cập nhật Global CSS trong <style>")

    # 3. HEADER MINI BAR
    # Tinh giản trên mobile: title co giãn, mini score gọn, nút toggle bảng hiển thị biểu tượng súc tích
    old_mini_header = """    <div class="max-w-6xl mx-auto px-3.5 py-2 flex items-center justify-between gap-2">
      <div class="flex items-center gap-2 overflow-hidden cursor-pointer" onclick="toggleTopBoard()">
        <span class="bg-blue-600 text-white text-[10px] font-extrabold px-2 py-0.5 rounded-full uppercase tracking-wider shrink-0">AI/ML</span>
        <h1 class="text-xs sm:text-sm font-extrabold text-slate-900 truncate">Ôn Tập AI/ML (68 Câu Độc Nhất)</h1>
      </div>

      <div class="flex items-center gap-2 shrink-0">
        <!-- Tóm tắt điểm số mini trên mobile -->
        <div class="text-[11px] font-semibold text-slate-700 bg-slate-100 px-2.5 py-1 rounded-lg flex items-center gap-1.5 border border-slate-200">
          <span class="text-emerald-600 font-bold" id="miniScoreCorrect">0 Đúng</span>
          <span class="text-slate-300">•</span>
          <span class="text-rose-600 font-bold" id="miniScoreWrong">0 Sai</span>
          <span class="text-slate-300">•</span>
          <span class="text-blue-600 font-bold" id="miniProgress">0%</span>
        </div>

        <!-- Nút Thu Gọn / Mở Rộng Bảng Điều Khiển -->
        <button id="toggleTopBoardBtn" onclick="toggleTopBoard()" class="px-2.5 py-1 rounded-lg bg-blue-50 hover:bg-blue-100 active:bg-blue-200 text-blue-700 border border-blue-300 text-xs font-extrabold transition flex items-center gap-1 shadow-xs cursor-pointer" title="Thu gọn hoặc mở rộng bảng điều khiển">
          <span id="toggleTopBoardText">Thu gọn bảng</span>
          <span id="toggleTopBoardIcon" class="text-[10px]">▲</span>
        </button>
      </div>
    </div>"""

    new_mini_header = """    <div class="max-w-6xl mx-auto px-3 py-1.5 sm:px-3.5 sm:py-2 flex items-center justify-between gap-1.5 sm:gap-2">
      <div class="flex items-center gap-1.5 sm:gap-2 overflow-hidden cursor-pointer" onclick="toggleTopBoard()">
        <span class="bg-blue-600 text-white text-[10px] font-extrabold px-1.5 sm:px-2 py-0.5 rounded-full uppercase tracking-wider shrink-0">AI/ML</span>
        <h1 class="text-xs sm:text-sm font-extrabold text-slate-900 truncate">Ôn Tập AI/ML (68 Câu)</h1>
      </div>

      <div class="flex items-center gap-1.5 sm:gap-2 shrink-0">
        <!-- Tóm tắt điểm số mini trên mobile -->
        <div class="text-[10px] sm:text-[11px] font-semibold text-slate-700 bg-slate-100 px-2 sm:px-2.5 py-1 rounded-lg flex items-center gap-1 sm:gap-1.5 border border-slate-200">
          <span class="text-emerald-600 font-bold" id="miniScoreCorrect">0 Đúng</span>
          <span class="text-slate-300">•</span>
          <span class="text-rose-600 font-bold" id="miniScoreWrong">0 Sai</span>
          <span class="text-slate-300">•</span>
          <span class="text-blue-600 font-bold" id="miniProgress">0%</span>
        </div>

        <!-- Nút Thu Gọn / Mở Rộng Bảng Điều Khiển -->
        <button id="toggleTopBoardBtn" onclick="toggleTopBoard()" class="px-2 py-1 rounded-lg bg-blue-50 hover:bg-blue-100 active:bg-blue-200 text-blue-700 border border-blue-300 text-xs font-extrabold transition flex items-center gap-1 shadow-xs cursor-pointer shrink-0" title="Thu gọn hoặc mở rộng bảng điều khiển">
          <span id="toggleTopBoardText" class="hidden sm:inline">Thu gọn bảng</span>
          <span id="toggleTopBoardIcon" class="text-[10px]">▲</span>
        </button>
      </div>
    </div>"""

    if old_mini_header in content:
        content = content.replace(old_mini_header, new_mini_header)
        print("✓ Tinh gọn Sticky Mini Header trên mobile")

    # 4. FILTER BAR 7 BUTTONS & SEARCH INPUT
    # Chuyển 7 nút sang dạng cuộn ngang mượt mà (overflow-x-auto, min-h-[36px]), search input font 16px chống zoom
    old_filter_section = """      <!-- Filters & Search Bar -->
      <div class="bg-slate-100/70 border-t border-slate-200/80 px-4 py-2.5">
        <div class="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-between gap-3">
          <!-- 7 Nút Bộ Lọc Chuẩn Hóa -->
          <div class="flex flex-wrap items-center gap-1.5 text-xs font-medium w-full md:w-auto">
            <button onclick="setFilter('all')" id="filter-all" class="filter-btn active px-3 py-1.5 rounded-full bg-blue-600 text-white font-semibold transition cursor-pointer" data-filter="all">Tất cả (68)</button>
            <button onclick="setFilter('single')" id="filter-single" class="filter-btn px-3 py-1.5 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-slate-100 transition cursor-pointer" data-filter="single">Trắc nghiệm đơn (47)</button>
            <button onclick="setFilter('multi')" id="filter-multi" class="filter-btn px-3 py-1.5 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-slate-100 transition cursor-pointer" data-filter="multi">Nhiều đáp án (5)</button>
            <button onclick="setFilter('essay')" id="filter-essay" class="filter-btn px-3 py-1.5 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-slate-100 transition cursor-pointer" data-filter="essay">Tự luận & Tình huống (16)</button>
            
            <span class="text-slate-300 hidden sm:inline">|</span>
            
            <!-- Chuyên đề 3 Tracks -->
            <button onclick="setFilter('track1')" id="filter-track1" class="filter-btn px-3 py-1.5 rounded-full bg-blue-50 border border-blue-300 text-blue-800 hover:bg-blue-100 font-semibold transition cursor-pointer" data-filter="track1">🤖 Track 1: Applications (25)</button>
            <button onclick="setFilter('track2')" id="filter-track2" class="filter-btn px-3 py-1.5 rounded-full bg-amber-50 border border-amber-300 text-amber-800 hover:bg-amber-100 font-semibold transition cursor-pointer" data-filter="track2">🛠️ Track 2: Infrastructure (34)</button>
            <button onclick="setFilter('track3')" id="filter-track3" class="filter-btn px-3 py-1.5 rounded-full bg-emerald-50 border border-emerald-300 text-emerald-800 hover:bg-emerald-100 font-semibold transition cursor-pointer" data-filter="track3">📈 Track 3: Product (22)</button>
          </div>

          <!-- Ô Tìm Kiếm Real-time -->
          <div class="relative w-full md:w-72 flex-shrink-0">
            <input type="text" id="searchInput" oninput="handleSearch()" placeholder="Tìm kiếm (ReAct, ROI, RAGAS, P99...)" class="w-full pl-8 pr-3 py-1.5 text-xs bg-white border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition shadow-xs">
            <svg class="w-4 h-4 text-slate-400 absolute left-2.5 top-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>
        </div>
      </div>"""

    new_filter_section = """      <!-- Filters & Search Bar -->
      <div class="bg-slate-100/70 border-t border-slate-200/80 px-3 py-2 sm:px-4 sm:py-2.5">
        <div class="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-between gap-2.5 sm:gap-3">
          <!-- 7 Nút Bộ Lọc Chuẩn Hóa (Hỗ trợ cuộn ngang mượt mà phong cách Native App) -->
          <div class="flex items-center gap-1.5 text-xs font-medium w-full md:w-auto overflow-x-auto whitespace-nowrap scrollbar-none pb-1 sm:pb-0 md:flex-wrap md:whitespace-normal">
            <button onclick="setFilter('all')" id="filter-all" class="filter-btn active shrink-0 min-h-[36px] px-3.5 py-1.5 rounded-full bg-blue-600 text-white font-semibold transition cursor-pointer flex items-center justify-center" data-filter="all">Tất cả (68)</button>
            <button onclick="setFilter('single')" id="filter-single" class="filter-btn shrink-0 min-h-[36px] px-3.5 py-1.5 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-slate-100 transition cursor-pointer flex items-center justify-center" data-filter="single">Trắc nghiệm đơn (47)</button>
            <button onclick="setFilter('multi')" id="filter-multi" class="filter-btn shrink-0 min-h-[36px] px-3.5 py-1.5 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-slate-100 transition cursor-pointer flex items-center justify-center" data-filter="multi">Nhiều đáp án (5)</button>
            <button onclick="setFilter('essay')" id="filter-essay" class="filter-btn shrink-0 min-h-[36px] px-3.5 py-1.5 rounded-full bg-white border border-slate-300 text-slate-700 hover:bg-slate-100 transition cursor-pointer flex items-center justify-center" data-filter="essay">Tự luận & Tình huống (16)</button>
            
            <span class="text-slate-300 hidden md:inline">|</span>
            
            <!-- Chuyên đề 3 Tracks -->
            <button onclick="setFilter('track1')" id="filter-track1" class="filter-btn shrink-0 min-h-[36px] px-3.5 py-1.5 rounded-full bg-blue-50 border border-blue-300 text-blue-800 hover:bg-blue-100 font-semibold transition cursor-pointer flex items-center justify-center" data-filter="track1">🤖 Track 1: Applications (25)</button>
            <button onclick="setFilter('track2')" id="filter-track2" class="filter-btn shrink-0 min-h-[36px] px-3.5 py-1.5 rounded-full bg-amber-50 border border-amber-300 text-amber-800 hover:bg-amber-100 font-semibold transition cursor-pointer flex items-center justify-center" data-filter="track2">🛠️ Track 2: Infrastructure (34)</button>
            <button onclick="setFilter('track3')" id="filter-track3" class="filter-btn shrink-0 min-h-[36px] px-3.5 py-1.5 rounded-full bg-emerald-50 border border-emerald-300 text-emerald-800 hover:bg-emerald-100 font-semibold transition cursor-pointer flex items-center justify-center" data-filter="track3">📈 Track 3: Product (22)</button>
          </div>

          <!-- Ô Tìm Kiếm Real-time (font-size 16px chống iOS auto-zoom) -->
          <div class="relative w-full md:w-72 flex-shrink-0">
            <input type="text" id="searchInput" oninput="handleSearch()" placeholder="Tìm kiếm (ReAct, ROI, RAGAS, P99...)" class="w-full pl-8 pr-3 py-1.5 text-[16px] sm:text-xs bg-white border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition shadow-xs">
            <svg class="w-4 h-4 text-slate-400 absolute left-2.5 top-2.5 sm:top-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>
        </div>
      </div>"""

    if old_filter_section in content:
        content = content.replace(old_filter_section, new_filter_section)
        print("✓ Tối ưu Thanh bộ lọc 7 nút (cuộn ngang, touch target >= 36px)")

    # 5. MAIN CONTAINER PADDING
    content = content.replace(
        '<main class="max-w-4xl mx-auto px-4 py-8 flex-1 w-full">',
        '<main class="max-w-4xl mx-auto px-3 sm:px-4 py-4 sm:py-8 flex-1 w-full overflow-hidden sm:overflow-visible">'
    )
    print("✓ Cập nhật padding thẻ <main>")

    # 6. SMART BACK TO TOP BUTTON
    old_back_to_top = """  <!-- Nút Lên Đầu Trang Nổi Thông Minh Cho Mobile & PC (Tự động ẩn/hiện, bo tròn có chữ Về đầu) -->
  <div id="backToTopContainer" class="fixed bottom-6 right-5 z-40 transition-all duration-300 opacity-0 pointer-events-none translate-y-3">
    <button onclick="window.scrollTo({ top: 0, behavior: 'smooth' })" class="px-3.5 py-2.5 bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white rounded-full shadow-xl border border-blue-400 transition-all flex items-center gap-1.5 text-xs font-bold shadow-blue-500/30 active:scale-95 cursor-pointer" title="Cuộn về đầu trang">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg>
      <span>Về đầu</span>
    </button>
  </div>"""

    new_back_to_top = """  <!-- Nút Lên Đầu Trang Nổi Thông Minh Cho Mobile & PC (Tự động ẩn/hiện, gọn gàng, bán trong suốt) -->
  <div id="backToTopContainer" class="fixed bottom-4 right-4 z-40 transition-all duration-300 opacity-0 pointer-events-none translate-y-3">
    <button onclick="window.scrollTo({ top: 0, behavior: 'smooth' })" class="w-10 h-10 sm:w-auto sm:px-3.5 sm:py-2 bg-blue-600/85 hover:bg-blue-600 active:bg-blue-700 backdrop-blur-sm text-white rounded-full shadow-lg border border-blue-400/40 transition-all flex items-center justify-center gap-1 text-xs font-bold active:scale-95 cursor-pointer" title="Cuộn về đầu trang">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 10l7-7m0 0l7 7m-7-7v18"></path></svg>
      <span class="hidden sm:inline">Về đầu</span>
    </button>
  </div>"""

    if old_back_to_top in content:
        content = content.replace(old_back_to_top, new_back_to_top)
        print("✓ Tối ưu Smart Back-To-Top (bottom-4 right-4, bán trong suốt)")

    # 7. CARD PADDING: Đổi p-6 thành p-3.5 sm:p-5
    old_card_tag = '<article class="bg-white rounded-2xl border ${isBookmarked ? \'border-amber-300 ring-2 ring-amber-100\' : \'border-slate-200\'} p-6 shadow-sm hover:shadow-md transition">'
    new_card_tag = '<article class="bg-white rounded-2xl border ${isBookmarked ? \'border-amber-300 ring-2 ring-amber-100\' : \'border-slate-200\'} p-3.5 sm:p-5 shadow-sm hover:shadow-md transition">'
    if old_card_tag in content:
        content = content.replace(old_card_tag, new_card_tag)
        print("✓ Tinh chỉnh padding thẻ câu hỏi: p-3.5 sm:p-5")

    # 8. ESSAY DRAFT TEXTAREA FONT SIZE
    old_draft_ta = """              <textarea 
                id="essay-draft-${q.id}" 
                oninput="saveDraft(${q.id}, this.value)" 
                placeholder="Gõ nháp câu trả lời của bạn tại đây... Khi bấm 'Xem lời giải' hay bấm 'Thu gọn/Mở gợi ý', toàn bộ nội dung bạn gõ ở đây đều được giữ nguyên vẹn 100%." 
                rows="3" 
                class="w-full p-3 text-xs sm:text-sm bg-white border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none transition leading-relaxed shadow-inner"
              >${currentDraft}</textarea>"""

    new_draft_ta = """              <textarea 
                id="essay-draft-${q.id}" 
                oninput="saveDraft(${q.id}, this.value)" 
                placeholder="Gõ nháp câu trả lời của bạn tại đây... Khi bấm 'Xem lời giải' hay bấm 'Thu gọn/Mở gợi ý', toàn bộ nội dung bạn gõ ở đây đều được giữ nguyên vẹn 100%." 
                rows="3" 
                class="w-full p-3 text-[16px] sm:text-sm bg-white border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none transition leading-relaxed shadow-inner font-sans"
              >${currentDraft}</textarea>"""

    if old_draft_ta in content:
        content = content.replace(old_draft_ta, new_draft_ta)
        print("✓ Tối ưu textarea nháp tự luận: text-[16px] sm:text-sm (chống iOS zoom)")

    # 9. SUB-QUESTION TEXTAREA FONT SIZE
    old_sub_ta = """                        <textarea
                          id="sub-input-${q.id}-${sIdx}"
                          oninput="saveSubAnswer(${q.id}, ${sIdx}, this.value)"
                          placeholder="✍️ Gõ câu trả lời của bạn cho câu hỏi nhỏ này để tự kiểm tra kiến thức trước khi mở đáp án..."
                          rows="2"
                          class="w-full text-xs p-2.5 rounded-lg border border-slate-300 focus:border-sky-500 focus:ring-1 focus:ring-sky-400 outline-none bg-white transition resize-y font-sans text-slate-800 leading-relaxed placeholder:text-slate-400 placeholder:italic shadow-inner"
                        >${escapeHtml(savedSubVal)}</textarea>"""

    new_sub_ta = """                        <textarea
                          id="sub-input-${q.id}-${sIdx}"
                          oninput="saveSubAnswer(${q.id}, ${sIdx}, this.value)"
                          placeholder="✍️ Gõ câu trả lời của bạn cho câu hỏi nhỏ này để tự kiểm tra kiến thức trước khi mở đáp án..."
                          rows="2"
                          class="w-full text-[16px] sm:text-xs p-2.5 rounded-lg border border-slate-300 focus:border-sky-500 focus:ring-1 focus:ring-sky-400 outline-none bg-white transition resize-y font-sans text-slate-800 leading-relaxed placeholder:text-slate-400 placeholder:italic shadow-inner"
                        >${escapeHtml(savedSubVal)}</textarea>"""

    if old_sub_ta in content:
        content = content.replace(old_sub_ta, new_sub_ta)
        print("✓ Tối ưu textarea câu con: text-[16px] sm:text-xs (chống iOS zoom)")

    # 10. SUB-QUESTION CONTROLS ROW: flex flex-wrap items-center justify-between gap-1.5
    old_sub_controls = """                        <div class="flex items-center justify-between gap-2 pt-0.5">
                          <div class="flex items-center gap-2">
                            <button 
                              type="button" 
                              id="sub-ans-btn-${q.id}-${sIdx}" 
                              onclick="toggleSubAnswer(${q.id}, ${sIdx})" 
                              class="px-2.5 py-1 text-xs font-bold rounded-lg border border-emerald-300 bg-emerald-50 hover:bg-emerald-100 text-emerald-900 transition flex items-center gap-1 shadow-xs cursor-pointer select-none"
                            >
                              <span id="sub-ans-btn-text-${q.id}-${sIdx}">👁️ Xem đáp án</span>
                              <span id="sub-ans-icon-${q.id}-${sIdx}">▼</span>
                            </button>
                            <button 
                              type="button" 
                              onclick="clearSubAnswer(${q.id}, ${sIdx})" 
                              class="text-[11px] text-slate-400 hover:text-red-600 transition px-1.5 py-0.5 rounded hover:bg-red-50 cursor-pointer"
                              title="Xóa nội dung đã gõ"
                            >
                              🗑️ Xóa nháp
                            </button>
                          </div>
                          <span id="sub-char-count-${q.id}-${sIdx}" class="text-[10px] text-slate-400 font-mono">
                            ${savedSubVal.length} ký tự
                          </span>
                        </div>"""

    new_sub_controls = """                        <div class="flex flex-wrap items-center justify-between gap-1.5 pt-1">
                          <div class="flex items-center gap-1.5 flex-wrap">
                            <button 
                              type="button" 
                              id="sub-ans-btn-${q.id}-${sIdx}" 
                              onclick="toggleSubAnswer(${q.id}, ${sIdx})" 
                              class="px-2.5 py-1 text-xs font-bold rounded-lg border border-emerald-300 bg-emerald-50 hover:bg-emerald-100 text-emerald-900 transition flex items-center gap-1 shadow-xs cursor-pointer select-none"
                            >
                              <span id="sub-ans-btn-text-${q.id}-${sIdx}">👁️ Xem đáp án</span>
                              <span id="sub-ans-icon-${q.id}-${sIdx}">▼</span>
                            </button>
                            <button 
                              type="button" 
                              onclick="clearSubAnswer(${q.id}, ${sIdx})" 
                              class="text-[11px] text-slate-400 hover:text-red-600 transition px-1.5 py-0.5 rounded hover:bg-red-50 cursor-pointer"
                              title="Xóa nội dung đã gõ"
                            >
                              🗑️ Xóa nháp
                            </button>
                          </div>
                          <span id="sub-char-count-${q.id}-${sIdx}" class="text-[10px] text-slate-400 font-mono">
                            ${savedSubVal.length} ký tự
                          </span>
                        </div>"""

    if old_sub_controls in content:
        content = content.replace(old_sub_controls, new_sub_controls)
        print("✓ Tối ưu hàng nút điều khiển câu con: flex-wrap gap-1.5")

    # 11. SUB-QUESTION TOOLBAR & BADGE
    old_sub_tb = """              <!-- Thanh công cụ hàng loạt cho câu con -->
              <div class="flex items-center justify-between flex-wrap gap-2 pb-2 border-b border-sky-200/70">
                <span class="text-[11px] font-bold text-sky-950 flex items-center gap-1">
                  <span>📝</span> Danh sách ${q.origin_sub_questions.length} câu hỏi con:
                </span>
                <div class="flex items-center gap-1.5">
                  <button 
                    type="button" 
                    onclick="toggleAllSubAnswers(${q.id}, true)" 
                    class="px-2.5 py-1 text-[11px] font-bold rounded-lg bg-sky-100 hover:bg-sky-200 text-sky-900 border border-sky-300 transition shadow-xs flex items-center gap-1 cursor-pointer"
                  >
                    <span>👁️ Mở tất cả đáp án</span>
                  </button>
                  <button 
                    type="button" 
                    onclick="toggleAllSubAnswers(${q.id}, false)" 
                    class="px-2.5 py-1 text-[11px] font-semibold rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-300 transition shadow-xs flex items-center gap-1 cursor-pointer"
                  >
                    <span>▲ Thu gọn tất cả</span>
                  </button>
                </div>
              </div>"""

    new_sub_tb = """              <!-- Thanh công cụ hàng loạt cho câu con -->
              <div class="flex flex-wrap items-center justify-between gap-2 pb-2 border-b border-sky-200/70">
                <span class="text-[11px] font-bold text-sky-950 flex items-center gap-1 shrink-0">
                  <span>📝</span> Danh sách ${q.origin_sub_questions.length} câu hỏi con:
                </span>
                <div class="flex items-center gap-1.5 flex-wrap">
                  <button 
                    type="button" 
                    onclick="toggleAllSubAnswers(${q.id}, true)" 
                    class="px-2.5 py-1 text-[11px] font-bold rounded-lg bg-sky-100 hover:bg-sky-200 text-sky-900 border border-sky-300 transition shadow-xs flex items-center gap-1 cursor-pointer"
                  >
                    <span>👁️ Mở tất cả</span>
                  </button>
                  <button 
                    type="button" 
                    onclick="toggleAllSubAnswers(${q.id}, false)" 
                    class="px-2.5 py-1 text-[11px] font-semibold rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-300 transition shadow-xs flex items-center gap-1 cursor-pointer"
                  >
                    <span>▲ Thu gọn</span>
                  </button>
                </div>
              </div>"""

    if old_sub_tb in content:
        content = content.replace(old_sub_tb, new_sub_tb)
        print("✓ Tối ưu Toolbar câu con co giãn tự nhiên, không vỡ hàng")

    # 12. CANVAS INITIALIZATION: RESPONSIVE WIDTH
    old_canvas_init = """        const parentWidth = canvas.parentElement.clientWidth || 340;
        canvas.width = Math.max(parentWidth, 300);
        canvas.height = 240;"""

    new_canvas_init = """        const parentWidth = (canvas.parentElement && canvas.parentElement.clientWidth > 0) ? canvas.parentElement.clientWidth : 320;
        canvas.width = parentWidth;
        canvas.height = 240;"""

    if old_canvas_init in content:
        content = content.replace(old_canvas_init, new_canvas_init)
        print("✓ Tối ưu kích thước Canvas: 100% responsive width theo parent")

    # 13. RENDER SUB ANSWER: BREAK-WORDS & OVERFLOW
    content = content.replace(
        '<div class="bg-white/95 p-3 rounded-lg border border-emerald-200/90 text-slate-800 text-xs leading-relaxed select-text shadow-2xs">',
        '<div class="bg-white/95 p-3 rounded-lg border border-emerald-200/90 text-slate-800 text-xs leading-relaxed select-text shadow-2xs overflow-x-auto break-words">'
    )

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    new_len = len(content)
    print(f"✓ Đã ghi đè index.html thành công: {new_len} ký tự, {content.count(chr(10))} dòng")

if __name__ == "__main__":
    polish_index_html()
