import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from copy import deepcopy
from collections import deque
import sys
sys.setrecursionlimit(10000)

text = get_data(23, 2023, True)
lines = text.split('\n')
R = len(lines)
C = len(lines[0])
G = [[lines[i][j] for j in range(C)] for i in range(R)]

class Node:
    def __init__(self, weight):
        self.weight = weight
        self.neighbours = []


def dfs(r: int, c: int, step: int, seen: set) -> int:

    seen = deepcopy(seen)
    pahts = []
    while True:
        neighbours = []
        for r_, c_ in [(1,0), (0,1), (-1,0), (0,-1)]:
            rr, cc = (r+r_, c+c_)
            if 0<rr<R and 0<cc<C and G[rr][cc] != '#' and (rr,cc) not in seen:
                neighbours.append((rr, cc))

        neighbour_count = len(neighbours)
        # if no neighbour => dead end
        if neighbour_count == 0:
            return 0
        # if one neighbour => handle outside loop
        elif neighbour_count > 1:
            break            
        # if one neighbours => check that neighbour
        elif neighbour_count == 1:
            r, c = neighbours[0]
            seen.add((r,c))
            step += 1
            if r == R-1 and c == C-2:
                return step

    # handle multiple neighbours
    for rr, cc in neighbours:
        seen.add((rr,cc))
        pahts.append(dfs(rr, cc, step+1, seen)) 
    return max(pahts)

NS = [[[]]*C]*R
for r, row in enumerate(G):
    NS.append([])
    for c, cell in enumerate(row):
        if cell != '#':
            for r_, c_ in [(1,0), (0,1), (-1,0), (0,-1)]:
                rr, cc = (r+r_, c+c_)
                if 0<=rr<R and 0<=cc<C and G[rr][cc] != '#':
                    NS[r][c].append((rr, cc))

start = Node(0)
curr = start
Q = deque([(0,1,0)])
SEEN = set()
N = [start]
while Q:
    r, c, step = Q.popleft()
    if (r,c) in SEEN:
        continue
    SEEN.add((r,c))
    neighbours = NS[r][c]
    for rr, cc in neighbours:        
        Q.append((rr, cc, step+1))
        if 2 < len(neighbours):
            node = Node(step)
            curr.neighbours.append(node)
            node.neighbours.append(curr)
            curr = node
            N.append(node)  


for n in N:
    print(n.neighbours)



