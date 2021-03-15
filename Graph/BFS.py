# BFS algorithm
# concept : visit a node and explore

from collections import *
graph = defaultdict(list)
def addEdge(graph,key,value):
    graph[key].append(value)


def bfs(graph, start):
    explored = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in explored:   #if node value is not in explored list
            explored.append(node)  #then add it to the explored
            value_list = graph[node]
            for adjacent in value_list:
                queue.append(adjacent)
    return explored

#main 
for i in range(int(input("enter total Nodes: "))):
    vertex = list(map(int,input('enter a value').split()))
    addEdge(graph,vertex[0],vertex[1])

print(graph)
print('Breadth first search: ',bfs(graph,2))


