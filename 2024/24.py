from util import *

gates, wires = get_data().split('\n\n')

G={}
for g in gates.split('\n'):
    k,v = g.split(': ')
    G[k] = int(v)

W=[]
WW = {}
for w in wires.split('\n'):
    op, r = w.split(' -> ')
    a, o, b = op.split(' ')
    if a not in G:
        G[a] = -1
    if b not in G:
        G[b] = -1
    W.append((a,o,b,r, True))
    WW[r] = (a,o,b)

def calc(W, G):
    W=dc(W)
    G=dc(G)
    first=True
    while first or -1 in G.values() or any(list(map(lambda a: a[4], W))):
        for i, (a,o,b,r,do) in en(W):
            if not do or G[a] == -1 or G[b] == -1:
                continue

            if o == 'AND':
                G[r] = G[a] and G[b]
                W[i] = (a,o,b,r,False)
            if o == 'OR':
                G[r] = G[a] or G[b]
                W[i] = (a,o,b,r,False)
            if o == 'XOR':
                G[r] = G[a] ^ G[b]
                W[i] = (a,o,b,r,False)
        first = False
    return G

def get_nums(RES):
    X = {}
    Y = {}
    Z = {}
    for k,v in RES.items():
        if k.startswith('x'):
            X[int(k[1:])] = v
        if k.startswith('y'):
            Y[int(k[1:])] = v
        if k.startswith('z'):
            Z[int(k[1:])] = v
    x=''
    y=''
    z=''
    for k in reversed(sorted(X.keys())):
        x += str(X[k])
    for k in reversed(sorted(Y.keys())):
        y += str(Y[k])
    for k in reversed(sorted(Z.keys())):
        z += str(Z[k])

    return x, y, z

RES = calc(W,G)
_,_,z = get_nums(RES)
pr(int(z,2))

def findR(x,y,op):
    for a,o,b,r, _ in W:
        if set((x, y)) == set((a,b)) and o == op:
            return r
    raise NameError

def findXY(res,op):
    for a,o,b,r, _ in W:
        if o == op and res == r:
            return x,y
    assert False

def swap(k1, k2):
    S = set()
    for i, (a,o,b,r,s) in en(W):
        if k1 == r and i not in S:
            W[i] = (a,o,b,k2,s)
            S.add(i)
        if k2 == r and i not in S:
            W[i] = (a,o,b,k1,s)
            S.add(i)
    if len(S) < 2:
        assert False

SWAP=[]
prevrem=findR('x00', 'y00', 'AND')
i=1
while i < 45:
    xk = f"x{i:02}"
    yk = f"y{i:02}"
    zk = f"z{i:02}"
    
    tmpres = findR(xk, yk, 'XOR')
    rem = findR(xk, yk, 'AND')

    # print(f'{i=} {prevrem=} {tmpres=} {rem=}', end=' ')
    try:
        z = findR(tmpres, prevrem, 'XOR')
        # print(f'{z=} {zk=}', end=' ')
    
        if z != zk:
            swap(z, zk)
            SWAP.extend((zk, z))
            # print(f'{nextrem=}', end='\n\n')
            continue
    except:
        swap(tmpres, rem)
        SWAP.extend((tmpres, rem))
        continue


    nextrem = findR(tmpres, prevrem, 'AND')
    # print(f'{nextrem=}', end='\n\n')
    prevrem = findR(nextrem, rem, 'OR')
    i+=1


SWAP.sort()
pr(','.join(SWAP))

