from copy import deepcopy

FILENAME = '18.txt'

with open(FILENAME) as f:
    lines = f.readlines()
    f.close()



cubes = []
for line in lines:
    line = line.strip()
    words = []
    for coord in line.split(','):
        words.append(int(coord))
    cubes.append(words)

dest = [22,22,22]
def isGhostCube(cube, tmp, limit=0):
    if limit >= 5:
        return False
    if cube in tmp or cube == dest:
        return False
    N = [
        [cube[0]-1, cube[1], cube[2]],
        [cube[0]+1, cube[1], cube[2]],
        [cube[0], cube[1]-1, cube[2]],
        [cube[0], cube[1]+1, cube[2]],
        [cube[0], cube[1], cube[2]-1],
        [cube[0], cube[1], cube[2]+1]
    ]

    nc = 0
    for n in N:
        if n in tmp:
            nc += 1
        newTmp = deepcopy(tmp)
        newTmp.append(cube)
        if isGhostCube(n, newTmp, limit+1):
            nc += 1

    return nc == 6



def getSpareSides(cube):
    N = [
        [cube[0]-1, cube[1], cube[2]],
        [cube[0]+1, cube[1], cube[2]],
        [cube[0], cube[1]-1, cube[2]],
        [cube[0], cube[1]+1, cube[2]],
        [cube[0], cube[1], cube[2]-1],
        [cube[0], cube[1], cube[2]+1]
    ]
    notSpare = 0
    for n in N:
        if n in cubes:
            notSpare += 1
    return 6 - notSpare


ans = 0
for p, cube in enumerate(cubes):
    ans += getSpareSides(cube)
    print(str(p / len(lines)*100) + '%')

print(ans)
