from input_data import get_data

data = get_data()
s=0
p2=True
b=None
for j,i in enumerate(data):
    if i == '(':
        s+=1
    elif i == ')':
        s-=1
    if s < 0 and p2:
        p2=False
        b=j

print(s)
print(b)