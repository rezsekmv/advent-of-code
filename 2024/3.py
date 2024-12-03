from input_data import get_data
import re

data = get_data(3)

p1 = 0
p2 = 0

def getNumbers(str):
    return [int(num) for num in re.findall(r'-?\d+', str)]

res = re.findall("(mul\((\d*)\,(\d*)\))+|(don\'t\(\))+|(do\(\))+", data)
print(res)
c=True
for i in res:
    for j in i:
        if j.startswith('mul('):
            x,y = getNumbers(j)
            p1+=x*y
            if c:
                p2+=x*y
        elif j.startswith("don't()"):
            c=False
        elif j.startswith('do()'):
            c=True

print(p1)
print(p2)

