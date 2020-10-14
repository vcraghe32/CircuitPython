import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)


while True:
     print("Make it red!")
     dot.fill((255,0,0))
     time.sleep(.5)
     print("Make it purple!")
     dot.fill((204, 0, 204))
     time.sleep(.5)
     print("Make it red!")
     dot.fill((255,0,0))
     time.sleep(.5)
     