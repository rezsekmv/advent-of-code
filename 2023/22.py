import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from copy import deepcopy
import time

start_time = time.time()

text = get_data(22, 2023)
bricks = []
lines = text.split('\n')

for i, line in enumerate(lines):
    start, end = line.split('~')
    x1, y1, z1 = start.split(',')
    x2, y2, z2 = end.split(',')
    x1, x2, y1, y2, z1, z2 = int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)

    bricks.append([])
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                bricks[-1].append((x, y, z))
    bricks[-1].append(i)

print("Calculating... (on an average pc this can take up to 1 hour for 1300 lines)")


def falling(bricks, do):
    uniqe = set()
    while True:
        fell = 0
        for i in range(len(bricks)):
            can_fall = True
            for ii in range(len(bricks)):
                if bricks[i] == bricks[ii]:
                    continue
                for j, coords in enumerate(bricks[i][:-1]):
                    x, y, z = coords
                    if  (x, y, z-1) in bricks[ii] or z <= 1:
                        can_fall = False
                        break
                if not can_fall:
                    break
            if can_fall:
                for j, coords in enumerate(bricks[i][:-1]):
                    if do:
                        x, y, z = coords
                        bricks[i][j] = (x, y, z-1)
                        uniqe.add(bricks[i][-1])
                fell += 1
               
        if not do:
            return fell

        if fell < 1:
            break

    return len(uniqe)

falling(bricks, True)

p1 = 0
p2 = 0
percentages = set()
for i, brick in enumerate(bricks):
    # log percentage
    percentage = (i+1)* 100 // len(lines)
    if (percentage % 10 == 0 and percentage not in percentages):
        print(percentage, '%', sep='')
        percentages.add(percentage)

    tmp_bricks = deepcopy(bricks)
    tmp_bricks.remove(brick)
    if falling(tmp_bricks, False) == 0:
        p1 += 1
    p2+=falling(tmp_bricks, True)

end_time = time.time()
print('Calculation time: {:.2f} ms'.format(end_time - start_time))

print(p1)
print(p2)
