import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio

btn0_pin = board.GP0
btn1_pin = board.GP1
btn2_pin = board.GP2
btn3_pin = board.GP3
btn4_pin = board.GP4
btn5_pin = board.GP5
btn6_pin = board.GP6
btn7_pin = board.GP7
btn8_pin = board.GP8
btn9_pin = board.GP9
btn10_pin = board.GP10
btn11_pin = board.GP11
btn12_pin = board.GP12
btn13_pin = board.GP13
btn14_pin = board.GP14
btn15_pin = board.GP15
btn16_pin = board.GP16
btn17_pin = board.GP26
btn18_pin = board.GP27
btn19_pin = board.GP28
btn20_pin = board.GP29

btn0 = digitalio.DigitalInOut(btn1_pin)
btn0.direction = digitalio.Direction.INPUT
btn0.pull = digitalio.Pull.DOWN

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn1_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn1_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn1_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn1_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn1_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn1_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8 = digitalio.DigitalInOut(btn1_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9 = digitalio.DigitalInOut(btn1_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

btn10 = digitalio.DigitalInOut(btn1_pin)
btn10.direction = digitalio.Direction.INPUT
btn10.pull = digitalio.Pull.DOWN

btn11 = digitalio.DigitalInOut(btn1_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.DOWN

btn12 = digitalio.DigitalInOut(btn1_pin)
btn12.direction = digitalio.Direction.INPUT
btn12.pull = digitalio.Pull.DOWN

btn13 = digitalio.DigitalInOut(btn1_pin)
btn13.direction = digitalio.Direction.INPUT
btn13.pull = digitalio.Pull.DOWN

btn14 = digitalio.DigitalInOut(btn1_pin)
btn14.direction = digitalio.Direction.INPUT
btn14.pull = digitalio.Pull.DOWN

btn15 = digitalio.DigitalInOut(btn1_pin)
btn15.direction = digitalio.Direction.INPUT
btn15.pull = digitalio.Pull.DOWN

btn16 = digitalio.DigitalInOut(btn1_pin)
btn16.direction = digitalio.Direction.INPUT
btn16.pull = digitalio.Pull.DOWN

btn17 = digitalio.DigitalInOut(btn1_pin)
btn17.direction = digitalio.Direction.INPUT
btn17.pull = digitalio.Pull.DOWN

btn18 = digitalio.DigitalInOut(btn1_pin)
btn18.direction = digitalio.Direction.INPUT
btn18.pull = digitalio.Pull.DOWN

btn19 = digitalio.DigitalInOut(btn1_pin)
btn19.direction = digitalio.Direction.INPUT
btn19.pull = digitalio.Pull.DOWN

btn20 = digitalio.DigitalInOut(btn1_pin)
btn20.direction = digitalio.Direction.INPUT
btn20.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)

while True:
    if btn0.value:
        keyboard.send(Keycode.CONTROL, Keycode.A)
        time.sleep(0.1)
    if btn1.value:
        keyboard.send(Keycode.CONTROL, Keycode.B)
        time.sleep(0.1)
    if btn2.value:
        keyboard.send(Keycode.CONTROL, Keycode.C)
        time.sleep(0.1)
    if btn3.value:
        keyboard.send(Keycode.CONTROL, Keycode.D)
        time.sleep(0.1)
    if btn4.value:
        keyboard.send(Keycode.CONTROL, Keycode.E)
        time.sleep(0.1)
    if btn5.value:
        keyboard.send(Keycode.CONTROL, Keycode.F)
        time.sleep(0.1)
    if btn6.value:
        keyboard.send(Keycode.CONTROL, Keycode.G)
        time.sleep(0.1)
    if btn7.value:
        keyboard.send(Keycode.CONTROL, Keycode.H)
        time.sleep(0.1)
    if btn8.value:
        keyboard.send(Keycode.CONTROL, Keycode.I)
        time.sleep(0.1)
    if btn9.value:
        keyboard.send(Keycode.CONTROL, Keycode.J)
        time.sleep(0.1)
    if btn10.value:
        keyboard.send(Keycode.CONTROL, Keycode.K)
        time.sleep(0.1)
    if btn11.value:
        keyboard.send(Keycode.CONTROL, Keycode.L)
        time.sleep(0.1)
    if btn12.value:
        keyboard.send(Keycode.CONTROL, Keycode.M)
        time.sleep(0.1)
    if btn13.value:
        keyboard.send(Keycode.CONTROL, Keycode.N)
        time.sleep(0.1)        
    if btn14.value:
        keyboard.send(Keycode.CONTROL, Keycode.O)
        time.sleep(0.1)
    if btn15.value:
        keyboard.send(Keycode.CONTROL, Keycode.P)
        time.sleep(0.1)
    if btn16.value:
        keyboard.send(Keycode.CONTROL, Keycode.Q)
        time.sleep(0.1)
    if btn17.value:
        keyboard.send(Keycode.CONTROL, Keycode.R)
        time.sleep(0.1)
    if btn18.value:
        keyboard.send(Keycode.CONTROL, Keycode.P)
        time.sleep(0.1)
    if btn19.value:
        keyboard.send(Keycode.CONTROL, Keycode.S)
        time.sleep(0.1)
    if btn20.value:
        keyboard.send(Keycode.CONTROL, Keycode.T)
        time.sleep(0.1)
    time.sleep(0.1)
