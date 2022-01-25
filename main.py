# CONFIGURE
min = 25
max = 75

import psutil # for battery info
from time import sleep
import AppKit # for alert sound
from termcolor import colored

color = "white" # dont configure this

while 1:
    battery = psutil.sensors_battery()
    perc = int(battery.percent / 10)
    
    # displaying battery
    print("\n" + colored(str(battery.percent) + "%", color),"[", end="")
    for i in range(perc):
        print(colored("+", "green"), end="")

    for j in range(10 - perc):
        print(colored("-", "red"), end="")

    print("]")
    
    if battery.percent <= min and not battery.power_plugged:
        AppKit.NSBeep()
        color = "yellow"
        sleep(1)

    elif battery.percent >= max and battery.power_plugged:
        AppKit.NSBeep()
        color = "yellow"
        sleep(1)

    else:
        color = "white"
        sleep(5)
