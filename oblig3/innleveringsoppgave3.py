#oblig 3 IN2010

import csv
import sys
from collections import defaultdict, deque
from classes import Actor, Graph, Movie

#oppgave 1 - build the graph
print("\n--------------- OPPGAVE 1 ----------------\n")

actorList = [] #list of actors, nodes
movieList = [] #list of movies, edges

# make edges of movies, marvel_
with open('movies.tsv', encoding="utf-8") as file:
    movies = csv.reader(file, delimiter="\t")
    # printing data line by line
    for line in movies:
        movie = Movie(line[0], line[1], line[2])
        movieList.append(movie)


# open .tsv file as csv and read the file
# make nodes of actors marvel_
with open('actors.tsv', encoding="utf-8") as file:
    actors = csv.reader(file, delimiter="\t")
    for line in actors:
        actor = Actor(line[0], line[1])
        actorList.append(actor)
        i = 2
        while i < len(line): # adding movies to the actor
            actor.add_movie(line[i])
            i += 1


graph = Graph(actorList) #add nodes to graph

for movie in movieList: #add edges to graph
    m_id = movie.get_id()
    for actor1 in actorList:
        if m_id in actor1.get_movies():
            for actor2 in actorList:
                if actor1 != actor2 and m_id in actor2.get_movies():
                    graph.add_edge(actor1, actor2, movie)


print("Nodes: ", len(actorList))
print("Edges: ", len(graph.graph))

# Graph
# for i in graph.graph:
#     print(i[2].get_name(), i[0].get_name(), i[1].get_name())


#oppgave 2 - shortest path through graph
print("\n--------------- OPPGAVE 2 ----------------\n")

def printFinal_path(final_path):
    print(final_path[0][0].get_name())
    i = 1
    while i < len(final_path):
        print('=== [',final_path[i][0].get_name(), '(', final_path[i][0].get_rating(), ') ] ===> ', final_path[i][1].get_name())
        i += 1
    return


#width first search, takes actor nodes
def shortestPath(graph, start, end):
    if start == end:
        print("Same actor")
        return []
    queue = [[start]]
    visited = set()

    #loop to traverse the graph, using queue
    while queue:
        path = queue.pop(0)
        current_node = path[-1]

        #check if the node has been visited, get neighbors
        if current_node not in visited:
            #dict neighbor with actor:movie
            neighbors = graph.get_neighbors(current_node)

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == end:
                    final_path = [[start]]
                    i = 0
                    while i < len(new_path)-1:
                        for s, d, movie in graph.graph:
                            if new_path[i] == s and new_path[i+1] == d:
                                final_path.append([movie, d]) #add movie and actor to list
                        i += 1
                    #printing the path
                    printFinal_path(final_path)
                    return final_path  
            visited.add(current_node)

    print("A connecting path doesn't exist between", start.get_name() ,' and ' , end.get_name(), " :( \n")
    return

sp = (shortestPath(graph, actorList[2], actorList[4]))

#oppgave 3 - chillest path through graph
print("\n--------------- OPPGAVE 3 ----------------\n")


def chillestPath(graph, start, end):
    
    unvisited_nodes = graph.get_nodes()[:] #will not mutate graph when remove is used
    dist = dict()
    previous_nodes = dict()

    for node in unvisited_nodes:
        dist[node] = sys.maxsize
    dist[start] = 0
    
    while len(unvisited_nodes) > 0:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif dist[node] < dist[current_min_node]:
                current_min_node = node

        neighbors = graph.get_neighbors(current_min_node)
        for neighbor in neighbors:
            temp_val = dist[current_min_node] + (10 - float(neighbors[neighbor].get_rating()))
            if temp_val < dist[neighbor]:
                dist[neighbor] = temp_val
                previous_nodes[neighbor] = current_min_node
        
        unvisited_nodes.remove(current_min_node)
      
    new_path = []
    node = end
    
    while node != start:
        new_path.append(node)
        node = previous_nodes[node]
 
    new_path.append(start)
    new_path.reverse()

    
    final_path = [[start]]
    i = 0
    totalW = 0
    while i < len(new_path)-1:
        for s, d, movie in graph.graph:
            if new_path[i] == s and new_path[i+1] == d:
                final_path.append([movie, d]) #add movie and actor to list
                totalW += (10-float(movie.get_rating()))
        i += 1
    #printing the path
    printFinal_path(final_path)
    print('Total weight:', round(totalW, 1))
    return dist


sp = (chillestPath(graph, actorList[2], actorList[4]))

#oppgave 4 - connected components
print("\n--------------- OPPGAVE 4 ----------------\n")

def findAllComponents(graph):
    #get make graph with neighbours
    dictGraph = defaultdict(set)
    for actor in graph.get_nodes():
        dictGraph[actor] = graph.get_neighbor_actors(actor)
    
    seen = set()
    result = []
    for node in dictGraph:
        if node not in seen:
            connected, seen = findComponents(node, seen, dictGraph)
            result.append(connected)
    return result


def findComponents(node, seen, dictGraph):
        result = []
        nodes = set([node])
        while nodes:
            node = nodes.pop()
            seen.add(node)
            nodes = nodes or dictGraph[node] - seen
            result.append(node)
        return result, seen

def sizeOfComponents(graph):
    components = findAllComponents(graph)
    lenCounter = []
    for component in components:
        lenCounter.append(len(component))
    
    repComp = dict((i, lenCounter.count(i)) for i in lenCounter)
    for i in repComp:
        print('There are', repComp[i], 'components of size', i)

sizeOfComponents(graph)
print('\n')