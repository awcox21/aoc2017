# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 11:48:43 2017

@author: acox37

Returns a lot of information but currently doesn't tell the answer
"""
import re
from collections import defaultdict

class Program(object):
    def __init__(self, name, weight, supporting):
        self.name = name
        self.weight = weight
        self.supporting = supporting


class Tower(object):
    def __init__(self, programs):
        self.programs = programs

    def check_subtowers(self):
        safe, unsafe = [], []
        for program in self.programs:
            name = program.name
            if not program.supporting:
                safe.append(name)
            else:
                subtowers = []
                for supported in program.supporting:
                    subtowers.append(self.get_supported_weight(supported))
                if all(_i == subtowers[0] for _i in subtowers[1:]):
                    safe.append(name)
                else:
                    unsafe.append(tuple([name, subtowers]))

        return safe, unsafe

    def get_base(self):
        names, supported = list(), set()
        for program in programs:
            names.append(program.name)
            supported.update(program.supporting)
        return set(names).difference(supported).pop()

    def get_program(self, program_name):
        for program in self.programs:
            if program.name == program_name:
                return program
        else:
            raise KeyError('Program not found')

    def get_supported_weight(self, supported):
        base_name = self.get_base()
        weight_stack = self.get_weight_stack(base_name)
        supported_program = self.get_program(supported)
        tower_weight = [supported_program.weight]

        def get_weight(self, base):
            for key, weight in weight_stack[base]:
                tower_weight.append(weight)
                supported = self.get_program(key)
                if supported.supporting:
                    get_weight(self, supported)

        get_weight(self, supported)
        return sum(tower_weight)


    def get_weight_stack(self, base_name):
        program = self.get_program(base_name)
        weight_stack = defaultdict(list)

        def get_weight(self, program):
            key = program.name
            for name in program.supporting:
                supported = self.get_program(name)
                weight_stack[key].append(
                        tuple([supported.name, supported.weight]))
                get_weight(self, supported)

        get_weight(self, program)
        return weight_stack



def unpack(inp):
    programs = []
    with open(inp, 'r') as f:
        for line in f:
            line = line.strip()
            name = re.match('\w+', line).group()
            weight = int(re.search('\d+', line).group())
            try:
                supporting = line.split('->')[1].split(',')
                supporting = [_.strip() for _ in supporting]
            except IndexError:
                supporting = []
            programs.append(Program(name, weight, supporting))
    return programs



programs = unpack('day7_test.txt')
tower = Tower(programs)
print(tower.get_base())
print(tower.check_subtowers())

programs = unpack('day7_input.txt')
tower = Tower(programs)
print(tower.get_base())
weight_stack = tower.get_weight_stack(tower.get_base())
safe, unsafe = tower.check_subtowers()
