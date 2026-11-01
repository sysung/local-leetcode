"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import reconcile_campaign_events
else:
    from main import reconcile_campaign_events


class TestCases(unittest.TestCase):

    def test_missing_and_duplicate_delivery(self):
        args = ([('c', 'e1'), ('c', 'e1'), ('c', 'e2')], [('c', 'e1'), ('c', 'e3')])
        before = deepcopy(args)
        self.assertEqual(reconcile_campaign_events(*args), [('c', 'e1', 2, 1), ('c', 'e2', 1, 0), ('c', 'e3', 0, 1)])
        self.assertEqual(args, before)

    def test_matching_multisets(self):
        args = ([('c', 'e'), ('c', 'e')], [('c', 'e'), ('c', 'e')])
        before = deepcopy(args)
        self.assertEqual(reconcile_campaign_events(*args), [])
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], [])
        before = deepcopy(args)
        self.assertEqual(reconcile_campaign_events(*args), [])
        self.assertEqual(args, before)

    def test_source_only(self):
        args = ([('b', 'x')], [])
        before = deepcopy(args)
        self.assertEqual(reconcile_campaign_events(*args), [('b', 'x', 1, 0)])
        self.assertEqual(args, before)

    def test_destination_only(self):
        args = ([], [('a', 'x'), ('a', 'x')])
        before = deepcopy(args)
        self.assertEqual(reconcile_campaign_events(*args), [('a', 'x', 0, 2)])
        self.assertEqual(args, before)

    def test_campaign_is_part_of_key(self):
        args = ([('a', 'e')], [('b', 'e')])
        before = deepcopy(args)
        self.assertEqual(reconcile_campaign_events(*args), [('a', 'e', 1, 0), ('b', 'e', 0, 1)])
        self.assertEqual(args, before)

    def test_sorted_keys(self):
        args = ([('z', 'b'), ('a', 'z'), ('a', 'a')], [])
        before = deepcopy(args)
        self.assertEqual(reconcile_campaign_events(*args), [('a', 'a', 1, 0), ('a', 'z', 1, 0), ('z', 'b', 1, 0)])
        self.assertEqual(args, before)

    def test_destination_excess(self):
        args = ([('c', 'e')], [('c', 'e'), ('c', 'e'), ('c', 'e')])
        before = deepcopy(args)
        self.assertEqual(reconcile_campaign_events(*args), [('c', 'e', 1, 3)])
        self.assertEqual(args, before)

    def test_order_independent(self):
        args = ([('b', 'e'), ('a', 'e')], [('a', 'e'), ('b', 'e')])
        before = deepcopy(args)
        self.assertEqual(reconcile_campaign_events(*args), [])
        self.assertEqual(args, before)

    def test_mixed_equal_and_unequal(self):
        args = ([('a', 'e'), ('b', 'e')], [('a', 'e'), ('b', 'e'), ('b', 'e')])
        before = deepcopy(args)
        self.assertEqual(reconcile_campaign_events(*args), [('b', 'e', 1, 2)])
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
