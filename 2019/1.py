from input_data import get_data

data = get_data(1).split()


p1 = 0
p2 = 0
for d in data:
    f = int(d)
    s = 0
    while f > 2:
        f = f//3-2
        s += f if f > 0 else 0
    
    p2+=s

    p1+=int(d)//3-2    
    

print(p1)
print(p2)
