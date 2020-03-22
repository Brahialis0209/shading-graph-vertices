from collections import defaultdict


def pars_config_file(parameter_cmd: str):
    with open(parameter_cmd) as config_handler:
        graph = defaultdict(list)
        start_node = config_handler.readline().split('=')[1].replace("\n", '')
        traversal = config_handler.readline().split('=')[1].replace("\n", '')
        for item in config_handler:
            item = item.split()
            from_node = item[0]
            to_node = item[1]
            if to_node == 'empty':
                graph[from_node] = []
            else:
                graph[from_node].append(to_node)
    return start_node, traversal, graph
