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
