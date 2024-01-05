import sys
sys.path.append('../advent_of_code')
from input_data import get_data

lines = get_data(3, 2021).split('\n')

lenght = len(lines[0])
gamma = ''
epsilon = ''

for col in range(lenght):
    count = [0, 0]
    for line in lines: 
        if line[col] == '0':
            count[0] += 1
        elif line[col] == '1':
            count[1] += 1
    
    if count[0] > count[1]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))