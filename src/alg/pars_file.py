from collections import defaultdict


def pars_config_file(parameter_cmd: str):
    with open(parameter_cmd) as config_handler:
        graph: defaultdict = defaultdict(list)
        start_node = config_handler.readline().split('=')[1].replace("\n", '')
        traversal = config_handler.readline().split('=')[1].replace("\n", '')
        for line in config_handler:
            from_node, to_node = line.split()
            graph[from_node].extend(to_node if to_node != "empty" else [])
    return start_node, traversal, graph
