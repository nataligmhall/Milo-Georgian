#!/usr/bin/env python3
"""
Build mobile-friendly lesson reader for GitHub Pages.

Output: docs/  (enable Pages → Deploy from branch main, folder /docs)

    python3 build_reader_site.py
    git add docs && git commit -m "Update lesson reader" && git push
"""

import html
import json
from pathlib import Path

from config import LESSON_DATA, READER_DIR, romanize
from level_placement import BOOK_LABELS
from reader_extras import merge_reader_extras
from worksheet import build_worksheet_exercises

BOOK_ORDER = ("a1", "a2", "a2plus", "b1")

CSS = """\
:root {
  --bg: #f5f0eb;
  --card: #fff;
  --ink: #1a1a1a;
  --muted: #777;
  --accent: #8b4513;
  --gold: #c8a96e;
  --ru: #6b4fa0;
  --green: #2d5a3d;
  --line: #e8dfd4;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1a1816;
    --card: #252220;
    --ink: #f0ebe4;
    --muted: #9a9088;
    --accent: #d4a574;
    --gold: #c8a96e;
    --ru: #b09ad4;
    --green: #7ecf9a;
    --line: #3a3530;
  }
}
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  margin: 0;
  padding: 0 0 5rem;
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}
.wrap { max-width: 42rem; margin: 0 auto; padding: 1rem 1rem 2rem; }
header { margin-bottom: 1.25rem; }
.brand { font-size: 0.75rem; letter-spacing: 0.08em; color: var(--gold); font-weight: 700; }
h1 { font-size: 1.35rem; margin: 0.25rem 0 0.35rem; color: var(--accent); line-height: 1.25; }
.sub { font-size: 0.85rem; color: var(--muted); margin: 0; }
nav.top { display: flex; gap: 0.5rem; flex-wrap: wrap; margin: 1rem 0; }
nav.top a, .pill {
  display: inline-block;
  padding: 0.45rem 0.75rem;
  border-radius: 999px;
  background: var(--card);
  border: 1px solid var(--line);
  color: var(--accent);
  text-decoration: none;
  font-size: 0.82rem;
  font-weight: 600;
}
nav.top a:hover { border-color: var(--gold); }
.done-btn {
  flex-shrink: 0;
  width: 1.75rem;
  height: 1.75rem;
  border-radius: 50%;
  border: 2px solid var(--line);
  background: var(--card);
  color: var(--muted);
  font-size: 0.95rem;
  line-height: 1;
  cursor: pointer;
  padding: 0;
}
.done-btn.done { border-color: var(--green); background: rgba(45,90,61,.12); color: var(--green); }
.progress-bar {
  margin: 0.75rem 0 1rem;
  font-size: 0.82rem;
  color: var(--muted);
}
.progress-track {
  height: 6px;
  background: var(--line);
  border-radius: 999px;
  overflow: hidden;
  margin-top: 0.35rem;
}
.progress-fill { height: 100%; background: var(--green); border-radius: 999px; width: 0%; transition: width .2s; }
.lesson-row {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  margin: 0.35rem 0;
  padding: 0.2rem 0;
  border-bottom: 1px solid var(--line);
}
.lesson-row.done a { color: var(--muted); text-decoration: line-through; text-decoration-color: var(--green); }
.lesson-row a {
  flex: 1;
  color: var(--ink);
  text-decoration: none;
  font-size: 0.92rem;
  padding: 0.2rem 0;
}
.lesson-row a:hover { color: var(--accent); }
.lesson-done-toggle {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  margin-top: 0.5rem;
  font-size: 0.88rem;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}
.lesson-done-toggle input { width: 1.1rem; height: 1.1rem; accent-color: var(--green); }
.phrase-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 0.85rem 1rem;
  margin-bottom: 0.55rem;
}
.phrase-ge { font-size: 1.1rem; font-weight: 600; }
.phrase-en { font-size: 0.9rem; margin-top: 0.2rem; }
.phrase-ru { color: var(--ru); font-size: 0.84rem; margin-top: 0.1rem; }
.grammar ul { margin: 0.5rem 0 0; padding-left: 1.1rem; font-size: 0.92rem; }
.grammar ul li { margin: 0.25rem 0; }
details.gram-table {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 10px;
  margin: 0.55rem 0;
  overflow: hidden;
}
details.gram-table summary {
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 700;
  padding: 0.65rem 0.85rem;
  color: var(--accent);
}
details.gram-table[open] summary { border-bottom: 1px solid var(--line); }
.table-wrap { overflow-x: auto; padding: 0 0.5rem 0.5rem; }
.gram-table table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.86rem;
}
.gram-table th, .gram-table td {
  padding: 0.45rem 0.55rem;
  text-align: left;
  border-bottom: 1px solid var(--line);
}
.gram-table th { color: var(--muted); font-weight: 600; font-size: 0.78rem; }
.gram-table td:first-child { color: var(--muted); }
.gram-table .cell-ge { font-weight: 600; font-size: 0.95rem; }
.table-note {
  margin: 0 0.85rem 0.65rem;
  font-size: 0.8rem;
  color: var(--muted);
}
.can-do {
  background: rgba(200, 169, 110, 0.12);
  border: 1px solid var(--gold);
  border-radius: 14px;
  padding: 1rem 1.1rem;
  margin: 1.25rem 0;
}
.can-do h2 { margin: 0 0 0.55rem; font-size: 0.95rem; }
.can-do ul { margin: 0; padding-left: 1.15rem; font-size: 0.92rem; }
.can-do li { margin: 0.3rem 0; }
.reading-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 1rem 1.1rem;
}
.reading-ge {
  font-size: 1.05rem;
  line-height: 1.65;
  font-weight: 500;
}
.reading-toggle {
  margin-top: 0.75rem;
  font-size: 0.82rem;
  color: var(--accent);
  cursor: pointer;
  font-weight: 600;
  border: none;
  background: none;
  padding: 0;
}
.reading-en {
  margin-top: 0.55rem;
  font-size: 0.9rem;
  color: var(--muted);
  line-height: 1.55;
  border-top: 1px dashed var(--line);
  padding-top: 0.65rem;
}
.reading-en.hidden { display: none; }
section { margin: 1.5rem 0; }
h2 { font-size: 1rem; color: var(--accent); margin: 0 0 0.75rem; }
.card {
  background: var(--card);
  border-radius: 14px;
  padding: 1rem 1.1rem;
  margin-bottom: 0.65rem;
  border: 1px solid var(--line);
  box-shadow: 0 1px 4px rgba(0,0,0,.04);
}
.grammar p { margin: 0.4rem 0; font-size: 0.95rem; }
.grammar .ru { color: var(--ru); font-style: italic; font-size: 0.9rem; }
.grammar .ex-ge { font-size: 1.1rem; font-weight: 600; margin-top: 0.6rem; }
.grammar .ex-en { color: var(--muted); font-size: 0.88rem; }
.easier {
  margin-top: 0.75rem;
  padding: 0.65rem 0.8rem;
  background: rgba(45,90,61,.08);
  border-radius: 8px;
  font-size: 0.88rem;
  color: var(--green);
}
.vocab-group { margin-bottom: 1.5rem; }
.vocab-group h3 {
  font-size: 0.78rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
  margin: 0 0 0.65rem;
  font-weight: 700;
}
.vocab-grid {
  display: grid;
  gap: 0.75rem;
}
@media (min-width: 480px) {
  .vocab-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
.vocab-card {
  background: var(--card);
  border-radius: 12px;
  padding: 0.9rem 1rem;
  border: 1px solid var(--line);
  box-shadow: 0 1px 4px rgba(0,0,0,.04);
}
.vocab-ge { font-size: 1.25rem; font-weight: 700; letter-spacing: 0.01em; line-height: 1.3; }
.vocab-rom { color: var(--gold); font-style: italic; font-size: 0.86rem; margin-top: 0.1rem; }
.vocab-en { font-size: 0.94rem; margin-top: 0.25rem; line-height: 1.35; }
.vocab-ru { color: var(--ru); font-size: 0.84rem; margin-top: 0.15rem; }
details.work {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 0.65rem 0.85rem;
  margin-bottom: 0.5rem;
}
details.work summary { cursor: pointer; font-size: 0.92rem; font-weight: 600; }
details.work .ans { margin-top: 0.5rem; font-size: 0.88rem; color: var(--green); }
.book-grid { display: grid; gap: 1rem; }
.book-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 1rem;
}
.book-card h2 { margin-top: 0; }
.lesson-list { list-style: none; padding: 0; margin: 0; }
.lesson-list li { margin: 0.35rem 0; }
.lesson-list a {
  color: var(--ink);
  text-decoration: none;
  font-size: 0.92rem;
  display: block;
  padding: 0.35rem 0;
  border-bottom: 1px solid var(--line);
}
.lesson-list a:hover { color: var(--accent); }
footer {
  text-align: center;
  font-size: 0.75rem;
  color: var(--muted);
  margin-top: 2rem;
  padding: 1rem;
}
"""

