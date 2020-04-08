from src.alg.draw_graph import draw_graph
from src.alg.queue import Queue
from src.alg.stack import Stack


def traversal_algorithm(graph: dict, start_element: str, container_type, draw: bool):
    container = container_type()
    visited = {}
    container.put(start_element)
    while not container.empty():
        work_node = container.pop()
        visited[work_node] = work_node
        if draw:
            draw_graph(graph, list(visited.keys()))
        for adjacent_node in graph[work_node]:
            if adjacent_node not in visited:
                container.put(adjacent_node)
    return list(visited.keys())


def traversal_graph(graph, start_node, traversal, draw: bool):
    structure = Stack if traversal == "DFS" else Queue
    return traversal_algorithm(graph, start_node, structure, draw)
