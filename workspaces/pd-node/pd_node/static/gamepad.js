let interval;

const API_BASE = "http://" + window.location.hostname + ":8000";

const directionState = {
  left: false,
  right: false,
  up: false,
  down: false,
};

window.addEventListener("gamepadconnected", (e) => {
  const gp = navigator.getGamepads()[e.gamepad.index];

  console.log(
    `Gamepad connected at index ${gp.index}: ${gp.id} with ${gp.buttons.length} buttons, ${gp.axes.length} axes.`,
  );

  interval = setInterval(gamepadLoop, 50);
});

window.addEventListener("gamepaddisconnected", async (event) => {
  console.log("Gamepad Disconnected:", event);
  clearInterval(interval);

  for (const direction of Object.keys(directionState)) {
    if (directionState[direction]) {
      await freezeMotor(direction);
      directionState[direction] = false;
    }
  }
});

async function gamepadLoop() {
  const gamepads = navigator.getGamepads();
  if (!gamepads) return;

  const gamepad = gamepads[0];
  if (!gamepad) return;

  await updateDirection("left", isLeft(gamepad));
  await updateDirection("right", isRight(gamepad));
  await updateDirection("up", isUp(gamepad));
  await updateDirection("down", isDown(gamepad));
}

async function updateDirection(direction, isActive) {
  const wasActive = directionState[direction];

  if (isActive && !wasActive) {
    await moveMotor(direction);
    directionState[direction] = true;
  }

  if (!isActive && wasActive) {
    await freezeMotor(direction);
    directionState[direction] = false;
  }
}

async function moveMotor(direction) {
  await fetch(`${API_BASE}/motor/move`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ direction }),
  });
}

async function freezeMotor(direction) {
  await fetch(`${API_BASE}/motor/freeze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ direction }),
  });
}

function isLeft(gp) {
  const deadzone = 0.2;

  return (
    gp.buttons[14]?.pressed || gp.axes[0] < -deadzone || gp.axes[2] < -deadzone
  );
}

function isRight(gp) {
  const deadzone = 0.2;

  return (
    gp.buttons[15]?.pressed || gp.axes[0] > deadzone || gp.axes[2] > deadzone
  );
}

function isUp(gp) {
  const deadzone = 0.2;

  return (
    gp.buttons[12]?.pressed || gp.axes[1] < -deadzone || gp.axes[3] < -deadzone
  );
}

function isDown(gp) {
  const deadzone = 0.2;

  return (
    gp.buttons[13]?.pressed || gp.axes[1] > deadzone || gp.axes[3] > deadzone
  );
}
