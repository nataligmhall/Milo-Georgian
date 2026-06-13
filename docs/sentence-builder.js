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
