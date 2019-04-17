# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:03:22 2017

@author: acox37
"""

from collections import deque

def spinlock(steps, iterations=1):
    vortex = deque([0])
    for num in range(1, iterations + 1):
        vortex.rotate(-steps)
        vortex.append(num)
    return vortex

#test = spinlock(3, 2017)
#print(list(test)[0])
#vortex = spinlock(312, 2017)
#print(list(vortex)[0])
vortex = spinlock(312, 50000000)
index = list(vortex).index(0) + 1
vortex.rotate(-index)
print(list(vortex)[0])
