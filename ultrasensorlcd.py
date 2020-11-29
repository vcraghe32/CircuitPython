from digitalio import DigitalInOut, Direction, Pull
import time
import board
import neopixel
import math#made it possible to use the round featutur for whole integers

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# some LCDs are 0x3f... some are 0x27, import all libraries for lcd
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)#add ultrasonic sensor

lcd.set_cursor_pos(0,0)#sets the area where the lcd will type to the top row
time.sleep(2)
counter = 0
lcdmessage = "Hello!"
lcd.print(lcdmessage)
print(lcdmessage)
lcd.clear
time.sleep(2)
dotvalue1 = sonardisval.range(225, 0, 1)
dotvalue2 = sonardisval.range(0, 225, 1)
dotvalue3 = sonardisval.range(0, 225, 1)

sonardisval = sonardis.range(0, 35, 1)
while True:
    try:
        lcd.set_cursor_pos(0,0)
        lcdmessage = "Distance: "#message at bottom row
        sonardis = round(sonar.distance, 0)#sensor distance rounded
        lcdmessage += str(sonardis)
        lcd.print(lcdmessage)
        print(lcdmessage)
    except RuntimeError:
        lcd.set_cursor_pos(0,0)
        lcdmessage = "Retrying!"#if it's too far away, it will say "retrying"
        lcd.print(lcdmessage)
        print(lcdmessage)
    else:
        lcd.set_cursor_pos(0,0)
        lcdmessage = lcdmessage
        print(lcdmessage)
    time.sleep(0.1)
    #for dotvalue in range(0, 225, 5)
    if sonardis.value:
        dot.fill(str(dotvalue1, dotvalue2, dotvalue3))
    