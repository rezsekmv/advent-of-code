from util import *

L1 = defaultdict(bool)
L2 = defaultdict(int)

for line in get_data().split('\n'):
    o1, o2 = line.split()[:2]
    s1, s2, e1, e2 = getNumbers(line)

    for r in range(s1, e1+1):
        for c in range(s2, e2+1):
            if o1 == 'toggle':
                L1[(r,c)] = not L1[(r,c)]
                L2[(r,c)] += 2

            elif o1 == 'turn' and o2 == 'off':
                L1[(r,c)] = False
                L2[(r,c)] = L2[(r,c)]-1 if L2[(r,c)]-1>=0 else 0

            elif o1 == 'turn' and o2 == 'on':
                L1[(r,c)] = True
                L2[(r,c)] += 1

pr(list(L1.values()).count(True))
pr(sum(L2.values()))