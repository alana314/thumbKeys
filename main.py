import time
import microcontroller
import board
import digitalio
import busio
import usb_hid
from digitalio import DigitalInOut, Direction

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

led = DigitalInOut(board.LED_INVERTED)
led.direction = Direction.OUTPUT

cc = ConsumerControl(usb_hid.devices)  # usb_hid.Device.CONSUMER_CONTROL
kbd = Keyboard(usb_hid.devices)
keyboard = KeyboardLayoutUS(kbd)
btn1 = digitalio.DigitalInOut(board.D0) # F1 DEL
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP
btn2 = digitalio.DigitalInOut(board.D1) # F2 ESC
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP
btn3 = digitalio.DigitalInOut(board.D2) # F3 TAB
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.UP
btn4 = digitalio.DigitalInOut(board.D3) # F4 SPACE
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.UP
btn5 = digitalio.DigitalInOut(board.D4) # F5 SHIFT
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.UP
btn6 = digitalio.DigitalInOut(board.D5) # F6 ALT
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.UP
btn7 = digitalio.DigitalInOut(board.D6) # F7 CTRL
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.UP
led.value = True
led.value = False
print("starting")

btn1_state = False
btn2_state = False
btn3_state = False
btn4_state = False
btn5_state = False
btn6_state = False
btn7_state = False

# loop 2 0 1 4 3 5 
while True:
    if btn1.value == False and btn1_state == False:
        print("Del")
        btn1_state = True
        kbd.press(Keycode.DELETE)
        led.value = True
    elif btn1.value == True and btn1_state == True:
        btn1_state = False
        kbd.release(Keycode.DELETE)
        led.value = False
    elif btn2.value == False and btn2_state == False:
        print("ESC")
        btn2_state = True
        kbd.press(Keycode.ESCAPE)
        led.value = True
    elif btn2.value == True and btn2_state == True:
        btn2_state = False
        kbd.release(Keycode.ESCAPE)
        led.value = False
    elif btn3.value == False and btn3_state == False:
        print("Tab")
        btn3_state = True
        kbd.press(Keycode.TAB)
        led.value = True
    elif btn3.value == True and btn3_state == True:
        btn3_state = False
        kbd.release(Keycode.TAB)
        led.value = False
    elif btn4.value == False and btn4_state == False:
        print("space")
        btn4_state = True
        kbd.press(Keycode.SPACEBAR)
        led.value = True
    elif btn4.value == True and btn4_state == True:
        btn4_state = False
        kbd.release(Keycode.SPACEBAR)
        led.value = False
    elif btn5.value == False and btn5_state == False:
        print("Shift")
        btn5_state = True
        kbd.press(Keycode.SHIFT)
        led.value = True
    elif btn5.value == True and btn5_state == True:
        btn5_state = False
        kbd.release(Keycode.SHIFT)
        led.value = False
    elif btn6.value == False and btn6_state == False:
        print("Alt")
        btn6_state = True
        kbd.press(Keycode.ALT)
        led.value = True
    elif btn6.value == True and btn6_state == True:
        btn6_state = False
        kbd.release(Keycode.ALT)
        led.value = False
    elif btn7.value == False and btn7_state == False:
        print("Ctrl")
        btn7_state = True
        kbd.press(Keycode.CONTROL)
        led.value = True
    elif btn7.value == True and btn7_state == True:
        btn7_state = False
        kbd.release(Keycode.CONTROL)
        led.value = False
    else:
        #print("no buttons")
        pass
    time.sleep(0.02)



