import subprocess
import time

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

pd_proc = None

@app.get("/status")
async def root():
    return {
        "device": "rpi-4-4gb",
        "application": "pegion-defence-node",
        "running": bool(pd_proc),
        "pid": pd_proc.pid if pd_proc else None
    }

@app.post("/start")
async def start():
    global pd_proc

    if pd_proc:
        return { "error": "Process already started" }

    pd_proc = subprocess.Popen(
        ["uv", "run", "rpi_node"],
        start_new_session=True
    )

    return { "message": "Process started" }
    
@app.post("/stop")
async def stop():
    global pd_proc

    if not pd_proc:
        return { "message": "ok" }

    if pd_proc.poll() is None:
        pd_proc.terminate()

    time.sleep(2)

    if pd_proc.poll() is None:
        pd_proc.kill()

    return { "message": "ok" }
