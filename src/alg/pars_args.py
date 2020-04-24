import argparse


def arguments_parser():
    parser = argparse.ArgumentParser(description='shading graphs')
    parser.add_argument('example', type=str, help='Input file name with example.')
    return parser.parse_args()
