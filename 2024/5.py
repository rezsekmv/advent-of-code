import sys
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)

from input_data import get_data

text = get_data(5, example=False)
rules, lines = text.split('\n\n')
rules = rules.split('\n')

p1=0
p2=0

def calc(az):
    good = True
    
    for i, a in enumerate(az):
        for b in rules:
            x,y = b.split('|')
            if a == x and y in az[:i]:
                good = False
            if a == y and x in az[i+1:]:
                good = False
    return good, int(az[len(az)//2])


I=[]
for l in lines.split('\n'):
    az = l.split(',')
    good, m = calc(az)
    if good:
        p1 += m
    else:
        I.append(az)
pr(p1)

for j in I:
    good = False
    while not good:
        good = True
        for i in range(len(j)):
            for b in rules:
                x,y = b.split('|')
                if j[i] == x and y in j[:i]:
                    good = False
                    j[i], j[i-1] = j[i-1], j[i]
                if j[i] == y and x in j[i+1:]:
                    good = False
                    j[i], j[i+1] = j[i+1], j[i]
    
    p2 += calc(j)[1]
pr(p2)
