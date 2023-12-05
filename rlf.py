#credit: Matthew

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def max_indep_set(g):
    p=g.copy()
    nodes_list=[*p.nodes]
    ret=[]
    while len(nodes_list)>0:
        vert=nodes_list[0]

        ret.append(vert)
        neigh=[k for k in p.neighbors(vert)]
        p.remove_node(vert)

        for n in neigh:
            p.remove_node(n)

        nodes_list=[*p.nodes]
    return ret


def rlf (g):
    q=g.copy()
    color_dict=dict()
    num=0

    while q.number_of_nodes()>0:
        s=max_indep_set(q)

        for vertex in s:
            q.remove_node(vertex)
            color_dict[vertex]=num
            
        num+=1
    return color_dict