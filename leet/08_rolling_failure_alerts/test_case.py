"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import failure_alerts


class TestCases(unittest.TestCase):
    def test_repeated_failure(self):
        args = ([(1, 'a', 'FAIL'), (2, 'a', 'FAIL'), (3, 'a', 'PASS')], 5, 2)
        before = deepcopy(args)
        expected = [(2, 'a', 2), (3, 'a', 2)]
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_exclusive_boundary(self):
        args = ([(0, 'a', 'FAIL'), (5, 'a', 'FAIL')], 5, 2)
        before = deepcopy(args)
        expected = []
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], 3, 1)
        before = deepcopy(args)
        expected = []
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_independent_devices(self):
        args = ([(1, 'a', 'FAIL'), (2, 'b', 'FAIL'), (3, 'a', 'FAIL')], 5, 2)
        before = deepcopy(args)
        expected = [(3, 'a', 2)]
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_simultaneous(self):
        args = ([(1, 'a', 'FAIL'), (1, 'a', 'PASS'), (1, 'a', 'FAIL')], 1, 2)
        before = deepcopy(args)
        expected = [(1, 'a', 2)]
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_all_pass(self):
        args = ([(0, 'a', 'PASS'), (1, 'a', 'PASS')], 2, 1)
        before = deepcopy(args)
        expected = []
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_invalid_window(self):
        args = ([], 0, 1)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            failure_alerts(*args)
        self.assertEqual(args, before)

    def test_invalid_threshold(self):
        args = ([], 1, -1)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            failure_alerts(*args)
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
