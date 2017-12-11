# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 11:33:55 2017

@author: acox37
"""

from collections import deque
from itertools import cycle

def reallocate(inp):
    while True:
        indices = deque([_i for _i in range(len(inp))])
        index_ = inp.index(max(inp))
        hold = inp[index_]
        inp[index_] = 0
        indices.rotate(-index_ - 1)
        indices_ = cycle(indices)
        while True:
            if hold > 0:
                inp[next(indices_)] += 1
                hold -= 1
            else:
                break
        yield inp

test = [0, 2, 7, 0]

def test1(inp):
    configurations = []
    for config in reallocate(inp):
        if config in configurations:
            return len(configurations) + 1
        else:
            configurations.append(list(config))

print(test1(test))

def part1(inp_file):
    inp = []
    with open(inp_file, 'r') as f:
        for line in f:
            inp.extend(int(_i) for _i in line.strip().split())
    configurations = []
    for count, config in enumerate(reallocate(inp)):
        if config in configurations:
            return len(configurations) + 1
        elif count > 10000:
            raise ValueError('Infinite loop')
        else:
            configurations.append(list(config))

print(part1('day6_input.txt'))

def part2(inp_file):
    inp = []
    with open(inp_file, 'r') as f:
        for line in f:
            inp.extend(int(_i) for _i in line.strip().split())
    configurations = []
    for count, config in enumerate(reallocate(inp)):
        if config in configurations:
            return len(configurations) - configurations.index(config)
        elif count > 10000:
            raise ValueError('Infinite loop')
        else:
            configurations.append(list(config))

print(part2('day6_input.txt'))
