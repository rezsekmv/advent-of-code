FILENAME = '5.txt'
lines = []

with open(FILENAME) as f:
    lines = [l.rstrip() for l in f.readlines()]
    f.close()

#====================================================


result = ''

stacks = []
stackCount = 0

for i in range(len(lines)):
    if lines[i] == '':
        stackCount = i;
        break;

for i in range(stackCount):
    stacks.append('')

for line in lines:
    for i in range(len(line)):
        if line[i] == '[':
            stacks[i//4] = line[i+1] + stacks[i//4]

    if line == '':
        break;

print(stacks[0:3])
for i in range(stackCount+1, len(lines)):
    line = lines[i]
    t = line.split(' ')

    cou = int(t[1])
    fro = int(t[3])-1
    to =  int(t[5])-1

    tmp = stacks[fro][-cou:]
    stacks[fro] = stacks[fro][:-cou]
    stacks[to] = stacks[to] + tmp

for s in stacks:
    if s != '':
        print(s[-1], end='')
    else:
        print('', end='')
    