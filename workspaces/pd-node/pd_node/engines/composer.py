import time

import pd_node.utils as utils

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
            utils.draw_bboxes(frame, results.boxes, names)

        utils.draw_fps(frame)
        utils.draw_datetime(frame)

        if state.recorder.is_running():
            state.recorder.push_frame(frame.copy())

        display_frame = frame.copy()
        if state.recorder.is_running():
            utils.draw_recording_indicator(frame)

        state.composer.set_frame(frame)

        time.sleep(1/15)
