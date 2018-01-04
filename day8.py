from collections import defaultdict

def evaluate_instructions(instructions):
    max_ = 0
    register = defaultdict(int)
    for instruction in instructions:
        reg, move, increment, _if, check, cond, value = instruction.strip().split()
        if eval("register[check]" + cond + value):
            if move == 'inc':
                register[reg] += int(increment)
            else:
                register[reg] -= int(increment)
            max_ = max(max_, register[reg])
    return register, max_
    
test = ['b inc 5 if a > 1',
        'a inc 1 if b < 5',
        'c dec -10 if a >= 1',
        'c inc -20 if c == 10']
        
reg, max_ = evaluate_instructions(test)
print(max(reg.values()))
print(max_)

reg, max_ = evaluate_instructions(open('day8_input.txt', 'r'))
print(max(reg.values()))
print(max_)
    