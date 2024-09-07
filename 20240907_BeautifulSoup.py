# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:51:42 2024

@author: cclin
"""

html_sample = '''
<html>
<head>
<title>Story</title>
</head>
<body>
<a href="www.a.com"class="L">A</a>
<p class="story">在很久以前，有一個國家叫猿創力
</p>
<a href="www.b.com"class="I">B</a>
</body>
</html>'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_sample,'html.parser')

print(soup.find_all('a'))