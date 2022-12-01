FILENAME = '1.txt'
result = [0, 0, 0]
line = 0
summary = 0

with open(FILENAME) as f:
    lines = [l.rstrip() for l in f.readlines()]
    
    for line in lines: 
        if line == '':
            if summary > min(result):
                result.append(summary)
                result.pop(result.index(min(result)))
            summary = 0
        else:
            summary += int(line.strip())

print(sum(result))