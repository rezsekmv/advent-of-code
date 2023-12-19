import sys
sys.path.append('../advent_of_code')
from input_data import get_data

text = get_data(18, 2023)
lines = text.split('\n')

DIR = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}

DIR2 = {
    '3': (-1, 0),
    '0': (0, 1),
    '1': (1, 0),
    '2': (0, -1)
}

def polygonArea(X, Y):
    n = len(X)
    area = 0.0
 
    j = n - 1
    for i in range(0,n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i
    
    return int(abs(area / 2.0))
 
current = (0, 0)
side = 0
X = [0]
Y = [0]

X2 = [0]
Y2 = [0]
current2 = (0, 0)
side2 = 0
for i, l in enumerate(lines):    
    # part1
    dir, dist, color = l.split()
    dist = int(dist)

    next = (current[0] + DIR[dir][0]*dist, current[1] + DIR[dir][1]*dist)
    side += abs(next[0]-current[0]) + abs(next[1]-current[1])
    X.append(next[0])
    Y.append(next[1])
    current = next

    # part2
    dist2 = int(color[2:-2], 16)
    dir2 = color[-2]
    next2 = (current2[0] + DIR2[dir2][0]*dist2, current2[1] + DIR2[dir2][1]*dist2)
    side2 += abs(next2[0]-current2[0]) + abs(next2[1]-current2[1])
    X2.append(next2[0])
    Y2.append(next2[1])
    current2 = next2

side = side//2 + 1
area = polygonArea(X, Y)
print(area + side)

side2 = side2//2 + 1
area2 = polygonArea(X2, Y2)
print(area2+side2)