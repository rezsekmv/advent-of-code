import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from collections import deque
import math

text = get_data(17, 2023, True)
lines = text.split('\n')

R = len(lines)
C = len(lines[0])
G = [[int(lines[i][j]) for j in range(C)] for i in range(R)]
class Node:
    def __init__(self, coords, direction, distance, straight):
        self.crd = coords
        self.dir = direction
        self.dist = distance
        self.str = straight
    
    def __str__(self):
        return '{} {} {} {}'.format(self.coords, self.direction, self.distance, self.straight)

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
distances = [[(math.inf, 0) for j in range(C)] for i in range(R)]

unvisited = [[[(i, j, k) for k in range(4)] for j in range(C)] for i in range(R)]

buffer = deque([Node((0,0), 2, 0, 0)])
while len(buffer) > 0:
    node = buffer.popleft()

    for d in range(node.dir-1, node.dir+2):
        d %= len(DIRECTIONS)
        r = node.crd[0]+DIRECTIONS[d][0]
        c = node.crd[1]+DIRECTIONS[d][1]
        straight = node.str+1 if d == node.dir else 1

        if straight > 3:
            continue
        
        if 0 <= r < R and 0 <= c < C:
            if distances[r][c][0] < node.dist:
                continue

            distances[r][c] = (node.dist+G[r][c], straight)
            buffer.append(Node((r,c), d, node.dist+G[r][c], straight))
            
print(distances[R-1][C-1])
