from collections import defaultdict


def is_rib(line):
    return len(line.split()) > 1


def parse_dates(example_file, config_file):
    start_node, traversal = pars_config_file(config_file)
    graph = pars_example_file(example_file)
    return start_node, traversal, graph


def pars_example_file(example_file):
    with open(example_file) as example:
        graph: defaultdict = defaultdict(list)
        for line in example:
            from_node, to_node = line.split() if is_rib(line) else (line.strip(), '')
            graph[from_node].extend(to_node if to_node != '' else [])
    return graph


def pars_config_file(config_file):
    with open(config_file) as config_handler:
        start_node = config_handler.readline().split()[1].rstrip()
        traversal = config_handler.readline().split()[1].rstrip()
    return start_node, traversal
