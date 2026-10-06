"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import normalize_records


class TestCases(unittest.TestCase):

    def test_empty(self):
        args = ([],)
        before = deepcopy(args)
        self.assertEqual(normalize_records(*args), [])
        self.assertEqual(args, before)

    def test_missing(self):
        args = ([{}],)
        before = deepcopy(args)
        self.assertEqual(normalize_records(*args), [{'item_id': None, 'timestamp': None, 'status': None}])
        self.assertEqual(args, before)

    def test_legacy(self):
        args = ([{'id': 'a', 'time': 0, 'result': 'PASS', 'extra': 9}],)
        before = deepcopy(args)
        self.assertEqual(normalize_records(*args), [{'item_id': 'a', 'timestamp': 0, 'status': 'PASS'}])
        self.assertEqual(args, before)

    def test_canonical_priority(self):
        args = ([{'item_id': 'new', 'id': 'old', 'timestamp': 1, 'time': 2, 'status': 'FAIL', 'result': 'PASS'}],)
        before = deepcopy(args)
        self.assertEqual(normalize_records(*args), [{'item_id': 'new', 'timestamp': 1, 'status': 'FAIL'}])
        self.assertEqual(args, before)

    def test_falsey(self):
        args = ([{'item_id': None, 'id': 'old', 'timestamp': 0, 'time': 9, 'status': False, 'result': 'PASS'}],)
        before = deepcopy(args)
        self.assertEqual(normalize_records(*args), [{'item_id': None, 'timestamp': 0, 'status': False}])
        self.assertEqual(args, before)

    def test_order(self):
        args = ([{'id': 'b'}, {'id': 'a'}, {'id': 'b'}],)
        before = deepcopy(args)
        self.assertEqual(normalize_records(*args), [{'item_id': 'b', 'timestamp': None, 'status': None}, {'item_id': 'a', 'timestamp': None, 'status': None}, {'item_id': 'b', 'timestamp': None, 'status': None}])
        self.assertEqual(args, before)

    def test_no_coercion(self):
        args = ([{'id': '', 'time': '012', 'result': 0}],)
        before = deepcopy(args)
        self.assertEqual(normalize_records(*args), [{'item_id': '', 'timestamp': '012', 'status': 0}])
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
