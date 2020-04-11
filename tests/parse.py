def parser_tests(file_name):
    with open(file_name) as paths_handler:
        paths = list()
        for path in paths_handler.readlines():
            paths.append(path.rstrip())
    return paths
