import sys
sys.path.append('../')

from src.alg.pars_args import arguments_parser
from src.alg.graph_traversal import traversal_graph
from src.alg.pars_file import parse_dates


def main():
    start_node, traversal, graph = parse_dates(*arguments_parser())
    traversal_graph(graph, start_node, traversal, True)


if __name__ == "__main__":
    main()
