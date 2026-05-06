from types import SimpleNamespace
from .utils import get_webcams, get_capture

import linuxpy.video.device as video_device

def mock_cameras(monkeypatch, cameras):
    monkeypatch.setattr(video_device, "iter_video_capture_devices", lambda: iter(cameras))

class FakeDevice:
    def __init__(self, filename="/dev/video0", card="USB Camera", capabilities=None):
        self.filename = filename
        self.info = SimpleNamespace(
            card=card,
            capabilities=SimpleNamespace(**(capabilities or {"VIDEO_CAPTURE": True}))
        )

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return None
    
camera0 = FakeDevice(filename="/dev/video-1")
camera1 = FakeDevice(filename="/dev/video1")
bcm2835 = FakeDevice(filename="/dev/video27", card="bcm2835")

class TestGetWebcams:
    def test_returns_empty_array(self, monkeypatch):
        mock_cameras(monkeypatch, [])

        cameras = get_webcams()
        assert cameras == []

    def test_returns_camera(self, monkeypatch):
        mock_cameras(monkeypatch, [camera0])

        cameras = get_webcams()
        assert cameras == [camera0]

    def test_ignores_bcm2835_cameras(self, monkeypatch):
        mock_cameras(monkeypatch, [camera0, bcm2835])

        cameras = get_webcams()
        assert cameras == [camera0]

    def test_sorts_by_name(self, monkeypatch):
        mock_cameras(monkeypatch, [camera1, camera0])

        cameras = get_webcams()
        assert cameras == [camera0, camera1]

