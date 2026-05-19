from fastapi import APIRouter

from pd_node.api.state import app_state

from pd_node.api.stream import stream_api

api = APIRouter(prefix="/api")
api.include_router(stream_api)

@api.get("/status")
def status():
    return { "ok": True }

