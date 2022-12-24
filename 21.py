from my_input import lines
import util
import math

d = dict()
s = dict()

for line in reversed(lines):
    words = line.split(':')
    if len(line) < 11:
        d[words[0]] = int(words[1].strip())
    else:
        a = words[1].strip().split()
        a[0] = 'd[\'' +a[0] + '\']'
        if a[1] == '\\':
            a[1] = '\\\\'
        if words[0] == 'root':
            a[1] = '-'
        a[2] = 'd[\'' +a[2] + '\']'
        s[words[0]] = ''.join(a)
        d[words[0]] = float('-inf')

from copy import deepcopy

for i in range(10000):
    cp = deepcopy(d)
    cp['humn'] = i
    run = True
    while run:
        for k,v in s.items():
            if cp['root'] != float('-inf'):
                run = False
                break
            dep = util.getRegexp(v, regexp='[a-z]{4}')
            if cp[dep[0]] != float('-inf') and cp[dep[1]] != float('-inf'):
                cp[k] = eval(v)
                print(cp[k])
    if cp['root'] == 0:
        break

print(d['humn'])