import board
import time
import digitalio #import library for digital output for led

led = digitalio.DigitalInOut(board.D3)
led.direction = digitalio.Direction.OUTPUT  #connects the led to the board as an output of A1

while True:
    led.value = True        #led is on
    time.sleep(0.5)         #delay
    led.value = False       #led is off
    time.sleep(0.5)
    
    
    
