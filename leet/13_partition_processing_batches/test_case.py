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


    def test_negative_batch_count(self):
        args = ([1, 2], -1)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            minimize_max_batch_load(*args)
        self.assertEqual(args, before)

    def test_negative_last_load(self):
        args = ([0, 0, -1], 1)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            minimize_max_batch_load(*args)
        self.assertEqual(args, before)

    def test_single_zero_load(self):
        args = ([0], 1)
        before = deepcopy(args)
        expected = 0
        self.assertEqual(minimize_max_batch_load(*args), expected)
        self.assertEqual(args, before)

    def test_dominant_individual_load(self):
        args = ([1, 1000000000, 1], 3)
        before = deepcopy(args)
        expected = 1000000000
        self.assertEqual(minimize_max_batch_load(*args), expected)
        self.assertEqual(args, before)

    def test_balanced_uneven_values(self):
        args = ([8, 1, 1, 8], 2)
        before = deepcopy(args)
        expected = 9
        self.assertEqual(minimize_max_batch_load(*args), expected)
        self.assertEqual(args, before)

    def test_maximum_uniform_workloads(self):
        loads = [1] * 100000
        self.assertEqual(minimize_max_batch_load(loads, 1000), 100)
        self.assertEqual(loads.count(1), 100000)

    def test_large_integer_total(self):
        self.assertEqual(minimize_max_batch_load([10**9] * 100000, 100), 10**12)

    def test_nearly_one_batch_per_item(self):
        self.assertEqual(minimize_max_batch_load([1] * 100000, 99999), 2)

    def test_maximum_mostly_zero_workloads(self):
        self.assertEqual(minimize_max_batch_load([0] * 99999 + [10**9], 50000), 10**9)

    def test_exhaustive_small_partition_oracle(self):
        import itertools
        for length in range(1, 6):
            for sequence in itertools.product(range(3), repeat=length):
                loads = list(sequence)
                for batch_count in range(1, length + 1):
                    candidates = []
                    for cuts in itertools.combinations(range(1, length), batch_count - 1):
                        boundaries = (0, *cuts, length)
                        candidates.append(max(sum(loads[start:end]) for start, end in zip(boundaries, boundaries[1:])))
                    with self.subTest(loads=loads, batch_count=batch_count):
                        self.assertEqual(minimize_max_batch_load(loads, batch_count), min(candidates))


if __name__ == "__main__":
    unittest.main()
