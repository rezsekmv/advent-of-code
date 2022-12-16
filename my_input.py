import sys

FILENAME = sys.argv[0].split('/')[-1].replace('.py', '') + '.in'
lines = []

with open(FILENAME) as f:
    lines = [l.rstrip() for l in f.readlines()]
    f.close()



