#oblig 3 IN2010
# task 1 build the graph
import csv

class Actor:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.movies = list()

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_id(self):
        return self.id

    def get_movies(self):
        return self.movies

    def get_name(self):
        return self.name

class Movie:
    def __init__(self, id, name, rating):
        self.id = id
        self.name = name
        self.rating = rating

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_rating(self):
        return self.rating

actorList = [] #list of actors, nodes
movieList = [] #list of movies

# make edges of movies, marvel_
with open('marvel_movies.tsv', encoding="utf-8") as file:
    movies = csv.reader(file, delimiter="\t")
    #tall  = 0
    # printing data line by line
    for line in movies:
        movie = Movie(line[0], line[1], line[2])
        movieList.append(movie)
        #tall+= 1
        #print('movie: ',tall)

# open .tsv file as csv and read the file
# make nodes of actors marvel_
with open('marvel_actors.tsv', encoding="utf-8") as file:
    actors = csv.reader(file, delimiter="\t")
     
    # printing data line by line
    #tall  = 1
    for line in actors:
        actor = Actor(line[0], line[1])
        actorList.append(actor)
        i = 2
        while i < len(line): # adding movies to the actor
            actor.add_movie(line[i])
            #print("actor: ", tall)
            i += 1
        #tall += 1
        #send each line to make nodes
        #append nodes to list to send to graph

class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = []
        
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
    
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
        # "Returns the value (a movie) of an edge between two nodes."
        return self.graph[node1][node2]


#oppgave 2 - shortest path.   
#Breadth-first search https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/
def wfsSearch(graph, start, end):
    queue = [[start]]
    visited = []

    if start == end:
        return start
    
    while queue:
        path = queue.pop(0) #dequeue, remove from start of list, index 0
        node = path[-1]

        if node not in visited:
            neighbors = graph

        for s, d, w in graph: #iterating through all the edges
            if s == u and d not in visited:
                visited.add(d)
                queue.append(d) #enqueue, add to end of list
    return path



graph = Graph(actorList) #add nodes to graph

for movie in movieList:
    m_id = movie.get_id()
    for actor1 in actorList:
        if m_id in actor1.get_movies():
            for actor2 in actorList:
                if actor1 != actor2 and m_id in actor2.get_movies():
                    graph.add_edge(actor1, actor2, movie)
                    graph.add_edge(actor2, actor1, movie) #for undirected graph
                    

print("\nOppgave 1\n")
print("Nodes: ", len(actorList))
print("Edges: ", len(graph.graph))

# for i in graph.graph:
#     print(i[0].get_name(), i[1].get_name(), i[2].get_name())
 