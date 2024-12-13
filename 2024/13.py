from util import *
data = get_data().split('\n\n')

M=[]
for line in data:
    t=[]
    for d in line.split('\n'):
        t.append(getNumbers(d))
    M.append(t)

P1=[]
P2=[]

for m in M:
    ax = m[0][0]
    ay = m[0][1]
    bx = m[1][0]
    by = m[1][1]
    mx = m[2][0]
    my = m[2][1]

    eqs = [ax*x + bx*y - mx, ay*x + by*y - my] 
    for r in solve(eqs, x, y, dict=True):
        if int(r[x]) == r[x] and int(r[y]) == r[y]:
            P1.append(int(r[x]*3+r[y]))

    eqs = [ax*x + bx*y - mx-10000000000000, ay*x + by*y - my-10000000000000] 
    for r in solve(eqs, x, y, dict=True):
        if int(r[x]) == r[x] and int(r[y]) == r[y]:
            P2.append(int(r[x]*3+r[y]))

pr(sum(P1))
pr(sum(P2))

