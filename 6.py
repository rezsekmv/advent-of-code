FILENAME = '6.txt'
lines = []

with open(FILENAME) as f:
    lines = [l.rstrip() for l in f.readlines()]
    f.close()

#====================================================

result = 0
line = lines[0]

buffer = line[:14]


def bufferRepeating(s):
    return len(list(set(s))) != len(s)

for i in range(14, len(line)):
    print(i, line[i], buffer, line[:i-13])
    if(line[i] not in buffer and not bufferRepeating(buffer)):
        break;
    
    buffer += line[i]
    buffer = buffer[1:]
    

print(i)
