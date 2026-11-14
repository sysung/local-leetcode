"""Visible tests import the learner implementation, never the reference."""
import unittest

if __package__:
    from .main import count_target_ranges
else:
    from main import count_target_ranges


class TestCases(unittest.TestCase):
    def test_negative_adjustments(self):
        self.assertEqual(count_target_ranges([1, -1, 1], 1), 3)

    def test_zero_multiplicity(self):
        self.assertEqual(count_target_ranges([0, 0, 0], 0), 6)

    def test_empty_and_missing(self):
        self.assertEqual(count_target_ranges([], 0), 0)
        self.assertEqual(count_target_ranges([2, 4], 3), 0)

    def test_negative_target(self):
        self.assertEqual(count_target_ranges([-2, -1, 3, -2], -3), 1)

    def test_no_mutation(self):
        values = [2, -2, 2]
        self.assertEqual(count_target_ranges(values, 2), 3)
        self.assertEqual(values, [2, -2, 2])

    def test_small_exhaustive(self):
        from itertools import product
        for size in range(5):
            for values in product((-1, 0, 1), repeat=size):
                for target in range(-2, 3):
                    expected = sum(sum(values[i:j]) == target for i in range(size) for j in range(i+1, size+1))
                    self.assertEqual(count_target_ranges(list(values), target), expected)


if __name__ == "__main__":
    unittest.main()
