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
    
class Graph(object):
    def __init__(self, nodes=list):
        self.nodes = nodes
        self.graph = []
        self.edges = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
    
    def get_nodes(self):
        return self.nodes
    
    def get_ActorById(self, num_id):
        for _1, _2, movie in self.edges:
            if num_id == movie.get_id():
                return movie
        print("there is no actor with this ID")
        return
    
    def get_MovieById(self, num_id):
        for actor in self.nodes:
            if num_id == actor.get_id():
                return actor
        print("there is no actor with this ID")
        return
    
    #Returns the neighbors of a node
    def get_neighbors(self, node):
        connections = dict()
        for s, d, m in self.graph:
            if s == node:
                connections[d] = m
        return connections