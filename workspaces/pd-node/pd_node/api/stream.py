from datetime import datetime
from pathlib import Path
import asyncio
import subprocess

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import cv2

from .state import app_state
from pd_node.engines.recorder.utils import get_video_dir
from pd_node.utils import get_base_path, stream_video

stream_api = APIRouter(prefix="/stream")

@stream_api.get("/live")
async def live():
    return StreamingResponse(
        stream_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame",
    )

@stream_api.get("/playback/{timestamp}")
async def playback(timestamp):

    timestamp = int(timestamp)

    video_dir = Path(get_video_dir())

    videos = []

    for path in video_dir.iterdir():
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".mp4"}:
            continue

        start_time = path.name.replace("recording_", "").replace(".mp4", "")

        try:
            start_time = datetime.strptime(start_time, "%y-%m-%d_%H-%M-%S").timestamp()
        except Exception:
            continue

        videos.append({
            "filename": path.name,
            "start_time": start_time
        })

    videos.sort(key=lambda v: v["start_time"], reverse=True)

    wanted_video = None
    for video in videos:
        if video["start_time"] <= timestamp:
            wanted_video = video
            break;
    
    if wanted_video:
        print("Will stream video", wanted_video["filename"])
        return StreamingResponse(
            stream_video(video_dir / wanted_video["filename"]),
            media_type="multipart/x-mixed-replace; boundary=frame"
        )
    else:
        return { "ok": False }

async def stream_frames():
    while True:
        try:
            frame = app_state.composer.get_frame()

            if frame is None:
                await asyncio.sleep(1/15)
                continue

            ok, buffer = cv2.imencode(".jpg", frame)

            if not ok:
                await asyncio.sleep(1/15)
                continue

            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n"
            )

            await asyncio.sleep(1/15)

        except asyncio.CancelledError:
            print("stream disconnected")
            raise
        except FileNotFoundError:
            pass

