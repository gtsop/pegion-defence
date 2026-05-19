from pathlib import Path
import threading

from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse 
import uvicorn

from pd_node.api import api, app_state
from pd_node.utils import get_base_path 
from pd_node.db import create_db_and_tables
from pd_node.engines.recorder.utils import get_video_dir

import pd_node.engines as engines

create_db_and_tables()

app = FastAPI()
app.include_router(api)

app.mount("/static", StaticFiles(directory=get_base_path() / "static"), name="static")

@app.get("/")
def root():
    return FileResponse(get_base_path() / "static/index.html")

@app.post("/video/start")
def video_start():
    app_state.video.start()
    return { "ok": True }

@app.post("/video/stop")
def video_stop():
    app_state.video.stop()
    return { "ok": True }

@app.post("/inference/start")
def inference_start():
    app_state.inference.start()
    return { "ok": True }

@app.post("/inference/stop")
def inference_stop():
    app_state.inference.stop()
    return { "ok": True }

@app.post("/composer/start")
def composer_start():
    app_state.composer.start()
    return { "ok": True }

@app.post("/composer/stop")
def composer_stop():
    app_state.composer.stop()
    return { "ok": True }

@app.get("/engines/status")
def engines_status():
    return {
        "video": app_state.video.is_running(),
        "inference": app_state.inference.is_running(),
        "composer": app_state.composer.is_running(),
        "recorder": app_state.recorder.is_running()
    }

@app.get("/recorder/disk/stats")
def recorder_disk_stats():
    stats = app_state.recorder.get_stats()
    return {
        "ok": True,
        "stats": stats
    }

@app.post("/recorder/start")
def recorder_start():
    app_state.recorder.start()
    return { "ok": True }

@app.post("/recorder/stop")
def recorder_stop():
    app_state.recorder.stop()
    return { "ok": True }

@app.get("/recorder/videos/")
def recorder_videos():
    VIDEO_DIR = Path(get_video_dir())
    videos = []

    for path in VIDEO_DIR.iterdir():
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".mp4"}:
            continue
        stat = path.stat()

        videos.append({
            "name": path.name,
            "created_at": int(stat.st_mtime)
        })

        videos.sort(key=lambda v: v["created_at"], reverse=True)

    return videos

@app.post("/motor/angle")
def motor_angle(params = Body(...)):
    app_state.motor.set_target_angle(params["angle"])
    return {
        "ok": True,
        "angle": params["angle"]
    }

@app.post("/motor/move")
def motor_angle(params = Body(...)):
    app_state.motor.move(params["direction"])
    return {
        "ok": True,
        "direction": params["direction"]
    }

@app.post("/motor/freeze")
def motor_angle(params = Body(...)):
    app_state.motor.freeze(params["direction"])
    return {
        "ok": True,
        "direction": params["direction"]
    }


@app.on_event("startup")
def start_thread():
    video_thread = threading.Thread(target=engines.video.thread, args=(app_state,), daemon=True)
    video_thread.start()

    inference_thread = threading.Thread(target=engines.inference.thread, args=(app_state,), daemon=True)
    inference_thread.start()

    composer_thread = threading.Thread(target=engines.composer.thread, args=(app_state,), daemon=True)
    composer_thread.start()

    recorder_thread = threading.Thread(target=engines.recorder.thread, args=(app_state,), daemon=True)
    recorder_thread.start()

    motor_thread = threading.Thread(target=engines.motor.thread, args=(app_state,), daemon=True)
    motor_thread.start()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


