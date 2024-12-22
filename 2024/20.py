from util import *

data = get_data().split('\n')

data, R, C = getGrid(data)

for y in range(R):
    for x in range(C):
        if data[y][x] == 'S':
            start = (x,y)
        if data[y][x] == 'E':
            target = (x,y)

def shorest(s):
    CS={}
    OPEN = deque([(0, s[0], s[1], True)])
    SEEN = set()
    while OPEN:
        c, x, y, w = OPEN.popleft()
        
        if CS.get((x,y), math.inf) > c:
            CS[(x,y)] = c

        if (x, y, w) in SEEN:
            continue
        SEEN.add((x,y,w))

        if (x, y) == target:
            return CS
            
        for nd in DIRS:
            nx, ny = x+nd[0], y+nd[1]
            
            if not (0<=nx<C and 0<=ny<R):
                continue
            
            nw = w
            if data[ny][nx] == '#':
                if w:
                    continue
                else:
                    nw = True

            OPEN.append((c+1, nx, ny, nw))
    assert False

def find_cheats(CS, better_then, limit):
    D=defaultdict(set)
    for k,v in CS.items():
        OPEN = deque([(v, k[0], k[1])])
        SEEN = set()
        while OPEN:
            c, x, y = OPEN.popleft()

            key = (k, x, y)
            if key in SEEN: continue
            SEEN.add(key)

            if (x,y) in CS and (x,y) != k:
                diff = CS[(x,y)]-c                
                if better_then <= diff:
                    D[diff].add((k, (x,y)))
                
            for nd in DIRS:
                nx, ny = x+nd[0], y+nd[1]
                
                if not (0<=nx<C and 0<=ny<R) or limit <= c-v:
                    continue
                
                OPEN.append((c+1, nx, ny))
    return OrderedDict(sorted(D.items()))

CS = shorest(start)

P1 = find_cheats(CS, 1 if ex else 100, 2)
for k,v in P1.items():
    # print(f'{k}: {len(v)}')
    p1+=len(v)
pr(p1)
if ex: assert p1 == 44

P2 = find_cheats(CS, 50 if ex else 100, 20)
for k,v in P2.items():
    # print(f'{k}: {len(v)}')
    p2+=len(v)
pr(p2)
if ex: assert p2 == 285
