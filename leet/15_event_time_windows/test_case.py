"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import aggregate_event_time


class TestCases(unittest.TestCase):
    def test_out_of_order(self):
        args = ([(7, 'a', 'PASS'), (3, 'a', 'FAIL'), (16, 'a', 'PASS'), (4, 'a', 'FAIL')], 10, 5)
        before = deepcopy(args)
        expected = ([(0, 'a', 2, 1), (10, 'a', 1, 0)], [3])
        self.assertEqual(aggregate_event_time(*args), expected)
        self.assertEqual(args, before)

    def test_watermark_equality(self):
        args = ([(10, 'b', 'PASS'), (5, 'a', 'FAIL'), (4, 'a', 'PASS')], 5, 5)
        before = deepcopy(args)
        expected = ([(5, 'a', 1, 1), (10, 'b', 1, 0)], [2])
        self.assertEqual(aggregate_event_time(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], 10, 0)
        before = deepcopy(args)
        expected = ([], [])
        self.assertEqual(aggregate_event_time(*args), expected)
        self.assertEqual(args, before)

    def test_fixed_boundaries(self):
        args = ([(0, 'a', 'PASS'), (9, 'a', 'FAIL'), (10, 'a', 'PASS')], 10, 0)
        before = deepcopy(args)
        expected = ([(0, 'a', 2, 1), (10, 'a', 1, 0)], [])
        self.assertEqual(aggregate_event_time(*args), expected)
        self.assertEqual(args, before)

    def test_device_order(self):
        args = ([(1, 'z', 'FAIL'), (1, 'a', 'PASS')], 10, 0)
        before = deepcopy(args)
        expected = ([(0, 'a', 1, 0), (0, 'z', 1, 1)], [])
        self.assertEqual(aggregate_event_time(*args), expected)
        self.assertEqual(args, before)

    def test_large_lateness_flush(self):
        args = ([(20, 'a', 'PASS'), (0, 'a', 'FAIL')], 10, 100)
        before = deepcopy(args)
        expected = ([(0, 'a', 1, 1), (20, 'a', 1, 0)], [])
        self.assertEqual(aggregate_event_time(*args), expected)
        self.assertEqual(args, before)

    def test_repeated_arrivals(self):
        args = ([(0, 'a', 'FAIL'), (0, 'a', 'FAIL')], 1, 0)
        before = deepcopy(args)
        expected = ([(0, 'a', 2, 2)], [])
        self.assertEqual(aggregate_event_time(*args), expected)
        self.assertEqual(args, before)

    def test_zero_lateness(self):
        args = ([(2, 'a', 'PASS'), (1, 'a', 'FAIL'), (2, 'a', 'FAIL')], 10, 0)
        before = deepcopy(args)
        expected = ([(0, 'a', 2, 1)], [1])
        self.assertEqual(aggregate_event_time(*args), expected)
        self.assertEqual(args, before)

    def test_invalid_size(self):
        args = ([], 0, 1)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            aggregate_event_time(*args)
        self.assertEqual(args, before)

    def test_invalid_lateness(self):
        args = ([], 1, -1)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            aggregate_event_time(*args)
        self.assertEqual(args, before)

    def test_negative_timestamp(self):
        args = ([(-1, 'a', 'PASS')], 10, 0)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            aggregate_event_time(*args)
        self.assertEqual(args, before)

    def test_one_shot_iterable(self):
        events = iter([(0, "a", "FAIL"), (10, "a", "PASS")])
        self.assertEqual(aggregate_event_time(events, 10, 0), ([(0, "a", 1, 1), (10, "a", 1, 0)], []))


if __name__ == "__main__":
    unittest.main()
