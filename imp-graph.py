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

#print("\n---------------START RECURSTION----------------\n")

v = {'a', 'b', 'c', 'd', 'e'}
e = {('a', 'b'), ('b', 'c'), ('c', 'a'), ('e', 'd'), ('a', 'c')}
g = [v, e]

dfsFull(g)

#print("\n---------------START ITERATIVE----------------\n")
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

#Breadth-first search
print("\n---------------START Breadth-first----------------\n")

def wfsVisit(graph, start, visited):
    queue = [start]
    visited.add(start) #visits the start node first, should be added????
    while len(queue)>0:
        u = queue.pop(0) #dequeue, remove from start of list, index 0
        for uv in graph[1]: #iterating through all the edges
            if uv[0] == u and uv[1] not in visited:
                visited.add(uv[1])
                queue.append(uv[1]) #enqueue, add to end of list
        

def wfsFull(graph):
    visited = set()
    for node in graph[0]:
        if node not in visited:
            wfsVisit(graph, node, visited)
    print('visited F',visited, '\n')
    
        
wfsFull(g)


