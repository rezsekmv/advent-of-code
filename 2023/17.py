import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from collections import defaultdict

text = get_data(16, 2023, True)
step = text.split(',')

boxes = defaultdict(list)
p2 = 0

def get_name(s):
    return s.split('=')[0].split('-')[0]

def hash(s):
    curr = 0
    for i in s:
        curr += ord(i)
        curr *= 17
        curr %= 256
    return curr

def find(val, box):
    for i, l in enumerate(box):
        if get_name(l) == val:
            return i, l 
    return -1, None

p1 = 0
curr = 0
for s in step:
    p1 += hash(s)

    name = get_name(s)
    idx = hash(name)
    i, v = find(name, boxes[idx])
    
    if '-' in s:
        if i >= 0:
            boxes[idx].remove(v)

    if '=' in s:
        if i >= 0:
            boxes[idx][i]
            boxes[idx][i] = s
        else:
            boxes[idx].append(s)

print(p1)

for k, v in boxes.items():
    for i, s in enumerate(v):
        p2 += (k+1) * (i+1) * int(s.split('=')[1])

print(p2)


