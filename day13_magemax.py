# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:17:25 2017

@author: acox37
"""

d={}
with open("day13_input.txt") as maf:
    for line in maf:
        l=line.strip().split(": ")
        d[int(l[0])]=int(l[1])

j=len(d)

s=0
for i in d.keys():
    k=d[i]
    if i%(2*k-2)==0:
       s+=i*k

print s

de=0
ok=False
while not ok:
    ok=True
    for i in d.keys():
        k=d[i]
        if (i+de)%(2*k-2)==0:
           ok=False
           de+=1
           break

print de
