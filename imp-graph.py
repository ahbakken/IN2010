#graphs, traversal, topological sorting
#G = (V, E), 
#   V is set with nodes 
#   E is set with edges (node pairs that are connected)

#Depth first search, 
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
# print("\n---------------START Breadth-first----------------\n")

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
    #print('visited F',visited, '\n')
    
        
wfsFull(g)

def indegree(dict, key):
    deg = 0
    for v in dict:
        if key in dict.get(v):
            deg+=1
    return deg

#topological sorting, use dictionary for V (keyes) and E *(values)
def topSort(graphDict):
    tempDict = graphDict #Temp-graph used for sorting
    stack = []
    output = [] #list of ordered nodes
    for v in tempDict: #the nodes (is the keys)
        if indegree(tempDict, v) == 0: #check how many keyes have list key in their value (list of nodes they connect to)
            stack.append(v) #push v onto the stack
    while len(stack)>0:
        u = stack.pop() #remove from the stack
        output.append(u)
        if u in tempDict:
            tempDict.pop(u)
        for uv in tempDict:
            if u in tempDict.get(uv): #remove u from the value list in dict
                tempVal = tempDict.get(uv) #hold the list of edges (value) for this key
                tempVal.remove(u) #removes the edge/connection
                tempDict[uv] = tempVal #updates the value in the Temp-graph
            if indegree(tempDict, uv) == 0:
                stack.append(uv)
        # print('OUTPUT LIST', output)
        # print('temp graph dict', tempDict)
    if len(output)<len(graphDict):
        print('Error: Graph contains a cycle and cannot be topologically ordered.')
    return output 

gdict = {'a': ('b', 'e'), 'b': ('c'), 'c': [], 'd': [], 'e':('d', 'b')}
# print(gdict['a'])

# print(topSort(gdict))
#topological sorting, DFS
def dfsTopSort(graph):
    stack = []
    visited = set()
    for u in graph[0]:
        if u not in visited:
            dfsVisitMod(graph, u, visited, stack)
    return stack

def dfsVisitMod(graph, u, visited, stack):
    visited.add(u)
    for uv in graph[1]:
        if uv[1] not in visited:
            dfsVisitMod(graph, uv[1], visited, stack)
    stack.append(u)

#print(dfsTopSort(g))

#Weighted graphs week 40
#G = (V, E), 
#   V is set with nodes 
#   E is set with edges (node pairs that are connected)
import math

v = {'a', 'b', 'c', 'd', 'e'}
e = {('a', 'b'), ('b', 'c'), ('c', 'a'), ('e', 'd'), ('a', 'c')}
g = [v, e]


def dijkstras(G, s):
    dist = {}
    queue = []
    nodes = G[1]
    edges = G[2]
    for v in nodes:
        dist[v] = math.inf
        queue.append(v)
    dist[s] = 0
    for value in dist.keyes:
        
    #decrease prioroty queue (?)
    #sort it after priority?
    #from high to low, pop to remove priority

    while queue.len() > 0:
        u = queue.pop
        for e in edges:
            c = dist[e[0]] + weight(e[0], e[0])

kart = dijkstras(g, v[0])