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

def getBrightness():
    return str(int(float(os.popen("xbacklight").read()[:-1])))

def getVolume():
    raw = os.popen("amixer get Master").read()
    theLine = raw.split('\n')[5]
    splitLine = theLine.split(' ')
    mute = splitLine[-1]=="[off]"
    if mute:
    	return splitLine[-2]+'[MUTE]'
    else:
    	return splitLine[-2]

class Py3status:

    # available configuration parameters
    cache_timeout = 1


    def volumebrightness(self, i3s_output_list, i3s_config):
        """
        This method gets executed by py3status
        """

        response = {
            'cached_until': time() + self.cache_timeout,
            'color':'#ff22aa',
            'full_text': ''
        }

        output = "bright[" + getBrightness() + "%] loud" + getVolume()

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
        print(x.volumebrightness([],config))
        sleep(1)
