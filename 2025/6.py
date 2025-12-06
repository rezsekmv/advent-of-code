from util import *

lines  = get_data().split('\n')

def calc(D):
    p=0
    for d in D:
        if d[-1] == '+':
            t = int(d[0])
            for j in d[1:-1]:
                t+=int(j)
            p +=t
        if d[-1] == '*':
            t = int(d[0])
            for j in d[1:-1]:
                t*=int(j)
            p +=t
    return p


A = [[]]*len(lines[0].split())
D = [[]]*len(lines[0].split())
data, R, C = getGrid(lines)


for l in lines:
    t = l.split()
    for i in range(len(t)):
        A[i] = [*A[i], t[i]]

i=0
for c in range(C):
    n = ''
    for r in range(R-1):
        n += data[r][c]
    
    if n.strip() == '':
        sign = lines[R-1].split()[i]        
        D[i] = [*D[i], sign.strip()]
        i+=1
    else:
        D[i] = [*D[i],n.strip()]

sign = lines[R-1].split()[i]        
D[i] = [*D[i], sign.strip()]

pr(calc(A))
pr(calc(D))

