#!/usr/bin/env python3
"""
Build mobile-friendly lesson reader for GitHub Pages.

Output: docs/  (enable Pages → Deploy from branch main, folder /docs)

    python3 build_reader_site.py
    git add docs && git commit -m "Update lesson reader" && git push
"""

import html
import json
import random
import shutil
from pathlib import Path

from config import CLIPS_DIR, DATASET, LESSON_DATA, READER_DIR, TRANSLATIONS, romanize
from level_placement import BOOK_LABELS
from reader_extras import merge_reader_extras
from reader_theme import BOOK_ZINE, CSS, CULTURE_TAGS, FONTS_HEAD
from worksheet import build_worksheet_exercises

BOOK_ORDER = ("a1", "a2", "a2plus", "b1")
GE_DIR = Path(__file__).resolve().parent
LOGO_SRC = GE_DIR / "assets" / "milo-logo.png"

FAVICON_INDEX = """\
<link rel="icon" type="image/png" sizes="512x512" href="favicon.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">"""

FAVICON_LESSON = """\
<link rel="icon" type="image/png" sizes="512x512" href="../favicon.png">
<link rel="apple-touch-icon" href="../apple-touch-icon.png">"""

# CSS lives in reader_theme.py — stub removed below

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

HARD_WORDS_JS = """\
(function () {
  const KEY = "milo-hard-words";
  var flashKeys = [];
  var flashIdx = 0;
  var flashFlipped = false;

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || "{}"); }
    catch (e) { return {}; }
  }

  function save(data) {
    localStorage.setItem(KEY, JSON.stringify(data));
    syncFlags(data);
    renderBank(data);
    updateFlashStart(data);
  }

  function sortedKeys(data) {
    return Object.keys(data).filter(function (k) { return data[k]; }).sort(function (a, b) {
      var da = data[a], db = data[b];
      if (da.book !== db.book) return da.book < db.book ? -1 : 1;
      if (da.lesson !== db.lesson) return parseInt(da.lesson, 10) - parseInt(db.lesson, 10);
      return a < b ? -1 : 1;
    });
  }

  function syncFlags(data) {
    document.querySelectorAll(".hard-flag-btn").forEach(function (btn) {
      var id = btn.dataset.wordId;
      var on = !!(id && data[id]);
      btn.classList.toggle("flagged", on);
      btn.textContent = on ? "🚩" : "⚑";
      var card = btn.closest(".vocab-card");
      if (card) card.classList.toggle("flagged", on);
    });
  }

  function updateFlashStart(data) {
    var btn = document.getElementById("flash-start-btn");
    if (!btn) return;
    var n = sortedKeys(data).length;
    btn.disabled = n === 0;
    btn.textContent = n ? "Start flashcards (" + n + ")" : "Start flashcards";
  }

  function renderBank(data) {
    var root = document.getElementById("hard-words-bank");
    if (!root) return;
    var keys = sortedKeys(data);
    var countEl = document.getElementById("hard-bank-count");
    if (countEl) countEl.textContent = keys.length ? keys.length + " word" + (keys.length === 1 ? "" : "s") : "";
    updateFlashStart(data);
    if (!keys.length) {
      root.innerHTML = '<p class="hard-bank-empty">No flagged words yet. Tap ⚑ on any vocab card in a lesson.</p>';
      return;
    }
    var html = "";
    if (keys.length > 2) {
      html += '<p class="hard-bank-hint">Swipe sideways to browse →</p>';
    }
    html += '<div class="hard-bank-scroll"><div class="hard-bank-grid">';
    keys.forEach(function (id) {
      var w = data[id];
      var href = w.book + "/lesson-" + String(w.lesson).padStart(2, "0") + ".html";
      var ru = w.ru ? " · " + w.ru : "";
      var enId = "hb-en-" + id.replace(/[^a-zA-Z0-9_-]/g, "_");
      html += '<div class="hard-bank-card" data-word-id="' + id + '">';
      html += '<div class="hb-ge">' + w.ge + '</div>';
      html += '<div class="hb-meta"><code>' + (w.rom || "") + '</code>' + ru + '</div>';
      html += '<button type="button" class="hb-show" data-show-en="' + enId + '">Show meaning</button>';
      html += '<div class="hb-en hidden" id="' + enId + '">' + (w.en || "") + '</div>';
      html += '<div class="hb-meta">' + w.book.toUpperCase() + " L" + w.lesson + '</div>';
      html += '<div class="hb-actions"><a href="' + href + '">Lesson</a>';
      html += '<button type="button" class="hb-remove" data-remove-hard="' + id + '">✕</button></div></div>';
    });
    html += "</div></div>";
    root.innerHTML = html;
  }

  function renderFlashCard() {
    var data = load();
    var card = document.getElementById("flash-card");
    var counter = document.getElementById("flash-counter");
    if (!card || !flashKeys.length) return;
    var w = data[flashKeys[flashIdx]];
    if (!w) return;
    flashFlipped = false;
    if (counter) counter.textContent = (flashIdx + 1) + " / " + flashKeys.length;
    var ru = w.ru ? '<div class="fc-meta">🇷🇺 ' + w.ru + "</div>" : "";
    card.innerHTML =
      '<div class="fc-ge">' + w.ge + '</div>' +
      '<div class="fc-rom">' + (w.rom || "") + '</div>' +
      '<div class="fc-hint">Tap to flip</div>' +
      '<div class="fc-back hidden">' +
      '<div class="fc-en">' + (w.en || "") + '</div>' + ru +
      '<div class="fc-meta">' + w.book.toUpperCase() + " L" + w.lesson + '</div></div>';
    document.getElementById("flash-prev").disabled = flashIdx === 0;
    document.getElementById("flash-next").disabled = flashIdx >= flashKeys.length - 1;
  }

  function openFlash() {
    var data = load();
    flashKeys = sortedKeys(data);
    if (!flashKeys.length) return;
    flashIdx = 0;
    document.getElementById("flash-overlay").classList.add("open");
    document.body.style.overflow = "hidden";
    renderFlashCard();
  }

  function closeFlash() {
    document.getElementById("flash-overlay").classList.remove("open");
    document.body.style.overflow = "";
  }

  function flipFlash() {
    var back = document.querySelector("#flash-card .fc-back");
    var hint = document.querySelector("#flash-card .fc-hint");
    if (!back) return;
    flashFlipped = !flashFlipped;
    back.classList.toggle("hidden", !flashFlipped);
    if (hint) hint.classList.toggle("hidden", flashFlipped);
  }

  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".hard-flag-btn");
    if (btn) {
      e.preventDefault();
      var id = btn.dataset.wordId;
      if (!id) return;
      var data = load();
      if (data[id]) delete data[id];
      else {
        data[id] = {
          ge: btn.dataset.ge || "", en: btn.dataset.en || "",
          rom: btn.dataset.rom || "", ru: btn.dataset.ru || "",
          book: btn.dataset.book || "", lesson: btn.dataset.lesson || ""
        };
      }
      save(data);
      return;
    }
    var rm = e.target.closest("[data-remove-hard]");
    if (rm) {
      var data2 = load();
      delete data2[rm.dataset.removeHard];
      save(data2);
      return;
    }
    var show = e.target.closest("[data-show-en]");
    if (show) {
      var el = document.getElementById(show.dataset.showEn);
      if (!el) return;
      var hid = el.classList.toggle("hidden");
      show.textContent = hid ? "Show meaning" : "Hide meaning";
      return;
    }
    if (e.target.id === "flash-start-btn") { openFlash(); return; }
    if (e.target.id === "flash-close") { closeFlash(); return; }
    if (e.target.id === "flash-overlay") { closeFlash(); return; }
    if (e.target.closest("#flash-card")) { flipFlash(); return; }
    if (e.target.id === "flash-prev" && flashIdx > 0) {
      flashIdx--; renderFlashCard(); return;
    }
    if (e.target.id === "flash-next" && flashIdx < flashKeys.length - 1) {
      flashIdx++; renderFlashCard(); return;
    }
    if (e.target.id === "flash-shuffle") {
      for (var i = flashKeys.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var t = flashKeys[i]; flashKeys[i] = flashKeys[j]; flashKeys[j] = t;
      }
      flashIdx = 0; renderFlashCard();
    }
  });

  document.addEventListener("keydown", function (e) {
    var ov = document.getElementById("flash-overlay");
    if (!ov || !ov.classList.contains("open")) return;
    if (e.key === "Escape") closeFlash();
    if (e.key === "ArrowLeft" && flashIdx > 0) { flashIdx--; renderFlashCard(); }
    if (e.key === "ArrowRight" && flashIdx < flashKeys.length - 1) { flashIdx++; renderFlashCard(); }
    if (e.key === " ") { e.preventDefault(); flipFlash(); }
  });

  var initial = load();
  syncFlags(initial);
  renderBank(initial);
})();
"""

