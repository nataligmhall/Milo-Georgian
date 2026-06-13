(function () {
  const KEY = "milo-hard-words";

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || "{}"); }
    catch (e) { return {}; }
  }

  function save(data) {
    localStorage.setItem(KEY, JSON.stringify(data));
    syncFlags(data);
    renderBank(data);
  }

  function wordKey(book, lesson, ge) {
    return book + "-" + lesson + "-" + ge;
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

  function renderBank(data) {
    var root = document.getElementById("hard-words-bank");
    if (!root) return;
    var keys = Object.keys(data).filter(function (k) { return data[k]; });
    var countEl = document.getElementById("hard-bank-count");
    if (countEl) countEl.textContent = keys.length ? keys.length + " word" + (keys.length === 1 ? "" : "s") : "";
    if (!keys.length) {
      root.innerHTML = '<p class="hard-bank-empty">No flagged words yet. Tap ⚑ on any vocab card in a lesson.</p>';
      return;
    }
    keys.sort(function (a, b) {
      var da = data[a], db = data[b];
      if (da.book !== db.book) return da.book < db.book ? -1 : 1;
      if (da.lesson !== db.lesson) return parseInt(da.lesson, 10) - parseInt(db.lesson, 10);
      return a < b ? -1 : 1;
    });
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

  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".hard-flag-btn");
    if (btn) {
      e.preventDefault();
      var id = btn.dataset.wordId;
      if (!id) return;
      var data = load();
      if (data[id]) {
        delete data[id];
      } else {
        data[id] = {
          ge: btn.dataset.ge || "",
          en: btn.dataset.en || "",
          rom: btn.dataset.rom || "",
          ru: btn.dataset.ru || "",
          book: btn.dataset.book || "",
          lesson: btn.dataset.lesson || ""
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
    }
  });

  var initial = load();
  syncFlags(initial);
  renderBank(initial);
})();
