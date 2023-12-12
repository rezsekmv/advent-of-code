import sys
sys.path.append('../advent_of_code')
from input_data import get_data
import util
import math
from collections import deque, defaultdict
import itertools
from copy import deepcopy

text = get_data(12, 2023, True)
lines = text.split('\n')

def check(s, a):
    res = []
    fin = True
    for c in s:
        if c == '#':
            if fin:
                res.append(1)
                fin = False
            else:
                res[-1] += 1
        if c == '.':
            fin = True

    return res == a
            
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def get_arrangement(springs, arrangement):
    qs = find(springs, '?')
    L = len(qs)
    springs = list(springs)
    good = []

    for perm in itertools.product(['.', '#'], repeat=L):
        perm = list(perm)
        for q, char in zip(qs, perm):
            springs[q] = char
        strSprings = "".join(springs)
        if check(strSprings, arrangement):
            good.append(strSprings)
    
    print(good)
    combP = list(itertools.product(range(len(good)), repeat=5))
    combQ = list(itertools.product(['.', '#'], repeat=4))
    count = 0
    print(combP)
    for c in combP:
        for q in combQ:
            tmp = ''
            for i in range(4):
                tmp += good[c[i]] + q[i]
            tmp += good[c[4]]
            if check(tmp, arrangement*5):
                count += 1

    print(count)
    return count
                

p1 = 0
for i, line in enumerate(lines):
    data, sep = line.split(' ')
    s = []
    for se in sep.split(','):
        s.append(int(se))
    p1 += get_arrangement(data, s)
    
print(p1)

# Sorba kell behelyettesítgetni a dolgokat, ha már rossz, nem nézzük tovább