SENTENCE_BUILDER_JS = """\
(function () {
  document.querySelectorAll(".sb-exercise").forEach(function (ex) {
    var answered = false;
    var full = ex.dataset.full || "";
    ex.querySelectorAll(".sb-choice").forEach(function (btn) {
      btn.addEventListener("click", function () {
        if (answered) return;
        answered = true;
        var ok = btn.dataset.correct === "1";
        btn.classList.add(ok ? "sb-right" : "sb-wrong");
        if (!ok) {
          var right = ex.querySelector('.sb-choice[data-correct="1"]');
          if (right) right.classList.add("sb-right");
        }
        var fb = ex.querySelector(".sb-feedback");
        if (fb) {
          fb.textContent = ok ? "✓ " + full : "✗ Correct: " + full;
          fb.className = "sb-feedback " + (ok ? "sb-ok" : "sb-bad");
        }
        ex.querySelectorAll(".sb-choice").forEach(function (b) {
          if (b.dataset.correct !== "1" && b !== btn) b.disabled = true;
        });
      });
    });
  });
})();
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
      if (el.classList.contains("lesson-row") || el.classList.contains("lesson-card-wrap")) {
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
      const pill = document.getElementById("progress-pill");
      if (summary) summary.textContent = doneCount + " / " + total + " lessons";
      if (pill) pill.textContent = doneCount + " / " + total;
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
    return f"<section><h2>Phrases &amp; dialogues</h2>{''.join(items)}</section>"


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
    return f'<section class="can-do"><h2>After this lesson you can…</h2><ul>{lis}</ul></section>'


def focus_verb_html(lesson):
    v = lesson.get("focus_verb")
    if not v:
        return ""
    rows = v.get("rows") or []
    body = "".join(
        f'<tr><td>{esc(r[0])}</td><td class="cell-ge">{esc(r[1])}</td>'
        f'<td>{esc(r[2]) if len(r) > 2 else ""}</td></tr>'
        for r in rows
    )
    tense = v.get("tense", "Present")
    note = v.get("note") or ""
    note_html = f'<p class="verb-note">{esc(note)}</p>' if note else ""
    return (
        f'<section class="focus-verb">'
        f'<h2>Verb focus — {esc(v["ge"])}</h2>'
        f'<p class="verb-meta">{esc(v["en"])} · <b>{esc(tense)}</b> '
        f'— <code>{esc(romanize(v["ge"]))}</code></p>'
        f'<div class="verb-table-wrap"><table class="verb-table">'
        f"<thead><tr><th>Person</th><th>Georgian</th><th>English</th></tr></thead>"
        f"<tbody>{body}</tbody></table></div>{note_html}</section>"
    )


def practice_audio_html(lesson):
    audio = lesson.get("practice_audio")
    if not audio or not audio.get("file"):
        return ""
    en = (audio.get("en") or "").strip()
    en_block = f'<div class="audio-en">→ {esc(en)}</div>' if en else ""
    disclaimer = (
        "This clip is from <b>Mozilla Common Voice</b> — free, royalty-free recordings "
        "by native Georgian speakers. It's here for <b>listening and pronunciation practice only</b>: "
        "the sentence isn't lesson vocabulary and you don't need to memorize it. "
        "Listen, repeat aloud, and train your ear."
    )
    return (
        f'<section class="practice-audio">'
        f"<h2>Pronunciation practice</h2>"
        f'<div class="audio-disclaimer">{disclaimer}</div>'
        f'<div class="audio-clip-card">'
        f'<audio controls preload="none" src="../audio/{esc(audio["file"])}"></audio>'
        f'<div class="audio-ge">{esc(audio.get("ge", ""))}</div>'
        f'<div class="audio-rom">{esc(audio.get("rom", ""))}</div>'
        f"{en_block}</div></section>"
    )


def quiz_prompt_html(prompt):
    """Turn worksheet prompt markup into safe HTML."""
    p = esc(prompt)
    p = p.replace("&lt;b&gt;", "<strong>").replace("&lt;/b&gt;", "</strong>")
    p = p.replace("&lt;code&gt;", '<span class="sb-ge-inline">').replace(
        "&lt;/code&gt;", "</span>"
    )
    return p.replace("\n", "<br>")


def mc_choice_buttons(choices, answer, seed):
    rng = random.Random(seed)
    opts = list(choices)
    rng.shuffle(opts)
    buttons = []
    for opt in opts:
        correct = "1" if opt == answer else "0"
        buttons.append(
            f'<button type="button" class="sb-choice" data-correct="{correct}">'
            f"{esc(opt)}</button>"
        )
    return "".join(buttons)


def quiz_section_html(lesson, book, num, vocab):
    """Interactive multiple-choice: sentence gaps + vocab/grammar drills."""
    items = []

    for i, ex in enumerate(lesson.get("sentence_builder") or []):
        opts = list(ex["options"])
        rng = random.Random(f"{book}-{num}-sb-{i}")
        rng.shuffle(opts)
        tpl = esc(ex["template"])
        display = tpl.replace("___", '<span class="sb-gap">___</span>')
        full = esc(ex["template"].replace("___", ex["answer"]))
        buttons = []
        for opt in opts:
            correct = "1" if opt == ex["answer"] else "0"
            buttons.append(
                f'<button type="button" class="sb-choice" data-correct="{correct}">'
                f"{esc(opt)}</button>"
            )
        items.append(
            f'<div class="sb-exercise" data-full="{full}">'
            f'<p class="sb-prompt">{esc(ex["en"])}</p>'
            f'<div class="sb-template">{display}</div>'
            f'<div class="sb-choices">{"".join(buttons)}</div>'
            f'<p class="sb-feedback hidden"></p></div>'
        )

    for i, ex in enumerate(build_worksheet_exercises(lesson, vocab)):
        answer = ex["answer"]
        items.append(
            f'<div class="sb-exercise" data-full="{esc(answer)}">'
            f'<p class="sb-prompt">{quiz_prompt_html(ex["prompt"])}</p>'
            f'<div class="sb-choices">{mc_choice_buttons(ex["choices"], answer, f"{book}-{num}-ws-{i}")}</div>'
            f'<p class="sb-feedback hidden"></p></div>'
        )

    if not items:
        return ""

    n = len(items)
    return (
        f'<section class="quiz-section"><h2>Quick test</h2>'
        f'<p class="sub" style="margin:-0.35rem 0 0.75rem">'
        f"Tap the correct answer — {n} questions.</p>"
        f'{"".join(items)}</section>'
    )


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
        f"<section><h2>Short reading</h2>"
        f'<div class="reading-card">'
        f'<div class="reading-ge">{esc(reading["ge"])}</div>'
        f"{toggle}{en_block}</div></section>"
    )


def vocab_card(v, book, num):
    rom = v.get("rom") or romanize(v["ge"])
    ru = v.get("ru", "")
    ru_div = f'<div class="vocab-ru">🇷🇺 {esc(ru)}</div>' if ru else ""
    wid = f"{book}-{num}-{v['ge']}"
    return (
        f'<div class="vocab-card" data-word-id="{esc(wid)}">'
        f'<button type="button" class="hard-flag-btn" aria-label="Flag as hard word" '
        f'data-word-id="{esc(wid)}" data-ge="{esc(v["ge"])}" data-en="{esc(v["en"])}" '
        f'data-rom="{esc(rom)}" data-ru="{esc(ru)}" data-book="{esc(book)}" '
        f'data-lesson="{esc(num)}">⚑</button>'
        f'<div class="vocab-ge">{esc(v["ge"])}</div>'
        f'<div class="vocab-rom">{esc(rom)}</div>'
        f'<div class="vocab-en">{esc(v["en"])}</div>{ru_div}</div>'
    )


def vocab_sections(vocab, book, num):
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
        cards.append(vocab_card(v, book, num))
    if cards:
        groups.append(
            f'<div class="vocab-group"><h3>{esc(current)}</h3>'
            f'<div class="vocab-grid">{"".join(cards)}</div></div>'
        )
    return "\n".join(groups)


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
{FAVICON_LESSON}
{FONTS_HEAD}
<link rel="stylesheet" href="../style.css">
</head>
<body data-lesson="{lesson_id}">
<div class="wrap">
{nav_links(book, num, lessons)}
<header class="lesson-header">
  <p class="lesson-kicker">GEO · FL · {esc(book.upper())} · LESSON {int(num):02d}</p>
  <h1>{esc(lesson.get('title', ''))}</h1>
  <p class="sub">{esc(label)} · {len(vocab)} words</p>
  <label class="lesson-done-toggle"><input type="checkbox" class="lesson-done-cb" data-lesson="{lesson_id}"> Mark complete</label>
</header>
{can_do_html(lesson)}
{focus_verb_html(lesson)}
<section>
  <h2>Grammar</h2>
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
  <h2>Vocabulary</h2>
  <p class="sub" style="margin:-0.35rem 0 0.75rem">Tap ⚑ to flag hard words — they land in your word bank on the homepage.</p>
  {vocab_sections(vocab, book, num)}
</section>
{quiz_section_html(lesson, book, num, vocab)}
{practice_audio_html(lesson)}
<p class="sub" style="margin-top:1.5rem;font-family:var(--mono);font-size:0.68rem;letter-spacing:0.06em;text-transform:uppercase">More audio &amp; quizzes in Telegram · /audio · /quiz</p>
<footer class="page-footer">GEO · FL · აღმართი reader · <a href="https://www.geofl.ge/">geofl.ge</a></footer>
</div>
<script src="../progress.js"></script>
<script src="../hard-words.js"></script>
<script src="../sentence-builder.js"></script>
<script src="../reading.js"></script>
</body>
</html>"""
    return body


