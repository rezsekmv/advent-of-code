FILENAME = '4.txt'
lines = []
pairs = []
result = 0

def contain(first, second):
    if set(first) <= set(second) or set(second) <= set(first):
        return True
    return False

def overlap(first, second):
    if any(x in first for x in second) or any(x in second for x in first):
        return True
    return False

with open(FILENAME) as f:
    lines = [l.rstrip() for l in f.readlines()]
    f.close()

for line in lines:
    sp = line.split(',')
    sp[0] = list(range(int(sp[0].split('-')[0]), int(sp[0].split('-')[1])+1))
    sp[1] = list(range(int(sp[1].split('-')[0]), int(sp[1].split('-')[1])+1))
    
    pairs.append(sp)

for pair in pairs:
    if overlap(pair[0], pair[1]):
        result += 1

print(result)