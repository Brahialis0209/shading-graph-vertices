import sys
sys.path.append('../')

from src.logic.graph_traversal import traversal_graph
from src.logic.pars_file import pars_config_file
from tests.parse_test import parser_tests


def main():
    parameters_cmd = list()
    for param in sys.argv:
        parameters_cmd.append(param)
    if len(parameters_cmd) > 2:
        print("config file error!")
        return
    parameter_cmd = parameters_cmd[1]
    path_first_test = parser_tests(parameter_cmd)
    start_node, traversal, graph = pars_config_file(path_first_test)
    draw = False
    visited = traversal_graph(graph, start_node, traversal, draw)
    if traversal == "DFS":
        assert (visited == ['1', '4', '3', '7', '8', '2', '6', '5'])
    if traversal == "BFS":
        assert (visited == ['1', '2', '3', '4', '5', '6', '7', '8'])


if __name__ == '__main__':
    main()
