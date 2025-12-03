from util import *

lines = get_data().split('\n')

data = [list(d) for d in lines]

A = []
for d in data:
    A.append([int(e) for e in d])

p1 = 0
p2 = 0

def calc(d, to):
    maxi = -1
    tmp = ''
    ans = 0
    for k in range(1, to+1):
        m = max(d) if to-k == 0 else max(d[:-(to-k)])
            
        maxi = d.index(m)
        d = d[maxi+1:]
        tmp += str(m)

    ans += int(tmp)
    return ans


P1 = 2
P2 = 12
for i,d in en(A):
    p1 += calc(d, P1)
    p2 += calc(d, P2)

pr(p1)
pr(p2)
