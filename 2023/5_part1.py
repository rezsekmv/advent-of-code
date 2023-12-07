import sys
sys.path.append('../advent_of_code')
from input_data import get_data
import util
import math
from collections import defaultdict

text = get_data(5, 2023)
lines = text.split('\n\n')

dic = defaultdict(list)
seeds = util.getNumbers(lines[0].split(':')[1])
for l in lines[1:]:
    key, vtext = l.split(':')
    vtext = vtext.strip().split('\n')
    f, _, t = key.split()[0].split('-')
    for v in vtext:
        dic[f, t].append(util.getNumbers(v))


min = math.inf
for seed in seeds:
    for k, v in dic.items():
        for a in v: 
            if a[1] <= seed < a[1] + a[2]:
                seed += (a[0]-a[1])
                break    

    if seed < min:
        min = seed

print(min)