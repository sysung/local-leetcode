"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import resolve_identities
else:
    from main import resolve_identities


class TestCases(unittest.TestCase):

    def test_transitive_identity(self):
        args = ([('email:a', 'cookie:b'), ('customer:c', 'email:a'), ('orphan', 'orphan')],)
        before = deepcopy(args)
        self.assertEqual(resolve_identities(*args), [('cookie:b', 'cookie:b'), ('customer:c', 'cookie:b'), ('email:a', 'cookie:b'), ('orphan', 'orphan')])
        self.assertEqual(args, before)

    def test_separate_components(self):
        args = ([('z', 'y'), ('b', 'b'), ('a', 'a')],)
        before = deepcopy(args)
        self.assertEqual(resolve_identities(*args), [('a', 'a'), ('b', 'b'), ('y', 'y'), ('z', 'y')])
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([],)
        before = deepcopy(args)
        self.assertEqual(resolve_identities(*args), [])
        self.assertEqual(args, before)

    def test_isolated_duplicates(self):
        args = ([('b', 'b'), ('a', 'a'), ('b', 'b')],)
        before = deepcopy(args)
        self.assertEqual(resolve_identities(*args), [('a', 'a'), ('b', 'b')])
        self.assertEqual(args, before)

    def test_link_endpoints(self):
        args = ([('b', 'a')],)
        before = deepcopy(args)
        self.assertEqual(resolve_identities(*args), [('a', 'a'), ('b', 'a')])
        self.assertEqual(args, before)

    def test_cycles(self):
        args = ([('c', 'b'), ('b', 'a'), ('a', 'c')],)
        before = deepcopy(args)
        self.assertEqual(resolve_identities(*args), [('a', 'a'), ('b', 'a'), ('c', 'a')])
        self.assertEqual(args, before)

    def test_self_link(self):
        args = ([('u', 'u')],)
        before = deepcopy(args)
        self.assertEqual(resolve_identities(*args), [('u', 'u')])
        self.assertEqual(args, before)

    def test_duplicate_reversed_links(self):
        args = ([('c', 'c'), ('b', 'a'), ('a', 'b'), ('b', 'a')],)
        before = deepcopy(args)
        self.assertEqual(resolve_identities(*args), [('a', 'a'), ('b', 'a'), ('c', 'c')])
        self.assertEqual(args, before)

    def test_python_lexical_order(self):
        args = ([('id:2', 'id:10')],)
        before = deepcopy(args)
        self.assertEqual(resolve_identities(*args), [('id:10', 'id:10'), ('id:2', 'id:10')])
        self.assertEqual(args, before)

    def test_chain(self):
        args = ([('d', 'c'), ('c', 'b'), ('b', 'a')],)
        before = deepcopy(args)
        self.assertEqual(resolve_identities(*args), [('a', 'a'), ('b', 'a'), ('c', 'a'), ('d', 'a')])
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
