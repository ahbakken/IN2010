#oblig 3 IN2010
# task 1 build the graph
import csv

class Actor:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.movies = []

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

    

actorList = [] #list of actors
movieList = [] #list of movies

# open .tsv file as csv and read the file
with open('marvel_actors.tsv') as file:
    actors = csv.reader(file, delimiter="\t")
     
    # printing data line by line
    for line in actors:
        actor = Actor(line[0], line[1])
        i = 2
        while i < len(line):
            actor.add_movie(line[i]) #the movies they acted in
            i +=1
        actorList.append(actor)
        #send each line to make nodes
        #append nodes to list to send to graph

with open('marvel_movies.tsv') as file:
    movies = csv.reader(file, delimiter="\t")
     
    # printing data line by line
    for line in movies:
        movie = Movie(line[0], line[1], line[2])
        
        movieList.append(movie)

