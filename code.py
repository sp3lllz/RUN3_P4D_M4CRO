import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio

button_pins = [
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4,
    board.GP5, board.GP6, board.GP7, board.GP8, board.GP9,
    board.GP10, board.GP11, board.GP12, board.GP13, board.GP14,
    board.GP15, board.GP26, board.GP27, board.GP28, board.GP29
]

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]

for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)

while True:
    for i, button in enumerate(buttons):
        if button.value:
            # Use i+1 as the Keycode, assuming you want to map buttons to F1-F20
            keyboard.send(Keycode.F1 + i)
            time.sleep(0.1)
    time.sleep(0.1)
