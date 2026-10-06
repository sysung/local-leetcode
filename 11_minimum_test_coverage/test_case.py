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


    def test_both_inputs_empty(self):
        args = ([], set())
        before = deepcopy(args)
        expected = None
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_all_events_required(self):
        args = (['A', 'B', 'C'], {'C', 'A', 'B'})
        before = deepcopy(args)
        expected = (0, 2)
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_best_window_at_end(self):
        args = (['X', 'A', 'X', 'B', 'A'], {'A', 'B'})
        before = deepcopy(args)
        expected = (3, 4)
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_later_shorter_window_wins(self):
        args = (['A', 'X', 'X', 'B', 'A'], {'A', 'B'})
        before = deepcopy(args)
        expected = (3, 4)
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_redundant_codes_inside_coverage(self):
        args = (['A', 'A', 'B', 'B', 'C'], {'C', 'A', 'B'})
        before = deepcopy(args)
        expected = (1, 4)
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_more_requirements_than_events(self):
        args = (['A'], {'A', 'B'})
        before = deepcopy(args)
        expected = None
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_case_sensitive_codes(self):
        args = (['a', 'B', 'A'], {'A', 'B'})
        before = deepcopy(args)
        expected = (1, 2)
        self.assertEqual(minimum_test_coverage(*args), expected)
        self.assertEqual(args, before)

    def test_maximum_complete_coverage(self):
        codes = [str(i) for i in range(100000)]
        required = {str(i) for i in range(90000, 100000)}
        self.assertEqual(minimum_test_coverage(codes, required), (90000, 99999))
        self.assertEqual(codes[0], "0")

    def test_maximum_repeated_coverage(self):
        codes = ["A", "B"] * 50000
        self.assertEqual(minimum_test_coverage(codes, {"A", "B"}), (0, 1))

    def test_maximum_impossible_coverage(self):
        self.assertIsNone(minimum_test_coverage(["X"] * 100000, {"A", "B"}))

    def test_exhaustive_small_sequence_oracle(self):
        import itertools
        for length in range(5):
            for sequence in itertools.product("ABX", repeat=length):
                codes = list(sequence)
                candidates = [(end - start + 1, start, end) for start in range(length) for end in range(start, length) if {"A", "B"} <= set(codes[start:end + 1])]
                expected = min(candidates)[1:] if candidates else None
                with self.subTest(sequence=sequence):
                    self.assertEqual(minimum_test_coverage(codes, {"A", "B"}), expected)


if __name__ == "__main__":
    unittest.main()
