import sys
sys.path.append('../advent_of_code')
from fetch_data import fetch_data
import math
from collections import deque

day = sys.argv[0].split('/')[-1].replace('.py', '')
data = fetch_data(day)

print(data)