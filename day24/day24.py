"""
Heavily pulled from reddit

https://www.reddit.com/r/adventofcode/comments/7lte5z/2017_day_24_solutions/drovs1c?utm_source=share&utm_medium=web2x
"""
# inp = 'day24test.txt'
inp = 'day24.inp'

def run(b, d):
    available = [i for i in d if b[1] in i]
    if not available:
        yield b
    else:
        for i in available:
            d_ = d.copy()
            d_.remove(i)
            for q in run((b[0] + [i], i[0] if b[1] == i[1] else i[1]), d_):
                yield q

data = list()
with open(inp, 'r') as f:
    for line in f:
        data.append(tuple(map(int, line.split('/'))))

bridge = (list(), 0)

# part 1
print(max(map(
    lambda bridge: sum([a + b for a, b in bridge[0]]), run(bridge, data))))

# part 2
max_len = max(map(lambda bridge: len(bridge[0]), run(bridge, data)))
longest = filter(lambda bridge: len(bridge[0]) == max_len, run(bridge, data))
print(max(map(lambda bridge: sum([a + b for a, b in bridge[0]]), longest)))
