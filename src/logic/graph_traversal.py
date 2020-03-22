import time

from src.logic.draw_graph import draw_graph
from src.logic.queue import Queue
from src.logic.stack import Stack


def traversal_algorithm(graph: dict, start_element: str, container_type, draw: bool):
    container = container_type()
    visited = {}
    container.put(start_element)

    while not container.empty():
        work_node = container.get()
        container.pop()
        visited[work_node] = work_node
        if draw:
            draw_graph(graph, list(visited.keys()))
        time.sleep(1)

        for adjacent_node in graph[work_node]:
            if adjacent_node not in visited:
                container.put(adjacent_node)
    return list(visited.keys())


def traversal_graph(graph, start_node, traversal, draw: bool):
    visited_nodes = list()
    if traversal == "DFS":
        visited_nodes = traversal_algorithm(graph, start_node, Stack, draw)
    elif traversal == "BFS":
        visited_nodes = traversal_algorithm(graph, start_node, Queue, draw)
    return visited_nodes
