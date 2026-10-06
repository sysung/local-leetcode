"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import sliding_medians
else:
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


    def test_single_reading_returns_float(self):
        result = sliding_medians([7], 1)
        self.assertEqual(result, [7.0])
        self.assertIs(type(result[0]), float)

    def test_alternating_extreme_values(self):
        args = ([-1000000000, 1000000000, -1000000000, 1000000000], 2)
        before = deepcopy(args)
        expected = [0.0, 0.0, 0.0]
        self.assertEqual(sliding_medians(*args), expected)
        self.assertEqual(args, before)

    def test_duplicate_values_cross_heap_boundary(self):
        args = ([2, 2, 1, 1, 2, 2], 3)
        before = deepcopy(args)
        expected = [2.0, 1.0, 1.0, 2.0]
        self.assertEqual(sliding_medians(*args), expected)
        self.assertEqual(args, before)

    def test_whole_input_odd(self):
        args = ([5, 1, 3, 2, 4], 5)
        before = deepcopy(args)
        expected = [3.0]
        self.assertEqual(sliding_medians(*args), expected)
        self.assertEqual(args, before)

    def test_descending_even_windows(self):
        args = ([6, 5, 4, 3, 2, 1], 4)
        before = deepcopy(args)
        expected = [4.5, 3.5, 2.5]
        self.assertEqual(sliding_medians(*args), expected)
        self.assertEqual(args, before)

    def test_maximum_constant_input(self):
        values = [0] * 100000
        self.assertEqual(sliding_medians(values, 501), [0.0] * 99500)
        self.assertEqual(values.count(0), 100000)

    def test_maximum_increasing_large_window(self):
        values = list(range(100000))
        self.assertEqual(sliding_medians(values, 50001), [float(i) for i in range(25000, 75000)])
        self.assertEqual(values[0], 0)
        self.assertEqual(values[-1], 99999)

    def test_maximum_decreasing_large_even_window(self):
        values = list(range(100000, 0, -1))
        self.assertEqual(sliding_medians(values, 50000), [75000.5 - i for i in range(50001)])
        self.assertEqual(values[0], 100000)


if __name__ == "__main__":
    unittest.main()
