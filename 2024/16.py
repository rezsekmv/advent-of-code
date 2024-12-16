from util import *
lines = get_data().split('\n')
data, R, C = getGrid(lines)

for y in range(R):
    for x in range(C):
        if data[y][x] == 'S':
            s = (x,y)
        if data[y][x] == 'E':
            target = (x,y)

def draw(TILES):    
    for y in range(R):
        for x in range(C):
            if (x,y) in TILES:
                print('O',end='')
            elif data[y][x] == '.':
                print(' ', end='')
            else:
                print(data[y][x], end='')
        print()


start = (0, s[0], s[1], (1,0))
OPEN = [start]
CLOSED = set()
T=defaultdict(set)
TC=defaultdict(lambda: math.inf)
while OPEN:
    c, x, y, d = hq.heappop(OPEN)
    CLOSED.add((x,y,d))

    if (x, y) == target:
        break
    
    for nd in DIRS:
        nx, ny = x+nd[0], y+nd[1]
        if d == nd:
            nc = c+1
            if (nx, ny, nd) in CLOSED or data[ny][nx] == '#':
                continue
            hq.heappush(OPEN, (nc, nx, ny, nd))

            if nc == TC[(nx,ny,nd)]:
                T[(nx,ny, nd)].add((x,y,d))
            elif nc < TC[(nx,ny, nd)]:
                TC[(nx,ny, nd)] = nc
                T[(nx,ny, nd)] = set()
                T[(nx,ny, nd)].add((x,y,d))
        else:
            nc = c+1000
            if (nx, ny, nd) in CLOSED or data[ny][nx] == '#':
                continue
            hq.heappush(OPEN, (nc, x, y, nd))

            if nc == TC[(x,y,nd)]:
                T[(x,y, nd)].add((x,y,d))
            elif nc < TC[(x,y, nd)]:
                TC[(x,y, nd)] = nc
                T[(x,y, nd)] = set()
                T[(x,y, nd)].add((x,y,d))

pr(c)

Q=[]
for i in DIRS: Q.append(T[(target[0], target[1], i)])
TILES=set()
TILES.add(target)
while Q:
    s = Q.pop(0)
    if (x,y) == s:
        break

    for x,y,d in s:
        TILES.add((x,y))
        Q.append(T[(x,y,d)])
        T[(x,y,d)] = set()

# draw(TILES)
pr(len(TILES))