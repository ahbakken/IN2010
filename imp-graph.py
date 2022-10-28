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
print_result(previous_nodes, shortest_path, start_node="a", target_node="d")
