from pathlib import Path
import subprocess
import time

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^http://(localhost|127\.0\.0\.1|192\.168\.\d+\.\d+)(:\d+)?$",
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/start")
async def start():
    return systemctl("start", "pd-daemon")


@app.post("/stop")
async def stop():
    return systemctl("stop", "pd-daemon")


@app.post("/kill")
async def kill():
    return systemctl("kill", "pd-daemon")


@app.post("/status")
async def status():
    return systemctl("status", "pd-daemon")

@app.get("/video")
async def video():
    return StreamingResponse(
        stream_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame",
    )


def stream_frames():
    last_frame = None

    while True:
        try:
            frame = get_frame()

            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
            )
        except FileNotFoundError:
            pass
        time.sleep(1/15)

BASE_DIR = Path(__file__).resolve().parent
PLACEHOLDER_PATH = BASE_DIR / "static" / "no-video.jpg"
FRAME_PATH = Path("/run/pigeon-defence/frame.jpg")

def get_frame():
    try:
        if not FRAME_PATH.exists():
            return PLACEHOLDER
        return FRAME_PATH.read_bytes()
    except Exception:
        return PLACEHOLDER

def systemctl(action, service):
    result = subprocess.run(
        ["systemctl", action, service],
        capture_output=True,
        text=True
    )

    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
