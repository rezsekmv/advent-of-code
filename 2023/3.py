import sys
sys.path.append('../advent_of_code')
from input_data import get_data

text = get_data(3, 2023)
rows = text.split('\n')

data = ['.'*len(rows[0])]
for r in rows:
    data.append('.'+r+'.')
data.append('.'*len(rows[0]))

digits = []
stars = []
for i, r  in enumerate(data):
    z = 0
    for j, c in enumerate(r):
        if c.isdigit():
            z += 1
        elif z > 0:
            digits.append([i, j-z, z])
            z = 0
        if c == '*':
            stars.append((i, j))

for d in digits:
    t = ''
    for z in range(d[2]):
        t += data[d[0]][d[1]+z]
    d.append(int(t))

part = [False] * len(digits)
for i, d in enumerate(digits):
    if data[d[0]][d[1]-1] != '.' or data[d[0]][d[1]+d[2]] != '.':
        part[i] = True
        continue
    for c in range(-1, d[2]+1):
        if data[d[0]-1][d[1]+c] != '.' or data[d[0]+1][d[1]+c] != '.':
            part[i] = True
            break

grs = []
for i, j in stars:
    gr = 1
    many = 0
    for d in digits:
        found = False
        for r, c in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            for a in range(d[2]):
                if i+r == d[0] and j+c == d[1]+a:
                    many += 1
                    gr *= d[3]
                    found = True
                    break
            if found:
                break

    if many == 2:
        grs.append(gr)

p = []
for i, d in enumerate(digits):
    if part[i]:
        p.append(d[3])

print(sum(p))
print(sum(grs))