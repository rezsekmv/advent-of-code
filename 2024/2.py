from input_data import get_data
from copy import deepcopy

data = get_data(2).split('\n')

p1 = 0
p2 = 0

def calc(A):
    prev = A[0]
    DEC = A[0] > A[1]
    INC = A[0] < A[1]

    for j in A[1:]:
            b = abs(int(j)-int(prev))
            if not (1 <= b <= 3):
                return False
            if DEC and int(prev) <= int(j):
                return False
            if INC and int(prev) >= int(j):
                return False
            prev = int(j)
    return True

for row in data:
    c = False

    B = list(map(int, row.split()))
    for part2 in [False, True]:
        if part2:
            for k in range(len(B)):
                a = True
                A = B[:k] + B[k+1:]
                
                if calc(A):
                    c = True
                    break
            if c:
                p2 += 1 
        else:
            if calc(B):
                p1 += 1

print(p1)
print(p2)

