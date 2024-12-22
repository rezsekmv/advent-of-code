from util import *
regs, ins = get_data().split('\n\n')

p1=[]
R={}
P=list(map(int,ins.split(':')[1].strip().split(',')))
for r in regs.split('\n'):
    s = r.split(':')
    letter = s[0].split(' ')[1]
    val = int(s[1].strip())
    R[letter] = val

def getCombo(num, R):
    if 0<=num<=3: 
        return num
    elif num == 4:
        return R['A']
    elif num == 5:
        return R['B']
    elif num == 6:
        return R['C']
    else:
        assert False


def run(R, P):
    out=[]
    i=0
    jump=False

    while i < len(P)-1:
        op = P[i]
        pa = P[i+1]
        
        if op == 0:
            R['A'] = R['A']//(2**getCombo(pa, R))
        elif op == 1:
            R['B'] = R['B'] ^ pa
        elif op == 2:
            R['B'] = getCombo(pa, R)%8
        elif op == 3:
            if R['A'] != 0:
                i=pa
                jump=True
        elif op == 4:
            R['B'] = R['B'] ^ R['C']
        elif op == 5:
            res = getCombo(pa, R)%8
            out.append(res)
        elif op == 6:
            R['B'] = R['A']//(2**getCombo(pa, R))
        elif op == 7:
            R['C'] = R['A']//(2**getCombo(pa, R))
        else:
            assert False

        if jump:
            jump = False
        else:
            i+=2
    return out


pr(','.join(map(str,run(dc(R),P))))

R = {
    'A':0,
    'B':0,
    'C':0
}
Q=deque([(0, 1)])
while Q:
    a,i = Q.popleft()

    if i > len(P):
        break

    for aa in range(a*8, a*8+9):
        goal = P[-1*i:]
        R['A']=aa
        o=run(dc(R),P)
        if o == goal:
            Q.append((aa, i+1))

pr(a)

    



    


