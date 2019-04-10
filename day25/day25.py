import re
from collections import namedtuple


class State(object):
    def __init__(self, key, conditions):
        self.key = key
        self.conditions = conditions

    def __str__(self):
        return self.key

    def __call__(self, tape, loc):
        cont = None
        for condition in self.conditions:
            try:
                cont, loc = condition(tape, loc)
            except ValueError:
                pass
            else:
                break
        if cont is None:
            raise ValueError('No conditions matched')
        return cont, loc

    @classmethod
    def from_str(cls, s):
        lines = s.splitlines()
        key = re.search(r'In state (\w+)', lines[0]).group(1)
        str_ = str()
        strings = list()
        for line in lines[1:]:
            if re.match(r'If', line.strip()):
                if str_.strip():
                    strings.append(str_)
                    str_ = str()
                str_ += line + '\n'
            elif re.match(r'-', line.strip()):
                str_ += line + '\n'
        else:
            strings.append(str_)
        conditions = list(map(lambda x: Condition.from_str(x), strings))
        return cls(key, conditions)


class Condition(object):
    def __init__(self, value, write, move, cont):
        self.value = value
        self.write = write
        self.move = move
        self.cont = cont

    def __call__(self, tape, loc):
        if loc in tape:
            value = 1
        else:
            value = 0
        if value == self.value:
            if self.write:
                tape[loc] = 1
            elif loc in tape:
                tape.pop(loc)
            if self.move == 'left':
                loc -= 1
            else:
                loc += 1
        else:
            raise ValueError('Condition does not match')
        return self.cont, loc

    @classmethod
    def from_str(cls, s):
        lines = iter(s.splitlines())
        value = int(re.search(r'\d+', next(lines)).group())
        write = int(re.search(r'\d+', next(lines)).group())
        move = re.search(r'left|right', next(lines)).group()
        cont = re.search(r'state (\w+)', next(lines)).group(1)
        return cls(value, write, move, cont)


# inp = 'day25test.txt'
inp = 'day25.inp'
with open(inp, 'r') as f:
    start = re.match(r'Begin in state (\w+)', next(f)).group(1)
    steps = int(re.search(r'\d+', next(f)).group(0))
    next(f)
    states = dict()
    str_ = str()
    for line in f:
        if line.strip():
            str_ += line
        elif str_.strip():
            state = State.from_str(str_)
            states[str(state)] = state
            str_ = str()
        else:
            pass
    else:
        if str_.strip():
            state = State.from_str(str_)
            states[str(state)] = state

state = states[start]
tape, loc = dict(), 0
for _ in range(steps):
    state, loc = states[str(state)](tape, loc)
print(sum(tape.values()))
