from util import *

lines = get_data().split('\n')

G, R, C = getGrid(lines)

OPEN=[]
for y in range(R):
    for x in range(C):
        if G[y][x] == 'S':
            s = y,x

SEEN=set()
DP={}
def calc(r,c,d):
    global SEEN
    if (r,c) in DP:
        return DP[(r,c)]
    
    if not 0<=r+1<R:
        return d
    
    if G[r+1][c] == '^':
        SEEN.add((r+1,c))
        a = calc(r+1,c+1, d+1) + calc(r+1,c-1, d+1)
    if G[r+1][c] == '.':
        a = calc(r+1,c, 1)
    
    DP[(r,c)] = a
    return a

p2 = calc(s[0],s[1], 1)
pr(len(SEEN))
pr(p2)