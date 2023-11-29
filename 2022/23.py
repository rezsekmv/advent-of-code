from my_input import lines
import util
import math
from enum import Enum

class Dir(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

directions = [Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT]
elves = []
border = (len(lines), len(lines[0]))
for row, line in enumerate(lines):
    for col, cell in enumerate(line):
        if cell == '#':
            elves.append((row, col))

def proposeMove(elf, d):
    if d == Dir.UP:
        for delta in [(-1, 0), (-1, -1), (-1, 1)]:
            coord = (elf[0]+delta[0], elf[1]+delta[1])
            if not(0 <= coord[0] < border[0] and 0 <= coord[1] < border[1] and coord not in elves):
                break
        else:
            return (elf[0]-1, elf[1])
    
    if d == Dir.DOWN:
        for delta in [(1, 0), (1, -1), (1, 1)]:
            coord = (elf[0]+delta[0], elf[1]+delta[1])
            if not(0 <= coord[0] < border[0] and 0 <= coord[1] < border[1] and coord not in elves):
                break
        else:
            return (elf[0]+1, elf[1])

    if d == Dir.LEFT:
        for delta in [(0, -1), (-1, -1), (1, -1)]:
            coord = (elf[0]+delta[0], elf[1]+delta[1])
            if not(0 <= coord[0] < border[0] and 0 <= coord[1] < border[1] and coord not in elves):
                break
        else:
            return (elf[0], elf[1]-1)

    if d == Dir.RIGHT:
        for delta in [(0, 1), (-1, 1), (1, 1)]:
            coord = (elf[0]+delta[0], elf[1]+delta[1])
            if not(0 <= coord[0] < border[0] and 0 <= coord[1] < border[1] and coord not in elves):
                break
        else:
            return (elf[0], elf[1]+1)


for i in range(10):
    tmpElves = []
    for e in elves:
        for d in directions:
            prop = proposeMove(e, d)
            if prop != None:
                break
        else:
            prop = e
        tmpElves.append(prop)


    for t in tmpElves:
        indices = [i for i, x in enumerate(tmpElves) if x == t]
        if indices == 1:
            elves[indices] = t

        d = directions.pop(0)
        directions.append(d)


sides = [100, 100, 0, 0]
for e in elves:
    if e[0] < sides[0]:
        sides[0] = e[0]
    
    if e[1] < sides[1]:
        sides[1] = e[1]
    
    if e[0] > sides[2]:
        sides[2] = e[0]
    
    if e[1] > sides[3]:
        sides[3] = e[1]

empty = (sides[2]-sides[0])*(sides[3]-sides[1])-len(elves)
# 0, 1, 12, 10
print(sides)
print(empty)