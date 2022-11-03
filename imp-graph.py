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


#makes graphs 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}

        #update() inserts specified items into the dictionary
        graph.update(init_graph)

        for node, edges in graph.items():
            for adjecent_node, value in edges.items():
                if graph[adjecent_node].get(node, False) == False:
                    graph[adjecent_node][node] = value
        return graph
    
    def get_nodes(self):
        # "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        # "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        # "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

    
#Weighted graphs week 40
#G = (V, E), 
#   V is set with nodes 
#   E is set with edges (node pairs that are connected)

from genericpath import exists
from math import dist
import sys

def dijkstras(G, s):
    unvisited_nodes = list(G.get_nodes())
    dist = {}
    previous_nodes= {}

    for v in unvisited_nodes:
        dist[v] = sys.maxsize
    dist[s] = 0

    while len(unvisited_nodes) > 0:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif dist[node] < dist[current_min_node]:
                current_min_node = node

        edges = G.get_outgoing_edges(current_min_node)
        for e in edges:
            temp_val = dist[current_min_node] + G.value(current_min_node, e)
            if temp_val < dist[e]:
                dist[e] = temp_val
                previous_nodes[e] = current_min_node
        
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, dist
   
def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))

v = ['a', 'b', 'c', 'd', 'e']

init_graph = {}
for node in v:
    init_graph[node] = {}

init_graph['a']['b'] = 3
init_graph['a']['c'] = 6
init_graph['c']['a'] = 4
init_graph['b']['e'] = 2
init_graph['e']['d'] = 1

graph = Graph(v, init_graph) 

kart = dijkstras(graph, 'a')
previous_nodes, shortest_path = kart
# print_result(previous_nodes, shortest_path, start_node="a", target_node="d")

# print(kart[1])

#G = (V, E), 
#   V is set with nodes 
#   E is set with edges (node pairs that are connected)
#graph for bellman ford
class Graph_BellmanFord:
    def __init__(self, nodes):
        self.nodes = nodes # Total number of vertices in the graph
        self.graph = []
        
    def add_edge(self, s, d, w): #start,  destination, weight
        self.graph.append([s, d, w])

    def bellman_ford(self, start):
        dist = dict()
        for node in self.nodes:
            dist[node] = float("Inf")
        dist[start] = 0

        for _ in range(len(self.graph)-1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("error: Negative cycle exists")
                return
        
        return dist


#bellman-ford algorithm for shortest path
# knows when a cycle is negative

nodes = ['a', 'b', 'c', 'd', 'e']

graph_bell = Graph_BellmanFord(nodes) 

graph_bell.add_edge('a', 'b', 3)
graph_bell.add_edge('a', 'c', 6)
graph_bell.add_edge('c', 'a', 4)
graph_bell.add_edge('b', 'e', 2)
graph_bell.add_edge('e', 'd', 1)

# shortest_path = graph_bell.bellman_ford('a')
# print(shortest_path)
    

#G = (V, E), 
#   V is set with nodes 
#   E is set with edges (node pairs that are connected)
#   When G is a directed acyclic graph (DAG)


#Python program to print topological sorting of a DAG
# https://www.geeksforgeeks.org/python-program-for-topological-sorting/
from collections import defaultdict
 
#Class to represent a graph
class GraphTop:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = vertices #No. of vertices
        self.edges = []

    def addEdgeList(self, edges):
        self.edges = edges
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dag(self, weight, start):
        if len(weight) == len(self.graph):
            dist = dict()
            sortList = self.topologicalSort()
            for u in range(len(sortList)):
                    dist[u] = float("Inf")
            dist[start] = 0

            for _ in sortList:
                for u, v, w in self.edges:
                    tempHold = dist[u] + w
                    if tempHold < dist[v]:
                        dist[v] = tempHold
        return dist
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self,v,visited,stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
 
        # Push current vertex to stack which stores result
        stack.insert(0,v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack =[]
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
 
        # Print contents of stack
        return stack
 
g= GraphTop(6)


edges = [(5, 2, 3), (5, 0, 4), (4, 0, 2), (4, 1, 6), (2, 3, 3),(3, 1, 3)]

for edge in edges:
    g.addEdge(edge[0], edge[1])
 
g.addEdgeList(edges)

g.topologicalSort()
weight = [2, 5, -2, 4, -5 ,-2]
# print(g.dag(weight, 4))

# Prims algoritm for minimal spanning trees
# https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
# The program is for adjacency matrix representation of the graph

class PrimGraph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = [[0 for column in range(num_nodes)]
                      for row in range(num_nodes)]
        
    def add_edge(self, node1, node2, weight):
        self.graph[node1][node2] = weight
        self.graph[node2][node1] = weight


    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.num_nodes):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initialize min value
        min = sys.maxsize
 
        for v in range(self.num_nodes):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index 
    
    
    def prim(self):
        queue = [sys.maxsize] * self.num_nodes
        parent = [None] * self.num_nodes
        
        queue[0] = 0
        treeSet = [False] * self.num_nodes

        parent[0] = -1 #set the root of the tree

        for i in range(self.num_nodes):
            u = self.minKey(queue, treeSet)
            treeSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.num_nodes):
 
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and treeSet[v] == False and queue[v] > self.graph[u][v]:
                    queue[v] = self.graph[u][v]
                    parent[v] = u
        
        return parent



example_graph = PrimGraph(9)

example_graph.graph = [ [0, 4, 7, 0, 0, 0, 0, 0, 0],
                        [4, 0, 11, 9, 0, 20, 0, 0, 0],
                        [7, 11, 0, 0, 0, 1, 0, 0, 0],
                        [0, 9, 0, 0, 2, 0, 6, 0, 0],
                        [0, 0, 0, 2, 0, 1, 10, 5, 15],
                        [0, 20, 1, 0, 1, 0, 0, 3, 0],
                        [0, 0, 0, 6, 10, 0, 0, 0, 5],
                        [0, 0, 0, 0, 5, 3, 0, 0, 12],
                        [0, 0, 0, 0, 15, 0, 5, 12, 0] ]

p = example_graph.prim()
example_graph.printMST(p)
