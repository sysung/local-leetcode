"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import deduplicate_events


class TestCases(unittest.TestCase):
    def test_newest(self):
        args = ([{'event_id': 'b', 'payload': 'old', 'timestamp': 1},
          {'event_id': 'a', 'payload': 'a', 'timestamp': 3},
          {'event_id': 'b', 'payload': 'new', 'timestamp': 2}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': 'a', 'timestamp': 3},
         {'event_id': 'b', 'payload': 'new', 'timestamp': 2}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_ties(self):
        args = ([{'event_id': 'a', 'payload': 'first', 'timestamp': 4},
          {'event_id': 'a', 'payload': 'last', 'timestamp': 4}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': 'last', 'timestamp': 4}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_older_arrives_last(self):
        args = ([{'event_id': 'a', 'payload': None, 'timestamp': 8},
          {'event_id': 'a', 'payload': 0, 'timestamp': 1}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': None, 'timestamp': 8}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_single(self):
        args = ([{'event_id': 'x', 'payload': {'value': 3}, 'source': 'station', 'timestamp': 0}],)
        before = deepcopy(args)
        expected = [{'event_id': 'x', 'payload': {'value': 3}, 'source': 'station', 'timestamp': 0}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_distinct(self):
        args = ([{'event_id': 'z', 'payload': 0, 'timestamp': 0},
          {'event_id': 'b', 'payload': 1, 'timestamp': 0}],)
        before = deepcopy(args)
        expected = [{'event_id': 'b', 'payload': 1, 'timestamp': 0},
         {'event_id': 'z', 'payload': 0, 'timestamp': 0}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
