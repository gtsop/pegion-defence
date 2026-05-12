import subprocess
import time

class FFmpegWriter():
    def __init__(self, width, height, fps, out_dir):
        self.width = width
        self.height = height
        self.fps = fps
        self.proc = None
        self.out_dir = out_dir

    def write(self, frame):
        if self.proc is None:
            self.proc = self.init_process()

        if self.proc.poll() is not None:
            self.proc = self.init_process()

        try:
            self.proc.stdin.write(frame.tobytes())
        except BrokenPipeError:
            self.clean_process()

    def stop(self):
        self.clean_process()
        self.proc = None

    def init_process(self):
        return subprocess.Popen(
            self.__ffmpeg_cmd(),
            stdin=subprocess.PIPE,
            stdout=None,
            stderr=None,
            bufsize=0,
        )

    def clean_process(self):
        if self.proc.poll() is not None:
            return

        try:
            self.proc.stdin.close()
        except Exception:
            pass

        try:
            self.proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.proc.kill()
                self.proc.wait()

        
    def __ffmpeg_cmd(self):
        return [
            "ffmpeg",
            "-hide_banner",
            "-loglevel", "warning",
            "-y",
            "-f", "rawvideo",
            "-pix_fmt", "bgr24",
            "-video_size", f"{self.width}x{self.height}",
            "-framerate", str(self.fps),
            "-i", "-",
            "-b:v", "300k",
            "-f", "segment",
            "-segment_time", "60",
            "-reset_timestamps", "1",
            "-strftime", "1",
            "-g", "50",
            self.out_dir + "/recording_%y-%m-%d_%H-%M-%S.mp4",
        ]
