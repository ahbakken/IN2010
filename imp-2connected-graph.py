import copy
from collections import defaultdict

#example graphs lists
v = ['a', 'b', 'c', 'd', 'e']
e = [['a', 'b', 'e'], ['b', 'c', 'e', 'a'], ['c', 'd', 'b'], ['d', 'e', 'c'], ['e', 'a', 'b', 'd']]
g = [v, e]


v2 = ['a', 'b', 'c', 'd', 'e']
e2 = [['a', 'b'], ['b', 'c'], ['c', 'a'], ['e', 'd'], ['d', 'c']]
g2 = [v, e]


#2-CONNECTED GRAPH TEST
def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        #print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return visited

def isBiConnectedNaive(graph):
    for node in graph.keys(): #iterate over list of nodes
        tempGraph = copy.deepcopy(graph)
        # remove nokkel from the graph, nodes and edges, 
        # it should not be able to visit this node
        for value in tempGraph.values(): #remove node from edges to other nodes
            if node in value:
                value.remove(node)
        tempGraph.pop(node, None) #remove key(node) from graph
        
        visited = set()
        visited = dfs(visited, tempGraph, list(tempGraph)[0])
        order = list(tempGraph.keys())
        if len(visited) != len(order):
            return False
    return True

gdict1 = {'a': ['b', 'e'], 'b': ['c', 'a', 'e'], 'c': ['b', 'd'], 'd': ['c', 'e'], 'e':['d', 'b', 'a']}

gdict2 = {'a': ['b', 'c'], 'b': ['c', 'a'], 'c': ['b', 'd'], 'd': ['c', 'e'], 'e':['d']}

# print('The graph1 is 2-connected: ', isBiConnectedNaive(gdict1))
# print('The graph2 is 2-connected: ', isBiConnectedNaive(gdict2))

# ---------------------------------------------------------------

# Finding separation nodes
def separationVertices(graph):
    s = list(graph)[0] #choosing first node
    s_edges = graph[s]
    depth[s] = 0
    low[s] = 0
    children = 0
    
    for i in range(len(s_edges)):
        if s_edges[i] not in depth:
            separationVerticesRec(graph, s_edges[i], 1)
            children += 1
    if children > 1:
        seps.add(s)
    
    return seps 

def separationVerticesRec(graph, u, d):
    depth[u] = d
    low[u] = d
    new_edges = graph[u]

    for v in new_edges:
        if v in depth:
            low[u] = min(low[u], depth[v])
            continue
        separationVerticesRec(graph, v, d+1)
        low[u] = min(low[u], low[v])
        if d <= low[v]:
            seps.add(u)

#this is 2-connected
# depth = dict()
# low = dict()
# seps = set()
# print('The graph1 separation nodes: ', separationVertices(gdict1))


#this is not 2-connected
# depth = dict()
# low = dict()
# seps = set()
# print('The graph2 separation nodes: ', separationVertices(gdict2))

#use separationVertices to test is a graph is 2-connected
def isBiConnected(graph):
    return len(separationVertices(graph)) < 1

# depth = dict()
# low = dict()
# seps = set()
# print('Graph1 is 2-connected test with separation: ', isBiConnected(gdict1))

# depth = dict()
# low = dict()
# seps = set()
# print('Graph2 is 2-connected test with separation: ', isBiConnected(gdict2))


# reverse a graph
def reverseGraph(graph):
    graph_inv = defaultdict(list)
    #make new dict that is reversed
    for node, edges in graph.items():
        for edge in edges:
            graph_inv[edge].append(node)
    #add any missing nodes
    for node in graph.keys():
        if node not in graph_inv.keys():
            graph_inv[node] = []
    #transform to common dict
    return dict(graph_inv)

#2connected graph
gdict1 = {'a': ['b', 'e'], 'b': ['c', 'a', 'e'], 'c': ['b', 'd'], 'd': ['c', 'e'], 'e':['d', 'b', 'a']}
#separation nodes
gdict2 = {'a': ['b', 'c'], 'b': ['c', 'a'], 'c': ['b', 'd'], 'd': ['c', 'e'], 'e':['d']}
#clear directed graph
gdict3 = {'a': ['b'], 'b': ['d'], 'c': ['b'], 'd': ['c', 'e'], 'e':[]}

# print(reverseGraph(gdict2))



# Graph class, might be used at some point...
# class Graph:
 
#     def __init__(self, vertices):
#         self.V = vertices  # No. of vertices
#         self.graph = defaultdict(list)  # default dictionary to store graph
 

#     # function to add an edge to graph
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)

# def addGraph(ordbok):
#     graph = Graph(len(ordbok))
#     for nokkel in ordbok.keys():
#         for node in ordbok[nokkel]:
#             graph.addEdge(nokkel, node)