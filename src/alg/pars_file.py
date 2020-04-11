from collections import defaultdict


def is_rib(line):
    return len(line.split()) > 1


def pars_example_file(parameter_cmd: str):
    with open(parameter_cmd) as config_handler:
        graph: defaultdict = defaultdict(list)
        start_node = config_handler.readline().split()[1].rstrip()
        traversal = config_handler.readline().split()[1].rstrip()
        for line in config_handler:
            from_node, to_node = line.split() if is_rib(line) else (line.strip(), '')
            graph[from_node].extend(to_node if to_node != '' else [])
    return start_node, traversal, graph
