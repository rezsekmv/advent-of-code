from util import *

EQS = ['OR', 'AND', 'NOT', 'LSHIFT', 'RSHIFT']
def inp(P1 = True):
    Q = []
    for line in get_data().split('\n'):
        eq, res = line.split(' -> ')
        a = []
        o = None
        for e in eq.split(' '):
            if e in EQS:
                o = e
            else:
                a.append(e)
        if not P1 and not o and res == 'b':
            continue
        Q.append((o, a, res))
    return Q

def calc(Q, D):
    while len(Q) > 0:
        o,a,res = Q.pop(0)

        try:
            x = int(D.get(a[0], a[0]))
            if len(a) > 1:
                y = int(D.get(a[1], a[1]))
        except:
            Q.append((o,a,res))
            continue

        if o is None:
            D[res] = x

        if o == 'OR':
            D[res] = x | y

        if o == 'AND':
            D[res] = x & y

        if o == 'NOT':
            D[res] = ~ x

        if o == 'LSHIFT':
            D[res] = x << y

        if o == 'RSHIFT':
            D[res] = x >> y

        D[res] %= 2**16

    return D

P1 = calc(inp(), {})
p1 = P1['a']
pr(p1)

P2 = calc(inp(False), {'b': p1})
pr(P2['a'])