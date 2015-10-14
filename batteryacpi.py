# -*- coding: utf-8 -*-

# batteryacpi.py
# sbl github.com/liberto
# a py3status module. diplays battery infromation from acpi.
# includes battery percentage, dischare/recharge status,
#   and discharge/recharge time remaining.

from __future__ import division
from time import time
import os
import requests

#written by sika-others https://github.com/sika-others/python-acpi
def raw_acpi():
    return os.popen("acpi").read()

#written by sika-others https://github.com/sika-others/python-acpi
def acpi(acpi_str=None):
    if not acpi_str:
        acpi_str = raw_acpi()
    data = []
    for response in acpi_str.split("\n"):
        try:               battery, response = response.split(": ", 1)
        except ValueError: break
        status, response = response.split(", ", 1)
        if status in ("Full", "Unknown"):
            level = int(response.strip("%"))
            uptime = None
            str_uptime = None
        else:
            raw_level, response = response.split(", ", 1)
            level = int(raw_level.strip("%"))
            response_split = response.split(" ")
            try:
                # str_uptime = response_split[0]
                # struct_uptime = time.strptime(str_uptime, "%H:%M:%S")
                # uptime = 3600*struct_uptime.tm_hour + 60*struct_uptime.tm_min + struct_uptime.tm_sec
                uptime = response_split[0]
            except ValueError:
                str_uptime = None
                uptime = None
        data.append((battery, status, level, uptime))
    return data

class Py3status:

    # available configuration parameters
    cache_timeout = 5


    

    def batteryacpi(self, i3s_output_list, i3s_config):
        """
        This method gets executed by py3status
        """

        response = {
            'cached_until': time() + self.cache_timeout,
            'color':'#00ebff',
            'full_text': ''
        }

        output = "battery "

        #form string
        acpiNow = acpi()[0]
        charging = (acpiNow[1] == 'Charging')
        percentage = acpiNow[2]
        if acpiNow[3]:
            timeRemaining = acpiNow[3][:-3] + " "
        else:
            timeRemaining = ""
        output += timeRemaining + str(percentage) + "%"
        if charging:
            output += " Charging"

        #set color and launch popup alerts
        if charging==True:
            response['color']='#00FF00'
        elif percentage<=5:
            response['color']='#FF3300'
            os.popen("notify-send --icon=/home/sbl/.i3/py3status/lowbattery.png 'low battery' 'no seriouesly, plug in your charger now.'")
        elif percentage<=10:
            response['color']='#FF3300'
            os.popen("notify-send --icon=/home/sbl/.i3/py3status/lowbattery.png 'low battery' 'plug in your charger'")

        response['full_text'] += '{} '.format(output)
        response['full_text'] = response['full_text'].strip()
    

        return response

    

if __name__ == "__main__":
    """
    Test this module by calling it directly.
    """
    from time import sleep
    x = Py3status()
    config = {
        'color_good': '#00FF00',
        'color_bad': '#FF0000',
    }
    while True:
        print(x.batteryacpi([], config))
        sleep(1)
