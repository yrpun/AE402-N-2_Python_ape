# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:33:15 2024

@author: cclin
"""

import requests
import json
from bs4 import BeautifulSoup

date = input("哪一天開始查詢早鳥優惠(格式:2023/05/05)? ")

def searchTHSR(date):
    payload = {"SearchType": "S",
            "Lang": "TW",
            "StartStation": "NanGang",
            "EndStation": "ZuoYing",
            "OutWardSearchDate": date,
            "OutWardSearchTime": "20:00"
            }
    res = requests.post("https://www.thsrc.com.tw/TimeTable/Search",data = payload)

    finish = False
    print(date)
    soup = BeautifulSoup(res.text,"html.parser")
    train_dict = json.loads(soup.text)
    if train_dict['data']['DepartureTable']['TrainItem']:
        for item in train_dict['data']['DepartureTable']['TrainItem']:
            trainNumber = item['TrainNumber']
            DepartureTime = item['DepartureTime']
            DestinationTime = item['DestinationTime']
           
            for discount in item['Discount']:
                name = discount['Name']
                value = discount['Value']
                if name == '早鳥':
                    if int(DepartureTime[0:2]) >= int(payload['OutWardSearchTime'][0:2]):
                        print('車次:'+trainNumber, '出發時間:'+DepartureTime, '抵達時間:'+DestinationTime)
                        print(name, value)
                        finish = True
       
    day = int(date[8:])

    if finish:
        print('查詢完成')
    else:
        day = int(day) + 1
        if day < 10:
            date = date[0:8]+'0'+str(day)
        else:
            date = date[0:8]+str(day)
        searchTHSR(date)
       
searchTHSR(date)