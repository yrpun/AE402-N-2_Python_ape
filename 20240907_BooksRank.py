# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:40:06 2024

@author: cclin
"""

import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.books.com.tw/web/sys_saletopb/books/?attribute=30&loc=P_0008_books_002')
soup = BeautifulSoup(res.text,'html.parser')
divs = soup.find_all("div",class_="type02_bd-a")

amount = 0
for index,each_div in enumerate(divs):
    h4 = each_div.find('h4')
    if not h4:
        continue
    a = h4.find('a')
    if not a:
        continue
    bookName = a.text
    print('排名'+str(index+1)+': '+bookName)
    ul = each_div.find('ul')
    lis = ul.find_all('li')
    for each_li in lis:
        strongs = each_li.find_all('strong')
        if strongs:
            b = strongs[-1].find('b')
            print('價格: '+b.text+'元')
        amount+=1
        if amount>4:
            break