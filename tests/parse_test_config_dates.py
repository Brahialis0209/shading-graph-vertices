def parser_tests(parameter_cmd):
    with open(parameter_cmd) as config_handler:
        path_first = config_handler.readline().replace('\n', '')
    return path_first