def culture_strip_html():
    tags = "".join(f'<span class="culture-tag">{t}</span>' for t in CULTURE_TAGS)
    return f"""<section class="culture-strip" id="culture">
  <p class="culture-kicker">№ 04 — CULTURE SUPPLEMENT</p>
  <h2 class="culture-headline">You're not <em>studying.</em><br>You're packing.</h2>
  <p class="culture-body">Every lesson smuggles in a piece of Georgia — a khinkali fold, a supra toast, a 4&nbsp;a.m. cab driver telling you about his grandmother in Kakheti.</p>
  <div class="culture-tags">{tags}</div>
  <div class="culture-deco" aria-hidden="true">🥟🍷</div>
</section>"""


def syllabus_block_html(book, lessons):
    meta = BOOK_ZINE.get(book, {})
    label = BOOK_LABELS.get(book, book.upper())
    level_code = label.split("—")[0].strip() if "—" in label else book.upper()
    level_name = meta.get("short", label.split("—")[-1].strip() + "." if "—" in label else "")
    issue = meta.get("issue", "01")

    cards = []
    for num in sorted(lessons[book].keys(), key=int):
        les = lessons[book][num]
        href = lesson_href(book, num)
        lid = f"{book}-{num}"
        ge_hint = ""
        phrases = les.get("phrases") or []
        if phrases:
            ge_hint = f'<span class="lesson-card-ge">{esc(phrases[0]["ge"])}</span>'
        cards.append(
            f'<li class="lesson-card-wrap" data-lesson="{lid}">'
            f'<div class="lesson-card">'
            f'<button type="button" class="done-btn" data-lesson="{lid}" '
            f'aria-label="Mark lesson complete">○</button>'
            f'<a class="lesson-card-link" href="{href}">'
            f'<span class="lesson-card-num">L{num}</span>'
            f'<span class="lesson-card-body">'
            f'<span class="lesson-card-title">{esc(les.get("title", ""))}</span>'
            f'{ge_hint}'
            f'<span class="lesson-card-meta">CHAPTER {int(num):02d}</span>'
            f'</span>'
            f'<span class="lesson-card-go" aria-hidden="true">→</span>'
            f'</a></div></li>'
        )

    polaroid = (
        f'<div class="syllabus-polaroid">'
        f'<div class="pol-img" aria-hidden="true">⛪</div>'
        f'<p class="pol-cap">{esc(meta.get("polaroid", ""))}</p></div>'
    )
    return (
        f'<section class="syllabus-block" id="syllabus-{book}">'
        f'<p class="syllabus-kicker">№ {issue} — THE SYLLABUS</p>'
        f'<div class="syllabus-head">'
        f'<h2>{esc(level_code)} — <span class="level-red">{esc(level_name)}</span></h2>'
        f'<p class="syllabus-blurb">{esc(meta.get("blurb", ""))}</p>'
        f'{polaroid}</div>'
        f'<ul class="lesson-list">{"".join(cards)}</ul></section>'
    )


