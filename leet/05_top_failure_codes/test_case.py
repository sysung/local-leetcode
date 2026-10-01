"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import top_failure_codes


class TestCases(unittest.TestCase):
    def test_frequency(self):
        args = (['ECC', 'TEMP', 'ECC', 'POWER'], 2)
        before = deepcopy(args)
        expected = [('ECC', 2), ('POWER', 1)]
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_all_tied(self):
        args = (['Z', 'A', 'B'], 5)
        before = deepcopy(args)
        expected = [('A', 1), ('B', 1), ('Z', 1)]
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], 3)
        before = deepcopy(args)
        expected = []
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_zero_k(self):
        args = (['A'], 0)
        before = deepcopy(args)
        expected = []
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_negative_k(self):
        args = (['A'], -2)
        before = deepcopy(args)
        expected = []
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_one_code(self):
        args = (['A', 'A', 'A'], 1)
        before = deepcopy(args)
        expected = [('A', 3)]
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
