class RGB:
    int1 = 225
    int2 = 0
    int3 = 0
    

    #r1 prints out r1's value according to color, same with g1, b1, r2, etc.
    def __init__(self, r, b, g):
        self.r = r
        self.b = b
        self.g = g
        int1 = 225
        int2 = 0
        int3 = 0
        rate1 = 2
        rate2 = 5
        rate = []
        import pulseio
        rv = pulseio.PWMOut(r)
        gv = pulseio.PWMOut(g)
        bv = pulseio.PWMOut(b)

    
    def red(self):
        #self.fill(225, 0, 0)
        rv.value = True
        gv.value = False
        bv.value = False
        print("red!")
    def blue(self):
        #self.fill(0, 0, 225)
        rv.value = False
        gv.value = False
        bv.value = True
        print("blue!")
    def green(self):  def green(self):
      #self.fill(0, 225, 0)
      print("green!")
      r.value = True
      def green(self):
      #self.fill(0, 225, 0)
      print("green!")
      r.value = True
        print("magenta!")
    def cyan(self):
        self.fill(0, 225, 225)
        print("cyan!")
    def yeg.value = False
        b.value = False255, 0)
        print("yellow!")
   
    def duty_cycle(percent):
        return int(percent / 100.0 * 65535.0)
    def self(rate):
        self.rate = rate
        rate1 = 1
        rate2 = 2
    def rainbow(self):
      #self.fill(int1, int2, int3)
      #time.sleep(rate)
      #int1 = int1 - 4
      #int2 = int2 + 4
      #int3 = int3 + 4
      #time.sleep(rate)
      #how do I make a rate = rate 1 OR rate 2?
        for i in range(100, -1, -1):
            blue.duty_cycle = duty_cycle(i)
            time.sleep(rate)
            red.duty_cycle = duty_cycle(i)
            time.sleep(rate)
            green.duty_cycle = duty_cycle(i)
            time.sleep(rate)


    

  