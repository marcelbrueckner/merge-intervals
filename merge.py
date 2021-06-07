#!/usr/bin/env python3

from argparse import ArgumentParser, ArgumentError
import re

# Define a custom argument type `interval` to properly parse arguments
# https://docs.python.org/3/library/argparse.html#type
def interval(arg):
    pattern = re.compile("^\d+,\d+$")

    if not pattern.match(arg):
        raise ArgumentError

    # Convert comma-separated list (of strings) to list of integers
    return sorted([int(i) for i in arg.split(",")])

# Define and parse arguments
parser = ArgumentParser(description='Merge probably overlapping intervals into non-overlapping intervals.')
parser.add_argument('intervals', metavar='interval', type=interval, nargs='+',
                    help='list of intervals to merge (example: 1,3 3,9)')
args = parser.parse_args()

print(args)
