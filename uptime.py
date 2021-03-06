
# -*- coding: utf-8 -*-

# uptime.py
# sbl github.com/liberto
# a py3status module. diplays machine uptime.

from __future__ import division
from time import time
import os
import requests

def raw_uptime():
    return os.popen("uptime").read()

class Py3status:

    # available configuration parameters
    cache_timeout = 60


    

    def mybattery(self, i3s_output_list, i3s_config):
        """
        This method gets executed by py3status
        """

        response = {
            'cached_until': time() + self.cache_timeout,
            'color':'#99FF33',
            'full_text': ''
        }
        output = "uptime "
        splitRawUptime = raw_uptime().strip().split(" ")
        output+=splitRawUptime[2] + ' ' + splitRawUptime[3]
        if splitRawUptime[3]!='min,':
            output += ' ' + splitRawUptime[4] + ' ' + splitRawUptime[5]
        if output[-1]==' ':
            output = output[:-1]
        if output[-1]==',':
            output = output[:-1]
        response['full_text'] += '{} '.format(output)
        response['full_text'] = response['full_text'].strip()
    
        return response

    

if __name__ == "__main__":
    """
    Test this module by calling it directly.
    """
    print raw_uptime().strip().split(" ")
    from time import sleep
    x = Py3status()
    config = {
        'color_good': '#00FF00',
        'color_bad': '#FF0000',
    }
    while True:
        print(x.mybattery([], config))
	print raw_uptime().strip().split(" ")
        sleep(1)
