# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 14:15:37 2017

@author: acox37
"""
from collections import deque
from operator import xor
from scipy.ndimage.measurements import label
from numpy import array


def knot_hash(inp, rounds=64):
    lengths = [ord(_i) for _i in inp]
    lengths += [17, 31, 73, 47, 23]
    deque_ = deque([_ for _ in range(256)])
    index, skip = 0, 0
    for _ in range(rounds):
        for length in lengths:
            deque_.rotate(-index)
            _deque = (list(reversed(list(deque_)[:length])) +
                      list(deque_)[length:])
            deque_ = deque(_deque)
            deque_.rotate(index)
            index += length + skip
            skip += 1
    list_ = list(deque_)
    hash_ = ''
    for i in range(16):
        entry = format(reduce(xor, list_[16 * i: 16 * i + 16]), 'x')
        if len(entry) == 1:
            entry = '0' + entry
        hash_ += entry
    return hash_


def part1(inp):
    used = 0
    for row in range(128):
        row_inp = inp + '-{}'.format(row)
        row_hash = knot_hash(row_inp)
        row_bin = ''.join(
                ['{:04d}'.format(int(bin(int(_i, 16)).split('b')[-1])) for _i
                 in row_hash])
        used += row_bin.count('1')
    return used


def get_array(inp):
    array_ = []
    for row in range(128):
        row_inp = inp + '-{}'.format(row)
        row_hash = knot_hash(row_inp)
        row = []
        for hex_ in row_hash:
            row.append('{:04d}'.format(
                    int(format(int('0x{}'.format(hex_), 16), 'b'))))
        row_bin = ''.join(row)
        array_.append([int(_) for _ in row_bin])
    return array(array_)


test = 'flqrgnkx'
test_used = part1(test)
test_array = get_array(test)
_, regions = label(test_array)
print(regions)

inp = 'xlqgujun'
used = part1(inp)
array_ = get_array(inp)
labeled, regions = label(array_)
print(regions)
