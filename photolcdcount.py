from digitalio import DigitalInOut, Direction, Pull
import time
import board

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# some LCDs are 0x3f... some are 0x27, import all libraries for lcd
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

interrupter = DigitalInOut(board.D7)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

lcd.set_cursor_pos(0,0)#sets the area where the lcd will type to the top row
time.sleep(2)
counter = 0


max = 3
start = time.time()
while True:
    lcd.set_cursor_pos(0,0)
    if interrupter.value:
     counter += 1
     time.sleep(.20)
    else:
        counter = counter

    remaining = max - time.time()
    if remaining <= 0:
        lcdmessage = "Interruptions: "#message at bottom row
        lcdmessage += str(counter)
        lcd.print(lcdmessage)
        print(lcdmessage)
        
        max = time.time() + 4
        counter = counter