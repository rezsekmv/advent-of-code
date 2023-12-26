import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from copy import deepcopy

text = get_data(21, 2023)
lines = text.split('\n')

# init
S = len(lines)
G = [[lines[i][j] for j in range(S)] for i in range(S)]
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start = None
part1_steps = 64
part2_steps = 26501365

# find start
for r in range(S):
    for c in range(S):
        if G[r][c] == 'S':
            start = (r,c)

sr, sc = start

# find possible steps (working for one grid)
def bfs(start, steps):
    can_be = set([start])
    for _ in range(steps):
        next = set()
        while can_be:
            curr = can_be.pop()
            r = curr[0]
            c = curr[1]
            for rd, cd in DIRS:
                rr, cc = (r+rd, c+cd)
                if rr in range(S) and cc in range(S) and G[rr][cc] != '#':
                    next.add((rr,cc))
        can_be = deepcopy(next)
        
    return len(can_be)

# part1
print(bfs((sr, sc), part1_steps))


# ========= PART2 magic ===============
# visulaization: https://raw.githubusercontent.com/democat3457/AdventOfCode/master/2023/resources/day21gridvis.png

grids_in_the_row = part2_steps // S - 1

start_grids = (grids_in_the_row // 2 * 2 +1 ) ** 2
non_start_grids = ((grids_in_the_row + 1) // 2 * 2) ** 2

start_grid_points = bfs((sr, sc), S*2 +1)
non_start_grid_points = bfs((sr, sc), S*2)

mid_top = bfs((S-1, sc), S-1)
mid_right = bfs((sr, 0), S-1)
mid_bottom = bfs((0, sc), S-1)
mid_left = bfs((sr, S-1), S-1)
mids = mid_top + mid_right + mid_bottom + mid_left

large_tr = bfs((S-1, 0), S*3//2-1)
large_br = bfs((0, 0), S*3//2-1)
large_bl = bfs((0, S-1), S*3//2-1)
large_tl = bfs((S-1, S-1), S*3//2-1)
larges = large_tr + large_br + large_bl + large_tl

small_tr = bfs((S-1, 0), S//2-1)
small_br = bfs((0, 0), S//2-1)
small_bl = bfs((0, S-1), S//2-1)
small_tl = bfs((S-1, S-1), S//2-1)
smalls = small_tr + small_br + small_bl + small_tl

p2 = \
    start_grids * start_grid_points + \
    non_start_grids * non_start_grid_points + \
    mids + \
    grids_in_the_row * larges + \
    (grids_in_the_row + 1) * smalls

print(p2)