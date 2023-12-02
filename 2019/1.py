import sys
sys.path.append('../advent-of-code')

from input_data import get_data
import os
import math
from collections import deque

data = get_data(1, 2019).split('\n')
res = []

def use(f):
    c = 0
    while f > 0: 
        f = math.floor(int(f)/3)-2
        c += f
    return c



for d in data:
    res.append(use(int(d)))


    
print(sum(res))
print('end')