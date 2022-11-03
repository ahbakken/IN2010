#oblig 3 IN2010

import csv
from classes import Actor, Graph, Movie

#oppgave 1 - build the graph
print("\n--------------- OPPGAVE 1 ----------------\n")

actorList = [] #list of actors, nodes
movieList = [] #list of movies, edges

# make edges of movies, marvel_
with open('marvel_movies.tsv', encoding="utf-8") as file:
    movies = csv.reader(file, delimiter="\t")
    # printing data line by line
    for line in movies:
        movie = Movie(line[0], line[1], line[2])
        movieList.append(movie)


# open .tsv file as csv and read the file
# make nodes of actors marvel_
with open('marvel_actors.tsv', encoding="utf-8") as file:
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
                    print(final_path[0][0].get_name())
                    i = 1
                    while i < len(final_path):
                        print('=== [',final_path[i][0].get_name(), '] ===> ', final_path[i][1].get_name())
                        i += 1
                    print('\n')
                    return final_path  
            visited.add(current_node)

    print("A connecting path doesn't exist between", start.get_name() ,' and ' , end.get_name(), " :( \n")
    return

sp = (shortestPath(graph, actorList[2], actorList[4]))

#oppgave 23 - chillest path through graph
print("\n--------------- OPPGAVE 3 ----------------\n")


