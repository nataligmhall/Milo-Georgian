document.addEventListener("click", function (e) {
  var btn = e.target.closest("[data-reading-toggle]");
  if (!btn) return;
  var id = btn.dataset.readingToggle;
  var en = document.getElementById(id + "-en");
  if (!en) return;
  var hidden = en.classList.toggle("hidden");
  btn.textContent = hidden ? "Show translation" : "Hide translation";
});
