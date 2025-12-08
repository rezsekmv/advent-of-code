from util import *

lines = get_data().split('\n')
P = 10 if ex else 1000

C=[]
for l in lines:
    a,b,c=l.split(',')
    C.append((int(a), int(b), int(c)))
L=len(C)

def man(a, b):
    return math.sqrt(abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2 + abs(a[2]-b[2])**2)


CS=defaultdict(lambda: False)
for c1 in range(L):
    for c2 in range(c1+1, L):
        s = man(C[c1], C[c2])
        CS[(c1,c2)] = s


SORTED = dict(sorted(CS.items(), key=lambda item: item[1]))
def union(D):
    while True:
        ids=[]
        for c1 in range(len(D)):
            for c2 in range(c1+1, len(D)):
                if len(getCommon(list(D[c1]),list(D[c2]))) > 0:
                    ids.append((c1,c2))

        if len(ids) == 0:
            break

        for i in ids:
            D[i[0]] = D[i[0]].union(D[i[1]])
            del D[i[1]]
    return D
    
D=[]
keys = list(SORTED.keys())
for p in [True, False]:
    for i in range(P if p else len(SORTED)):
        a,b = keys[i]

        g=False
        for d in D:
            if a in d:
                d.add(b)
                g=True
            elif b in d:
                d.add(a)
                g=True
        
        if not g:
            D.append(set([a,b]))
        
        D = union(D)
        if len(D) == 1 and len(D[0]) == L:
            break
    
    if p:
        ANS = sorted(D, key = lambda l: -len(l))
        pr(len(ANS[0])*len(ANS[1])*len(ANS[2]))
    else:
        pr(C[a][0]*C[b][0])
