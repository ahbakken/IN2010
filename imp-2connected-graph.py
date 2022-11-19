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

print('The graph1 is 2-connected: ', isBiConnectedNaive(gdict1))
print('The graph2 is 2-connected: ', isBiConnectedNaive(gdict2))




class Graph:
    count = 0
 
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.Time = 0
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

def addGraph(ordbok):
    graph = Graph(len(ordbok))
    for nokkel in ordbok.keys():
        for node in ordbok[nokkel]:
            graph.addEdge(nokkel, node)


# Finding separation nodes