def index_page(lessons):
    blocks = []
    total = 0
    for book in BOOK_ORDER:
        if book not in lessons:
            continue
        total += len(lessons[book])
        blocks.append(syllabus_block_html(book, lessons))

    a1 = BOOK_ZINE.get("a1", {})
    sticker_ge = a1.get("sticker_ge", "გამარჯობა")
    sticker_en = a1.get("sticker_en", "HELLO · LESSON 01")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="description" content="Georgian, but make it fun — 48 mobile-first აღმართი lessons with grammar, vocab, and quick tests.">
<title>Georgian, but make it fun — GEO · FL</title>
{FAVICON_INDEX}
{FONTS_HEAD}
<link rel="stylesheet" href="style.css">
</head>
<body data-total-lessons="{total}">
<div class="site">
<header class="masthead">
  <div class="masthead-brand">
    <span class="logo-mark" aria-hidden="true">ა</span>
    <div>
      <span class="masthead-geo">GEO · FL</span>
      <span class="masthead-issue">issue № 01 — winter · აღმართი</span>
    </div>
  </div>
  <span class="progress-pill" id="progress-pill">0 / {total}</span>
  <nav class="masthead-nav" aria-label="Sections">
    <a href="#word-bank">Word bank</a>
    <a href="#lessons">Lessons</a>
    <a href="#culture">Culture</a>
  </nav>
