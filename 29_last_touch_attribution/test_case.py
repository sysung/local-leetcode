"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import attribute_last_touch
else:
    from main import attribute_last_touch


class TestCases(unittest.TestCase):

    def test_latest_eligible(self):
        args = ([('u', 1, 'old'), ('u', 8, 'new'), ('u', 12, 'future')], [('c1', 'u', 10)], 5)
        before = deepcopy(args)
        self.assertEqual(attribute_last_touch(*args), [('c1', 'new')])
        self.assertEqual(args, before)

    def test_campaign_tie_and_unattributed(self):
        args = ([('u', 7, 'z'), ('u', 7, 'a')], [('c2', 'missing', 10), ('c1', 'u', 10)], 3)
        before = deepcopy(args)
        self.assertEqual(attribute_last_touch(*args), [('c1', 'a'), ('c2', None)])
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], [], 5)
        before = deepcopy(args)
        self.assertEqual(attribute_last_touch(*args), [])
        self.assertEqual(args, before)

    def test_no_touches(self):
        args = ([], [('c', 'u', 5)], 5)
        before = deepcopy(args)
        self.assertEqual(attribute_last_touch(*args), [('c', None)])
        self.assertEqual(args, before)

    def test_lower_bound_inclusive(self):
        args = ([('u', 5, 'a')], [('c', 'u', 10)], 5)
        before = deepcopy(args)
        self.assertEqual(attribute_last_touch(*args), [('c', 'a')])
        self.assertEqual(args, before)

    def test_outside_lookback(self):
        args = ([('u', 4, 'a')], [('c', 'u', 10)], 5)
        before = deepcopy(args)
        self.assertEqual(attribute_last_touch(*args), [('c', None)])
        self.assertEqual(args, before)

    def test_zero_lookback(self):
        args = ([('u', 9, 'a'), ('u', 10, 'b')], [('c', 'u', 10)], 0)
        before = deepcopy(args)
        self.assertEqual(attribute_last_touch(*args), [('c', 'b')])
        self.assertEqual(args, before)

    def test_future_only(self):
        args = ([('u', 11, 'a')], [('c', 'u', 10)], 100)
        before = deepcopy(args)
        self.assertEqual(attribute_last_touch(*args), [('c', None)])
        self.assertEqual(args, before)

    def test_user_isolation(self):
        args = ([('v', 9, 'a'), ('u', 1, 'b')], [('c', 'u', 10)], 2)
        before = deepcopy(args)
        self.assertEqual(attribute_last_touch(*args), [('c', None)])
        self.assertEqual(args, before)

    def test_reuse_and_duplicates(self):
        args = ([('u', 1, 'a'), ('u', 1, 'a')], [('z', 'u', 3), ('a', 'u', 2)], 5)
        before = deepcopy(args)
        self.assertEqual(attribute_last_touch(*args), [('a', 'a'), ('z', 'a')])
        self.assertEqual(args, before)

    def test_tie_reversed(self):
        args = ([('u', 7, 'a'), ('u', 7, 'z')], [('c', 'u', 7)], 0)
        before = deepcopy(args)
        self.assertEqual(attribute_last_touch(*args), [('c', 'a')])
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
