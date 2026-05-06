import cv2
import linuxpy.video.device as video_device

def get_webcams():
    webcams = []

    for device in video_device.iter_video_capture_devices():

        with device:
            caps = dir(device.info.capabilities)

            if "bcm2835" in str(device.info.card):
                continue

            if "VIDEO_CAPTURE" in caps or "VIDEO_CAPTURE_MPLANE" in caps:
                webcams.append(device)

    return sorted(webcams, key=lambda d: str(d.filename))

def get_capture():
    cameras = get_webcams()

    # Auto-select the first camera if it exists
    if len(cameras) == 0:
        return None

    camera = cameras[0]

    index = int(camera.filename.name.replace("video", ""))

    cap = cv2.VideoCapture(index, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 10)

    return cap


