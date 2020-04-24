import argparse


def arguments_parser():
    parser = argparse.ArgumentParser(description='shading graphs')
    parser.add_argument('example', type=str, help='Input file name with example graph.')
    parser.add_argument('config', type=str, help='Input file name with config app.')
    args = parser.parse_args()
    return args.example, args.config
