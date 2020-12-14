import time
import math
class LED:
    
    

    #r1 prints out r1's value according to color, same with g1, b1, r2, etc.
<<<<<<< HEAD
    def __init__(self, onep, twop, threep):#when Myrgb1(r1,g1,b1) is put into the code, the re pin corresponds with self.r in the library....
        import digitalio
        
        self.one = digitalio.DigitalInOut(onep)
        self.one.direction = digitalio.Direction.OUTPUT
       
       #the "onep"-onepin corresponds to the board number specified in the given code
        
        self.two = digitalio.DigitalInOut(twop)#self.g = .......
        self.two.direction = digitalio.Direction.OUTPUT
        
        self.three = digitalio.DigitalInOut(threep)
        self.three.direction = digitalio.Direction.OUTPUT

    
    def chase(self):
        #(225, 0, 0)
        self.one.value = True
        time.sleep(1)
        self.one.value = False #true = on for leds
        self.two.value = True
        time.sleep(1)
        self.two.value = False
        self.three.value = True
        time.sleep(1)
        self.three.value = False
        
        self.one.value = True
        time.sleep(1)
        self.one.value = False
        self.two.value = True
        time.sleep(1)
        self.two.value = False
        self.three.value = True
        time.sleep(1)
        self.three.value = False
       
        self.one.value = True
        time.sleep(1)
        self.one.value = False
        self.two.value = True
        time.sleep(1)
        self.two.value = False
        self.three.value = True
        time.sleep(1)
        self.three.value = False
        print("chase!")#prints to serial monitor

    
    def blink(self):
        self.one.value = True
        self.two.value = True
        self.three.value = True
        time.sleep(1)
        self.one.value = False
        self.two.value = False
        self.three.value = False
        time.sleep(1)
        self.one.value = True
        self.two.value = True
        self.three.value = True
        time.sleep(1)
        self.one.value = False
        self.two.value = False
        self.three.value = False
        time.sleep(1)
        self.one.value = True
        self.two.value = True
        self.three.value = True
        time.sleep(1)
        self.one.value = False
        self.two.value = False
        self.three.value = False
        time.sleep(1)
        print("blink!")
    
    def alternate(self):
        self.one.value = True
        self.two.value = False
        self.three.value = True
        time.sleep(1)
        self.one.value = False
        self.two.value = True
        self.three.value = False
        time.sleep(1)
        self.one.value = True
        self.two.value = False
        self.three.value = True
        time.sleep(1)
        self.one.value = False
        self.two.value = True
        self.three.value = False
        time.sleep(1)
        self.one.value = True
        self.two.value = False
        self.three.value = True
        time.sleep(1)
        self.one.value = False
        self.two.value = True
        self.three.value = False
        time.sleep(1)
        print("alternate!")
   
   
    def twinkle(self):
        #random function from the defined above from a list
        suplist = [sup1, sup2, sup3, sup4, sup5, sup6, sup7, sup8]
        random.choice(suplist)
        time.sleep(1)
        random.choice(suplist)
        time.sleep(1)
        random.choice(suplist)
        time.sleep
        random.choice(suplist)
        time.sleep
        random.choice(suplist)
        time.sleep
        random.choice(suplist)
        time.sleep
    
    def sup1:
        self.one.value = False
        self.two.value = True
        self.three.value = False
    def sup2:
        self.one.value = False
        self.two.value = True
        self.three.value = True
    def sup3:
        self.one.value = False
        self.two.value = False
        self.three.value = False
    def sup3:
        self.one.value = False
        self.two.value = False
        self.three.value = True
    def sup4:
        self.one.value = True
        self.two.value = True
        self.three.value = True
    def sup5:
        self.one.value = True
        self.two.value = True
        self.three.value = False
    def sup6:
        self.one.value = True
        self.two.value = False
        self.three.value = True
    def sup7:
        self.one.value = True
        self.two.value = False
        self.three.value = False

       


    

  
