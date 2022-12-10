from my_input import lines

data = []
for index, line in enumerate(lines):
    d = line.split(' ')
    for i in range(int(d[1])):
        data.append(d[0])

map = []
size = 1000
for i in range(size):
    map.append([])
    for j in range(size):
        map[i].append('.')

knots = []
for i in range(10):
    knots.append([size//2, size//2])

def getTailMove(h, t):
    rowDif = abs(h[0] - t[0])
    colDif = abs(h[1] - t[1])

    if (rowDif == 1 and colDif == 1) or \
    (rowDif == 0 and colDif == 1) or \
    (rowDif == 1 and colDif == 0) or \
    (rowDif == 0 and colDif == 0):
        return t

    elif rowDif == 2:
        # move row
        if h[0] > t[0]:
            t[0] += 1
        elif h[0] < t[0]:
            t[0] -= 1
        if colDif > 0:
            # move col
            if h[1] > t[1]:
                t[1] += 1
            elif h[1] < t[1]:
                t[1] -= 1

    elif colDif == 2:
        # move col
        if h[1] > t[1]:
            t[1] += 1
        elif h[1] < t[1]:
            t[1] -= 1
        if rowDif > 0:
            # move row
            if h[0] > t[0]:
                t[0] += 1
            elif h[0] < t[0]:
                t[0] -= 1

    return t


for d in data:

    if d == 'U':
        knots[0][0] -= 1

    elif d == 'R':
        knots[0][1] += 1

    elif d == 'D':
        knots[0][0] += 1

    elif d == 'L':
        knots[0][1] -= 1

    for i in range(len(knots)-1):
        knots[i+1] = getTailMove(knots[i], knots[i+1])

    print(knots)
    print()

    map[knots[-1][0]][knots[-1][1]] = '#'

count = 0
for row in map:
    for c in row:
        if c == '#':
            count += 1

print(count)