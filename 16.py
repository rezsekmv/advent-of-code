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
def DFS(start, visited, maxx = 30):
    if maxx < 1:
        return 

    visited.append(start)

    for neighbour in start.neighbours:
        if neighbour not in visited:
            DFS(neighbour, visited, maxx-1)


# add shortest path info to node objects
shortestPathMx = floydWarshall(graph)
for i, node in enumerate(allNode):
    node.shortestPath = shortestPathMx[i]



# brute force
limit = 30
opened = []

# sort the nodes
# go trought sort order
# node value = limit-steps-1

while True:
    for time in range(limit+1):








# imitate time
ans = 0

print(ans)
