import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from copy import deepcopy

text = get_data(21, 2023, True)
lines = text.split('\n')

R = len(lines)
C = len(lines[0])
G = [[lines[i][j] for j in range(C)] for i in range(R)]
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start = None
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            G[r][c] = '.'
            start = (r,c)

def bfs(start, steps):
    can_be = set([start])
    for i in range(steps):
        next = set()
        while can_be:
            curr = can_be.pop()
            r = curr[0]
            c = curr[1]
            for rd, cd in DIRS:
                rr = r+rd
                cc = c+cd
                if G[rr%R][cc%C] == '.':
                    next.add((rr,cc))
        can_be = deepcopy(next)
        
    return can_be



for i in range(101):
    print(len(bfs(start, i)))