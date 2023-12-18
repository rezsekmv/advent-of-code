import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from collections import deque
import math

text = get_data(18, 2023, True)
lines = text.split('\n')

DIR = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}

DIR2 = {
    '3': (-1, 0),
    '0': (0, 1),
    '1': (1, 0),
    '2': (0, -1)
}

digged = set()
current = (0, 0)
for i, l in enumerate(lines):
    print(i)
    
    dir, dist, color = l.split()
    dist = int(color[2:-2], 16)
    print(dist)
    dir = color[-2]

    next = (current[0] + DIR2[dir][0]*dist, current[1] + DIR2[dir][1]*dist)
    digged.add((current, next))
    current = next

count = 0
buffer = deque([(1, 1)])
while len(buffer) > 0:
    r, c = buffer.popleft()
    for (rr, cc) in DIR.values():
        next = (r+rr, c+cc)
        if next not in digged:
            digged.add(next)
            buffer.append(next)


print(len(digged))