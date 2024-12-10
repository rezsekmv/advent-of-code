from util import *
data = get_data(ex=False).split('\n')
data, R, C = getGrid(data)

starts = []
for r in range(R):
    for c in range(C):
        if data[r][c] == '.':
            data[r][c] = -2
        else:
            data[r][c] = int(data[r][c])
        if data[r][c] == 0:
            starts.append((r,c))

p1=[0]*len(starts)
p2=[0]*len(starts)
for p in [True, False]:
    for i, start in en(starts):
        OPEN = [start]
        CLOSED = set()

        while OPEN:
            r, c = OPEN.pop(0)
            CLOSED.add((r,c))
            if data[r][c] == 9:
                if p:
                    p1[i]+=1
                else:
                    p2[i]+=1
            
            for rr, cc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr, nc = r+rr, c+cc
                
                cond = nr < 0 or R <= nr or nc < 0 or R <= nc or data[nr][nc] - data[r][c] != 1
                if p:
                    if cond or (nr,nc) in CLOSED or (nr,nc) in OPEN:
                        continue
                else:
                    if cond: 
                        continue
                
                OPEN.append((nr, nc))

pr(sum(p1))
pr(sum(p2))