</header>

<section class="hero">
  <p class="hero-start">→ start here</p>
  <div class="hero-tape">A mixed-media reader · აღმართი</div>
  <h1 class="hero-title">Georgian,<br><em>but make</em><br>it <span class="hi-yellow">fun.</span></h1>
  <p class="hero-lede">A pocket-sized zine of <strong>48 lessons</strong>, torn-paper vocab and handwritten grammar notes — same textbook content as <a href="https://www.geofl.ge/" class="squiggle">geofl.ge</a>, re-cut for your phone.</p>
  <div class="hero-cta">
    <a class="btn-primary" href="#lessons">Start speaking →</a>
    <a class="btn-secondary" href="#word-bank">Flip flashcards ★</a>
    <span class="hero-aside">— no PDFs, no nonsense.</span>
  </div>
  <div class="hero-collage" aria-hidden="true">
    <span class="collage-food">🫓</span>
    <div class="collage-sticker">
      <div class="st-ge">{esc(sticker_ge)}</div>
      <div class="st-en">{esc(sticker_en)}</div>
    </div>
    <div class="collage-stamp">
      <span class="stamp-floral">✿</span>
      <span>GEORGIA</span>
    </div>
  </div>
</section>

{culture_strip_html()}

<div class="progress-block">
  <div class="progress-label" id="progress-summary">0 / {total} lessons</div>
  <div class="progress-track"><div class="progress-fill" id="progress-fill"></div></div>
