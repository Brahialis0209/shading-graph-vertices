import sys
sys.path.append('../')

from src.alg.graph_traversal import traversal_graph
from src.alg.pars_file import pars_example_file


def main():
    parameters_cmd = list()
    for param in sys.argv:
        parameters_cmd.append(param)
    if len(parameters_cmd) > 2:
        print("example file error!")
        return
    parameter_cmd = parameters_cmd[1]
    start_node, traversal, graph = pars_example_file(parameter_cmd)
    traversal_graph(graph, start_node, traversal, True)


if __name__ == "__main__":
    main()
