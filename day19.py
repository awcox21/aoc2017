# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:24:15 2017

@author: acox37
"""
from string import ascii_uppercase

def move(x, y, direction):
    if direction == 'up':
        x -= 1
    elif direction == 'down':
        x += 1
    elif direction == 'left':
        y -= 1
    elif direction == 'right':
        y += 1
    return x, y

def read_map(path):
    mapping = dict()
    with open(path, 'r') as f:
        for x, line in enumerate(f):
            for y, char in enumerate(line.rstrip()):
                if char != ' ':
                    mapping[(x, y)] = char
                    if x == 0:
                        start = (x, y)
    return mapping, start

def travel(mapping, start):
    direction = 'down'
    x, y = start
    steps, string = 1, ''
    while True:
        if direction in ['left', 'right']:
            others = ['up', 'down']
        else:
            others = ['left', 'right']
        x_, y_ = move(x, y, direction)
        if (x_, y_) in mapping:
            steps += 1
            x, y = x_, y_
            if mapping[(x, y)] in ascii_uppercase:
                string += mapping[(x, y)]
        else:
            for new in others:
                x_, y_ = move(x, y, new)
                if (x_, y_) in mapping:
                    direction = new
                    break
            else:
                break
    return steps, string

test_map, start = read_map('day19.test')
test_steps, test = travel(test_map, start)
print(test)
print(test_steps)

mapping, start = read_map('day19.in')
steps, string = travel(mapping, start)
print(string)
print(steps)

