from copy import deepcopy

def getHighest(coords):
    return max(coords, key=lambda c: c[0])[0]

def getRow(row, coordList):
    ans = set()
    for coord in coordList:
        if coord[0] == row:
            ans.add(coord[1])
    return ans

rocks = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]

FILENAME = '17.txt'

line = ''
with open(FILENAME) as f:
    line = f.read()
    f.close()


width = 7

rockIndex = 0
lineIndex = 0

currentRock = []
coordsPlaced = set()
rocksPlaced = 0
highestRock = 0
sortedCoords = []

cache = []
cc = 0
ci = -1
# main loop
while rocksPlaced < 5022:

    currentRock = deepcopy(rocks[rockIndex % len(rocks)])
    for i in range(len(currentRock)):
        currentRock[i] = (currentRock[i][0] + highestRock +
                          4, currentRock[i][1] + 3)

    stopped = False
    while not stopped:
        # go side
        # right
        if line[lineIndex % len(line)] == '>':
            for x, y in currentRock:
                if not (0 < y+1 < width+1) or (x, y+1) in coordsPlaced:
                    break
            else:
                for i in range(len(currentRock)):
                    currentRock[i] = (currentRock[i][0], currentRock[i][1]+1)

        # left
        elif line[lineIndex % len(line)] == '<':
            for x, y in currentRock:
                if not (0 < y-1 < width+1) or (x, y-1) in coordsPlaced:
                    break
            else:
                for i in range(len(currentRock)):
                    currentRock[i] = (currentRock[i][0], currentRock[i][1]-1)

        lineIndex += 1

        # go down
        for x, y in currentRock:
            if (x-1, y) in coordsPlaced or x-1 < 1:
                stopped = True
                break
        else:
            for i in range(len(currentRock)):
                currentRock[i] = (currentRock[i][0]-1, currentRock[i][1])

    tmp = deepcopy(currentRock)
    for i in range(len(tmp)):
        tmp[i] = (tmp[i][0]-highestRock, tmp[i][1])

    if cc == 0:
        try:
            ci = cache.index(tmp)
        except:
            pass
    elif cc > 0 and ci > 0:
        ci += 1
        if cache[ci] == tmp:
            print('found', cc)
            cc += 1
        else:
            cc = 0
            ci = -1

    if cc > 10:
        print(cc)
    cache.append(tmp)    
    
    # next
    rockIndex += 1
    rocksPlaced += 1
    coordsPlaced.update(currentRock)
    highestRock = getHighest(coordsPlaced)

sortedCoords = sorted(list(coordsPlaced), key=lambda a: (a[0], a[1]))

print('sym finished')

