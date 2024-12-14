from util import *
lines = get_data().split('\n')

def draw(ROBOTS):
    for y in range(R):
        for x in range(C):
            p=0
            for r in ROBOTS:
                if r[:2] == [x,y]:
                    p+=1
        
            print(p if p>0 else '.', end='')
        print()

ROBOTS=[]
for row in lines:
    ROBOTS.append(getNumbers(row, negative=True))

def xmas_found(ROBOTS):
    t=True
    for j in range(30):
        tl=bl=False
        for _,r in en(ROBOTS):
            if [45+j,R-18] == r[:2]:
                bl=True
            if [45+j,R-50] == r[:2]:
                tl=True
        if not (tl and bl):
            t=False
            break
    return t

C=101
R=103
sec = 100
i=1
while not xmas_found(ROBOTS):
    for j,r in en(ROBOTS):
        ROBOTS[j][0] = (ROBOTS[j][0]+ROBOTS[j][2])%C
        ROBOTS[j][1] = (ROBOTS[j][1]+ROBOTS[j][3])%R
    
    if i==sec:
        Qs=[0]*4
        for j,r in en(ROBOTS):
            x,y = r[:2]
            if x < C//2 and y < R//2:
                Qs[0]+=1
            if x > C//2 and y < R//2:
                Qs[1]+=1
            if x < C//2 and y > R//2:
                Qs[2]+=1
            if x > C//2 and y > R//2:
                Qs[3]+=1
        pr(math.prod(Qs))

    i+=1

i-=1 # because of last addition in while (when condition is false)

# draw(ROBOTS)
print(i)
