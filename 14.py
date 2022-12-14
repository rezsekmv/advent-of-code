FILENAME = 'input/' + '14' + '.in'
lines = []

with open(FILENAME) as f:
    lines = [l.rstrip() for l in f.readlines()]
    f.close()

import util
import math

mir = 0
mic = 0

rmax = 0 
for line in lines:
    rocks = line.split('->')
    for i in range(len(rocks)-1):
        r = int(rocks[i+1].strip().split(',')[1])
        if r > rmax:
            rmax = r
        
rows = rmax+1
cols = 600

grid = []
for r in range(rows):
    row = []
    for c in range(cols):
        row.append('.')
    grid.append(row)

for line in lines:
    rocks = line.split('->')
    for i in range(len(rocks)-1):
        c = int(rocks[i].strip().split(',')[0])
        r = int(rocks[i].strip().split(',')[1])
        cc = int(rocks[i+1].strip().split(',')[0])
        rr = int(rocks[i+1].strip().split(',')[1])

        for y in range(cc-c+1):
            if r >= rr:
                for x in range(r-rr+1):
                    grid[r-x][c+y] = '#'
            else:
                for x in range(rr-r+1):
                    grid[r+x][c+y] = '#'


start = 0, 500
grid[start[0]][start[1]] = '+'

def fall(pos):
    while True:
        # print(pos)
        if (pos[0] < mir or pos[1] < mic or pos[0] >= rows-1 or pos[1] >= cols-1):
            return None
        for d in [(1,0), (1,-1), (1,1)]:
            newPos = (pos[0] + d[0], pos[1] + d[1])
            if grid[newPos[0]][newPos[1]] == '.':
                break
        else:
            return pos
        pos = newPos


while True:
    newSand = fall(start)
    if newSand is None:
        break
    else:
        grid[newSand[0]][newSand[1]] = 'o'

for x in range(0, 80):
    for y in range(490,540):
        print(grid[x][y], end='')
    print()


count = 0
for r in grid:
    for c in r:
        if (c == 'o'):
            count += 1

print(count)