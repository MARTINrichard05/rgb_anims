import psutil
from time import sleep
import os
import requests
delay = 0.5

args = "-l"


process_color = {
    'DesktopEditors' : [2, 220, 200, 200],
    'Brave' : [1, 0, 50, 255],
    'Discord' : [0 , 40, 40, 255]

}

def running_apps():
    result = os.popen("wmctrl -l")
    return result.read()

while True:
    known_apps_running = []
    known_apps_running_index = []
    b = []
    a = running_apps().split("\n")
    for i in range(len(a)):
        buffer = a[i].split(" ")
        for j in range(len(buffer)):
            b.append(buffer[j])
    for i in range(len(process_color)):
        try :
            known_apps_running_index.append(b.index(list(process_color.keys())[i]))
            known_apps_running.append(b[known_apps_running_index[-1]])

        except :
            pass

    unsorted_dict = {}

    for i in range(len(known_apps_running)):
        unsorted_dict[known_apps_running[i]] = process_color[known_apps_running[i]][0]

    sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))
    try:
        rgb = process_color[list(sorted_dict.keys())[-1]]
        try:
            requests.get("http://127.0.0.1:6670/[" + str(rgb[-3]) + "," + str(rgb[-2]) + "," + str(rgb[-1]) + "]")
        except:
            pass
    except:
        try:
            requests.get("http://127.0.0.1:6670/[100, 255, 100]")
        except:
            pass

    sleep(delay)


