FILENAME = '3.txt'
lines = []
groups = []
result = 0

def findCommon(backpack):
    return list(set(backpack[0])&set(backpack[1])&set(backpack[2]))[0]

def getPriority(item):
    if ord(item) >= 97:
        return ord(item)-96
    else:
        return ord(item)-64+26

with open(FILENAME) as f:
    lines = [l.rstrip() for l in f.readlines()]
    f.close()

for i in range(0, len(lines), 3):
    groups.append([lines[i], lines[i+1], lines[i+2]])

for group in groups:
    result += getPriority(findCommon(group))

print(result)