READING_JS = """\
document.addEventListener("click", function (e) {
  var btn = e.target.closest("[data-reading-toggle]");
  if (!btn) return;
  var id = btn.dataset.readingToggle;
  var en = document.getElementById(id + "-en");
  if (!en) return;
  var hidden = en.classList.toggle("hidden");
  btn.textContent = hidden ? "Show translation" : "Hide translation";
});
"""

PROGRESS_JS = """\
(function () {
  const KEY = "milo-lesson-progress";

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || "{}"); }
    catch (e) { return {}; }
  }

  function save(data) {
    localStorage.setItem(KEY, JSON.stringify(data));
  }

  function isDone(id, data) {
    return !!data[id];
  }

  function setDone(id, done) {
    const data = load();
    if (done) data[id] = true;
    else delete data[id];
    save(data);
    syncUI(data);
  }

  function syncUI(data) {
    document.querySelectorAll("[data-lesson]").forEach(function (el) {
      const id = el.dataset.lesson;
      if (!id || id.indexOf("-") === -1) return;
      const done = isDone(id, data);
      if (el.classList.contains("lesson-row")) {
        el.classList.toggle("done", done);
        const btn = el.querySelector(".done-btn");
        if (btn) {
          btn.classList.toggle("done", done);
          btn.textContent = done ? "✓" : "○";
        }
      }
    });
    document.querySelectorAll(".lesson-done-cb").forEach(function (cb) {
      const id = cb.dataset.lesson;
      if (id) cb.checked = isDone(id, data);
    });
    const total = parseInt(document.body.dataset.totalLessons || "0", 10);
    if (total > 0) {
      const doneCount = Object.keys(data).filter(function (k) { return data[k]; }).length;
      const pct = Math.round((doneCount / total) * 100);
      const summary = document.getElementById("progress-summary");
      const fill = document.getElementById("progress-fill");
      if (summary) summary.textContent = "Progress: " + doneCount + " / " + total + " lessons";
      if (fill) fill.style.width = pct + "%";
    }
  }

  document.addEventListener("click", function (e) {
    const btn = e.target.closest(".done-btn");
    if (!btn) return;
    e.preventDefault();
    const id = btn.dataset.lesson;
    if (!id) return;
    const data = load();
    setDone(id, !isDone(id, data));
  });

  document.addEventListener("change", function (e) {
    if (!e.target.classList.contains("lesson-done-cb")) return;
    setDone(e.target.dataset.lesson, e.target.checked);
  });

  syncUI(load());
})();
"""


