import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from collections import deque, defaultdict
import math

text = get_data(17, 2023)
lines = text.split('\n')

R = len(lines)
C = len(lines[0])
G = [[int(lines[i][j]) for j in range(C)] for i in range(R)]

class Node:
    def __init__(self, coords, dist, wrong_dir):
        self.crd = coords
        self.dist = dist
        self.wrong_dir = wrong_dir
    
    def __str__(self):
        return 'Node: {} {} {}'.format(self.crd, self.dist, self.wrong_dir)

    def __eq__(self, other):
        return self.crd == other.crd and self.dist == other.dist and self.wrong_dir == other.wrong_dir
    
    def __hash__(self) -> int:
        return hash((self.crd, self.dist, self.wrong_dir))

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dijkstra():
    dists = {}
    visited = set()
    
    start = Node((0, 0), 0, -1)
    buffer = deque([start])
    while buffer:
        curr = buffer.popleft()
        
        # found the distance to bottom right
        if curr.crd[0] == R-1 and curr.crd[1] == C-1:
            return curr.dist

        # if already visited => skip
        tmp = Node(curr.crd, None, curr.wrong_dir)
        if tmp in visited:
            continue
        visited.add(tmp)

        # go trough neighbours in graph
        for i, d in enumerate(DIRECTIONS):
            # don't go backwards
            if curr.dir == (i-2)%len(DIRECTIONS):
                continue
            
            # if go straight => 
            if curr.dir == i:
                pass
            
            for distance in range(1, 4):
                tmp_dist = 0
                rr = curr.crd[0] + d[0] * distance
                cc = curr.crd[1] + d[1] * distance
                if 0<=rr<R and 0<=cc<C:
                    tmp_dist += G[rr][cc]
                    new_dist = curr.dist + tmp_dist
                    Node((rr, cc), d)
                    if dists.get() <= new_dist:
                        continue
                    dists[Node((rr, cc), d)] = new_dist
                    buffer.append(Node((rr, cc), new_dist, d))

print(dijkstra())

# for i, (k,v) in enumerate(graph.items()):
#     print(k)
#     for g in v:
#         print('\t', g)
#     if i == 30:
#         break
# print(len(graph))