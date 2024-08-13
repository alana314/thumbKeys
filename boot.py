import digitalio
import storage
import board
btn7 = digitalio.DigitalInOut(board.D6) # F7 CTRL
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.UP
if btn7.value:
    print(f"boot: button not pressed, disabling drive")
    storage.disable_usb_drive()