</div>

<section class="hard-bank" id="word-bank">
  <h2>Word bank <span id="hard-bank-count" class="sub-bank"></span></h2>
  <p class="sub-bank">Flagged vocab for review — swipe below, or flip through flashcards. Saved on this device only.</p>
  <div id="hard-words-bank"><p class="hard-bank-empty">No flagged words yet — tap ⚑ on any vocab card.</p></div>
  <button type="button" class="flash-start-btn" id="flash-start-btn" disabled>Start flashcards</button>
</section>

<div id="lessons">{"".join(blocks)}</div>

<p class="site-footer-bar">48 lessons · grammar + vocab · quick tests, no PDFs · <strong>mobile-first</strong></p>
<footer class="page-footer">GEO · FL · aligned with <a href="https://www.geofl.ge/">geofl.ge</a> · აღმართი</footer>
</div>
<div class="flash-overlay" id="flash-overlay">
  <div class="flash-modal" id="flash-modal">
    <div class="flash-top">
      <span id="flash-counter">1 / 1</span>
      <button type="button" class="flash-close" id="flash-close" aria-label="Close">×</button>
    </div>
    <div class="flash-card" id="flash-card"></div>
    <div class="flash-nav">
      <button type="button" id="flash-prev">← Prev</button>
      <button type="button" id="flash-shuffle">Shuffle</button>
      <button type="button" id="flash-next">Next →</button>
    </div>
  </div>
