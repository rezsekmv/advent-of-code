from input_data import get_data

data = get_data()
s={(0,0)}
    
for p1 in [True, False]:
    c=(0,0)
    r=(0,0)
    s2={c}
    for j,i in enumerate(data):
        x2,y2=r
        x,y=c
        if p1 or j%2==0:
            match i:
                case '^':
                    c = (x,y+1)
                case '<':
                    c = (x-1,y)
                case '>':
                    c = (x+1,y)
                case 'v':
                    c = (x,y-1)
            if p1:
                s.add(c)
            else:
                s2.add(c)
        else:
            match i:
                case '^':
                    r = (x2,y2+1)
                case '<':
                    r = (x2-1,y2)
                case '>':
                    r = (x2+1,y2)
                case 'v':
                    r = (x2,y2-1)
            s2.add(r)
print(len(s))
print(len(s2))
