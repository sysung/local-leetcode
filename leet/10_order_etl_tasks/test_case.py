"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import order_tasks


class TestCases(unittest.TestCase):
    def test_pipeline(self):
        args = ({'extract': [], 'publish': ['transform'], 'transform': ['extract']},)
        before = deepcopy(args)
        expected = ['extract', 'transform', 'publish']
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_alphabetical_choice(self):
        args = ({'b': ['a'], 'c': [], 'z': []},)
        before = deepcopy(args)
        expected = ['a', 'b', 'c', 'z']
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ({},)
        before = deepcopy(args)
        expected = []
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_duplicate_dependencies(self):
        args = ({'b': ['a', 'a']},)
        before = deepcopy(args)
        expected = ['a', 'b']
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_diamond(self):
        args = ({'b': ['a'], 'c': ['a'], 'd': ['b', 'c']},)
        before = deepcopy(args)
        expected = ['a', 'b', 'c', 'd']
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_cycle(self):
        args = ({'a': ['b'], 'b': ['a']},)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            order_tasks(*args)
        self.assertEqual(args, before)

    def test_self_cycle(self):
        args = ({'a': ['a']},)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            order_tasks(*args)
        self.assertEqual(args, before)

    def test_partial_cycle(self):
        args = ({'a': ['b'], 'b': ['a'], 'x': []},)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            order_tasks(*args)
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