def esc(s):
    return html.escape(str(s or ""))


def lesson_filename(num):
    return f"lesson-{int(num):02d}.html"


def lesson_href(book, num, from_book=None):
    """Relative link: same-book pages live in docs/{book}/."""
    fname = lesson_filename(num)
    if from_book is None:
        return f"{book}/{fname}"
    if book == from_book:
        return fname
    return f"../{book}/{fname}"


def nav_links(book, num, lessons):
    nums = sorted(int(k) for k in lessons[book].keys())
    n = int(num)
    parts = ['<nav class="top">', f'<a href="../index.html">All levels</a>']

    if n > nums[0]:
        parts.append(f'<a href="{lesson_href(book, n - 1, book)}">← L{n - 1}</a>')
    else:
        idx = BOOK_ORDER.index(book)
        if idx > 0 and BOOK_ORDER[idx - 1] in lessons:
            pb = BOOK_ORDER[idx - 1]
            plast = max(int(k) for k in lessons[pb])
            plabel = BOOK_LABELS.get(pb, pb.upper())
            parts.append(
                f'<a href="{lesson_href(pb, plast, book)}">← {esc(plabel)} L{plast}</a>'
            )

    if n < nums[-1]:
        parts.append(f'<a href="{lesson_href(book, n + 1, book)}">L{n + 1} →</a>')
    else:
        idx = BOOK_ORDER.index(book)
        if idx + 1 < len(BOOK_ORDER) and BOOK_ORDER[idx + 1] in lessons:
            nb = BOOK_ORDER[idx + 1]
            nlabel = BOOK_LABELS.get(nb, nb.upper())
            parts.append(f'<a href="{lesson_href(nb, 1, book)}">{esc(nlabel)} L1 →</a>')

    parts.append("</nav>")
    return "".join(parts)


