import sys
sys.path.append('../advent-of-code')
from input_data import get_data

import copy

text = get_data(1, 2023)
data = text.split('\n')

def replaceData(a):
    b = a.replace('one', 'o1e')
    b = b.replace('two', 't2o')
    b = b.replace('three', 't3e')
    b = b.replace('four', 'f4r')
    b = b.replace('five', 'f5e')
    b = b.replace('six', 's6x')
    b = b.replace('seven', 's7n')
    b = b.replace('eight', 'e8t')
    b = b.replace('nine', 'n9e')
    return b

def genNumbers(nums):
    res = []
    for d in nums:
        num = ''
        for i in d:
            try:
                n = int(i)
                if num == '':
                    num += str(n)
            except ValueError:
                continue
        num += str(n)
        res.append(int(num))
    return res

data2 = copy.deepcopy(data)
for i, d in enumerate(data2):
    l = len(d)
    for j in range(len(d)):
        tmp = replaceData(data2[i][j:j+5])
        data2[i] = data2[i].replace(data2[i][j:j+5], tmp)
        if (l != len(tmp)):
            j = 0

print(sum(genNumbers(data)))
print(sum(genNumbers(data2)))