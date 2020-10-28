import time
import board
import pulseio
from adafruit_motor
import servo
import digitalio

#button_a = digitalio.DigitalInOut(board.A2)
#button_a.direction = digitalio.Direction.INPUT
#button_a.pull = digitalio.Pull.DOWN
 
#button_b = digitalio.DigitalInOut(board.A5)
#button_b.direction = digitalio.Direction.INPUT
#button_b.pull = digitalio.Pull.DOWN
# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
 
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
 
while True:
    #if button_a.value:
     for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        
    #elif button_b.value:
        for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
    #else
        myservo.angle = 90