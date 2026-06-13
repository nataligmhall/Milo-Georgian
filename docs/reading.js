document.addEventListener("click", function (e) {
  var btn = e.target.closest("[data-reading-toggle]");
  if (btn) {
    var id = btn.dataset.readingToggle;
    var en = document.getElementById(id + "-en");
    if (!en) return;
    var hidden = en.classList.toggle("hidden");
    btn.textContent = hidden ? "Show translation" : "Hide translation";
    return;
  }
  var audioBtn = e.target.closest("[data-audio-en-toggle]");
  if (audioBtn) {
    var en2 = document.getElementById(audioBtn.dataset.audioEnToggle);
    if (!en2) return;
    var h = en2.classList.toggle("hidden");
    audioBtn.textContent = h ? "What does it mean? (not lesson vocab)" : "Hide meaning";
  }
});
