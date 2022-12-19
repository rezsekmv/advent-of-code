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
before = 0
# main loop
while rocksPlaced < 1000000000000%3878:

    currentRock = deepcopy(rocks[rockIndex % len(rocks)])
    for i in range(len(currentRock)):
        currentRock[i] = (currentRock[i][0] + highestRock + 4, currentRock[i][1] + 3)

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

    signature = (rockIndex%len(rocks), lineIndex%len(line) )
    if (signature in cache):
        cc += 1
        before = highestRock
    else:
        cc = 0
        before = 0
        cache.append( signature )
    
    if rocksPlaced//2 == cc and rocksPlaced > 10:
        ans = highestRock
        break
    
    # next
    rockIndex += 1
    rocksPlaced += 1
    coordsPlaced.update(currentRock)
    highestRock = getHighest(coordsPlaced)

sortedCoords = sorted(list(coordsPlaced), key=lambda a: (a[0], a[1]))
ans = 0
a = 1000000000000 // 96
ans += highestRock*a
print('sym finished')
print(ans)

