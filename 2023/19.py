import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from collections import defaultdict, deque
from copy import deepcopy

text = get_data(19, 2023)
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

def p1():
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
    intervals = deque([
        {
            'x': (1, 4000),
            'm': (1, 4000),
            'a': (1, 4000),
            's': (1, 4000),
            'state': 'in'
        }
    ])
    good_intervals = []
    while intervals:
        interval = intervals.popleft()
        for rule, dest in rules[interval['state']]:
            new_interval = deepcopy(interval)
            new_interval['state'] = dest

            if '<' in rule:
                letter, num = rule.split('<')
                num = int(num)
                new_interval[letter] = (interval[letter][0], num-1)
                interval[letter] = (num, interval[letter][1])
                if dest == 'A':
                    good_intervals.append(new_interval)
                elif not dest == 'R':
                    intervals.append(new_interval)
            elif '>' in rule:
                letter, num = rule.split('>')
                num = int(num)
                new_interval[letter] = (num+1, interval[letter][1])
                interval[letter] = (interval[letter][0], num)
                if dest == 'A':
                    good_intervals.append(new_interval)
                elif not dest == 'R':
                    intervals.append(new_interval)
            elif 'True' in rule:
                interval['state'] = dest
                if dest == 'A':
                    good_intervals.append(interval)
                elif not dest == 'R':
                    intervals.append(interval)
            else:
                assert False
    
    p2 = 0
    for gi in good_intervals:
        row = 1
        for value in list(gi.values())[:-1]:
            start, end = value
            row *= (end-start+1)
        p2 += row
    return p2 

print(p1())
print(p2())
