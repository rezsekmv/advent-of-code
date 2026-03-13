from util import *

A = [getNumbers(l) for l in get_data().split('\n')]
n = len(A)

def combinations(remaining, idx, amounts):
    if idx == n - 1:
        amounts[idx] = remaining
        yield amounts[:]
    else:
        for v in range(remaining + 1):
            amounts[idx] = v
            yield from combinations(remaining - v, idx + 1, amounts)

for part in [False, True]:
    best = 0
    for combo in combinations(100, 0, [0] * n):
        if part and sum(A[i][4] * combo[i] for i in range(n)) != 500:
            continue
        score = 1
        for j in range(4):
            score *= max(0, sum(A[i][j] * combo[i] for i in range(n)))
        best = max(best, score)
    pr(best)
