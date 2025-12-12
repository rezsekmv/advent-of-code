from util import *

lines = get_data().split('\n')

G, R, C = getGrid(lines)

OPEN=set()
for y in range(R):
    for x in range(C):
        if G[y][x] == 'S':
            OPEN.add((x,y))

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def shortest(x, y, target, ob=set()):
    COSTS = defaultdict(lambda: float('inf'))
    start = (0, x, y)
    OPEN = []
    hq.heappush(OPEN, start)
    CLOSED = set()
    PARENT = {}

    while OPEN:
        f, g, x, y = hq.heappop(OPEN)
        if (x, y) in CLOSED:
            continue
        CLOSED.add((x,y))

        if (x, y) == target:
            path = []
            while (x,y) in PARENT:
                path.append((x,y))
                x,y = PARENT[(x,y)]
            path.append((start[2], start[3]))
            return path[::-1]

        for dx, dy in DIRS:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < C and 0 <= ny < R):
                continue
            if (nx, ny) in CLOSED or (nx, ny) in ob:
                continue

            ng = g + 1
            if ng < COSTS[(nx, ny)]:
                COSTS[(nx, ny)] = ng
                # nf = ng + manhattan((nx, ny), target)
                hq.heappush(OPEN, (ng, nx, ny))
                PARENT[(nx, ny)] = (x, y)

    assert False


pr(p1)