from util import *
data = get_data(ex=False).split()


m = defaultdict(int)
for i in data:
    m[i]+=1

for _ in range(75):
    print(_)
    tmp=defaultdict(int)
    for k,v in m.items():
        a=len(k)
        if int(k) == 0:
            tmp['1']+=v
        elif a%2==0:
            tmp[k[:a//2]]+=v
            tmp[str(int(k[a//2:]))]+=v
        else:
            tmp[str(int(k)*2024)]+=v
    m = tmp


pr(sum(m.values()))