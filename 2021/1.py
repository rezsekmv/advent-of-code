import sys
sys.path.append('../advent_of_code')
from input_data import get_data
import math
from collections import deque

data = get_data(1, 2021).split('\n')

inc = 0
prev = deque([math.inf, math.inf, math.inf])
for i in data:
    s = sum(prev)
    new = prev.copy()
    new.pop()
    new.appendleft(int(i))
    n = sum(new)
    if n > s:
        inc += 1
    prev.pop()
    prev.appendleft(int(i)) 

print(inc)