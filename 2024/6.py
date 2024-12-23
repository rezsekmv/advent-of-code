from util import *

text = get_data()
data, R, C = getGrid(text.split('\n'))


def solveP1():
    p1=set()
    d=0
    for y in range(R):
        for x in range(C):
            if data[y][x] == '^':
                s=(x,y)
    p1.add(s)

    while True:
        match d:
            case 0:
                ns = (s[0], s[1]-1)
            case 1:
                ns = (s[0]+1, s[1])
            case 2:
                ns = (s[0], s[1]+1)
            case 3:
                ns = (s[0]-1, s[1])

        if not (0 <= ns[0] < C and 0 <= ns[1] < R):
            break
        if data[ns[1]][ns[0]] == '.':
            p1.add(ns)
        if data[ns[1]][ns[0]] == '#':
            d = (d+1)%4
            ns = s
        s = ns
    return len(p1)
            

def solveP2():
    p2=0
    for i in range(R):
        for j in range(C):
            o=set()
            d=0
            for y in range(R):
                for x in range(C):
                    if data[y][x] == '^':
                        s=(x,y)

            while True:
                match d:
                    case 0:
                        ns = (s[0], s[1]-1)
                    case 1:
                        ns = (s[0]+1, s[1])
                    case 2:
                        ns = (s[0], s[1]+1)
                    case 3:
                        ns = (s[0]-1, s[1])

                if not (0 <= ns[0] < C and 0 <= ns[1] < R):
                    break
                if data[ns[1]][ns[0]] == '#' or ns == (j,i):
                    if (d, ns) in o:
                        p2+=1
                        break
                    o.add((d, ns))
                    d = (d+1)%4
                    ns = s
                s = ns
    return p2

pr(solveP1())
pr(solveP2())
