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


def esc(s):
    return html.escape(str(s or ""))


def lesson_path(book, num):
    return f"{book}/lesson-{int(num):02d}.html"


def nav_links(book, num, lessons):
    nums = sorted(int(k) for k in lessons[book].keys())
    n = int(num)
    parts = ['<nav class="top">', f'<a href="../index.html">All levels</a>']
    if n > nums[0]:
        parts.append(f'<a href="{lesson_path(book, n - 1)}">← L{n - 1}</a>')
    if n < nums[-1]:
        parts.append(f'<a href="{lesson_path(book, n + 1)}">L{n + 1} →</a>')
    else:
        idx = BOOK_ORDER.index(book)
        if idx + 1 < len(BOOK_ORDER) and BOOK_ORDER[idx + 1] in lessons:
            nb = BOOK_ORDER[idx + 1]
            parts.append(f'<a href="{lesson_path(nb, 1)}">{BOOK_LABELS.get(nb, nb)} L1 →</a>')
    parts.append("</nav>")
    return "".join(parts)


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
    g = lesson.get("grammar", {})
    easier = lesson.get("easier_than_russian", "")
    label = BOOK_LABELS.get(book, book.upper())
    vocab = [dict(v, rom=romanize(v["ge"])) for v in lesson.get("vocab", [])]
    easier_block = f'<div class="easier">💚 <b>Easier than Russian:</b> {esc(easier)}</div>' if easier else ""

    body = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<title>{esc(label)} L{num} — {esc(lesson.get('title', ''))}</title>
<link rel="stylesheet" href="../style.css">
</head>
<body>
<div class="wrap">
{nav_links(book, num, lessons)}
<header>
  <div class="brand">აღმართი · Milo reader</div>
  <h1>{esc(label)} — Lesson {num}</h1>
  <p class="sub">{esc(lesson.get('title', ''))} · {len(vocab)} words</p>
</header>
<section>
  <h2>📖 Grammar</h2>
  <div class="card grammar">
    <p>{esc(g.get('en', ''))}</p>
    <p class="ru">🇷🇺 {esc(g.get('ru', ''))}</p>
    <div class="ex-ge">{esc(g.get('example_ge', ''))}</div>
    <div class="ex-en">{esc(g.get('example_en', ''))}</div>
    {easier_block}
  </div>
</section>
<section>
  <h2>📚 Vocabulary</h2>
  {vocab_sections(vocab)}
</section>
{worksheet_html(lesson, vocab)}
<p class="sub" style="margin-top:1.5rem">🎧 Audio &amp; quizzes in Telegram · /audio · /quiz</p>
<footer>Milo Georgian Tutor · synced from lesson_data.json</footer>
</div>
</body>
</html>"""
    return body


def index_page(lessons):
    blocks = []
    for book in BOOK_ORDER:
        if book not in lessons:
            continue
        label = BOOK_LABELS.get(book, book.upper())
        items = []
        for num in sorted(lessons[book].keys(), key=int):
            les = lessons[book][num]
            href = lesson_path(book, num)
            items.append(f'<li><a href="{href}">L{num} — {esc(les.get("title", ""))}</a></li>')
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
<body>
<div class="wrap">
<header>
  <div class="brand">აღმართი · GeoFL</div>
  <h1>Georgian Lesson Reader</h1>
  <p class="sub">Mobile-first აღმართი · 48 lessons · grammar, vocab &amp; worksheets · no PDFs</p>
  <p class="sub" style="margin-top:0.5rem">Faster than <a href="https://www.geofl.ge/">geofl.ge</a> on your phone — same textbook content, built for reading.</p>
</header>
<div class="book-grid">{"".join(blocks)}</div>
<footer>Milo Georgian Tutor · <a href="https://www.geofl.ge/">geofl.ge</a></footer>
</div>
</body>
</html>"""


def build():
    with open(LESSON_DATA, encoding="utf-8") as f:
        lessons = json.load(f)

    READER_DIR.mkdir(parents=True, exist_ok=True)
    (READER_DIR / "style.css").write_text(CSS, encoding="utf-8")
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
