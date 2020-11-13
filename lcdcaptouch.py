import board
import busio
import touchio
import digitalio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)
touchstate = True
touch_pad1 = board.A3
touch1 = touchio.TouchIn(touch_pad1)
touch_pad2 = board.A5
touch2 = touchio.TouchIn(touch_pad2)
lcd.set_cursor_pos(0,0)
lcd.print("Hello CircuitPython!")
time.sleep(2)
pushcount = 0


while True:
    
    if touch1.value:
        lcdmessage = "Direction: UP   "
        touchstate = False
        
    else:
        lcdmessage = "Direction: DOWN "
        touchstate = True
    lcd.set_cursor_pos(0,0)
    lcd.print(lcdmessage)
    if touchstate == True:
        touchdirection = -1
    else:
        touchdirection = 1
    
    if touch2.value:
        pushcount = pushcount + touchdirection
        lcd.set_cursor_pos(1,0)
        lcdmessage = "Presses: "
        lcdmessage += str(pushcount)
        print(pushcount)
        lcd.print(lcdmessage)
    else:
        pushcount = pushcount
        

   