import psutil # for battery info
from time import sleep
import AppKit # for alert sound
from termcolor import colored

color = "white"

while 1:
    battery = psutil.sensors_battery()
    perc = int(battery.percent / 10)
    
    # displaying battery
    print("\n" + colored(str(battery.percent) + "%", color),"[ ", end="")
    for j in range(perc):
        print(colored("+", "green"), end="")

    for j in range(10 - perc):
        print(colored("-", "red"), end="")

    print(" ]")
    
    if battery.percent <= 33 and not battery.power_plugged:
        AppKit.NSBeep()
        color = "yellow"
        sleep(1)

    elif battery.percent >= 75 and battery.power_plugged:
        AppKit.NSBeep()
        color = "yellow"
        sleep(1)

    else:
        color = "white"
        sleep(5)
