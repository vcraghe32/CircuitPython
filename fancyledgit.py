import time
import math
import random
class FancyLED:
    v = 1
    

    #r1 prints out r1's value according to color, same with g1, b1, r2, etc.

    def __init__(self, onep, twop, threep):#when Myrgb1(r1,g1,b1) is put into the code, the re pin corresponds with self.r in the library....
        import digitalio
        
        v = 1           #sets time as a value, I can easily change it
        self.one = digitalio.DigitalInOut(onep)
        self.one.direction = digitalio.Direction.OUTPUT
       
       #the "onep"-onepin corresponds to the board number specified in the given code
        
        self.two = digitalio.DigitalInOut(twop)#self.g = .......
        self.two.direction = digitalio.Direction.OUTPUT
        
        self.three = digitalio.DigitalInOut(threep)
        self.three.direction = digitalio.Direction.OUTPUT

    
    def chase(self):
        v = .5
        #(225, 0, 0)
        self.one.value = True
        time.sleep(v)
        self.one.value = False #true = on for leds
        self.two.value = True
        time.sleep(v)
        self.two.value = False
        self.three.value = True
        time.sleep(v)
        self.three.value = False
        
        self.one.value = True
        time.sleep(v)
        self.one.value = False
        self.two.value = True
        time.sleep(v)
        self.two.value = False
        self.three.value = True
        time.sleep(v)
        self.three.value = False
       
        self.one.value = True
        time.sleep(v)
        self.one.value = False
        self.two.value = True
        time.sleep(v)
        self.two.value = False
        self.three.value = True
        time.sleep(v)
        self.three.value = False
        self.one.value = False
        self.two.value = False
        print("chase!")#prints to serial monitor

    
    def blink(self):
        v = .5
        self.one.value = True
        self.two.value = True
        self.three.value = True
        time.sleep(v)
        self.one.value = False
        self.two.value = False
        self.three.value = False
        time.sleep(v)
        self.one.value = True
        self.two.value = True
        self.three.value = True
        time.sleep(v)
        self.one.value = False
        self.two.value = False
        self.three.value = False
        time.sleep(v)
        self.one.value = True
        self.two.value = True
        self.three.value = True
        time.sleep(v)
        self.one.value = False
        self.two.value = False
        self.three.value = False
        time.sleep(v)
        print("blink!")
    
    def alternate(self):
        v = .5
        self.one.value = True
        self.two.value = False
        self.three.value = True
        time.sleep(v)
        self.one.value = False
        self.two.value = True
        self.three.value = False
        time.sleep(v)
        self.one.value = True
        self.two.value = False
        self.three.value = True
        time.sleep(v)
        self.one.value = False
        self.two.value = True
        self.three.value = False
        time.sleep(v)
        self.one.value = True
        self.two.value = False
        self.three.value = True
        time.sleep(v)
        self.one.value = False
        self.two.value = True
        self.three.value = False
        time.sleep(v)
        self.one.value = False
        self.two.value = False
        self.three.value = False
        print("alternate!")
   
    
    def suprise(self):
        v = 2
        #random function from the defined above from a list
        suplist = [self.sup1(), self.sup2(), self.sup3()] #self.sup4(), self.sup5(), self.sup6(), self.sup7(), self.sup8()]
        #list contains sup1-8
        random.choice(suplist)#random functon from the list
        time.sleep(v)
        random.choice(suplist)
        time.sleep(v)
        random.choice(suplist)
        time.sleep(v)
        random.choice(suplist)
        time.sleep(v)
        random.choice(suplist)
        time.sleep(v)
        random.choice(suplist)
        time.sleep(v)
        self.one.value = False
        self.two.value = False
        self.three.value = False
    
    def sup1(self):       #short for "suprise1"
            self.one.value = False
            self.two.value = True
            self.three.value = False
            print("sup1")
    def sup2(self):
            self.one.value = False
            self.two.value = True
            self.three.value = True
            print("sup2")
    def sup3(self):
            self.one.value = False
            self.two.value = False
            self.three.value = False
            print("sup3")
    def sup4(self):
            self.one.value = True
            self.two.value = True
            self.three.value = True
    def sup5(twinkle):
            self.one.value = True
            self.two.value = True
            self.three.value = False
    def sup6(twinkle):
            self.one.value = True
            self.two.value = False
            self.three.value = True
    def sup7(twinkle):
            self.one.value = True
            self.two.value = False
            self.three.value = False

    


    

  
