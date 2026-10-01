"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import reconstruct_trace


class TestCases(unittest.TestCase):
    def test_simple_trace(self):
        args = ([('extract', 'validate'), ('validate', 'publish')], 'extract')
        before = deepcopy(args)
        expected = ['extract', 'validate', 'publish']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_lexicographic(self):
        args = ([('A', 'C'), ('A', 'B'), ('B', 'A'), ('C', 'A')], 'A')
        before = deepcopy(args)
        expected = ['A', 'B', 'A', 'C', 'A']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], 'start')
        before = deepcopy(args)
        expected = ['start']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_duplicate_edges(self):
        args = ([('A', 'B'), ('A', 'B'), ('B', 'A')], 'A')
        before = deepcopy(args)
        expected = ['A', 'B', 'A', 'B']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_self_loop(self):
        args = ([('A', 'A')], 'A')
        before = deepcopy(args)
        expected = ['A', 'A']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_dead_end_requires_postorder(self):
        args = ([('J', 'K'), ('J', 'N'), ('N', 'J')], 'J')
        before = deepcopy(args)
        expected = ['J', 'N', 'J', 'K']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_disconnected(self):
        args = ([('A', 'B'), ('C', 'D')], 'A')
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            reconstruct_trace(*args)
        self.assertEqual(args, before)

    def test_wrong_start(self):
        args = ([('A', 'B')], 'B')
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            reconstruct_trace(*args)
        self.assertEqual(args, before)

    def test_invalid_branch(self):
        args = ([('A', 'B'), ('A', 'C')], 'A')
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            reconstruct_trace(*args)
        self.assertEqual(args, before)

    def test_impossible_degrees(self):
        args = ([('A', 'B'), ('B', 'A'), ('A', 'C'), ('B', 'C')], 'A')
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            reconstruct_trace(*args)
        self.assertEqual(args, before)

    def test_long_chain(self):
        edges = [(str(i), str(i + 1)) for i in range(2000)]
        self.assertEqual(reconstruct_trace(edges, "0"), [str(i) for i in range(2001)])


if __name__ == "__main__":
    unittest.main()
