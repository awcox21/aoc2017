# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:33:14 2017

@author: acox37
"""

def process(network_file):
    keys, values = [], []
    with open(network_file, 'r') as f:
        for line in f:
            key, value = line.strip().split(' <-> ')
            keys.append(int(key))
            values.append([int(_value) for _value in value.split(', ')])
    return dict(tuple([key, value]) for key, value in zip(keys, values))

def connections(network, destination=0):
    connected = set([destination])
    for _ in range(10):
        for key in network:
            if destination == key:
                connected.update([key] + network[key])
            elif key in connected:
                connected.update([key] + network[key])
            elif any(program in connected for program in network[key]):
                connected.update([key] + network[key])
    return sorted(list(connected))

def find_groups(network):
    groups = []
    for key in network:
        if not any(key in group for group in groups):
            groups.append(connections(network, key))
    return groups

test = 'day12_test.txt'
test_net = process(test)
test_connected = connections(test_net)
print(len(test_connected))
test_groups = find_groups(test_net)
print(len(test_groups))

inp = 'day12_input.txt'
inp_net = process(inp)
inp_connected = connections(inp_net)
print(len(inp_connected))
inp_groups = find_groups(inp_net)
print(len(inp_groups))
