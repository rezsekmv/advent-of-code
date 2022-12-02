FILENAME = '2.txt'
lines = []

elf = ['A', 'B', 'C']
me  = ['X', 'Y', 'Z']
scores = [1, 2, 3]
result = 0

def getScore(shape):
    if (data[0] == 'A' and shape == 'Z'):
        return 0
    if (data[0] == 'C' and shape == 'X'):
        return 6
    if elf.index(data[0]) > me.index(shape):
        return 0
    if elf.index(data[0]) == me.index(shape):
        return 3
    if elf.index(data[0]) < me.index(shape):
        return 6

def giveShape(shape, points):
    if elf.index(data[0]) > me.index(shape):
        return 0
    if elf.index(data[0]) == me.index(shape):
        return 3
    if elf.index(data[0]) < me.index(shape):
        return 6


with open(FILENAME) as f:
    lines = [l.rstrip() for l in f.readlines()]
    f.close()

for line in lines:
    data = line.split(' ')
    points = 0
    chosen = ''
    for shape in me:
        if (data[1] == 'X') and getScore(shape) == 0:
                chosen = shape
        if (data[1] == 'Y') and getScore(shape) == 3:
                chosen = shape
        if (data[1] == 'Z') and getScore(shape) == 6:
                chosen = shape
    
    points = me.index(chosen)+1 + getScore(chosen)
    result += points
    
print(result)

