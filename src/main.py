import sys
import argparse
sys.path.append('../')

from src.alg.graph_traversal import traversal_graph
from src.alg.pars_file import pars_example_file


def main():
    parser = argparse.ArgumentParser(description='shading graphs')
    parser.add_argument('example', type=str, help='Input file name with example.')
    args = parser.parse_args()
    start_node, traversal, graph = pars_example_file(args.example)
    traversal_graph(graph, start_node, traversal, True)


if __name__ == "__main__":
    main()
