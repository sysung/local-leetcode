"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import minimum_test_coverage


class TestCases(unittest.TestCase):
    def test_shortest(self):
        args = (['A', 'X', 'B', 'A', 'C', 'B'], {'C', 'B', 'A'})
        before = deepcopy(args)
        expected = (2, 4)
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_duplicates(self):
        args = (['A', 'A', 'B'], {'B', 'A'})
        before = deepcopy(args)
        expected = (1, 2)
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_empty_requirements(self):
        args = (['A'], set())
        before = deepcopy(args)
        expected = None
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_empty_codes(self):
        args = ([], {'A'})
        before = deepcopy(args)
        expected = None
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_missing_code(self):
        args = (['A', 'B'], {'C', 'A'})
        before = deepcopy(args)
        expected = None
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_single_required(self):
        args = (['X', 'A', 'A'], {'A'})
        before = deepcopy(args)
        expected = (1, 1)
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_earliest_tie(self):
        args = (['A', 'B', 'A', 'B'], {'B', 'A'})
        before = deepcopy(args)
        expected = (0, 1)
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_irrelevant_prefix(self):
        args = (['X', 'Y', 'A', 'B', 'Z'], {'B', 'A'})
        before = deepcopy(args)
        expected = (2, 3)
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_large_redundant_prefix(self):
        self.assertEqual(minimum_test_coverage(["A"] * 10000 + ["B"], {"A", "B"}), (9999, 10000))


if __name__ == "__main__":
    unittest.main()
