from util import *

def solve(lines):
    p1=p2=0
    for i, l in en(lines):
        # parse
        lights, *comps, DEST2 = l.split()
        DEST1 = []
        for a in list(lights[1:-1]):
            if a == '#':
                DEST1.append(True)
            else:
                DEST1.append(False)
        DEST1 = tuple(DEST1)
        BUTTONS = []
        for b in comps:
            tmp = eval(b)
            try:
                BUTTONS.append(tuple(list(tmp)))
            except:
                BUTTONS.append(tuple([tmp]))
            
        LAMPS = [False] * len(DEST1)
        DEST2 = eval(f'({DEST2[1:-1]})')
        # ===========


        # part1
        DP = defaultdict(lambda: math.inf)
        Q = deque([(0, tuple(LAMPS))]) 
        while True:
            c, state = Q.popleft()

            if state == DEST1:
                p1 += c
                break

            if DP[state] < c:
                continue
            DP[state] = c

            for button in BUTTONS:
                newstate = [*state]
                for s in button:
                    newstate[s] = not newstate[s]
                Q.append((c+1, tuple(newstate)))     


        # part2
        solver = z3.Optimize()
        _vars = []
        state_vars = [None] * len(DEST2)

        for name, button in en(BUTTONS):
            var = z3.Int(str(name))
            _vars.append(var)
            solver.add(var >= 0)
            
            for b in button:
                state_vars[b] = var if state_vars[b] is None else state_vars[b] + var

        for i, b in en(DEST2):
            if state_vars[i] is None:
                continue
            solver.add(DEST2[i] == state_vars[i])

        presses = solver.minimize(sum(_vars))
        if solver.check() == z3.sat:
            p2 += presses.value().as_long()

    return p1, p2

lines = get_data().split('\n')
p1, p2 = solve(lines)
pr(p1)
pr(p2)