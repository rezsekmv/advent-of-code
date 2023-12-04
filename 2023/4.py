import sys
sys.path.append('../advent_of_code')
from input_data import get_data
import math
import util

text = get_data(4, 2023)
lines = text.split('\n')

score = []
times = [1]*len(lines)
for i, l in enumerate(lines):
    d = l.split(':')[1]
    d = d.strip().split('|')
    winning = util.getNumbers(d[0])
    myNums = util.getNumbers(d[1])
    score_times = len(util.getCommon(winning, myNums))
    
    score.append(int(math.pow(2, score_times-1)))

    for t in range(0, times[i]):
        for s in range(i+1, i+score_times+1):
            times[s] += 1


print(sum(score))
print(sum(times))

