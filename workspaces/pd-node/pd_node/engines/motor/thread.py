import time

from .utils import set_angle

def thread(state):

    # Do initial reset
    state.motor.set_target_angle(48)
    
    while True:
        
        if not state.motor.is_running():
            log("off")
            time.sleep(1)

        if state.motor.needs_movement():
            log("moving")
            set_angle(state.motor.get_target_angle())
            state.motor.did_move()
        else:
            time.sleep(1/10)


def log(msg):
    print("[motor_thread]: " + msg)
