import psutil # for battery info
from time import sleep
import AppKit # for alert sound

while 1:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    print(str(battery.percent) + "%")
    
    if battery.percent and not plugged <= 25:
        AppKit.NSBeep()
        print("unplug")
        sleep(1)

    elif battery.percent and plugged >= 75:
        AppKit.NSBeep()
        print("plug")
        sleep(1)

    else:
        sleep(30)
