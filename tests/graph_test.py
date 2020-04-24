import unittest
import sys

sys.path.append('../')

from src.alg.graph_traversal import traversal_graph
from src.alg.pars_file import pars_example_file

tests_path = "tests/dates/"


class TestTraversalGraph(unittest.TestCase):

    def test_connected_graph_DFS(self):
        test_name = "connected_graph"
        start_node, traversal, graph = pars_example_file(tests_path + test_name)
        traversal = "DFS"
        visited = traversal_graph(graph, start_node, traversal, False)
        self.assertEqual(len(visited), 8)
        self.assertEqual(sorted(graph.keys()), sorted(visited))

    def test_connected_graph_BFS(self):
        test_name = "connected_graph"
        start_node, traversal, graph = pars_example_file(tests_path + test_name)
        traversal = "BFS"
        visited = traversal_graph(graph, start_node, traversal, False)
        self.assertEqual(len(visited), 8)
        self.assertEqual(sorted(graph.keys()), sorted(visited))


if __name__ == '__main__':
    unittest.main()
