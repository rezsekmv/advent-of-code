import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from copy import deepcopy
import sys
sys.setrecursionlimit(10000)

text = get_data(23, 2023)
lines = text.split('\n')
R = len(lines)
C = len(lines[0])
G = [[lines[i][j] for j in range(C)] for i in range(R)]
F = {}
print('Calculating... (approx. 2-3 minutes)')
def dfs(r: int, c: int, step: int, seen: set) -> int:
    if r == R-1 and c == C-2:
        return step

    seen = deepcopy(seen)
    if (r,c) in seen:
        return 0
    seen.add((r,c))


    cell = G[r][c]
    if cell == '.':
        pahts = []
        for r_, c_ in [(1,0), (0,1), (-1,0), (0,-1)]:
            rr, cc = (r+r_, c+c_)
            if 0<=rr<R and 0<=cc<C and G[rr][cc] != '#' and (rr,cc) not in seen:        
                pahts.append(dfs(rr, cc, step+1, seen)) 
        return max(pahts)
    elif cell == '>':
       return dfs(r, c+1, step+1, seen)
    elif cell == '<':
       return dfs(r, c-1, step+1, seen)
    elif cell == 'v':
       return dfs(r+1, c, step+1, seen)
    elif cell == '^':
       return dfs(r-1, c, step+1, seen)
    

print(dfs(0, 1, 0, set()))

# ========= PART2 ==========

# find graph points
for r, row in enumerate(G):
    for c, cell in enumerate(row):
        if cell != '#':
            n = 0
            for r_, c_ in [(1,0), (0,1), (-1,0), (0,-1)]:
                rr, cc = (r+r_, c+c_)
                if 0<=rr<R and 0<=cc<C and G[rr][cc] != '#':
                    n+=1
            if n == 1 or n > 2:
                F[(r,c)] = set()

# build up the graph with weights
for r, c in F.keys():
    lr, lc = r, c
    for x_, y_ in [(1,0), (0,1), (-1,0), (0,-1)]:
        if 0<=lr+x_<R and 0<=lc+y_<C and G[lr+x_][lc+y_] != '#':
            weight = 1
            seen = set([(lr, lc), (lr+x_, lc+y_)])
            found = False
            rr, cc = (lr+x_, lc+y_)
            while True:
                for r_, c_ in [(1,0), (0,1), (-1,0), (0,-1)]: 
                    rrr, ccc = (rr+r_, cc+c_)
                    if 0<=rrr<R and 0<=ccc<C and G[rrr][ccc] != '#' and (rrr, ccc) not in seen:
                        weight += 1
                        if (rrr, ccc) in F.keys():
                            F[(rrr,ccc)].add((r,c, weight))
                            F[(r,c)].add((rrr,ccc, weight))
                            found = True
                            break
                        seen.add((rrr, ccc))
                        rr, cc = (rrr, ccc)

                if found:
                    break

seen =set()
# dfs for built graph
def dfs2(r: int, c: int, weight: int) -> int:
    if r == R-1 and c == C-2:
        return weight

    if (r,c) in seen:
        return 0
    seen.add((r,c))

    paths = []
    for rr, cc, w in F[(r,c)]:
        paths.append(dfs2(rr, cc, weight+w))

    seen.remove((r,c))
    return max(paths)

# call dfs for part2
print(dfs2(0, 1, 0))
