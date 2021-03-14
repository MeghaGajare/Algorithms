# create graph
from collections import *

#this method is not needed 
def create_graph(graph):
    edges = []
    for left_end in graph:
        for right_end in graph[key]:
            edges.append((left_end,right_end))
    return edges




# this method is important
# this edges will add to the graph
def addEdge(graph, key, value):
    graph[key].append(value)


graph = defaultdict(list)
for i in range(int(input('enter a value: '))):
    v = list(map(str,input().split()))
    addEdge(graph, v[0], v[1])
    
print(graph)
