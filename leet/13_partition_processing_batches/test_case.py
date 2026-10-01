"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import minimize_max_batch_load


class TestCases(unittest.TestCase):
    def test_balanced_split(self):
        args = ([7, 2, 5, 10, 8], 2)
        before = deepcopy(args)
        expected = 18
        self.assertEqual(minimize_max_batch_load(*args), expected)
        self.assertEqual(args, before)

    def test_three_batches(self):
        args = ([1, 2, 3, 4, 5], 3)
        before = deepcopy(args)
        expected = 6
        self.assertEqual(minimize_max_batch_load(*args), expected)
        self.assertEqual(args, before)

    def test_single_batch(self):
        args = ([2, 3, 4], 1)
        before = deepcopy(args)
        expected = 9
        self.assertEqual(minimize_max_batch_load(*args), expected)
        self.assertEqual(args, before)

    def test_one_per_item(self):
        args = ([2, 8, 3], 3)
        before = deepcopy(args)
        expected = 8
        self.assertEqual(minimize_max_batch_load(*args), expected)
        self.assertEqual(args, before)

    def test_all_zero(self):
        args = ([0, 0, 0], 2)
        before = deepcopy(args)
        expected = 0
        self.assertEqual(minimize_max_batch_load(*args), expected)
        self.assertEqual(args, before)

    def test_mixed_zero(self):
        args = ([0, 5, 0, 5], 2)
        before = deepcopy(args)
        expected = 5
        self.assertEqual(minimize_max_batch_load(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], 1)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            minimize_max_batch_load(*args)
        self.assertEqual(args, before)

    def test_zero_batches(self):
        args = ([1], 0)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            minimize_max_batch_load(*args)
        self.assertEqual(args, before)

    def test_too_many_batches(self):
        args = ([1, 2], 3)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            minimize_max_batch_load(*args)
        self.assertEqual(args, before)

    def test_negative_load(self):
        args = ([1, -1], 1)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            minimize_max_batch_load(*args)
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
