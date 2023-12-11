import sys
sys.path.append('../advent_of_code')
from input_data import get_data

text = get_data(11, 2023)
lines = text.split('\n')

data = [list(d) for d in lines]
R = len(data)
C = len(data[0])


empty_rows = []
# find empty rows
for row in range(R):
    if all(cell == '.' for cell in data[row]):
        empty_rows.append(row)

empty_cols = []
# find empty columns
for col in range(C):
    column = []
    for row in range(R):
        column.append(data[row][col])
    if all(cell == '.' for cell in column):
        empty_cols.append(col) 

# find shortest path between 'a' and 'b' galaxy
def find_path(a, b, p2):
    extra = 0
    extra += len(set(range(a[0], b[0])) & set(empty_rows))
    
    st, en = None, None
    if a[1] < b[1]:
        st, en = a[1], b[1]
    else:
        st, en = b[1], a[1]
    
    extra += len(set(range(st, en)) & set(empty_cols))
    extra = extra*(1_000_000-1) if p2 else extra
    return abs(b[0]-a[0])+abs(b[1]-a[1])+extra

galaxies = []
# find galaxies
for row in range(R):
    for col in range(C):
        if data[row][col] == '#':
            galaxies.append((row, col))

p1 = 0
p2 = 0
# go trough galaxy pairs (only 1 times per pair)
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        p1 += find_path(galaxies[i], galaxies[j], False)
        p2 += find_path(galaxies[i], galaxies[j], True)

print(p1)
print(p2)