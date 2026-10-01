"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import merge_streams


class TestCases(unittest.TestCase):
    def test_interleaved(self):
        args = ([[(1, 'a'), (4, 'd')], [(2, 'b'), (3, 'c')]],)
        before = deepcopy(args)
        expected = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_ties(self):
        args = ([[(1, 'z'), (1, 'y')], [(1, 'a')]],)
        before = deepcopy(args)
        expected = [(1, 'z'), (1, 'y'), (1, 'a')]
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_no_streams(self):
        args = ([],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_empty_streams(self):
        args = ([[], [], []],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_one_stream(self):
        args = ([[(0, 'a'), (0, 'b'), (9, 'c')]],)
        before = deepcopy(args)
        expected = [(0, 'a'), (0, 'b'), (9, 'c')]
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_mixed_empty(self):
        args = ([[], [(2, 'b')], [], [(1, 'a')]],)
        before = deepcopy(args)
        expected = [(1, 'a'), (2, 'b')]
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_incremental_consumption(self):
        consumed = [0, 0]
        def stream(index, timestamps):
            for timestamp in timestamps:
                consumed[index] += 1
                yield timestamp, str(index)
        merged = merge_streams([stream(0, range(0, 100, 2)), stream(1, range(1, 100, 2))])
        self.assertIs(iter(merged), merged)
        self.assertEqual(next(merged), (0, "0"))
        self.assertEqual(consumed, [1, 1])
        self.assertEqual(next(merged), (1, "1"))
        self.assertEqual(consumed, [2, 1])
        self.assertEqual(len(list(merged)), 98)


if __name__ == "__main__":
    unittest.main()
