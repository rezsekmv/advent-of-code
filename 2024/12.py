from util import *
data = get_data(ex=True if len(sys.argv) > 1 else False).split()
data, R, C = getGrid(data)


T = []
K = []
DIRS=[(1,0), (0,-1), (-1,0), (0,1)]
SEEN=set()
REG=[]
for rr in range(R):
    for cc in range(C):
        if (cc,rr) in SEEN:
            continue

        Q=[(cc,rr, -1, -1)]
        t=k=0
        DD = {}

        while Q:
            x,y, px, py = Q.pop(0)
            if (x,y) in SEEN:
                continue
            SEEN.add((x,y))
            DD[(x,y)] = []

            r=data[y][x]

            t+=1
            n=0
            for xx, yy in [(0,1), (1,0), (-1,0), (0,-1)]:
                dx, dy = x+xx, y+yy
                if (0<=dx<C and 0<=dy<R) and data[dy][dx] == r:
                    if (dx,dy) not in SEEN:
                        Q.append((dx,dy, x,y))
                else:
                    n+=1
                    DD[(x,y)].append((xx,yy))
            k+=n
        T.append(t)
        K.append(k)
        REG.append(DD)

for i in range(len(T)):
    p1+=K[i]*T[i]

pr(p1)

DI = {
    (0,1): [(1,0), (-1,0)],
    (1,0): [(0,1), (0,-1)],
    (-1,0): [(0,1), (0,-1)],
    (0,-1): [(1,0), (-1,0)]
}
def sumd(d):
    a = 0
    for v in d.values():
        a+=len(v)
    return a

for j,r in en(REG):
    side = 0
    for k in list(r.keys()):
        x,y = k
        for i in range(len(r[k])):
            for xx, yy in DI[r[k][i]]:
                dx, dy = x+xx, y+yy
                while (0<=dx<C and 0<=dy<R) and data[dy][dx] == data[y][x]:
                    if r[k][i] in r[(dx,dy)]:
                        r[(dx,dy)].remove(r[k][i])
                    else:
                        break
                    dx, dy = dx+xx, dy+yy
    
    p2+=len(r)*sumd(r)

pr(p2)