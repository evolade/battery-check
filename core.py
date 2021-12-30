import psutil # for battery info
from time import sleep
import AppKit # for alert sound

while 1:
    battery = psutil.sensors_battery()
    perc = int(battery.percent / 10)
    
    # displaying battery
    print(str(battery.percent) + "%","[ ", end="")
    for j in range(perc):
        print("+", end="")

    for j in range(10 - perc):
        print("-", end="")

    print(" ]")
    
    if battery.percent <= 25 and not battery.power_plugged:
        AppKit.NSBeep()
        print("PLUG IN")
        sleep(1)

    elif battery.percent >= 75 and battery.power_plugged:
        AppKit.NSBeep()
        print("UNPLUG")
        sleep(1)

    else:
        sleep(5) 
