from input_data import get_data

data = get_data().split()

vow='aeiou'
n = ['ab', 'cd', 'pq', 'xy']
p1=0
for d in data:
    c=0
    for v in vow:
        c+=d.count(v)
    
    p=''
    t=False
    for l in d:
        if l == p:
            t=True
            break
        p=l
    
    m=True
    for i in n:
        if i in d:
            m=False
            break
    
    if 3<=c and t and m:
        p1+=1
    
print(p1)

p2=0
for d in data:
    r1=False
    for i in range(len(d)-1):
        s = d[i]+d[i+1]
        if s in d[:i] or s in d[i+2:]:
            r1 = True
            break

    r2=False
    for i in range(len(d)-2):
        if d[i] == d[i+2]:
            r2=True
            break

    if r1 and r2:
        p2+=1
print(p2)