import sys
sys.path.append('../advent_of_code')
from input_data import get_data

text = get_data(12, 2023)
lines = text.split('\n')

def check_char(row: str, arrange, hash_count, C):

    if len(row) == 0:
        if len(arrange) == 0:
            return 1
        elif len(arrange) == 1:
            if arrange[0] == hash_count:
                return 1
            else:
                return 0
        else: 
            return 0

    if len(arrange) == 0:
        if all([i=='.' or i=='?' for i in row]):
            return 1
        else:
            return 0


    if hash_count > arrange[0]:
        return 0

    if row[0] == '#':
        a = check_char(row[1:], arrange, hash_count+1, C)
        if a == 1:
            C.add(row)
        return a

    if row[0] == '.':
        if hash_count > 0:
            if hash_count == arrange[0]:
                a = check_char(row[1:], arrange[1:], 0, C)
                if a == 1:
                    C.add(row)
                return a
            else:
                return 0
        else:
            return check_char(row[1:], arrange, 0)
    
    if row[0] == '?':
        return check_char('.'+row[1:], arrange, hash_count, C) + check_char('#'+row[1:], arrange, hash_count, C)

    assert False


ans = 0
for i, line in enumerate(lines):
    print(i)
    data, sep = line.split(' ')
    s = []
    for se in sep.split(','):
        s.append(int(se))
    a = check_char(data + ('?' + data)*4, s*5, 0, set())
    ans += a
    
print(ans)
