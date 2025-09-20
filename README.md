# Joy-Con Virtual Joystick for AntiMicroX

This repository contains a Python script that creates a **virtual joystick** from a Nintendo Joy-Con on Linux using `uinput` and `evdev`. Once the virtual joystick is running, you can map buttons and sticks in **AntiMicroX** to use your Joy-Con in games or other applications. In my case, I use it as a tv-remote for Kodi with my current linux computer. As the hid-controller for this joycon didn't work out of the box.

---

## Requirements

- Linux with Python 3
- Python packages:
  ```bash
  pip install evdev python-uinput

## Usage
- If you have joycond enabled, run
  ```bash
  sudo systemctl stop joycond
- Then run
  ```bash
  sudo modprobe uinput
- Then run the python script
  ```bash
  sudo python joycon.py
- Then run antimicrox
  ```bash
  antimicrox


<img width="1339" height="760" alt="image" src="https://github.com/user-attachments/assets/22099150-685c-43fc-8a5d-3a56ef4116c7" />


