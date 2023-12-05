#credit: Pachie

import matplotlib.pyplot as plt
import networkx as nx

def flatten(lst2d):
    out = []
    for lst in lst2d:
        for item in lst:
            out.append(item)
    return out


def create_graph(list_of_lists):
    #init graph
    graph = nx.Graph()

    #add nodes for each list
    for lst in list_of_lists:
        graph.add_node(' '.join(lst))

    
    #add edges
    items = set(flatten(list_of_lists))

    for item in items:
        for i in range(len(list_of_lists)):
            for j in range(len(list_of_lists)):
                if i != j:
                    if item in list_of_lists[i] and item in list_of_lists[j]:
                        graph.add_edge(' '.join(list_of_lists[i]), ' '.join(list_of_lists[j]))
    

    return graph


if __name__ == '__main__':
    sample = [['apple', 'b', 'c'], ['add', 'b', 'f'], ['apple', 'b', 'e']]
    create_graph(sample)
