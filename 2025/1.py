from util import *

data = get_data().split('\n')

p1 = 0
p2 = 0
curr = 50

def run(n, plus):
    global curr, p2
    for _ in range(n):
        if plus:
            curr += 1
        else:
            curr -= 1
        curr = curr % 100
        
        if curr == 0:
            p2 += 1

for i,d in en(data):
    if (d[0] == 'R'):
        run((int(d[1:])), True)
    if (d[0] == 'L'):
        run((int(d[1:])), False)
    
    if curr == 0:
        p1 += 1
    
    curr = curr % 100

pr(p1)
pr(p2)
