import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from copy import deepcopy

lines = get_data(3, 2021).split('\n')
lenght = len(lines[0])

def calc(remaining: list, most_common: bool) -> str:
    for i in range(lenght):
        count = [0, 0]
        for line in remaining:
            if line[i] == '0':
                count[0] += 1
            elif line[i] == '1':
                count[1] += 1    
        
        to_eq = None
        if most_common:
            to_eq = '0' if count[0] > count[1] else '1'
        else:
            to_eq = '1' if count[0] > count[1] else '0'
            
        remaining = list(filter(lambda line: line[i] == to_eq, remaining))
        if len(remaining) == 1:
            return remaining[0]


o2 = calc(deepcopy(lines), True)
co2 = calc(deepcopy(lines), False)

print(int(o2, 2) * int(co2, 2))
