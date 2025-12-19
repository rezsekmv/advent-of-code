from util import *
import itertools

lines = get_data().splitlines()

D = defaultdict(dict)
for line in lines:
	words = line.split()
	mul = -1 if words[2] == 'lose' else 1
	D[words[0]][words[10][:-1]] = mul * int(words[3])


def calc(arr):
	ans = 0
	for i in range(len(arr)):
		ans += D[arr[i]][arr[(i+1)%len(arr)]]
		ans += D[arr[(i+1)%len(arr)]][arr[i]]
	return ans

perms = list(itertools.permutations(D.keys()))
for arr in perms:
	ans = calc(arr)
	p1 = max(p1, ans)

pr(p1)

D['me'] = defaultdict(int)
for k in D.keys():
	D['me'][k] = 0
	D[k]['me'] = 0

perms = list(itertools.permutations(D.keys()))
for arr in perms:
	ans = calc(arr)
	p2 = max(p2, ans)

pr(p2)