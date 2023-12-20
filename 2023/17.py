import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from collections import deque, defaultdict
import math

text = get_data(17, 2023, True)
lines = text.split('\n')

R = len(lines)
C = len(lines[0])
G = [[int(lines[i][j]) for j in range(C)] for i in range(R)]

class Node:
    def __init__(self, coords, dist, straight):
        self.crd = coords
        self.dist = dist
        self.straight = straight
    
    def __str__(self):
        return 'Node: {} {} {}'.format(self.crd, self.dist, self.straight)

    def __eq__(self, other):
        return self.crd == other.crd and self.dist == other.dist and self.straight == other.straight
    
    def __hash__(self) -> int:
        return hash((self.crd, self.dist, self.straight))

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dijkstra():
    dists = defaultdict(lambda: math.inf)
    visited = set()
    
    start = Node((0, 0), 0, -1)
    buffer = deque([start])
    while buffer:
        curr = buffer.popleft()
        # print(curr)
        # found the distance to bottom right
        # if curr.crd[0] == R-1 and curr.crd[1] == C-1:
        #     return curr.dist

        # if already visited => skip
        tmp = (curr.crd, curr.straight)
        if tmp in visited:
            continue
        visited.add(tmp)

        # go trough neighbours in graph
        for i, d in enumerate(DIRECTIONS):
            # don't go backwards or forward
            if curr.straight == (i-2)%len(DIRECTIONS) or curr.straight == i:
                continue

            tmp_dist = 0
            for distance in range(1, 4):    
                rr = curr.crd[0] + d[0] * distance
                cc = curr.crd[1] + d[1] * distance
                if 0<=rr<R and 0<=cc<C:
                    tmp_dist += G[rr][cc]
                    new_dist = curr.dist + tmp_dist
                    if dists[(rr, cc, i)] < new_dist:
                        continue
                    dists[(rr, cc, i)] = new_dist
                    buffer.append(Node((rr, cc), new_dist, i))

    for k,v in dists.items():
        print(k[:2], v)


print(dijkstra())
