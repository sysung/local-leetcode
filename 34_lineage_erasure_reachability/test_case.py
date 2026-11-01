"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import erasure_scope
else:
    from main import erasure_scope


class TestCases(unittest.TestCase):

    def test_transitive_downstream(self):
        args = ([('raw', 'profiles'), ('profiles', 'audience'), ('raw', 'audit')], ['raw'])
        before = deepcopy(args)
        self.assertEqual(erasure_scope(*args), ['audience', 'audit', 'profiles', 'raw'])
        self.assertEqual(args, before)

    def test_cycle(self):
        args = ([('a', 'b'), ('b', 'c'), ('c', 'a')], ['b'])
        before = deepcopy(args)
        self.assertEqual(erasure_scope(*args), ['a', 'b', 'c'])
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], [])
        before = deepcopy(args)
        self.assertEqual(erasure_scope(*args), [])
        self.assertEqual(args, before)

    def test_unknown_root(self):
        args = ([], ['missing'])
        before = deepcopy(args)
        self.assertEqual(erasure_scope(*args), ['missing'])
        self.assertEqual(args, before)

    def test_direction_matters(self):
        args = ([('raw', 'report')], ['report'])
        before = deepcopy(args)
        self.assertEqual(erasure_scope(*args), ['report'])
        self.assertEqual(args, before)

    def test_no_roots(self):
        args = ([('a', 'b')], [])
        before = deepcopy(args)
        self.assertEqual(erasure_scope(*args), [])
        self.assertEqual(args, before)

    def test_self_edge(self):
        args = ([('a', 'a')], ['a'])
        before = deepcopy(args)
        self.assertEqual(erasure_scope(*args), ['a'])
        self.assertEqual(args, before)

    def test_duplicates(self):
        args = ([('a', 'b'), ('a', 'b')], ['a', 'a'])
        before = deepcopy(args)
        self.assertEqual(erasure_scope(*args), ['a', 'b'])
        self.assertEqual(args, before)

    def test_multiple_roots(self):
        args = ([('a', 'c'), ('b', 'c'), ('c', 'd')], ['b', 'a', 'orphan'])
        before = deepcopy(args)
        self.assertEqual(erasure_scope(*args), ['a', 'b', 'c', 'd', 'orphan'])
        self.assertEqual(args, before)

    def test_disconnected_branch(self):
        args = ([('a', 'b'), ('x', 'y')], ['a'])
        before = deepcopy(args)
        self.assertEqual(erasure_scope(*args), ['a', 'b'])
        self.assertEqual(args, before)

    def test_diamond(self):
        args = ([('a', 'b'), ('a', 'c'), ('b', 'd'), ('c', 'd')], ['a'])
        before = deepcopy(args)
        self.assertEqual(erasure_scope(*args), ['a', 'b', 'c', 'd'])
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
