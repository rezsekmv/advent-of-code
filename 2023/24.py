import sys
sys.path.append('../advent_of_code')
from input_data import get_data
# import numpy as np

text = get_data(24, 2023)
lines = text.split('\n')

border = (200000000000000, 400000000000000)

stones = []
for line in lines:
    pos, vel = line.split('@')
    x, y, z = [int(a.strip()) for a in pos.split(',')]
    vx, vy, vz = [int(a.strip()) for a in vel.split(',')]
    stones.append(((x,y,z), (vx,vy,vz)))

# dx = 0
# for i in range(len(stones)-1):
#     pos, v = stones[i]
#     r = np.array([v[0], v[1]])
#     p = np.array([pos[0], pos[1]])
    
#     for j in range(i+1, len(stones)):
#         pos2, y = stones[j]
#         solver = np.array([y[0], y[1]])
#         q = np.array([pos2[0], pos2[1]])
#         if (pos, v) == (pos2, y):
#             continue
        
#         # algo from: https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
#         rxs = np.cross(r, solver)
#         qpxr = np.cross((q-p), r)
#         _1 = rxs == 0 and qpxr == 0 # collinear
#         _2 = rxs == 0 and qpxr != 0 # parallel
#         if _1 or _2:
#             continue

#         t = np.cross((q-p), solver) / rxs
#         u = np.cross((q-p), r) / rxs
#         # print('t:', t, '\t', 'u:', u)
        
#         cross_point = p + t*r
#         if 0<t and 0<u:
#             if border[0] < cross_point[0] < border[1] and border[0] < cross_point[1] < border[1]:
#                 dx += 1

# print(dx)


# ========== PART2 ===========
# solved with z3 equation solver

from z3 import Solver, IntVector

S = len(stones)
x, y, z , v_xv, v_yv, v_zv = IntVector('var', 6)
ts = IntVector('t', S)
solver = Solver()
for i in range(len(stones[:5])):
    ((x0,y0,z0), (xv, yv, zv)) =  stones[i]
    t = ts[i]
    solver.add(x + t * v_xv - (x0 + t * xv) == 0)
    solver.add(y + t * v_yv - (y0 + t * yv) == 0)
    solver.add(z + t * v_zv - (z0 + t * zv) == 0)


stat = solver.check()
model = solver.model()
print(model)
print(model.eval(x+y+z))
