def parser_tests(config_name):
    with open(config_name) as config_handler:
        paths = list()
        for path in config_handler.readlines():
            paths.append(path.replace('\n', ''))
    return paths
