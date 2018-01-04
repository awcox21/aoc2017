# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:19:12 2017

@author: acox37
"""

def hex_walk(path):
    x, y, z = 0, 0, 0
    max_ = 0
    for step in path.split(','):
        if step == 'n':
            x += 1
            y -= 1
        elif step == 'ne':
            y -= 1
            z += 1
        elif step == 'nw':
            x += 1
            z -= 1
        elif step == 's':
            x -= 1
            y += 1
        elif step == 'se':
            x -= 1
            z += 1
        elif step == 'sw':
            y += 1
            z -= 1
        d = distance(tuple([x, y, z]))
        if d > max_:
            max_ = d
    position = tuple([x, y, z])
    return position, max_

def distance(position):
    x, y, z = position
    return (abs(x) + abs(y) + abs(z)) / 2

tests = ['ne,ne,ne', 'ne,ne,sw,sw', 'ne,ne,s,s', 'se,sw,se,sw,sw']
for test in tests:
    test_position, test_max = hex_walk(test)
    test_distance = distance(test_position)
    print(test_position, test_distance, test_max)

inp = ''
with open('day11_input.txt', 'r') as f:
    for line in f:
        inp += line.strip()
inp_position, inp_max = hex_walk(inp)
inp_distance = distance(inp_position)
print(inp_position, inp_distance, inp_max)
