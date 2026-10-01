"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import failure_alerts


class TestCases(unittest.TestCase):
    def test_repeated_failure(self):
        args = ([(1, 'a', 'FAIL'), (2, 'a', 'FAIL'), (3, 'a', 'PASS')], 5, 2)
        before = deepcopy(args)
        expected = [(2, 'a', 2), (3, 'a', 2)]
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_exclusive_boundary(self):
        args = ([(0, 'a', 'FAIL'), (5, 'a', 'FAIL')], 5, 2)
        before = deepcopy(args)
        expected = []
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], 3, 1)
        before = deepcopy(args)
        expected = []
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_independent_devices(self):
        args = ([(1, 'a', 'FAIL'), (2, 'b', 'FAIL'), (3, 'a', 'FAIL')], 5, 2)
        before = deepcopy(args)
        expected = [(3, 'a', 2)]
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_simultaneous(self):
        args = ([(1, 'a', 'FAIL'), (1, 'a', 'PASS'), (1, 'a', 'FAIL')], 1, 2)
        before = deepcopy(args)
        expected = [(1, 'a', 2)]
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_all_pass(self):
        args = ([(0, 'a', 'PASS'), (1, 'a', 'PASS')], 2, 1)
        before = deepcopy(args)
        expected = []
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_invalid_window(self):
        args = ([], 0, 1)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            failure_alerts(*args)
        self.assertEqual(args, before)

    def test_invalid_threshold(self):
        args = ([], 1, -1)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            failure_alerts(*args)
        self.assertEqual(args, before)


    def test_negative_window(self):
        args = ([], -1, 1)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            failure_alerts(*args)
        self.assertEqual(args, before)

    def test_zero_threshold(self):
        args = ([], 1, 0)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            failure_alerts(*args)
        self.assertEqual(args, before)

    def test_threshold_above_event_count(self):
        args = ([(0, 'a', 'FAIL'), (1, 'a', 'FAIL')], 10, 3)
        before = deepcopy(args)
        expected = []
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_threshold_one(self):
        args = ([(0, 'a', 'FAIL'), (1, 'a', 'PASS'), (2, 'a', 'FAIL')], 10, 1)
        before = deepcopy(args)
        expected = [(0, 'a', 1), (1, 'a', 1), (2, 'a', 2)]
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_pass_after_expiry(self):
        args = ([(0, 'a', 'FAIL'), (2, 'a', 'PASS')], 2, 1)
        before = deepcopy(args)
        expected = [(0, 'a', 1)]
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_multiple_failures_expire_together(self):
        args = ([(0, 'a', 'FAIL'), (0, 'a', 'FAIL'), (5, 'a', 'PASS')], 5, 2)
        before = deepcopy(args)
        expected = [(0, 'a', 2)]
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_very_large_time_gap(self):
        args = ([(0, 'a', 'FAIL'), (1000000000000000000, 'a', 'FAIL')], 10, 2)
        before = deepcopy(args)
        expected = []
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_count_decreases_but_stays_above_threshold(self):
        args = ([(0, 'a', 'FAIL'), (1, 'a', 'FAIL'), (2, 'a', 'FAIL'), (5, 'a', 'PASS')], 5, 2)
        before = deepcopy(args)
        expected = [(1, 'a', 2), (2, 'a', 3), (5, 'a', 2)]
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_simultaneous_independent_devices(self):
        args = ([(1, 'a', 'FAIL'), (1, 'b', 'FAIL'), (1, 'a', 'FAIL'), (1, 'b', 'FAIL')], 1, 2)
        before = deepcopy(args)
        expected = [(1, 'a', 2), (1, 'b', 2)]
        self.assertEqual(failure_alerts(*args), expected)
        self.assertEqual(args, before)

    def test_maximum_dense_failure_batch(self):
        events = [(i, "a", "FAIL") for i in range(100000)]
        self.assertEqual(failure_alerts(events, 100000, 99999), [(99998, "a", 99999), (99999, "a", 100000)])
        self.assertEqual(events[0], (0, "a", "FAIL"))

    def test_maximum_sparse_failure_batch(self):
        events = [(i * 10, "a", "FAIL") for i in range(100000)]
        self.assertEqual(failure_alerts(events, 1, 2), [])

    def test_maximum_device_churn(self):
        events = [(i, str(i), "FAIL") for i in range(100000)]
        self.assertEqual(failure_alerts(events, 1, 1), [(i, str(i), 1) for i in range(100000)])


if __name__ == "__main__":
    unittest.main()
