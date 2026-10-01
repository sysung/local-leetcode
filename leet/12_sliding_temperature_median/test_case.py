"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import sliding_medians


class TestCases(unittest.TestCase):
    def test_odd_windows(self):
        args = ([1, 3, -1, -3, 5, 3, 6, 7], 3)
        before = deepcopy(args)
        expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
        self.assertEqual(sliding_medians(*args), expected)
        self.assertEqual(args, before)

    def test_even_windows(self):
        args = ([10, 20, 30, 40], 2)
        before = deepcopy(args)
        expected = [15.0, 25.0, 35.0]
        self.assertEqual(sliding_medians(*args), expected)
        self.assertEqual(args, before)

    def test_duplicates(self):
        args = ([5, 5, 5, 5], 3)
        before = deepcopy(args)
        expected = [5.0, 5.0]
        self.assertEqual(sliding_medians(*args), expected)
        self.assertEqual(args, before)

    def test_k_one(self):
        args = ([3, -2, 8], 1)
        before = deepcopy(args)
        expected = [3.0, -2.0, 8.0]
        self.assertEqual(sliding_medians(*args), expected)
        self.assertEqual(args, before)

    def test_whole_input(self):
        args = ([9, 1, 4, 2], 4)
        before = deepcopy(args)
        expected = [3.0]
        self.assertEqual(sliding_medians(*args), expected)
        self.assertEqual(args, before)

    def test_negative_readings(self):
        args = ([-5, -1, -3], 2)
        before = deepcopy(args)
        expected = [-3.0, -2.0]
        self.assertEqual(sliding_medians(*args), expected)
        self.assertEqual(args, before)

    def test_zero_k(self):
        args = ([1], 0)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            sliding_medians(*args)
        self.assertEqual(args, before)

    def test_oversized_k(self):
        args = ([1, 2], 3)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            sliding_medians(*args)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], 1)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            sliding_medians(*args)
        self.assertEqual(args, before)

    def test_negative_k(self):
        args = ([1], -1)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            sliding_medians(*args)
        self.assertEqual(args, before)

    def test_long_monotonic_sequences(self):
        self.assertEqual(sliding_medians(list(range(2000)), 5), [float(x) for x in range(2, 1998)])
        self.assertEqual(sliding_medians(list(range(2000, 0, -1)), 5), [float(x) for x in range(1998, 2, -1)])

    def test_against_small_sorted_window_oracle(self):
        import random
        rng = random.Random(12)
        values = [rng.randrange(-10, 11) for _ in range(60)]
        for k in range(1, 16):
            expected = []
            for start in range(len(values) - k + 1):
                window = sorted(values[start:start + k])
                expected.append((window[(k - 1) // 2] + window[k // 2]) / 2.0)
            with self.subTest(k=k):
                self.assertEqual(sliding_medians(values, k), expected)


if __name__ == "__main__":
    unittest.main()