def phrases_html(lesson):
    phrases = lesson.get("phrases") or []
    if not phrases:
        return ""
    items = []
    for p in phrases:
        ru = f'<div class="phrase-ru">🇷🇺 {esc(p.get("ru", ""))}</div>' if p.get("ru") else ""
        items.append(
            f'<div class="phrase-card">'
            f'<div class="phrase-ge">{esc(p["ge"])}</div>'
            f'<div class="phrase-en">{esc(p["en"])}</div>{ru}</div>'
        )
    return f"<section><h2>💬 Phrases &amp; dialogues</h2>{''.join(items)}</section>"


def grammar_bullets_html(g):
    bullets = g.get("bullets") or []
    if not bullets:
        return ""
    items = "".join(f"<li>{esc(b)}</li>" for b in bullets)
    return f"<ul>{items}</ul>"


def grammar_tables_html(g):
    tables = g.get("tables") or []
    if not tables:
        return ""
    blocks = []
    for i, tbl in enumerate(tables):
        headers = tbl.get("headers") or []
        ge_cols = {j for j, h in enumerate(headers) if h in ("Georgian", "Pattern", "Noun", "Country")}
        if not ge_cols and headers:
            if headers[0] == "Georgian":
                ge_cols = {0}
            elif len(headers) >= 2:
                ge_cols = {1}
        head = ""
        if headers:
            head = "<thead><tr>" + "".join(f"<th>{esc(h)}</th>" for h in headers) + "</tr></thead>"
        body_rows = []
        for row in tbl.get("rows") or []:
            cells = []
            for j, cell in enumerate(row):
                cls = ' class="cell-ge"' if j in ge_cols else ""
                cells.append(f"<td{cls}>{esc(cell)}</td>")
            body_rows.append("<tr>" + "".join(cells) + "</tr>")
        body = "<tbody>" + "".join(body_rows) + "</tbody>" if body_rows else ""
        note = tbl.get("note") or ""
        note_html = f'<p class="table-note">{esc(note)}</p>' if note else ""
        open_attr = " open" if i == 0 else ""
        blocks.append(
            f'<details class="gram-table"{open_attr}>'
            f'<summary>{esc(tbl.get("title", "Table"))}</summary>'
            f'<div class="table-wrap"><table>{head}{body}</table></div>{note_html}</details>'
        )
    return f'<div class="grammar-tables">{"".join(blocks)}</div>'


def can_do_html(lesson):
    items = lesson.get("can_do") or []
    if not items:
        return ""
    lis = "".join(f"<li>{esc(x)}</li>" for x in items)
    return f'<section class="can-do"><h2>🎯 After this lesson you can…</h2><ul>{lis}</ul></section>'


