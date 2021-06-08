#!/usr/bin/env python3

from argparse import ArgumentParser, ArgumentError
import re, sys

# Define a custom argument type `interval` to properly parse arguments
# https://docs.python.org/3/library/argparse.html#type
def interval(arg):
    pattern = re.compile("^\s*\[?(-?\d+,-?\d+)\]?$")
    match = pattern.match(arg)

    if not match:
        raise ArgumentError

    # Convert comma-separated list (of strings) to list of integers
    arg = match.group(1)
    return sorted([int(i) for i in arg.split(",")])

# argparse has issues with parameters starting with a negative integer value,
# thus a little workaround is required (by adding a space in front)
# https://stackoverflow.com/questions/9025204/python-argparse-issue-with-optional-arguments-which-are-negative-numbers
for i, arg in enumerate(sys.argv):
    if (arg[0] == '-') and arg[1].isdigit(): sys.argv[i] = ' ' + arg

# Define and parse arguments
parser = ArgumentParser(description='Merge probably overlapping intervals into non-overlapping intervals.')
parser.add_argument('intervals', metavar='interval', type=interval, nargs='+',
                    help='list of intervals to merge (example: -1,3 3,9)')
args = parser.parse_args()

# Merge intervals
merged_interval = None
merged_intervals = []
for i, current_interval in enumerate(sorted(args.intervals)):

    # First iteration
    if merged_interval is None:
        merged_interval = current_interval

    # Current interval overlaps with the previous(ly merged) interval(s)
    if current_interval[0] <= merged_interval[1]:
        merged_interval[1] = max(current_interval[1], merged_interval[1])

    # Current interval doesn't overlap with previous(ly merged) inverval(s)
    # As intervals are sorted by the interval's lower limit, no other interval at a higher index will.
    # Thus the previous(ly merged) inverval(s) are "complete".
    else:
        merged_intervals.append(merged_interval)
        merged_interval = current_interval

    # Last iteration
    if i == len(args.intervals) - 1:
        merged_intervals.append(merged_interval)

print(merged_intervals)
