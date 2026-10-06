"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import shortest_ordered_match
else:
    from main import shortest_ordered_match


class TestCases(unittest.TestCase):

    def test_shorter_later(self):
        args = (['A', 'X', 'B', 'C', 'A', 'B', 'C'], ['A', 'B', 'C'])
        before = deepcopy(args)
        self.assertEqual(shortest_ordered_match(*args), (4, 6))
        self.assertEqual(args, before)

    def test_repeated_required(self):
        args = (['A', 'B', 'A', 'B'], ['A', 'A', 'B'])
        before = deepcopy(args)
        self.assertEqual(shortest_ordered_match(*args), (0, 3))
        self.assertEqual(args, before)

    def test_wrong_order(self):
        args = (['B', 'A'], ['A', 'B'])
        before = deepcopy(args)
        self.assertEqual(shortest_ordered_match(*args), None)
        self.assertEqual(args, before)

    def test_empty_required(self):
        args = (['A'], [])
        before = deepcopy(args)
        self.assertEqual(shortest_ordered_match(*args), None)
        self.assertEqual(args, before)

    def test_empty_codes(self):
        args = ([], ['A'])
        before = deepcopy(args)
        self.assertEqual(shortest_ordered_match(*args), None)
        self.assertEqual(args, before)

    def test_earliest_tie(self):
        args = (['A', 'B', 'A', 'B'], ['A', 'B'])
        before = deepcopy(args)
        self.assertEqual(shortest_ordered_match(*args), (0, 1))
        self.assertEqual(args, before)

    def test_single_code(self):
        args = (['X', 'A', 'A'], ['A'])
        before = deepcopy(args)
        self.assertEqual(shortest_ordered_match(*args), (1, 1))
        self.assertEqual(args, before)

    def test_not_enough_occurrences(self):
        args = (['A'], ['A', 'A'])
        before = deepcopy(args)
        self.assertEqual(shortest_ordered_match(*args), None)
        self.assertEqual(args, before)

    def test_latest_prefix(self):
        args = (['A', 'X', 'A', 'B', 'C'], ['A', 'B', 'C'])
        before = deepcopy(args)
        self.assertEqual(shortest_ordered_match(*args), (2, 4))
        self.assertEqual(args, before)

    def test_missing(self):
        args = (['A', 'B'], ['A', 'C'])
        before = deepcopy(args)
        self.assertEqual(shortest_ordered_match(*args), None)
        self.assertEqual(args, before)

    def test_all_repeated(self):
        args = (['A', 'A', 'A', 'A'], ['A', 'A', 'A'])
        before = deepcopy(args)
        self.assertEqual(shortest_ordered_match(*args), (0, 2))
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
