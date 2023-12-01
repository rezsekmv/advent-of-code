import sys
sys.path.append('../advent_of_code')
from input_data import get_data
import math
from collections import deque

text = get_data(1, 2018)
data = text.split('\n')

freq = 0
past = [0]
same = True
while same:
    for d in data:
        freq += int(d)
        if freq in past:
            same = False
            print(freq)
            break;
        past.append(freq)
    
print(len(past))
print(len(set(past)))
print(freq)