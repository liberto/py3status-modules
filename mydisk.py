
# -*- coding: utf-8 -*-

# uptime.py
# sbl github.com/liberto
# a py3status module. diplays machine uptime.

from __future__ import division
from time import time
import os
import requests

def raw_df():
    return os.popen("df -h").read()

class Py3status:

    # available configuration parameters
    cache_timeout = 60


    

    def mydisk(self, i3s_output_list, i3s_config):
        """
        This method gets executed by py3status
        """

        response = {
            'cached_until': time() + self.cache_timeout,
            'color':'#FF3399',
            'full_text': ''
        }
        output = "uptime "
        splitDf = raw_df().strip().split("\n")
        x=0
        while splitDf[x][:27] != '/dev/mapper/ubuntu--vg-root':
            x+=1
        splitLine = splitDf[x].split(" ")
        output = splitLine[8] + " remaining"
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
        print(x.mydisk([], config))
        sleep(1)
