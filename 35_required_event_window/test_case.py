"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import shortest_event_window
else:
    from main import shortest_event_window


class TestCases(unittest.TestCase):

    def test_shortest_window(self):
        args = (['view', 'noise', 'buy', 'view', 'buy'], ['view', 'buy'])
        before = deepcopy(args)
        self.assertEqual(shortest_event_window(*args), (2, 4))
        self.assertEqual(args, before)

    def test_duplicate_requirements(self):
        args = (['view', 'buy', 'view', 'noise', 'view'], ['view', 'view', 'buy'])
        before = deepcopy(args)
        self.assertEqual(shortest_event_window(*args), (0, 3))
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], [])
        before = deepcopy(args)
        self.assertEqual(shortest_event_window(*args), (0, 0))
        self.assertEqual(args, before)

    def test_empty_required(self):
        args = (['view'], [])
        before = deepcopy(args)
        self.assertEqual(shortest_event_window(*args), (0, 0))
        self.assertEqual(args, before)

    def test_empty_events(self):
        args = ([], ['buy'])
        before = deepcopy(args)
        self.assertEqual(shortest_event_window(*args), None)
        self.assertEqual(args, before)

    def test_missing_type(self):
        args = (['view', 'view'], ['view', 'buy'])
        before = deepcopy(args)
        self.assertEqual(shortest_event_window(*args), None)
        self.assertEqual(args, before)

    def test_insufficient_multiplicity(self):
        args = (['view', 'buy'], ['view', 'view'])
        before = deepcopy(args)
        self.assertEqual(shortest_event_window(*args), None)
        self.assertEqual(args, before)

    def test_earliest_tie(self):
        args = (['view', 'buy', 'view', 'buy'], ['view', 'buy'])
        before = deepcopy(args)
        self.assertEqual(shortest_event_window(*args), (0, 2))
        self.assertEqual(args, before)

    def test_shrink_surplus(self):
        args = (['view', 'view', 'noise', 'buy'], ['view', 'buy'])
        before = deepcopy(args)
        self.assertEqual(shortest_event_window(*args), (1, 4))
        self.assertEqual(args, before)

    def test_one_type_repeated(self):
        args = (['a', 'a', 'a'], ['a', 'a'])
        before = deepcopy(args)
        self.assertEqual(shortest_event_window(*args), (0, 2))
        self.assertEqual(args, before)

    def test_requirement_order_irrelevant(self):
        args = (['buy', 'view'], ['view', 'buy'])
        before = deepcopy(args)
        self.assertEqual(shortest_event_window(*args), (0, 2))
        self.assertEqual(args, before)

    def test_shorter_later(self):
        args = (['a', 'noise', 'b', 'noise', 'a', 'b'], ['a', 'b'])
        before = deepcopy(args)
        self.assertEqual(shortest_event_window(*args), (4, 6))
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