def reading_html(lesson):
    reading = lesson.get("reading")
    if not reading or not reading.get("ge"):
        return ""
    rid = f"reading-{lesson.get('_rid', 'x')}"
    en = reading.get("en", "")
    en_block = (
        f'<div class="reading-en hidden" id="{rid}-en">{esc(en)}</div>'
        if en
        else ""
    )
    toggle = (
        f'<button type="button" class="reading-toggle" data-reading-toggle="{rid}">'
        f"Show translation</button>"
        if en
        else ""
    )
    return (
        f"<section><h2>📄 Short reading</h2>"
        f'<div class="reading-card">'
        f'<div class="reading-ge">{esc(reading["ge"])}</div>'
        f"{toggle}{en_block}</div></section>"
    )


def vocab_card(v):
    rom = v.get("rom") or romanize(v["ge"])
    ru = f'<div class="vocab-ru">🇷🇺 {esc(v.get("ru", ""))}</div>' if v.get("ru") else ""
    return (
        f'<div class="vocab-card">'
        f'<div class="vocab-ge">{esc(v["ge"])}</div>'
        f'<div class="vocab-rom">{esc(rom)}</div>'
        f'<div class="vocab-en">{esc(v["en"])}</div>{ru}</div>'
    )


def vocab_sections(vocab):
    groups = []
    current = None
    cards = []
    for v in vocab:
        group = v.get("group") or "Vocabulary"
        if group != current:
            if cards:
                groups.append(
                    f'<div class="vocab-group"><h3>{esc(current)}</h3>'
                    f'<div class="vocab-grid">{"".join(cards)}</div></div>'
                )
            current = group
            cards = []
        cards.append(vocab_card(v))
    if cards:
        groups.append(
            f'<div class="vocab-group"><h3>{esc(current)}</h3>'
            f'<div class="vocab-grid">{"".join(cards)}</div></div>'
        )
    return "\n".join(groups)


def worksheet_html(lesson, vocab):
    exercises = build_worksheet_exercises(lesson, vocab)
    if not exercises:
        return ""
    items = []
    for i, ex in enumerate(exercises, 1):
        prompt = ex["prompt"].replace("<b>", "").replace("</b>", "").replace("<code>", "").replace("</code>", "")
        items.append(
            f"<details class=\"work\"><summary>{i}. {esc(prompt)}</summary>"
            f"<div class=\"ans\">✓ {esc(ex.get('answer', ''))}</div></details>"
        )
    return f"<section><h2>📝 Worksheet ({len(exercises)} exercises)</h2>{''.join(items)}</section>"


def lesson_page(book, num, lesson, lessons):
    lesson = merge_reader_extras(lesson, book, num)
    lesson["_rid"] = f"{book}-{num}"
    g = lesson.get("grammar", {})
    easier = lesson.get("easier_than_russian", "")
    label = BOOK_LABELS.get(book, book.upper())
    vocab = [dict(v, rom=romanize(v["ge"])) for v in lesson.get("vocab", [])]
    easier_block = f'<div class="easier">💚 <b>Easier than Russian:</b> {esc(easier)}</div>' if easier else ""

    lesson_id = f"{book}-{num}"
    bullets = grammar_bullets_html(g)
    tables = grammar_tables_html(g)

    body = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<title>{esc(label)} L{num} — {esc(lesson.get('title', ''))}</title>
<link rel="stylesheet" href="../style.css">
</head>
<body data-lesson="{lesson_id}">
<div class="wrap">
{nav_links(book, num, lessons)}
<header>
  <div class="brand">აღმართი · Milo reader</div>
  <h1>{esc(label)} — Lesson {num}</h1>
  <p class="sub">{esc(lesson.get('title', ''))} · {len(vocab)} words</p>
  <label class="lesson-done-toggle"><input type="checkbox" class="lesson-done-cb" data-lesson="{lesson_id}"> Mark lesson complete</label>
