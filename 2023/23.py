import sys
sys.path.append('../advent_of_code')
from input_data import get_data

text = get_data(23, 2023, True)
lines = text.split('\n')
R = len(lines)
C = len(lines[0])
G = [[lines[i][j] for j in range(C)] for i in range(R)]


def dfs(r: int, c: int, step: int, seen: set) -> int:
    if r == R-1 and c == C-2:
        return step+1
    
    if (r, c) in seen:
        return 0
    seen.add((r,c))

    cell = G[r][c]
    if cell == '.':                    
        T = []
        for r_, c_ in [(1,0), (0,1), (-1,0), (0,-1)]:
            rr, cc = (r+r_, c+c_)
            if 0<rr<R and 0<cc<C and G[rr][cc] != '#':
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
        
print(dfs(0, 1, 0, set()))