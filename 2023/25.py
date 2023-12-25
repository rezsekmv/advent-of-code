import sys
sys.path.append('../advent_of_code')
from input_data import get_data
import networkx as nx

text = get_data(25, 2023)
components = set()
G = nx.DiGraph()
for line in text.split('\n'):
    key, rest = line.split(':')
    conns = rest.strip().split(' ')
    components.add(key)
    for conn in conns:
        G.add_edge(key, conn, capacity=1)
        G.add_edge(conn, key, capacity=1)
        components.add(conn)
    
ans = 0
left = list(components)[0]
for right in list(components)[1:]:
    # minimum_cut calculates the possible cuts to separate 'left' and 'right'
    cut_value, (left_part, right_part) = nx.minimum_cut(G, left, right)
    # we are searching for 3 cuts
    if cut_value == 3:
        ans = len(left_part) * len(right_part)
        break
            
print(ans)

