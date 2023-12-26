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


def dfs(r: int, c: int, step: int, seen: set) -> int:
    if r == R-1 and c == C-2:
        return step
    print(r,c, step)
    if (r, c) in seen:
        return 0
    seen = deepcopy(seen)
    seen.add((r,c))

    cell = G[r][c]
    if cell == '.':
        T = []
        while True:
            neighbours = []
            for r_, c_ in [(1,0), (0,1), (-1,0), (0,-1)]:
                rr, cc = (r+r_, c+c_)
                if 0<rr<R and 0<cc<C and G[rr][cc] != '#' and (rr,cc) not in seen:
                    neighbours.append((rr, cc))

            n = len(neighbours)
            if n == 0:
                return 0
            elif n > 1:
                break            
            elif n == 1:
                r, c = neighbours[0]
                seen.add((r,c))
                step += 1
                if r == R-1 and c == C-2:
                    return step

        
        for rr, cc in neighbours:
            T.append(dfs(rr, cc, step+1, seen))
        return max(T)

    elif cell == '>':
        return dfs(r, c+1, step+1, seen)
    elif cell == '<':
        return dfs(r, c-1, step+1, seen)
    elif cell == 'v':
        return dfs(r+1, c, step+1, seen)
    elif cell == '^':
        return dfs(r-1, c, step+1, seen)
    

# print(dfs(0, 1, 0, set()))

for i, row in enumerate(G):
    for j, cell in enumerate(row):
        if cell == '>' or cell == '<' or cell == 'v' or cell == '^':
            G[i][j] = '.'

print(dfs(0, 1, 0, set()))