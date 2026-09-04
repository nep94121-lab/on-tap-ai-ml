import json

# Load the questions
with open('c:/Users/Admin/Desktop/học tập/Bo_De_AI_ML_Da_Giai/questions_deduplicated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Prepare all questions with type info
all_questions = []

for q in data['single_choice']:
    all_questions.append({
        'id': q['id'],
        'type': 'single',
        'type_label': 'TNĐ',
        'question': q['question'],
        'choices': q['choices'],
        'correct': q['correct'],
        'explanation': q['explanation']
    })

for q in data['multiple_choice']:
    all_questions.append({
        'id': q['id'],
        'type': 'multi',
        'type_label': 'TNN',
        'question': q['question'],
        'choices': q['choices'],
        'correct': q['correct'],
        'explanation': q['explanation']
    })

for q in data['essay_fill']:
    all_questions.append({
        'id': q['id'],
        'type': 'essay',
        'type_label': 'TL',
        'question': q['question'],
        'choices': q.get('choices', []),
        'correct': q.get('correct', ''),
        'explanation': q['explanation']
    })

# Sort by ID
all_questions.sort(key=lambda x: x['id'])

print(f"Total questions: {len(all_questions)}")
print(f"Single: {len([q for q in all_questions if q['type']=='single'])}")
print(f"Multi: {len([q for q in all_questions if q['type']=='multi'])}")
print(f"Essay: {len([q for q in all_questions if q['type']=='essay'])}")

# Generate HTML
html_content = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ôn Tập Tổng Hợp 124 Câu AI & ML</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .question-card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 16px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        .question-card:hover {
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        .question-card.hidden {
            display: none;
        }
        .btn-filter {
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.2s ease;
            border: 2px solid transparent;
        }
        .btn-filter:hover {
            transform: translateY(-2px);
        }
        .btn-filter.active {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-color: transparent;
        }
        .btn-filter.inactive {
            background: #f3f4f6;
            color: #4b5563;
            border-color: #e5e7eb;
        }
        .btn-explain {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
        .btn-explain:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }
        .explanation {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 16px;
            border-radius: 8px;
            margin-top: 12px;
            border-left: 4px solid #667eea;
        }
        .badge-tnd {
            background: #3b82f6;
            color: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 600;
        }
        .badge-tnn {
            background: #f59e0b;
            color: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 600;
        }
        .badge-tl {
            background: #10b981;
            color: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 600;
        }
        .choice-item {
            padding: 10px 14px;
            background: #f9fafb;
            border-radius: 8px;
            margin-bottom: 8px;
            border: 1px solid #e5e7eb;
            transition: all 0.2s ease;
        }
        .choice-item:hover {
            background: #f3f4f6;
            border-color: #d1d5db;
        }
        .correct-answer {
            background: #dcfce7 !important;
            border-color: #22c55e !important;
            font-weight: 600;
        }
        .correct-answer::before {
            content: "✓ ";
            color: #22c55e;
        }
        .stats-bar {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .filter-section {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        h1 {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .header-gradient {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
    </style>
</head>
<body class="bg-gray-100 min-h-screen pb-10">
    <!-- Header -->
    <div class="header-gradient text-white py-8 mb-8">
        <div class="max-w-4xl mx-auto px-4">
            <h1 class="text-3xl font-bold mb-2">ON TAP TONG HOP 124 CAU</h1>
            <p class="text-white/80">AI & Machine Learning - De Thi Da Giai</p>
        </div>
    </div>

    <div class="max-w-4xl mx-auto px-4">
        <!-- Stats Bar -->
        <div class="stats-bar mb-6">
            <div class="flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z" />
                    <path fill-rule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z" clip-rule="evenodd" />
                </svg>
                <span id="stats-display">Da lam: 0/124</span>
            </div>
            <div class="flex items-center gap-4 text-sm">
                <span class="flex items-center gap-1"><span class="w-3 h-3 bg-blue-500 rounded"></span> TNĐ: ''' + str(len([q for q in all_questions if q['type']=='single'])) + '''</span>
                <span class="flex items-center gap-1"><span class="w-3 h-3 bg-amber-500 rounded"></span> TNN: ''' + str(len([q for q in all_questions if q['type']=='multi'])) + '''</span>
                <span class="flex items-center gap-1"><span class="w-3 h-3 bg-green-500 rounded"></span> TL: ''' + str(len([q for q in all_questions if q['type']=='essay'])) + '''</span>
            </div>
        </div>

        <!-- Filter Section -->
        <div class="filter-section mb-6">
            <h3 class="text-lg font-semibold mb-4 text-gray-700">Loc theo loai cau hoi:</h3>
            <div class="flex flex-wrap gap-2">
                <button onclick="filterAll()" id="btn-all" class="btn-filter active">
                    Tat ca (124)
                </button>
                <button onclick="filterSingle()" id="btn-single" class="btn-filter inactive">
                    Trac nghiem don (''' + str(len([q for q in all_questions if q['type']=='single'])) + ''')
                </button>
                <button onclick="filterMulti()" id="btn-multi" class="btn-filter inactive">
                    Nhieu dap an (''' + str(len([q for q in all_questions if q['type']=='multi'])) + ''')
                </button>
                <button onclick="filterEssay()" id="btn-essay" class="btn-filter inactive">
                    Tu luan (''' + str(len([q for q in all_questions if q['type']=='essay'])) + ''')
                </button>
            </div>
        </div>

        <!-- Questions Container -->
        <div id="questions-container">
'''

# Generate question cards
for q in all_questions:
    q_type = q['type']
    q_type_class = 'badge-tnd' if q_type == 'single' else ('badge-tnn' if q_type == 'multi' else 'badge-tl')

    # Escape HTML entities
    question_text = q['question'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    explanation = q['explanation'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

    html_content += f'''
            <div class="question-card" data-type="{q_type}" data-id="{q['id']}">
                <div class="flex items-center gap-3 mb-4">
                    <h3 class="text-lg font-bold text-gray-800">Cau {q['id']}</h3>
                    <span class="{q_type_class}">{q['type_label']}</span>
                </div>
                <p class="text-gray-700 mb-4 font-medium">{question_text}</p>
'''

    # Add choices for single and multiple choice
    if q['choices'] and len(q['choices']) > 0:
        html_content += '                <div class="choices mb-4">\n'
        for i, choice in enumerate(q['choices']):
            choice_letter = chr(65 + i)  # A, B, C, D
            choice_text = choice.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
            html_content += f'                    <div class="choice-item"><span class="font-semibold mr-2">{choice_letter}.</span> {choice_text}</div>\n'
        html_content += '                </div>\n'

    # Add correct answer for multiple choice
    if q_type == 'multi' and q['correct']:
        correct_text = str(q['correct']).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        html_content += f'                <div class="mb-4 p-3 bg-green-50 border border-green-200 rounded-lg"><strong class="text-green-700">Dap an dung:</strong> <span class="text-green-800">{correct_text}</span></div>\n'

    # Add correct answer for single choice
    if q_type == 'single' and q['correct']:
        correct_text = str(q['correct']).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        html_content += f'                <div class="mb-4 p-3 bg-green-50 border border-green-200 rounded-lg"><strong class="text-green-700">Dap an dung:</strong> <span class="text-green-800">{correct_text}</span></div>\n'

    # Add essay answer if available
    if q_type == 'essay' and q['correct']:
        correct_text = str(q['correct']).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br>')
        html_content += f'                <div class="mb-4 p-3 bg-green-50 border border-green-200 rounded-lg"><strong class="text-green-700">Dap an:</strong> <span class="text-green-800">{correct_text}</span></div>\n'

    # Add explanation button and content
    html_content += f'''                <button class="btn-explain" onclick="toggleExplain(this)">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
                    </svg>
                    Giai Thich
                </button>
                <div class="explanation" style="display: none;">
                    <strong class="text-purple-800">Giai thich chi tiet:</strong><br>
                    <span class="text-gray-700">{explanation}</span>
                </div>
            </div>
'''

# Add JavaScript
html_content += '''
        </div>

        <!-- Footer -->
        <div class="text-center text-gray-500 text-sm mt-8 pb-4">
            <p>Bo De AI & ML Da Giai - 124 Cau Hoi</p>
        </div>
    </div>

    <script>
        let currentFilter = 'all';

        function filterAll() {
            currentFilter = 'all';
            updateFilterButtons();
            document.querySelectorAll('.question-card').forEach(card => {
                card.classList.remove('hidden');
            });
            updateStats();
        }

        function filterSingle() {
            currentFilter = 'single';
            updateFilterButtons();
            document.querySelectorAll('.question-card').forEach(card => {
                if (card.dataset.type === 'single') {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
            updateStats();
        }

        function filterMulti() {
            currentFilter = 'multi';
            updateFilterButtons();
            document.querySelectorAll('.question-card').forEach(card => {
                if (card.dataset.type === 'multi') {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
            updateStats();
        }

        function filterEssay() {
            currentFilter = 'essay';
            updateFilterButtons();
            document.querySelectorAll('.question-card').forEach(card => {
                if (card.dataset.type === 'essay') {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
            updateStats();
        }

        function updateFilterButtons() {
            const btnAll = document.getElementById('btn-all');
            const btnSingle = document.getElementById('btn-single');
            const btnMulti = document.getElementById('btn-multi');
            const btnEssay = document.getElementById('btn-essay');

            [btnAll, btnSingle, btnMulti, btnEssay].forEach(btn => {
                btn.classList.remove('active');
                btn.classList.add('inactive');
            });

            if (currentFilter === 'all') btnAll.classList.add('active');
            else if (currentFilter === 'single') btnSingle.classList.add('active');
            else if (currentFilter === 'multi') btnMulti.classList.add('active');
            else if (currentFilter === 'essay') btnEssay.classList.add('active');

            if (currentFilter !== 'all') btnAll.classList.remove('inactive');
            if (currentFilter !== 'single') btnSingle.classList.remove('inactive');
            if (currentFilter !== 'multi') btnMulti.classList.remove('inactive');
            if (currentFilter !== 'essay') btnEssay.classList.remove('inactive');
        }

        function toggleExplain(btn) {
            const explanation = btn.nextElementSibling;
            if (explanation.style.display === 'none') {
                explanation.style.display = 'block';
                btn.innerHTML = `
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM9 9a1 1 0 012 0v2a1 1 0 11-2 0V9zm2-1a1 1 0 10-2 0v2a1 1 0 102 0V9z" clip-rule="evenodd" />
                    </svg>
                    An Giai Thich
                `;
            } else {
                explanation.style.display = 'none';
                btn.innerHTML = `
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
                    </svg>
                    Giai Thich
                `;
            }
        }

        function updateStats() {
            const visibleCards = document.querySelectorAll('.question-card:not(.hidden)');
            document.getElementById('stats-display').textContent = `Da lam: 0/${visibleCards.length}`;
        }

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            updateStats();
        });
    </script>
</body>
</html>
'''

# Write the HTML file
output_path = 'c:/Users/Admin/Desktop/học tập/Bo_De_AI_ML_Da_Giai/ON_TAP_TONG_HOP_124_CAU.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"\nHTML file created successfully at: {output_path}")
print(f"File contains {len(all_questions)} questions")
