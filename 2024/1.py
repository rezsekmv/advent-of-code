from input_data import get_data

data = get_data(1).split()

e = sorted(data[::2])
m = sorted(data[1::2])

p1 = 0
p2 = 0
for i in range(len(e)):
    p1 += abs(int(e[i])-int(m[i]))
    p2 += m.count(e[i])*int(e[i])

print(p1)
print(p2)