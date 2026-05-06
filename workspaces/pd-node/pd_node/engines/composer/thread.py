import time

import pd_node.utils as utils

from .utils import draw_bboxes

def thread(state):
    
    while True:

        if not state.composer.is_running():
            time.sleep(5)
            continue

        frame = state.video.get_frame()
        
        if frame is None:
            time.sleep(1)
            continue

        frame = frame.copy()
        results = state.inference.get_results()

        if results:
            names = state.inference.get_names()
            draw_bboxes(frame, results.boxes, names)

        utils.draw_fps(frame)
        utils.draw_datetime(frame)

        if state.recorder.is_running():
            state.recorder.push_frame(frame.copy())

        if state.recorder.is_running():
            utils.draw_recording_indicator(frame)

        if state.motor.is_moving_left():
            utils.draw_move_left(frame)
        elif state.motor.is_moving_right():
            utils.draw_move_right(frame)

        state.composer.set_frame(frame)

        time.sleep(1/15)
