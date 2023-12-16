import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from collections import deque

text = get_data(16, 2023)
lines = text.split('\n')

G = [[lines[i][j] for j in range(len(lines[0]))] for i in range(len(lines))]
R = len(G)
C = len(G[0])

DIR = {
    'UP': (-1, 0),
    'RIGHT': (0, 1),
    'DOWN': (1, 0),
    'LEFT': (0, -1)
}

def step(r, c, d):
    if G[r][c] == '.':
        return [d]
    
    if G[r][c] == '\\':
        if d == 'UP':
            return ['LEFT']
        if d == 'RIGHT':
            return ['DOWN']
        if d == 'DOWN':
            return ['RIGHT']
        if d == 'LEFT':
            return ['UP']
        
    if G[r][c] == '/':
        if d == 'UP':
            return ['RIGHT']
        if d == 'RIGHT':
            return ['UP']
        if d == 'DOWN':
            return ['LEFT']
        if d == 'LEFT':
            return ['DOWN']
        
    if G[r][c] == '-':
        if d == 'UP' or d == 'DOWN':
            return ['LEFT', 'RIGHT']
        if d == 'LEFT' or d == 'RIGHT':
            return [d]
        
    if G[r][c] == '|':
        if d == 'UP' or d == 'DOWN':
            return [d]
        if d == 'LEFT' or d == 'RIGHT':
            return ['UP', 'DOWN']
    
    assert False

right_starts = [(i, -1, 'RIGHT') for i in range(R)]
left_starts = [(i, C, 'LEFT') for i in range(R)]
down_starts = [(-1, i, 'DOWN') for i in range(C)]
up_starts = [(R, i, 'UP') for i in range(C)]
starts = right_starts + left_starts + down_starts + up_starts
ans = []
for start in starts:    
    buffer = deque([start])
    energized = set()
    cache = set()
    while len(buffer) > 0:
        r, c, d = buffer.popleft()
        rr = r+DIR[d][0]
        cc = c+DIR[d][1]
        if 0 <= rr < R and 0 <= cc < C:
            if (rr, cc, d) in cache:
                continue
            else:
                cache.add((rr, cc , d))
                
            energized.add((rr, cc))
            dirs = step(rr, cc, d)
            for di in dirs: 
                buffer.append((rr, cc, di))

    ans.append(len(energized))

print(ans[0])
print(max(ans))