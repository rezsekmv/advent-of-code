import sys
sys.path.append('../advent_of_code')
from input_data import get_data
import math

text = get_data(8, 2023)
inp, data = text.split('\n\n')
lines = data.split('\n')

map = dict()
for line in lines:
    start, end = line.split('=')
    left, right = end.strip().split(',')
    map[start.strip()] = (left[1:], right[1:-1])

current = []    
for k in map.keys():
    if k[-1] == 'A':
        current.append(k)

C = len(current)
steps = 0
cache = []
p1 = 0
while len(cache) != C:
    to_pop = []
    for i in range(len(current)):
        current[i] = map[current[i]][0] if inp[steps%len(inp)] == 'L' else map[current[i]][1]

        if current[i][-1] == 'Z':
            if current[i] == 'ZZZ':
                p1 = steps+1
            cache.append(steps+1)
            to_pop.append(i)
    
    for i in to_pop:
        current.pop(i)
    steps += 1

print(p1)
print(math.lcm(*cache))
