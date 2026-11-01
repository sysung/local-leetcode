"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import build_audience
else:
    from main import build_audience


class TestCases(unittest.TestCase):

    def test_intersection_then_suppression(self):
        args = (['a', 'b', 'c', 'd'], [['a', 'b', 'c'], ['b', 'c', 'd']], ['c'])
        before = deepcopy(args)
        self.assertEqual(build_audience(*args), ['b'])
        self.assertEqual(args, before)

    def test_no_required_groups(self):
        args = (['b', 'a', 'b'], [], ['b'])
        before = deepcopy(args)
        self.assertEqual(build_audience(*args), ['a'])
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], [], [])
        before = deepcopy(args)
        self.assertEqual(build_audience(*args), [])
        self.assertEqual(args, before)

    def test_empty_required_group(self):
        args = (['a', 'b'], [['a', 'b'], []], [])
        before = deepcopy(args)
        self.assertEqual(build_audience(*args), [])
        self.assertEqual(args, before)

    def test_outside_universe(self):
        args = (['a'], [['a', 'x']], ['x'])
        before = deepcopy(args)
        self.assertEqual(build_audience(*args), ['a'])
        self.assertEqual(args, before)

    def test_duplicates(self):
        args = (['b', 'a', 'a'], [['a', 'a', 'b'], ['b', 'b', 'a']], [])
        before = deepcopy(args)
        self.assertEqual(build_audience(*args), ['a', 'b'])
        self.assertEqual(args, before)

    def test_all_excluded(self):
        args = (['a', 'b'], [], ['a', 'b'])
        before = deepcopy(args)
        self.assertEqual(build_audience(*args), [])
        self.assertEqual(args, before)

    def test_disjoint_groups(self):
        args = (['a', 'b'], [['a'], ['b']], [])
        before = deepcopy(args)
        self.assertEqual(build_audience(*args), [])
        self.assertEqual(args, before)

    def test_sorted_result(self):
        args = (['z', 'b', 'a'], [['z', 'a', 'b']], [])
        before = deepcopy(args)
        self.assertEqual(build_audience(*args), ['a', 'b', 'z'])
        self.assertEqual(args, before)

    def test_empty_universe(self):
        args = ([], [['x']], [])
        before = deepcopy(args)
        self.assertEqual(build_audience(*args), [])
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
