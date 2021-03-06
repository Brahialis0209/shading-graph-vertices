from src.alg.draw_graph import draw_graph
from src.alg.queue import Queue
from src.alg.stack import Stack


def traversal_algorithm(graph: dict, start_element: str, container_type, draw: bool):
    container = container_type()
    visited = set()
    container.put(start_element)
    while not container.empty():
        cur_node = container.pop()
        visited.add(cur_node)
        if draw:
            draw_graph(graph, visited)
        for adjacent_node in graph[cur_node]:
            if adjacent_node not in visited:
                container.put(adjacent_node)
    return list(visited)


def traversal_graph(graph, start_node, traversal, draw: bool):
    structure = Stack if traversal == "DFS" else Queue
    return traversal_algorithm(graph, start_node, structure, draw)
