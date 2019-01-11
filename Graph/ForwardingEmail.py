from collections import defaultdict
import re
import numpy as np
a=[]
nodes=[]
connections =[]

T =int (input())
if T >20 :
    exit(0)
for x in range(T):
    b = int (input())
    if b>5000:
        exit(0)
    nodes.append(b)
    for i in range(b):
        c=input()
        first=int(re.split('\s+', c)[0])
        second =int(re.split('\s+', c)[1])
        a.append((first,second))
    connections.append(a)
    a=[]
    
class Graph(object):
    def __init__(self, connections):
        self._graph = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self._graph[node1].add(node2)
        return node1 in self._graph and node2 in self._graph[node1]

def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    size=np.size(path)
    return size

for h in range(T):
    g = Graph(connections[h])
    for k in range(nodes[h]+1):
        a.append(dfs_iterative(g._graph, k+1))
    print('Case '+str(h+1)+': '+str(np.argmax(a)+1))
    a=[]