</header>
{can_do_html(lesson)}
<section>
  <h2>📖 Grammar</h2>
  <div class="card grammar">
    <p>{esc(g.get('en', ''))}</p>
    {bullets}
    {tables}
    <p class="ru">🇷🇺 {esc(g.get('ru', ''))}</p>
    <div class="ex-ge">{esc(g.get('example_ge', ''))}</div>
    <div class="ex-en">{esc(g.get('example_en', ''))}</div>
    {easier_block}
  </div>
</section>
{reading_html(lesson)}
{phrases_html(lesson)}
<section>
  <h2>📚 Vocabulary</h2>
  {vocab_sections(vocab)}
</section>
{worksheet_html(lesson, vocab)}
<p class="sub" style="margin-top:1.5rem">🎧 Audio &amp; quizzes in Telegram · /audio · /quiz</p>
<footer>Milo Georgian Tutor · synced from lesson_data.json</footer>
</div>
<script src="../progress.js"></script>
<script src="../reading.js"></script>
</body>
</html>"""
    return body


def index_page(lessons):
    blocks = []
    total = 0
    for book in BOOK_ORDER:
        if book not in lessons:
            continue
        label = BOOK_LABELS.get(book, book.upper())
        items = []
        for num in sorted(lessons[book].keys(), key=int):
            les = lessons[book][num]
            href = lesson_href(book, num)
            lid = f"{book}-{num}"
            total += 1
            items.append(
                f'<li class="lesson-row" data-lesson="{lid}">'
                f'<button type="button" class="done-btn" data-lesson="{lid}" aria-label="Mark lesson complete">○</button>'
                f'<a href="{href}">L{num} — {esc(les.get("title", ""))}</a></li>'
            )
        blocks.append(
            f'<div class="book-card"><h2>{esc(label)}</h2>'
            f'<ul class="lesson-list">{"".join(items)}</ul></div>'
        )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Georgian Lessons — აღმართი Reader</title>
<link rel="stylesheet" href="style.css">
</head>
<body data-total-lessons="{total}">
<div class="wrap">
<header>
  <div class="brand">აღმართი · GeoFL</div>
  <h1>Georgian Lesson Reader</h1>
  <p class="sub">Mobile-first აღმართი · 48 lessons · grammar, vocab &amp; worksheets · no PDFs</p>
  <p class="sub" style="margin-top:0.5rem">Faster than <a href="https://www.geofl.ge/">geofl.ge</a> on your phone — same textbook content, built for reading.</p>
  <div class="progress-bar" id="progress-summary">Progress: 0 / {total} lessons</div>
  <div class="progress-track"><div class="progress-fill" id="progress-fill"></div></div>
</header>
<div class="book-grid">{"".join(blocks)}</div>
<footer>Milo Georgian Tutor · <a href="https://www.geofl.ge/">geofl.ge</a></footer>
</div>
<script src="progress.js"></script>
</body>
</html>"""


def build():
    with open(LESSON_DATA, encoding="utf-8") as f:
        lessons = json.load(f)

    READER_DIR.mkdir(parents=True, exist_ok=True)
    (READER_DIR / "style.css").write_text(CSS, encoding="utf-8")
    (READER_DIR / "progress.js").write_text(PROGRESS_JS, encoding="utf-8")
    (READER_DIR / "reading.js").write_text(READING_JS, encoding="utf-8")
    (READER_DIR / ".nojekyll").touch()
    (READER_DIR / "index.html").write_text(index_page(lessons), encoding="utf-8")

    count = 0
    for book in BOOK_ORDER:
        if book not in lessons:
            continue
        book_dir = READER_DIR / book
        book_dir.mkdir(exist_ok=True)
        for num, lesson in lessons[book].items():
            path = book_dir / f"lesson-{int(num):02d}.html"
            path.write_text(lesson_page(book, num, lesson, lessons), encoding="utf-8")
            count += 1

    print(f"✅ Built {count} lessons + index → {READER_DIR}")
    print("   GitHub Pages: repo Settings → Pages → Deploy from /docs on main")


if __name__ == "__main__":
    build()
