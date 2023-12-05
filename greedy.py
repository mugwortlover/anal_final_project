#credit: Jimmy

import networkx as nx

def filter_colors(coloring, node, graph):
    illegal_colors = []
    for neighbor in graph.neighbors(node):
        if coloring.get(neighbor) is not None:
            illegal_colors.append(coloring.get(neighbor))
    return illegal_colors


def greedy_coloring(graph: nx.Graph):
    node_list = [*nx.nodes(graph)]

    color = 0
    colors = []

    coloring = {}

    node_list.sort(key=lambda node: len(list(graph.neighbors(node))), reverse=True)

    for node in node_list:
        if color == 0:
            coloring[node] = color
            colors.append(color)
            color += 1
        else:
            insert = True
            # Fix this line
            illegal_colors = filter_colors(coloring, node, graph)
            for i in range(0, color):
                if i not in illegal_colors:
                    coloring[node] = i
                    insert = False
            if insert:
                coloring[node] = color
                color += 1

    return coloring