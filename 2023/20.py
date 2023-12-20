import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from collections import deque
from math import lcm

text = get_data(20, 2023)
lines = text.split('\n')

modules = {}
rx_in = None
for line in lines:
    name, dest = line.split('->')
    name = name.strip()
    dest = dest.strip()
    dest_list = dest.split(',')
    
    if name == 'broadcaster':
        modules[name] = []
        for d in dest_list:
            modules[name].append(d.strip())
        
    if name[0] == '%':
        name = name[1:]
        modules[name] = ['flip-flop', [], 'off']
        for d in dest_list:
            modules[name][1].append(d.strip())

    if name[0] == '&':
        name = name[1:]
        d = {}
        if 'rx' in dest_list:
            rx_in = name
        for l in lines:
            src, dest = l.split('->')
            if name in dest:
                d[src.strip()[1:]] = 'low'
        modules[name] = ['conjunction', [], d]
        for d in dest_list:
            modules[name][1].append(d.strip())


low = 0
high = 0
cycle_nums = {}
to_find = list(modules[rx_in][2].keys())
n = 1
while len(cycle_nums) < 4:
    signals = deque([('button', 'low', 'broadcaster')])
    low += 1
    while signals:
        src, t, dest = signals.popleft()
        
        if dest not in modules:
            continue
        
        if src in to_find and t == 'high' and src not in cycle_nums:
            cycle_nums[src] = n
        
        module = modules[dest]
        if dest == 'broadcaster':
            for m in module:
                signals.append((dest, t, m))
                low += 1
            
        elif module[0] == 'flip-flop' and t == 'low':
            if module[2] == 'off':
                module[2] = 'on'
                for m in module[1]:
                    signals.append((dest, 'high', m))
                    high += 1

            elif module[2] == 'on':
                module[2] = 'off'
                for m in module[1]:
                    signals.append((dest, 'low', m))
                    low += 1

        elif module[0] == 'conjunction':
            module[2][src] = t
            if all([v == 'high' for v in module[2].values()]):
                for m in module[1]:
                    signals.append((dest, 'low', m))
                    low += 1
            else:
                for m in module[1]:
                    signals.append((dest, 'high', m))
                    high += 1
    
    if n == 1000:
        print(low * high)
    n += 1

print(lcm(*cycle_nums.values()))

