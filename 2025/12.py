from util import *

lines = get_data().split('\n\n')

R = C = 3
P = []
Gs = []
for li in lines[:-1]:
    G, R, C = getGrid(li.split('\n')[1:])
    P.append(G)

for li in lines[-1].split('\n'):
    words = li.split()
    a,b = words[0].split('x')
    TMP = [(int(a), int(b.split(':')[0]))]
    tmp = []
    for w in words[1:]:
        tmp.append(int(w))
    TMP.append(tuple(tmp))
    Gs.append(TMP)

p1 = 0
for i,g in en(Gs):
    size,tiles = g
    R,C = size
    count = sum(tiles)

    a = R*C

    b = 0
    for i,t in en(tiles):
        c = 0
        for p in flatten(P[i]):
            if p == '#':
                c += 1 
        b+=c*t        

    if a > b:
        p1 += 1

pr(p1)



