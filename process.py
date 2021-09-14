import argparse
from analysis import Analysis

parser = argparse.ArgumentParser()
parser.add_argument("--path", help="define path to logs")
arguments = parser.parse_args()

if arguments.path:
    path = arguments.path
else:
    path = './logs/logs.txt'

Analysis(path).export()

