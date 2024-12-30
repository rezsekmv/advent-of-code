from util import *

data = get_data().split('\n')

DIGITS=[
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    ['#','0','A'],
]
ARROWS=[
    ['#','^','A'],
    ['<','v','>'],
]
DIR_TO_CHAR={
    (1,0): '>',
    (0,1): 'v',
    (-1,0): '<',
    (0,-1): '^',
    (0,0): 'A'
}

def find_in_grid(grid, target):
    r=len(grid)
    c=len(grid[0])
    for y in range(r):
        for x in range(c):
            if grid[y][x] == target:
                return x,y

P1 = 3
P2 = 26
DP = {}
def find_best_move(target, robot, i, part2=False):
    if i == 0:
        return 1, robot

    if part2:
        key = i, target, robot
        if key in DP:
            return DP[key]

    if part2:
        TO = P2
    else:
        TO = P1

    rx, ry = robot
    tx, ty = find_in_grid(DIGITS if TO == i else ARROWS, target)

    P=[]
    dx,dy = tx-rx, ty-ry
    for _ in range(abs(dx)):
        if dx < 0:
            P.append((-1, 0))
        if 0 < dx:
            P.append((1, 0))
    for _ in range(abs(dy)):
        if dy < 0:
            P.append((0, -1))
        if 0 < dy:
            P.append((0, 1))


    ALL_PS = list(map(list, list(set(it.permutations(P)))))
    for ps in ALL_PS:
        ps.append((0,0))

    MOVES = []
    for plan in ALL_PS:
        
        next_rob = 2,0
        tmp_moves = 0
        tmp_robot = robot

        for move in plan:
            dx, dy = tmp_robot[0]+move[0], tmp_robot[1]+move[1]
            
            if (i == TO and DIGITS[dy][dx] == '#') or (i != TO and ARROWS[dy][dx] == '#'):
                tmp_moves = None
                break
            
            arrow = DIR_TO_CHAR[move]
            moves, next_rob = find_best_move(arrow, next_rob, i-1, part2)
            tmp_robot = dx, dy
            tmp_moves += moves

        if tmp_moves is not None:
            MOVES.append(tmp_moves)
    
    robot = tx, ty
    best = min(MOVES)

    if part2:
        DP[key] = best, robot
    return best, robot


for row in data:
    res=res2=0
    robot=robot2=2,3
    for char in row:  
        moves, robot = find_best_move(char, robot, P1)
        res+=moves
        
        moves2, robot2 = find_best_move(char, robot2, P2, True)
        res2+=moves2
    
    p1+=res*int(row[:-1])
    p2+=res2*int(row[:-1])
    
pr(p1)
pr(p2)
