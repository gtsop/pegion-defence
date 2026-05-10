import time

from .utils import move

def thread(state):

    # Do initial reset
    state.motor.set_target_angle(48)
    
    while True:
        
        if not state.motor.is_running():
            log("off")
            time.sleep(1)

        if state.motor.should_move("right"):
            move("right")
        elif state.motor.should_move("left"):
            move("left")
        elif state.motor.should_move("up"):
            move("up")
        elif state.motor.should_move("down"):
            move("down")
        time.sleep(1/10)


def log(msg):
    print("[motor_thread]: " + msg)
