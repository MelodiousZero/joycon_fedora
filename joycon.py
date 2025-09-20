import uinput
from evdev import InputDevice, ecodes

# --- Bluetooth event number. ---
JOYCON_EVENT_NUMBER = 14
JOYCON_EVENT = f"/dev/input/event{JOYCON_EVENT_NUMBER}"

# --- Event Mapping ---
EVENTS = (
    uinput.BTN_A,
    uinput.BTN_B,
    uinput.BTN_X,
    uinput.BTN_Y,
    uinput.BTN_TL,
    uinput.BTN_TL2,
    uinput.BTN_TR,
    uinput.BTN_TR2,
    uinput.BTN_MODE,
    uinput.BTN_SELECT,
    uinput.BTN_START,
    uinput.ABS_X + (-32767, 32767, 0, 0),
    uinput.ABS_Y + (-32767, 32767, 0, 0),
)

# Map Joy-Con codes -> Virtual codes
KEY_MAP = {
    304: uinput.BTN_A,       # BTN_SOUTH
    305: uinput.BTN_B,       # BTN_EAST
    307: uinput.BTN_X,       # BTN_NORTH
    308: uinput.BTN_Y,       # BTN_WEST
    310: uinput.BTN_TL,
    311: uinput.BTN_TR,
    312: uinput.BTN_TL2,
    313: uinput.BTN_TR2,
    315: uinput.BTN_START,
    316: uinput.BTN_SELECT,  # Joy-Con "minus" button
}

ABS_MAP = {
    3: uinput.ABS_X,  # ABS_RX
    4: uinput.ABS_Y,  # ABS_RY
}

# --- Setup virtual device ---
ui = uinput.Device(EVENTS, name="Joy-Con Virtual JS")
dev = InputDevice(JOYCON_EVENT)
print(f"Mapping {JOYCON_EVENT} -> virtual joystick...")

# --- Event loop ---
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY and event.code in KEY_MAP:
        ui.emit(KEY_MAP[event.code], event.value)
    elif event.type == ecodes.EV_ABS and event.code in ABS_MAP:
        ui.emit(ABS_MAP[event.code], event.value)
