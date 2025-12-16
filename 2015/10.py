from util import *

inp = "1321131112"

def calc(inp):
    ans = ''
    i = 0
    a = 0
    while i < len(inp)-1:
        if inp[i+1] == inp[i]:
            a += 1
        else:
            ans += (str(a+1) + inp[i])
            a = 0
        i += 1

    ans += (str(a+1) + inp[i])

    return ans 

for i in range(40):
    inp = calc(inp)

pr(len(inp))

for i in range(10):
    inp = calc(inp)

pr(len(inp))