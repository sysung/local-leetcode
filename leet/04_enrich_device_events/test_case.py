"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import enrich_events


class TestCases(unittest.TestCase):
    def test_matched_and_unknown(self):
        args = ([{'device_id': 'a', 'value': 7}, {'device_id': 'x', 'value': 8}],
         [{'device_id': 'a', 'model': 'GPU', 'site': 'lab'}])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': 'GPU', 'site': 'lab', 'value': 7},
         {'device_id': 'x', 'model': None, 'site': None, 'value': 8}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_duplicate_metadata(self):
        args = ([{'device_id': 'a'}],
         [{'device_id': 'a', 'model': 'old', 'site': 'one'},
          {'device_id': 'a', 'model': 'new', 'site': 'two'}])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': 'new', 'site': 'two'}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_empty_events(self):
        args = ([], [{'device_id': 'a', 'model': 'x', 'site': 'y'}])
        before = deepcopy(args)
        expected = []
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_empty_metadata(self):
        args = ([{'device_id': 'a'}], [])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': None, 'site': None}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_existing_fields(self):
        args = ([{'device_id': 'a', 'model': 'stale', 'site': 'old'}],
         [{'device_id': 'a', 'model': 'new', 'site': 'lab'}])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': 'new', 'site': 'lab'}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_preserve_order(self):
        args = ([{'device_id': 'b'}, {'device_id': 'a'}, {'device_id': 'b'}], [])
        before = deepcopy(args)
        expected = [{'device_id': 'b', 'model': None, 'site': None},
         {'device_id': 'a', 'model': None, 'site': None},
         {'device_id': 'b', 'model': None, 'site': None}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
