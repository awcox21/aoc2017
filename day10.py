from collections import deque
from functools import reduce
from operator import xor

def knot_hash(inp, lengths, num_rounds=1):
    deque_ = deque(inp)
    index, skip = 0, 0
    for _ in range(num_rounds):
        for length in lengths:
            deque_.rotate(-index)
            _deque = list(reversed(list(deque_)[:length])) + list(deque_)[length:]
            deque_ = deque(_deque)
            deque_.rotate(index)
            index += length + skip
            skip += 1
    return list(deque_)
    
def part2(inp, length_string, num_rounds):
    lengths = [ord(_i) for _i in length_string]
    lengths += [17, 31, 73, 47, 23]
    hashed = knot_hash(inp, lengths, num_rounds)
    output = ''.join([hex(reduce(xor, hashed[16 * _i: 16 * _i + 16]))[-2:] for _i
                      in range(16)])
    return output
    
        

test_list = [0, 1, 2, 3, 4]
test_lengths = [3, 4, 1, 5]
test_hashed = knot_hash(test_list, test_lengths)
print(test_hashed, test_hashed[0] * test_hashed[1])

inp_list = [_ for _ in range(256)]
inp_lengths = [70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41]
inp_hashed = knot_hash(inp_list, inp_lengths)
print(inp_hashed[0] * inp_hashed[1])

inp_list = [_ for _ in range(256)]
inp_length_string = '70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41'
output = part2(inp_list, inp_length_string, 64)
with open('day10_output.txt', 'w') as f:
    f.write('{}\n'.format(output))
