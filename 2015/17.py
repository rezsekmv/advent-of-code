from util import *

containers = [int(l) for l in get_data().split('\n')]
goal = 150

count = 0
min_containers = len(containers)

for r in range(1, len(containers) + 1):
    for combo in it.combinations(containers, r):
        if sum(combo) == goal:
            count += 1
            min_containers = min(min_containers, r)

min_count = sum(1 for combo in it.combinations(containers, min_containers) 
                if sum(combo) == goal)

pr(count)
pr(min_count)