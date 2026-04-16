 #!/usr/bin/env bash

 ffmpeg -re -stream_loop -1 -i ./scripts/fake-feed.mp4 -f v4l2 /dev/video10
