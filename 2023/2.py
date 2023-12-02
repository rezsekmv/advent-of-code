import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from util import *

text = get_data(2, 2023)
data = text.split('\n')

powers = []
possible = []

colors = ['red', 'green', 'blue']
limit = [12, 13, 14]
for d in data:
    p = d.split(':')
    id = getNumbers(p[0])[0]
    turn = p[1].split(';')
    
    biggest = [0,0,0]
    inpossible = False
    for t in turn:
        for i in range(3):
            num = getFirstRegexp(getFirstRegexp(t, f'\d+ {colors[i]}'), '\d+')
            num = int(num) if num != '' else 0
            
            if num > limit[i]:
                inpossible = True
            if num > biggest[i]:
                biggest[i] = num
    
    if not inpossible:
        possible.append(id)
    powers.append(biggest[0]*biggest[1]*biggest[2])

print(sum(possible))
print(sum(powers))