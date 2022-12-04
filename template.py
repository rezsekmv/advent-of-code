FILENAME = '0.txt'
lines = []

with open(FILENAME) as f:
    lines = [l.rstrip() for l in f.readlines()]
    f.close()

for line in lines:
    pass

print(lines)