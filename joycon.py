import uinput
from evdev import InputDevice, categorize, ecodes

JOYCON_EVENT_NUMBER = 14
JOYCON_EVENT = f"/dev/input/event{str(JOYCON_EVENT_NUMBER)}"

events = (
    uinput.BTN_A,
    uinput.BTN_B,
    uinput.BTN_X,
    uinput.BTN_Y,
    uinput.BTN_TL,
    uinput.BTN_TR,
    uinput.BTN_SELECT,
    uinput.BTN_START,
    uinput.ABS_X + ( -32767, 32767, 0, 0),
    uinput.ABS_Y + ( -32767, 32767, 0, 0),
)
    
ui = uinput.Device(events, name="Joy-Con Virtual JS")

dev = InputDevice(JOYCON_EVENT)
print(f"Mapping {JOYCON_EVENT} to virtual joystick...")

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        code = event.code
        state = event.value
        if code == 304:  # BTN_SOUTH
            ui.emit(uinput.BTN_A, state)
        elif code == 305:  # BTN_EAST
            ui.emit(uinput.BTN_B, state)
        elif code == 307:  # BTN_NORTH
            ui.emit(uinput.BTN_X, state)
        elif code == 308:  # BTN_WEST
            ui.emit(uinput.BTN_Y, state)
        elif code == 310:  # BTN_TL
            ui.emit(uinput.BTN_TL, state)
        elif code == 311:  # BTN_TR
            ui.emit(uinput.BTN_TR, state)
        elif code == 315:  # BTN_START
            ui.emit(uinput.BTN_START, state)
        elif code == 316:  # BTN_MODE
            ui.emit(uinput.BTN_SELECT, state)

    elif event.type == ecodes.EV_ABS:
        if event.code == 3:  # ABS_RX
            ui.emit(uinput.ABS_X, event.value)
        elif event.code == 4:  # ABS_RY
            ui.emit(uinput.ABS_Y, event.value)
