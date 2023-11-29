from my_input import lines
from copy import deepcopy

numbers = []
null = 0
for i, line in enumerate(lines):
    el = (i, int(line))
    numbers.append(el)
    if el[1] == 0:
        null = el


def move(array, n):
    newIndex = array.index(n) + n[1]
    array.remove(n)
    length = len(array)
    
    if newIndex > length:
        newIndex = newIndex%length
    
    if newIndex == 0:
        newIndex = length

    array.insert(newIndex, n)

def mix():
    # print(numbers)
    for i in range(len(numbers)):
        for n in numbers:
            if n[0] == i:
                move(numbers, n)
                # print(numbers)
                break
                
mix()
nullI = numbers.index(null)

ans = numbers[(nullI+1000)%len(numbers)][1] + numbers[(nullI+2000)%len(numbers)][1] + numbers[(nullI+3000)%len(numbers)][1]
print(numbers[(nullI+1000)%len(numbers)], numbers[(nullI+2000)%len(numbers)], numbers[(nullI+3000)%len(numbers)])
print(ans)