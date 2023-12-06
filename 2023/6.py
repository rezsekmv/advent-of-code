import sys
sys.path.append('../advent_of_code')
from input_data import get_data
import util
import math
from collections import deque, defaultdict

text = get_data(6, 2023)
data = text.split('\n')

time = util.getNumbers(data[0])
dist = util.getNumbers(data[1])

p1 = 1
for race in range(len(time)):
    mode = 0
    for hold in range(time[race]+1):
        curr = (time[race] - hold) * hold
        if dist[race] < curr:
            mode += 1
    p1 *= mode
print(p1)


time2 = int(data[0].split(':')[1].strip().replace(' ', ''))
dist2 = int(data[1].split(':')[1].strip().replace(' ', ''))

p2 = 0
for hold in range(time2+1):
    curr = (time2 - hold) * hold
    if dist2 < curr:
        p2 += 1
print(p2)