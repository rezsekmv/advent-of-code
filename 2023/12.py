import sys
sys.path.append('../advent_of_code')
from input_data import get_data
import functools

text = get_data(12, 2023)
lines = text.split('\n')

def handle_dot(row, arrange):
    return calc(row[1:], arrange)

def handle_hash(row, arrange):
    # replace '?'s with '#'s
    group = row[:arrange[0]].replace('?', '#')

    # check if there is a '.' in char 
    if group != arrange[0] * '#':
        return 0
    # from now group only contains arrange[0]*'#'
    
    # if last group
    if len(arrange) == 1:
        # there can't be more '#'-s after this group
        if '#' in row[arrange[0]:]:
            return 0
        else:
            return 1 

    # if next char is separator
    if len(row) > arrange[0] and row[arrange[0]] in '?.':
        # skip this group and the separator character and remove current arrange
        return calc(row[arrange[0]+1:], arrange[1:])

    # everything else is wrong
    return 0


# add cache functionality
@functools.cache
def calc(row: str, arrange: list):
    # out of arrange numbers
    if not arrange:
        if '#' not in row:
            return 1
        else:
            return 0
    # arrange is not empty

    # out of characters
    if not row:
        return 0

    result = 0
    # if next char is '.'
    if row[0] == '.':
        result = handle_dot(row, arrange)

    # if next char is '#'
    if row[0] == '#':
        result = handle_hash(row, arrange)

    # if next char is '?' check both '.' and '#' possibilities
    if row[0] == '?':
        result = handle_dot(row, arrange) + handle_hash(row, arrange)

    # print(row, arrange, result)
    return result



p1 = 0
p2 = 0
for i, line in enumerate(lines):
    data, sep = line.split(' ')
    s = tuple([int(se) for se in sep.split(',')])
    
    p1comb = calc(data, s)
    p2comb = calc(data + ('?' + data)*4, s*5)

    p1 += p1comb
    p2 += p2comb
    
print(p1)
print(p2)