"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import merge_intervals


class TestCases(unittest.TestCase):
    def test_overlap(self):
        args = ([(5, 8), (1, 4), (3, 6)],)
        before = deepcopy(args)
        expected = [(1, 8)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_touch_and_gap(self):
        args = ([(1, 2), (2, 3), (5, 7)],)
        before = deepcopy(args)
        expected = [(1, 3), (5, 7)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_nested(self):
        args = ([(1, 10), (2, 3), (4, 8)],)
        before = deepcopy(args)
        expected = [(1, 10)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_duplicates(self):
        args = ([(2, 4), (2, 4)],)
        before = deepcopy(args)
        expected = [(2, 4)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_points(self):
        args = ([(0, 0), (0, 1), (3, 3)],)
        before = deepcopy(args)
        expected = [(0, 1), (3, 3)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
