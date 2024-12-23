from util import *

C=[]
D=set()
for row in get_data().split('\n'):
    a,b = row.split('-')
    C.append((a,b))
    D.add(a)
    D.add(b)

G = nx.Graph()
G.add_nodes_from(D)
G.add_edges_from(C)
m=[]
for s in nx.enumerate_all_cliques(G):
    if len(s) == 3:
        for a in s:
            if a.startswith('t'):
                p1+=1
                break
    if len(s) > len(m):
        m=s

pr(p1)
m.sort()
pr(','.join(m))