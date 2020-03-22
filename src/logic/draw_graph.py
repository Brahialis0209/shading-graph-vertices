from graphviz import Digraph


def draw_graph(graph: dict, used: list):
    dot = Digraph()
    paths = graph.items()

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
