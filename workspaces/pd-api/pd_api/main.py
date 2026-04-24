import subprocess

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
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
