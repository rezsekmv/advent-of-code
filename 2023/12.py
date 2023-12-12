import sys
sys.path.append('../advent_of_code')
from input_data import get_data

text = get_data(12, 2023, True)
lines = text.split('\n')
cache = dict()

def check_string(row: str, arrange: list):
    
    if '?' in row:
        return check_string(row.replace('?', '.', 1), arrange) + check_string(row.replace('?', '#', 1), arrange)

    if len(row) == 0 and len(arrange) == 0:
        return 1

    if '#' not in row:
        if len(arrange) == 0:
            return 1
        else:
            return 0
    elif len(arrange) == 0:
        return 0


    if row in cache.keys() and cache[row] == arrange[0]:
        print('yays')
        return 1

    hash_idx = row.index('#')
    i = 0
    while hash_idx+i < len(row) and row[hash_idx+i] == '#':
        i += 1

    if arrange[0] == i:
        cache[row[:hash_idx+i]] = arrange[0]
        return check_string(row[hash_idx+i:], arrange[1:])


    return 0

ans = 0
for i, line in enumerate(lines):
    # print(i)
    data, sep = line.split(' ')
    s = []
    for se in sep.split(','):
        s.append(int(se))
    a = check_string(data + ('?' + data)*4, s*5)
    # a = check_string(data, s)
    ans += a
    print(a)
    
print(ans)
