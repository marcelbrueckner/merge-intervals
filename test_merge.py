#!/usr/bin/env python3

import unittest
from argparse import ArgumentError
from merge import interval_int, merge

class TestMerge(unittest.TestCase):

    def test_input_valid(self):
        """
        Test valid input is converted to a list
        """

        input = "1,3"
        intervals = interval_int(input)
        self.assertIsInstance(intervals, list)


    def test_input_invalid(self):
        """
        Test invalid input raises an error
        """

        input = "1"

        with self.assertRaises(ArgumentError):
            interval_int(input)


    def test_merge(self):
        """
        Test given intervals are properly merged
        """

        intervals = [[1,3],[5,6],[3,9],[13,20]]
        merged_intervals = merge(intervals)
        self.assertListEqual(merged_intervals, [[1, 9], [13, 20]])


    def test_merge_bigint(self):
        """
        Test very high interval limits are properly merged
        """

        intervals = [[-10**100,-10**50],[-10**60,0],[3,10**100],[10**1000,10**100000]]
        merged_intervals = merge(intervals)
        self.assertListEqual(merged_intervals, [[-10**100,0], [3,10**100],[10**1000,10**100000]])


if __name__ == '__main__':
    unittest.main()
