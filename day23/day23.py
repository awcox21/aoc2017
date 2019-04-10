"""
https://www.reddit.com/r/adventofcode/comments/7lms6p/2017_day_23_solutions/drngit2?utm_source=share&utm_medium=web2x
https://github.com/dp1/AoC17/blob/master/day23.5.txt
"""
import re

inp = 'day23.inp'
cmds = list(map(lambda x: x.split(), open(inp, 'r').readlines()))
regs = [0 for _ in range(8)]

def getval(r):
    """
    Extract value from command or get value or reg
    """
    if re.match(r'[\-0-9]', r):
        return int(r)
    else:
        return regs[ord(r) - 97]  # ord is a pointer, a is 97 so offset to 0

# Part 1
i, m = 0, 0
while 0 <= i < len(cmds):
    cmd = cmds[i]
    c = cmd[0]
    if c == 'jnz':
        if getval(cmd[1]) != 0:
            i += getval(cmd[2])
        else:
            i += 1
    else:
        if c == 'set':
            regs[ord(cmd[1]) - 97] = getval(cmd[2])
        elif c == 'sub':
            regs[ord(cmd[1]) - 97] -= getval(cmd[2])
        elif c == 'mul':
            regs[ord(cmd[1]) - 97] *= getval(cmd[2])
            m += 1
        i += 1
print(m)
print(regs)
"""
Part 2
------
b when a != 1
b = 93 * 100 + 100000 = 109300
c = c + 17000 = 126300
"""
h = 0
for x in range(109300, 126300 + 1, 17):
    for i in range(2, x):
        if not x % i:
            h += 1
            break
print(h)
