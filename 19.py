from my_input import lines
import util
import math
from copy import deepcopy
import collections
import datetime


def addDicts(dicts):
    counter = collections.Counter()
    for d in dicts: 
        counter.update(d)
        
    return dict(counter)

def affordable(pack, cost):
    for m in cost:
        if pack[m] < -cost[m] :
            return False
    return True

class Blueprint:

    def __init__(self, id, ore, clay, obsidian, geode) -> None:
        self.id = id
        self.cost = {
            'ore': ore,
            'clay': clay,
            'obsidian': obsidian,
            'geode': geode
        }
        self.largest = 0
        self.robots = {
            'ore': 1,
            'clay': 0,
            'obsidian': 0,
            'geode': 0
        }
        self.pack = {
            'ore': 0,
            'clay': 0,
            'obsidian': 0,
            'geode': 0
        }
        self.time = 0

    def qualitylvl(self):
        return self.id * self.pack['geode']

    def build(self, type):
        self.pack = addDicts( [self.cost[type], self.pack] )
        self.robots[type] += 1

    def __str__(self):
        return 'id: ' + str(self.id) + ' robots: ' + str(self.robots) + ' pack: ' + str(self.pack) + ' time: ' + str(self.time)

    def __eq__(self, __o: object) -> bool:
        return self.pack == __o.pack and self.time == __o.time and self.robots == __o.robots

B = []
for line in lines:
    words = line.strip().split()
    id = int(words[1][:-1])
    ore = {
        'ore': -int(words[6]),
        'clay': 0,
        'obsidian': 0
    }
    clay ={
        'ore': -int(words[12]),
        'clay': 0,
        'obsidian': 0
    }
    obsidian = {
        'ore': -int(words[18]),
        'clay': -int(words[21]),
        'obsidian': 0
    }
    geode = {
        'ore': -int(words[27]),
        'clay': 0,
        'obsidian': -int(words[30])
    }

    b = Blueprint(id, ore, clay, obsidian, geode)    
    B.append(b)

def harvest(robots, pack):
    pack['ore'] += robots['ore']
    pack['clay'] += robots['clay']
    pack['obsidian'] += robots['obsidian']
    pack['geode'] += robots['geode']

def eliminate(q, toElim):
    for state in q:
        if state.robots == toElim.robots and state.time <= toElim.time:
            if all([v >= toElim.pack[k] for k,v in state.pack.items()]):
                return True
    return False

materials = ['ore', 'clay', 'obsidian', 'geode']
largests = [None for _ in range(len(B))]
cache = []
def solve(bl):
    best = 0
    queue = [bl]
    while len(queue) > 0:
        state = queue.pop(0)
        if len(cache) % 1_000 == 0:
            print(state.time, len(cache))
        if state in cache:
            continue
        cache.append(deepcopy(state))
        best = max(best, state.pack['geode'])
        if state.time == 24:
            continue
        
        # opt
        # maxOreR = max(state.cost.values())
        # if state.robots['ore'] > maxOreR:
        #     state.robots['ore'] = maxOreR


        # do nothing
        cp = deepcopy(state)
        harvest(cp.robots, cp.pack)
        cp.time += 1
        queue.append(cp)

        for robot in reversed(materials):
            if affordable(cp.pack, cp.cost[robot]):
                cp = deepcopy(state)
                harvest(cp.robots, cp.pack)
                cp.build(robot)
                cp.time += 1
                queue.append(cp)

    return best

bests = []
bests.append(solve(B[0]))
ans = 0
# 9 12  
print(bests)
for i, be in enumerate(bests):
    print(be)
    ans += be*(i+1)
# 33 1550  18630
print(ans)