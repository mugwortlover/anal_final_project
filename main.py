#credit: everyone

from greedy import greedy_coloring
from rlf import rlf
from schedule import coloringSchedule
from create_graph import create_graph

import matplotlib.pyplot as plt
import networkx as nx


def main(list_of_lists):
    graph = create_graph(list_of_lists)

    user_selection = user_input('select: \n0 -> greedy \n1 -> rlf', 'try again loser', ['0', '1'])
    if user_selection == '1':
        coloring = rlf(graph)
    else:
        coloring = greedy_coloring(graph)

    coloringSchedule(coloring)

    graph_flag = user_input('would you like to see the graph? (y/n)', 'nope, ur bad', ['y', 'n'])
    if graph_flag == 'y':
        nx.draw(graph, with_labels = True)
        plt.show()


def user_input(request_msg, fail_msg, valid_responses):
    response = input(request_msg + '\n')
    while response not in valid_responses:
        print(fail_msg + '\n')
        response = input(request_msg + '\n')
    return response


    


if __name__ == '__main__':
    sample = [['apple', 'b', 'c'], ['add', 'b', 'f'], ['apple', 'b', 'e']]
    sample2 = [['GT', 'D', 'L'], ['K', 'P', 'D'], ['P', 'K', 'V'], ['GT', 'GF', 'N'], ['H', 'J'], ['GT', 'K', 'P']]

    main(sample2)