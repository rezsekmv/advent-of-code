import sys
sys.path.append('../advent_of_code')
from input_data import get_data

fw = 0
depth = 0
aim = 0
for line in get_data(2, 2021).split('\n'):
    direction, step = line.split()
    step = int(step)
    
    match direction:
        case 'forward':
            fw += step
            depth += aim*step
        case 'down':
            aim += step
        case 'up':
            aim -= step

print(fw * aim)
print(fw * depth)