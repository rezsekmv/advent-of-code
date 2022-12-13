from my_input import lines
from copy import deepcopy
import util
import math
import json

ans = []
data = []

def rightOrder(left, right, i=0):
    if isinstance(left, int):
        if isinstance(right, int):
            if left == right:
                return 0
            if left < right:
                return 1
            if left > right:
                return -1
        if isinstance(right, list):
            return rightOrder([left], right)

    if isinstance(left, list):
        if isinstance(right, int):
            return rightOrder(left, [right])
        
        if isinstance(right, list):
            if len(left) == len(right) and len(left) == i:
                return 0
            elif len(right) <= i:
                return -1
            elif len(left) <= i:
                return 1
            else:
                res = rightOrder(left[i], right[i])
                if res == 1:
                    return 1
                elif res == -1:
                    return -1
                elif res == 0:
                    return rightOrder(left, right, i+1)
                else:
                    print('HIBA')
import ast
    
tmp = []
for line in lines:
    
    if line != '':
        data.append(ast.literal_eval(line))

data.append([[2]])
data.append([[6]])

for i in range(len(data)-1):
    for j in range(len(data)-i-1):
        if rightOrder(data[j], data[j+1]) == -1:
            tmp = data[j]
            data[j] = data[j+1]
            data[j+1] = tmp

data.sort(key=rightOrder)

ans = (data.index([[2]])+1) * (data.index([[6]])+1)

print(ans)