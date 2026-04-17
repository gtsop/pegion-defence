ffmpeg \
-f v4l2 \
-framerate 30 \
-video_size 1280x720 \
-i /dev/video10 \
-c:v libx264 \
-preset veryfast \
-tune zerolatency \
-pix_fmt yuv420p \
-f mpegts \
"srt://127.0.0.1:9000?mode=listener&transtype=live&latency=200"
