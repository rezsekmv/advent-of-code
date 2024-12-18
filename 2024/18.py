from util import *
data = []
for line in get_data().split('\n'):
    x,y = line.split(',')
    data.append((int(x), int(y)))

S=0,0
E=70,70
b=1024
while True:
    OPEN = deque([(0, S[0], S[1])])
    SEEN = set()
    found=False
    while OPEN:
        c, x, y = OPEN.popleft()
        if (x, y) in SEEN:
            continue
        SEEN.add((x,y))

        if (x, y) == E:
            found=True
            if b == 1024:
                pr(c)
            break
        
        for nd in DIRS:
            nx, ny = x+nd[0], y+nd[1]
            
            if not (0<=nx<=E[0] and 0<=ny<=E[1]) or (nx, ny) in data[:b]:
                continue

            OPEN.append((c+1, nx, ny))

    if not found:
        b-=1
        break
    b+=1

pr(f'{data[b][0]},{data[b][1]}')