import unittest
import sys

sys.path.append('../')

from src.alg.graph_traversal import traversal_graph
from src.alg.pars_file import pars_example_file

tests_path = "tests/dates/"


class TestTraversalGraph(unittest.TestCase):

    def test_connected_graph_DFS(self):
        test_name = "connected_graph"
        graph = pars_example_file(tests_path + test_name)
        visited = traversal_graph(graph, '1', "DFS", False)
        self.assertEqual(len(visited), 8)
        self.assertEqual(sorted(graph.keys()), sorted(visited))

    def test_connected_graph_BFS(self):
        test_name = "connected_graph"
        graph = pars_example_file(tests_path + test_name)
        visited = traversal_graph(graph, '1', "BFS", False)
        self.assertEqual(len(visited), 8)
        self.assertEqual(sorted(graph.keys()), sorted(visited))

    def test_long_graph_DFS(self):
        test_name = "long_graph"
        graph = pars_example_file(tests_path + test_name)
        visited = traversal_graph(graph, '1', "DFS", False)
        self.assertEqual(len(visited), 7)
        self.assertEqual(sorted(graph.keys()), sorted(visited))

    def test_long_graph_BFS(self):
        test_name = "long_graph"
        graph = pars_example_file(tests_path + test_name)
        visited = traversal_graph(graph, '1', "BFS", False)
        self.assertEqual(len(visited), 7)
        self.assertEqual(sorted(graph.keys()), sorted(visited))

    def test_unconnected_graph(self):
        test_name = "unconnected_graph"
        graph = pars_example_file(tests_path + test_name)
        visited = traversal_graph(graph, '1', "DFS", False)
        self.assertEqual(len(visited), 3)
        self.assertEqual(['1', '2', '3'], sorted(visited))


if __name__ == '__main__':
    unittest.main()
