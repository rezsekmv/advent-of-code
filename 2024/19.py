from util import *
towels, data = get_data().split('\n\n')

DP={}
def calc(puzzle, c):
    if puzzle in DP:
        return DP[puzzle]    
    
    if len(puzzle) == 0:
        return 1

    a=0
    for t in towels.split(', '):
        if puzzle.startswith(t):
            a += calc(puzzle[len(t):], c)

    DP[puzzle] = a    
    return a

for d in data.split('\n'):
    if calc(d,0) > 0:
        p1+=1
    p2+=calc(d, 0)

pr(p1)    
pr(p2)