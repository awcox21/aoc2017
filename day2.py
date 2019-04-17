# -*- coding: utf-8 -*-
"""
Created on Sat Dec 02 13:40:19 2017

@author: Adam Cox
"""
from itertools import combinations

test_spreadsheet = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]

def checksum(spreadsheet):
    if isinstance(spreadsheet, str):
        spreadsheet_ = []
        with open(spreadsheet, 'r') as f:
            for row in f:
                spreadsheet_.append([int(_i) for _i in row.strip().split()])
        spreadsheet = spreadsheet_
    checksum = 0
    for row in spreadsheet:
        checksum += max(row) - min(row)
    return checksum

print(checksum(test_spreadsheet))
print(checksum('day2_input.dat'))

test_spreadsheet = [[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]

def checksum2(spreadsheet):
    if isinstance(spreadsheet, str):
        spreadsheet_ = []
        with open(spreadsheet, 'r') as f:
            for row in f:
                spreadsheet_.append([int(_i) for _i in row.strip().split()])
        spreadsheet = spreadsheet_
    checksum = 0
    for row in spreadsheet:
        for a, b in combinations(sorted(row), 2):
            if b % a == 0:
                checksum += b / a
                break
    return checksum

print(checksum2(test_spreadsheet))
print(checksum2('day2_input.dat'))
