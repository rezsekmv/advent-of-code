import sys
sys.path.append('../advent_of_code')
from input_data import get_data
import util

text = get_data(6, 2023)
data = text.split('\n')

time = util.getNumbers(data[0])
dist = util.getNumbers(data[1])
time2 = [int(data[0].split(':')[1].strip().replace(' ', ''))]
dist2 = [int(data[1].split(':')[1].strip().replace(' ', ''))]

def calculate(time, dist):
    ans = 1
    for race in range(len(time)):
        mode = 0
        for hold in range(time[race]+1):
            curr = (time[race] - hold) * hold
            if dist[race] < curr:
                mode += 1
        ans *= mode
    return ans

print(calculate(time, dist))
print(calculate(time2, dist2))