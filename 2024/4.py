from input_data import get_data

text = get_data(4, example=False)
lines = text.split('\n')

data = [list(d) for d in lines]
R = len(data)
C = len(data[0])

def match(a,b):
    if len(a) != len(b):
        return False
    for i in range(len(b)):
        if a[i] != b[i]:
            return False
    return True

X = ['X', 'M', 'A', 'S']
M1 = ['M', 'S', 'M', 'S']
M2 = ['M', 'S', 'S', 'M']
M3 = ['S', 'M', 'M', 'S']
M4 = ['S', 'M', 'S', 'M']

p1=0
p2=0
for y in range(R):
    for x in range(C):
        
        if x+3 < C and (match(list(reversed(data[y][x:x+4])), X) or match(data[y][x:x+4], X)):
            p1+=1
        
        if y+3 < R:
            n = []
            for i in data[y:y+4]:
                n.append(i[x])
            if match(n, X) or match(list(reversed(n)), X):
                p1+=1

        n = []
        for i in range(4):
            if x+i >= C or y+i >= R:
                break
            n.append(data[y+i][x+i])
        if match(n, X) or match(list(reversed(n)), X):
            p1+=1

        n = []
        for i in range(4):
            if x+i >= C or y-i < 0:
                break
            n.append(data[y-i][x+i])
        if match(n, X) or match(list(reversed(n)), X):
            p1+=1

        if 0 <= x-1 and x+1 < C and 0 <= y-1 and y+1 < R:
            n = []
            n.append(data[y-1][x-1])
            n.append(data[y+1][x+1])
            n.append(data[y+1][x-1])
            n.append(data[y-1][x+1])
            if data[y][x] == 'A' and (match(n, M1) or match(n, M2) or match(n, M3) or match(n, M4)):
                print(x,y)
                p2+=1



print(p1)
print(p2)

