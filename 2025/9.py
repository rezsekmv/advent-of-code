from util import *

lines = get_data().split('\n')

def area(a,b):
    return (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)

C = []
for j in range(len(lines)):
    a,b = lines[j].split(',')
    a = int(a)
    b = int(b)
    C.append((a,b))
L=len(C)

p1=0
for i in range(L):
    for j in range(i+1, L):
        a,b = C[i]
        c,d = C[j]

        e = area((a,b), (c,d))
        if (e > p1):
            p1 = e

print(p1)

def inside(a,b, z):
    d1 = a[0] - z[0]
    d2 = b[0] - z[0]

    dd1 = a[1] - z[1]
    dd2 = b[1] - z[1]

    c1 = d1 > 0 and d2 < 0
    c2 = dd1 > 0 and dd2 < 0
    b1 = d1 < 0 and d2 > 0
    b2 = dd1 < 0 and dd2 > 0

    if (c1 and c2) or (c1 and b2) or (b1 and c2) or (b1 and b2):
        return True

    return False

p2=0
for i in range(L):
    for j in range(i+1, L):
        a = C[i]
        b = C[j]
        A = area(a,b)

        ins = False
        for i2 in range(L):
            z1 = C[i2]
            if a == z1 or b == z1:
                continue
            if inside(a,b,z1):
                ins = True
                break
        
        M1 = max(C[248][1], C[249][1])
        M2 = min(C[248][1], C[249][1])
        magic = (( M2 >= a[1] and M2 >= b[1]) or ( M1 <= a[1] and M1 <= b[1]))

        if not ins and magic:
            if p2 <= A:
                p2 = A

print(f'magic numbers: {M1=} {M2=}')
print(p2)