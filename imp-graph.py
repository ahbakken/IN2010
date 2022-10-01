#graphs, traversal, topological sorting
#Depth first search, 
#G = (V, E), 
#   V is set with nodes 
#   E is set with edges (node pairs that are connected)
#Recursive

#visit
def dfsVisit(graph, start, visited):
    visited.add(start)
    for v in graph[1]:
        if v[1] not in visited:
            dfsVisit(graph, v[1], visited)
#full
def dfsFull(graph):
    visited = set()
    for v in graph[0]:
        if v[0] not in visited:
            dfsVisit(graph, v[0], visited)

print("\n---------------START RECURSTION----------------\n")

v = {'a', 'b', 'c', 'd', 'e'}
e = {('a', 'b'), ('b', 'c'), ('c', 'a'), ('e', 'd')}
g = [v, e]

dfsFull(g)

print("\n---------------START ITERATIVE----------------\n")
#Iterative
#visit
def dfsVisitIT(graph, start, visited):
    stack = [start]
    while len(stack)>0:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            for e in graph[1]:
                stack.append(e[1]) #push

#full
def dfsFullIT(graph):
    visited = set()
    for v in graph[0]:
        if v[0] not in visited:
            dfsVisitIT(graph, v[0], visited)

dfsFullIT(g)