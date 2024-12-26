from util import *
data = get_data().split('\n\n')


locks = []
keys = []
for d in data:
    pins, R, C = getGrid(d.split('\n'))

    tmp = []
    for x in range(C):
        c = 0
        for y in range(R):
            if pins[y][x] == '#':
                c += 1
        tmp.append(c-1)
    
    if all(map(lambda a: a == '#',pins[0])):
        locks.append(tuple(tmp))
    else:
        keys.append(tuple(tmp))
    

for l in locks:
    for k in keys:
        ok = True
        for i in range(len(k)):
            if 5 < l[i]+k[i]:
                ok = False
                break
        if ok:
            p1 += 1

pr(p1)
