from my_input import lines
import math
import util
from copy import deepcopy

# init values
allNode = []
INF = 99999
graph = [[INF for i in range(len(lines))] for j in range(len(lines))]

# Valve data class
class Node:
    def __init__(self, name, rate, neighbours, idx):
        self.name = name
        self.rate = rate
        self.neighbours = neighbours
        self.idx = idx
        self.shortestPath = []

    def __eq__(self, __o: object) -> bool:
        if __o is None:
            return False
        else:
            return self.name == __o.name

    def __str__(self) -> str:
        return self.name

# read in lines
for idx, line in enumerate(lines):
    neighbours = util.getRegexp(line, regexp='[A-Z]{2}')
    rate = util.getNumbers(line, '')[0]
    name = neighbours.pop(0)
    
    va = Node(name, rate, [], idx)
    allNode.append(va)

# function to get Node object from allNode list
def getNodeByName(name):
    for node in allNode:
        if node.name == name:
            return deepcopy(node)

# add neighbour Node objects to valve objects
for i, line in enumerate(lines):
    neighbours = util.getRegexp(line, regexp='[A-Z]{2}')
    neighbours.pop(0)
    for neigh in neighbours:
        allNode[i].neighbours.append(getNodeByName(neigh))

# create steps graph init
for node in allNode:
    for neigh in node.neighbours:
        graph[node.idx][neigh.idx] = 1

# shortest path algorithym (retrun MX)
N = len(allNode)
def floydWarshall(graph): 
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


# DFS
def DFS(start, time, state, opened , result):
    result[state] = max(result.get(state, 0), opened)
    for node in allNode:
        newbudget = time - start.shortestPath[node.idx] - 1
        if newbudget <= 0:
            continue
        DFS(node, newbudget, state, opened + newbudget * node.rate, result)
    return result   

# add shortest path info to node objects
shortestPathMx = floydWarshall(graph)
for i, node in enumerate(allNode):
    node.shortestPath = shortestPathMx[i]



# brute force
bests = DFS(getNodeByName('AA'), 30, 0, 0, {}).values()
print(max(bests))
