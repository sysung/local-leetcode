"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import peak_concurrency
else:
    from main import peak_concurrency


class TestCases(unittest.TestCase):

    def test_empty(self):
        args = ([],)
        before = deepcopy(args)
        self.assertEqual(peak_concurrency(*args), 0)
        self.assertEqual(args, before)

    def test_zero_duration(self):
        args = ([(1, 1), (0, 0)],)
        before = deepcopy(args)
        self.assertEqual(peak_concurrency(*args), 0)
        self.assertEqual(args, before)

    def test_touching(self):
        args = ([(0, 2), (2, 4), (4, 6)],)
        before = deepcopy(args)
        self.assertEqual(peak_concurrency(*args), 1)
        self.assertEqual(args, before)

    def test_overlap(self):
        args = ([(0, 4), (2, 5), (4, 7)],)
        before = deepcopy(args)
        self.assertEqual(peak_concurrency(*args), 2)
        self.assertEqual(args, before)

    def test_duplicates(self):
        args = ([(1, 3), (1, 3), (2, 2)],)
        before = deepcopy(args)
        self.assertEqual(peak_concurrency(*args), 2)
        self.assertEqual(args, before)

    def test_nested(self):
        args = ([(0, 10), (2, 8), (3, 4)],)
        before = deepcopy(args)
        self.assertEqual(peak_concurrency(*args), 3)
        self.assertEqual(args, before)

    def test_unsorted(self):
        args = ([(9, 10), (2, 8), (1, 5)],)
        before = deepcopy(args)
        self.assertEqual(peak_concurrency(*args), 2)
        self.assertEqual(args, before)

    def test_simultaneous_changes(self):
        args = ([(0, 2), (0, 2), (2, 4), (2, 4), (2, 4)],)
        before = deepcopy(args)
        self.assertEqual(peak_concurrency(*args), 3)
        self.assertEqual(args, before)

    def test_large_endpoints(self):
        args = ([(0, 1000000000000), (999999999999, 1000000000000)],)
        before = deepcopy(args)
        self.assertEqual(peak_concurrency(*args), 2)
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
