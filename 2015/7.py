from util import *

D = {}
EQS = ['OR', 'AND', 'NOT', 'LSHIFT', 'RSHIFT']
for line in get_data().split('\n'):
    eq, res = line.split(' -> ')
    a = []
    for e in eq.split(' '):
        if e in EQS:
            o = e
        else:
            a.append(e)

    if o == 'OR':
        res = a[0] or a[1]

pr(p1)