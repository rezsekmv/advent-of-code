import sys
sys.path.append('../advent_of_code')
from input_data import get_data
import util
from collections import deque

text = get_data(9, 2023)
lines = text.split('\n')
data = []

for l in lines:
    data.append(deque(util.getNumbers(l)))

def calculateNextLine(line):
    nextLine = deque()
    for i in range(len(line)-1):
        nextLine.append(line[i+1] - line[i])
    return nextLine
    
prevValues = []
nextValues = []
forecasts = []
for i, d in enumerate(data):
    forecasts.append([d])
    while True:
        forecasts[i].append(calculateNextLine(forecasts[i][-1]))
        if all(f == 0 for f in forecasts[i][-1]):
            break

for forecast in forecasts:
    for i in range(len(forecast)-1, 0-1, -1):
        if i == len(forecast)-1:
            forecast[i].append(0)
            forecast[i].appendleft(0)
        else:
            forecast[i].append(forecast[i][-1] + forecast[i+1][-1])
            forecast[i].appendleft(forecast[i][0] - forecast[i+1][0])
            if i == 0:
                nextValues.append(forecast[i][-1])
                prevValues.append(forecast[i][0])


print(sum(nextValues))
print(sum(prevValues))
