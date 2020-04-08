import unittest
import sys

sys.path.append('../')

from src.logic.graph_traversal import traversal_graph
from src.logic.pars_file import pars_config_file
from tests.parse_test import parser_tests


def give_test_paths():
    config_name = "config"
    test_paths = parser_tests(config_name)
    return test_paths


class TestTraversalGraph(unittest.TestCase):
    test_paths = give_test_paths()

    def setUp(self):
        self.test_path = self.test_paths.pop(0)

    def test_first(self):
        start_node, traversal, graph = pars_config_file(self.test_path)
        draw = False
        visited = traversal_graph(graph, start_node, traversal, draw)
        self.assertEqual(visited, ['1', '4', '3', '7', '8', '2', '6', '5'])

    def test_second(self):
        start_node, traversal, graph = pars_config_file(self.test_path)
        draw = False
        visited = traversal_graph(graph, start_node, traversal, draw)
        self.assertEqual(visited, ['1', '2', '3', '4', '5', '6', '7', '8'])


if __name__ == '__main__':
    unittest.main()
