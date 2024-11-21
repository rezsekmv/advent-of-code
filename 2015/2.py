from input_data import get_data

data = get_data(2).split('\n')
p1=0
p2=0
for i in data:
    l,w,h = list(map(int, i.split('x')))
    p1 += 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,l*h)
    p2 += 2*l + 2*w + 2*h - 2*max(l,w,h) + h*l*w

print(p1)
print(p2)