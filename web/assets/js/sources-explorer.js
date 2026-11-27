"use strict";
function matchesSource(countries, category, selectedCountry, selectedCategory) {
  return (selectedCountry === "all" || countries.split(" ").includes(selectedCountry)) &&
    (selectedCategory === "all" || category === selectedCategory);
}
(function () {
  const panel = document.getElementById("source-filters");
  if (!panel) return;
  const country = document.getElementById("source-country");
  const category = document.getElementById("source-category");
  const cards = Array.from(document.querySelectorAll("[data-source-id]"));
  const count = document.getElementById("source-count");
  const empty = document.getElementById("source-empty");
  function refresh() {
    let visible = 0;
    for (const card of cards) {
      const show = matchesSource(card.dataset.countries, card.dataset.category, country.value, category.value);
      card.hidden = !show;
      if (show) visible += 1;
    }
    count.textContent = count.dataset.label + ": " + visible + " / " + cards.length;
    empty.hidden = visible !== 0;
  }
  country.addEventListener("change", refresh);
  category.addEventListener("change", refresh);
  document.getElementById("source-reset").addEventListener("click", function () {
    country.value = "all"; category.value = "all"; refresh();
  });
  panel.hidden = false;
  refresh();
})();
