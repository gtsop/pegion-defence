 #!/usr/bin/env bash

sudo modprobe v4l2loopback devices=1 video_nr=10 card_label="VirtualCam"

 ffmpeg -re -stream_loop -1 -i ./videos/vice-pegions-short.mp4 -f v4l2 /dev/video10
