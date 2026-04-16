# Pegion Defence

This project will contain all the digital assets required to setup and operate an automatic water/laser turret against pegions to defend some physical area

## Webpam preview

If you don't have a webcam, run a fake webcam feed:

```
./scripts/fake-webcam.sh
```

Then run the python script

```
uv run python webcam-feed.py
```

## Webcam pegion detection

```
uv run python detection.py
```

## Plan

### Phase 1 - Image recognition - DELIVERED

Deliverables: A desktop application that can detect a pegion in a static image

Goals:

- Gain understanding regarding the technology involved in image recognition of pegions

### Phase 2 - Video recognition - DELIVERED

Deliverables: A desktop application that can detect a pegion in a video playback

Goals:

- Figure out how to chop video into image frames and feed it to the detection algorithm
- Figure out if we can track a single pegion as it moves ( "knowing" it is the same pegion )
- Gain insights into the performance required to perform the image recognition on video
- Tinker with performance optimizations, compress video, reduce color depth, reduce framerate etc

### Phase 3 - Stream video

Deliverables: An embeded application that can stream a camera feed to a server.

Goals:

- Gain technical insight into video streaming from low-powered devices
- Gain experience from deploying hardware on the field (how to power them, weather protection, remote access etc)
- Gain architectual insight into whether to perform the image recognition on the server, or the node, or use a hybrid model.

### Phase 4 - Water turret

Deliverables: An embeded application that can shoot a water stream at a distance

Goals:

- Gain technical insight into using pressure to eject water out some tube or turret head
- Gain insight into how the water behaves after being ejected ( how far does it go, air interference )
- Understaind how much water is needed in a reservoir for defending an area

### Phase 5 - Laser turret

Deliverables: An embeded application that can shoot a laser

Goals:

- Validate if lasers actually annoy pegions
- Gain technical insight into shooting a laser beam from a remote device.

### Phase 6 - Manual weapon aiming

Deliverables: An embeded application that allows the user to aim and shoot the weapon

Goals:

- Figure out how to mehcanically aim the weapon
- Figure out how to calibrate the weapon aiming with the camera feed

### Phase 7 - Automatic weapon aiming

Deliverables: An embeded application automatically aims and shoots the weapon

Goals:

- Figure out how to automatically aim the weapon on the detected pegions
