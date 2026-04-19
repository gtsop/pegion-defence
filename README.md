# Pegion Defence

This project will contain all the digital assets required to setup and operate an automatic water/laser turret against pegions to defend some physical area

As of right now, there is a raspberry pi 4 targeted package that detects "birds" using a camera and gives a signal via a pin (eg to open a LED)

[rpi_node](./workspaces/rpi-node/)

## Plan

A high-level list of the remaining things to be researched/developed

### 1. Stream video

Deliverables: An embeded application that can stream a camera feed to a server.

Goals:

- Gain technical insight into video streaming from low-powered devices
- Gain experience from deploying hardware on the field (how to power them, weather protection, remote access etc)
- Gain architectual insight into whether to perform the image recognition on the server, or the node, or use a hybrid model.

### 2. Water turret

Deliverables: An embeded application that can shoot a water stream at a distance

Goals:

- Gain technical insight into using pressure to eject water out some tube or turret head
- Gain insight into how the water behaves after being ejected ( how far does it go, air interference )
- Understaind how much water is needed in a reservoir for defending an area

### 3. Laser turret

Deliverables: An embeded application that can shoot a laser

Goals:

- Validate if lasers actually annoy pegions
- Gain technical insight into shooting a laser beam from a remote device.

### 4. Manual weapon aiming

Deliverables: An embeded application that allows the user to aim and shoot the weapon

Goals:

- Figure out how to mehcanically aim the weapon
- Figure out how to calibrate the weapon aiming with the camera feed

### 4. Automatic weapon aiming

Deliverables: An embeded application automatically aims and shoots the weapon

Goals:

- Figure out how to automatically aim the weapon on the detected pegions
