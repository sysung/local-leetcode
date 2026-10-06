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


    def test_negative_window_size(self):
        args = ([], -1, 0)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            aggregate_event_time(*args)
        self.assertEqual(args, before)

    def test_negative_timestamp_must_not_be_treated_as_late(self):
        args = ([(10, 'a', 'PASS'), (-1, 'a', 'FAIL')], 10, 0)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            aggregate_event_time(*args)
        self.assertEqual(args, before)

    def test_unit_windows(self):
        args = ([(0, 'a', 'PASS'), (0, 'a', 'FAIL'), (1, 'a', 'FAIL')], 1, 0)
        before = deepcopy(args)
        expected = ([(0, 'a', 2, 1), (1, 'a', 1, 1)], [])
        self.assertEqual(aggregate_event_time(*args), expected)
        self.assertEqual(args, before)

    def test_repeated_late_events_do_not_count(self):
        args = ([(10, 'a', 'PASS'), (0, 'a', 'FAIL'), (0, 'a', 'FAIL')], 10, 0)
        before = deepcopy(args)
        expected = ([(10, 'a', 1, 0)], [1, 2])
        self.assertEqual(aggregate_event_time(*args), expected)
        self.assertEqual(args, before)

    def test_closed_window_cannot_be_reopened(self):
        args = ([(0, 'a', 'FAIL'), (15, 'a', 'PASS'), (10, 'b', 'FAIL'), (9, 'a', 'FAIL')], 10, 5)
        before = deepcopy(args)
        expected = ([(0, 'a', 1, 1), (10, 'a', 1, 0), (10, 'b', 1, 1)], [3])
        self.assertEqual(aggregate_event_time(*args), expected)
        self.assertEqual(args, before)

    def test_maximum_sequential_finalized_windows(self):
        events = ((i, "a", "FAIL") for i in range(100000))
        self.assertEqual(aggregate_event_time(events, 1, 0), ([(i, "a", 1, 1) for i in range(100000)], []))

    def test_maximum_open_windows_out_of_order(self):
        events = ((i, "a", "PASS") for i in range(99999, -1, -1))
        self.assertEqual(aggregate_event_time(events, 1, 100000), ([(i, "a", 1, 0) for i in range(100000)], []))

    def test_randomized_accepted_event_grouping_oracle(self):
        import random
        rng = random.Random(15)
        for _ in range(150):
            events = [(rng.randrange(40), rng.choice("ABC"), rng.choice(["PASS", "FAIL"])) for _ in range(rng.randrange(25))]
            window_size = rng.randrange(1, 10)
            lateness = rng.randrange(15)
            accepted = []
            rejected = []
            maximum = 0
            watermark = float("-inf")
            for index, (timestamp, device, status) in enumerate(events):
                if timestamp < watermark:
                    rejected.append(index)
                else:
                    accepted.append((timestamp, device, status))
                    maximum = max(maximum, timestamp)
                    watermark = maximum - lateness
            keys = {(timestamp // window_size * window_size, device) for timestamp, device, _ in accepted}
            expected = []
            for start, device in sorted(keys):
                statuses = [status for timestamp, event_device, status in accepted if event_device == device and start <= timestamp < start + window_size]
                expected.append((start, device, len(statuses), statuses.count("FAIL")))
            with self.subTest(events=events, window_size=window_size, lateness=lateness):
                self.assertEqual(aggregate_event_time(events, window_size, lateness), (expected, rejected))


if __name__ == "__main__":
    unittest.main()
