def parser_tests(file_name):
    with open(file_name) as config_handler:
        paths = list()
        for path in config_handler.readlines():
            paths.append(path.replace('\n', ''))
    return paths
