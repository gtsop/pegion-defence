document.addEventListener("DOMContentLoaded", function () {
  renderTimeline();
});

const finishTime = new Date();
let startTime = new Date();

async function listVideos() {
  const response = await get("/recorder/videos");
  const videos = await response.json();

  return videos.sort((a, b) => {
    if (a.created_at > b.created_at) return -1;
    if (a.created_at < b.created_at) return 1;
    return 0;
  });
}

function findVideoContainingTimestamp(videos, time) {
  return videos.find((video) => {
    return Math.floor(video.created_at) <= Math.floor(time.getTime() / 1000);
  });
}

async function renderTimeline() {
  const timeline = $("#timeline");
  const cursor = $("#timeline__cursor");
  const cursorLegend = $("#timeline__cursor__legend");

  const videos = await listVideos();
  startTime = new Date(videos[videos.length - 1].created_at * 1000);

  videos.forEach(renderVideoMarker);

  timeline.addEventListener("mousemove", function (e) {
    const rect = timeline.getBoundingClientRect();
    const left = e.clientX - rect.left;

    cursor.style.left = left + "px";

    const timelineWidth = rect.width;
    const totalSecondsInTimeline = Math.floor(
      (finishTime.getTime() - startTime.getTime()) / 1000,
    );
    const secondsPerPixel = totalSecondsInTimeline / rect.width;

    const cursorTime = new Date(
      startTime.getTime() + left * secondsPerPixel * 1000,
    );

    const formatted = new Intl.DateTimeFormat("sv-SE", {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    }).format(cursorTime);

    cursorLegend.textContent = formatted;
  });

  timeline.addEventListener("click", function (e) {
    const rect = timeline.getBoundingClientRect();
    const left = e.clientX - rect.left;

    cursor.style.left = left + "px";

    const timelineWidth = rect.width;
    const totalSecondsInTimeline = Math.floor(
      (finishTime.getTime() - startTime.getTime()) / 1000,
    );
    const secondsPerPixel = totalSecondsInTimeline / rect.width;

    const cursorTime = new Date(
      startTime.getTime() + left * secondsPerPixel * 1000,
    );

    //const video = findVideoContainingTimestamp(videos, cursorTime);

    //const newSrc = API_URL + "/recorder/videos/" + video.name;
    const newSrc =
      API_URL + "/api/stream/playback/" + Math.floor(cursorTime / 1000);
    $("#live").src = newSrc;
  });

  renderDayMarkers();
}

function timeToOffsetX(time) {
  const timeline = $("#timeline");
  const rect = timeline.getBoundingClientRect();

  const timelineWidth = rect.width;
  const totalSecondsInTimeline = Math.floor(
    (finishTime.getTime() - startTime.getTime()) / 1000,
  );
  const secondsPerPixel = totalSecondsInTimeline / rect.width;

  const pixelsPerSecond = rect.width / totalSecondsInTimeline;

  const seconds = Math.floor((time.getTime() - startTime.getTime()) / 1000);

  return seconds * pixelsPerSecond;
}

function renderDayMarkers() {
  const timeline = $("#timeline");

  const today = startOfDay(finishTime);

  let day = finishTime;

  while (renderDayMarker(startOfDay(day))) {
    day = removeDays(day, 1);
  }
}

function renderDayMarker(date) {
  const offsetX = timeToOffsetX(date);

  if (offsetX < 0) {
    return false;
  }

  const marker = document.createElement("div");
  marker.className = "timeline__marker--day";
  marker.style.left = offsetX + "px";

  const label = new Intl.DateTimeFormat("sv-SE", {
    month: "2-digit",
    day: "2-digit",
  }).format(date);
  marker.textContent = label;

  timeline.appendChild(marker);

  return true;
}

function removeDays(date, days) {
  const ret = new Date(date);
  ret.setDate(ret.getDate() - days);

  return ret;
}

function startOfDay(date) {
  const ret = new Date(date);
  ret.setHours(0);
  ret.setMinutes(0);
  ret.setSeconds(0);
  ret.setMilliseconds(0);

  return ret;
}

function renderVideoMarker(video) {
  const date = new Date(video.created_at * 1000);
  const offsetX = timeToOffsetX(date);

  if (offsetX < 0) {
    return;
  }

  const timeline = $("#timeline");

  const marker = document.createElement("div");
  marker.className = "timeline__marker timeline__marker--video";
  marker.style.left = offsetX + "px";
  timeline.appendChild(marker);
}
