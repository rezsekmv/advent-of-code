from my_input import lines

visible = 0

def getValue(row, col):
    tree = int(lines[row][col])

    #left
    lcount = 0
    if col > 0:
        for j in range(col-1, -1, -1):
            tmp = int(lines[row][j])
            if tmp < tree:
                lcount += 1
            else:
                lcount += 1
                break

    #right
    rcount = 0
    if col < len(lines[row]):
        for j in range(col+1, len(lines[row])):
            tmp = int(lines[row][j])
            if tmp < tree:
                rcount += 1
            else:
                rcount += 1
                break
    
    #up
    ucount = 0
    if row > 0:
        for i in range(row-1, -1, -1):
            tmp = int(lines[i][col])
            if tmp < tree:
                ucount += 1
            else:
                ucount += 1
                break
    #down
    dcount = 0
    if row < len(lines):
        for i in range(row+1, len(lines)):
            tmp = int(lines[i][col])
            if tmp < tree:
                dcount += 1
            else:
                dcount += 1
                break

    return lcount * rcount * ucount * dcount


m = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        v = getValue(i, j)
        if v > m:
            m = v
            print(i,j)
    
print(m)