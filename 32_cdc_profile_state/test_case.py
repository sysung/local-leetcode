"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import materialize_profiles
else:
    from main import materialize_profiles


class TestCases(unittest.TestCase):

    def test_out_of_order_and_delete(self):
        args = ([('a', 2, 'upsert', 'new'), ('a', 1, 'upsert', 'old'), ('b', 4, 'delete', None), ('b', 3, 'upsert', 'stale')],)
        before = deepcopy(args)
        self.assertEqual(materialize_profiles(*args), [('a', 2, 'new')])
        self.assertEqual(args, before)

    def test_same_version_conflicts(self):
        args = ([('a', 1, 'upsert', 'A'), ('a', 1, 'upsert', 'Z'), ('b', 2, 'upsert', 'x'), ('b', 2, 'delete', None)],)
        before = deepcopy(args)
        self.assertEqual(materialize_profiles(*args), [('a', 1, 'Z')])
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([],)
        before = deepcopy(args)
        self.assertEqual(materialize_profiles(*args), [])
        self.assertEqual(args, before)

    def test_delete_without_upsert(self):
        args = ([('a', 1, 'delete', None)],)
        before = deepcopy(args)
        self.assertEqual(materialize_profiles(*args), [])
        self.assertEqual(args, before)

    def test_recreate_after_delete(self):
        args = ([('a', 2, 'delete', None), ('a', 3, 'upsert', 'back')],)
        before = deepcopy(args)
        self.assertEqual(materialize_profiles(*args), [('a', 3, 'back')])
        self.assertEqual(args, before)

    def test_version_beats_value(self):
        args = ([('a', 1, 'upsert', 'z'), ('a', 2, 'upsert', 'a')],)
        before = deepcopy(args)
        self.assertEqual(materialize_profiles(*args), [('a', 2, 'a')])
        self.assertEqual(args, before)

    def test_duplicate_replay(self):
        args = ([('a', 1, 'upsert', 'x'), ('a', 1, 'upsert', 'x'), ('a', 1, 'upsert', 'x')],)
        before = deepcopy(args)
        self.assertEqual(materialize_profiles(*args), [('a', 1, 'x')])
        self.assertEqual(args, before)

    def test_empty_value_and_version_zero(self):
        args = ([('a', 0, 'upsert', '')],)
        before = deepcopy(args)
        self.assertEqual(materialize_profiles(*args), [('a', 0, '')])
        self.assertEqual(args, before)

    def test_sorted_profiles(self):
        args = ([('z', 1, 'upsert', 'z'), ('a', 2, 'upsert', 'a')],)
        before = deepcopy(args)
        self.assertEqual(materialize_profiles(*args), [('a', 2, 'a'), ('z', 1, 'z')])
        self.assertEqual(args, before)

    def test_delete_tie_reversed(self):
        args = ([('a', 1, 'delete', None), ('a', 1, 'upsert', 'zz')],)
        before = deepcopy(args)
        self.assertEqual(materialize_profiles(*args), [])
        self.assertEqual(args, before)

    def test_upsert_tie_reversed(self):
        args = ([('a', 1, 'upsert', 'z'), ('a', 1, 'upsert', 'a')],)
        before = deepcopy(args)
        self.assertEqual(materialize_profiles(*args), [('a', 1, 'z')])
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
