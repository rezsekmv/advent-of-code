from util import *
data = get_data(ex=False)

a=[]
id=0
file=True
for i in data:
    if file:
        for j in range(int(i)):
            a.append(str(id))
        id += 1
    else:
        for j in range(int(i)):
            a.append('.')

    file=not file

a1 = deepcopy(a)
l1=0
r1=len(a1)-1
while l1 != r1:
    if a1[l1] != '.':
        l1+=1
    elif a1[r1] == '.':
        r1-=1
    else:
        a1[l1], a1[r1] = a1[r1], a1[l1]

for i,v in en(a1):
    if v != '.':
        p1 += i*int(v)

pr(p1)


l=0
r=len(a)-1
while 0 < r:
    if a[r] != '.':
        y=0
        t=a[r]
        while a[r-y] == t:
            y+=1


        l=0
        while l < r:
            while a[l] != '.' :
                l+=1
            x=0
            while l+x <= r-y and a[l+x] == '.':
                x+=1
            # print(l,r, x,y, a[l], a[r], ''.join(a))
            if y <= x and l < r-y:
                for i in range(y):
                    a[r-i], a[l+i] = a[l+i], a[r-i]
                break
            else:
                l+=x
        
        r-=y
        
    else:
        r-=1

for i,v in en(a):
    if v != '.':
        p2 += i*int(v)

pr(p2)
