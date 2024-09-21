# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:08:23 2024

@author: cclin
"""

import requests
import json

num = 1
while num < 6:
    
    responce = requests.get('https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page={}&sort=sale/dc'.format(num))
    jsonData = json.loads(responce.text)