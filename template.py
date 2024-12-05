import sys
import re
import heapq as hq
from collections import defaultdict, deque
from copy import deepcopy
import pyperclip as pc
sys.setrecursionlimit(10**6)
def pr(s):
    print(s)
    pc.copy(s)

from input_data import get_data

text = get_data(5, example=False)
lines = text.split('\n')
# data = [list(d) for d in lines]
# R = len(data)
# C = len(data[0])

# data = list(map(int, lines))

p1=0
p2=0



pr(p1)
pr(p2)
