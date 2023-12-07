import sys
sys.path.append('../advent_of_code')
from input_data import get_data
from collections import defaultdict
from functools import cmp_to_key

text = get_data(7, 2023)
lines = text.split('\n')

data = []
for line in lines:
    hand, bid = line.split()
    data.append((hand, int(bid)))

    
def get_occurance_dict(hand):
    freq = defaultdict(int)
    for card in hand:
        freq[card] += 1
    return freq
    
def co(h1, h2, part2):
    order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    if part2:
        order.pop(3)
        order.append('J')

    for i in range(5):
        if order.index(h1[i]) < order.index(h2[i]):
            return 1
        elif order.index(h2[i]) < order.index(h1[i]):
            return -1
        
    return 0 


def compare(d1, d2, part2=False):
    dict1 = get_occurance_dict(d1[0])
    dict2 = get_occurance_dict(d2[0])
    if part2:
        if dict1['J']:            
            j = dict1['J']
            del dict1['J']
            if dict1:
                dict1[max(dict1, key=dict1.get)] += j
            else:
                dict1['J'] = 5
        else:
            del dict1['J']


        if dict2['J']:
            j = dict2['J']
            del dict2['J']
            if dict2:
                dict2[max(dict2, key=dict2.get)] += j
            else:
                dict2['J'] = 5
        else:
            del dict2['J']


    srted1 = sorted(dict1.values(), reverse=True)
    srted2 = sorted(dict2.values(), reverse=True)

    if srted1 < srted2:
        return -1
    elif srted2 < srted1:
        return 1
    else:
        return co(d1[0], d2[0], part2)
        

p1s = sorted(data, key=cmp_to_key(lambda d1,d2: compare(d1, d2)))
p2s = sorted(data, key=cmp_to_key(lambda d1,d2: compare(d1, d2, True)))

p1 = 0
for i, d in enumerate(p1s):
    p1 += (i+1)*d[1]

p2 = 0
for i, d in enumerate(p2s):
    p2 += (i+1)*d[1]

print(p1)
print(p2)
