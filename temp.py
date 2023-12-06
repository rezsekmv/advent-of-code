import sys
sys.path.append('../advent_of_code')
from input_data import get_data
import util
import math
from collections import deque, defaultdict

text = get_data(1, 2023)
data = text.split('\n')

for d in data:
    print(d)
