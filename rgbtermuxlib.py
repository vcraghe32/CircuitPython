class RGB:
    int1 = 225
    int2 = 0
    int3 = 0
    

    #r1 prints out r1's value according to color, same with g1, b1, r2, etc.
    def __init__(self, r, b, g):
        self.r = r  #when Myrgb1(r1,g1,b1) is put into the code, the r1 corresponds with r in the library....
        self.b = b  #same goes for g1----(g), b1----(b).
        self.g = g
        int1 = 225#these next five lines are just for the rainbow part, just ignore them
        int2 = 0
        int3 = 0
        rate1 = 2
        rate2 = 5
        rate = []#this makes a list, so when you add say "dog" and "cat" it shows up as[dog, cat]. 
        #you can add or delete objects from the list, or pick random objects from the list using functions
        #I have code for these from a camp I did last summer
        import pulseio
        rv = pulseio.PWMOut(r)# rv(red value) we will use in the code- the r correspond to the board number specified in the given code
        gv = pulseio.PWMOut(g)#same with the others
        bv = pulseio.PWMOut(b)

    
    def red(self):
        #self.fill(225, 0, 0) this was from the neopixel code, didn't work but i'm keeping it just in case
        rv.value = True #I haven't figured out if I could put the led on a certain voltage to make 255 work,...
        gv.value = False#or if i should say true or false. I'll ask Dr,shields about this during office hours or class
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


    

  
