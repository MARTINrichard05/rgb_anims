import colorsys
from time import sleep
import requests

print("Starting ")

hsv = [0, 1, 0.5]
color_step = 0.005
sleep_time = 0.05

while True:
    if hsv[0] >= 1-color_step:
        hsv[0] = 0
    else:
        hsv[0] += color_step
    rgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
    try :
        requests.get("http://127.0.0.1:6670/[" + str(int(rgb[0]*255)) + "," + str(int(rgb[1]*255)) + "," + str(int(rgb[2]*255)) + "]")
    except:
        pass
    sleep(sleep_time)
