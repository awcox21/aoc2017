# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:25:08 2017

@author: acox37
"""
import re
from collections import defaultdict


def sound(command, register, played):
    reg = re.match('snd (\w+)', command)
    key = reg.group(1)
    played.append(register[key])
    return register, played, 0, None


def set_(command, register, played):
    reg = re.match('set (\w+) (\w+|[+-]?\d+)', command)
    key, value = reg.group(1), reg.group(2)
    try:
        val = int(value)
    except ValueError:
        val = register[value]
    register[key] = val
    return register, played, 0, None


def add(command, register, played):
    reg = re.match('add (\w+) (\w+|[+-]?\d+)', command)
    key, value = reg.group(1), reg.group(2)
    try:
        val = int(value)
    except ValueError:
        val = register[value]
    register[key] += val
    return register, played, 0, None


def mul(command, register, played):
    reg = re.match('mul (\w+) (\w+|[+-]?\d+)', command)
    key, value = reg.group(1), reg.group(2)
    try:
        val = int(value)
    except ValueError:
        val = register[value]
    register[key] *= val
    return register, played, 0, None


def mod(command, register, played):
    reg = re.match('mod (\w+) (\w+|[+-]?\d+)', command)
    key, value = reg.group(1), reg.group(2)
    val = register[key]
    try:
        mod_ = int(value)
    except ValueError:
        mod_ = register[value]
    register[key] = val % mod_
    return register, played, 0, None


def rcv(command, register, played):
    reg = re.match('rcv (\w+)', command)
    key = reg.group(1)
    if register[key] == 0:
        recovered = None
    else:
        recovered = played[-1]
    return register, played, 0, recovered


def jgz(command, register, played):
    reg = re.match('jgz (\w+) (\w+|[+-]?\d+)', command)
    key, value = reg.group(1), reg.group(2)
    if register[key] == 0:
        return register, played, 0, None
    else:
        try:
            jump = int(value)
        except ValueError:
            jump = register[value]
    return register, played, jump, None


def execute(path):
    commands = []
    register = defaultdict(int)
    played = []
    with open(path, 'r') as f:
        for line in f:
            commands.append(line)
    index, command = 0, commands[0]
    while True:
        try:
            register, played, jump, recovered = sound(command, register, played)
        except AttributeError:
            try:
                register, played, jump, recovered = set_(command, register, played)
            except AttributeError:
                try:
                    register, played, jump, recovered = add(command, register, played)
                except AttributeError:
                    try:
                        register, played, jump, recovered = mul(command, register, played)
                    except AttributeError:
                        try:
                            register, played, jump, recovered = mod(command, register, played)
                        except AttributeError:
                            try:
                                register, played, jump, recovered = rcv(command, register, played)
                            except AttributeError:
                                try:
                                    register, played, jump, recovered = jgz(command, register, played)
                                except AttributeError:
                                    print(command)
        if recovered is not None:
            print('Recovered : {}'.format(recovered))
            break
        if jump != 0:
            move = jump
        else:
            move = 1
        try:
            index += move
            command = commands[index]
        except IndexError:
            break
    return register, played


# test_register, test_played = execute('day18_test.txt')
# register, played = execute('day18_input.txt')


class Program(object):
    def __init__(self, id_):
        self.register = defaultdict(int)
        self.register['p'] = id_
        self.sent = []
        self.received = []

    def __call__(self, command):
        sent = list(self.sent)
        try:
            self.register, self.sent, jump, recovered = self.sound(command, self.register, self.sent)
        except AttributeError:
            try:
                self.register, self.sent, jump, recovered = self.set_(command, self.register, self.sent)
            except AttributeError:
                try:
                    self.register, self.sent, jump, recovered = self.add(command, self.register, self.sent)
                except AttributeError:
                    try:
                        self.register, self.sent, jump, recovered = self.mul(command, self.register, self.sent)
                    except AttributeError:
                        try:
                            self.register, self.sent, jump, recovered = self.mod(command, self.register, self.sent)
                        except AttributeError:
                            try:
                                self.register, self.sent, jump, recovered = self.rcv(command, self.register, self.sent)
                            except AttributeError:
                                self.register, self.sent, jump, recovered = self.jgz(command, self.register, self.sent)
        if sent != self.sent:
            sent = self.sent[-1]
        else:
            sent = None
        if recovered is not None:
            try:
                self.register[recovered] = self.received.pop(0)
                return jump, sent
            except IndexError:
                return 0, sent
        else:
            return jump, sent

    def sound(self, command, register, played):
        reg = re.match('snd (\w+)', command)
        key = reg.group(1)
        played.append(register[key])
        return register, played, 1, None

    def set_(self, command, register, played):
        reg = re.match('set (\w+) (\w+|[+-]?\d+)', command)
        key, value = reg.group(1), reg.group(2)
        try:
            val = int(value)
        except ValueError:
            val = register[value]
        register[key] = val
        return register, played, 1, None

    def add(self, command, register, played):
        reg = re.match('add (\w+) (\w+|[+-]?\d+)', command)
        key, value = reg.group(1), reg.group(2)
        try:
            val = int(value)
        except ValueError:
            val = register[value]
        register[key] += val
        return register, played, 1, None

    def mul(self, command, register, played):
        reg = re.match('mul (\w+) (\w+|[+-]?\d+)', command)
        key, value = reg.group(1), reg.group(2)
        try:
            val = int(value)
        except ValueError:
            val = register[value]
        register[key] *= val
        return register, played, 1, None

    def mod(self, command, register, played):
        reg = re.match('mod (\w+) (\w+|[+-]?\d+)', command)
        key, value = reg.group(1), reg.group(2)
        val = register[key]
        try:
            mod_ = int(value)
        except ValueError:
            mod_ = register[value]
        register[key] = val % mod_
        return register, played, 1, None

    def rcv(self, command, register, played):
        reg = re.match('rcv (\w+)', command)
        key = reg.group(1)
        return register, played, 1, key

    def jgz(self, command, register, played):
        reg = re.match('jgz (\w+) (\w+|[+-]?\d+)', command)
        key, value = reg.group(1), reg.group(2)
        if register[key] == 0:
            return register, played, 1, None
        else:
            try:
                jump = int(value)
            except ValueError:
                jump = register[value]
        return register, played, jump, None


def part2(path):
    commands = []
    with open(path, 'r') as f:
        for line in f:
            commands.append(line)
    program0, program1 = Program(0), Program(1)
    index0, index1 = 0, 0
    done0, done1 = False, False
    while True:
        try:
            command0 = commands[index0]
            jump0, sent0 = program0(command0)
            index0 += jump0
        except IndexError:
            done0 = True
        try:
            command1 = commands[index1]
            jump1, sent1 = program1(command1)
            index1 += jump1
        except IndexError:
            done1 = True
        if done0 and done1:
            break
        elif jump0 == 0 and jump1 == 0:
            break
        else:
            if sent0 is not None:
                program1.received.append(sent0)
            if sent1 is not None:
                program0.received.append(sent1)
    return len(program1.sent)

sent_length = part2('day18_input.txt')
print(sent_length)
