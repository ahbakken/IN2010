# oppgave 2 - shortest path.   
# Breadth-first search 
def wfsSearch(graph, start, end):
    path_lst = [[start]]
    path_indx = 0
    visited = {start}

    if start == end:
        return queue[0]
    
    
    while path_indx < len(path_lst):
        current_path = path_lst[path_indx]
        last_node = current_path[-1]
        next_nodes = graph.get_outgoing_edges(last_node)

        previous_nodes = {start}
        
        if end in next_nodes:
            current_path.append(end)
            return current_path
            
        for next_node in next_nodes:
            if not next_node in previous_nodes

            if neighbour[0] == end:
                print(new_path[0].get_name())
                for i in range(1, len(new_path)):
                    print(new_path[i][1].get_name(), '=>' ,new_path[i][0].get_name())
                return
            
        visited.append(node)

    print("There is no connection between ", start.name, ' and ', end.name)
    return