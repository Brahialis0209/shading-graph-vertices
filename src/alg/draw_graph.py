from graphviz import Digraph
import time


def draw_graph(graph: dict, used: set):
    dot = Digraph()
    paths = graph.items()
    time.sleep(2)
    for path in paths:
        start_node = path[0]
        color = "red" if start_node in used else "black"
        dot.node(start_node, start_node, color=color)
    for path in paths:
        start_node, to_nodes = path
        for to_node in to_nodes:
            dot.edge(start_node, to_node)
    dot.graph_attr["rankdir"] = "LR"
    dot.render("graph", view=True)
