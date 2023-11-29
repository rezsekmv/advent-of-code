from my_input import lines
import util

sen = []
bac = []
dist = []

for line in lines:
    a = line.split()
    x = int(a[2][2:-1])
    y = int(a[3][2:-1])
    bx = int(a[8][2:-1])
    by = int(a[9][2:])

    sen.append((x,y))
    bac.append((bx,by))
    dist.append(abs(x-bx) + abs(y-by))
        
maxy = 4000000

for s, d in zip(sen, dist):
    for x0, dir in [(s[0]-d-1, (1,1)), (s[0]-d-1, (1,-1)), (s[0]+d+1 ,(-1,1)), (s[0]+d+1, (-1,-1))]:
        for i in range(d+1):
            x = x0 + dir[0]*i
            y = s[1] + dir[1]*i
            if 0 > x or x > maxy or 0 > y or y > maxy:
                continue 
            if not any(abs(x-si[0])+abs(y-si[1]) <= di for si, di in zip(sen, dist)):
                assert False, x*maxy + y
