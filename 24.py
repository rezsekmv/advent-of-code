from my_input import lines
import util
import math
from copy import deepcopy

current = (0,1)
maxx = len(lines[0])-1
maxy = len(lines)-1
goal = (maxy-1, maxx-2)
blizs = []
dirs = []
for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if c == '#' or c == '.':
            continue
        blizs.append((int(x), int(y)))
        dirs.append(c)

bcache = []
def bPos(blizzards, num):
    for i in range(num):
        if i % 100 == 0:
            print(i)
        for i, d in enumerate(dirs):
            if d == '>':
                nextpos = blizzards[i][1]+1
                if nextpos == maxx:
                    nextpos = 1
                blizzards[i] = (blizzards[i][0], nextpos)
            if d == '<':
                nextpos = blizzards[i][1]-1
                if nextpos == 0:
                    nextpos = maxx - 1
                blizzards[i] = (blizzards[i][0], nextpos)
            if d == '^':
                nextpos = blizzards[i][0]-1
                if nextpos == 0:
                    nextpos = maxy - 1
                blizzards[i] = (nextpos, blizzards[i][1])
            if d == 'v':
                nextpos = blizzards[i][0]+1
                if nextpos == maxy:
                    nextpos = 1
                blizzards[i] = (nextpos, blizzards[i][1])
        bcache.append(deepcopy(blizzards))


def bfs(start):
    queue = [(start, 18)]

    while len(queue) > 0:
        node, steps = queue.pop(0)
        if steps%50 == 0:
            print(steps, node)
        if node == current:
            return steps

        for d in [(0,0), (1,0), (0,1), (-1,0), (0,-1)]:
            n = (node[0]+d[0], node[1]+d[1])
            if n not in bcache[steps+1] and (n, steps+1) not in queue and 0 <= n[0] < maxy and 0 < n[1] < maxx:
                queue.append((n, steps+1))

bPos(deepcopy(blizs), 2000)


print('blizzard cache rdy')

# goal (149, 20) reached after 373 steps (queue size: 904)
# goal (0, -1) reached after 706 steps (queue size: 949)
# goal (149, 20) reached after 997 steps (queue size: 874)

print(bfs(goal))
    





