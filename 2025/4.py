from util import *

data = get_data().split('\n')
g, R, C = getGrid(data)

p1=0
run=True
first = True
while first or run:
    if not first:
        run=False
    for i in range(R):
        for j in range(C):
            if g[i][j] != '@':
                continue

            c = 0
            for l in [-1,0,1]:
                for k in [-1,0,1]:
                    if (l==0 and k==0):
                        continue
                    if 0 <= i+l < C and 0 <= j+k < R and g[i+l][j+k] == '@':
                        c += 1

            if c < 4:
                run = True
                if not first:
                    g[i][j] = '.'
                p2+=1
                if first:
                    p1+=1
    first = False

pr(p1)
pr(p2)
