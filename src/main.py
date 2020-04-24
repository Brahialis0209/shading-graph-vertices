import sys

from src.alg.pars_args import arguments_parser

sys.path.append('../')

from src.alg.graph_traversal import traversal_graph
from src.alg.pars_file import pars_example_file


def main():
    start_node, traversal, graph = pars_example_file(arguments_parser().example)
    traversal_graph(graph, start_node, traversal, True)


if __name__ == "__main__":
    main()
