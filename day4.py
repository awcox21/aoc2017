# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 13:06:45 2017

@author: acox37
"""

def valid_passphrase(inp):
    list_ = inp.split()
    return sorted(list(set(list_))) == sorted(list_)

tests = ['aa bb cc dd ee', 'aa bb cc dd aa', 'aa bb cc dd aaa']
for test in tests:
    print(valid_passphrase(test))

def part1(txt):
    num_valid = 0
    with open(txt, 'r') as f:
        for line in f:
            line = line.strip()
            if valid_passphrase(line):
                num_valid += 1
    return num_valid

print(part1('day4_input.txt'))

def valid_2(inp):
    list_ = [''.join(sorted(word)) for word in inp.split()]
    return sorted(list(set(list_))) == sorted(list_)

tests = ['abcde fghij', 'abcde xyz ecdab', 'a ab abc abd abf abj',
         'iiii oiii ooii oooi oooo', 'oiii ioii iioi iiio']
for test in tests:
    print(valid_2(test))

def part2(txt):
    num_valid = 0
    with open(txt, 'r') as f:
        for line in f:
            line = line.strip()
            if valid_2(line):
                num_valid += 1
    return num_valid

print(part2('day4_input.txt'))
