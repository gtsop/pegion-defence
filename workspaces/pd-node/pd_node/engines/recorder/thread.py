import os
import time

from .ffmpeg import FFmpegWriter

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

