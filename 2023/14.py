import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from copy import deepcopy

text = get_data(14, 2023)
lines = text.split('\n')

R = len(lines)
C = len(lines[0])
G = [[lines[i][j] for j in range(len(lines[0]))] for i in range(len(lines))]

rocks = []
for r in range(R):
    for c in range(C):
        if G[r][c] == 'O':
            rocks.append((r,c))

for p2 in [False, True]:
    cache = []
    for cycle in range(1_000_000_000):
        if p2:
            if G in cache:
                break
            cache.append(deepcopy(G))
        for rr, cc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            moved = True
            while moved:
                moved = False
                for i, (r, c) in enumerate(rocks):
                    if 0 <= r+rr < R and 0 <= c+cc < C and G[r+rr][c+cc] == '.':
                        G[r][c] = '.'
                        G[r+rr][c+cc] = 'O'
                        rocks[i] = (r+rr, c+cc)
                        moved = True

            if not p2:
                break
        if not p2:
            break        
        

    if p2:
        idx = cache.index(G)
        cache = cache[idx:]
        G = cache[(1_000_000_000-cycle) % len(cache)]

    ans = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] == 'O':
                ans += R-r

    print(ans)      

