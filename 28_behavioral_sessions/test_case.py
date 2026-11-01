"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import sessionize
else:
    from main import sessionize


class TestCases(unittest.TestCase):

    def test_timeout_boundary(self):
        args = ([('u', 0, 'a'), ('u', 5, 'b'), ('u', 11, 'c')], 5)
        before = deepcopy(args)
        self.assertEqual(sessionize(*args), [('u', 1, 0, 5, 2), ('u', 2, 11, 11, 1)])
        self.assertEqual(args, before)

    def test_independent_users(self):
        args = ([('b', 4, 'b1'), ('a', 9, 'a2'), ('a', 1, 'a1')], 10)
        before = deepcopy(args)
        self.assertEqual(sessionize(*args), [('a', 1, 1, 9, 2), ('b', 1, 4, 4, 1)])
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], 5)
        before = deepcopy(args)
        self.assertEqual(sessionize(*args), [])
        self.assertEqual(args, before)

    def test_single_event(self):
        args = ([('u', 7, 'e')], 0)
        before = deepcopy(args)
        self.assertEqual(sessionize(*args), [('u', 1, 7, 7, 1)])
        self.assertEqual(args, before)

    def test_zero_timeout_equal_times(self):
        args = ([('u', 1, 'b'), ('u', 1, 'a'), ('u', 2, 'c')], 0)
        before = deepcopy(args)
        self.assertEqual(sessionize(*args), [('u', 1, 1, 1, 2), ('u', 2, 2, 2, 1)])
        self.assertEqual(args, before)

    def test_duplicate_rows_count(self):
        args = ([('u', 1, 'a'), ('u', 1, 'a')], 10)
        before = deepcopy(args)
        self.assertEqual(sessionize(*args), [('u', 1, 1, 1, 2)])
        self.assertEqual(args, before)

    def test_many_sessions(self):
        args = ([('u', 20, 'c'), ('u', 0, 'a'), ('u', 10, 'b')], 2)
        before = deepcopy(args)
        self.assertEqual(sessionize(*args), [('u', 1, 0, 0, 1), ('u', 2, 10, 10, 1), ('u', 3, 20, 20, 1)])
        self.assertEqual(args, before)

    def test_chained_gaps(self):
        args = ([('u', 0, 'a'), ('u', 4, 'b'), ('u', 8, 'c')], 5)
        before = deepcopy(args)
        self.assertEqual(sessionize(*args), [('u', 1, 0, 8, 3)])
        self.assertEqual(args, before)

    def test_numbering_resets(self):
        args = ([('b', 10, 'd'), ('a', 0, 'a'), ('b', 0, 'c'), ('a', 10, 'b')], 1)
        before = deepcopy(args)
        self.assertEqual(sessionize(*args), [('a', 1, 0, 0, 1), ('a', 2, 10, 10, 1), ('b', 1, 0, 0, 1), ('b', 2, 10, 10, 1)])
        self.assertEqual(args, before)

    def test_large_timestamp(self):
        args = ([('u', 1000000000000, 'b'), ('u', 999999999999, 'a')], 1)
        before = deepcopy(args)
        self.assertEqual(sessionize(*args), [('u', 1, 999999999999, 1000000000000, 2)])
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
