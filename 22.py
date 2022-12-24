from my_input import lines
import util
import math
from enum import Enum

class Dir(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

emptys = []
walls = []
commands = lines[-1]
for row, line in enumerate(lines):
    if line == '':
        break
    for col, cell in enumerate(line):
        if cell == '.':
            emptys.append((row, col))
        if cell == '#':
            walls.append((row, col))

pos = emptys[0]
direction = Dir.RIGHT
a = 50

def getSide(coord):
    if a <= coord[1] < 2*a   and 0 <= coord[0] < a:
        return 1
    if 2*a <= coord[1] < 3*a and 0 <= coord[0] < a:
        return 2
    if a <= coord[1] < 2*a   and a <= coord[0] < 2*a:
        return 3
    if 0 <= coord[1] < a     and 2*a <= coord[0] < 3*a:
        return 4
    if a <= coord[1] < 2*a   and 2*a <= coord[0] < 3*a:
        return 5
    if 0 <= coord[1] < a     and 3*a <= coord[0] < 4*a:
        return 6


def wrap(dir, pos):
    side = getSide(pos)

    if dir == Dir.RIGHT:
        if side == 1 or side == 4:
            return Dir.RIGHT, (pos[0], pos[1]+1)
        if side == 2:
            return Dir.LEFT, (2*a+pos[0], 2*a-1)
        if side == 3:
            return Dir.UP, (pos[1]+a, a-1)
        if side == 5:
            return Dir.LEFT, (pos[0]-2*a, 3*a-1)
        if side == 6:
            return Dir.UP, (3*a-1, pos[0]-2*a)


    if dir == Dir.LEFT:
        if side == 2 or side == 5:
            return Dir.LEFT, (pos[0], pos[1]-1)

        if side == 1:
            return Dir.RIGHT, (pos[0]+2*a, 0)
        if side == 3:
            return Dir.DOWN, (2*a, pos[0]-a)
        if side == 4:
            return Dir.RIGHT, (pos[0]-2*a, a)
        if side == 6:
            return Dir.DOWN, (a, pos[0]-2*a)


    if dir == Dir.UP:
        if side == 3 or side == 5 or side == 6:
            return Dir.UP, (pos[0]-1, pos[1])

        if side == 1:
            return Dir.RIGHT, (pos[1]+2*a, 0)
        if side == 2:
            return Dir.UP, (4*a-1, pos[1]-2*a)
        if side == 4:
            return Dir.RIGHT, (pos[1]+a, a)


    if dir == Dir.DOWN:
        if side == 1 or side == 3 or side == 4:
            return Dir.DOWN, (pos[0]+1, pos[1])

        if side == 2:
            return Dir.LEFT, (pos[1]+a, 2*a)
        if side == 5:
            return Dir.LEFT, (pos[1]+a, a)
        if side == 6:
            return Dir.DOWN, (0, pos[1]+2*a)


    assert False, (dir, pos)



def do(command, pos, direction):
    if command == '':
        return pos, direction
    if command == 'R':
        return pos, Dir((direction.value+1)%4)
    elif command == 'L':
        return pos, Dir((direction.value-1)%4)
    else:
        newDir = direction
        for _ in range(int(command)):
            if direction == Dir.RIGHT:
                nextPos = (pos[0], pos[1]+1)    
                # wrap around
                if nextPos not in emptys and nextPos not in walls:
                    newDir, nextPos = wrap(direction, pos)
                # next
                if nextPos in walls:
                    break
                elif nextPos in emptys:
                    pos = nextPos
                    direction = newDir


            if direction == Dir.LEFT:
                nextPos = (pos[0], pos[1]-1)
                
                # wrap around
                if nextPos not in emptys and nextPos not in walls:
                    newDir, nextPos = wrap(direction, pos)

                # next
                if nextPos in walls:
                    break
                elif nextPos in emptys:
                    pos = nextPos
                    direction = newDir


            if direction == Dir.UP:
                nextPos = (pos[0]-1, pos[1])
                
                # wrap around
                if nextPos not in emptys and nextPos not in walls:
                    newDir, nextPos = wrap(direction, pos)
                
                # next
                if nextPos in walls:
                    break
                elif nextPos in emptys:
                    pos = nextPos
                    direction = newDir


            if direction == Dir.DOWN:
                nextPos = (pos[0]+1, pos[1])
                
                # wrap around
                if nextPos not in emptys and nextPos not in walls:
                    newDir, nextPos = wrap(direction, pos)

                # next
                if nextPos in walls:
                    break
                elif nextPos in emptys:
                    pos = nextPos
                    direction = newDir


        return pos, direction


wait = ''
for c in commands:
    if not c.isnumeric():
        pos, direction = do(wait, pos, direction)
        wait = ''
        pos, direction = do(c, pos, direction)
    else:
        wait += c

pos, direction = do(wait, pos, direction)

print(pos[0], pos[1], direction)
print(1000*(pos[0]+1) + 4*(pos[1]+1) + direction.value)