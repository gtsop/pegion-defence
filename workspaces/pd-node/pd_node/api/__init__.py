from fastapi import APIRouter

api = APIRouter(prefix="/api")

@api.get("/status")
def status():
    return { "ok": True }

