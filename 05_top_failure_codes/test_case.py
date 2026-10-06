"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import top_failure_codes
else:
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


    def test_k_one_frequency_wins(self):
        args = (['A', 'Z', 'Z'], 1)
        before = deepcopy(args)
        expected = [('Z', 2)]
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_k_one_tie(self):
        args = (['Z', 'A'], 1)
        before = deepcopy(args)
        expected = [('A', 1)]
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_tie_at_cutoff(self):
        args = (['D', 'B', 'C', 'A'], 2)
        before = deepcopy(args)
        expected = [('A', 1), ('B', 1)]
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_descending_counts(self):
        args = (['A', 'B', 'B', 'C', 'C', 'C'], 3)
        before = deepcopy(args)
        expected = [('C', 3), ('B', 2), ('A', 1)]
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_case_sensitive_order(self):
        args = (['a', 'A', 'a', 'A', 'B'], 3)
        before = deepcopy(args)
        expected = [('A', 2), ('a', 2), ('B', 1)]
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_unicode_ties(self):
        args = (['Ω', 'é', 'A'], 3)
        before = deepcopy(args)
        expected = [('A', 1), ('é', 1), ('Ω', 1)]
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_numeric_code_order(self):
        args = (['2', '10', '1'], 3)
        before = deepcopy(args)
        expected = [('1', 1), ('10', 1), ('2', 1)]
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_large_k_single_code(self):
        args = (['A', 'A'], 1000000000)
        before = deepcopy(args)
        expected = [('A', 2)]
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_empty_zero_k(self):
        args = ([], 0)
        before = deepcopy(args)
        expected = []
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_punctuation_codes(self):
        args = (['TEMP:HIGH', 'ECC_ERR', 'TEMP:HIGH'], 2)
        before = deepcopy(args)
        expected = [('TEMP:HIGH', 2), ('ECC_ERR', 1)]
        self.assertEqual(top_failure_codes(*args), expected)
        self.assertEqual(args, before)

    def test_maximum_distinct_codes_small_k(self):
        codes = [f"C{i:06d}" for i in range(99999, -1, -1)]
        self.assertEqual(top_failure_codes(codes, 5), [(f"C{i:06d}", 1) for i in range(5)])
        self.assertEqual(codes[0], "C099999")

    def test_maximum_hot_code(self):
        self.assertEqual(top_failure_codes(["ECC"] * 100000, 1), [("ECC", 100000)])

    def test_maximum_output_cardinality(self):
        codes = [f"C{i:06d}" for i in range(100000)]
        self.assertEqual(top_failure_codes(codes, 100000), [(code, 1) for code in codes])

    def test_large_equal_frequency_groups(self):
        codes = [f"C{i % 1000:04d}" for i in range(100000)]
        self.assertEqual(top_failure_codes(codes, 10), [(f"C{i:04d}", 100) for i in range(10)])


if __name__ == "__main__":
    unittest.main()
