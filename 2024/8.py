from util import *
data = get_data(ex=False).split('\n')
data, R, C = getGrid(data)

def add(a,b):
    return a[0]+b[0], a[1]+b[1]

def mul(a,k):
    return a[0]*k, a[1]*k

def bounds(a):
    return 0<= a[0] < C and 0<= a[1] < R

D = defaultdict(list)
for y in range(R):
    for x in range(C):
        c = data[y][x]
        if c != '.' and c != '#':
            
            D[c].append((x,y))
S=set()
S2=set()
for k,v in D.items():
    S2.update(v)
    for i in range(len(v)-1):
        for j in range(i+1, len(v)):
            a1, a2 = v[i], v[j]
            diff = a1[0]-a2[0], a1[1]-a2[1]
            diff2 = a2[0]-a1[0], a2[1]-a1[1]
    
            # p1
            b1=add(a1, diff)
            b2=add(a2, diff2)
            if bounds(b1):
                S.add(b1)
            if bounds(b2):
                S.add(b2)
    
            # p2
            for k in range(max(C,R)):
                b1=add(a1, mul(diff,k))
                b2=add(a2, mul(diff2,k))
                if bounds(b1):
                    S2.add(b1)
                if bounds(b2):
                    S2.add(b2)
        
def debug(): 
    for y in range(R):
        for x in range(C):
            if (x,y) in S2:
                print('#', end='')
            elif data[y][x] == '#': 
                print('.', end='')
            else:
                print(data[y][x],end='')
        print()


pr(len(S))
pr(len(S2))