</div>
<script src="progress.js"></script>
<script src="hard-words.js"></script>
</body>
</html>"""


def lesson_linear_index(book, num):
    idx = 0
    for b in BOOK_ORDER:
        if b == book:
            return idx + int(num) - 1
        idx += 12
    return int(num) - 1


def load_translation_map():
    if not TRANSLATIONS.exists():
        return {}
    with open(TRANSLATIONS, encoding="utf-8") as f:
        data = json.load(f)
    out = {}
    for entry in data:
        if isinstance(entry, dict):
            key = Path(entry.get("audio", entry.get("path", ""))).name
            if key:
                out[key] = entry.get("en", entry.get("text", ""))
    return out


def load_audio_pool():
    if not DATASET.exists():
        return []
    with open(DATASET, encoding="utf-8") as f:
        data = json.load(f)
    pool = []
    for entry in data:
        fname = Path(entry["audio"]).name
        if not (CLIPS_DIR / fname).exists():
            continue
        wc = entry.get("word_count", 0)
        if 5 <= wc <= 18:
            pool.append(entry)
    return pool


def prepare_lesson_audio(lessons):
    """Assign one Common Voice clip per lesson; copy MP3s into docs/audio/."""
    pool = load_audio_pool()
    if not pool:
        print("   ⚠️  No audio clips found — skipping practice audio")
        return {}

    trans_map = load_translation_map()
    audio_dir = READER_DIR / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}
    copied = set()

    for book in BOOK_ORDER:
        if book not in lessons:
            continue
        for num in sorted(lessons[book].keys(), key=int):
            li = lesson_linear_index(book, num)
            pick = pool[(li * 997 + 42) % len(pool)]
            fname = Path(pick["audio"]).name
            src = CLIPS_DIR / fname
            if fname not in copied and src.exists():
                shutil.copy2(src, audio_dir / fname)
                copied.add(fname)
            en = (pick.get("en") or trans_map.get(fname, "")).strip()
            manifest[f"{book}-{num}"] = {
                "file": fname,
                "ge": pick["ge"],
                "en": en,
                "rom": romanize(pick["ge"]),
            }

    print(f"   🎧 Copied {len(copied)} Common Voice clips → {audio_dir}")
    return manifest


def build():
    with open(LESSON_DATA, encoding="utf-8") as f:
        lessons = json.load(f)

    READER_DIR.mkdir(parents=True, exist_ok=True)
    if LOGO_SRC.exists():
        shutil.copy2(LOGO_SRC, READER_DIR / "favicon.png")
        shutil.copy2(LOGO_SRC, READER_DIR / "apple-touch-icon.png")
    audio_manifest = prepare_lesson_audio(lessons)
    (READER_DIR / "style.css").write_text(CSS, encoding="utf-8")
    (READER_DIR / "progress.js").write_text(PROGRESS_JS, encoding="utf-8")
    (READER_DIR / "hard-words.js").write_text(HARD_WORDS_JS, encoding="utf-8")
    (READER_DIR / "sentence-builder.js").write_text(SENTENCE_BUILDER_JS, encoding="utf-8")
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
            enriched = dict(lesson)
            key = f"{book}-{num}"
            if key in audio_manifest:
                enriched["practice_audio"] = audio_manifest[key]
            path.write_text(lesson_page(book, num, enriched, lessons), encoding="utf-8")
            count += 1

    print(f"✅ Built {count} lessons + index → {READER_DIR}")
    print("   GitHub Pages: repo Settings → Pages → Deploy from /docs on main")


if __name__ == "__main__":
    build()
