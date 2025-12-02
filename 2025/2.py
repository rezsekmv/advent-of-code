from util import *

data = get_data().split(',')

p1 = 0
p2 = 0

for i,d in en(data):
    r1,r2 = d.split('-')
    arr = [x for x in range(int(r1), int(r2)+1)]


    for p in [False, True]:
        for j, a in en(arr):
            b=str(a)
        
            if not p:
                if len(b)%2 == 1:
                    continue
                
                h = len(b)//2
                if b[:h] == b[h:]:
                    p1 += a

            g = False
            for elem in range(1, len(b)):
                g2 = True
                for l in range(elem, len(b), elem):
                    if b[:elem] != b[l:l+elem]:
                        g2 = False
                        break
                if g2:
                    g = True
                    break
            
            if g:
                if p:
                    p2 += a

pr(p1)
pr(p2)
