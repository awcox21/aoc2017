# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 12:44:36 2017

@author: acox37
"""
from itertools import cycle
from collections import deque

def process(inp_file):
    firewall = dict()
    with open(inp_file, 'r') as f:
        for line in f:
            depth, range_ = line.strip().split(': ')
            firewall[int(depth)] = int(range_)
    return firewall

def get_paths(firewall):
    paths = dict()
    for depth in firewall:
        path = [_ for _ in range(firewall[depth])]
        path.extend(list(reversed(path))[1:-1])
        paths[depth] = path
    return paths


def ride(firewall, paths=None, delay=0, check_caught=False):
    if paths is None:
        paths = get_paths(firewall)
    max_depth = max(firewall.keys())
    cycles = dict()
    for depth in firewall:
        path = paths[depth]
        offset = delay % len(path)
        path = deque(path)
        path.rotate(-offset)
        path = list(path)
        cycles[depth] = cycle(path)
    scanners = dict((depth, None) for depth in firewall.keys())
    scanners = increment(scanners, cycles)
    severity = 0
    for depth in range(max_depth + 1):
        try:
            if scanners[depth] == 0:
                if check_caught:
                    return None, True
                severity += depth * firewall[depth]
            else:
                pass
        except KeyError:
            pass
        scanners = increment(scanners, cycles)
    return severity, False

def increment(scanners, cycles):
    for depth in scanners:
        scanners[depth] = next(cycles[depth])
    return scanners

def get_through(firewall):
    paths = get_paths(firewall)
    delay = 0
    while True:
        _, caught = ride(firewall, paths, delay, True)
        if not caught:
            break
        else:
            delay += 1
    return delay

test = 'day13_test.txt'
test_firewall = process(test)
test_severity, _ = ride(test_firewall)
print(test_severity)
test_delay = get_through(test_firewall)
print(test_delay)

inp = 'day13_input.txt'
firewall = process(inp)
severity, _ = ride(firewall)
print(severity)
delay = get_through(firewall)
print(delay)
