# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 11:54:58 2017

@author: Adam Cox
"""


def gen(start, factor, length):
    divisor = 2147483647
    current = start
    count = 0
    while count < length:
        next_ = (current * factor) % divisor
        yield next_
        count += 1
        current = next_


def gen_(start, factor, multiple, length):
    divisor = 2147483647
    current = start
    count = 0
    while count < length:
        next_ = (current * factor) % divisor
        if next_ % multiple == 0:
            yield next_
            count += 1
        current = next_


def judge(gen1, gen2):
    count = 0
    for val1, val2 in zip(gen1, gen2):
        bin1 = '{:016d}'.format(int(format(val1, 'b')))
        bin2 = '{:016d}'.format(int(format(val2, 'b')))
        if bin1[-16:] == bin2[-16:]:
            count += 1
    return count


#length = 5
#length = int(4e7)
#test_gen1 = gen(65, 16807, length)
#test_gen2 = gen(8921, 48271, length)
#for val1, val2 in zip(test_gen1, test_gen2):
#    print(val1, val2)
#test_count = judge(test_gen1, test_gen2)
#print(count)

#gen1 = gen(703, 16807, length)
#gen2 = gen(516, 48271, length)
#count = judge(gen1, gen2)
#print(count)

#length = 5
#length = 1056
length = int(5e6)
#test_gen1 = gen_(65, 16807, 4, length)
#test_gen2 = gen_(8921, 48271, 8, length)
#for val1, val2 in zip(test_gen1, test_gen2):
#    print(val1, val2)
#test_count = judge(test_gen1, test_gen2)
#print(test_count)

gen1 = gen_(703, 16807, 4, length)
gen2 = gen_(516, 48271, 8, length)
count = judge(gen1, gen2)
print(count)
