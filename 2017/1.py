from input_data import get_data

data = get_data(1)

p1, p2 = 0, 0
prev = data[-1]
hi = len(data)//2
for b in data: 
    if b == prev:
        p1 += int(b)
    prev = b

    if b == data[hi%len(data)]:
        p2 += int(b)
    hi += 1

print(p1)
print(p2)
    