"""Visible tests import the learner implementation, never the reference."""
import unittest

if __package__:
    from .main import max_area
else:
    from main import max_area


class TestCases(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_small_inputs(self):
        self.assertEqual(max_area([]), 0)
        self.assertEqual(max_area([5]), 0)
        self.assertEqual(max_area([4, 7]), 4)

    def test_equal_and_zero_heights(self):
        self.assertEqual(max_area([5, 5, 5]), 10)
        self.assertEqual(max_area([0, 0, 0]), 0)

    def test_no_mutation(self):
        heights = [9, 1, 1, 9]
        self.assertEqual(max_area(heights), 27)
        self.assertEqual(heights, [9, 1, 1, 9])

    def test_large_integer_area(self):
        self.assertEqual(max_area([10**9, 0, 10**9]), 2 * 10**9)

    def test_small_exhaustive(self):
        from itertools import product
        for size in range(6):
            for heights in product(range(3), repeat=size):
                expected = max((min(heights[i], heights[j]) * (j-i) for i in range(size) for j in range(i+1, size)), default=0)
                self.assertEqual(max_area(list(heights)), expected)


if __name__ == "__main__":
    unittest.main()
