import sys
import re
import heapq as hq
from collections import defaultdict, deque, OrderedDict
from copy import deepcopy
dc=deepcopy
import pyperclip as pc
import math
import time
import functools
from sympy.solvers import solve
from sympy.abc import x, y, z
sys.setrecursionlimit(10**6)
from input_data import get_data
en =enumerate
p1=p2=0
DIRS = [(1,0), (0,1), (-1,0), (0,-1)]
ex=len(sys.argv) > 1

def pr(s):
    print(s)
    pc.copy(s)

def getCommon(list1, list2):
    return list(set(list1).intersection(list2))

def getNumbers(str, negative=True):
    if negative:
        return [int(num) for num in re.findall(r'-?\d+', str)]
    else:
        return [int(num) for num in re.findall(r'\d+', str)]

def getRegexp(str, regexp='^[a-zA-Z]+$'):
    return re.findall(regexp, str)

def getFirstRegexp(str, regexp='^[a-zA-Z]+$'):
    res = re.findall(regexp, str)
    if len(res) > 0:
        return res[0]
    else:
        return ''

def getGrid(lines):
    data = [list(d) for d in lines]
    R = len(data)
    C = len(data[0])
    return data, R, C

def flatten(xss):
    if not isinstance(xss[0], list):
        return xss
    return [x for xs in xss for x in xs]

def isInt(num):
    return int(num) == num

# def astar(x, y, target):    
#     start = (dist, x, y)
#     OPEN = [start]
#     CLOSED = set()

#     while OPEN:
#         dist, x, y = heapq.heappop(OPEN)
#         CLOSED.add((x,y))

#         if (x, y) == target:
#             return True
        
#         for xx, yy in [(1,0), (0,1), (-1,0), (0,-1)]:
#             nx, ny = x+xx, y+yy
#             if util.out_of_bounds((nx,ny), board_size) or (nx,ny) in obstackles or (nx, ny) in CLOSED:
#                 continue

#             g = details[x][y].g + 1.0
#             h = util.calc_manhattan((nx, ny), target)
#             f = g + h
#             if details[nx][ny].f != 99999 or details[nx][ny].f < f:
#                 continue
            
#             heapq.heappush(OPEN, (f, nx, ny))