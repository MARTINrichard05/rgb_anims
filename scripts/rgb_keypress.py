import keyboard
import requests
import time
from threading import Thread
r = 0 # r
g = 255 # g
b = 255 # b
decrease_step = 3# the decrease_step until the desired values
i_r = 50 #idle r
i_g = 0 # idle g
i_b = 200 # idle b
wait_time = 0.002 # if you change this it is gonna change the anim speed
idle_wait_time = 0.01 #0.1 is the best value for a balance of latency and latency

class Main :
    def __init__(self):
        self.r = i_r
        self.g = i_g
        self.b = i_b
        self.timer = 0
        self.change = False
        listener = Thread(target=self.listener)
        listener.start()
        while True:
            if self.r + self.g + self.b >= decrease_step:
                if self.r < i_r:
                    self.r =i_r
                    self.change = True
                elif self.r > i_r:
                    self.r -= decrease_step
                    self.change = True

                if self.g < i_g:
                    self.g = i_g
                    self.change = True
                elif self.g > i_g:
                    self.g -= decrease_step
                    self.change = True

                if self.b < i_b:
                    self.b = i_b
                    self.change = True
                elif self.b > i_b:
                    self.b -= decrease_step
                    self.change = True
            else:
                time.sleep(idle_wait_time)
            if self.timer == 10:
                self.timer = 0
                if self.change == True :
                    self.send_color(self.r, self.g, self.b)
                    self.change = False
            else:
                self.timer += 1

            time.sleep(wait_time)

    def illuminate(self,x):
        key = 0
        self.r = r
        self.g = g
        self.b = b

    def listener(self):
        keyboard.on_press(callback=self.illuminate)
        keyboard.wait()

    def send_color(self,r,g,b):
        try:
            requests.get("http://127.0.0.1:6670/["+str(r)+","+str(g)+","+str(b)+"]")
        except :
            pass

print("Starting animation")
a = Main()
