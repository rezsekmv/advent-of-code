from util import *

lines = get_data().split('\n')

G = {}
for i,l in en(lines):
    words = l.split()
    
    src = words[0][:-1]
    dests = words[1:]

    G[src] = dests

def part1(curr):
    if curr == 'out':
        return 1

    S = 0
    for g in G[curr]:
        S += part1(g)
    return S

@functools.cache
def part2(curr, dac, fft):
    if curr == 'out':
        return 1 if dac and fft else 0
    
    if curr == 'dac':
        dac = True

    if curr == 'fft':
        fft = True

    S = 0
    for g in G[curr]:
        S += part2(g, dac, fft)
    return S

pr(part1('you'))
pr(part2('svr', False, False))