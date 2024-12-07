from util import *
data = get_data().split('\n')

for i,d in en(data):
    res, ns = d.split(':')
    res = int(res)
    ns = getNumbers(ns)
    
    a=[ns[0]]
    b=[ns[0]]
    for j in range(1,len(ns)):
        tmp = []        
        for k in a:
            tmp.append(k+ns[j])
            tmp.append(k*ns[j])
        a=tmp
        tmp2 = []
        for k in b:
            tmp2.append(k+ns[j])
            tmp2.append(k*ns[j])
            tmp2.append(int(str(k) + str(ns[j])))
        b=tmp2

    if res in a:
        p1 += res
    if res in b:
        p2 += res

pr(p1)
pr(p2)