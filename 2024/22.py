from util import *

def prune(sec):
    return sec % 16777216

def mix(sec, n):
    return n ^ sec

S=[]
DS=[]
for sec in list(map(int, get_data().split('\n'))):
    prev = int(str(sec)[-1])
    P=deque([])
    D={}
    for i in range(2000):
        sec = prune(mix(sec, sec * 64))
        sec = prune(mix(sec, sec // 32))
        sec = prune(mix(sec, sec * 2048))

        ones = int(str(sec)[-1])

        if prev is not None:
            diff = ones-prev
            P.append(diff)
            if len(P) > 4: P.popleft()
            if len(P) == 4 and D.get(tuple(P), None) is None: 
                D[tuple(P)] = ones
        
        prev = ones
        
    S.append(sec)
    DS.append(D)
    
pr(sum(S))

SUM = defaultdict(int)
for d in DS:
    for k,v in d.items():
        SUM[k] += v

pr(max(SUM.values()))