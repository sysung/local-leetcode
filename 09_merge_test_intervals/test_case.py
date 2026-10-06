"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import merge_intervals
else:
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


    def test_single_interval(self):
        args = ([(3, 7)],)
        before = deepcopy(args)
        expected = [(3, 7)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_negative_endpoints(self):
        args = ([(-5, -1), (-2, 3)],)
        before = deepcopy(args)
        expected = [(-5, 3)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_unsorted_disjoint(self):
        args = ([(8, 9), (0, 1), (4, 5)],)
        before = deepcopy(args)
        expected = [(0, 1), (4, 5), (8, 9)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_duplicates_with_contained_intervals(self):
        args = ([(1, 5), (1, 5), (2, 3)],)
        before = deepcopy(args)
        expected = [(1, 5)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_touching_chain(self):
        args = ([(4, 6), (0, 2), (2, 4)],)
        before = deepcopy(args)
        expected = [(0, 6)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_equal_starts(self):
        args = ([(1, 2), (1, 10), (1, 5)],)
        before = deepcopy(args)
        expected = [(1, 10)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_equal_ends(self):
        args = ([(5, 10), (1, 10), (7, 10)],)
        before = deepcopy(args)
        expected = [(1, 10)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_enclosing_interval_arrives_last(self):
        args = ([(2, 3), (5, 7), (0, 10)],)
        before = deepcopy(args)
        expected = [(0, 10)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_point_inside_interval(self):
        args = ([(2, 2), (0, 4)],)
        before = deepcopy(args)
        expected = [(0, 4)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_isolated_points(self):
        args = ([(3, 3), (1, 1), (2, 2)],)
        before = deepcopy(args)
        expected = [(1, 1), (2, 2), (3, 3)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_large_coordinates(self):
        args = ([(0, 1000000000000000000), (1000000000000000000, 1000000000000000001)],)
        before = deepcopy(args)
        expected = [(0, 1000000000000000001)]
        self.assertEqual(merge_intervals(*args), expected)
        self.assertEqual(args, before)

    def test_maximum_repeated_intervals(self):
        intervals = [(1, 9)] * 100000
        self.assertEqual(merge_intervals(intervals), [(1, 9)])
        self.assertEqual(len(intervals), 100000)

    def test_maximum_disjoint_intervals(self):
        intervals = [(3 * i, 3 * i + 1) for i in range(99999, -1, -1)]
        self.assertEqual(merge_intervals(intervals), list(reversed(intervals)))
        self.assertEqual(intervals[0], (299997, 299998))

    def test_maximum_touching_chain(self):
        intervals = [(i, i + 1) for i in range(99999, -1, -1)]
        self.assertEqual(merge_intervals(intervals), [(0, 100000)])


if __name__ == "__main__":
    unittest.main()
