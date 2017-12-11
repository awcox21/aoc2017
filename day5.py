# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 10:09:59 2017

@author: acox37
"""

test = [0, 3, 0, 1, -3]

def jumps(inp):
    position, count = 0, 0
    while True:
        try:
            jump = inp[position]
        except IndexError:
            break
        inp[position] += 1
        position += jump
        count += 1
        if position < 0:
            break
    return count, inp

print(jumps(test))

def part1(inp_file):
    instructions = []
    with open(inp_file, 'r') as f:
        for line in f:
            instructions.append(int(line.strip()))
    return jumps(instructions)

num, _ = part1('day5_input.txt')
print(num)

test = [0, 3, 0, 1, -3]

def jumps2(inp):
    position, count = 0, 0
    while True:
        try:
            jump = inp[position]
        except IndexError:
            break
        if jump >= 3:
            inp[position] -= 1
        else:
            inp[position] += 1
        position += jump
        count += 1
        if position < 0:
            break
    return count, inp

print(jumps2(test))

def part2(inp_file):
    instructions = []
    with open(inp_file, 'r') as f:
        for line in f:
            instructions.append(int(line.strip()))
    return jumps2(instructions)

num, _ = part2('day5_input.txt')
print(num)
