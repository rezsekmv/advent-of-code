from util import *

lines = get_data().split('\n')

sa = 0
sc = 0
saa = 0
for line in lines:
    sa += len(line)
    sc += len(eval(line))

    escape = line.count('\\') + line[1:-1].count('\\"') + 4
    saa += len(line) + escape

pr(sa-sc)
pr(saa-sa)
