import subprocess
import time

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


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

    pd_proc = subprocess.Popen(
        ["systemcl", "start", "rpi-node"],
        start_new_session=True
    )

    return { "message": "Process started" }
    
@app.post("/stop")
async def stop():
    pd_proc = subprocess.Popen(
        ["systemcl", "stop", "rpi-node"],
        start_new_session=True
    )

    return { "message": "ok" }
