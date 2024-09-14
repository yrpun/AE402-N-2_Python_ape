# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:27:51 2024

@author: cclin
"""

#for迴圈(loop)
num = 0

for i in range(10):
    num += i
#print(num)

#遞迴
def recurive(n):
    if n<1:
        return 1
    return n *recurive(n-1)

print(recurive(5))