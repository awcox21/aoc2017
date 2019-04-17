from string import ascii_lowercase
import re

#class Memoize(object):
#    def __init__(self, fn):
#        self.fn = fn
#        self.memo = {}
#
#    def __call__(self, *args):
#        if args not in self.memo:
#            self.memo[args] = self.fn(*args)
#        return self.memo[args]

def spin(command, list_):
    reg = re.match('s(\d+)', command)
    num = int(reg.group(1))
    list_ = list_[-num:] + list_[:-num]
    return list_

def exchange(command, list_):
    reg = re.match('x(\d+)/(\d+)', command)
    first, last = int(reg.group(1)), int(reg.group(2))
    list_[first], list_[last] = list_[last], list_[first]
    return list_

def partner(command, list_):
    reg = re.match('p(\w+)/(\w+)', command)
    first, last = reg.group(1), reg.group(2)
    first, last = list_.index(first), list_.index(last)
    list_[first], list_[last] = list_[last], list_[first]
    return list_

def dance(list_, commands, repeat=1):
    memo = {}
    for _ in range(repeat):
        start = ''.join(list_)
        if start in memo:
            list_ = [_i for _i in memo[start]]
        else:
            for command in commands:
                try:
                    list_ = spin(command, list_)
                except AttributeError:
                    try:
                        list_ = exchange(command, list_)
                    except AttributeError:
                        list_ = partner(command, list_)
            memo[start] = ''.join(list_)
    return ''.join(list_)

def day16(path, repeat=1):
    list_ = [_ for _ in ascii_lowercase[:16]]
    commands = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip().split(',')
            commands.extend(line)
    return dance(list_, commands, repeat)

#test_list = [_ for _ in ascii_lowercase[:5]]
#test_commands = ['s1', 'x3/4', 'pe/b']
#test_dance = dance(test_list, test_commands)
#print(test_dance)

path = 'day16_input.txt'
#out = day16(path)
#print(out)
out = day16(path, 10000)  # int(1e9))
print(out)
