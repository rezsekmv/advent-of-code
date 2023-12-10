import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from collections import deque

text = get_data(10, 2023)
data = text.split('\n')
for i, d in enumerate(data):
    data[i] = list(d)

#find start coord and init start steps
start = [(0,0), 0]
for i, d in enumerate(data):
    try:
        start[0] = (i, d.index('S'))
    except:
        pass


DIR = {
    'S': set([(0, 1), (1, 0), (0, -1), (-1, 0)]),
    '-': set([(0, -1), (0, 1)]),
    '|': set([(-1, 0), (1, 0)]),
    'L': set([(-1, 0), (0, 1)]),
    'J': set([(-1, 0), (0, -1)]),
    '7': set([(0, -1), (1, 0)]),
    'F': set([(0, 1), (1, 0)]), 
    '.': set()
}

def check(pos, newPos):
    return (pos[0]-newPos[0], pos[1]-newPos[1]) in DIR[data[newPos[0]][newPos[1]]]

P = set(start[0])
maxSteps = 0
buffer = deque([start])
run = True
while buffer:
    pos, steps = buffer.popleft()
    for di in DIR[data[pos[0]][pos[1]]]:
        newPos = pos[0]+di[0], pos[1]+di[1]
        if check(pos, newPos):
            if newPos not in P:
                P.add(newPos)
                maxSteps = steps+1
                buffer.append((newPos, steps+1))

print(maxSteps)

# ====================== PART 2 =======================

# replace junk with .
for i, _ in enumerate(data):
    for j, _ in enumerate(data[i]):
        if (i, j) not in P:
            data[i][j] = '.'

# replace S with the correct pipe
startDirs = set()
for startRow, _ in enumerate(data):
    try:
        startCol = data[startRow].index('S')
        pos = (startRow, startCol)
        for di in DIR[data[pos[0]][pos[1]]]:
            newPos = pos[0]+di[0], pos[1]+di[1]
            if check(pos, newPos):
                startDirs.add(di)

        data[startRow][startCol] = (list(DIR.keys())[list(DIR.values()).index(startDirs)])
        break
    except:
        pass


inside = 0
# find inside cells
for i, row in enumerate(data):
    parity = 0
    l = False
    f = False
    for j, cell in enumerate(row):
        match cell:
            case '|':
                l = False
                f = False
                parity += 1

            case 'L':
                f = False
                l = True
                
            case 'F':
                l = False
                f = True

            case '7':
                if l:
                    l = False
                    f = False
                    parity += 1

            case 'J':
                if f:
                    l = False
                    f = False
                    parity += 1

            case '.':
                l = False
                f = False
                if parity%2 == 1:
                    data[i][j] = 'I'
                    inside += 1
    # print(i, "".join(row), inside)
print(inside)

