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
    var html = '<div class="hard-bank-grid">';
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
      html += '<div class="hb-actions"><a href="' + href + '">Open lesson</a>';
      html += '<button type="button" class="hb-remove" data-remove-hard="' + id + '">Remove</button></div></div>';
    });
    html += "</div>";
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
