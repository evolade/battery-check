import psutil # for battery info
from time import sleep
import AppKit # for alert sound

while 1:
    battery = psutil.sensors_battery()
    print(str(battery.percent) + "%")
    
    if battery.percent <= 25:
        AppKit.NSBeep()
        print("unplug")
        sleep(1)

    else if battery.percent >= 75:
        AppKit.NSBeep()
        print("plug")
        sleep(1)

    else:
        sleep(30)
