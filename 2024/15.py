from util import *
map, ins = get_data().split('\n\n')

ins = ins.replace('\n', '')
map, R, C = getGrid(map.split('\n'))

C2=C+C
map2 = deepcopy(map)
for y in range(R):
    nx = []
    for x in range(C):
        if map2[y][x] == '@':
            nx.append('@')
            nx.append('.')
        elif map2[y][x] == 'O':
            nx.append('[')
            nx.append(']')
        elif map2[y][x] == '#':
            nx.append('#')
            nx.append('#')
        elif map2[y][x] == '.':
            nx.append('.')
            nx.append('.')
    map2[y] = nx

B=[]
W=[]
B2=[]
W2=[]
for y in range(R):
    for x in range(C):
        if map[y][x] == '@':
            pos = (x,y)
        if map[y][x] == 'O':
            B.append((x,y))
        if map[y][x] == '#':
            W.append((x,y))

    for x in range(C2):
        if map2[y][x] == '@':
            pos2 = (x,y)
        if map2[y][x] == '[' and map2[y][x+1] == ']':
            B2.append([(x,y), (x+1,y)])
        if map2[y][x] == '#':
            W2.append((x,y))

DI = {
    '<': (-1, 0),
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1)
}
def draw(pos, W, B, C):
    for y in range(R):
        for x in range(C):
            if (x,y) == pos:
                print('@',end='')
            elif (x,y) in flatten(B):
                print('O',end='')
            elif (x,y) in W:
                print('#',end='')
            else:
                print('.',end='')
        print()

def allowed(xx,yy, d, skip, B, W, p2=False):
    if (xx,yy) in W:
        return False

    if p2:
        for i, (a,b) in en(B):
            if i == skip:
                continue
            if a == (xx,yy) or b == (xx,yy):
                return allowed(a[0]+d[0], a[1]+d[1], d, i, B, W, p2) and allowed(b[0]+d[0], b[1]+d[1], d, i, B, W, p2)
    else:
        if (xx,yy) in B:
            i = B.index((xx,yy))
            if B.index((xx,yy)) != skip:
                return allowed(xx+d[0], yy+d[1], d, i, B, W, p2)
    return True


def move_boxes(x,y,d,skip, B, p2=False):
    if p2:
        for i,b in en(B):
            if i in skip:
                continue
            f=False
            for j,p in en(b):
                if p == (x,y):
                    b[0] = b[0][0]+d[0],b[0][1]+d[1]
                    b[1] = b[1][0]+d[0],b[1][1]+d[1]
                    skip.add(i)
                    f=True
                    
            if f:
                move_boxes(b[0][0],b[0][1],d,skip, B, p2)
                move_boxes(b[1][0],b[1][1],d,skip, B, p2)
                break
    else:
        for i,b in en(B):
            if i in skip:
                continue
            if b == (x,y):
                B[i] = b[0]+d[0],b[1]+d[1]
                skip.add(i)
                move_boxes(B[i][0],B[i][1],d,skip, B, p2)
                break

for I in ins:
    d = DI[I]

    x,y = pos[0]+d[0], pos[1]+d[1]
    if allowed(x,y,d, -1, B, W):
        pos = x,y
        move_boxes(x,y,d, set(), B)
    # draw(pos, W, B, C)


    x2,y2 = pos2[0]+d[0], pos2[1]+d[1]
    if allowed(x2,y2,d, -1, B2, W2, True):
        pos2 = x2,y2
        move_boxes(x2,y2,d, set(), B2, True)
    # draw(pos2, W2, B2, C2)

for x,y in B:
    p1 += (x+y*100)
pr(p1)

for b in B2:
    x,y = b[0]
    p2 += (x+y*100)
pr(p2)
