import os
import time

from .ffmpeg import FFmpegWriter
from .logger import log

VIDEO_DIR = "/var/lib/pd-node/videos"
os.makedirs(VIDEO_DIR, exist_ok=True)

def thread(state):

    writer = None

    while True:
        if not state.recorder.is_running():
            if writer is not None:
                write_frames(state, writer)
                writer.stop()
                writer = None
                print("Saved video")
            time.sleep(2)
            continue

        if writer is None:
            writer = FFmpegWriter(640, 480, 10, VIDEO_DIR)

        write_frames(state, writer)
        
        time.sleep(.5)

def write_frames(state, writer):
    frames = state.recorder.get_frames()
    for frame in frames:
        writer.write(frame)


def get_video_dir():
    return os.environ.get("PD_VIDEO_DIR") or "/var/lib/pd-node/videos"

def init_video_dir():
    
    video_dir = get_video_dir()

    # Ensure the directory exists
    try:
        os.makedirs(video_dir, exists_ok=True)
    except PermissionError:
        log(video_dir, ": Directory does not exist")
        log(video_dir, ": Process does not have permission to create this directory")
        
        
        

    
