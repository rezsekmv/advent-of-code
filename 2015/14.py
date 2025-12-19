from util import *

lines = get_data().split('\n')

R = []
for l in lines:
    v,t,r = getNumbers(l)
    R.append((v,t,r,False,t-1,0))

def maxd(A):
    max_ = 0
    maxi = []
    for i,r in en(A):
        if max_ < r[-1]:
            max_ = r[-1]
            maxi = [i]
        if max_ == r[-1]:
            maxi.append(i)
    return max_, maxi

RR = [0]*len(R)
for i in range(2503):
    for i,(v,t,r,rest,go_time,dist) in en(R):
        if rest:
            if go_time == 0:
                R[i]=(v,t,r,not rest,t-1,dist)
            else:
                R[i]=(v,t,r,rest,go_time-1,dist)
        else:
            if go_time == 0:
                R[i]=(v,t,r,not rest,r-1,dist+v)
            else:
                R[i]=(v,t,r,rest,go_time-1,dist+v)
    
    for mm in maxd(R)[1]:
        RR[mm] += 1

pr(maxd(R)[0])
pr(max(RR))