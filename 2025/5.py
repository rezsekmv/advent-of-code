from util import *

RS, IDS  = get_data().split('\n\n')
RS = RS.split('\n')
IDS = IDS.split('\n')

S = []
for j,r in en(RS):
    a,b = r.split('-')
    a = int(a)
    b = int(b)
    S.append((a,b))

# p1
for id in IDS:
    for i in range(len(S)):
        if S[i][0] <= int(id) <= S[i][1]:
            p1+=1
            break

# p2
for i in range(len(S)):
    j=0
    while j<i:
        aa,bb = S[j]
        f = False

        if aa <= S[i][0] <= bb:
            if aa <= S[i][1] <= bb:
                # benne van
                S[i] = (1,0)
            else:
                # ha nincs benne, akkor határra
                S[i] = (bb+1, S[i][1])
                f = True
        
        if aa <= S[i][1] <= bb:
            S[i] = (S[i][0], aa-1)
            f = True

        if S[i][0]<= aa <=S[i][1] and S[i][0]<= aa <=S[i][1]:
            S[j] = (1,0)

        if f:
            j=0
        else:
            j+=1 
    i+=1


pr(p1)

for s in S:
    p2 += s[1]-s[0]+1

pr(p2)