import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from collections import defaultdict
import math

text = get_data(19, 2023, True)
rules_in, parts_in = text.split('\n\n')

# parse input
parts = []
for pa in parts_in.split('\n'):
    part = pa[1:-1].split(',')
    for i, p in enumerate(part):
        part[i] = p.split('=')[1]
    part.append('in')
    parts.append(part)

rules = defaultdict(list)
for r in rules_in.split('\n'):
    state, rest = r[:-1].split('{')
    ru = rest.split(',')
    rule = []
    for rr in ru:
        parsed = rr.split(':')
        if len(parsed) == 1:
            parsed = ['True', parsed[0]]
        rule.append(parsed)
    rules[state] = rule

def p1()
    while not all([p[-1]=='A' or p[-1]=='R' for p in parts]):
        for part in parts:
            x=int(part[0])
            m=int(part[1])
            a=int(part[2])
            s=int(part[3])
            
            if part[-1] == 'R' or part[-1] == 'A':
                continue

            for rule, dest in rules[part[-1]]:
                if eval(rule):
                    part[-1] = dest            
                    break

    ans = 0
    for part in parts:
        if part[-1] == 'A':
            for p in part[:-1]:
                ans += int(p)
    return ans

def p2():
    for key, values in rules.items():
        for v in values:
            if v[1] == 'A':
                print(v)
    return 0

print(p1())
print(p2())