import time
class RGB:
    
    

    #r1 prints out r1's value according to color, same with g1, b1, r2, etc.
    def __init__(self, rp, bp, gp):#when Myrgb1(r1,g1,b1) is put into the code, the re pin corresponds with self.r in the library....
        import pulseio
        import digitalio
        
        
        rv = digitalio.DigitalInOut(rp)
        rv.direction = digitalio.Direction.OUTPUT
        self.r = rv
       # rv(red value) we will use in the code- the rp corresponds to the board number specified in the given code
        gv = digitalio.DigitalInOut(gp)#self.g = .......
        gv.direction = digitalio.Direction.OUTPUT
        self.g = gv
        
        bv = digitalio.DigitalInOut(bp)
        bv.direction = digitalio.Direction.OUTPUT
        self.b = bv
        #rvp = pulseio.PWMOut(r)
        #gvp = pulseio.PWMOut(g)
        #bvp = pulseio.PWMOut(b)

    
    def red(self):
        #(225, 0, 0)
        self.r.value = False#false = on for common rgb anodes
        self.g.value = True
        self.b.value = True
        print("red!")#prints to serial monitor
    def blue(self):
        #(0, 0, 225)
        self.r.value = True
        self.g.value = True
        self.b.value = False
        print("blue!")
    def green(self):
        #(0, 225, 0)
        self.r.value = True
        self.g.value = False
        self.b.value = True
        print("green!")
    def magenta(self):
        #(255, 0, 255)
        self.r.value = False
        self.g.value = True
        self.b.value = False
        print("green!")
        print("magenta!")
    def cyan(self):
        #(0, 225, 225)
        self.r.value = True
        self.g.value = False
        self.b.value = False
        print("cyan!")
    def yellow(self):
        #(225, 225, 0)
        self.r.value = False
        self.g.value = False
        self.b.value = True
        print("yellow!")
  
    def rainbow(self, rate: float):
      
      time.sleep(rate)
      self.red()
      time.sleep(rate)
      #self.orange() how would i do this one?
      #time.sleep(rate)
      self.yellow()
      time.sleep(rate)
      self.green()
      time.sleep(rate)
      self.blue()
      time.sleep(rate)
      self.magenta()
      time.sleep(rate)
      
      
      #int2 = int2 + 4
      #int3 = int3 + 4
      #time.sleep(rate)
      #how do I make a rate = rate 1 OR rate 2?
       


    

  