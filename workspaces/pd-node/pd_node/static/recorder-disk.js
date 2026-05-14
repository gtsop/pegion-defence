document.addEventListener("DOMContentLoaded", async function () {
  const response = await get("/recorder/disk/stats");

  const data = await response.json();

  const stats = data.stats;

  document.querySelector(".disk-stats__used").textContent = stats.used;
  document.querySelector(".disk-stats__total").textContent = stats.total;
  document.querySelector(".disk-stats__perc").textContent =
    stats.used_percent + "%";
});
