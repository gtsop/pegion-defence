 ffmpeg -re -stream_loop -1 -i ./videos/vice-pegions-short.mp4 -c copy -f rtsp rtsp://localhost:8554/mystream
