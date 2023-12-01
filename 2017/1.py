import sys
sys.path.append('../advent_of_code')
from input_data import get_data
import math
from collections import deque
from submit import submit

text = get_data(1, 2017)
data = text

s = 0
prev = data[-1]
for b in data: 
    if b == prev:
        s += int(b)
    prev = b

print(s)
    