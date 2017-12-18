

def process_stream(stream):
    stream = iter(stream)
    processed, garbage, garbage_flag = '', '', False
    while True:
        try:
            char = next(stream)
            if char == '!':
                next(stream)
            elif garbage_flag:
                if char == '>':
                    garbage_flag = False
                else:
                    garbage += char
            elif char == '<':
                garbage_flag = True
            else:
                processed += char
        except StopIteration:
            break
    value, score_total = 0, 0
    for char in processed:
        if char == '{':
            value += 1
        elif char == '}':
            score_total += value
            value -= 1
    return score_total, garbage
        
    
tests = ['{}', '{{{}}}', '{{}, {}}', '{{{},{},{{}}}}', '{<a>,<a>,<a>,<a>}',
         '{{<ab>},{<ab>},{<ab>},{<ab>}}', '{{<!!>},{<!!>},{<!!>},{<!!>}}',
         '{{<a!>},{<a!>},{<a!>},{<ab>}}']
for test in tests:
    score, _ = process_stream(test)
    print(score)

tests = ['<>', '<random characters>', '<<<<>', '<{!>}>', '<!!>', '<!!!>>',
         '<{o"i!a,<{i<a>']
for test in tests:
    _, garbage = process_stream(test)
    print(len(garbage))
    
stream = ''
with open('day9_input.txt', 'r') as f:
    for line in f:
        stream += line.strip()
score, garbage = process_stream(stream)
print(score)
print(len(garbage))  
