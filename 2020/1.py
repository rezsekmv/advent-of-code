import sys
sys.path.append('../advent-of-code')

from input_data import get_data
from collections import deque

data = get_data(1, 2020).split('\n')

for i in data:
    for j in data:
        for k in data:
            i = int(i)
            j = int(j)
            k = int(k)
            if i + j + k == 2020:
                print(i*j*k)

print('end')