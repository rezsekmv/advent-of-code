from util import *

lines = get_data().split('\n')

D = defaultdict(list)
L = set()
ALL = set()
for line in lines:
    n, w = line.split('=')
    f, t = n.split('to')
    
    w = int(w)
    f = f.strip()
    t = t.strip()

    L.add(f)
    ALL.add(f)
    ALL.add(t)
    D[f].append((t, w))
    D[t].append((f, w))

def calc(min=True):
    ans = math.inf if min else 0
    for f in L:
        Q = [(0, f, set([f]))]
        while Q:
            c, ff, seen = hq.heappop(Q)

            if len(seen) == len(ALL):
                cond = c < ans if min else c > ans
                if cond:
                    ans = c

            for t, w in D[ff]:
                if t in seen:
                    continue

                hq.heappush(Q, (c+w, t, set([*seen, t])))      
    return ans

pr(calc())
pr(calc(False))
  
    