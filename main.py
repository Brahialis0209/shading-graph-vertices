import time
from my_queue import MyQueue
from my_stack import MyStack
from graphviz import Digraph


def BFS(Graph: dict, start_element: str):
    queue = MyQueue()
    visited = []
    queue.put(start_element)

    while not queue.empty():
        work_element = queue.get()
        queue.pop()
        visited.append(work_element)
        drawGraph(Graph, visited)
        time.sleep(1)

        for adjacent_node in Graph[work_element]:
            if adjacent_node not in visited:
                queue.put(adjacent_node)


def DFS(Graph: dict, start_element: str):
    stack = MyStack()
    visited = []
    stack.put(start_element)

    while not stack.empty():
        work_element = stack.get()
        stack.pop()
        visited.append(work_element)
        drawGraph(Graph, visited)
        time.sleep(1)

        for adjacent_node in Graph[work_element]:
            if adjacent_node not in visited:
                stack.put(adjacent_node)


def drawGraph(Graph: dict, used: list):
    dot = Digraph()
    paths = Graph.items()

    for path in paths:
        start_node = path[0]
        if start_node in used:
            dot.node(start_node, start_node, color="red")
        else:
            dot.node(start_node, start_node)

    for path in paths:
        start_node = path[0]
        to_nodes = path[1]
        for to_node in to_nodes:
            dot.edge(start_node, to_node)

    dot.graph_attr["rankdir"] = "LR"
    dot.render("graph", view=True)


if __name__ == "__main__":
    Graph = {"1": ["2", "3", "4"],
             "2": ["5", "6"],
             "3": ["7"],
             "4": [],
             "5": [],
             "6": [],
             "7": ["8"],
             "8": []}
    start_node = '1'
    DFS(Graph, start_node)
