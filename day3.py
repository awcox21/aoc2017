# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 11:56:48 2017

@author: acox37
"""
import math
from itertools import count
# Part 1


def spiral_memory(inp):
    side = int(math.ceil(math.sqrt(inp)))
    if side % 2 == 0:
        side += 1
    axes = ([int(side ** 2 - ((side - 1) * _i) - math.floor(side / 2)) for _i
             in range(4)])
    offset = min([abs(_i - inp) for _i in axes])
    return (side - 1) / 2 + offset


test_inputs = [1, 12, 23, 1024]
for inp in test_inputs:
    print(spiral_memory(inp))

print(spiral_memory(368078))

# Part 2 code from https://www.reddit.com/r/adventofcode/comments/7h7ufl/2017_day_3_solutions/dqox0fv/?st=jasic11f&sh=cb0dfe44

def sum_spiral():
    a, i, j = {(0, 0): 1}, 0, 0

    sn = lambda i,j: sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                         for l in range(j-1,j+2))

    for s in count(1, 2):
        for _ in range(s):
            i += 1
            a[i, j] = sn(i, j)
            yield a[i, j]
        for _ in range(s):
            j -= 1
            a[i, j] = sn(i, j)
            yield a[i, j]
        for _ in range(s+1):
            i -= 1
            a[i, j] = sn(i, j)
            yield a[i, j]
        for _ in range(s+1):
            j += 1
            a[i, j] = sn(i, j)
            yield a[i, j]


def part2(n):
    for x in sum_spiral():
        if x > n:
            return x

print(part2(368078))
