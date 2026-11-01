"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import latest_consent
else:
    from main import latest_consent


class TestCases(unittest.TestCase):

    def test_latest_per_purpose(self):
        args = ([('u1', 'ads', 4, True), ('u1', 'ads', 9, False), ('u1', 'email', 5, True)], 10)
        before = deepcopy(args)
        self.assertEqual(latest_consent(*args), [('u1', 'ads', 9, False), ('u1', 'email', 5, True)])
        self.assertEqual(args, before)

    def test_revocation_wins_tie(self):
        args = ([('u1', 'ads', 7, False), ('u1', 'ads', 7, True)], 7)
        before = deepcopy(args)
        self.assertEqual(latest_consent(*args), [('u1', 'ads', 7, False)])
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], 10)
        before = deepcopy(args)
        self.assertEqual(latest_consent(*args), [])
        self.assertEqual(args, before)

    def test_only_future(self):
        args = ([('u', 'ads', 11, True)], 10)
        before = deepcopy(args)
        self.assertEqual(latest_consent(*args), [])
        self.assertEqual(args, before)

    def test_as_of_inclusive(self):
        args = ([('u', 'ads', 10, True), ('u', 'ads', 11, False)], 10)
        before = deepcopy(args)
        self.assertEqual(latest_consent(*args), [('u', 'ads', 10, True)])
        self.assertEqual(args, before)

    def test_later_grant_after_revocation(self):
        args = ([('u', 'ads', 9, True), ('u', 'ads', 2, False)], 9)
        before = deepcopy(args)
        self.assertEqual(latest_consent(*args), [('u', 'ads', 9, True)])
        self.assertEqual(args, before)

    def test_sorted_users_and_purposes(self):
        args = ([('z', 'ads', 1, True), ('a', 'email', 2, False), ('a', 'ads', 3, True)], 5)
        before = deepcopy(args)
        self.assertEqual(latest_consent(*args), [('a', 'ads', 3, True), ('a', 'email', 2, False), ('z', 'ads', 1, True)])
        self.assertEqual(args, before)

    def test_duplicate_replay(self):
        args = ([('u', 'ads', 0, False), ('u', 'ads', 0, False)], 0)
        before = deepcopy(args)
        self.assertEqual(latest_consent(*args), [('u', 'ads', 0, False)])
        self.assertEqual(args, before)

    def test_tie_reversed(self):
        args = ([('u', 'ads', 7, True), ('u', 'ads', 7, False)], 7)
        before = deepcopy(args)
        self.assertEqual(latest_consent(*args), [('u', 'ads', 7, False)])
        self.assertEqual(args, before)

    def test_large_timestamp(self):
        args = ([('u', 'ads', 1000000000000, True)], 1000000000000)
        before = deepcopy(args)
        self.assertEqual(latest_consent(*args), [('u', 'ads', 1000000000000, True)])
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
